#!/usr/bin/env python3
# SOURCE-TO-BUNDLE ENUMERATION REPLAY (Addy v2 ruling's weakest link).
# Independent sphenic enumerator: NO shared code with e_highN.py — per-integer trial
# factorization over the window, no sieve-of-least-prime-factor, no triple loop.
# For every replay bundle: re-derive from (N, v, a) alone the cell list of C_{>=a} and the
# L_v^{>=a} edge list; compare EXACTLY (as sorted sets) with the bundled ones.
import json, gzip, glob, time, hashlib
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)

def factor_trial(n):
    fs=[]
    d=2
    m=n
    while d*d<=m:
        if m%d==0:
            e=0
            while m%d==0: m//=d; e+=1
            fs.append((d,e))
        d+=1 if d==2 else 2
    if m>1: fs.append((m,1))
    return fs

def sphenics_independent(N):
    out=[]
    for n in range(N//2+1, N+1):
        fs=factor_trial(n)
        if len(fs)==3 and all(e==1 for _,e in fs):
            out.append(tuple(sorted(p for p,_ in fs)))
    return out

import sys
TOTBAD=0
import glob as _g
for base in sorted(_g.glob("certificates/N*")):
    N=int(base.split("N")[-1])
    log(f"{base}: independently enumerating window sphenics for N={N} by trial factorization ...")
    cells_full=sphenics_independent(N)
    cellset_full=set(cells_full)
    log(f"  independent enumeration: {len(cells_full)} window sphenics")
    man=json.load(open(f"{base}/MANIFEST.json"))
    bad=0; npair=0
    for fn in sorted(man):
        full=f"{base}/{fn}"
        h=hashlib.sha256(open(full,'rb').read()).hexdigest()
        if h!=man[fn]["sha256"]:
            log(f"  HASH MISMATCH {fn}"); bad+=1; continue
        b=json.loads(gzip.open(full,'rb').read())
        v,a=b["v"],b["a"]
        # independent derivation of C_{>=a} and L_v^{>=a}
        my_cells=sorted(c for c in cellset_full if c[0]>=a)
        their_cells=sorted(map(tuple,b["cells"]))
        ok1=(my_cells==their_cells)
        my_Lv=sorted((q,r) for (p,q,r) in cellset_full if p==v and q>=a)
        their_Lv=sorted(map(tuple,b["Lv"]))
        ok2=(my_Lv==their_Lv)
        npair+=1
        if not(ok1 and ok2):
            bad+=1; log(f"  ENUM MISMATCH v={v} a={a}: cells={ok1} Lv={ok2}")
    log(f"  {base}: {npair} bundles, enumeration mismatches: {bad}")
    TOTBAD+=bad
log("VERDICT: "+("SOURCE-TO-BUNDLE ENUMERATION REPLAY CLEAN" if TOTBAD==0 else f"{TOTBAD} MISMATCHES"))
log("DONE")
