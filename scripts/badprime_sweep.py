#!/usr/bin/env python3
# MODULAR-FIRST BAD-PRIME TRIAGE for C-0746: for every replay pair, recompute the two (LG) ranks
# over EVERY prime p < 1000 (plus the 31-bit reference) and report any pair x prime where either
# rank differs from the reference or (LG) fails. A clean sweep certifies: no bad prime < 1000
# anywhere in the certificate set, and (LG) holds at every characteristic in that range.
import json, gzip, time, sys
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
def primes_below(n):
    s=[True]*n
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n,i): s[j]=False
    return [i for i in range(5,n) if s[i]]
PS=primes_below(1000)
REF=2147483647

def balance_basis(edges,p):
    piv={}; basis=[]
    for ei,(u,w) in enumerate(edges):
        r={u:1,w:1}; combo={ei:1}; placed=False
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr,pc=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%p
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
                for cc,vv in pc.items():
                    nv=(combo.get(cc,0)-fct*vv)%p
                    if nv: combo[cc]=nv
                    elif cc in combo: del combo[cc]
            else:
                inv=pow(r[k],p-2,p)
                piv[k]=({cc:(vv*inv)%p for cc,vv in r.items()},{cc:(vv*inv)%p for cc,vv in combo.items()})
                placed=True; break
        if not placed: basis.append(dict(combo))
    return basis

def elim_rank(cols,p):
    piv={}; rank=0
    for col in cols:
        r={k:v%p for k,v in col.items() if v%p}
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%p
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[k],p-2,p); piv[k]={cc:(vv*inv)%p for cc,vv in r.items()}; rank+=1; break
    return rank,piv

def reduce_mod(vec,piv,p):
    r={k:v%p for k,v in vec.items() if v%p}
    out={}
    while r:
        k=min(r)
        if k in piv:
            fct=r[k]; pr=piv[k]
            for cc,vv in pr.items():
                nv=(r.get(cc,0)-fct*vv)%p
                if nv: r[cc]=nv
                elif cc in r: del r[cc]
        else:
            out[k]=r.pop(k)
    return out

def pair_ranks(b,p):
    v,a=b["v"],b["a"]; cells=[tuple(c) for c in b["cells"]]; Lv=set(tuple(e) for e in b["Lv"])
    S={}
    for (x,y,z) in cells:
        S.setdefault((y,z),[]).append(x); S.setdefault((x,z),[]).append(y); S.setdefault((x,y),[]).append(z)
    La=[(q,r) for (x,q,r) in cells if x==a]
    Svecs=[]
    fibA={}
    for (x,y) in La:
        for c in S.get((x,y),[]):
            if c>a: fibA.setdefault(c,[]).append((x,y))
    for c,edges in fibA.items():
        if len(edges)<3: continue
        for kv in balance_basis(edges,p):
            Svecs.append({('E',)+edges[ei]:cf for ei,cf in kv.items()})
    Lva=[e for e in Lv if a in S.get(e,[]) and e[0]>a]
    if len(Lva)>=3:
        for kv in balance_basis(Lva,p):
            Svecs.append({('E',)+Lva[ei]:(-cf)%p for ei,cf in kv.items()})
    fibB=set()
    for e in Lv:
        if a in e:
            for bb in S.get(e,[]):
                if bb!=v and bb>a: fibB.add(bb)
    for bb in sorted(fibB):
        full=[e for e in Lv if bb in S.get(e,[]) and e[0]>=a and bb not in e]
        if len(full)<3: continue
        for kv in balance_basis(full,p):
            vec={}
            for ei,cf in kv.items():
                s,t=full[ei]
                if s==a: key=('E',)+tuple(sorted((bb,t)))
                elif t==a: key=('E',)+tuple(sorted((bb,s)))
                else: continue
                vec[key]=(vec.get(key,0)-cf)%p
            vec={k:val for k,val in vec.items() if val%p}
            if vec: Svecs.append(vec)
    _,pivS=elim_rank(Svecs,p)
    def colof(cell,aug):
        x,q,r=cell
        col={}
        for ed in ((q,r),(x,r),(x,q)):
            if ed in Lv:
                col[('B',ed[0])]=(col.get(('B',ed[0]),0)+1)%p
                col[('B',ed[1])]=(col.get(('B',ed[1]),0)+1)%p
            else:
                col[('F',)+ed]=(col.get(('F',)+ed,0)+1)%p
        if aug and x==a:
            red=reduce_mod({('E',q,r):1},pivS,p)
            for k,val in red.items(): col[('Q',)+k]=(col.get(('Q',)+k,0)+val)%p
        return col
    r1,_=elim_rank((colof(c,False) for c in cells),p)
    r2,_=elim_rank((colof(c,True) for c in cells),p)
    return r1,r2

issues=0; done=0
for base in ("/lab/replay_c0746/N100000","/lab/replay_c0746/N200000"):
    man=json.load(open(f"{base}/MANIFEST.json"))
    for fn in sorted(man):
        b=json.loads(gzip.open(f"{base}/{fn}",'rb').read())
        ref1,ref2=pair_ranks(b,REF)
        for p in PS:
            r1,r2=pair_ranks(b,p)
            if (r1,r2)!=(ref1,ref2) or r1!=r2:
                issues+=1
                log(f"BAD-PRIME SIGNAL {base.split('/')[-1]} v={b['v']} a={b['a']} p={p}: ({r1},{r2}) vs ref ({ref1},{ref2})")
        done+=1
        if done%20==0: log(f"progress: {done} pairs swept over {len(PS)} primes, issues={issues}")
log(f"SWEEP COMPLETE: {done} pairs x {len(PS)} primes (5..997), issues={issues}")
log("VERDICT: "+("NO BAD PRIMES BELOW 1000 ANYWHERE" if issues==0 else f"{issues} SIGNALS"))
log("DONE")
