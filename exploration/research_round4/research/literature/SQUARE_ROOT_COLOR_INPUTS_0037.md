# Square-root source corners: bounded primary-source search

## Exact target

The requested object colors directed cells/edges
\((b^2,a^2)\), with square endpoints, in two colors.  It forbids a
monochromatic ordered triple
\[
(b^2,a^2),\quad(d^2,a^2),\quad(d^2,c^2)
\]
when \(a<c\), \(b<d\), and
\(b^2-a^2=d^2-c^2>0\).  This is an edge-color condition on a selected
square-root source, not a coloring of the roots themselves.

Three focused query batches were run: (i) Pythagorean/edge-color Ramsey,
(ii) rational-square and 2-adic Ramsey colorings, and (iii) Boolean
Pythagorean and quadratic partition-regularity results.  Two primary sources
were read in full-source form below.  No general-corners source was replayed.

## 1. Boolean Pythagorean triples: exact theorem, wrong colored object

**M. J. H. Heule, O. Kullmann, and V. W. Marek, [*Solving and Verifying the
boolean Pythagorean Triples problem via Cube-and-Conquer*](https://arxiv.org/abs/1605.00723),
Theorem 1.1.**  The theorem states that \(\{1,\ldots,7824\}\) can be
partitioned into two sets with no monochromatic integer triple
\(a^2+b^2=c^2\), while this is impossible for \(\{1,\ldots,7825\}\).
The paper encodes one Boolean variable \(x_i\) for each **integer vertex**
\(i\), and for each Pythagorean triple imposes the two NAE clauses on
\(x_a,x_b,x_c\) (Section 5.1).

**Mismatch.**  The square-root source has a Boolean variable for each
ordered edge \((b^2,a^2)\), and its three edges are linked by an
equal-*difference* parallelogram.  A Pythagorean triple is an additive
relation among three vertex labels.  Neither the variables nor the forbidden
hyperedges translate, even after restricting vertices to rational or integer
squares.  This is therefore not a finite obstruction or coloring theorem for
the requested source.

## 2. Quadratic partition regularity: vertex colors and a different equation

**Ben Green and Sofia Lindqvist, [*Monochromatic Solutions to
\(x+y=z^2\)*](https://doi.org/10.4153/CJM-2017-036-1), Canadian Journal of
Mathematics 71 (2019), 579--605.**  Its stated theorem is that every
two-coloring of \(\mathbb N\) has infinitely many monochromatic **vertex**
solutions of \(x+y=z^2\); it also gives a three-coloring with only finitely
many such solutions.

**Mismatch.**  The variables \(x,y,z\) are individually colored integers,
and the relation is a sum equal to a square.  The target colors square-endpoint
edges and compares two differences of squares.  The theorem has no directed
orientation, no shared lower endpoint, and no conclusion about a two-color
edge coloring of a square-source graph.

## 2-adic lead

The rational/2-adic queries returned valuation colorings associated with
Monsky-style square dissections, which use three colors on **points of a
plane** to force a tricolored geometric triangle.  No primary theorem found
in the bounded search states a two-edge-color result for the above
equal-difference square corner.  Such valuation results therefore cannot be
imported without a new edge-color translation.

## Scoped outcome

Within the three query batches and two read primary sources, there is no
usable published theorem or obstruction for the requested ordered square-root
edge configuration.  The closest literature is vertex-color arithmetic
Ramsey theory, with an explicit object-level mismatch.  This is a bounded
search gap, not a novelty claim.
