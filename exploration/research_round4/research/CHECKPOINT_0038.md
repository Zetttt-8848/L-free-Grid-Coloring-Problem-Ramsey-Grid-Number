# Research checkpoint R4-RESEARCH-0038

Continuation of CHECKPOINT_0037.md. The previous goal turn was progress:
it changed authoritative research state through the anchored fan arc
injection, partial-matching theorem, and explicit mechanism limitations.
This continuation makes further progress through a new point-deletion
theorem on the two-distance class, reanchored fan transport, and supported
reversed-sum forcing. The full objective remains active and incomplete.
The bounds remain 21<=R3<=465 and R4<=21991300. The attributed general
growth theorem is complete and unchanged. EP10, H10, D(7/5), S21, the
finite R3 cap, and an original superior small-color method remain open
in their required generality.

All three auxiliary agents are terminal, confirmed in the live listing.
One new ordinary graph discovery ran and terminated; there were no SAT
calls, no old-record reruns, no separate audits, and no reset credit.
There is no external blocker. Keep the user-requested results summary
withheld until all objectives are achieved.

## 1. Root closes EP10 on the two-distance representation class

TWO_DISTANCE_POINT_DELETION_0038.md proves that, if A has an injective
Freiman-2 homomorphism into a Euclidean set with distinct squared
distances tau and 2tau, then every source mark a satisfies

    T(A)-T(A\{a})<=10(|A|-1).

It is stronger than an endpoint assertion on this class, but does not
improve the earlier global H7 and M<=15 span estimates already known
there. The new content is the pointwise deletion estimate. General
proper sources, including sources with three-term progressions, have
no asserted two-distance representation.

Normalize the image of a to 0 and tau to 1. There are n1 near points
of squared norm 1 and n2 far points of squared norm 2. Each far w has
q_w unordered near decompositions u+v=w, with endpoint set D_w of size
2q_w. Each actual source square through a maps to one of these;
extra geometric relations may be counted, so the deletion cost is at
most 2 sum_w q_w.

If 0 belongs to a midpoint fiber of k>=9 long pairs, the existing
separation theorem puts all incident squares in that fiber and the
cost is at most 2(k-1)<=m-2. Otherwise every q_w<=7. Let H consist of
outputs with q_w>=6.

For w in H, its q_w near pairs plus {0,w} give k=q_w+1 orthogonal
midpoint axes of squared norm 1/2. Another far point v at squared
distance 1 from w has centered vector eta=v-w/2 of squared norm 1
and inner products +/-1/4 with every axis; the root-axis sign is fixed.

For q_w=7, all norm lies on the eight axes, leaving a seven-bit code
whose pairwise Hamming distances are 2 or 4. For q_w=6, the seven
axes leave a residual of squared norm 1/8. Root closed the previously
unresolved residual issue: if two six-bit axis words differ in d
positions, their squared distance is d/2 plus a residual distance
in [0,1/2]. Allowed total distances 1 and 2 force residuals equal
for d=2,4 and antipodal for d=1,3; d=0 cannot give distinct points,
and d>=5 is impossible. All residuals therefore lie in one antipodal
pair, yielding a seventh binary coordinate and again distances 2 or 4.

A simple quadratic function-space proof bounds either seven-bit code
by 29 words. For sign codewords s, the functions

    (<s,t>-3)(<s,t>+1)

vanish at other codewords and equal 32 at s. On the sign cube they
lie in the 29-dimensional span of 1, the seven coordinates, and
their 21 pair products. Hence each high output w has at most 29 far
near-neighbors.

If D_v intersects D_w, the far outputs v,w must be near. For if their
squared distance were 2, the midpoint distance average forces v to
have squared distance 2 from every endpoint in D_w, inconsistent
with membership in D_v. Thus any near point belongs to at most 30
high-output endpoint sets. With I=sum_H 2q_w,

    I<=30n1,
    sum_H(q_w-5)<=I/7<=30n1/7,
    deletion cost <=10n2+(60/7)n1<=10(n1+n2).

The full proof includes the positive integer-source transfer and all
cases. The auxiliary notes fibers/TWO_DISTANCE_ENDPOINT_BUDGET_0038.md
and fibers/LARGE_MIDPOINT_ENDPOINT_INTERACTIONS_0038.md remain useful
derivations; their final coefficient-ten/residual gap paragraphs are
superseded by the appended root continuation and this theorem. Their
earlier 26-word spectral bound for the q=7 subcase is not needed by
root's proof; the uniform elementary bound 29 suffices.

## 2. Root: transporting fans to a later physical column

REANCHORED_FAN_TRANSPORT_0038.md starts with a same-color anchored fan
at a: labels x,y,z with 0<y<z and

    f_a(x)=f_a(x+y)=f_a(x+z)=c.

Its two forced offset-x cells have color -c, and their completion
has color c. At b=a+y, h=z-y, the actual marks b,b+h,b+x,b+x+h
therefore supply the opposite-color addition arc x->x+h in J_b.
This works even when the corresponding step or target is missing
from the original anchor's label set. No source mark is filled in.

For a target arc with endpoint colors -c,c, its incoming anchor set is

    U_(b,x,h)={a in A:a<b, a+x in A,
      z(a+x,a)=z(b+x,a)=z(b+x+h,a)=c}.

The original labels are recovered uniquely as y=b-a,z=b+h-a, so

    sum_(all anchored fans) binom(k,2)
       =sum_(opposite target arcs) |U_(b,x,h)|.

Each U is Golomb and has no pair at difference h. Such a pair would
make (b+x,a),(b+x+h,a),(b+x+h,a+h) monochromatic. Two incoming anchors
a<a' also force the earlier opposite-color arc x->x+(a'-a) in J_a.
Its step differs from h. This latter map is not asserted injective
over different target arcs. The new formulation trades the fixed-anchor
holes for real but uncontrolled transport multiplicity; an unweighted
arc budget does not follow.

## 3. Reversed sums acquire supported choices and forced incidences

fibers/REVERSED_SUM_COUPLING_0038.md keeps both physical cells of a
reversed relation x+y=w, f(x)=f(y)=-f(w).

If 0<x<y and 2x is a same-color anchor as x, then the anchored corner
at x,2x forces z(2x,x) opposite. The corner
(2x,x),(w,x),(w,y) makes at least one of the latter two cells have
the input color. Thus y in P_x or x in P_y.

The stronger reflected-cap lemma assumes x,y,x+y,2y,2y-x are present,
0<x<y, and

    f(x)=f(y)=f(2y)=f(2y-x)=s.

Two anchored corners force (2y,y),(2y,x) to -s. The corner
(x+y,x),(2y,x),(2y,y) forces z(x+y,x)=s, and the anchored addition
then forces f(x+y)=-s. In particular x belongs to P_y.

Applying this at x=r and x=2r, with the eight support marks listed in
the note and y>4r, would put r,2r in P_y. This contradicts the fact
that P_y union {0} is Golomb, equivalently the relevant sum-free
condition. Missing or wrong-color doubles and reflections leave the
general reversed-sum incidence R uncontrolled; no universal R cap
or EP10 follows from this local motif.

## 4. Column-triangle route and a small square support

COLUMN_TRIANGLES_AND_SQUARES_0038.md records the exact special-class
dictionary. A triangle in the column graph anchored at a has rows
a+x,a+x+r,a+x+r+s, and requires

    a+{0,x,r,s,x+r,r+s,x+r+s}, x,r,s>0,

with coincidences allowed. The omitted cube vertex x+s is unnecessary.
If every column graph were bipartite, independently coloring those
graphs would provide a proper strict source coloring. This is only a
sufficient strategy: ordinary proper source colors need not cut all
column edges.

New bounded discovery fibers/SQUARE_COLUMN_DISCOVERY_0038.py/json built
the ordinary column graph for square roots through 300 at anchor 1
and stopped after a BFS odd cycle was found. Planned anchors 4 and 9
were not used after this first success. No source-color SAT instance
or old coloring record was run.

The root note gives a direct literal triangle, with no graph-search
verdict as premise:

    169-121+1=49,
    289-169+1=121,
    289-121+1=169.

Thus the five-square source {1,49,121,169,289} has a triangle on rows
121,169,289 at column 1. It cannot have all those column edges cut
by two anchored colors. The special all-columns-bipartite construction
therefore cannot color every square source through 17^2. This does
not rule out arbitrary proper square-source colorings or change the
old square-energy discussion.

## 5. Narrow primary-source comparisons

literature/ANCHORED_ADDITION_INPUTS_0038.md discusses integral sum-graph
matching decompositions and full-interval monochromatic Schur counts.
An apparent identification was repaired during integration: the sum
graph is NOT the underlying anchored graph. A distinct-input sum edge
{x,y} labeled w expands to two arcs x->w,y->w; equal summands give
one arc. At B={1,2,3}, the loopless sum graph has just {1,2}, while
the anchored graph is a triangle. No external cut/fan/defect estimate
transfers from that source.

literature/ORDERED_MATCHING_COVER_INPUTS_0038.md compares ordinary
induced matchings with the one-sided ordered outer-edge condition
in a source difference fiber. Both cross edges are absent in the
ordinary induced-matching definition; source properness forces only
the relevant outer edge's opposite color. No applicable quadratic
cover theorem was located in the bounded search.

literature/PARTIAL_CUBE_COLUMN_INPUTS_0038.md finds only a full-cube
extremal theorem with a three-quarter exponent, inherited one-way
by the stronger seven-point avoidance condition. It does not provide
a square-root or energy estimate. These are bounded source maps,
not novelty or nonexistence claims.

## 6. Next central implication

Root still owns the uniform finite-span bound and R4. The geometric
point-deletion proof succeeds because high-output neighborhoods have
bounded overlap. That proof does not provide a general geometric
embedding. The actual-color route now has fixed-anchor fan-to-arc
injection, reanchored transport with incoming multiplicity, and the
double/reflected-cap constraints on reversed additions. A useful next
step must use these together to bound additions or their aggregate
cost, while retaining absent supports and repeated targets.

Do not revive a universal R+D<=2n, assume every column is bipartite,
or discard the reanchored incoming multiplicity. Reuse the completed
two-distance proof as a class input, not an object for a separate
audit. All auxiliary agents are terminal and can receive fresh
bounded derivation tasks through followup_task. The full goal remains
active, with no results summary or completion claim.
