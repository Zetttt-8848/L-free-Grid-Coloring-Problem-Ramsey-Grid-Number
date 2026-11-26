# A weak-triangle certificate for the three-color side 143

This is Part 1 of the November 23 Antigravity research plan. The certificate
proves that every coloring of the square of side 143 with at most three
colors contains a monochromatic directed equal-leg L, using the finite
triangle catalogs and local square refutations from [PR 11][pr11] at
`98af36bdb368609f38bc350b664310d7a5b45877`.

## Embedding and integer contradiction

Write the square as `{0,...,N-1}^2`. The weak triangle
`W_N = {(x,y): 0 <= y <= x < N}` contains the main diagonal.
The translation `(x,y) -> (x+1,y)` maps it bijectively to the strict triangle
`T_(N+1) = {(u,v): 0 <= v < u < N+1}`. This translation preserves the
forbidden triple `(x,y), (x+d,y), (x+d,y+d)` for every positive integer
`d`. In particular, the host of order 144 fits in a square of side 143.

Use the weights and translated triangle ceilings of the
[PR 11 certificate](../boundary_certificates_20261115/THREE_COLOR_WEIGHTED.md).
For each source placement, recalculate which ambient-square refutations fit
in the physical square. For a translation with gaps `(a,b,c)`, the weak
source starts at `(a+b,b)`. A stride-compatible patch of offset `(p,q)`,
side `s`, and scale `e` has lower-left point `(a+b-e*p,b-e*q)` and span
`e*(s-1)` on each axis. Check all four boundaries and the antidiagonal
reflection before using the patch's lower bound.

The line identity on the order-144 host bounds its total rainbow count by
`C(144,2) - 143 + floor(143/3) = 10,200`. The translated subtriangle
ceilings and ranked residual incidences give the upper score. Applying the
source floors to every placement gives the lower score. Two calculations
using physical and barycentric coordinates respectively produce the same
integers.

| Quantity | Value |
| --- | ---: |
| Weighted lower score | 10,529,664,005,555,371 |
| Weighted upper score | 10,513,208,388,341,315 |
| Lower minus upper | **16,455,617,214,056** |

Any proper coloring of the full square would satisfy both inequalities.
Their strictly positive difference proves the stated bound. The new
geometric step is the inclusion of the diagonal, with the ambient-square
positions recomputed for the smaller host square.

## Reproduction

From this directory, run both integer checks with the archived catalogs.

```sh
python3 verify_143.py
python3 verify_143_with_pr11.py
```

The 10 baseline square patches divide into 539 groups of complete
palette-normalized local cases. In this review, each saved refutation was
replayed against its reconstructed DIMACS input with both drat-trim and the
[standalone C99 RUP checker](rup_check.c). All decoded proof SHA-256 values
matched the [run manifest](data/baseline_patch_manifest.json). The saved
proof files total 341,690,580 compressed bytes. The manifest identifies
every group, and the verifier can replay the original archive or regenerate
missing proofs with python-sat's Glucose 4 solver.

```sh
cc -O3 -std=c99 rup_check.c -o rup_check
python3 verify_patch_proofs.py --proof-dir /path/to/baseline_patch_proofs \
    --drat-trim /path/to/drat-trim --rup-check ./rup_check --jobs 8
```

Add `--generate-missing` when reproducing the archive in an empty directory.
Freshly generated traces are checked against the same formulas by both tools
and can have different hashes. The original run recorded drat-trim revision
`2e3b2dc`. The inherited catalog coverage and its reproduction commands
are documented in [the local rainbow minima record](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md).

The follow-up certificates establish [side 141](SIDE_141.md),
[side 140](SIDE_140.md), and [side 139](SIDE_139.md) for three colors, and
[side 21,947,855](../r4_disjoint_edge_bins_20261123/README.md),
[side 21,947,834](../r4_subadditive_farkas_20261124/README.md), and
[side 21,947,830](../r4_stratified_farkas_20261124/README.md) for four colors.

The [side-16 through side-18 placement classifications](ORDER13_SIDE18.md) and
[rounded source floors](SOURCE_FLOORS.md) provide further local results.
The [five-target status table](PLAN_STATUS.md) links the current proofs and
records the remaining placement and exact-minimum questions.

[pr11]: https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/pull/11
