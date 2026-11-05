# Self-verification report

## Definition and encoding — PASS

The property is pinned to `((x,y),(x+d,y),(x+d,y+d))` with positive `d` and
all three cells in the full square.  The generator and the independent audit do
not import one another.  The audit reconstructed the complete expected clause
multiset directly from the property and obtained an exact match to the DIMACS
file.  It separately checked all 81 cube tuples and all assumption literals.

Boundary regressions covered `n=1,2,5,21`.  At `n=1` the geometric-corner
count is zero; at `n=21` the independent loop and sum-of-squares formula both
give 2870.

The inherited phase checkpoint was parsed independently as exactly 441 values
in `{0,1,2}`.  Direct enumeration checked all 2870 corners and reproduced its
eight-conflict description before it was used as a phase hint.

## Quantitative claims — PASS

`exact_claims.py` used only Python integers and `Fraction`.  All exact checks
passed: 1323 variables; 2870 corners; 10374 pre-symmetry clauses; 10815 total
clauses; 81 cubes; 546 nominal first-stage solver seconds; 33 certified easy
cubes plus 48 unresolved cubes; 42924 affine parameter pairs, of which 26103
were attempted and 16821 remain; inherited gap 444 and ratio `155/7`.

## Positive-witness discipline — PASS

No side-21 matrix was produced or claimed.  The restricted side-3
difference-circulant matrix contains exactly three symbols and the independent
verifier checked all five mandated corners with zero violations.  Its SHA-256
is `6c6f355fb14605b05d54e4dace6590a8d7dbd00e4ea34fd578d1400c1dc528cb`.

## Negative-certificate discipline — PASS at stated scope

The independent RUP checker directly unit-propagated the base CNF plus cube
units to contradiction for exactly 33 cubes.  It checked the same 33 orders as
the first-stage raw-UNSAT set.  This proves only those disjoint subinstances.
All 48 other cubes interrupted in both the initial and 60-second portfolio
stages.  They have no negative certificate and keep the global result
UNDECIDED.

No local general DRAT/LRAT checker was found.  Glucose3, Glucose4, and
Lingeling emitted nonempty traces on the separate PHP(5) interface test, but
Lingeling lacks bounded solving through this wrapper.  No unverified solver
trace is used as a bound.

## Prediction and R10 audit — PASS

The first-stage status counts matched the frozen forecast.  Six discrepancies
in proof-smoke discrimination, Lingeling bounded support, MapleCM live
interruption, affine throughput, and post-artifact shell status were halted and
recorded append-only in `ERRATA.md` before the relevant branch resumed or was
closed.  None changes mathematical status.

## Final honesty labels

- Side-21 decision: **UNDECIDED**.
- Nonexistence of solutions in the 33 easy cubes: **PROVED** by direct unit
  propagation, scoped to those cubes.
- Existence/nonexistence in each of the 48 hard cubes: **UNDECIDED**.
- Difference-circulant ceiling `n<=3` and equality at 3: **PROVED** for that
  family only.
- Modular-affine side-21 scan: **UNDECIDED**; 26103 raw-UNSAT calls are
  telemetry, 16821 pairs are unattempted, and no negative proof is present.

CLAIM: T_21=2870 geometric corners | MY VALUE: 2870 | THEIR VALUE: 2870 | VERDICT: PASS | METHOD: independent integer sum sum_{d=1}^{20}(21-d)^2 and closed sum-of-squares formula

CLAIM: side-21 encoding has 1323 variables and 10815 clauses | MY VALUE: 1323 variables and 10815 clauses | THEIR VALUE: 1323 variables and 10815 clauses | VERDICT: PASS | METHOD: independent clause-family reconstruction and exact DIMACS multiset comparison

CLAIM: the split has 81 exhaustive disjoint cubes | MY VALUE: 81 unique tuples covering {0,1,2}^4 | THEIR VALUE: 81 exhaustive disjoint cubes | VERDICT: PASS | METHOD: exact tuple-set and literal-map enumeration

CLAIM: the phase hint is a valid three-symbol side-21 grid with 8 conflicts | MY VALUE: 441 entries in {0,1,2}, 2870 corners inspected, 8 conflicts | THEIR VALUE: valid three-symbol side-21 grid with 8 conflicts | VERDICT: PASS | METHOD: independent JSON parsing and direct corner enumeration

CLAIM: 33 easy cubes are contradictory by unit propagation | MY VALUE: 33 independently propagated contradictions | THEIR VALUE: 33 easy cubes | VERDICT: PASS | METHOD: direct Boolean unit propagation on the exact CNF conjoined with each cube's four units

CLAIM: project-local inherited endpoint gap is 444 with ratio 155/7 | MY VALUE: gap 444 and ratio 155/7 | THEIR VALUE: gap 444 and ratio 155/7 | VERDICT: PASS | METHOD: exact integer subtraction and Fraction reduction
