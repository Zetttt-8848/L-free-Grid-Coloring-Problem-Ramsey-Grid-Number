# Endpoint-sensitive neighbor inequality

Author: root. Status: candidate pending independent reviews.

Let a_1<...<a_s be integer marks with span at most L. Suppose every
contiguous block of i+1 marks has span at least ell_i, with ell_0=0.
For 1<=c<s put H=cs-c(c+1)/2. Then the sum T_c of the H distances
a_(h+j)-a_h, 1<=j<=c, 1<=h<=s-j, satisfies

 T_c = sum_(i=0)^(c-1) (c-i)(a_(s-i)-a_(i+1))
     <= L*c(c+1)/2 - 2 sum_(i=0)^(c-1) (c-i)ell_i.

To prove the identity, fix j. Cancellation of the two lists in
sum_h(a_(h+j)-a_h) gives sum_(i=0)^(j-1)(a_(s-i)-a_(i+1)).
This formula still holds when the first and last j marks overlap:
their common entries cancel in the expression on the right. Sum over j.
For each i, subtract the spans of the first and last i+1 marks from
a_s-a_1. The result is a_(s-i)-a_(i+1), even when these endpoint blocks
overlap. Each subtracted span is at least ell_i, proving the inequality.

If the positive distance d occurs at most v_d times, let M(H) be the
sum of the H smallest members of the multiset having v_d copies of d.
Then M(H)<=T_c. If H>sum_d v_d, the marks are already impossible.
Thus M(H) greater than the displayed upper bound excludes the marks.
For fixed c the left side is nondecreasing as s increases; the right
side is independent of s, so a contradiction excludes larger s too.

Distinct integer marks give ell_i=i. The resulting correction is
2*binom(c+1,3), since sum_(i=0)^(c-1)(c-i)i=(c^3-c)/6.
An exhaustive certified window profile h(w) gives ell_i>=w whenever
h(w)<=i: a span below w would fit i+1 marks in w integer positions.
Such spacing bounds also satisfy ell_(i+j)>=ell_i+ell_j, because a
block of i+j+1 marks splits into blocks of i+1 and j+1 sharing a mark.
Taking the maximum of these primitive and split bounds is valid.

Checks: c is positive and less than s; every index lies in [1,s].
For s=2,c=1 the identity is the single span and the correction is zero.
For s=3,c=2 and marks 0,1,2, both sides equal4. No color hypothesis is
needed for the identity; the use of a window profile requires its own
valid corner-free color-class premise. Short fibers contribute only
their actual marks. A monochromatic grid cannot satisfy the imported
corner-free window profile. Overlapping endpoint blocks are explicitly
allowed, so the proof has no hidden c<=s/2 assumption. Exact audit
against direct summation on small mark sets is recorded separately.

This is a spacing refinement. It does not prove the proposed 45-cap.
Every numerical result based on a 45/46 profile is conditional unless
that profile is independently established from the full geometry.
