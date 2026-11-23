# Progress against the five Antigravity research targets

| Target | Verified result | Status |
| --- | --- | --- |
| 1. Audit the side-144 result and prove a bound of at most 143 | The baseline arithmetic and 539 square proof groups were replayed. The weak triangle excludes side 143. | Reached |
| 2. Classify small-square extensions and their rainbow profiles | 322 of 509 cutoff/offset cases have certified existence or exclusion. At order 13 and side 18, 27 of 28 offsets have a complete survivor list. | Partial |
| 3. Use square symmetry and local weights to reach 140 or below | The exact three-color certificate excludes the full 141-square, with a positive margin of 40,535,231. | 141 proved, 140 open |
| 4. Determine the order-14 minimum and propagate improvements | The minimum is in $[14,17]$. Eight conditional minima are sharp. At orders 14 through 18, a coloring with exactly as many rainbows as its order has two or three boundary rainbows on different sides. | Exact minimum open |
| 5. Improve the four-color bound below 21,947,865 | The disjoint endpoint capacities and independent integer calculation give $R_4(L)\le21,947,855$. | Reached |

### Square placements

| Side | Spacing | Witnessed | Excluded | Open | Total |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 1 | 113 | 0 | 0 | 113 |
| 17 | 1 | 149 | 0 | 0 | 149 |
| 18 | 1 | 29 | 31 | 130 | 190 |
| 21 | 2 | 0 | 0 | 14 | 14 |
| 23 | 2 | 0 | 0 | 43 | 43 |
| **Total** | | **291** | **31** | **187** | **509** |

Each row counts both cutoffs at orders 11 and 12 and the single cutoff
at order 13. Antidiagonal reflections are identified. A witnessed case
has an explicit proper square coloring. Listing all its surviving words
requires a separate classification. At order 13 in the 18-square the
only outstanding offset is (0, 6). The placement (3, 2) has exactly
three surviving oriented words. Run `python3 verify_placement_witnesses.py`
to reproduce the table from the witness and exclusion manifests.

### Proofs and reproduction

- [Side-143 audit](README.md) and [side-141 three-color certificate](SIDE_141.md)
- [Square witnesses](PLACEMENTS.md) and [order-13 survivor classifications](ORDER13_SIDE18.md)
- [Eight sharp extension minima](ORDER14_EXTENSIONS.md), [boundary structure through order 18](BOUNDARY_LAYERS.md), and [local weighted bounds through order 32](SOURCE_FLOORS.md)
- [Four-color integer certificate](../r4_disjoint_edge_bins_20261123/README.md)

The draft *Directed L-grid proof archives for PR #19* on the
[repository Releases page](https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/releases)
holds the downloadable proof traces for collaborators with write access.
