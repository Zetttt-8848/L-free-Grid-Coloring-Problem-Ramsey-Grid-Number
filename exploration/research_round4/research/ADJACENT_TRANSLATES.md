# Consecutive differences and nested sums in a translated ruler

Root research derivation, R4-RESEARCH-0003. This gives structural necessary conditions for a particular family of two-color weak triangles. It does not establish a universal fiber cap or a Ramsey upper bound.

Let A be a Golomb set of integers with no two consecutive marks. Put B=A, C=A+1, so B and C are disjoint. Suppose W(B union C) has a corner-free two-coloring whose diagonal is blue on B and green on C. For a<b in A write U(b,a) for the color of the mixed cell (b+1,a). All cells (b,a) with a<b in A are green, and all (b+1,a+1) are blue, because the corresponding diagonal endpoints have the same color.

## An orientation law for consecutive differences

Suppose [a,b] and [c,e] are intervals with endpoints in A and lengths h and h+1, respectively, where h>0.

Their starts cannot coincide: a=c would give e=b+1, contrary to the absence of consecutive marks. There are two possibilities:

* If a<c, then U(b,a) is blue and U(e,a) is green.
* If a>c, then U(b,a) is green and U(b,c) is blue.

Proof of the first case. The cells (b+1,a), (e,a), (e,c) form a positive corner, since e-(b+1)=c-a>0. Its last two cells are green. Thus (b+1,a) is blue. The cells (b+1,a), (e+1,a), (e+1,c+1) then form a corner of step c+1-a>0. The first and last are blue, so (e+1,a) is green.

Proof of the second case. Here a>=c+2. The cells (e+1,c+1), (b+1,c+1), (b+1,a) form a positive corner of step a-c-1. Its first two cells are blue, so (b+1,a) is green. The cells (e,c), (b+1,c), (b+1,a) form a corner of step a-c>0. Its endpoints are green, so (b+1,c) is blue. Every stated coordinate belongs to B union C, and each row exceeds its column. This proves the law.

Thus each pair of consecutive positive differences forces two specified mixed cells to opposite colors. The Golomb hypothesis makes the interval realizing each difference unique; the geometric proof itself only needs the stated intervals and the absence of consecutive marks.

## Two-sided near-sum obstruction

For every a<b in A, put I=A intersect (a,b). Then the two memberships

    a+b-1 in I+I,       a+b+1 in I+I

cannot both hold. Repeated summands in I+I are permitted.

Proof. If p,q in I satisfy p+q=a+b-1, then [a,p] and [q,b] have consecutive lengths, with the shorter interval starting first. The first case of the orientation law makes U(b,a) green.

If r,s in I satisfy r+s=a+b+1, then [r,b] and [a,s] have consecutive lengths, with the shorter interval starting later. The second case makes U(b,a) blue. These conclusions contradict each other. The intervals in both applications have positive lengths because their internal marks lie strictly between a and b.

For example, A containing {129,140,142,152} is excluded: the outer sum is 281, while 140+140=280 and 140+142=282. This explains the failure of both one-step translates obtained by removing either endpoint of the unique adjacent pair from the literal order-24 ruler used in the earlier research. No enumeration of all rulers is involved in this conclusion.

## A structural consequence for every run of pair sums

Let Sigma(A)={a+b:a,b in A,a<=b}. Each sum has a unique representing unordered pair. Indeed, two different pairs of the same sum would give two different positive-difference representations: if a<c and a+b=c+d with a<=b,c<=d, then c-a=b-d>0, with a<c<=d<b. This contradicts the Golomb property.

For s in Sigma(A), let ell(s)=b-a for its unique pair a<=b. Consider any run of consecutive integers contained in Sigma(A). The sequence ell(s) along this run first strictly decreases and then strictly increases; either part may be empty.

To prove this, first observe that adjacent sums cannot have a common endpoint: their other endpoints would differ by one. Their interval lengths also cannot be equal, because an interval's sum and length have the same parity.

If ell(s) exceeded both ell(s-1) and ell(s+1), both neighboring pairs would lie strictly inside the interval representing s. This follows from the endpoint formulas (s-ell)/2 and (s+ell)/2. A neighboring endpoint could coincide only if the two pairs shared that endpoint, which has just been excluded. The two interior pair sums would be s-1 and s+1, contradicting the near-sum obstruction. Thus there is no strict local maximum. In a finite sequence with unequal adjacent entries, any increase followed later by a decrease has an increase-to-decrease transition, which is a strict local maximum. Therefore all decreases precede all increases, proving the assertion.

This constrains a whole run of the pair-sum sequence, beyond a single forbidden source pattern. It supplies no sufficient numerical bound on the number of marks: controlling the number and total lengths of these runs is a remaining mathematical problem.

## Discovery scope

The bounded adjacent-translation experiment considered the two previously supplied literal rulers. Each has a unique pair of consecutive marks. Removing either endpoint and translating the remaining ruler by one gives four disjoint pairs: two with 44 total marks and span 373, and two with 46 total marks and span 426. All four produced forced-color conflicts before any SAT search was needed. These are four specified examples, not a negative decision for arbitrary translated rulers. The general assertions above follow from the displayed corner arguments.
