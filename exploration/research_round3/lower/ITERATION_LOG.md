# Route-5 iteration log

## 2026-09-10 — setup and first escalation

- Exact-verify environment self-test: `ENVIRONMENT OK`.
- Route self-tests: passed pinned variable, corner, clause, and RUP regression
  checks.
- Independent instance audit: PASS for 1323 variables, 2870 corners, 10815
  clauses, all 81 unique cubes, and exact coverage.
- MapleChrono bounded-interface smoke: PASS.
- Stage 1: all 81 cubes attempted with 2-second caps on 33 formerly easy cubes
  and 10-second caps on 48 formerly open cubes.  Result: 33 raw UNSAT, 48
  interrupted, 0 SAT; total 481.0631858 wall seconds.  Global status UNDECIDED.
- Independent direct unit propagation: PASS on all 33 easy augmented cube
  CNFs.  This certifies only those 33 disjoint cubes.
- Modular-affine scan first epoch: 18916 of 42924 parameter pairs attempted in
  the frozen 180-second wall cap; all returned raw UNSAT, no SAT or conflict-
  budget interruption.  The 24008 unattempted pairs and absent proof
  certificates leave the family result UNDECIDED.

## 2026-09-10 — hard-cube portfolio

- Exact combined API smoke found Glucose4 usable with nonempty proof output and
  MapleCM usable for bounded phase-guided solving but returning empty proof
  output on the smoke instance.
- Lingeling was excluded after the R3-R5-E2 interface halt.
- The 48 hard cubes were split deterministically into two 24-cube shards.  Each
  cube receives 60 seconds; Glucose4 handles shard 0 and MapleCM shard 1.
- MapleCM produced five capped interruption records, then failed to honor the
  sixth live timer and was halted under R3-R5-E3.  Glucose3 handled exactly the
  remaining 19 records.
- Final portfolio: all 48 hard cubes matched the immutable manifest and all 48
  ended INTERRUPTED_UNDECIDED.  Glucose4 handled 24, MapleCM five, and Glucose3
  19.  No SAT model and no raw UNSAT trace appeared.  The independent merge and
  global 81-cube coverage audits both passed.
- Global checkpoint: 33 cubes are certified contradictory by direct unit
  propagation; 48 remain unresolved.  The side-21 decision is UNDECIDED.
- Modular-affine scan: three epochs covered indices 0 through 26102, exactly
  26103 of 42924 parameter pairs.  No candidate appeared, but all negative
  statuses lack checked proofs and 16821 pairs remain unattempted.  Status is
  UNDECIDED.  Further raw scanning halted after R3-R5-E6.
- Difference-circulant theorem: PROVED exact ceiling side 3 in that restricted
  family; its 3 by 3 equality witness passed all five direct corner checks.
