# Independent encoding and hereditary-transfer review

Reviewer: a separate theory agent. Files read in full: `finite_caps.py`,
`transfer.py`, `consumer.py`, the inherited `verify_four_rank.py`, and
`verify_four_edges.py`. No numerical jobs were run by this reviewer.
The added `audit_finite.py` is for the main agent to execute; its execution
status belongs in the main verification record. This is not Lean or external
peer review.

## Finite-source encoding: soundness and completeness

The first n variables select coordinate marks. Each pair 0 <= y < x < n has
one Boolean cell-color variable; a Boolean already gives exactly one of two
colors. For every physical L, both monochromatic assignments are forbidden
when all its coordinate marks are selected. The guard uses the distinct
marks in {x,y,x+d,y+d}; this correctly handles the three-mark case x=y+d.

The threshold variable s(i,j) means that at least j of the first i marks are
selected. Its four clauses are exactly

    p -> z;  (a and q) -> z;
    z -> (p or a);  z -> (p or q),

where z=s(i,j), p=s(i-1,j), q=s(i-1,j-1), and a is the current mark.
Together they express z iff p or (a and q). The boundary values s(i,0)=true
and s(i,j)=false for j>i make induction on i immediate. Asserting s(n,K)
therefore imposes cardinality at least K, in both directions.

The implementation's Boolean simplification is correct: it distinguishes
Python Boolean constants by their type before testing or removing them, so
integer literal 1 is not accidentally treated as a true constant.

Every satisfying assignment restricts to a proper source on the selected
marks. Conversely, every proper source of at least K marks extends to a
satisfying assignment by coloring unused cells arbitrarily and setting the
threshold variables to their actual prefix meanings. No symmetry-breaking
restriction or special family is imposed.

Thus complete checked UNSAT certificates establish universal finite-source
caps. SAT witnesses establish matching lower values only at their actual
cardinalities. In particular, an upper cap at 20 positions is not an exact
maximum unless a matching 14-mark witness is supplied.

`audit_finite.py` independently reconstructs the CNFs without importing the
encoder: it discovers physical Ls by pairs of equal-diagonal arms, allocates
threshold IDs by a closed prefix-count formula, and compares clause multisets.
It also checks all source cells and every physical L in each supplied witness.
It deliberately does not implement a partial DRAT checker. With `--checker`
and the executable path, it invokes complete drat-trim verification separately
for each stored CNF, expanding `.drat.xz` traces in a temporary directory.
Without that option it makes no proof-verification claim. Checker and expanded
trace hashes plus output logs identify the full proof checks when run.

## Hereditary minimum-span propagation

If at most c marks fit in n consecutive positions, c+1 marks require span
at least n. Hence the seeds {8:8,10:12,12:16,15:20} have the correct positions
versus span interpretation, subject to their finite certificates.

Let ell(j) be a proved lower span for j marks, with ell(1)=0. For k marks
in span L, the H=c*k-c*(c+1)/2 pairs at rank distances 1 through c have total
distance at most

    c*(c+1)*L/2 - 2*sum_(j=1)^c (c-j+1)*ell(j).

This follows by summing the first/last-j endpoint bounds; each endpoint subset
inherits the proper source coloring. Meanwhile, at distance h the two disjoint
Golomb start classes have total size at most Q(L-h)+Q(L-h-1): after ordering
their distinct minima, the second class starts at least one position later.
An empty class causes no problem. Q denotes capacity for a span, not positions.

Greedily filling the shortest distances up to these upper multiplicities
gives a valid lower bound P on that total distance. If there are fewer than H
available slots, the candidate span is impossible. Otherwise the necessary
inequality is 2P+4*endpoints <= L*c*(c+1), exactly as used in `transfer.py`.

The algorithm need not retest an earlier rank after increasing the candidate
span: every integer it discards has already failed a proved necessary
condition. It only claims a lower span, not that the first unrejected span
is realizable. Strict growth ell(k)>=ell(k-1)+1 follows by deleting an endpoint.

Taking the minimum of this hereditary cap and the old analytic cap is valid.
The right-bisection expression uses span n-1 for n positions, and the terminal
sentinel must exceed every endpoint span queried, as the script asserts.

## Scope of numerical promotion

This review establishes the encoding and transfer arguments above. It does
not independently execute the proof checker or reproduce the final numerical
consumer. The full R4 assertion additionally needs the checked proof traces,
executed independent witness/CNF audit, exact variance and consumer arithmetic,
and the inherited full-square reduction. Those are separate dependencies;
an improved local cap alone is not a Ramsey bound.
