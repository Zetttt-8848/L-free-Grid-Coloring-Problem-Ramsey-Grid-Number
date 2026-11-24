# Boundary rainbows at order 14 and budget 14

If a properly three-colored $T_{14}$ has fourteen rainbow Ls, **each
rainbow L that meets the boundary meets exactly one of its three
outer sides**. In particular, every L of step 11 or 12 is bichromatic.
The existence of a proper coloring with fourteen rainbows remains open.
The [boundary-layer proof](BOUNDARY_LAYERS.md) further forces two or three
distinct boundary rainbows at this count and propagates the conclusion
through order 18.

There is also an unconditional weighted inequality. Give a corner
weight 3 if it meets at most one outer side, 2 if it meets two and
1 if it meets three. Every proper coloring has weighted rainbow score
at least **42**.

Write the base gaps of a directed L of step $h$ with first cell $(x,y)$
as $(x-y-1,y,13-x-h)$. These gaps sum to $12-h$.
A zero gap means that the L has two vertices on the corresponding
outer side. An L meeting at least two outer sides therefore has gaps
$(0,0,12-h)$ after a geometric symmetry. Each $1\le h\le12$ gives
one such orbit. The largest step meets all three sides. These twelve
orbits include every L of step 11 or 12.

The [order-13 extension minima](SOURCE_FLOORS.md) give at least thirteen
rainbows on every order-13 face of a triangle with fourteen rainbows.
Deleting an outer side removes at most one rainbow. If the designated
L is rainbow, every other L on each outer side it meets must be
bichromatic. The finite tests fix the colors of the designated L to
0, 1, 2 in vertex order, which preserves a representative of every
coloring up to palette permutation.

The formula enforces one color per cell, forbids monochromatic Ls,
and marks an L whenever its three colors differ. At most fourteen Ls may
be marked. For each smaller translated triangle with guaranteed minimum
$f$, at most $14-f$ marks can lie outside it. The tests at steps 1
through 11 use $f=13,10,7,1$ for orders 13, 12, 11, 10 respectively.
The order-11 and order-12 values follow from the [sharp extension
table](ORDER14_EXTENSIONS.md). At step 12, the weaker unconditional
values 6 and 3 suffice at orders 12 and 11.

All twelve formulas have RUP refutations. The [manifest](data/order14_boundary.json)
records each formula and proof SHA-256. The archive
`order-14-two-face-rup.zip` has SHA-256
`7235eaf4f15b8acf1fc362bb2a5d85507833054dcb8711ab9d89e97402a1d8a1`.
With python-sat installed, extract the archive into one directory and run

```sh
cc -O3 -std=c99 rup_check.c -o /tmp/lgrid-rup-check
python3 verify_order14_boundary.py --proof-dir /path/to/extracted-proofs \
    --drat-trim /path/to/drat-trim --rup-check /tmp/lgrid-rup-check --jobs 2
```

Passing `--generate-missing` regenerates a missing trace with Glucose.
The checks rebuild the formulas and replay the proofs with both tools.

## Weighted inequality at every rainbow count

Let $t$ be the total number of rainbows. Let $d_2$ and $d_3$ count the
rainbows meeting exactly two and exactly three sides. The unique extreme
corner gives $d_3\le1$. At $t=14$ the twelve refutations give
$d_2=d_3=0$, hence the weighted score is 42. At larger $t$, write $B$
for the maximum number of rainbows that can disappear upon deletion of
one side. Summing over sides gives $2d_2+3d_3\le3B$, so
$d_2+2d_3\le\lfloor(3B+1)/2\rfloor$.

For $t=15,16$, every remaining order-13 triangle has at least 13 rainbows,
so $B\le t-13$. For $t=17,18$ the corresponding bound is $B\le t-12$.
For $t\ge19$ it is $B\le t-11$. Substitution bounds the weighted score
$3t-d_2-2d_3$ below by 42, 43, 43, 45 at $t=15,16,17,18$ respectively.
For $t\ge19$ the lower estimate is increasing and starts at 45.
