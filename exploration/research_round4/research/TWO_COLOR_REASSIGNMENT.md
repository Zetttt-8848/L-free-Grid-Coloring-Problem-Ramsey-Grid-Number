# Reassigning two colors while fixing the third

Checkpoint-0013 update: the former target F13 is refuted by the proper
fourteen-rainbow coloring in THIRTEEN_TRIANGLE_FOURTEEN_RAINBOW.md.
The cut and packing theorems below remain valid. Their fixed-class
example does not extend to a seventeen-rainbow bound for all classes.

Root derivation continuing checkpoint R4-RESEARCH-0011. This is an exact
reformulation and a properness-preserving move system, not a Ramsey bound.

Let H be any finite three-uniform hypergraph, with a proper coloring in
colors a,b,c. Fix its color-c vertex set C and put U=V(H)\C. Let H_C be
the hypergraph of edges contained in U. Define a weighted graph G_C on U:
for each hyperedge with exactly one vertex in C, add one unit to the
edge joining its other two vertices. Multiple contributions are added.

Every reassignment of colors a,b to U is a bit vector f on U. It extends
the fixed class C to a proper three-coloring if and only if no edge of
H_C has three equal bits. Indeed, edges contained in U have precisely
this restriction. An edge meeting C and U already contains two distinct
colors. An edge contained in C cannot exist because the original coloring
was proper.

For any such proper reassignment, its exact number of rainbow hyperedges
is

    R(f) = sum_{uv in G_C} w(uv) [f(u) != f(v)].             (1)

Edges with no c or with two c's cannot be rainbow. An edge with one c is
rainbow exactly when its other two vertices receive different bits.
This proves (1), including its multiplicities. Thus fixing one color
class turns rainbow minimization into a nonnegative graph cut subject
to the requirement that every edge of H_C is nonmonochromatic.

## Exact description by flip sets

Write x_v=1 when the original a/b color of v is interchanged. In each
edge of H_C let p,q be the two originally equal-colored vertices and r
the originally different-colored vertex. Its new colors are all equal
exactly when

    x_p = x_q = 1-x_r.

Consequently a flip set S preserves properness exactly when, for every
such ordered triple (p,q;r),

    p,q in S       implies r in S,
    p,q outside S  implies r outside S.                    (2)

Equivalently, both S and its complement are closed under each implication
{p,q}->r. This condition is necessary and sufficient. In particular,
it is weaker than requiring all three vertices of every H_C edge to
be flipped together.

## The restricted component exchanges

If every connected component of H_C is flipped as a whole, (2) holds.
For component indices i,j let p_ij count the originally nonrainbow
hyperedges with one c whose other vertices lie in these two distinct
components, and let q_ij count the originally rainbow ones. For component
flip bits x_i, the rainbow count is exactly

    R(x)=R(0)+sum_{i<j}(p_ij-q_ij)(x_i xor x_j).             (3)

For such a hyperedge its other colors change equality exactly when one
of its two components is flipped. If it was rainbow it loses one; if
it was not rainbow it gains one. Edges inside a component keep their
type. This proves (3). In a coloring minimizing R over all proper
colorings, every component cut therefore has nonnegative total weight
p_ij-q_ij. This is necessary, with no claim of sufficiency.

The connected-component calculation in fibers/KEMPE_RAINBOW_PROBE.md
shows that these restricted moves give only global label permutations
from the saved 21-rainbow T_13 seed. It does not impose the stronger
conclusion that (2) has only the two constant solutions. The unrestricted
two-color reassignment problem (1)-(2) is a different, larger search.

The former hypothesis F13 (every proper T_13 has at least 17 rainbows)
is false: the new literal proper coloring has fourteen. A result in
one fixed-C problem does not establish a global lower bound.

## A packing lower bound with a direct proof

Call a connected subgraph J of G_C a forcing subgraph when its vertex
set contains all three vertices of some edge of H_C. For every proper
reassignment f, that hyperedge has two different colors. A path inside
J between two differently colored vertices contains an edge across
the cut. Thus the cut contains at least one edge of J.

Assign nonnegative weights lambda_J to any family of forcing subgraphs,
subject to

    sum_{J containing e} lambda_J <= w(e)

for each edge e of G_C. Summing the preceding one-edge lower bounds and
then interchanging the two finite sums proves

    R(f) >= sum_J lambda_J.                              (4)

This uses the common reassignment f throughout: the separate forcing
subgraphs do not receive independent colors. Edges unused by the packing
only add nonnegative cut cost. The proof applies to real nonnegative
weights; a concrete rational packing is an exact finite lower-bound
certificate for the specified fixed C.

The proposed uniform implication for F13 would have required every
feasible fixed class to admit a sufficient lower bound, for example
a packing of total weight greater than 16. That implication is now
refuted by the fourteen-rainbow coloring. A packing for one saved class
never established it.

The bounded discovery calls in two_color_reassignment_probe.json found
no coloring below 21 while fixing any one of the seed's three color
classes. Their reported optimization statuses are computation records,
not premises of the theorems here and not a proof of F13.

## Geometric cost of a forcing subgraph

For directed grid corners, every forcing subgraph has at least four
edges. Here is a direct proof. Two vertices of a corner uniquely
determine the third vertex: their shared row, column or slope-one
diagonal determines the missing corner cell. Thus a pair in an H_C
edge cannot also be an edge of G_C. The three terminals of a forcing
subgraph form an independent set in G_C.

No fourth cell is joined in G_C to all three terminals. It suffices to
prove this for the larger graph joining every two cells on a shared
row, column or slope-one diagonal. Translate and divide coordinates
by the corner step, so the terminals are (0,0),(1,0),(1,1). A point
(s,0) on their common bottom row can align with (1,1) only if s=0 or
s=1, giving a terminal. Away from that row, a common neighbor of the
first two terminals lies at the intersection of a vertical or diagonal
line through each. The only intersections are (0,-1) and (1,1).
The latter is a terminal; the former shares none of the three permitted
lines with (1,1). There is no permitted fourth cell.

A connected graph with at most three edges has at most four vertices.
To connect three pairwise nonadjacent terminals with one additional
vertex, that vertex must be adjacent to all three. The preceding
paragraph excludes it. This proves the four-edge assertion.

It follows that every packing in (4), on a directed-corner hypergraph,
satisfies

    4 sum_J lambda_J
        <= sum_J lambda_J |E(J)|
        <= sum_e w(e).                                   (5)

The last quantity is the number of corners meeting C exactly once.
In particular, a packing proving the integer bound R>=17 must have
mass greater than 16, and hence needs at least 65 such corners. This
is a limitation of this packing argument, not of other lower bounds.

## Executed finite discriminator

The discovery script fixed_class_packing_probe.py builds connected
candidate subgraphs by unions of three paths from a common root to
an H_C edge, and prunes only leaves outside that edge. These operations
preserve the required connected terminal set. It then searches for
nonnegative packings. The rational data are saved separately in
fixed_class_packing_certificate.json; they are specific to the three
saved color classes, with no coverage of other classes.

For the seed's color-2 class, the data contain 89 positive-weight
subgraphs. Their weights in units of 1/100 sum to 2041, and each graph
edge has load at most 99 units. Thus the stored packing has mass
2041/100>20 and is within unit capacities. The full graph-edge and
rooted-tree tables, with the packing proof, are displayed in
FIXED_CLASS_PACKING_INSTANCE.md. Equation (4) and integrality give
R>=21 for every proper reassignment preserving exactly this class.
The seed attains 21, so this fixed-class minimum is exactly 21.
The universal assertion proposed for F13 is now known to be false.
No solver optimum, global minimum over all classes, or Ramsey
improvement is asserted from the finite optimization statuses.

Further use of this formulation needs a different target than F13,
such as weights that retain host color information. Improving the
optimization of the three saved classes cannot repair the false
uniform seventeen-rainbow assertion.
