# Provenance and actual computational scope

Base commit: `df6e35cfff68580dc78aa91bc35d4c6399a6464a`. Date: 2026-11-08.
Work package: `research/coupled_budget_20261108/numeric_upper/`.

## Certified deliverables

- `CONTRACT.md`: object, target, evidence standard, and outcome.
- `THEOREM.md`: complete geometric reduction, general joint endpoint lemma, exact 466 application, and independent reconstruction of the archived direct 465 proof.
- `inputs.json`: the only two external numerical inputs needed by 465 and 466, their primary completion reports, published corroboration, and archival locator.
- `verify.py`: integer-only standard-library checker. It does not import `capacities.py`, SciPy, or any scouting result.
- `results.json`: actual output, input/proof hashes, all endpoint-scan rows, full 93-weight autocorrelation, and the small partition check.

Command: `python research/coupled_budget_20261108/numeric_upper/verify.py` from the repository root, or `python verify.py` in this directory. The checker rewrites only its own `results.json`. Actual environment: CPython 3.13.5, Windows x64. The numerical checks completed with `PASS`:

| Check | Exact outcome |
|---|---:|
| 466 selected pair count | 9493 |
| 466 lower distance | 319760 |
| 466 upper distance | 319539 |
| 466 contradiction gap | 221 |
| Restored 465 grouped convolution gap | 285630 |
| Restored 465 directly convolved Cauchy gap | 571260 |
| Restored 465 with integer occupancy refinement | 286095 |
| Exhaustive small partition/cutoff cases, lengths at most 9 | 15168 |

The endpoint scan covers every side `300,...,480` and every positive cutoff certified by the pair-budget minimum-class bound stated in the theorem. Its first positive result is `n=466,c=22`; at 465 the best tested gap is `-336,c=21`. These negative values describe a specified inequality, not feasible square colorings or a universal method barrier.

The exact-verify environment self-test was run before verification and returned `ENVIRONMENT OK`. The 465 computation rebuilds the autocorrelation by pairs of weight positions and also constructs the full convolution literally; it does not execute or adapt the archived checker. The publication arithmetic 493 was separately reconstructed from the paper's capacity table: with `n=493,c=12,m=165`, the 1902 selected pairs have greedy distance at least 37836, exceeding the endpoint allowance 37804 by 32. This auxiliary reproduction uses the fuller published table and is not a dependency of either improved certificate.

## Sources read and dependency classification

1. Mammel, Smith, Yerger, *Ramsey Theory on the Integer Grid: The “L” Problem*, **Integers 25 (2025), A21**, DOI [10.5281/zenodo.15090985](https://doi.org/10.5281/zenodo.15090985), [journal PDF](https://math.colgate.edu/~integers/z21/z21.pdf). Theorem 6 (pages 10–11) and Algorithm 3 (page 11) were checked, including the occupied-position convention. The [arXiv v1](https://arxiv.org/html/2502.05162v1) dated 2025-02-07 was also read for the interval method and Golomb reduction. These sources establish the 493 baseline and the antecedent method; they do not contain the 465 certificate asserted here.
2. [distributed.net November 2004 primary reports](https://blogs.distributed.net/2004/11/), entries dated November 1, confirm completed exhaustive OGR-24 optimality at span 425. The completion report identifies the final verified work unit, verification passes, and correction of the earlier omitted initial-mark category. This is the provenance of `G(24)>=425`.
3. [distributed.net October 2008 primary report](https://blogs.distributed.net/2008/10/), October 25 at 23:14, confirms exhaustive OGR-25 optimality at span 480 and the final verified work unit on October 24. This is the provenance of `G(25)>=480`.
4. Local `manuscript/main.tex`, diagonal exclusion/weak restriction and Golomb-class lemmas, was read. The reduction is reproved from physical coordinates in `THEOREM.md`.
5. Local `exploration/research_round4/checks/build_verification_report.py`, section “Direct conditional proof of the inherited three-color bound,” already contains the triangular-weight 465 calculation. Its external-input concern is addressed by sources 1–3. This prevents claiming the restored result as newly original.

Source access and local arithmetic occurred on 2026-11-08. No full distributed OGR search was downloaded or rerun. No DRAT/LRAT proof, Lean verification, or global literature-priority proof is asserted. Input facts and source locations are pinned in `inputs.json`, whose byte hash is in `results.json`.

## Retained exploratory computations

All scripts below were actually executed. They remain as research records, separate from the exact checker. They use the full table in the 2025 paper, in occupied-position convention; that table was not independently reproved. NumPy version 2.1.0 and SciPy version 1.16.3 were used for LP scouting.

| File | Executed range | Status and interpretation |
|---|---|---|
| `scratch.py` | sides 450–499; all cutoffs through half the selected class size | Integer single-class endpoint scout; first positive side in that scan is 493. |
| `water_scout.py` | sides 460,470,480,487,490,492,493,500,510,520; shifts 2–199 | Integer endpoint-capped waterfilling. At 493, shift 43 gives gap 116. It did not provide a smaller certified upper bound. Nonmonotonic output beyond 493 reflects table thresholds; the existence of a smaller forbidden square already excludes larger squares. |
| `transport_scout.py` | sides 493,492,490,487,481,475; cutoffs 13,25,50 | Floating-point single-class transport relaxation; no rational certificate supplied. |
| `full_transport_scout.py` | same six sides; every rank for the selected class | Floating-point transport relaxation with the corrected full-rank endpoint bound. `lp_candidate.json` records side 493, cutoff 164, objective about 0.63736 and dual coefficients. These are discovery values, not a proof certificate. |
| `joint_colors_scout.py` | sides 300–493; cutoffs 1–39 | Initial balanced-size coefficient scout. Balanced class sizes were only a discovery model; it is superseded for theorem purposes by the universal size argument and exact scan in `verify.py`. |
| `joint_transport_scout.py` | sides 466,465,464,463,462,460; cutoff 40 | Floating-point three-class transport scout. Raw objectives/dual coefficients are saved as `joint_lp_<n>_40.json`; no primal rational feasible witness or universal optimality proof is claimed. |
| `capacities.py` | imported by joint scouts and auxiliary reproduction | Published-table helper. Neither final certificate needs this broader table. |

The saved joint LP objective at side 466 is approximately 0.87352; at 465 it is approximately -1.33992, and at 464 approximately -3.50198. They helped choose the elementary certificate but do not establish a rigorous feasibility barrier below 466. The direct, exact endpoint proof and the restored convolution proof carry the theorem, independently of all floating-point results.

## Claim verdicts

The target inputs are the explicitly listed integers and weight definitions; the independent method reconstructs distances and autocorrelations. These arithmetic verdicts leave the external evidence tier above unchanged.

CLAIM: 466 rearrangement contradiction gap | MY VALUE: 221 | THEIR VALUE: 221 | VERDICT: PASS | METHOD: integer greedy capacities and sorted endpoint coefficients

CLAIM: archived 465 convolution contradiction gap | MY VALUE: 285630 | THEIR VALUE: 285630 | VERDICT: PASS | METHOD: autocorrelation from weight-position pairs checked against literal full convolution

CLAIM: first positive endpoint gap in the stated finite scan | MY VALUE: n=466,c=22 | THEIR VALUE: n=466,c=22 | VERDICT: PASS | METHOD: exact scan of sides 300 through 480 and all cutoffs allowed by the stated size bound

CLAIM: floating-point LP feasibility below 466 is exactly certified | MY VALUE: not established | THEIR VALUE: no exact certificate asserted | VERDICT: UNDECIDED | METHOD: rational primal verification was not performed; floating-point scout is retained only as exploration
