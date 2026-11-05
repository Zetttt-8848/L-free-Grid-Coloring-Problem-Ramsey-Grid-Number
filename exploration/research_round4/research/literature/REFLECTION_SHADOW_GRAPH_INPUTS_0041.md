# Reflection-shadow graph inputs (0041)

## Exact graph being compared

For a finite integer Golomb set \(B\), the local construction in `NESTED_REFLECTION_HOLE_BUDGET_0041.md`, Section 6, has vertices \(Z_B\) consisting of internal reflection outputs \(r=a+q-p\) from \(a<p<q\) in \(B\).  Its directed neighbors are the lower and upper reflection shadows from pairs of anchors in \(A_B(r)\) and \(Q_B(r)\).  They remain in \(Z_B\), and the recorded outdegree is exactly
\[
2{\mu_B(r)\choose2}.
\]
In a proper weak source with opposite diagonal class \(C\), every out-neighbor of a selected \(r\in C\cap Z_B\) is absent from the full source.  The desired theorem would therefore need an independent-set or expansion statement for this particular ordered reflection graph, coupled to a second Golomb set \(C\).

## Closest primary incidence correspondence: not the same graph

Sean Eberhard and Freddie Manners, [*The apparent structure of dense Sidon sets*](https://escholarship.org/content/qt15b1v90m/qt15b1v90m_noSplash_e7126ab19c35d9d31b0717d3bc080da2.pdf), Proposition 2.1, gives an exact standard incidence equivalence.  For an abelian group \(G\) and a Sidon set \(S\subseteq G\), its development has points and lines both equal to \(G\), with incidence \(p-\ell\in S\); it is a partial linear space exactly when \(S\) is Sidon.  Conversely, a partial linear space with a regular abelian action produces a Sidon set.

This identifies the standard difference-incidence object attached to a Sidon set, but it does not identify \(Z_B\) with either its point set or line set.  In particular, the development has no order relation \(a<p<q\), no triple-reflection output map, no shadow edges, and no condition that a chosen vertex's out-neighborhood be avoided by a second Golomb class.  Its dense-set/projective-plane conclusions also assume a finite ambient group and near-square-root density, neither of which is a hypothesis on an arbitrary finite integer ruler in an interval.  It supplies terminology for a possible incidence reformulation, not the requested expansion theorem.

## Generic Sidon/Cayley graph result: explicit mismatch

[*Sidon Sets in Groups and Induced Subgraphs of Cayley Graphs*](https://doi.org/10.1016/S0195-6698(85)80001-9) proves that suitable Sidon subsets of groups can realize arbitrary finite graphs as induced subgraphs of Cayley graphs.  Its conclusion runs in the opposite direction from the needed rigidity: it uses a separately constructed ambient group/Cayley graph and says nothing about the reflection-shadow graph determined by one fixed integer Golomb ruler.  It cannot yield a universal independence or expansion bound for \(Z_B\).

## Bounded outcome

Two focused query batches and the two directly relevant primary reads located no theorem for the reflected triple-output graph, nor an exact equivalent incidence graph carrying its directed shadow rule.  Standard Sidon developments control repeated pair-difference incidences, while the new graph is built from ordered triples and their nested reflected holes.  This is a scoped mismatch, not an absence or novelty claim.
