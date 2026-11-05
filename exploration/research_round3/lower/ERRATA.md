# Append-only Route-5 correction record

## R3-R5-E1 — trivial proof smoke was nondiscriminating

The frozen P5.2 prediction said at least one installed PySAT solver would emit
a nonempty proof on the tiny UNSAT smoke instance `[[1],[-1]]`.  All tested
solvers (`cadical195`, `cadical300`, `glucose3`, `glucose4`, `lingeling`)
returned raw UNSAT and an empty proof list.  This contradicts the literal
prediction, so the proof-tool branch halted before any n=21 use.

Root cause: a contradiction already present by unit propagation can legitimately
require no learned proof steps, so nonemptiness on this formula does not
discriminate between working proof logging and absent proof logging.  Resume
condition: retest on a nontrivial UNSAT formula requiring a derived step and
record exact proof content.  Until an independent checker is identified and a
nontrivial trace checks, solver UNSAT remains telemetry only.

The first replacement (all four binary clauses on two variables) was still
eliminated with an empty returned trace by every solver and remained
nondiscriminating.  The second replacement used `PHP(5)` (30 variables, 81
clauses).  Glucose3, Glucose4, and Lingeling then returned nonempty textual
proofs; CaDiCaL 1.9.5 and 3.0.0 still returned empty lists through this wrapper.
The proof-emission branch may resume with Glucose/Lingeling, subject to an
independent checker.  This does not repair or erase the original prediction
mismatch.

## R3-R5-E2 — Lingeling proof mode is not bounded through PySAT

The planned second hard-cube worker used Lingeling because the PHP(5) smoke
showed nonempty proof output.  Before any hard cube ran, the exact portfolio
API smoke (`with_proof`, `set_phases`, `solve_limited`, interrupt/clear) raised
`NotImplementedError: Limited solve is currently unsupported by Lingeling`;
even `clear_interrupt` is unsupported.  The portfolio branch halted with zero
hard cubes attempted.  Root cause: proof-output support and bounded-interface
support are separate wrapper capabilities.  Resume condition: select the
second solver only after it passes the exact combined API smoke.  Lingeling is
excluded from bounded workers in this environment.

## R3-R5-E3 — MapleCM accepted interrupts but did not honor the live cap

The exact PHP(5) API smoke established that MapleCM accepted `interrupt`,
`clear_interrupt`, and `solve_limited`, but PHP(5) finished before the timer and
therefore did not test a live interruption.  In the hard-cube worker, MapleCM
returned five 60-second interruptions, then failed to return from cube 6 for
more than an additional 120 seconds.  This contradicted the per-cube 60-second
stage specification.  The MapleCM process was stopped; its five fully returned
records are retained and the in-flight sixth cube has no record.

Root cause: accepting the limited-solve API did not guarantee that this solver
honors asynchronous interruption on the hard instance.  Resume condition: do
not use MapleCM again; assign only the 19 untouched shard-1 cubes to Glucose3,
whose wrapper shares the bounded interface already exercised by Glucose4.

## R3-R5-E4 — parallel affine continuation missed its completion forecast

P5.6 predicted that the second affine epoch would attempt all 24008 remaining
parameter pairs within 300 seconds.  Running concurrently with two 60-second
hard-cube workers, it attempted only 4198 pairs before the wall cap.  All 4198
returned raw UNSAT and none hit the conflict budget, but `24008-4198=19810`
pairs remain unattempted.  The prediction was contradicted and the affine route
halted.

Root cause: the completion forecast extrapolated the first epoch's throughput
without accounting for contention from both portfolio workers.  Resume
condition: wait until the hard-cube portfolio releases its cores, freeze a new
budget for the exact remaining deterministic pair indices 23114 through 42923,
and keep the negative family status UNDECIDED regardless of raw statuses.

## R3-R5-E5 — Glucose4 shell status disagreed with its completed artifact

The Glucose4 worker wrote a final JSON reporting all 24 shard-0 targets
attempted, all 24 interrupted, and mathematical status UNDECIDED, then its
managed shell session reported exit code 1 with no error text.  The script's
declared return path is 0, so the shell status and completed artifact disagree.
The affected integration branch halted; no solver result is promoted from the
process status.

Root cause is not established from the empty error stream and is recorded as
an execution-wrapper anomaly.  Resume condition: parse the final JSON afresh,
check all 24 records against the immutable cube manifest, hash the artifact,
and require the independent 48-cube merge audit to pass.  Since every recorded
status is already UNDECIDED, this anomaly cannot create a false SAT or UNSAT
claim.

The Glucose3 recovery worker later showed the same pattern: it wrote a complete
final JSON for all 19 recovery cubes (all interrupted, status UNDECIDED), then
the managed shell session reported exit code 1 without error text.  This
repeat supports an execution-wrapper/solver-cleanup explanation but does not
establish it.  The same resume condition applies: accept only records that pass
fresh parse, hash, and exact cube-manifest checks.

## R3-R5-E6 — affine throughput remained low after one worker finished

P5.8 predicted that the final 19810 affine parameter pairs would finish within
300 seconds after Glucose4 released one core.  Only 2989 pairs were attempted;
all returned raw UNSAT and none hit the conflict budget.  Together the three
epochs cover deterministic indices `0..26102`, exactly 26103 pairs, leaving
`42924-26103=16821` unattempted.  The prediction was contradicted and the
affine scan halted.

Root cause: the prior explanation in R3-R5-E4 was incomplete.  Solver cost per
parameter also rose at the larger moduli reached by later deterministic
indices, so throughput from the low-modulus first epoch did not extrapolate.
No further raw-UNSAT scan is justified without either a certificate plan or a
new algorithmic premise.  The exact difference-circulant theorem remains
valid independently of this scan.
