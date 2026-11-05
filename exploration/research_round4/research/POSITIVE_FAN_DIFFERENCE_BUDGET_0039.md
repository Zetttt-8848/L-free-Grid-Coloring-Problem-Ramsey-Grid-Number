# Positive fans return to same-color anchored arcs

Root derivation, continuation 0039. This is a second forced-color
injection for the endpoint graph, complementary to
ANCHORED_FAN_ARC_BUDGET_0037.md. It also supplies a structural restriction
on the supported differences of a positive fan. Neither statement
discards missing source marks or establishes EP10.

Normalize min A=0, write B=A\{0}, n=|B|, and let z be one proper strict
two-color source coloring. For x in B use the actual colors and sets

    f(x)=z(x,0),
    P_x={y in B:x+y in B, z(x+y,y)=f(x)},
    Y_x={y in B:x+y in B, f(x+y)=f(x)}.

The existing anchored lemmas give:

* P_x union {0} is Golomb, so P_x is Golomb and sum-free;
* Y_x is Golomb;
* f(x+y)=-f(x) for y in P_x;
* z(x+y,y)=-f(x) for y in Y_x.

In particular P_x and Y_x are disjoint. Put p_x=|P_x|, k_x=|Y_x|,
p=sum_x p_x, and s=sum_x k_x. Here s is exactly the number of same-color
arcs in J_0(A). Let o be its opposite-color arc count, so the endpoint
deletion cost is e=s+o.

## 1. The positive-pair injection

Take y<z in P_x, set h=z-y, and abbreviate c=f(x). The actual cells

    (x+y,y), (x+z,z)

both have color c. Their positive corner completion

    Q=(x+z,y)

therefore has color -c. Membership in P_x also gives f(x+z)=-c.
If x+h is in B, the three supported cells

    (x+h,0), (x+z,0), (x+z,y)

form a positive corner of step y: indeed (x+z)-(x+h)=y. Its last two
cells both have color -c. Consequently

    f(x+h)=c.                                           (1)

If additionally h is in B, this is the same-color anchored arc

    x -> x+h.                                          (2)

Different positive-fan pairs cannot charge the same arc. The arc fixes
x and h; Golombness of P_x allows only one pair y<z with difference h.
This is global injectivity into arcs, not injectivity into output marks.

Let E_P be the number of triples (x,y,z), y<z in P_x, for which either
h=z-y is absent from B or x+h is absent from B. The alternatives are
counted once even if both absences occur. Then

    sum_x binom(p_x,2) <= s+E_P.                       (3)

Retaining the analogous earlier defect E_Y for same-color anchored fans
gives the simultaneous necessary pair of inequalities

    sum_x binom(p_x,2) <= s+E_P,
    sum_x binom(k_x,2) <= o+E_Y.                       (4)

Thus, for n>0, Cauchy--Schwarz gives

    p^2/(2n)-p/2 <= s+E_P,
    s^2/(2n)-s/2 <= o+E_Y.                            (5)

The two charge inventories on the right of (4) are disjoint by their
actual anchored endpoint colors. No bound on E_P or E_Y is assumed.

## 2. Supported differences are both Golomb and sum-free

Define the positive difference set Delta P_x and its supported part

    D_x=Delta P_x intersect B intersect (B-x),
    B-x={h:x+h in B}.                                 (6)

Equation (1) proves D_x subset Y_x. Hence D_x is Golomb. The new
iteration in fibers/POSITIVE_FAN_ITERATION_0039.md proves that it is
also sum-free; the short argument is included to complete the chain.

Suppose h,d,h+d all belong to D_x. Their membership in Y_x gives
f(x+h)=f(x+d)=f(x+h+d)=c. The two offset-x cells at starts h and h+d
are both -c, so their completion (x+h+d,h) has color c. But

    (x+d,0), (x+h+d,0), (x+h+d,h)

is a supported positive corner of step h whose three colors are c.
This is impossible. The reasoning includes d=h: the two distinct
starts h and 2h suffice. Therefore

    h,d in D_x imply h+d not in D_x.                  (7)

In particular the graph Gamma_x on vertex set P_x, joining y<z exactly
when z-y belongs to D_x, is triangle-free. All three edges of a triangle
would have gaps h,d,h+d in D_x.

## 3. A stronger common-neighbor restriction

The Golomb condition on D_x constrains Gamma_x beyond triangle-freeness.

**Lemma.** Any two distinct vertices of Gamma_x have at most two common
neighbors. If there are two, one lies strictly between the two vertices
and the other lies outside their closed interval.

**Derivation.** Fix u<v in P_x. For a common neighbor w, the two positive
distances |w-u| and |w-v| both lie in D_x. Distances associated with
different edges of P_x are distinct because P_x is Golomb.

If w<u, the two distances differ by v-u. Thus two common neighbors on
the left would give two distinct representations of the positive
difference v-u inside D_x, contradicting its Golomb property. The same
argument handles two common neighbors on the right. Moreover one left
neighbor and one right neighbor would also give two distinct
representations of v-u. Thus the two exterior regions together contain
at most one common neighbor.

If u<w<v, the two distances add to v-u. Two different common neighbors
in this open interval would give two different unordered pairs of
elements of D_x with the same sum. Golombness excludes this as well:
for two distinct equal-sum pairs, ordering their smaller elements
turns the equality into two distinct equal positive differences.
The four distances here are distinct by Golombness of P_x, so there
is no coincident-pair exception. Hence there is at most one interior
common neighbor. These conclusions prove the lemma.

Let t=|P_x| and j=|E(Gamma_x)|=|D_x|. Counting unordered common-neighbor
incidences gives

    sum_(v in P_x) binom(deg(v),2) <= 2 binom(t,2).

For t>0 the left side is at least 2j^2/t-j, by Cauchy--Schwarz and
sum deg=2j. Solving the resulting quadratic inequality yields

    j <= (t/4)[1+sqrt(8t-7)].                         (8)

The equality j=|D_x| holds because the positive differences of P_x are
all distinct. For t=0 there are no edges. Combining (8) with the exact
partition of all positive-fan pairs gives the lower bound on actual
support defects

    E_P(x)=binom(t,2)-|D_x|
       >= binom(t,2)-(t/4)[1+sqrt(8t-7)],              (9)

with the trivial lower bound zero used whenever the displayed expression
is negative. This is a lower bound on defects, not a way to delete them
from (3). In particular it explains why a large positive fan must have
many absent difference labels or absent translated targets.

## 4. Integration with reversed-output concentration

For each output w, let q_w count its distinct-input reversed relations
x+y=w, x<y, f(x)=f(y)=-f(w). Let G_w be the cross-support graph in
fibers/REVERSED_OUTPUT_CONCENTRATION_0039.md, and delta_w its independent
set expansion defect. Its complete derivation gives at least
q_w-delta_w positive-fan memberships among the two retained cells of
those q_w relations. Different relations and outputs give different
memberships (x,y) in the family of P_x: the membership determines its
output x+y and its ordered input pair. Therefore

    sum_w q_w <= p + Delta,
    Delta=sum_w delta_w.                              (10)

Let r_eq count equal-input reversed relations x+x=w. Their number is
at most n, but they are kept as an actual count. The earlier reversed
arc incidence is R=2 sum_w q_w+r_eq, so

    R <= 2p+2Delta+r_eq.                              (11)

Combining the established identity o-s=R-P_mono, P_mono>=0, with (4)
and (11) gives a coupled necessary system at one endpoint:

    e=s+o,
    o<=s+2p+2Delta+r_eq,
    sum_x binom(p_x,2)<=s+E_P,
    sum_x binom(k_x,2)<=o+E_Y.                        (12)

All four lines refer to one source coloring. The nonlinear terms cannot
be chosen independently of the positive-fan and cross-support graphs.
The support graph Gamma_x also obeys (7)--(9).

## 5. Scope and next implication

The new constraint sends supported pairs of positive fan labels to
same-color arcs, whereas the previous constraint sends same-color fan
pairs to opposite-color arcs. Iterating the two rules makes D_x
sum-free, and its inherited Golomb property gives the explicit
common-neighbor restriction above. Reversed-output expansion now
feeds genuine memberships into this second budget through (10).

What remains unproved is a uniform joint bound on the support defects
E_P,E_Y and the reversed-output expansion defect Delta, or a different
way to use their geometry to bound e. Equations (9) and (12) must not be
read as upper bounds on those defects. Large-span proper families may
have many holes, and the same missing numerical label can appear for
several x. The new derivation neither proves EP10/S21 nor changes the
working small-color bounds.

## 6. A four-cycle is attainable

The fresh single forced discovery in
fibers/POSITIVE_FAN_CYCLE_DISCOVERY_0039.py/json suggested a monotone
four-cycle. The subsequent auxiliary derivation
fibers/POSITIVE_FAN_CYCLE_CONSTRUCTION_0039.md supplies a literal coloring
and complete offset classification on

    A=S union (10000+S),
    S={0,1,10,100,111,1000,1001,1011,1111}.

At x=10000 it has P_x={1000,1001,1011,1111} and
D_x={1,10,100,111}. The supported graph is precisely the four-cycle
with successive increasing gaps 1,10,100 and closing gap 111. One pair
of opposite vertices has an interior and an exterior common neighbor.
Thus the common-neighbor bound two is attained on an actually proper
source. Replacing it by one, or requiring the graph to be a forest or
four-cycle-free, is not a viable universal strengthening. The source
construction gives a direct finite argument; the raw solver status
alone is not used as its proof premise.
