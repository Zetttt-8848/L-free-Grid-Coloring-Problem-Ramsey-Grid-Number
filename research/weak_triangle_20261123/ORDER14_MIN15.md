# Unconditional lower bound `r_14 >= 15` and propagated floors through order 32

Every proper three-coloring of the order-14 triangle `T_14` contains at least
**15** rainbow directed Ls (`r_14 >= 15`). Together with the boundary-layer
induction in [`BOUNDARY_LAYERS.md`](BOUNDARY_LAYERS.md), this immediately
raises the unconditional local rainbow minima for orders 14 through 18 to

```text
r_14 >= 15,   r_15 >= 16,   r_16 >= 17,   r_17 >= 18,   r_18 >= 19.
```

## Exhaustive refutation of `r_14 = 14`

By [`ORDER14_BOUNDARY.md`](ORDER14_BOUNDARY.md) and
[`BOUNDARY_LAYERS.md`](BOUNDARY_LAYERS.md), any putative proper three-coloring
of `T_14` with `r_14 = 14` has no rainbow L touching two or more outer sides,
and at most one rainbow L per outer side. The cases with `0` or `1` outer side
carrying a rainbow L are already refuted in [`data/tight_shells.json`](data/tight_shells.json).

The remaining cases have exactly `2` or `3` outer sides carrying a single
rainbow L each. Partitioning by the six-cell scale-6 coarse subtriangle `T_4`
up to geometric and palette symmetries yields:

- **2 touched outer sides (`shell 2`)**: **14** symmetry orbits;
- **3 touched outer sides (`shell 3`)**: **6** symmetry orbits.

All **20** formulas are UNSAT and carry RUP refutations independently checked
by both `drat-trim` and the standalone C99 checker `rup_check`. Their exact
DIMACS and proof SHA-256 digests are recorded in
[`data/order14_min15.json`](data/order14_min15.json). The archived proof bundle
`order14-min15-proofs.zip` has SHA-256
`8e84f7dac42c19443cdbe31909a5624a4ee4871bf46f35c979fc84270cbffb11`.

## Sharp weighted inequalities and upgraded packing floors

Combining `r_14 >= 15` with the sharp extension table in
[`ORDER14_EXTENSIONS.md`](ORDER14_EXTENSIONS.md) yields the tightened
unconditional order-14 rays:

```text
3 r_14 + 2 sum r_13 >= 123,
6 r_14 +   sum r_12 >= 150,
10 r_14 +  sum r_11 >= 220,
20 r_14 + 3 sum r_11 >= 490.
```

For `15 <= m <= 18`, since every child `T_{m-1}` now satisfies
`r_{m-1} >= m`, deleting any outer side from a coloring with `r_m = m + k`
(`k >= 1`) removes at most `k` rainbows, sharpening the multi-side boundary
inequality to `3 r_m - d_2 - 2 d_3 >= 3 m + 1`.

Re-packing these strengthened local inequalities through order 32
([`data/local_boundary_packings_15.json`](data/local_boundary_packings_15.json))
gives the following exact integer floors:

| Order | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Unconditional (`r_14 >= 15`) | 21 | 24 | 29 | 33 | 38 | 44 | 49 | 54 | 61 | 67 | 73 | 80 | 87 | 96 |
| With 7-step clearance | 22 | 26 | 31 | 36 | 41 | 46 | 51 | 57 | 63 | 69 | 76 | 83 | 91 | 99 |

## Reproduction

```sh
python3 verify_order14_min15.py --jobs 4
python3 verify_order14_min15.py --proof-dir /path/to/extracted-proofs \
    --drat-trim /path/to/drat-trim --rup-check ./rup_check --jobs 4
```
