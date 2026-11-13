# Extremal rigidity as a shared span cost

Base: `5b5db22c3c65123193cb31f2aa5bd949b3075e1a`.

The object is the six **actual, pairwise disjoint** Golomb completion classes
on one subdiagonal of a proper three-color directed-L square. The target is a
joint capacity stronger than six independent ruler bounds and the existing
distinct-minima count. No lower-bound SAT search is authorized for this package.

New interaction considered: several nearly extremal classes must share the
same ambient endpoints, but extremal shapes cannot necessarily coexist. A
class that cannot use an extremal shape must pay an integer span increment.
Success requires a universal packing inequality, authenticated extremal-shape
input, and exact arithmetic. A numerical relaxation status is not a proof.

The first uncertainty was whether endpoint/rank transport already detects
this cost. The bounded floating probe reports feasibility at 431 positions;
this is diagnostic rather than an exact feasibility certificate. The exact
rigidity argument excludes six 24-mark classes there.

This is a finite-capacity refinement. It has not supplied the requested large
Ramsey improvement. A future substantial improvement needs a stability or
near-optimal-shape theorem extending the cost beyond the four corrected
positions. No unknown near-optimal-ruler counts are assumed.
