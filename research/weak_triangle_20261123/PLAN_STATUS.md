# Progress against the five Antigravity research targets

| Target | Verified result | Status |
| --- | --- | --- |
| 1. Audit the side-144 result and prove a bound of at most 143 | The baseline arithmetic and 539 square proof groups were replayed. The weak triangle excludes side 143. | Reached |
| 2. Classify small-square extensions and their rainbow profiles | 325 of 509 cutoff/offset cases have certified existence or exclusion. At order 13, all 64 placements across sides 16, 17, and 18 (15 + 21 + 28 orbits) have complete witnessed survivor lists and RUP-refuted complements. | All $T_{13}$ unit-step placements complete |
| 3. Use square symmetry and local weights to reach 140 or below | Exact three-color certificates exclude the full [141-square](SIDE_141.md) (margin `40,535,231`) and the full [140-square](SIDE_140.md) (margin `338,693,821`), proving $R_3(\mathcal L)\le 140$. At side 139 the current patch and boundary-layer LP has lower bound `1.0056 > 1`. | Reached ($R_3(\mathcal L)\le 140$) |
| 4. Determine the order-14 minimum and propagate improvements | The minimum is in $[14,17]$. Eight conditional minima are sharp. At orders 14 through 18, a coloring with exactly as many rainbows as its order has two or three boundary rainbows on different sides. | Exact minimum open |
| 5. Improve the four-color bound below 21,947,865 | The disjoint endpoint capacities and independent integer calculation give $R_4(\mathcal L)\le21{,}947{,}855$. | Reached |

### Square placements

| Side | Spacing | Witnessed | Excluded | Open | Total |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 1 | 113 | 0 | 0 | 113 |
| 17 | 1 | 149 | 0 | 0 | 149 |
| 18 | 1 | 29 | 33 | 128 | 190 |
| 21 | 2 | 0 | 0 | 14 | 14 |
| 23 | 2 | 0 | 1 | 42 | 43 |
| **Total** | | **291** | **34** | **184** | **509** |

Each row counts both cutoffs at orders 11 and 12 and the single cutoff
at order 13. Antidiagonal reflections are identified. A witnessed case
has an explicit proper square coloring. At order 13, all 28 offsets in
the 18-square are decided (27 excluded and `(3, 2)` with three surviving
oriented words), all 15 offsets in the 16-square and all 21 offsets in
the 17-square have complete surviving-word lists, and the unique stride-2
offset `(0, 0)` in the 23-square is excluded. Run
`python3 verify_placement_witnesses.py` to reproduce the table from the
witness and exclusion manifests.

### Proofs and reproduction

- [Side-143 audit](README.md), [side-141 certificate](SIDE_141.md), and [side-140 certificate](SIDE_140.md)
- [Square witnesses and exclusions](PLACEMENTS.md) and [order-13 survivor classifications across sides 16–18](ORDER13_SIDE18.md)
- [Eight sharp extension minima](ORDER14_EXTENSIONS.md), [boundary structure through order 18](BOUNDARY_LAYERS.md), and [local weighted bounds through order 32](SOURCE_FLOORS.md)
- [Four-color integer certificate](../r4_disjoint_edge_bins_20261123/README.md)

The draft *Directed L-grid proof archives for PR #19* on the
[repository Releases page](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/releases)
holds the downloadable proof traces for collaborators with write access.
