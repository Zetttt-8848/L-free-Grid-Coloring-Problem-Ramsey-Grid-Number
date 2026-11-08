# Completion-demand and line-count work package

Base commit: `5b5db22c3c65123193cb31f2aa5bd949b3075e1a`.

Primary object: all three strict sources selected by the actual main
diagonal color classes of a three-color square, with their prescribed
binary colors. Count triples of requests from different sources that
jointly exclude all three colors at a shared missing completion cell.
This couples the original diagonal color classes, not only offsets.

Secondary object: an arbitrary finite integer set A and the full strict source
V(A)={(v,u):u<v; u,v in A}, colored by signs ±1. The directed equal-leg
L is (x,y),(x+d,y),(x+d,y+d), d>0. No weak diagonal or extension to a
square is assumed.

Target: replace separate offset capacities by a count that retains both
physical completion collisions and row/column information. The proposed
chain is: cross-offset completion demands -> collision count and a joint
three-direction line budget -> a source bound -> an upper bound for R3.

The first two arrows are proved here, including an explicit obstruction
with all three strict sources individually proper. The last two are **UNDECIDED**:
the signed missing-completion term has no sufficiently strong global
bound at density approximately one third. This package does not improve
the adopted numerical bound R3<=464 and does not run a lower-bound SAT
search. Exact small-source enumeration checks identities and illustrates
their scope, not a new three-color square impossibility theorem.

Existing `manuscript/main.tex`, thm:forcing already keeps the pointwise
completion condition H_q=|Kz|_q. The new collision expression is a
higher-moment count of that condition, not a logically new restriction
when the entire pointwise system is retained. The joint line expression
is a direct binary indicator expansion; no literature-priority claim is
made for this elementary counting device.
