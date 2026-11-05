# Research checkpoint R4-RESEARCH-0046

Continuation of CHECKPOINT_0045.md. This checkpoint also records the
user's subsequent change of objective from continued silent research to
a progress report. New exploration stopped when that change arrived.
The reporting request is separate from completion of the original
mathematical campaign. No new unconditional small-color bound was derived.

## Objective status

Of the four original major objectives, one is complete: the general
polynomial-exponent growth bound, as the attributed literature corollary
in GENERAL_BOUND.md. The original superior-method objective, R3<465,
and R4<100000 (with aspirational R4<10000) remain unmet.

The working bounds remain 21<=R3<=465 and R4<=21991300. Counting the four
objectives equally gives25% completion. This is only an objective-count
measure, not a credible estimate of remaining research time or difficulty.
The central global argument remains missing.

S21, H10, EP10, G9, D(7/5), F11(5), and F12(7) are still open. The
completed S21 transfer would give R3<=379 and R4<=99996, but neither is
an unconditional bound. These are available consequences of an unproved
premise, not achievements of this continuation.

## Completed0046 output inventory

Before this checkpoint and the status report, the0046 batch contains ten
completed mathematical/support notes: seven derivation or construction
notes, two bounded computational summaries, and one literature map.
The script and JSON accompanying one summary are not counted as extra
research tasks. This is a count of this latest batch, not a retrospective
count of all delegated assignments in the campaign.

Derivation/construction notes:

1. THREE_CUBE_MIXED_CORNER_MINIMUM_0046.md.
2. fibers/PARTIAL_FORCING_BLOCK_LABELS_0046.md.
3. fibers/CROSS_DIRECTION_FORCING_BLOCKS_0046.md.
4. fibers/SEMI_INDUCED_BLOCK_DENSITY_0046.md.
5. fibers/TWO_ANCHOR_CROSS_MASS_0046.md.
6. fibers/COMPANION_FORCING_CUBE_SLOTS_0046.md.
7. fibers/ALMOST_MONOCHROMATIC_ANCHOR_FORCING_0046.md.

Bounded summaries:

8. fibers/WEAK_CROSS_MASS_DISCOVERY_0046.md.
9. fibers/COMPANION_CORNER_METRICS_0046.md, with its new script and JSON.

Literature map:

10. literature/ORDERED_MATCHING_BLOCK_INPUTS_0046.md.

## Root: sharp mixed-corner cost of a three-cube

For an injective positive three-cube in an actual proper strict source,
each of its three primitive difference fibers has four cube starts. A
same-color fiber class is Golomb, whereas these four starts form a
parallelogram and are not Golomb. Their color split is therefore
nonconstant and contributes at least3 mixed parallel-endpoint pairs.
The three primitive offsets are distinct, giving at least9 mixed corners.

The new symbolic three-cube coloring attains9 for positive2-dissociated
weights. Give color1 to empty/singleton and empty/doubleton cells,
singleton/full cells, and singleton/complementary-doubleton cells; all
other cells have color0. Signed-support classification supplies the full
properness derivation. The exact profile is M28,T24,B9,H15. Thus9 is the
sharp minimum in the separated family. An all-forcing proper source
cannot contain an injective positive three-cube. Cube avoidance alone
does not give the needed global energy estimate.

## Partial forcing blocks and their limitations

For a separated one-column partial forcing block with inputs a and
outputs b, the third mark is c=u+b-a in A. Two edges with the same c
force their northeast cross edge to be absent from the forcing block.
For fixed c the collision-to-missing-edge map is injective; globally,
its exact reuse r_f must be retained. With label multiplicities m_c,

    sum_c binom(m_c,2)=sum_missing f r_f,
    r_f<=min(number of repeated labels, endpoint degrees,p-1,q-1).

The note gives the resulting quadratic inequality for the edge count
and an abstract sharp reuse pattern. It does not assert that every
abstract block has a full proper source extension.

The source map identifies this one-sided matching rule with a
semi-induced matching condition, using Gandhi et al., Radio aggregation
scheduling, TCS840(2020), Definition1. The actual number of labels is at
most |A|, not |A|^2; this scope correction is preserved in the note.
No literature theorem closing the global forcing-edge budget was used.

The new abstract countermodel retains even the correct label cap:
N=3^d, A=[0,4N], I=[1,N], B=[3N+1,4N], and edges have a+b=4N+s,
where s has ternary digits0/1. It has at least2^(d-1)(N-1) edges,
all difference labels in A, and the one-sided collision exclusion.
Thus these necessary block conditions alone do not imply O(|A|) edges.
The interval A is not a proper source; this is no counterexample to G9.

The cross-direction2-by-2 overlap note derives actual missing-mark or
forced-color alternatives at slots r_j+(a_i-u). If all four slots are
present, they are distinct; the possible off-diagonal coincidence
produces a monochromatic corner. Further closures retain their support
conditions. No global reuse budget is obtained.

## Companion forcing parallelograms

For a four-mark additive parallelogram, call it FF when both companion
corners have monochromatic parallel endpoints, FM when exactly one
does, and MM when neither does. Its FF side cells all have the color
opposite to its outer completion.

For three marks x<y<z, the possible fourths are

    ell=x+y-z, middle=x+z-y, right=y+z-x.

The middle FF completion cannot coexist with either exterior FF
completion. Both exterior FF completions are also impossible when
x,y,z form an arithmetic progression. In the nondegenerate case, if
both exterior completions are FF and the middle mark is present, its
two companion corners must both be mixed.

For two adjacent FF faces of an injective positive three-cube, their
three shared-direction cells have one color. Either at least one of
the two remaining cube slots is absent, or the top shared-direction
cell has the opposite color and produces three explicit mixed corners.
The note gives a direct shared-completion contradiction and retains
both open slots. It does not claim a full coloring from the partial
seven-slot assignments or a global constant on mixed-corner reuse.

The bounded companion metrics from saved symbolic witnesses are:

    three-cube: FF6, FM3, MM3; H15,B9;
    four-cube: FF15,FM45,MM40; H75,B125;
    weight-two with five atoms: FF15,FM0,MM0; H30,B0.

These are descriptive finite inputs, not the universal source proof.

## Two additional bounded results and one closed premise

The two-anchor note proves T(S)<=2bc for disjoint Golomb diagonal
classes B,C when min(b,c)<=2. It uses the exact decomposition
T=2rho+N+Q, the two-anchor relation N=2b-R+E, Q<=4, and the completed
joint-query bound for the two small remaining sizes. It does not extend
the theorem to arbitrary class sizes.

The proposed universal weak inequality T(S)<=2bc is false: the saved
proper weak twelve-mark witness has b=c6 and T74>72. Its new measured
difference profile is1^1,2^11,3^8,4^3,7^1. This also rules out universal
weak T<=M. The old valid weak bound T<=2M is unaffected.

For an all-forcing source, numerical difference colors are well defined.
At a minimum endpoint0, every positive addition x+y=w in A obeys
f(x)=f(y)=-f(w). Hence a uniform nonzero anchor color makes the endpoint
addition count zero. With exactly one exceptional anchor mark r,
the only additions are decompositions x+y=r and possibly r+r=2r.
The involution x->r-x proves the sharp deletion bound

    e_0(A)<=|A|-2.

A separated reflected family attains equality for arbitrarily many
marks. This is a one-endpoint special case: the anchor condition need
not survive deletion, so no unrestricted peeling theorem follows.

## Remaining research gap and execution state

The latest root-owned main route was to turn actual-color local forcing
constraints into a global source-mark payment. Companion FF/FM/MM
configurations were being explored when the user requested the report.
No unwritten global FF inequality, canonicalization theorem, or general
source bound is asserted.

The strongest concrete sufficient target remains a source estimate such
as binom(|A|,2)<=21span(A) for every actual proper strict source in the
specified finite range. Global energy and forcing-edge budgets would
suffice, but they remain unproved. The gap is mathematical, not merely
calculation, exposition, or a final review.

All three auxiliary agents are terminal. No root solver or shell session
is live. No usage reset was authorized or performed. No separate audit
or formalization was undertaken. The original campaign is incomplete;
completion of the user's newly substituted status-report objective must
not be described as completion of that campaign.
