# Independent review of Round-3 cores C and L

## Review metadata

| Field | Value |
|---|---|
| Sub-Task ID | `R3-F6-C-L-SETUP-SOL` |
| Assigned model | GPT-5.6 Sol, xhigh, Level 2 |
| Assignment | Author-independent review of cores C and L |
| Reviewer relation | Reviewer did not author either assigned core |
| Primary result | **PASS** on every scoped claim; no Minor or Major issue |
| Side-21 result | **UNDECIDED**, correctly stated by the author |
| Confidence | High for every finite and algebraic claim in scope |
| Dependencies | Inherited corner geometry and Golomb table; the window-13 `ell` table is an explicit accepted dependency and was not re-enumerated here |
| Independence | Fresh code; no author checker/generator was imported or run; no other reviewer result or code was consulted |

The normalized verdict is: the AP5, endpoint-neighbor, and ordered-overlap
lemmas are **proved as written**; the ruler-pair certificate is
**computationally verified exactly for its stated 60-configuration family**;
the side-21 CNF, cube cover, and 33 scoped unit contradictions are verified;
the 48 remaining cubes have no deciding certificate, so the global side-21
question remains **UNDECIDED**.  The hypothetical 45/46 profile calculations
are exact conditional implications and do not prove either cap premise.

## Claim cards and dependency graph

### C1. Five-term progression uniqueness

**Claim.** If `A` is a monochromatic slope-one diagonal coordinate set in a
corner-free three-color square, then for every positive step `a` at most one
five-term progression of step `a` lies in `A`.  Equivalently, for each positive
`d`, `F_d={u:u,u+d in A}` contains no five-term arithmetic progression.

**Dependencies.** Two such progressions -> a weak triangle `W5` of completion
points -> all 15 points avoid the source color -> a binary coloring of `W5` ->
a monochromatic corner.  The last implication was checked directly on all
`2^15=32768` binary assignments, so the review does not need to import the
inherited `T6` computation.

### C2. Endpoint-sensitive neighbor inequality

**Claim.** For integer marks `a_1<...<a_s`, `1<=c<s`, and valid block-span
bounds `ell_i`, the collected rank-neighbor sum satisfies

`T_c = sum_{i=0}^{c-1}(c-i)(a_{s-i}-a_{i+1})`

and

`T_c <= L*c(c+1)/2 - 2*sum_{i=0}^{c-1}(c-i)ell_i`.

Together with multiplicity caps, `M(H)>upper`, where
`H=cs-c(c+1)/2`, excludes `s` marks.

**Dependencies.** Telescoping identity -> two endpoint block spans -> cap
multiset lower bound.  The actual `n=464` conclusion uses the inherited caps
and distinct integral marks.  The `n=454` and partial-46 conclusions also use
the separately reviewed window-13 spacing table.

### C3. Literal ruler-pair forcing certificate

**Claim.** Every disjoint translate or reflected translate in the specified
family formed from the two literal order-23 and order-24 rulers has no binary
coloring of its complete weak triangle extending the two diagonal colors.

**Dependencies.** Literal ruler arrays -> independent enumeration of all
admissible transformations -> diagonal seed colors -> each cited corner makes
one Boolean unit implication -> final monochromatic corner.  This is a finite
claim about two fixed rulers.  It is not a theorem about every near-extremal
Golomb ruler.

### C4. Ordered overlap identity and bounds

**Claim.** For `d<e`, `Delta=e-d`,
`C=B_d intersect B_e`, and `D=B_e intersect (B_d-Delta)`,

`|Q_d intersect Q_e| = sum_{q in D} |{u in C:u<q}|`.

The stated `X,Y` containments give the three cap bounds; the binomial, ordered
`J`, and cap-square upper bounds imply the quoted Cauchy lower bound.

**Dependencies.** Equality of two ordered output coordinates -> the `C,D`
bijection -> `C subset X`, `D subset Y` -> elementary injections into the
three difference fibers -> Cauchy.  Color and Golomb facts enter only the
later interpretation of the output union, not the set identity.

### L1-L4. Side-21 encoding, cubes, scoped contradictions, and circulants

**Claims.** The DIMACS file exactly encodes three-color corner-free matrices
with the stated sound color normalization; the 81 cubes are a disjoint cover;
exactly 33 cubes contradict by unit propagation; the other 48 stored records
are their unresolved complement; and the difference-circulant family has
maximum possible side 3, attained by the stored matrix.

**Dependencies.** Geometric definition -> fresh one-hot/corner clause
reconstruction -> sound residual color swap -> cube restriction of four
one-hot cells -> direct unit propagation.  The unresolved solver telemetry is
not a negative certificate.  The circulant ceiling has a direct universal
argument independent of the side-21 computation.

## Decisive proof checks

### AP5 weak-triangle geometry

Suppose the two starts are `x` and `x+d`, with `a,d>0`.  For
`0<=i<=j<=4`, use the two source diagonal points indexed by
`x+i*a` and `x+d+j*a`.  Their positive separation is
`d+(j-i)*a`, so their completion point is

`Q_ij=(x+j*a+d+sigma, x+i*a)`.

Both coordinates lie between source endpoints, and each `Q_ij` avoids the
source color.  The map `(j,i) -> Q_ij` applies the same positive scale `a` in
both coordinates and a translation vector, hence preserves every positive
corner.  Its domain is exactly
`W5={(j,i):0<=i<=j<=4}`.  Translation by `(1,0)` maps `W5` bijectively to
`{(r,s):0<=s<r<=5}`.

The fresh enumerator found 15 points and 20 corners, exhausted all 32,768
binary assignments, and found zero corner-free assignments.  The smallest
number of monochromatic corners among those assignments is one.  Thus the two
AP5s are impossible.  Conversely, an AP5 `x,x+a,...,x+4a` in `F_d` supplies
the two source AP5s at starts `x` and `x+d`, proving the stated equivalence.

For the auxiliary linear encoding, a fully occupied AP forces its auxiliary
`y` to one through `sum x_i <= 4+y`; the fixed-step sum `sum y<=1` therefore
forbids two full AP5s.  Conversely, set `y=1` exactly for a full AP5.  At
`n=464`, the exact number of AP5 occurrences is

`sum_{a=1}^{115}(464-4a)=26680`,

in 115 fixed-step groups.

### Endpoint telescoping and arithmetic

For fixed `j`, cancellation gives

`sum_{h=1}^{s-j}(a_{h+j}-a_h)
 = sum_{i=0}^{j-1}(a_{s-i}-a_{i+1})`.

This equality is an equality of formal sums and remains valid when the two
endpoint lists overlap.  Summing `j=1,...,c` gives coefficient `c-i` on the
`i`th endpoint difference.  Also

`a_{s-i}-a_{i+1}
 = (a_s-a_1)-(a_{i+1}-a_1)-(a_s-a_{s-i})
 <= L-2ell_i`.

The `H` collected distances use any positive distance at most its cap, so
their sum is at least the sum `M(H)` of the `H` smallest entries in the cap
multiset.  This proves the exclusion criterion.  For distinct integer marks,
`ell_i=i` and the total subtraction is
`2*sum_i(c-i)i=2*binom(c+1,3)`.

Fresh direct evaluation on every subset of `{0,...,9}` of size at least two
and every legal `c` checked 4,097 identities and inequalities.  The exact
load-bearing witnesses are:

| Status | `n,s,c` | `H` | `M(H)` | endpoint upper | margin |
|---|---:|---:|---:|---:|---:|
| Actual inherited caps, hence `s<=158` | `464,159,13` | 1976 | 41676 | 41405 | **271** |
| Conditional cap 45 through 27 + window table | `454,152,11` | 1606 | 29414 | 29390 | **24** |
| Conditional cap 46 through 27, first 3 at 45 + window table | `464,155,10` | 1495 | 25110 | 25091 | **19** |

The source-position convention was independently checked: a difference `d`
leaves `n-d` source positions, whose span is `n-d-1`; therefore the cap uses
`q(n-d)`.  At `n=464`, the inherited cap is 48 at `d=38` because
`464-38=426=H_24`, and 46 at `d=39`.  The last distances used by the three
rows are respectively 42, 36, and 33.  The conditional rows prove only the
displayed implications.  This review makes no claim that either hypothetical
profile follows from the grid geometry.

### Ruler-pair certificate

The two literal rulers have respectively 253 and 276 positive differences,
all distinct.  I regenerated every shift `1<=h<=462-span` of the second copy,
both reflected and unreflected, then retained exactly the copies disjoint from
the first ruler.  This produced 60 configurations: 42 of order 23 and 18 of
order 24; four are unreflected and 56 reflected.  Their key triples
`(order,reflected,shift)` and every union `F` match the certificate exactly.

For each case I initialized `(z,z)` to color 0 on the first ruler and color 1
on the transformed ruler.  Each of the 16,425 stored steps was then checked
from its three literal coordinates: it is a positive geometric corner in
`{(x,y):x,y in F,y<=x}`, the claimed point was previously unassigned, and the
other two points were already assigned the opposite common color.  Each step
is therefore a valid forced assignment.  Every final cited corner is valid,
assigned, and monochromatic.

Direct AP5 counting found 59 AP5-free unions.  In particular, the order-24
reflected copy at shift 2 has 48 points, span 427, zero AP5s, and a valid
192-step contradiction.  These results establish the complete stated literal
family and do not generalize to unlisted rulers.

### Ordered overlap

Write an element of `Q_d` as `(v+d,u)` with `u<v` in `B_d`, and an element of
`Q_e` as `(q+e,p)` with `p<q` in `B_e`.  Equality forces `p=u` and
`v=q+Delta`.  Hence `u in C`, `q in D`, and `u<q`.  Conversely those three
conditions give the two valid source pairs and the common output `(q+e,u)`.
That output recovers `(u,q)`, so this is a bijection.

For `X={u:u,u+d,u+e in A}`, clearly `C subset X`.  For
`Y={q:q,q+Delta,q+e in A}`, `D subset Y`.  The sets `X` and `Y` inject into
each of the `d`, `e`, and `Delta` difference fibers, using a translation for
the side not based at their displayed start.  Thus both sizes are at most
`min(r_A(d),r_A(e),r_A(Delta))`.  Containment in either single `Q` supplies
the two binomial bounds.  This proves O1 and O2.  Applying Cauchy to output
multiplicities gives O3 whenever `M>0`; the statement correctly excludes
division at `M=0`.

The fresh finite check enumerated every source subset for `1<=n<=7`, every
`d<e`, and every independent choice `B_d subset F_d`, `B_e subset F_e`:
26,104 cases, with total intersection size 3,491.  O1, both containments, all
four O2 bounds, and the two-set Cauchy inequality passed in every case.

For the saturation witness `A={1,4,8,14,18,21}`, `d=3`, `e=7`,
`B_d={1,18}`, `B_e={1,14}`, the independent computation gives
`C={1}`, `D={14}`, and `Q_d=Q_e={(21,1)}`.  Hence `M=2`, `O=1`, the union has
size one, and the Cauchy lower bound is exactly one.  The claimed obstruction
is therefore saturated.

### Side-21 CNF and cube package

I rebuilt the instance directly from
`X[x,y,c]=3*(21*x+y)+c+1`.  Each of 441 cells contributes one ternary
at-least-one clause and three binary at-most-one clauses.  Direct enumeration
of `1<=d<min(21-x,21-y)` gives
`sum_{m=1}^{20}m^2=2870` geometric corners, each contributing three negative
ternary clauses.  The exact counts are:

| Item | Count |
|---|---:|
| Variables | 1323 |
| Cell clauses | 1764 |
| Corner clauses | 8610 |
| Clauses before symmetry | 10374 |
| Symmetry clauses | 441 |
| Total clauses | 10815 |

The reconstructed clause multiset equals the parsed DIMACS multiset exactly;
all clauses are unique and all literals are in range.  The file SHA-256 is
`49a989044d4255e7aba75a0b45256a7b480172b8f121545eeaf350164177f8e5`.

The symmetry consists of fixing the first cell to color 0 and 440 clauses
forbidding color 2 before a prior row-major color-1 occurrence among the
remaining cells.  Given any coloring, permute its first-cell color to 0.  If
one or both residual colors occur, swap their names so the earliest occurring
residual color is 1; if neither occurs, either naming works.  This proves that
every color orbit retains a representative.

The split cells are `(0,1),(1,0),(1,1),(20,20)`.  The stored tuples are exactly
all 81 elements of `{0,1,2}^4`, and each positive literal matches the stated
cell/color.  Every total one-hot assignment therefore selects exactly one
cube, while two different tuples are incompatible at a differing split cell.

A fresh occurrence-list unit propagator processed the full CNF under every
one of the 81 cubes.  Exactly the following 33 orders reached contradiction:

`1,2,8,9,18,21,24,25,27,29,30,34,35,37,42,43,44,45,46,47,48,49,53,55,59,62,65,68,69,75,77,79,80`.

This set matches the 33-record easy manifest exactly.  The 48 hard portfolio
records are the exact set complement, with unique orders and matching
assumptions; every one says `INTERRUPTED_UNDECIDED` and has no proof path,
proof hash, or witness.  The global audit's `33+48=81` accounting is correct.
Because 48 disjoint cubes remain without a certificate, the side-21 instance
is not decided by this package.

### Difference-circulant family

For `chi(x,y)=f((y-x) mod m)` and any `0<=i<j<n`, the valid corner
`(i,0),(j,0),(j,j-i)` has residues `-i,-j,-i`.  Corner-freeness forces
`f(-i)!=f(-j)`.  Thus the `n` values `f(0),f(-1),...,f(-(n-1))` are pairwise
distinct in a three-element codomain, so `n<=3`.  Repeated residues make the
required inequality self-contradictory and are already covered.

The stored `n=m=3` matrix is exactly `f(r)=r+1`.  Fresh enumeration checked all
five geometric corners and found zero violations.  This proves equality only
inside the difference-circulant family and has no general Ramsey-bound effect.

## Three-step hostile checks and verdicts

| Item | Definitions and quantifiers | Boundary/adversarial check | Verdict |
|---|---|---|---|
| C1 AP5 | `a,d>0`, `i<=j` makes every completion step positive | overlapping source AP5s do not identify `Q_ij`; all 32,768 W5 assignments exhausted | **PASS** |
| C2 endpoint | `1<=c<s`; endpoint blocks may overlap | `s=2,c=1`, all small integer mark sets, source-position off-by-one checked | **PASS** |
| C3 pair forcing | Complete weak triangle on exact literal unions | all allowable shifts/reflections regenerated; repeated or unjustified assignments rejected | **PASS** |
| C4 overlap | `d<e`, so `Delta>0`; ordered pairs retain `u<q` | empty fibers and `M=0` handled; saturated two-fiber witness checked | **PASS** |
| L1 CNF | exact orientation and zero-based literal map | full clause multiset reconstructed, rather than sampled | **PASS** |
| L2 cubes | every four-cell color tuple present once | one-hot clauses prove disjointness and total restriction proves coverage | **PASS** |
| L3 easy/hard | direct UP on all 81 cubes | exact 33/48 complement; interruptions not promoted | **PASS**, global result **UNDECIDED** |
| L4 circulant | arbitrary `m` and total `f` | repeated residues included; equality matrix checked directly | **PASS** |

No Minor or Major issue was found.  The only execution correction was the
reviewer's initial use of the wrong JSON collection key for the cube manifest;
it was halted before an L verdict and is recorded in `R10.md`.

## Computation contract and provenance

The finite surrogate was exact integer and Boolean evaluation of: all W5
binary assignments; all certificate configurations and trace steps; all
overlap cases through `n=7`; three named endpoint witnesses; the complete
side-21 clause and cube data; direct unit propagation on all 81 cubes; and all
five corners of the side-3 matrix.  A pass validates those finite assertions.
It cannot prove the hypothetical cap profiles, settle any hard cube, extend
the two-ruler conclusion to arbitrary rulers, or re-certify the imported
window-13 table.

The reproducible command is:

`python research_round3/audits/setup_sol/independent_audit.py`

It ran under Python 3.13.5 on Windows AMD64 in 1.702646800000366 seconds,
with no randomness.  The exact-verify self-test printed `ENVIRONMENT OK`.
The result SHA-256 is
`142aef77f12f65e780d51c52cd1162fff02e4674f7f6e37bc87d1dbb145c66f0`.
All source hashes, bounds, non-claims, and environment details are in
`computation_manifest.json`; the installed mathbox manifest validator accepts
it as a valid legacy version-1 evidence record.  This workspace did not expose
a repository revision to the run, so provenance rests on the recorded exact
input and output hashes rather than a commit identifier.

## Exact-verification verdict lines

CLAIM: W5 has no binary corner-free coloring | MY VALUE: 0 among 32768 assignments | THEIR VALUE: 0 | VERDICT: PASS | METHOD: fresh enumeration of all 15-point assignments and 20 literal corners

CLAIM: the ruler-pair certificate covers 60 cases and 16425 valid forcing steps | MY VALUE: 60 cases, 16425 steps, 59 AP5-free unions | THEIR VALUE: 60, 16425, 59 | VERDICT: PASS | METHOD: regenerated transformation family and replayed every literal implication

CLAIM: inherited endpoint caps at n=464 imply size at most 158 | MY VALUE: H=1976, M=41676, upper=41405, margin=271 | THEIR VALUE: same | VERDICT: PASS | METHOD: exact cap multiset with q(n-d) and c=13

CLAIM: conditional 45 profile closes n=454 | MY VALUE: H=1606, M=29414, upper=29390, margin=24 | THEIR VALUE: same | VERDICT: PASS CONDITIONAL | METHOD: exact arithmetic using the named window-13 ell dependency

CLAIM: conditional 46-through-27 plus first three at 45 closes n=464 | MY VALUE: H=1495, M=25110, upper=25091, margin=19 | THEIR VALUE: same | VERDICT: PASS CONDITIONAL | METHOD: exact arithmetic using the named window-13 ell dependency

CLAIM: ordered-overlap finite audit has 26104 cases and summed intersection 3491 | MY VALUE: 26104 and 3491 | THEIR VALUE: same | VERDICT: PASS | METHOD: fresh exhaustive enumeration from source subsets and independent fiber subsets through n=7

CLAIM: side-21 CNF has 1323 variables, 2870 corners, and 10815 clauses | MY VALUE: 1323, 2870, 10815 | THEIR VALUE: same | VERDICT: PASS | METHOD: fresh clause reconstruction and exact DIMACS multiset comparison

CLAIM: exactly 33 easy cubes contradict by unit propagation and 48 remain unresolved | MY VALUE: 33 contradictory, 48 exact unresolved complement | THEIR VALUE: same | VERDICT: PASS | METHOD: fresh direct unit propagation on all 81 cubes and independent record reconciliation

CLAIM: the side-21 package decides existence or nonexistence | MY VALUE: it does not; 48 cubes lack proof or witness | THEIR VALUE: UNDECIDED | VERDICT: PASS | METHOD: certificate-coverage audit
