# A balance-mode structure theorem for the unsigned kernel of the sphenic window complex

*Working write-up, Improbability Lab, 2 July 2026. Not a submission. Audience: algebraic combinatorics and oriented hypergraphs. Status labels are load-bearing: **[PROVED]**, **[BANKED]** (proved and cleared by the lab's hostile adjudication protocol at the stated scope), **[VERIFIED]** (exact numerics), **[CERTIFIED]** (holds by a hashed finite certificate at the stated N and characteristics), **[OPEN]**. Registry anchors: C-0744 (the every-field slab identity, which supplies the characteristic-2 stratum here because unsigned and signed boundaries coincide over GF(2)), C-0745 (the top count), C-0746 (this structure theorem, at the certified perimeter). The scope of the main theorem is finite and explicit: it is stated and banked at the certified perimeter, not for all N.*

---

## Abstract

Let C be the sphenic window complex at level N: the 2-complex whose triangles are the squarefree three-prime integers pqr in the window (N/2, N], with edges the co-occurring prime pairs and vertices the primes. Let ∂ᵘ be its *unsigned* boundary, the all-positive incidence map, which presents C as an oriented hypergraph with every adjacency negative in the sense of Rusnak. We give a structural description of the rational kernel of ∂ᵘ as a span of explicit *balance modes* fibered over vertex-pairs, and we certify it at a finite, explicit perimeter.

**Structure theorem, at the certified perimeter. [BANKED as C-0746, certified perimeter.]** For the five bundled complexes N ∈ {50000, 100000, 200000, 300000, 500000}, certified over ℚ and an eight-prime battery at all five N (and over every prime characteristic outside {2, 3} on the two-stage integer-certified subset N ∈ {10⁵, 2×10⁵}),

ker ∂ᵘ = span{ m_{a,b,z} = Σ_g z_g ([a ∪ g] − [b ∪ g]) : prime pairs a < b, z ∈ Z_bal(L_{a,b}) },

where L_{a,b} is the common link graph of the pair and Z_bal is its balance kernel (the Zaslavsky even-circle cycle space: even cycles and odd-cycle barbells). Consequently, at that perimeter, e := dim ker ∂ᵘ is a fibered balance count, the unsigned rank is ru = F − e, the frustration term is δ = elem − e, and the canonical density κ = (h₁ − δ)/V is determined entirely by link-graph balance and connectivity combinatorics. The characteristics 2 and 3 are exceptional and exactly understood (§5): over GF(2) the kernel is elem, over GF(3) it is e + 1.

The generators are not new circuit species. The parity boxes are balanced circuits and the barbell modes are balanceable circuits, both classified in the oriented-hypergraph program of Rusnak and of Rusnak, Li, Xu, Yan and Zhu. What is apparently unstated is the *spanning* statement: no nullity or spanning theorem for hypergraph incidence kernels exists in that program (the unbalanceable circuits are their declared open problem), and our theorem asserts that on the sphenic family the two classified families already span the rational kernel. We prove the reduction unconditionally (cone split plus graded induction), reduce the remaining content to a single finite leakage-gauge condition (LG), and certify (LG) at the perimeter above with a machine-checkable certificate stack. The all-N form is **open**, with the band localization proved and a richness program stated (§7).

---

## 1. The unsigned kernel, and the statement at the certified perimeter

### 1.1 The object

The complex C is as in Paper 1: triangles are the sphenics pqr in (N/2, N], edges are the co-occurring prime pairs, vertices are the primes. The *signed* boundary ∂₂ (the usual alternating one) has rank F − elem by the slab identity of Paper 1. This paper is about the *unsigned* boundary

∂ᵘ [p, q, r] = [q, r] + [p, r] + [p, q] (all coefficients +1),

which is the incidence map of C viewed as an oriented hypergraph with all-positive incidence, equivalently all adjacencies negative in Rusnak's dictionary. Over a field of characteristic ≠ 2 the two boundaries are genuinely different maps, and their nullities differ by the frustration term

δ := ru − rank ∂₂ = (F − e) − (F − elem) = elem − e, where e := dim ker ∂ᵘ, ru := rank ∂ᵘ.

The term δ is the one quantity in the whole coprime-graph arc that has resisted a rank-free closed form (Paper 1, §5). The point of the structure theorem is to express e, hence δ, as a balance count.

### 1.2 The fiber objects

For a vertex v, the *link* L_v is the graph on primes with an edge {x, y} whenever {v, x, y} is a triangle of C. For a prime pair {a, b}, the *common link* L_{a,b} is the graph whose edges g = {x, y} satisfy that both {a, x, y} and {b, x, y} are triangles of C.

Signing every adjacency negative (equivalently, working with the all-positive incidence), the *balance kernel* Z_bal(G) of a graph G is the Zaslavsky even-circle cycle space: the space spanned by the even circles and the odd-circle barbells of G. This is the cycle space of the signed graphic matroid of the all-negative signing of G. For each pair {a, b} and each z ∈ Z_bal(L_{a,b}), the *balance mode* is

m_{a,b,z} = Σ_g z_g ([a ∪ g] − [b ∪ g]),

with g ranging over the edges of L_{a,b}.

### 1.3 The theorem, scoped

> **Structure theorem (unsigned kernel; certified perimeter). [BANKED as C-0746 at the certified perimeter.]** For each of the five bundled complexes N ∈ {50000, 100000, 200000, 300000, 500000}, certified over ℚ and an eight-prime battery at all five N, and over every prime characteristic p ∉ {2, 3} on the two-stage integer-certified subset N ∈ {10⁵, 2×10⁵},
>
> ker ∂ᵘ = span{ m_{a,b,z} : a < b prime, z ∈ Z_bal(L_{a,b}) }.

We state the scope plainly, because it is the honest one. The inclusion ⊇ (the modes are kernel vectors) is an unconditional lemma for all N (§2). The reduction of ⊆ to a finite condition (LG) is unconditional for all N (§3). What is verified rather than proved in general is (LG) itself, and it is verified at the five N above by an exact certificate stack (§4). The characteristic scope matches the certificate inventory exactly: the leakage-gauge two-rank test over an eight-prime battery covers all five N and pins the kernel over ℚ, while the all-characteristic closure (no bad-prime window) is certified by the two-stage integer certificates only on N ∈ {10⁵, 2×10⁵}; we do not claim all characteristics at the three larger N, where those integer certificates are not yet in the repository. The all-N statement is open (§7). We never claim the theorem for all N, and every downstream consequence (e as a balance count, δ = elem − e as a characteristic-2 jump, κ reduced to counting) inherits the certified-perimeter scope.

---

## 2. The proved core: modes are cycles, and the cone split

### 2.1 Lemma A: modes are kernel vectors

> **Lemma A. [PROVED, all N.]** For any prime pair {a, b} and any z with zero unsigned vertex sums on L_{a,b} (that is z ∈ Z_bal(L_{a,b})), the chain m_{a,b,z} satisfies ∂ᵘ m_{a,b,z} = 0.

**Proof.** Examine each facet coefficient of ∂ᵘ m. A facet of the form {x, y} interior to an edge g receives z_g from [a ∪ g] and z_g from [b ∪ g] with the mode's sign difference, so the coefficients cancel. A facet {a, u} receives Σ over edges g of L_{a,b} incident to u of z_g, which is the unsigned vertex sum of z at u, and this is zero by the balance condition. The same holds for facets {b, u}. The facet {a, b} never occurs, because a and b never lie in a common mode cell. Hence ∂ᵘ m = 0. ∎

### 2.2 Lemma B: cone split at the least vertex

Filter the kernel by least vertex. For a vertex v let C_{≥v} be the subcomplex on vertices at least v, and let w ∈ ker ∂ᵘ|_{C_{≥v}} have least vertex v in its support. Split supp(w) = A ⊔ B, where A is the cells containing v and B is the rest. Write w_A for the tail chain of the A-cells (drop the v).

> **Lemma B. [PROVED, all N; audited in advisory mode, support convention explicit, characteristic ≠ 2.]**
>
> (i) w_A has zero unsigned vertex sums on the link L_v restricted to vertices at least v, that is w_A ∈ Z_bal(L_v^{≥v}); this is the v-facet block of ∂ᵘ w = 0.
> (ii) w_A = − ∂ᵘ(u) exactly, where u is the B-part of w; this is the v-free facet block, and both sides are supported on L_v-edges because every off-link facet coefficient of ∂ᵘ u must vanish.
> (iii) If B = ∅ then w = 0.

**Corollary (the realizable space).** Writing W_v for the space of A-parts of kernel vectors of C_{≥v} with least vertex v,

W_v = Z_bal(L_v^{≥v}) ∩ ∂ᵘ(chains of C_{>v}).

The second condition is not decorative: the naive version without it is false, with a measured deficit of 1276 at N = 10⁵. Any proof attempt that ignores the boundary witness is refuted by that counterexample.

### 2.3 Lemma C: graded reduction

> **Lemma C. [PROVED, all N.]** The A-part map identifies the graded quotient K(C_{≥v}) / K(C_{>v}) with W_v, and the modes with a = v have A-parts exactly Σ over b > v of Z_bal(L_{v,b}^{≥v}) ⊆ W_v. Hence, by downward induction on the finitely many least-vertex levels (primes up to roughly N^{1/3}), the structure theorem for C_{≥v} follows from the theorem for C_{>v} together with the

> **Realizable Decomposition Lemma (the crux).** W_v ⊆ Σ over b > v of Z_bal(L_{v,b}^{≥v}), at every level.

In words: every balanced, link-supported boundary of the upper subcomplex splits into pair-fiber balance cycles. Lemmas A, B and C are unconditional. The whole remaining content is the crux, and §3 reduces the crux to a finite gauge condition.

---

## 3. The peeling architecture, with corrected bookkeeping

This section reproduces the elimination proof of the crux under a finite hypothesis (LG). The architecture originated in an AI-assisted solver round briefed by the lab and was independently cold-refereed; see the method note. The essential correction over the lab's earlier attempts is the bookkeeping: one does *not* hold the witness boundary fixed while removing a layer. Instead each peeling step subtracts a certified element q from the current boundary, so the boundary itself changes as h ↦ h − q.

### 3.1 Notation for the filtration

Order vertices by prime value. For a vertex a > v let X_a be the cells all of whose vertices are at least a, and let a⁺ be the next vertex after a. For b ≥ a let L_{v,b}^a be the common link on vertices at least a with b removed, and put T_v^a = Σ over b ≥ a of Z_bal(L_{v,b}^a), so that T_v^{a_0} = T, the target pair-fiber span, where a_0 is the first vertex above v. For the current level a, let L_a be the link of a inside X_a, and set T_a = Σ over c > a of Z_bal(L_{a,c}). For a chain u ∈ C_2(X_a), its a-tail ℓ_a(u) keeps the tail [x, y] of each cell [a, x, y] with least vertex a and sends all other cells to 0.

### 3.2 Mode halves and the leakage tail

For z ∈ Z_bal(L_{v,b}^a), the C'-half of the corresponding full v-mode is R_{v,b}(z) = − Σ over edges g of z_g [b ∪ g], and balance of z gives ∂ᵘ R_{v,b}(z) = − z on the link edges. Summing over b, for a tuple z = (z_b) one gets a chain R(z) with ∂ᵘ R(z) = − q(z), where q(z) = Σ_b z_b ∈ T_v^a. The *leakage-tail map* is β_{v,a}(z) = ℓ_a(R(z)), an explicit linear map into C_1(L_a): the tail edge {x, y} receives − (z_a)_{xy} − (z_x)_{ay} − (z_y)_{ax}, with absent terms read as 0. So adding mode-halves to a witness subtracts a certified q from its boundary and perturbs its a-tail by a controlled leakage vector.

### 3.3 Straddle localization by the window (P1)

Let u ∈ C_2(X_a) with h = ∂ᵘ u ∈ Z_bal(L_v^a) and a-tail t = ℓ_a(u). The imbalance of t at a vertex x equals h_{ax} when {a, x} is a link edge and 0 otherwise, so the imbalance of the a-tail is supported on the straddle set S_{v,a} = { x > a : {a, x} ∈ L_v }, and it sums to zero there because h is balanced. The window supplies the key localization (P1): if a cell {a, x, y} shares the edge {a, x} with a cell {v, a, x}, then their third vertices y and v differ by a factor below 2, so y < 2v. In particular, once a ≥ 2v no straddling contribution can occur, and the a-tail is automatically balanced. This confines the whole difficulty to the factor-2 band a ∈ (v, 2v).

### 3.4 The finite leakage-gauge hypothesis

Let U_{v,a} be the space of a-tails that actually occur, U_{v,a} = { ℓ_a(u) : u ∈ C_2(X_a), ∂ᵘ u supported on and balanced in L_v^a }.

> **Hypothesis (LG)_{v,a}.** For every occurring tail t ∈ U_{v,a} there is a mode-half tuple z with t + β_{v,a}(z) ∈ T_a. Equivalently, in the quotient C_1(L_a) / T_a, the occurring tails lie in the image of the leakage map: overline(U_{v,a}) ⊆ image(overline(β_{v,a})). A stronger link-only sufficient form is C_1(L_a) = image(β_{v,a}) + T_a.

### 3.5 One-step elimination and the induction

> **One-step elimination lemma. [PROVED under (LG)_{v,a}.]** Given u ∈ C_2(X_a) with h = ∂ᵘ u ∈ Z_bal(L_v^a), there exist q ∈ T_v^a and u⁺ ∈ C_2(X_{a⁺}) with ∂ᵘ u⁺ = h − q and h − q ∈ Z_bal(L_v^{a⁺}).

**Proof.** Let t = ℓ_a(u). By (LG)_{v,a} pick z with p := t + β_{v,a}(z) ∈ T_a, and set R = R(z), q = q(z) ∈ T_v^a, so ∂ᵘ R = − q and ℓ_a(R) = β_{v,a}(z). Since internal kernel tails are exactly T_a (an application of Lemma C inside X_a), choose an internal cycle N with ℓ_a(N) = p. Put u⁺ = u + R − N. Then ∂ᵘ u⁺ = h − q, and ℓ_a(u⁺) = t + β_{v,a}(z) − p = 0, so u⁺ has no cell with least vertex a and lies in C_2(X_{a⁺}). Finally h − q is balanced (both h and q are) and, being ∂ᵘ u⁺ with u⁺ free of a, has no edge incident to a, so h − q ∈ Z_bal(L_v^{a⁺}). ∎

Reverse induction on a now proves the filtered statement: if u ∈ C_2(X_a) and ∂ᵘ u = h ∈ Z_bal(L_v^a), then h ∈ T_v^a. The base after the largest vertex is trivial (C_2 is zero, so h = 0); the step is the one-step lemma plus the induction hypothesis applied to h − q. Taking a = a_0 gives W_v ⊆ T, which is the crux, hence the structure theorem, under the (LG) hypotheses. Unwinding the recursion exhibits the corrected bookkeeping explicitly: chains u_0 = u, u_1, ..., u_r = 0 and certified elements q_i ∈ T with ∂ᵘ u_i = h_i and h_{i+1} = h_i − q_i, so that h = q_0 + q_1 + ... + q_{r−1} ∈ T. The witness boundary is not held fixed; each peel subtracts a certified pair-fiber element.

---

## 4. (LG) as a finite condition, and the certificate system

### 4.1 The finite rank form

For fixed a, the hypothesis (LG)_{v,a} is a single rank equality. Let U_a be a matrix whose columns span the occurring tails U_{v,a} (itself a kernel of an explicit two-block boundary matrix), let G_a span the image of the leakage map β_{v,a}, and let H_a span T_a. Then

(LG)_{v,a} holds iff rank[ G_a  H_a  U_a ] = rank[ G_a  H_a ].

This is a machine-checkable equality of ranks of explicit integer matrices, one per level pair (v, a). The band localization of §3.3 confines the nontrivial checks to a ∈ (v, 2v).

### 4.2 The certificate stack

The structure theorem is certified at the five bundled complexes by the following stack. Every entry point runs from the repository root; bundles under `certificates/` are gzipped JSON with SHA-256 manifests.

- **Leakage-gauge rank certificates.** The two-rank test of §4.1 is passed at 616 level pairs across the five N (50000, 100000, 200000, 300000, 500000), integer-exact. **[CERTIFIED.]**
- **Eight-prime battery at emission.** Every claimed rank is confirmed over eight prime characteristics as the certificates are emitted, guarding against a single-characteristic coincidence. **[CERTIFIED.]**
- **Modular sweep.** A 32,868-check sweep over characteristics up to 997 finds no bad prime below 1000: outside {2, 3} every rank matches the generic value on all checked pairs. **[VERIFIED.]**
- **Two-stage integer certificates.** For N ∈ {10⁵, 2×10⁵} (198 pairs), a unit-pivot unimodular reduction followed by an exact Smith normal form of the residual block produces integer invariant factors with no invariant factor divisible by any prime outside {2, 3}. This closes the field story on that subset without a bad-prime window above 1000. At the three larger N the certificates currently cover ℚ and the eight-prime battery, not all characteristics. **[CERTIFIED on N ∈ {10⁵, 2×10⁵}.]**
- **Independent enumeration replay.** A separate program rebuilds every cell inventory from N alone (stdlib only) and reproduces the fiber and generator data, closing the weakest link (a shared enumeration error). **[VERIFIED clean.]**
- **Independent checker replay.** A second implementation, using spanning-tree balance bases and a different elimination order, re-verifies every claimed rank over the eight-prime battery. **[VERIFIED clean.]**

The formal adjudication banked the ℚ plus eight-prime perimeter at N ∈ {10⁵, 2×10⁵} (198 pairs, 1584 rank-pair checks) with the exact integer kernel-membership lower bound and the finite-field nullity upper bound; the five-N, 616-certificate extension is on the same epistemic footing (a theorem modulo a hashed finite certificate, the same shape as the density result of Paper 1). We hold to the certified-perimeter scope in every statement.

### 4.3 The bug that failed loudly (reproducibility)

The independent checker earned its keep. Its first version had a sign error in the barbell balance-closure, and it failed loudly: the checker disagreed with the emitter on 22 of 78 fibers, at all eight primes at once. The fault was in the checker, not in the certificates, and a loud, characteristic-independent disagreement is exactly what an independent replay should produce when something is wrong. The checker was rewritten with a brute-forced sign closure plus a per-component dimension guard (each balance component contributes E − V + [component is bipartite]), after which the emitter, the checker, and the independent enumerator agree on every pair. We report this because a certificate stack whose independent replays never disagree has not really been tested; the loud disagreement is the evidence that the replay is genuinely independent, and the adjudication credited it as such.

---

## 5. Characteristic stratification

The kernel dimension of ∂ᵘ is not field-independent, and the two exceptional characteristics are exactly the ones the oriented-hypergraph taxonomy predicts.

- **Characteristic 2. [PROVED; from C-0744.]** Over GF(2) the unsigned and signed boundaries coincide, so ker ∂ᵘ = ker ∂₂ has dimension elem by the slab identity of Paper 1. The kernel is the fitting-cell space, not the balance-mode space.
- **Characteristic 3. [VERIFIED; CERTIFIED on the perimeter.]** Over GF(3) the kernel dimension is exactly e + 1: precisely one extra class appears, a single cross-theta configuration. This is the all-entrant GF(k) phenomenon of the oriented-hypergraph program: an all-entrant minimal k-cross-theta is minimally dependent only over GF(k), so at k = 3 exactly one such dependency becomes rational over GF(3) and disappears elsewhere. The measured e + 1 is therefore a confirmed prediction of Rusnak's characteristic theory, and we state it as such.
- **Every other characteristic. [CERTIFIED on the perimeter.]** Over ℚ and over every prime outside {2, 3} the kernel dimension is e (two-stage subset; battery-scoped elsewhere), by the certificate stack of §4.

So on the certified set the picture is a clean stratification: GF(2) gives elem, GF(3) gives e + 1, and the generic value e holds everywhere else, with δ = elem − e the characteristic-2 jump.

---

## 6. Positioning in the oriented-hypergraph program

The generators of the kernel are classified circuits; only the spanning statement is ours to claim, and even that is scoped and hedged.

Under the standard dictionary (all-positive incidence corresponds to all-negative adjacency, so a positive circle is an even circle and Zaslavsky balance is evenness), the two mode families are known objects. The parity boxes are *balanced circuits* in the sense of Rusnak, *Oriented Hypergraphs: Introduction and Balance* (Electron. J. Combin. 20(3) (2013) #P48; the arXiv preprint 1210.0943 carries the title *Oriented Hypergraphs I*), whose classification of balanced circuits is the relevant result (cited from the arXiv numbering as Theorem 7.2.7; confirm against the published version before quoting the number). The barbell modes are *balanceable circuits* in the sense of Rusnak, Li, Xu, Yan and Zhu, *Oriented Hypergraphs: Balanceability* (Discrete Math. 345 (2022), arXiv:2005.07722). We cite Lucas J. Rusnak as sole author of the 2013 paper.

What is apparently unstated is the spanning statement. No nullity or spanning theorem exists anywhere in the oriented-hypergraph program: the unbalanceable circuit family is their declared open problem, and no global kernel-dimension formula for hypergraph incidence matrices is known at all. Our theorem, restricted to the sphenic and window family and at the certified perimeter, asserts that the two classified families already span the rational kernel, fibered over vertex-pairs by link balance; equivalently, the unbalanceable circuits are rationally redundant on this family. There is independent structural support from the program's own results: the all-entrant minimal k-cross-thetas are minimally dependent only over GF(k), so the simplest unbalanceable circuits contribute no rational kernel vectors in our all-positive setting, exactly the mechanism visible as the GF(3) stratum of §5. We frame the contribution as an apparently unstated spanning equality over their taxonomy, not as a new circuit theory.

The fiber object is the Zaslavsky even-circle matroid, which suggests a matroid-union reading of e (a union of pair-fiber cycle spaces saturating the kernel) that could yield both a uniform proof and an Euler-characteristic-type formula for e; we note it as a route, not a result. Adjacent but distinct is the Nagel and Reiner complex-of-boxes machinery (Electron. J. Combin. 16(2) (2009) #R3, arXiv:0712.2537), which resolves the associated monomial ideal, a different functor on the same skew objects. The one named residual specialist check for novelty is Duval's relative Laplacian spectral recursion (Electron. J. Combin. 11(2) (2006) #R26, math/0507130): a spectral, characteristic-0 method on shifted pairs whose relationship to our all-characteristic integral kernel should be confirmed by a specialist before any language stronger than "apparently unstated."

---

## 7. The all-N problem, and what is proved toward it

The all-N structure theorem is **open**. The obstruction is precisely a uniform (LG): the finite certificate of §4 confirms the gauge condition at five N, but does not prove it for all N. Two things are proved toward it.

- **Band localization. [PROVED.]** By the window bound (P1) of §3.3, all straddle imbalance lives in the factor-2 band: for a level a ≥ 2v every occurring a-tail is automatically balanced, so the nontrivial gauge condition is confined to partners a ∈ (v, 2v). Above 2v the peeling is straddle-free and unconditional. The all-N difficulty is therefore a band-local statement, not a global one.
- **The richness program. [OPEN, sharply stated.]** What remains is to show the leakage map is surjective onto the occurring band tails uniformly in N, plausibly under an explicit finite richness hypothesis on the band fibers (enough independent even circles and barbells in each L_{v,b} with v < b < 2v to realize every occurring straddle correction). This is a concrete, machine-testable family of conditions; proving it uniformly, or replacing it by a band-local witness-modification argument, would upgrade the theorem from the certified perimeter to all N.

Until then, the honest statement is the one in §1.3: the modes are always kernel vectors, the reduction to (LG) is unconditional, and the equality of the kernel with the mode span is certified at the five bundled N and their non-exceptional characteristics.

---

## 8. Consequences at the certified perimeter

At the certified perimeter, the whole coprime-graph arc becomes counting. The unsigned nullity e is the dimension of a sum of pair-fiber balance spaces, computed by inclusion and exclusion over overlapping pairs; each component's balance dimension is E − V + [component is bipartite], with the non-bipartite fraction growing with scale (measured by the bipartite census at three of the certified N: 0.73, 0.81, 0.88), which confines corrections to the completer fringe. The frustration term δ = elem − e becomes the characteristic-2 jump of a certified quantity, and the canonical density κ = (h₁ − δ)/V is reduced, at these N, to link-graph balance and connectivity combinatorics. Combined with the exact signed profile of Paper 1, this removes the last uncertified rank from the sphenic layer of Banerjee's −1 multiplicity at the perimeter. The transcendence question for κ at infinity remains tied to the all-N richness program of §7.

---

## Appendix. Machine certificates (reproducible)

All scripts run from the repository root (concept DOI 10.5281/zenodo.21135221); the auxiliary paths inside some scripts reflect the lab environment.

- `scripts/mode_completeness.py` (and a 5×10⁵ variant): global completeness, rank of the mode family equals e at N ∈ {5×10⁴, 10⁵, 2×10⁵, 5×10⁵}, values 482, 1270, 3082, 9402.
- `scripts/graded_completeness.py`: the graded crux verified level by level, integer-exact at all accessible least-vertex levels across the bundled complexes.
- `scripts/atomic_space_test.py`: the atomic realizable decomposition at space level, dim W_v equal to the fiber-sum dimension.
- `scripts/lg_rank_test.py`, `scripts/twostage_certify.py`: the (LG) two-rank certificates and the two-stage integer certificates (unit-pivot unimodular reduction plus residual Smith normal form).
- `scripts/lg_replay_check.py`, `scripts/enum_replay.py`: the independent checker replay and the independent enumeration replay.
- `scripts/gauge_anatomy2.py`, `scripts/slab_gf2_sweep.py`: the GF(3) and GF(2) characteristic strata.

## References

- L. J. Rusnak, *Oriented Hypergraphs: Introduction and Balance*, Electron. J. Combin. 20(3) (2013) #P48 (arXiv:1210.0943; the preprint carries the title *Oriented Hypergraphs I*).
- L. J. Rusnak, S. Li, B. Xu, E. Yan, and S. Zhu, *Oriented Hypergraphs: Balanceability*, Discrete Math. 345 (2022), arXiv:2005.07722.
- T. Zaslavsky, *Signed graphs*, Discrete Appl. Math. 4 (1982), no. 1, 47–74.
- A. M. Duval, *A relative Laplacian spectral recursion*, Electron. J. Combin. 11(2) (2006) #R26, math/0507130.
- U. Nagel and V. Reiner, *Betti numbers of monomial ideals and shifted skew shapes*, Electron. J. Combin. 16(2) (2009) #R3, arXiv:0712.2537.
- S. Banerjee, *On Structural Properties and Adjacency Spectrum of Coprime Graph of Integers*, arXiv:2506.10583 (2025).

(References verified against the published record by web search, 2 July 2026; the internal theorem number cited from Rusnak 2013 should still be confirmed against the print version.)

## Method note

All results were developed in an AI-assisted workflow: a Claude working session for construction and hostile self-review, with a GPT-5.5-based adversarial adjudicator for banking rulings, under a protocol in which every claim is attacked by independent implementations, randomized controls, and adversarial review before being recorded. The one-step elimination architecture of §3 originated in a solver round briefed by the lab and was reproduced and independently cold-refereed here. The certificate stack of §4 exists so that no reader need care how the mathematics was produced: the enumeration replay rebuilds the objects from N alone, and the checker replay re-derives every rank by a different algorithm. The independent checker caught a real sign bug before banking, which is recorded in §4.3 as a feature of the protocol.
