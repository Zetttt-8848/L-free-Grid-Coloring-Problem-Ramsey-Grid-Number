# Nested reflection tails force holes in a weak source

Root derivation, continuation0041. This strengthens the cross-anchor
packing by retaining the nesting of the same diagonal color's tails.
Every charge considered below lands at an actual absent source mark;
the mixed-pair and shared-length bins in the earlier auxiliary estimate
are unnecessary. The resulting global hole budget is complete, but it
does not yet establish a weak-source capacity or a Ramsey improvement.

Let S=B disjoint union C be the diagonal classes of one proper two-color
weak source W(S). Write b=|B|, c=|C|, n=b+c, and translate S into [0,L]
with both endpoints occupied when S is nonempty. Its two classes are
Golomb. The colors are denoted B and C as well as their classes.

For a in B put

    P_a={p-a:p in B, p>a},
    D_a=Delta P_a intersect(S-a).

The supported-difference theorem from0039 says that h in D_a forces
both a+h in C and z(a+h,a)=B. In particular D_a is Golomb and sum-free.

## 1. Exact reflection incidences

For r outside B let

    R_B(r)={(a,p,q):a<p<q in B, r=a+q-p},
    mu_B(r)=|R_B(r)|.

All these reflections lie strictly between their two extremes a,q.
Different triples at fixed r have different a and different q:
fixing a fixes the positive difference q-p=r-a, while fixing q fixes
p-a=q-r, and Golombness fixes the relevant ordered pair. Thus the
left and right endpoint sets

    A_B(r)={a:(a,p,q) in R_B(r)},
    Q_B(r)={q:(a,p,q) in R_B(r)}

both have size mu_B(r). They are subsets of B, hence Golomb. When
r in C, each left endpoint a has r-a in D_a and z(r,a)=B.
Reflection of the source order gives z(q,r)=B for every right endpoint.
Equivalently these two color conclusions follow directly from the
three same-color diagonal marks in the reflection triple.

## 2. The lower shadow is always missing

Fix r in C and a<a' in A_B(r). Put delta=a'-a and t=r-delta.
The witness for a' has the form (a',p',q') with

    a'<p'<q',  r=a'+q'-p'.

Write h=q'-p'=r-a'. Since a<a', both p',q' also lie above a. Therefore

    h in Delta P_a.                                      (1)

The two reflection incidences force z(r,a)=z(r,a')=B. If t were in S,
the three physical cells

    (t,a), (r,a), (r,a')

would form a positive corner of step delta: t-a=r-a'=h>0. Properness
would force z(t,a)=C. But (1) and t=a+h in S would give h in D_a;
the supported-difference theorem would force z(t,a)=B. This is a
contradiction. Hence

    r-Delta A_B(r) is disjoint from S.                    (2)

This is stronger than retaining the alternative that (t,a) is an
available cell of the opposite color. Tail nesting (1) eliminates
that alternative. In fact t cannot belong to B even without coloring:

    t=a+q'-p',  a<p'<q'

would then violate Golombness of B. Properness additionally excludes C.

The lower shadow t is itself an internal reflection of B, with the
displayed triple (a,p',q'). No hole outside [0,L] is introduced:
a<t<r and all these marks lie inside the source hull.

## 3. The upper shadow and the exact per-output count

Reflect the source by the map on cells

    (v,u) -> (L-u,L-v).

It preserves positive directed corners, reversing their endpoint order.
The reflected version of (2) is

    r+Delta Q_B(r) is disjoint from S.                    (3)

An explicit triple description is also useful. Take q<q' in Q_B(r),
and let (a,p,q) be the witness for q. Then

    r+(q'-q)=a+q'-p,  a<p<q<q',

so the upper shadow is another internal reflection of B. Its position
lies strictly between r and q'.

Golombness of A_B(r) and Q_B(r) makes the lower and upper shadows
separately distinct. Their ranges lie on opposite sides of r, so they
are disjoint. Consequently the shadow set

    H_B(r)=(r-Delta A_B(r)) union(r+Delta Q_B(r))

has the exact size

    |H_B(r)|=2 binom(mu_B(r),2),
    H_B(r) subset ([0,L] intersect Z) without S.         (4)

All assertions hold with B,C exchanged. They include multiplicities
zero or one, for which the corresponding shadow set is empty.

For example, (4) gives the individual restriction

    mu_B(r)(mu_B(r)-1) <= L+1-n.                        (5)

This does not contradict the sharp single-output construction in0040:
that construction has space for the quadratic number of shadows.

One can retain a smaller local interval in (4). When mu_B(r)>=2 put
alpha=span(A_B(r)), beta=span(Q_B(r)), and I_r=[r-alpha,r+beta].
All shadows lie in I_r, hence

    mu_B(r)(mu_B(r)-1)
      <=alpha+beta+1-|S intersect I_r|.                (5a)

The interval I_r lies strictly inside the hull of the B extreme marks
used by these triples: r-alpha>min A_B(r) and
r+beta<max Q_B(r). Thus only holes inside that hull can pay this output.
For mu zero or one the unlocalized zero bound already covers the case.

## 4. Global packing with ordered hole-output pairs

Let H be the holes of S in [0,L], H=|H|=L+1-n. Define

    F= sum_(r in C) binom(mu_B(r),2)
       +sum_(r in B) binom(mu_C(r),2).

Each lower shadow charge maps to (t,r), t in H, r in S, t<r.
For fixed output r its pair of same-color anchors is recovered from
delta=r-t by Golombness of that anchor class. Thus this map is
globally injective, with no multiplicity suppressed. Similarly upper
charges inject into pairs (t,r) with t>r. Hence

    F <= H^+ := sum_(t in H) |S intersect(t,L]|,
    F <= H^- := sum_(t in H) |S intersect[0,t)|.          (6)

Since each hole lies before or after each of the n marks,

    H^+ + H^- = nH.

The complete symmetric bound is therefore

    2F <= n(L+1-n).                                    (7)

In contrast to the earlier estimate F<=bc+2rho+H^+, neither occupied
mixed pairs nor shared differences are available charge bins here.
They have both been excluded by the proof of (2).

Writing S={s_1<...<s_n}, the directional capacities are also explicit:

    H^+ = sum_i [s_i-(i-1)],
    H^- = nL-sum_i s_i-binom(n,2).                     (8)

Their smaller value in (6) retains positional asymmetry that (7) loses.

## 5. Coupling to the reflection first moment

Put

    K= sum_(r in C) mu_B(r)+sum_(r in B) mu_C(r).

The positional first-moment theorem in0040 already proves K<=floor(bc/2).
There is a separate consequence of (7). For n>0, Cauchy--Schwarz gives

    2F = sum_r mu(r)^2-K >= K^2/n-K.

Combining this with (7) yields

    K^2-nK <= n^2(L+1-n),
    K <= (n/2)[1+sqrt(1+4(L+1-n))].                  (9)

The inequality with K^2-nK retains integrality without rounding the
square root. Neither (9) nor the earlier upper bound on K supplies a
lower bound on K for an arbitrary source. Missing first-level reflection
outputs can absorb many same-color triples; this remains an actual gap.

## 6. A finite graph interface for future counting

For a fixed Golomb B, let Z_B be all its internal reflection outputs.
These are disjoint from B. On Z_B place directed edges r->t for the
lower and upper shadows defined from all the triples R_B(r), regardless
of whether r is chosen as an opposite-color source mark. The construction
in Sections2-3 shows that every target is again in Z_B and that

    outdegree(r)=2 binom(mu_B(r),2).                    (10)

Every proper weak source with diagonal class B must have no such edge
from C intersect Z_B to C intersect Z_B. Moreover all neighbors of a
chosen output are absent from the entire source, by (2)-(3).

This graph depends only on the finite ruler B; its restriction is a
necessary consequence of the actual weak coloring. Equation (10)
retains the multiplicity of internal reflections rather than replacing
it by a constant. A useful finite-span capacity theorem would need an
expansion or independent-set estimate for these particular graphs,
coupled to the Golomb condition on C. No such estimate is asserted here.

The new graph is not an arbitrary graph on the interval, and ordinary
graph extremal bounds cannot be imported without their hypotheses.
The present results are complete hole-forcing and packing statements;
S21, the finite R3 capacities, and both small-color bounds remain open.
