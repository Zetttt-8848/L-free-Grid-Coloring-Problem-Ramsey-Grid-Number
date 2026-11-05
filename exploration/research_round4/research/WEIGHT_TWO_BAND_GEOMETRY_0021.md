# Single-band geometry of weight-two source models

Root new derivation, checkpoint 0021. This note uses the completed
weight-two source construction from CONSTANT_WEIGHT_SOURCES.md as an
input. It does not repeat its coloring proof. It proves a band theorem
for this model and identifies its sharp asymptotic coefficient. It does
not prove D1 or D(7/5) for arbitrary properly colored sources.

## 1. The model and its inherited fiber structure

Let w_1,...,w_r be distinct integers such that

    sum_i c_i w_i=0, c_i in {-2,-1,0,1,2}
    implies every c_i=0.                              (1)

Take A={w_i+w_j:i<j}. Then m=binom(r,2), and the inherited coloring by
intersection size of the two indexing pairs is proper in two colors.
Its only difference fibers with more than one representation correspond
to exchanges w_j-w_i: each has r-2 representations. All differences
joining disjoint indexing pairs are singletons. This is exactly the
fiber classification already derived for the weight-two construction.

For any real H>0 let G_H be the graph on the r weights with an edge
between w_i,w_j when H<=|w_i-w_j|<2H. Thus

    T_H=e(G_H) binom(r-2,2).                          (2)

## 2. A triangle-free graph supplies the band bound

G_H contains no triangle. If a<b<c were its three weight values, the
edges ab and bc would give b-a>=H and c-b>=H, so c-a>=2H, excluding ac.

Here is the elementary edge bound needed for completeness. In any
triangle-free graph on r vertices, adjacent vertices x,y have disjoint
neighborhoods, hence deg(x)+deg(y)<=r. Summing over all edges gives

    sum_x deg(x)^2<=r e.

Also sum_x deg(x)=2e, and Cauchy--Schwarz gives

    4e^2/r<=sum_x deg(x)^2<=r e.

For e>0, this yields e<=r^2/4; for e=0 the same inequality holds.
Since e is integral, e<=floor(r^2/4). For r>=4, (2) therefore gives

    T_H/M
      <= floor(r^2/4) binom(r-2,2)
                          / binom(binom(r,2),2)
      = r(r-3)/(r^2-1),             r even,
        (r-3)/r,                   r odd.            (3)

Both quantities are below one. For r<=3 there are no repeated-fiber
pairs, so the band count vanishes. Consequently D1 holds throughout
this weight-two model, for every positive H, not just dyadic H.

The mechanism here is a triangle-free graph of exchanges between the
underlying weights. The graph of differences on the source marks A
itself is also triangle-free in one band, but (2) is special to the
weight-two model; it must not be assumed for an arbitrary source.

## 3. Concentration makes coefficient one asymptotically necessary

For r=2n>=4, start with v_i=5^i, 1<=i<=2n, and put S=sum_i v_i.
Choose a power of two H>8S and set D=3H/2, an integer. Define

    w_i=v_i,       1<=i<=n,
    w_i=D+v_i,     n<i<=2n.                          (4)

These weights satisfy (1). Indeed a relation as in (1) becomes

    D sum_{i>n}c_i + sum_i c_i v_i=0.

The second summand has absolute value at most 2S<D. Since the first
is an integer multiple of D, both summands must vanish. If the remaining
power-of-five relation had largest nonzero index j, its largest term
would have magnitude at least 5^j, greater than 2 sum_{i<j}5^i; hence
no such j exists.

Within either group in (4), all positive differences are below S<H.
Every cross-group difference lies between D-S and D+S, and these are
strictly between H and 2H. Thus G_H is exactly K_{n,n}. Equation (2)
and the even case of (3) now give the exact ratio

    T_H/M = 2n(2n-3)/[(2n-1)(2n+1)]
           = 1-(6n-1)/(4n^2-1) -> 1.               (5)

The sources have the inherited proper two-coloring, and H is dyadic.
Thus no universal single-band coefficient smaller than one can hold
for all properly two-colored sources. In particular a proof strategy
aiming below one would fail even within this explicit model. The open
D(7/5) target has room above this obstruction.

This model analysis supports a concrete next question: can the active
repeated-fiber count of a general proper source be represented or bounded
by an analogous triangle-free exchange count, with a controlled error?
No such representation is established here, and no Ramsey bound changes.
