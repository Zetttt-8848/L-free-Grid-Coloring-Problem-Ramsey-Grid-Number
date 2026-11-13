# Warehouses, Definitions and Evidence Maps

This is a navigation snapshot when creating the skill on 2026-11-08. Subsequent use shall be subject to actual submission, current proof and valid certificate. The project results in this document represent that the warehouse has provided corresponding certification or limited evidence, and do not mean that this independent audit or document priority audit of all certifications has been completed.

Latest: [Six types of completion figures are counted together](../../../../research/kernel_compatibility_20261108/README.md), base submission`654cc044cad3d8ca6079a1931565a6ec44dcf2b5`. The project range is now`21≤R3≤464`. The common minimum starting point count gives a complete 464 proof; the colored adjacent comparison layer paths provide further common budgets. The user made it clear that the current focus is on inventing an upper bound counting method and not starting a new lower bound SAT search. The next numerical target of 463 has not yet been achieved. Subsequent paragraphs 465 and 493 retain their historical or documentary meaning.

For follow-up research on the same day, please see [Boundary Compatibility Checkpoint](../../../../research/boundary_extension_20261108/README.md): The 45-lattice counterexample that full-source optimality does not guarantee three-dimensional block balance, the four-sided expansion obstacles and necessary internal modifications of the literature 20×20 matrix, and the applicability check of new literature in 2026. The following creates a snapshot that is retained; the checkpoint is also read during the continuation, and shortcuts that are negated by its exact counterexample cannot be attempted again.

Later checkpoint: [Three-color joint constraints](../../../../research/coupled_budget_20261108/README.md), based on PR4`df6e35cfff68580dc78aa91bc35d4c6399a6464a`. The current project interval is updated to`21≤R3≤465`: Two external Golomb dependencies of the historical direct convolution proof have found the original completion announcement, and reconstructed the proof and independently verified it accurately; do not rely on the invalid rainbow hypothesis. The new joint endpoint lemma of this round gives 466 independently. The main manuscript has not yet been incorporated into these reviews. There are also irreparable certificates for a single defective 21 square with a radius of 10, as well as a counterexample of a local forced imbalance being offset by an external same-fiber lattice. The following 493 still refers to the document baseline at the time of creation.

## 1. Source level and version

| Source | Fixed version at creation | Purpose |
|---|---|---|
| master branch |`080822bb1d434b164a1f42ea159d0bf148396b71`| Current mathematical master manuscript, clarified conditional results, literature and roadmap |
| [PR 1](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/1) | `d6755b48f1fb6e786cc9b480b0d40139f3da2140`| Forced edge minimization and nine-step equilibrium for three-dimensional sources |
| [PR 2](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/2) | `7f8e8bfc4d5c8d46664764c6ca0a534bd6a90962`| External single cell blocking, border coverage budget |
| [PR 3](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/3) | `a53970c49472813ac65d37428074e5c530134e76`| Double-grid repair counterexample, precise eight-grid threshold for selected instances |

When created, the three PRs were all open and unmerged, with the last branch as the base in turn; the tree of PR 3 contains the research files of the first two PRs. Don't just read main and miss these obstacles, and don't just replace the main branch with an entire research branch. PR status is variable information and will be read again when the connection is continued.

Main manuscript entry: [fixed version main.tex](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/blob/080822bb1d434b164a1f42ea159d0bf148396b71/manuscript/main.tex). Use LaTeX tag positioning to avoid relying on line numbers that drift.

Prioritization: Current theorems and complete proofs/certificates → Corresponding source versions and scope → Explicit revisions in the latest branches of research → Historical exploration. Historical findings can be re-verified, and historical "passed" does not automatically overwrite the current draft.

## 2. Objects, symbols and assumptions that cannot be omitted

| Notation | Precise meaning |
|---|---|
| `[n]²`| Complete square, text coordinates are 1 to n |
| `V(A)`| All`u<v`actual source format`(v,u)`, A is a finite set of integers |
| `W(A)`| plus all`(u,u)`Weak source of |
| `𝒯_m` | `V({0,…,m−1})`, including`binom(m,2)`Complete strict triangle of lattice |
| `m=|A|`| Number of markers; avoid mixing with square side length n |
| `M(A)` | `binom(m,2)`, strict source lattice number |
| `L(A)` | `max A−min A`, is the span; the number of interval grid points is`L+1` |
| `F_δ(A)` | `{u:u,u+δ∈A}`,δ>0;`r_δ=|F_δ|` |
| `T(A)`| The number of all geometries L in the strict source, not the number of monochromatic angles |
| `E(A)`| The ordered four-tuple satisfies`a−b=c−e`The quantity of is equal to the sum of the squares of the ordered sum representation number |
| mixed corner | Parallel input of different colors; automatic normalization for two-color sources |
| forcing corner | Parallel input of the same color; in a normal two-color source, the completion grid can only take another color |
| rainbow | The three colors are different in two and two, and may only appear when there are at least three colors |

The source angle can be uniquely written as`(u+δ,u),(v+δ,u),(v+δ,v)`,in`u<v∈F_δ`. δ is the fiber offset and the actual L step size is`v−u`, the two cannot be confused.

Inherit weak shading as`w_δ(v,u)=z(v+δ,u)`, defined in`W(F_δ(A))`; Its two pairs of character classes are Golomb sets. Two-color decomposition occurs at the starting point set of fibers, not automatically at A.

No carry condition also needs to be distinguished: positive weight separated means`w_(i+1)>2Σ_(j≤i)w_j`;2-dissociated means that the coefficient is in`{-2,-1,0,1,2}`The zero relation can only be trivial; injective only requires that the subset sums are different. The former implies the latter in turn, and the converse generally does not hold.

The transposition between documents of different orientations is a correspondence between problems, and is not a solution-preserving symmetry that can be applied in any square coloring. source mark reflection`t↦c−dt`corresponding on the grid point`(x,y)↦(c−dy,c−dx)`;retain d>0. Each additional symmetry constraint in SAT requires its own representative existence argument.

## 3. Reusable exact identities

text`prop:counts`,`cor:span`:

```math
\sum_{\delta>0}r_\delta=M,\quad
T=\sum_{\delta>0}\binom{r_\delta}{2},\quad
E=2m^2-m+4T,\quad
T\le CM\ \Longrightarrow\ M\le(2C+1)L.
```

text`thm:forcing`where z is taken as ±1,`s_δ=Σ_(u∈F_δ)z(u+δ,u)`,`Φ=Σs_δ²`, the vertices of Γ are the real source lattice:

```math
|E(\Gamma)|=2H,\qquad
H=\frac{2T-M+\Phi}{4},\qquad
2T=M+2|E(\Gamma)|-\Phi.
```

Γ is a simple bipartite graph with no cycles when edges are oriented with increasing offsets; these necessary conditions are not sufficient by themselves to give the required edge budget. A local decrease in Φ will simultaneously decrease H, but`2|E(Γ)|−Φ`Invariant on fixed A.

## 4. Numerical starting point that has been verified by the academic community

As of the original text verification within this limited scope, adopt`R₂=5`,`21≤R₃≤493`. This is not a statement that "all subsequent literature has been exhausted."

| Original source and version | Available conclusions and positioning | Boundaries of use |
|---|---|---|
| Axenovich–Manske, Integers 8 (2008), A21, [Journal Article](https://math.colgate.edu/~integers/i21/i21.pdf)| Two-color accurate datum; cross-checked with Canakci et al. Theorem 2.2 | Convert its L convention first, it cannot be applied to any three right-angled points |
| Canakci et al., [arXiv:2312.01159v1](https://arxiv.org/html/2312.01159v1), 2023-12-02 | Theorem 3.1 vs. Figure 1: Full 20×20 normal tristain, so`R₃≥21`| The calculation structure proves the existence, but does not prove that 21×21 does not exist |
| Mammel–Smith–Yerger, Integers 25 (2025), A21, [Journal Article](https://math.colgate.edu/~integers/z21/z21.pdf)| Theorem 6, PDF pages 10–11:`R₃≤493`, Algorithm 3 | Distinguish Golomb span from number of available positions; early middle bounds differ between abstract and text |
| Jaber–Liu–Lovett–Ostuni–Sawhney,[arXiv:2504.07006v2](https://arxiv.org/html/2504.07006v2), 2025-07-14 | Theorem 1.1, finite Abelian group standard corners density bound, index`1/600`| It is a non-zero group step size version; switching to this project requires direction and no wraparound bridge |

`literature/KNOWN_RESULTS.md`With two copies of BibTeX providing wider access to the literature, not every result is included in this re-audit. General corners input by the main draft`lem:H`,`lem:J`,`lem:embed`After conversion there are`R_k≤exp(O((log(2k))^600))`;Constant is unspecified and does not give the available trichromatic numerical improvements. The stronger exponent of the finite field model cannot directly replace the exponent via ordinary binary encoding.

The original master branch did not contain a separate 20×20 full matrix certificate;`exploration/research_round2/checks/cache_legacy20.py`References to old native files that were not imported. This skill comes with new`assets/paper20.json`: Obtain the matrix from the local supplementary material and compare it with [Figure 3 of Mammel et al. v1](https://arxiv.org/html/2502.05162v1#S3)All 400 values ​​matched one by one, checking all 2,470 corners in the direction of this project, with zero monochromatic corners. It is a replication of an existing literature construction, not a new lower bound, and does not rely on 4×4 cropping to prove the existence of complete squares.

## 5. The project has concluded and open dependencies

| Project objects | Master positioning | Available content/restrictions |
|---|---|---|
| Union of two disjoint Golomb sets |`thm:energy`,`cor:imbalance` | `T≤min(2M,M+5ρ)`and imbalance losses; before application, check that there are indeed two Golomb decompositions in the integrated set |
| Actual fiber |`cor:moments`| Sum control`K₃=ΣT(F_δ)`;not the same estimate of the overall T |
| cube |`lem:capacity`,`cor:occupancy`,`thm:fourcube`| Five-dimensional injective cubes are excluded; separated four-dimensional sources exist complete normal two-color coloring |
| Three-dimensional mixed extreme value |`thm:nine`| The minimum mixed is 9, obtained under 2-dissociation; not the minimum forcing |
| Six-mark extreme values ​​and classification |`prop:six-point-extremal`,`prop:six-mark-classification`| The maximum normal two-color source is T=16, E=130; the congruent sign type is classified by the proof, and the limited enumeration is only supported |
| Complete product, complete direct sum |`thm:progression`,`thm:direct`| There must be integrity and separation; filling in sparse gaps may destroy colorability |
| Paired Panning |`thm:matching`| It is required that the two translation sets do not intersect and the difference range is not required to be separated |
| Two distance geometry |`thm:two_distance`,`thm:midpoint-three`| Need to include the preservation of the sum relationship and the exact distance ratio of duplicate tags; not all sources meet |
| Graph encoding source |`thm:graph-source`,`prop:weight-two-family` | `A_G={5^i+5^j:ij∈E(G)}`,`T=2C₄(G)`; Strings are allowed on the four rings. The complete family of graphs forces the universal T/M coefficient to be at least 2 |
| No high-energy examples of five-dimensional cubes |`prop:cube-free-energy`| There is no claim that there is normal dichromatic source coloring in this family; it is only denied that "arranging cubes is enough" |

Open chain:`EP10 ⇒ H10 ⇒ S21`;`G9 ⇒ G9^exists ⇒ M≤20L`. G9 is not the same quantifier as existential G9: the latter simply chooses one coloration for each colorable source. The text range of S21 is`L≤99,994`.

The main manuscript condition value is: S21 lower`R₃≤379`,`R₄≤98,777`;Appropriate span memory under type G9`R₃≤361`. These numbers do not replace the unconditional starting point. History 465 has restored the direct convolution proof and external input one by one at the above joint constraint checkpoint, and can be used according to its clear evidence scope. The old values ​​​​of 459, 455, 454, four-color forms and the old general K-color targets must still be restored one by one. The restoration of 465 cannot lead to the restoration of other numbers, nor can the independent certification be completely rejected because of the failure of the rainbow route.

## 6. Key additions to the three research strands

| Files (in the respective commit tree) | New information | Boundaries that must be preserved in the next step |
|---|---|---|
| `research/three_cube_forcing/README.md`| The minimum Φ in the positive 2-dissociated three-dimensional source is 4, the forcing angle is at least 6, and the forcing edge is at least 12; there are at most nine legal single-cell descents inside | The mixed minimum of 9 in the main manuscript is still correct; the two extreme value targets are opposite. The specific rules for direct four-color dimension extension are invalid |
| `research/three_cube_boundary/README.md`| Fixed external color can block all internal single-cell paths; bounded coverage inequality and local budget | The analytical coefficient 8 and the coefficient 6 isomorphic to the enumeration combined with constraints are marked separately; the budget is for Φ_Q within the block |
| `research/three_cube_pair_repair/README.md`| The two-grid non-increasing repair is negated by the six-grid invariant; the complete state diagram with fixed boundaries selected gives a minimum step radius of 8 | The minimum Hamming distance directly to equilibrium is 12; unlike the path's maximum step radius of 8. 8 Non-arbitrary universal upper bound |

Boundary record usage`Q={0,1,5,6,25,26,30,31}`,`A=Q∪{2}`. Two blocking records have different external coloring and cannot be confused with the same witness. Full-bound C++ search aggregation differs from stand-alone Python exhaustive coverage of selected boundaries.

## 7. Locate code and history by problem

- Current certificate:`manuscript/verify_directed_L_manuscript.py`;Additional moment:`manuscript/check_energy_examples.py`.
- Rainbow CNF and total model verification:`manuscript/encode_rainbow_sat.py`,`manuscript/SAT_USAGE.md`. This tool does not run a solver, nor is it a general complete square solver.
- Nether:`exploration/research_round3/lower/ENCODING.md`,`SUBTASK_REPORT.md`,`build_instance.py`,`check_rup_proofs.py`. Historical side-21 work still has pending branches and cannot synthesize global conclusions from local UNSAT.
- Global instances with insufficient local conditions:`exploration/research_round3/joint/REPORT.md`and`triangle_core*.json`. A one-dimensional feasible label set does not necessarily have a complete triangular continuation.
- Global billing:`exploration/research_round4/research/ANCHORED_REFLECTED_PRODUCT_FORCING_0045.md`,`fibers/PARTIAL_FORCING_BLOCK_LABELS_0046.md`,`fibers/SEMI_INDUCED_BLOCK_DENSITY_0046.md`,`fibers/COMPANION_FORCING_CUBE_SLOTS_0046.md`.
- Invalid route:`SPAN_COMPRESSION_OBSTRUCTION.md`,`THREE_COLOR_ENERGY_BARRIER.md`,`FINITE_FIELD_TRANSFER_OBSTRUCTION.md`, all in the same round4 research directory; specific counterexamples only constrain their respective assertions.
- Historical formalization:`formal/README.md`,`formal/historical_records/SCOPE.md`,`coverage.json`,`manuscript_revision_crosswalk.json`. See the current module and corresponding check entrance.`formal/lakefile.lean`,`AllAxioms.lean`,`CountingAxiomAudit.lean`.
- Original import scope:`docs/IMPORT_SCOPE.md`,`exploration/README.md`. The old script contains local paths, missing external files and optional dependencies; first adapt and then run in the isolated output directory, retaining the original input.

During the creation process, it was also discovered that the local untracked`lfree_sat/`, which is not part of the pinned GitHub commit mentioned above. This time we only read its description, problem contract, verifier entry and literature matrix, and do not modify or authenticate the directory as a whole. Its README lists core feedback, hit set repair, and same-budget ablation as exploratory work, and makes it clear that no speedup has been demonstrated, and no 21×21 legal structure has been found; the corresponding input, source code, and reports must still be verified before using these historical experiments. Deployment of this skill does not rely on this local directory. The complete benchmark has been separately verified and standardized.

The full index includes all paths, Git blobs, SHA-256 for each pinned version, as well as Python declarations/imports, Lean declarations/imports, Markdown headers, JSON top-level structures, and CNF headers. The actual scope of the text and mathematical review can be found in`docs/RESEARCH_SKILL_REVIEW.md`.

## 8. Global count continuation checkpoint

`research/global_counting_20261108/README.md`Records are based on commits
`5b5db22c3c65123193cb31f2aa5bd949b3075e1a`A new round of parallel upper bound research.
The six-box conflict counting and quantification of cross-source color requests must have L cost, full-level regression and double-ended matching,
The common span cost and span translation overlap moment for extreme shapes have been independently proven and reviewed.
Under the assumption of a normal square of order 463, the overall number of span 425 completion classes is at most 56, which is better than the stepwise length of 74;
No contradictory unified estimates have yet been obtained. The current range is still 21 to 464.
At this stage, the user requested to give priority to the invention of a purely mathematical upper bound count with greater compression potential, and no lower bound SAT search was carried out.
Details and pending bridges are subject to the current certification and review of the catalog; this navigation is not to be regarded as a certificate of certification.
