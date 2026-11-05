The modules below formalize universal statements over arbitrary finite integer
sets. They do not enumerate a bounded family of examples. They target
`Energy_and_forcing_complete.tex`, SHA256
`edfd42329af59aa8419fa1eed18fa6cb0c31ba693df434d57bb98964c8ef6158`.

| Paper result | Complete formal coverage |
|---|---|
| `prop:counts` | `SourceCounting`: actual source-cell cardinality, positive-difference mass, actual source-corner bijection and cardinality, square-sum identity, ordered equal-difference energy identity. |
| `cor:span` | `SourceCounting`: actual positive support lies in the integer span interval, its cardinality bound, finite Cauchy inequality, pair bound, both exact and simplified square-root bounds for every real nonnegative kappa. |
| `thm:energy` | `TwoGolomb`: actual cross-fiber incidence counts, complete same-orientation collision bijection, exact corner decomposition, all three resource bounds on Q, the two corner bounds and the energy bound. |
| `cor:imbalance` | `TwoGolombImbalance`: the actual Q and common-difference deficits, both eta-corrected corner bounds, energy bound, and both near-equality stability conclusions. |
| `cor:moments` | `CubeMoments` and `EnergyMomentLower`: actual ordered positive/signed cube counts, all displayed cube identities and bounds, and both moment inequalities on the manuscript's exact integer ranges. |
| `thm:progression` | `SeparatedProducts` and `ProgressionProducts`: actual separated mark bijection, energy factorization, exact progression fiber and interval energy, every integer parameter case, both the weaker two-Golomb assumption and the proper-coloring assumption, and all three conclusions. |
| `lem:rectangles` | `RectangleObstructions` and `OverlapRestrictions`: universal 7 by 3 and 5 by 5 rectangle obstructions, exact product fibers, two-Golomb partitions of both actual factors, energy product, and both positive-difference multiplicity caps for either factor. |

The following choices make the translation explicit.

* `sourceCorners A` contains triples `(x,y,z)` with `y<x<z` and all four marks
  `x,y,z,y+z-x` in A. Its cells are `(x,y),(z,y),(z,y+z-x)`. The offset is
  `x-y`, and the corner step is `z-x`. No proof conflates these parameters.
* `E A` counts ordered quadruples with `a-b=c-d`, exactly the manuscript's
  definition. `energy_eq_additive_quadruples` also proves the conventional
  equal-sum definition by an explicit coordinate permutation.
* Infinite-looking positive sums are represented by `posDiffs A`, the exact
  finite support. Omitted coefficients are proved zero. The two final moment
  theorems instead use the literal intervals `Icc 1 L` and `Ico 1 L`, with
  denominators `2*(L-d)+1` and `L-d` in the real numbers. Thus the final
  zero-separated statement has no zero denominator.
* `Golomb` is the original geometric module's predicate: any two ordered
  increasing pairs with equal differences coincide. Cross-fiber indicators are
  proved equivalent to their 0-or-1 cardinalities, not assumed.
* `Qinc` consists of all actual positive-length opposing cross incidences.
  Its cardinality is proved equal to the manuscript's sum of products. The Q
  bounds follow from injective maps into internal pairs or ordered pairs.
  These resource bounds in fact need no disjointness assumption. The full
  two-Golomb theorem retains disjointness because its collision identities need it.
* Empty classes and empty integer sets are included. No positive-size premise
  replaces a missing edge case. The stability theorem alone assumes n at least
  two, exactly as in the manuscript.
* A `CubeTuple j` is an ordered list of j integer generators and a base.
  `cubeParametersEquiv` identifies it with `Int × (Fin j → Int)`.
  `cubeVertex_eq_sum` proves that its vertex is the base plus the selected
  generators. `mem_positiveCubes_iff` and `mem_signedCubes_iff` prove that
  finite membership means all 2^j vertices lie in A, with positivity imposed
  only for positive cubes. Generators and vertices may coincide.
* Signed counts are proved through translation bijections and signed-fiber
  recurrences. They include every sign pattern and every zero-generator case.
* Fiber classes are the actual color classes of the restricted source. Their
  Golombness follows from `fiber_class_golomb` and the stated properness
  hypothesis. `Dmoment_eq`, `Pmoment_eq`, and `Rmoment_eq` prove equality to
  the shared `FiberDominance` quantities, including natural-subtraction and
  absolute-value conversions.
* The interval energy lower bounds follow from actual difference-support
  cardinalities, actual mass/energy identities, and finite Cauchy--Schwarz.
  The intrinsic span bound for each nonempty positive fiber is proved from
  minima and maxima.

No additional combinatorial hypotheses, precomputed cardinalities, or
arithmetic certificates stand in for a counting argument in these five
results. The proofs use Lean's kernel with Mathlib v4.19.0. They contain no
`sorry`, `admit`, new axioms, unsafe declarations, or `native_decide`.
`CountingAxiomAudit.lean` prints the dependencies of the principal claims.
The progression theorem uses natural t with t at least two, which is equivalent
to the manuscript's integer t under that assumption. Q remains an arbitrary
integer subject only to the stated separation inequality. Its small-size
exceptions follow from a proved empty-corner result for every set with at most
two marks, not from selected numerical representatives. The separated-energy
factorization itself holds for arbitrary finite factors, including empty ones.
This record does not claim formal coverage of any other paper result.

The rectangle argument counts actual same-color row pairs. The 7 by 3
obstruction uses a six-label pigeonhole argument. The 5 by 5 obstruction uses
pairwise disjoint column pair sets and the parity contradiction at equality.
Only the local facts about one three-bit or five-bit column are closed finite
kernel computations. These cover all eight or thirty-two possible columns;
the arbitrary array theorem and its application to arbitrary integer factors
are proved universally. No bounded selection of factor sets substitutes for
the integer-set theorem.

Reproduction command:

```
python formal_verification_round3/lean_compile.py SourceCounting.lean TwoGolomb.lean TwoGolombImbalance.lean CubeMoments.lean EnergyMomentLower.lean SeparatedProducts.lean ProgressionProducts.lean CountingAxiomAudit.lean
```


## Full strengthened small-factor lemma and direct sums

`ArithmeticProgressions.lean` proves successor closure implies a complete finite arithmetic progression and that two endpoint deletions which are progressions force the original set to be one for n>=4. `SharpSmallFactors.nonAP_corner_deficit` proves the universal bound T+(n-2)<=choose(n,3), n>=3, under precisely non-AP. Its energy corollary, maximal-corner AP characterization, and six-mark T<=16,E<=130 are all compiled. `SmallFactorBounds.four_mark_cap_two` supplies the four-mark cap-two assertion through the unique maximal difference.

`ProgressionSix.no_two_color_progression_six` instantiates all20 actual corners of P6, then uses ordinary Bool case splits and simplification to produce a kernel-checked propositional contradiction on its15 Bool cell colors. This is a complete finite obstruction, not an assumed SAT result or `native_decide`. `SmallFactorCompletion` supplies a universally quantified positive affine pullback of proper colorings and both actual factor embeddings, completing the six-mark factor assertion. The manuscript uses the equivalent line-count proof, not this finite propositional proof.

`DirectSums.direct_sum_bounds` proves all three thm:direct conclusions universally for arbitrary finite integer B,C of cardinality>=2, Q>2span(B), and an actual Bool proper coloring of their complete separated sum. It uses actual separated energy/cardinality bijections, both two-Golomb partitions, universal rectangle-derived multiplicity caps, and the complete small-factor results. `DirectComparison` is only its algebraic case comparison, never counted alone as full.

All modules above were actually compiled with pinned Lean4.19/mathlib. The previous source hash is obsolete after the root author incorporated the universal non-AP strengthening; final source binding is maintained by the root runner.

Final axiom audit for P6, all small-factor declarations, and direct_sum_bounds contains only propext, Classical.choice, Quot.sound. An intermediate bv_decide proof was replaced after the audit detected Lean.ofReduceBool; it is absent from the final proof.


## Full general two-distance theorem

`TwoDistanceCounting` defines actual long/short unordered pairs, their midpoint fibers, and actual unordered pairs of distinct long pairs sharing a midpoint. `geometricCollisions_card` proves the finite fiber-cardinality sum; `geomT_moment` proves geomT=sum k(k-1). The predicates contain no presumed count equality.

`TwoDistanceSource.source_corner_le_geomT` maps the actual unordered pair-pair collisions from `SourcePairCollisions` into image collisions injectively. The exact T=2*collision-cardinality identity is used after the proved absence of three-term progressions. Only the manuscript's forward pair-sum preservation is used.

`TwoDistanceIncidence.eight_midpoint_incidence` proves112*q8<=(|X|-2)*s on the actual finite set. Each eight-pair block has16 distinct vertices and exactly8 long internal pairs, hence112 short pairs. A fixed short pair{x,y} maps each containing midpoint c injectively to2c-x in X minus{x,y}. No choice of orientation adds a factor. `geomT_small_cap_eight` combines this with the literal cap8 and card<=53.

`TwoDistanceRemoval.isolated_collision_partition` and `isolated_geomT_add` prove the exact decomposition using the independently formalized isolation theorem. `geomT_six_bound` uses strong induction on the actual point cardinality. An isolated block with k>=8 removes2k points. If none exists, all midpoint multiplicities are at most8 by the proved nine-radius orthogonality result. A remaining multiplicity8 either would be removable or has a nonorthogonal outside point and the proved cardinality<=53 bound applies.

`TwoDistanceRemoval.two_distance_bounds` concludes T(A)<=6M(A), M(A)<=13span(A), and proper squared-distance coloring for an arbitrary finite integer source and an arbitrary real inner-product space under exactly `TwoDistance.Hypotheses`. It is stronger in target generality than finite-dimensional R^r and adds no hypothesis. All20 authored mathematical modules are frozen and compiled; the exact hash manifest is COUNTING_FINAL_MANIFEST.json.

Independent reviews: round2_energy reviewed the actual incidence/counting argument and returned PASS. round2_structured reviewed the collision definitions, source injection, removal identity, and final induction and returned PASS. The author reviewed the updated manuscript small-factor proof against the universal formal theorem and found no mismatch.
