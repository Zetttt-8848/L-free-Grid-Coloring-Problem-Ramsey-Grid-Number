# A computer-assisted upper bound R4 <= 21,947,865

## Claim and evidence status

Every coloring of {0,...,21,947,864}^2 with at most four colors contains
three cells of one color at (x,y), (x+d,y), (x+d,y+d), for integer d>0.
Thus R4 <= 21,947,865. This is an unconditional computer-assisted claim:
there is no open S21, G9, or other conjectural premise. Its evidence comprises
the proofs below, checked finite exclusion traces, exact rational data, and
integer/rational arithmetic. It is not a Lean formalization or an external
referee decision. Internal independent reviews and checks are packaged here.

The prior certificate in this branch proves R4 <= 21,947,877. The improvement
is 12. The comparison without the new finite exclusions reaches 21,947,866,
so 11 units come from transporting existing rank information into a different
consumer and one further unit from the finite-compatibility input.

## 1. Finite source capacities

Define C(n) as the maximum size of A subset {0,...,n-1} such that the strict
source V(A)={(v,u):u<v, u,v in A} admits a proper binary coloring.
The finite package establishes

    C(4)=4, C(8)=7, C(12)=9, C(16)=11, C(20)<=14.

For the four nontrivial upper caps, the formulas for (n,k)=(8,8),(12,10),
(16,12),(20,15) exclude all sources with at least k marks. Every coordinate
has a presence bit; every possible strict-source cell has a color bit.
For every physical L, two clauses forbid its three colors from being equal
whenever all distinct coordinate marks are present. Prefix threshold variables
encode the cardinality by full Boolean equivalence. The construction is
sound and complete and uses no symmetry breaking. See ENCODING_REVIEW.md.

Complete DRAT traces are checked by the independently compiled
[DRAT-trim checker](https://github.com/marijnheule/drat-trim/tree/2e3b2dc0ecf938addbd779d42877b6ed69d9a985).
Matching complete colorings establish the three nontrivial equalities.
C(20) is not claimed exact: its 13-mark test was undecided at the chosen
conflict limit, and its checked witness only gives C(20)>=12.

Translation preserves the problem. Therefore each s-mark source has span
at least e_s, with the seeds e_8>=8, e_10>=12, e_12>=16, e_15>=20.
These seeds constrain every translated short interval, not a selected source.

## 2. Hereditary rank transfer

Use the elementary Golomb lower-span array g_s from
../boundary_certificates_20261115/FOUR_COLOR.md, reconstructed by its formula.
Put Q(L)=max{s:g_s<=L}, with Q(L)=0 for L<0. For a binary-source set of
span L, the starts at difference h split into two disjoint Golomb sets.
Ordering their minima gives

    r_A(h) <= v_h(L)=Q(L-h)+Q(L-h-1),  1<=h<=L.

For s ordered marks and rank parameter 1<=c<s, let H=cs-c(c+1)/2.
Let P(H;v) be the sum of the cheapest H available differences when positive
difference h has capacity v_h. The rank-neighbor telescoping identity gives

    2P(H;v) + 4 sum_(i=0)^(c-1) (c-i)e_(i+1) <= L*c*(c+1).

The first and last i+1 marks belong to the same hereditary family, so the
endpoint spans are at least e_(i+1). The inequality also holds when those
blocks overlap. If there are fewer than H available differences, the source
is immediately excluded.

For each s=2,...,600, start at max(e_(s-1)+1, applicable seed). Test every
c<=min(s-1,80), discarding every integer L that violates its rank inequality.
Previously discarded spans stay excluded. Every endpoint cost refers to
smaller ranks, so induction proves the stored lower spans. The final entry
exceeds 1820; no local capacity lookup extrapolates past the table.

At n positions define the improved local cap as the minimum of the old
elementary cap and max{s:e_s<=n-1}. Restriction proves its applicability to
every short interval used in the endpoint discrepancy calculation.

## 3. Endpoint discrepancy and binary witnesses

Keep the original rational windows, seven sample entries, interval grouping,
and all parameter domains. In the binary endpoint discrepancy formula replace
only the local capacities by those from section 2. Direct rational summation
gives a discrepancy lower bound about 219.44128252868413. In particular,

    D >= 1097/5 = 219.4.

The original discrepancy proof allows any positive real D below P; it does
not require an integer. Therefore the same coverage/Cauchy proof gives

    k^2 <= (p + B*alpha - 1097/5)
           * (k*a_0 + 2 sum_(h>0) v_h*a_h).

The ordinary Golomb correction remains 52, with all 201 thresholds rebuilt
and their original domains checked. Each row of consumer_results.json
excludes size K+1 at its stated p and dilation B by a strict rational
inequality. Heredity extends that cap to every smaller p. The last row is
an explicit shorter-interval continuation, not an extra unproved cap.

The exact rational matrices are inherited from the pinned data directory in
../r4_binary_compatibility_20261114/external_windows/. Their original source
revision and hashes are recorded there. No rounded asymptotic Sidon constant
is used as a premise.

## 4. Arbitrary four-color squares and the final contradiction

Start with an arbitrary proper four-color square of side n. At each positive
main-diagonal lag, partition equal-color endpoint pairs by original color and
completion color. The twelve classes have properly binary-colored strict
sources by the two color exclusions. Their distinct minima give the baseline
sum of the twelve staggered binary capacities proved in section 3.

Use exactly the inherited twenty-shift counting lemma: over each isolated
capacity drop the two short diagonal words have total selected matches at
most 133, against allowance 174. Hence at least 41 matches are missing in
each disjoint block. This is proved by the four-count recurrence, not by
assuming independent choices at different shifts.

Keep the original outer width 35,990 and quartic integer weights

    u_i=i*(35991-i), w_i=u_i*(5*35991^2+6*u_i), 1<=i<=35990.

Let b_d=sum_i w_i*w_(i+d). Joint Cauchy on the four diagonal colors requires

    -3*n*b_0 + 2 sum_(d=1)^35989 (n-d-4*U_d)*b_d <= 0,

where block savings are credited at each block's minimum correlation.
For n=21,947,865, substituting the checked capacities and the disjoint-block
savings gives the strictly positive integer

    667767862929561436134957406955093129954012400.

This contradiction excludes every allowed coloring of that square. It does
not merely exclude a source, a triangle, a fixed boundary, or a selected
coloring family. The scan's unsuccessful preceding side is not an optimality
claim and is not used as evidence for the upper bound.
