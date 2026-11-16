# Kimi research plan for directed L-grid Ramsey numbers

Date: 2026-11-15. This is a planning document, not a mathematical result.

## 1. Fixed problem and objective

For integer `d>0`, forbid three cells of one color at
`(x,y), (x+d,y), (x+d,y+d)`. `R_k` is the least `n` such that every coloring
of the full `n x n` square with at most `k` colors contains this configuration.

The governing objective is to improve rigorous upper bounds for both `R_3` and
`R_4`, using mechanisms beyond another direct application of the existing
diagonal/Golomb/convolution chain. Four-color work is authorized now. Lower
bounds and finite searches support structure discovery and falsification but do
not replace the upper-bound objective.

## 2. Frontier understood in this orientation round

- `main` at `1231d436d1990f22a9f421246c5b8fc51b66750f` is primarily the
  imported manuscript and literature baseline, not the current frontier.
- Codex's active line concerns binary-source compatibility, collisions,
  finite capacities, hereditary rank transfer, and exact window consumers.
  Its round-3 branch at `14647e607c2525b0cd12081b03899827d306a030` reports
  the internally reviewed, computer-assisted checkpoint `R_4<=21,947,865`.
- Claude's active line concerns ternary-source grid compatibility, joint fiber
  deficits/MS*, prefix certificates, and local triangle refutations. Its
  upper-bound branch reports `R_3<=462` with external optimal-Golomb-ruler
  inputs. These claims must be read against the cited proof packages whenever
  used; this orientation round is not an independent audit.
- Conditional values under S21 or G9, including `R_4<=98,777`, are not
  established bounds.

## 3. Nonduplication rule

Before every work package, refresh all branches and open PRs and record their
full commits. Do not repeat the occupied Codex and Claude lanes above. Do not
infer that an unmerged branch is wrong or that a merged branch has been
independently audited.

Each package starts with a five-field candidate card: limitation, mechanism,
exact proposition, cheapest discriminating test, and consequence chain to a
Ramsey bound. Include a stop condition and nearest known obstruction.

## 4. Candidate portfolio for later rounds

These are candidates, not assignments or claimed results.

### Route Q: palette quotients on contiguous small blocks (closed in round 1)

The first round proved a three-L quotient-cover lower bound and found a checked
counterexample to universal three-L sufficiency. Arbitrary combinatorial row
and column selections do not preserve equal-leg geometry, so the proposed
all-combinatorial-subsquare averaging mechanism is invalid. Only geometry-
preserving selections, such as contiguous or equally scaled blocks, may be used.
The remaining contiguous-block count has no known upper-bound consumer; do not
expand this lane without first supplying that consumer.

### Route O: two-diagonal product classes (refuted in round 2)

The proposed joint-fiber palette reduction is false. Main and off-diagonal
pairs of lag `h` on diagonals `0` and `c` use different completion cells
`W_h[u]` and `W_(c+h)[u]`. A checked proper 3 by 3 square refutes the enabling
statement, and the sixteen-class consumer was not run. Only the standard
single-lag restriction `F_c(J_(a,a))=empty` survives. Do not revive product-class
capacities without a genuinely different shared-cell mechanism.

### Route M: explicit multiscale full-square recursion

Use only subdomains that preserve the equal-leg configuration, such as
contiguous sub-squares or Cartesian arithmetic-progression selections with the
same row and column step. Seek a recursion or weighted cover that combines
scales, rather than applying one source estimate at one scale. Require a
complete treatment of Ls crossing blocks and scales. Stop a construction if
only block-interior Ls are checked.

### Route F: certified finite kernels as lemma generators

Only if routes Q/O/M do not yield a usable inequality, extract small full-grid
unsatisfiable kernels with independently checked proofs. Use them to propose
general forbidden patterns. Bare UNSAT, unchecked DRAT, partial cubes, and
timeouts remain UNDECIDED and cannot support a Ramsey bound.

## 5. Next-round execution protocol

1. Refresh GitHub state and verify that the selected lane remains unoccupied.
2. Create a separate branch from the newest appropriate checkpoint and a dated
   directory under `research/`.
3. Write `CONTRACT.md` before computation; pre-register the test and pivot
   condition.
4. Run the cheapest exact test. Validate the checker on known positive and
   negative instances before interpreting output.
5. On failure, preserve the exact witness or quantitative gap and switch to a
   different mechanism. Do not merely enlarge the same search.
6. On success, derive the complete chain from an arbitrary full-square coloring
   before claiming any change to `R_3` or `R_4`.
7. Run independent verification and `python scripts/check_english_only.py`;
   then commit and push only the new branch. Do not merge PRs or edit shared
   manuscripts without explicit authorization.

## 6. Collaboration interfaces

For Codex: export any full-square quotient or multiscale inequality that could
consume its exact binary capacities, with explicit overlap accounting.

For Claude: export any off-diagonal or quotient constraint that could strengthen
MS* without assuming it, retaining the ternary-source quantifiers and scale.

For both: report exact domain, colors, span range, evidence status, certificate
path, consumer, missing bridge, and non-claims. Negative results are deliverables
when they prevent duplicated work.

## 7. Evidence language

Use PROVED, CONDITIONAL, CONJECTURE, FINITE-CHECKED, COUNTEREXAMPLE, REFUTED,
SUPERSEDED, and UNDECIDED exactly as defined by `lgrid-verify`. Separate a new
mechanism, a technical integration improvement, and a numerical bound. Internal
review is not external peer review or Lean formalization.
