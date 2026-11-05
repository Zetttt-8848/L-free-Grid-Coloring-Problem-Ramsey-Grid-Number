# R3-G1 — refined multiplicity constants

Author: root, GPT-6 Astra ultra, Level3. BaseR3-CP0.
Status: UNVERIFIED candidate with complete derivation; independent reviews pending.
Prediction: G-P2 in PREDICTIONS.md. No external theorem beyond the inherited
completion-closed transfer, generalized Golomb bound, and partition inequality.

## Lemma G1: fixed-scale capacities

Fix an integer k>=5 and put b=k(k-2), N=b^(2^(k-1)),
alpha_q=1-2^(1-q). Set

 c1=1, c2=17/16, c3=3/2, c4=11/5, cq=q-2 (q>=5).

For1<=q<=k-1, every monochromatic same-diagonal set S in a
completion-closed corner-free region inside[N]^2 using at mostq colors
has |S|<=cq N^alpha_q.

Proof. q1 is the inherited singleton fact. Throughout,
N^(1/4)=b^(2^(k-3)) >=(3k)^4 >=16k^2, because k>=5.
Thus for u=N^alpha_q, q>=2, u>=sqrtN>=256k^4.

Forq2, each positive difference of S is used at mostonce by one-color
completion closure. The inherited generalized Golomb estimate gives
|S|<=sqrtN+N^(1/4)+1. Writing z=N^(1/4)>=17,
z^2-16z-16>=1, since its value at17 is1 and it increases thereafter.
Consequently z+1<=z^2/16, and |S|<=(17/16)N^alpha_2.

Forq>=3, apply induction inside T(S), which excludes S's color and
is completion closed. Its distance-d fiber splits into at mostq-1
monochromatic diagonal sets. Hence the positive-difference multiplicity
is at most the positive integer

 V=(q-1) floor(c_(q-1) N^alpha_(q-1)).

Set C=(q-1)c_(q-1). The Golomb estimate is applied to this integerV
before monotonicity replaces it by the larger real number
C N^alpha_(q-1). As (1+alpha_(q-1))/2=alpha_q, it yields

 |S| <=sqrtC u + C^(1/4) sqrtu +1.

We have c_(q-1)<=q-1 and thus C<=k^2. Therefore the two error terms,
divided byu, are at most

 sqrtk/sqrtu +1/u <=1/(16 k^(3/2))+1/(256k^4) <=1/(8k).

Forq3, sqrtC=sqrt(17/8)<=59/40 and1/(8k)<=1/40;
their sum is at most3/2. Forq4, sqrtC=sqrt(9/2)<=87/40,
so the sum is at most11/5. Forq5, sqrtC=sqrt(44/5)<=119/40,
so the sum is at most3. The squared comparison numerators over1600
are respectively3481>=3400,7569>=7200,14161>=14080.

Forq>=6 put r=q-2. Now C=(q-1)(q-3)=r^2-1, and

 sqrt(r^2-1)<=r-1/(2r),

as both sides are nonnegative and the square of the right side is
r^2-1+1/(4r^2). Since1/(8k)<=1/(2r), the error is absorbed and
|S|<=r u. This completes the induction.

Immediate audit. The ambientN is fixed at every level; no sparse region
is replaced by a square. Empty sets and singleton sets are allowed. q1
does not invoke the fractional coefficients. All differences are positive
integers, all roots have nonnegative arguments, and all color-removal steps
strictly decreaseq. Floors precede the integer multiplicity lemma. The
largeN lower bounds explicitly exclude n1 and other small counterexamples
to asymptotic coefficient estimates. Monochromatic complete grids violate
the corner-free premise. At d1 and in a shorter fiber, the same upper-span
estimate applies; it never asserts the existence of extra marks.

## Theorem G2: general bound

For every integerk>=5,

 Rk(L) <=[k(k-2)]^(2^(k-1)).

Suppose a corner-free k-coloring of[N]^2 exists withN above. A main-diagonal
class A has each difference multiplicity at most

 V*=(k-1)c_(k-1) N^alpha_(k-1).

This follows from G1 on its actual completion fibers. The inherited full
diagonal partition identity and k-term Cauchy give, for every nonnegative
unit-weight autocorrelationprofile a_d=t-d (0<=d<t),

 sum_(d=1)^(t-1) (N-d-k^2 V*) a_d <=(k-1)N a0/2.

Write delta=1-k^2 V*/N. Since N^(2^(2-k))=b^2, for k5,
delta=1-25*4*(11/5)/225=1/45. For k>=6,
delta=1-(k-1)(k-3)/(k-2)^2=1/(k-2)^2. Thus always
delta>=1/[5(k-2)^2].

Choose the integer t=10k(k-2)^2. We have t<=N because
N>=b^4 and b^4/t=k^3(k-2)^2/10>1 for k>=5.
Summing the unit-weight profile and dividing by t/2 yields

 delta N(t-1)-(t^2-1)/3 <=(k-1)N.

But its left side minus right side is at least

 [k+1-1/(5(k-2)^2)]N -(t^2-1)/3
 > kN-t^2/3
 >= [k^5-(100/3)k^2](k-2)^4 >0,

since k^3>=125>100/3. This contradiction proves the claimed bound.

Immediate audit. The Cauchy coefficientk^2 is unchanged: one factor for
the k-term inequality and one for summing per-color caps. t<=N, a0=t,
and all positive-lag correlations are nonnegative. The k5 case uses c4,
not the q>=5 expression. No finite computation replaces the universal
induction or the positive-margin estimate. The statement does not include
k1,2,3,4; inherited specializedbounds cover those colorcounts.

## Corollary G3: a uniform polynomial-factor improvement

For all integerk>=3, Rk(L)<=k^(2^k-2).

For k>=5, induction from k5 proves2^(k-1)>=(k-1)(k-2): doubling
the right side dominates k(k-1) at the nextstep because2(k-2)>=k.
Bernoulli's inequality, whose binomial expansion has nonnegative terms,
gives

 (k/(k-2))^(2^(k-2)) >=1+2^(k-1)/(k-2) >=k.

Squaring proves that the ratio k^(2^k)/N is at leastk^2.
For k3 use465<=729=3^6; for k4 use22006246<=268435456=4^14.

Immediate audit. Bernoulli has an integer exponent and positive increment;
the induction starts at16>=12. The inherited small-color comparisons are
separate proof leaves, not asserted by G1's k>=5 range. k1 is excluded;
k2 could be handled separately but is outside the stated corollary.

## Route4 interpretation and remaining gap

The profile recurrence before taking maxima is
r_S(d)<=sum_(colors c) capacity_c(T(S) intersect diagonal_d).
Taking uniform bounds recovers V_q<=(q-1)C_(q-1), then the neighbor estimate
scales the leading capacity as sqrt(V_q N). Refining the coefficientcq
uses slack in that recurrence but retains alpha_q=1-2^(1-q).
This is an unconditional explicit-bound improvement, not a reduced tower
height and not a proof that all distance-dependent methods are incapable
of improving the exponents. Such an impossibility statement would require
simultaneously realizable nested extremizers, which are not constructed here.

Dependency graph: inherited closure -> G1 induction; inherited Golomb
estimate + exact scalar inequalities -> G1; G1 + inherited partition
identity -> G2; G2 + binomial inequality + smallk inputs -> G3.
No computationally negative run is a proof leaf. Confidence: candidate
derivation high, publication/research status UNVERIFIED until independent
review and exact coefficient checks complete.
