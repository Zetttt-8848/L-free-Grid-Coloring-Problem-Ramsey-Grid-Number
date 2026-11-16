# Kimi round 4: exact four-color energy, zero-kernel witnesses, and consumer closure

**Outcome: no new numerical upper bound on `R_4` or `R_3`.** The round produced
an exact general line identity, three complete counterexample colorings, and a
corrected full-square embedding calculation that closes the preregistered
uniform asymptotic consumer.

Branch: `kimi/r4-energy-20261115`.
Base: `b7d52434061f7cb15395d50edc949e2700356926`.
Contract commits: `2f56b6e8c774adc534cf7e67dcd360d77c04b474` and the
pre-enumeration amendment `7b5fa53293f1791ae52d5d7546565648beff7348`.

## 1. Frontier and read coverage

Before work, GitHub authentication, all 19 then-existing branches, and all 12
open PRs were refreshed. No remote research head had moved since round 3. The
state-refresh script returned STALE because its 2026-11-13 pins predate current
research branches; this was treated as a stale snapshot, not as a runtime
failure.

Read in full for this lane: governing research/invention/verification skills;
dated state, obstruction, information-loss, and color-transfer references;
manuscript `lem:variance` and `lem:weighted`; PR 11's three weighted proof
reports; Codex's round-3 theorem/report; Claude's D1 preregistration,
grid-compatibility report, and upper-bound proof. The collaborator bounds were
used only for routing and were not independently replayed or adopted.

The local clone remains on old `main` because remote writes use the authorized
GitHub interface and the local object store lacks the round-3 head. All new
files are isolated in this dated directory. No shared manuscript, shared status
file, or collaborator package was changed.

## 2. Work completed in finite steps

### Step A: Route N algebra

Proved for every `k`-coloring of the complete strict triangle:

```text
D_k+2R_k-4B_k=2*C(N,3)-S_N/k+3*C(N,2).
```

This includes improper colorings and reduces exactly to the manuscript's
three-color identity. At four colors, line balancing gives a rainbow-count
ceiling asymptotic to `C(N,3)/4`; equivalently the equal-pair floor has leading
ratio `3/4`. It cannot force a contradiction at any `N`. Route N was stopped
without an energy scan.

### Step B: Route F finite witnesses

Complete proper four-color full squares at orders `3,4,5` were found with zero
rainbow Ls in their strict lower triangles. Therefore the exact local minima
`rho_3,rho_4,rho_5` are all zero. In fact each witness has zero rainbow Ls in
its entire square. The preregistered zero-witness rule stopped each search
immediately; no incomplete minimization was promoted.

### Step C: consumer correction and pivot decision

The contracted unrestricted square-origin count was found to overcount copies
that cannot be charged to the host strict triangle. It was corrected before any
bound claim. Exact valid-origin and incidence formulas were proved and checked
by direct enumeration.

For uniform scale weights and the uniform cap `K=C(m,3)`, a large-`N`
contradiction would require

```text
rho_m/C(m,3) > m(m-1)/(4(m+1)).
```

Orders `3,4,5` fail by their zero witnesses. For every `m>=6`, the required
fraction exceeds one, so even a maximal local rainbow count cannot supply a
positive leading margin. The route was stopped rather than enlarged to order 6.
Nonuniform weights, position-dependent estimates, other host regions, and
isolated finite sides are explicitly outside this closure.

## 3. Evidence and actual coverage

| Check | Coverage | Result |
|---|---|---|
| General energy identity | All 4,164 four-color words on `T_2,T_3,T_4`, proper and improper | PASS in generator and independent verifier |
| Pair-completion geometry | Every line pair and L at `N=2,3,4` | PASS |
| Exact energy table | `N=1,...,10`, rational arithmetic | PASS |
| Three-color reduction | Formula checked through `N=99`; proof is general | PASS |
| Full-square witnesses | Every L: 5, 14, and 30 at orders 3, 4, 5 | Proper, zero rainbow |
| Project coloring checker | All three exported witness files | PASS |
| Known-answer encoding | Two-color 4-square SAT and 5-square UNSAT | PASS by independent pruned enumeration |
| Valid origins and incidences | Five small host scenarios, seven scale rows | Literal/formula agreement |
| Uniform asymptotic coefficient | Exact finite sums and finite differences for `m=3,...,8` | PASS |
| English-only repository check | Recorded in `manifest.json` | Required before final push |

The raw outputs are `energy_results.json`, `kernel_results.json`,
`consumer_results.json`, their independent verification files, and
`standard_3.json`, `standard_4.json`, `standard_5.json`.

## 4. Development corrections and negative results

- An initial development assertion compared a `Counter` with a mapping whose
  values were triples rather than unit multiplicities. The generator was fixed
  and rerun; no failed output was accepted.
- An incorrect verifier assertion that `H_N` itself must always be integral was
  removed. The proof uses exact rational `H_N`; the rainbow estimate is the
  stated rational expression. No mathematical identity changed.
- The original square-copy count was mathematically wrong for the intended host
  triangle. `CONSUMER_ERRATUM.md` gives an explicit four-origin/three-origin
  example and the corrected formula.
- No SAT/UNSAT claim, DRAT proof, capacity improvement, or local lower-bound
  catalog is asserted. The finite searches here produced witnesses, not proof
  of nonexistence.

## 5. Reproduction

From the repository root:

```sh
python research/kimi_r4_energy_20261115/energy_probe.py
python research/kimi_r4_energy_20261115/verify_energy.py
python research/kimi_r4_energy_20261115/enumerate_kernels.py
python research/kimi_r4_energy_20261115/verify_kernels.py
python research/kimi_r4_energy_20261115/consumer_audit.py
python research/kimi_r4_energy_20261115/verify_consumer.py
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py research/kimi_r4_energy_20261115/kernel_3.json --output research/kimi_r4_energy_20261115/standard_3.json
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py research/kimi_r4_energy_20261115/kernel_4.json --output research/kimi_r4_energy_20261115/standard_4.json
python .agents/skills/directed-l-grid-research/scripts/check_coloring.py research/kimi_r4_energy_20261115/kernel_5.json --output research/kimi_r4_energy_20261115/standard_5.json
python research/kimi_r4_energy_20261115/build_manifest.py
python scripts/check_english_only.py
```

All new programs use only the Python standard library. The finite-kernel search
was pre-registered at 120 seconds per order and 300 seconds total, one worker;
actual witnesses were found without using the budget as evidence. Exact input
and output hashes, interpreter version, and final English-check results are in
`manifest.json`.

## 6. Next discriminating action

Do not repeat the uniform square-copy count or enumerate orders `m>=6` for that
same consumer. A future attempt must first exhibit either (a) nonuniform scale
weights and a position-sharp incidence certificate with a positive exact margin,
or (b) a genuinely different full-square inequality coupling the four-color
line discrepancy to existing capacity information. Neither bridge is supplied
here. The next experiment needs a new contract and a quantitative sensitivity
test before any further coloring search.
