# Directed L-grid project: Kimi Work instructions

All repository artifacts, research notes, proofs, code comments, commits, issues,
and pull requests must be in English. Only direct communication with the owner
may use Chinese.

## Objective and fixed statement

Improve rigorous upper bounds for both R_3 and R_4; R_4 research is authorized
now. For integer d>0, the forbidden pattern is
`(x,y), (x+d,y), (x+d,y+d)` in one color. R_k quantifies over every coloring of
the full n by n square with at most k colors. Never substitute a sparse source,
partial coloring, frozen family, or failed search for this quantifier.

## Startup

1. Load `directed-l-grid-research` and the repository's current
   `.claude/skills/lgrid-research/SKILL.md`; run its state refresh when the
   files are locally available.
2. Load `lgrid-invent` before choosing methods and `lgrid-verify` before
   assigning evidence status or reporting a bound.
3. Inspect all current branches and open PRs. The mathematical checkpoints are
   mostly unmerged; `main` is not the current research frontier.
4. Record the base branch and full commit. Work on a separate branch and in a
   new dated `research/` directory. Do not modify the shared manuscript.
5. Read the current route ledger before computing. Do not duplicate Codex's
   binary-source capacity/collision lane or Claude's ternary grid
   compatibility/MS* lane.

## Current comparison checkpoint

As observed on 2026-11-15, Codex branch
`codex/r4-local-capacity-round3-20261114`, commit
`14647e607c2525b0cd12081b03899827d306a030`, reports the internally reviewed,
computer-assisted bound `R_4 <= 21,947,865`. Treat the cited theorem and proof
traces as the authority, not this summary. Conditional values such as 98,777
are not established bounds. The latest Claude branch reports R_3 <= 462 with
external OGR inputs; verify its current proof package before relying on it.

## Method discipline

Write a candidate card: limitation, mechanism, exact statement, cheapest
 discriminating test, and consequence chain to R_3 or R_4. Try to falsify the
statement first. Pivot immediately after a checked counterexample or a
quantitatively failed consumer. Distinguish a refuted proposition, a failed
method, an implementation error, an exhausted budget, and an undecided search.

Do not add savings that charge the same cells. Keep source level, color count,
span range, and coordinate conventions explicit. A finite check never becomes
an arbitrary-scale theorem. UNSAT requires a checked proof and complete branch
coverage before it supports an upper bound.

## Collaboration

Leave reusable interfaces for Codex and Claude: exact input, domain,
quantifiers, certificate path, consumer, missing bridge, and what this result
does not imply. Never overwrite their files or merge their PRs. Preserve failed
routes and negative results; they prevent duplicated computation.

Before delivery run the relevant independent checker, the main manuscript
verifier if affected, and `python scripts/check_english_only.py`. Do not commit
secrets, chat logs, paid papers, tool installations, or build caches.
