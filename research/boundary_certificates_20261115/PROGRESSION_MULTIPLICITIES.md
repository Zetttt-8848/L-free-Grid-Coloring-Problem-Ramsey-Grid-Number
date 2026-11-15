# Sharp bounds on four- and five-term progressions in a binary strict source

Let \(A\) be a finite set of integers such that its strict triangle admits a proper binary coloring. For \(h>0\), write \(P_j(h)=\{x:x,x+h,\ldots,x+(j-1)h\in A\}\). Then
\[
 |P_4(h)|\le3,\qquad \operatorname{diam} P_4(h)\le h \text{ when nonempty},\qquad |P_5(h)|\le1 .
\]
Both cardinality bounds are attained by suitable binary-colorable sources. Moreover, \(P_3(h)\) contains no three-term arithmetic progression of step \(g\ne h\). It contains at most one progression of step \(h\). These statements apply to each diagonal color of any proper three-color square.

## Comparing the starts modulo \(h\)

For any prescribed collection of starts, translate the smallest to zero. Express their positions as \(jh+r\), with \(0\le r<h\), and replace each distinct residue by its rank in increasing order. Then each resulting mark has label \((j,i)\), ordered lexicographically. Two formal differences are declared equal when the integral part difference agrees and either both residue differences vanish or both ordered residue pairs agree. Every such equality is a true equality of physical differences for any choice of actual residues of those ranks. Each resulting symbolic directed triple is thus a physical directed triple. These are the constraints checked below. Additional physical equalities can only add constraints.

For two four-term starts \(0,b\), separation \(b>3h\) is excluded by the [two-block proof](ORDERED_BOXES.md). The entire remaining forbidden range \(h<b\le3h\) consists of exactly four cases. For \(h<b<2h\) the start labels are \((0,0),(1,1)\). For \(b=2h\) they are \((0,0),(2,0)\). For \(2h<b<3h\) they are \((0,0),(2,1)\), and for \(b=3h\) they are \((0,0),(3,0)\). Each template has a checked refutation. Hence all starts are within a single interval of length \(h\).

Suppose now that four starts occur, with least start zero. If the greatest is smaller than \(h\), their labels are \((0,0),(0,1),(0,2),(0,3)\). If the greatest equals \(h\), their labels are \((0,0),(0,1),(0,2),(1,0)\). Both templates are impossible. For three starts strictly within one step, the generic three-residue template has a proper coloring. To realize it as integers choose residues \(0,1,3\) and step \(h=10\). These residues have distinct nonzero differences and \(h>2\cdot3\). The symbolic and physical equality relations agree, proving sharpness of the bound three.

For two five-term starts, the corresponding four-term starts already imply \(b\le h\). When \(0<b<h\), the labels are \((0,0),(0,1)\). When \(b=h\), they are \((0,0),(1,0)\). Both five-term templates are impossible. A single five-term progression admits a proper coloring, checked in the last case below, proving sharpness of the bound one.

## Three-by-three sums at arbitrary ratios

If \(P_3(h)\) contains a three-term progression of step \(g\), then \(A\) contains a translate of \(\{ih+jg:0\le i,j\le2\}\). Interchanging \(h,g\) lets us take \(g\ge h\). For \(h<g<2h\), the nine physical marks occur in a fixed order. The only possible positive ratios where two such marks can exchange order are \(1/2,1,2\), since equality has the form \((i-i')h=(j'-j)g\) with nonzero coefficients at most two in absolute value. The checker uses the order at ratio \(3/2\) and only coordinatewise equal differences. It excludes this entire interval. For \(g>2h\) the order is different and constant, and the corresponding formal case is also impossible. At \(g=2h\), coincidences leave seven consecutive \(h\)-spaced marks; its actual strict source is refuted. At \(g=h\), the five consecutive marks admit a proper coloring, and each such configuration corresponds to one five-term start. This proves the assertion about \(P_3(h)\).

Run **python verify_apmultiplicity.py**. It reconstructs the 13 formulas and checks every coloring or reverse-unit-propagation proof in **progression_certificates.json**. The earlier two-separated-progressions case is checked independently by **verify_box_shapes.py**. The multiplicity proof works for arbitrary finite spans.
