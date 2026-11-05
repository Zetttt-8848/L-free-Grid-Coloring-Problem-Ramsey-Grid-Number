# Bi-hypergraph input for the T11 directed-corner system (0045)

## Exact encoding

Let \(V=T_{11}=\{(v,u):0\leq u<v\leq10\}\), so \(|V|=55\), and let
\(E\) consist of the actual directed equal-step corners

\[
 \{(x,y),(x+d,y),(x+d,y+d)\},\qquad d>0,
\]

whose three cells lie in \(V\).  There are

\[
 \sum_{d=1}^{9}\sum_{x=1}^{10-d}x
 =\sum_{k=1}^{9}\frac{k(k+1)}2=165
\]

such triples.  A three-coloring with neither a monochromatic nor a rainbow
corner is exactly a proper coloring of the 3-uniform bi-hypergraph
\(\mathcal H=(V,E)\): each member of \(E\) is simultaneously a C-edge and a
D-edge, hence has exactly two colors.

This particular bi-hypergraph is **linear**.  Indeed, two distinct cells in a
corner have displacement, up to reversal, of exactly one of
\((d,0),(0,d),(d,d)\).  In each of those three cases the third cell and \(d\)
are forced; all other displacements occur in no directed corner.  Thus two
distinct corners share at most one cell.

## One targeted primary-source pass

M. Zhang, F. Dong, and R. Zhang, [*On the colorability of
bi-hypergraphs*](https://arxiv.org/abs/2310.06464), arXiv:2310.06464 (submitted
10 October 2023), studies precisely the model in which a bi-edge must be
neither monochromatic nor polychromatic.

The paper's Theorem 1 says that an \(r\)-uniform bi-hypergraph is colorable if
either

1. it has fewer than \((r-1)^{r-1}\) edges; or
2. every edge is incident with fewer than
   \((r-1)^{r-1}e^{-1}-1\) other edges.

For \(r=3\), the first condition is fewer than four edges and the second
numerical bound is negative, so this theorem gives no 3-uniform input for the
165-edge corner system.  Their Theorem 2 proves that a minimal uncolorable
3-uniform bi-hypergraph has at least ten edges (and that ten is attained).
It also has the wrong direction here: a coloring with fewer than five rainbow
corners supplies a coloring of the surviving bi-edges; it does not create an
uncolorable subhypergraph.

Most decisively, the source ends by asking whether **every linear uniform
bi-hypergraph is colorable** (its Problem 3).  The T11 corner hypergraph above
already has that linearity property, and the desired assertion is stronger and
different: it seeks a lower bound of five on the number of edges which must
be rainbow in every proper three-coloring.  The source contains no theorem
about that defect count, about a prescribed linear incidence system, or about
three-colorings as opposed to unrestricted colorability.

## Bounded conclusion

This direct bi-hypergraph source verifies the exact vocabulary and exposes a
precise mismatch: its available 3-uniform results concern the existence of an
arbitrary proper coloring, whereas the target begins with a proper
three-coloring and asks for a quantitative failure of the bi-edge constraint.
Because even linear-uniform colorability is posed there as an open problem,
neither Theorem 1 nor Theorem 2 transfers to the T11 five-rainbow claim.
