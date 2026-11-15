# Binary cross-lag forcing and a sharp collision obstruction

Status: written proofs with literal finite cross-checks; external peer review
pending. No new numerical Ramsey bound. No claim of worldwide novelty.

## 1. Definitions and forcing

Let A be a finite set of integers and let z:V(A)->{0,1} be proper, where
V(A)={(v,u):u<v, u,v in A}. Define

\[
C_h^e=\{u:u,u+h\in A,\ z(u+h,u)=e\},\qquad h>0.
\]

For t>0 define

\[
m_t^e(u)=\#\{h:0<h<t,\ u,u+t-h\in C_h^e\}.
\]

If h is counted, the source contains the L
(u+h,u), (u+t,u), (u+t,u+t-h). Its two arms have color e.
Consequently z(u+t,u)=1-e, or u in C_t^{1-e}. This proves the
cross-lag forcing relation with no hypotheses beyond properness and membership.

Put R_t^e=sum_u m_t^e(u), E_t^e=sum_u m_t^e(u)^2, and let U_t^e
be the number of starts with positive multiplicity. Then
(R_t^e)^2 <= U_t^e E_t^e by Cauchy, and U_t^e <= |C_t^{1-e}|.
Neither inequality by itself bounds collision amplification.

## 2. A universal bound, and why a constant replacement is impossible

Every counted h determines a distinct element u+h in
A intersect (u,u+t) intersect (2u+t-A). Therefore

\[
m_t^e(u)\le |A\cap(u,u+t)\cap(2u+t-A)|\le |A|-2.
\]

The last inequality is applied only when m is positive, so both endpoints
are present. Multiplying by m and summing gives
E_t^e <= (|A|-2)R_t^e for |A|>=2. The construction below makes this exact.

Let B={b_0,...,b_r} be a Golomb set with 0=b_0<...<b_r=M, r>=1.
Set T=5M and A=B union (T-B). Color every source cell by

\[
z(v,u)=\begin{cases}1&v+u=T,\\0&v+u\ne T.\end{cases}
\]

**Properness.** Sums of two low marks are in [0,2M], mixed sums in
[4M,6M], and sums of two high marks in [8M,10M]. These intervals are disjoint.
The Golomb property implies unique unordered two-term sums within B,
including repeated terms: two different equal sums would give a repeated
positive difference. It also implies uniqueness of each nonzero difference
b_i-b_j. Thus two distinct unordered pairs of A can have the same sum
only at T, where a mixed pair consists of b_i and T-b_i.

For a source L (x,y),(x+d,y),(x+d,y+d), the unordered mark pairs
{y,x+d} and {y+d,x} are distinct and have the same sum. They cannot be
identical because d>0 and y<x. Hence x+d+y=T. The three cell sums are
T-d,T,T+d, so their colors are (0,1,0). Every L is proper.

**Pointwise sharpness.** At target (T,0), each h in A other than 0,T
gives 0,T-h in C_h^0. These are all possible h, so m_T^0(0)=2r=|A|-2.
There is no other start at lag T. Hence E_T^0=(|A|-2)R_T^0.

**Global collision formula.** Every request forces a color-1 cell, so all
requests land at (T-b_i,b_i), of lag T-2b_i. At that cell, exactly the
2(r-i) marks strictly between its endpoints can supply an h. Both arms
have sums different from T, so every one does supply a request of color 0.
There are no other requests. Consequently

\[
R:=\sum_{t,e,u}m_t^e(u)=r(r+1),\qquad
E:=\sum_{t,e,u}m_t^e(u)^2=\frac{2r(r+1)(2r+1)}3.
\]

Thus E/R=(4r+2)/3 is unbounded. Candidate C1, even in its global version
E<=C R with an absolute C, is false. Arbitrary nonnegative target weighting
does not rescue it: weights may be concentrated on the sharp target.

## 3. Explicit polynomial-span examples

Take b_i=(r^2+1)i+i^2 for 0<=i<=r. For j>i,

\[
b_j-b_i=(r^2+1)(j-i)+(j^2-i^2),\quad 1\le j^2-i^2\le r^2.
\]

Division by r^2+1 determines j-i and the remainder. The remainder divided
by j-i gives j+i, so the ordered pair is determined. B is Golomb.
The source has 2r+2 marks and span 5(r^3+r^2+r).

At r=40 it has 82 marks, span 328200, maximum collision multiplicity 80,
and global E/R=54. Thus substantial collisions can occur within a lag range
comparable to the current window support, not only at exponential distances.
This example is nevertheless far from the large-capacity regime of the R4
consumer. It does not refute a claim with a justified near-extremality premise.

`check_collision_family.py` checks the power-of-five family for r=1,...,12
and the polynomial family at r=1,2,4,8,16,32,40. It checks every physical L,
every Golomb fiber class, all forcing targets, and the exact energy formulas.
The proof above, not those 19 finite checks, supplies the universal statements.

## 4. A valid interface to a weighted consumer

For nonnegative, finitely supported weights w_t define
R_w=sum_{t,e,u}w_t m_t^e(u), E_w=sum_{t,e,u}w_t m_t^e(u)^2, and
U_w=sum_{t,e}w_t U_t^e. Weighted Cauchy gives R_w^2 <= U_w E_w.
If A lies in an interval of span L and Q(p) caps Golomb sets in p positions,
then U_w <= 2 sum_{1<=t<=L} w_t Q(L-t+1).

There is also the exact identity
sum_{t,e} R_t^e = sum_{h,e} binom(|C_h^e|,2), since each unordered
same-class pair contributes once to target t=h+(v-u).
For weighted targets the pair receives w_{h+v-u}; it is incorrect to replace
that weight by w_h without further justification.

These identities are a consumer interface, not an improvement. A useful new
argument needs both weighted demand and a collision bound that is stronger
in the relevant regime. The construction shows why dropping the regime
conditions cannot work.

## 5. Pivot for the integration discussion

Do not expand the unrestricted constant-energy search. Consider instead a
deficit/collision dichotomy for the fixed consumer weights: either the actual
weighted fiber count already has the A0-required deficit, or its near-saturation
forces a quantitative collision bound. Such a claim must specify the cap,
the weight, the span range, the deficit, and the constants before testing.
Its parameters must be chosen for a mathematical reason, not fitted to a
desired bound. This is a proposed next task, not an established inequality.

For Claude: the reflected family is also a proper coloring using at most
three colors, so it is a required adversarial test for unrestricted source
claims. It is not shown to extend to a proper four-colored full square and
cannot refute statements requiring that stronger origin or near-saturated
completion classes. Preserve that distinction.
