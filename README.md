# sphenic-homology

[![DOI](https://zenodo.org/badge/1287222164.svg)](https://doi.org/10.5281/zenodo.21135221)

**The homology of the sphenic window complex, reduced to counting functions, with machine-verifiable certificates.**

For a window `(N/2, N]`, build the 2-complex whose triangles are the *sphenics* (squarefree p·q·r) in the window, edges the co-occurring prime pairs, vertices the primes. This repository is the machine-verifiable supplement to **Papers 3 and 4** (see [The papers](#the-papers)); it contains their proofs, exact identities, and replayable certificates:

1. **Slab identity theorem** (Paper 3): for any finite *slab* (difference of order ideals of increasing integer tuples, of which the sphenic complex is the ω=3 prime-ruler case), the top boundary's kernel dimension equals the number of *fitting* cells (`x` with `x+(1,…,1)` still in the slab), over every field, with an explicit ±1 basis. Hence **rank ∂₂ = F − elem** for the sphenic complex.
2. **Exact prime-count Betti numbers** (Paper 3): for `N > 1,040,255` the full homology is
   `(b₀, b₁, b₂) = (1, 10 + Σ₇ [π(N/2pq) − π(N/p⁺q⁺)], S(N) − S(N/2) − D(N/2) + 10 + Σ₁₀ [...])`
   — fourteen prime counts, sphenic counts, and one odd-semiprime count. No linear algebra required.
3. **Exact rational density** (Paper 3): `b₁/π(N/6) → 6H − 3/22 = 97360699/1078282205 ≈ 0.0902924`, unconditionally (PNT + Bertrand + Dusart + a finite certificate). This pins the signed Betti density underlying the −1-multiplicity error term of S. Banerjee (arXiv:2506.10583).
4. **Balance-mode structure theorem** (Paper 4): the kernel of the *unsigned* boundary is spanned by pair-difference balance modes `([a]−[b]) ∧ z`, `z` a balanced cycle (Zaslavsky even-circle) of the common link graph `L_{a,b}`. Proof: cone-split + graded reduction (proved) + a finite leakage-gauge condition **(LG)** certified at 616 level pairs across five N, all characteristics (exact integer invariant factors for the certified set; characteristics 2 and 3 are exceptional and exactly understood). Positioning: the generators are classified circuits of Rusnak (EJC 2013) and Rusnak–Li–Xu–Yan–Zhu (Discrete Math. 2022); the *spanning* statement addresses their declared open problem (Paper 4).

## The papers

This repository is the supplement to a four-paper series on the −1-eigenspace of the coprime graph (all by Lee Rich):

1. *The −1-eigenspace of the coprime graph of integers: prime-cube modes and an exact multiplicity*, [10.5281/zenodo.20933665](https://doi.org/10.5281/zenodo.20933665).
2. *The −1-eigenvalue multiplicity of the coprime graph: a conditional sublinear law*, [10.5281/zenodo.21169867](https://doi.org/10.5281/zenodo.21169867).
3. *Exact prime-count homology of the sphenic window complex*, [10.5281/zenodo.21171567](https://doi.org/10.5281/zenodo.21171567) &mdash; [`papers/paper3_exact_prime_count_homology.pdf`](papers/paper3_exact_prime_count_homology.pdf).
4. *A balance-mode structure theorem for the unsigned kernel of the sphenic window complex*, [10.5281/zenodo.21172540](https://doi.org/10.5281/zenodo.21172540) &mdash; [`papers/paper4_balance_mode_structure_theorem.pdf`](papers/paper4_balance_mode_structure_theorem.pdf).

Papers 3 and 4, this repository's subject, determine the three-prime (sphenic, ω=3) layer of the −1-multiplicity decomposition set up in Papers 1 and 2. The working derivations behind them are in [`notes/`](notes/).

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

- The structure theorem is banked at the **certified perimeter** (the bundled N; all characteristics outside {2,3} for the certified set). The all-N form is work in progress (the straddle-free band localization and the richness program are documented in Paper 4; working notes in `notes/03`, `notes/04`).
- The novelty of the slab identity is stated as *adjacent* to Björner–Kalai (whose near-cone theorem is exactly the pure-ideal case) and Nagel–Reiner (whose complex-of-boxes is the same species applied to ideal resolutions); see Paper 4 (`notes/05`).
- Nothing here bears on the Riemann hypothesis or on predicting primes; the spectral appearances of ζ-zeros in these objects are the classical explicit-formula duality, verified to be exactly that and no more (Paper 3, §7).

## Method note

All results were developed in an AI-assisted workflow (Claude + a GPT-5.5-based adversarial adjudicator) under a hostile-verification protocol: every claim was attacked by independent implementations, randomized controls, and adversarial review before being recorded. The certificates in this repository exist so that no reader need care how the mathematics was produced: run them.

## Citation

If you use this work, please cite the relevant paper (Paper 3 for the prime-count homology, Paper 4 for the structure theorem; see [The papers](#the-papers)) and, if you use the certificates or code, the software archive via `CITATION.cff` ([10.5281/zenodo.21135221](https://doi.org/10.5281/zenodo.21135221)). Author: Lee Rich (The Improbability Lab).
