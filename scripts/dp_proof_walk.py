#!/usr/bin/env python3
# PROOF-WALK: execute the Dominated-Pair proof's own construction on random real cycles.
# Stronger than testing the conclusion: every internal assertion of the induction is checked live.
#   walk(z, omega):
#     omega==2 : constructive base (find graph cycle; min vertex a*; smaller neighbour p;
#                first path edge with max endpoint > p dominates (a*,p))
#     omega>=3 : v = min vertex; A = cells containing v (assert nonempty, v first coord);
#                w = tail chain (assert nonzero cycle); B nonempty; recurse on w -> e<<f;
#                assert some y in B(supp) contains f; assert (v,e) << y; return pair.
# Any failed assertion = a hole in the proof. Cycles = random combinations of exact GF(p) kernel basis.
import numpy as np, random, time
from itertools import combinations
t0=time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]",*a,flush=True)
P=2147483647
rng=random.Random(31)

def nullspace_modp(cells):
    fidx={}
    for c in cells:
        for i in range(len(c)):
            f=c[:i]+c[i+1:]
            if f not in fidx: fidx[f]=len(fidx)
    m=len(fidx); n=len(cells)
    M=np.zeros((m,n),dtype=np.int64)
    for j,c in enumerate(cells):
        for i in range(len(c)):
            f=c[:i]+c[i+1:]
            M[fidx[f],j]=(M[fidx[f],j]+((-1)**i))%P
    # gaussian elimination to RREF mod p, track pivots
    Mw=M.copy(); piv=[]; r=0
    for col in range(n):
        sel=None
        for i in range(r,m):
            if Mw[i,col]%P: sel=i; break
        if sel is None: continue
        Mw[[r,sel]]=Mw[[sel,r]]
        inv=pow(int(Mw[r,col])%P,P-2,P)
        Mw[r]=(Mw[r]*inv)%P
        for i in range(m):
            if i!=r and Mw[i,col]%P:
                Mw[i]=(Mw[i]-Mw[i,col]*Mw[r])%P
        piv.append(col); r+=1
        if r==m: break
    free=[j for j in range(n) if j not in piv]
    basis=[]
    for fc in free:
        v=np.zeros(n,dtype=np.int64); v[fc]=1
        for ri,pc in enumerate(piv):
            v[pc]=(-Mw[ri,fc])%P
        basis.append(v)
    return basis

def boundary_chain(z):
    out={}
    for cell,co in z.items():
        for i in range(len(cell)):
            f=cell[:i]+cell[i+1:]
            out[f]=(out.get(f,0)+((-1)**i)*co)%P
    return {k:v for k,v in out.items() if v%P}

def base_pair(z):
    # z: nonzero edge cycle dict {(a,b):coef}
    edges=list(z.keys())
    adj={}
    for a,b in edges: adj.setdefault(a,set()).add(b); adj.setdefault(b,set()).add(a)
    for v,nb in adj.items(): assert len(nb)>=2, f"degree<2 at {v}"
    # find a cycle by walking never-backtracking
    start=min(adj); prev=None; cur=start; path=[start]; seen={start:0}
    while True:
        nxt=min(x for x in adj[cur] if x!=prev) if prev in adj[cur] and len(adj[cur])>1 else min(adj[cur])
        if nxt in seen:
            cyc=path[seen[nxt]:]; break
        seen[nxt]=len(path); path.append(nxt); prev,cur=cur,nxt
    astar=min(cyc); i=cyc.index(astar)
    n1,n2=cyc[(i-1)%len(cyc)],cyc[(i+1)%len(cyc)]
    p,q=(n1,n2) if n1<n2 else (n2,n1)
    # path from p to q around the cycle avoiding astar
    ring=cyc[(i+1)%len(cyc):]+cyc[:i]
    if ring[0]!=p: ring=ring[::-1]
    assert ring[0]==p and ring[-1]==q and astar not in ring
    e0=(astar,p)
    for u,vtx in zip(ring,ring[1:]):
        c,d=(u,vtx) if u<vtx else (vtx,u)
        if d>p:
            assert astar<c and p<d
            return e0,(c,d)
    raise AssertionError("no dominating edge found on path")

def walk(z,omega):
    if omega==2: return base_pair(z)
    verts=set(v for c in z for v in c)
    v=min(verts)
    A={c:co for c,co in z.items() if c[0]==v}
    assert A, "A empty"
    assert all(v not in c for c in z if c not in A), "v inside a B-cell not at position 0"
    B={c:co for c,co in z.items() if c not in A}
    w={c[1:]:co for c,co in A.items()}
    assert len(w)==len(A), "tail collision"
    assert boundary_chain(w)=={}, "w not a cycle"
    assert B, "B empty but z nonzero"
    e,f=walk(w,omega-1)
    assert all(a<b for a,b in zip(e,f)), "recursion returned non-dominating pair"
    fs=set(f)
    ys=[y for y in B if fs.issubset(set(y))]
    assert ys, "no B-cell covers f"
    y=ys[0]
    x=(v,)+e
    assert all(a<b for a,b in zip(x,y)), f"insertion failed: {x} !<< {y}"
    assert x in z and y in z
    return x,y

def gen_slab(omega,kind,nmax,rng2):
    if kind=='prime':
        from sympy import prime
        PRL=[prime(i) for i in range(1,nmax+3)]
        w=lambda xs: float(np.prod([float(PRL[i-1]) for i in xs]))
    elif kind=='add': w=lambda xs: float(sum(xs))
    elif kind=='wts':
        cs=sorted(rng2.uniform(0.5,3.0) for _ in range(omega))
        w=lambda xs,cs=cs: float(sum(c*v for c,v in zip(cs,xs)))
    else: w=lambda xs: float(sum((2**i)*v for i,v in enumerate(xs)))
    allc=list(combinations(range(1,nmax+1),omega))
    vals=sorted(w(list(c)) for c in allc)
    hi=vals[int(len(vals)*rng2.uniform(0.3,0.85))]
    lo=0.0 if rng2.random()<0.4 else hi*rng2.uniform(0.3,0.8)
    return [c for c in allc if lo<w(list(c))<=hi]

tot=0; slabs=0
for omega,nmax,kinds,tries in ((3,15,('prime','add','wts','silly'),6),(4,12,('add','wts','silly'),5),(5,11,('add','wts'),3)):
    for kind in kinds:
        for _ in range(tries):
            cells=gen_slab(omega,kind,nmax,rng)
            if not(15<=len(cells)<=260): continue
            basis=nullspace_modp(cells)
            if not basis: continue
            slabs+=1
            ncyc=min(40,6*len(basis))
            for _ in range(ncyc):
                k=rng.randint(1,min(4,len(basis)))
                vecs=rng.sample(basis,k)
                v=np.zeros(len(cells),dtype=np.int64)
                for b in vecs: v=(v+rng.randint(1,P-1)*b)%P
                z={cells[j]:int(v[j]) for j in range(len(cells)) if v[j]%P}
                if not z: continue
                assert boundary_chain(z)=={}, "sampled z not a cycle?!"
                x,y=walk(z,omega)
                tot+=1
            if slabs%10==0: log(f"{slabs} slabs, {tot} cycles walked clean")
log(f"RESULT: {tot} random cycles across {slabs} slabs (omega 3,4,5): every proof step held, every walk returned a verified dominated pair")
log("DONE")
