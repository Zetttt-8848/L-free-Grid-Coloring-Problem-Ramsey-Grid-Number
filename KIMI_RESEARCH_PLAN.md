# Kimi research plan for directed L-grid Ramsey numbers

Date: 2026-11-15. This is a planning document, not a numerical result.

## 1. Fixed problem and objective

For integer `d>0`, forbid three cells of one color at
`(x,y), (x+d,y), (x+d,y+d)`. `R_k` is the least `n` such that every coloring
of the full `n x n` square with at most `k` colors contains one. An upper bound
must start from an arbitrary coloring of that complete square.

The governing objective is to improve rigorous upper bounds for both `R_3` and
`R_4`, using mechanisms beyond another direct application of the existing
diagonal/Golomb/convolution chain. Four-color work is authorized now. Lower
bounds and finite searches support structure discovery and falsification but do
not replace the upper-bound objective.

## 2. Frontier refresh and evidence limits

Before every work package, authenticate, list all branches and open PRs, record
full commits, and read the changed proof/report files. `main` at
`1231d436d1990f22a9f421246c5b8fc51b66750f` is a literature snapshot, not the
frontier. The local state-refresh pins are stale until re-derived.

- Codex's round-3 branch at
  `14647e607c2525b0cd12081b03899827d306a030` reports the internally reviewed,
  computer-assisted checkpoint `R_4<=21,947,865`. Kimi has not independently
  replayed that complete chain. Codex occupies binary-source capacities,
  hereditary rank transfer, collisions, short requests, and exact windows.
- Claude's upper-bound branch at
  `4517f60d7c9d9284cb0b60428f7cb362d59d02c4` reviews `R_3<=462` with external
  optimal-Golomb-ruler inputs and `R_4<=21,987,409` at an older PR 11 head.
  Claude occupies ternary-source compatibility, joint fiber deficits/MS*,
  prefix certificates, and local triangle refutations.
- PR 11's newest fork head
  `98af36bdb368609f38bc350b664310d7a5b45877` reports `R_3<=144` and
  `R_4<=21,947,877`. Kimi read the new weighted proof reports for routing only;
  the newest claims are not independently audited or adopted as working bounds.
- Conditional values under S21 or G9, including `R_4<=98,777`, are not
  established bounds. Keep the `R_3` and `R_4` ledgers separate.

## 3. Nonduplication and pivot rule

Do not repeat the occupied Codex and Claude lanes or Kimi's closed statements.
Unmerged does not mean wrong; merged does not mean independently audited.
Before each experiment, write an English `CONTRACT.md` with coordinates,
quantifiers, retained information, cheapest discriminating test, stop condition,
consumer chain, nearest obstruction, and required evidence.

Run the smallest exact test capable of changing the route. On a counterexample,
store the complete object and nearest surviving variant. On a weak consumer,
record the quantitative gap and stop. On UNKNOWN or timeout, record UNDECIDED
and do not enlarge the same search automatically. Keep an alternative that does
not depend on the failed premise.

## 4. Route ledger

### Route Q: palette quotients on contiguous small blocks

Q1 remains a cover lower bound using `R_2=5`: at least three Ls are required to
cover all seven quotient signatures in a proper four-color 5-square. Q2 remains
refuted by the stored proper 5-square: three Ls do not always suffice. The
obstruction to independently selecting arbitrary rows and columns also remains.

**Q3a is REFUTED and must not be used.** The old inequality

```text
sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2
```

has a checked proper 6-square counterexample with left side `1381/144<12`.
Fixed-L block multiplicity is position-dependent, and the old weighted direction
was wrong. More fundamentally, every three-cell word in four colors has nonempty
quotient signature, so `P_d=(n-d)^2` for every coloring, even an improper one.
The old unweighted inequality is true but trivial and has no structural content.

See `research/kimi_r4_quotient_multiscale_20261115/ERRATUM.md` and
`research/kimi_r4_multiscale_20261115/THEOREM.md`.

### Route O: two-diagonal product classes (refuted in round 2)

The proposed joint-fiber palette reduction is false. Main and off-diagonal pairs
of lag `h` on diagonals `0` and `c` use different completion cells `W_h[u]` and
`W_(c+h)[u]`. A checked proper 3 by 3 square refutes the enabling statement, and
the sixteen-class consumer was not run. Only the standard single-lag restriction
`F_c(J_(a,a))=empty` survives. Do not revive product-class capacities without a
genuinely different shared-cell mechanism.

### Route M: multiscale full-square recursion

Only contiguous sub-squares or Cartesian arithmetic-progression selections with
the same positive row and column step preserve the equal-leg geometry. Every
cross-block and cross-scale incidence must be included.

**The quotient-count version is closed in round 3.** Every 5-copy has 30
pair-tight Ls, giving the coloring-independent identity
`sum_L m_s(L)=30 C_s`. Weighted sums over scales remain the same identity. The
seven-quotient lower bound `Q_s>=7 C_s` is dominated by the universal nonempty
signature bound `Q_s>=30 C_s`; its induced rainbow upper bound is likewise
weaker than the trivial one. No further quotient sampling or scale scan is
authorized without a genuinely different coloring-dependent statistic.

General non-quotient multiscale recursion is not refuted. A future candidate
must retain information that distinguishes proper from improper colorings and
must name a compatible upper estimate before computation.

### Route N: non-quotient two-dimensional color-class energy (next candidate)

Represent the full square directly by its four color-class indicators and study
horizontal, vertical, slope-one, and higher-order correlations without palette
quotients. First compare the exact statement against manuscript Lemma
`lem:variance`, its weighted embedding lemma, and PR 11's triangle catalogs.
The cheapest test is an algebraic consumer check, not a large energy scan. Stop
if it is only the known line identity or if the four-color leading coefficient
cannot contradict properness. No proposition in this route is currently claimed.

### Route F: certified finite kernels as lemma generators

This is the independent fallback if Route N has no usable inequality. Extract
small full-grid obstructions only to propose general forbidden patterns. Bare
UNSAT, unchecked DRAT/RUP, partial cubes, restricted families, and timeouts are
not upper-bound evidence. A new numerical bound would still require arbitrary
full-square colorings and complete geometric reductions.

## 5. English research and writing protocol

Each dated package contains the contract, exact theorem or counterexample,
standalone checker, raw output, report, collaboration handoff, and manifest.
Record commands, actual coverage, interpreter version, important input hashes,
and explicit non-claims. Validate checkers on known positive and negative
instances and independently recompute decisive values from definitions.

Lead every report with whether a numerical Ramsey bound changed. Separate a new
mechanism, a technical integration improvement, and a numerical bound. Use
PROVED, CONDITIONAL, CONJECTURE, FINITE-CHECKED, COUNTEREXAMPLE, REFUTED,
SUPERSEDED, and UNDECIDED only for exact statements with evidence. Internal
verification is not external peer review or formalization.

Run syntax checks, independent verification, and
`python scripts/check_english_only.py` before pushing. Create a separate branch
and draft PR. Do not merge, close, rewrite shared manuscripts, or alter another
agent's package without separate owner authorization.

## 6. Collaboration interfaces

For Codex and Claude: immediately withdraw old Q3a from any proposed consumer.
Do not spend time on an upper estimate for pair-tight cardinality; it is just
the geometric L count. Q1 and Q2 may still inform cover constructions, but they
do not justify the withdrawn averaging inequality.

For future full-square inequalities: export exact coordinates, scale, overlap
multiplicities, color scope, certificate path, and missing consumer. For
capacity consumers, identify shared cells and combine overlapping savings by
intersection unless joint accounting is proved. Negative results and errata are
deliverables when they prevent duplicated or invalid work.
