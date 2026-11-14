---
name: lgrid-verify
description: Evidence and acceptance standards for the directed L-grid project. Use before assigning any status (proved, conditional, conjecture, finite-checked, counterexample, refuted, undecided), before accepting a SAT/solver/search/enumeration outcome or a numerical certificate as evidence, when citing or applying a literature result, when reviewing a proof or pull request, and before reporting or recording any bound on R_3 or R_4.
---

# Evidence and acceptance

Load `lgrid-research` first. The purpose of this skill is that every claim
in a report or record can be traced to exactly the evidence that supports
it, and no further.

## Status vocabulary

A status belongs to an **exact statement** (domain, quantifiers, `k`, range)
at a **commit**, with its assumptions listed.

| Status | Requires |
|---|---|
| PROVED | A complete argument whose every input is itself proved or is a located external theorem whose hypotheses match. Name external inputs in the status line ("PROVED with external inputs G(24) >= 425, ..."). |
| CONDITIONAL | A proved implication from named open statements. The consequent is never reported as a bound. |
| CONJECTURE | A precise statement plus the range in which counterexamples were sought. |
| FINITE-CHECKED | Exact finite domain, encoding, coverage, and checker stated; no extrapolation. |
| COUNTEREXAMPLE | A complete explicit object, verified constraint by constraint, with the statement it refutes. |
| REFUTED / SUPERSEDED | The original record kept, with a pointer to the witness or successor. |
| UNDECIDED | Timeouts, `UNKNOWN`, bare `UNSAT` without a checked proof, unsuccessful searches, incomplete coverage, missing inputs. |

Layer statuses when needed: an implication can be PROVED while its
hypothesis is open (so the bound is CONDITIONAL); arithmetic can be rerun
(PASS) while inherited lemmas are unaudited. Say each layer; do not merge
them into one green label. Also say **who checked**: author only, a separate
in-repository reviewer, a rerun in this session, a formal proof.

## Does it bound a Ramsey number?

Before writing `R_k <= n`, confirm each of these, for the stated `k`:

1. The argument starts from an **arbitrary** coloring of the full `n x n`
   square with at most `k` colors, not from a source, triangle, restricted
   family, or partial coloring.
2. Every reduction preserves the configuration exactly: orientation, equal
   legs, `d > 0`, cells inside the domain. Translations of one coordinate
   preserve it; transposition and reflections exchange it with another
   orientation and are not symmetries of a fixed coloring.
3. Every lemma is applied on the domain where it was proved (strict versus
   weak source, span versus number of positions, the number of colors of
   that source).
4. Every external input is used in the direction it was proved (a ruler
   example bounds `G(m)` from above; only an exhaustive search bounds it
   from below) and within its range (the OGR inputs cover at most 480
   positions).
5. Combined savings have a proved joint accounting: multiplicities, shared
   cells, boundary terms, interactions between sources. Otherwise combine by
   intersection.
6. The final inequality is checked in exact integer or rational arithmetic,
   strict where strictness is needed, and the checker reconstructs its
   inputs from the stated formulas, not from cached tables.

A lower bound `R_k >= n + 1` needs one complete coloring of `[n]^2`, checked
cell by cell with `python
.agents/skills/directed-l-grid-research/scripts/check_coloring.py`.

## Computational impossibility

An `UNSAT` or exhaustive-search result supports an upper bound only with all
of the following; anything less is UNDECIDED:

- **Sound and complete encoding** of the stated problem: variables mapped to
  cells, exactly one color per cell, every L constraint, auxiliary variables
  with two-way semantics. Test the encoding on instances with known answers
  in both directions (for example the proper `20 x 20` coloring must satisfy
  it; `R_2 = 5` must be reproduced).
- **Justified symmetry breaking**: color permutation is safe; each further
  constraint needs a proof that every solution has a representative.
- **Complete coverage**: every cube or branch accounted for, with consistent
  assumptions, and a proof for each.
- **Independently checkable proof objects** (DRAT/LRAT or equivalent),
  actually checked by a separate tool, with input and proof hashes.
- A solver's reported status, a custom checker that handles only part of the
  proof format, heuristic cuts, or a subset of branches do not qualify.

Restricted-family impossibility (frozen interior, periodic or symmetric
colorings, a single partial coloring) is reported as exactly that.

## New algorithms

Report separately, and do not let one stand in for another:

| Aspect | Evidence |
|---|---|
| Correctness (soundness) | Proof, or reduction to a checked certificate per run |
| Completeness | Proof that no solution is missed, including pruning rules |
| Complexity | Proved bounds only; otherwise "not analyzed" |
| Empirical performance | Instances, budgets, hardware, seeds, comparison under equal budgets |
| Heuristic behavior | Labelled as such; never cited for impossibility |

## Numerical certificates

- Floating point may suggest weights or duals. The certificate is exact:
  integers or rationals, reconstructed from a formula, with the margin
  printed.
- A positive margin at one `n` proves the statement at that `n`. A negative
  margin proves nothing; a scan of a weight family is not an optimum.
- Record command, input hashes, interpreter version, and actual run range.
  Rerun on a temporary copy when a checker writes next to its inputs.

## Literature inputs

Read the original statement. Record: source and version, theorem number,
exact hypotheses, orientation and coordinate convention, whether constants
are explicit, and the dictionary to project notation. An asymptotic bound
with an unspecified constant gives no numerical bound for `k = 3` or `4`.
Novelty statements are limited to "not found in the sources searched",
with the sources listed.

## Reviewing a proof or a pull request

1. Restate the claim with its quantifiers before reading the proof.
2. Read the proof against the definition, not against its own summary;
   check degenerate cases (empty and one-element classes, overlapping pairs,
   `h = t`, boundary lags, off-by-one between span and positions).
3. Recompute decisive numbers with a checker written from the definition,
   not by importing the author's code.
4. Classify each finding as affecting the statement, the proof, the scope,
   or the presentation. A corrected scope is a result; record it.
5. State what was not checked.

## Recording

Use the project's existing structure: a dated directory under `research/`
with the contract, statement and proof, checker, results, and review; then
`docs/RESULTS_INDEX.md`, `docs/OPEN_PROBLEMS.md`, and `README.md` when a
checkpoint is accepted; then `lgrid-research/references/state.md` and
`pins.json`. Follow `docs/CONTRIBUTING.md` and the English-only policy.
The legacy reference
`.agents/skills/directed-l-grid-research/references/evidence.md` documents
the coloring-checker input formats.
