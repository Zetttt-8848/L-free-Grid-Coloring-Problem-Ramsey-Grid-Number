---
name: directed-l-grid-research
description: Pointer for the directed L-grid Ramsey project. The governing guidance moved to .claude/skills (lgrid-research, lgrid-invent, lgrid-verify) on 2026-11-13; read those files before any research, review, or status claim in this repository.
---

# Directed L-grid Ramsey research (pointer)

This skill was the project workflow until 2026-11-13. Its priority rule
("three colors first; four colors only as a generalization test") no longer
governs. The current objective is to improve the upper bounds of both `R_3`
and `R_4`; see `AGENTS.md` at the repository root.

Read, in this order:

1. `.claude/skills/lgrid-research/SKILL.md` - objective, problem definition,
   state refresh, three-color versus four-color distinction.
2. `.claude/skills/lgrid-invent/SKILL.md` - when proposing or ranking methods.
3. `.claude/skills/lgrid-verify/SKILL.md` - before any status or bound claim.

Retained in this directory:

- `scripts/check_coloring.py` and `assets/paper20.json`: the coloring
  checker and the literature `20 x 20` witness, still in use.
- `references/evidence.md`: checker input formats and reproduction notes.
- `references/routes.md`, `references/repository-map.md`: route notes and a
  navigation snapshot dated 2026-11-08, written under the former priority.
  Treat them as historical context, not as current guidance or state.
- The previous text of this file is in Git history at commit
  `dc1cbe6daf7d9816329217a511741fbeabd726b3`.
