# A proper 20 by 21 rectangle

The rows in **rectangle_20_21.json** give a three-coloring of \(\{0,\ldots,19\}\times\{0,\ldots,20\}\) with no monochromatic directed equal-leg L. The 420 cells use the three colors 139, 145, and 136 times. The literal checker tests every one of the \( \sum_{d=1}^{19}(20-d)(21-d)=2,660 \) triples. The map \((x,y)\mapsto(20-y,19-x)\) gives a proper 21 by 20 rectangle. The known square lower bound is still [21](https://arxiv.org/html/2312.01159v1).

## Exactly what prevents the last row

Keep all 420 colors fixed. If the new row precedes this rectangle, its position \(y\) sees a forbidden color whenever the two old cells \((d-1,y)\) and \((d-1,y+d)\) agree in that color. The positions \(0,1,2,4,5,7,8,9,11,13\) see all three colors. The eleven other positions can be colored independently, so ten holes are necessary and sufficient.

If the new row follows the rectangle, write \(z_y\) for its color at column \(y\). Each pair \(y<j\) forbids the single assignment \(z_y=z_j=W_{20-(j-y),y}\). Enumerating subsets of blank positions gives the following exact counts.

| Number of blank cells | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Sets of positions admitting an extension | 0 | 0 | 0 | 0 | 16 |

For example, the partial last row **.221211.2..0010210211** works, with blanks at \(0,7,9,10\). The checker uses exhaustive branching on the three available colors and validates each returned partial coloring directly on the full square. These counts concern the displayed rectangle with its colors fixed.

Run **python verify_rectangle.py** for both the construction and the two extension counts.

The [whole-line obstruction](RECTANGLE_LINE_BOUNDS.md) proves that extending this rectangle to the square requires changes in at least 14 original rows and 15 columns.
