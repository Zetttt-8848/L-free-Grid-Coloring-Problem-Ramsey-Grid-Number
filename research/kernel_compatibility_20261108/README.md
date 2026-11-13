# New count: Six types of completion grids share a starting point, pushing the upper bound to 464

Date: 2026-11-08. based on`654cc044cad3d8ca6079a1931565a6ec44dcf2b5`(PR5). This round focused on inventing the upper bound counting method according to the direction specified by the user; no new lower bound SAT search was carried out.

Proof of this round **`R3≤464`**, the project interval is updated to **`21≤R3≤464`**. Different from the previous round of restoration of historical 465 proofs, this advancement comes from the newly added common occupancy count. The new derivation is a combinatorial proof; numerical applications still use the verified external Golomb span lower bound`G(24)≥425,G(25)≥480`, the two external exhaustive results were not reproved or rerun.

## What changes have occurred to the counting object?

The old count estimates differential fibers separately for each main diagonal color and then sums the three upper bounds. This allows fibers of different colors to reuse the same earliest positions in estimation.

New counts retain both color labels. For each step size d, define

```math
B_{c,b}(d)=\{u:\chi(u,u)=\chi(u+d,u+d)=c,\ \chi(u+d,u)=b\},\qquad b\ne c.
```

There are six actual sets. They are both Golomb sets, and no two of them intersect. A 24-mark set requires a span of at least 425, so its smallest point can only occupy the first p−425 positions out of p available positions. Different sets cannot share this minimum point.

Sort the non-empty set by the smallest point to get a more general common occupancy count:

```math
R_d=\sum_{c\ne b}|B_{c,b}(d)|\le\sum_{j=0}^{5}g(n-d-j),
```

where g(p) represents the maximum size of the Golomb set in p consecutive positions. The old upper limit is 6g(n−d). The two are strictly different at the Golomb capacity jump:

| Available positions p | 426 | 427 | 428 | 429 | 430 |
|---|---:|---:|---:|---:|---:|
| Estimate six categories separately | 144 | 144 | 144 | 144 | 144 |
| Common minimum point count | 139 | 140 | 141 | 142 | 143 |

[Complete geometric derivation](geometry/SIX_CLASS_LEMMA.md)It is proved why the six categories do not intersect, why they are Golomb sets, and how to deal with empty categories, overlapping point pairs and span endpoints. This constraint handles co-location competition that is missed by the old count.

## How it produces actual numerical improvements

Let the new upper limit be U(n−d). The three-color principal diagonal indicates that the sum of the functions is equal to the entire diagonal, so counting sums of squares gives the necessary inequality

```math
\sum_{d>0}(n-d-3U(n-d))a_d\le na_0,\qquad
a_d=\sum_i w_iw_{i+d}.
```

Pick`n=464`,`w_i=i(86−i)`(i=1,…,85). The autocorrelation coefficient has an explicit quintic polynomial formula, and the sum of all integers can be calculated directly:

| Counts under the same weight | Left side minus right side |
|---|---:|
| Old independent capacity | −2,799,639,872 |
| New common space capacity | **477,965,143** |

Positive numbers contradict necessary inequalities. So the improvement does come from new counts, not just replacing weights. [Complete algebraic proof](kernel_upper/README.md)Gives formulas and piecewise sums; [Independent review](review/REVIEW.md)It is deduced separately from the actual grid point reconstruction.

## New count for the second layer: sharing the same set of colors with different sync sizes

The minimum point also has the original diagonal color c, and each c has only two completion color labels. Let k=max(0,n−d−425), and let m_c(d) count the first k point pairs in the starting point and the diagonal color at both ends are c, then

```math
R_d\le138+\sum_c\min(2,m_c(d)).
```

m_c with different d are not independent variables, they come from the same boundary color word. The comparison edges of two adjacent layers form an alternating path. If the path uses r colors, the number of single-color edges is at most 2k-r; each color contributes up to 4 counting units in the two layers. therefore

```math
t_{k-1}+t_k\le\max_{1\le r\le3}\min(4r,2k-r).
```

This gives a common budget across strides. Combining three such constraints with non-negative weights adds another 721,186,665 inconsistencies to the 464 certificate, but does not yet lower the integer upper bound to 463. [Combined Counting Work Package](combinatorial_upper/THEOREM.md)Give purely combinatorial proofs, exact numerical values, and unfinished continuations.

Limited experiments with boundary word lengths 5 to 9 support stronger enumerations; these enumerations do not serve as premises for Theorem 464. The weighted experiment of length 9 still leaves a negative difference of −161,570,116 at 463, and it cannot be claimed that 463 is established based on this.

## Verification, Provenance and Innovation Boundaries

- The main conclusion has a complete combinatorial proof, two independent integer implementations and a review by a new reviewer starting from the definition. The calculation is used to check identities and find candidates without using SAT unsatisfiability or floating point infeasible state proofs 464.
- The small example verification covers all 59,049 fourth-order weak triangle shading assignments, as well as a Golomb example in which the common occupancy upper limit is strictly better than the independent upper limit and can be obtained. They test realization, and universal propositions are undertaken by written proofs.
- The Golomb Ruler has a research history. The contribution of this round is the common count of the six actual completion categories, the stride color correlation and its 464 consequences; no existing concepts or weight optimization are claimed as new fields. For differences in source, actual reading range, and applicability of 2026 differential filling papers, see [Comparison of Counting Methods](COUNTING_COMPARISON.md).
- Fourier search, weight discovery and boundary word experiments retain the source code, actual scope and results. The fact that floating point is feasible does not mean that grid coloring exists, and the timeout does not mean that it is not feasible. There is no new Lean formalization or full-text review statement for the main manuscript.

Accurate verification entrance:

```sh
python research/kernel_compatibility_20261108/verify_release.py
python research/kernel_compatibility_20261108/kernel_upper/certificate.py
python research/kernel_compatibility_20261108/geometry/audit_464.py
python research/kernel_compatibility_20261108/geometry/verify_geometry.py
```

The first command re-executes the five exact checks in a temporary copy and logs the input hashes and actual output, preserving the original run record. Independent review and assembly work packages have their own recurrence commands. All files are kept in this research branch, and the mathematical main manuscript has not yet been incorporated.

## Next counting question

The key to the next step is not to increase the SAT search volume, but to prove the joint extreme value of "up to two contributions per color per layer" in the boundary comparison array, or to find new additive losses. Adjacent layer path counts have given the first set of strict relationships, and there are loops and shared vertices between further layers that require simultaneous control. Any further numerical conclusion must complete the derivation from the common count to the positive contradiction quantity; currently, 463 is reserved as a target to be solved.
