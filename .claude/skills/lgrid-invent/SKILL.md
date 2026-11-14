---
name: lgrid-invent
description: Method invention for the directed L-grid upper bounds. Use when proposing, comparing, or developing a new counting method, invariant, representation, lemma, or algorithm for R_3 or R_4; when deciding which candidate to pursue or drop; when a candidate lemma fails; when judging whether an idea is a new mechanism or a re-tuning; or when moving a three-color argument to four colors.
---

# Inventing methods for the upper bounds

Load `lgrid-research` first. This skill is about deciding **what to try and
how to learn the most from trying it**.

## Start from what the current proofs throw away

Every existing bound is a chain of steps, each of which keeps some
information about a coloring and discards the rest. A new mechanism is a way
to keep something that is currently discarded and still sum it up. Read
`references/information-losses.md` for the dated map of the two chains and
where each loses information; extend it when you find a new loss.

Useful moves, none mandatory:

- **Keep an object until after the summation.** Replace a number (a cap, a
  count, a correlation) by the labelled object it summarizes (which class,
  which color, which endpoint), and bound the labelled sum.
- **Couple what is estimated separately.** Different lags of one diagonal
  class, different diagonal classes, different sources requesting the same
  cell, different levels of the recursion, different diagonals of the grid.
- **Change the representation.** Diagonal words `W_c`, completion-class
  incidence structures, request multigraphs on cells, weighted transport
  between endpoints: a constraint invisible in one may be linear in another.
- **Turn rigidity into cost.** Extremal configurations (optimal rulers,
  equality cases of Cauchy, saturated caps) are few and rigid; near-extremal
  ones must pay somewhere. A stability statement converts that into margin.
- **Let exact computation propose the lemma.** A minimal unsatisfiable core,
  an LP dual, or an extremal example is a hint at a general inequality.
  The inequality still needs a proof.

Established tools stay available. Using a known theorem as a component does
not make an approach derivative, and avoiding one does not make it new.

## The candidate card

Before spending real effort, write these five lines for the candidate, in
the research directory. If one cannot be written, that line is the task.

```text
Limitation:   the step of an existing argument that loses information, or
              the interaction it treats as independent
Mechanism:    the object, invariant, or algorithm that retains it
Statement:    the exact proposition needed (domain, quantifiers, span range,
              constants); for which k
Cheapest test: the least expensive proof attempt, counterexample search, or
              exact computation whose outcome would change the plan, with
              the outcome that would count against the statement
Consequence:  the chain from the statement to a bound on R_3 and/or R_4,
              naming every remaining gap; "structural value only, because
              ..." is acceptable at first
```

Then add:

- **Status of each link** (proved, conditional, conjectural).
- **Inherited / modified / apparently new**, checked against
  `references/information-losses.md`, the `research/` packages, and the
  primary literature in `literature/KNOWN_RESULTS.md`. "Apparently new within
  the search performed" is the strongest claim available; record what was
  searched.
- **Color scope**: which `k`, and for `k = 4` which level of the recursion.

A candidate does not need an immediate numerical gain. It does need a
credible route to one, or an explicit reason its structural content is worth
having.

## Ranking candidates

Compare on these, in words, without invented scores or probabilities:

1. **Significance of the missing lemma**: does success close a chain, or
   leave another open bridge behind it?
2. **Information per unit cost of the cheapest test.**
3. **Known obstructions** (`lgrid-research`, `references/obstructions.md`):
   does the statement survive each relevant counterexample, and why?
4. **Reach**: `R_3` only, `R_4` only, or both; see the sensitivity notes in
   `references/information-losses.md`.
5. **Dependence**: if it rests on an unresolved conjecture, what is the
   independent alternative being kept alive?

Prefer the candidate whose cheapest test is most likely to change the plan,
not the one with the largest hoped-for gain.

## Working a candidate

- Try to **break the statement first**: smallest cases exhaustively, then
  the known extremal and near-extremal examples, then adversarial
  constructions suggested by the obstruction ledger.
- When exploring computationally, decide beforehand what result would make
  you stop. If doubling the instance size cannot change the decision, do not
  double it.
- Weight or parameter optimization is reconnaissance. A scanned family is not
  an optimal dual; a hypothetical cap reduction is a target lemma, not a
  result. Convert each promising scenario into the statement it would
  require.
- Before adding two savings, identify the objects each one constrains. If
  they overlap, combine by intersection or prove the joint accounting:
  multiplicities, boundary terms, and cells shared between sources included.

## When a statement fails

Record, in the research directory and in the obstruction ledger:

1. the exact statement refuted and the explicit witness (checkable);
2. which hypothesis or step actually failed;
3. the nearest variants the witness does **not** refute (extra hypothesis,
   weighted or amortized form, different invariant, restricted span range);
4. whether the failure is of the statement, of one proof method, of an
   implementation, or of the budget.

Only the first kind closes anything. Retrying a mechanism is legitimate when
the new statement visibly escapes the witness; rerunning the same search
larger, or renaming the lemma, is not.

## Four colors

Read `references/color-transfer.md` before transferring any argument. The
default assumption is that a three-color lemma does **not** transfer: its
four-color counterpart is a new statement at the ternary level with its own
proof, and often a different natural regime (large spans, crude constants).

## When a statement succeeds

Write the full chain to the bound and locate the next gap before celebrating
the lemma. Then hand the result to `lgrid-verify`: independent check, exact
certificate, status, and the entry in the project records. Classify the
outcome honestly as mechanism, technical improvement, or numerical bound.
