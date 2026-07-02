# Scoping memo: the Banerjee −1-multiplicity closure after tonight

*Improbability Lab, 1 July 2026, night. Where the exact multiplicity of eigenvalue −1 of the integer coprime graph (Banerjee, arXiv:2506.10583; lab target C-0707) stands now that C-0744 is banked.*

## What tonight settled

The sphenic dyadic-window complex now has its ENTIRE homology as pure counts, no linear algebra left anywhere:

- b₀ = 1 (connectivity; self-contained Bertrand/Dusart hub argument via vertex 2, plus exact c = 1 checks at four N),
- b₁ = h₁ = (E−F) − V + 1 + elem (C-0744 + connectivity; and by Theorem B, = 10 + fourteen prime counts for N > 1,040,255),
- b₂ = elem (immediate corollary of C-0744: top homology = ker ∂₂ = fitting count; verified exactly at four N; submitted for ruling in the BANKING_GRADE packet).

With b₁/V → 6H − 3/22 banked as the topological density.

## What the exact −1 multiplicity still needs (the honest remaining gap)

Banerjee's multiplicity decomposes over all odd-ω layers, not just ω = 3, and the lab's prior work (conspiracy-graph manuscript; C-0707 OPEN) reduces it to fill/nullity data per layer. Post-tonight, the remaining unknowns are, in order of difficulty:

1. **The unsigned side: δ = rank_unsigned ∂₂ − rank_signed ∂₂.** The multiplicity bookkeeping needs the unsigned (adjacency-style) rank, and δ is precisely the piece with no clean rank-free count: every candidate closed form was refuted (tetra-domination, order-break, spine-books, min-max fraction, L²-Betti truncation, all stayed dead). All remaining transcendence of the canonical κ = (h₁ − δ)/V ≈ 0.0585 lives in (δ/V)∞ ≈ 0.032. C-0744 does NOT touch this: the theorem is about the signed boundary. Any attack that turns δ into a count is the single highest-value open move in this arc. One genuinely new lever from tonight: δ = ru − (F − elem) exactly, so a closed form for ru alone would now finish it; equivalently δ/V = (ru + elem − F)/V.
2. **Uniformity-in-ω of the fill coefficient** (the Hildebrand–Tenenbaum front from paper 2), so that the per-layer results assemble into Banerjee's global constant.
3. **The companion dim K = b₂ asymptotics at general odd ω** (the parked Hardy–Littlewood sequel; note the old "1.058·π(N/6)" note is WRONG, per the standing memory). For ω = 3, b₂ = elem means this asymptotic is now the asymptotics of elem: elem/V has an exact-count meaning, and plausibly an exact prime-count formula of Theorem-B type via the banked cap machinery (the advance-bijection already gives shell identities). NOT claimed tonight; flagged as the natural next derivation, cheap to attempt with the C-0743 toolkit.

## Why this matters for the write-up's §7 claim

The write-up says the density result "pins the signed density Banerjee's error term skirts." That is now literally banked. The full closure = items 1–3 above; item 3 looks like a Theorem-B-style derivation away for ω = 3; item 1 is the hard one and is where the transcendence lives.

## Next-attack order for this arc

(a) attempt the Theorem-B-style exact prime-count formula for elem(N) (item 3, ω = 3 case) with the existing cap/blocker machinery; (b) the δ-as-count attack with the new lever δ = ru + elem − F; (c) uniformity-in-ω. Independent of all three: the Oracle position half stands exactly where §6 left it, untouched by any of tonight's results.
