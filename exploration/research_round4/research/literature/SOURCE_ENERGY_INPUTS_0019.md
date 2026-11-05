# Source-energy input: focused edge/additive literature check

## Target

Let a two-coloring assign a color to every ordered cell `(v,u)` with
`u<v` in a finite integer source `A`.  For

\[
u<b\le c<v,\qquad b-u=v-c>0,
\]

both equal-gap source triples

\[
\{(b,u),(v,c),(v,u)\},\qquad
\{(c,u),(v,b),(v,u)\}
\]

are required to be non-monochromatic (with the stated collapse when
`b=c`).  The desired input would turn this **two-edge-color** condition into
\(\binom{|A|}{2}\le21\operatorname{span}(A)\), or a stronger square-root
source-size bound.  This note follows the earlier near-miss list in
`EDGE_COLORED_SOURCE_INPUTS_0016.md` and does not repeat its locally additive,
grid-rectangle, or vertex-Sidon-Ramsey entries.

## 1. Anti-Ramsey Sidon equation: the equation is right, but the colors are on integers

**Vladislav Taranchuk and Craig Timmons, [*The Anti-Ramsey Problem for the
Sidon equation*](https://arxiv.org/abs/1808.09846), Theorem 1.1 (2018;
Discrete Mathematics 342 (2019), 2856--2866).**

For a vertex coloring \(c:[n]\to[k]\), let
\(AR_{X+Y=Z+T}^{k}(n)\) be the maximum number of *rainbow* solutions of
\(X+Y=Z+T\).  For \(n\ge k\ge4\), Theorem 1.1 gives

\[
AR_{X+Y=Z+T}^{k}(n)
 \le\left(\frac1{12}-\frac1{24k}\right)n^3+O_k(n^2),
\]

and constructs colorings with at least

\[
\left(\frac1{12}-\frac1{3k}\right)n^3-O_k(n^2)
\]

rainbow Sidon solutions.  Its four variables satisfy the same additive
identity \(u+v=b+c\) as an equal-gap quadruple.

**Mismatch.**  The theorem colors the four *integer vertices*, seeks four
distinct colors, and begins at four colors.  The source condition colors the
three **edges/cells** selected from a quadruple, uses two colors, and forbids
one monochromatic three-edge pattern.  Neither its upper bound nor its
additive-energy argument controls that edge pattern or provides a span bound.

## 2. Completely balanced edge colorings: genuinely edge-colored, but rainbow and many-colored

**Maria Axenovich and Felix C. Clemen, [*Rainbow subgraphs in edge-colored
complete graphs: Answering two questions by Erdős and Tuza*](https://doi.org/10.1002/jgt.23063),
Theorem 1.4 (Journal of Graph Theory 106 (2024), 57--66).**

For an integer \(q\ge8\) with \(q\equiv2\) or \(3\pmod4\), put
\(\ell=\binom q2\).  For every \(k\ge1\) and
\(n=(\ell+1)^k\), their theorem constructs a completely balanced
\(\ell\)-edge-coloring of \(K_n\) with no rainbow \(K_q\).  “Completely
balanced” means that every vertex is incident to the same number of edges of
each of the \(\ell\) colors.

**Mismatch.**  This is an exact complete-graph edge-coloring theorem, but its
configuration is a rainbow clique and its construction uses
\(\ell=\binom q2\) colors, rather than a two-color prohibition of a selected
monochromatic equal-gap triple.  It assumes no integer order or equation
\(u+v=b+c\).  Complete balance does not follow from the source hypothesis,
and the theorem is a construction showing that a rainbow conclusion can fail,
not a source-size forcing theorem.

## 3. Common additive configurations: two colors, but on a group’s vertices and only density-level forcing

**Leo Versteegen, [*Linear configurations containing 4-term arithmetic
progressions are uncommon*](https://arxiv.org/abs/2106.06846), Theorem 1.6
(JCTA 200 (2023), 105792).**

A linear configuration \(\Phi\) in an Abelian group \(G\) is *common* when
every two-coloring of the **elements of \(G\)** has at least the random-coloring
number of monochromatic instances of \(\Phi\).  Theorem 1.6 states that, for
all sufficiently large primes \(p\), every injective distinct-forms
configuration over \(\mathbb Z_p\) which contains a 4-term arithmetic
progression is uncommon; equivalently there is a two-coloring with strictly
fewer monochromatic instances than the random benchmark by a positive
constant density.

**Mismatch.**  Although the additive quadruple is central to this framework,
the colors remain on group elements, while the source colors ordered pairs.
“Uncommon” permits many monochromatic copies and concerns asymptotic density
in \(\mathbb Z_p\), not zero occurrences of the directed three-cell pattern
inside an arbitrary \(A\subset\mathbb Z\).  It yields neither a reduction to
the source condition nor an explicit coefficient at most 21.

## Bounded result

The focused search located one Sidon-equation anti-Ramsey theorem, one
edge-colored complete-graph theorem, and one two-color additive-density
theorem.  Each misses a different essential feature: respectively edge versus
vertex colors, two colors plus same-step orientation, and zero-forcing on an
arbitrary integer source.  No primary statement located here implies the
requested \(\binom{|A|}{2}\le21\operatorname{span}(A)\) bound.  This bounded
result does not establish novelty or rule out a theorem outside the search.
