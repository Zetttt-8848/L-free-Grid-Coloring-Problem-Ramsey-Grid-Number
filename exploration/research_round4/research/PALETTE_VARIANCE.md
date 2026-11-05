# A simultaneous palette-variance identity on the full grid

Base R4-RESEARCH-0001. Root auxiliary derivation. This is a necessary inequality with a complete proof; its quantitative use for a stronger Ramsey bound remains unresolved.

Let chi:[N]^2->[k] be corner-free, with k>=2. For q=(x,y), and each color i, put

P_i(q)=#{h:1<=h<=min(x-1,N-y), chi(x-h,y)=chi(x,y+h)=i},
P(q)=sum_i P_i(q).

These are the numbers of diagonal endpoint pairs of each color completing at q. In particular,

P_(chi(q))(q)=0.                                          (1)

All h are positive and all three cells remain in the square, so (1) follows directly from the excluded directed L.

## Forced variance

For every q,

sum_i (P_i(q)-P(q)/k)^2 >= P(q)^2/[k(k-1)].              (2)

Proof. At least one P_i(q) is zero by (1). Cauchy's inequality on the other k-1 nonnegative entries gives sum_i P_i(q)^2>=P(q)^2/(k-1). Expanding the left side of (2) gives sum_i P_i(q)^2-P(q)^2/k, which proves the claim. The case P(q)=0 gives equality. This is a quantitative deficit forced by the absent palette color; it does not posit that unconditioned color counts are unequal.

For nonnegative weights w_q with W=sum_q w_q>0, summing (2) and applying weighted Cauchy gives

sum_q w_q sum_i (P_i(q)-P(q)/k)^2
    >= (sum_q w_q P(q))^2/[k(k-1)W].                    (3)

Indeed (sum w_q P(q))^2 <= W sum w_q P(q)^2; this follows by Cauchy applied to sqrt(w_q) and sqrt(w_q)P(q).

## A color-independent lower bound for total completions

Write l_sigma=N-|sigma| for the lengths of the slope-one diagonals, -(N-1)<=sigma<=N-1. If n_(sigma,i) counts color i on that diagonal, then

sum_q P(q)=sum_sigma sum_i binom(n_(sigma,i),2).          (4)

Each same-color pair on a diagonal has one positive completion, and conversely every pair counted by P is such a pair, proving (4) without overcounting. Cauchy on each diagonal gives

sum_i binom(n_(sigma,i),2)
    >= (l_sigma^2/k-l_sigma)/2.

Since sum_sigma l_sigma=N^2 and

sum_sigma l_sigma^2=N^2+2 sum_(j=1)^(N-1)j^2
                    =N(2N^2+1)/3,

we obtain sum_q P(q)>=B, where

B=max(0, N(2N^2+1)/(6k)-N^2/2).

Taking unit weights in (3), with W=N^2, proves

sum_q sum_i (P_i(q)-P(q)/k)^2 >= B^2/[k(k-1)N^2].       (5)

The maximum with zero matters when the elementary lower bound from Cauchy is negative; it permits squaring without reversing the intended implication.

## The remaining implication

An upper bound for the left side of (5), derived jointly from the row, column and completion-fiber constraints, could force a contradiction. No such sufficiently strong upper bound is established here. The variance is made from fourth-order color correlations, because each P_i already counts pairs. Arbitrary balanced first-order color proportions do not determine it. Conversely, (5) alone is consistent with substantial palette variation and supplies no new numerical R3 or R4 bound.

For a two-color completion triangle, the analogous absent-color statement forces all monochromatic endpoint pairs at a cell to have the opposite sign; the signed identity in SIGNED_COMPLETION.md is its exact two-color version. The mixed-color ordered inequalities in fibers/DERIVATIONS.md retain additional restrictions on how these forced palettes can overlap at different cells.
