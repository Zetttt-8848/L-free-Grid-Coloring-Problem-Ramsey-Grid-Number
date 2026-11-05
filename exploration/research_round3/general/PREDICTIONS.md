# G-P1 uniform polynomial-factor improvement

First target N=k^(2^k-2), k>=5, with inherited specialized bounds covering
k3,4. Predict the same capacity induction is still valid at this ambientN,
and its uniform cap leaves a positive final-window coefficient for k>=5.
No tower-height reduction is predicted. Initial exact diagnostic at each
k=5,...,12 compares N against [k^2(k-1)^2]^(2^(k-2)), with no radicals or
floating arithmetic. A finitepositive result will only motivate a uniformproof.

G-P2 stronger candidate derived before exact testing/review: for k>=5,
N=[k(k-2)]^(2^(k-1)) should suffice. Use refined capacities c2=17/16,
c3=3/2,c4=11/5,cq=q-2 for q>=5 instead of the inherited coefficientq.
The normalized fourth-root error is at most1/(8k) at this fixedN. Predict
all coefficient comparisons pass exactly and the final window
t=10k(k-2)^2 has a positive universal margin. This retains the square-root
exponent recursion; it is not a tower-height improvement. Ifproved, it
implies Rk<=k^(2^k-2) for allk>=3 using inheritedsmallk cases.

G-P3 slack iteration after G-P2, frozen before arithmetic execution:
for k>=6, b=k(k-2)-1 and N=b^(2^(k-1)) should suffice. Refine the
capacities to c2=101/100,c3=57/40,c4=207/100,c5=72/25,c6=19/5,
cq=q-2-1/(q-2) for q>=7. The normalized error should be at most
1/(8k^3)<=1/1000. Predict all five rational comparisons q3..7 pass,
delta>=1/b^2, and window t=2kb^2 has a universally positive margin.
This is a further constant improvement; the fixed-scale exponent recursion
is unchanged. Retain G-P2 for k5 and its polynomial-factor corollary.

G-P4 method replacement diagnostic: the self-contained integer ruler
b_i=2pi+(i^2 mod p), 0<=i<p, for an odd prime p, should have all positive
differences distinct and fit in [0,2p^2). Its weak triangle, with diagonal
one color and strict triangle a second color, should be corner-free.
Verify exactly at p=3,5,7,11,13,17,19,23,29,31. This shows a first-level
square-root-sized obstruction even when the entire multiplicity profile
is known, not simultaneous saturation of k>=5 nesting.
