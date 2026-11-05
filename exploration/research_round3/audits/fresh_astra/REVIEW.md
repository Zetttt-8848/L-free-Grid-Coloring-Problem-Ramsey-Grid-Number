# Fresh Astra independent review of cores G, J and F

Reviewer: `fresh_astra`, GPT-6 Astra, requested Level 3 / ultra. Assignment:
`research_round3/audits/reviewer_assignment.json`. The reviewer is not an author
of any assigned core. No subagent was spawned. No author file was edited.

**Primary verdict: proved as written, using the expressly accepted Round-2
proof leaves. All assigned load-bearing items PASS. No Major or mathematical
Minor issue was found.** This verdict is independent review of the actual
mathematical objects and proofs, not acceptance of an author/checker label.
The finite computation verdict is **implementation and finite assertion
verified in the stated range**. Optional optimization and scouting claims
outside the theorem certificate are expressly excluded below.

The authoritative statements reviewed are `general/refined_constants_proof.md`,
`general/refined_minus_one.md`, `general/square_root_barrier.md`, `joint/REPORT.md`,
and `four/R3_R4_REPORT.md`. Original inputs and the reviewed revisions are
identified by SHA-256 in the result files, manifest, and final seal.

| Item | Verdict | Exact scope |
|---|---|---|
| G1/G2 | PASS | Fixed-scale capacity induction and universal bound `[k(k-2)]^(2^(k-1))`, every integer `k>=5` |
| G3 | PASS | Uniform corollary `R_k(L)<=k^(2^k-2)`, every integer `k>=3`, with the two inherited small-color leaves |
| G4 | PASS | Sharper universal bound `[k(k-2)-1]^(2^(k-1))`, every integer `k>=6`, including separate `k=6,7` branches |
| G5 | PASS | Explicit first-level Golomb obstruction in completion-closed two-color regions, and separately stated conditional density implication |
| J literal sets | PASS | All three assigned 155-sets, each at exactly its stated predicate strength |
| J window certificate | PASS | All 8192 labeled supports; all 109 RUP refutations; all 334 literal colorings; complete containment coverage |
| J four cores | PASS | Reconstructed literal geometry, full CNF equality, and every RUP addition through the empty clause |
| J uniform families | PASS | All 51 and 46 corner equalities coefficient by coefficient, injectivity/order and positive steps on the entire stated parameter domains |
| F transfer and capacity | PASS | Actual residual span `L-h`, endpoint telescope, integer strict thresholds, and all 561 valid run witnesses |
| F final score | PASS | All 35999 score terms, recomputed correlations, and exact positive margin at `n=21991300` |
| Optional scan/sensitivity claims | Out of scope | No fresh exhaustive verification of all 111 outer parameters per distance, other candidate side lengths, fixed-parameter alternatives, or global optima |

## Independent reconstruction of G

The claim concerns integer color counts and corner-free colorings of actual
completion-closed regions inside a *fixed* square `[N]^2`. It does not replace
a sparse triangle by a square inferred from its cardinality. If a one-color
region had two same-diagonal points, their required completion would give a
monochromatic corner, proving the singleton base directly. For a monochromatic
source set `S`, the actual triangle `T(S)` omits its color and remains completion
closed. Its cells at distance `d` correspond injectively to pairs of `S` at that
distance. Partitioning those cells into the remaining colors and applying the
preceding capacity proves the integer cap

`V=(q-1) floor(c_(q-1) N^alpha_(q-1))`.

This is a positive integer at the ambient scales under consideration, including
when `S` itself is empty. Apply the accepted generalized Golomb estimate to this
integer first. Monotonic enlargement to `C N^alpha_(q-1)`, where
`C=(q-1)c_(q-1)`, is valid. Since `alpha_q=(1+alpha_(q-1))/2`, putting
`u=N^alpha_q` gives

`|S|/u <= sqrt(C) + C^(1/4)/sqrt(u) + 1/u`.

For the first coefficients, `b=k(k-2)>=3k`, `k>=5`, so
`N^(1/4)>= (3k)^4 >=16k^2`; hence `u>=256k^4`. The error is at most
`1/(16 k^(3/2))+1/(256k^4)<=1/(8k)`. Each summand is at most `1/(16k)`
for this range. The Golomb base `q=2` follows from
`z^2-16z-16>=1` at `z>=17`. The three small squared gaps for `q=3,4,5`
are positive. For `q>=6`, write `r=q-2`; the preceding coefficient is
`r^2-1`, while `(r-1/(2r))^2=r^2-1+1/(4r^2)` and the right side being
squared is nonnegative. Its spare `1/(2r)` exceeds the error because
`r<=k-3`. These arguments prove the induction for every admissible `q` and
every `k>=5`; finite arithmetic checks are supplementary.

For the sharper coefficients, `b=k(k-2)-1>=3k` for `k>=6`: at the lower
endpoint `k^2-5k-1=5`, and this polynomial increases thereafter. Thus
`N^(1/4)>= (3k)^8 >=16k^4`, and the error is at most `1/(8k^3)<=1/1000`.
The base absorbs its error using `z^2-100z-100>=1` for `z>=101`.
The five explicit coefficient comparisons cover `q=3,...,7`; only those
with `q<=k-1` are used. For `q>=8`, set `r=q-2`. Direct algebra gives

`(r-1/r)^2-(r+1)(r-1-1/(r-1))=1/r^2+2/(r-1)>2/r`.

Subtracting `e=1/(8k^3)` from the positive target leaves squared gap greater
than `2/r-r/(4k^3)>=2/k-1/(4k^2)>0`. The target minus `e` is positive.
This proves the entire tail, not a checked finite approximation to it.

I also rebuilt the partition coefficient. Writing `M_d` for the sum of
within-color pair counts and expanding all translated finite weight windows
gives `E=Na_0+2 sum a_d M_d` and total squared mass
`Na_0+2 sum (N-d)a_d`. Cauchy multiplies `E` by `k`. The bound
`M_d<=k V_*` introduces the second factor `k`, yielding exactly

`sum (N-d-k^2 V_*)a_d <= (k-1)Na_0/2`.

Nonnegative correlations are essential for that substitution and are present.
Unit weights of integer length `t` have `a_d=t-d`; their mass and first moment
are `t(t-1)/2` and `t(t^2-1)/6`. Dividing by `t/2` is legitimate and gives
the stated normalized contradiction margin.

For the first bound, the exact slack is `delta=1/45` at `k=5`, and
`delta=1/(k-2)^2` at `k>=6`. For `t=10k(k-2)^2`,
`N>=b^4>t`, and the normalized margin exceeds
`[k^5-(100/3)k^2](k-2)^4>0` throughout `k>=5`.
For the sharper bound the numerators of `delta` over `b^2` are `53/5`,
`194/5`, and `2k^2/(k-3)+4k+1` in the three stated branches. They exceed
one. With `t=2kb^2`, `N>=b^5>=t`; the margin exceeds
`kb^4(b-4k/3)>0`. These estimates correctly preserve every strict sign.

For the uniform corollary, induction gives `2^(k-1)>=(k-1)(k-2)` from
`16>=12`. The binomial inequality at positive increment `2/(k-2)` and
integer exponent `2^(k-2)` gives
`(k/(k-2))^(2^(k-2))>=k`. Squaring compares the first bound to
`k^(2^k-2)`. The separate inherited comparisons at `k=3,4` complete the
stated range. None of these inductions purports to establish a formula at
`k=1,2`, and no large-scale estimate is applied at `n=1`. Positive distance
`d=1`, short fibers, empty sets and singleton sets cause no exception.

For G5, equality of ruler differences first implies equality of index gaps:
the residue-difference discrepancy has absolute value at most `2p-2`, too
small to be a nonzero multiple of `2p`. Modulo the odd prime, invertibility of
`2t` then identifies both endpoints. The last mark is in fact
`2p^2-2p+1`, so a translated region fits at side `N=2p^2-2p+2<=2p^2`.
The weak-triangle coloring is completion closed. A color-one corner would
give two distinct equal differences; a color-zero corner cannot use two
distinct diagonal cells on its vertical edge. As odd primes are unbounded,
these examples rule out a uniform `o(sqrt(N))` two-color diagonal capacity
for these regions. They supply no simultaneous later-level extremizers.
The conditional density statement uses an integer strictly above
`exp((Ck)^(1/a))`; its logarithm is therefore strictly above the required
threshold. It imports no unproved density theorem.

CLAIM: First coefficient squared gaps | MY VALUE: 81/1600, 369/1600, 81/1600 | THEIR VALUE: 81/1600, 369/1600, 81/1600 | VERDICT: PASS | METHOD: Independent rational squaring of the displayed coefficients

CLAIM: Sharper coefficient squared gaps for q=3 through 7 | MY VALUE: 243/31250, 5761/1000000, 8641/1000000, 32401/1000000, 230401/1000000 | THEIR VALUE: 243/31250, 5761/1000000, 8641/1000000, 32401/1000000, 230401/1000000 | VERDICT: PASS | METHOD: Independent rational squaring before reading the saved exact-result comparison

CLAIM: k=5 side and normalized contradiction margin | MY VALUE: N=6568408355712890625; t=450; delta=1/45; margin=117793456512450969376/3 | THEIR VALUE: N=6568408355712890625; t=450; delta=1/45; margin=117793456512450969376/3 | VERDICT: PASS | METHOD: Exact partition summation at N=15^16

CLAIM: k=6 side and normalized contradiction margin | MY VALUE: N=37608910510519071039902074217516707306379521; t=6348; delta=53/2645; margin=68925828964323664149419624101576583553901223087/15 | THEIR VALUE: N=37608910510519071039902074217516707306379521; t=6348; delta=53/2645; margin=68925828964323664149419624101576583553901223087/15 | VERDICT: PASS | METHOD: Exact partition summation at N=23^32

CLAIM: Exceptional k=6 and k=7 deficit numerators | MY VALUE: 53/5 and 194/5 | THEIR VALUE: 53/5 and 194/5 | VERDICT: PASS | METHOD: Direct evaluation of b^2-k^2(k-1)c_(k-1)

## Independent reconstruction of J

The pinned inherited cap is the corrected *position-count* expression
`2 max{j:H_j<=464-d}`. It is not the mandate's superseded off-by-one
transcription. I reconstructed all increasing-pair counts using direct set
membership, and every progression by its endpoints. Each original set is
strictly increasing, has least mark one, is contained in `[464]`, and has
exactly 155 marks. The first witness has 22 small distances exceeding 45,
so its advertised obstruction to deriving the shave from the original
one-class predicates is valid. Its restrictions have 154 and 153 marks;
they do not establish the smaller-side surrogate.

For the window certificate, I built cells `(x,y)` with `x>y` from literal
supports and formed corners by joining horizontal cell pairs `(x,y),(z,y)`
and testing for the required cell `(z,y+z-x)`. Thus geometry was not read
from a cached corner list. I reconstructed both nonmonochromatic clauses
for every corner and the single color-interchange pin. The pin is complete
because interchanging both colors preserves every unpinned clause. Each
serialized CNF equals this reconstructed multiset exactly.

The new RUP checker represents positive and negative literals as separate
integer bit masks. For each proposed clause it negates all literals and
performs fresh unit propagation until conflict or a fixed point, then adds
the clause only after successful conflict. Every variable is checked against
the actual cell count; every proof ends with a verified empty clause. No SAT
library, producer, or supplied checker is imported or run. All 109 inlined
proofs also agree with their separate CNF/RUP files. Literal maximal-good
colorings were checked directly on reconstructed geometric corners.

Every one of the 8192 masks is contained in a verified good support or
contains a verified bad support, exclusively. I checked the antichains and
single-deletion/single-addition minimality and maximality against this full
classification. Thus restriction of colorings and inheritance of refutations
justify the entire coverage. The capacities for all widths through 13 are
then maxima over the fully classified masks, not separate solver outputs.
They imply minimum spans `6,7,9,10,12` for `6,7,8,9,10` marks, respectively.

Normalizing every minimal bad support by its minimum and positive gcd gives
exactly the 56-pattern catalog. Its reflection closure also checks. Positive
affine maps preserve corner incidence; reflection is induced by
`(X,Y)->(-Y,-X)` and also preserves the positive-step corner relation.
Both stronger assigned witnesses were checked against every affine copy of
every normalized pattern and against the complete AP5 uniqueness condition.
The AP5 geometric lemma itself has the correct dependency: two distinct
starts give an affine copy of the weak triangle on five indices, whose
translation by `(1,0)` is the independently exhaustively checked `T_6`.

For the two uniform families I labeled marks by their coefficient vectors in
`(x,h,b)` and rebuilt the source corner lists. Every horizontal step equals
its corresponding vertical step coefficient by coefficient. In the first
family, write `b=6h+u`; in the second write `b=4h+u`, with `h,u>=1`.
Every adjacent mark difference and every required corner step becomes a
nonzero nonnegative linear combination of `h,u`. Thus marks are distinct
and ordered, and all steps are positive throughout each stated domain.
The same fixed-label RUP proof applies uniformly; extra corners can only
strengthen the restrictions. I compared the resulting coefficient records
to both supplied coefficient-audit JSONs only after deriving them.

Direct block enumeration in a set and its reflection tests the first family
completely. Its minimum span is `11h+1`, so at side 464 only `h<=42` can
occur. The older window/AP5 witness has seven forward and four reflected
violations; the final parametric witness has none. The final witness contains
`{1,2,3,5,10,11,12,13,14}`, and hence the separately checked `core_v4`
refutation. This is the new second family at `x=1,h=1,b=9`; the final
saved YES does **not** satisfy that new premise and does **not** lift to a
completion triangle. The author's final scope statements are faithful.

CLAIM: Base literal witness checks | MY VALUE: 155 marks; 11935 increasing pairs; 463 valid caps; 21298 AP6 exclusions; maximum multiplicity 48; 22 of first 27 multiplicities exceed 45 | THEIR VALUE: 155 marks; 11935 increasing pairs; 463 valid caps; 21298 AP6 exclusions; maximum multiplicity 48; 22 of first 27 multiplicities exceed 45 | VERDICT: PASS | METHOD: Direct literal set intersections and independent endpoint enumeration

CLAIM: Complete window classification | MY VALUE: 8192 supports = 7147 good + 1045 bad; 109 minimal bad; 334 maximal good; 31605 RUP additions | THEIR VALUE: 8192 supports = 7147 good + 1045 bad; 109 minimal bad; 334 maximal good; 31605 RUP additions | VERDICT: PASS | METHOD: Fresh geometry, bit-mask unit propagation, literal colorings, and exhaustive containment coverage

CLAIM: Window capacities h(1) through h(13) | MY VALUE: 1,2,3,4,5,5,6,7,7,8,9,9,10 | THEIR VALUE: 1,2,3,4,5,5,6,7,7,8,9,9,10 | VERDICT: PASS | METHOD: Cardinality maxima over the fully certified support classification

CLAIM: Four core cell/corner/clause/RUP counts | MY VALUE: (36,55,111,151), (45,79,159,427), (45,51,103,1297), (36,46,93,157) | THEIR VALUE: (36,55,111,151), (45,79,159,427), (45,51,103,1297), (36,46,93,157) | VERDICT: PASS | METHOD: Literal geometry and complete fresh RUP verification

CLAIM: Both window/AP5 witness predicates | MY VALUE: 56 normalized patterns; 543170 affine exclusions per witness; 26680 AP5 occurrences in 115 step groups; zero violations | THEIR VALUE: 56 normalized patterns; 543170 affine exclusions per witness; 26680 AP5 occurrences in 115 step groups; zero violations | VERDICT: PASS | METHOD: Catalog reconstructed from certified minimal supports and every literal copy enumerated

CLAIM: Uniform family coefficient lifting | MY VALUE: all 51 first-family and 46 second-family identities vanish, with universal positive steps and strict mark order on their stated domains | THEIR VALUE: all 51 first-family and 46 second-family identities vanish, with universal positive steps and strict mark order on their stated domains | VERDICT: PASS | METHOD: Exact affine coefficient subtraction and positivity after b=6h+u or b=4h+u

## Independent reconstruction of F

A monochromatic diagonal set of actual span at most `L` in a three-color
completion-closed region has a distance-`h` completion fiber spanning at most
`L-h`. Splitting it by its two remaining colors gives two Golomb sets by
accepted FM1. Therefore the cap is exactly `2Q(L-h)` in span notation.
For a full-grid outer distance `d`, the relevant positions are `1,...,n-d`,
so the span is `L_d=n-d-1`. These two index conversions agree throughout.

The endpoint identity follows by telescoping each rank gap and then summing
over gaps. Overlap of the first and last endpoint blocks causes cancellation,
not a missing term. Distinctness gives each endpoint span at least `i` and
the correction `2 binom(c+1,3)` before doubling. Packing the rank-neighbor
distances into the allowed multiplicity multiset gives a lower bound on their
sum. For Golomb multiplicity one this doubled minimum is `H(H+1)`, so the
last integer span excluded is exactly

`floor((H(H+1)+4 binom(c+1,3)-1)/(c(c+1)))`.

The minus one is necessary and correctly placed. Thresholds are nondecreasing
in target size because every previously admissible `c` remains admissible and
its rank-neighbor count increases. I independently scanned all admissible `c`
for sizes 4600 through 4900, with an additional boundary at 4599. Every used
span lies above that boundary. Thus there is no omitted earlier threshold
affecting the selected caps. The nine used transition records and their
maximizer `c=68` agree exactly with the certificate.

For each of the 561 runs I rebuilt `H` at size `K+1`, then consumed the
literal capacities `2Q(L-h)` in increasing positive `h`, using a partial last
distance if needed. Every strict run comparison passes; the smallest margin
is 244. This certifies all larger sizes impossible for the chosen `c`.
As `d` increases within a run, the permitted multiplicities weakly decrease
and the span upper bound decreases. The packed lower sum can only increase
(or become impossible), so the longest-span witness certifies the whole run.
The run intervals cover every `d=1,...,35999` without gaps or overlap.

Correlations were recomputed using Newton finite differences of the quartic
`f(i)=i(t+1-i)(i+d)(t+1-i-d)`. Its five initial values determine the
quartic exactly. Summing its binomial-basis expansion uses
`sum_(i=0)^m binom(i,j)=binom(m+1,j+1)` and `f(0)=0`.
This independent route does not use the author's power-sum formula or the
other checker’s NTT/CRT implementation. The quartic identity was separately
symbolically simplified to zero and checked at exact points. Direct sums
validate every lag for small windows and extreme/interior lags of the actual
window. All 36000 correlations and all 35999 signed score terms are retained
in `F_exact_arrays.json`. The final positive margin contradicts accepted
FM2-4 and proves the stated upper bound.

CLAIM: Four-color certificate score | MY VALUE: a0=2015819151552432004800; doubled lhs=133542662853982446330820777152; doubled rhs=132991451122604993841474720000; margin=551211731377452489346057152 | THEIR VALUE: a0=2015819151552432004800; doubled lhs=133542662853982446330820777152; doubled rhs=132991451122604993841474720000; margin=551211731377452489346057152 | VERDICT: PASS | METHOD: Independent strict run packing, exact Newton-summed correlations, and all 35999 score terms

CLAIM: Four-color improvement | MY VALUE: 22006246-21991300=14946 | THEIR VALUE: 14946 | VERDICT: PASS | METHOD: Integer subtraction after certificate validation

## Dependencies, reproducibility and limits

The dependency graph is acyclic. G uses accepted completion closure and the
generalized Golomb estimate, then its own coefficient induction and the
partition identity; its corollary additionally uses the inherited specialized
small-color bounds. J uses accepted diagonal completion and the pinned H
table, then independently checked literal certificates; AP5 uniqueness uses
the separate elementary weak-triangle reduction. Window coverage supplies
rank restrictions downstream and does not depend on G or F. F uses accepted
FM1/FM2-4/FM3, the directly reconstructed endpoint identity, then its profile
certificate. No positive surrogate is used as a grid coloring, and no
uncertified solver negative is a proof leaf.

The relevant proof-audit, computation-audit and exact-verify skills were read.
The required exact-verify environment test returned `ENVIRONMENT OK` before
quantitative checking and in the sealed final run. The workspace has no
`.mathbox` ledger at the root or Round-3 directory. All reviewer writes are
under this directory. Author proof/certificate/checker programs were neither
imported nor executed. SymPy is used only for exact algebraic identities;
all verdict-bearing finite counts, packed sums and RUP propagation use
integers, rational fractions or Boolean operations. Elapsed times are metadata.

Reproduction from the project root:

```text
python research_round3/audits/fresh_astra/run_review.py
python C:/Users/ZhuanZ/.codex/plugins/cache/openai-curated-remote/mathbox/3.0.0/skills/computation-audit/scripts/validate_manifest.py research_round3/audits/fresh_astra/manifest.json --root .
```

The manifest validator passed as a legacy version-1 evidence record. That
schema does not by itself attest resource limits or enforce input hashes;
the wrapper separately hashes every input before/after its final run and
asserts equality. The manifest discloses this provenance limit. Original
inputs and output hashes are retained, as are actual subprocess commands
and logs. The four-color source certificate hash is
`7adbd5d660f735997213fbbef6c6d214e3b802cec4611259de600e7e42bd9562`.

Finite supplementary checks cover G scalar values `k=5,...,12`, ten literal
odd-prime rulers, 2448 partition-identity cases, and 1785 endpoint-identity
cases. Algebraic identities were simplified exactly and evaluated at exact
points including zero, one, and a large integer; denominator-zero points
were recorded as outside the identity's domain, not treated as failures.
The universal G theorem and parameterized J families have the separate
arguments given above. No bounded success is promoted to a universal proof.

The central G and F theorem statements in `report_general.tex` and
`report_four_final.tex` faithfully express the audited results. This review
does not verify unrelated sections of the full integration draft, historical
solver telemetry, the auxiliary `pattern_v1_600` / `ap5_600` snapshots, every
outer-parameter optimality claim, or the optional sensitivity table. These
items are not proof leaves for any bound passed here. Release still requires
the other assigned independent reviewer and root integration checks.

There is no remaining mathematical gap in an assigned load-bearing claim.
The strongest safe conclusion is the stated G bounds, the precisely scoped
J finite and uniform obstructions, and `R_4(L)<=21991300`, with the inherited
three-color interval unchanged. No further computation is required by this
review; the next step is to combine the independent reviewer verdicts.
