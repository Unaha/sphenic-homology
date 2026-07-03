# PROOF DRAFT: the slab identity at every ω (Dominated-Pair Lemma closed, join modes close the other side)

*Improbability Lab, 1 July 2026, late evening. STATUS: **BANKED as C-0744** (Lee's go given; Addy-pro two rounds: v1 CONDITIONAL with three demands, all met; v2 BANKED, high confidence, "the finite-slab theorem is proved on the submitted record", RULING_slab-dp-proof-v2_20260701T205900Z). The Tier-2 packet then also ruled **BANKED** (RULING_c0743-tier2-promotion_20260701T210545Z): rank ∂₂ = F − elem at every N, b₁ = h₁ identically (with C-0739 connectivity), so 6H − 3/22 is the topological signed Betti density, unconditional. Novelty framing per Addy: adjacent to Björner–Kalai and Nagel–Reiner, NOT claimed as a new theorem pending specialist positioning. Upgrade path to BANKING_GRADE: self-contained dependency packet + specialist referee.*

---

## 0. Statement

**Theorem A (slab identity, finite form; scope per Addy round 1).** Fix ω ≥ 2. Let P_ω be the poset of strictly increasing ω-tuples of positive integers under the coordinatewise order. Let R = D_hi ∖ D_lo be a **finite** slab (a difference of down-sets, D_lo ⊆ D_hi, with R finite). View each tuple as an (ω−1)-simplex on its entries, with the alternating boundary ∂ into the full space of (ω−2)-simplices. Write δ = (1,…,1), and call x ∈ R fitting if x + δ ∈ R. Then, over every field,

dim ker ∂|_R = #{x ∈ R : x + δ ∈ R}.

Moreover ker_ℤ ∂|_R is free with an explicit basis of ±1-vectors (§2b), and all invariant factors of ∂|_R equal 1 (no torsion anywhere in the Smith form).

Scope remarks. Every complex the lab uses (the sphenic slab at any N, any windowed ruler slab) is finite, so finiteness costs nothing here. Lemma 1 below holds with no finiteness assumption (cycles have finite support); only the counting assembly (§2) uses |R| < ∞. For infinite slabs the identity should hold in a direct-limit sense, but the fitting condition does not localize naively to truncations (the truncation gotcha of §7), so we do not claim it.

Write x ≪ y for strict domination: x_t < y_t for every t.

## 1. The two lemmas

### Lemma 1 (Dominated-Pair Lemma, every ω ≥ 2)

*In the support of any nonzero (ω−1)-cycle z (any finite chain of increasing ω-tuples with ∂z = 0, over any field) there exist cells x ≪ y. Equivalently: a ≪-antichain of cells has linearly independent boundaries.*

**Proof, base ω = 2.** A nonzero edge-chain with ∂z = 0 gives every vertex of the support graph signed degree zero, hence degree ≥ 2, so the support contains a graph cycle C. Let a* be the smallest vertex of C and (a*, p), (a*, q) its two edges there, p < q. Walk C from p to q avoiding a*; every vertex on this walk exceeds a*. Since the walk ends at q > p, it contains an edge g = (c, d) (sorted) with d > p, and c > a* holds for every walk vertex. Then (a*, p) ≪ (c, d). ∎

**Proof, induction step ω ≥ 3 (assuming the lemma at ω − 1).** Let z ≠ 0, ∂z = 0, and let v be the smallest vertex occurring in supp(z). Split supp(z) = A ⊔ B, where A = cells containing v (necessarily as first coordinate) and B = the rest (whose vertices all exceed v, since v is the global minimum and they omit v). Write each x ∈ A as v ∗ x′ with tail x′ an increasing (ω−1)-tuple on values > v; the tails are distinct across A. Using ∂(v ∗ x′) = [x′] − v ∗ ∂[x′] and sorting facets by whether they contain v:

- v-part: v ∗ (Σ_A c_x ∂x′) = 0, and v∗ is injective on v-free chains, so **w := Σ_A c_x [x′] is a cycle**. It is nonzero: A ≠ ∅ (v occurs), the tails are distinct, the c_x are nonzero. (If B were empty the v-free part below would force w = 0, hence z = 0; so B ≠ ∅.)
- v-free part: **Σ_A c_x [x′] + Σ_B c_y ∂y = 0** (B-cells contribute no v-facets, tails contain no v).

Apply the lemma at ω − 1 to w: there are tails e ≪ f in supp(w). Since the coefficient of [f] in w is nonzero, the v-free relation forces the facet f to appear in ∂y for some y ∈ B ∩ supp(z), i.e. **some y ∈ supp(z) with f ⊂ y**, say y = f ∪ {s}, s ∉ f, s > v.

**Insertion claim: (v, e) ≪ y.** First coordinate: v < y_1 since all of y's entries exceed v. Let s land at index k of the sorted y, so y_j = f_j for j < k, y_k = s, y_j = f_{j−1} for j > k. For each t ∈ {1,…,ω−1} compare e_t with y_{t+1}: if t+1 < k then y_{t+1} = f_{t+1} > f_t > e_t; if t+1 = k then y_k = s > f_{k−1} > e_{k−1} = e_t; if t+1 > k then y_{t+1} = f_t > e_t. In every case e_t < y_{t+1}. So (v, e) ≪ y with both cells in supp(z): supp(z) contains a dominated pair. ∎

Two remarks. (a) The step never uses a slab: Lemma 1 is the raw antichain statement, as conjectured. (b) The same step with a degenerate base also re-proves ω = 2: the tails are single vertices, the v-part forces Σ_A c_x = 0, hence |A| ≥ 2, giving tails p < q (which is e ≪ f in one coordinate), and the insertion claim runs verbatim; so the whole lemma is one induction from a trivial base.

### Lemma 2 (join modes: every fitting cell carries an explicit cycle)

*Let x be fitting in the slab R. Partition x into maximal runs of consecutive integers. For a run occupying coordinates with values a, a+1, …, b, let its factor be the boundary cycle of the simplex on the value set {a, …, b+1} (the alternating sum of its (b−a+1)-subsets, each obtained by skipping one value). Let J_x be the join (concatenation, values across runs being disjoint and increasing) of the run factors, with product signs. Then:*

1. J_x is a nonzero cycle: each factor is the boundary of a simplex, a cycle in reduced homology, and a join of cycles is a cycle.
2. supp(J_x) = {y ∈ P_ω : x ≤ y ≤ x+δ} exactly (in each run, choose which value to skip), and every such y lies in R by the sandwich argument: y ≤ x+δ ∈ D_hi gives y ∈ D_hi; y ≥ x ∉ D_lo gives y ∉ D_lo.
3. The coefficient of x in J_x is ±1 (x = skip the top value in every run), all coefficients are ±1, and x is the unique coordinatewise minimum of the support: any other support cell keeps some run's top value b+1 and is ≥ x with strict inequality somewhere.

*Consequently, for any strictly monotone ruler (any linear extension of the coordinatewise order by a value function), every support cell of J_x other than x has strictly larger value, and ∂x lies in the span of {∂y : y ∈ R, val(y) > val(x)}.*

This is the resolution of the "collision wall": a colliding fitting cell (x_{t+1} = x_t + 1 somewhere) does not have a full 2^ω box, but the degenerate box is not a failure, it is a join of higher simplex boundaries (for one collision, the suspension of a triangle boundary, a 2-sphere on 6 cells). The 30 Jun "signed cube-mode completeness FAILS" observation was measuring the non-degenerate boxes only; the missing kernel vectors are exactly these collision joins.

## 2. Assembly of Theorem A

- **Non-fitting cells form a ≪-antichain.** If x, y ∈ R are non-fitting and x ≪ y, then x + δ ≤ y ∈ D_hi puts x + δ in D_hi, and x + δ ≥ x ∉ D_lo keeps it out of D_lo (down-set), so x + δ ∈ R and x was fitting. Contradiction. (Stronger: a non-fitting cell is ≪-below no cell of R.)
- **rank ≥ #non-fitting.** A nontrivial dependency among the non-fitting boundaries is a nonzero cycle supported on a ≪-antichain, contradicting Lemma 1.
- **rank ≤ #non-fitting.** Order the cells of R by strictly decreasing ruler value (any strictly monotone value function; ties broken arbitrarily, noting Lemma 2 needs only the strict comparisons it provides). Eliminate columns in this order. When a fitting cell x arrives, Lemma 2 writes ∂x as a ±1-combination of boundaries of cells with strictly larger value, all already processed, so x contributes no pivot. Hence rank ≤ #non-fitting.
- Therefore rank = #non-fitting and dim ker = #cells − rank = #fitting. Both lemmas are field-agnostic and the join modes have ±1 coefficients, so the count holds over every field. ∎

## 2b. The ℤ-basis and torsion-freeness, explicitly (added for Addy round 2)

Order the cells of R by any linear extension ⊴ of the coordinatewise order. For each fitting x, the column vector J_x ∈ ℤ^R has its ⊴-least nonzero entry at row x (x is the unique coordinatewise minimum of supp(J_x), Lemma 2.3, hence ⊴-least in its support), and that entry is ±1. Distinct fitting cells give distinct pivot rows. So the family {J_x : x fitting} is in permuted echelon form with ±1 pivots. Consequences:

1. **Independence over every field** (echelon with unit pivots).
2. **Saturation.** Let L = ℤ-span{J_x} ⊆ ℤ^R. If an integer vector u lies in ℚ ⊗ L, eliminate along the pivots in ⊴-order: each step subtracts an integer multiple of some J_x (the pivot entries are ±1, so the required multiplier is the integer entry of u at the pivot row), and terminates at 0. Hence u ∈ L: L is a saturated (primitive) sublattice of rank #fit.
3. **L = ker_ℤ ∂|_R.** ker_ℤ is saturated of rank dim_ℚ ker = #fit (by §2); L ⊆ ker_ℤ is saturated of the same rank; a saturated sublattice of full rank in a saturated lattice is the lattice. So ker_ℤ is free with basis {J_x}.
4. **All invariant factors of ∂|_R are 1.** rank_{GF(p)} ∂ = #non-fitting = rank_ℚ ∂ for every prime p (§2 is field-agnostic), so no invariant factor is divisible by any p; the Smith normal form is (1,…,1,0,…,0). In particular ∂ contributes no torsion to any homology of any chain complex containing it. ∎

## 3. Consequences

1. **rs-identity is a theorem** (modulo hostile review): the sphenic complex is the ω = 3 slab with the prime ruler (write-up §3), so rank ∂₂ = F − elem for every N and every window shape (N/f, N], and likewise at every ω. The next-prime advance is the shift x ↦ x+δ in prime-position coordinates.
2. **C-0743 Tier-2 promotion candidate:** h₁ = (E−F) − V + 1 + elem equals the first Betti number b₁, so K = 6H − 3/22 = 97360699/1078282205 is the exact rational limiting density of the honest topological b₁/V. The write-up's title no longer over-claims.
3. **Placement, with the documented prior-art pass (Addy round 2 requirement).** Items pulled and compared 1 Jul evening:
   - **Björner–Kalai (near-cones, 1988):** covers exactly the pure case D_lo = ∅, via β_{ω−1} = #{top cells avoiding vertex 1} and the bijection x ↦ x−δ. Classical; cited as such.
   - **Klivans (thesis; *Threshold graphs, shifted complexes, and graphical complexes*, Discrete Math 2007, math/0703114):** establishes the P_s shifting order and structural theory of shifted complexes; does not state the slab identity.
   - **Duval (*Algebraic shifting increases relative homology*, math/9809195, Discrete Math 2000):** the nearest relative-pair result; an inequality, not an equality, and about relative homology, which our object is not (relative top cycles need boundary only inside D_lo; ours need boundary zero in the ambient complex; ours is a strictly smaller space).
   - **Nagel–Reiner (*Betti numbers of monomial ideals and shifted skew shapes*, Electron. J. Combin. 16(2) 2009, arXiv:0712.2537):** the closest machinery found. They build cellular minimal resolutions for (squarefree) strongly stable ideals generated in fixed degree, supported on a "complex of boxes", and prove field-independent combinatorial Betti formulas for shifted-skew-shape ideals. Their boxes are the same species as our join modes. However their statements concern minimal free resolutions of the associated ideals, not the cycle space of the top simplicial boundary restricted to a slab, and we did not find Theorem A stated there or in works citing it.
   - **Eliahou–Kervaire (stable ideals) and Aramova–Herzog–Hibi (squarefree stable):** explicit resolutions with facet-counting Betti numbers; same family of counts, different object.
   Honest verdict: the statement of Theorem A was not located; the box technology overlaps Nagel–Reiner; novelty is UNCLEAR pending a specialist, and any external write-up must cite Björner–Kalai (pure case) and Nagel–Reiner (box complexes) prominently. Lemma 1 in raw antichain form may be of independent interest regardless.
4. Banerjee: with Tier-2 promoted, what remains for the exact −1 multiplicity is the companion b₂ count (the parked Hardy–Littlewood sequel) and δ.

## 4. What was NOT proved tonight

The canonical κ∞ = (h₁ − δ)/V ≈ 0.0585 stays open (all remaining transcendence lives in (δ/V)∞); nothing here touches the zeros' positions (the Oracle wall stands exactly as the write-up's §6 states it); and this document is a draft pending Lee's review and a hostile adjudication round when Lee un-benches Addy.

## 5. Where the proof came from (honest provenance)

The reduction (antichain of non-fitting cells, split into two inequalities) and the ω = 2 laminar lemma are the lab's, from 30 Jun. The literature anchor (Björner–Kalai for the pure case) came out of tonight's sweep and suggested the cone split at the minimum vertex. The new ingredients are: (i) using the deletion relation to force a B-cell to cover the dominating tail f, (ii) the insertion argument showing coverage forces domination, and (iii) reading the degenerate boxes as joins of simplex boundaries. Nothing else is imported.

## 6. Hostile self-review (attack surface for the eventual adjudication)

- The v-part/v-free-part separation and the injectivity of v∗: machine-checked implicitly by Step 4 below; hand-checked twice.
- Reduced vs unreduced bookkeeping at the degenerate base: the presented base ω = 2 is a direct graph argument, no reduced homology needed.
- Tie-breaking in the elimination: Lemma 2 gives strict value inequalities, ties between other cells are harmless (the argument never compares them).
- Lemma 2 sign bookkeeping (product signs under concatenation): machine-checked on 3,000 collision-rich cells, ω = 2..6 (Step 3).
- The covering step needs only the existence of one y ⊇ f with nonzero contribution; cancellation among several such y cannot erase the coefficient of [f] in Σ_B c_y ∂y, because it must equal −(coeff of f in w) ≠ 0. If EVERY y ⊇ f had cancelling signs the coefficient would be zero, contradiction, so at least one y ∈ supp(z).
- Adversarial question for a referee: does the induction secretly require the vertex set to be well-ordered with a minimum (yes, and finiteness of supp(z) provides it); any issue with infinite slabs (no: cycles have finite support).

## 7. Verification log (all on the box, 1 Jul evening)

- `/lab/scripts/dp_proof_verify.py` (job dpverify): Step 1 base case, exhaustive 2,429 antichain edge-sets (V ≤ 8, k ≤ 6) plus 200,000 randomized: 0 cycles. Step 2 insertion lemma: 200,000 random (e ≪ f, s) instances: 0 violations. Step 3 join modes: 3,000 collision-rich cells, ω = 2..6: all cycles, all supported exactly on [x, x+δ], coefficient ±1 at x, x the unique min: 0 failures. Step 4 end-to-end shadow: 64 generic slabs, 4 rulers, ω = 3,4, decreasing-value elimination pivots exactly the non-fitting cells: 0 failures. VERDICT: ALL FOUR STEPS CLEAN.
- `/lab/scripts/slab_gf2_sweep.py` (job gf2sweep2): the identity over GF(2) with odd-prime cross-check, 149 slabs, 4 rulers, ω = 2..5: 0 mismatches (consistent with the ℤ-freeness the proof now predicts).
- Prior standing evidence: identity exact on thousands of slabs, ω = 2,3,4 all rulers, ω = 5,7 prime; morse_verify.py per-cell free ⟺ fit at the prime ruler; 5,933 ω = 2 regions.
