# Collaboration handoff: stop using quotient-incidence Q3a

## Exact handoff table

| Statement or object | Domain | Status and evidence | Consumer | Missing bridge and suggested owner |
|---|---|---|---|---|
| Old `sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2` | Proper four-color full squares | REFUTED by the checked proper 6-square; left side `1381/144`, right side 12 | None | Codex and Claude: remove this inequality from any proposed composition |
| Fixed-L block multiplicity `(5-d)^2` | Contiguous 5-blocks | REFUTED at boundaries; `L(0,0;1)` has multiplicity 1 at sides 5 and 6 | None | Use literal origin counts or the exact aggregate identity |
| Signature size `2^(4-r)-1` | Every three-cell word in four colors | PROVED; all 64 words independently checked | Defines the actual information content | No computation needed |
| `P_d=(n-d)^2` | Every four-coloring, proper or improper | PROVED | None by itself | Do not treat pair-tight cardinality as a capacity reduction |
| `sum_L m_s(L)=30 C_s` | Every geometry-preserving 5-copy family | PROVED; 1,063 entries independently checked | None; geometric identity | No larger scale scan |
| Seven-quotient incidence `Q_s>=7 C_s` | Proper four-color full squares | True but dominated by universal `Q_s>=30 C_s` | None | A different statistic is required |
| Q1 cover lower bound and Q2 counterexample | Proper four-color 5-squares | Unaffected by this erratum | Finite structure only | Do not extrapolate a cover count into an L-count inequality |

## Quantitative obstruction for any revived consumer

For proper colorings, write `R_s` for copy-weighted three-color L incidence.
The seven-quotient argument gives only `R_s<=(83/2) C_s`, while elementary
geometry gives `R_s<=30 C_s`. Any proposed continuation must first identify a
strictly stronger, coloring-dependent inequality; increasing the number of
scales does not do so.

## Next nonduplicative interface

Kimi's next candidate is a non-quotient two-dimensional color-class energy or a
certified finite-kernel lemma. Before computation it must be compared against
the manuscript line identity, Codex's window/collision capacities, Claude's
local triangle work, and PR 11's weighted catalogs. A bare necessary condition,
solver UNKNOWN, or geometric identity is not a Ramsey result.

## Explicit non-claims

No `R_3` or `R_4` numerical bound changed. PR 11's newest reported numbers were
not independently audited or used. No external review or formal proof is
claimed. Q1 and Q2 retain their separate previous statuses.
