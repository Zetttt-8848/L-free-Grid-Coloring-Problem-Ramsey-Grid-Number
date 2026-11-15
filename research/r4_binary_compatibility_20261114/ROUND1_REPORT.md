# Codex lane A: round-1 result

Agreement: R4-PAIR-20261114-v2. Date: 2026-11-14.
Branch: codex/r4-binary-compatibility-20261114.
Base: 726998b9da3edd36247a6e2a5c487ba25b0a7297.

**No new R4 upper bound is established.** This round produced an exact
sensitivity target, an analytic obstruction to an unrestricted collision-energy
route, a directly checked family of examples, and a source-aware replay of
the current R4 window certificate. External Claude's report is still needed
before integration and round 2.

## A0: exact hypothetical sensitivity

See sensitivity.py and sensitivity.json. The original certificates are unchanged.

| Consumer / tested rows | Hypothetical improvement | Consequence at that row |
|---|---|---|
| Elementary, rows 0/304/607 | 5 ppm uniform pointwise reduction of the active multiplicity profile | Excludes size K, improving that row's cap from K to K-1 |
| Elementary, same rows | 19921/19922/19922 ppm on the tested 1-ppm grid | Excludes floor(0.99K), with the original rank witness |
| Window, rows 0/282/564 | Weighted off-diagonal budget deficit strictly greater than about 4.372494/4.364222/4.381608 ppm | Excludes size K, improving that row's cap from K to K-1 |

Exact rational thresholds are in the JSON. Approximate ppm values are for
readability only. These are distinct hypotheses: a pointwise profile reduction
is stronger than one weighted budget reduction. Three representative rows are
not complete coverage of the outer consumer. No new whole-square bound follows.

The attempted one-percent window-cap targets fall below k=455000, outside
the certified endpoint-discrepancy range. The script explicitly refuses those
evaluations. Reusing the correction there would be unjustified.

## A1/A2: collision candidate refuted, with a sharp replacement bound

THEORY.md proves the forcing C_h^e pairs -> C_{h+delta}^{1-e}. It then
refutes the candidate E<=C R for every absolute C, even after summing over
all targets and colors. The reflected-Golomb family has

    |A| = 2r+2,  R = r(r+1),  E = 2r(r+1)(2r+1)/3.

Thus E/R=(4r+2)/3 is unbounded. The elementary pointwise replacement
m_t^e(u)<=|A|-2 is sharp. A polynomial-span example at r=40 has 82 marks,
span 328200, maximum collision multiplicity 80, and global E/R=54.

All 19 finite examples pass literal checks of every physical L, Golomb class,
forcing target, and energy formula. Generality comes from the written proof.
The family is sparse; it does not refute near-extremal or fixed-consumer
weighted deficit/collision statements. It is not a full-square construction.

Decision: **pivot away from unrestricted constant-energy bounds**. Do not
spend the remaining pilot allowance on a larger catalog for that false claim.

## Baseline audit

WINDOW_AUDIT.md records the mathematical review and successful raw-data
regeneration. The latest EDGE route uses exact rational data plus elementary
inequalities; its rounded published Sidon theorem and older twelve-shift
certificate are not active premises. One wording ambiguity about source
cardinality versus difference multiplicity was identified; the implementation
uses the correct distinction. Full independent formal certification is not
claimed.

## Exports for Claude

| ID | Exact content and scope | Evidence / consumer / near-extremality |
|---|---|---|
| A-FORCE | Binary-source same-class pair forces opposite target color | Written geometric proof; coordinate formula in THEORY.md; no near-extremality |
| A-COLLISION-FAIL | No absolute C bounds global E/R for all proper binary sources | Explicit universal counterfamily and 19 checked instances; rejects an unrestricted input to union growth; no near-extremality |
| A-WEIGHTED-BRIDGE | R_w^2<=U_w E_w and U_w<=2 sum_t w_t Q(L-t+1) | Written Cauchy/forcing deduction; needs weighted demand and a stronger regime-specific energy bound |
| A-SENSITIVITY | Exact hypothetical thresholds at six representative input rows | Reproducible rational calculation; not a theorem supplying a new cap; endpoint-domain assumptions retained |

All objects are finite integer sources with at most two colors, actual
coordinates, and the directed equal-leg L. No full-square extension is
asserted. The pinned base and artifact hashes identify the evidence.

## Proposed next task, subject to integration

Use Claude's B result to formulate one quantitative alternative: either the
fixed consumer's weighted fiber deficit meets the A0 threshold, or its
near-saturation controls collisions sufficiently to bound the request union.
Name the precise cap and weight before searching. Test the reflected-Golomb
family first; it must fall on the large-deficit side, not be silently excluded.
If no such statement has a credible consumer, use a different forcing statistic.

Codex has not started round 2. First review Claude's actual P1/D1 package,
check shared-cell accounting, and obtain reciprocal review of this proof.

## Reproduction

From this worktree root, with Python and its standard library:

```text
python research/boundary_certificates_20261115/verify_four_rank.py
python research/boundary_certificates_20261115/verify_four_edges.py research/r4_binary_compatibility_20261114/external_windows
python research/r4_binary_compatibility_20261114/sensitivity.py
python research/r4_binary_compatibility_20261114/check_collision_family.py
```

All four commands were run successfully in this session. Numerical jobs were
sequential and short; no solver or enumeration ran unattended. Read-only
internal helpers supplied theory and source review, not a replacement for
the external Claude partner. No remote write was performed.
