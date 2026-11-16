# Round 1 report: quotient colors and multiscale averaging

> **ERRATUM:** The displayed Q3a inequality, its density interpretation as a
> quotient result, and the contiguous-averaging PASS label are withdrawn. Q1,
> Q2, and the arbitrary-subselection obstruction are unaffected. See
> `ERRATUM.md` and the round-3 package for a complete 6-square counterexample.

**No new Ramsey bound is established.** The unaffected results are the Q1 cover
lower bound, the Q2 counterexample to its sharp three-L formulation, and the
geometric obstruction to arbitrary combinatorial-subselection averaging. The
later contiguous-block weighted inequality is withdrawn by this erratum.

Branch: `kimi/r4-quotient-multiscale-20261115`.
Base: `14647e607c2525b0cd12081b03899827d306a030`.
Date: 2026-11-15. Author: Kimi.

## Finite experiment

The preregistered deterministic probe used seed 20261115 and at most 2000
samples. It stopped at the first counterexample, as authorized by the contract.
Of 77 proper four-color 5 by 5 samples, 76 had exact quotient-cover size three
and one required at least four. Random generation made 559 attempts. This
distribution describes only the generated samples and is not an estimate over
a defined uniform distribution of proper colorings.

The stored counterexample passed a separate verifier that shares no code with
the generator. All 25 cells, all 30 Ls, all seven quotient signatures, and all
subsets of at most three Ls were checked. The probe also validated signature
sizes on all 64 three-cell color words, found a proper binary 4-square by
exhaustive enumeration, and checked 100 sampled binary 5-squares against the
known positive answer. The latter samples supplement but do not prove R_2=5.

## Corrected consumer decision

The initial all-combinatorial-subsquare mechanism is invalid because arbitrary
row and column selections do not preserve equal-leg geometry. The later Q3a
contiguous-block inequality is also false and is withdrawn. A proper 6-square
counterexample and the general triviality proof are in
`research/kimi_r4_multiscale_20261115/`.

Every L in every four-coloring is pair-tight for some quotient, so the proposed
pair-tight cardinality is only `(n-d)^2`. It cannot supply a coloring-dependent
capacity contradiction. Do not seek an upper-bound consumer for old Q3a.

## Implementation corrections retained for audit

Development prototypes initially mis-enumerated the seven palette sides and
used an incorrect total-L formula. Self-tests and independent verification
exposed both implementation errors. The attempted use of arbitrary
combinatorial subsquares was a geometric error. The subsequent Q3a multiplicity
and weighting error was caught only in round 3; the old averaging PASS label
was therefore not valid evidence for Q3a. Historical artifacts are retained,
but their mathematical claim is withdrawn.

## Classification after erratum

- Q1 quotient-cover lower bound and Q2 counterexample: unaffected.
- Q3a incidence inequality: REFUTED; no mechanism or technical improvement is
  claimed from it.
- Numerical Ramsey bound: unchanged.
- Next route after round 2 and the round-3 closure: non-quotient full-square
  statistics with a stated consumer.

## Reproduction of the unaffected Q2 witness

From the repository root with Python 3.12.16 and only the standard library:

```text
python research/kimi_r4_quotient_multiscale_20261115/verify_results.py research/kimi_r4_quotient_multiscale_20261115/quotient_results.json
```

The old averaging commands are intentionally omitted. Use the new independent
round-3 checkers for the erratum. These are internal reproducibility checks,
not external peer review or Lean formalization.
