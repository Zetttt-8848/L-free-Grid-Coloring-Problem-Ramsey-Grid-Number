# R3-JOINT correction and prediction-deviation log (append-only)

R3-JE0: J3's frozen forecast required a score decrease and did not predict
that the600-second run would reach zero. The run did reach zero, so the
expected research status of the checkpoint changes from potentially
UNDECIDED to a positive candidate, then PROVED after independent checking.
This is an unforecast positive outcome, not a specification contradiction:
the frozen prediction did not claim zero impossible. The exact cause is
a successful search in the joint feasible space. Preserve both original
prediction and literal output; do not silently reinterpret the result as
a grid coloring. J4/J5 were frozen before their dependent execution.

R3-JE1: the single-class CP run is stopped at root's direction after the
same mathematical feasibility question has a verified positive witness.
Its saved solver log remains an interrupted, UNDECIDED engineering run;
the witness, not that log, establishes the positive result. No global
termination or UNSAT claim is made.

J6 frozen before completion-triangle execution: encode all actual L
corners inside T(A) for the canonical literal155-set, with two colors
because every cell is a completion of two diagonal points of the same
third color. Predict this stronger literal triangle may be UNSAT, but no
negative theorem will follow without a checked proof. The exact corner
count is not forecast; enumerate and save it before solving. Use a
600-second solver budget and preserve any proof output. A failed witness
lift redirects to forced-pattern cuts, not a change in the one-class YES.

R3-JE2: T(A) Glucose4 returned false after17 conflicts, but get_proof()
returned an empty list despite proof mode. Halt the negative-claim path:
the output is only unverified solver telemetry. An empty file is not a
proof. Root cause under investigation is this environment's proof capture;
preserve the raw result. Resume via a separate small-core extraction and
an independently checkable explicit RUP refutation.

J7 frozen before extraction: seek an inclusion-minimal subset B of the
literal155-set whose two-color completion triangle is unsatisfiable.
Predict a core with at most30 marks can be found by prefix search and
greedy mark deletion. Solver status here selects a candidate only. Generate
a DRAT-compatible RUP proof with a separate exact DPLL implementation and
check each proof addition using an independent unit-propagation checker.
If this fails or exceeds resources, the negative claim stays UNDECIDED.
