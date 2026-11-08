# Coupled diagonal upper-bound work package

Date: 2026-11-08. Base: `df6e35cfff68580dc78aa91bc35d4c6399a6464a`.

Object: every map from `{0,...,n-1}^2` to at most three colors. The forbidden configuration is exactly `(x,y),(x+d,y),(x+d,y+d)` with positive integer `d`. An impossibility proof at side `n` proves `R_3 <= n`, not a construction or a lower bound.

Target: compress the published upper bound 493 without G9, S21, a rainbow-minimization assertion, a source-extension assumption, or a floating-point infeasibility assertion. The proposed new interaction is competition among the three diagonal color classes for the same endpoint positions; the proposed reusable lemma bounds their combined short-rank pair distances by a joint rearrangement.

Success evidence: a complete universal geometric reduction, exact integer arithmetic for a finite contradictory inequality, explicit external inputs and their original sources, and comparison with the published interval method and archived repository work. All numerical code that supports the theorem uses Python integers. Exploratory linear programs remain discovery-only.

First uncertain steps at the start: the difference-fiber capacity must hold separately for every diagonal class; all three classes must be large enough for the coefficient formula; joint endpoint accounting must cover every color partition, including unbalanced partitions. These are resolved in `THEOREM.md`.

Outcome: the new joint rearrangement gives an independent 466 proof. An archival check uncovered an older direct convolution proof of 465, which is reconstructed independently here and depends only on authenticated external Golomb results. Consequently 466 is a method checkpoint, not the best upper bound established by this package. The restored 465 proof is not newly original research and does not validate the unrelated, unproved rainbow route.

Evidence boundary: `G(24) >= 425` and `G(25) >= 480`, where `G` is minimum span, are established external computational theorems. Their primary completion reports and the 2025 paper's table were checked. This package does not replay the exhaustive distributed.net searches. With the conventional practice of using these published results, the consequences are unconditional; with an entirely self-contained, locally replayable proof standard, the external dependency remains explicit.
