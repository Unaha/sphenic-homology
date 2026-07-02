#!/usr/bin/env python3
# INTEGER-SANDWICH FEASIBILITY PROBE (the explosion-free all-characteristic route).
# For a sample of replay pairs: run EXACT INTEGER sparse elimination on the (LG) matrices,
# choosing pivots ONLY at entries +-1 (unit pivots => the elimination step is integer and the
# rank contribution is FIELD-INDEPENDENT). Columns that never find a unit pivot are deferred
# to a residual block. Measure per pair:
#   - #columns eliminated with unit pivots vs total,
#   - residual block size (columns + surviving coordinate support),
#   - MAX |entry| encountered (growth must stay bounded for the route to be practical).
# If residuals are ~zero and growth mild: all-char certificates are cheap. Memory-capped by caller.
import json, gzip, time, sys
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)

def tree_balance_basis_int(edges):
    # integer balance basis via the checker's spanning-tree method (self-verifying)
    import types
    src=open('scripts/lg_replay_check.py').read()
    srcf=src[:src.index("import sys\nbase=")]
    mod=types.ModuleType("chk"); exec(srcf,mod.__dict__)
    return mod.tree_balance_basis(edges)[0]

def probe_pair(b):
    v,a=b["v"],b["a"]; cells=[tuple(c) for c in b["cells"]]; Lv=set(tuple(e) for e in b["Lv"])
    S={}
    for (x,y,z) in cells:
        S.setdefault((y,z),[]).append(x); S.setdefault((x,z),[]).append(y); S.setdefault((x,y),[]).append(z)
    La=[(q,r) for (x,q,r) in cells if x==a]
    # build integer G,H
    GH=[]
    fibA={}
    for (x,y) in La:
        for c in S.get((x,y),[]):
            if c>a: fibA.setdefault(c,[]).append((x,y))
    for c,edges in fibA.items():
        if len(edges)<3: continue
        for kv in tree_balance_basis_int(edges):
            GH.append({('E',)+edges[ei]:cf for ei,cf in kv.items()})
    Lva=[e for e in Lv if a in S.get(e,[]) and e[0]>a]
    if len(Lva)>=3:
        for kv in tree_balance_basis_int(Lva):
            GH.append({('E',)+Lva[ei]:-cf for ei,cf in kv.items()})
    fibB=set()
    for e in Lv:
        if a in e:
            for bb in S.get(e,[]):
                if bb!=v and bb>a: fibB.add(bb)
    for bb in sorted(fibB):
        full=[e for e in Lv if bb in S.get(e,[]) and e[0]>=a and bb not in e]
        if len(full)<3: continue
        for kv in tree_balance_basis_int(full):
            vec={}
            for ei,cf in kv.items():
                s,t=full[ei]
                if s==a: key=('E',)+tuple(sorted((bb,t)))
                elif t==a: key=('E',)+tuple(sorted((bb,s)))
                else: continue
                vec[key]=vec.get(key,0)-cf
            vec={k:val for k,val in vec.items() if val}
            if vec: GH.append(vec)
    # integer columns for the AUGMENTED system: cells (with raw tail coords) + GH columns
    cols=[]
    for (x,q,r) in cells:
        col={}
        for ed in ((q,r),(x,r),(x,q)):
            if ed in Lv:
                col[('B',ed[0])]=col.get(('B',ed[0]),0)+1
                col[('B',ed[1])]=col.get(('B',ed[1]),0)+1
            else:
                col[('F',)+ed]=col.get(('F',)+ed,0)+1
        if x==a: col[('E',q,r)]=col.get(('E',q,r),0)+1
        cols.append(col)
    cols+= [dict(g) for g in GH]
    # exact integer elimination, UNIT PIVOTS ONLY
    piv={}; unit=0; deferred=[]; maxent=1
    for col in cols:
        r={k:v for k,v in col.items() if v}
        progressed=True
        while r and progressed:
            progressed=False
            # reduce against existing pivots
            changed=True
            while changed:
                changed=False
                for k in list(r.keys()):
                    if k in piv:
                        pr=piv[k]
                        f=r[k]  # pivot entry is +-1 in pr => subtract f*pr
                        s=pr[k]  # +-1
                        mult=f*s
                        for cc,vv in pr.items():
                            nv=r.get(cc,0)-mult*vv
                            if nv: r[cc]=nv
                            elif cc in r: del r[cc]
                            if abs(nv)>maxent: maxent=abs(nv)
                        changed=True
                        break
            if not r: break
            # find a unit entry to pivot on
            uk=None
            for k,vv in r.items():
                if abs(vv)==1: uk=k; break
            if uk is not None:
                piv[uk]=dict(r); unit+=1; r={}
            else:
                deferred.append(dict(r)); r={}
    return len(cols),unit,len(deferred),maxent,sum(len(d) for d in deferred)

import glob
sample=[]
for base in ("/lab/replay_c0746/N100000","/lab/replay_c0746/N200000"):
    fns=sorted(glob.glob(f"{base}/pair_*.json.gz"))
    sample+=fns[::6]   # every 6th pair = ~33 pairs across sizes
log(f"probing {len(sample)} pairs")
worst_res=0; worst_ent=1
for fn in sample:
    b=json.loads(gzip.open(fn,'rb').read())
    ncols,unit,ndef,maxent,ressz=probe_pair(b)
    worst_res=max(worst_res,ndef); worst_ent=max(worst_ent,maxent)
    log(f"  v={b['v']} a={b['a']} cells={b['ncells']}: cols={ncols} unit-pivots={unit} residual-cols={ndef} (support {ressz}) max|entry|={maxent}")
log(f"PROBE SUMMARY: worst residual block = {worst_res} columns; worst entry growth = {worst_ent}")
log("VERDICT: "+("UNIMODULAR ROUTE VIABLE" if worst_res<=8 and worst_ent<=64 else "NEEDS THOUGHT"))
log("DONE")
