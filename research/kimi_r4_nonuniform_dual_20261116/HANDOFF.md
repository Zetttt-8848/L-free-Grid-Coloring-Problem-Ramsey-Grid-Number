# Collaboration handoff: nonuniform six-square scale consumer

| Field | Reusable interface |
|---|---|
| Exact statement | At `m=6`, the exact normalized fractional copy-packing values are `V(30,6)=7458/125`, `V(60,6)=671151/1250`, and `V(120,6)=2810248/625`. |
| Domain | Complete strict host triangles `T_N`; valid geometry-preserving full six-square copies; nonnegative scale weights; uniform normalized incidence cap `Lambda_h<=1` for every `1<=h<=N-2`. |
| Quantifiers | Primal and dual certificates cover every nonnegative scale vector. Consumer statements about local kernels use only `rho_6<=20`; no particular proper kernel is assumed. |
| Evidence | Exact rational primal and dual vectors in `dual_results.json`; independent standard-library verification in `dual_verification.json`; equal objectives prove optimality. |
| Consumer | `rho_6*J<=K*calR_N<=K*U_N`, inherited from Round 4 after its valid-origin correction. |
| Finite obstruction | At `N=30`, `20*V<U_30`; even a hypothetical all-rainbow local triangle cannot give a contradiction through this consumer. |
| Finite openings | At `N=60,120`, `20*V>U_N`; actual use would require respectively `rho_6>13112500/671151` and `rho_6>24415625/1405124`. |
| Missing bridge | A proved actual lower bound on `rho_6`, or a different statistic with a proved local lower bound. No such lower bound is supplied here. |
| Suggested owner | Kimi or a future full-square finite-kernel researcher, under a new contract. This does not request Codex capacity work or Claude prefix/local-triangle work. |
| What this does not imply | No new Ramsey bound; no positive `rho_6`; no all-`N` conclusion; no conclusion for position-dependent incidences, other host regions, or non-rainbow invariants. |

Codex and Claude need not change their numerical certificates. These vectors
are not additive savings to be combined with capacity or compatibility bounds;
they belong only to the stated square-copy consumer.
