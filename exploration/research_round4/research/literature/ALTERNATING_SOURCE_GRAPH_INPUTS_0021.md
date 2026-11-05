# Alternating source graphs: bounded lonesum/Ferrers input

## Source pattern

For a fixed additive parallelogram
\((u,u+d,u+h,u+d+h)\), regard the two opposite `d`-cells and the two
opposite `h`-cells as the four positions of a bipartite rectangle.  A red pair
on one opposite side together with a blue pair on the other is an alternating
two-color \(C_4\).  Properness forbids that alternating pattern on the
parallelograms supported by the integer source.

This is much sparser than a full bipartite matrix condition: the available
rectangles have row/column displacement tied by the additive relation
\(u+(u+d+h)=(u+d)+(u+h)\).  The four focused searches below found the
following exact full-support inputs and did not locate an additive-only
extension.

## 1. Ryser's lonesum characterization: exact full-matrix theorem

**H. J. Ryser, *Combinatorial properties of matrices of zeros and ones*,
Canadian Journal of Mathematics 9 (1957), 371--377; restated as Theorem 1
in [Brewbaker, *A combinatorial interpretation of the Genocchi numbers*](https://math.colgate.edu/~integers/i2/i2.pdf).**

Ryser's theorem says that a finite zero-one matrix is uniquely determined by
its row-sum and column-sum vectors (is *lonesum*) if and only if it contains
neither of the two permutation matrices

\[
\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

as a two-by-two submatrix, after choosing **arbitrary** two rows and
arbitrary two columns.  In a red/blue coloring of a complete bipartite graph,
these are exactly the two alternating \(C_4\) colorings.

**Translation and limit.**  If the source rule were known for every choice
of two rows and two columns in one global bipartite incidence matrix, it would
give a lonesum matrix and hence nested neighborhoods/Ferrers structure.  The
source rule only covers additive parallelograms.  It leaves most two-by-two
submatrices unconstrained, so Ryser's hypothesis cannot presently be invoked.
The theorem is structural rather than a bound on the number of edges or on
\(|A|\) versus span.

## 2. Chain/Ferrers graph characterization: another all-rectangle condition

**D. Dyer and H. Müller, [*Counting subgraphs in Hamiltonian graphs*](https://www.numdam.org/item/10.5802/afst.1469.pdf), Lemma 2.20 and the chain-graph discussion in Section 2.5 (which records the classical characterization).**

For a bipartite graph \(G=(X,Y,E)\), a chain (Ferrers) graph has an ordering
of one part under which its neighborhoods are nested.  Equivalently, it has
no induced \(2K_2\): no two independent edges whose two cross edges are both
absent.  Matrix-wise, after independently ordering rows and columns, its
ones occupy a Ferrers shape.

**Translation and limit.**  Taking red positions as edges, an alternating
red/blue rectangle is precisely an induced \(2K_2\) in the red bipartite
graph (and likewise in blue).  Thus absence of alternating \(C_4\)'s on all
rectangles gives the chain/Ferrers conclusion.  But this equivalence also
requires that the missing cross positions are present as matrix entries and
that every choice of two rows and columns is tested.  Additive-supported
parallelograms do not supply that complete test set.  The cited source gives
no partial/additive-support stability estimate.

## 3. Edge-colored \(C_4\) extremal work: different color requirement

**Y. Wu, [*Properly colored and rainbow \(C_4\)'s in edge-colored graphs*](https://doi.org/10.1002/jgt.23019), Journal of Graph Theory (2024).**

This paper studies conditions forcing properly colored or rainbow four-cycles
in edge-colored graphs, including a bipartite extremal counterpart of a
rainbow-\(C_4\) result.  Its hypotheses concern color degrees / the number of
colors in an edge-colored host graph, and its conclusions require adjacent
cycle edges to receive different colors or all four edge colors to differ.

**Mismatch.**  A two-color alternating source boundary has opposite edges
equal and adjacent edges different.  It is neither a rainbow \(C_4\) nor the
standard proper-edge-coloring setting, and the host is not the sparse family
of additive parallelograms.  Consequently these extremal bounds do not give
an edge count for a red/blue translation graph or a source-span coefficient.

## Bounded conclusion

The usable exact statement is Ryser/Ferrers: full absence of alternating
two-by-two patterns forces a lonesum/chain structure.  Its essential
quantifier is over all pairs of rows and all pairs of columns.  I did not find
within this bounded four-query search a theorem replacing that complete
quantifier by only the additive parallelograms of an integer source, nor an
explicit extremal bound for those translation-restricted red/blue graphs.
This is a limited retrieval result, not a general nonexistence assertion.
