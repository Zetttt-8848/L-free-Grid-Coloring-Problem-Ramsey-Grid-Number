# Proper progression products have a uniform energy bound

Continuation 0040: TWO_GOLOMB_MIXED_ENERGY_0040.md improves the class
input below to E(S)<=6|S|^2-5|S|. The complete successor derivation
PROGRESSION_PRODUCT_REFINEMENT_0040.md gives T(A)<=7M(A)/2 and
M(A)<=8span(A) under the same full progression-product hypotheses.
The historical argument below remains valid but is no longer the
strongest saved estimate for this class.

Root derivation, continuation 0027. The theorem below uses actual source
properness through the entire overlap at one step. It applies to complete
no-carry progression products, with an arbitrary base. It does not assert
that a general proper source has this form. The Ramsey bounds are unchanged.

## 1. Energy of a union of two Golomb sets

For a finite set S in a torsion-free abelian group, put n=|S| and

    q_S(v)=#{(x,y) in S^2:y-x=v},
    E(S)=sum_v q_S(v)^2.

For an integer set also write M(S)=binom(n,2) and
T(S)=sum_{d>0} binom(r_S(d),2). Then

    E(S)=2n^2-n+4T(S).                              (1)

If S is Golomb, its nonzero signed differences each occur once, so

    E(S)=2n^2-n.                                    (2)

Suppose S=S_0 disjoint-union S_1, with both parts Golomb. We claim that,
for n>=2,

    E(S)<=8n(n-1),
    T(S)<=3M(S)-n/4.                               (3)

Here and below an empty Golomb part is permitted. To derive the needed
norm inequality without invoking a Fourier estimate, define

    q_{U,V}(v)=#{(u,w) in U x V:w-u=v}.

Counting two equal cross differences gives

    sum_v q_{U,V}(v)^2=sum_v q_U(v)q_V(v)
                        <=sqrt(E(U)E(V)).           (4)

The equality follows by rearranging w-u=w'-u' as w-w'=u-u'; the
symmetry q_U(v)=q_U(-v) removes any orientation convention. The four
ordered part types in S^2 give

    q_S=q_{S_0}+q_{S_1}+q_{S_0,S_1}+q_{S_1,S_0}.

The triangle inequality in l2 and (4) imply

    E(S)^(1/2)
      <=E(S_0)^(1/2)+E(S_1)^(1/2)
                           +2(E(S_0)E(S_1))^(1/4),

and consequently

    E(S)^(1/4)<=E(S_0)^(1/4)+E(S_1)^(1/4).          (5)

Put f(x)=(2x^2-x)^(1/4) for x>=1. Its second derivative is

    f''(x)=(-16x^2+8x-3)/[16(2x^2-x)^(7/4)]<0.

If both parts are nonempty, their sizes n_0,n_1 are at least one.
Concavity, (2), and (5) give

    E(S)<=[f(n_0)+f(n_1)]^4
         <=[2f(n/2)]^4=8n^2-8n.

If one part is empty, (2) gives the same inequality because
8n^2-8n-(2n^2-n)=n(6n-7)>=0 for n>=2. This proves the energy assertion
in (3). Subtracting 2n^2-n in (1) proves its T assertion. The singleton
case is kept separate: E(S)=1 and T(S)=0 there.

## 2. The overlap supplied by an actual source coloring

Let B be a nonempty finite integer set, m=|B|, Q>2 span(B), and t>=2
an integer. Form the complete progression product

    A=B+Q{0,1,...,t-1}.                              (6)

All these translates are disjoint. Suppose V(A) has a proper two-color
coloring for the original directed positive equal-step L. Its overlap
at step Q is exactly

    F_Q=A intersect (A-Q)=B+Q{0,1,...,t-2}.           (7)

The cells (v+Q,u), for u,v in F_Q with u<=v, belong to V(A). They are
a translated weak source triangle W(F_Q), so their inherited coloring
is proper. The established weak-triangle diagonal lemma says that each
of its two diagonal color classes is Golomb. Thus F_Q is a union of two
Golomb sets. This uses the colors shared by the full source; mere
properness of the two individual layers would not supply it.

Section 1 therefore yields, when (t-1)m>=2,

    E(F_Q)<=8(t-1)m[(t-1)m-1].                       (8)

The same implication applies whenever F_Q is otherwise known to admit
a two-Golomb partition, even without a proper coloring of all of V(A).

## 3. Exact no-carry energy factorization

For P_s={0,1,...,s-1}, direct difference counting gives

    e_s:=E(P_s)=s^2+2 sum_{j=1}^{s-1}(s-j)^2
               =s(2s^2+1)/3.                       (9)

Equality of two differences in B+QP_s forces equality of both coordinate
differences: the discrepancy of the B differences has magnitude at most
2 span(B)<Q, and cannot cancel a nonzero multiple of Q. Hence the
ordered difference multiplicities factor coordinatewise, including
the zero coordinate differences. Summing their squares proves

    E(B+QP_s)=e_s E(B).                             (10)

In particular, writing rho_t=e_t/e_{t-1}, equations (8)-(10) give

    E(A)<=8 rho_t [(t-1)^2 m^2-(t-1)m].             (11)

This exact factorization, rather than an unrestricted union estimate
for the layers, is what retains a useful constant.

## 4. Uniform product theorem

We prove from (11) that

    E(A)<=12(tm)^2-11tm,
    T(A)<=5 binom(tm,2).                           (12)

Let D_t=2(t-1)^2+1. The difference between the proposed energy upper
bound in (12) and the right side of (11) is

    (tm/D_t) [4m(t-2)(2t^2-4t-1)-6t^2+44t-25].    (13)

For t=2 the bracket is 39, so it is positive. For t>=3, the coefficient
of m in the bracket is positive. Since m>=1, the bracket is at least

    8t^3-38t^2+72t-17.                             (14)

At t=3 and t=4 this expression is respectively 73 and 175. For t>=5,
its first two terms equal t^2(8t-38)>=2t^2, and the remaining term
72t-17 is positive. Thus (13) is positive for all t>=2 under the
non-singleton hypothesis used in (8). The exceptional case
(t-1)m=1 is t=2,m=1, when A has two points and T(A)=0 directly.
This proves the first assertion in (12) in every required case.
Equation (1), now with |A|=tm, gives

    T(A)<=[12(tm)^2-11tm-2(tm)^2+tm]/4
          =5 binom(tm,2),

as asserted.

**Theorem.** If the complete no-carry progression product (6) has a
proper two-color strict source triangle, then T(A)<=5M(A). More
generally the conclusion follows from a two-Golomb partition of its
overlap (7).

In particular the standard positive-difference Cauchy argument gives

    M(A)<=11 span(A)                                (15)

for this class: sum_d r_A(d)=M and sum_d r_A(d)^2=M+2T<=11M.

## 5. Relation to the current research targets

The theorem permits an arbitrary base B, including bases with many
additive relations. It uses source properness to constrain an entire
overlap before applying the exact product energy factorization. Thus it
is different from an unconditional energy calculation on a Golomb base
or a Euclidean two-distance base.

For a binary product the elementary recurrence in
fibers/PRODUCT_COLOR_COMPOSITION_0026.md is T(A)=6T(B)+2M(B).
That recurrence alone suggests growing energy under indefinite lifts.
The present theorem explains the missing restriction: every actual
proper lift forces B itself to have a two-Golomb partition, and the
whole product obeys (12). No indefinitely iterable construction follows
from the recurrence without this inherited weak-source condition.

The hypothetical universal H5 would establish both requested numerical
improvements, as recorded in SOURCE_ENERGY_BOTTLENECK.md. Here H5 and
the resulting source-size estimate are proved only for complete
progression products. A general proper source may have no such product
decomposition. Filling missing marks is not justified: it can destroy
properness, so the theorem cannot be applied to a filled-in superset.
No unconditional small-color Ramsey bound, universal representation,
or original-method completion is asserted.
