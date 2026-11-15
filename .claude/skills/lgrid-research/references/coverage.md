# Coverage record

## 2026-11-14, Codex binary-source round 2

Base: fb33871768bd94fd8e88452ac62ac2789eb0e882. Remote fetch and state refresh
completed. The dated state pins remain stale; no repository-wide review or
new numerical bound is claimed. External Claude's unfinished work was not read.

Read: all three governing skills; state, obstructions, information-losses,
and color-transfer references; round-1 THEORY.md, sensitivity.py, and
check_collision_family.py; boundary-certificate FOUR_COLOR.md,
FOUR_COLOR_EDGE_VARIANCE.md, verify_four_edges.py, verify_four_double.py;
the complete newly authored round-2 package.

Searched/partial: manuscript/main.tex (forcing and signed-completion section
read; other matches searched), docs/RESULTS_INDEX.md, this coverage record,
and literature/KNOWN_RESULTS.md. No fresh external literature audit.

Run: the bounded probes, exact certificate generator, and independent
verify_round2.py, with coverage in ROUND2_REPORT.md and verification.json.
These checks do not independently rederive the inherited capacity tables or
the external correlation construction. Internal helpers performed theory and
read-only review, apart from the reviewer's REVIEW.md; no numerical workers.

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
