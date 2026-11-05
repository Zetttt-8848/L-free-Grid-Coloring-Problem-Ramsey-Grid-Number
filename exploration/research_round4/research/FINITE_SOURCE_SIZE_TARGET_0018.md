# A weaker sufficient source target: S21

Root quantitative derivation, checkpoint R4-RESEARCH-0018.

The new finite source hypothesis below is open. This note proves its
conditional consequences and explains why it is sufficient for both
requested small-color improvements. It does not claim either improvement
unconditionally.

## 1. The revised sufficient statement

For a finite integer source A, let

    V(A)={(v,u):u,v in A, u<v},
    M(A)=binom(|A|,2),
    L(A)=max A-min A.

The directed L has its original orientation and equal positive step.
Consider the finite-range statement

    S21: if V(A) admits a proper two-coloring and L(A)<=99994,
         then M(A)<=21 L(A).                         (1)

The empty and singleton cases have M=0. For all other cases (1) gives

    |A|<=1+sqrt(42 L(A)).                            (2)

Indeed (|A|-1)^2<=|A|(|A|-1)<=42L(A).

The earlier S11 target used a smaller coefficient and a slightly shorter
span range. S21 is a different sufficient finite target: it allows almost
twice as many source pairs per unit span, while extending the required
range to 99994. A universal H(10), namely T(A)<=10M(A) for proper sources,
would imply S21 by the existing positive-difference energy argument.
Neither H(10) nor S21 is proved here.

## 2. Conditional three-color consequence

Assume S21. In a hypothetical proper three-color square of side 379, a
main-diagonal color appears at least ceil(379/3)=127 times. Let A be any
127 of those diagonal positions. If u<v lie in A, the cells

    (u,u), (v,u), (v,v)

form an original directed L. Thus (v,u) avoids their common diagonal color,
and the strict source triangle V(A) has a proper two-coloring.
Its span is at most 378. S21 would imply

    binom(127,2)=8001 <=21*378=7938,

a contradiction. Therefore

    S21 implies R3(L)<=379<465.                      (3)

## 3. An explicit finite shift-count inequality

Let D be a source of exactly a marks and span at most L. Suppose

    r_D(h)<=W       for every positive h,            (4)

where W is a nonnegative real number. For an integer t>=1 define

    g(x)=sum_(i=0)^(t-1) 1_D(x-i).

The support of g has at most L+t integer positions and sum_x g(x)=at.
Cauchy--Schwarz and expansion of the square give

    a^2 t^2/(L+t)
       <=sum_x g(x)^2
       =at+2 sum_(h=1)^(t-1)(t-h)r_D(h)
       <=at+W t(t-1).

Canceling t>0 yields the necessary integer-window inequality

    a^2 t <=(L+t)[a+W(t-1)].                        (5)

This is the existing shifted-interval/Golomb counting mechanism in an
explicit finite form. It is used to strengthen the transfer from a new
source theorem; no originality claim is made for (5).

## 4. Conditional four-color consequence

Assume S21 and suppose that a square of side

    N=99996

has a proper four-coloring. Choose exactly

    a=N/4=24999

positions of one main-diagonal color and call their source D. The same
completion argument gives a proper three-coloring of V(D). Put

    L=N-1=99995.

For h>0, partition F_h=D intersect (D-h) by the actual colors of the cells
(x+h,x). These cells avoid the original diagonal color, so there are at
most three parts. For one such part E, two starts u<v in E force the cell
(v+h,u) to avoid their common color. The cells

    {(v+h,u):u,v in E, u<v}

are a translated proper two-color copy of V(E). Translation of the first
coordinate preserves the positive orientation and the equality of the
corner's two legs. Furthermore

    span(E)<=L-h<=99994.

S21 therefore applies to every part. Summing (2) over the three parts,
with the same bound also permitted for empty parts, gives

    r_D(h)<=3[1+sqrt(42(L-h))]
           <=3[1+sqrt(42L)] <6153,                  (6)

because

    42L=4199790 <2050^2=4202500,
    3(1+2050)=6153.

In particular the uniform cap (4) holds with W=6153. Apply (5) with

    t=550.

Its two sides would have to satisfy

    24999^2*550
      <=(99995+550)[24999+6153*549].                 (7)

The left side is 343722500550. The right side is

    100545*3402996=342154232820.

Their difference is 1568267730>0, contradicting (7). Thus

    S21 implies R4(L)<=99996<100000.                 (8)

All source sets to which S21 is applied have span at most 99994, exactly
the range stated in (1). No source triangle has been substituted for a
full-grid coloring in the reverse direction.

## 5. Research consequence and scope

Equations (3) and (8) establish a complete conditional route from S21 to
both small-color thresholds. The numerical target can therefore be pursued
through M(A)<=21 span(A), or the sufficient energy hypothesis H(10), rather
than requiring H(5) solely because of the older, less efficient transfer.
The earlier S11/H5 implications remain valid; they are stronger sufficient
routes, not the only viable ones.

The discovery task is still the source theorem itself. The interval-counting
transfer is inherited machinery and does not meet the original-method
objective. No numerical Ramsey bound changes until the new source estimate
has a complete derivation.
