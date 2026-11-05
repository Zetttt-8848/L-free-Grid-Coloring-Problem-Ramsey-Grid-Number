# Direct-sum overlap mechanism: scoped literature comparison

The local theorem in `PROPER_DIRECT_SUM_ENERGY_0028.md` assumes a complete
no-carry sum \(A=B+QC\) and derives factor overlap caps from a two-Golomb
partition of each translated fiber.  This note distinguishes its elementary
rectangle ingredients from a source-color/product theorem.

## 1. Monochromatic rectangles are standard bipartite Ramsey objects

**William Gasarch, [*Rectangle Free Coloring of Grids*](https://www.cs.umd.edu/~gasarch/gridtalk.pdf), Theorem 9.4; see also the associated paper.**

The bipartite Ramsey number \(BR(2,2)=5\) says every red/blue coloring of
the edges of \(K_{5,5}\), equivalently every two-color \(5\)-by-\(5\) array,
contains a monochromatic two-by-two submatrix.  The source also records that
\(4\)-by-\(5\) arrays can avoid such a rectangle, so this is the sharp square
threshold.

The 7-by-3 fact used locally is an even smaller direct pigeonhole lemma: each
row chooses a same-color column pair, from only \(2\binom32=6\) labels, so
two of seven rows agree.  It is an asymmetric bipartite Ramsey consequence,
not a new additive statement.  Its transpose supplies the exchanged factor
bound.

## 2. Rectangle-free arrays have a developed general theory, but no extra source-color input

The same grid source formulates rectangle-free colorings as colorings of
complete bipartite graphs without monochromatic \(C_4\)'s and gives general
bipartite Ramsey bounds.  This literature controls which full arrays can
avoid monochromatic rectangles.

**Limit for the direct-sum mechanism.**  In the local argument, the relevant
array is not an arbitrary coloring: it comes from the two Golomb diagonal
classes of a concrete overlap fiber of a complete product.  The 7-by-3 and
5-by-5 consequences are sufficient because the complete product supplies
every cell.  Generic rectangle-free-array results do not prove that a partial
source support can be completed to such an array, nor do they yield the
factor energy product estimate.

## 3. Additive/edge-color encodings do not match the overlap theorem

**Keevash, Mubayi, Sudakov and Verstraëte, [*Rainbow Turán Problems*](https://homepages.math.uic.edu/~mubayi/papers/rainbow-turan-final.pdf).**

Their additive construction takes two copies of an abelian group, joins
\(x\) to \(y\) when \(x-y\) lies in a set, and colors that edge by the
difference.  It is a properly edge-colored graph; \(B_k^*\) hypotheses give
rainbow-cycle exclusions.  This is a genuine additive/edge-colored product
method, but colors are difference labels and the result concerns rainbow
cycles.

**Mismatch.**  The direct-sum overlap theorem has two source colors, its
arrays come from partitions into Golomb classes, and its conclusion is an
energy bound using the exact no-carry factorization \(E(B+QC)=E(B)E(C)\).
The Rainbow Turán framework supplies none of the two-Golomb overlap
partitions, the 7-by-3/5-by-5 caps, or this energy conclusion.

## Bounded conclusion

The rectangle steps are standard, sharp bipartite-Ramsey ingredients: the
5-by-5 threshold is \(BR(2,2)=5\), while the 7-by-3 assertion is a direct
six-label pigeonhole argument.  Within the three focused leads, no published
theorem was located that packages a complete no-carry direct sum, proper
strict-source coloring, two-Golomb overlap fibers, and the stated energy
bound.  This is a scoped comparison, not a novelty claim.
