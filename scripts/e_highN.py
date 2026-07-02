import numpy as np, time, sys, os
import scipy.sparse as sp
import pandas as pd
from collections import deque
P=2147483647
CORP="/lab/lab_db/kappa_highN.parquet"
Mbig=1<<26

def sieve_spf(NMAX):
    spf=np.zeros(NMAX+1,dtype=np.int32)
    for i in range(2,int(NMAX**0.5)+1):
        if spf[i]==0:
            sl=spf[i*i::i]; sl[sl==0]=i
    z=np.nonzero(spf[2:]==0)[0]+2; spf[z]=z.astype(np.int32)
    return spf

def sphenics(N,spf):
    half=N//2
    arr=np.arange(half+1,N+1,dtype=np.int64)
    a=spf[arr].astype(np.int64); m=arr//a
    ok=m>1; ok&=(m%np.where(a==0,1,a)!=0)
    b=np.zeros_like(m); b[ok]=spf[m[ok]]
    m2=arr.copy(); m2[ok]=m[ok]//np.where(b[ok]==0,1,b[ok])
    ok&=(m2>1); ok&=(b!=a); ok&=(m2%np.where(b==0,1,b)!=0)
    c=m2; ok&=(spf[np.where(c<2,2,c)]==c); ok&=(c!=b)
    return a[ok],b[ok],c[ok]

def bm_vec(s):
    s=np.asarray(s,dtype=np.int64)%P; n_=len(s); M=n_+2
    C=np.zeros(M,dtype=np.int64);C[0]=1;lenC=1
    B=np.zeros(M,dtype=np.int64);B[0]=1;lenB=1
    L=0;m=1;b=1
    for n in range(n_):
        if L>0: d=(int(s[n])+int(((C[1:L+1]*s[n-L:n][::-1])%P).sum()))%P
        else: d=int(s[n])%P
        if d==0: m+=1; continue
        coef=(d*pow(int(b),P-2,P))%P; newlenC=max(lenC,m+lenB)
        if 2*L<=n:
            T=C.copy();lenT=lenC
            C[m:m+lenB]=(C[m:m+lenB]-coef*B[:lenB])%P
            lenC=newlenC;L=n+1-L;B=T;lenB=lenT;b=d;m=1
        else:
            C[m:m+lenB]=(C[m:m+lenB]-coef*B[:lenB])%P; lenC=newlenC;m+=1
    return list(C[:L+1])

def wrank(A,seed=0):
    rng=np.random.default_rng(seed); E,F=A.shape; AT=A.T.tocsr()
    D1=rng.integers(1,P,size=E,dtype=np.int64);D2=rng.integers(1,P,size=F,dtype=np.int64)
    def Bmul(v):
        t=(D2*v)%P;t=(A.dot(t))%P;t=(D1*t)%P;t=(AT.dot(t))%P;t=(D2*t)%P;return t
    u=rng.integers(0,P,size=F,dtype=np.int64);v=rng.integers(0,P,size=F,dtype=np.int64)
    seq=[];w=v.copy()
    for _ in range(2*F+1): seq.append(int(((u*w)%P).sum()%P));w=Bmul(w)
    C=bm_vec(seq);L=len(C)-1; return L-(1 if C[L]%P==0 else 0)

def core_e(A,B,C):
    F=len(A)
    codes=np.concatenate([A*Mbig+B, A*Mbig+C, B*Mbig+C])
    uniq,inv=np.unique(codes,return_inverse=True); Ec=len(uniq)
    te=np.stack([inv[:F],inv[F:2*F],inv[2*F:]],axis=1)
    edeg=np.bincount(te.ravel(),minlength=Ec).astype(np.int64)
    flat_e=te.ravel(); flat_t=np.repeat(np.arange(F,dtype=np.int64),3)
    order=np.argsort(flat_e,kind='stable')
    t_sorted=flat_t[order]
    bounds=np.searchsorted(flat_e[order],np.arange(Ec+1))
    alive=np.ones(F,dtype=bool)
    ptr=bounds[:-1].copy()
    dq=deque(np.nonzero(edeg==1)[0].tolist())
    while dq:
        e=dq.popleft()
        if edeg[e]!=1: continue
        p=ptr[e]; hi=bounds[e+1]; ti=-1
        while p<hi:
            cand=t_sorted[p]
            if alive[cand]: ti=cand; break
            p+=1
        ptr[e]=p
        if ti<0: continue
        alive[ti]=False
        for ee in te[ti]:
            edeg[ee]-=1
            if edeg[ee]==1: dq.append(int(ee))
    coretri=te[alive]; Fc=len(coretri)
    if Fc==0: return 0,0,0
    ce=np.unique(coretri.ravel())
    remap=-np.ones(Ec,dtype=np.int64); remap[ce]=np.arange(len(ce))
    cc=remap[coretri]; Ecore=len(ce)
    rows=cc.ravel(); cols=np.repeat(np.arange(Fc,dtype=np.int64),3)
    Au=sp.csr_matrix((np.ones(3*Fc,dtype=np.int64),(rows,cols)),shape=(Ecore,Fc))
    ru=wrank(Au,1); e=Fc-ru
    return Fc,Ecore,e

def run(N):
    spf=sieve_spf(N)
    A,B,C=sphenics(N,spf)
    V=int(np.unique(np.concatenate([A,B,C])).size)
    E=int(np.unique(np.concatenate([A*Mbig+B,A*Mbig+C,B*Mbig+C])).size)
    F=len(A)
    Fc,Ecore,e=core_e(A,B,C)
    chi=V-E+F; kV=(1-chi)+e
    return dict(N=N,V=V,E=E,F=F,Fcore=Fc,e=e,chi=chi,kappaV=kV,
                kappa=kV/V,chi_over_V=chi/V,e_over_V=e/V,method='wiedemann_2core_fast')

if __name__=="__main__":
    r=run(200000)
    exp=3082
    print(f"VALIDATE 200k: e={r['e']} (exp {exp}) kappaV={r['kappaV']} kappa={r['kappa']:.5f}  {'PASS' if r['e']==exp else 'FAIL'}",flush=True)
    if r['e']!=exp:
        print("VALIDATION FAILED",flush=True); sys.exit(1)
    NS=[int(x) for x in sys.argv[1:]]
    for N in NS:
        t=time.time(); r=run(N)
        df=pd.DataFrame([r])
        if os.path.exists(CORP):
            old=pd.read_parquet(CORP); df=pd.concat([old,df],ignore_index=True)
            df=df.drop_duplicates(subset=['N'],keep='last').sort_values('N')
        df.to_parquet(CORP,index=False)
        print(f"N={N}: V={r['V']} Fcore={r['Fcore']} e={r['e']} kappa={r['kappa']:.5f} chi/V={r['chi_over_V']:.4f} e/V={r['e_over_V']:.4f}  [{time.time()-t:.0f}s]",flush=True)
    print("DONE",flush=True)
