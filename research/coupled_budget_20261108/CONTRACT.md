# Coupled-budget research checkpoint

Base: `df6e35cfff68580dc78aa91bc35d4c6399a6464a` (PR #4, still open at start).
Date: 2026-11-08. This continues the research goal rather than reclassifying the
previous counterexamples as a Ramsey-bound improvement.

Target: improve the unconditional interval `21 <= R3 <= 493` by a complete
3-color square witness or a complete impossibility argument. The geometry is
exactly `(x,y),(x+d,y),(x+d,y+d)`, integer `d>0`; coordinates start at zero.
Strict two-colored sources and complete three-colored squares are distinct.

Routes with independent failure mechanisms:

1. `numeric_upper/`: coupled finite shift/interval counting with authenticated
   Golomb capacities and exact certificates; no assumed G9 or S21.
2. `lower/`: use certified obstruction supports to choose actual interior
   recolorings; run bounded complete-square search and compare controls.
3. `structural/`: retain external fields and true overlap multiplicities in
   a globally summable budget or prove a precise obstruction to one.
4. Coordinator: independently derive/check the load-bearing implication,
   reconcile evidence, and publish all substantiated results and code.

Each route writes only its assigned directory, retains source/inputs and
SHA-256, actual tested range, run status, first unresolved implication, and
next discriminating continuation. Solver timeout is UNDECIDED. A smaller
relaxation certificate requires a proof it applies to every original coloring.
New results are not called globally original without a separate source audit.

The previous 45-cell energy reversal forbids deducing local balance from global
potential minimality. The previous 20-square support packings forbid assuming
a frozen seed or tiny unverified repair can extend. New work must address
those obstructions rather than repeat them with larger radius or more seeds.

Publication: a new research branch based on PR #4; preserve old proofs and
certificates. Do not modify the main manuscript without a justified audited
mathematical dependency change. Final report separates numerical bounds,
general lemmas, exact finite evidence, heuristics, and remaining gaps.
