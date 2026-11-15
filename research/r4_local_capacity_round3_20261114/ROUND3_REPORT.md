# Round 3: R4 <= 21,947,865

**Result: an unconditional computer-assisted improvement by 12 positions**
over the previous 21,947,877 certificate. This is a modest numerical advance,
not an exponent improvement. See [THEOREM.md](THEOREM.md) for the complete
dependency chain from an arbitrary four-color square.

Base: fdaa1f05ad8fc12f4f890117fde1b25e8b6d3d83.
Branch: codex/r4-local-capacity-round3-20261114. Date: 2026-11-14.
The owner authorized continuation and publication while Claude's first round
remains unfinished. This round stays in Codex's binary-source lane.

## Results and attribution

| Input / consumer | Certified outcome |
|---|---|
| All subsets in 8 positions, with every proper binary source allowed | Exact maximum 7 marks |
| All subsets in 12 positions | Exact maximum 9 marks |
| All subsets in 16 positions | Exact maximum 11 marks |
| All subsets in 20 positions | 12 <= maximum <= 14; exact value unresolved |
| Existing uniform rank information transferred to endpoints | Discrepancy about 217.325810 |
| Nonuniform rank transfer, no finite seeds | Discrepancy about 219.003380; R4 <= 21,947,866 |
| Nonuniform transfer with checked finite seeds | Discrepancy about 219.441283; using D=1097/5 gives R4 <= 21,947,865 |

The no-finite comparison was also run with its full exact rational discrepancy,
not just its rounded value 219, and still yields 21,947,866 in the tested
consumer. Thus the measured finite-seed contribution is one further position.
This does not establish global optimality of either method.

The new input retains joint physical coloring constraints over entire local
sources. The rank and window consumers are inherited techniques. Eleven of
the twelve saved positions are a technical integration improvement; one is
attributable to the new finite-compatibility input in this comparison. No
worldwide novelty claim or improvement to R3 is asserted.

## Verification completed

1. Every stored finite CNF was reconstructed independently from geometry and
   the exact cardinality semantics. Five complete refutations (including one
   redundant 12-position check) passed the standard DRAT-trim checker.
2. All 15 supplied complete source witnesses passed literal physical-L checks.
3. A separately authored arithmetic verifier, importing no discovery functions,
   checked all stored rank-span bounds, the endpoint discrepancies, 201 Golomb
   thresholds, all 566 binary interval rows for each comparison, the twenty-shift
   recurrence, and the full-square contradiction.
4. The original rational matrices were replayed through the inherited checker,
   including all coarse coverage checks and reconstruction of input coefficients.
5. The final positive margin is exactly

       667767862929561436134957406955093129954012400.

The independent arithmetic implementation uses interval integration rather
than the author's tail-subtraction calculation, power sums rather than
interpolation for correlations, and capacity-interval summation rather than
per-lag lookups in the outer count. See ENCODING_REVIEW.md and NUMERIC_REVIEW.md.
These are internal reviews, not external peer review or Lean formalization.

## What remains unresolved

The 20-position/13-mark, 24-position/18-mark, and 32-position/24-mark solver
runs returned UNDECIDED at the chosen 100,000-conflict limit. They contribute
no exclusion or cap. No larger search was launched automatically.
There is no claim that the final tested side is optimal.

The full square theorem depends on exact rational window data, elementary
geometric/counting lemmas, and checked finite proof traces. It does not depend
on a conjectural binary-source inequality or on the rounded Sidon constants
from an older branch. The standard checker, its compiler, and the executable
arithmetic implementations remain part of the computational trust base.

## Reproduction

Read TOOLS.md to obtain the pinned DRAT-trim source and compile it. From the
repository root, replacing CHECKER with its executable path:

```text
python research/r4_local_capacity_round3_20261114/audit_finite.py --checker CHECKER
python research/r4_local_capacity_round3_20261114/verify_numeric.py
python research/boundary_certificates_20261115/verify_four_edges.py research/r4_binary_compatibility_20261114/external_windows
```

The second command needs only the Python standard library. Replaying proof
archives requires no SAT solver. To reconstruct discovery inputs/results:

```text
python research/r4_local_capacity_round3_20261114/finite_caps.py CHECKER 4 8 12 16
python research/r4_local_capacity_round3_20261114/finite_caps.py CHECKER 20 24 32
python research/r4_local_capacity_round3_20261114/transfer.py
python research/r4_local_capacity_round3_20261114/consumer.py
```

Discovery uses PySAT. Every numerical job was sequential and short, within
one worker and the agreed pilot allocation. Helpers supplied theory, review,
and independent checker code, without running numerical jobs.
No shared manuscript was changed. The proof archives are losslessly compressed.

## Handoff and next discriminating task

Claude can use the updated binary capacity profile directly as an input to
its ternary lane, after reviewing the new contribution. Keep the full profile
and its p-dependent conditions; do not add this gain arithmetically to another
result charging the same cells.

Before attempting larger finite intervals, compute the endpoint and final-side
sensitivity to the particular proposed stronger cap. The successful bridge
is now explicit: checked local color compatibility -> hereditary span costs ->
endpoint variance -> binary capacities -> outer contradiction. Future searches
should be selected by that consumer, not by merely increasing n.
