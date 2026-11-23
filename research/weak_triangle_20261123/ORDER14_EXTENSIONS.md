# Sharp order-14 extension minima

Let $T_m$ have cells $(x,y)$ with $1\le x<m$ and $0\le y<x$. Write $r_m$ for
the number of rainbow directed Ls in a proper three-coloring of $T_m$.
Among colorings of $T_{14}$ that contain a translated unit-step $T_m$
with $r_m\le k$, the exact minimum of $r_{14}$ is as follows.

| Subtriangle | Cutoff $k$ | Minimum on $T_{14}$ | Oriented source colorings |
| --- | ---: | ---: | ---: |
| $T_{11}$ | 3 | 20 | 66 |
| $T_{11}$ | 4 | 19 | 798 |
| $T_{11}$ | 5 | 17 | 16,452 |
| $T_{11}$ | 6 | 17 | 356,406 |
| $T_{12}$ | 6 | 19 | 204 |
| $T_{12}$ | 7 | 18 | 1,578 |
| $T_{12}$ | 8 | 17 | 11,028 |
| $T_{12}$ | 9 | 17 | 96,360 |

For the upper endpoints the [data file](data/order14_extension_minima.json)
gives one literal 91-cell coloring per row. The verifier checks all 364
directed Ls and cuts out every translation of the indicated subtriangle.
The minimum of $r_{14}$ over **all** proper colorings remains between 14
and 17 inclusive.

At the lower endpoint, the [boundary refutations](ORDER14_BOUNDARY.md)
exclude all twelve orbits of rainbow Ls touching multiple outer sides.

## Exhaustive lower endpoints

Take the complete [low-rainbow catalogs](../boundary_certificates_20261115/triangle_grid_catalogs.json.xz)
through 6 at order 11 and 9 at order 12. Expand all six permutations of
the barycentric coordinates and normalize color names by first appearance.
For a source translated by $(a+b,b)$, its three boundary margins are
$(a,b,14-m-a-b)$. Permuting the three barycentric coordinates of the host
permutes these margins, preserves directed Ls as unordered triples, and
induces one of the six enumerated source orientations. It therefore
suffices to use the three sorted margin triples at order 11 and the two
at order 12. Every matching coloring and placement occurs up to symmetry.

For each oriented source and each placement, the [extension search](fixed_subtriangle.cpp)
tries all three colors of each remaining cell. It checks each L as soon
as its last cell has been assigned. A monochromatic L or a rainbow count
above the budget rules out every completion of that branch. In each row,
budget one below the reported minimum exhausts the search. From this directory run

```sh
c++ -O3 -std=c++17 fixed_subtriangle.cpp -o /tmp/fixed_subtriangle
python3 verify_order14_extensions.py /tmp/fixed_subtriangle
```

## Consequences for weighted rainbow counts

If $r_{14}\le16$, every one of the ten $T_{11}$ subtriangles has at least
seven rainbows and every one of the six $T_{12}$ subtriangles has at least
ten. Writing the sums over all translated unit-step subtriangles gives

$$
20r_{14}+3\sum r_{11}\ge490,\qquad
24r_{14}+5\sum r_{12}\ge636.
$$

For the first inequality, partition $r_{14}$ into $14$ through $16$,
$17$ through $18$, $19$, and $20$ or higher. The respective lower
bounds on each $r_{11}$ are 7, 5, 4, and 3. The resulting left-hand
sides are at least 490, 490, 500, and 490. For the second inequality use
$14$ through $16$, $17$, $18$, and $19$ or higher. The lower bounds on
each $r_{12}$ are 10, 8, 7, and 6, giving 636, 648, 642, and 636.
The unconditional source minima and the corresponding inequality for
the three order-13 faces are recorded in [the local bounds](SOURCE_FLOORS.md).
