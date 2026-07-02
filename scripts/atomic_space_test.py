#!/usr/bin/env python3
# POUR THE CONCRETE: basis-independent ATOMIC test.
# W_v = (span of witness boundaries) ∩ balance.  ATOMIC RDL form:  W_v == Σ_b ( W_v ∩ ⟨L_{v,b}-edges⟩ ).
# Compute dim W_v (must equal the graded increment) and dim of the atomic sum; compare.
import numpy as np, time, importlib.util
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
PB=2147483647
N=200000
spf=eh.sieve_spf(N); idx=np.arange(N+1)
A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]
allcells=[(int(a),int(b),int(c)) for a,b,c in zip(A,B,C)]

def col_elim_basis(vectors):
    # returns (rank, pivot dict) for span; vectors = list of dicts
    piv={}; rank=0
    for vec in vectors:
        r={k:v%PB for k,v in vec.items() if v%PB}
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%PB
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[k],PB-2,PB); piv[k]={cc:(vv*inv)%PB for cc,vv in r.items()}; rank+=1; break
    return rank,piv

def in_span(vec,piv):
    r={k:v%PB for k,v in vec.items() if v%PB}
    while r:
        k=min(r)
        if k not in piv: return False
        fct=r[k]; pr=piv[k]
        for cc,vv in pr.items():
            nv=(r.get(cc,0)-fct*vv)%PB
            if nv: r[cc]=nv
            elif cc in r: del r[cc]
    return True

def analyze(v):
    cells=[c for c in allcells if c[0]>=v]
    Lv=[(b,c) for (a,b,c) in cells if a==v]
    eidx={e:i for i,e in enumerate(Lv)}
    upper=[c for c in cells if c[0]>v]
    fidx={}; rows=[]
    for (a,b,c) in upper:
        fe=[]; le=[]
        for ed in ((b,c),(a,c),(a,b)):
            if ed in eidx: le.append(eidx[ed])
            else:
                if ed not in fidx: fidx[ed]=len(fidx)
                fe.append(fidx[ed])
        rows.append((fe,le))
    piv={}; wit=[]
    for ci,(fe,le) in enumerate(rows):
        r={f:1 for f in fe}; combo={ci:1}; placed=False
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
    Hs=[]
    for ell in wit:
        h={}
        for ci,cf in ell.items():
            for le in rows[ci][1]: h[le]=(h.get(le,0)+cf)%PB
        h={k:val for k,val in h.items() if val%PB}
        if h: Hs.append(h)
    dimH,_=col_elim_basis(Hs)
    # W_v = H ∩ balance: work in H-coordinates: reduce H to an echelon basis first
    _,pivH=col_elim_basis(Hs)
    # extract echelon basis vectors from pivH? easier: re-eliminate Hs keeping reduced independent reps
    piv2={}; Hbasis=[]
    for h in Hs:
        r=dict(h)
        while r:
            k=min(r)
            if k in piv2:
                fct=r[k]; pr=piv2[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%PB
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[k],PB-2,PB); red={cc:(vv*inv)%PB for cc,vv in r.items()}
                piv2[k]=red; Hbasis.append(red); break
    # balance constraint matrix applied to Hbasis coordinates
    # vertex-sum functionals: for combo x = sum_i xi * Hbasis_i, sums per vertex must vanish
    verts={}
    for i,hb in enumerate(Hbasis):
        for le,val in hb.items():
            s,t=Lv[le]
            verts.setdefault(s,{})[i]=(verts.setdefault(s,{}).get(i,0)+val)%PB
            verts.setdefault(t,{})[i]=(verts.setdefault(t,{}).get(i,0)+val)%PB
    # nullspace of the (vertex x basis-index) matrix with combo tracking over basis indices
    piv3={}; Wcoefs=[]
    for i in range(len(Hbasis)):
        r={s:verts[s][i] for s in verts if i in verts[s] and verts[s][i]%PB}
        combo={i:1}; placed=False
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
                placed=True; break
        if not placed: Wcoefs.append(combo)
    Wbasis=[]
    for combo in Wcoefs:
        h={}
        for i,cf in combo.items():
            for le,val in Hbasis[i].items(): h[le]=(h.get(le,0)+cf*val)%PB
        h={k:val for k,val in h.items() if val%PB}
        if h: Wbasis.append(h)
    dimW,pivW=col_elim_basis(Wbasis)
    # atomic subspaces: W ∩ single-fiber support
    S={}
    for (a,b,c) in cells:
        S.setdefault((b,c),[]).append(a); S.setdefault((a,c),[]).append(b); S.setdefault((a,b),[]).append(c)
    fibedges={}
    for (s,t) in Lv:
        for b in S[(s,t)]:
            if b>v: fibedges.setdefault(b,set()).add(eidx[(s,t)])
    atomic=[]
    for b,eset in fibedges.items():
        # solve within Wbasis: combos supported in eset: nullspace of coordinates outside eset
        out={}
        for i,wb in enumerate(Wbasis):
            for le,val in wb.items():
                if le not in eset: out.setdefault(le,{})[i]=val
        piv4={}; combos=[]
        for i in range(len(Wbasis)):
            r={le:out[le][i] for le in out if i in out[le] and out[le][i]%PB}
            combo={i:1}; placed=False
            while r:
                k=min(r)
                if k in piv4:
                    fct=r[k]; pr,pc=piv4[k]
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
                    piv4[k]=({cc:(vv*inv)%PB for cc,vv in r.items()},{cc:(vv*inv)%PB for cc,vv in combo.items()})
                    placed=True; break
            if not placed: combos.append(combo)
        for combo in combos:
            h={}
            for i,cf in combo.items():
                for le,val in Wbasis[i].items(): h[le]=(h.get(le,0)+cf*val)%PB
            h={k:val for k,val in h.items() if val%PB}
            if h: atomic.append(h)
    dimAtomic,_=col_elim_basis(atomic)
    log(f"v={v}: dim(spanH)={dimH} dim(W_v)={dimW} dim(atomic sum)={dimAtomic} -> {'ATOMIC' if dimAtomic==dimW else f'GAP {dimW-dimAtomic}'}")
for v in (13,17,19):
    analyze(v)
log("DONE")
