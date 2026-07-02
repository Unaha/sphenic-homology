#!/usr/bin/env python3
# C-0746 REPLAY PACKAGE, INDEPENDENT CHECKER. Shares NO algorithmic path with the emitter:
#  - reads ONLY cells + Lv from each bundle; recomputes fibers itself;
#  - balance bases via SPANNING-TREE POTENTIALS (fundamental even cycles + odd-edge barbells
#    with +-2 connecting paths), NOT incidence elimination; every generator verified BALANCED
#    in EXACT INTEGER arithmetic (vertex sums == 0 in Z) before use;
#  - rank computation: its own elimination with REVERSED-shuffled column order and max-key pivots;
#  - recomputes k1/k2 over the same 8-prime battery and compares to the manifest claims.
import numpy as np, json, gzip, glob, time, random, hashlib
t0=time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]",*a,flush=True)
PRIMES=[5,7,11,13,131,10007,1073741789,2147483647]

def tree_balance_basis(edges):
    # spanning-tree potential construction with per-component dimension GUARD.
    adj={}
    for i,(u,w) in enumerate(edges): adj.setdefault(u,[]).append((w,i)); adj.setdefault(w,[]).append((u,i))
    def vsums(vec):
        s={}
        for ei,val in vec.items():
            u,w=edges[ei]; s[u]=s.get(u,0)+val; s[w]=s.get(w,0)+val
        return {k:v for k,v in s.items() if v}
    seen=set(); basis=[]
    for root in sorted(adj):
        if root in seen: continue
        parent={root:(None,None)}; depth={root:0}; stack=[root]; seen.add(root); tree=set(); vc=1
        while stack:
            x=stack.pop()
            for (y,ei) in adj[x]:
                if y not in parent:
                    parent[y]=(x,ei); depth[y]=depth[x]+1; seen.add(y); tree.add(ei); stack.append(y); vc+=1
        comp_edges=[i for i,(u,w) in enumerate(edges) if u in parent and w in parent]
        ec=len(comp_edges)
        def tree_path(u,w):
            pu=[]; pw=[]
            uu,ww=u,w
            while depth[uu]>depth[ww]: pu.append(parent[uu][1]); uu=parent[uu][0]
            while depth[ww]>depth[uu]: pw.append(parent[ww][1]); ww=parent[ww][0]
            while uu!=ww:
                pu.append(parent[uu][1]); uu=parent[uu][0]
                pw.append(parent[ww][1]); ww=parent[ww][0]
            return pu,pw,uu
        def loop_vec(ei):
            u,w=edges[ei]
            pu,pw,anc=tree_path(u,w)
            vec={ei:1}
            s=-1
            for e2 in pu: vec[e2]=vec.get(e2,0)+s; s=-s
            s=-1
            for e2 in pw: vec[e2]=vec.get(e2,0)+s; s=-s
            vec={k:v for k,v in vec.items() if v}
            return vec
        nontree=[i for i in comp_edges if i not in tree]
        evens=[]; odds=[]
        for ei in nontree:
            vec=loop_vec(ei); res=vsums(vec)
            if not res: evens.append((ei,vec))
            else: odds.append((ei,vec,res))
        for ei,vec in evens: basis.append(vec)
        if odds:
            e0,v0,r0=odds[0]
            (A0,ra)=list(r0.items())[0]
            assert abs(ra)==2 and len(r0)==1, f"odd-loop residual malformed {r0}"
            for ei,vi,ri in odds[1:]:
                (A1,rb)=list(ri.items())[0]
                assert abs(rb)==2 and len(ri)==1
                found=None
                for cb in (1,-1):
                    cand={}
                    for k,val in v0.items(): cand[k]=cand.get(k,0)+val
                    for k,val in vi.items(): cand[k]=cand.get(k,0)+cb*val
                    if A0!=A1:
                        pu,pw,anc=tree_path(A0,A1)
                        path=pu+pw[::-1]
                        for st in (1,-1):
                            c2=dict(cand); s=st
                            for e2 in path: c2[e2]=c2.get(e2,0)+s; s=-s
                            c2={k:v for k,v in c2.items() if v}
                            if not vsums(c2): found=c2; break
                        if found: break
                        # also try coefficient 2 paths
                        for st in (2,-2):
                            c2=dict(cand); s=st
                            for e2 in path: c2[e2]=c2.get(e2,0)+s; s=-s
                            c2={k:v for k,v in c2.items() if v}
                            if not vsums(c2): found=c2; break
                        if found: break
                    else:
                        cand={k:v for k,v in cand.items() if v}
                        if not vsums(cand): found=cand; break
                assert found is not None, f"barbell construction failed for edges {e0},{ei}"
                basis.append(found)
        # DIMENSION GUARD
        bip = not odds
        expected = ec - vc + (1 if bip else 0)
        got = len(evens) + (len(odds)-1 if odds else 0)
        assert got==expected, f"component dim mismatch: got {got} expected {expected} (E={ec},V={vc},bip={bip})"
    for vec in basis:
        assert not vsums(vec), "unbalanced generator escaped"
    return basis,len(basis)

def elim_rank_shuffled(cols,p,seed):
    cols=list(cols)
    rnd=random.Random(seed); rnd.shuffle(cols)
    piv={}; rank=0
    for col in cols:
        r={k:v%p for k,v in col.items() if v%p}
        while r:
            k=max(r)
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
        k=max(r)
        if k in piv:
            fct=r[k]; pr=piv[k]
            for cc,vv in pr.items():
                nv=(r.get(cc,0)-fct*vv)%p
                if nv: r[cc]=nv
                elif cc in r: del r[cc]
        else:
            out[k]=r.pop(k)
    return out

def check_pair(fn,claims):
    b=json.loads(gzip.open(fn,'rb').read())
    v,a=b["v"],b["a"]; cells=[tuple(c) for c in b["cells"]]; Lv=set(tuple(e) for e in b["Lv"])
    S={}
    for (x,y,z) in cells:
        S.setdefault((y,z),[]).append(x); S.setdefault((x,z),[]).append(y); S.setdefault((x,y),[]).append(z)
    # NOTE: fibers must be computed within C_{>=v}; Lv given in bundle already restricted; thirds from cells C_{>=a}
    La=[(q,r) for (x,q,r) in cells if x==a]
    # rebuild S/G/H independently
    fibA={}
    for (x,y) in La:
        for c in S.get((x,y),[]):
            if c>a: fibA.setdefault(c,[]).append((x,y))
    ok_all=True
    tails_S=[]
    nint=0
    Hv=[]
    for c,edges in fibA.items():
        if len(edges)<3: continue
        basis,_=tree_balance_basis(edges)
        for kv in basis:
            Hv.append({('E',)+edges[ei]:cf for ei,cf in kv.items()}); nint+=1
    Gv=[]
    Lva=[e for e in Lv if a in S.get(e,[]) and e[0]>a]
    if len(Lva)>=3:
        basis,_=tree_balance_basis(Lva)
        for kv in basis: Gv.append({('E',)+Lva[ei]:-cf for ei,cf in kv.items()})
    fibB=set()
    for e in Lv:
        if a in e:
            y=e[1] if e[0]==a else e[0]
            for bb in S.get(e,[]):
                if bb!=v and bb>a: fibB.add(bb)
    for bb in sorted(fibB):
        full=[e for e in Lv if bb in S.get(e,[]) and e[0]>=a and bb not in e]
        if len(full)<3: continue
        basis,_=tree_balance_basis(full)
        for kv in basis:
            vec={}
            for ei,cf in kv.items():
                s,t=full[ei]
                if s==a: key=('E',)+tuple(sorted((bb,t)))
                elif t==a: key=('E',)+tuple(sorted((bb,s)))
                else: continue
                vec[key]=vec.get(key,0)-cf
            vec={k:val for k,val in vec.items() if val}
            if vec: Gv.append(vec)
    res={}
    for p in PRIMES:
        _,pivS=elim_rank_shuffled(Gv+Hv,p,seed=v*100003+a)
        Lvset=Lv
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
        r1,_=elim_rank_shuffled((colof(c,False) for c in cells),p,seed=v*7+a)
        r2,_=elim_rank_shuffled((colof(c,True) for c in cells),p,seed=v*7+a)
        claimed=claims[str(p)]
        same=(r1==claimed["k1_rank"] and r2==claimed["k2_rank"] and r1==r2)
        res[p]=same
        ok_all&=same
    return v,a,ok_all,res

import sys
base=sys.argv[1] if len(sys.argv)>1 else "/lab/replay_c0746/N100000"
man=json.load(open(f"{base}/MANIFEST.json"))
npair=0; bad=0
for fn,meta in sorted(man.items()):
    full=f"{base}/{fn}"
    h=hashlib.sha256(open(full,'rb').read()).hexdigest()
    if h!=meta["sha256"]:
        log(f"HASH MISMATCH {fn}"); bad+=1; continue
    v,a,ok,res=check_pair(full,meta["ranks"])
    npair+=1
    if not ok:
        bad+=1; log(f"CHECK FAIL v={v} a={a}: {res}")
    if npair%25==0: log(f"progress {npair} pairs, bad={bad}")
log(f"{base}: INDEPENDENT CHECK: {npair} pairs, failures={bad}")
log("VERDICT: "+("ALL REPLAYED CLEAN" if bad==0 else "FAILURES"))
log("DONE")
