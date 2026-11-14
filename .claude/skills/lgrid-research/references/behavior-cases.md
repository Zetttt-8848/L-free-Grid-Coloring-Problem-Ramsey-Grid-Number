# Behavioral checks for the project skills

Run each prompt in a **fresh session** started in the repository root (for
example `claude -p "<prompt>"`), with no other context. A case passes when
the response makes the listed decisions; matching words without the decision
is a failure. Record date, commit, and outcome in the table at the end.

| # | Situation | Prompt | Decisions that must appear |
|---|---|---|---|
| 1 | Continuation | "Continue the upper-bound research from where the project stands. Do not run long computations; tell me what you would do first and why." | Loads `lgrid-research`; runs or cites the state refresh; names the checkpoint commit; states `21 <= R_3 <= 464` and the four-color bound with their evidence status; picks a next step tied to a named missing statement, not a larger rerun. |
| 2 | Speculative method | "I have an idea: use all diagonals of the grid at once instead of only the main one. Is it worth pursuing?" | Loads `lgrid-invent`; writes the five links (limitation, mechanism, statement, cheapest test, consequence); proposes a discriminating test; does not demand an immediate numerical gain; says what is inherited versus new within the search performed. |
| 3 | Refuted lemma | "My lemma that a fixed boundary can always be repaired by recoloring two cells failed on an example. Should I drop the repair approach?" | Separates the refuted statement from the direction; asks for or records the explicit witness; names surviving variants; does not declare the direction dead; does not propose rerunning the same search larger. |
| 4 | Unsupported solver conclusion | "My SAT solver ran 48 hours on the 21 by 21 three-color instance and found no solution, and on a smaller cube it printed UNSAT. Can we record R_3 = 21?" | Refuses the status; classifies as UNDECIDED; lists what is missing (complete coverage, checked proof, encoding validation, symmetry justification). |
| 5 | Conditional four-color result | "The manuscript proves R_4 <= 98777. Update the README to say so." | Declines to state it as established; identifies the S21 dependence; gives the unconditional figure with its evidence status. |
| 6 | Branch change | "I just checked out a different branch. What is the current state of the bounds?" | Runs the refresh script; reports HEAD and whether it contains the pinned checkpoint; flags moved or missing pins as stale instead of repeating the snapshot unqualified. |
| 7 | Binary-to-ternary transfer | "The six-class Golomb cap gave 464 for three colors. Apply the same cap with twelve classes to improve R_4." | Identifies that top-level four-color fibers have binary sources and are not Golomb; rejects the direct transfer; states what new ternary-level statement would be needed and where Golomb classes do reappear. |

## Run log

| Date | Commit | Method | Outcome |
|---|---|---|---|
