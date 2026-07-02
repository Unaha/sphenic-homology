# Positioning memo: C-0744 (slab identity) vs Nagel–Reiner and the shifted-complex literature

*Improbability Lab, 1 July 2026, night. Basis: full deep-read of Nagel–Reiner, "Betti numbers of monomial ideals and shifted skew shapes", arXiv:0712.2537 = Electron. J. Combin. 16(2) (2009) #R3 (all 38 pages, isolated-context read), plus the earlier passes on Björner–Kalai, Klivans, Duval.*

## The one-paragraph positioning (for any external write-up)

Our slab is precisely a *skew squarefree strongly stable d-uniform hypergraph* in the sense of Nagel–Reiner (their Definition 3.4): a difference K ∖ K′ of order ideals in the Gale (componentwise) order on increasing tuples, which is identical to our coordinatewise order. Nagel–Reiner study a different invariant of these objects: the minimal free resolution of the associated monomial ideal. For the non-skew case (K′ = ∅) their complex-of-boxes resolution (Theorem 3.12, Corollary 3.13) shows the syzygies of I(K) are indexed by the boxes X₁ × ⋯ × X_d inside K, counted by maxima statistics; for skew shapes their results are confined to d = 2 (Theorem 2.15, Corollary 2.16, via Hochster's formula on the complement's clique complex); and the resolution of I(K ∖ K′) for general d is posed by them as an open problem (Question 5.1). Our theorem concerns a different functor on the same combinatorial data: not the syzygies of the ideal but the top-dimensional cycle space of the generators themselves regarded as (d−1)-simplices, for which the kernel dimension equals the number of cells x with x+(1,…,1) still in the slab, over every field, with an explicit ±1 basis of join modes supported on the diagonal intervals [x, x+δ]. Neither statement implies the other. The pure case (K′ = ∅) of our theorem is classical (Björner–Kalai near-cones, via the bijection x ↦ x−δ). The closest prior work on our invariant for skew shapes is Duval's relative Laplacian spectral recursion (Electron. J. Combin. 11(2) (2006) #R26, math/0507130), cited by Nagel–Reiner as the reference for these skew objects.

## Why Theorem A does not follow from Nagel–Reiner (three independent blockers)

1. **Wrong functor.** Every NR theorem computes β_i(I) = dim Tor_i of the monomial ideal (resolutions/Hochster). Ours is dim ker of the top simplicial boundary on generators-as-simplices, the top cycle space of the pure complex they generate. Different invariants of the same data; no conversion between the statements.
2. **Wrong regime.** NR's skew results are d = 2 only. Their general-d machinery (complex of boxes) requires K′ = ∅. The general-d skew case is their open Question 5.1, and even that question is about the ideal.
3. **Wrong count.** NR's Betti indices are box enumerations with arbitrary side sizes classified by generator maxima (µ_k, α_k statistics). No diagonal-shift/fitting count #{x : x+δ ∈ R} appears anywhere in the paper. Their boxes are full d-partite products; nothing like our degenerate collision joins (suspensions of simplex boundaries) occurs, because their d-partite setting makes coordinate collisions impossible.

## The suggestive overlaps (why the adjacency must be cited)

Same poset (Gale order = componentwise order on increasing tuples). Same skew species (their Definition 3.4 names our slabs and cites Duval for them). Shared box aesthetic: their complex-of-boxes cells vs our join modes. Shared conclusions of field-independence. Their d = 2 skew answer is governed by "staircase cells" (cells at positions (i, i+1)), a diagonal-adjacency statistic of the diagram, cousin to (but not equal to) our fitting condition.

## The residual specialist check (the one named risk to novelty)

**Duval, "A relative Laplacian spectral recursion", EJC 11(2) #R26 (2006)** studies combinatorial Laplacian spectra of shifted PAIRS (Φ, Φ′) via a deletion/contraction recursion. Two reasons it likely does not contain our count, and one reason to check anyway: (a) the relative-pair boundary projects chains modulo C(Φ′); our boundary maps into the full ambient chain group unprojected, a strictly smaller kernel; (b) spectral methods are characteristic-0, while C-0744 is an every-field statement with a ±1 integral basis. But (c) if his recursion yields a combinatorial formula for the multiplicity of eigenvalue 0 of the top up-down Laplacian in some formulation equivalent to ours, the count itself could be implicit there. A specialist (or a dedicated deep-read of #R26 and of Duval–Reiner, "Shifted simplicial complexes are Laplacian integral", Trans. AMS 354 (2002)) should settle this before any novelty language stronger than "adjacent, apparently unstated."

## Bonus fact found during the read

Nagel–Reiner's Question 5.1 (general-d skew ideal resolutions, field-independence, combinatorial recipe, cellular realization) is OPEN as of that paper. Our join modes live on exactly their skew objects and handle collisions their d-partite boxes cannot see. Whether the join-mode technology contributes to their Question 5.1 (the ideal-resolution side) is a plausible future lab thread, and would be the natural vehicle for publishing Theorem A inside a recognized open problem's orbit.

## Registry actions

C-0744 notes already carry "novelty UNCLEAR, frame adjacent to Björner–Kalai + Nagel–Reiner." This memo sharpens that to: NR's theorems do not contain Theorem A (three blockers above); their Question 5.1 confirms the general-d skew regime was open territory for the ideal invariant; residual check = Duval 2006/2002.
