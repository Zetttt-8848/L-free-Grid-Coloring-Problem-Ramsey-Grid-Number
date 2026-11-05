# Two corner labels cannot connect a corner

Root geometric derivation, continuing checkpoint R4-RESEARCH-0012.
This supplies a lower bound for forcing-subgraph labels, not a Ramsey bound.

Fix two distinct plane points A,B. On all other plane points form a graph
G: join x,y with label A or B when {x,y,A} or {x,y,B}, respectively, is
a directed corner of positive step. A pair of corner vertices uniquely
determines its third vertex. Thus each label is a matching, and G has
maximum degree two.

**Theorem.** No connected component of G contains a directed corner.
Consequently a forcing subgraph in the fixed-class formulation must use
at least three different labels from the fixed class. This applies to
finite grid subgraphs as well, since restricting vertices and edges only
splits the plane components.

## Reduction of the two fixed points

Translation and the linear maps

    S(v,u)=(v,v-u),       J(v,u)=(-u,-v)

preserve directed corners. Substitution into the three corner vertices
shows that each map permutes the vertices of another corner of the same
positive step. We may also interchange the names A,B.

Translate A to (0,0), and write B=(a,b). In the nonaligned case, these
operations reduce to 0<b<a. To see this, interchange A,B if necessary
to make a>0. If b>a, applying J and interchanging the two fixed points
gives the relative vector (b,a). If b<0, first applying S gives
(a,a-b), whose second coordinate exceeds its first, and the preceding
operation gives (a-b,a). The cases b=0, b=a, or a=0 are aligned and
reduce by the same maps to B=(a,0), a>0.

## Nonaligned case: 0<b<a

Any vertex of degree two must share one of the three permitted line
directions with each of A and B. Intersecting the three lines through
A with the three through B gives precisely these six candidates:

    p=(a-b,0), q=(a,0), r=(a,a), s=(b,b),
    t=(0,b),   z=(0,b-a).                              (1)

The same-direction lines are parallel and distinct. Each of the other
six intersections is in (1). Some candidates could lose an edge when
its partner is a fixed point; allowing them in the list cannot omit a
degree-two vertex.

The link matching of a fixed point X=(x,y) pairs points along the rays

    X+(d,0)       with X+(d,d),
    X+(-d,0)      with X+(0,d),
    X+(-d,-d)     with X+(0,-d),       d>0.             (2)

Applying (2) to (1) gives the full neighbor table:

| vertex | neighbor under label A | neighbor under label B |
|---|---|---|
| p | l=(a-b,a-b) | q |
| q | r | p |
| r | q | s |
| s | h=(b,0) | r |
| t | (-b,0) | (a,a+b) |
| z | (b-a,b-a) | (a,b-a) |

Every displayed neighbor outside (1) has degree at most one, because
(1) contains every possible degree-two vertex. The neighbors of t,z
are outside (1). The only coincidences between l,h and (1) occur at
a=2b, when l=s and h=p. No other coincidence in this table joins its
different rows into a further component: signs and the strict
inequalities 0<b<a distinguish their remaining coordinates.

If a!=2b, the only component with more than three vertices is therefore
the six-vertex path

    l --A-- p --B-- q --A-- r --B-- s --A-- h.          (3)

The components through t,z have three vertices each. All other
components have at most two vertices.

No two vertices of a directed corner can be adjacent in G, since their
unique third vertex is the remaining corner vertex, rather than A or B.
Thus a corner in (3) would have to be an independent triple. The four
independent triples of a six-vertex path are

    {l,q,s}, {l,q,h}, {l,r,h}, {p,r,h}.                 (4)

None is a corner. In {l,q,s}, l and s lie on the diagonal v-u=0;
their completion has both coordinates positive, whereas q has second
coordinate zero. If a=2b those two diagonal vertices coincide, and
we are outside the six-vertex case. In {l,q,h}, q and h share row u=0;
their completion is (a,a-b), different from l=(a-b,a-b). In
{l,r,h}, l and r share the diagonal v-u=0; their completion is again
(a,a-b), different from h=(b,0). Finally, in {p,r,h}, p and h share
row u=0, and their completion has first coordinate max(a-b,b)<a,
whereas r has first coordinate a. This excludes every triple in (4).

If a=2b, (3) reduces to the four-cycle p,q,r,s,p, whose largest
independent set has size two. It therefore contains no corner either.
A component of at most three vertices cannot contain a corner: if it
had exactly those three corner vertices, its connectivity would give
an edge between two of them, which was just excluded.

## Aligned case: A=(0,0), B=(a,0), a>0

Every possible degree-two vertex lies on the common row u=0 or is
(0,-a) or (a,a), by the same line-intersection calculation. For a point
(x,0) with x!=0,a, its two partners under (2) are outside this list.
Indeed, under A they are (x,x) for x>0 or (0,-x) for x<0;
under B they are (x,x-a) for x>a or (a,a-x) for x<a.
Equality with either exceptional point would require x=0 or x=a.
The point (0,-a) has partners (-a,-a) and (a,-a), also outside the list.
Both potential partners of (a,a) are fixed points A or B, so this
vertex is isolated after the fixed points are removed.

There is consequently no edge between two degree-two vertices. Every
component has at most three vertices, and the last argument in the
nonaligned case excludes a corner. This completes the proof.

## Consequence for four-edge trees

A four-edge forcing tree need not have all three terminals as leaves.
It can also be a path on five vertices whose terminals occupy the two
ends and the middle vertex. Thus a matching argument at a degree-three
vertex does not by itself prove the label lower bound for every tree.
The theorem above handles both shapes, and proves a minimum of three
labels. The explicit construction in fibers/FOUR_EDGE_FORCING_GEOMETRY.md
attains three using the branching shape. Its repetition classification
is stated only for that shape.
