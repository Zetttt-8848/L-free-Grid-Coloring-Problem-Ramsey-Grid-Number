Continue the Directed L-Free Grid Ramsey project at https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number] Develop and rigorously verify new methods that improve the upper bounds for both R_3 and R_4, going beyond straightforward reuse of the existing diagonal/Golomb/convolution approach.

Follow AGENTS.md and use the project-specific skills. Load .claude/skills/lgrid-research/SKILL.md and perform its state refresh before starting. Use lgrid-invent when developing methods and lgrid-verify when evaluating evidence, consulting literature, or reporting results.

Fetch the latest remote state and inspect all branches and relevant pull requests, including unmerged collaborator contributions. Identify and read their distinct research contributions, reuse shared context, and record the relevant commit identifiers. Establish the current verified bounds, known obstructions, and unresolved questions from their supporting evidence. Do not assume that main contains all progress. State any access or review gaps accurately.

Preserve the problem definition: the forbidden monochromatic configuration consists of (x,y), (x+d,y), and (x+d,y+d), where d is a positive integer and all three cells lie inside the grid. An upper bound R_k <= n must exclude every coloring of the n-by-n grid using at most k colors. Keep conditional results separate from unconditional bounds.

Select a promising unresolved upper-bound task and carry it through a concrete research cycle: formulate a precise claim, develop a proof or algorithm, test it against known obstructions, and verify the resulting evidence. Four-color research is an active objective, not deferred until the three-color problem is solved. Use lower-bound examples when they help discover structure or refute a claim. Check carefully whether arguments relying on binary sources remain valid for four colors.

Aim for substantive methodological advances. Compare promising methods with relevant primary literature and distinguish new mechanisms from parameter tuning. Preserve useful counterexamples and negative results. If a candidate fails, record its precise failure and move to a justified alternative.

Produce reviewable mathematical artifacts: theorem statements, complete mathematical proofs where available, implementations, explicit witnesses, reproducible experiments, and verification results. Provide concise summaries of conclusions, assumptions, and limitations. Internal model deliberations or private reasoning transcripts are not requested.

Label results accurately as proved, conditional, conjectural, finite-checked, refuted, or undecided. A timeout, unsuccessful search, or unsupported solver status does not prove an upper bound. Computational impossibility claims require a justified encoding, complete coverage, and appropriate checkable evidence.

Keep GitHub updated at each meaningful checkpoint during this session. I explicitly authorize creating research branches, committing task-related changes, pushing them to this repository, and opening or updating relevant pull requests. Save substantive results promptly, including useful negative findings, rather than waiting for a final breakthrough. Clearly label exploratory work and distinguish it from verified results.

Place new research in the designated dated directory on a research branch. Preserve existing uncommitted work and collaborator changes. This authorization does not include force-pushing, deleting branches, rewriting history, merging pull requests, or rewriting the shared manuscript.

Write all new or modified project content and GitHub descriptions in professional English. Preserve mathematical meaning when translating. Before committing, run relevant validation and python scripts/check_english_only.py. After pushing, verify the remote commit and record its link. If synchronization fails, preserve the local work and report the actual blocker.

Begin with the state refresh, then proceed into substantive research. Finish each major checkpoint with a concise account of the result, verification performed, remaining limitation, GitHub location, and next research action. Before ending the session, publish completed checkpoints where possible and leave enough information for the next session to resume reliably.
