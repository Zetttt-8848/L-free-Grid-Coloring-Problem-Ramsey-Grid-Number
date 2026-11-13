# Boundary compatibility research: local equilibrium counterexamples, expansion barriers and new literature

2026-11-08; Basic submission`080822bb1d434b164a1f42ea159d0bf148396b71`. Goals and work packages are available at [CONTRACT.md](CONTRACT.md). This round completed clear mathematical checkpoints in both directions, **no improvement in the unconditional interval`21≤R₃≤493`, and R₃** has not been determined.

## 1. Upper bound direction: global optimal does not guarantee local balance

exist`Q={0,1,5,6,25,26,30,31}`,`A=Q∪{2,3}`On the complete strict source, two copies of normal secondary coloring are given. Only change the inner grid`(6,5)`, block internal potential`Φ_Q:8→4`, the whole source is blocked`Φ_A:9→13`.

The parity lower bound proves that 9 is already the absolute minimum value of all sources; when the external color shown is fixed and Q balance is required, the minimum value is exactly 13. This is a goal conflict, not a legal repair path that cannot be found. It excludes the reasoning of directly assuming local equilibrium through global minimum; it does not deny G9/S21 itself.

- [Complete certificate, 45-square witness and outfield lower boundary](upper/README.md)
- [Discover code](upper/discover.py),[independent verifier](upper/verify.py), [calculation list](upper/computation_manifest.json)
- [Coordinator’s independent physical three-point verification](upper_witness_audit.json), [Wolfram Exact Arithmetic Cross Check](wolfram_crosscheck.json)

General replacement must preserve both cross-boundary forbidden color constraints and external fibers and e; the correct target contains`2⟨e,s_Q⟩`. The general representation is constrained elimination and square expansion, with no separate claim to originality. The new contribution is to make local/global mismatches complete, reviewable counterexamples and exact restricted optima.

## 2. Lower bound direction: the literature sample must be modified internally to expand

An exact decomposition of a fixed old square, adding a bottom row and a right column, is proved for any n,k: an independent list of forbidden colors in the right column, plus a color-labeled point pair constraint in the bottom row. General placement retains all uniary, binary, and ternary cross-boundary constraints. [General Theorem and Proof](lower/THEOREM.md)

For the complete 20×20 three-coloring of the literature, this round proves that none of the four sides can remain internally unchanged and add a single row/column. There are 41 deletion minimal kernels composed of constraints on the lower side, and 38 on the left side. Attached are the complete 24-node and 18-node branch proofs and the feasible witness after each constraint is deleted. "Delete minimum" does not mean the minimum number of constraints.

Further find the core of conflict that supports each other but does not intersect with each other. If the original matrix is ​​placed at a 21×21 square offset position`(ox,oy)`, any legal extension must modify at least the following amount of the original 400 colors:

| Offset | (0,0) | (0,1) | (1,0) | (1,1) |
|---|---:|---:|---:|---:|
| Proven lower bound on necessary modifications | 10 | 2 | 14 | 8 |

These numbers are not optimal repair distances; no 21×21 configuration was provided to achieve them. They only apply to this given matrix and four consecutive placement positions, and do not exclude any general 21×21 construction.

- [Calculation results and reproduction instructions](lower/README.md)
- [Full Limited Certificate](lower/extension_results.json), [Mutually disjoint supporting certificates](lower/packing_results.json)
- [Standard Library Verifier](lower/verify.py), [Coordinator’s second certificate check](lower_cores_audit.json)
- [Independent Universal Certification Review](lower_proof_review.md), [Five groups of small parameters exhaustive cross-checking](lower_theorem_audit.json)

## 3. Check the latest literature and make your own inferences

[Literature report](literature/README.md)The actual search terms, original versions, article-by-article reading depth and inapplicable conditions are recorded, covering direct numerical papers, quasi-polynomial corners methods, and polynomial corners progress in 2026. The reading of abstracts was not recorded as a full-text audit, and no claim was made to exhaust the entire subsequent literature.

Recent independent polynomial results do not allow the two legs to be identical directly. For another 2026 preprint, the problem of mixing uniform image set weights and parameter multiplicity was discovered, and an exact rational number/circular polynomial check was given. [Narrow range diagnosis](literature/WEIGHT_AUDIT.md)It only refutes the equation referred to and does not claim that the final density theorem has been disproven.

The literature inspiration and this round of counterexamples share the same goal: retain the actual achievable state, field, color and resource multiplicity, and avoid taking rough bounds on each of them before splicing them together. What is missing is a globally summable budget that applies to arbitrary sources, so no new Ramsey upper bounds are derived from these observations.

Wiley Scholar Gateway requires re-accreditation this round and has not contributed documentary evidence. Wolfram has been used for exact arithmetic, and Mathbox has been used for source, proof, and calculation review processes; they do not constitute additional certification of general theorems.

## 4. Inspection and reproduction performed

Some procedures in the discovery phase require`python-sat`;The following certificate verification only uses the Python standard library. Execute from the repository root directory:

```sh
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py .agents/skills/directed-l-grid-research/assets/paper20.json
python research/boundary_extension_20261108/upper/verify.py
python research/boundary_extension_20261108/lower/verify.py --output /path/to/fresh/lower_check.json
python research/boundary_extension_20261108/audit_upper_witness.py
python research/boundary_extension_20261108/audit_lower_cores.py
python research/boundary_extension_20261108/audit_lower_theorem.py
python research/boundary_extension_20261108/literature/check_polynomial_weight.py --output /path/to/fresh/weight_check.json
```

The main draft verifier has been re-run: 13 items passed, [this round of report](manuscript_checks.json). The complete 20×20 certificate verification covers 400 squares, 2470 L, and zero single color angles, [report](paper20_check.json). This is not equivalent to a full-text proof audit or a Lean new compilation. Each report is tied to the corresponding input/code; the v2 manifest of the main calculation includes running status and pre- and post-hash.

[Scope of review](AUDIT.md); Calculation list: [upper bound](upper/computation_manifest.json), [lower bound](lower/checked_run/manifest.json),[Document weight diagnosis](literature/weight_run/manifest.json).

## 5. Renewable status

- **Upper bound route still open:** New counterexample requiring budget to preserve outfield. The next step is to check for double charges of outfield costs using two overlapping blocks, first looking for counterexamples and then looking for labeled fractional amortization. It is no longer necessary to directly deduce the equilibrium of each block from the total source minimization.
- **Nether routes are still open:** Unfreeze selections with disjoint conflict kernel constraints, comparing candidates that satisfy the necessary number of modifications to ordinary fixes. Controlled performance experiments have not yet been completed, and no legal construction of 21×21 has been found.
- **Independent alternative routes are still open:** Use the proven real geometric small kernel to discover forbidden types; any cross-instance generalization must re-prove the color, coordinate and coverage conditions, and the sample kernel cannot be regarded as a universal forbidden type.
- **Literature Dependencies:** The weight correction of the 2026 polynomial preprint is still incomplete; a direct replacement of the independent polynomial theorem to the equal-leg case is not available. Wiley coverage will be checked after reconnection.
- **Generalization conditions:** The lower bound constraint decomposition holds for general k; the upper bound ±1 odd-even potential depends on the two-color source. When generalized to the three-color source, the color vector budget must be re-derived. R₄ has not yet been systematically tackled.

Project-specific skills and their creation snapshots are imported with this branch.`docs/RESEARCH_SKILL_*`It is a historical record of the previous preparation stage and has not been used as new verification evidence in this round; it was not originally submitted`lfree_sat/`Not imported or certified in its entirety. Literature priority for the current results has not been established.
