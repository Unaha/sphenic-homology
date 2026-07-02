#!/usr/bin/env python3
# THE SUMMIT TEST: (LG)_{v,a} for all level pairs. Per the solver architecture (SOLVE_leakage_out.md):
# (LG): every realizable a-tail lies in im(beta) + T_a. Implemented WITHOUT combo tracking:
#   k1 = dim ker M   where M = [non-link facets ; balance rows of link facets] over cells of C_{>=a}
#   k2 = dim ker of M augmented with each least-vertex-a cell's tail coordinate REDUCED mod S=span[G,H]
#   (LG) <=> k1 == k2.
# G = beta-images of pair-fiber balance bases (b >= a; b=a full-edge case + b>a via edges (a,y));
# H = T_a = internal-tail fibers Z_bal(L_{a,c}), c > a.
import numpy as np, time, importlib.util
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
PB=2147483647
N=100000
spf=eh.sieve_spf(N)
A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]
allcells=[(int(a),int(b),int(c)) for a,b,c in zip(A,B,C)]
levels=sorted(set(a for a,_,_ in allcells))

def balance_basis(edges):
    piv={}; basis=[]
    for ei,(u,w) in enumerate(edges):
        r={u:1,w:1}; combo={ei:1}; placed=False
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
        if not placed: basis.append(dict(combo))
    return basis

def elim_rank(cols):
    piv={}; rank=0
    for col in cols:
        r={k:v%PB for k,v in col.items() if v%PB}
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

def reduce_mod(vec,piv):
    r={k:v%PB for k,v in vec.items() if v%PB}
    out={}
    while r:
        k=min(r)
        if k in piv:
            fct=r[k]; pr=piv[k]
            for cc,vv in pr.items():
                nv=(r.get(cc,0)-fct*vv)%PB
                if nv: r[cc]=nv
                elif cc in r: del r[cc]
        else:
            out[k]=r.pop(k)
    return out

def lg_test(v,a):
    cells=[c for c in allcells if c[0]>=a]
    if not cells: return None
    # link of v restricted to vertices >= a
    Sthirds={}
    cellsV=[c for c in allcells if c[0]>=v]
    for (p,q,r) in cellsV:
        Sthirds.setdefault((q,r),[]).append(p); Sthirds.setdefault((p,r),[]).append(q); Sthirds.setdefault((p,q),[]).append(r)
    Lv=set()
    for (p,q,r) in cellsV:
        if p==v and q>=a: Lv.add((q,r))
    if not Lv: return None
    # La (link of a within C_{>=a}) and its tail-edge index
    La=[(q,r) for (p,q,r) in cells if p==a]
    if not La: return None
    # ---- S = span[G,H] over tail-edge coords ('E',x,y)
    Svecs=[]
    # H: fibers of a: thirds c>a of La edges
    fibA={}
    for (x,y) in La:
        for c in Sthirds.get((x,y),[]):
            if c>a: fibA.setdefault(c,[]).append((x,y))
    for c,edges in fibA.items():
        if len(edges)<3: continue
        for kv in balance_basis(edges):
            Svecs.append({('E',)+edges[ei]:cf for ei,cf in kv.items()})
    # G: b=a term: z in Z_bal(L_{v,a}^a): edges (x,y) in Lv with a-third and x,y>=a... L_{v,a}: (x,y) in Lv with axy in C
    Lva=[e for e in Lv if a in Sthirds.get(e,[]) and e[0]>a]
    if len(Lva)>=3:
        for kv in balance_basis(Lva):
            Svecs.append({('E',)+Lva[ei]:(-cf)%PB for ei,cf in kv.items()})
    # G: b>a terms: fibers L_{v,b} with edges containing a: edge (a,y) in Lv, third b (b>=a? b>v, b!=a)
    fibB={}
    for e in Lv:
        if e[0]==a or e[1]==a:
            y=e[1] if e[0]==a else e[0]
            for b in Sthirds.get(e,[]):
                if b!=v and b>=a and b!=a: fibB.setdefault(b,[]).append(e)
    for b,aedges in fibB.items():
        # full fiber L_{v,b}^a for balance basis (edges (s,t) in Lv, b-third, s,t>=a, b not in edge)
        full=[e for e in Lv if b in Sthirds.get(e,[]) and e[0]>=a and b not in e]
        if len(full)<3: continue
        eloc={e:i for i,e in enumerate(full)}
        for kv in balance_basis(full):
            vec={}
            for ei,cf in kv.items():
                s,t=full[ei]
                if s==a: vec[('E',)+tuple(sorted((b,t)))]=(vec.get(('E',)+tuple(sorted((b,t))),0)-cf)%PB
                elif t==a: vec[('E',)+tuple(sorted((b,s)))]=(vec.get(('E',)+tuple(sorted((b,s))),0)-cf)%PB
            vec={k:val for k,val in vec.items() if val%PB}
            if vec: Svecs.append(vec)
    _,pivS=elim_rank(Svecs)
    # ---- M columns per cell (+ augmented tail-quotient coords)
    Lvset=Lv
    def colof(cell,aug):
        p,q,r=cell
        col={}
        for ed in ((q,r),(p,r),(p,q)):
            if ed in Lvset:
                col[('B',ed[0])]=(col.get(('B',ed[0]),0)+1)%PB
                col[('B',ed[1])]=(col.get(('B',ed[1]),0)+1)%PB
            else:
                col[('F',)+ed]=(col.get(('F',)+ed,0)+1)%PB
        if aug and p==a:
            tail={('E',q,r):1}
            red=reduce_mod(tail,pivS)
            for k,val in red.items(): col[('Q',)+k]=(col.get(('Q',)+k,0)+val)%PB
        return col
    r1,_=elim_rank(colof(c,False) for c in cells)
    r2,_=elim_rank(colof(c,True) for c in cells)
    return (r1,r2,len(cells))

fails=0; tested=0
for vi,v in enumerate(levels):
    for a in levels[vi+1:]:
        res=lg_test(v,a)
        if res is None: continue
        r1,r2,nc=res
        tested+=1
        if r1!=r2:
            fails+=1
            log(f"LG FAIL v={v} a={a}: rank {r1} -> {r2} (deficit {r2-r1}) cells={nc}")
log(f"N={N}: (LG) tested at {tested} level pairs, failures={fails}")
log("VERDICT: "+("ALL (LG) PASS — THEOREM CERTIFIED AT THIS N" if fails==0 else "LG FAILURES PRESENT"))
log("DONE")
