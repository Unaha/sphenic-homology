#!/usr/bin/env python3
# TWO-STAGE ALL-CHARACTERISTIC CERTIFIER for C-0746 (the explosion-free route, probe-validated).
# Per pair, for each of the three matrices (M = witness system; AUG = cells-with-tails + G/H; GH):
#   Stage 1: exact integer elimination with UNIT (+-1) pivots only — unimodular ops, so the
#            invariant-factor content of the whole matrix equals that of the residual block.
#            (Probe: growth <= 64, residuals <= ~310 cols.)
#   Stage 2: exact flint SNF of the SMALL residual block; collect primes dividing any invariant factor.
# CERTIFICATE: for every pair and matrix, the bad-prime set is a subset of {2,3}.
# Also re-verify the integer (LG) identity rank(AUG) == rank(M) + rank(GH) from the exact ranks.
import json, gzip, time, glob, types
from flint import fmpz_mat
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)

_src=open('scripts/lg_replay_check.py').read()
_mod=types.ModuleType("chk"); exec(_src[:_src.index("import sys\nbase=")],_mod.__dict__)
tree_balance_basis=lambda e: _mod.tree_balance_basis(e)[0]

def factor_small(n):
    n=abs(int(n)); fs=set()
    d=2
    while d*d<=n:
        while n%d==0: fs.add(d); n//=d
        d+=1 if d==2 else 2
    if n>1: fs.add(n)
    return fs

def unit_stage(cols):
    piv={}; unit=0; deferred=[]; maxent=1
    for col in cols:
        r={k:v for k,v in col.items() if v}
        while True:
            hit=False
            for k in list(r.keys()):
                if k in piv:
                    pr=piv[k]; mult=r[k]*pr[k]
                    for cc,vv in pr.items():
                        nv=r.get(cc,0)-mult*vv
                        if nv:
                            r[cc]=nv
                            if abs(nv)>maxent: maxent=abs(nv)
                        elif cc in r: del r[cc]
                    hit=True; break
            if not hit: break
        if not r: continue
        uk=None
        for k,vv in r.items():
            if abs(vv)==1: uk=k; break
        if uk is not None:
            # normalize pivot to store with its sign for mult calc
            piv[uk]=r; unit+=1
        else:
            deferred.append(r)
    # SECOND PASS: re-reduce deferred columns against the FINAL pivot set (pivots created after
    # a column's deferral were never applied to it); loop to fixpoint, drop emptied columns.
    final=[]
    for r in deferred:
        while True:
            hit=False
            for k in list(r.keys()):
                if k in piv:
                    pr=piv[k]; mult=r[k]*pr[k]
                    for cc,vv in pr.items():
                        nv=r.get(cc,0)-mult*vv
                        if nv:
                            r[cc]=nv
                            if abs(nv)>maxent: maxent=abs(nv)
                        elif cc in r: del r[cc]
                    hit=True; break
            if not hit: break
        # a re-reduced column may NOW have a unit entry: promote it to a pivot
        uk=None
        for k,vv in r.items():
            if abs(vv)==1: uk=k; break
        if uk is not None and r:
            piv[uk]=r; unit+=1
        elif r:
            final.append(r)
    # one more fixpoint round in case promotions enable further reductions/promotions
    changed=True
    while changed:
        changed=False
        nxt=[]
        for r in final:
            while True:
                hit=False
                for k in list(r.keys()):
                    if k in piv:
                        pr=piv[k]; mult=r[k]*pr[k]
                        for cc,vv in pr.items():
                            nv=r.get(cc,0)-mult*vv
                            if nv:
                                r[cc]=nv
                                if abs(nv)>maxent: maxent=abs(nv)
                            elif cc in r: del r[cc]
                        hit=True; break
                if not hit: break
            uk=None
            for k,vv in r.items():
                if abs(vv)==1: uk=k; break
            if uk is not None and r:
                piv[uk]=r; unit+=1; changed=True
            elif r:
                nxt.append(r)
        final=nxt
    return unit,final,maxent

def residual_snf(deferred):
    if not deferred: return 0,set()
    coords={}
    for d in deferred:
        for k in d:
            if k not in coords: coords[k]=len(coords)
    m=len(coords); n=len(deferred)
    M=[[0]*n for _ in range(m)]
    for j,d in enumerate(deferred):
        for k,v in d.items(): M[coords[k]][j]=int(v)
    S=fmpz_mat(M).snf()
    rank=0; primes=set()
    for i in range(min(m,n)):
        dd=int(S[i,i])
        if dd==0: break
        rank+=1
        if abs(dd)>1: primes|=factor_small(dd)
    return rank,primes

def build(b):
    v,a=b["v"],b["a"]; cells=[tuple(c) for c in b["cells"]]; Lv=set(tuple(e) for e in b["Lv"])
    S={}
    for (x,y,z) in cells:
        S.setdefault((y,z),[]).append(x); S.setdefault((x,z),[]).append(y); S.setdefault((x,y),[]).append(z)
    La=[(q,r) for (x,q,r) in cells if x==a]
    GH=[]
    fibA={}
    for (x,y) in La:
        for c in S.get((x,y),[]):
            if c>a: fibA.setdefault(c,[]).append((x,y))
    for c,edges in fibA.items():
        if len(edges)<3: continue
        for kv in tree_balance_basis(edges):
            GH.append({('E',)+edges[ei]:cf for ei,cf in kv.items()})
    Lva=[e for e in Lv if a in S.get(e,[]) and e[0]>a]
    if len(Lva)>=3:
        for kv in tree_balance_basis(Lva):
            GH.append({('E',)+Lva[ei]:-cf for ei,cf in kv.items()})
    fibB=set()
    for e in Lv:
        if a in e:
            for bb in S.get(e,[]):
                if bb!=v and bb>a: fibB.add(bb)
    for bb in sorted(fibB):
        full=[e for e in Lv if bb in S.get(e,[]) and e[0]>=a and bb not in e]
        if len(full)<3: continue
        for kv in tree_balance_basis(full):
            vec={}
            for ei,cf in kv.items():
                s,t=full[ei]
                if s==a: key=('E',)+tuple(sorted((bb,t)))
                elif t==a: key=('E',)+tuple(sorted((bb,s)))
                else: continue
                vec[key]=vec.get(key,0)-cf
            vec={k:val for k,val in vec.items() if val}
            if vec: GH.append(vec)
    Mcols=[]; AUGcols=[]
    for (x,q,r) in cells:
        col={}
        for ed in ((q,r),(x,r),(x,q)):
            if ed in Lv:
                col[('B',ed[0])]=col.get(('B',ed[0]),0)+1
                col[('B',ed[1])]=col.get(('B',ed[1]),0)+1
            else:
                col[('F',)+ed]=col.get(('F',)+ed,0)+1
        Mcols.append(dict(col))
        if x==a:
            col=dict(col); col[('E',q,r)]=col.get(('E',q,r),0)+1
        AUGcols.append(col)
    AUGcols=AUGcols+[dict(g) for g in GH]
    return Mcols,AUGcols,[dict(g) for g in GH]

issues=[]; done=0
import glob as _g
for base in sorted(_g.glob("certificates/N*")):
    for fn in sorted(glob.glob(f"{base}/pair_*.json.gz")):
        b=json.loads(gzip.open(fn,'rb').read())
        Mc,Ac,Gc=build(b)
        ranks={}; badp=set()
        for name,cols in (("M",Mc),("AUG",Ac),("GH",Gc)):
            u,defr,ment=unit_stage(cols)
            rres,pr=residual_snf(defr)
            ranks[name]=u+rres; badp|=pr
        lg_int=(ranks["AUG"]==ranks["M"]+ranks["GH"])
        bad=sorted(badp-{2,3})
        done+=1
        if bad or not lg_int:
            issues.append((base.split('/')[-1],b["v"],b["a"],bad,lg_int,ranks))
            log(f"  ISSUE {base.split('/')[-1]} v={b['v']} a={b['a']}: badprimes>{{2,3}}={bad} lg_int={lg_int} ranks={ranks}")
        if done%25==0: log(f"progress: {done} pairs two-stage certified, issues={len(issues)}")
log(f"TWO-STAGE CERTIFICATION: {done} pairs, issues={len(issues)}")
log("VERDICT: "+("ALL-CHARACTERISTIC CLEAN (no bad primes outside {2,3} anywhere; integer LG holds)" if not issues else f"{len(issues)} ISSUES"))
log("DONE")
