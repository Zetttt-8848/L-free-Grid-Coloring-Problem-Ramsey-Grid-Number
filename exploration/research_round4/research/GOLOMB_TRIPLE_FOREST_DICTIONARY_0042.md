# Exact triple convolution and the interval-forest branching dictionary

Root derivation, continuation0042. This note translates the one-ruler
arithmetic of MIXED_INTERVAL_FORESTS_0042.md into exact convolution
counts. It supplies inputs for a joint finite-span argument, not a new
Ramsey bound.

Let B be an integer Golomb set of size b, and define

    lambda_B(r)=#{(u,v,w) in B^3:u+v-w=r}.

The two positive coordinates are ordered. Let Delta B be the set of
positive B-differences, and write D_1(B)=sum_(d in Delta B) d.

## 1. Exact query representation

For r outside B,

    lambda_B(r)=sum_(u in B) 1_(|r-u| in Delta B)<=b. (1)

Indeed, after fixing u the equation is v-w=r-u, a nonzero signed
difference with at most one B representation. Conversely each
supported query gives that unique ordered pair v,w.

For r in B, Golombness says that u+v=w+r implies equality of the
unordered pairs {u,v} and {w,r}. This unordered-sum uniqueness includes
repeated marks: a nontrivial equality with a repeated mark would give
two equal positive differences in B. For every w different from r
there are two positive-coordinate orders, and for w=r there is one.
Consequently

    lambda_B(r)=2b-1  (r in B),
    sum_(r not in B) lambda_B(r)=b(b-1)^2.           (2)

The second identity subtracts b(2b-1) from the total b^3 triples.

## 2. Three disjoint types outside B

For r outside B define:

* mu_B(r): the number of triples a<p<q in B with r=a+q-p;
* nu_B(r): the number of triples a<p<q in B for which either
  r=p+q-a or r=a+p-q;
* delta_B(r): the number of ordered distinct pairs a,c in B with
  r=2a-c.

Every off-B ordered triple either has three distinct marks or has its
two positive marks equal. Coincidence between a positive and the
negative mark would put r in B. In the distinct case, subtracting
the middle mark gives mu, while subtracting an extreme gives nu.
Both have two orders for their positive marks. Thus

    lambda_B(r)=2mu_B(r)+2nu_B(r)+delta_B(r).         (3)

Summing over all r outside B gives separately

    sum mu_B=binom(b,3),
    sum nu_B=2binom(b,3),
    sum delta_B=b(b-1).                             (4)

Every displayed output is outside B by unordered-sum uniqueness.
An internal output is inside its triple's extreme interval. An
external distinct-triple output lies beyond one extreme of its own
triple, but need not lie outside the hull of all of B. That distinction
matters in any later finite-span localization.

## 3. Dictionary for a fixed opposite endpoint

Fix r outside B and form the B-parent forest on the b vertices (u,r).
The definitions and positive-corner construction are those in
MIXED_INTERVAL_FORESTS_0042.md, without needing a chosen color at r.

An internal reflection supplies its two unit roots, at the extreme
endpoints a,q. Distinct occurrences cannot share a given endpoint:
that endpoint and r recover a supported B-difference and its unique
representing pair. Hence there are exactly 2mu_B(r) unit roots.

A binary branch with parent endpoint u has two distinct children
v,w strictly between u and r, with v+w=u+r. If r>u this is the
external reflection r=v+w-u; if r<u it is the other external type.
Conversely every such external reflection gives exactly this parent
and its two children. Thus there are nu_B(r) two-child vertices.

A unary branch has midpoint child v, with r=2v-u. It corresponds
bijectively to a delta_B(r) occurrence. The complete dictionary is

    supported queries             lambda_B(r),
    unsupported roots             b-lambda_B(r),
    unit roots                    2mu_B(r),
    two-child vertices            nu_B(r),
    one-child vertices            delta_B(r),
    forest edges                  2nu_B(r)+delta_B(r),
    forest roots                  b-lambda_B(r)+2mu_B(r).

The edge formula agrees with lambda_B-2mu_B by (3). It is an exact
decomposition of the query inventory, not an assumption that the
unit roots and unsupported roots are distributed evenly.

## 4. A weighted global query identity

Define the supported interval mass at an outside point by

    Q_B(r)=sum_(u in B) |r-u| 1_(|r-u| in Delta B).

Then

    sum_(r not in B) Q_B(r)=2(b-1)D_1(B).           (5)

To see this, for each u in B and each d in Delta B first count the
two queries r=u+d and r=u-d. Their combined weight is 2d, so the
total before excluding r in B is 2bD_1(B). The excluded ordered
pairs (u,r) in B^2 with u different from r have combined weight
2D_1(B). Subtraction gives (5).

This identity sums over all integer outputs with supported queries;
there are finitely many. It cannot be substituted for an interior
window sum without retaining the exterior terms.

## 5. Interface with actual weak colors

For a disjoint second Golomb class C, the B contribution to the
mixed supported-query inventory is

    N_B=sum_(r in C) lambda_B(r),

and its unit count is 2sum_(r in C)mu_B(r). The analogous C terms
give the two underlying forest families. For an actual proper weak
coloring, MIXED_INTERVAL_FORESTS_0042.md selects one outward
successor at each mixed state and routes it to a color-compatible
unsupported sink. The chosen successors form a length-conserving
binary forest. This dictionary identifies the arithmetic origin of
each branch or unit but does not remove the need for that actual
color choice.

In particular the identities do not supply a lower bound for N_B,
for selected reflection mass, or for an antichain of units. Selecting
only C outputs can discard a large part of the global totals in
(2), (4), and (5). Bounding that selection using finite span and the
common proper colors is the unresolved capacity step.
