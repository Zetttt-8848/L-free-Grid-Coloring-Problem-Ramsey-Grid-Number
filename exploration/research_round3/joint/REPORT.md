# R3-JOINT checkpoint

Sub-Task ID: R3-JOINT. Assigned Model: GPT-6 Astra ultra, Level 3.
Task: decide the 155-set surrogate with stronger computation and carry
positive examples into actual completion-triangle constraints.

## PROPERTY (formal)

The base question asks for A subset [464], |A|=155, min A=1, with
r_A(d)<=2 max{j:H_j<=464-d} at every positive distance and no six-AP.
Positions and H follow the audited position-count convention in R3-E0.
All sets, patterns, triangles and colorings in this folder are literal
finite objects; no omitted region or extrapolation is a certificate.

## CHANNEL USED

C1: a strengthened CP-SAT model and an independently programmed stochastic
construction search. The CP model uses exact pair equivalence, sorted
ranks, consecutive-six-rank constraints, and valid linear rank-neighbor
cuts proved in property.md. The declared 600-second CP run was interrupted
after the mathematical question was settled positively by a checked
literal witness. Its own status remains UNDECIDED. Its model, setup,
telemetry and interruption reason are preserved.

C2: all positive objects are explicit finite sets. Certified small
completion-triangle obstructions yield entire affine pattern families.
No infinite construction family or grid coloring is asserted.

C3: stochastic proposals only find candidate objects. No probability,
first-moment, alteration or Local Lemma existence claim is used.

## WITNESS + CERTIFICATE

PROVED base YES: witness_464.json is a 155-element set satisfying all 463
distance caps and all 21298 six-AP exclusions. verify_set.py enumerates
all 11935 increasing pairs and every AP using an independent endpoint
enumeration. witness_464.canonical.check.json records PASS. The full
difference profile is witness_464.profile.json. Its first 27 values are
46,47,47,48,48,47,48,48,47,48,48,48,48,48,48,47,45,43,47,45,47,47,
48,47,44,42,46. The full maximum is 48;22 of these 27 values exceed 45.
Thus the base one-class conditions cannot imply a universal 45 cap.

The witness is NOT a grid coloring and gives no Ramsey lower-bound
improvement. Restricting it to [463] or [462] leaves respectively 154 or 153
marks, one fewer than required; no smaller-n witness is inferred.

PROVED new 9-mark exclusion: B={1,2,3,4,5,7,8,10,12} has no six-AP but
its strict completion triangle is not two-colorable. Its 36 cells and 55
corners produce 111 clauses including one complete color-interchange pin.
triangle_core.rup contains 151 RUP additions. verify_triangle_rup.py
independently reconstructs every geometric corner and validates every
addition, including the empty clause. The proof is a DRAT-compatible
all-RUP trace, not an unverified solver status.

PROVED new 10-mark exclusion: B={1,2,3,5,6,7,9,10,12,13} has no six-AP
and its 45-cell,79-corner triangle has a 427-addition RUP refutation.
The corresponding artifacts have prefix triangle_core_v2.

For either B, every cell of T(B) completes two diagonal points of its
color, so it must use the other two colors. Therefore every positive
affine copy of B is forbidden in any diagonal color class of a corner-free
three-color grid. Reflection is also valid: (x,y)->(-y,-x) preserves the
corner relation and takes T(B) to T(-B). Dividing integral offsets by
their positive gcd preserves the same finite corner incidence.

PROVED complete window classification: window13.json and its separate
checker establish 7147 good and 1045 bad supports among all 8192 labeled
subsets of {0,...,12}. The certificate consists of 109 minimal bad support
refutations, totaling 31605 RUP additions, and 334 full colorings of maximal
good supports. Every mask is covered exclusively by one side under
containment. All individual negative instances also have explicit CNF
and RUP files in window13/. The verified log passes the required log
integrity checker; no symmetry quotient is used.

The exact capacities h(w), for w=1,...,13, are
(1,2,3,4,5,5,6,7,7,8,9,9,10). Here h(w) is the largest support whose
two-color strict completion triangle exists inside w consecutive integer
positions. Consequently any grid diagonal class has at most h(w) marks
in any interval of w positions. By affine invariance the same restriction
holds on any w-term positive-step AP. For ordered marks, the minimum
possible spans for 6,7,8,9,10 marks are 6,7,9,10,12 respectively. Thus
a_(i+7)-a_i>=9, a_(i+8)-a_i>=10, a_(i+9)-a_i>=12 are valid global
rank constraints. Complete coverage, not sampled local patterns, supports
these implications.

PROVED strengthened surrogate YES: pattern_v1_600.json satisfies every
cap and all 40408 affine exclusions from six-APs and the 9-mark pattern
with its reflection. ap5_600.json additionally satisfies all 57888 affine
exclusions from both certified patterns/reflections and the root's
AP5-uniqueness property: for every step there is at most one five-AP.
verify_pattern_set.py independently checks every literal pattern copy
and all 26680 AP5 occurrences in 115 groups. Neither positive set is a
full triangle or grid coloring.

PROVED completed window/AP5 surrogate YES: witness_464_window_ap5.json satisfies
every cap, all 543170 affine copies of all 56 normalized minimal bad
window13 patterns, and AP5 uniqueness. The independent checker passes
all predicates. The catalog itself is independently bound to the complete
window certificate in patterns_window13.check.json. The exact early
rejection method in ITERATION_LOG.md reduced the expensive pattern
evaluations to 231658 among 11048921 proposals; the checked witness,
rather than this heuristic telemetry, proves the positive result.

PROVED further obstruction: this strongest witness contains
B={2,3,4,6,7,8,22,25,26,27}. Its 45-cell completion triangle has 51
corners and a 1297-addition RUP refutation (triangle_core_v3.*), checked
independently. Thus even the strongest saved one-class YES cannot lift
to a full completion triangle.

PROVED uniform two-block obstruction (pending independent-agent review):
for integers h>=1 and b>6h, no diagonal color class may contain

    (x+h*{0,1,2,4,5,6}) union (x+b+h*{0,3,4,5}).

The displayed literal core is the specialization x=2,h=1,b=20. Label
the 45 cells by ordered pairs of mark indices. Each coordinate is affine
in x,h,b. All 51 original corner equalities vanish coefficient by
coefficient; every required step stays positive when b>6h. Thus every
original clause, including the color-interchange normalization, remains
valid for the entire family. The same finite RUP refutation applies.
Extra corners at special parameter values only add restrictions. This
is a two-parameter family rather than a finite collection of fixed
shapes. verify_parametric_core.py checks all identities, ordering,
proof-file hashes and boundary/specialization cases exactly.

PROVED new strongest surrogate YES: witness_464_parametric.json satisfies
all earlier caps, all 543170 window-derived affine exclusions, AP5
uniqueness, and the entire uniform two-block family with its reflection.
The checker directly detects every actual L-, K-, and J-block start and
tests every forbidden start-pair relation for h=1,...,42. Larger h cannot
fit a forbidden family because its minimum span is 11h+1. All violations
are zero. PARAMETRIC_MODEL.md proves the reflected relation and gives a
compact exact prefix-OR encoding for future SAT work.

The older witness had seven forward and four reflected forbidden pairs.
The new search reduced its exact weighted score from 88 to 0. It used
7149873 proposals and 175037 expensive evaluations. These are engineering
statistics; the separately checked literal set proves feasibility.
This bounded author iteration is complete. A full triangle or grid
coloring is not inferred, and the broader research program is not closed.

PROVED final lifting obstruction: the final saved set contains
B={1,2,3,5,10,11,12,13,14}. Its 36-cell, 46-corner triangle has a
157-addition RUP refutation (triangle_core_v4.*), independently checked.
Therefore this final surrogate YES also does not lift to a triangle.

The same fixed-label proof gives another uniform family: for integers
h>=1 and b>4h, no diagonal class contains

    (x+h*{0,1,2,4}) union (x+b+h*{0,1,2,3,4}).

The source specialization is x=1,h=1,b=9. Every one of its 46 corner
identities holds coefficient by coefficient for arbitrary x,h,b; all
required steps stay positive on the stated domain. The independent
coefficient audit is parametric_ap5_core.check.json. This new premise
relates a five-AP to a separated four-mark hook. No new set search using
this last premise was run. Accordingly, witness_464_parametric.json is
a YES for its explicitly recorded earlier predicates, not for every
necessary condition discovered by the end of this author iteration.

## VERIFICATION METHOD

From the project root, run:

    python research_round3/joint/verify_set.py research_round3/joint/witness_464.json
    python research_round3/joint/verify_triangle_rup.py
    python research_round3/joint/verify_triangle_rup.py --tag triangle_core_v2
    python research_round3/joint/verify_window.py --width 13
    python research_round3/joint/verify_pattern_set.py research_round3/joint/ap5_600.json
    python research_round3/joint/verify_pattern_set.py research_round3/joint/witness_464_window_ap5.json
    python research_round3/joint/verify_catalog.py
    python research_round3/joint/verify_triangle_rup.py --tag triangle_core_v3
    python research_round3/joint/verify_parametric_core.py
    python research_round3/joint/verify_pattern_set.py research_round3/joint/witness_464_parametric.json
    python research_round3/joint/verify_triangle_rup.py --tag triangle_core_v4
    python research_round3/joint/verify_parametric_ap5_core.py

All mathematical checks use exact integers or Boolean values. Solver
telemetry and temperatures are scouting data, not arithmetic evidence.
The witness checkers import no solver or generator. The RUP/window
checkers reconstruct geometry independently and implement unit propagation
without a SAT library. The original large-triangle Glucose negative
response lacked a captured proof; it remains unverified telemetry.
Certified small cores, rather than that empty artifact, establish the
negative lifting obstruction. ERRATA.md records the proof-capture issue.

## BEST-KNOWN GAP TABLE

| Scope and date | Lower bound | Upper bound | Ratio | Last lower-side movement | Last upper-side movement |
|---|---:|---:|---:|---|---|
| Project-local R3, 2026-09-10 | 21 | 465 | 155/7 | Inherited baseline; no change in this subtask | Inherited baseline; no change in this subtask |

Project-local three-color bounds remain 21<=R3(L)<=465, with additive
gap 444 and ratio 465/21=155/7. No movement on either Ramsey side follows
from the one-class feasibility results. The upper-bound surrogate's
original fixed-size existence decision is settled YES. The full grid
problem and the strengthened partition problem remain open here.

## VERDICT / SELF-CHECK / DEPENDENCIES

PROVED: the literal 155-set base feasibility, four certified pattern
obstructions including two uniform two-block families, complete local-window
classification through 13, and the separately checked strengthened
surrogate witnesses described above. UNDECIDED: the interrupted CP run, the bounded partition search,
and all global Ramsey implications requiring further structure.

Confidence is high in these finite certificates; they have explicit
independent verification recipes. Independent-agent cross-review is a
separate pending integration gate. Dependencies are the inherited diagonal
completion reduction, fixed H table, integer affine corner invariance,
exact set checks, and checked RUP refutations. The AP5 property depends
on the root's separately documented weak-triangle lemma. No uncertified
solver negative result is a proof dependency.
