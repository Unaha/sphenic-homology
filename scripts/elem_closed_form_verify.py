#!/usr/bin/env python3
# EXACT VERIFICATION of the b2 = elem closed form (the elem/V attack).
# Chain to verify, all exact integers, at each N:
#   (1) ADVANCE-BIJECTION SHELL: J(N) := #{sphenic pqr <= N : p+q+r+ > N}  ==  D(N/2) := #{odd semiprimes qr <= N/2}
#       (i.e. the even sphenics 2qr <= N).
#   (2) SPLIT: B(N) := #{pqr in (N/2,N] : p+q+r+ > N} = J(N) - cap(N),  cap(N) := #{pqr <= N/2 : p+q+r+ > N}.
#   (3) HENCE: elem(N) = F(N) - D(N/2) + cap(N)   (exact, ALL N).
#   (4) CLOSED FORM for N > N1 = 1,040,255: cap = 10 + sum over the ten crossing pairs of [pi(N/2pq) - pi(N/p+q+)]
#       => elem(N) = F(N) - D(N/2) + 10 + sum_10 [pi(N/2pq) - pi(N/p+q+)].
#   (5) Cross-check elem against the direct window enumeration (the C-0744 fitting count).
import numpy as np, time, importlib.util
from sympy import nextprime
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
PAIRS=[(2,3),(2,5),(2,7),(3,5),(3,7),(3,13),(3,19),(3,23),(5,7),(7,13)]
NXT={2:3,3:5,5:7,7:11,13:17,19:23,23:29}

def sphenics_upto(N,spf):
    # all squarefree pqr <= N (not just window): enumerate p<q<r
    idx=np.arange(N+1); PR=idx[(spf==idx)&(idx>=2)].astype(np.int64)
    A=[];Bv=[];C=[]
    for i,p in enumerate(PR):
        if p*(p+2)*(p+6)>N: break
        for j in range(i+1,len(PR)):
            q=PR[j]
            if p*q*q>N: break
            lim=N//(p*q)
            ks=PR[(PR>q)&(PR<=lim)]
            for r in ks:
                A.append(p);Bv.append(q);C.append(r)
    return np.array(A,np.int64),np.array(Bv,np.int64),np.array(C,np.int64),PR

def check(N):
    spf=eh.sieve_spf(N)
    A,Bv,C,PR=sphenics_upto(N,spf)
    S_N=len(A)
    prod=A*Bv*C
    j=np.searchsorted(PR,A); jb=np.searchsorted(PR,Bv); jc=np.searchsorted(PR,C)
    top=np.int64(nextprime(int(PR[-1])))
    nA=np.where(j+1<len(PR),PR[np.minimum(j+1,len(PR)-1)],top)
    nB=np.where(jb+1<len(PR),PR[np.minimum(jb+1,len(PR)-1)],top)
    nC=np.where(jc+1<len(PR),PR[np.minimum(jc+1,len(PR)-1)],top)
    sh=nA*nB*nC
    Jn=int(((prod<=N)&(sh>N)).sum())
    # D(N/2): odd semiprimes qr <= N/2  == even sphenics 2qr <= N
    Dn=int(((A==2)).sum())   # sphenics <= N with smallest prime 2: 2*q*r <= N <=> qr <= N/2, q,r odd  -- exact
    inwin=prod> N//2
    F=int(inwin.sum())
    Bn=int((inwin&(sh>N)).sum())
    cap=int(((prod<=N//2)&(sh>N)).sum())
    elem_direct=int((inwin&(sh<=N)).sum())
    # closed-form cap
    def pi(x):
        return int(np.searchsorted(PR,x,side='right'))
    cap_cf=10+sum(pi(N//(2*p*q))-pi(N//(NXT[p]*NXT[q])) for p,q in PAIRS)
    elem_cf=F-Dn+cap_cf
    ok1=(Jn==Dn); ok2=(Bn==Jn-cap); ok3=(elem_direct==F-Dn+cap)
    ok4=(cap==cap_cf) if N>1040255 else None
    ok5=(elem_direct==elem_cf) if N>1040255 else None
    log(f"N={N}: S={S_N} F={F} | J={Jn} D(N/2)={Dn} J==D:{ok1} | cap={cap} B={Bn} B==J-cap:{ok2} | "
        f"elem={elem_direct} F-D+cap={F-Dn+cap} eq:{ok3} | capCF={cap_cf} eq:{ok4} | elemCF={elem_cf} eq:{ok5}")
    return ok1 and ok2 and ok3 and (ok4 in (True,None)) and (ok5 in (True,None))

ok=True
for N in (200000, 500000, 1050000, 2000000, 5000000, 20000000):
    ok &= check(N)
log("VERDICT:", "ALL EXACT" if ok else "MISMATCH FOUND")
log("DONE")
