#!/usr/bin/env python3
# EXHAUSTIVE FINITE CERTIFICATE for the sphenic-complex vertex-completeness + connectivity lemma.
# For EVERY integer N in [30, 20000]:
#   (a) V(N) == {all primes <= N/6}  (vertex completeness, exact set equality)
#   (b) the edge graph is connected (c=1), and moreover every vertex is adjacent to vertex 2
#       (the "hub" form used by the analytic proof), for N where the complex is nonempty.
# Prints EVERY failing N with the failure mode; the analytic lemma (Nagura x>=25 at N/4p;
# Nagura at p for the collision regime p^2 in (N/4, 0.3N); real-Bertrand for N/4p in [3,25))
# covers all N > 5000, so the certificate must show no failures in (N_fail_max, 20000] with
# N_fail_max <= 5000. Output + this script get SHA-256 hashed into the banking packet.
import numpy as np, time, hashlib, sys
t0=time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]",*a,flush=True)
NMAX=20000
spf=np.arange(NMAX+1)
for i in range(2,int(NMAX**0.5)+1):
    if spf[i]==i: spf[i*i::i]=np.where(spf[i*i::i]==np.arange(i*i,NMAX+1,i),i,spf[i*i::i])
def factor3(n):
    ps=[]
    m=n
    while m>1:
        p=int(spf[m]); e=0
        while m%p==0: m//=p; e+=1
        if e>1: return None
        ps.append(p)
        if len(ps)>3: return None
    return ps if len(ps)==3 else None
primes=[i for i in range(2,NMAX+1) if spf[i]==i]
pset=set(primes)
# precompute sphenics up to NMAX
sph=[]
for n in range(30,NMAX+1):
    f=factor3(n)
    if f: sph.append((n,tuple(sorted(f))))
sph=np.array([(n,a,b,c) for n,(a,b,c) in sph],dtype=np.int64)
fails=[]
empty=[]
for N in range(30,NMAX+1):
    if N%2000==0: log(f'progress N={N}, fails so far={len(fails)}')
    lo,hi=N//2,N
    sel=sph[(sph[:,0]>lo)&(sph[:,0]<=N)]
    if len(sel)==0:
        empty.append(N); continue
    verts=set(sel[:,1])|set(sel[:,2])|set(sel[:,3])
    target={p for p in primes if p<=N//6}
    okV=(verts==target)
    # hub adjacency: every vertex shares a triangle with vertex 2 (or IS 2)
    hub=set()
    for n,a,b,c in sel:
        if a==2: hub.add(b); hub.add(c)
    okHub=(2 in verts) and all((v in hub) or v==2 for v in verts)
    # full connectivity via union-find (hub implies it, but check independently)
    par={}
    def find(x):
        while par.get(x,x)!=x: par[x]=par.get(par[x],par[x]); x=par[x]
        return x
    for n,a,b,c in sel:
        for u,v in ((a,b),(a,c),(b,c)):
            ru,rv=find(u),find(v)
            if ru!=rv: par[ru]=rv
    comps=len({find(v) for v in verts})
    okC=(comps==1)
    if not(okV and okC and okHub):
        fails.append((N,okV,okC,okHub,len(verts),len(target),comps))
log(f"scanned N=30..{NMAX}; complexes empty for {len(empty)} N (max empty N = {max(empty) if empty else '-'})")
log(f"failures: {len(fails)}")
if fails:
    fmax=max(f[0] for f in fails)
    log(f"MAX FAILING N = {fmax}  (analytic lemma needs this <= 5000: {'OK' if fmax<=5000 else 'PROBLEM'})")
    # print a compact failure log (all of them, they matter)
    for f in fails: print("FAIL",f,flush=True)
else:
    log("no failures at all in [30,20000]")
h=hashlib.sha256(open(sys.argv[0],'rb').read()).hexdigest()
log(f"script sha256 = {h}")
log("DONE")
