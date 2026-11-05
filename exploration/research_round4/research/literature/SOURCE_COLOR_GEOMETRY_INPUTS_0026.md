# Source-color geometry: bounded edge/additive retrieval

## Target

The source colors the edges/cells \((v,u)\), \(u<v\), of an integer set.
On each supported additive parallelogram it forbids a specified
three-edge monochromatic completion pattern.  The desired result would bound
additive energy or force a decomposition into bounded-complexity Freiman or
two-distance pieces.  This is not a vertex coloring of an ambient group.

## 1. Rainbow Turán/additive graph encoding: exact edge/additive bridge, wrong color regime

**Peter Keevash, Dhruv Mubayi, Benny Sudakov and Jacques Verstraëte,
[*Rainbow Turán Problems*](https://homepages.math.uic.edu/~mubayi/papers/rainbow-turan-final.pdf).**

For a subset \(B\) of an abelian group \(G\), the paper forms a bipartite
graph with both parts copies of \(G\), joins \(x\) to \(y\) when \(x-y\in B\),
and colors that edge by \(x-y\).  This is a **proper** edge-coloring.  Their
additive application states that if \(B\) is a \(B_k^*\)-set (no disjoint
equal-sum \(k\)-subsets), the graph has no rainbow \(C_{2k}\), linking
additive relations to rainbow extremal graph bounds.

**Mismatch.**  The source has only two unrestricted edge colors, while the
paper's colors are the individual differences and are proper at each vertex.
The forbidden source pattern is monochromatic on three selected cells, rather
than rainbow on an even cycle.  A proper source coloring does not produce the
paper's difference-labeled graph, so its \(B_k^*\) and rainbow-Turán bounds do
not imply an energy estimate or a factor decomposition here.

## 2. Fixed-volume parallelogram colorings: vertex colors and different geometry

**Vjekoslav Kovač, [*Coloring and density theorems for configurations of a
given volume*](https://doi.org/10.1112/plms.70143), 2026.**

This work studies measurable colorings of Euclidean space and monochromatic
or rainbow geometric configurations, including parallelogram restrictions of
fixed area/directions.  Its objects are colors of **points** in a continuum,
and its configurations are four vertices of geometric parallelograms.

**Mismatch.**  Source colors live on ordered pairs of marks; a source
parallelogram contributes cells/edges, with the outer diagonal participating
as a third colored object.  No passage from the strict source rule to a
vertex-coloring, a fixed-area condition, or the density hypotheses of this
theorem is supplied.  It therefore gives neither an additive-energy bound nor
a Freiman-factor conclusion.

## Bounded result

The first source is a genuine primary bridge between additive equations and
edge-colored graphs, but it relies on difference labels and rainbow cycles.
The second is geometrically about parallelograms but colors vertices.  No
newly located four-query source states a structure or energy theorem for the
two-edge-color strict source completion condition.  This limited finding does
not establish novelty or exclude a specialized theorem elsewhere.
