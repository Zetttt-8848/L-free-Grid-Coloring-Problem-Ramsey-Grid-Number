# Structured subtask report

**Sub-Task ID:** `R3-R5-L2`

**Assigned Model:** GPT-5.6 Sol, xhigh (Level 2 solver engineering and bounded
construction work; theorem and global exact-value judgments remain with the
root).

**Task Statement:** Launch a substantial, sound side-21 decision attempt using
the one-hot CNF and exact 81-cube cover; raise budgets by orders of magnitude;
retain exact encodings, hashes, cube telemetry, witnesses or proofs; seek
proof-capable tools; independently verify any candidate; and test a restricted
circulant/modular construction premise distinct from the closed injective
product family.

## PROPERTY (formal)

The universe is every total labeled map
`chi:{0,...,20}^2->{1,2,3}`.  The predicate requires that for every
`0<=x,y<21` and `1<=d<min(21-x,21-y)`, the colors on
`((x,y),(x+d,y),(x+d,y+d))` are not all equal.  There are exactly 2870 such
geometric triples.  A witness proves `R_3(L)>=22`; certified nonexistence,
combined with the inherited side-20 witness, would prove `R_3(L)=21`.  Color
permutation is the only quotient used by the solver.

## CHANNEL USED

**C1 solver-assisted search:** used.  The independently audited one-hot CNF has
1323 variables, 10374 clauses before symmetry, and 10815 after 441 sound color-
symmetry clauses.  Its SHA-256 is
`49a989044d4255e7aba75a0b45256a7b480172b8f121545eeaf350164177f8e5`.
All 81 assignments to four pinned split cells occur exactly once.

Stage 1 revisited all cubes: the 33 formerly easy cubes received 2 seconds and
the 48 formerly open cubes received 10 seconds, nominally 546 solver seconds
under a 600-second global cap.  MapleChrono finished in 481.0631858 measured
wall seconds with 33 raw UNSAT, 48 interrupted, and zero SAT.  Independent
unit propagation certifies exactly the 33 easy cubes.

At the root's checkpoint direction, the 48 hard cubes then received 60 seconds
each, 120 times the Round-2 half-second cap.  Glucose4 handled 24, MapleCM
returned five before its live-interrupt failure, and Glucose3 handled the
remaining 19.  The exact merge audit passed: all 48 expected cubes occur once,
all assumptions match, and every status is INTERRUPTED_UNDECIDED.  No solver
found a witness, raw UNSAT, or proof trace in this stage.  Glucose4 recorded
26,973,522 conflicts; MapleCM's five completed records 4,910,445; and Glucose3
23,114,131.  These are telemetry only.

The largest per-cube conflict counters, retained only as search telemetry, were
Glucose3 cube 57 with 1,512,254, Glucose4 cube 71 with 1,482,469, and MapleCM
cube 3 with 1,149,174.  Every one still ended at its wall cap, so “largest”
does not imply closest to a decision.  The complete per-cube assumptions,
times, counters, and statuses remain in the worker and merged JSON files.

Proof-tool audit found nonempty PySAT proof traces on PHP(5) from Glucose3,
Glucose4, and Lingeling.  No standalone DRAT/LRAT checker was found locally.
Lingeling does not support bounded solving through this wrapper.  The custom
independent checker supports RUP, not general RAT; it certified the 33 direct
unit contradictions and was not used to overstate any hard cube.

**C2 explicit construction:** used.  A new exact theorem closes the restricted
difference-circulant family `chi(x,y)=f((y-x) mod m)` at side 3, with a complete
verified equality witness.  The broader modular-affine family
`chi(x,y)=f((a*x+b*y) mod m)` was searched at side 21 for deterministic pair
indices 0 through 26102 over the frozen range `2<=m<=50`.  All 26103 attempts
returned raw UNSAT without proof; 16821 pairs remain unattempted.  This is
UNDECIDED telemetry and yields no general or finite-family impossibility claim.

**C3 probabilistic method:** deferred.  The Round-2 naive alteration route is
closed because the retained partial domain need not contain an affine square;
no new affine-structure premise was found, so it was not retried.

## WITNESS + CERTIFICATE

For the side-21 target: **none**.  No complete matrix was generated.

For the restricted difference-circulant theorem: the complete equality witness
is `difference_circulant_n3.txt`; the direct verification record is
`difference_circulant_n3_verify.json`.  It has balanced color counts `(3,3,3)`,
checks all five corners, and has zero violations.

For scoped negative evidence: `n21_quick_cube_rup_audit.json` contains the 33
direct unit-propagation verdicts.  The other 48 cubes have no negative
certificate.

## VERIFICATION METHOD

1. Rebuild and audit the instance independently:
   `python audit_instance.py --n 21 --cnf n21_exact.cnf --cubes n21_cubes.json --output n21_instance_audit.json`.
   This reconstructs the property clauses without importing the generator and
   compares the entire clause multiset, cube tuple set, and literal map.
2. Check scoped easy-cube contradictions:
   `python check_rup_proofs.py --cnf n21_exact.cnf --proof-manifest n21_quick_cube_proofs.json --output n21_quick_cube_rup_audit.json`.
   The checker directly unit-propagates the base clauses and four cube units.
3. Reconcile the full checkpoint:
   `python audit_global_checkpoint.py --cubes n21_cubes.json --stage1 n21_stage1_maplechrono.json --easy-audit n21_quick_cube_rup_audit.json --hard-merge n21_stage2_portfolio_merged.json --output n21_global_checkpoint_audit.json`.
   Observed result: PASS, with `81=33+48`, exact disjoint union, zero SAT, and
   48 unresolved.
4. Check any positive matrix directly with
   `python verify_coloring.py MATRIX --n N --output CHECK.json`.  The parser
   rejects a wrong shape or any symbol outside `{1,2,3}` and enumerates every
   mandated corner.  This passed for the side-3 restricted-family witness; no
   side-21 matrix exists to check.

## BEST-KNOWN GAP TABLE

| Side | Certified bound | Exact meaning | Date/scope | Route | Evidence |
|---|---:|---|---|---|---|
| Construction lower bound | 21 | inherited valid side-20 coloring | inherited, project-local | prior campaign | accepted Round-2 release |
| Impossibility upper bound | 465 | inherited forcing at side 465 | inherited, project-local | weighted diagonal proof | accepted Round-2 release |

The exact integer gap is `465-21=444`; the exact endpoint ratio is
`465/21=155/7`.  This subtask did not move either endpoint.

## VERDICT

**UNDECIDED** for the side-21 existence/nonexistence question.  The complete
81-cube accounting is **PROVED**; 33 cubes are **PROVED UNSAT at their scoped
assumptions** by direct unit propagation; 48 cubes remain **UNDECIDED** after
the full 60-second portfolio.  No inference to `R_3(L)=21` or
`R_3(L)>=22` is licensed.

The restricted difference-circulant ceiling `n<=3`, with equality at 3, is
**PROVED** for that family only.  The partial modular-affine scan is
**UNDECIDED** and has no Ramsey-bound implication.

## Result

The campaign interval remains `21<=R_3(L)<=465`.  The main durable progress is
a fully audited side-21 encoding/cube package, proof-level closure of 33 cubes,
and exact identification of all 48 hard cubes after 60-second independent
solver treatment.  The strongest new construction result is a narrow family
ceiling and does not improve the inherited side-20 witness.

## Self-Check

The exact-verify environment printed `ENVIRONMENT OK`; Route-5 self-tests pass;
the independent CNF/cube audit, 33-cube RUP audit, 48-cube merge, and global
checkpoint audit all pass.  Six R10 entries are preserved append-only.  Solver
telemetry and mathematical proofs are separated throughout.

## Confidence

High for the formal encoding, exact counts, cube coverage, 33 direct unit
contradictions, 48-cube unresolved status, and restricted circulant theorem.
No confidence is assigned to global nonexistence at side 21 because every hard
cube lacks a certificate.  The absence of a found witness is not evidence of
nonexistence.

## Dependencies

The inherited project-local interval `21<=R_3(L)<=465` and accepted side-20
witness/theorem package; PySAT 1.9.dev15 for search telemetry; the exact local
CNF and independent Python checkers for new scoped certificates.  No result
depends on the root's primary cap or joint-model branches.
