# Square placement witnesses and exclusions for Part 2

In a proper three-coloring every directed equal-leg L has at least two
colors. The square colorings in this package give the following exact
extension results for unit-step triangles.

| Square side | Source order | Rainbow cutoff | Offset orbits with witnesses | Coverage |
| ---: | ---: | ---: | ---: | --- |
| 16 | 11 | 5 | 28 | Every offset |
| 16 | 12 | 8 | 21 | Every offset |
| 16 | 13 | 12 | 15 | Every offset |
| 17 | 11 | 5 | 36 | Every offset |
| 17 | 12 | 8 | 28 | Every offset |
| 17 | 13 | 12 | 21 | Every offset |
| 18 | 11 | 5 | 8 | Eight representatives |
| 18 | 11 | 6 | 12 | Includes the eight at cutoff 5 |
| 18 | 12 | 9 | 8 | Eight representatives |
| 18 | 13 | 12 | 1 | Offset `(3, 2)` and its reflection |

The cutoff-5 and cutoff-8 witnesses also establish existence at cutoffs
6 and 9. This covers all 113 side-16 and all 149 side-17 combinations
in the plan after quotienting by antidiagonal reflection. A further 29
side-18 combinations have explicit square colorings in this archive.

Use coordinates `(x,y)` with `0 <= x,y < side`, in which an L has
vertices `(x,y),(x+d,y),(x+d,y+d)` for positive `d`. The file stores
`square[x][y]` and an offset `(ox,oy)` for the weak triangle of side
`order-1`. The antidiagonal reflection sends the offset to
`(gap-oy,gap-ox)` where `gap = side-order+1`, preserving every L and
the number of rainbow corners in the triangle. Each witness is given
for a representative of that orbit.

## Certified exclusions beyond the baseline

- **Order 13 in the 18-square (`stride = 1`)**: The [order-13 placement proof](ORDER13_SIDE18.md)
  completes all 28 offset orbits, excluding **27** orbits (all offsets except `(3, 2)`)
  and classifying all surviving oriented words at sides 16, 17, and 18.
- **Order 12 at `(0, 1)` in the 18-square (`stride = 1`)**: Every proper coloring
  has at least ten rainbows (and likewise at `(6, 7)` by reflection). The
  [group manifest](data/order12_side18_0_1.json.xz) covers all 96,360
  palette-normalized oriented words with at most nine rainbows in 1,004
  consecutive groups, excluding both cutoffs 8 and 9.
- **Order 11 at `(0, 0)` in the 18-square (`stride = 1`, cutoff 5)** and
  **Order 13 at `(0, 0)` in the 23-square (`stride = 2`, cutoff 12)**:
  The [side-140 patch manifest](data/side_140_patch_manifest.json.xz) excludes
  all 16,452 oriented words of $T_{11}$ with at most five rainbows at `(0, 0)`
  in the 18-square (172 RUP groups) and all 2,928 oriented words of stride-2
  $T_{13}$ with at most twelve rainbows in the 23-square (31 RUP groups). Note
  that `23 - 1 = 2 * 11`, so the stride-2 23-square has the exact bounding box
  of a dilated $T_{13}$ at every even step $d$, upgrading every even-dilation
  copy of $T_{13}$ across the entire host square to at least 13 rainbows.

- **Order 12 at `(0, 0)` in the 21-square (`stride = 2`, cutoff 6)**:
  The [stride-2 order-12 manifest](data/stride2_order12_21_manifest.json.xz)
  excludes all 204 palette-normalized oriented words of $T_{12}$ with at most
  six rainbows in 34 consecutive six-word RUP groups (`21 - 1 = 2 * 10`, so
  every even-dilation copy of $T_{12}$ across the entire host square has at
  least seven rainbows).

Run `python3 verify_placement_witnesses.py` to check all literal colorings and
updated plan totals, and `python3 verify_new_patches.py --collection side-140`
(or `--collection order12-side18` / `--collection stride2-order12`) to verify
the formula and RUP group manifests.
