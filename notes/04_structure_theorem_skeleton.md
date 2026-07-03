# MANUSCRIPT SKELETON — The rational kernel of the sphenic incidence: a fibered balance structure theorem

*Improbability Lab, 2 July 2026. Working skeleton; every claim carries its status. The one open step is §6 (leakage-gauge); solver round in progress. Nothing here is banked beyond what the registry already holds (C-0743 BANKING_GRADE, C-0744, C-0745).*

## 1. Statement

**Theorem (structure of the unsigned kernel; CONJECTURE pending §6).** Let C be the sphenic window complex at level N (2-cells = squarefree pqr ∈ (N/2, N]), and ∂ᵘ its unsigned boundary (all-positive incidence; an oriented hypergraph with every adjacency negative in the sense of Rusnak). Over any field of characteristic ≠ 2, 3:

ker ∂ᵘ = span{ m_{a,b,z} = Σ_e z_e([a∪e] − [b∪e]) : prime pairs a < b, z ∈ Z_bal(L_{a,b}) },

where L_{a,b} is the common link graph and Z_bal the balance kernel (Zaslavsky even-circle cycle space: even cycles and odd-cycle barbells). Consequently e := dim ker ∂ᵘ is a fibered balance count, ru = F − e, δ = elem − e, and the canonical density κ = (h₁ − δ)/V is determined by link-graph balance and connectivity combinatorics.

Characteristic stratification (observed, to be stated as a proposition): over GF(2) the kernel is elem (C-0744); over GF(3) exactly one extra cross-theta class appears (Rusnak all-entrant GF(k) phenomenon); generic characteristic gives e.

## 2. Positioning (verified by full deep-reads; ledger Addenda 15)

Generators are classified circuits: parity boxes = balanced circuits (Rusnak, EJC 20(3) 2013 #P48, Thm 7.2.7 arXiv numbering); barbell modes = balanceable circuits (Rusnak–Li–Xu–Yan–Zhu, Discrete Math. 345 (2022), optimal-shunting theorem). No spanning/nullity theorem exists in the oriented-hypergraph program (unbalanceable circuits = declared open problem); this theorem is a spanning statement over their taxonomy for the sphenic family. Fiber object = Zaslavsky even-circle matroid. Adjacent: Nagel–Reiner complex-of-boxes (ideal resolutions, different functor). Specialist checks owed: none outstanding beyond standard referee review; nine-item reference list in the ledger.

## 3. Proved: modes are kernel vectors (Lemma A)

Three-line facet check: facet (u,x) cancels between the a- and b-copies; facets (a,u), (b,u) vanish by the zero-vertex-sum (balance) condition; facet (a,b) never occurs. Status: PROVED.

## 4. Proved: cone split and the realizable space (Lemma B)

For w ∈ ker ∂ᵘ|_{C≥v} with least vertex v: the A-part tail chain w_A ∈ Z_bal(L_v^{≥v}) (v-facet block); w_A = −∂ᵘ(B-part) exactly (v-free block; off-link facet coefficients must vanish); B = ∅ ⇒ w = 0. Hence W_v = Z_bal(L_v^{≥v}) ∩ ∂ᵘ(C_{>v}), the graded quotient of the kernel along the least-vertex filtration (levels = primes ≤ (fN)^{1/3}-ish, finitely many). Status: PROVED (Addy-audited in advisory, support convention explicit, char ≠ 2).

## 5. Proved reduction + the verified crux

Downward induction on levels reduces the Theorem to the REALIZABLE DECOMPOSITION LEMMA: W_v ⊆ Σ_{b>v} Z_bal(L_{v,b}^{≥v}) at every level. Verified: 50/50 graded levels (three complexes to 5×10⁵); ATOMIC form exact at space level (dim W_v = graded increment = fiber-sum dim: 186/200/123 at three levels); 271/271 single-fiber element decompositions; 8/8 window families; global completeness 4 sizes to kernel dim 9,402. Status: reduction PROVED; crux VERIFIED, open.

## 6. The one open step: the leakage-gauge lemma

Induction skeleton (drafted): peel the witness u at ITS least vertex v₂; facet blocks force the peel tail t₂ to be balanced except at straddle vertices (the fiber L_{v,v₂}, band-constrained: partners live in (v, 2v) by the window); subtracting full v₂-modes pushes the least vertex up; recursion terminates at the top. GAP: rebalance the straddle terms — show the needed corrector exists in Z_bal(L_{v,v₂}) (or kill the straddle by band-local witness modification), possibly under an explicit finite richness hypothesis on the band fibers to be machine-verified. Solver round in progress; output to be cold-refereed. Status: OPEN, sharply stated.

## 7. Consequences (upon closing §6)

e = dim Σ-fibered balance spaces (inclusion–exclusion over overlapping pairs; banded, quasi-local); dim Z_bal per component = E − V + [bipartite], with non-bipartite dominance growing at scale (0.73 → 0.81 → 0.88 measured) confining corrections to the completer fringe; δ = elem − e as the characteristic-2 jump; canonical κ = (h₁ − δ)/V reduced to counting; the Banerjee −1 multiplicity program loses its last rank.

## 8. Machine appendix (all hashed on the box)

mode_completeness.py (+5e5 variant), graded_completeness.py (+5e5), atomic_space_test.py, gauge_anatomy2.py (GF(3)/GF(5) stratification), window_hostile_completeness.py, bipartite_census.py, unsigned_free_probe.py / unsigned_split_hunt.py / pair_dead_alive.py / threshold_hunt.py (the δ-carrier anatomy), dp_proof_verify.py / dp_proof_walk.py (C-0744 layer). Ledger: CONSOLIDATION_3DAY_TRUTH_LEDGER_01JUL2026.md Addenda 6–17.
