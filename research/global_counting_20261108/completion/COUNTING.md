# Count completion conflicts before summing away the labels

## 0. A cross-source count that separate binary sources cannot see

This is the principal new object of this work package. Partition
I={0,...,n-1} into three diagonal color classes A_0,A_1,A_2. Prescribe the
diagonal and a proper binary coloring of every V(A_c), avoiding color c.
These three source domains are disjoint. They do not specify cells whose
two diagonal endpoint colors differ.

Fix such a mixed cell q=(v,u), v>u, and write a=chi(v,v), b=chi(u,u),
a!=b; let e be the third color. Define two families of requests:

* A horizontal request from source a, of step h>0, is the pair
  `(v-h,u-h),(v,u-h)`, when u-h,v-h are in A_a. Let H_q^t count these
  pairs whose two cells both have color t.
* A vertical request from source b, of step k>0, is the pair
  `(v+k,u),(v+k,u+k)`, when u+k,v+k are in A_b. Let V_q^t count these
  pairs whose two cells both have color t.

All cells must lie in I squared. The displayed membership conditions
already ensure this. Both pairs form an L with q: the first uses q as
its upper endpoint, and the second uses q as its left endpoint. These
are exactly the row/column pairs counted as missing completions of the
three strict sources in Section 2. Their completion lies inside the
full strict triangle, though outside their own source.

Since source a avoids a and source b avoids b, H_q^a=V_q^b=0. Thus the
counts of requests forbidding colors a,b,e at q are respectively

`D_q^a=V_q^a`, `D_q^b=H_q^b`, `D_q^e=H_q^e+V_q^e`.

Define the global cross-source conflict count

`C_mix=sum_(q mixed) V_q^a H_q^b (H_q^e+V_q^e)`.    (M)

**Mixed-completion counting theorem (proved).** Every proper full square
has C_mix=0. More precisely, (M) counts triples of prescribed-source
requests at one physical cell, one request forbidding each color. Every
nonzero summand corresponds to six distinct input cells. If the three
proper source colorings are given independently and C_mix>0, they cannot
simultaneously extend to a proper full square.

Proof. Each listed request forbids its input color at q. One request of
each of the three colors leaves no available color. Conversely, **these
H/V row/column requests** leave some color available at this one q if
and only if at least one of D_q^a,D_q^b,D_q^e vanishes. This proves the
local request-list equivalence and the count. It does not assert that
all these local choices together extend to a proper square. For example,
there can also be an L with q as its bend and its two prescribed parallel
inputs belonging to different original sources; such a request is not
included in H or V. Other Ls can use multiple unspecified cells.

To check the multiplicity, requests of different steps within the H
family have disjoint two-cell supports, as do requests in the V family.
The H input cells lie in V(A_a), whereas the V input cells lie in
V(A_b), which is disjoint. The same H request cannot contribute both
color b and color e, so terms that formally reuse it vanish; likewise
for V. Every nonzero product therefore has six distinct cells. With
one-hot color indicators it is a degree-six multilinear count after
discarding these zero terms. For arbitrary nonnegative weights lambda_q,
the weighted sum of the products also must be zero.

There is an exact quantitative version. For **any** extension of the
prescribed sources to a full square, let N_mono be its total number of
monochromatic Ls. Then

`N_mono >= sum_(q mixed) min(V_q^a,H_q^b,H_q^e+V_q^e)`.             (Q)

Indeed coloring q by t makes exactly D_q^t of the listed requests
monochromatic. Each listed L has exactly one unspecified cell q and is
counted just once: q's geometric role and the two prescribed inputs
determine its source and step. The listed L families for different q
are therefore disjoint. Sum their individual minimum costs to obtain
(Q). In fact the right side is the exact minimum number of monochromatic
Ls **within this request family** over all choices of the mixed-cell
colors, because these choices are independent for that restricted
family. The analogous weighted statement holds with nonnegative L
weights and weighted request totals. This provides a global count with
explicit multiplicity, not merely the existence of one forbidden pattern.

There is a useful intermediate interpretation. The product H_q^b H_q^e
counts pairs of requests that **force q to its diagonal-endpoint color
a**, even though q is outside V(A_a). The opposite source can then
forbid that same color through V_q^a. Thus

`C_mix=sum_q [(H_q^b H_q^e)V_q^a + (V_q^a V_q^e)H_q^b]`

counts conflicts between such two-request color locks and requests
from the other original diagonal color class. It retains original
color, source, orientation, and physical completion labels.

### A complete distinguishing witness

Take n=10 and

`A_0={1,2,6,7,8}, A_1={3,4,9}, A_2={0,5}`.

Prescribe V(A_0) by the following complete table:

| Cell | Color | Cell | Color |
|---|---:|---|---:|
| (2,1) | 2 | (6,1) | 2 |
| (6,2) | 2 | (7,1) | 2 |
| (7,2) | 1 | (7,6) | 1 |
| (8,1) | 2 | (8,2) | 1 |
| (8,6) | 2 | (8,7) | 1 |

Give all three cells of V(A_1) color 0 and the one cell (5,0) of V(A_2)
color 0. Every prescribed source avoids its diagonal color and is proper.
The first source has five Ls, all nonmonochromatic; the other two have
none. In addition, all 19 Ls wholly contained in the union of the three
sources and the prescribed diagonal are proper. This is directly
verified from all physical triples, including those crossing sources.

At q=(8,3), the actual requests include

| Prescribed input pair | Source | Color excluded at q |
|---|---:|---:|
| (7,2),(8,2) | 0 | 1 |
| (6,1),(8,1) | 0 | 2 |
| (9,3),(9,4) | 1 | 0 |

Hence the term at this q is positive. Every individual binary source,
and consequently every valid necessary inequality on those individual
sources, passes; their joint prescription still has no square extension.
This is a concrete information gap in approaches that treat the three
original diagonal color classes independently. It is a **partial-coloring
extension obstruction**, not a claim that all 10-square colorings fail.

### What would turn the count into a smaller upper bound

A sufficient next theorem would give a positive lower bound on (M)
for every partition and proper source prescription arising at a proposed
square size, or give another forced contradiction from the induced
two-request locks. No such lower bound is proved here. Merely knowing
the total number of requests does not determine their distribution among
the three forbidden colors at each cell. This is a precise unsolved
counting problem, rather than an assumed uniform multiplicity budget.

## 1. A nonnegative cross-offset collision count

Let z:V(A)->{-1,+1}. For q=(v,u), put

`D_q={d:0<d<v-u, u+d in A, v-d in A}`,

`p_(q,d)=(u+d,u), r_(q,d)=(v,v-d)`.

These are the two parallel inputs of an L completed at q. Its step is
v-u-d, not d. Write H_q^+ and H_q^- for the numbers of d in D_q whose
two inputs have sign +1 and -1, respectively. Define

`C(A,z)=sum_q H_q^+ H_q^-`.

**Claim 1 (proved).** C is a nonnegative integer. It vanishes for every
proper binary source coloring. It counts pairs of incompatible forcing
requests at the same physical cell, with their distinct offsets retained.

Proof. A same-sign input pair forces the opposite sign at q. A positive
and a negative request cannot both be satisfied. For fixed q and distinct
d,e, the four input cells are distinct: the p cells are distinct along
the row through q, the r cells are distinct along its column, and their
only possible row/column intersection is q, which is excluded. Thus each
product H_q^+ H_q^- counts exactly one unordered pair of requests with
opposite signs, without a hidden same-cell identification. In particular,
the count genuinely couples different offsets. Summing proves the claim.

Set H_q=H_q^++H_q^- and

`(Kz)_q=(1/2)sum_(d in D_q)(z(p_(q,d))+z(r_(q,d)))`.

Then, for **every** coloring, proper or not,

`4C(A,z)=sum_q [H_q^2-(Kz)_q^2]`.

The terms are nonnegative because Kz=H^+-H^-. Equivalently the count
expands into degree-four indicator products on four distinct cells. Its
zero condition is stronger than an aggregate total-demand count, which
forgets whether requests at one cell agree. It is weaker than properness:
all-positive coloring has C=0 even when it contains many positive Ls.
It is not advertised as a new independent condition beyond the existing
full pointwise forcing system.

**Exact distinguishing example.** For A={0,1,2,3}, give (1,0),(3,2) sign
+1 and (2,0),(3,1) sign -1. The two offsets 1 and 2 send opposite
requests to (3,0), so C>=1 regardless of that completion's sign. The
assignment to (2,1) is irrelevant to this collision. This is the existing
shared-completion obstruction now measured by a sum that can be weighted
and aggregated without dropping the offset labels.

## 2. A joint row, column, and offset square count

Put m=|A| and M=binom(m,2). For each positive offset d let

`r_d=|{u:u,u+d in A}|`, `s_d=sum_u z(u+d,u)`,

`T=sum_d binom(r_d,2)`, `Phi=sum_d s_d^2`.

T is the number of all directed Ls in V(A), regardless of their colors:
two distinct cells of one offset have exactly one completion in V(A).
For each source row and column sum its signs; let R and C_line be the
sums of squares of those row sums and column sums. Empty lines contribute
zero.

Let J be all unordered pairs of cells in a common row or a common column.
Each such pair determines a unique directed-L completion in the integer
plane. Let D be the pairs for which that third cell is absent from V(A),
and let

`S_D=sum_({p,r} in D) z(p)z(r)`.

**Claim 2 (proved, exact for arbitrary colorings).** If N_mono is the
number of monochromatic directed Ls in V(A), then

`8 N_mono = 2T + Phi + R + C_line - 3M - 2S_D`.       (1)

Proof. For signs x,y,z,

`4*1_(x=y=z)=1+xy+xz+yz`.

Sum over all T Ls. Their parallel-input pair products sum to
(Phi-M)/2. Their horizontal and vertical leg-pair products sum to
(R+C_line-2M)/2-S_D: the full row/column square expansion counts J,
and precisely D must be removed. The three pair roles are distinct,
and every pair in each role specifies at most one L. Multiplication by
two gives (1).

For a proper coloring (1) becomes

`2T + Phi + R + C_line = 3M + 2S_D`.                 (2)

There are binom(m,3) common-row pairs and binom(m,3) common-column pairs.
Each actual L supplies exactly two of these pairs. Consequently

`|D|=2binom(m,3)-2T`.

Using S_D<=|D| in (2) yields the universal necessary condition

`6T + Phi + R + C_line <= 3M + 4binom(m,3)`.         (3)

Every line sum has the parity of that line's length, so each odd-length
line contributes at least 1 to its square. The source rows have lengths
0,...,m-1, and so do its columns. Hence

`R+C_line >= 2 floor(m/2)`,

`Phi >= #{d:r_d is odd}`.

This gives a completely color-free necessary inequality

`6T + #{d:r_d odd} + 2floor(m/2) <= 3M+4binom(m,3)`. (4)

This is a joint line count rather than six separate ruler capacities.
It retains exactly the information discarded when actual row/column
pairs are replaced by a single aggregate offset count.

## 3. A hand-checkable consequence and its limits

Take A={0,1,2,3,4,5}. Then M=15, T=20, Phi>=3 and R+C_line>=6. Inequality
(3) would require 129<=125, a contradiction. Thus this strict source has
no proper binary coloring, by a short pure counting argument. This
noncolorability is not claimed as a newly discovered extremal result.

More generally for an interval of m marks, D is empty and T=binom(m,3),
so (1) gives the quantitative lower bound

`N_mono >= max(0,ceil((2binom(m,3)-3binom(m,2)+3floor(m/2))/8))`.

The exact checker enumerates every binary source coloring for all subsets
of {0,...,5}; it separately enumerates the 2^15 colorings of the six-mark
interval and records its true minimum N_mono. Those finite checks audit
the identities; the proofs above establish them for arbitrary finite A.

**Why this has not improved R3.** A diagonal color class in a hypothetical
three-color square generally has density around one third. In that
regime, the number of missing completions can be large; replacing S_D
with |D| loses the cross-color geometry that is needed. For example,
on the fixed integer set {0,3,6,...,459} there are no missing completions
relative to its own lattice, and (4) excludes it strongly. But many sets
of the same cardinality and span have much smaller additive T and are
not excluded by (4). Density alone does not make the interval argument
applicable.

The unproved bridge is a bound on **signed** S_D, summed over the three
actual diagonal color classes, that uses their shared full-square
completion cells. A missing horizontal completion from one diagonal
color class and a missing vertical completion from another can be the
same physical cell. Its available color must satisfy both demand lists.
The nonnegative conflict count in Section 1 suggests a way to measure
this compatibility, but no uniform bound strong enough for a new R3
number is proved here. More small interval checks cannot repair that gap.

## 4. A geometric check on prospective graph estimates

For a **proper binary source coloring**, the physical forcing graph has
an edge from each input of a same-sign pair to its opposite-sign
completion. Under this properness hypothesis it has no four-cycle
following the four sides of an axis-aligned rectangle.

Indeed let p=(a,b), q=(a+h,b), s=(a,b-k), r=(a+h,b-k), with h,k>0.
Suppose all four sides are forcing edges. Bipartiteness gives p,r the
same sign, and q,s the other sign. The forcing edge p->q supplies the
same-sign mate A=(a+h,b+h); p->s supplies the same-sign mate
D=(a-k,b-k). Thus D,r,A are a monochromatic L of step h+k, contradiction.

This argument does **not** exclude four-cycles wholly inside one row or
one column. Accordingly it does not justify importing a general C4-free
graph extremal bound. Nor is rectangle-freeness alone a proved linear
bound on the total forcing edges. It is retained as a check on a future
counting model, not as a replacement for the missing global estimate.

## 5. Generalization and evidence status

Both formulas exploit binary signs after one diagonal color has been
excluded. For a four-color square that source has three colors, and the
binary monochromatic-triple identity no longer applies. The physical
demand-list formulation still makes sense with more colors, but local
incompatibility then requires requests collectively to exclude every
available color. No numerical four-color consequence is asserted.

Status: The mixed-completion counting theorem, Claims 1 and 2,
inequalities (3)-(4), and the rectangle argument
are **PROVED** by the displayed arguments. The exhaustive checker is
**FINITE-CHECKED** in its stated domain. A smaller three-color Ramsey
upper bound from these counts is **UNDECIDED**. The accepted interval
remains 21<=R3<=464.
