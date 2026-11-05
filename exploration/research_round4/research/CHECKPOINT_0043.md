# Research checkpoint R4-RESEARCH-0043

Continuation of0042. The preceding turn was progress through interval
forests, exact convolution, and the reflected-middle hole rule. This
turn is progress: root changed the homothety averaging measure and
derived two explicit integer-weight implications for the R3 target.
The required local rainbow lemmas remain open. Root also reduced the
complete two-point binary obstruction system to two arithmetic patterns.

The full objective remains active and incomplete. Unconditional bounds
remain 21<=R3<=465 and R4<=21991300. The attributed general-growth
corollary is complete and unchanged. No original method with an
unconditional small-color improvement has yet been established.
S21/H10/EP10 and the R4 target remain open. Withhold a results summary
until every objective is achieved. There is no external blocker and
no basis to mark the goal blocked or complete.

## 1. Root: a materially changed rainbow amplification

DIVISOR_WEIGHTED_TRIANGLE_AVERAGING_0043.md is the main new root
derivation. Earlier uniform-dilation scalar averaging is closed at
local sizes10--13 under the recorded witness/weight scopes. The new
argument assigns a nonnegative weight a_d to every copy of local
T_m with dilation d. Its total copy weight and safe host load are

    J=sum_d a_d binom(N-d(m-2),2),
    L_h=sum_(j|h,1<=j<=m-2)binom(m-j,2)a_(h/j).

Every host corner of step h has multiplicity at most L_h, since
each local corner and dilation determine at most one translation.
If L_h<=K and every proper three-color T_m has at least rho
rainbows, the exact host identity V+2R=2binom(N,2) gives

    rho J<=K binom(N,2).

The changed measure is substantive: a low-rainbow coloring that
blocked uniform multiplicities can now lie above the sufficient
weighted threshold. This is a conditional method improvement within
the project, not a new Ramsey theorem or a priority claim.

For N464,m11, root constructs 42 integer weights by the recursion

    c_j=binom(11-j,2), 1<=j<=9,
    a_n=floor((45000-sum_(j|n,2<=j<=9)c_j a_(n/j))/45)
         for 1<=n<=42;
    a_n=0 for n>42.

The full integer table is in the proof. All a_n lie in [0,1000].
The recurrence controls loads h<=42. For h43..168 with a prime
factor >=11, their {2,3,5,7}-smooth part is <=15 and has the same
relevant divisor recursion. The truncated host load is bounded by
that small smooth-part load. The remaining 34 smooth h are listed
with their exact loads, all below45000. For h>=169 only j>=5 can
contribute, so L_h<=35000. This is an elementary integer proof;
no LP optimum or floating feasibility status is a premise.

The exact weighted count is

    J11=974699503,
    5J11-45000 binom(464,2)=39777515>0.

Thus the new open finite premise

    F11(5): every proper three-coloring of T11 has >=5 rainbows

would imply R3<=464. A saved proper coloring has exactly5; it
supplies no lower theorem. The old uniform T11 scheme was blocked
by that same count5. Its old limitation has not been contradicted;
the averaging weights have changed.

Section6 gives an independent explicit construction for m12.
Use c_j=binom(12-j,2),1<=j<=10, K55000, divide by55 in the same
42-term recursion. All weights remain in[0,1000]. Smooth-part
reduction handles nonsmooth h<=210, the 41 remaining smooth loads
are listed, and h>=211 has load<=35000. Now

    J12=857622447,
    7J12-55000 binom(464,2)=95477129>0.

Therefore the alternative premise F12(7), every proper three-color
T12 has >=7 rainbows, also implies R3<=464. Both premises are open;
neither conditional number changes the working bound.

## 2. New bounded computation and source-map scope

The Terra source map literature/LARGER_LOCAL_OBJECT_STATUS_0043.md
found no saved full T14,T15,T16-or-larger rainbow lower theorem,
exact whole-corner multiplicity analysis, or full proper-coloring
record. Larger restricted-step probes are not full-triangle results.
The existing uniform T10/T11/T12/T13 limitations remain as recorded.

The new discovery fibers/DILATION_WEIGHT_DISCOVERY_0043.py/json
ran nine small floating LPs, local m10..18 at host464. Each
maximized weighted copy count under the safe divisor-load rows.
All returned raw HiGHS success status. The corresponding raw
thresholds were approximately 3.383,4.927,6.880,9.302,12.284,
15.940,20.396,25.772,32.179. These are discovery observations,
not exact optima, local lower bounds, or Ramsey conclusions.
literature/DILATION_WEIGHT_DISCOVERY_0043.md records the scope.

Root subsequently constructed fresh integer sequences and derived
their load bounds as in Section1, rather than using numerical
feasibility or conducting a separate verification pass. The
integer tables and full proof are the retained mathematical input.
No separate audit, review, formalization, or reset was requested.

## 3. Local lemma attempts and the correct geometry

fibers/T11_FIVE_RAINBOW_LEMMA_0043.md records a completed bounded
auxiliary attempt without the lower theorem. It gives exact
equivalent targets for a proper T11:

    V<=100,
    sum_p lambda(p)<=160,

where lambda(p) counts corners in which p is the unique singleton
color. The identity is R+sum lambda=165. Each T11 cell belongs
to exactly9 original corners. These are reformulations, not
proved inequalities with the desired constants.

The note also expresses a possible <=4-rainbow counterexample
through the existing53 F3 reconstruction coordinates, the total
zero-sum set, and the common excluded affine-slope set. It proves
that the165 corner incidence vectors form a projective cap, so
the simplest projective-line blocking certificate is unavailable.
A bounded fresh stronger minimum-zero discovery attempt produced
no result and was stopped; its temporary script was removed.
The former local exec cell54 is no longer live. The cut agent is
terminal and reusable.

The T12 auxiliary attempt is now complete without the local theorem;
see fibers/T12_SEVEN_RAINBOW_LEMMA_0043.md. Its one
fresh original-geometry Glucose4 search for <=6 rainbows stopped
after60 seconds with no result. It is not a negative premise and
no solver process remains live. The note gives the exact line-square
identity Q+2R=638 and hence the target Q<=624. It explicitly maps
every monochromatic subset on each of the33 geometric lines to a
proper two-color strict source, retaining all99 systems' shared
ambient completion cells.

For the three barycentric T11 subtriangles it derives

    3R=R_x+R_y+R_s+D,

where D counts missed face incidences of rainbow corners. An R<=6
counterexample either has one T11 face with <=4 rainbows or has
one of five exact patterns: R5,D0,faces555; or R6 with
(D,faces)=(0,666),(1,566),(2,556),(3,555). Conditional on F11(5),
the remaining target is D+sum_i(R_i-5)>=6. This is a precise
coupling gap, not a completed F12 proof.

During that derivation an ordinary K12 graph-triangle reduction
was proposed and immediately abandoned because it does not
preserve the original geometry. A generic corner, for example
(3,0),(5,0),(5,2), involves four marks and is not a K3 under the
cell-edge map. Ordinary graph Ramsey degree bounds and their
degree-pattern formulas are inapplicable. The discovery code did
use the actual directed equal-step corners, so its bounded
undecided status has its stated scope. Do not revive the invalid
graph reduction or confuse the count binom(N,3) with incidence
isomorphism to ordinary graph triangles.

## 4. Complete two-point binary types and root normal form

fibers/TWO_POINT_BINARY_OBSTRUCTION_TYPES_0043.md completes the
binary classification for Golomb B against C={0,d}. The matching
consists of exterior edges L,U and the unique interior pair's
two edges I,J (or one midpoint edge K), with at most3 choices.
The exact parent witnesses between same-side B endpoints f,n are
f-n in B at anchor0, and d+f-n in B at anchor d.

Golomb difference and pair-sum uniqueness exclude an alternating
path on two distinct parent edges in the small choice graph.
With units, every contradiction needs at most two unit seeds.
It reduces either to one matching edge with two unit endpoints,
or two matching edges whose non-unit endpoints share one parent
edge while their opposite endpoints are units. The latter cannot
occur between the two interior choices. Every exterior-interior
parent edge itself creates the reflected-middle unit obstruction:

    B contains {x,d-x,d+x,2d}, C={0,d},
    or B contains {-d,-x,x,d-x}, C={0,d}.

The complete form retains general0<x<d and the B-Golomb premise.
The earlier x<d/2 subfamily remains a useful example, but changing
x to d-x does not preserve the actual witness d+x. That dependent
wording was repaired during integration. Midpoints are included.
The possible shared-difference ternary corner remains separate.

Root's TWO_POINT_BINARY_NORMAL_FORM_0043.md further proves that
an interior matching edge can never have two B units. Its common
length h has one B representation beginning at a. The lower-
oriented unit would require a>p>0, while the upper-oriented unit
would require a<0. Thus direct double-unit edges are exterior.
They are exactly anchored doubling patterns {h,2h} subset D_b^+
or D_b^-, where D_b^+ records opposite outputs b+h supported by
same-class differences strictly above b, and D_b^- is reflected.

Therefore the complete one-sided two-point binary test consists
of just anchored doubling and reflected-middle cores. For larger
C this characterizes the B-versus-two-C restrictions on every
selected pair. Exchanging classes adds the symmetric restrictions.
It does not prove that the full many-anchor binary/ternary system
is satisfiable, and it gives no finite-span incidence lower bound
by itself. Keep the main S21/R4 question active.

## 5. Top-half sink chains and their remaining coupling gap

fibers/TOP_HALF_SINK_CHAIN_COUPLING_0043.md uses the0042
antichain theorem: vertices of one basin with weights>W_sink/2
form a single chain. At common offsets d_i of opposite-orientation
top-half chains, let a_i,b_i be their intervening N-edge counts
and A_i the active-Q indicator. Then

    A_(i+1)=A_i xor((a_i+b_i) mod2).

If both links are active and a_i=b_i=1, their common increment
h_i=d_(i+1)-d_i lies in both Golomb difference sets, via the two
moving endpoints. Such synchronous one-edge increments are
distinct, including after ruling out swapped class-pair reuse by
interval nesting. For r such transitions,

    r(r+1)/2<=d_last-d_first.

The multi-edge synchronized case yields only equality of two
mixed sums. Its rotated ternary cells need not lie on the two
chains, so no improved global bound on active links is asserted.
Sink mass and cross-offset coupling are still unpaid resources.

## 6. Next root-owned steps and execution status

The most concrete new R3 route is to derive F11(5) or F12(7),
using actual L geometry and the complete integer amplification
already written. A <=4 or <=6 proper witness would respectively
close that premise; a raw negative run would not prove it.
Do not spend another turn optimizing the already sufficient
weights or rechecking the derived integer construction.

Root must also continue the S21/actual-fiber or other R4 route.
The two-pattern binary normal form supplies a more complete local
input than isolated hole rules, but an aggregate finite-span
resource estimate is still missing. Do not shrink the full
objective to the R3 conditional route or a catalogue of patterns.

All three auxiliary handles are now terminal. No solver, numerical
job, or root shell process is live. Do not restart either finished
local discovery merely because its result was undecided. All three
existing handles are reusable for fresh bounded derivations. The
full goal remains active, with results withheld.
