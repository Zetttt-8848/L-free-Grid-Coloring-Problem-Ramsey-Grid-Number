# Directed L research skill: source and inspection scope

Compilation date: 2026-11-08. The delivery goal is to develop a project research workflow for sustainable use; there are no claims to address R₃, obtain new unconditional bounds, or complete an independent audit of full warehouse certification.

## Delivery files

- [SKILL.md](../.agents/skills/directed-l-grid-research/SKILL.md): Exact problems, upper and lower bound parallelism, method screening, counterexample constraints, evidence status and generalization conditions.
- [Study Map](../.agents/skills/directed-l-grid-research/references/repository-map.md): Positioning of main manuscript, documentation, open dependencies, research PR and historical code.
- [Routes and Obstacles](../.agents/skills/directed-l-grid-research/references/routes.md): There are five groups of routes in the upper bound and four groups in the lower bound, each with its first gap, judgment experiment and success conditions; these groups are candidate menus and are not required to be exhausted one by one.
- [Evidence and Reproduction](../.agents/skills/directed-l-grid-research/references/evidence.md): Certificate format, verification command, SAT/Lean range, cross-session recording.
- [Complete literature benchmark](../.agents/skills/directed-l-grid-research/assets/paper20.json): Normal 20×20 tri-stain with original source.
- [Construct Verifier](../.agents/skills/directed-l-grid-research/scripts/check_coloring.py)with [source code indexer](../.agents/skills/directed-l-grid-research/scripts/index_repository.py): Both rely only on the Python standard library.
- [Full source code index](RESEARCH_SKILL_SOURCE_INDEX.json)With [this inspection record](RESEARCH_SKILL_CHECKS.json).

Skills are placed in project directories`.agents/skills/directed-l-grid-research/`, available in a project session as`$directed-l-grid-research`Call; for discovery behavior and directory conventions, please refer to [OpenAI official description](https://developers.openai.com/api/reference/cli). The preloaded skill list of the current session may not be hot updated and will be called in a new session of this project when necessary.

## GitHub scope

Obtain repository metadata, root directories, Issue/PR queries, and PR status via the GitHub connector; then clone locally to support full file indexing and limited validation. Create a working branch`codex/directed-l-research-skill`. No remote PRs have been committed, pushed, merged, or modified.

| Fixed input | Submit | Number of files in the tree |
|---|---|---:|
| main | `080822bb1d434b164a1f42ea159d0bf148396b71` | 1,082 |
| PR 1 head | `d6755b48f1fb6e786cc9b480b0d40139f3da2140` | 1,091 |
| PR 2 head | `7f8e8bfc4d5c8d46664764c6ca0a534bd6a90962` | 1,102 |
| PR 3 head | `a53970c49472813ac65d37428074e5c530134e76` | 1,114 |

When created, PR 1–3 were not merged and were in series dependence. The index retains all paths of each tree and deduplicates the same blob; different versions of the same path are recorded separately. It doesn't just list directories by file name: it reads all raw blob bytes, parses Python/JSON syntax, extracts Lean declarations, Markdown headers, LaTeX tags and CNF headers, and no corresponding parsing errors are found. Grammar is proven correct by not stating program logic or mathematics.

## Reading depth

The scope of intensive reading includes the project README, all collaborations/goals/open issues/documentation descriptions, the definition and main proof chain of the main mathematical draft, conditional numerical transfer, failure rainbow premise and certificate description, the geometry and constraint logic of the current verification/encoding, the formal scope and version record, as well as the complete research description, proof and counterexamples of the three PRs. The historical reading focuses on lower bound encoding and pending records, obstacles to the non-continuation of local feasible sets, the multiplicity problem of global accounting, source span compression counterexamples, energy methods and failure boundaries of finite domain transformations.

The remaining historical documents and codes have completed the full file structure index and are positioned according to the research mechanism; **all historical programs and all historical proofs have not been manually reviewed line by line**. This time, we did not re-run all historical searches, reconstruct Lean, or prove that the current full text is consistent with the historical formalization item by item. When using the skill later, the original proof and implementation will be read according to the work package. This report cannot be regarded as a certificate of correctness of the entire database.

The workspace also has untracked directories that are not part of the pinned GitHub commit`lfree_sat/`. This time, we only perform relevant read-only positioning, find the literature matrix from it, and then independently re-match it with the original paper. This directory remains intact and is not covered by this new file or the full database Git index.

## Actual verification

1. Master Verifier rerun passes all 13 sets of limited checks. It verifies specified tables, structures, partial equal sign cases, and numerical arithmetic, but does not verify all theorems of any scale.
2. The two complete SAT models marked by 11 and 12 pass CNF and independent geometry checks; it still only proves that the specified coloring is feasible, but does not prove that the rainbow number is minimum.
3. The selected fixed boundary of PR 3 is re-exhausted from the original witness to reproduce the legal state, equilibrium state, repair closure and accurate eight-square threshold. No rerun of full outer bounds C++ search.
4. The new construction checker is compared to another implementation of "Determine geometry after traversing all unordered triads", covering all dichromatic squares with side lengths up to 3, and checking for orientation discrimination, weak/null sources, illegal input and existing triangle certificates.
5. The literature 20×20 matrix matches all values ​​of Figure 3 of arXiv:2502.05162v1 HTML, and is checked by two geometric enumerations; the complete benchmark has been written into this skill.
6. The integer threshold arithmetic for the conditions q=20, 21, and 27 has been recalculated; the cross-term accounting formulas of the global situation and the local situation have been expanded with accurate polynomials and checked with rational values. The unverified source budget remains unverified.
7. The skill structure has passed the verification, and the supporting links, files, instructions and script interfaces have been self-reviewed; there is no claim to have conducted independent agent behavior evaluation.

The full master copy reproduced report and the PR 3 reproduced report are kept in the work results directory for this session; a summary for use with the repository, input/checker summary and actual scope are recorded in [RESEARCH_SKILL_CHECKS.json](RESEARCH_SKILL_CHECKS.json). The Git blob hash uses the raw bytes of the repository; the SHA-256 running the verifier uses the actual input file, and Windows newlines may make the two different and cannot be mixed.

## Core items for independent and accurate review

The following PASS only covers the finite certificatess and arithmetic specified, and does not cover universal optimality, open premises, or document priority. Accurate computing environment self-test has been run before independent inspection and obtained`ENVIRONMENT OK`.

CLAIM: Geometric angle number and monochromatic angle number of 20×20 literature matrix | MY VALUE: (2470,0) | THEIR VALUE: (2470,0) | VERDICT: PASS | METHOD: Enumerate unordered three-point groups from the complete matrix and determine the specified direction and equal-leg conditions, and check cross comparison by horizontal point pairs

CLAIM: Eleven marks the number of monochrome angles and rainbow angles of a given triangle | MY VALUE: (0,3) | THEIR VALUE: (0,3) | VERDICT: PASS | METHOD: Reconstruct all grid points from the original line words, traverse the three-point group to determine geometry and color

CLAIM: Twelve marks the number of monochrome angles and rainbow angles of a given triangle | MY VALUE: (0,6) | THEIR VALUE: (0,6) | VERDICT: PASS | METHOD: Reconstruct all grid points from the original line words, traverse the three-point group to determine geometry and color

CLAIM: Angular and additive energy for a given six-labeled source | MY VALUE: (16,130) | THEIR VALUE: (16,130) | VERDICT: PASS | METHOD: Corner-by-corner counting from the complete grid points and recalculating the energy from the sum of the squares of the sum of all ordered labels

CLAIM: Strict margin of diagonal contradictions for q=20, 21, 27 | MY VALUE: (60,63,81) | THEIR VALUE: (60,63,81) | VERDICT: PASS | METHOD: Direct recalculation of the point logarithm of ceil((18q+1)/3) markers minus q(18q); arithmetic only, no proof of source budget

CLAIM: The cross term in the local potential expansion is 2eΔs | MY VALUE: 0 | THEIR VALUE: 0 | VERDICT: PASS | METHOD: Exact polynomial expansion of the difference on both sides and exact comparison at 0, 1, 1000000, 2/3 parameters

## Mathematics editor self-review

The scope of the review is only for newly written skills, three reference files, and mathematical notations and cross-references in this report. text`manuscript/main.tex`, the original mathematical proofs, historical status and certificates have not been modified. No mathematical token changes have been made to the old manuscript; the newly written conditional examples still explicitly retain the conditions and do not record them as new numerical results.
