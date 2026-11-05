# Research checkpoint R4-RESEARCH-0044

Continuation of0043, including the interrupted and resumed0044 work.
The preceding goal turn was progress: auxiliary derivations and concrete
constructions changed the remaining geometric questions. This checkpoint
adds complete root derivations, rather than recording only those plans.

The full objective remains active and incomplete. Unconditional bounds
remain 21<=R3<=465 and R4<=21991300. The attributed general-growth
corollary is complete and unchanged. S21/H10/EP10 and both local
rainbow premises remain open. No original method with an unconditional
small-color improvement is yet established. Withhold the results report
until all objectives are achieved; do not mark the goal complete or
blocked. There is no external blocker.

## 1. Root: exclusive continuation of interlaced shared pairs

INTERLACED_SHARED_PAIR_COMPLETION_0044.md is a full new derivation.
In an actual proper weak source, normalize the unique two classes'
interlaced h-pairs as C{r,r+h}, B{r+p,r+h+p}, 0<p<h. Put

    q_-=r+p-h, q_+=r+2h,
    v_-=r+2p,  v_+=r+h-p.

The three exact occupancy constraints are

    1S(q_-)+1S(q_+)<=1,
    1S(q_-)+1S(v_-)<=1,
    1S(q_+)+1S(v_+)<=1.

For the first, both outer marks would have forced opposite diagonal
classes. At length h-p, the three cells
(r,r+p-h),(r+h,r+p),(r+2h,r+h+p) have fixed outer colors B,C.
Their two adjacent completions have colors B,C respectively, forcing
the middle cell both ways. The other two constraints use the completed
reflected-middle seed rule. Every interlaced shared pair therefore
forces two DISTINCT missing positions, including coincident-interior
and midpoint cases.

Let I count interlaced shared lengths and K_seed all upper/lower seeds
across both class roles. A seed is exactly an occupied outer position,
so K_seed<=I<=rho. This is stronger than one-per-class uniqueness:
actual weak properness is needed to exclude both roles at one h.

Root also injects a seed into an internal reflection a<m<q in one
class with opposite output s=a+q-m. Upper seeds have m>s; lower
seeds have m<s. The displayed inverse formulas recover the seed,
so K_seed<=K_ref<=floor(bc/2), using the existing distinct-unit count.
Consequently K_seed<=min(rho,floor(bc/2)).

For the interlaced pairs whose two outer positions stay within the
source hull, the note derives I_int<=(n-2)(ell+1-n). A fixed interior
hole has at most n-2 outer appearances, by doubling-path forests on
each side and class, and at most n-2 interior appearances, by unique
pair sums charged to a nonextreme opposite-class mark. This is an
explicit O(n) reuse bound, not constant bare-hole multiplicity.

For actual fibers of a proper strict A, K_A=sum_d K_seed(F_d) obeys

    8K_A+sum_d s_d^2<=2T(A)+M(A),
    2K_A<=K_3(A),

where s_d=b_d-c_d. Exact window versions weight a seed by
(t-d-2h)_+, its whole source span. The note retains the restricted
signed variances rather than replacing them by arbitrary weights of
the full-fiber variance. These are new simultaneous constraints;
they do not force many seeds in a general high-energy source.

## 2. Root: energy when shared support is small

LOW_SHARED_SUPPORT_WEAK_ENERGY_0044.md derives, for any disjoint
Golomb B,C, the additional bound

    T(B union C)<=min(2M,M+5rho).

It keeps the exact decomposition T=2rho+N+Q. If J counts mixed
queries at shared lengths and Z those at lengths unsupported in
either class, then N=bc+J-Z. The integer identity

    k=1_(k>0)+binom(k,2)-binom(max(k-1,0),2)

gives J=2rho+nu-E-P, where nu<=rho counts same-orientation mixed
collisions whose displacement itself lies in the shared support;
E,P are nonnegative empty-orientation and excess-collision terms.
Thus the exact new identity is

    T=M+4rho+nu-[Z+(U-Q)+E+P].

In particular disjoint within-class difference supports give T<=M,
and additive energy <=4n^2-3n. Applying this to all actual weak fibers
gives K3(A)<=min(2T(A),T(A)+5R(A)), R(A)=sum_d rho_d, together with
the full exact defect and whole-span window identities.

This supplies the small-shared-support branch complementary to the
activated-pair theorem. It does not control M(A)/span(A). In particular,
the uncolored Golomb-overlap examples already satisfy K3=0 while
T/M grows; their properness remains unspecified. A moment-only
inference to S21 would still be invalid.

## 3. Root: a proper three-cube with rho_d=0 everywhere

SHARED_DIFFERENCE_FREE_THREE_CUBE_0044.md gives a new symmetric
strict coloring for every positive two-dissociated three weights.
Represent source marks by subsets of {1,2,3}. Color a strict cell1
exactly for endpoint pairs empty/singleton, singleton/full, or
singleton/complementary-doubleton; all others get0.

The proof classifies all corners by disjoint positive generator
supports of total size2 or3. It gives the actual two corner color
patterns in each sign and face case. No raw solver result is used
as a proof premise. Every primitive fiber has a 3+1 diagonal split,
and every other fiber has at most2 starts. Hence rho_d=0 for all d.
The exact fiber profile is three of size4, six of size2, four of
size1, giving M28,T24,K3=6.

Thus absence of shared signed-fiber differences does not imply
positive three-cube avoidance, even under actual properness. The
whole fiber need not be Golomb. The ratio T/M=6/7 does not refute
H10 or S21. The construction pinpoints a necessary complementary
branch of a method using activated shared pairs.

The bounded precursor fibers/CUBE_DIRECTION_TYPE_DISCOVERY_0044.py/json
made one original-geometry SAT call on weights1,4,16. Its first
type triple N,N,N returned a full28-cell array and the pass stopped.
This was discovery only. Root changed the isolated complementary
cell to derive the symmetric parameterized rule above; it did not
replay or independently audit the solver assignment.

## 4. Auxiliary seed transfer, defect, and path work

fibers/BINARY_CORE_FIBER_TRANSFER_0044.md transfers the core through
actual F_d and originally charges it to a signed pair plus an
interior missing translation edge. Its exact gap-hole ledger and
finite span bounds are complete. The new root bounds in Section1
supersede using that much larger ambient ledger as the sole seed cap.

fibers/REFLECTION_SEEDS_AND_MIXED_DEFECT_0044.md gives four-way
saturation of an upper seed C{0,h},B{p,h+p,2h}: it exposes an unused
opposite pair-sum resource, an unshared side difference, a deficient
mixed p-query, or the saturated package p,h-p,h,2h-p all shared
together with an alternative B pair-sum representation of h.
Unused opposite Q-pairs receive seeds injectively. A full proper
weak example B{-100,2,9,14,107},C{0,7} shows that the opposite
pair can instead be Q-used; it refutes that canonical charge only.
No absolute K_seed<=c delta follows from the note.

fibers/ACTIVATED_SHARED_DIFFERENCE_PATHS_0044.md gives a canonical
successor tau(h)=h-|sigma_h|, the length of the forced adjacent
same-class side pair. Activated-to-activated arrows strictly
decrease length. Unshared terminal tau gives a specific U-2rho
resource; shared but inactive tau is neutral under this argument.
A separated-powers Golomb diagonal fan has arbitrarily many selected
activated configurations with the same terminal pair {0,1}, while
respecting their two required holes. No full proper weak coloring
of that fan is asserted. Thus diagonal geometry and those local
holes alone do not control merging; other actual mixed-cell
compatibility is required.

fibers/DIFFERENCE_SUM_RESOURCE_CYCLES_0044.md studies the graph on
distinct within-class pair resources, with equal-difference and
equal-sum matching edges. A four-cycle has exact coordinates
B:(s1,d1),(s2,d2), C:(s1,d2),(s2,d1). The note handles parity and
endpoint degeneracies and shows that it forces companion matched
cross pairs. Its four core weak constraints are locally compatible;
a cycle exclusion cannot be inferred from those four constraints.

Root subsequently supplied a complete proper WEAK three-cube coloring,
integrated in fibers/PROPER_WEAK_RESOURCE_CYCLE_CONSTRUCTION_0044.md.
The diagonal color is subset parity. Distinct same-parity endpoints
get the opposite parity; a primitive edge is color1 only when it
ends at the full subset; complementary singleton/doubleton pairs
get1 and empty/full gets0. The full positive-corner support table
and offset-zero argument prove properness for every positive
two-dissociated three weights. The two parity classes have identical
six-element positive-difference and distinct-pair-sum sets; all three
alternating resource four-cycles are written symbolically and at
weights1,4,16. Thus actual properness DOES permit these cycles.
For this family rho6,U12,Q12,N0, so the first and third mixed defects
both vanish while the middle defect is32. Acyclicity or a positive
saving from the first and third defects alone is unavailable.

fibers/PROPER_WEAK_JOINT_QUERY_BUDGET_0044.md proves N+Q<=M whenever
min(b,c)<=2, even without properness. For C{0,d}, it writes
N=2b-R+E, where R counts mixed queries unsupported by Delta B and
E counts exterior marks -d,2d. The three anchor pair sums bound
Q<=4; b>=4 follows immediately and b1,2,3 have explicit symbolic
cases. The arbitrary-size proper weak target N+Q<=M remains open
from class sizes3+3 onward. The familiar B{0,2,5,6},C{1,3,4,8}
excess is excluded directly: internal reflections (0,5,6)->1 and
(1,3,8)->6 force z(6,1) to opposite colors. This one conflict is
not a general budget proof. No solver was used for this attempt.

## 5. Auxiliary local R3 and source inputs

The integer dilation-weight implications in
DIVISOR_WEIGHTED_TRIANGLE_AVERAGING_0043.md remain the concrete R3
route: F11(5) or F12(7) would imply R3<=464. Do not optimize those
already sufficient weights again. The local lower lemmas are open.

fibers/LOW_ZERO_BOUNDARY_PROPAGATION_0044.md derives the exact
three-valued sign-type transport on every zero-free compatibility
hexagon D_e g_d=D_d g_e. It also supplies a full proper T11 coloring
with13 rainbows, all at strictly interior barycentric bases, and a
complete165 corner-sum table. Boundary-only forcing is therefore
false; this is not a <=4-rainbow counterexample.

fibers/LOW_ZERO_SLOPE_COUPLING_0044.md derives the affine-orbit
identity V(F_beta)=110-2Z+6k_beta and sum_beta V=330-6r, retaining
the defined-slope and divisible-step distinctions. For three zero
corners at (p,d),(p+d e_x,e),(p+d e_y,e), with slopes alpha,beta_x,
beta_y, it gives g_(d+e)(p)=e(beta_y-beta_x). Equal translated slopes
force an outer zero; properness then requires alpha d=beta e.
One four-zero packet can still omit the proper affine slope. A
second overlapping packet or a new incidence theorem is missing.

literature/TERNARY_BLOCKING_INPUTS_0044.md translates the stronger
five-zero statement to the absence of weights161..165 in the
53-dimensional ternary corner-sum code. Greene's weight-enumerator/
Tutte theorem applies in principle but supplies no relevant
coefficients. Strong-blocking/trifferent results need a spanning
intersection hypothesis not furnished by capness or sparse normals.
No generic five-fold blocking theorem was obtained.

literature/MIXED_DEFECT_SPAN_INPUTS_0044.md maps the existing
resources without recomputation: the prior general lower bound on
delta was just nonnegativity; the saved hole and supported-difference
budgets had no injection into a defect summand. Sections1-2 above
are the new subsequent root inputs, with their limitations retained.

## 6. Current execution and next root-owned question

The original three auxiliary handles were terminal before the
interruption and were missing from the live inventory on resume.
No solver or root shell process remained live. The fresh bounded Sol
high handles /root/shared_difference_paths and /root/weak_joint_budget
have now completed their derivation tasks, including the proper weak
resource-cycle construction and the two-anchor joint query budget.
Both are terminal and reusable. No computation or auxiliary task is
currently live. Do not wait on or restart the completed bounded
discovery. A new assignment must address a new mathematical question.

Root retains the main R4/S21 problem. The new useful division is
between small shared support, controlled only at the higher moment
by Section2, and activated shared support, paid by Section1. Neither
currently forces the finite-span conclusion. The next substantive
step must connect those alternatives to span or actual source cut
constraints, not merely optimize the seed upper bound. Keep the
local F11/F12 route in parallel and preserve the whole objective.

No separate audit, repeated completed-proof check, formalization,
or usage reset was requested or performed in0044.
