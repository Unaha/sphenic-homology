#!/usr/bin/env python3
# DARTBOARD NULL for the 14-denominator zero-free envelope M(rho) (write-up section 6, corr 0.992 claim).
# Question: is corr(measured 30-zero amplitudes of h1/V, |M(1/2+ig)/rho|) special to OUR 14
# topology-selected denominators, or does any random signed 14-tuple of small integers score it?
# Controls (hostile-null discipline): N1 LOOSE = 14 random distinct ints 10..200, balanced signs;
# N2 MATCHED = 7 crossing pairs (+m,-m') with m'~m*(1.005..1.6) mimicking bracket structure.
# Secondary sharp score: corr with the common 1/|rho| decay STRIPPED (meas*|rho| vs |M|),
# since the shared decay alone inflates the primary corr for ANY envelope.
import numpy as np, time
t0=time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]",*a,flush=True)

G=np.array([14.134725141734693,21.022039638771554,25.010857580145688,30.424876125859513,
32.935061587739189,37.586178158825671,40.918719012147495,43.327073280914999,
48.005150881167159,49.773832477672302,52.970321477714460,56.446247697063394,
59.347044002602353,60.831778524609809,65.112544048081606,67.079810529494173,
69.546401711173979,72.067157674481907,75.704690699083933,77.144840068874805,
79.337375020249367,82.910380854086030,84.735492980517050,87.425274613125229,
88.809111207634465,92.491899270558484,94.651344040519886,95.870634228245309,
98.831194218193692,101.317851005731391])

d=np.loadtxt('/lab/lab_db/hires2.csv',delimiter=',',skiprows=1)
N=d[:,0]; h1V=d[:,4]; x=np.log(N)
log(f"series: {len(N)} pts, lnN {x[0]:.2f}..{x[-1]:.2f}")

# detrend: smooth part = asymptotic series in 1/lnN
Xs=np.column_stack([x**0,1/x,1/x**2,1/x**3,1/x**4])
beta,_,_,_=np.linalg.lstsq(Xs,h1V,rcond=None)
r=(h1V-Xs@beta)*np.sqrt(N)   # rescale to stationary (fluct ~ N^-1/2)
log(f"detrended; rms(r)={r.std():.5f}")

# measured amplitudes: joint LSQ of cos/sin at all 30 zeros (they interfere)
C=np.concatenate([np.cos(np.outer(x,G)),np.sin(np.outer(x,G))],axis=1)
coef,_,_,_=np.linalg.lstsq(C,r,rcond=None)
meas=np.hypot(coef[:30],coef[30:])
np.save('/lab/lab_db/dartboard_meas30.npy',meas)
log("measured amps:",np.array2string(meas,precision=4,max_line_width=200))

mtrue=np.array([20,-21,28,-33,42,-55,78,-85,114,-115,138,-145,182,-187])
rho=0.5+1j*G; arho=np.abs(rho)
def envamp(ms):
    ms=np.asarray(ms,float); s=np.sign(ms); m=np.abs(ms)
    return np.abs((s[None,:]*m[None,:]**(-rho[:,None])).sum(1))
def scores(ms):
    aM=envamp(ms)
    p=aM/arho                              # primary convention (decay included)
    c=np.corrcoef(meas,p)[0,1]; c1=np.corrcoef(meas[1:],p[1:])[0,1]
    c2=np.corrcoef(meas*arho,aM)[0,1]      # decay-stripped (sharp)
    c21=np.corrcoef((meas*arho)[1:],aM[1:])[0,1]
    return c,c1,c2,c21

ct,ct1,ct2,ct21=scores(mtrue)
log(f"TRUE: corr={ct:.4f}  excl-g1={ct1:.4f}  | stripped={ct2:.4f}  stripped-excl-g1={ct21:.4f}")

rng=np.random.default_rng(7); NDRAW=20000
def null_loose():
    m=rng.choice(np.arange(10,201),14,replace=False)
    s=np.array([1]*7+[-1]*7); rng.shuffle(s); return s*m
def null_matched():
    out=[]
    for _ in range(7):
        a=int(np.exp(rng.uniform(np.log(15),np.log(190))))
        b=max(a+1,int(a*rng.uniform(1.005,1.6))); out+=[a,-b]
    return np.array(out)

for name,gen in [("LOOSE",null_loose),("MATCHED",null_matched)]:
    cs=np.empty((NDRAW,4))
    for i in range(NDRAW):
        cs[i]=scores(gen())
        if i%4000==0: log(f"{name} {i}/{NDRAW}")
    lab=["corr","excl-g1","stripped","stripped-excl-g1"]; tv=[ct,ct1,ct2,ct21]
    for k in range(4):
        v=cs[:,k]; pct=(v<tv[k]).mean()*100
        log(f"NULL {name} [{lab[k]:>16}]: median={np.median(v):+.3f} p90={np.percentile(v,90):+.3f} "
            f"p99={np.percentile(v,99):+.3f} max={v.max():+.3f}  TRUE={tv[k]:+.4f} -> percentile {pct:.2f}%")
    np.save(f'/lab/lab_db/dartboard_null_{name}.npy',cs)
log("DONE")
