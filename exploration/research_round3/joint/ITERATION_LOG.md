# R3-JOINT iteration log (append-only)

J1/J2/J3 executed after predictions were frozen. Direct model construction
confirmed all three predicted pair/AP specification counts. The J3 search
found a zero-score candidate before its declared cap. The independently
implemented checker passed the literal result, inspecting every distance
and every admissible AP. This positive result was not forecast, but does
not contradict the frozen statement that no zero score was presumed.

Result: PROVED existence of a 155-set in [464] satisfying the joint
one-class necessary conditions. No R3 bound movement follows. This
discriminates in favor of the partition/coupling alternatives. The earlier
CP-SAT search continues as a separate engineering benchmark; no negative
claim is permitted from it.

J4 frozen after J3 and before partition execution: seek a ternary word of
length464 with class sizes155,155,154, all per-class caps, and all six-APs
nonmonochromatic. This balanced family is sufficient for a positive
partition witness but is not complete for a negative partition theorem.
One600-second stochastic run with seed20260911 is predicted to reduce
its initial exact integer violation score; no zero score is forecast.

J5 frozen before solver execution: run a600-second exact CP-SAT model of
the general ternary partition plus a completion-closed lower diagonal
band of width20. Grid variables in this band take colors0,1,2. Include
every actual L-corner entirely in this band. This is a necessary condition
for a grid and a stronger partition test; any positive band assignment
still is not a full grid coloring. Prediction: bounded result may remain
UNDECIDED. Exact counts will be computed from the stated finite domain
and saved before solving; no count is presumed from an unverified formula.

J5 scheduling change: defer band CP while the root-prioritized triangle
core/cut loop runs. J4 partition stochastic remains active. This is a
route scheduling decision, not completion or mathematical exhaustion.

J7 outcome: the extracted9-mark pattern is certified by151 RUP additions
whose geometry and unit propagation were checked independently. Its
normalized offsets are P={0,1,2,3,4,6,7,9,11}. No six-AP occurs in P.

J8 frozen before cut/refind execution: forbid all translated positive
integer dilates of P and of 11-P, in addition to the original caps and
all six-APs. Predict each shape contributes9555 distinct copies in[464],
giving40408 forbidden hyperedges in total. Run one600-second search with
seed20260912. Predict score decreases; a zero score is possible but not
forecast. Any result is independently checked against the saved full
pattern list before triangle testing. No one-class negative conclusion
is inferred from this bounded heuristic.

Reflection proof: the cell map (x,y)->(-y,-x) preserves strict lower
triangles and maps each L-corner to an L-corner (after reordering its
three cells). It takes T(A) to T(-A). Translation and positive integer
dilation also preserve corners. Thus P and its reflection are both
necessary exclusions for any diagonal color class of an L-free grid.

J8 outcome: a second155-set satisfies all40408 exclusions and all caps;
the independent endpoint-based checker passes. Thus this finite added
pattern family alone is still insufficient for a one-class contradiction.

J9 frozen before execution: minimize a triangle obstruction inside the
second literal set. Predict a core with at most18 marks and an explicit
RUP refutation within the producer's60-second/1000000-node bound. Any
negative result without a verified proof remains unverified. If the
second complete triangle is feasible, save its entire coloring instead.

J9 outcome: a certified10-mark obstruction was found, with427 RUP
additions; both the literal set and its proof remain preserved.

J10 frozen before complete-window classification: for W=13, classify all
8192 support masks A subset{0,...,12} by two-colorability of T(A). Predict
the resulting capacity h(13) is at most11; no exact maximum is presumed.
Process masks by cardinality. A certified minimal bad mask excludes all
its supersets; a literal coloring of a maximal good mask certifies all
its subsets. Save both families and independently check that they cover
every mask with no contradictory coverage. Each bad mask receives a
separately generated RUP refutation; each good mask a full cell coloring.
Derive h(w) only for1<=w<=13 from complete coverage. Derive rank-span
consequences only within this finite verified window range. A600-second
preparation/proof budget is imposed; resource failure means UNDECIDED,
not completion. This is a complete local-window classification, beyond
the closed route of testing a few six-mark examples.

J11 frozen before paired-five-AP execution: add the root's geometric
lemma that each common difference admits at most one five-term AP in A.
The root's weak-triangle argument is recorded separately. At n464 there
are115 differences and26680 five-AP occurrences; independently derive
the count by summing464-4d for1<=d<=115. Retain caps and all57888
hyperedges from patterns_v2. Run600 seconds, seed20260913. Predict score
decreases; no feasible or infeasible mathematical outcome is presumed.
Zero score must be checked by direct enumeration of every AP5 group.

J10 outcome: the independent checker certified all8192 masks using109
minimal bad RUP proofs and334 maximal good colorings. The capacities for
widths1..13 are1,2,3,4,5,5,6,7,7,8,9,9,10. Thus minimum spans for
6..10 marks are6,7,9,10,12. All counts are in window13.check.json.

J11 outcome: a third155-set passes all caps, all57888 listed affine
exclusions, and every five-AP uniqueness constraint. The independent
checker passed every one of26680 AP5 occurrences. This is further positive
surrogate feasibility, not a grid coloring or a new lower bound.

J12 frozen before execution: normalize all109 certified minimal bad
supports from the complete width13 classification by subtracting the
minimum and dividing by the gcd of their offsets, then discard identical
normalized lists. Each original bad mask and every positive affine copy
is covered; dividing by a common positive integer preserves the corner
incidence and the certified impossibility. There can be at most109
distinct lists. Add all their affine copies, plus AP5 uniqueness and
the original caps, and run600 seconds with seed20260914. Predict a score
decrease; no zero or negative mathematical outcome is presumed. The rank
consequences are a_(i+7)-a_i>=9, a_(i+8)-a_i>=10, and
a_(i+9)-a_i>=12, in addition to the inherited six-rank restriction.

J13 frozen at the J12 checkpoint: its saved best candidate has reported
score1. Independently audit that score, preserve a stable snapshot, and
test every single mark-swap from that snapshot while keeping min A=1.
Predict at most155*464 proposals before filtering; no repair is presumed.
This finite neighborhood is not the full set space. Use the full caps,
all normalized window13 pattern copies, and AP5 uniqueness when checking
any candidate repair. A failure to repair has no non-existence implication.

J13 outcome: the snapshot's only violation is r_A(54)=47>46. All543170
pattern copies and AP5 uniqueness pass. All47586 single swaps were
tested; none meets every distance cap. This certifies no global claim.

J14 frozen before execution: accelerate the same objective by a rigorous
early rejection bound. Write the current score C+P where C is cap excess
and P>=0 is the weighted pattern/group penalty. After a proposed swap's
cap change dC is known, its full score change is at least dC-P. If this
exceeds the Metropolis acceptance threshold, reject before touching the
expensive pattern incidence lists. Otherwise compute the exact full
change. This preserves the acceptance rule for the sampled threshold.
Run600 seconds, seed20260915, from the preserved score1 snapshot. Predict
strictly fewer expensive evaluations than total proposals; no zero or
negative mathematical outcome is presumed. Retain the original run.

J14 outcome: the accelerated run found a zero-score literal155-set;
all463 distance caps, all543170 forbidden copies, and all26680 AP5
occurrences pass the independent checker. It used11048921 proposals
and231658 expensive evaluations, confirming the frozen engineering
prediction. This settles the strongest listed surrogate positively.

J15 frozen before execution: test/minimize the full completion triangle
of window_ap5_fast600.json. Predict a further obstruction on at most20
marks can be extracted, with a RUP proof under the existing60-second
producer bound; no negative claim is presumed if certificate generation
fails. Any such new obstruction must escape the completely certified
window13 affine-pattern family, since this literal set avoids that whole
family. If the triangle is SAT, save its complete coloring instead.

J15 outcome: a10-mark core{2,3,4,6,7,8,22,25,26,27} has a verified
1297-addition RUP refutation on45 cells and51 corners. Thus the strongest
saved YES still does not lift to a full completion triangle.

J16 frozen before symbolic audit: replace that core by two blocks
x+h*{0,1,2,4,5,6} and x+b+h*{0,3,4,5}, with integers h>=1,
b>6h. Predict all51 corners in the certified core remain corners
identically in the independent parameters x,h,b. Preserve every Boolean
cell label by ordered mark index. Check each affine identity exactly,
and prove positivity of each new step from h>0 and b>6h. Extra corners
are harmless. If every identity passes, the existing RUP proof yields
a uniform two-parameter forbidden family, beyond isolated fixed shapes.

J16 outcome: all51 affine coefficient identities and all strict-order
inequalities pass. The1297-addition RUP proof therefore certifies the
whole two-parameter family on h>=1,b>6h.

J17 frozen before the new bounded iteration requested by root: retain
witness_464_window_ap5.json and all preceding proofs as a fixed checkpoint.
Predict this witness violates at least one new parametric-family relation
(the literal core supplies one). At n464, only h<=42 can contribute,
because the minimum span is11h+1. A forward violation pairs an L-start
x, L={0,1,2,4,5,6}, with a K-start z, K={0,3,4,5}, when z>x+6h.
The reflected condition pairs a J-start y, J={0,1,2,5}, with an L-start
x when x>y+5h. Each occurrence of these shorter blocks is recorded once.
Search scoring will count forbidden start pairs using Fenwick trees,
not materialize all ten-point copies. Retain all old caps, complete
window13 exclusions, and AP5 uniqueness. Run600 seconds, seed20260916,
from the strongest frozen witness. Predict a score decrease, without
presuming a feasible or infeasible outcome. Every positive result must
be checked by independent direct block detection and all start-pair tests.

J17 outcome: initial witness had7 forward and4 reflected start-pair
violations, exact weighted score88. The compact search found a new155-set
with score0 after7149873 proposals and175037 expensive evaluations. The
independent checker passed all earlier predicates and all start-pair
relations for h1..42. The new canonical witness is
witness_464_parametric.json. This is a further positive surrogate result;
neither a full triangle coloring nor a grid coloring is asserted.

J18 frozen before root's final lifting audit: test the full completion
triangle of witness_464_parametric.json and, if negative, extract a small
literal core. Predict a core with at most20 marks can be found and its
RUP refutation generated within the existing60-second producer limit.
A proofless negative remains UNVERIFIED. A positive result requires the
entire triangle coloring. No further stochastic search is part of this
audit; this is the final distinction between surrogate feasibility and
triangle liftability before independent-agent review.

J18 outcome: the final saved surrogate witness contains a certified
9-mark obstruction{1,2,3,5,10,11,12,13,14}. Its36-cell,46-corner
triangle has a157-addition RUP refutation, independently checked. Thus
the final surrogate witness does not lift to a full triangle.

J19 frozen before a final symbolic check, with no new stochastic route:
replace that core by (x+h*{0,1,2,4}) union
(x+b+h*{0,1,2,3,4}), integers h>=1,b>4h. Predict all46 source
corner clauses persist identically. If the coefficient and positivity
checks pass, preserve this as another uniform lifting lemma for review.
The final witness will then be explicitly a YES only for the previously
tested premise set, not for this newly extracted lemma.

J19 outcome: the46 identities and all step/order inequalities pass.
The source157-addition refutation certifies the entire four-mark-hook
plus five-AP family. All author experiments in this assigned iteration
are now complete; independent-agent review is the next gate. This is a
subtask checkpoint, not global termination or method exhaustion.
