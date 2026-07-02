# Results at a glance

| # | Result | Status | Where |
|---|--------|--------|-------|
| 1 | Slab identity: dim ker of the top boundary of any finite slab = number of fitting cells, every field, Z-free with explicit ±1 basis | Proved (two-round adversarial review) | papers/02 |
| 2 | rs-identity: rank of the sphenic boundary = F − elem, every N and window | Corollary of 1 | papers/01 §3 |
| 3 | b1 = 10 + fourteen prime counts (N > 1,040,255); b1/π(N/6) → 6H − 3/22 = 97360699/1078282205 exactly, unconditionally | Proved (four-round hardening + dependency packet) | papers/01 |
| 4 | b2 = elem = F − D(N/2) + cap exactly (every N); ten-pair π-form above the threshold; entire homology = counting functions | Proved (single-round review) | papers/01, 06 |
| 5 | Balance-mode structure theorem for the unsigned kernel | Certified perimeter: five N, all characteristics ∉ {2,3} for the certified set; all-N in progress | papers/03, 04 |
| 6 | Prior-art positioning (Björner–Kalai, Nagel–Reiner, Rusnak line) | Deep-read, documented | papers/05 |

Evidence stack for (5): 616/616 leakage-gauge rank certificates over five N; 8-prime battery at emission; independent checker replay (different algorithms) clean; independent enumeration replay clean; 32,868-check modular sweep: no bad primes below 1000; exact integer invariant-factor certificates (unit-pivot + residual SNF): none outside {2,3}; characteristic stratification observed exactly (GF(2) → elem; GF(3) → +1 cross-theta, matching Rusnak's all-entrant GF(k) dependency).

## Replay and certification log (2 Jul 2026)

- Independent-checker replay (job chknew): N50000 (55 pairs), N300000 (153 pairs), N500000 (210 pairs) all replayed clean by the independent checker (different algorithm, different elimination order), 0 failures. Verdict: ALL REPLAYED CLEAN.
- Two-stage all-characteristic certifier (job ts5e5, 5x10^5 giants, 60 GB cap): 75 pairs two-stage certified (issues=0), then the run aborted at the memory cap (FLINT allocation failure at ulimit). The remaining 5x10^5 giant pairs are battery-scoped: they hold over the eight-prime battery, but their two-stage integer (all-characteristic) certificate was not obtained. Per protocol, dense SNF was not attempted and the cap was not raised. The all-characteristic scope in papers/08 is therefore N in {1e5, 2e5}.
