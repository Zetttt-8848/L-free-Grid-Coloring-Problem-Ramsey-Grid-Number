# Square placement witnesses for Part 2

In a proper three-coloring every directed equal-leg L has at least two
colors. The square colorings in this package give the following exact
extension results for unit-step triangles.

| Square side | Source order | Rainbow cutoff | Offset orbits with witnesses | Coverage |
| ---: | ---: | ---: | ---: | --- |
| 16 | 11 | 5 | 28 | Every offset |
| 16 | 12 | 8 | 21 | Every offset |
| 16 | 13 | 12 | 15 | Every offset |
| 17 | 13 | 12 | 21 | Every offset |
| 18 | 13 | 12 | 1 | Offset (3, 2) and its reflection |

The side-16 examples for cutoffs 5 and 8 also establish existence at
cutoffs 6 and 9, respectively. This covers all 113 side-16 combinations
in the plan after quotienting by the antidiagonal reflection.

Use coordinates `(x,y)` with `0 <= x,y < side`, in which an L has
vertices `(x,y),(x+d,y),(x+d,y+d)` for positive `d`. The file stores
`square[x][y]` and an offset `(ox,oy)` for the weak triangle of side
`order-1`. The antidiagonal reflection sends the offset to
`(gap-oy,gap-ox)` where `gap = side-order+1`, preserving every L and
the number of rainbow corners in the triangle. Each witness is given
for a representative of that orbit.

The order-13 witness at offset (3, 2) in the 18-square has exactly
12 rainbows. The [side-141 proof](SIDE_141.md) records the checked
refutations at the two offsets used in that certificate. The other
host sizes and the exhaustive classification of surviving rainbow
profiles are ongoing work.

Run `python3 verify_placement_witnesses.py` to check all colorings and
coverage from the [compressed witness file](data/placement_witnesses.json.xz).
