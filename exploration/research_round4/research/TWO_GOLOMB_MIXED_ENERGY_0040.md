# A mixed-pair energy budget for two Golomb classes

Root derivation, continuation 0040. This improves the earlier energy
estimate for a union of two Golomb sets from H3 to H2. It is an
unconditional theorem about that class, so in particular it applies to
every proper weak two-color source. It does not assert that every proper
strict source admits such a partition.

Let S=B disjoint union C be finite integer sets, with B and C Golomb.
Write b=|B|, c=|C|, n=b+c, and M=binom(n,2). Empty parts are allowed.
For positive d define

    beta_d=1_{d in Delta B}, gamma_d=1_{d in Delta C},
    X_d={u in B:u+d in C}, x_d=|X_d|,
    Y_d={u in C:u+d in B}, y_d=|Y_d|.

Golombness makes beta_d and gamma_d the actual same-class difference
multiplicities. The full multiplicity is

    r_S(d)=beta_d+gamma_d+x_d+y_d,
    sum_d(x_d+y_d)=bc.

Put rho=|Delta B intersect Delta C| and

    N=sum_d (beta_d+gamma_d)(x_d+y_d),
    Q=sum_d x_d y_d.

## 1. Exact decomposition

The same-orientation mixed collision identity is

    sum_d [binom(x_d,2)+binom(y_d,2)]=rho.            (1)

Here is its direct bijection. Two starts u<v in X_d give the unique
B-pair u,v and C-pair u+d,v+d at shared difference h=v-u; the Y_d
case reverses the classes. Conversely a shared difference h has one
B-pair and one C-pair. Their starts differ by a nonzero signed amount,
since B,C are disjoint. Its absolute value is d, and the two h-pair
endpoints give either an X_d collision or a Y_d collision according
to the sign. These maps are inverse.

Expanding the binomial of r_S(d), noting beta_d,gamma_d in {0,1}, and
then using (1), gives the exact identity

    T(S)=sum_d binom(r_S(d),2)=2rho+N+Q.              (2)

The first two terms have the immediate budgets

    2rho<=binom(b,2)+binom(c,2),
    N<=2bc.                                         (3)

The gain over the previous norm estimate comes from charging Q to
unordered same-class pairs, including the repeated-mark cases correctly.

## 2. Charging the opposite-orientation collisions

An incidence counted in Q consists of a positive d, u in X_d, v in Y_d.
It gives the equal-sum pair match

    {u,v+d} in B,    {u+d,v} in C,
    u+(v+d)=(u+d)+v.                                (4)

These are unordered pairs; one may have a repeated mark. Both cannot
have repeated marks, since that would give simultaneously u=v+d and
v=u+d, inconsistent with d>0.

Golombness implies uniqueness of unordered pair sums within either
class, with repeated marks included. Indeed, two different unordered
representations of one sum yield two equal nonzero positive differences
after their smaller terms are ordered. An arithmetic progression,
which would match a repeated pair to a distinct pair, is excluded by
the same difference argument.

Consequently each unordered B-pair in (4) matches at most one C-pair,
and conversely. A matched pair of distinct B marks and distinct C
marks contributes exactly two incidences to Q. To see this, order the
four marks as a<b'<c'<d'. The equal-sum pairs must be the outer pair
{a,d'} and the inner pair {b',c'}. If B is the outer pair, the two
mixed lengths are b'-a=d'-c' and c'-a=d'-b'; exchanging the class
names handles the other possibility. These are the two positive
opposite-orientation pairings, and they exhaust (4).

If one class pair is repeated, the other has distinct endpoints with
the repeated mark as their midpoint. It contributes exactly one
positive mixed length to Q.

Thus a match with four distinct marks contributes two to Q and uses
one distinct unordered pair from each class. A match with a repeated
mark contributes one and uses one distinct unordered pair from the
other class. Each distinct unordered pair is used at most once by
pair-sum uniqueness. Counting those resources proves

    Q<=binom(b,2)+binom(c,2).                         (5)

Repeated pairs are not extra resources in (5). Their contribution is
charged to the distinct pair on the other side, which is why replacing
this budget by the separate bound Q<=min(b^2,c^2) loses a useful term.

## 3. The uniform class theorem

Combining (2), (3), and (5),

    T(S)<=2binom(b,2)+2binom(c,2)+2bc
         =n(n-1)=2M(S).                              (6)

Equivalently, using the existing exact ordered-energy identity,

    E(S)=2n^2-n+4T(S)<=6n^2-5n.                      (7)

The empty and singleton cases are included. No source coloring was
needed beyond the assumed two Golomb classes. Every proper weak source
has those classes as its two diagonal color classes, so it satisfies
(6)-(7). For a proper strict source A, the theorem applies to each
actual weak fiber F_d, not automatically to A itself.

## 4. Why the separate mixed-deficit strengthening was unnecessary

An intermediate approach retained Q<=min(b^2,c^2) and tried to save a
linear term in N. The candidate N<=2bc-min(b,c) is false, as the
complete construction in fibers/TWO_GOLOMB_MIXED_DEFICIT_0040.md shows:

    B={0,2,5,6}, C={1,3,4,8}, N=29>28.

This does not affect (6). The proof instead counts the opposite-
orientation collision resources jointly across the two classes through
(5), leaving the valid simpler bound N<=2bc. No deficit is required at
each individual mixed endpoint.

## 5. Scope relative to the research objective

The bound E<=6n^2-5n supersedes the weaker E<=8n(n-1) input of
PROPER_PROGRESSION_PRODUCT_ENERGY_0027.md for unions of two Golomb
sets. That earlier derivation remains valid; no separate review is
being performed. The new combinatorial accounting improves its input
and can be substituted into subsequent class arguments.

The general source obstruction remains: a proper strict source need
not be a union of two Golomb sets. In fact the existing weight-two
constructions require arbitrarily many Golomb classes. Separate weak
fiber energy estimates, even when each fiber is itself Golomb, were
already shown insufficient for the main uniform source bound.
Therefore this theorem does not establish H2, S21, or an improved
Ramsey number for every properly colored strict source.
