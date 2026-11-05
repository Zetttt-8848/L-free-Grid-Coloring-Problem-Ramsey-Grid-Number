# Cartesian cuts and the source-energy transfer

Root derivation, checkpoint R4-RESEARCH-0016. This note opens a different
all-source route. The Cartesian hypothesis below and the sharper transfer
target are open. No small-color Ramsey improvement is asserted.

## 1. The Cartesian question

For finite integer sets B,C, put

    U(B,C)=sum_(h>0) r_B(h) r_C(h).

This is the number of positive, equal-step corners in B x C. Consider

    C(lambda): every properly two-colored B x C satisfies
               U(B,C)<=lambda |B||C|.

The current candidate is C(2), not an established result. See
fibers/CARTESIAN_CUT_LEMMA_0016.md for its routing formulation and
fibers/CARTESIAN_REFLECTION_0016.md for the supported inverse-corner rule.
The discovery file CARTESIAN_CUT_DISCOVERY_0016.json is finite experimental
input, not a premise for C(2).

If V(A) is properly two-colored and B,C are separated subsets of A with
every element of B less than every element of C, then C x B is a genuine
full Cartesian subregion of V(A). Swapping the names of its coordinate
sets leaves U unchanged. Thus C(lambda), if proved, applies to every such
pair, including every split of every contiguous source interval. It does
not automatically apply to two interleaved source subsets: their full
Cartesian product need not lie in V(A).

## 2. Exact decomposition at a cut

Let A=B disjoint-union C with B<C, b=|B|, c=|C|. For h>0 write

    q(h)=#{(u,v) in B x C:v-u=h}.

Then

    r_A(h)=r_B(h)+r_C(h)+q(h),
    sum_h q(h)^2=bc+2U(B,C).                         (1)

For the second identity, diagonal terms pair each cross edge with itself
and give bc. Two different cross edges have equal difference exactly when
their B endpoints have a common nonzero difference with their C endpoints.
Choosing its positive sign counts U(B,C), and reversing the ordered pair
counts it once more. All cross differences are positive because B<C.

Put

    E_+(A)=sum_(h>0) r_A(h)^2=M(A)+2T(A).

If E_+(B)<=kappa M(B), E_+(C)<=kappa M(C), and
U(B,C)<=lambda bc, then

    ||r_B+r_C||_2^2
       <=kappa M(A)-(kappa-2lambda)bc.              (2)

The triangle inequality in the Euclidean space indexed by h, followed by
(1), therefore gives the full conditional estimate

    sqrt(E_+(A))
      <=sqrt(kappa M(A)-(kappa-2lambda)bc)
         +sqrt((1+2lambda)bc).                      (3)

This explicitly retains the cross-difference term. Dropping it would lose
the source quadruples with three marks on one side of the cut.

## 3. What a bare Cauchy transfer would actually prove

For lambda>=0 define

    kappa(lambda)
      =3+8lambda+sqrt(8+48lambda+64lambda^2).         (4)

Assuming C(lambda), induction on |A| proves

    E_+(A)<=kappa(lambda) M(A)                      (5)

for every properly two-colored V(A).

Here is a complete derivation. The empty and singleton cases have both
sides zero. Split a larger A by source rank into b=floor(m/2) and
c=ceil(m/2), so that bc/M(A)>=1/2. Apply the induction hypothesis to the
two children and C(lambda) to their Cartesian cross region.

Write kappa=kappa(lambda), alpha=1+2lambda, beta=kappa-2lambda and
t=bc/M(A). The right side of (3), divided by sqrt(M(A)), is

    F(t)=sqrt(kappa-beta t)+sqrt(alpha t).

At t=1/2, formula (4) gives F(1/2)=sqrt(kappa). To obtain (4) directly,
the equality is

    sqrt(kappa+2lambda)+sqrt(1+2lambda)=sqrt(2kappa).

Squaring and isolating the positive radical gives

    (kappa+1)^2=8kappa(1+2lambda),

whose larger root is (4). This root has the positive signs in the original
radical equation.

The maximum of F occurs at

    t_*=alpha kappa/[beta(beta+alpha)]
        =alpha kappa/[(kappa-2lambda)(kappa+1)].

The root relation substitutes alpha kappa=(kappa+1)^2/8, so

    t_*=(kappa+1)/[8(kappa-2lambda)]<1/2.

The strict inequality follows from 3kappa>8lambda+1, which is immediate
from (4). Thus F is decreasing for t>=1/2 throughout the domain of its
radicals. Since the balanced cut has t>=1/2, (3) gives (5) and closes the
induction.

The corresponding source-size consequence, still conditional on
C(lambda), is

    M(A)<=kappa(lambda) span(A),                    (6)

by M(A)^2<=span(A) E_+(A). This is exactly the same positive-difference
Cauchy step used in the existing S11 transfer, with a different coefficient.

For the candidate lambda=2, formula (4) gives

    kappa(2)=19+6sqrt(10).

It exceeds 11. Consequently C(2), combined only with (1)--(3), would not
establish S11 or the requested small-color targets. This is a limitation
of this particular transfer, not a counterexample to a stronger use of
the Cartesian hypothesis.

Wolfram Language was used once during discovery to solve the equivalent
radical fixed-point equation. The algebra above is the derivation; no
separate recomputation or verification pass was run.

## 4. A sharper additive transfer target

Let D(A) count four distinct source marks

    u<b<c<v,             u+v=b+c,

and let P3(A) count three-term progressions in A. Then

    T(A)=2D(A)+P3(A).                                (7)

Indeed a collision of two equal positive differences has four distinct
marks unless the two intervals meet at an endpoint. Four distinct marks
have the displayed symmetric form and give exactly two collisions:
the two disjoint short intervals and the two overlapping long intervals.
Meeting intervals give a three-term progression. Also P3(A)<=M(A), since
its two extreme marks determine its middle uniquely.

For a separated cut B<C, U(B,C) counts exactly those four-mark patterns
whose two smaller marks lie in B and two larger marks lie in C.

Define Lambda(A) as the maximum of U(B,C)/(|B||C|) over nonempty left and
right blocks obtained by cutting any contiguous source-index interval.
A sufficient new purely additive statement would be

    T(A)<=(1+2Lambda(A)) M(A).                       (8)

It would combine with C(2) to give H5, hence the existing S11 numerical
transfers. Statement (8) is presently a conjectural route, not an available
lemma. The simpler sufficient inequality D(A)<=Lambda(A) M(A) is also
unproved. Generic cut averaging does not establish either statement:
a four-mark pattern is counted only by cuts between its two middle marks,
and that gap can be arbitrarily short compared with its outer span.
Any proof must handle that geometry explicitly, including the three-on-one
side patterns exposed in (1)--(3).

The associated auxiliary attempt is
fibers/ORDERED_ENERGY_TRANSFER_0016.md; bounded source-only diagnosis is
recorded separately in ORDERED_ENERGY_TRANSFER_DISCOVERY_0016.py/json.
