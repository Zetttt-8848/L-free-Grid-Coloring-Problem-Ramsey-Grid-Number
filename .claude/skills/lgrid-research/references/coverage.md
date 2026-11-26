# Coverage record

What has actually been read, and how deeply. Append dated entries; do not
upgrade a level without doing the reading. Levels:

- **Read**: the whole file, statement by statement.
- **Searched**: located by pattern search or read in part.
- **Inventoried**: seen in a listing, diff, or index only.
- **Rerun**: a checker was executed; says nothing about files it did not read.

## 2026-11-13, at checkpoint `dc1cbe6daf7d`

The checkpoint tree has 1,297 tracked files. This session did **not** review
the repository completely.

Read:

- `README.md`, `docs/ROADMAP.md`, `docs/OPEN_PROBLEMS.md`,
  `docs/RESULTS_INDEX.md`, `docs/CONTRIBUTING.md`,
  `docs/ENGLISH_ONLY_POLICY.md`, `literature/KNOWN_RESULTS.md`
- `research/global_counting_20261108/README.md` and `review/REVIEW.md`
- `research/kernel_compatibility_20261108/geometry/SIX_CLASS_LEMMA.md`
- `research/coupled_budget_20261108/numeric_upper/THEOREM.md`
- `manuscript/main.tex`: only the span-to-Ramsey section (`open:s21`
  through `thm:s21four`, including `lem:shift`) and the closing questions
- `.agents/skills/directed-l-grid-research/SKILL.md` and
  `references/routes.md`
- `origin/codex/recover-claude-calibration-20261113`: `README.md`,
  `baseline_scores.py`, `ceilings.mjs`

Searched (partial reading):

- `exploration/research_round3/four/R3_R4_REPORT.md` (sections 1-4),
  `R3_R4_OBJECTIVE.md` (head), `exploration/research_round3/STATUS.md`,
  `README.md`, `general/square_root_barrier.md`,
  `audits/fresh_astra/REVIEW.md` (verdict table)
- `docs/RESEARCH_SKILL_REVIEW.md` (first half), legacy
  `references/evidence.md` and `references/repository-map.md` (first parts)
- Repository-wide pattern search for four-color material and for the figures
  `21991300` and `22006246`

Rerun:

- `exploration/research_round3/four/verify_r4_profile_certificate.py`: PASS
  at `n = 21991300`
- `research/kernel_compatibility_20261108/geometry/audit_464.py` on a
  temporary copy: PASS, margin `477965143`

Inventoried only:

- Everything else, including the remainder of `manuscript/main.tex`,
  `formal/`, all of `exploration/` outside the files above (in particular the
  Round-2 lemmas FM1, FM2-4, FM3 that the four-color certificate inherits),
  `research/boundary_extension_20261108/`, the remaining files of the other
  `research/` packages, and pull requests 1-3 beyond their titles.
- Branches: tips and pull-request metadata for all remote branches were
  recorded (`pins.json`); their trees were compared by diff statistics only.
- The untracked `lfree_sat/` directory in the primary working tree was listed
  and not read.

External sources: OGR-24/25 announcements and the cited papers were not
reread; their use rests on the repository's own verification records.

## 2026-11-26, at checkpoint `b3bff4112585` (`codex/swarm-r3-r4-20261126`)

Read:

- `AGENTS.md`, `.claude/skills/{lgrid-research,lgrid-invent,lgrid-verify}/SKILL.md`,
  and all files in `.claude/skills/lgrid-research/references/`
- `research/r3_side138_20261126/`: `README.md`, `verify.py`, `inputs/provenance.json`
- `research/r4_mcf_minimax_20261126/`: `README.md`, `verify.py`, `rup_check.c`,
  `window_tables/provenance.json`, `zero_rainbow_witnesses.json`
- `research/binary_source_spans_20261126/`: `README.md`, `verify.py`, `verify_trees.c`,
  `witnesses_k2_k16.json`
- `research/weak_triangle_20261123/`: `README.md`, `PLAN_STATUS.md`, `SIDE_139.md`,
  `SIDE_140.md`, `SIDE_141.md`, `verify_full_square.py`, `rup_check.c`
- `research/r4_stratified_farkas_20261124/`: `README.md`, `verify.py`;
  `research/r4_subadditive_farkas_20261124/README.md`;
  `research/r4_disjoint_edge_bins_20261123/`: `README.md`, `verify_c20.py`
- `research/boundary_certificates_20261115/README.md`
- Unmerged sibling branch reports:
  `origin/codex/r4-local-capacity-round3-20261114` (`ROUND1_REPORT.md`, `ROUND2_REPORT.md`,
  `SHORT_DEMAND.md`, `ROUND3_REPORT.md`, `THEOREM.md`, `TOOLS.md`, `finite_caps.py`),
  `origin/claude/r4-grid-compatibility-20261114` (`ROUND1_REPORT.md`, `review_codex_r3/REVIEW.md`,
  `check_finite_caps.py`, `round2/NEXT_TARGETS.md`, `MX_STAGE1_RESULT.md`, `MX_STAGE2_RESULT.md`,
  `NTSD_F_ATTEMPT.md`, `CL_ATTACK.md`),
  `origin/claude/upper-bounds-20261114` (`README.md`, `pr11_review/REVIEW.md`),
  and `origin/kimi/r4-hybrid-dual-20261116` (`KIMI_RESEARCH_PLAN.md`, `ROUND1_REPORT.md`
  through `ROUND5_REPORT.md`, `THEOREM.md`).

Rerun (all PASS):

- `python3 research/r3_side138_20261126/verify.py` (in-repo and standalone out-of-tree copy;
  margin `+1,659,966,634` on `S_138`)
- `python3 research/r4_mcf_minimax_20261126/verify.py` (C99 `rup_check`, `--pure-python`, and
  external `drat-trim` on all 11 `.rup.xz` proofs; margin `+67,076,013,380,690,640,788,136,578,854,518,589,429,308,720`
  at `21,947,741` and negative at `21,947,740`; `check_coloring.py` on `S_6..S_10` witnesses)
- `python3 research/binary_source_spans_20261126/verify.py` (default C99 and `--pure-python` modes;
  `check_coloring.py` on `k = 2..16` witnesses)
- Ancestor verifiers on `d18a965` (`verify_full_square.py` for `139`, `r4_stratified_farkas_20261124/verify.py`
  for `21,947,830`, `verify_local_packing.py`, `verify_order14_min15.py`, `verify_new_patches.py`),
  `manuscript/verify_directed_L_manuscript.py`, and `scripts/check_english_only.py`.
