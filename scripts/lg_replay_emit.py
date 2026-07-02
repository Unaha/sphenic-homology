#!/usr/bin/env python3
# C-0746 REPLAY PACKAGE, EMITTER. For every level pair (v,a) at N in {1e5, 2e5}:
# emit raw replayable objects (cells of C_{>=a}, L_v^{>=a} edges, G-generators, H-generators)
# plus claimed k1/k2 computed over an 8-prime battery. Output: /lab/replay_c0746/N{N}/pair_v{v}_a{a}.json.gz
# and MANIFEST.json with SHA-256 of every bundle. The checker (separate, independent code) replays all.
import numpy as np, time, importlib.util, json, gzip, hashlib, os
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
spec=importlib.util.spec_from_file_location('eh','/lab/scripts/e_highN.py')
eh=importlib.util.module_from_spec(spec); spec.loader.exec_module(eh)
PRIMES=[5,7,11,13,131,10007,1073741789,2147483647]

def balance_basis(edges,p):
    piv={}; basis=[]
    for ei,(u,w) in enumerate(edges):
        r={u:1,w:1}; combo={ei:1}; placed=False
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr,pc=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%p
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
                for cc,vv in pc.items():
                    nv=(combo.get(cc,0)-fct*vv)%p
                    if nv: combo[cc]=nv
                    elif cc in combo: del combo[cc]
            else:
                inv=pow(r[k],p-2,p)
                piv[k]=({cc:(vv*inv)%p for cc,vv in r.items()},{cc:(vv*inv)%p for cc,vv in combo.items()})
                placed=True; break
        if not placed: basis.append(dict(combo))
    return basis

def elim_rank(cols,p):
    piv={}; rank=0
    for col in cols:
        r={k:v%p for k,v in col.items() if v%p}
        while r:
            k=min(r)
            if k in piv:
                fct=r[k]; pr=piv[k]
                for cc,vv in pr.items():
                    nv=(r.get(cc,0)-fct*vv)%p
                    if nv: r[cc]=nv
                    elif cc in r: del r[cc]
            else:
                inv=pow(r[k],p-2,p); piv[k]={cc:(vv*inv)%p for cc,vv in r.items()}; rank+=1; break
    return rank,piv

def reduce_mod(vec,piv,p):
    r={k:v%p for k,v in vec.items() if v%p}
    out={}
    while r:
        k=min(r)
        if k in piv:
            fct=r[k]; pr=piv[k]
            for cc,vv in pr.items():
                nv=(r.get(cc,0)-fct*vv)%p
                if nv: r[cc]=nv
                elif cc in r: del r[cc]
        else:
            out[k]=r.pop(k)
    return out

def gens_for(v,a,allcells,p):
    cellsV=[c for c in allcells if c[0]>=v]
    cells=[c for c in allcells if c[0]>=a]
    S={}
    for (x,y,z) in cellsV:
        S.setdefault((y,z),[]).append(x); S.setdefault((x,z),[]).append(y); S.setdefault((x,y),[]).append(z)
    Lv=set((q,r) for (x,q,r) in cellsV if x==v and q>=a)
    La=[(q,r) for (x,q,r) in cells if x==a]
    if not Lv or not La: return None
    G=[]; H=[]
    fibA={}
    for (x,y) in La:
        for c in S.get((x,y),[]):
            if c>a: fibA.setdefault(c,[]).append((x,y))
    for c,edges in fibA.items():
        if len(edges)<3: continue
        for kv in balance_basis(edges,p):
            H.append({"fiber":int(c),"vec":[[int(edges[ei][0]),int(edges[ei][1]),int(cf)] for ei,cf in kv.items()]})
    Lva=[e for e in Lv if a in S.get(e,[]) and e[0]>a]
    if len(Lva)>=3:
        for kv in balance_basis(Lva,p):
            G.append({"fiber":int(a),"kind":"b=a","vec":[[int(Lva[ei][0]),int(Lva[ei][1]),int((-cf)%p)] for ei,cf in kv.items()]})
    fibB=set()
    for e in Lv:
        if e[0]==a or e[1]==a:
            for b in S.get(e,[]):
                if b!=v and b>a: fibB.add(b)
    for b in sorted(fibB):
        full=[e for e in Lv if b in S.get(e,[]) and e[0]>=a and b not in e]
        if len(full)<3: continue
        for kv in balance_basis(full,p):
            vec={}
            for ei,cf in kv.items():
                s,t=full[ei]
                if s==a: key=tuple(sorted((b,t)))
                elif t==a: key=tuple(sorted((b,s)))
                else: continue
                vec[key]=(vec.get(key,0)-cf)%p
            vec={k:val for k,val in vec.items() if val%p}
            if vec: G.append({"fiber":int(b),"kind":"b>a","vec":[[int(k[0]),int(k[1]),int(val)] for k,val in vec.items()]})
    return cells,sorted(Lv),La,G,H

def ranks_for(v,a,cells,Lv,G,H,p):
    Lvset=set(map(tuple,Lv))
    Svecs=[{('E',r[0],r[1]):r[2] for r in g["vec"]} for g in G]+[{('E',r[0],r[1]):r[2] for r in h["vec"]} for h in H]
    _,pivS=elim_rank(Svecs,p)
    def colof(cell,aug):
        x,q,r=cell
        col={}
        for ed in ((q,r),(x,r),(x,q)):
            if ed in Lvset:
                col[('B',ed[0])]=(col.get(('B',ed[0]),0)+1)%p
                col[('B',ed[1])]=(col.get(('B',ed[1]),0)+1)%p
            else:
                col[('F',)+ed]=(col.get(('F',)+ed,0)+1)%p
        if aug and x==a:
            red=reduce_mod({('E',q,r):1},pivS,p)
            for k,val in red.items(): col[('Q',)+k]=(col.get(('Q',)+k,0)+val)%p
        return col
    r1,_=elim_rank((colof(c,False) for c in cells),p)
    r2,_=elim_rank((colof(c,True) for c in cells),p)
    return r1,r2

for N in (100000,200000):
    spf=eh.sieve_spf(N)
    A,B,C=[np.asarray(x,dtype=np.int64) for x in eh.sphenics(N,spf)]
    allcells=[(int(a),int(b),int(c)) for a,b,c in zip(A,B,C)]
    levels=sorted(set(a for a,_,_ in allcells))
    outdir=f"/lab/replay_c0746/N{N}"
    os.makedirs(outdir,exist_ok=True)
    manifest={}
    npairs=0; fails=0
    for vi,v in enumerate(levels):
        for a in levels[vi+1:]:
            got=gens_for(v,a,allcells,PRIMES[-1])
            if got is None: continue
            cells,Lv,La,G,H=got
            ranks={}
            ok=True
            for p in PRIMES:
                # G/H coefficient vectors are prime-dependent via balance_basis; regenerate per prime
                g2=gens_for(v,a,allcells,p)
                _,_,_,Gp,Hp=g2
                r1,r2=ranks_for(v,a,cells,Lv,Gp,Hp,p)
                ranks[str(p)]={"k1_rank":r1,"k2_rank":r2,"lg_pass":bool(r1==r2)}
                ok&= (r1==r2)
            npairs+=1
            if not ok: fails+=1; log(f"LG FAIL v={v} a={a}: {ranks}")
            bundle={"N":N,"v":int(v),"a":int(a),"cells":cells,"Lv":Lv,"G_bigprime":G,"H_bigprime":H,
                    "primes":PRIMES,"ranks":ranks,"ncells":len(cells)}
            raw=json.dumps(bundle,separators=(',',':')).encode()
            fn=f"{outdir}/pair_v{v}_a{a}.json.gz"
            with gzip.open(fn,'wb') as f: f.write(raw)
            manifest[f"pair_v{v}_a{a}.json.gz"]={"sha256":hashlib.sha256(open(fn,'rb').read()).hexdigest(),
                                                 "ranks":ranks}
        log(f"N={N}: level v={v} done ({npairs} pairs so far)")
    json.dump(manifest,open(f"{outdir}/MANIFEST.json","w"),indent=1)
    log(f"N={N}: EMITTED {npairs} pairs, LG failures across 8-prime battery: {fails}")
    log(f"MANIFEST sha256: {hashlib.sha256(open(f'{outdir}/MANIFEST.json','rb').read()).hexdigest()}")
log("DONE")
