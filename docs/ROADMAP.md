# Research route: Original structural method, solve R3 first

> **Objective update, 2026-11-13.** By direction of the project owner, the
> governing objective is now to improve the upper bounds of both `R_3` and
> `R_4`, with four-color upper-bound research authorized immediately. Where
> this roadmap defers four colors until `R_3` is resolved, the update takes
> precedence; see [AGENTS.md](../AGENTS.md). The unconditional four-color
> baseline and its evidence are summarized in
> [the research state snapshot](../.claude/skills/lgrid-research/references/state.md).

## Overall goal and sequence

The long-term first goal: continuously improve the lower bound and lower the upper bound of R3(L), ​​finally determine the precise value, and provide matching construction and impossibility proof. Only after completing this goal can we start the systematic upper and lower bound research on R4(L). When R3 has not yet been solved, R4 only retains the existing background and conditional inferences.

The current verified numerical benchmarks and literature can be found in [Academic Results](../literature/KNOWN_RESULTS.md). The following route is a research plan and does not mean that any open lemma has been established.

2026-11-08 [Six types of completed grids are counted together](../research/kernel_compatibility_20261108/README.md)The project upper bound has been advanced from the restored 465 to 464, and the current project range is 21 to 464. Document 493 is retained as a baseline for comparison. [Latest global count](../research/global_counting_20261108/README.md)Parallel exploration of cross-source color requests, full-level double-ended matching, and common span costs for extreme shapes. According to the user's latest priority, we will focus on new upper bound counts with greater compression potential; we will not reduce the count by one or expand the SAT lower bound search as the main line of this stage.

Current priorities are explicitly specified by the user: invent new ways of counting with upper bounds. Re-select counting objects, retain the common constraints of old counting losses, and complete numerical derivation; proof collation, old parameter optimization, or expanded SAT search cannot be considered completion of this goal. The six categories of minimum starting point count and stride length color comparison of this round are two layers of specific mechanisms. The lower bound route is retained as a long-term background and does not automatically occupy the current round of work resources.

## Short term goals

### S1: Make the comparison baseline concrete

- Read and verify the specific input of the 20×20 Coloring Certificate and 493 Certificate.
- Establish a ledger of "academic theorem/project proven/conditional/conjecture/refuted" and record the direction, parameter range and literature version.
- Reproduce the current finite certificates and list the missing mapping between the existing Lean coverage and the current body.

Completion Criteria: Each benchmark can be directed to the original attestation or the full certificate, with no summary, search failure, or software showing green in lieu of attestation.

### S2: Turn major obstacles into precise propositions

- Analyze why the fiber-by-fiber Golomb constraint cannot control the shared completion grid.
- Distinguish between a budget that is satisfied by every normal coloring and a budget that is satisfied by one normal coloring.
- Write precise hypotheses for candidate global source bounds, endpoint deletion bounds and cross-scale counts, first using existing counterexamples to eliminate overly strong versions.

Completion criteria: At least one structural lemma with a complete proof, or a clear counterexample that explains the failure. Passing small-scale tests can only support conjecture.

### S3: Propose new mechanisms that can be promoted

Prioritized exploration but not presupposition: global resource allocation of shared completion lattices, telescope-summable potential functions, structure-stochastic decomposition, cross-fiber stability, and recursive description of extreme coloration. Each route must answer: Which interaction does the new control miss that the old method missed? Does it work at any scale? How to derive the specific upper and lower bounds of three colors?

Completion criteria: Give new objects or invariants, core lemmas and their complete derivation to R3. If the parameters are only changed in the old interval formula, it will be recorded as a technical improvement and will not be marked as an original method.

## Long term goals

### L1: Bidirectional compression range of R3

Upper bound route: Invent a count that can control the common geometric limit and continue to break through 464. The current priority is to study how colored minimum points of different step sizes coexist, and the common loss in multi-layer comparisons. A complete universal derivation and an exact contradiction are required; the conditional source bound can only be transformed into a new unconditional numerical upper bound after its assumptions are also proved.

Lower bound route: Search for normal three-color constructions that are interpretable, verifiable, and preferably parameterizable or recursively extendable.

```math
\text{There is normal triple coloring}[n]^2\quad\Longrightarrow\quad R_3(\mathcal L)\ge n+1.
```

SAT can be used to find samples and counterexamples. Failure of a finite search is not an upper bound proof; if the upper bound relies on SAT unsatisfiability, an independently verifiable proof certificate is required, and symmetry constraints and coding equivalence must still be stated.

### L2: Determine the precise value of R3 and refine the method

Once the construction and impossibility bounds are aligned, complete proofs, independent certificates, boundary and direction checks, and comparisons explaining why the method is superior to existing routes are delivered. New methods should reveal structure and be generalizable, not just leave larger one-off enumerations.

### L3: Advance R4 after R3 is completed

Then study the additional difficulties of the three-color strict source and examine which parts of R3's new mechanism can be transferred. The two-color source lemma cannot be directly applied to three-color sources. The existing R4 conditional bounds can only be used as baseline materials, and unproven premises must be retained.

## Tool Responsibilities

Theoretical derivation is responsible for discovering and proving mechanisms; calculations are used to generate evidence, find counterexamples, and check certificates; Lean tests proofs within the scope of its coding. The three cooperate, but the amount of tool runs is not used as mathematical progress. Each round of discussion records a precise question, a proof or counterexample, current obstacles, and next experiments that would differentiate the path.
