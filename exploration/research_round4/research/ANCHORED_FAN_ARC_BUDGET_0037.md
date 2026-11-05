# A global arc budget for monochromatic anchored fans

Root derivation, continuation 0037. The endpoint-addition graph and its
actual column colors are defined in ANCHORED_SUM_PEELING_0037.md. This note
combines that reduction with the new auxiliary forcing lemma in
fibers/ANCHORED_SUM_COLOR_COUPLING_0037.md. It removes reuse of a charged
anchor by charging a directed addition arc instead. Missing vertices and
missing addition labels remain explicit defects.

Normalize min A=0, put B=A\{0}, n=|B|, and let J have arcs x->w whenever
x,w,w-x belong to B and x<w. Let f(x)=z(x,0) be the actual anchored color.
Write e_s and e_o for the numbers of arcs with equal and opposite endpoint
colors under f, respectively. Thus

    e(J)=e_s+e_o=T(A)-T(B).                            (1)

For x in B, let

    Y_x={y in B:x+y in B, f(x+y)=f(x)},
    k_x=|Y_x|,
    W=sum_(x in B) binom(k_x,2).                     (2)

The set Y_x is Golomb, as it lies in one actual signed fiber. Also
sum_x k_x=e_s.

## 1. Exact partition of the fan pairs

For each x and y<z in Y_x, define

    h=z-y>0,  a=x+h.                                 (3)

The anchored fan-difference lemma states that, if a is in B, then

    f(a)=-f(x).                                      (4)

Its proof uses the two anchored corners at x to force (x+y,y) and
(x+z,z) to -f(x), their ordinary completion (x+z,y) to f(x), and the
competing anchored corner at a to exclude f(a)=f(x). The support labels
y,z are in B by the definition of Y_x.

Partition the pairs in (2) into three disjoint types:

    D_step: h not in B;
    D_target: h in B but a not in B;
    I: h and a both in B.                            (5)

Use the same symbols for their cardinalities and put D=D_step+D_target.
For type I, (3) supplies an actual arc x->a of J, and (4) makes it an
opposite-color arc. This map is injective globally. The directed arc
fixes x and h=a-x. For that fixed x, Golombness of Y_x permits at most
one pair y<z with difference h. Different tails give different arcs.
Consequently

    W=I+D_step+D_target,
    I<=e_o,
    W<=e_o+D.                                        (6)

This is an arc injection, not a claim that each target a is used once.
Many different tails can point to the same a; they consume different arcs
already included in e_o. No bound on their indegrees is being assumed.

## 2. A nonlinear anchored cut inequality

For n>0, Cauchy-Schwarz applied to the k_x gives

    W=(sum_x k_x^2-e_s)/2
      >=e_s^2/(2n)-e_s/2.                            (7)

Combining (6)-(7) yields the necessary inequality

    e_s^2/(2n)-e_s/2 <=e_o+D,                        (8)

or, using e=e_s+e_o,

    e_s^2/(2n)+e_s/2 <=e+D.                          (9)

The cut on J in these formulas is specifically its coloring f inherited
from the source column. It is not an independently optimized coloring of
the addition graph. In particular, D depends on the monochromatic fans
selected by f and on the actual arithmetic support of A.

If tau(J)=|E(J)|-MaxCut(J), then e_s>=tau(J). The function
t^2/(2n)+t/2 is increasing for t>=0, so (9) also implies

    tau(J)^2/(2n)+tau(J)/2 <=e+D.                    (10)

This last form is useful only with a justified bound on D. Dropping D
would fill holes in the source and is not permitted. One may replace D by
the color-independent count of all pairs of forward addition labels
having either defect in (5), but that larger relaxation can lose the
actual-color gain.

## 3. Separating the reversed-sum additions

An unordered Schur relation x+y=w with x<y contributes two arcs, and an
equal-summand relation 2x=w contributes one. Define R to be the number of
arc incidences belonging to relations whose inputs have one anchored
color and whose output has the opposite color:

    R=2 #{x<y:x,y,x+y in B, f(x)=f(y)=-f(x+y)}
      +#{x: x,2x in B, f(x)=-f(2x)}.                (11)

A relation with opposite-colored inputs gives one arc of each type.
A relation whose two inputs and output all have one color gives only
same-color arcs. The remaining relations are exactly those in (11),
which give only opposite-color arcs. Therefore, if P counts the arc
incidences of the wholly monochromatic relations, then

    e_o-e_s=R-P,  P>=0,
    e_o<=e_s+R.                                     (12)

Equations (8) and (12) imply

    e_s^2/(2n)-(3/2)e_s <=R+D,
    e_s <=[3n+sqrt(9n^2+8n(R+D))]/2.                (13)

Hence the following conditional local estimate is complete:

    e(J) <=3n+sqrt(9n^2+8n(R+D))+R.                 (14)

For example, the special hypothesis R+D<=2n makes the square root in
(14) at most 5n and R at most 2n, giving e(J)<=10n. Such a hypothesis at
one endpoint at every deletion would supply EP10 in the preceding note.
It is a sufficient local condition only, not a universal source theorem.

## 4. Why the example hypothesis is not universal

The inherited proper weight-two source shows concretely why R itself
cannot be forced below 2n. Take increasing sufficiently dissociated
positive weights w_1,...,w_q and all pair sums

    A={w_i+w_j:1<=i<j<=q}.

Its minimum is w_1+w_2. The standard proper source coloring distinguishes
intersecting and disjoint coordinate pairs; the complete proof is also a
special case of TWO_DISTANCE_SOURCE_ENERGY_0025.md. Normalize by subtracting
the minimum and use its actual anchored coloring f. The nonzero source
marks whose coordinate pairs meet {1,2} have one anchored color, and those
disjoint from {1,2} have the other.

Coordinatewise dissociation determines every nontrivial sum relation at
this minimum. For each {j,k} subset {3,...,q}, there are exactly two:

    (w_1+w_j)+(w_2+w_k)=(w_1+w_2)+(w_j+w_k),
    (w_1+w_k)+(w_2+w_j)=(w_1+w_2)+(w_j+w_k).

Each gives two arcs after normalization. Both inputs meet the root pair,
and the output is disjoint from it. Thus every one is a reversed-sum
relation, and

    n=binom(q,2)-1,
    R=e(J)=4 binom(q-2,2),
    e_s=0, D=0.                                      (15)

There are no equal-summand relations, again by coordinatewise dissociation.
For q>=8, the difference R-2n is

    2(q-2)(q-3)-[q(q-1)-2]=(q-7)(q-2)>0.            (16)

Therefore the sufficient condition R+D<=2n is false as a universal
assertion about proper sources. The actual arc count in (15) is still
less than 4n, so it does not refute EP10. The loss in (14) is that it
permits many same-color arcs simultaneously with R, whereas this family
has none. An eventual general argument must retain that tradeoff or
control the actual degrees k_x, rather than uniformly cap R by 2n.

## 5. Remaining uniform implication

The new global fact is the injective alternative (6): every monochromatic
anchored fan pair consumes a distinct opposite-color addition arc unless
its difference or target is absent. It turns the previous charge to a
possibly reused anchor into a global graph inequality, while keeping both
arithmetic defects explicit.

The missing conclusion is a linear upper bound on e_s+e_o. Equations
(8)-(14) alone do not provide one: a large R, a large D, or their allowed
coexistence with many monochromatic fans leaves room. The proper weight-
two family shows that one tempting uniform restriction on R is invalid.
The next useful step must couple the opposite-color additions to the
monochromatic fan degrees or pay the missing-label and missing-target
defects using actual source information. No new unconditional small-color
bound is claimed.
