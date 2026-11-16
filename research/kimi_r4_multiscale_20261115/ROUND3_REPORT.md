# Round 3 report: incidence erratum and closure of quotient-count scaling

**No new Ramsey bound is established.** This round found and corrected a serious
error in Kimi's round-1 Q3a, supplied a complete finite counterexample, and
proved that the proposed multiscale pair-tight and seven-quotient counts have no
Ramsey consumer.

Branch: `kimi/r4-multiscale-20261115`.
Base: `af166bc27aaa3f22b4f62907d983fbecb20f4aec`.
Date: 2026-11-15. Author: Kimi.

## Preregistration and nonduplication

The remote frontier, all repository branches, and all open PRs were refreshed
before computation. The contract was pushed at commit
`f81582ee8b307b17b796655952cdaa76e3d44e7b` before running the experiment.

Codex remains in binary-source capacities, rank transfer, collisions, short
requests, and exact windows. Claude remains in ternary-source compatibility,
MS*, prefix certificates, and local triangle refutations. PR 11's newest fork
head reports weighted rainbow and window bounds; those reports were read to
avoid overlap but were not adopted or audited. No conditional statement is used.

## Exact outcomes

1. **Old Q3a is REFUTED.** A proper 6 by 6 four-coloring has
   `P_d=(6-d)^2`, so the old left side is `1381/144`, below the claimed right
   side 12. All 55 Ls were checked by two new implementations and by the
   project's standard coloring checker.
2. **The old multiplicity claim is REFUTED.** Boundary Ls have fewer than
   `(5-d)^2` block occurrences; at `(0,0;1)` in sides 5 and 6 the actual count
   is one, not 16.
3. **The pair-tight count is geometric, not chromatic.** Every three-cell word
   in four colors has a nonempty quotient signature. Thus `P_d=(n-d)^2` for
   every coloring, including a monochrome square.
4. **The exact multiscale identity is trivial.** Every 5 by 5 copy has 30 Ls,
   so the total copy-L incidence is `30 C_s`, with all boundaries and
   cross-block Ls included. Adding scales only gives `30 sum_s lambda_s C_s`.
5. **Seven-quotient averaging is dominated.** Its lower bound `7 C_s` is weaker
   than the universal `30 C_s` obtained from nonempty signatures. Its induced
   rainbow upper bound `(83/2) C_s` is weaker than the trivial `30 C_s`.

Q1 and Q2 are not refuted by this audit. The unweighted round-1 lower bound is
true but follows directly from the fixed geometric counts; its earlier proof is
withdrawn.

## Consumer decision and pivot

There is no valid chain from these identities to a Ramsey contradiction. The
count is unchanged even for an improper monochrome coloring. Further random
samples, larger quotient blocks, or more scales cannot repair that loss. The
route is therefore closed without a capacity run.

The next lane must be non-quotient and must use a coloring-dependent full-square
statistic with a stated upper-bound consumer. A two-dimensional color-class
energy representation is a candidate only after checking it against the
manuscript line identity and PR 11's weighted triangle work. If it is merely a
relabeling, the independent fallback is certified finite kernels as lemma
generators, not a bare UNSAT search.

## Verification history

The initial generator passed. The independent checker then caught two mistakes
in the new checker itself: an incorrect closed-form signature guess and a 54
versus 55 subtotal that omitted step 5. Both were corrected explicitly. A
canonical ordering was added to multiplicity hashes after the independent
programs used different enumeration orders. The final rerun regenerated the raw
output and passed every check.

Final coverage:

- 64 three-cell color words;
- 36 cells and all 55 Ls of the proper witness;
- all four contiguous 5-blocks in the proper and monochrome 6-squares;
- six scale rows and 1,063 individually reconstructed L-copy multiplicities;
- exact rational arithmetic for the counterexample and quotient-incidence gap.

No SAT/UNSAT claim, external peer review, Lean formalization, or numerical
Ramsey improvement is asserted.

## Reproduction

From the repository root, using Python 3.12.16 and only the standard library:

```text
python research/kimi_r4_multiscale_20261115/audit_incidence.py research/kimi_r4_multiscale_20261115/counterexample_6.json --output research/kimi_r4_multiscale_20261115/audit_results.json
python research/kimi_r4_multiscale_20261115/verify_audit.py research/kimi_r4_multiscale_20261115/counterexample_6.json research/kimi_r4_multiscale_20261115/audit_results.json --output research/kimi_r4_multiscale_20261115/verification.json
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py research/kimi_r4_multiscale_20261115/counterexample_6.json
```

To regenerate the witness from the archived 20-square without changing that
source:

```text
python research/kimi_r4_multiscale_20261115/prepare_counterexample.py .agents/skills/directed-l-grid-research/assets/paper20.json research/kimi_r4_multiscale_20261115/counterexample_6.json
```

Expected final independent status: PASS. The old `averaging.py` and
`verify_averaging.py` are retained only as historical artifacts; their Q3a
status is withdrawn and their old PASS label must not be used.
