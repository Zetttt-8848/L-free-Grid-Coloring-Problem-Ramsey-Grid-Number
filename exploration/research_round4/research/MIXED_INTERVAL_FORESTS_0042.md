# Rooted interval forests in the weak mixed-cell system

Root derivation, continuation0042. The N-type unit/binary constraints in
WEAK_MIXED_CELL_REDUCTION_0041.md have more structure than arbitrary
binary clauses. They form two families of rooted binary trees on the
mixed intervals. Each edge strictly enlarges the interval, and the
lengths of two children add to the parent's length. In an actual proper
coloring, forward implications therefore form a forest whose sinks are
unsupported mixed differences. This supplies a weighted propagation
budget; it is not yet a source-capacity or Ramsey theorem.

Let B,C be disjoint integer Golomb sets, and prescribe their two colors
on the diagonal of W(B union C). A mixed variable is identified with
(b,c) in B times C; its physical cell is (max(b,c),min(b,c)). Write

    I(b,c)=[min(b,c),max(b,c)], w(b,c)=|b-c|>0.

All B-B strict cells have fixed color C, and all C-C strict cells have
fixed color B. Only the mixed variables remain free.

## 1. The B-derived parent map

Fix c in C and b in B. Put d=|b-c|. If d is absent from Delta B, give
(b,c) no B-parent and call it an unsupported B-root. Otherwise let
p<q be the unique B-pair with q-p=d.

If b<c, then b cannot equal p, since that would give c=q in B.

* If b<p, the endpoint cells (c,b) and (q,p) have completion (q,b).
  The last two are B-B cells of color C, so this is exactly a unit
  force of color B at (b,c). Give it no B-parent.
* If b>p, their completion is the mixed cell (c,p). The corner gives
  a binary constraint forbidding color C at both (b,c) and (p,c).
  Set the B-parent of (b,c) equal to (p,c).

If b>c, then c cannot equal p, again by disjointness.

* If c>p, the homogeneous endpoint (q,p) and mixed endpoint (b,c)
  have homogeneous completion (b,p). This forces color B at (b,c);
  give it no B-parent.
* If c<p, the completion is the mixed cell (q,c). Set the B-parent
  to (q,c); the binary constraint forbids color C at both variables.

All listed corners have their starts in increasing order and equal
positive endpoint offset d. The completion is the ordinary outer cell.
These cases are exactly the B-derived part of the N-type classification.

Whenever the parent exists, its B endpoint moves strictly away from c:
p<b<c in the first binary case, and c<b<q in the second. Thus

    I(child) is a proper subinterval of I(parent),
    w(child)<w(parent).                               (1)

Every mixed variable has at most one B-parent. Repeatedly following
parents terminates because the finite set of interval lengths strictly
increases. The underlying graph is a forest: an undirected cycle with
outdegree at most one would force a directed cycle. Its roots are
precisely the unsupported B-roots and the B-reflection unit vertices.

Exchanging B and C gives the C-parent forest at each fixed b. Its
binary edges forbid color B at both endpoints, its parents enlarge
the C endpoint away from b, and its roots are unsupported C-roots
or unit vertices forced to color C.

## 2. Each parent has at most two children

Consider a B-parent vertex (u,c) with u<c. A child is (v,c) with
u<v<c and B-difference c-v represented by the pair u<q. Hence

    q=c+u-v,   v+q=c+u.                              (2)

Conversely, any unordered pair {v,q} of B-marks strictly inside (u,c)
with sum c+u gives precisely those child vertices: both v and q
when distinct, and one when v=q. Golombness of B gives uniqueness
of this unordered pair, including repeated marks. Thus there are
zero children, one midpoint child, or two distinct children.

The same reasoning for u>c gives children strictly inside (c,u)
whose B endpoints sum c+u. It also applies to the C-forests.
Writing w for interval length, one obtains the exact local law

    two children:  w(child1)+w(child2)=w(parent),
    one child:     2w(child)=w(parent),
    no children:   sum of child lengths=0.            (3)

The one-child case is exactly a three-term progression with the
opposite-class endpoint at one end and the parent-class midpoint
inside. In all cases the sum of child lengths is at most the parent
length. No regular spacing or no-carry model is needed.

## 3. Counts of roots and constraints

Let N_B=sum_(b in B,c in C) 1_(|b-c| in Delta B), and let u_B be the
number of unit forces of color B. The mixed-cell reduction gives
u_B=2 sum_(r in C) mu_B(r). The preceding parent construction gives

    number of B-forest edges = N_B-u_B,
    number of B-forest roots = bc-N_B+u_B.             (4)

Of the roots, bc-N_B are unsupported and u_B are reflection units.
The corresponding C counts use N_C and u_C. In particular

    N=N_B+N_C,
    u_B+u_C=2K,
    number of N-type binary edges = N-2K.

An edge cannot be generated twice: the shorter interval is its
unique child, which has a unique relevant within-class difference.
B-edges and C-edges are also distinct because they fix different
opposite-class endpoints. These counts concern the N-type clauses;
the Q-type binary clauses and rho three-variable clauses remain
additional constraints.

## 4. The actual-color implication forest

Now assume a proper weak extension z is fixed. Keep one state for each
mixed variable, with its actual color. Define its forward successor by

    a color-B vertex follows its C-parent, if that parent exists;
    a color-C vertex follows its B-parent, if that parent exists.

The corresponding binary constraint forces the parent to have the
opposite color. Thus these are genuine implications between actual
states. Every successor strictly enlarges the interval by (1), so
this forward graph is a forest with one outgoing edge or none at
each vertex.

A color-B sink cannot be a C-unit root, because that would require
its color to be C. It must instead have its length absent from
Delta C. Likewise a color-C sink has length absent from Delta B.
Thus the sink set is exactly

    Z = {(b,c):z(b,c)=B and |b-c| not in Delta C}
        union
        {(b,c):z(b,c)=C and |b-c| not in Delta B}.       (5)

This conclusion uses actual properness, including the unit colors;
it does not posit a canonical coloring for arbitrary B,C.

At a color-B parent, every incoming edge belongs to its B-forest:
the child has color C and follows that B-parent. There are at most
two such children, possibly a subset of the children in Section2.
At a color-C parent the analogous statement uses its C-forest.
Consequently throughout this actual implication forest,

    sum_(incoming children) w(child) <= w(parent).     (6)

The fixed-color choice is essential here: incoming edges from both
underlying forest families are never combined at one actual state.

## 5. A weighted antichain capacity

Call a set U of actual mixed vertices an antichain if no vertex in U
lies on the forward path from another vertex in U. On each finite
rooted component, repeatedly apply (6) from descendants to the root.
An induction on the tree shows that the sum of the weights of any
antichain in that component is at most the root weight. Summing gives

    sum_(v in U) |b_v-c_v|
      <=sum_(z in Z) |b_z-c_z|.                      (7)

The right side is an explicit capacity of unsupported mixed
differences. It is at most the full unsupported weighted inventory

    sum_(b,c) |b-c|
      [1_(|b-c| not in Delta B)+1_(|b-c| not in Delta C)],

but (5) retains the actual color and usually the smaller set.

For example, (7) applies to an antichain of reflection-unit vertices.
It does not assert that all reflection-unit vertices form an antichain.
Units can in principle lie along the same forward path, and summing
their weights without accounting for that ancestry would be invalid.

The restriction to one component's antichain is also what prevents
recounting a merged implication path. The proof requires neither
disjoint numerical holes nor injectivity of the terminal sink map.

## 6. Relation to the finite-span target

This forest structure is a consequence of Golomb difference uniqueness
and unordered-pair-sum uniqueness. It strengthens the earlier observation
N<=2bc by retaining unique parents, roots, exact sibling lengths, and
the actual-color sink inventory. It also supplies a new possible way
to account for dependencies among reflection forces.

To deduce a capacity bound, one still needs a sufficiently large
antichain of forced vertices, a bound on forced vertices along one
path, or a coupling of these forests to the Q-type and three-variable
constraints. The root lengths in (7) can be large, and their number
has no currently proved useful uniform deficit. The theorem therefore
does not imply S21 or the finite R3 caps as it stands.

It is not permissible to assume that two arbitrary forest constraint
families have a cooperative two-coloring. The exact arithmetic interval
structure and the additional clauses have been stated explicitly; a
general graph theorem must match them before being used.
