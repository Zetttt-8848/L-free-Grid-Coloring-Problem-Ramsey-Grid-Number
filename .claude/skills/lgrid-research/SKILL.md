---
name: lgrid-research
description: Governing skill for the directed L-grid Ramsey project (upper bounds for R_3 and R_4). Load at the start of any work in this repository - continuing research, choosing what to investigate, reading or reporting bounds, reviewing a branch or pull request, or after a branch or checkpoint change. Refreshes the research state, protects the problem definition and the three-color versus four-color distinction, and routes to lgrid-invent and lgrid-verify.
---

# Directed L-grid research: orientation and steering

## Objective

Improve, with rigorous justification, the **upper bounds of `R_3` and `R_4`**.
A result counts toward the objective only if it changes what can be proved
about every coloring of a full square. Prefer mechanisms that are new relative
to the diagonal/Golomb/convolution method over re-tuning it. Lower-bound
constructions and searches are instruments for finding structure and killing
false lemmas, not a parallel goal. Both color counts are live now: do not
postpone four-color work.

Report three things separately, always: a **new mechanism** (new object,
invariant, or lemma), a **technical improvement** (weights, parameters,
implementation, exact-versus-linearized arithmetic), and a **numerical bound**.
Any one can occur without the others.

## The problem, fixed

```text
Forbidden: (x,y), (x+d,y), (x+d,y+d), integer d > 0, all three cells in the
grid and of one color.
R_k = least n such that every coloring [n]^2 -> {k colors} contains one.
```

Orientation, equal legs, positive step, the full square as domain, and the
universal quantifier are all part of the problem. Checks to apply to every
statement and encoding:

- An upper bound excludes **every** coloring of the square. A source that
  cannot be colored, a restricted family with no member, a partial coloring
  that does not extend, or a search that found nothing excludes less.
- `V(A) = {(v,u) : u < v, u,v in A}` (strict source), `W(A)` (weak source,
  diagonal included), complete triangles, fibers `F_d(A) = {u : u, u+d in A}`
  and full squares are different domains. State which one a claim lives on.
- Equivalent exact form (useful for checking encodings): write `W_c[y]` for
  the color of cell `(y+c, y)`. A forbidden L is `W_c[y] = W_c[y+d] =
  W_{c+d}[y]`: a same-color pair at distance `d` on diagonal `c` forbids that
  color at the earlier index on diagonal `c+d`.
- State the coordinate convention (zero- or one-based, which coordinate is
  the row) before translating between a paper, the manuscript, and code.

## Three colors and four colors are different arguments

Excluding a diagonal color leaves a source with `k-1` colors.

| | `k = 3` | `k = 4` |
|---|---|---|
| Source of a diagonal class | binary | ternary |
| Fiber classes of that source | Golomb sets (proved) | sets with a **binary** source, not Golomb |
| Levels of the capacity recursion | 2 | 3 |
| What a "complementary color" argument gives | the other color is forced | two colors remain; nothing is forced |

Anything that uses forcing, signs `+1/-1`, a bipartite forcing graph,
"balance", or a two-class decomposition is a binary-source argument. Moving
it to four colors requires a new statement and proof at the ternary level;
record that statement explicitly (see `lgrid-invent`,
`references/color-transfer.md`). Keep separate ledgers for `R_3` and `R_4`
and never copy a cap, constant, or status across them.

## Start of session: refresh, do not reread

1. Run `python .claude/skills/lgrid-research/scripts/refresh_state.py`
   (add `--fetch` when network access is appropriate). It compares the
   repository against the pinned snapshot and lists what moved.
2. Read `references/state.md` for the baseline and its evidence status.
   Every figure there is dated; where the script reports a moved pin, the
   corresponding lines are **stale until re-derived** from the changed files.
3. Reread only what changed and what the task depends on. The first
   orientation of a new line of work should be thorough for that line; a
   continuation should not reread the repository.
4. The working tree you start in may sit on an old commit with someone
   else's uncommitted work. Do not switch its branch or discard its changes.
   Do new research in a separate worktree based on the latest research
   checkpoint, on a new branch.
5. Unmerged does not mean wrong; merged does not mean independently checked.
   Most of the research line lives in stacked open pull requests, not in
   `main`. Cite branch and full commit for every claim you rely on.
6. Keep `references/coverage.md` honest: files read in full, files searched,
   files only inventoried. Never describe an inventory as a review.

## Choosing what to work on

Load `lgrid-invent` to generate and rank candidates. The steering questions,
in order:

1. Which **missing statement** would move a bound if proved? Name it exactly
   (objects, quantifiers, range of spans, constants).
2. What is the **cheapest evidence that discriminates** between the statement
   being true, false, or true only in a weaker form? Prefer an exact small
   computation or a proof attempt on the hardest known example over a larger
   run of something already tried.
3. What happens **after success** (is the chain to `R_3` or `R_4` complete,
   or is there another gap?) and **after failure** (which variant survives
   the counterexample)?
4. Is the leading route conditional on an open conjecture? Then keep one
   alternative alive that does not depend on it.

Stop expanding a computation when further instances cannot change the answer
to question 1. A larger scan of a necessary condition does not prove it
sufficient; a longer search does not turn `UNKNOWN` into an upper bound.

Two regimes are worth keeping in mind, because they reward different tools
(details and current numbers in `lgrid-invent`,
`references/information-losses.md`):

- `R_3`: small spans (below about 480) and sharp constants. Gains come from
  exact finite structure: near-extremal Golomb rulers, shared positions,
  cross-lag and cross-source compatibility.
- `R_4`: spans up to about `2.2 * 10^7` and crude constants. Any bound on
  binary sources that beats the three-quarter-power capacity, even with a
  large constant, is amplified through the recursion.

## Evidence discipline

Load `lgrid-verify` before assigning any status or accepting any
computational or literature input. In brief: a status attaches to an exact
statement, with assumptions, evidence path, and commit; finite checks do not
extend beyond their range; conditional numbers stay conditional; savings from
two counts that constrain the same objects are combined by intersection, not
added, unless the accounting is proved.

## Keeping the system current

- Changing facts go in `references/state.md` (baseline and pins) and
  `references/obstructions.md` (refuted statements and what survives), each
  citing the project record that is the authority. Do not create further
  ledgers; update `README.md`, `docs/RESULTS_INDEX.md`, and
  `docs/OPEN_PROBLEMS.md` when a checkpoint is accepted.
- After a checkpoint or branch change, update `references/pins.json` only
  after rereading the changed evidence, in the same commit as the updated
  `state.md`.
- Durable guidance lives in the three `SKILL.md` files. If a rule here stops
  matching how good work on this problem is done, change the rule and say why
  in the commit; do not work around it silently.
- Behavioral checks for this skill set are in
  `references/behavior-cases.md`; rerun them after substantial edits.

## Reporting

Lead with whether the stated goal was reached. Then: exact statement,
status, evidence and its scope, what was not checked, and the next
discriminating action. Report `R_3` and `R_4` separately. Do not convert
activity into progress percentages.
