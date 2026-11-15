# Which ordered progressions force a binary corner

Consider a single diagonal color in a proper three-color square. Its marks \(A\) carry a properly two-colored strict triangle \(V(A)\). The following small configurations therefore constrain the diagonal word. In particular, **two nonoverlapping four-term progressions of the same color and step cannot occur at ordered starts separated by more than three steps**. The finite proof has 28 binary cells. The [full progression bounds](PROGRESSION_MULTIPLICITIES.md) sharpen this to at most three starts in an interval of length one step and at most one start of a five-term progression. It directly excludes a specific pair of boundary words at side 460 that survives the numeric test for 461.

Write the coordinates of a product in decreasing order of significance. Map a tuple \(x\) to \(\sum_i b_i x_i\) with positive integer \(b_i\). Suppose each increment in a more significant coordinate exceeds the whole span of the subsequent coordinates. The encoded marks are distinct, and their order agrees with lexicographic order. Every coordinatewise equality of differences gives an actual equality of differences, with the same signs. The symbolic directed triples below are consequently present for every such choice of coefficients.

| Numbers of choices per coordinate | Strict cells | Symbolic binary strict source |
|---|---:|---|
| 2, 4 | 28 | Impossible |
| 4, 2 | 28 | Colorable |
| 2, 2, 3 | 66 | Impossible |
| 2, 3, 2 | 66 | Impossible |
| 3, 2, 2 | 66 | Colorable |
| 2, 2, 2 | 28 | Colorable |
| 3, 3 | 36 | Impossible |

An impossible row applies for every ordered embedding above. For a colorable row, choose each higher coefficient greater than twice the entire subsequent span. Equality of encoded differences then implies equality of all coordinate differences, so the exhibited coloring supplies actual integer examples. This distinction matters for intermediate scales that have additional equal differences.

For instance, take the marks \(a+ih+jb\) for \(0\le i<4\), \(j\in\{0,1\}\), with \(b>3h>0\). The first row of the table applies. In a proper grid this implies that the set of starts of monochromatic four-term progressions with fixed color and step \(h\) has diameter at most \(3h\). For the three-factor example take \(a+ih+jb+kc\), \(0\le i<3\), \(j,k\in\{0,1\}\), \(b>2h\), \(c>b+2h\). The row \(2,2,3\) applies. These results use the direction of the forbidden L.

## Boundary example at side 460

Use the same 34-letter word **1110002122020220110110221020101022** at physical positions \(0,\ldots,33\) and \(426,\ldots,459\). With effective 24-mark span at least 426, the loss in the [35-letter method](THREE_COLOR_461.md), adapted to 34 letters, is 3,797,480,611. The baseline is \(-13,601,128,606\), and the margin after the loss is \(-2,208,686,773\). Equal ends permit the selected minima to match maxima exactly 426 positions later. But positions \(25,27,29,31\) and \(451,453,455,457\) all have color zero. Their two progressions have step 2 and separation 426. The first obstruction above excludes this pair from any proper grid.

The [optimal 24-mark exclusion](NO_OPTIMAL_461.md) applies at side 460 as well. A placement at side 460 is contained in the tested length-461 interval, so its original color would have at most 95 positions. The one-color inequality at side 460 gives at least 134 positions in every color. This observation justifies using the effective span 426 in the boundary example. The general three-color upper bound remains 461.

## Verification

Run **python verify_box_shapes.py** to check every truth assignment or short refutation in **ordered_box_certificates.json**. The checker constructs the geometric triples by following a leftmost cell. The producer enumerated equal ordered differences. Each triple gives the two clauses excluding the all-zero and all-one assignments. A negative certificate adds only clauses whose negation gives a contradiction by unit propagation, ending with the empty clause. The positive certificates give all cell colors.
