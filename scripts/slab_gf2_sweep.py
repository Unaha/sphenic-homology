#!/usr/bin/env python3
# GF(2) SLAB SWEEP - closes the torsion gap in the slab identity evidence.
# Prior sweeps verified dim ker d = #fitting over GF(3),GF(7),GF(101),GF(2^31-1) but NEVER GF(2),
# and 2-torsion is the torsion that actually occurs in simplicial homology (RP^2).
# Since rank_GF2 <= rank_Q, we have ker_GF2 >= ker_Q = #fitting (verified over big odd p).
# If ker_GF2 == #fitting on every slab, there is no 2-torsion in the relevant homology and
# "field-independent, torsion-free" becomes airtight. Any strict excess = 2-TORSION FOUND.
# Rulers: prime-multiplicative / additive / random-increasing-weights / silly (1,2,4,...).
# omega = 2,3,4 (+ a few omega=5 prime slabs). Windows random, incl. pure down-sets (lo=0).
import numpy as np, time
from itertools import combinations
from sympy import prime
t0=time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]",*a,flush=True)

rng=np.random.default_rng(11)
PR=[prime(i) for i in range(1,400)]   # primes by position, 1-indexed positions used below

def gf2_kernel_dim(cells):
    # cells: list of tuples (vertex ids). boundary over GF(2): each facet ((w-1)-subset) once.
    fidx={}; rows=[]
    for c in cells:
        cols=[]
        for f in combinations(c,len(c)-1):
            if f not in fidx: fidx[f]=len(fidx)
            cols.append(fidx[f])
        rows.append(cols)
    ncols=len(fidx); W=(ncols+63)//64
    piv={}; rank=0
    one=np.uint64(1)
    for cols in rows:
        v=np.zeros(W,np.uint64)
        for c in cols: v[c>>6]^=one<<np.uint64(c&63)
        while True:
            nz=np.flatnonzero(v)
            if len(nz)==0: break
            w0=int(nz[0]); b=int(v[w0])
            pc=(w0<<6)|((b&-b).bit_length()-1)
            if pc in piv: v^=piv[pc]
            else: piv[pc]=v.copy(); rank+=1; break
    return len(rows)-rank

def make_ruler(kind,omega):
    if kind=='prime':
        return lambda xs: float(np.prod([PR[i-1] for i in xs])), 'prime'
    if kind=='add':
        return lambda xs: float(sum(xs)), 'add'
    if kind=='wts':
        c=np.sort(rng.uniform(0.5,3.0,omega))
        return lambda xs,c=c: float(np.dot(c,xs)), 'wts'
    if kind=='silly':
        c=[2**i for i in range(omega)]
        return lambda xs,c=c: float(np.dot(c,xs)), 'silly'

def slab_cells(w,omega,nmax,lo,hi):
    cells=[]
    for xs in combinations(range(1,nmax+1),omega):
        v=w(list(xs))
        if lo<v<=hi: cells.append(xs)
    return cells

def fitting_count(w,cells,hi,nmax):
    return sum(1 for xs in cells if xs[-1]+1<=nmax and w([x+1 for x in xs])<=hi)

def gfp_kernel_dim(cells,p=2147483647):
    # signed boundary, sparse elimination mod big odd prime (replicates the verified setup)
    fidx={}; rank=0; piv={}
    for c in cells:
        r={}
        for i in range(len(c)):
            f=c[:i]+c[i+1:]
            if f not in fidx: fidx[f]=len(fidx)
            r[fidx[f]]=(p-1) if (len(c)-1-i)%2 else 1   # drop i-th smallest: sign (-1)^(pos from end) convention consistent
        while r:
            cmin=min(r)
            if cmin in piv:
                fct=r[cmin]; pr=piv[cmin]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%p
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[cmin],p-2,p)
                piv[cmin]={cc:(vv*inv)%p for cc,vv in r.items()}
                rank+=1; break
    return len(cells)-rank

fails=0; total=0
for omega in (2,3,4):
    for kind in ('prime','add','wts','silly'):
        for trial in range(12):
            w,_=make_ruler(kind,omega)
            nmax={2:60,3:34,4:22}[omega]
            allv=sorted(w(list(xs)) for xs in combinations(range(1,nmax+1),omega))
            hi=allv[int(len(allv)*rng.uniform(0.25,0.85))]
            lo=0.0 if trial%3==0 else hi*rng.uniform(0.3,0.8)
            cells=slab_cells(w,omega,nmax,lo,hi)
            if not(20<=len(cells)<=6000): continue
            # guard: cells must not touch the nmax boundary in a way that clips fitting test
            k=gf2_kernel_dim(cells); fit=fitting_count(w,cells,hi,nmax); kq=gfp_kernel_dim(cells)
            total+=1; ok = (k==fit==kq)
            if not ok:
                fails+=1
                log(f"MISMATCH omega={omega} {kind} lo={lo:.3g} hi={hi:.3g} cells={len(cells)} kerGF2={k} kerGFbig={kq} fit={fit}")
            if total%20==0: log(f"progress: {total} slabs, {fails} mismatches")
# a few omega=5 prime slabs
omega=5
w,_=make_ruler('prime',omega)
for trial in range(6):
    nmax=16
    allv=sorted(w(list(xs)) for xs in combinations(range(1,nmax+1),omega))
    hi=allv[int(len(allv)*rng.uniform(0.3,0.8))]
    lo=0.0 if trial%2==0 else hi*rng.uniform(0.4,0.8)
    cells=slab_cells(w,omega,nmax,lo,hi)
    if not(10<=len(cells)<=6000): continue
    k=gf2_kernel_dim(cells); fit=fitting_count(w,cells,hi,nmax); kq=gfp_kernel_dim(cells)
    total+=1
    if not(k==fit==kq):
        fails+=1; log(f"MISMATCH omega=5 prime cells={len(cells)} kerGF2={k} kerGFbig={kq} fit={fit}")
log(f"RESULT: {total} slabs tested over GF(2), {fails} mismatches -> "+("NO 2-TORSION, identity holds mod 2" if fails==0 else "2-TORSION / IDENTITY FAILURE FOUND"))
log("DONE")
