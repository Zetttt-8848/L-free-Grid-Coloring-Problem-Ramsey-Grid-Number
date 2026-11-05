# Research checkpoint R4-RESEARCH-0040

Continuation of CHECKPOINT_0039.md. The preceding turn was progress:
it completed positive-fan and weak-source support structure and a
sharp four-cycle construction. This turn also makes progress. Root
derived a stronger energy theorem for two Golomb classes, improved
the completed product-class estimates, obtained a positional internal
reflection budget, and proved that the sharp single-output reflection
coefficient persists under actual weak coloring.

The full research objective remains active and incomplete. The working
bounds are still 21<=R3<=465 and R4<=21991300. The attributed general
growth theorem is complete and unchanged. The uniform strict-source
S21, EP10, H10, dyadic D(7/5), finite R3 capacity, and original method
with new small-color bounds remain open. Withhold the user's results
summary until all objectives are achieved. There is no external blocker.

All three auxiliary tasks have returned terminal results. No new SAT
or old solver replay was requested in this turn. The auxiliary mixed-
deficit counterexample is saved as explicit difference and incidence
tables, not a solver theorem. No separate audit, review, formalization,
or reset credit was used. The root advances derivations; the user will
undertake later verification.

## 1. Root: H2 for every union of two Golomb sets

TWO_GOLOMB_MIXED_ENERGY_0040.md proves, for disjoint integer Golomb
sets B,C, n=|B|+|C|, M=binom(n,2),

    T(B union C)<=2M,
    E(B union C)<=6n^2-5n.

This supersedes the former E<=8n(n-1) and H3 input for this class.
It applies in particular to every proper weak two-color source and
to every actual weak fiber of a proper strict source. It does not
assert that a general proper strict source is a union of two Golomb
sets; that premise is false in the known large constructions.

For d>0, let beta_d,gamma_d indicate the within-class differences,
and let x_d,y_d count oriented B->C and C->B mixed pairs. Define

    rho=|Delta B intersect Delta C|,
    N=sum_d(beta_d+gamma_d)(x_d+y_d),
    Q=sum_d x_d y_d.

The inherited same-orientation collision bijection is reexpressed in
the derivation to give the exact decomposition

    T=2rho+N+Q.

The first budgets are 2rho<=binom(b,2)+binom(c,2), N<=2bc. The new
joint resource count is

    Q<=binom(b,2)+binom(c,2).

An opposite-orientation mixed collision matches an unordered B-pair
sum with a C-pair sum. Each class has unique unordered pair sums,
including repeated marks. A match of two distinct pairs contributes
two to Q and uses two distinct-pair resources, one in each class.
A repeated-mark match contributes one to Q and uses the distinct
pair on the other side. Both sides cannot be repeated because B,C
are disjoint. Each resource is used at most once. The three budgets
sum to T<=2M; the full derivation includes all repeated-mark cases.

An intermediate separate estimate N<=2bc-min(b,c) was refuted by
fibers/TWO_GOLOMB_MIXED_DEFICIT_0040.md:

    B={0,2,5,6}, C={1,3,4,8}, N=29>28.

Root's theorem uses N<=2bc and the stronger joint Q budget, so it
does not depend on repairing that false estimate. The counterexample
note has an appended continuation recording this distinction.

## 2. Root: sharper complete-product consequences

PROGRESSION_PRODUCT_REFINEMENT_0040.md improves the complete no-carry
progression class A=B+Q{0,...,t-1}, Q>2span(B), t>=2:

    T(A)<=7M(A)/2, M(A)<=8span(A).

The actual overlap F_Q=B+Q{0,...,t-2} is a union of two Golomb sets.
Using the existing factorization E(B+QP_s)=e_s E(B), with
e_s=s(2s^2+1)/3, and the new energy bound gives, n=t|B|,

    E(A)<=lambda_t n^2-5R_t n,
    R_t=(2t^2+1)/(2(t-1)^2+1),
    lambda_t=6(t-1)R_t/t.

The complete polynomial calculation proves this is at most
9n^2-8n, including the singleton overlap. Subtracting the exact
energy identity yields H7/2. This improves the earlier H5/M<=11L
on that complete class, not the uniform research target.

DIRECT_SUM_REFINEMENT_0040.md improves arbitrary complete no-carry
two-factor sources A=B+QC with both factor sizes at least two:

    T(A)<=7M(A), M(A)<=15span(A).

It reuses the actual weak overlap partitions and completed finite
rectangle restrictions from PROPER_DIRECT_SUM_ENERGY_0028.md, with
the new E<=6r^2-5r input. The only new small-factor observation is
that equality T(S)=binom(|S|,3) forces S to be an arithmetic
progression: every index triple (1,2,k) must come from a corner,
so all nonminimal marks have a predecessor at the first gap.
Proper six-mark factors exclude that progression and have T<=19,
E<=142. A full factor-size case calculation gives E(A)<=16n^2-15n.
No optimal six-mark energy or new finite solver result is assumed.

The previous class theorems remain valid inputs, now with these
stronger successors. Full products, all layers, and difference
separation remain essential. These results do not cover arbitrary
incomplete supports or justify filling missing marks.

## 3. Root and auxiliary: reflection multiplicity and its positional sum

fibers/GOLOMB_REFLECTION_MULTIPLICITY_0040.md fixes r outside a
Golomb B and counts a<t<q in B with r=a+q-t. It proves

    mu_B(r)<=min(|B<r|,|B>r|)<=floor(|B|/2).

Both extremes are injective: a fixes q-t=r-a, and q fixes t-a=q-r.
The extremal pairs form a matching; the whole triples need not.
An explicit six-mark equality example has a three-cycle in the
triple quotient. An infinite power-separated path family attains
floor(|B|/2), with a formal-difference derivation of Golombness.

WEAK_REFLECTION_POSITION_BUDGET_0040.md sums the positional bound
across disjoint Golomb classes B,C and proves

    K=sum_(r in C) mu_B(r)+sum_(r in B) mu_C(r)
      <=floor(bc/2).

Pair symmetric ranks of each class into nested open intervals. At
each output the min(left,right) bound counts how many rank intervals
contain it. A pair of B/C intervals has at most two endpoint-inside
incidences. Accounting for unpaired medians gives exactly floor(bc/2).
This improves the coarse bc capacity for this internal-triple
inventory. It does not include reflections outside the triple hull.

At an actual opposite-color output r in a proper weak source, each
B triple forces both z(r,a) and z(q,r) to the B color. Root also
proves a universal one-point weak extension: for ANY Golomb B and
ANY r outside it, color B diagonals +, the r diagonal -, strict
B-cells -, and strict r-incident cells +. At positive offset two
- endpoints would repeat a B difference; two + endpoints can only
be (r,r-d),(r+d,r), whose completion is a - B-cell. The diagonal
case is immediate. Thus this is always a proper weak coloring.

Applying it to the equality families shows that even actual weak
properness cannot improve the coefficient 1/2 at a single output.
Further gain must couple several outputs or use span. The auxiliary
multiplicity note has an appended pointer to this completed root
extension and the positional sum.

## 4. Cross-anchor supported-difference constraints

fibers/WEAK_ANCHOR_OVERLAP_0040.md uses the supported D_a from
WEAK_SOURCE_SUPPORTED_DIFFERENCES_0039.md. For same-color diagonal
anchors a<a', delta=a'-a, if h belongs to both D_a,D_a', the actual
offset-h cells have the same color, forcing their completion at
(a'+h,a) opposite. Therefore

    D_a intersect D_a' intersect (D_a-delta)=empty.

For an output r in the other diagonal class and its supported anchor
set A(r), every pair a<a' gives r-a' not in D_a. The corresponding
potential cell (r-a'+a,a) is either unsupported or forced to the
opposite color. This charge is injective for fixed r, producing
binom(|A(r)|,2) exclusions.

Reuse across outputs is explicit. The reuse set for fixed a,h is

    E_(a,h)={a'>a:h in D_a', h+a'-a in D_a}.

It injects into D_a, has h not in D_a when nonempty, and satisfies
Delta E_(a,h) intersect D_a=empty. These conditions do not constantly
bound reuse. The new H2 theorem for weak sources does not make these
per-output exclusions disjoint or fill absent supports.

## 5. Unit-shift weak sources and adjacent ruler differences

fibers/UNIT_SHIFT_ADJACENT_DIFFERENCES_0040.md treats only
S=P disjoint union (P+1), P Golomb with no difference1, with prescribed
diagonal colors 0 and1 on the copies. It retains alpha_p=z(p+1,p),
u_pq=z(q+1,p), and v_pq=z(q,p+1), while the same-copy cells are
forced 1 and0. For adjacent ruler differences q-p=d, s-r=d+1,
the direct positive-corner derivation gives

    p<r => z(s+1,p)=1,
    r<p => z(q+1,r)=0.

The note retains the intermediate shared-cell implications and the
alpha-pair rule. It charges adjacent-difference pairs to these actual
forced cross cells with multiplicity at most two, using unordered
pair-sum uniqueness to recover the inner endpoints. The two order
types cannot share a physical target since they force different
colors. The total target-cell universe is still quadratic, so no
linear adjacent-difference count or corrected product-span theorem
follows. Do not broaden this prescribed-copy hypothesis to arbitrary
weak sources.

## 6. Narrow source comparison and next central implication

literature/REFLECTED_HOLE_INPUT_MAP_0040.md retrieves at most six
relevant prior inputs; it locates no existing one-point Golomb
extension theorem in the local source collection. The direct
extension above is proved without an external input.

literature/TWO_SIDON_ENERGY_COMPARISON_0040.md records a bounded
primary-source search for the exact two-class energy coefficient.
No matching primary theorem was located in the two focused query
batches. The single-Sidon energy literature supplies terminology,
not this bound. The harmonic-analysis theorem that a union of two
Sidon sets is Sidon uses another definition and does not transfer.
This is only a scoped retrieval outcome, not a novelty claim.

Root still owns the uniform finite-source and small-color
breakthrough. The next useful use of the new energy budget must
retain shared colors or geometry across several weak fibers; an
overlap-only generalization is already ruled out by earlier
constructions. The weak cross-anchor exclusions and positional
reflection budget are actual additional structures, but their
missing-support reuse remains unclosed. The endpoint P/Y/Delta
system from 0039 remains available with every defect retained.

Do not revive the refuted isolated N deficit, the single-output
coefficient improvement, or the four-cycle-free support graph.
Reuse the stronger class estimates as inputs and continue toward
the unchanged full objective without a results summary.
