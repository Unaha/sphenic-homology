# sphenic-homology

[![DOI](https://zenodo.org/badge/1287222164.svg)](https://doi.org/10.5281/zenodo.21135221)

**The homology of the sphenic window complex, reduced to counting functions, with machine-verifiable certificates.**

For a window `(N/2, N]`, build the 2-complex whose triangles are the *sphenics* (squarefree p·q·r) in the window, edges the co-occurring prime pairs, vertices the primes. This repository contains proofs, exact identities, and replayable certificates establishing:

1. **Slab identity theorem** (`papers/02`): for any finite *slab* (difference of order ideals of increasing integer tuples, of which the sphenic complex is the ω=3 prime-ruler case), the top boundary's kernel dimension equals the number of *fitting* cells (`x` with `x+(1,…,1)` still in the slab), over every field, with an explicit ±1 basis. Hence **rank ∂₂ = F − elem** for the sphenic complex.
2. **Exact prime-count Betti numbers** (`papers/01`): for `N > 1,040,255` the full homology is
   `(b₀, b₁, b₂) = (1, 10 + Σ₇ [π(N/2pq) − π(N/p⁺q⁺)], S(N) − S(N/2) − D(N/2) + 10 + Σ₁₀ [...])`
   — fourteen prime counts, sphenic counts, and one odd-semiprime count. No linear algebra required.
3. **Exact rational density**: `b₁/π(N/6) → 6H − 3/22 = 97360699/1078282205 ≈ 0.0902924`, unconditionally (PNT + Bertrand + Dusart + a finite certificate). This pins the signed Betti density underlying the −1-multiplicity error term of S. Banerjee (arXiv:2506.10583).
4. **Balance-mode structure theorem** (`papers/03`, `04`): the kernel of the *unsigned* boundary is spanned by pair-difference balance modes `([a]−[b]) ∧ z`, `z` a balanced cycle (Zaslavsky even-circle) of the common link graph `L_{a,b}`. Proof: cone-split + graded reduction (proved) + a finite leakage-gauge condition **(LG)** certified at 616 level pairs across five N, all characteristics (exact integer invariant factors for the certified set; characteristics 2 and 3 are exceptional and exactly understood). Positioning: the generators are classified circuits of Rusnak (EJC 2013) and Rusnak–Li–Xu–Yan–Zhu (Discrete Math. 2022); the *spanning* statement addresses their declared open problem (`papers/05`).

## Verify it yourself

Nothing here asks for trust. From the repo root (Python 3, numpy; `python-flint` only for the all-characteristic stage):

```bash
# 1. Independent enumeration: re-derive every cell inventory from N alone (stdlib only)
python3 scripts/enum_replay.py

# 2. Independent certificate replay: rebuild fibers/generators from raw cells with a
#    different algorithm (spanning-tree balance bases) and different elimination order,
#    re-verify every claimed rank over an 8-prime battery
python3 scripts/lg_replay_check.py certificates/N100000
python3 scripts/lg_replay_check.py certificates/N200000   # (and N50000 / N300000 / N500000)

# 3. All-characteristic certificates: unit-pivot unimodular reduction + exact SNF of residuals
python3 scripts/twostage_certify.py
```

Note: paths inside some auxiliary scripts reflect the lab environment (`/lab/...`); the three verification entry points above run from the repo root. Bundles under `certificates/` are gzipped JSON with SHA-256 manifests.

## Scope, honestly stated

- The structure theorem is banked at the **certified perimeter** (the bundled N; all characteristics outside {2,3} for the certified set). The all-N form is work in progress (the straddle-free band localization and the richness program are documented in `papers/03`).
- The novelty of the slab identity is stated as *adjacent* to Björner–Kalai (whose near-cone theorem is exactly the pure-ideal case) and Nagel–Reiner (whose complex-of-boxes is the same species applied to ideal resolutions); see `papers/05`.
- Nothing here bears on the Riemann hypothesis or on predicting primes; the spectral appearances of ζ-zeros in these objects are the classical explicit-formula duality, verified to be exactly that and no more (`papers/01`, §6).

## Method note

All results were developed in an AI-assisted workflow (Claude + a GPT-5.5-based adversarial adjudicator) under a hostile-verification protocol: every claim was attacked by independent implementations, randomized controls, and adversarial review before being recorded. The certificates in this repository exist so that no reader need care how the mathematics was produced: run them.

## Citation

See `CITATION.cff`. Author: Lee Rich (The Improbability Lab).
