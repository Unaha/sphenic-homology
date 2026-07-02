# PROOF CAMPAIGN: completeness of the balance modes (the ru structure theorem)

*Improbability Lab, 2 July 2026. STATUS: CAMPAIGN IN PROGRESS. Target: ker ∂₂ᵘ = span{([a]−[b]) ∧ Z_balance(L_{a,b})} for the sphenic window complex (and conjecturally any finite slab). ⊆ is PROVED; the graded skeleton is verified at all 29 accessible levels (two complexes); ONE lemma remains. Nothing banked; Addy used in ADVISORY mode only.*

## 0. Why this matters

If completeness proves: e = F − ru is a fibered balance count, δ = elem − e follows, and canonical κ = (h₁ − δ)/V ≈ 0.0585, the last open constant of the arc, reduces to link-graph balance and connectivity combinatorics (prime-gap configurations, Bertrand/Nagura territory). Together with C-0743/44/45 the entire coprime-graph program becomes counting.

## 1. What is proved (rigorous, self-contained)

**Lemma A (modes are cycles).** For any prime pair {a,b} and any z with zero unsigned vertex sums on L_{a,b} (the balance kernel: even cycles and odd-cycle barbells of signed-graph theory), the chain m = Σ_e z_e([a∪e] − [b∪e]) satisfies ∂ᵘm = 0. Proof: facet (u,x) of an edge e: coefficients z_e − z_e = 0; facets (a,u): Σ_{e∋u} z_e = 0 by the vertex condition; likewise (b,u); the facet (a,b) never occurs. ∎

**Lemma B (cone split at the least vertex).** Let w ∈ ker ∂ᵘ|_{C≥v}, v = least vertex of supp(w), A = cells containing v with tail chain w_A on L_v^{≥v}, B = the rest. Then (i) w_A has zero unsigned vertex sums (from the v-facet block); (ii) **w_A = −∂ᵘ(u) exactly**, where u = the B-part of w (the v-free facet block; both sides are supported on L_v-edges since every other facet coefficient of ∂u must vanish); (iii) if B = ∅ then w = 0. ∎

**Corollary (the realizable space).** W_v := {A-parts of kernel vectors of C≥v with least vertex v} = balance(L_v^{≥v}) ∩ ∂ᵘ(chains of C_{>v}). The second condition is not decorative: the naive lemma without it is FALSE (deficit 1276 at N=10⁵).

**Lemma C (graded reduction).** The A-part map identifies K(C≥v)/K(C>v) ≅ W_v, and the a=v modes have A-parts exactly Σ_{b>v} balance(L_{v,b}^{≥v}) ⊆ W_v. Hence, by downward induction on the (finite, ≤ π(N^{1/3})) least-vertex levels, completeness for C≥v follows from completeness for C_{>v} plus the

> **REALIZABLE DECOMPOSITION LEMMA (the crux, open):**
> balance(L_v^{≥v}) ∩ ∂ᵘ(C_{>v}) ⊆ Σ_{b>v} balance(L_{v,b}^{≥v}).
> In words: every balanced, link-supported boundary of the upper subcomplex splits into pair-fiber balance cycles.

## 2. Evidence for the crux

- Graded test: dim K(C≥v) = rank(modes of C≥v) at ALL levels, N = 10⁵ (13 levels) and 2×10⁵ (16 levels), integer-exact; 5×10⁵ run in progress. Since Lemma C is proved, these equalities are precisely the crux verified at every accessible (v, N).
- Global completeness: rank(mode family) = e at N = 5×10⁴, 10⁵, 2×10⁵, 5×10⁵ (482/1270/3082/9402).
- The failed naive version (documented in the ledger, Addendum 11) shows the boundary condition must be used; any proof attempt that ignores the witness is doomed by counterexample.

## 3. Attack routes (state of each)

**Route 1: B-witness double induction (primary).** Given h ∈ W_v with witness u (h = −∂ᵘu, u a chain of C_{>v}): by the graded induction hypothesis, ker ∂ᵘ|_{C>v} = span(modes of C_{>v}), so u may be normalized modulo the mode span of the upper complex (the witness is unique up to upper modes). Then peel u at ITS least vertex v₂: the v₂-facet block of h = −∂u relates u's v₂-tail chain to h's (v₂,·)-edges. Wanted: a move that strips the (v₂,·) content of h using pair fibers {v, b} and reduces |supp(u)| or raises its least vertex. Status: the bookkeeping identity is written (the v₂-tail vertex sums equal −h(v₂,·) where (v₂,x) ∈ L_v, else 0); the move is not yet found. The single-pair case is the calibration: a mode's own witness is its b-half, and the identity closes trivially by balance at b.
**Route 2: double cover / twisted homology.** The unsigned kernel is the anti-invariant cycle space of the orientation double cover (lab knew this: b₂(cover) = 2e + δ, 29 Jun). If the cover of a slab complex is slab-like, C-0744 could be applied upstairs and the twisted part extracted. Not yet explored; may give completeness without the crux.
**Route 3: matroid/graphic route.** Each fiber balance space is the cycle space of a signed graphic matroid; the mode span is a matroid union over pairs; completeness = the union saturating the kernel. Matroid union theorems (Nash-Williams) give rank formulas: could yield BOTH the proof and the E−V+C-type formula for e in one shot. Speculative but the payoff is the formula itself.

## 4. Small-case anatomy (for whoever climbs next)

- A single cell's boundary is never balanced (triangle vertex sums = 2). A two-cell boundary (p,q,r) − (p,q,s) is not balanced either (sums 2 at r-side vertices). The minimal balanced boundaries seem to require the full pair-mode structure or longer entangled chains; charting the minimal witnesses at small N is a cheap next probe and would likely reveal Route 1's missing move.
- The diagonal-corner cells (the one anomaly per N of the segment/corner laws) are the expected hard case for any explicit-extremal-mode argument.

## 4b. Prior-art placement (2 Jul morning, full deep-read; see ledger Addendum 15)

The generators are NOT new circuit species: the parity box is a *balanced circuit* in the sense of Rusnak, "Oriented Hypergraphs I" (EJC 20(3) 2013 #P48, Theorem 7.2.7 arXiv numbering; verify against the published numbering before quoting), and the barbell mode is a *balanceable circuit* in the sense of the optimal-shunting theorem of Rusnak–Li–Xu–Yan–Zhu (Discrete Math. 345, 2022; arXiv:2005.07722), both under the standard all-negative-adjacency dictionary (all-positive incidence ⇒ positive circle = even circle = Zaslavsky balance). What is NEW: the spanning statement. No nullity/spanning theorem exists anywhere in the oriented-hypergraph program (the unbalanceable circuit family is their declared open problem; no global kernel-dimension formula is known for hypergraph incidence matrices at all). Our theorem, restricted to the sphenic/window family, asserts the two CLASSIFIED families already span the rational kernel, fibered over vertex-pairs by link balance, i.e. unbalanceable circuits are rationally redundant here. Independent structural support from their own results: all-entrant minimal k-cross-thetas are minimally dependent ONLY over GF(k), hence contribute no rational kernel vectors — the simplest unbalanceable circuits literally vanish over ℚ in our all-positive setting. **Proof-relevant lever:** the gauge/threading argument should aim to show every unbalanceable dependency in our family is a rational combination of classified ones, with the GF(k) phenomenon as the mechanism template. Attribution care: cite Rusnak 2013 (sole author), not "Reff–Rusnak", for the circuit classification. Nine-item specialist reference list in the ledger.

## 5. Discipline

Naive DL is FALSE (do not re-derive; ledger Addendum 11). Nothing here is banked; the structure theorem stays CONJECTURE until the crux proves and survives a hostile round. The 5×10⁵ graded run and an advisory (non-banking) Addy read of this document are the current support actions.
