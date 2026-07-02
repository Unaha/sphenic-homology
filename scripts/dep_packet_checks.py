#!/usr/bin/env python3
# EXPLICIT DEPENDENCY CHECKS for the BANKING_GRADE packet (Addy Tier-2 ruling requirements):
#  (a) VERTEX SET: actual vertex count of the sphenic window complex vs pi(N/6), exactly.
#  (b) CONNECTIVITY: number of connected components c of the edge graph (need c=1).
#  (c) FITTING = elem: the slab fitting condition (next-prime shift stays in window) counted
#      two independent ways (position-coordinates vs value test).
#  (d) RANK: signed rank of d2 = F - elem re-confirmed by ordered elimination, and per-cell
#      free <=> fitting (the C-0744 mechanism), hence b2 = elem and b1 = h1 = (E-F)-V+1+elem.
# Run at several N, print a table. All exact integer arithmetic.
import numpy as np, time, importlib.util
from sympy import nextprime
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
P=2147483647

def check(N):
    spf=eh.sieve_spf(N); idx=np.arange(N+1)
    PR=idx[(spf==idx)&(idx>=2)].astype(np.int64)
    A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]  # window (N/2,N]
    F=len(A)
    # (a) vertex set
    verts=np.unique(np.concatenate([A,B,C]))
    V_actual=len(verts)
    piN6=int(np.searchsorted(PR,N//6,side='right'))
    all_le_N6=bool((verts<=N//6).all())
    every_prime_le_N6=bool(V_actual==piN6 and all_le_N6)
    # (b) connectivity via union-find on edges
    M=np.int64(N+10)
    co=np.unique(np.concatenate([A*M+B,A*M+C,B*M+C]))
    E=len(co)
    par={}
    def find(x):
        while par.get(x,x)!=x: par[x]=par.get(par[x],par[x]); x=par[x]
        return x
    for e in co:
        u,v=int(e//M),int(e%M)
        ru,rv=find(u),find(v)
        if ru!=rv: par[ru]=rv
    comps=len({find(int(v)) for v in verts})
    # (c) fitting = elem two ways
    j=np.searchsorted(PR,A); jb=np.searchsorted(PR,B); jc=np.searchsorted(PR,C)
    assert (PR[j]==A).all() and (PR[jb]==B).all() and (PR[jc]==C).all()
    nA=np.where(j+1<len(PR),PR[np.minimum(j+1,len(PR)-1)],np.int64(nextprime(int(PR[-1]))))
    nB=np.where(jb+1<len(PR),PR[np.minimum(jb+1,len(PR)-1)],np.int64(nextprime(int(PR[-1]))))
    nC=np.where(jc+1<len(PR),PR[np.minimum(jc+1,len(PR)-1)],np.int64(nextprime(int(PR[-1]))))
    fit_mask=(nA*nB*nC<=N)
    elem_pos=int(fit_mask.sum())
    # independent value test with sympy nextprime on a sample + full via dict
    nxt={int(p):int(nextprime(int(p))) for p in np.unique(np.concatenate([A,B,C]))}
    elem_val=int(sum(1 for a,b,c in zip(A,B,C) if nxt[int(a)]*nxt[int(b)]*nxt[int(c)]<=N))
    # (d) ordered elimination: signed rank + per-cell free<=>fit
    prod=A*B*C
    order=np.argsort(-prod)
    eidx={int(e):k for k,e in enumerate(co)}
    piv={}; free=np.zeros(F,bool)
    for jj in order:
        a,b,c=int(A[jj]),int(B[jj]),int(C[jj])
        r={eidx[b*M+c]:1, eidx[a*M+c]:P-1, eidx[a*M+b]:1}
        placed=False
        while r:
            e=min(r)
            if e in piv:
                fct=r[e]; pr=piv[e]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%P
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[e],P-2,P)
                piv[e]={cc:(vv*inv)%P for cc,vv in r.items()}; placed=True; break
        if not placed: free[jj]=True
    rank=F-int(free.sum())
    mech=bool((free==fit_mask).all())
    b2=F-rank; b1=E-V_actual+comps-rank
    h1=(E-F)-V_actual+1+elem_pos
    log(f"N={N}: V_actual={V_actual} pi(N/6)={piN6} equal={every_prime_le_N6} | comps={comps} | "
        f"elem(pos)={elem_pos} elem(val)={elem_val} equal={elem_pos==elem_val} | rank={rank} F-elem={F-elem_pos} "
        f"rank==F-elem={rank==F-elem_pos} | free<=>fit per-cell={mech} | b2={b2} elem={elem_pos} b2==elem={b2==elem_pos} | "
        f"b1={b1} h1={h1} b1==h1={b1==h1}")
    return every_prime_le_N6 and comps==1 and elem_pos==elem_val and rank==F-elem_pos and mech and b2==elem_pos and b1==h1

ok=True
for N in (200000, 500000, 1050000, 2000000):
    ok &= check(N)
log("PACKET CHECKS:", "ALL PASS" if ok else "FAILURE PRESENT")
log("DONE")
