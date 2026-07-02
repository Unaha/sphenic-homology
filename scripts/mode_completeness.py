#!/usr/bin/env python3
# ru ATTACK, THE DECIDER: completeness of the difference-wedge modes.
# Mode family: for every prime pair {a,b}, common-link graph L_{a,b} = {(u,v): auv AND buv window sphenics}.
# A vector c on L's edges with ZERO UNSIGNED VERTEX SUMS (kernel of the all-ones incidence; even cycles
# + odd-cycle barbells, signed-graph balance) lifts to a full unsigned-kernel mode:
#   sum_e c_e [ (a,u,v) ] - c_e [ (b,u,v) ]
# (facet (u,v): a/b cancel; facets (a,u),(b,u): vertex sums vanish; facet (a,b): never present.)
# TEST: rank( all lifted modes over all pairs ) ?= e = F - ru.  Sanity: verify sample modes are null.
import numpy as np, time, importlib.util
from sympy import nextprime
from itertools import combinations
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
P=2147483647

def sparse_rank_cols(cols_iter):
    piv={}; rank=0
    for r in cols_iter:
        r={k:v%P for k,v in r.items() if v%P}
        while r:
            e=min(r)
            if e in piv:
                fct=r[e]; pr=piv[e]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%P
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[e],P-2,P); piv[e]={cc:(vv*inv)%P for cc,vv in r.items()}; rank+=1; break
    return rank

def incidence_kernel_basis(edges):
    # edges: list of (u,v). kernel of UNSIGNED vertex-edge incidence over GF(P), with combo tracking.
    piv={}; basis=[]
    for ei,(u,v) in enumerate(edges):
        r={u:1,v:1}; combo={ei:1}
        placed=False
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

def run(N):
    spf=eh.sieve_spf(N); idx=np.arange(N+1)
    PR=idx[(spf==idx)&(idx>=2)].astype(np.int64)
    A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]
    F=len(A)
    cellid={}
    for i in range(F): cellid[(int(A[i]),int(B[i]),int(C[i]))]=i
    # e via standard elimination
    M=np.int64(N+10); prod=A*B*C
    order=np.argsort(-prod); piv={}; freecnt=0
    for jj in order:
        a,b,c=int(A[jj]),int(B[jj]),int(C[jj])
        r={b*M+c:1,a*M+c:1,a*M+b:1}; placed=False
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%P
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[k],P-2,P); piv[k]={cc:(vv*inv)%P for cc,vv in r.items()}; placed=True; break
        if not placed: freecnt+=1
    e=freecnt
    log(f"N={N}: F={F} e={e}")
    # third-prime sets per edge
    S={}
    for i in range(F):
        a,b,c=int(A[i]),int(B[i]),int(C[i])
        S.setdefault((b,c),[]).append(a); S.setdefault((a,c),[]).append(b); S.setdefault((a,b),[]).append(c)
    # link edge lists per pair {a,b} (a<b): edges (u,v) with both auv,buv present
    Lpairs={}
    npairs_edges=0
    for (u,v),ws in S.items():
        if len(ws)<2: continue
        ws=sorted(ws)
        for a,b in combinations(ws,2):
            Lpairs.setdefault((a,b),[]).append((u,v))
            npairs_edges+=1
    log(f"  edges={len(S)}; candidate pairs={len(Lpairs)}; total link-edge incidences={npairs_edges}")
    # per-pair kernels -> lifted modes -> global rank
    def modes():
        nmodes=0
        for (a,b),edges in Lpairs.items():
            if len(edges)<3: continue
            basis=incidence_kernel_basis(edges)
            for kv in basis:
                col={}
                ok=True
                for ei,cf in kv.items():
                    u,v=edges[ei]
                    ta=tuple(sorted((a,u,v))); tb=tuple(sorted((b,u,v)))
                    if ta not in cellid or tb not in cellid: ok=False; break
                    col[cellid[ta]]=(col.get(cellid[ta],0)+cf)%P
                    col[cellid[tb]]=(col.get(cellid[tb],0)-cf)%P
                if ok:
                    nmodes+=1
                    yield col
        log(f"  lifted modes: {nmodes}")
    R=sparse_rank_cols(modes())
    log(f"  RANK(mode family) = {R}  vs  e = {e}   ->  {'COMPLETE' if R==e else f'DEFICIT {e-R}' if R<e else 'OVERSHOOT?!'}")
    # sanity: verify 3 modes are null vectors of the full unsigned boundary
    cnt=0
    for (a,b),edges in Lpairs.items():
        if len(edges)<3: continue
        basis=incidence_kernel_basis(edges)
        for kv in basis:
            chk={}
            good=True
            for ei,cf in kv.items():
                u,v=edges[ei]
                ta=tuple(sorted((a,u,v))); tb=tuple(sorted((b,u,v)))
                if ta not in cellid or tb not in cellid: good=False; break
                for cell,s in ((ta,cf),(tb,-cf)):
                    x,y,z=cell
                    for f in ((y,z),(x,z),(x,y)): chk[f]=(chk.get(f,0)+s)%P
            if good:
                assert all(vv%P==0 for vv in chk.values()), f"MODE NOT NULL for pair {(a,b)}"
                cnt+=1
            if cnt>=3: break
        if cnt>=3: break
    log(f"  sanity: {cnt} modes verified null against the full unsigned boundary")
    return R,e

for N in (50000, 100000, 200000):
    run(N)
log("DONE")
