# CAP-P1: literal near-extremal two-ruler triangles

Before execution: use two explicit ruler arrays of orders23 and24, independently
verify their positive differences, then test disjoint reflected/translated
pairs whose span is at most462. The arrays are discovery inputs, not imported
optimality theorems. Predict some pairs pass the isolated two-ruler condition;
do not predict they extend to the required two-color completion-closed region.

First finite family: each order separately, second ruler optionally reflected,
translation h=1,...,462-span, first ruler fixed at0. Reject intersections.
For each remaining pair, test the complete weak triangle on their union,
including its two-colored diagonal. A SAT witness refutes a45-cap based
only on those local two-color hypotheses; it does not refute the full-grid
cap claim. A negative solver response has no theorem status without a
verified proof and covers only that literal pair, never all ruler pairs.

Second stage if a local triangle is feasible: embed the fiber at source
distance d=1 and impose the full two-color T(A), A=F union(F+1), with the
fiber colors pinned. This retains the additional red-source geometry.
Again no complete square or155-element source set is presumed.

Solver budget per literal model initially5seconds; stop the family early
upon a verified positive witness, or after120seconds of solving. This is
a scoped discriminator, not exhaustive non-existence at n464.

CAP-P2 AP5 uniqueness: the full geometric proof predicts every F_d is
five-AP-free. Before testing the canonical155-set, predict it violates
at leastone AP5 start-multiplicity group. Such a positiveviolatingcount
would separate the new geometric condition from the old necessary system.
Also enumerate all2^10 binarycolorings of weakT4 and recover the inherited
36 validcolorings through the translation fromstrictT5; record their
four-diagonal colorpatterns. WeakT5 has2^15 rawcolorings and expectedzero.

CAP-P3 diagnostic after wrapperexit anomaly: rerun the unchanged tiny
pair-family program with complete stdout/stderr captured, expecting all
previous attempts to retain the same rawnegative statuses. The purpose is
to identify the process-exit cause; no rawnegative result is promoted.

CAP-P4 endpoint correction, frozen before execution: the inherited profile
at n464 should exclude s159 and give bound158, not exclude s155. The
hypothetical 45-cap through distance27 should close at least n460..465
after endpoint spacing. The hypothetical 46-cap through27 plus 45-caps
at distances1,2,3 should exclude s155 at464 using window13 spacing.
Scan n450..465 and all c, distinguishing these conditional profiles.

CAP-P6 conditional descent: CAP-P4 found the first closed grid size454
within the prespecified range450..465 when the45-cap is assumed and
window13 spacing is used. Before extending the range, predict no closure
at n6..453 from that same profile. Scan every n6..465 exactly, retaining
nonmonotonic ceil(n/3) effects and all c. This tests the scope of the
conditional mechanism, not the validity of the unproved45-cap itself.
