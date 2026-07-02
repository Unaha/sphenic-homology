#!/usr/bin/env python3
# FILL THE HOLE: (1) GF(3) vs rational kernel (Rusnak cross-theta prediction: e_GF3 > e_Q,
# the excess = unbalanceable content, rationally invisible); (2) constructive decomposition
# anatomy of W_v at mid-levels: for each realizable boundary basis element h, solve
# h = sum_b z_b over pair fibers, report fiber count, support size, locality.
import numpy as np, time, importlib.util
from itertools import combinations
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
PB=2147483647
N=200000
spf=eh.sieve_spf(N); idx=np.arange(N+1)
A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]
allcells=[(int(a),int(b),int(c)) for a,b,c in zip(A,B,C)]

def kernel_dim(cells,p):
    piv={}; rank=0
    for (a,b,c) in cells:
        r={(b,c):1,(a,c):1,(a,b):1}
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
    return len(cells)-rank

# (1) GF(3) vs rational
eq=kernel_dim(allcells,PB)
e3=kernel_dim(allcells,3)
e5=kernel_dim(allcells,5)
log(f"N={N}: e_Q(proxy GF(2^31-1))={eq}  e_GF3={e3}  e_GF5={e5}  excess3={e3-eq} excess5={e5-eq}")

# (2) decomposition anatomy at v=13, 17
def anatomy(v):
    cells=[c for c in allcells if c[0]>=v]
    Lv=[(b,c) for (a,b,c) in cells if a==v]
    eidx={e:i for i,e in enumerate(Lv)}
    upper=[c for c in cells if c[0]>v]
    # free edges of C_{>v}: edges of upper cells not in Lv
    fidx={}
    rows=[]  # per upper cell: (free edge ids, Lv edge ids)
    for (a,b,c) in upper:
        fe=[]; le=[]
        for ed in ((b,c),(a,c),(a,b)):
            if ed in eidx: le.append(eidx[ed])
            else:
                if ed not in fidx: fidx[ed]=len(fidx)
                fe.append(fidx[ed])
        rows.append((fe,le))
    # left-nullspace of the (cells x free-edges) matrix: vectors ell over cells with, for each
    # free edge, sum of ell over incident cells = 0. Compute via column elimination on the
    # TRANSPOSE: columns = cells (variables), rows = free edges. Track combos to get ell basis.
    piv={}; wit=[]
    for ci,(fe,le) in enumerate(rows):
        r={f:1 for f in fe}
        combo={ci:1}; placed=False
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr,pc=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%PB
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
                for cc,vv in pc.items():
                    nv=(combo.get(cc,0)-fct*vv)%PB
                    if nv: combo[cc]=nv
                    elif cc in combo: del combo[cc]
            else:
                inv=pow(r[k],PB-2,PB)
                piv[k]=({cc:(vv*inv)%PB for cc,vv in r.items()},{cc:(vv*inv)%PB for cc,vv in combo.items()})
                placed=True; break
        if not placed: wit.append(combo)
    # boundaries h = sum ell_y * (Lv-edge rows of y); drop zero h (these are kernels of C_{>v})
    S={}
    for (a,b,c) in cells:
        S.setdefault((b,c),[]).append(a); S.setdefault((a,c),[]).append(b); S.setdefault((a,b),[]).append(c)
    fib={}
    for (s,t) in Lv:
        for b in S[(s,t)]:
            if b>v: fib.setdefault(b,[]).append((s,t))
    # fiber balance bases as vectors over Lv-edge idx
    def balance_basis(edges):
        piv2={}; basis=[]
        for ei,(u,w) in enumerate(edges):
            r={u:1,w:1}; combo={ei:1}; placed=False
            while r:
                k=min(r)
                if k in piv2:
                    fct=r[k]; pr,pc=piv2[k]
                    for cc,vv in pr.items():
                        nv=(r.get(cc,0)-fct*vv)%PB
                        if nv: r[cc]=nv
                        elif cc in r: del r[cc]
                    for cc,vv in pc.items():
                        nv=(combo.get(cc,0)-fct*vv)%PB
                        if nv: combo[cc]=nv
                        elif cc in combo: del combo[cc]
                else:
                    inv=pow(r[k],PB-2,PB)
                    piv2[k]=({cc:(vv*inv)%PB for cc,vv in r.items()},{cc:(vv*inv)%PB for cc,vv in combo.items()})
                    placed=True; break
            if not placed: basis.append(dict(combo))
        return basis
    fibvecs=[]  # (b, vector dict over Lv idx)
    for b,edges in fib.items():
        for kv in balance_basis(edges):
            fibvecs.append((b,{eidx[edges[ei]]:cf for ei,cf in kv.items()}))
    # eliminate fiber vectors, keep pivot structure with fiber-tag combos to decompose h's
    piv3={}
    for fi,(b,vec) in enumerate(fibvecs):
        r=dict(vec); combo={fi:1}; 
        while r:
            k=min(r)
            if k in piv3:
                fct=r[k]; pr,pc=piv3[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%PB
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
                for cc,vv in pc.items():
                    nv=(combo.get(cc,0)-fct*vv)%PB
                    if nv: combo[cc]=nv
                    elif cc in combo: del combo[cc]
            else:
                inv=pow(r[k],PB-2,PB)
                piv3[k]=({cc:(vv*inv)%PB for cc,vv in r.items()},{cc:(vv*inv)%PB for cc,vv in combo.items()})
                break
    nh=0; stats=[]
    for ell in wit:
        h={}
        for ci,cf in ell.items():
            for le in rows[ci][1]:
                h[le]=(h.get(le,0)+cf)%PB
        h={k:val for k,val in h.items() if val%PB}
        if not h: continue
        # BALANCE FILTER: h in W_v needs zero unsigned vertex sums (the v-facet block)
        vs={}
        for le,val in h.items():
            s,t=Lv[le]
            vs[s]=(vs.get(s,0)+val)%PB; vs[t]=(vs.get(t,0)+val)%PB
        if any(x%PB for x in vs.values()):
            continue
        nh+=1
        # decompose h against fiber pivots
        r=dict(h); used={}
        ok=True
        while r:
            k=min(r)
            if k not in piv3: ok=False; break
            fct=r[k]; pr,pc=piv3[k]
            for cc,vv in pr.items():
                nv=(r.get(cc,0)-fct*vv)%PB
                if nv: r[cc]=nv
                elif cc in r: del r[cc]
            for cc,vv in pc.items(): used[cc]=(used.get(cc,0)+fct*vv)%PB
        if not ok:
            stats.append((len(h),-1,-1))
            continue
        fibs=set(fibvecs[fi][0] for fi,cf in used.items() if cf%PB)
        stats.append((len(h),len([1 for fi,cf in used.items() if cf%PB]),len(fibs)))
    dec_ok=sum(1 for s in stats if s[1]>=0)
    log(f"v={v}: witnesses={len(wit)} BALANCED-h={nh} decomposed={dec_ok}/{nh}")
    if stats:
        hs=[s[0] for s in stats]; nf=[s[2] for s in stats if s[2]>=0]
        log(f"   |supp(h)|: min={min(hs)} med={sorted(hs)[len(hs)//2]} max={max(hs)} | #fibers used: min={min(nf) if nf else '-'} med={sorted(nf)[len(nf)//2] if nf else '-'} max={max(nf) if nf else '-'}")
for v in (13,17):
    anatomy(v)
log("DONE")
