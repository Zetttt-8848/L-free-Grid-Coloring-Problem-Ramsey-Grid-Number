# Finite shifts, three-color lines, and the S21 four-color consequence

These modules were developed and compiled against Lean 4.19.0 and the official
Mathlib v4.19.0 checkout. They contain no `sorry`, admitted goals, custom axioms,
`unsafe`, or `native_decide`.

## ShiftCounting.lean

`finite_shift_profile` proves manuscript Lemma `lem:shift`, equation
`eq:shift-profile`, for an arbitrary `Finset ℤ`, its intrinsic span, and every
integer `t ≥ 1`. It derives the triangular coefficients by counting mixed
additive energy, and bounds the actual shifted sumset inside an interval.
`finite_shift_count` proves the stated consequence for every real cap `W ≥ 0`.
No counting identity or Cauchy conclusion is an extra hypothesis.

## LineCounting.lean

`variance_identity` proves the complete identity in `lem:variance` for every
three-coloring and every natural `N`. `rainbowCount_upper` proves the stated
`U_N` upper bound when `N ≥ 1` and the triangle coloring is proper.

The variance is represented in the rationals because every summand is a square
of an integer minus a third of an integer. This is the same finite expression
as in the manuscript. Three explicit inverse bijections identify row, column,
and slope-one line pairs with the three pairs in geometric corners. Separate
integer line minima and the exact count of lengths not divisible by three are
proved universally. `cornerSum_source_bridge` identifies the index sums with
the actual integer source corners on `[0,N)`, and `properOn_triangle_bridge`
connects the coloring hypothesis to the existing geometric `properOn`.

## S21Four.lean

`S21_four` proves `ActualSpanEstimateOn 21 98775 → ramseyL 4 98777`.
`S21_four_full` gives the manuscript's S21 hypothesis on the larger range.
This is the full conditional theorem `thm:s21four`, including the diagonal
pigeonhole argument, extraction of exactly 24,695 marks, removal of a color,
inherited weak-fiber colorings, their two-color restrictions, and application
of S21 to all three color classes. `S21_fiber_profile` establishes the genuine
offset bound. Polynomial weight identities and the finite shift count then
give the contradiction at `t = 600`.

The proof does not assert S21 itself.

## WeightedEmbeddingGeometry.lean and WeightedEmbedding.lean

These modules prove the complete weighted embedding lemma `lem:weighted`.
`weighted_embedding_implication` gives both `rho J ≤ K R_N ≤ K U_N`, and
`weighted_embedding_ramsey` gives the actual `ramseyL 3 N` consequence of the
strict inequality. The parameters are arbitrary integers `N ≥ m ≥ 3`, natural
`rho`, arbitrary real nonnegative weights, and real `K ≥ 0`.

The actual affine map is `(v,u) ↦ (p₁-d+dv,p₂+du)`, with
`p₂ < p₁ < N-d(m-2)` and nonnegative translation coordinates. This is exactly
the manuscript's parametrization with `alpha=p₂`, `beta=p₁-p₂-1`; the third gap
coordinate is determined. The module proves membership, injectivity, positive
step multiplication, preservation of proper colorings and rainbow corners,
and uniqueness of scale and translation for a fixed local corner and its
host image. `weighted_incidence_count` double-counts the actual finite
incidences. `totalCharge_bound` derives the divisor-sum load by grouping local
corners by their step, using the exact counts in `WeightedEmbeddingCounts`.
The charge inequality is not supplied as an assumption.

`weightedCopies` sums over all legal positive scales. The formal result even
allows nonzero nonnegative weights outside that finite scale range: those
weights only enlarge the load. It therefore includes the manuscript's stated
support restriction. `rainbows_card_eq` identifies the actual finite rainbow
set with the line-count module's count; `square_triangle_proper` proves the
final square-to-triangle restriction.

The hypotheses `LocalRainbow m rho` remain explicit. The two refuted premises
are not asserted to hold. Their arithmetic table consequences are handled in
a separate module by the coordinator's other agent.

These modules do not establish the whole manuscript; outstanding results are
tracked by the coordinator separately. Every proof module has
`set_option autoImplicit false` and was recompiled after it was added.

`EnergyFormalAxioms.lean` prints the dependencies of the principal declarations.
The shared launcher command is:

    python formal_verification_round3/lean_compile.py ShiftCounting.lean LineCounting.lean S21Four.lean WeightedEmbeddingGeometry.lean WeightedEmbedding.lean EnergyFormalAxioms.lean
## Graph sources and the family with corner density approaching two

The modules GraphSourceDigits, GraphSourceSets, GraphSourceColoring, and GraphSourceEuclidean use a finite family of two-element subsets of Fin r as the exact representation of an arbitrary simple graph. Base-five decoding is injective for arbitrary length and gives pair-sum equivalence with the actual Euclidean incidence vectors, including repeated marks. The actual graph-source coloring is proper, and the real squared distances are two and four.

SourcePairCollisions proves for arbitrary finite integer sets without nonconstant three-term progressions that T equals twice the actual unordered four-mark collision count. It also proves the universal pair-sum-fiber cap-three implication T≤2M. GraphMatchings derives that cap from the complete classification into the three perfect matchings of four distinct vertices, and proves M≤5span.

GraphCycles maps graph-edge degree collisions bijectively to the integer collisions. GraphCycleFidelity proves both directions of the literal four-cycle characterization and proves that forgetting the two alternating matchings is injective. Its simpleFourCycles objects are actual sets of four graph edges forming a simple cycle, with no induced-subgraph condition, so chords are allowed. This closes the exact T=2C4 and E=2m²−m+8C4 formulas without defining C4 through the desired integer count.

GraphCompleteMatchings classifies every pairing of an arbitrary four-element vertex set and proves its cardinality is exactly three. CompleteGraphCounts forms the actual disjoint union over all four-vertex subsets and obtains C4=3*choose(r,4), T=6*choose(r,4), and the exact energy. WeightTwoFamily proves the exact real-cast M formula, the ratio formula for every r≥3, the actual limit as r tends to infinity, and the coefficient lower bound two. No finite test range replaces a universal parameter.

All eleven proof modules and GraphFormalAxioms.lean compiled under the pinned Lean4.19/mathlib4.19 environment. The 24 principal declarations printed only propext, Classical.choice, and Quot.sound. All modules set autoImplicit false. No sorry, new axioms, unsafe code, or native_decide are used. The manuscript source was not changed by this formalization work.
