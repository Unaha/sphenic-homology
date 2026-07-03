# A prime-free slab identity, an exact prime-count formula for the first Betti number of the sphenic complex, and its limiting density

*Working write-up v2, Improbability Lab, 1 July 2026. Not a submission. Status labels are used throughout: **[PROVED]**, **[VERIFIED]** (exact numerics, not a proof), **[CONJECTURED]**, **[KNOWN]** (classical / not ours), **[NOT CLAIMED]*.*

*v2 changes (1 Jul evening audit): §4.1 inputs relabelled PROVED (they are inside the banked, Addy-v4-cleared C-0743 Tier-1 package; v1 undersold them, which made Theorem C's label self-contradicting); Dusart added to Theorem C's dependency list; the b₁ claim hedged in the abstract (Tier-2 is conjectural); §6 correlation numbers made consistent (0.992/0.974); observed max r = 5,591 distinguished from the certified bound r < 14,872; GF(2) added to the field sweep (149/149, no 2-torsion); the pure down-set case of Theorem A identified as classical Björner–Kalai; a dartboard null added for the envelope correlation (true envelope beats all 40,000 random envelopes). Date corrected from 2 July.*

---

## Abstract

We study finite 2-dimensional complexes built from the squarefree three-prime integers ("sphenics") lying in a dyadic window (N/2, N], objects that arise in connection with S. Banerjee's question on the multiplicity of the eigenvalue −1 of the integer coprime graph. We report three linked results and one honest negative.

1. **A purely combinatorial identity.** For a *slab* R (the set-difference of two order ideals) in the coordinatewise order on strictly increasing integer tuples, the dimension of the top boundary-cycle space of the associated simplicial chain complex equals the number of *fitting* cells, those whose all-ones diagonal shift x ↦ x+(1,…,1) again lies in R. The statement contains no arithmetic: primes are merely one choice of "ruler." We prove it for tuples of length 2 and reduce the general case to a single boundary-rigidity lemma living in the shifted-complex order of Klivans and Kalai. For a pure order ideal (empty lower ideal) the identity is classical, Björner–Kalai's near-cone theorem (§2.3); the slab case is the new content.

2. **An exact prime-count formula.** Specialised to the sphenic complex, the identity gives, for all N > 1,040,255, an exact closed form as a signed sum of fourteen prime-counting values for h₁ := (E−F)−V+1+elem, which equals the first Betti number b₁ identically (Theorem A at ω = 3, proved and banked 1 Jul night as C-0744, plus connectivity C-0739):
   h₁(N) = 10 + Σ over seven pairs (p,q) of [ π(N/2pq) − π(N/p⁺q⁺) ].

3. **An exact limiting density.** Consequently h₁(N)/π(N/6) → 6H − 3/22 = 97360699/1078282205 ≈ 0.0902924, an exact positive rational, unconditionally (on the prime number theorem, Bertrand's postulate, Dusart's explicit prime-gap bounds, and a finite computation).

**The honest negative.** These prime counts "carry" the non-trivial zeros of ζ, and one can read a great many of them out of the fluctuation of h₁. This is nothing more than the classical explicit-formula duality, present in *any* prime count; we verify directly that the plain-integer and random rulers do **not** produce the zeros, only the prime ruler does. **[NOT CLAIMED]** anything toward the Riemann hypothesis, and **[NOT CLAIMED]** any faster route to primes or zeros: the construction consumes the primes as input.

---

## 1. Introduction

### 1.1 The object

Fix N. Let the *window* be W = (N/2, N]. A *sphenic* is a squarefree integer with exactly three distinct prime factors, n = p·q·r with p<q<r. Build a 2-complex K_N:

- **vertices** = primes dividing some sphenic in W (to leading order the primes up to N/6);
- **triangles (2-cells)** = the sphenics in W, one 2-simplex {p,q,r} each;
- **edges** = the prime pairs {p,q} that co-occur in at least one such triangle.

Write V, E, F for the numbers of vertices, edges, triangles. Let ∂₂ be the simplicial boundary of the triangles (each oriented [p,q,r] ↦ [q,r] − [p,r] + [p,q]). The two quantities of interest are the ranks of ∂₂ over ℚ, and the first Betti number b₁ = E − (V−1) − rank ∂₂.

This complex was isolated because b₁, and a companion count, control the exact multiplicity of the eigenvalue −1 in the integer coprime graph, which S. Banerjee (2025, arXiv:2506.10583) computes up to an error term he leaves open. The present note is about the structure of b₁ and the constant it converges to.

### 1.2 What is here, in one paragraph

The first Betti number turns out to be governed by a completely non-arithmetic fact about staircase-shaped regions of a lattice (§2). Applied to the sphenic window that fact collapses, after an exact cancellation, into a short signed sum of prime counts (§3–4). Dividing by the vertex count and letting N → ∞ gives an exact rational constant (§5). Finally (§6) we address the tempting appearance that the object "sees" the Riemann zeros, and delimit it precisely: it is the ordinary duality and nothing more.

---

## 2. The combinatorial core: a slab identity

### 2.1 Setup

Fix an integer ω ≥ 2. Let P_ω be the set of strictly increasing ω-tuples of positive integers, ordered coordinatewise: x ≤ y iff x_t ≤ y_t for every t. A subset D ⊆ P_ω is a *down-set* (order ideal) if y ∈ D and x ≤ y imply x ∈ D. A **slab** is a difference R = D_hi ∖ D_lo of two down-sets, D_lo ⊆ D_hi.

Regard each ω-tuple as an (ω−1)-simplex on the vertex set {x_1,…,x_ω}, with the alternating boundary ∂. Restricting to the cells of R gives a chain group and a boundary map ∂ = ∂_{ω−1}. Let δ = (1,1,…,1). Call a cell x ∈ R **fitting** if x + δ ∈ R.

### 2.2 The identity

> **Theorem A [PROVED for finite slabs at every ω — 1 Jul night, banked as C-0744 after a two-round hostile adjudication; see proof_draft_slab_identity_all_omega_01JUL2026.md].**
> dim ker ∂_{ω−1}(R) = #{ x ∈ R : x + δ ∈ R } = (number of fitting cells).
>
> (The status notes below this box are the pre-proof evidence trail, retained for the record.)

**Evidence and status.**

- The identity holds over every field tried: GF(2), GF(3), GF(7), GF(101), GF(2³¹−1). The GF(2) case was added 1 Jul evening (149 slabs, 4 rulers, ω = 2,3,4,5, with an odd-prime cross-check per slab, zero mismatches); characteristic 2 is the torsion that actually occurs in simplicial homology, so its absence makes the torsion-free reading solid. The kernel dimension is field-independent and the associated homology is torsion-free. On the real sphenic complex, rank over GF(2) = rank over ℚ to the integer (verified 30 Jun). **[VERIFIED]** (Reproduction note: on a truncated universe, coordinates ≤ n_max, the region is R ∩ box, itself a slab, and the fitting test must respect the truncation; testing the untruncated fitting condition against the truncated kernel produces spurious mismatches.)
- It holds for *every* ruler used to build the slab: primes-multiplicative, additive (values x_1+x_2+x_3 in a band), arbitrary increasing weights, and the deliberately meaningless weighting x_1+2x_2+4x_3. It fails precisely for non-slabs (regions that are not a difference of down-sets). Hence the content is pure order theory. **[VERIFIED]**
- **ω = 2 [PROVED].** If a cell (edge) x is non-fitting then x+δ is dominated by no cell of R (else, R being sandwiched below a down-set, x would be fitting). This forces the non-fitting edges to be *crossing-free* (no two of them (a,b),(a′,b′) with a<a′ and b<b′), hence laminar, hence a forest; a forest has independent boundaries, so the cycle space is spanned by the fitting cells. Verified on 5,933 slabs with zero exceptions, consistent with the proof.
- **ω ≥ 3 [CONJECTURED, reduced].** The statement reduces to one lemma. Split the cells into fitting and non-fitting. (i) The fitting cells contribute nothing to the rank; (ii) the boundaries of the non-fitting cells are linearly independent, equivalently *every non-zero (ω−1)-cycle has a fitting cell in its support*. Part (ii) reduces to the
  > **Dominated-Pair Lemma [CONJECTURED; VERIFIED].** In the support of any non-zero (ω−1)-cycle there are two cells x, y with x_t < y_t for every coordinate t (a strictly dominated pair). Equivalently, a set of cells that is an antichain for the strict-domination order has linearly independent boundaries.
  Verified on 4,000+ cycles at ω = 3 and 4 with no exception; a sharpened form ("the lexicographically largest cell of a cycle's support dominates another support cell") verified 19,992/19,992.

### 2.3 Placement, and what is classical

The strict-domination order used above is exactly the order "x + (1,…,1) ≤ y", which is the P_s shifting order of Klivans (*Threshold graphs, shifted complexes, and graphical complexes*) and underlies Kalai's algebraic shifting.

**The pure case is Björner–Kalai [KNOWN].** For D_lo = ∅ the down-closure of a down-set's top cells is a shifted complex, and Björner–Kalai's near-cone theorem gives: the complex is a wedge of spheres and β_{ω−1} = #{top cells not containing vertex 1}. The map x ↦ x−δ is a bijection from top cells with x₁ ≥ 2 onto fitting cells (x−δ ≤ x lies in D by the down-set property and (x−δ)+δ = x ∈ D; conversely y fitting gives y+δ with first coordinate ≥ 2). So for pure down-sets Theorem A *is* the classical theorem, in one line.

**The slab case is the new content, and it is not relative homology.** The relative top cycles of the pair (D_hi, D_lo) only need boundary supported inside D_lo; our cycle space demands boundary zero in the ambient complex, a strictly smaller space, so Duval's relative-shifting results (math/9809195) do not settle it. The consistency structure implied by Theorem A plus Björner–Kalai is: Z(D_hi) = Z(D_lo) ⊕ Z(R) ⊕ (a straddling space of dimension exactly #{x ∈ D_lo : x+δ ∈ R}). In this language the missing step remains an acyclic discrete-Morse matching certified by a linear extension; a specialist referee is exactly who could confirm whether it is already a theorem there. A targeted literature pass (1 Jul) found the near-cone machinery and the relative-shifting inequality but no statement of the slab identity itself.

---

## 3. The sphenic complex as a slab

Number the primes p_1 = 2, p_2 = 3, p_3 = 5, …, and give each prime the **coordinate equal to its position** i. A sphenic p_i p_j p_k becomes the increasing triple (i,j,k); its "value" is the product p_i p_j p_k, used only to test window membership. The all-ones shift (i,j,k) ↦ (i+1,j+1,k+1) is exactly "advance each prime to the next prime," p ↦ p⁺. Thus the sphenic complex is the ω = 3 slab with the prime ruler, and the fitting condition is p⁺q⁺r⁺ ≤ N.

Define the *fitting count* elem(N) = #{ sphenic pqr ∈ W : p⁺q⁺r⁺ ≤ N }. Theorem A at ω = 3 reads

> **rank ∂₂ = F − elem** (the "rs-identity"). **[PROVED — corollary of Theorem A (C-0744), every ω, every finite window; the ω = 2,3,4,5,7 exact verifications are now supplementary.]**

Because rank ∂₂ = F − elem, the first Betti number becomes a pure count with no linear algebra left in it:

> **h₁ = E − (V−1) − rank ∂₂ = (E − F) − V + 1 + elem.**

We take this last expression as the *definition* of the integer h₁(N) from here on; that it equals the Betti number b₁ is Theorem A at ω = 3 plus connectivity (C-0739), and is now PROVED (Tier-2 promotion ruling, 1 Jul night): **h₁ = b₁ identically, at every N.** The title of this write-up is now earned, not hedged.

---

## 4. An exact prime-count formula for h₁

### 4.1 Ingredients (established)

Two facts are used as input. Both were proved during the exact evaluation of the constant of §5 and both sit inside the banked C-0743 Tier-1 package (independently re-derived by hand 1 Jul morning; four hostile adjudication rounds, cleared v4 "no surviving defect in Tier-1 scope"; reproducible audit script SHA-256 ed1e8bb7…, formula-free brute-force confirmation at N = 1.05, 1.20, 1.50 ×10⁶; derivation doc RIGOROUS_finite_parts_kappa_inf_01JUL2026.md):

- **Master identity [PROVED; VERIFIED exact].** With B := F − elem, E − B = π(N/4) + cap − D_E − 1, where cap and D_E are two explicit correction counts (cap = "crossing" triples pqr ≤ N/2 with p⁺q⁺r⁺ > N; D_E = a "blocker/isolation" pair count). The transcendental semiprime term Q₂(N/2) cancels identically in the derivation, which is why no Mertens-type constant survives.
- **Finite-parts lemma [PROVED; certificate below].** For N > N₁ = 1,040,255,
  - cap = Σ over the ten pairs {(2,3),(2,5),(2,7),(3,5),(3,7),(3,13),(3,19),(3,23),(5,7),(7,13)} of [π(N/2pq) − π(N/p⁺q⁺)], plus a constant 10;
  - D_E = [π(N/4) − π(N/6)] + Σ over p ∈ {3,5,7} of [π(N/2p·p⁻) − π(N/p·p⁺)].
  The threshold N₁ comes from a finite family of at most 601 "late-crossing" triples, dominated by the bound (p⁺/p)(q⁺/q) ≤ 1.98925 < 2 together with Dusart's explicit prime-gap estimates, which certify r < 14,872; the enumerated family's observed maximum is r = 5,591. (The certified bound and the observed maximum are distinct numbers; v1 conflated them.)

### 4.2 The cancellation

From h₁ = (E − F) − V + 1 + elem = (E − B) − (V − 1) and the master identity,

h₁ = π(N/4) − π(N/6) + cap − D_E.

Insert the finite-parts forms. The leading π(N/4) − π(N/6) cancels the p = 2 term of D_E. Three of the ten cap-pairs, (2,3), (3,5), (5,7), cancel term-for-term against the three blocker terms for p = 3, 5, 7 (denominators 12/15, 30/35, 70/77 match exactly). Seven cap-pairs and the constant 10 survive:

> **Theorem B [PROVED, given the §4.1 inputs; VERIFIED independently].** For all N > 1,040,255,
> **h₁(N) = 10 + Σ over (p,q) ∈ 𝒫 of [ π(N/2pq) − π(N/p⁺q⁺) ]**, 𝒫 = {(2,5),(2,7),(3,7),(3,13),(3,19),(3,23),(7,13)}.

Explicitly, h₁(N) = 10 + π(N/20) − π(N/21) + π(N/28) − π(N/33) + π(N/42) − π(N/55) + π(N/78) − π(N/85) + π(N/114) − π(N/115) + π(N/138) − π(N/145) + π(N/182) − π(N/187).

The constant 10 has a concrete meaning: for each of the ten crossing pairs, the open interval count π(N/2pq) − π(N/p⁺q⁺) drops the single completer sitting on its lower edge (the largest prime ≤ N/p⁺q⁺, whose successor clears N), and those ten dropped completers are genuine cells. **[VERIFIED 10/10 at N = 2×10⁶ and 5×10⁷.]**

### 4.3 Check

h₁ − (seven-pair sum) = 10 exactly at nine values of N from 1.105×10⁶ to 1.20×10⁸, with h₁ on the left computed independently as (E−F)−V+1+elem from the enumerated complex. The directly evaluated seven-pair sum reproduces the entire oscillation of h₁ to numerical identity. (Beyond 1.2×10⁸ the identity is used, not re-verified against an enumerated complex; §6's long series inherit it through the proof, and a belt-and-braces direct count at N ≈ 10⁹–10¹⁰ is queued.)

---

## 5. The limiting density

Each bracket π(N/2pq) − π(N/p⁺q⁺) ~ N/(log N) · (1/2pq − 1/p⁺q⁺), and V = π(N/6) ~ N/(6 log N). Dividing and taking N → ∞:

> **Theorem C [PROVED, unconditional on PNT + Bertrand + Dusart + finite computation].**
> h₁(N)/V(N) → K := 6H − 3/22 = 97360699/1078282205 = 0.0902924…, where H is the explicit finite rational Σ over the ten crossing pairs of (1/2pq − 1/p⁺q⁺) = 488798363/12939386460. The limit is positive because K = 6(1/4 − 7/66 + H) − 1 and the three fractions 1/60 + 1/420 + 5/924 already exceed 1/44. (Equivalently, and more simply: the three cancelled pairs of H sum to exactly 1/44, so K = 6 × (seven-pair sum), a sum of seven positive brackets. Re-derived from scratch and confirmed exactly, 1 Jul evening.)

Two remarks. First, no transcendental constant appears: the leading prime-count constant (a Mertens-type term) cancels identically between the numerator's pieces, which is why K is rational rather than an expression in the Euler–Mascheroni or Mertens constants. Second, K is the density of the *signed* first Betti number h₁ = b₁ (an identity, now proved: C-0744 + C-0739, Tier-2 ruling 1 Jul). The lab also tracks the "canonical" density (h₁ − δ)/V ≈ 0.0585, where δ = rank_unsigned ∂₂ − rank_signed ∂₂ is a torsion-like frustration term; that constant is **not** known to be rational and is where any remaining transcendence lives. These two numbers must not be confused.

---

## 6. The spectral shadow, and exactly how far it goes

### 6.1 What is true

Because h₁ is, by Theorem B, a fixed signed combination of prime-counting functions, its fluctuation about the smooth part is, by the classical explicit formula, a sum over the non-trivial zeros ρ of ζ:

h₁(N) − (smooth) = − Σ_ρ M(ρ) · (N^ρ-type term), with M(ρ) = Σ over the fourteen denominators m of ± m^{−ρ}.

The factor M(ρ), a Dirichlet polynomial in fourteen small integers, is derived with no reference to ζ. Scored against the measured per-zero amplitudes of h₁/V (data to N = 6×10¹⁰; the known zeros are used only as sampling frequencies, the envelope formula itself stays zero-free), it predicts the relative amplitudes with which individual zeros appear: correlation 0.992 over the first 30 zeros, 0.974 with the dominant first zero removed, matching into the noise floor (γ₂₄ measured 0.026 vs predicted 0.027; γ₃₀ 0.026 vs 0.028). **[VERIFIED]** Reading zeros directly off the spectrum recovers 11 of them, up to the 18th (γ₁₈ ≈ 72.1), resolution-limited not signal-limited (6 → 9 → 11 zeros as the sieve depth grows 3×10⁸ → 6×10⁹ → 6×10¹⁰). The fluctuation grows no faster than N^{1/2} (measured exponent 0.44), consistent with, and required by, the Riemann hypothesis; indeed the fourteen-term combination cancels ~99.6% of the individual prime-count fluctuation, so h₁ is an unusually "quiet" object.

**The dartboard null [VERIFIED, 1 Jul evening].** The 0.992 needed a yardstick: perhaps *any* signed 14-tuple of small integers correlates with the measured amplitudes (both decay with height, which inflates raw correlations). Tested against 20,000 loose controls (14 random distinct integers in [10,200], balanced signs) and 20,000 matched controls (7 crossing-style pairs (+m, −m′) with m′/m ∈ [1.005, 1.6]): the true envelope scores 0.998 (independent re-measurement of the amplitudes; 0.993 excluding γ₁) against a null median of 0.64 and a null maximum, across all 40,000 draws, of 0.94. With the shared 1/|ρ| decay stripped out, the null collapses to median ≈ 0.00 (99th percentile 0.43, max 0.67) while the true envelope holds 0.992. The true denominators beat every one of 40,000 controls on every scoring. The amplitude channel is specific to the topology-selected denominators, not an artifact of shared decay.

### 6.2 What this is not

All of §6.1 is the ordinary prime-to-zero duality. The zeros are present because h₁ is built from prime counts, and every prime count contains them (Riemann, 1859). Two direct controls make the point:

- **The envelope is blind to the zeros' positions.** |M(1/2 + it)| at the 30 true zeros averages 0.489; at 5,000 random heights it averages 0.500. The zeros sit at the 48th percentile of M's own values: M does not know where they are. So the geometry weights the zeros but does not locate them. **[VERIFIED]**
- **Only the prime ruler throws them.** Running the identical slab construction with the plain-integer ruler gives a top spectral peak at the window-beat frequency, not the first zero; the prime ruler gives the first zero at amplitude far above everything else. **[VERIFIED]** The zeros belong to the primes, not to the geometry.

Consequently: **[NOT CLAIMED]** any progress on the Riemann hypothesis, any new bridge between primes and zeros, or any means of computing primes or zeros more cheaply. Computing h₁ requires the primes as input; nothing is obtained more cheaply than it is supplied.

---

## 7. Discussion: what is genuinely here, and what it might be good for

**Proven, unconditional:** the rational density K = 6H − 3/22 for the signed first-Betti count (Theorem C), and its exact finite-N form as fourteen prime counts (Theorem B), both resting only on PNT + Bertrand + Dusart + a finite certificate. This is the strongest and most self-contained result, and it is directly relevant to Banerjee's open multiplicity constant: it pins, exactly and rationally, the signed density that his error term skirts. (Full closure of the −1 multiplicity would additionally need the Tier-2 topological reading, i.e. the ω=3 rs-identity, and the companion b₂ count, both still open.)

**Possibly the most broadly interesting:** the ω = 2 slab identity (Theorem A) is a clean statement with no arithmetic in it; its pure-down-set case at every ω is classical (Björner–Kalai), and the slab case is a concrete conjecture in a well-studied corner of algebraic combinatorics (shifted complexes). If the slab case is new, it is a tidy addition; if it is known, that is worth learning, and a combinatorialist would know on sight.

**A tool, not a theorem:** Theorem B makes h₁, hence K, computable by prime counting alone (no complex need be built), which is how the constant was pushed to N = 6×10¹⁰ cheaply.

**Honestly not here:** any route to the Riemann hypothesis, and any "oracle" for primes. The appearance of the zeros is the classical duality, verified to be prime-specific, geometry-blind on positions, and (new, §6.1) envelope-specific on amplitudes.

**Where a reader might find use.** (a) A combinatorialist: is the slab case of Theorem A new, and does the shifted-complex framework close ω ≥ 3? (b) An analytic number theorist: is the exact rational density, or the fourteen-term identity, of independent interest for coprime-graph spectra, and is the finite-parts certificate airtight? (c) Anyone studying almost-prime counting: h₁ = 10 + fourteen prime counts is an unusually strong cancellation identity whose ~99.6% suppression of the √N fluctuation might be a useful example.

---

## Appendix A. The fourteen denominators

Signed, in order: +20, −21, +28, −33, +42, −55, +78, −85, +114, −115, +138, −145, +182, −187. Each pair (2pq, p⁺q⁺) is a crossing pair (p⁺q⁺ > 2pq), so each bracket counts primes in a thin interval and is non-negative.

## Appendix B. Certificates and data (reproducible)

- Field-independence and the slab identity: dim ker over GF(2), GF(3), GF(7), GF(101), GF(2³¹−1) equal (GF(2): /lab/scripts/slab_gf2_sweep.py, 149 slabs, odd-prime cross-check per slab, 0 mismatches); verified ω = 2,3,4 across many rulers; ω = 5,7 for the prime case.
- Theorem B: h₁ − seven-pair sum = 10 at N ∈ {1.105, 1.986, 3.569, 6.413, 11.52, 20.71, 37.21, 66.87, 120.2} ×10⁶.
- Theorem C finite parts: H = 488798363/12939386460; D_E-constant = 7/66; K = 97360699/1078282205; late-crossing family ≤ 601 triples, certified r < 14,872 (Dusart), observed max r = 5,591; hashed audit script (SHA-256 ed1e8bb7…) reproduces all certificates plus a formula-free brute-force check at N = 1.05, 1.20, 1.50 ×10⁶. Banked as C-0743 Tier-1 (Addy v4, 1 Jul); Tier-2 (b₁ reading) CONJECTURE pending §2.
- §6: 30-zero envelope correlation 0.992 (0.974 without the first zero); dartboard null 40,000 controls, true envelope above all (decay-stripped null median ≈ 0.00 vs true 0.992; /lab/scripts/envelope_dartboard.py); position-blindness control (0.489 vs 0.500); ruler control (primes vs integers vs random); growth exponent 0.44.
