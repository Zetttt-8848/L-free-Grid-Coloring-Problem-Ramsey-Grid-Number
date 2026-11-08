# Full 21 construction attempts and a certified repair barrier

Base `df6e35cfff68580dc78aa91bc35d4c6399a6464a`. **No valid 21×21 construction was found; the Ramsey lower bound is unchanged.** The new durable result is an exact repair obstruction and a sound, explicitly instantiated cut-lifting mechanism.

## Results

- **PROVED logical mechanism + FINITE-CHECKED instance:** 34 previously certified boundary cores lift to 22,680 distinct redundant full-square clauses, under color permutations, translations, and antidiagonal reflection. The independent checker rechecks the seed proof trees and complete transformed clause set. No arbitrary rotation is used.
- **INVALID candidate:** weighted whole-square local search produced a complete 441-cell matrix with exactly one monochromatic L. It is saved explicitly in `runs/local71.json`, not treated as a construction.
- **FINITE-CHECKED repair barrier:** no proper 21-square lies at Hamming distance≤10 from that matrix. Radius 10 has 1,235,525 proof nodes; a separate standard-library checker verifies complete branch coverage. Any successful repair must change at least 11 cells, with no claim that 11 suffices.
- **UNDECIDED construction attempts:** adaptive interior thawing, unrestricted SAT with/without certified cuts, and defect-directed exact SAT repair all reached wall limits without a positive model. No UNSAT status from these searches is used as a theorem.

The proofs and quantifiers are in [THEOREMS.md](THEOREMS.md). Redundant-clause lifting and weighted min-conflict search are established methods; the contributions here are the sound geometric instantiation, complete certificates, and newly measured obstruction. No universal speedup or literature priority is claimed.

## Actual attempts

| Run | Scope and limit | Observed outcome |
|---|---|---|
| guided17 | Full 21 formula; seed 20 at (0, 1); certified-support-aware thaw; 60s budget, 63s outer cap | External timeout; 67 completed calls recorded |
| random17 | Same seed/offset and wall cap; random thaw | External timeout; 79 completed calls recorded |
| cuts120 | Unrestricted full 21, 22,680 certified redundant clauses, same phase hint; 120s+3s outer cap | External timeout inside first call; no completed solver call |
| plain120 | Same unrestricted formula/phase hint without cuts, same wall cap | Same outcome; no acceleration conclusion |
| local71 | All 441 cells free; 90s local search after compilation | One violated L; 308,500,000 moves, an auxiliary work count only |
| repair91 | Repair the one-defect candidate; actual conflict cores plus lifted cuts; 90s+3s outer cap | External timeout; 172 completed calls recorded |

Matched runs were launched with overlapping wall time on the shared machine; they are exploratory comparisons, not controlled throughput benchmarks. Glucose conflict budgets and even the requested interrupt path did not ensure the intended per-call return in this environment. The outer subprocess timeout did terminate each worker. A checkpoint's `elapsed_seconds` refers to its last completed call, while the runner field records actual total wall time; do not mistake stale checkpoint time for finished solver time.

The initial radius survey exhausted 1..8 and stopped 9/10 at 100,001 nodes. Its summary is preserved in `runs/initial_defect_summary.json` and is superseded by `defect_certified.json`, where all radii 1..10 completed. The earlier bulky exploratory tree is retained locally in ignored `_scratch/`; only the final compact, independently checked certificates are publication evidence.

## Evidence and reproduction

Only discovery requires `python-sat` (1.9.dev15, Glucose 4) or NumPy/Numba. The two checkers require only Python 3.10+ standard library, plus the prior checked certificate verifier already in this repository. No executable is downloaded by these scripts.

```sh
python research/coupled_budget_20261108/lower/verify.py
python research/coupled_budget_20261108/lower/verify_defect.py
python research/coupled_budget_20261108/lower/run_audit.py
```

`verify.py` validates the 34 base cores and independently reconstructs the entire lifted set using normalized geometry. It imports the prior standalone core verifier, never the new discovery code. `verify_defect.py` imports neither search implementation nor solver; it verifies every required branch from raw geometry and the input matrix.

Fresh discovery examples (outputs must not already exist):

```sh
python research/coupled_budget_20261108/lower/adaptive_repair.py --method guided --seed 17 --offset 0,1 --seconds 60 --output /path/to/fresh/guided.json
python research/coupled_budget_20261108/lower/certified_cuts.py --cuts --seconds 120 --output /path/to/fresh/cuts.json
python research/coupled_budget_20261108/lower/local_candidates.py --seconds 90 --seed 71 --output /path/to/fresh/local.json
python research/coupled_budget_20261108/lower/defect_search.py --input research/coupled_budget_20261108/lower/runs/local71.json --output /path/to/fresh/defect.json --max-radius 10 --per-radius-seconds 30 --node-cap 2000000 --tree-through 10
```

The spaces between option names and their values are required; see each program's `--help`. The state and script hashes in recorded runs bind actual executed programs. The final finite checking manifest binds its inputs before/after and recorded outputs; a completed run is interpreted only for its stated finite claim.

## What changed and what remains

The previous frozen 20 obstruction is now explicitly crossed by releasing interior cells, and its proved cores can also be reused as globally sound clauses. The new candidate shows that low violation count alone is a poor neighborhood-size rule: its only defect cannot be repaired with 10 changes.

Next discriminators: use radius≥11 with a different branching heuristic; derive coupled cores from the discrepancy proof to guide larger neighborhoods; or generate a structurally different full candidate. These routes remain open. The 22,680-cut portfolio has not demonstrated a speed benefit. A positive full 21 matrix must still pass every geometric L before any R3 lower-bound claim changes.
