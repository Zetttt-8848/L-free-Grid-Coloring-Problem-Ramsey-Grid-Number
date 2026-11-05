# Research checkpoint R4-RESEARCH-0028

Continuation of CHECKPOINT_0022.md, covering new work numbered 0023-0028.
The user requests sustained invention, no separate verification or audit
workflow, and no results summary until all objectives are achieved. The
goal remains active. No unconditional small-color improvement has been
derived: 21<=R3<=465 and R4<=21991300 remain the working bounds. The
attributed general growth theorem in GENERAL_BOUND.md remains complete
and was not replayed. No reset credit was authorized or used.

All three auxiliary agents and all bounded computations named here are
terminal. Reuse their handles with followup_task for a new bounded task;
do not wait for a completed run or send_message to activate one.

## 1. Current central gap and the new root mechanism

The open finite source-size target remains S21, with span<=99994. Its
conditional implications R3<=379 and R4<=99996 are already derived in
FINITE_SOURCE_SIZE_TARGET_0018.md. The sufficient band statement D(7/5)
and its completed transfer are in DYADIC_SOURCE_SIZE_TARGET_0019.md.
Do not repeat those calculations. Neither S21 nor general D(7/5) is
proved by the new class theorems below.

The most recent root route retains the proper coloring of a complete
source while looking at an entire coordinate overlap. Every nonzero
overlap F_d has a translated proper weak two-color triangle; hence its
diagonal classes give a two-Golomb partition. Complete direct sums turn
this into full arrays, where elementary monochromatic-rectangle arguments
give new restrictions on the factors. Exact energy factorization then
retains a constant which unrestricted layer union estimates lose.

### Root theorem: progression products

PROPER_PROGRESSION_PRODUCT_ENERGY_0027.md proves

    A=B+Q{0,...,t-1}, t>=2, Q>2 span(B), V(A) proper
        => T(A)<=5M(A), and M(A)<=11 span(A).

The base B is arbitrary. The proof first derives, for a union S of two
Golomb sets and n=|S|>=2,

    E(S)<=8n(n-1),  T(S)<=3M(S)-n/4.

It uses the cross-difference l2 identity and concavity of
(2x^2-x)^(1/4), retaining the linear term. A singleton is treated
separately. With e_t=t(2t^2+1)/3, no carry gives

    E(A)=e_t E(B),
    E(F_Q)=e_{t-1}E(B),  |F_Q|=(t-1)|B|.

The overlap partition bounds E(F_Q), and the explicit polynomial in
section 4 proves E(A)<=12|A|^2-11|A|, hence H5 on this full class.
The argument does not fill missing marks or assume a general source is
a progression product.

### Root theorem: arbitrary complete direct sums

PROPER_DIRECT_SUM_ENERGY_0028.md proves

    A=B+QC, |B|,|C|>=2, Q>2 span(B), V(A) proper
        => T(A)<=8M(A), and M(A)<=17 span(A).

Both factors are arbitrary. The exact coordinate overlap products are
F_h=(B intersect (B-h))+QC and
F_{Q delta}=B+Q(C intersect (C-delta)). Their two-Golomb partitions have
no monochromatic rectangles. Elementary complete proofs of the 7-by-3
and 5-by-5 two-color rectangle facts yield

    |B|>=7 => r_C(delta)<=2,
    |B|>=3 => r_C(delta)<=6,
    |B|>=5 => r_C(delta)<=4,

and the exchanged bounds for B. Both factors also have two-Golomb
partitions. The proof combines these facts with
E(A)=E(B)E(C), the cap formula E(S)<=(k+1)n^2-kn when r_S<=k, and
the elementary extremal bound E(S)<=n(2n^2+1)/3 for small factors.
All size cases are explicit, giving E(A)<=18m^2-17m.

This is a source-compatible theorem, not the already refuted assertion
that arbitrary Cartesian strips have constant energy. The present
complete source includes both child triangles and all their common
completion cells. Still, it covers only full products. An arbitrary
subset of a product may lack the arrays needed in the proof, and filling
its holes can destroy properness. Extending the mechanism to general
sources with a controlled total budget is the new central gap.

### First extension to a product with missing marks

DENSE_PARTIAL_PRODUCT_ENERGY_0028.md proves H5 and source constant 11
for a subset A of B+QC when both factor sizes are at least 28 and every
row and column contains at least seven eighths of its possible marks.
If a factor difference had three representations, the six associated
neighborhoods would have at least seven common supported positions in
the other factor. The corresponding actual overlap would contain a
7-by-3 array, contradicting its two-Golomb partition. Thus both factors
have difference multiplicities at most two. Energy monotonicity into
the ambient product, followed by its exact energy factorization, then
gives H5 for the actual subset. The filled product is never assumed
properly colored.

This is a genuine extension to incomplete supports with quantitative
minimum row and column densities. It does not cover arbitrary sparse or
irregular supports. No method name or superiority claim completing the
objective has been assigned to these partial-class results.

## 2. Earlier root geometric theorem, now integrated

TWO_DISTANCE_SOURCE_ENERGY_0025.md proves an unconditional model theorem.
If X is a Euclidean set with all nonzero squared distances in {tau,2tau},
then T_geom(X)<=7 binom(|X|,2). A common sphere is unnecessary.

There are no three-term progressions. Every additive parallelogram is a
square, with short sides and long diagonals. If k_c long pairs share a
midpoint c, its contribution is k_c(k_c-1). A fiber with k_c>=9 has
orthogonal axes p_i. For an outside point c+q the two-distance condition
forces either q perpendicular to all p_i or |<q,p_i>|=tau/4 for every i.
The second case contradicts Bessel because k_c>8. Projection then shows
that no additive square mixes the fiber's endpoints with the rest of X.
Peeling such fibers leaves k_c<=8 and gives the total coefficient seven.

An injective Freiman-2 homomorphism A->X preserving all source equalities
therefore yields T(A)<=7M(A), M(A)<=15 span(A), and a proper coloring
by the two squared distances. Reflection of extra equalities is not
needed for the upper bound. Such an embedding is a genuine hypothesis:
proper sources may contain three- and four-term progressions, which
this class cannot. No universal embedding is asserted.

The auxiliary SPHERICAL_TWO_DISTANCE_BANDS_0024.md derives the exact
band contribution via signed midpoint-axis projections. It proves
T_H<=4M/3 if every midpoint has at most three axes, and isolates the
high-rank overlap issue. The root total-energy separation above uses a
different argument and does not establish general D(7/5) for this class.

## 3. Signed-root family and its actual limitations

SIGNED_ROOT_BAND_FAMILY_0025.md studies A_r={+/-w_i+/-w_j:i<j} with
coefficient-four dissociated atoms w_i=D+9^i, placed in the explicit
single-band geometry there. It derives all difference types, full energy,
and the band formula. The uncolored r=5 band ratio is 58/39>7/5; the
asymptotic band ratio is 13/4. These are not proper-source counterexamples.

Root proves directly that r>=7 cannot be properly two-colored. An
exchange overlap is C union (E+C), C={+/-w_k:k outside two chosen indices}.
Its weak diagonal classes must be Golomb. Each four-point axis gives
at least two same-color pairs; across all axes four difference/sum
families have total capacity eight. Thus the number r-2 of axes is at
most four.

fibers/SIGNED_ROOT_OBSTRUCTION_0025.md shows why a single-fiber argument
does not exclude r=4: each formal fiber type admits a two-Golomb partition.
In particular its two-axis binary overlap has an explicit partition.
fibers/THREE_AXIS_BINARY_FIBER_0027.md now supplies the three-axis
partition as well:

    R={+/-a1,a3,E+/-a2,E-a3},
    B={+/-a2,-a3,E+/-a1,E+a3}.

The symbolic difference-type argument is in that note. Thus this
particular local partition test also does not settle the signed r=5
source. Common-completion coherence across different fibers remains
necessary. Do not treat antipodal reflection as a relation between colors.

fibers/SIGNED_ROOT_SOURCE_DISCOVERY_0024.py/json contains one final
full-corner bounded solver call for each r=3,4,5,6. Raw statuses are SAT,
UNSAT, UNSAT, UNSAT, with respectively 12,24,40,60 marks and band ratios
7/11,26/23,58/39,103/59. A preliminary pass had mistakenly imposed only
band corners; this was corrected before the saved full-system run.
These computational negatives are not paper obstruction proofs. The
r>=7 proof and explicit overlap partitions above are separate derivations,
not checks of these solver outputs. No solver remains live.

## 4. Auxiliary product derivations and one repaired quantifier

fibers/PRODUCT_COLOR_COMPOSITION_0026.md classifies all corners in
A=B+Q{0,1}, using two layer colorings and a full cross matrix g.
Its horizontal compatibility quantifies over arbitrary base starts x,y,
including x=y and x>y; numerical order follows from the different layers.
The original x<y restriction in that condition was repaired during active
integration. The mixed condition still has x<y, but its signed coordinate
increment delta may be positive, negative, or zero. All these cases must
remain in a composition rule.

The note derives T(A)=6T(B)+2M(B), M(A)=4M(B)+|B|. Endpoint-linear
Boolean rules are possible through three factors and impossible for
four or more by their common-kernel dimension. This does not exclude
nonlinear four-factor colorings. The later root progression theorem
explains why an arbitrary indefinitely iterable proper lift is not
supplied by the increasing-energy recurrence: every lift requires a
two-Golomb partition of its base.

fibers/WEIGHT_TWO_BINARY_OBSTRUCTION_0027.md proves that the full
weight-two layer on r>=6 dissociated atoms has no proper binary lift.
A Golomb subset of its marks corresponds to a C4-free edge subset of
K_r. The note gives an elementary proof that every two-color K6 has
a monochromatic C4. Hence this base cannot have the two-Golomb partition
forced by the lift. This is a complete family obstruction.

fibers/SHORT_PROGRESSION_FACTOR_0023.md gives unconditional D(7/5) for
B+{0,h,...,qh}, q=2,3,4, when B is Golomb and h>2 span(B), by classifying
fine, pure, and mixed differences and the possible clusters in a band.
Its hypothesis is different from the proper arbitrary-base theorem.

fibers/TWO_DISTANCE_PROGRESSION_EXTENSION_0026.md treats arbitrary subsets
of three layers over a two-distance Euclidean base. It proves T<=17M,
and for a full product the exact formula T=19T(X)+10M(X)+|X| gives T<=16M.
A full weight-two base gives a purely additive limiting ratio 16/3.
Proper coloring of that full model is not asserted. The later root H5
theorem covers its properly colored full-product subclass when represented
with no carry, but does not cover arbitrary partial layers.

## 5. Other new bounded inputs

fibers/SPATIAL_BAND_STRIPS_0023.md decomposes a band into spatial strips
and retains an exact color identity. Far completions produce genuine
lower-band charges, but nested outer completion pairs can have many-to-one
fan-in. Near completions and that aggregation gap remain open.

fibers/PROGRESSION_BAND_DISCOVERY_0023.py/json generated 100 new stepped
progression-cluster sources, at most 24 marks and span 300. Six high-band
candidates received one two-second call each, all raw UNSAT. No product
candidate was actually reached before the generator's cap; do not report
that products were tested. The maximal tested uncolored ratio was 46/35
on the literal source recorded in that file. No bounded negative changes
the universal source theorem.

literature/TWO_DISTANCE_GRAPH_INPUTS_0024.md identifies the exact
common-sphere Gram condition I-A+mu J positive semidefinite. It controls
the complementary adjacency matrix on the subspace perpendicular to one,
not automatically its full least eigenvalue. The standard generalized
line-graph/root classification cannot be imported without the missing
hypothesis. Root's two-distance energy theorem does not rely on it.

literature/SOURCE_COLOR_GEOMETRY_INPUTS_0026.md records a bounded search
for an edge-color-to-geometry bridge. Difference-labeled proper edge
colorings and vertex-colored geometric configurations have different
hypotheses and did not supply the actual source theorem.

literature/DIRECT_SUM_OVERLAP_INPUTS_0028.md places the 5-by-5 and 7-by-3
facts in standard bipartite Ramsey/rectangle-free array theory. Its
focused comparison did not locate a theorem packaging the present
proper-source overlap and exact product-energy argument. This is a
scoped source comparison, not a priority claim.

## 6. Continuation instructions

Root retains main method design, the general-source inequality, and the
small-color integration. The latest useful mechanism is now the complete
direct-sum overlap theorem, not a freely postulated Gram representation.
The next substantive step should go beyond the explicit dense-partial
product hypothesis or derive a general source argument using shared
overlap colors without multiplying the constant by an uncontrolled number
of blocks. A mere product representation assumption or arbitrary filling
of missing marks is not such a step. The dense-partial theorem's supported
intersection argument is available as a starting input, not a universal
structural description of high-energy sources.

The previous band, cloud, Hall-deficiency, and fan routes retain their
precise gaps in CHECKPOINT_0022.md; none was silently solved here. All
previous closed routes, including the F13 hypothesis, standalone Cartesian
constant bounds, and unweighted spectral shifts, remain closed in their
recorded scopes. Continue research, preserve full derivations, leave the
goal active, and withhold a results summary until the entire mandate is
actually achieved.
