# Sidon-overlap families: bounded quantitative source check

For a finite integer source, write \(F_d=A\cap(A-d)\).  The proper-source
diagonal lemma says each nonempty \(F_d\) is a union of at most two Sidon
sets.  The desired input would control the whole family, and thus \(E(A)\),
despite the two Sidon parts being allowed to depend on \(d\).

## 1. Sidon sets and a C4-free bipartite graph: one set only

[This EJC source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p26/pdf/)
records the standard equivalence: a set \(S\) is Sidon exactly when the
bipartite graph with edge \((x,y)\) whenever \(x+y\in S\) has no \(C_4\).
For a torsion-free Sidon set of size \(s\), unique nonzero differences give
the exact ordered-energy scale \(E(S)=2s^2-s\).

**Mismatch.** This is a single-set statement.  It does not bound summed
energies or cross-correlations for \(\{F_d\}\) when their two Sidon pieces
change with \(d\).  Applying it fiberwise gives only the known local bound.

## 2. Higher-energy structure: a global hypothesis in the opposite direction

**I. D. Shkredov, [*Energies and structure of additive sets*](https://arxiv.org/abs/1405.3132).**
The paper derives decompositions into small-doubling pieces and related
structure from global higher-energy or sumset/difference-set hypotheses for a
single set.  Its input is quantitative control of a global energy, including
the higher energy \(\mathsf E_3\).

**Mismatch.** Local two-Sidon decompositions of every \(F_d\) do not supply
the paper's global higher-energy assumption, nor a common decomposition across
translations.  Thus it gives no numerical conclusion such as
\(E(A)\le C|A|^2\) from the overlap hypothesis.

## 3. Dense Sidon packing: a common ambient group is essential

[The dense-Sidon source](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p33/pdf/)
records the ambient-group packing inequality
\(|S|(|S|-1)\le |G|-1\) for a Sidon set \(S\subset G\), and studies
near-extremal constructions.  This is quantitative information for one Sidon
set in one finite group.

**Mismatch.** The translate fibers live in varying intersections and have no
fixed common Sidon class.  Summing the individual packing inequalities does
not control repeated participation of a pair across fibers, so it gives no
structured-versus-irregular dichotomy for the family.

## Bounded conclusion

The three leads control a single Sidon set or derive structure from a global
energy premise.  None gives an energy theorem for a family of translate
intersections each decomposable into two independently chosen Sidon sets. The
missing ingredient is compatibility between the fiber partitions. This is a
scoped mismatch, not a novelty assertion.
