# R3-G4: one further coefficient refinement

Author: root, GPT-6 Astra ultra, Level3. UNVERIFIED pending independent
reviews. This is a separate derivation after the candidate in
refined_constants_proof.md; no older proof is silently replaced.

For every integer k>=6, put b=k(k-2)-1 and N=b^(2^(k-1)). The claim is

 R_k(L)<=N.

Use the inherited completion-closed capacity induction at this fixed N,
with alpha_q=1-2^(1-q) and coefficients

 c1=1, c2=101/100, c3=57/40, c4=207/100,
 c5=72/25, c6=19/5, cq=q-2-1/(q-2) for q>=7.

Lemma G4a. Every monochromatic same-diagonal set in a completion-closed
corner-free region inside [N]^2 using at most q colors, 1<=q<=k-1,
has size at most cq*N^alpha_q.

Proof. The q1 singleton base is inherited. Since k>=6, b>=3k and
N^(1/4)=b^(2^(k-3))>=(3k)^8>=16k^4. Put u=N^alpha_q for q>=2.
Then sqrt(u)>=N^(1/4)>=16k^4. For q2, Golomb gives
|S|<=sqrt(N)+N^(1/4)+1. For z=N^(1/4)>=101, z^2-100z-100>=1
(equality at101, then increasing), so the bound is at most(101/100)sqrt(N).

For q>=3 apply induction in the actual triangle T(S), excluding the
color of S. Every positive distance has integer multiplicity at most
V=(q-1)floor(c_(q-1)N^alpha_(q-1)). Set C=(q-1)c_(q-1)<=k^2.
The generalized Golomb bound, applied first with this integer V, yields

 |S|/u <= sqrt(C)+C^(1/4)/sqrt(u)+1/u.

The last two terms are at most

 sqrt(k)/(16k^4)+1/(256k^8) <=1/(8k^3)<=1/1000.

Indeed sqrt(k)<=k gives the first term <=1/(16k^3), and
1/(256k^8)<=1/(16k^3); also8k^3>=1728>1000.
For q=3,...,7 direct exact rational squaring gives

 (cq-1/1000)^2 >= (q-1)c_(q-1),

where both square roots have nonnegative arguments and cq-1/1000>0.
The exact differences are supplied in minus_one_exact.json and can be
recomputed by fraction arithmetic from the displayed coefficients.
For q>=8, put r=q-2. Then

 C=(r+1)(r-1-1/(r-1))=r^2-2-2/(r-1),
 cq=r-1/r,
 cq^2-C=1/r^2+2/(r-1)>2/r.

For e=1/(8k^3), we have cq-e>0 and
(cq-e)^2-C>2/r-r/(4k^3)>=2/k-1/(4k^2)>0.
Therefore sqrt(C)+e<cq. This proves the induction.

Immediate checks. The two special ranges q2 and q3..7 precede the
asymptotic range q>=8; for small k only the required q<=k-1 are used.
All capacities refer to the fixed ambient square, never a smaller square
inferred from the cardinality of a triangle. The span upper bound N
only enlarges the actual span. The induction has decreasing color count;
floors precede the integer multiplicity theorem. Empty sets and singleton
fibers satisfy all bounds. Monochromatic grids violate corner-freeness,
not the algebra; k1..5 are expressly outside the theorem. The formulas
remain valid at d1 and on short subdiagonals.

Theorem G4b. A main-diagonal class in a corner-free k-coloring has
r_A(d)<=V*=(k-1)c_(k-1)N^alpha_(k-1). Set delta=1-k^2V*/N.
Since N^(2^(2-k))=b^2, we have delta>=1/b^2. To verify this:

 k6: b^2-k^2(k-1)c_(k-1)=529-2592/5=53/5>1;
 k7: the same expression=1156-5586/5=194/5>1;
 k>=8: it equals2k^2/(k-3)+4k+1>1.

Apply the inherited k-color partition inequality with unit weights of
integer length t=2kb^2. We have t<=N: N>=b^5 and b^3>=2k.
The inequality would require

 delta*N*(t-1)-(t^2-1)/3 <=(k-1)N.

But delta*(t-1)-(k-1)>=k+1-1/b^2>k. Thus the left side minus the
right side is greater than

 kN-t^2/3 >=k*b^4*(b-4k/3)>0,

using N>=b^5 and b>=3k. This is the contradiction.

Immediate checks. t is positive, integral, and no larger than N. Every
autocorrelation is nonnegative and the k^2 factor is the unchanged product
of the Cauchy factor and the number of diagonal classes. The k6 and k7
capacity coefficients are treated individually; k>=8 uses the stated
tail formula. No asymptotic limit, floating computation, or finite scan
is used for the universal claim. Boundary cases k1,2 use inherited exact
values and do not enter this proof. The new expression is strictly below
the previous candidate for k>=6 because both bases are positive and the
new base is one smaller.

Dependence: inherited closure + generalized Golomb estimate -> G4a;
G4a + inherited full-diagonal partition inequality -> G4b. This improves
an explicit constant and preserves the double exponential. No claim of
exhausting all coefficient choices or of proving the square-root loss
unavoidable in all profile methods is made.
