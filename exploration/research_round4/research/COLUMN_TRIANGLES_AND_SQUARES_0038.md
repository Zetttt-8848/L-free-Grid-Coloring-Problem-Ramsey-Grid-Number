# Column triangles and a literal square-source instance

Root integration of new bounded discovery, continuation 0038. This note
describes a restrictive source class and shows directly that the square
source already lies outside it. It makes no noncolorability claim for
the square source itself.

For a in A, the anchored column graph has vertices t in A with t>a,
and joins u<v when a+v-u is in A. A triangle has unique ordered rows

    a+x, a+x+r, a+x+r+s,  x,r,s>0.

Its three required difference labels are a+r,a+s,a+r+s. Consequently
the triangle exists exactly when the seven expressions

    a+{0,x,r,s,x+r,r+s,x+r+s}                         (1)

all belong to A. Coincidences among the seven expressions are allowed;
the three row vertices themselves remain distinct. The expression
a+x+s is not required.

If every anchored column graph is bipartite, choosing a proper graph
two-coloring independently in each column gives a proper coloring of
V(A): every source corner has its first cell and completion joined
in that column graph, so those two colors differ. This is a sufficient
construction criterion. A general proper source coloring may have
same-color edges in a column graph, with the corner's third cell
preventing monochromaticity. Thus graph bipartiteness is not necessary.

In particular, excluding (1) in every column is a necessary condition
for this special bipartite-column construction, but not for general
two-color source properness.

## The small square instance

The new finite graph discovery in fibers/SQUARE_COLUMN_DISCOVERY_0038.py
looked at square roots through 300 and stopped at the first odd cycle.
The following literal identities give a complete direct instance
independently of using a BFS verdict as a premise:

    169-121+1=49,
    289-169+1=121,
    289-121+1=169.                                   (2)

All five integers 1,49,121,169,289 are squares. Equation (2) makes
121,169,289 a triangle in the column graph anchored at 1. In (1),
take a=1,x=120,r=48,s=120; the seven expressions are

    1,121,49,121,169,169,289.

The repeated expressions are legitimate. An arbitrary two-coloring of
the three anchored cells (121,1),(169,1),(289,1) has a same-color pair,
and (2) supplies its actual corner. A proper source coloring must give
that corner's third cell the opposite color. It cannot arrange for
every corner to have opposite colors already on its first cell and
completion in this column.

Hence an arbitrary square source containing the squares through 17^2
cannot be colored by the special strategy of making every column graph
bipartite. This does not rule out a proper coloring of its strict
source triangle: the weaker NAE condition permits the same-color pair
just described. The old square-source coloring record was not rerun.
