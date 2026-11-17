# Kimi round 5: exact nonuniform scale duals

**Outcome: no new numerical upper bound on `R_4` or `R_3`.** The round replaced
a nonuniform-weight scan by three exact finite optimizations. It found one
finite best-case obstruction and two positive best-case margins, then stopped
as preregistered because the actual six-square rainbow minimum remains unknown.

Branch: `kimi/r4-hybrid-dual-20261116`.
Base: `e1a62f30ce74d03681c04b58d0486e551e775124` on
`kimi/r4-energy-20261115`.
Research directory: `research/kimi_r4_nonuniform_dual_20261116/`.

## 1. Frontier and read coverage

GitHub authentication, all 22 visible branches, and all 14 open pull requests
were refreshed before method selection. The local state-refresh script reported
STALE because its 2026-11-13 pins predate the research branches. The primary
working tree contained unrelated uncommitted work and was not modified; this
round used a separate worktree.

Read for routing and proof scope:

- Kimi's round-4 plan, contract, theorem, report, consumer generator, and
  independent consumer verifier;
- Codex's round-3 `THEOREM.md` and `ROUND3_REPORT.md` at commit
  `14647e607c2525b0cd12081b03899827d306a030`;
- Claude's latest `siege/notes.md` at commit
  `f690b9c6730e3e2989f845b561d32e84afe62bbe`;
- the governing research, invention, verification, information-loss,
  color-transfer, route, evidence, and English-only instructions.

This reading establishes lane separation, not independent adoption of any
collaborator numerical bound. The present proof uses only Round 4's geometric
consumer and exact line-energy ceiling, both reread in full.

## 2. Finite goals and decisions

1. **Pre-register the consumer.** The exact program, quantifiers, three host
   sizes, and stopping rules were written in `CONTRACT.md` before optimization.
2. **Run the smallest discriminating test.** Only `(N,m)=(30,6),(60,6),(120,6)`
   were run. No larger host, kernel enumeration, or SAT search was launched.
3. **Certify rather than scan.** SciPy/HiGHS supplied discovery vectors only.
   They were converted to rational feasible primal and dual vectors. Equal
   exact objectives certify each finite optimum.
4. **Pivot on the missing mathematical input.** The positive best-case margins
   at `N=60,120` were not promoted to bounds. The next bridge is an actual
   lower bound on `rho_6`; more weight optimization cannot supply it.

## 3. Exact findings

| `N` | Exact optimal `V(N,6)` | `20*V-U_N` | Uniform-weight margin | Decision |
|---:|---:|---:|---:|---|
| 30 | `7458/125` | `-7093/25` | -672 | Best-case consumer closed |
| 60 | `671151/1250` | `31052/125` | -3105 | Actual `rho_6` required |
| 120 | `2810248/625` | `1474742/125` | -15060 | Actual `rho_6` required |

At the two positive hosts, the consumer would respectively require
`rho_6>13112500/671151` and `rho_6>24415625/1405124`. These are approximately
19.5373 and 17.3761 rainbow Ls out of 20. No such local minimum is proved.
The result therefore refines the obstruction; it does not solve it.

## 4. Verification and actual coverage

`verify_dual.py` imports no discovery code and uses only the Python standard
library. It independently reconstructs copy counts by origin-difference
summation, all incidence coefficients, all dual covering inequalities, and the
rainbow ceiling from line-length residues.

| Check | Actual coverage | Result |
|---|---|---|
| Copy-count formulas | Eight small scale rows, by two literal formulas | PASS |
| Primal feasibility | `28+58+118=204` host-step constraints | PASS |
| Dual feasibility | `5+11+23=39` scale constraints | PASS |
| Exact optimality | Three equal feasible primal/dual objective pairs | PASS |
| Exact margins and uniform comparison | Three rows | PASS |
| Negative controls | One infeasible primal and one infeasible dual | Both rejected |
| Known feasible controls | Zero and uniform primal vectors | Both accepted |
| Rainbow minimum `rho_6` | Not computed | UNDECIDED |
| New Ramsey bound | None | Not claimed |

The floating-point arrays and solver messages are quarantined in
`solver_diagnostics.json`, explicitly labelled non-evidentiary. Mathematical
outputs are exact rational strings in `dual_results.json` and
`dual_verification.json`.

## 5. Reproduction

From the repository root:

```sh
python research/kimi_r4_nonuniform_dual_20261116/dual_probe.py
python research/kimi_r4_nonuniform_dual_20261116/verify_dual.py
python research/kimi_r4_nonuniform_dual_20261116/build_manifest.py
python scripts/check_english_only.py
```

Discovery requires NumPy and SciPy; this run used Python 3.12.16, NumPy 2.4.4,
and SciPy 1.18.1. The independent verifier and manifest builder use only the
standard library. Important hashes and the final language-check result are in
`manifest.json`.

## 6. Next discriminating action

Do not enlarge the same scale optimization. A future attempt must either prove
a useful actual lower bound for a complete proper four-colored six-square, with
an independently checked full witness catalog and a new contract, or change to
a position-dependent or genuinely different full-square inequality. Until such
a local theorem exists, the positive best-case margins at `N=60,120` have no
Ramsey consequence.
