# Ordered matching-cover inputs (0038)

## Target and ordinary inducedness

Let a same-colored numerical-difference fiber contain \((a,b)\) and \((c,d)\), with \(a<c\), \(b<d\), and \(b-a=d-c\).  Strict-source properness forces only the outer edge \((a,d)\) to have the opposite color.  It leaves the other cross edge \((c,b)\), when it is an admissible ordered cell, without the corresponding forced conclusion.  Thus these fiber edges are not thereby an ordinary induced matching: the latter requires both endpoint-disjointness and absence of every other graph edge among the endpoints.

This note records two focused query batches and two source reads.  It does not identify the one-sided ordered rule with an induced-matching cover.

## Matching covers and Ruzsa--Szemerédi graphs: exact inducedness, wrong forcing pattern

Ashish Goel, Michael Kapralov, and Sanjeev Khanna, [*On the communication and streaming complexity of maximum bipartite matching*](https://web.stanford.edu/~ashishg/papers/matching-covers.pdf), Definition 2.3, define an induced matching \(F\) in a bipartite graph by requiring that the full edge set induced on its incident left and right vertices equals \(F\).  Their Definition 2.4 calls a graph an \(\epsilon\)-Ruzsa--Szemerédi graph when its edges are partitioned into induced matchings of size at least \(\epsilon n\).  Section 9 relates the extremal edge count of such graphs to the size of approximate matching covers; in particular their Theorems 9.1--9.3 compare the two parameters.

This is relevant background for the proposed relaxation: it is a primary source for a global theory in which many edge classes are genuine induced matchings.  It does not give the requested Nordhaus--Gaddum statement for a graph and its complement, nor an ordered one-sided substitute.  More decisively, the theorem's hypothesis needs the two cross nonedges for each pair of matching edges.  The strict-source rule only controls one outer cross edge and controls its *color* rather than deleting it.  No conversion of the numerical difference fibers into the source's induced-matchings was supplied by this source.

The same paper explicitly describes the extremal density of constant-size induced-matching partitions as a difficult problem, so its matching-cover correspondence alone does not yield an \(\Omega(m^2)\) lower bound on the number of difference labels in the present setting.

## Scoped Nordhaus--Gaddum outcome

Within the two focused searches, no primary theorem was located giving a Nordhaus--Gaddum lower bound for the sum of strong chromatic indices (edge induced-matching cover numbers) of \(G\) and \(\overline G\), nor one for the stated ordered one-sided relation.  The search did locate Nordhaus--Gaddum results for ordinary matching numbers, but those concern endpoint-disjointness only and are not an induced-matching-cover input.  This is a bounded retrieval gap, not a claim that no such theorem exists.

Accordingly, an application would require a new ordered parameter retaining exactly the forced outer cross edge, plus an independent theorem comparing its two color classes.  Ordinary strong chromatic-index or Ruzsa--Szemerédi bounds cannot be invoked from the stated source implication alone.
