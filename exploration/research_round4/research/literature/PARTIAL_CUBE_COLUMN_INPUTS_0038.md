# Seven-point partial-cube / column input (0038)

## Exact pattern

The forbidden configuration is
\[
 a+\{0,x,r,s,x+r,r+s,x+r+s\},\qquad x,r,s>0,
\]
with legal coincidences retained.  It is the three-dimensional Hilbert cube with the \(x+s\) vertex omitted.  As specified in the request, this is equivalent to forbidding the corresponding labelled triangle in every anchored addition/column graph; it is not the ordinary full-cube condition.

Two focused source-query batches were used.  The sole relevant primary read below concerns full sumsets and is recorded only for its exact one-way implication.

## Full Hilbert cubes: available, but quantitatively and structurally too weak

Javier Cilleruelo and Rafael Tesoro, [*On sets free of sumsets with summands of prescribed size*](https://www.researchgate.net/publication/274403361_On_Sets_Free_of_Sumsets_with_Summands_of_Prescribed_Size), define \(L^{(r)}_{2,\ldots,2}\)-free sets as sets avoiding a full \(r\)-dimensional Hilbert cube, namely a sumset of \(r\) two-point sets.  Their Theorem 1 states
\[
 F\bigl(N,L^{(r)}_{2,\ldots,2}\bigr)
 \le N^{1-1/2^{r-1}}+O\!\left(N^{3/4-1/2^{r-1}}\right).
\]
For \(r=3\), this is \(O(N^{3/4})\) for a full-three-cube-free subset of \([N]\).  The paper also attributes the same main exponent for this special case to earlier full-cube work of S\'andor.

Every full positive three-cube contains the displayed seven-point partial cube.  Therefore seven-point avoidance implies full-three-cube avoidance, and the quoted \(O(N^{3/4})\) estimate is a valid but weak inherited cardinality bound.  The implication is only in this direction: full-cube avoidance permits a set to contain the seven-point pattern with the omitted vertex absent, so it does not characterize column-triangle-free sets.

Nothing in the theorem tracks the omitted vertex, a fixed anchor \(a\), the labels \(r,s,r+s\), or the bipartiteness of all column graphs.  It gives no \(O(\sqrt N)\) conclusion, explicit square-root constant, or additive-energy bound \(T(A)=O(|A|^2)\).

## Scoped outcome

No primary extremal result for this exact seven-vertex \(Q_3\) minus one vertex configuration was located in the bounded search.  Standard "partial cube" terminology retrieved graph-isometric-subgraph work rather than additive integer-set avoidance, and ordinary \(B_2\)/Sidon results concern repeated pair sums rather than this three-generator seven-point support.  This is a bounded source mismatch, not an absence claim.
