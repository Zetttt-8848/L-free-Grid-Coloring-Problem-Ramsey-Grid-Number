# Directed L-grid Ramsey project: standing instructions

These instructions apply to every agent session in this repository. They are
routing and invariants only; research facts live in the project records.

## Governing objective (set by the project owner on 2026-11-13)

Establish rigorously justified improvements to the **upper bounds of both
`R_3` and `R_4`** for the directed equal-leg L, by methods that go beyond
re-applying the existing diagonal/Golomb/convolution technique. Four-color
upper-bound research is authorized now and is not deferred until `R_3` is
resolved. Lower-bound constructions and searches are supporting tools for
structure discovery and falsification; they do not displace the upper-bound
objective. Where `README.md`, `docs/ROADMAP.md`, or older skill text say
"R3 first, then R4", this section takes precedence.

## Problem definition (do not let it drift)

Forbidden: three cells of one color at `(x,y), (x+d,y), (x+d,y+d)` with
integer `d > 0`, all inside the grid. `R_k` is the least `n` such that every
coloring of the `n x n` grid with at most `k` colors contains one. An upper
bound `R_k <= n` must exclude every allowed coloring of that grid.

## Required routing

1. Before any research, review, computation, or status claim in this
   repository, load the `lgrid-research` skill
   (`.claude/skills/lgrid-research/SKILL.md`) and run its state refresh.
   Claude Code: invoke it with the Skill tool. Other agents: read the file.
2. When proposing, ranking, or developing a method, lemma, representation,
   or algorithm, also load `lgrid-invent`.
3. Before recording any status (proved, conditional, refuted, finite-checked,
   undecided), accepting a solver or search outcome, citing literature, or
   reporting a bound, also load `lgrid-verify`.

The legacy skill `.agents/skills/directed-l-grid-research` is retained only
as a pointer and as historical reference material; its former "R3 first"
priority no longer governs.

## Working rules

- Current bounds and their evidence are recorded in
  `.claude/skills/lgrid-research/references/state.md`, which cites the
  project records as the authority. Treat every number there as a dated
  snapshot and re-check it against the refresh script output.
- Never present a conditional figure (for example `98,777` under S21, or
  `379`/`361` for three colors) as an established bound.
- New research goes in a dated directory under `research/`, on a branch;
  do not rewrite the shared manuscript, push, merge, or alter history
  without explicit authorization. Preserve uncommitted work you did not
  create.
- All tracked content is English only; run
  `python scripts/check_english_only.py` before committing.
