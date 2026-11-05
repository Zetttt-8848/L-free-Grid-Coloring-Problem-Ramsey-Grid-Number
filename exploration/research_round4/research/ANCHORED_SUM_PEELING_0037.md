# Endpoint deletion and anchored addition graphs

Root derivation, continuation 0037. This changes the location of the
remaining energy problem: it asks for a linear budget in a graph on source
marks, with its colors inherited from one physical source column. It does
not establish that budget, H10, S21, or a new Ramsey bound.

For a finite integer source A, use

    V(A)={(v,u):u,v in A, u<v},
    M(A)=binom(|A|,2),
    T(A)=sum_(d>0) binom(|A intersect (A-d)|,2).

All corners below have the original positive orientation and equal legs.
Properness always refers to one coloring of the entire V(A).

## 1. Exact endpoint deletion cost

Translate the minimum of a nonempty A to zero and put B=A\{0}. Define
J_0(A) to be the simple directed graph with vertex set B and the arcs

    x -> w  precisely when x<w and w-x is in B.       (1)

Thus an arc is an ordered addition x+y=w with x,y,w in B. Its tail x
distinguishes it from the arc y->w when x!=y. When x=y there is one arc,
not two. Write e_0(A) for the number of arcs.

The exact deletion identity is

    T(A)-T(B)=e_0(A).                                 (2)

Indeed a corner lost on deleting 0 must contain a cell whose column is
zero: zero cannot be a row of a strict cell. A positive corner whose
minimum source mark is zero has a unique expression

    (x,0), (w,0), (w,w-x),
    0<x<w, x,w,w-x in B.                              (3)

This is a corner of step w-x, with both legs equal and positive. Formula
(3) is a bijection from the arcs in (1) to the lost corners. Every corner
not using zero remains in V(B), proving (2).

Equivalently, let D_0 count the unordered decompositions x+y=w with
0<x<y and x,y,w in B, and let P_0 count x>0 with x,2x in B. Then

    e_0(A)=2D_0+P_0.                                  (4)

The factor two records two different corners on a four-mark additive
parallelogram. The three-mark progression contributes just one corner.

For a={min A} before normalization, replace every mark t by t-a.
Reflection A -> max(A)-A provides the analogous maximum-endpoint graph
and cost e_max(A). Reflection of source cells is

    (v,u) -> (max(A)-u, max(A)-v),

which preserves the strict triangle and sends an original positive corner
to an original positive corner after reversing the order of its three
listed cells. Thus properness and the deletion identity hold at either end.

## 2. A sufficient endpoint budget, and its exact scope

Consider the following open assertion:

    EP10: Every proper two-color source A with |A|>=2 has an
          endpoint a in {min A,max A} whose deletion loses at most
          10(|A|-1) corners.                          (5)

Repeatedly select such an endpoint. All remaining strict triangles inherit
the same proper coloring on their surviving cells. By (2) and its reflected
version, telescoping the successive deletion costs gives

    T(A) <= 10 sum_(j=1)^(|A|-1) j =10M(A).           (6)

Consequently the existing difference Cauchy argument gives

    M(A)^2 <= span(A)[M(A)+2T(A)] <=21 span(A) M(A),
    M(A)<=21 span(A).                                (7)

The zero-pair cases are immediate. Hence EP10, if established for all
proper sources of span at most 99994, would suffice for the finite S21
target: endpoint deletion only decreases span. The already completed
conditional transfers in FINITE_SOURCE_SIZE_TARGET_0018.md then apply.
They are not asserted unconditionally here.

It is enough to prove the stronger one-sided statement

    e_0(A)<=10(|A|-1)                                 (8)

for every proper source normalized at its minimum. The alternative in
(5) leaves additional room by permitting either endpoint. Neither (5)
nor (8) has been proved. H10 by itself has not been shown to imply either
endpoint assertion; the implication derived here goes from (5) to H10.

There is also a useful necessary feature of a minimal H10 counterexample.
If A is inclusion-minimal among proper sources with T(A)>10M(A), then for
every mark a in A,

    T(A)-T(A\{a}) >10(|A|-1).                         (9)

This follows by subtracting T(A\{a})<=10 binom(|A|-1,2) from the strict
failure at A. In particular, both endpoint addition graphs of such an A
would have more than 10(|A|-1) arcs. Equation (9) is a reduction for a
potential counterexample; it does not rule one out.

## 3. The actual anchored colors constrain the graph

Continue with min A=0. Let the two cell signs be +1 and -1, and define

    f(x)=z(x,0), x in B.                              (10)

These are actual colors of one source column, shared by all additions in
J_0(A). For an arc x->w, put y=w-x and

    g_x(y)=z(x+y,y).                                  (11)

By (3), properness says that f(x),f(x+y),g_x(y) are not all equal. In
particular,

    f(x+y)=f(x)  implies  g_x(y)=-f(x).               (12)

For a fixed x in B, split its positive addition labels into

    P_x={y in B:x+y in B, g_x(y)=f(x)},
    Q_x={y in B:x+y in B, g_x(y)=-f(x)}.              (13)

There are three simultaneous consequences:

    P_x union {0} is Golomb;
    Q_x is Golomb;
    f(x+y)=-f(x) for every y in P_x.                 (14)

The first two follow from the actual signed fiber of offset x, whose
starts are {0} union P_x union Q_x. Its start-zero cell has sign f(x),
so zero belongs specifically to the first Golomb class. The third
assertion is the contrapositive of (12), using the two-color palette.

For clarity, the signed-fiber fact in this application can be derived
directly. If one sign class of starts contains distinct equal-difference
pairs a,a+h and b,b+h, take a<b. The endpoint cells on offset x at a,a+h
force (a+h+x,a) to the opposite sign, and those at b,b+h force
(b+h+x,b) to that same opposite sign. These two cells lie on offset x+h,
so they force (b+h+x,a) back to the original sign. But the original
offset-x cells at a and b+h force this very cell to the opposite sign.
All cited source coordinates belong to A. This contradiction proves
Golombness, including the case in which the equal-difference pairs share
one start.

The placement of zero in (14) has additional content. The positive set
P_x is sum-free:

    u,v in P_x  implies  u+v not in P_x.             (15)

Otherwise {0,u+v} and {u,v} give distinct equal-sum pairs in P_x union
{0}; equivalently its positive difference u has the representations
(u,0) and (u+v,v). This includes u=v, which would give an arithmetic
progression 0,u,2u.

Another way to record the forced part is to set

    N_f^+(x)={w in B:w>x,w-x in B,f(w)=f(x)}.

Then

    N_f^+(x)-x is contained in Q_x,
    N_f^+(x) is Golomb.                              (16)

Thus monochromatic forward neighborhoods in the anchored vertex coloring
are not arbitrary graphs: each sits inside a single actual opposite-sign
fiber class. The remaining forward neighbors are not freely recolorable;
their labels and colors are still the physical cells in (11).

## 4. Addition patterns and the unclosed cost

For x,y,w=x+y in B with x!=y, there are two arcs and two internal cells
g_x(y),g_y(x). Their forced-color alternatives are:

* If f(x)=f(y)=f(w), both internal cells have the opposite sign.
* If f(x)!=f(y), exactly one input has the sign of f(w); the cell paired
  with that input is forced to the opposite sign. The other cell is
  constrained by the rest of the source but not forced by this triple.
* If f(x)=f(y)=-f(w), this triple by itself forces neither internal cell.
  Membership in P_x and P_y must nevertheless satisfy (14)-(15).

These cases follow directly from (12), once for each input. They identify
why a mere Schur coloring of B is not a substitute for the actual source
coloring. The last type may give many additions, while its internal cells
still participate in other source corners and in the shared fibers.

The elementary Golomb bounds on P_x and Q_x separately give only square-
root bounds for a single forward degree. Adding these bounds over x is
not a linear arc budget. Similarly, the fact that f has two vertex colors
does not make J_0(A) bipartite, sparse, or a bounded-degeneracy graph.

The new focused implication to pursue is therefore (5), or its stronger
form (8), using (12)-(16) together with the actual colors inside V(B).
It would suffice to control one endpoint at each deletion; no estimate
on every numerical difference or every physical completion load is
required by the telescoping argument. The main unresolved step remains
the linear bound on those anchored additions, and the working Ramsey
bounds have not changed.
