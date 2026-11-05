# A proper three-color triangle with exactly one rainbow corner

Root explicit construction, R4-RESEARCH-0004. This disproves the local hypothesis that every corner-free three-coloring of T_10 has at least seven rainbow corners. It is not a grid lower-bound construction.

For T_10={(v,u):0<=u<v<10}, the colors in row v are listed in column order u=0,...,v-1:

| row | colors |
|---|---|
| 1 | 0 |
| 2 | 10 |
| 3 | 120 |
| 4 | 0002 |
| 5 | 01111 |
| 6 | 222210 |
| 7 | 0021102 |
| 8 | 01022111 |
| 9 | 200120122 |

## No monochromatic corner

Every corner has two distinct endpoints (u+d,u),(v+d,v) on one slope-one diagonal, with u<v, and completion (v+d,u). The table below lists every endpoint-color group of size at least two. For each group, its completion colors are given in the lexicographic order of pairs of starts. Every listed completion color differs from the endpoint color, excluding all possible monochromatic corners. Groups of size zero or one cannot provide an equal-color endpoint pair.

| offset d | endpoint color | starts | completion colors |
|---|---|---|---|
| 1 | 0 | 0,1,2,5 | 1,1,2,2,2,2 |
| 1 | 1 | 4,7 | 2 |
| 1 | 2 | 3,6,8 | 1,1,1 |
| 2 | 0 | 2,5 | 2 |
| 2 | 1 | 0,3,4,6 | 0,2,0,2,2,2 |
| 2 | 2 | 1,7 | 0 |
| 3 | 1 | 0,2,4,5,6 | 0,0,0,2,2,0,0,2,2,0 |
| 4 | 0 | 0,5 | 2 |
| 4 | 1 | 1,3 | 0 |
| 4 | 2 | 2,4 | 0 |
| 5 | 2 | 1,2,3,4 | 0,1,0,0,0,1 |
| 6 | 0 | 1,2 | 1 |
| 7 | 0 | 0,2 | 2 |
| 8 | 0 | 0,1 | 2 |

Offset 9 has only one cell. These are all positive offsets in T_10. The full coloring and the endpoint-pair rule therefore prove corner-freeness.

## Exactly one rainbow corner

The sums of squared color counts over the row lines, column lines, and slope-one diagonal lines are respectively 121, 127, and 125. These numbers follow by counting the three colors in each line of the displayed array and squaring those counts. Each line family has lengths 1,...,9, whose squares sum to 285. Consequently the discrepancy V defined in TRIANGLE_RAINBOW_ENERGY.md is

    V=121+127+125-(3*285)/3=88.

There are M=binom(10,2)=45 cells. The proved identity V+2R=2M applies because corner-freeness was established above, so R=(90-88)/2=1. The one rainbow corner is

    {(4,2),(6,2),(6,4)},

whose colors are 0,2,1 and whose step is two. This also explicitly identifies the counted corner.

The construction establishes that a universal local lower bound R>=2 is already false for T_10. The discovery's raw negative for R=0 is not needed for this conclusion and is not asserted as a theorem here.
