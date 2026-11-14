<!-- Repository language policy: English only. -->
# Directed L-grid Ramsey numbers

A mathematical repository for collaborative research on forward L-grid Ramsey numbers. The complete proof, construction, and finite certificates of the current paper are at [manuscript/main.tex](manuscript/main.tex), references are saved separately in [references.bib](manuscript/references.bib).

Start with [Index of Propositions and Proofs](docs/RESULTS_INDEX.md), [Open issues and failure routes](docs/OPEN_PROBLEMS.md) and [collaboration agreement](docs/CONTRIBUTING.md).

Project instructions for agents: [AGENTS.md](AGENTS.md). Project skills: [lgrid-research](.claude/skills/lgrid-research/SKILL.md), [lgrid-invent](.claude/skills/lgrid-invent/SKILL.md), [lgrid-verify](.claude/skills/lgrid-verify/SKILL.md). Since 2026-11-13 the governing objective is to improve the upper bounds of both $`R_3`$ and $`R_4`$; the "R3 first, then R4" ordering below is superseded. The unconditional four-color baseline in the repository history is $`R_4\le21\,991\,300`$ ([report](exploration/research_round3/four/R3_R4_REPORT.md)); the figure $`98\,777`$ is conditional on S21. See the [state snapshot](.claude/skills/lgrid-research/references/state.md) and the [four-color sensitivity note](research/four_color_sensitivity_20261113/README.md).

Former workflow (now a pointer): [directed-l-grid-research](.agents/skills/directed-l-grid-research/SKILL.md). For the information and inspection snapshots when it was created, see [Compilation Report](docs/RESEARCH_SKILL_REVIEW.md); These historical records do not replace the current result verification.

Latest checkpoints: [Cross-source conflicts, double-ended resources, and extreme shape counting](research/global_counting_20261108/README.md). Parallel development of summable cross-color request conflicts, full-level double-ended matching, and common span costs has proven strict new capacity limits; smaller Ramsey upper bounds have not yet been introduced, and the current interval is still$`21\le R_3\le464`$. This round gave priority to the invention of pure mathematical upper bound counting, and did not carry out lower bound SAT search.

464 Proof: [Six types of completion cells count together](research/kernel_compatibility_20261108/README.md). The common occupancy count advances the item upper bound from 465 to 464, and the colored boundary count further connects adjacent steps.

Previous round: [Three-color joint constraints and repair distance](research/coupled_budget_20261108/README.md)Restore and verify historical 465 proofs, as well as independent 466 proofs and repair obstacles. New proofs and reviews are in the research catalog; not yet incorporated into the main manuscript.

2026-11-08 Research continuation: [Boundary compatibility, frozen expansion barriers and literature review](research/boundary_extension_20261108/README.md). Includes complete counterexamples of incompatibility between full-source optimality and local equilibrium, unilateral expansion barriers of literature 20×20 coloring, independent verification code and literature reading records; does not change the unconditional three-color interval.

## Problem

The forbidden directed equal-leg L consists of $`(x,y),(x+d,y),(x+d,y+d)`$ with $`d>0`$.
$`R_k(\mathcal L)`$ is the smallest side n such that every coloring of the n by n
square with at most k colors contains a monochromatic L. For a finite integer
set A, the strict source is $`V(A)=\{(v,u):u<v,\ u,v\in A\}`$.
The verified literature comparison is $`21\le R_3\le493`$; see
[known results](literature/KNOWN_RESULTS.md) for versions and hypotheses.
Research-checkpoint improvements must be read with their explicit dependencies.

## Current mathematical results

Each statement retains the hypotheses in its linked theorem. Consult the
proof before applying a result to a different source or domain.

- Exact counts: $`T=\sum_{d>0}\binom{r_d}{2}`$ and $`E=2n^2-n+4T`$. A bound $`T\le CM`$ implies $`M\le(2C+1)L`$.
- Two disjoint Golomb classes satisfy $`T\le\min(2M,M+5\rho)`$, with explicit imbalance and fiber-moment refinements. A bound on individual fibers is not a bound on the entire source.
- A properly two-colored strict source contains no complete injective five-dimensional cube. A complete 120-cell coloring of a separated four-dimensional cube attains dimension four.
- An injective three-dimensional cube has at least nine mixed corners; equality is attained under 2-dissociation.
- The physical forcing graph satisfies $`2T=M+2|E(\Gamma)|-\sum_d s_d^2`$.
- For properly two-colorable six-mark strict sources, the maximum is $`T=16,E=130`$. Equality types are translations, positive integer dilations, and reflections of $`\{0,1,2,3,4,6\}`$.
- A non-arithmetic set of $`n\ge3`$ marks satisfies $`T\le\binom{n}{3}-(n-2)`$, with energy deficit $`4(n-2)`$.
- Complete arithmetic products, complete direct sums, and paired translates have energy bounds $`9n^2-15n`$, $`(27n^2-25n)/2`$, and $`22n^2-41n`$, subject to their stated completeness, separation, disjointness, and colorability hypotheses.
- The two-distance representation gives $`T\le6M,M\le13L`$. If each midpoint has at most three long pairs, $`T\le2M,M\le5L`$; the coefficient two is asymptotically optimal.
- The graph encoding $`A_G=\{5^i+5^j:ij\in E(G)\}`$ satisfies $`T(A_G)=2C_4(G)`$, counting four-cycles with chords allowed. Complete graphs force any universal coefficient to be at least two.
- A construction containing no injective five-dimensional cube has $`E\ge\tfrac12n^{73/26}`$. No proper binary source coloring is claimed for this construction.
- Under the open S21 assumption, the conditional bounds are $`R_3\le379,R_4\le98777`$. The appropriate finite-span existence version of G9 would imply $`R_3\le361`$. These are open-premise implications, not established unconditional bounds.

The separately reviewed research checkpoints prove $`R_3\le464`$ using the six joint completion classes and cited Golomb inputs. See the checkpoint links above for the complete proof and its scope.

## Research goal: R3 first, then R4

The long-term main line is to simultaneously raise the lower bound on R3(L), ​​lower its upper bound, and ultimately determine the exact value with matching construction and impossibility proofs. After completing R3(L), ​​start the system research of R4(L). The existing R4 conditional corollary remains as background and is not used as the current main task.

The current priority is to invent a new counting method that can uniformly calculate cross-color, span-length, and cross-level constraints, and pursue greater upper bound compression. The proven consequences of new counts and the missing global estimates are clearly documented at each stage; methodological advancement and numerical boundary advancement are reported separately.

Original approach is the core goal. There are diagonal, interval, and Golomb methods as benchmarks; SAT, enumeration, and Lean for discovery, refutation, and verification. Merely adjusting the parameters of the old method or expanding the brute force search does not alone serve as the completion standard for the original mechanism.

For detailed staging, upper and lower bound routes and acceptance criteria, please see [Research Roadmap](docs/ROADMAP.md).

## Academic achievements and project achievements can be viewed separately

- [Academic achievements and original sources](literature/KNOWN_RESULTS.md): Exact values ​​of two colors, known bounds of three colors, density theorem and related inputs.
- [Literature database](literature/references.bib): Relevant literature entries, including sources of two-color results supplemented in this round.
- [Index of propositions and proofs of this project](docs/RESULTS_INDEX.md): The results and proofs in the paper cannot be used to automatically determine priority.
- [Open Assumptions and Failure Routes](docs/OPEN_PROBLEMS.md): Avoid treating conditional bounds or negated premises as existing upper bounds.

## Recurrence

```sh
cd manuscript
python verify_directed_L_manuscript.py --source main.tex --bib references.bib --output verification_results.json
latexmk -pdf main.tex
```

Python 3.10+, the main verifier only uses the standard library. SAT generation and model checking see`manuscript/SAT_USAGE.md`.
LaTeX requires TeX Live, BibTeX, latexmk and the macro packages used in the text. Lean construction ideas`formal/README.md`.

Table of contents:`manuscript/`Current certifications and certificates;`formal/`Formal source code and historical coverage records;`exploration/`Historical exploration, counterexamples, and failed routes;`docs/`Collaboration and status notes.

Personal information, cover page, acknowledgments, supporting disclosures, and defense materials from the complete paper are not imported. Preserving mathematical source attribution does not amount to claiming that all results are new. This repository does not grant copyright licenses to third-party documents.
