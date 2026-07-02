#!/usr/bin/env python3
# COMPLETENESS PROOF, THE CORRECT CRUX: graded test along the least-vertex filtration.
# C_{>=v} = cells with least prime >= v (only ~pi(N^{1/3}) levels!). Check for EVERY level:
#     e_v := dim ker d2^u restricted to C_{>=v}   ==   rank{ modes m_{a,b,z} with a >= v }  =: m_v
# where modes at level a use pair-links WITHIN C_{>=v}... note: a mode with a>=v automatically has all
# its cells' least vertices >= min(a, edge primes) — the cells (a,u,w),(b,u,w) have least prime
# min(a,u) etc. — CAREFUL: for the mode to live in C_{>=v} we need ALL its cells in C_{>=v}, i.e.
# every prime appearing >= v. We therefore build, per level v, the mode family of the SUBCOMPLEX
# C_{>=v} itself (pairs {a,b} with a,b >= v, links within the subcomplex; edges (u,w) have u,w > least
# automatically >= v). Equality at every level ==> the induction closes with graded surjectivity as
# the only remaining lemma, restated on the REALIZABLE quotient.
import numpy as np, time, importlib.util
from itertools import combinations
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
P=2147483647

def kernel_dim(cells):
    piv={}; rank=0
    for (a,b,c) in cells:
        r={(b,c):1,(a,c):1,(a,b):1}
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%P
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[k],P-2,P); piv[k]={cc:(vv*inv)%P for cc,vv in r.items()}; rank+=1; break
    return len(cells)-rank

def balance_basis(edges):
    piv={}; basis=[]
    for ei,(u,v) in enumerate(edges):
        r={u:1,v:1}; combo={ei:1}; placed=False
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr,pc=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%P
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
                for cc,vv in pc.items():
                    nv=(combo.get(cc,0)-fct*vv)%P
                    if nv: combo[cc]=nv
                    elif cc in combo: del combo[cc]
            else:
                inv=pow(r[k],P-2,P)
                piv[k]=({cc:(vv*inv)%P for cc,vv in r.items()},{cc:(vv*inv)%P for cc,vv in combo.items()})
                placed=True; break
        if not placed: basis.append(dict(combo))
    return basis

def mode_rank(cells):
    cellset=set(cells)
    S={}
    for (a,b,c) in cells:
        S.setdefault((b,c),[]).append(a); S.setdefault((a,c),[]).append(b); S.setdefault((a,b),[]).append(c)
    Lp={}
    for (u,v),ws in S.items():
        if len(ws)<2: continue
        for a,b in combinations(sorted(ws),2): Lp.setdefault((a,b),[]).append((u,v))
    piv={}; rank=0
    for (a,b),edges in Lp.items():
        if len(edges)<3: continue
        for kv in balance_basis(edges):
            col={}
            ok=True
            for ei,cf in kv.items():
                u,v=edges[ei]
                ta=tuple(sorted((a,u,v))); tb=tuple(sorted((b,u,v)))
                if ta not in cellset or tb not in cellset: ok=False; break
                col[ta]=(col.get(ta,0)+cf)%P; col[tb]=(col.get(tb,0)-cf)%P
            if not ok: continue
            r={k:v for k,v in col.items() if v%P}
            while r:
                k=min(r)
                if k in piv:
                    fct=r[k]; pr=piv[k]
                    for cc,vv in pr.items():
                        nv=(r.get(cc,0)-fct*vv)%P
                        if nv: r[cc]=nv
                        elif cc in r: del r[cc]
                else:
                    inv=pow(r[k],P-2,P); piv[k]={cc:(vv*inv)%P for cc,vv in r.items()}; rank+=1; break
    return rank

def run(N):
    spf=eh.sieve_spf(N); idx=np.arange(N+1)
    A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]
    cells=[(int(a),int(b),int(c)) for a,b,c in zip(A,B,C)]
    levels=sorted(set(a for a,_,_ in cells))
    log(f"N={N}: F={len(cells)} least-vertex levels: {levels}")
    ok=True
    for v in levels:
        sub=[c for c in cells if c[0]>=v]
        ev=kernel_dim(sub); mv=mode_rank(sub)
        stat="PASS" if ev==mv else f"FAIL (deficit {ev-mv})"
        ok &= (ev==mv)
        log(f"  v>={v:3}: cells={len(sub):6} e={ev:5} modes={mv:5}  {stat}")
    log(f"GRADED VERDICT N={N}: "+("ALL LEVELS PASS" if ok else "FAILURE PRESENT"))
    return ok
for N in (100000, 200000):
    run(N)
log("DONE")
