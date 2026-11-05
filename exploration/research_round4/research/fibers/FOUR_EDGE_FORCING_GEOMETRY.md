# Four-edge forcing trees can use three labels

## Setup

Fix a corner-free color class \(C\), and let \(G_C\) be the graph on the
remaining cells \(U\). An edge \(xy\) of \(G_C\) is labelled by the unique
cell \(\lambda(xy)\in C\) for which
\(\{x,y,\lambda(xy)\}\) is a corner. Edges with the same label form a
matching.

Consider a branching four-edge forcing tree for a corner whose three
cells are terminals and leaves. It has five vertices and degree sequence
\[
  3,2,1,1,1,
\]
and its three terminals are precisely its leaves. Write its vertices as
\[
  a,b,c,o,w
\]
so that \(a,b,c\) are the terminals, \(o\) has degree \(3\), \(w\) has
degree \(2\), and its edges are
\[
  oa,\quad ob,\quad ow,\quad wc.
\]

## Proposition

The minimum possible number of distinct \(C\)-labels on a branching
tree of this type is exactly \(3\), even under the requirement that
\(C\) is corner-free. The general lower bound, which also covers
four-edge paths with a terminal at the middle vertex, is proved in
`../TWO_LABEL_COMPONENTS.md`.

For this branching shape, if exactly three labels occur, then, up to interchanging \(a\)
and \(b\), the repeated label occurs on \(oa\) and \(wc\). Thus it occurs
on a center--terminal edge and the remote terminal edge.

### Lower bound and equality classification

The three edges \(oa,ob,ow\) meet at \(o\). Since each label class is a
matching, these three edges have pairwise distinct labels. Hence at least
three labels are necessary.

If only three labels occur on all four edges, the remaining edge \(wc\)
must repeat one of the labels on \(oa,ob,ow\). It cannot repeat the label
on \(ow\), because those two edges meet at \(w\). It may therefore repeat
only the label on \(oa\) or on \(ob\). These two cases are interchanged by
swapping \(a\) and \(b\), proving the classification.

### Explicit realization with three labels

Use cells \((v,u)\) with \(0\leq u<v\leq 4\), and take the terminal corner
\[
  a=(1,0),\qquad c=(2,0),\qquad b=(2,1).
\]
Choose the two internal vertices
\[
  o=(4,3),\qquad w=(4,2),
\]
and let
\[
  C=\{(4,0),(4,1),(3,2)\}.
\]
The four tree edges and their labels are
\[
\begin{array}{c|c|c}
\text{edge}&\text{label in }C&\text{resulting corner}\\ \hline
oa&(4,0)&\{(1,0),(4,0),(4,3)\}\\
ob&(4,1)&\{(2,1),(4,1),(4,3)\}\\
ow&(3,2)&\{(3,2),(4,2),(4,3)\}\\
wc&(4,0)&\{(2,0),(4,0),(4,2)\}.
\end{array}
\]
Indeed, the first, second, and fourth rows are obtained from pairs on a
common offset diagonal, while the third is obtained from the two adjacent
cells in row \(4\). Thus all four displayed edges belong to \(G_C\), and
the first and fourth, which are disjoint, share their label. The tree
connects all three cells of the terminal corner through four edges and
uses exactly the three displayed labels.

It remains to check the hypothesis on \(C\). The cells \((4,0)\) and
\((4,1)\) are the only pair in \(C\) lying on a common row, column, or
offset diagonal; their corner completion is \((3,0)\), which is not in
\(C\). Hence \(C\) contains no corner.

Consequently, corner-freeness of \(C\) does not raise the four-edge label
minimum from three to four.
