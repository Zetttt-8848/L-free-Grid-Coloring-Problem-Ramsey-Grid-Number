# Scope of the third Lean verification round

This package represents all 47 named theorem, lemma, proposition and corollary statements in `Energy_and_forcing_complete.tex`. The final acceptance and execution status is generated in `coverage.json` and `verification_manifest.json`. A representation inventory alone is not a successful kernel audit.

The proofs use Lean 4.19.0 and official mathlib v4.19.0, pinned to commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Earlier verification packages and their execution records were preserved. This directory contains the continued formalization and a new execution record.

## Exact mathematical objects

The counting results use actual finite integer sets, source cells, positive-difference fibers, source corners and ordered energy quadruples. Every cardinality transfer is supported by a proved injection, bijection, fiber count or finite-sum identity. The forcing graph uses unordered physical edges. The cube statements quantify over the stated generators and translations, with separate proofs of every representation transfer from a finite coloring certificate.

The probabilistic construction is proved by finite Bernoulli weights and exact expectation identities. Actual five-cubes are bounded through their six-point increasing paths, and actual vertices are deleted. A growing subsequence gives the stated exponent 73/26 and constant 1/2. No finite search is used to infer a universal existence result.

The structured-source results cover all allowed factor sizes. The new nonprogression deficit is proved for every cardinality at least three by endpoint deletion. The six-term progression obstruction uses Boolean case splitting and ordinary kernel simplification. It does not use `bv_decide` or native evaluation.

The two-distance proof uses actual finite image-point sets and actual unordered long pairs at each midpoint. `MidpointBlocks` proves the complete correspondence with orthogonal antipodal blocks. The exceptional eight-pair case is bounded by a genuine 37-dimensional linear-independence argument. The incidence count and exact block-removal partition lead to the universal bound by strong induction. Source-only maps extend to global maps explicitly; the latter's values outside the source do not enter the hypotheses. The formal target can be any real inner-product space, which includes the manuscript's finite-dimensional Euclidean target.

Graph sources use literal base-five marks and actual edge-indicator vectors. The four-cycle count is proved equivalent to literal four-edge simple cycle sets, so rotations and reversals are identified while chords are allowed. Exact formulas hold for the full complete-graph family. Its ratio tends to two, and the family satisfies the actual geometric midpoint cap. This proves the claimed optimal coefficient without truncating the parameter range.

## Inputs retained as hypotheses

The general Ramsey bound explicitly takes the cited quantitative corners estimate as an input. `ExternalCyclicCornersBound` states its precise cyclic-group specialization, including the exponent 1/600 and nonzero group steps. The transfer, constants and ceilings are formalized. The external theorem itself is not re-proved in Lean. Its source and version were checked separately in `GeneralBoundIndependentReview.json`.

S21, G9, G9-exists, EP10 and H10 remain open assertions. Their formalized consequences accept them as explicit arguments. They are not introduced as axioms and are not proved by those implications. The weighted Ramsey implications likewise retain their local rainbow premises; separate literal certificates refute those premises. No unconditional improvement is inferred from a refuted premise.

## Review and execution

`round3_mapping.py` binds each manuscript label to exact theorem names and explains its scope. Independent reviewers checked the mathematical representations, cardinality transfers and principal proof chains. Their reports pin the reviewed module hashes. `manuscript_revision_crosswalk.json` records that 46 result statements are unchanged and identifies the strengthened small-factor lemma. This crosswalk connects earlier source-bound reviews to the revised manuscript without silently changing their provenance.

The aggregate runner freshly recompiles every local mathematical module before its dependents. Independent modules may compile concurrently. It checks input hashes before and after the run, rejects proof stubs and new axioms, and prints the dependencies of every public `theorem` and `lemma`, including nested namespaces. These dependencies are transitive, so proof definitions used by the audited theorems are included. The inventory does not claim to separately enumerate every `def`, structure or instance.

Only `propext`, `Quot.sound` and `Classical.choice` are permitted in the reported dependencies. A successful run must have one printed axiom report per inventoried theorem or lemma, no unexpected axiom, no compilation error and unchanged inputs. Standalone audit imports are excluded from the mathematical-module count. The bounded execution manifest additionally records the command, software versions, limits, source hashes and generated outputs.

Acceptance covers the 47 manuscript statements with their explicit mathematical inputs. It does not turn the cited external theorem or open assertions into independently formalized results, nor certify every sentence or external reference in the paper.
