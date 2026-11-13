---
name: directed-l-grid-research
description: Study the directed equal-leg L grid Ramsey coloring of this project; used for parallel advancement of three-color upper and lower bounds, new structural methods, counterexample search and evidence sorting, and tracking conditions for promotion to four-color and general k-color.
---

# Directed L-grid Ramsey study

Repository: `Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number`.
The main goal of the research is to simultaneously improve the three-color lower bound and lower the three-color upper bound, and finally determine the precise value with a matching structure and impossibility proof; method innovation and numerical advancement are recorded separately. Four-color and general k-color are used as generalization tests of the method, and the three-color problem will not be automatically expanded to an independent large-scale research before it is solved.

## Fixed problem, don't let quantifier or direction drift

```math
\mathcal L(x,y;d)=\{(x,y),(x+d,y),(x+d,y+d)\},\qquad d\in\mathbb Z_{>0}.
```

What is prohibited is **three dots of the same color**. It is allowed to use up to k colors, i.e.`χ:[n]²→[k]`, without additional requirements for each color to appear. Equal arms, parallel axes, positive steps, and specified orientation are all part of the problem.

- `R_k`: the least n for which every coloring of the n by n square with at most k colors contains a monochromatic L.
- `N_k`: the largest side admitting an L-free k-coloring; `N_k=R_k-1`.
- A proper coloring of the n by n square proves `R_k>=n+1`. An upper bound `R_k<=n` requires excluding every allowed coloring of that square.
- Keep the quantifiers explicit; do not replace this problem with finding a domain that avoids L under every coloring.
- Code coordinates start at zero unless stated otherwise. State the coordinate dictionary before translating row and column conventions.

`V(A)={(v,u):u<v,u,v in A}` is the strict source; `W(A)` also allows equal endpoints. Full squares, complete triangles, sparse sources, individual fibers, and abstract graphs are different domains. A proper source coloring need not extend to a square. See the [research map](references/repository-map.md).

## When starting a job

1. Locate the repository root directory, read applicable project conventions, and record branches, complete commit numbers, and workspace changes. read`README.md`,`docs/ROADMAP.md`,`docs/OPEN_PROBLEMS.md`,`docs/RESULTS_INDEX.md`and related text; read-only changes while existing context is still valid.
2. When remote status is required, first use the GitHub connector to read the status of the default branch, related PR, base/head and differences. The fact that PR is not consolidated does not mean that it has no mathematical value; the fact that it is consolidated does not mean that an independent audit has been completed. Precise submissions and scope of evidence must be preserved.
3. The creation snapshot of this skill can be found on the research map. It is a navigation cache; after subsequent source code, certificate or document version changes, affected dependencies are rechecked. "current", "PASS", "accepted" and old numerical bounds in the history log do not automatically become the current facts.
4. Write a goal contract in the new research directory: object, quantifier, hypothesis, conclusion to be proved, upper/lower bound direction, evidence required for success, and the first uncertain step. Check first [route and obstacles](references/routes.md)of adjacent failure mechanisms before deciding to experiment.

No longer rereading the entire history each round. Full file index`docs/RESEARCH_SKILL_SOURCE_INDEX.json`Can be located by path, statement, or title; it only certifies that inventory and structure scanning have been completed, not a line-by-line review, a full database rerun, or a certificate of correctness.

## The upper and lower bounds are parallel, and the mechanism remains diverse.

For broad requests such as "continue research/compress the three-color interval", maintain both the lower bound work package and the upper bound work package; do not consume all resources on one side for a long time. Logical parallelism does not require that the processors be occupied at the same time. When the environment supports it and authorization has been delegated, the structure, global structure and independent verification tasks can be assigned separately; otherwise, they can be promoted in a staggered manner.

Each work package has a clear goal, basic commit, write directory and output evidence. Concurrent authors do not jointly rewrite the same master draft or status document, and are consolidated by the coordinator. Certification authors and verifiers start with definitions and original certificates respectively; another implementation does not automatically equal independent review.

From [Routes and Obstacles](references/routes.md)Select currently informative combinations:

| Direction | Priority research objects | Gaps that must be bridged |
|---|---|---|
| Lower bound | Complete square coloring, boundary signature, recursive splicing, search resulting pattern | Each cross-block, cross-scale L is controlled; output all grid point colors |
| Upper bound | Shared completion lattice, boundary constraints, resource multiplicity, source structure decomposition | Established for all allowed sources, or completely covering the target square; deduce actual numerical contradictions |
| Bridging | Extreme samples, unsatisfiable small kernels, FF/FM/MM relations, structural counterexamples | Clear necessary conditions for sample revelation, and global properties that cannot be guaranteed by local conditions |

The candidate route is written first: **Interaction of new controls → Key lemma → Cheapest discriminant experiment → Derivation to R₃**. If this link does not exist, the link should be supplemented first or downgraded to exploratory observation.

Method selection comprehensively compares mathematical information gain, unproven dependence, evidence cost, whether old barriers are touched, parameter sensitivity and generalization value. Don’t make up the probability of success, don’t call an uncompared method “optimal”. Maintain an alternative direction that does not rely on the core conjecture of the main route; the specific amount and budget will be adjusted according to the problem.

Acceptance of a new method requires a new object, representation, or reusable lemma, proof that it handles constraints missed by the old method, and demonstration of verifiable consequences. Parameter fine-tuning can be valuable, but it does not alone count method innovation. Methodological innovations, conditional improvements, unconditional numerical improvements, exact values, and new proofs of known results are recorded separately.

## Counterexamples that the new route must face

- The joint estimate of the two Golomb classes, when applied to real fibers, controls`T(F_d)`;The summation results in a higher-order cube count, which cannot be directly written as a whole`T(A)≤2M(A)`.
- The exclusion of five-dimensional cubes is only a necessary condition; there are already high-energy collections without five-dimensional cubes, and the general linear source boundary cannot be proven solely by cube exclusion.
- F11(5), F12(7), F13(17) have been negated by full normal coloring; their weight arithmetic may still be correct, and Ramsey improvements that rely on them have no effect.
- The nine-step equilibrium theorem inside a three-dimensional complete source does not guarantee repairability when embedded in a larger source. There are counterexamples to fixed-boundary single-cell and double-cell repair; the eight-cell threshold for a specific instance is not a universal upper bound for all borders.
- Local gaps, mixed color corners or boundary corners can be reused by many blocks. Any summation must give a true multiplicity and cannot replace angle numbers with external grid numbers or unlabel a labeled injective.
- For fixed A,`2|E(Γ_z)|−Σ_ds_d(z)²=2T(A)−M(A)`Nothing to do with coloring z. Optimizing shading can reduce forced edges or imbalances, but cannot change the number of corners of A; further independent global budgeting is required.

Counterexamples only deny the exact proposition. Routes with additional assumptions, changeable boundaries, weighted amortization, or different invariants can still be continued. When retrying a failed mechanism, explain how the new condition handles known counterexamples; expanding the same search or changing the name does not count as a barrier to resolution.

## Turn exploration into usable evidence

Implementation and delivery details are provided in [Evidence and Reproduction](references/evidence.md).

- `PROVED`: Complete proof that all external inputs are locatable, assuming they match the object.
- `CONDITIONAL`: The conclusion clearly depends on a proposition that has not yet been established; the dependencies are listed and cannot be upgraded to an unconditional bound.
- `CONJECTURE`: Limited samples, heuristics or guesses; write the counterexample search range.
- `COUNTEREXAMPLE`: Complete object and constraint-by-constraint verification, indicating negative quantifiers and scope.
- `FINITE-CHECKED`: Exact finite fields, encodings, coverages, and certificates checked; no extrapolation to arbitrary scale theorems.
- `UNDECIDED`: Timeout, UNKNOWN, naked UNSAT status, missing certificate or unclear input. Rebutted and superseded records are labeled separately`REFUTED`,`SUPERSEDED`, retain the original evidence.

The construct checks all colors and all positive steps L with independent physical grid verifiers. Available`scripts/check_coloring.py`Read explicit square or source certificates; see evidence file for input format. The verifier does not solve the SAT, prove the rainbow minimum, or turn the source certificate into a square lower bound.

Computing impossibility requires verification of bidirectional equivalence of codes, solutionability of all symmetry constraints, complete branch coverage, and every unsatisfiable proof. Independently checkable certificates such as DRAT/LRAT are preferred. Not finding a solution once, failing all branches taken, or rejecting a model do not prove an upper bound.

Update the text only if necessary to make affected mathematical changes; complete proofs or counterexamples in a separate directory first. After relevant changes are made to the main manuscript finite certificates, rerun the main verifier. Lean's historical coverage, current source code, current compilation, and proposition-by-proposition correspondence are stated separately; conditional propositions will not become proven because Lean accepts their inferences.

To determine the novelty of a document, you need to read the original source and limit the scope of the search. The failure to find similar methods does not mean that the originality has been proven. The asymptotic bounds of unknown absolute constants cannot directly give three-color numerical bounds.

## Continuation, promotion and delivery

Each meaningful checkpoint saves: the exact proposition, the current state, the original input and SHA-256, the command and actual run range, a proof or counterexample file, the first unresolved derivation, and the next distinguishable check. Use the existing state mechanism of the warehouse; do not add another set of ledgers if it is not necessary.

Before stopping a route, differentiate between "proposition is denied", "specific method fails", "implementation error", "budget exhausted" and "continuation that has not yet been attempted". Unfinished feasible continuation paths retain restart conditions. One route failure does not end the authorized overall research; when the user only requires writing a workflow or has clear resource boundaries, do not initiate indefinite solving without authorization.

For effective new mechanisms, maintain a generalization table: the number of required source colors, whether the two-color complementarity is essentially used, the dependence of the state number or constant on k, the missing three-color source lemma, and the expected scope of application. Four-color only performs necessary small-scale inspections or advances according to clear user requirements; do not confuse three-dimensional/four-dimensional cube dimensions with three-color/four-color.

The report first answers whether the original goal has been achieved, and then gives the exact results, methods, evidence, and limitations; the upper and lower bounds report the current changes respectively. If only partial lemmas, counterexamples or certificates are obtained, state their value accurately and do not convert the amount of research activities into a percentage of "close to proof".
