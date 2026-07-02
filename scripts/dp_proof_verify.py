#!/usr/bin/env python3
# MECHANICAL VERIFICATION of the four steps of tonight's Dominated-Pair proof.
# Step 1 (base): a <<-antichain of edges contains no graph cycle (exhaustive + randomized hunt).
# Step 2 (insertion lemma): e<<f (omega-1 tuples), y = sorted(f + {s}) any s not in f => e_t < y_{t+1} for all t.
# Step 3 (join modes): for ANY fitting-shaped x (with/without collisions), the join-of-run-simplex-boundary
#         chain J_x is a nonzero cycle, supported on exactly {y : x <= y <= x+1, strictly increasing},
#         with coefficient +-1 on x, and x the unique coordinatewise minimum of its support.
# Step 4 (end-to-end shadow): on random generic slabs (4 rulers, omega=3,4), decreasing-value column
#         elimination pivots EXACTLY the non-fitting cells (free <=> fitting per-cell), the mechanical
#         footprint of the full theorem. (morse_verify.py confirmed this for the prime ruler; here generic.)
import numpy as np, random, time
from itertools import combinations, product
from fractions import Fraction
t0=time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]",*a,flush=True)
rng=random.Random(23)

# ---------- Step 1: antichain edges are forests ----------
def has_cycle(edges):
    par={}
    def find(a):
        while par.get(a,a)!=a: par[a]=par.get(par[a],par[a]); a=par[a]
        return a
    for a,b in edges:
        ra,rb=find(a),find(b)
        if ra==rb: return True
        par[ra]=rb
    return False
def is_antichain(cells):
    for u,v in combinations(cells,2):
        if all(a<b for a,b in zip(u,v)) or all(a>b for a,b in zip(u,v)): return False
    return True
viol=0; tested=0
alledges=list(combinations(range(1,9),2))
for k in (3,4,5,6):
    for E in combinations(alledges,k):
        if is_antichain(E):
            tested+=1
            if has_cycle(E): viol+=1; log("STEP1 VIOLATION:",E)
log(f"STEP1 exhaustive: {tested} antichain edge-sets (V<=8, k<=6): {viol} with a cycle")
for _ in range(200000):
    E=rng.sample(list(combinations(range(1,15),2)),rng.randint(4,9))
    if is_antichain(E) and has_cycle(E): viol+=1; log("STEP1 VIOLATION:",E)
log(f"STEP1 randomized: total violations {viol}")

# ---------- Step 2: insertion lemma ----------
bad=0
for _ in range(200000):
    w=rng.randint(2,6)
    e=sorted(rng.sample(range(1,40),w)); f=[ei+rng.randint(1,5) for ei in e]
    # force f strictly increasing and e<<f
    for i in range(1,w):
        if f[i]<=f[i-1]: f[i]=f[i-1]+1
    if not all(a<b for a,b in zip(e,f)): continue
    s=rng.randint(1,50)
    if s in f: continue
    y=sorted(f+[s])
    if not all(e[t]<y[t+1] for t in range(w)): bad+=1; log("STEP2 VIOLATION:",e,f,s,y)
log(f"STEP2 insertion lemma: violations {bad}")

# ---------- Step 3: join modes ----------
def join_mode(x):
    # runs of consecutive coordinates in x
    runs=[]; cur=[x[0]]
    for a in x[1:]:
        if a==cur[-1]+1: cur.append(a)
        else: runs.append(cur); cur=[a]
    runs.append(cur)
    # each run [a..b] -> values a..b+1, cells choose all-but-one value = facets of the simplex on the run values
    # facet skipping the j-th value gets sign (-1)^j  (boundary of the run simplex)
    factors=[]
    for run in runs:
        vals=list(range(run[0],run[-1]+2))
        fac=[]
        for j in range(len(vals)):
            fac.append((tuple(vals[:j]+vals[j+1:]),(-1)**j))
        factors.append(fac)
    # join: concatenate chosen tuples; sign = product (values across runs are increasing & disjoint so no reshuffle)
    chain={}
    for combo in product(*factors):
        cell=tuple(v for tup,_ in combo for v in tup)
        sgn=1
        for _,s in combo: sgn*=s
        chain[cell]=chain.get(cell,0)+sgn
    return {c:v for c,v in chain.items() if v}
def boundary(chain):
    out={}
    for cell,co in chain.items():
        for i in range(len(cell)):
            f=cell[:i]+cell[i+1:]; s=(-1)**i
            out[f]=out.get(f,0)+s*co
    return {c:v for c,v in out.items() if v}
bad3=0; n3=0
for _ in range(3000):
    w=rng.randint(2,6)
    # build x with deliberate collisions
    x=[rng.randint(1,6)]
    for _ in range(w-1):
        x.append(x[-1]+ (1 if rng.random()<0.5 else rng.randint(2,5)))
    x=tuple(x); n3+=1
    J=join_mode(x)
    ok=True
    if boundary(J): ok=False; log("STEP3 not a cycle:",x)
    lo=np.array(x); hi=lo+1
    for cell,co in J.items():
        c=np.array(cell)
        if not (len(cell)==w and all(c[i]<c[i+1] for i in range(w-1))): ok=False; log("STEP3 bad cell",x,cell)
        if not ((c>=lo).all() and (c<=hi).all()): ok=False; log("STEP3 outside box",x,cell)
    if abs(J.get(x,0))!=1: ok=False; log("STEP3 x coeff wrong",x,J.get(x,0))
    mins=[cell for cell in J if all((np.array(cell)<=np.array(o)).all() for o in J)]
    if mins!=[x]: ok=False; log("STEP3 x not unique min",x,mins)
    if not ok: bad3+=1
log(f"STEP3 join modes: {n3} tested (collision-rich, omega 2..6), {bad3} failures")

# ---------- Step 4: decreasing-value elimination free<=>fit on generic slabs ----------
P=2147483647
def elim_free_eq_fit(cells,val,fitset):
    order=sorted(range(len(cells)),key=lambda j:-val[j])
    piv={}; ok=True
    for j in order:
        c=cells[j]; r={}
        for i in range(len(c)):
            f=c[:i]+c[i+1:]; r[f]=(r.get(f,0)+((-1)**i))%P
        r={k:v for k,v in r.items() if v}
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
        free=not placed
        if free!=(j in fitset): ok=False; break
    return ok
def gen_slab(omega,kind,nmax,rng2):
    if kind=='prime':
        from sympy import prime
        PRL=[prime(i) for i in range(1,nmax+3)]
        w=lambda xs: float(np.prod([PRL[i-1] for i in xs]))
    elif kind=='add': w=lambda xs: float(sum(xs))
    elif kind=='wts':
        cs=sorted(rng2.uniform(0.5,3.0) for _ in range(omega))
        w=lambda xs,cs=cs: float(sum(c*v for c,v in zip(cs,xs)))
    else: w=lambda xs: float(sum((2**i)*v for i,v in enumerate(xs)))
    allc=list(combinations(range(1,nmax+1),omega))
    vals=sorted(w(list(c)) for c in allc)
    hi=vals[int(len(vals)*rng2.uniform(0.3,0.85))]
    lo=0.0 if rng2.random()<0.4 else hi*rng2.uniform(0.3,0.8)
    cells=[c for c in allc if lo<w(list(c))<=hi]
    val=[w(list(c)) for c in cells]
    fitset=set(j for j,c in enumerate(cells) if c[-1]+1<=nmax and w([v+1 for v in c])<=hi)
    return cells,val,fitset
import random as _r
rng2=_r.Random(5)
bad4=0; n4=0
for omega,nmax in ((3,26),(4,17)):
    for kind in ('prime','add','wts','silly'):
        for _ in range(8):
            cells,val,fitset=gen_slab(omega,kind,nmax,rng2)
            if not(30<=len(cells)<=2500): continue
            n4+=1
            if not elim_free_eq_fit(cells,val,fitset):
                bad4+=1; log(f"STEP4 FAIL omega={omega} {kind} cells={len(cells)}")
log(f"STEP4 elimination free<=>fit: {n4} generic slabs, {bad4} failures")
log("VERDICT:", "ALL FOUR STEPS CLEAN" if (viol==0 and bad==0 and bad3==0 and bad4==0) else "SOMETHING BROKE")
log("DONE")
