# Round 1 report: quotient colors and multiscale averaging

**No new Ramsey bound is established.** The round produced a proved structural
lower bound, a checked counterexample to its sharp three-L formulation, a
geometric obstruction to arbitrary combinatorial-subselection averaging, and a
corrected contiguous-block weighted inequality.

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

## Consumer decision

The initial all-combinatorial-subsquare mechanism is invalid because arbitrary
row and column selections do not preserve equal-leg geometry. The corrected
contiguous-block result is

```text
sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2.
```

The incumbent R_4 capacity certificate does not provide an upper bound on this
pair-tight incidence. Therefore the inequality supplies no contradiction and
no numerical improvement. The route is stopped at this interface gap; larger
random samples or larger finite blocks would not answer that missing upper
bound question.

## Implementation corrections retained for audit

Development prototypes initially mis-enumerated the seven palette sides and
used an incorrect total-L formula. Self-tests and independent verification
exposed both implementation errors. The more serious mathematical error was
the attempted use of arbitrary combinatorial subsquares; it was caught when the
resulting impossible density growth prompted a geometry review. All final
outputs were regenerated after correction. No earlier output is a result.

## Classification

- New mechanism: quotient signatures and a contiguous-block incidence
  inequality; structural value only, apparently new within the repository
  records searched, with no worldwide novelty claim.
- Technical improvement: independent finite witness and incidence checkers.
- Numerical Ramsey bound: unchanged.
- Next route: off-diagonal words coupled to the main diagonal, after refreshing
  the remote frontier. Do not continue quotient sampling without a new
  upper-bound consumer.

## Reproduction

From the repository root with Python 3.12.16 and only the standard library:

```text
python research/kimi_r4_quotient_multiscale_20261115/quotient_probe.py --samples 2000 --output research/kimi_r4_quotient_multiscale_20261115/quotient_results.json
python research/kimi_r4_quotient_multiscale_20261115/verify_results.py research/kimi_r4_quotient_multiscale_20261115/quotient_results.json
python research/kimi_r4_quotient_multiscale_20261115/averaging.py --output research/kimi_r4_quotient_multiscale_20261115/averaging_results.json
python research/kimi_r4_quotient_multiscale_20261115/verify_averaging.py research/kimi_r4_quotient_multiscale_20261115/averaging_results.json
```

Expected independent statuses: PASS for the stored example and PASS for exact
contiguous-block arithmetic. These are internal reproducibility checks, not
external peer review or Lean formalization.
