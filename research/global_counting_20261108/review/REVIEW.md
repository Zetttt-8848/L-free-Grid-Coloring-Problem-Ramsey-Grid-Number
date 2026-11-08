# Independent audit of the global-counting checkpoint

**Primary verdict: proved as written**, for the final corrected claims and
with the named external OGR inputs retained as external dependencies.
The main counting identities, endpoint inequalities, mixed-source necessary
condition, four rigidity-adjusted capacities, and global occurrence budget
pass this audit. No result
here improves the adopted interval `21 <= R3 <= 464`.

This is a fresh reviewer reconstruction, not author self-review. The reviewer
read the displayed claims and author checker source, then wrote separate
checkers from the physical directed-L definition and raw integer sets. No
author checker or cached extremal table is imported or executed. Agreement
of finite checks is supplementary evidence, not a proof at arbitrary size.

Base revision: `5b5db22c3c65123193cb31f2aa5bd949b3075e1a`.
Branch: `codex/global-counting-research-20261108`. The reviewed research files
were uncommitted working-tree additions. Exact input hashes are recorded in
`independent_results.json` and `supplemental_results.json`; the latter includes
the added mixed-source and rigidity claims. This review changes only `review/`.

## Fixed objects and verdicts

The forbidden shape is exactly `(x,y),(x+d,y),(x+d,y+d)`, `d>0`, with three
equal colors. `V(A)={(v,u):u<v; u,v in A}` is a strict source, not a full
square. All integer coordinates in the computations start at zero.

| Claim | Domain and verdict |
|---|---|
| First-return and all-level identity | **Proved as written**, using the actual Golomb extremal function and every cardinality level. |
| Two-end transport, including empty/singleton cases | **Proved as written** for unions of at most two disjoint Golomb sets. |
| Convolution bridge | **Proved as written** as a necessary condition for a proper three-color square; the universal optimization remains unproved. |
| Binary request collision and second moment | **Proved as written**, with the zero condition necessary but not sufficient for properness. |
| Exact three-direction line identity and missing-pair count | **Proved as written** for every finite integer source and every sign assignment. |
| Six-mark interval obstruction and minimum | Counting obstruction **proved**; exact minimum of one mono-L **computationally verified** over all 32,768 assignments. |
| Mixed-source product and six-input multiplicity | **Proved as written** for the specified horizontal/vertical request families; the initial broader local converse was restricted during review. |
| Quantitative mixed-source lower bound (Q) | **Proved as written**, with exact minimum only within the listed request family. |
| Ten-position partial-coloring obstruction | **Computationally verified** as a complete proper partial coloring with a forced extension conflict, not universal impossibility at side ten. |
| Rectangle exclusion | **Proved as written after correction** to state the proper binary source-coloring hypothesis. |
| Span cost and four improved capacities | **Proved using named external inputs**: OGR-24 optimality and uniqueness up to reflection, OGR-25 lower span bound. Their exhaustive searches were not rerun. |
| Global span-425 occurrence budget | **Proved using the same external inputs**: at sides 463/464, at most eight monochromatic copies per orientation and at most 56 extremal completion classes in total across all offsets. |
| Information-gap witness | **Computationally verified** for the two specified diagonal words; neither word is claimed to extend to a square. |
| A numerical upper bound below 464 | **Incomplete**: no uniform count or positive exact exclusion certificate is supplied. |

## Dependencies and decisive proof checks

The square bridge has the following dependency chain:

`proper three-color square -> source excludes its diagonal color -> proper
binary weak triangle -> each completion-color class is Golomb -> first/last
or transport capacity -> diagonal convolution Cauchy inequality`.

The geometric leaf was read in
`../../kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md` and checked
against the prescribed orientation. Translation of the first coordinate
preserves the shape. Equal-difference pairs `(a,a+h)` and
`(a+t,a+t+h)` in a binary weak-triangle diagonal class force the three
opposite-color cells `(a+h,a),(a+t+h,a),(a+t+h,a+t)`, a valid L of step
`t>0`; overlapping ruler pairs cause no degeneracy. This proves the needed
Golomb property, not merely an abstract graph surrogate.

For the all-level identity, `g(p-s_i)` contributes at level `m` precisely
when `s_i+d < n-G(m)`. Among the first two return starts, the number meeting
this cutoff is exactly `min(2,r_d(A_c intersect [0,n-G(m))))`. This explains
both the `+1` convention in span versus positions and why an omitted level
would invalidate the equality. Empty prefixes and absent first/second
returns contribute zero. The sums are finite because a ruler cannot have
more marks than ambient positions.

For transport, sort the two actual minima and the two actual maxima
independently. The minima are coordinatewise no earlier than `f_1,f_2`;
the maxima are no later than `f_(r-1),f_r`. The actual class incidence is
one of the two matchings. Replacing endpoints in these directions can only
increase each allowed interval length, so taking the maximum of the two
matching sums is safe. A single class is covered by the first matching.
For `r=2`, its inner length is nonpositive and is correctly assigned
capacity zero; for `r=0,1`, the separate definitions are necessary. Both
matching sums are bounded by both separate first/last budgets. The proof
also supports the stated generalization after maximizing over the actual
number of nonempty classes.

For the bridge, let `f_c` be the diagonal color indicators. Expanding
`3 sum_c ||f_c*w||^2 >= ||1_[0,n-1]*w||^2` gives

`3(n a_0+2 sum_d R_d a_d) >= n a_0+2 sum_d (n-d)a_d`.

Thus `sum_d(n-d-3R_d)a_d <= n a_0`. Since `a_d>=0` and `R_d<=C_d`,
substitution gives the stated necessary inequality with `C_d`. The sign
of this substitution is correct. This does not bound the maximum over all
diagonal words; that maximum is the unresolved universal input.

For binary source counts, a pair of distinct equal-offset cells uniquely
specifies its corner in `V(A)`. A horizontal or vertical pair specifies
one L in the integer plane; it is counted internally exactly when its third
cell belongs to `V(A)`. The horizontal, vertical, and equal-offset roles
are disjoint. Consequently the pair-square expansion gives exactly

`4N_mono = T + (Phi-M)/2 + (R+C_line-2M)/2 - S_D`.

This establishes the displayed identity for arbitrary colorings. There
are `2 binom(m,3)` row/column pairs, and precisely `2T` of these are
internal legs, proving the missing-pair cardinality without a factor-two
loss. The bounds `S_D<=|D|`, `R+C_line>=2 floor(m/2)`, and the offset-parity
bound then apply in their stated directions. At `m=6` the resulting
necessary comparison is exactly `129<=125`, which is impossible.

The binary collision product counts one positive and one negative request
at the same corner. Distinct offsets yield four distinct input cells; no
pair of opposite-sign requests can be satisfied there. Algebraically
`H=H^++H^-` and `Kz=H^+-H^-`, so `H^2-(Kz)^2=4H^+H^-`. All-positive
coloring shows why this is not equivalent to properness.

For mixed-source requests, a horizontal pair lies wholly in `V(A_a)` and
a vertical pair wholly in the disjoint domain `V(A_b)`. Distinct horizontal
steps lie on different rows; distinct vertical steps lie on different
columns. Each nonzero product selects one request of each excluded color,
so no request can be reused with two colors. Its six input cells are
therefore distinct. Every proper square has zero such product at every
mixed cell. This establishes a necessary compatibility condition, not a
sufficient extension test.

The added quantitative inequality (Q) also passes: each listed L has one
mixed, unspecified cell, so distinct completion cells index disjoint sets
of Ls. Choosing color `t` at `q` incurs exactly `D_q^t` monochromatic
members of that family. Minimizing independently at each `q` gives the
displayed sum of three-way minima. This is an attained minimum for the
restricted family and a lower bound, not an exact minimum, for all Ls of
the full square. The same argument handles nonnegative individual L weights.

For span cost, distinct minima have sum at least `0+...+(t-1)` and
distinct maxima sum at most `(p-t)+...+(p-1)`, independent of their pairing.
Their difference is `t(p-t)`. At most two span-425 classes and integral
spans give the lower total `425t+(t-2)_+`. In the general multilevel version,
the premise that every span is at least `g_0` must be explicit.

The primary [OGR-24 announcement](https://blogs.distributed.net/2004/11/)
was read directly on 2026-11-08: its November 1 nugget entry states both
exhaustive optimality at span 425 and uniqueness up to reflection. The
published gap list reconstructs the displayed `Q`. The
[OGR-25 announcement](https://blogs.distributed.net/2008/10/) of October 25
states exhaustive optimality at span 480. These are accepted external
computational inputs, not local certificates. The independent exact check
confirms all 276 positive differences of `Q` are distinct, every difference
1 through 127 is present, and 128 is absent. Two equally oriented optimal
rulers in at most 553 positions have translation displacement at most 127
and must intersect. This proves the at-most-two bound with the cited
uniqueness input. The explicit opposite-orientation packing in 427
positions is also valid.

For the added global occurrence argument, every pair of distinct translated
copies in a fixed orientation intersects in exactly one point: the shift
is a positive integer at most 127 and occurs exactly once as a ruler
difference. Consequently any monochromatic copies in that orientation
must have one common diagonal color. Counting copy-point incidences and
unordered copy-pair intersections proves the three moments in (3), while
Cauchy and two-term inclusion-exclusion give (4), including the empty case.

The injection (5) also passes. A completion class `P+s` at lag `d>0`
requires monochromatic diagonal copies at starts `s` and `s+d`. Their
unordered pair determines `s,d`, the original color, and the physical set
of completion cells. This set cannot simultaneously be two different
completion-color classes. Thus no extra multiplicity is lost in the
weighted pair budget. Opposite orientations are counted separately.

For one diagonal class, convolution with `w_i=i(86-i)`, `1<=i<=85`, is
supported on at most `n+84` positions. Its squared norm is
`m a_0+2 sum_d r_d(A_c)a_d`; the two-Golomb bounds give `r_d<=46` below
426 available positions and `r_d<=48` above that cutoff, throughout the
actually used range. Cauchy therefore yields the stated quadratic
necessary condition. The independent pairwise summation gives
`W=105995`, `a_0=156809003`, `S_463=527721881456`, and
`S_464=527996693840`.

Writing its left side minus right side as `F_n(m)`, the endpoint values
are `F_463(164)=-555944285156`, `F_463(165)=3054576458428`,
`F_464(164)=-1259980029536`, and `F_464(165)=2350383905045`.
Every integer `m` from zero through `n` was checked; the largest feasible
value is 164. Increasing positive differences of this quadratic also
show directly that all larger values are excluded. For `t=9,...,38`
or `9,...,39`, the minimum of `24t-binom(t,2)` is 180, already exceeding
164. Hence `t<=8`; the moment bound safely controls the general large-t
tail but is not additionally needed on these two short ranges. The
injection then gives at most `2 binom(8,2)=56` extremal classes across
all lags. This concerns only span-425 completion classes; longer
24-mark classes are not included in that budget.

## Scope findings resolved during review

1. **Rectangle properness.** With `A={0,1,2,3}`, assign the ordered cells
   `(1,0),(2,0),(2,1),(3,0),(3,1),(3,2)` signs
   `(+,-,+,+,-,+)`. Then `(2,1),(3,1),(3,0),(2,0)` form a four-sided
   forcing rectangle, even if only edges to opposite-sign completions
   are retained. The assignment is improper: `(1,0),(3,0),(3,2)` is
   monochromatic. Thus the rectangle proof is correct only with the
   proper-coloring hypothesis, which must be attached to its statement.

2. **Mixed request-list converse.** The `H/V` lists do not include every
   request from the prescribed sources. A mixed `q=(v,u)` can also be
   the corner of the L with inputs `(v-h,u)` from `V(A_b)` and
   `(v,u+h)` from `V(A_a)`. Both can have third color `e`, forbidding
   that color at `q`. Therefore the local equivalence involving the
   displayed `D_q` counts is valid only for the listed row/column
   requests. The main necessary condition `C_mix=0` is unaffected.

3. **Multilevel lower endpoint.** The generalized span-level inequality
   requires that each span is at least `g_0`. The actual application
   has this hypothesis from `G(24)=425`; spelling it out prevents an
   overbroad standalone reading.

These findings were sent to the respective authors. The final read confirms
that (1) properness is explicit in the rectangle statement, (2) the local
converse is restricted to H/V and explicitly acknowledges the omitted
parallel-input requests, and (3) the multilevel premise includes the lower
span bound `g_0`. No author-owned mathematical file was modified by the
reviewer. The historical findings above document why those restrictions
are mathematically necessary.

## Exact computation and coverage

The environment prerequisite `python scripts/self_test.py`, run in the
exact-verification skill directory, returned `ENVIRONMENT OK`.

From the repository root:

```
python research/global_counting_20261108/review/independent_check.py
python research/global_counting_20261108/review/supplemental_check.py
```

The first checker reconstructs short Golomb capacities by cardinality and
minimum occupied span, enumerates subsets followed by their two-color
partitions, and enumerates literal physical Ls from their left endpoint and
step. This differs from the author source checker, which constructs Ls
from corner/offset requests. Exact integer computations independently
reproduce the following claims:

CLAIM: source-check domain | MY VALUE: 64 sets, 40069 assignments, 1367 proper | THEIR VALUE: 64 sets, 40069 assignments, 1367 proper | VERDICT: PASS | METHOD: literal directed-L enumeration over all subsets of {0,...,5}

CLAIM: six-mark interval minimum monochromatic L count | MY VALUE: 1 | THEIR VALUE: 1 | VERDICT: PASS | METHOD: all 32768 sign assignments on the 15 physical source cells

CLAIM: transport separation capacities | MY VALUE: (10,10,10,9), zero valid partitions | THEIR VALUE: (10,10,10,9), zero valid partitions | VERDICT: PASS | METHOD: independently computed Golomb capacities through 14 positions and all 1024 partitions

CLAIM: all-level finite identities | MY VALUE: 191916 identities on 9840 nonempty words | THEIR VALUE: 191916 identities on 9840 nonempty words | VERDICT: PASS | METHOD: every ternary word of lengths 1 through 8, every lag and color

CLAIM: valid two-class partition coverage | MY VALUE: 27334 on ambient lengths 1 through 10 | THEIR VALUE: 27334 | VERDICT: PASS | METHOD: subsets followed by all binary class assignments; additionally one empty-ambient case

CLAIM: information-gap words | MY VALUE: common R=(5,5,3,2,1,0,0,0); E sums=(6,6,4,2,1,0,0,0) and (6,6,3,2,1,0,0,0) | THEIR VALUE: the same vectors | VERDICT: PASS | METHOD: direct reconstruction for 000000121 and 000010111 using short exact capacities

CLAIM: mixed-source extension witness | MY VALUE: source L counts (5,0,0), 19 proper fully prescribed Ls, C_mix=1 at (8,3) | THEIR VALUE: the same counts | VERDICT: PASS | METHOD: all physical triples in the 10 by 10 square and request products grouped by missing role

CLAIM: quantitative restricted-family minimum | MY VALUE: 1 monochromatic L among 9 listed requests | THEIR VALUE: 1 among 9 | VERDICT: PASS | METHOD: unique physical-triple keys and independent minimization over each completion cell's three request totals

CLAIM: rigidity capacities | MY VALUE: 428:140, 429:141, 430:142, 431:143; no other changes for 1<=p<=480 | THEIR VALUE: the same capacities and range | VERDICT: PASS | METHOD: independent total-endpoint and integer-span sums for every t in {0,...,6}

CLAIM: n=463 quadratic margin with shape cost | MY VALUE: -2534488525 | THEIR VALUE: -2534488525 | VERDICT: PASS | METHOD: direct sum over all unordered weight-position pairs, w_i=i(86-i), 1<=i<=85

CLAIM: n=464 quadratic margin with shape cost | MY VALUE: 1433217328 | THEIR VALUE: 1433217328 | VERDICT: PASS | METHOD: direct sum over all unordered weight-position pairs with the same exact weights

CLAIM: one-class cardinality at sides 463 and 464 | MY VALUE: at most 164 at both sides | THEIR VALUE: at most 164 | VERDICT: PASS | METHOD: direct weighted-pair reconstruction of Cauchy coefficients and exact evaluation for every integer 0<=m<=n

CLAIM: global extremal occurrence budget | MY VALUE: at most 8 copies per orientation and 56 span-425 completion classes total | THEIR VALUE: 8 and 56 | VERDICT: PASS | METHOD: unique-intersection incidence moments, exact integer range checks, and injective class-to-occurrence-pair count

Author checker ranges were inspected: the multilayer checker computes
`g(p)` for `0<=p<=14`, enumerates ternary states on lengths 1 through 10
only after requiring both represented classes to be Golomb, and checks
all words on lengths 1 through 8. The completion checker enumerates every
binary source on all subsets of `{0,...,5}`; its six-mark case is included
in that enumeration, not an additional independent exhaustive run. The
added ten-position witness is checked directly, not by a search over all
ten-position colorings. The rigidity checker verifies a particular ruler,
all relevant translation displacements, finite endpoint arithmetic, and
two weight margins; it does not prove the OGR uniqueness theorem locally.
Its added global-occurrence checks evaluate all integer cardinalities and
occurrence counts at sides 463/464 and illustrate the moments on four
start sets; those examples are not an exhaustive enumeration of start
subsets. The independent supplemental checker also checks every pairwise
intersection for both orientations throughout the relevant start ranges.

## Remaining gap and strongest safe conclusion

The package retains information genuinely absent from scalar correlation
counts and independent-source feasibility. It supplies exact necessary
conditions, a partial-extension obstruction, a four-entry capacity
improvement, and a global budget of 56 extremal completion classes. It
does not supply a universal lower bound for `C_mix`, a
universal upper bound for the weighted transport functional, or a positive
exact certificate at side 463. Those are the missing implications to a
smaller three-color Ramsey upper bound. Additional short-word or interval
enumeration alone cannot establish them.

The tested shape-cost margin at 463 is negative. Savings from the
shape-cost and colored-boundary restrictions constrain the same number
of 24-mark classes and must be combined by intersection/minimum before
optimization; adding their numerical savings would double-count.

The cheapest useful continuation is a uniform bound that uses mixed-cell
color lists or a correctly combined exact optimization of the common
24-mark-class count. The accepted numerical interval remains unchanged.

CLAIM: new numerical upper bound below 464 | MY VALUE: not established | THEIR VALUE: no improvement claimed | VERDICT: UNDECIDED | METHOD: missing universal counting bound or exact positive exclusion certificate
