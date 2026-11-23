# Local rainbow floors for the side-140 search

Let $r$ be the rainbow count on a properly three-colored order-14 triangle
and let $r_i$ be the counts on its three order-13 faces. Then

$$
6r+5(r_1+r_2+r_3) \ge 279.
$$

The [extension enumeration](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md)
gives a minimum of 19 in an order-14 extension of an 11-rainbow face and
17 in an extension of a 12-rainbow face. The unconditional base counts
are 14 and 11 at orders 14 and 13. For $r\le16$ all three faces have
at least 13 rainbows, giving $6\cdot14+5\cdot39=279$. For $r=17,18$
each has at least 12, giving at least 282. For $r\ge19$ the same
score is at least $6\cdot19+5\cdot33=279$. A corner with base gaps
$(a,b,c)$ receives weight 6 plus 5 for each strictly positive gap.
The finite extension minima can be reproduced with
`python3 ../boundary_certificates_20261115/verify_minimizer_extensions.py --through-12`.

The [sharp extension table](ORDER14_EXTENSIONS.md) gives two further
inequalities involving all ten order-11 subtriangles or all six order-12
subtriangles of the same order-14 triangle.

## Packing and integer rounding

| Source order | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Lower bound on every proper triangle | 20 | 23 | 27 | 32 | 36 | 42 | 47 | 52 | 57 | 63 |
| Lower bound with seven extra steps of space | 22 | 26 | 31 | 36 | 41 | 45 | 50 | 56 | 62 | 68 |

For the second row of bounds, embed the triangle with step $d$ in a
proper square. Its bounding box must have space for seven further $d$-steps
in both positive coordinate directions, or in both negative directions.
A unit-step subtriangle in the source inherits this property at the same
scale. The order-12 and order-13 lower bounds under this condition are 10
and 13, respectively. Their bounding boxes fit the side-18 square patches
at (0, 0), or the reflected patches. Subtriangles with larger relative
dilation use the unconditional bounds. At order 18 the seven-step condition
already gives a lower bound of 19.

Each [packing](data/local_packing_floors.json) assigns nonnegative integer
coefficients to translated and dilated copies of smaller triangles. Expand
all six permutations of a translation, with multiplicity. Let $L$ be
the sum of the certified lower counts times their coefficients and $D$
the largest sum of coefficients on any literal host corner. If the host
has $r$ rainbows, then $Dr\ge L$, so $r\ge\lceil L/D\rceil$.
Induct in increasing order. Run `python3 verify_local_packing.py`
to expand every physical corner independently and compare the exact
quotients. These local inequalities supply inputs for the global
side-140 calculation. The verified full-square bound in this package is
[141](SIDE_141.md).

## Packing with the boundary-layer inequalities

Use the [weighted boundary inequalities at orders 14 through 18](BOUNDARY_LAYERS.md)
and the [three embedded-subtriangle weight vectors at order 14](ORDER14_EXTENSIONS.md)
as further source columns. Independent integer rounding gives the following
improved bounds. The clearance condition is the same as in the preceding table.

| Order | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Unconditional | 20 | 24 | 28 | 32 | 37 | 42 | 48 |
| With clearance | 22 | 26 | 31 | 36 | 41 | 45 | 50 |

| Order | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Unconditional | 53 | 58 | 65 | 71 | 78 | 85 | 93 |
| With clearance | 56 | 62 | 69 | 75 | 82 | 90 | 98 |

The [integer columns](data/local_boundary_packings.json) record each
source, spacing, placement, weight rule and coefficient. Run
`python3 verify_local_packing.py` to expand the weights on the literal
corner sets, check each rational quotient, and reproduce both tables.
