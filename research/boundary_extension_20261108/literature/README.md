# Literature check and research transfer — 2026-11-08

Base: `080822bb1d434b164a1f42ea159d0bf148396b71`. Scope: directed, positive-step, equal-leg three-point L on the **complete integer square**. This is a source and application audit, not a claim that every cited theorem has been independently reproved. Dates below are source dates, not search-engine age labels. Source-response hashes are in `source_inventory.json`; full texts were read in memory and are not redistributed.

## Search outcome

The strongest directly applicable published numerical comparison found remains **21 ≤ R₃ ≤ 493**. No later primary source improving that interval was found in this bounded search; absence is not proof that none exists. Newer 2026 papers were located and read, but their hypotheses or unresolved source steps prevent importing a stronger numerical L-grid bound.

Wiley Scholar Gateway returned `UNAUTHORIZED`, requiring reauthentication. It supplied no literature evidence. Searches used the web index, arXiv primary records/full text, Integers, Cambridge Core, and citation leads subsequently checked at primary sources. Full citation-index coverage, paywalled database coverage, and a global novelty verdict remain unavailable.

## Core sources and reading scope

### C23 — Canakci et al., *On SAT Solvers and Ramsey-type Numbers*

[arXiv:2312.01159v1](https://arxiv.org/html/2312.01159v1), 2023-12-02. Read the complete L-specific Sections 2–3, including algorithm descriptions; the separate polynomial van der Waerden sections were outside scope.

Theorem 3.1 gives 21 ≤ R₃ ≤ 2593, using a complete 20×20 witness for the lower endpoint. Theorem 2.2 records R₂=5. The search preserves exactly one color per cell while changing colors; this mechanism and parallel random restarts are prior art. Its probabilistic solver's negative return is explicitly not a nonexistence proof. Source formulas use both transposed L descriptions; the coordinate dictionary must be fixed before importing a matrix.

Application: **verified after orientation translation** for the existing lower-bound benchmark; this report does not independently authenticate every pixel in its Figure 1. Novelty classification: **known after translation of notation**.

### M25 — Mammel–Smith–Yerger, *Ramsey Theory on the Integer Grid: The “L” Problem*

[Integers 25 (2025), A21](https://math.colgate.edu/~integers/z21/z21.pdf), published 2025-03-26; [arXiv:2502.05162v1](https://arxiv.org/html/2502.05162v1), 2025-02-07. Read all mathematical sections of the arXiv version (Sections 1–4), revisiting 2.2–2.3 separately, and journal pp. 10–12.

Journal Theorem 6 supplies 493 through forced diagonal Golomb classes and interval packing. The arXiv version additionally contains the complete Figure 3 matrix and SAT experiments. Triangle completion, right-column fixing, color fixing, and reverse-diagonal restrictions are already explored there. A 22×22 example is conjectured, not exhibited. The upper proofs of 772 and 493 are attributed to referees.

The printed Algorithm 3 is not directly executable: `ints` is undefined, loop increments are absent, and initialization needs interpretation. Replication must reconstruct the inequalities and trace Golomb capacities. This does not refute Theorem 6. Application: **published benchmark; independent algorithm reconstruction pending in this literature work package**. No originality claim is made for reusing these methods.

### J25 — Jaber–Liu–Lovett–Ostuni–Sawhney, *Quasipolynomial bounds for the corners theorem*

[arXiv:2504.07006v2](https://arxiv.org/html/2504.07006v2), 2025-07-14, latest revision shown by its primary record. Read Section 1, all proof-overview subsections 2.1–2.7, relative-sifting Theorem 3.5, and the full assembly proof in Section 7.2. The 73-page technical argument was **not** audited line by line.

Theorem 1.1 treats finite abelian-group standard corners with nonzero group step, giving density at most exp(−c(log|G|)^(1/600)). The finite-field exponent 1/178 in Theorem 1.3 has different hypotheses. The proof retains coordinate and sum restrictions in XYD containers, uses asymmetric relative sifting, and restores pseudorandomness under iteration. Theorem 7.9 is a counting version.

Application to positive integer L requires reflection/orientation and no-wraparound arguments. Constants are not supplied for a three-color numerical improvement. Status: **external theorem extracted; project transfer conditional on the existing bridge, not freshly audited here**. Overlap: **partial or adjacent result only** for boundary repair.

### S25/26 — Martin-Pizarro–Palacín–Wolf, *Stability, corners, and other two-dimensional shapes*

[Published article](https://doi.org/10.4153/S0008414X25101971), online 2025-12-26; PDF journal header says 2026. [arXiv:2210.14039v3](https://arxiv.org/abs/2210.14039v3), 2025-11-12. Read introduction, exact Theorems A/B, the scope of stationarity, and the finite-group application hypotheses; not the full model-theoretic proof.

Theorems impose density and scarcity of induced half-graphs. Theorem A additionally bounds group exponent; Theorem B uses abelian groups of odd order. They concern squares or 3×2 grids and qualitative constants. Their four-point “L-shape” is not the project's three-point L.

Application: **inapplicable as an unconditional numerical improvement** without new stability, quantitative, and integer-transfer lemmas. Overlap: **partial or adjacent result only**. This is a source of candidate structural assumptions, not evidence that every valid source satisfies them.

## New 2026 papers

### W26 — Wijaya, *Polynomial Corners Over Finite Fields*

[arXiv:2606.08890v1](https://arxiv.org/html/2606.08890v1), 2026-06-08. Read all Sections 1–4, including Proposition 4.1's proof. Theorem 1.1 concerns equal polynomial steps in integers; Theorem 1.2 concerns Fₚ and p>d².

The proposed transfer compares polynomial-step and linear-step corner counts. Definitions use a uniform normalized image weight, whereas the parameter-average operator induces preimage multiplicity. A displayed Fourier identity also mixes these measures. The exact mismatch is documented and independently reproducible in [WEIGHT_AUDIT.md](WEIGHT_AUDIT.md). The main theorem's exponent display and nonzero-step wording also require care; its proof uses the intended exp((c log p)^(1/600)) denominator.

Application: **unverified; do not import as a proved project dependency**. The finite diagnostic does **not** refute the stated norm inequality or final density theorem. A repaired weighted operator or a multiplicity-weight argument remains possible. Overlap: **partial or adjacent result only**.

### L26 — Li–Shen–Truong–Wu, *Polynomial corners in finite fields beyond the distinct-degree case*

[arXiv:2609.13891v1](https://arxiv.org/html/2609.13891v1), submitted 2026-09-12. Read Section 1 and full Sections 3–4, including fibre-energy estimates and threshold algebra. Sections 5–7's algebraic-geometric kernel proof were not fully audited.

Theorem 1.1 assumes bounded-degree polynomials vanishing at zero and **linear independence**. It states a density threshold Cp^(−1/14), improving the distinct-degree regime and treating equal-degree resonance. Its main term and error retain row/column energies rather than replacing both by coarse global norms.

The equal-leg substitution φ₁=φ₂ is excluded. Application: **inapplicable directly** to our L-grid numerical bound. The fibre-energy accounting is a methodological lead, not a transfer theorem. Overlap: **partial or adjacent result only**. This is the most recently submitted nearby primary paper located, not a claim of exhaustive recency.

### B26 — Bulj–Kovač, *On hyperbolic corners and unit-area triangles in planar sets of large measure*

[arXiv:2605.30033v1](https://arxiv.org/abs/2605.30033v1), 2026-05-28. Abstract/definition screening only, not a deep read: steps are t and 1/t in a measurable real square. This changes both geometry and domain. **Inapplicable** as a direct bound for equal integer legs; kept in the exclusion log to avoid keyword confusion.

## Our research deductions and proposed tests

These are our deductions, not theorems asserted by the cited papers.

1. **Keep the actual compatibility relation.** A boundary signature should describe which internal states can be extended through every crossing L, rather than only color counts or block-local potential. Two boundaries with equal counts can impose different clauses. First discriminate this on the PR 2/3 witnesses, retaining coordinates and support labels.
2. **Optimize a conditional state value.** For a fixed outside coloring with difference-fibre sums e_d, the correct objective on an inside state z is Φ_inside(z)+2Σ_d e_d s_d(z). A local minimizer of Φ_inside need not minimize this objective. The elementary square expansion is exact; usefulness for R₃ still needs compatible coverage of arbitrary sources and controlled overlap multiplicity.
3. **Retain joint terms before taking worst cases.** Instead of independently bounding “repair gain” and “boundary damage,” record their joint distribution on realizable states. A large damage term might force compensating structure; alternatively a complete witness may show no compensation. This can distinguish an actual inequality from a misleading sum of separate extrema.
4. **Use extension failure as a structured constraint.** Freezing a 20×20 interior tests one subfamily only. A failed extension should return actual blocking color assignments and identify which interior cells must be allowed to change. A new complete square is still required for a lower bound.
5. **Treat transference as an equality of weighted counts.** Coordinate maps can merge parameters. Before using a source count, derive its pushforward measure exactly. The W26 diagnostic illustrates this issue in a small independently checkable setting. The same discipline is needed for repeated source-completion resources.

No novelty verdict is claimed for these mechanisms. The next discriminating step is the finite boundary/extension work in the sibling research directories; no global source budget follows from this reading alone.

## Query and coverage log

Date horizon: through 2026-11-08; English mathematical terminology, directed L and adjacent arithmetic-combinatorial corners. Queries executed included:

- `"L" "grid" Ramsey Mammel Smith Yerger 2026`
- `"L-free" grid Ramsey 2026`
- `"corners theorem" 2026 quantitative`
- `"Ramsey Theory on the Integer Grid"`
- `site:arxiv.org "L" "Ramsey" "grid" "2026"`
- `site:arxiv.org "corners" "2026" bounds`
- `"Stability, corners, and other two-dimensional shapes" arxiv`
- `"2502.05162" "2026"`
- `site:arxiv.org/abs "corners" "quasipolynomial"`
- `site:arxiv.org/abs "Ramsey" "L" "493"`
- `"monochromatic" "L" "493" grid`
- `"corners" "quasipolynomial" "2026"`
- `"Polynomial Corners Over finite Fields" Wijaya arxiv`
- `"On hyperbolic corners and unit-area triangles" arxiv`

Later passes excluded irrelevant AI-note/blog and unrelated graph-L/corner terminology. Backward references were inspected in M25 and J25; forward leads to W26/L26 and the stability publication were authenticated through arXiv/publisher pages. This was a same-searcher second pass, not an independent novelty audit. No complete citation graph or exhaustive database export was obtained.
