# Two Golomb/Sidon class energy comparison (0040)

## Exact project-local object

The comparison target is the integer/additive-combinatorial statement in `TWO_GOLOMB_MIXED_ENERGY_0040.md`: for disjoint Golomb (distinct-positive-difference/Sidon) classes \(B,C\), \(n=|B|+|C|\), the direct derivation gives \(T(B\cup C)\le2{n\choose2}\) and \(E(B\cup C)\le6n^2-5n\).  The requested source would need the same finite-integer two-class hypotheses, or an equivalent exact mixed-pair collision count.

## Bounded primary-source search outcome

Two focused query batches were used: “union of two Sidon sets/additive energy” and “\(B_2[2]\)/union of two \(B_2\) sets/additive energy.” No primary source with the exact union-of-two-Golomb energy bound, its coefficient \(6\), or the stated corner/mixed-pair coefficient \(2\) was located.

The closest additive-energy paper retrieved was Norbert Hegyv\'ari, [*Some Remarks on the Distribution of Additive Energy*](https://link.springer.com/article/10.1007/s00025-023-02010-5) (2023). It defines ordinary additive energy and discusses energies of individual Sidon sets and general inverse/density questions. Its displayed Sidon discussion concerns a single Sidon set in a finite abelian group; it does not state a bound for a disjoint union of two integer Golomb classes, nor a same-class-versus-cross-class mixed-pair theorem. It therefore provides standard terminology only, not a transfer of the project-local bound.

The search also returned S. W. Drury’s classical “union of two Sidon sets is Sidon” result, but this is the harmonic-analysis notion of a Sidon set of characters (for example, the bibliographic statement is recorded in the [Encyclopedia of Mathematics entry](https://encyclopediaofmath.org/wiki/Harmonic_analysis,_abstract)). It is not the finite additive \(B_2\)/Golomb condition used here and cannot be used to bound integer additive energy of \(B\cup C\).

Results on \(B_2[g]\) sequences concern a *global* bounded representation function assumed for one set. The hypotheses “\(B\) and \(C\) separately Golomb” do not identify their union with such a class without a separate mixed-sum analysis, which is precisely the content of the root derivation.

## Attribution scope

The standard energy identity and single-Sidon facts are established background. Within this bounded search, the exact coefficient pair \((2,6)\) and the two-class mixed-pair route were not located in a primary source. This is a narrow retrieval outcome, not a novelty claim and not a review of the direct derivation.
