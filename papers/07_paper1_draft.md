# Exact prime-count homology of the sphenic window complex

*Working write-up, Improbability Lab, 2 July 2026. Not a submission. Audience: combinatorial and analytic number theorists. Status labels are used throughout and are load-bearing: **[PROVED]**, **[BANKED]** (proved and cleared by the lab's hostile adjudication protocol), **[VERIFIED]** (exact numerics, not a proof), **[KNOWN]** (classical, not ours), **[NOT CLAIMED]**. Registry anchors: C-0743 (BANKING_GRADE, the density constant and the self-contained connectivity certificate), C-0744 (slab identity), C-0745 (top homology); C-0739 is the related edge-support layer-graph lemma. All rational constants below are copied from the banked records and are exact.*

---

## Abstract

Fix a threshold N and let the window be W = (N/2, N]. The *sphenic window complex* K_N is the 2-dimensional simplicial complex whose triangles are the sphenics (squarefree integers p·q·r with three distinct prime factors) lying in W, whose edges are the prime pairs that co-occur in such a triangle, and whose vertices are the primes involved. These complexes arise in connection with S. Banerjee's question on the multiplicity of the eigenvalue −1 of the integer coprime graph (arXiv:2506.10583). We reduce the entire homology of K_N to prime-counting functions, with no linear algebra left in the answer, and we determine an exact rational limiting density.

We prove a purely combinatorial identity (Theorem A): for any finite *slab* R, that is any difference of two order ideals in the coordinatewise order on strictly increasing integer tuples, the dimension of the top boundary-cycle space equals the number of *fitting* cells, those x with the all-ones shift x + (1,...,1) still in R, over every field, with an explicit ±1 integral basis. The sphenic complex is the length-3 slab in the prime-position ruler, so Theorem A gives rank ∂₂ = F − elem exactly (the rs-identity), hence b₁ = (E − F) − V + 1 + elem. A finite-parts cancellation collapses this to a signed sum of fourteen prime counts (Theorem B), whose leading behaviour gives an exact rational density b₁/π(N/6) → 6H − 3/22 = 97360699/1078282205 ≈ 0.0902924 (Theorem C), unconditional on the prime number theorem, Bertrand's postulate, Dusart's explicit prime-gap bounds, and a finite computation. The top Betti number is b₂ = elem = F − D(N/2) + cap for every N, so the full profile is (b₀, b₁, b₂) = (1, h₁, elem) for all N ≥ 154.

We close with an honest negative. The prime counts in Theorem B carry the non-trivial zeros of ζ, and their amplitudes can be read off the fluctuation of b₁. This is exactly the classical explicit-formula duality present in any prime count, and we verify directly that only the prime ruler produces the zeros. We claim **nothing** toward the Riemann hypothesis and no cheaper route to primes or zeros: the construction consumes the primes as input.

---

## 1. The sphenic window complex, and Banerjee's motivation

### 1.1 The object

Fix N. The *window* is W = (N/2, N]. A *sphenic* is a squarefree integer with exactly three distinct prime factors, n = p·q·r with p < q < r. We build a 2-complex K_N as follows:

- the **vertices** are the primes dividing some sphenic in W (to leading order, the primes up to N/6);
- the **triangles**, that is 2-cells, are the sphenics in W, one 2-simplex {p, q, r} for each;
- the **edges** are the prime pairs {p, q} that co-occur in at least one such triangle.

Write V, E, F for the numbers of vertices, edges and triangles. Let ∂₂ be the simplicial boundary of the triangles, with the usual orientation [p, q, r] ↦ [q, r] − [p, r] + [p, q]. The two invariants of interest are the rank of ∂₂ over ℚ and the first Betti number b₁ = E − (V − 1) − rank ∂₂.

### 1.2 Why this complex

Banerjee (2025, arXiv:2506.10583) studies the coprime graph of integers and gives a lower bound on the multiplicity of the eigenvalue −1, leaving the exact value open. That multiplicity decomposes over the squarefree layers of the integers, and the sphenic (three-prime) layer contributes exactly the homological data of K_N: the first Betti number b₁, and a companion count. The present paper is about the structure of that data and the constant it converges to. It pins, exactly and rationally, the signed density underneath Banerjee's error term. It does not, on its own, close the full multiplicity, which additionally requires the unsigned rank and the other odd layers (see §7 and Paper 2).

### 1.3 The result in one paragraph

The first Betti number is governed by a completely non-arithmetic fact about staircase-shaped regions of a lattice (§2). Applied to the sphenic window that fact collapses, after an exact cancellation, into a short signed sum of prime counts (§3 and §4). Dividing by the vertex count and letting N grow gives an exact rational constant (§5). The top Betti number is a single semiprime count away from the same machinery (§6). Finally (§7) we address the tempting appearance that the object "sees" the Riemann zeros and delimit it precisely: it is the ordinary duality and nothing more.

---

## 2. The combinatorial core: the slab identity

### 2.1 Setup

Fix an integer ω ≥ 2. Let P_ω be the set of strictly increasing ω-tuples of positive integers, ordered coordinatewise: x ≤ y iff x_t ≤ y_t for every t. A subset D ⊆ P_ω is a *down-set* (order ideal) if y ∈ D and x ≤ y imply x ∈ D. A **slab** is a difference R = D_hi ∖ D_lo of two down-sets, D_lo ⊆ D_hi. We only ever use finite slabs, and every complex in this paper is finite.

Regard each ω-tuple as an (ω−1)-simplex on its entries {x_1, ..., x_ω}, with the alternating boundary ∂ into the space of (ω−2)-simplices. Restricting to the cells of R gives a chain group and a boundary map ∂ = ∂_{ω−1}. Write δ = (1, 1, ..., 1). Call a cell x ∈ R **fitting** if x + δ ∈ R, and write x ≪ y for strict domination, x_t < y_t for every t.

### 2.2 The theorem

> **Theorem A (slab identity). [PROVED; BANKED as C-0744.]** Fix ω ≥ 2 and let R = D_hi ∖ D_lo be a finite slab in P_ω. Then, over every field,
>
> dim ker ∂|_R = #{ x ∈ R : x + δ ∈ R } = (number of fitting cells).
>
> Moreover ker_ℤ ∂|_R is free with an explicit basis of ±1 vectors (§2.5), and every invariant factor of ∂|_R equals 1, so there is no torsion anywhere in the Smith normal form.

The proof occupies §2.3 to §2.5. It has two ingredients: a domination lemma that gives the rank lower bound (the boundaries of the non-fitting cells are independent), and an explicit family of cycles that gives the matching upper bound (each fitting cell carries a cycle expressible in strictly larger cells). Both ingredients are field-agnostic and integral.

### 2.3 Lemma 1: the Dominated-Pair Lemma

> **Lemma 1 (every ω ≥ 2). [PROVED.]** In the support of any nonzero (ω−1)-cycle z, over any field, there exist cells x ≪ y. Equivalently, a ≪-antichain of cells has linearly independent boundaries.

**Proof, base ω = 2.** A nonzero edge-chain with ∂z = 0 gives every vertex of the support graph signed degree zero, hence degree at least 2, so the support contains a graph cycle C. Let a* be the smallest vertex of C and (a*, p), (a*, q) its two edges on C, with p < q. Walk C from p to q avoiding a*; every vertex on this walk exceeds a*. Since the walk ends at q > p, it contains an edge g = (c, d) (written sorted) with d > p and c > a*. Then (a*, p) ≪ (c, d). ∎

**Proof, induction step ω ≥ 3 (assuming Lemma 1 at ω − 1).** Let z ≠ 0 with ∂z = 0, and let v be the smallest vertex occurring in supp(z). Split supp(z) = A ⊔ B, where A is the cells containing v (necessarily as first coordinate) and B is the rest, whose vertices all exceed v. Write each x ∈ A as v ∗ x′ with tail x′ an increasing (ω−1)-tuple on values above v; the tails are distinct across A. From ∂(v ∗ x′) = [x′] − v ∗ ∂[x′], sort the facets by whether they contain v:

- the v-part gives v ∗ (Σ_A c_x ∂x′) = 0, and v∗ is injective on v-free chains, so w := Σ_A c_x [x′] is a cycle. It is nonzero, since A is nonempty (v occurs), the tails are distinct, and the coefficients c_x are nonzero;
- the v-free part gives Σ_A c_x [x′] + Σ_B c_y ∂y = 0.

Apply Lemma 1 at ω − 1 to w: there are tails e ≪ f in supp(w). Since the coefficient of [f] in w is nonzero, the v-free relation forces the facet f to appear in ∂y for some y ∈ B ∩ supp(z), say y = f ∪ {s} with s ∉ f and s > v.

*Insertion claim: (v, e) ≪ y.* The first coordinate satisfies v < y_1 because every entry of y exceeds v. Let s land at sorted index k of y, so y_j = f_j for j < k, y_k = s, and y_j = f_{j−1} for j > k. For each t in {1, ..., ω−1} compare e_t with y_{t+1}: if t+1 < k then y_{t+1} = f_{t+1} > f_t > e_t; if t+1 = k then y_k = s > f_{k−1} > e_{k−1} = e_t; if t+1 > k then y_{t+1} = f_t > e_t. In every case e_t < y_{t+1}, so (v, e) ≪ y with both cells in supp(z). ∎

Two remarks. First, the step never uses the slab structure: Lemma 1 is the raw antichain statement. Second, the same step with a degenerate base re-proves ω = 2, so the whole lemma is a single induction from a trivial base.

### 2.4 Lemma 2: join modes

> **Lemma 2 (join modes). [PROVED.]** Let x be a fitting cell of the slab R. Partition x into maximal runs of consecutive integers. For a run occupying values a, a+1, ..., b, let its factor be the boundary cycle of the simplex on the value set {a, ..., b+1}, that is the alternating sum of its subsets each obtained by skipping one value. Let J_x be the join of the run factors, with product signs. Then:
>
> 1. J_x is a nonzero cycle: each factor is the boundary of a simplex, hence a cycle in reduced homology, and a join of cycles is a cycle.
> 2. supp(J_x) = { y : x ≤ y ≤ x + δ } exactly, and every such y lies in R by the sandwich argument: y ≤ x + δ ∈ D_hi gives y ∈ D_hi, and y ≥ x ∉ D_lo gives y ∉ D_lo.
> 3. Every coefficient of J_x is ±1, and x is the unique coordinatewise minimum of supp(J_x): any other support cell keeps some run's top value b+1.

Consequently, for any strictly monotone ruler, that is any value function that is a linear extension of the coordinatewise order, every support cell of J_x other than x has strictly larger value, so ∂x lies in the span of { ∂y : y ∈ R, val(y) > val(x) }.

This resolves what looked like a collision obstruction. A fitting cell with x_{t+1} = x_t + 1 somewhere does not carry a full 2^ω box, but the degenerate box is not a failure: it is a join of higher simplex boundaries. For a single collision it is the suspension of a triangle boundary, a 2-sphere on six cells. An earlier lab reading that "signed cube-mode completeness fails" was measuring only the non-degenerate boxes; the missing kernel vectors are exactly these collision joins.

### 2.5 Assembly, and the integral basis

**Non-fitting cells form a ≪-antichain.** If x, y ∈ R are non-fitting and x ≪ y, then x + δ ≤ y ∈ D_hi puts x + δ in D_hi, and x + δ ≥ x ∉ D_lo keeps it out of D_lo, so x + δ ∈ R and x was fitting after all, a contradiction.

**rank ≥ #non-fitting.** A nontrivial dependency among the non-fitting boundaries would be a nonzero cycle supported on a ≪-antichain, contradicting Lemma 1.

**rank ≤ #non-fitting.** Order the cells of R by strictly decreasing ruler value and eliminate columns in that order. When a fitting cell x arrives, Lemma 2 writes ∂x as a ±1 combination of boundaries of strictly larger-value cells, all already processed, so x contributes no new pivot.

Therefore rank = #non-fitting and dim ker = #cells − rank = #fitting. Both lemmas are field-agnostic and the join modes have ±1 coefficients, so the count holds over every field.

For the integral statement, order the cells by any linear extension of the coordinatewise order. For each fitting x, the vector J_x has its least nonzero entry at row x with value ±1 (Lemma 2.3), and distinct fitting cells give distinct pivot rows, so the family { J_x } is in permuted echelon form with unit pivots. This gives independence over every field; saturation of the integer span (eliminate along the ±1 pivots, subtracting integer multiples, terminating at 0); and hence ker_ℤ ∂|_R = ℤ-span{ J_x } is free of rank #fitting. Finally rank_{GF(p)} ∂ = #non-fitting = rank_ℚ ∂ for every prime p, so no invariant factor is divisible by any prime and the Smith normal form is (1, ..., 1, 0, ..., 0). ∎

### 2.6 Placement, and what is classical

The strict-domination order used above is exactly the shifting order x + δ ≤ y of Klivans (*Threshold graphs, shifted complexes, and graphical complexes*, Discrete Math. 2007, math/0703114), which underlies Kalai's algebraic shifting.

**The pure case is Björner–Kalai [KNOWN].** For D_lo = ∅ the complex is shifted (a near-cone), and the Björner–Kalai near-cone theorem gives β_{ω−1} = #{top cells not containing vertex 1}. The bijection x ↦ x − δ carries those top cells onto the fitting cells (x − δ ≤ x lies in D by the down-set property, and (x − δ) + δ = x ∈ D; conversely a fitting y has first coordinate at least 2 after shifting). So for pure down-sets Theorem A is the classical theorem, in one line.

**The slab case is the new content, and it is not relative homology.** The relative top cycles of the pair (D_hi, D_lo) only need boundary supported inside D_lo, whereas our cycles demand boundary zero in the ambient complex, a strictly smaller space. So Duval's relative-shifting inequality (*Algebraic shifting increases relative homology*, math/9809195) does not settle it. The nearest machinery is Nagel and Reiner (*Betti numbers of monomial ideals and shifted skew shapes*, Electron. J. Combin. 16(2) 2009 #R3, arXiv:0712.2537): their Definition 3.4 names exactly our slabs (skew squarefree strongly stable objects in the Gale order), and their complex-of-boxes cells are the same species as our join modes. But their theorems compute the minimal free resolution of the associated monomial ideal, a different functor from the top cycle space of the generators as simplices; their skew results are confined to d = 2, and their general-d skew case is their own open Question 5.1. The honest verdict, recorded in the positioning memo, is that the statement of Theorem A was not located in that literature; the novelty is UNCLEAR pending a specialist, and any external write-up must cite Björner–Kalai (the pure case) and Nagel–Reiner (the box complexes) prominently. A residual specialist check against Duval's relative Laplacian spectral recursion (Electron. J. Combin. 11(2) 2006 #R26, math/0507130) is named as the one remaining place the count could already be implicit.

---

## 3. The sphenic complex as a slab, and the rs-identity

Number the primes p_1 = 2, p_2 = 3, p_3 = 5, ..., and give each prime the coordinate equal to its position i. A sphenic p_i p_j p_k becomes the increasing triple (i, j, k); its value is the product p_i p_j p_k, used only to test window membership. The all-ones shift (i, j, k) ↦ (i+1, j+1, k+1) is exactly "advance each prime to the next prime," p ↦ p⁺. Thus the sphenic complex is the ω = 3 slab in the prime-position ruler, and the fitting condition is p⁺ q⁺ r⁺ ≤ N.

Define the *fitting count* elem(N) = #{ sphenic pqr ∈ W : p⁺ q⁺ r⁺ ≤ N }. Theorem A at ω = 3 reads:

> **rank ∂₂ = F − elem** (the rs-identity). **[PROVED, corollary of Theorem A (C-0744), every N and every window shape.]**

Because rank ∂₂ = F − elem, the first Betti number becomes a pure count with no linear algebra left in it:

> **h₁ := E − (V − 1) − rank ∂₂ = (E − F) − V + 1 + elem.**

We take this expression as the definition of the integer h₁(N). That it equals the topological first Betti number b₁ requires connectivity, so that E − (V − 1) − rank ∂₂ is genuinely b₁ = dim H₁:

> **Connectivity lemma. [PROVED; certified self-contained within the C-0743 BANKING_GRADE packet.]** For all N ≥ 154 the complex K_N is connected, so b₀ = 1 and h₁ = b₁ identically.

The proof is a hub argument through the vertex 2: every prime appearing as a vertex is tied back to the 2-hub through window sphenics whose existence is guaranteed by Bertrand's postulate, Nagura's bound, and Dusart's explicit prime-gap estimates once N ≥ N_c = 154, and the component count c = 1 is then checked exactly at four values of N. This hub argument, the threshold N_c = 154, and its interval certificate were proved self-contained inside the C-0743 BANKING_GRADE packet; the separate edge-support layer-graph lemma is C-0739, a related but distinct result. With connectivity in hand, h₁ = b₁ for all N ≥ 154, so the phrase "prime-count homology" in the title is earned rather than hedged.

---

## 4. An exact prime-count formula for b₁

### 4.1 Ingredients

Two facts are used as input. Both were proved during the exact evaluation of the constant of §5 and both sit inside the banked C-0743 package (independently re-derived by hand, cleared through four hostile adjudication rounds, with a hashed audit script and a formula-free brute-force confirmation at N = 1.05, 1.20, 1.50 ×10⁶).

> **Master identity. [PROVED; VERIFIED exact.]** With B := F − elem,
>
> E − B = π(N/4) + cap − D_E − 1,
>
> where cap and D_E are two explicit correction counts: cap counts the "crossing" triples pqr ≤ N/2 with p⁺ q⁺ r⁺ > N, and D_E is a blocker/isolation pair count. The transcendental semiprime term Q₂(N/2) cancels identically in the derivation, which is why no Mertens-type constant survives.

> **Finite-parts lemma. [PROVED; certificate below.]** For N > N₁ = 1,040,255,
>
> cap = Σ over the ten pairs {(2,3), (2,5), (2,7), (3,5), (3,7), (3,13), (3,19), (3,23), (5,7), (7,13)} of [ π(N/2pq) − π(N/p⁺q⁺) ], plus a constant 10;
>
> D_E = [ π(N/4) − π(N/6) ] + Σ over p ∈ {3, 5, 7} of [ π(N/2p·p⁻) − π(N/p·p⁺) ].

The threshold N₁ comes from a finite family of at most 601 late-crossing triples, dominated by the bound (p⁺/p)(q⁺/q) ≤ 1.98925 < 2 together with Dusart's explicit prime-gap estimates, which certify that the largest such third prime satisfies r < 14,872. The enumerated family's observed maximum is r = 5,591. The certified bound and the observed maximum are distinct numbers and are both kept on the record.

### 4.2 The cancellation

From h₁ = (E − F) − V + 1 + elem = (E − B) − (V − 1) and the master identity,

h₁ = π(N/4) − π(N/6) + cap − D_E.

Insert the finite-parts forms. The leading π(N/4) − π(N/6) cancels the p = 2 term of D_E. Three of the ten cap-pairs, namely (2,3), (3,5), (5,7), cancel term for term against the three blocker terms for p = 3, 5, 7, since the denominators 12 and 15, 30 and 35, 70 and 77 match exactly. Seven cap-pairs and the constant 10 survive:

> **Theorem B. [PROVED, given the §4.1 inputs; VERIFIED independently.]** For all N > 1,040,255,
>
> **h₁(N) = 10 + Σ over (p, q) ∈ 𝒫 of [ π(N/2pq) − π(N/p⁺q⁺) ]**, where 𝒫 = {(2,5), (2,7), (3,7), (3,13), (3,19), (3,23), (7,13)}.

Written out, the fourteen prime counts are

h₁(N) = 10 + π(N/20) − π(N/21) + π(N/28) − π(N/33) + π(N/42) − π(N/55) + π(N/78) − π(N/85) + π(N/114) − π(N/115) + π(N/138) − π(N/145) + π(N/182) − π(N/187).

The constant 10 has a concrete meaning. For each of the ten crossing pairs, the open interval count π(N/2pq) − π(N/p⁺q⁺) drops the single completer sitting on its lower edge, the largest prime at most N/p⁺q⁺, whose successor clears N. Those ten dropped completers are genuine cells. **[VERIFIED 10/10 at N = 2×10⁶ and 5×10⁷.]**

### 4.3 Check

The difference h₁ − (seven-pair sum) equals 10 exactly at nine values of N from 1.105×10⁶ to 1.20×10⁸, with h₁ on the left computed independently as (E − F) − V + 1 + elem from the enumerated complex. The directly evaluated seven-pair sum reproduces the entire oscillation of h₁ to numerical identity. Beyond 1.2×10⁸ the identity is used rather than re-verified against an enumerated complex; the long series of §7 inherit it through the proof.

---

## 5. The limiting density

Each bracket π(N/2pq) − π(N/p⁺q⁺) is asymptotic to N/(log N) · (1/2pq − 1/p⁺q⁺), and V = π(N/6) is asymptotic to N/(6 log N). Dividing and letting N grow:

> **Theorem C. [PROVED, unconditional on PNT + Bertrand + Dusart + a finite computation. BANKED as C-0743, BANKING_GRADE.]**
>
> h₁(N)/V(N) → K := 6H − 3/22 = 97360699/1078282205 = 0.0902924...,
>
> where H is the explicit finite rational H = Σ over the ten crossing pairs of (1/2pq − 1/p⁺q⁺) = 488798363/12939386460.

The limit is positive. Writing K = 6(1/4 − 7/66 + H) − 1, positivity is the inequality H > 1/44, and the three fractions 1/60 + 1/420 + 5/924 already exceed 1/44. Equivalently and more simply, the three cancelled pairs of H sum to exactly 1/44, so K = 6 × (seven-pair sum), a sum of seven positive brackets.

Two remarks. First, no transcendental constant appears. The leading prime-count constant, a Mertens-type term, cancels identically between the pieces of the numerator, which is why K is rational rather than an expression in the Euler-Mascheroni or Mertens constants. Second, K is the density of the signed first Betti number h₁ = b₁, now an identity by C-0744 plus the connectivity certified within the C-0743 packet. The lab separately tracks a canonical density (h₁ − δ)/V ≈ 0.0585, where δ = rank_unsigned ∂₂ − rank_signed ∂₂ is a torsion-like frustration term. That constant is **not** known to be rational, and it is where any remaining transcendence lives (Paper 2 reduces δ to counting at the certified perimeter). These two numbers must not be confused.

---

## 6. The top Betti number, and the full profile

The complex has no 3-cells, so H₂ = ker ∂₂ and b₂ = dim ker ∂₂ = elem by Theorem A directly. What C-0745 adds is a closed form for elem itself, through the advance map.

> **Advance bijection. [PROVED; BANKED as C-0745.]** The next-prime map T ↦ T⁺ = (p⁺, q⁺, r⁺) carries increasing prime triples bijectively onto increasing odd-prime triples (its inverse is the previous-prime map, with a one-line surjectivity argument). The shell count
>
> J(N) := #{ pqr ≤ N : p⁺ q⁺ r⁺ > N } = D(N/2) = #{ odd semiprimes ≤ N/2 } exactly, for every N.

The lower-bound step is one line: p⁺ q⁺ r⁺ > pqr, and a shell triple has pqr > N/2, so its image is an odd semiprime at most N/2, and the bijection matches the counts (recovering, for instance, 168330 at N = 2×10⁶). Splitting at the window edge then gives, with no threshold,

> **rank ∂₂ = D(N/2) − cap, and b₂ = elem = F − D(N/2) + cap, exact for every N.**

Above the finite-parts threshold this inherits the ten-pair π-form of cap, so for N > 1,040,255,

b₂(N) = S(N) − S(N/2) − D(N/2) + 10 + Σ over the ten crossing pairs of [ π(N/2pq) − π(N/p⁺q⁺) ],

where S counts sphenics up to its argument, so F = S(N) − S(N/2). This was verified exact at N ∈ {2×10⁵, 5×10⁵, 1.05×10⁶, 2×10⁶, 5×10⁶, 2×10⁷}; below N₁ the π-form is off by exactly 2, as the finite-parts threshold predicts.

Combining with §3 and §5, the entire homology of the sphenic window complex is a triple of counting functions:

> **Full profile. [PROVED.]** For all N ≥ 154,
>
> (b₀, b₁, b₂) = (1, h₁, elem),
>
> with h₁ = 10 + fourteen prime counts for N > 1,040,255, b₁/V → 6H − 3/22, and b₂ = elem = F − D(N/2) + cap. No linear algebra survives in any of the three numbers.

For Banerjee's problem this is the three-prime layer supplied in closed form: the signed density that his error term skirts is pinned exactly and rationally, and the top count is a semiprime count away from elementary. What the full −1 multiplicity still needs is the unsigned rank (the δ of §5, addressed at the certified perimeter in Paper 2) and the analogous data on the other odd layers.

---

## 7. The spectral shadow, and exactly how far it goes

### 7.1 What is true

Because h₁ is, by Theorem B, a fixed signed combination of prime-counting functions, its fluctuation about the smooth part is, by the classical explicit formula, a sum over the non-trivial zeros ρ of ζ:

h₁(N) − (smooth) = − Σ_ρ M(ρ) · (N^ρ-type term), with M(ρ) = Σ over the fourteen denominators m of ± m^{−ρ}.

The factor M(ρ) is a Dirichlet polynomial in fourteen small integers and is derived with no reference to ζ. Scored against the measured per-zero amplitudes of h₁/V, with data to N = 6×10¹⁰ and the known zeros used only as sampling frequencies (the envelope formula itself stays zero-free), it predicts the relative amplitudes with which individual zeros appear: correlation 0.992 over the first 30 zeros, 0.974 with the dominant first zero removed, matching into the noise floor (γ₂₄ measured 0.026 versus predicted 0.027; γ₃₀ 0.026 versus 0.028). **[VERIFIED.]** Reading zeros directly off the spectrum recovers 11 of them, up to the 18th near γ₁₈ ≈ 72.1, and this is resolution-limited rather than signal-limited: the count grows 6, 9, 11 as the sieve depth grows 3×10⁸, 6×10⁹, 6×10¹⁰. The fluctuation grows no faster than N^{1/2}, with measured exponent 0.44, consistent with and required by the Riemann hypothesis; the fourteen-term combination cancels about 99.6% of the individual prime-count fluctuation, so h₁ is an unusually quiet object.

**The dartboard null. [VERIFIED.]** The 0.992 needs a yardstick, since any signed tuple of small integers whose amplitudes decay with height inflates a raw correlation. Tested against 20,000 loose controls (fourteen random distinct integers in [10, 200], balanced signs) and 20,000 matched controls (seven crossing-style pairs with ratio in [1.005, 1.6]), the true envelope scores 0.998 (0.993 excluding γ₁) against a null median of 0.64 and a null maximum, across all 40,000 draws, of 0.94. With the shared decay stripped out, the null collapses to median about 0.00 (99th percentile 0.43, maximum 0.67) while the true envelope holds 0.992. The true denominators beat every one of 40,000 controls on every scoring. The amplitude channel is specific to the topology-selected denominators, not an artifact of shared decay.

### 7.2 What this is not

All of §7.1 is the ordinary prime-to-zero duality. The zeros are present because h₁ is built from prime counts, and every prime count contains them (Riemann, 1859). Two direct controls make the point.

First, the envelope is blind to the zeros' positions. The value |M(1/2 + it)| at the 30 true zeros averages 0.489; at 5,000 random heights it averages 0.500. The zeros sit at the 48th percentile of M's own values: the geometry weights the zeros but does not locate them.

Second, only the prime ruler throws them. Running the identical slab construction with the plain-integer ruler gives a top spectral peak at the window-beat frequency, not the first zero, while the prime ruler puts the first zero far above everything else. The zeros belong to the primes, not to the geometry.

Consequently we claim **[NOT CLAIMED]** any progress on the Riemann hypothesis, any new bridge between primes and zeros, or any means of computing primes or zeros more cheaply. Computing h₁ requires the primes as input, and nothing is obtained more cheaply than it is supplied. This honest negative is not a caveat bolted on: it is a result, namely that the spectral appearance is exactly the classical duality, prime-specific, position-blind, and (the one new observation) amplitude-specific to the fourteen topology-selected denominators.

---

## 8. Discussion

The self-contained core is the rational density K = 6H − 3/22 for the signed first Betti count (Theorem C) and its exact finite-N form as fourteen prime counts (Theorem B), resting only on PNT, Bertrand, Dusart, and a finite certificate. This is directly relevant to Banerjee's open multiplicity constant: it pins, exactly and rationally, the signed density his error term skirts, and the full profile of §6 supplies the whole three-prime layer as counting functions.

The most broadly interesting piece may be Theorem A itself, a statement with no arithmetic in it. Its pure-down-set case at every ω is classical (Björner–Kalai), and the slab case is a concrete theorem in a well-studied corner of algebraic combinatorics (shifted complexes and skew strongly stable objects). Whether it is already on record there is a question a specialist could settle on sight; the honest current label is "adjacent, apparently unstated."

Three questions for readers. For a combinatorialist: is the slab case of Theorem A new, and does the shifted-complex or Nagel–Reiner framework already contain it or its integral basis? For an analytic number theorist: is the exact rational density, or the fourteen-term identity, of independent interest for coprime-graph spectra, and is the finite-parts certificate airtight? For anyone studying almost-prime counting: h₁ = 10 + fourteen prime counts is an unusually strong cancellation identity, suppressing about 99.6% of the √N fluctuation, and might be a useful worked example.

What is honestly not here is any route to the Riemann hypothesis and any predictor for primes. The appearance of the zeros is the classical duality, verified to be exactly that.

---

## Appendix A. The fourteen denominators

Signed, in order: +20, −21, +28, −33, +42, −55, +78, −85, +114, −115, +138, −145, +182, −187. Each pair (2pq, p⁺q⁺) is a crossing pair with p⁺q⁺ > 2pq, so each bracket counts primes in a thin interval and is non-negative.

## Appendix B. Certificates and data (reproducible)

All entry points run from the repository root; the repository (concept DOI 10.5281/zenodo.21135221) holds the scripts and the certificate bundles under `certificates/` as gzipped JSON with SHA-256 manifests.

- **Slab identity and field-independence.** dim ker over GF(2), GF(3), GF(7), GF(101), GF(2³¹−1) agree (GF(2): `scripts/slab_gf2_sweep.py`, 149 slabs, odd-prime cross-check per slab, 0 mismatches). Verified ω = 2, 3, 4 across many rulers; ω = 5, 7 for the prime case. Proof verification: `scripts/dp_proof_verify.py` (Lemma 1 base and induction, Lemma 2 join modes, end-to-end elimination), all steps clean.
- **Theorem B.** h₁ − seven-pair sum = 10 at N ∈ {1.105, 1.986, 3.569, 6.413, 11.52, 20.71, 37.21, 66.87, 120.2} ×10⁶.
- **Theorem C finite parts.** H = 488798363/12939386460; the D_E constant 7/66 = 1/12 + 1/60 + 1/210 + 1/770 with blockers {2, 3, 5, 7}; K = 97360699/1078282205; late-crossing family at most 601 triples; certified r < 14,872 (Dusart) versus observed maximum r = 5,591; hashed audit script reproduces all certificates plus a formula-free brute-force check at N = 1.05, 1.20, 1.50 ×10⁶. Banked as C-0743 (BANKING_GRADE).
- **Top Betti number.** `scripts/elem_closed_form_verify.py`: b₂ = elem = F − D(N/2) + cap exact at N ∈ {2×10⁵, 5×10⁵, 1.05×10⁶, 2×10⁶, 5×10⁶, 2×10⁷}; the shell identity J(N) = D(N/2) recovers 168330 at N = 2×10⁶. Banked as C-0745.
- **Spectral shadow.** 30-zero envelope correlation 0.992 (0.974 without the first zero); dartboard null over 40,000 controls with the true envelope above all (decay-stripped null median about 0.00 versus true 0.992; `scripts/envelope_dartboard.py`); position-blindness control 0.489 versus 0.500; ruler control (primes versus integers versus random); growth exponent 0.44.

## References

- S. Banerjee, *On Structural Properties and Adjacency Spectrum of Coprime Graph of Integers*, arXiv:2506.10583 (2025).
- A. Björner and G. Kalai, *An extended Euler-Poincaré theorem*, Acta Math. 161 (1988), 279–303.
- A. Duval, *Algebraic shifting increases relative homology*, math/9809195, Discrete Math. (2000).
- A. Duval, *A relative Laplacian spectral recursion*, Electron. J. Combin. 11(2) (2006) #R26, math/0507130.
- C. Klivans, *Threshold graphs, shifted complexes, and graphical complexes*, Discrete Math. (2007), math/0703114.
- U. Nagel and V. Reiner, *Betti numbers of monomial ideals and shifted skew shapes*, Electron. J. Combin. 16(2) (2009) #R3, arXiv:0712.2537.
- P. Dusart, explicit estimates for prime-counting and prime gaps.

## Method note

All results were developed in an AI-assisted workflow (a Claude working session with a GPT-5.5-based adversarial adjudicator) under a hostile-verification protocol: every claim was attacked by independent implementations, randomized controls, and adversarial review before being recorded. The certificates in the repository exist so that no reader need care how the mathematics was produced; the verification entry points run from the repository root.
