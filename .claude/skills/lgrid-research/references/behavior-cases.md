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
| 2026-11-13 | `8222226` plus refresh-script fix | `claude -p` (CLI 2.1.322) started in the primary working tree | Session init listed `lgrid-research`, `lgrid-invent`, `lgrid-verify` among available skills: **discovery observed**. Every model turn returned "Not logged in", so no behavior was observed by this method. |
| 2026-11-13 | same | Seven cold subagents started in the primary working tree (at `080822b`, behind the checkpoint), each given only the case prompt | All seven cases made the listed decisions (case 2 wrote the five-link card and named a discriminating test, but stated that it had not searched `research/` for earlier multi-diagonal attempts). In every run the agent read `CLAUDE.md`/`AGENTS.md`, read the routed `SKILL.md` files, and ran the refresh script. The Skill tool did **not** list the project skills inside subagents (the parent session's skill registry predates their creation), so activation was through the instruction route, not the Skill tool. |
| 2026-11-13 | same | Scratch clone with the checkpoint ref advanced, one pinned ref deleted, one unmerged ref added | Refresh script exited 1 and listed the moved ref with files to reread, the missing ref, and the unpinned branch. |
