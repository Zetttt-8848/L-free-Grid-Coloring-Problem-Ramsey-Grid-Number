# Independent review of the six-class counting proof

Date: 2026-11-08. Primary verdict: **proved as written**, for the corrected
proof revisions pinned by SHA-256 in
[`independent_counting_results.json`](independent_counting_results.json).
Project classification: **PROVED, using two established external computational
theorems**. The independently reconstructed argument proves

\[
  R_3(\mathcal L)\le464,\qquad
  \mathcal L(x,y;d)=\{(x,y),(x+d,y),(x+d,y+d)\},\quad d\in\mathbb Z_{>0}.
\]

Thus every map from \(\{0,\ldots,463\}^2\) to three colors contains the
specified monochromatic positive equal-leg L. Colors need not all occur.
No counterexample or unresolved internal implication was found. The proof
does not determine \(R_3\), exclude side 463, or establish literature priority.

The new counting and convolution argument is elementary mathematics. Its
external numerical inputs, \(G(24)\ge425\) and \(G(25)\ge480\), are established
by exhaustive Golomb-ruler computations, accepted as external theorems here.
The reviewer authenticated their source statements and conventions, but did
not reproduce those computations. No SAT solver was used in this review or
needed for this implication.

## 1. Contract, dependencies, and independence

The audited proof sources are
[`geometry/SIX_CLASS_LEMMA.md`](../geometry/SIX_CLASS_LEMMA.md) and
[`kernel_upper/README.md`](../kernel_upper/README.md). Sections 1–4 of
[`combinatorial_upper/THEOREM.md`](../combinatorial_upper/THEOREM.md) were
also checked as an optional strengthening. That document's separate
length-six word enumeration, Section 5, is outside this review.

The dependency chain is:

1. A hypothetical proper square yields six **actual, disjoint** completion
   classes at each fixed positive shift.
2. Each class is Golomb, by two explicit physical-coordinate color exclusions.
3. The external span bounds and distinct minima imply a joint capacity.
4. Pointwise three-term Cauchy and nonnegative correlations turn those
   capacities into a necessary scalar inequality.
5. An explicitly specified integer weight violates that inequality.

Steps 1–4 have universal written proofs below. Step 5 is a finite exact
calculation, independently reconstructed from the weight definition.
There is no dependency on a floating optimizer, a coloring search, a balanced
diagonal, G9, S21, or a rainbow assumption.

This is a separate reviewer audit. The reviewer read the statements and proofs
but did not read, import, execute, or adapt the authors' verification code.
The new standard-library checker computes correlations by a distance
histogram of weight-position pairs and computes the full convolution literally.
It obtains the numerical values before comparing them with the claimed values.
An additional exact polynomial calculation verifies the autocorrelation formula.
Separate authorship does not itself guarantee correctness; the derivations and
reproducible checks are the evidence.

## 2. Geometric implication, directly in the square

Suppose \(\chi\) is a proper three-coloring of \(\{0,\ldots,n-1\}^2\).
Fix \(d\in\{1,\ldots,n-1\}\), set \(p=n-d\), and define

\[
B_{c,b}=\{u:0\le u<p,\ \chi(u,u)=\chi(u+d,u+d)=c,
                         \ \chi(u+d,u)=b\}.
\]

For each matching diagonal pair, its completion cannot have color \(c\):
the three cells \((u,u),(u+d,u),(u+d,u+d)\) already form the forbidden L.
There are exactly six possible ordered labels \((c,b)\) with \(c\ne b\).
A position \(u\) fixes both actual colors, so it belongs to at most one class.
Every matching diagonal pair belongs to one such class. Consequently

\[
R_d:=\#\{u:\chi(u,u)=\chi(u+d,u+d)\}
     =\sum_{c\ne b}|B_{c,b}|.
\]

Here is a fresh proof that each \(B_{c,b}\) is Golomb, without relying on
an abstract source being extendable to a square. For \(u<v\) in this class,
consider the physical cell \(P=(v+d,u)\). It cannot have color \(c\), because

\[
(u,u),\ (v+d,u),\ (v+d,v+d)
\]

is an L of positive step \(v+d-u\), whose first and last cells have color
\(c\). It cannot have color \(b\), because

\[
(u+d,u),\ (v+d,u),\ (v+d,v)
\]

is an L of positive step \(v-u\), whose first and last cells have color
\(b\). Hence \(P\) has the unique third color. All displayed coordinates
lie in the original square: \(0\le u<v<p\) and \(v+d\le n-1\).

Now suppose two distinct ordered increasing pairs in \(B_{c,b}\) have
the same positive difference. After ordering their starts they are
\((a,a+h)\) and \((a+t,a+t+h)\), with \(h,t>0\). The preceding exclusion
forces each of

\[
(a+h+d,a),\quad(a+t+h+d,a),\quad(a+t+h+d,a+t)
\]

to the third color. These are three distinct cells forming an L of step
\(t\), a contradiction. The proof allows \(h=t\), so the overlapping
three-mark repeated-difference case is included. It also allows \(h<t\)
and \(h>t\); no assumption about disjoint pair intervals was introduced.
This proves the Golomb property in precisely the required orientation.

## 3. Joint packing and its boundary cases

Let \(g(p)\) be the greatest size of an integer Golomb subset of \(p\)
consecutive positions, with \(g(p)=0\) for \(p\le0\). If \(q\) Golomb
sets are pairwise disjoint inside \(\{0,\ldots,p-1\}\), order the nonempty
sets by minima \(b_0<\cdots<b_{s-1}\). Then \(b_j\ge j\). Translation
places the corresponding set in \(p-b_j\) consecutive positions, and
monotonicity gives

\[
\sum_{i=1}^q |B_i|\le\sum_{j=0}^{s-1}g(p-b_j)
                    \le\sum_{j=0}^{q-1}g(p-j).
\]

Empty sets cause no problem; the appended terms are nonnegative. When
\(q>p\), there are at most \(p\) nonempty sets and all terms with
\(j\ge p\) are zero. For \(p=0\), every class is empty. Disjointness of
positions, rather than merely distinct class labels, is indispensable and
was established in Section 2.

The numerical specialization uses span, not occupied-position count.
For \(1\le p\le480\), no class has 25 marks: any 25-mark subset would
have span at most \(p-1\le479\), contradicting \(G(25)\ge480\).
Every 24-mark class with minimum \(u\) must satisfy

\[
425\le\max B-u\le p-1-u,
\qquad\text{hence}\qquad u\le p-426.
\]

There are exactly \(\max(0,p-425)\) eligible minima. Distinct classes
have distinct minima, and there are only six classes. If \(t\) have
24 marks, then

\[
t\le\min(6,\max(0,p-425)),\qquad
R_d\le6\cdot23+t.
\]

The trivial union bound \(R_d\le p\) therefore gives

\[
 U(p)=\min\{p,138+\min(6,\max(0,p-425))\}.
\]

In particular, \(U(425)=138\), \(U(426)=139\),
\(U(430)=143\), and \(U(431)=U(480)=144\). The case \(p=480\)
is included because its span is at most 479. The case \(p=481\)
cannot be included using these two inputs: a 25-mark ruler of span 480
fits in 481 positions. The target calculation only uses
\(380\le p\le463\), where the outer \(\min(p,\cdot)\) is redundant.

## 4. Cauchy, signs, and support

Let \(f_c(u)=1_{\chi(u,u)=c}\) on \(0\le u<n\), and zero elsewhere.
Let \(w\) be nonnegative and supported on at most \(n\) consecutive
integer positions. Define \(a_d=\sum_iw_iw_{i+d}\). Then \(a_d\ge0\)
and \(a_d=0\) for \(d\ge n\). Since \(\sum_cf_c=1_{[0,n-1]}\),
pointwise Cauchy gives

\[
 T:=\|1_{[0,n-1]}*w\|_2^2
 \le3\sum_c\|f_c*w\|_2^2=:3E.
\]

Expanding the finite sums by ordered pairs of diagonal positions gives

\[
 E=na_0+2\sum_{d=1}^{n-1}R_da_d,\qquad
 T=na_0+2\sum_{d=1}^{n-1}(n-d)a_d.
\]

If \(R_d\le U_d\) for all shifts with \(a_d\ne0\), nonnegativity yields
\(E\le na_0+2\sum U_da_d\). Combining these inequalities, then dividing
by two, gives exactly

\[
 \sum_{d=1}^{n-1}(n-d-3U_d)a_d\le na_0. \tag{1}
\]

No sign assumption on \(n-d-3U_d\) is needed. The sign needed for replacing
\(R_d\) by an upper bound is \(a_d\ge0\), which holds. No balance
condition on the three diagonal color classes is used.

During review, the coordinator made two expository corrections: the generic
weight paragraph now states the support restriction, and a sentence counting
eligible minima now includes \(\max(0,p-425)\). For unrestricted finite
weights, the full-indicator expansion instead requires \((n-d)_+\), or
explicit truncation at \(d=n-1\). The actual 85-position weight and the
actual capacity formula already satisfied both requirements. These corrections
do not change the 464 proof, its inputs, or any numerical value. The corrected
files were re-read and hashed before the final run.

## 5. Exact certificate and independent arithmetic

Take \(N=86\) and \(w_i=i(N-i)\) for \(1\le i<N\), zero otherwise.
Its nonzero positive correlations have \(1\le d\le84\). Put
\(m=N-d\). Direct multiplication gives

\[
 w_iw_{i+d}=[i(m-i)]^2+dN\,i(m-i).
\]

Summing over \(i=1,\ldots,m-1\), the ordinary power-sum identities give
\(\sum i(m-i)=(m^3-m)/6\) and
\(\sum[i(m-i)]^2=(m^5-m)/30\). Thus, for \(0\le d<N\),

\[
 a_d=\frac{m(m^2-1)(m^2+1+5dN)}{30}.
\]

This also gives zero at \(d=N-1\); correlations outside the support
are zero by definition. The checker separately expands the original
quartic product in \(\mathbb Q[m,d,i]\), substitutes power sums, and
reduces its difference from this formula to the zero polynomial.
Rational evaluations supplement, rather than replace, that identity check.

At \(n=464\), the coefficient in (1) is \(32-d\) for \(1\le d\le33\),
\(2d-67\) for \(34\le d\le38\), and \(50-d\) for \(39\le d\le84\).
The independently reconstructed values are:

| Quantity | Exact value |
|---|---:|
| \(a_0\) | 156809003 |
| Contribution from \(d=1,\ldots,33\) | 70470797408 |
| Contribution from \(d=34,\ldots,38\) | 1810500079 |
| Contribution from \(d=39,\ldots,84\) | 956045048 |
| Left side of (1) | 73237342535 |
| \(464a_0\) | 72759377392 |
| Left minus right | **477965143** |
| Literal full-convolution energy \(T\) | 4964649096992 |
| Capacity upper bound \(E_{\max}\) | 1654564388902 |
| \(T-3E_{\max}\) | **955930286** |

The last line is exactly twice the scalar gap. It independently checks the
factor two and the direction of the Cauchy contradiction. Since it is positive,
the hypothetical proper coloring cannot exist.

With the old separate-class cap, the same kernel gives gap \(-2799639872\).
The distinct-minimum count adds exactly \(3277605015\), changing its sign.
At side 463 the new scalar cap gives \(-3527580772\); this particular
certificate therefore does not exclude 463. None of these negative values
certifies a coloring or proves an optimality barrier for the method.

## 6. Additional adjacent-layer proof

The colored-minimum refinement is also valid. For \(b=n-425\), a charged
minimum at distance \(d<b\) satisfies \(u<b-d\), so both diagonal
endpoints \(u,u+d\) lie in the length-\(b\) prefix. If \(m_c\) such
matches have original diagonal color \(c\), at most \(\min(2,m_c)\)
large completion classes of that color can be charged. Using maxima yields
the analogous suffix inequality and permits the stated minimum of the two
per-color budgets.

Take two disjoint length-\(q\) windows with \(2q\le b\). The comparisons
at layers \(k\) and \(k-1\) form a path on \(2k\) distinct vertices:
after reindexing the right vertices, the order is
\(Y_0,X_0,Y_1,X_1,\ldots,Y_{k-1},X_{k-1}\).
If \(r\) colors occur on this path, at least \(r-1\) edges change color:
the first occurrence of each color after the first lies after a change.
Consequently there are at most \(2k-r\) matching edges. The capped counts
contribute at most four per color across two layers, so

\[
t_{k-1}+t_k\le\max_{r\in\{1,2,3\}}\min(4r,2k-r).
\]

For \(k=2,\ldots,8\), the bounds are respectively
\(3,4,6,8,9,11,12\). The value 11 at \(k=7\) is sharp even for
arbitrary endpoint words: \(X=0011122\), \(Y=0001122\) gives
\(t_6=5\), \(t_7=6\). Therefore a bound of 10 would be false.

Writing \(\delta_k=\min(6,k)-t_k\), the stated path bounds give
\(\delta_3+\delta_4\ge1\), \(\delta_5+\delta_6\ge2\), and
\(\delta_6+\delta_7\ge1\). For nonnegative nondecreasing weights,
multiplication by \(v_3,v_5,v_6-v_5\) gives total right side
\(v_3+v_5+v_6\). The left coefficients on deficits 3–7 are
\(v_3,v_3,v_5,v_6,v_6-v_5\), each at most its available \(v_k\).
All remaining deficits are nonnegative. This verifies the weighted charging
inequality without an optimization solver.

For the actual kernel, seven layers suffice: \(q=7\) satisfies \(2q\le b\)
at both sides. Exact correlations verify that \(v_k=a_{b-k}\) increase over
these layers. At side 464 the weighted deficit is \(240395555\), giving
the stronger gap \(1199151808\). At side 463 it is \(249859659\), giving
gap \(-2778001795\). These values were independently recomputed. This
strengthening proves the same 464 upper bound, not a smaller one.

## 7. External source audit

The external object is a finite set of distinct integer marks with all positive
pair differences distinct. Translating its first mark to zero preserves the
property, and its ruler length is \(\max B-\min B\). This is exactly the
span convention used above.

* **OGR-24.** The distributed.net completion announcement of November 1,
  2004, at 10:24, explicitly reports exhaustive optimality for 24 marks.
  The same day's explanation at 23:48 identifies the optimal span as 425.
  Therefore the needed lower bound \(G(24)\ge425\) is supported, rather
  than merely an existence upper bound. The announcement also describes
  completed verification passes and correction of an initially omitted search
  category. [Primary November 2004 reports](https://blogs.distributed.net/2004/11/).
* **OGR-25.** The completion announcement of October 25, 2008, at 23:14,
  reports exhaustive optimality and gives a 25-mark ruler from 0 to 480.
  The stated completed search, rather than that example alone, supplies
  \(G(25)\ge480\). [Primary October 2008 report](https://blogs.distributed.net/2008/10/).

Both primary records were read on 2026-11-08. Source authentication,
statement extraction, and translation to the required span lower bounds
passed. No full source text was copied into the repository; no external search
certificate or implementation was downloaded or reverified. These are known
results after notation translation. No novelty search was undertaken in this
review.

## 8. Obligations and reproducibility

| Obligation | Outcome and exact scope |
|---|---|
| Positive equal-leg orientation; containment in square | Passed by the physical-coordinate proof |
| Six classes cover exactly the matching pairs and are disjoint | Passed for every proper three-color square and fixed positive shift |
| Each class is Golomb, including overlapping repeated pairs | Passed by the third-color L contradiction |
| Sorted minima, empty classes, short intervals | Passed universally |
| Span-to-position conversion and threshold endpoints | Passed for \(1\le p\le480\) |
| OGR hypotheses and bound direction | Passed as an application of cited external theorems |
| Cauchy expansion, support, replacement sign, factor two | Passed with the displayed support/capacity hypotheses |
| Polynomial correlation formula | Passed symbolically over exact rational polynomials |
| 464 contradiction integers | Passed by independent pair histograms and literal convolution |
| Adjacent-layer path and weighted deficit | Passed; \(k=7\) bound 11 is sharp |
| External OGR exhaustive computations | Out of scope; accepted external inputs |
| Section 5 endpoint-word enumeration, Lean, global novelty | Not addressed |

The exact-arithmetic environment self-test printed `ENVIRONMENT OK` before
the numerical audit. The checker is
[`independent_counting_check.py`](independent_counting_check.py). Run it
from the repository root:

```text
python research/kernel_compatibility_20261108/review/independent_counting_check.py
```

Besides the load-bearing computation, the completed run checked the polynomial
formula against 7259 literal sums for \(2\le N\le120\), \(0\le d<N\);
all 97733 labeled disjoint families for \(0\le p\le8\) and
\(q\in\{1,2,3\}\), of which 58411 have every class Golomb; 864 physical
forcing configurations including overlapping cases; and 4368 exact convolution
expansions across all three-color diagonal words of lengths 1–6 and four fixed
kernels. It also checked the adjacent path's index description for
\(2\le k\le64\). These finite checks supplement the written proofs and
are not extrapolated into universal theorems.

The run used CPython 3.13.5 and only its standard library. No random sampling
or floating-point arithmetic enters the mathematical calculations; elapsed
time is merely metadata. All code and reviewed proof files have before/after
SHA-256 hashes in the
[`manifest`](independent_counting_manifest.json), with full arithmetic in
[`results`](independent_counting_results.json). The v2 manifest passed the
available computation-audit schema validator with current-file hash checks.
Its run status is `completed`. The coordinator supplied base commit
`654cc044cad3d8ca6079a1931565a6ec44dcf2b5`; this reviewer ran no Git commands.
The hash-pinned working files, rather than that base alone, identify the
audited revision. No output outside this review directory was written.

There is no remaining gap in the stated 464 implication under the two external
inputs. A stronger target such as exclusion of 463 requires a further argument;
the negative values reported here are only limits of these particular
certificates. No additional computation is needed to validate the reviewed
464 claim beyond rerunning the supplied checker if its inputs change.

CLAIM: six-class polynomial 464 contradiction gap | MY VALUE: 477965143 | THEIR VALUE: 477965143 | VERDICT: PASS | METHOD: independent weight-pair distance histogram and literal full convolution

CLAIM: same kernel with old separate capacities | MY VALUE: -2799639872 | THEIR VALUE: -2799639872 | VERDICT: PASS | METHOD: exact capacity substitution after independently constructing all correlations

CLAIM: gain from distinct minima | MY VALUE: 3277605015 | THEIR VALUE: 3277605015 | VERDICT: PASS | METHOD: exact difference of independently reconstructed capacity bounds

CLAIM: side 463 gap with the six-class capacity | MY VALUE: -3527580772 | THEIR VALUE: -3527580772 | VERDICT: PASS | METHOD: fresh literal convolution at n=463 with the same integer weight

CLAIM: adjacent-path bounds at k=2 through 8 | MY VALUE: 3,4,6,8,9,11,12 | THEIR VALUE: 3,4,6,8,9,11,12 | VERDICT: PASS | METHOD: exact max-min evaluation backed by the universal path proof

CLAIM: side 464 adjacent-layer strengthened gap | MY VALUE: 1199151808 | THEIR VALUE: 1199151808 | VERDICT: PASS | METHOD: explicit nonnegative multipliers and independently computed correlations

CLAIM: side 463 adjacent-layer strengthened gap | MY VALUE: -2778001795 | THEIR VALUE: -2778001795 | VERDICT: PASS | METHOD: explicit nonnegative multipliers and independently computed correlations
