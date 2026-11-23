# Square placement witnesses for Part 2

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
| 18 | 13 | 12 | 1 | Offset (3, 2) and its reflection |

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

The order-13 witness at offset (3, 2) in the 18-square has exactly
12 rainbows. The [side-141 proof](SIDE_141.md) records the checked
refutations at the two offsets used in that certificate. The [order-13 placement proof](ORDER13_SIDE18.md) classifies the full
set of surviving profiles at this offset and excludes 26 side-18
offset orbits.

For $T_{12}$ at offset (0, 1) in the 18-square, every proper coloring
has at least ten rainbows. Reflection gives the same conclusion at
(6, 7). The [group manifest](data/order12_side18_0_1.json.xz) covers all
96,360 palette-normalized oriented words with at most nine rainbows in
1,004 consecutive groups. This excludes the placement at both cutoffs
8 and 9. To replay the traces, use the command in the
[side-141 reproduction instructions](SIDE_141.md#reproduction) with
`--collection order12-side18`.

Run `python3 verify_placement_witnesses.py` to check all colorings and
coverage from the [compressed witness file](data/placement_witnesses.json.xz).
