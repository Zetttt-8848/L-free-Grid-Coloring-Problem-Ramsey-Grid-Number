# What is new in this counting argument

Research date: 2026-11-08. This comparison scopes the contribution; it is
not a proof of worldwide priority.

The old numerical count bounded each difference fiber of one main-diagonal
color by two Golomb cardinalities and then added over three colors. This
forgets that the six classes have **different actual positions**. The new
count indexes each class by `(original diagonal color, completion color)`.
A class of24 marks needs its minimum in a short prefix. Those minima are
distinct, so six independently maximal classes cannot always coexist.
The exact new geometric inequality is

`R_d <= sum_(j=0)^5 g(n-d-j)`,

where g(p) is maximum Golomb cardinality in p positions. It is a shared
position count, not a new name for optimizing the old weight sequence.
At n464, the same polynomial weight gives old margin -2799639872 and
new margin477965143. The exact gain3277605015 comes from the joint count.

## Sources and scope actually checked

1. Mammel, Smith, Yerger, *Ramsey Theory on the Integer Grid: The “L”
   Problem*, [arXiv:2502.05162v1](https://arxiv.org/html/2502.05162v1),
   with the published [Integers 25 A21 version](https://math.colgate.edu/~integers/z21/z21.pdf)
   already checked in the preceding package. Theorem6/Algorithm3 are the
  493 comparison baseline. The interval and Golomb mechanism is an
   antecedent, not a contribution of this round. The HTML was also searched
   for disjointness; absence of that word alone would not prove novelty.

2. Xu, Xiu, Fan, Liang, *Some constructive results on Disjoint Golomb Rulers*,
   [arXiv:2409.14409v1](https://arxiv.org/html/2409.14409v1), 2024-09-22.
   Definition, introduction, conjecture distinctions, and Section3
   construction inequalities were read. Disjoint Golomb rulers are an
   established subject; equal-size families are described by H(I,J).
   The paper develops constructions and conjectures. Neither its
   conjectures nor construction upper bounds are used as impossibility
   inputs here. The elementary distinct-minimum inequality and the concept
   of disjoint rulers are not claimed to be new mathematical subjects.

3. Xiu, Fan, Liang, [*On Disjoint Golomb Rulers*, arXiv:1405.4535](https://arxiv.org/abs/1405.4535),
   2014-05-18, and Shearer, [*Some new disjoint Golomb rulers*, IEEE TIT (1998)](https://research.ibm.com/publications/some-new-disjoint-golomb-rulers).
   Abstracts and metadata were used for historical attribution; a full
   proof audit of these works was not performed. The old arXiv HTML route
   was unavailable. No numerical theorem from either is imported.

4. Ma, Yi, *An Almost-Covering Threshold for Golomb-Ruler Difference
   Packings*, [arXiv:2608.13739v1](https://arxiv.org/html/2608.13739v1),
   2026-08-13. Definitions and Sections3–5 were read, including the
   Fourier and small-difference proof arguments. Its rulers have disjoint
   **positive difference sets**. Our six classes have disjoint **marks**,
   which does not imply that hypothesis. For example, {0,1,3} and {4,5,7}
   have disjoint marks and identical positive difference sets {1,2,3}.
   Its packing deficit cannot be imported directly. No claim of auditing
   its constructive Section2 or the whole manuscript is made.

The 2026 source illustrates a different way of counting selected
differences. It also explains why discarding the labels on our six
classes would create a false multiplicity-one claim. Our shared-minimum
count keeps those labels and controls occupied positions instead.

## Second mechanism opened here

Retain the original color of each early minimum. For n-d<=480, let
`k=max(0,n-d-425)` and
`m_c(d)=#{u<k: chi(u,u)=chi(u+d,u+d)=c}`.
There are at most two large completion classes for each c, so

`R_d <=138+sum_c min(2,m_c(d))`.

The values m_c(d) for different d arise from the same diagonal boundary
word. This changes the counting object again: instead of independently
maximizing a number for each d, one must count a jointly realizable
colored comparison pattern. The separate combinatorial package studies
that constraint. Its strongest universal proof, finite experiments, and
any still-missing numerical implication must be reported separately.

The contribution established here is the six-completion-class reduction,
the loss caused by their shared positions, and its explicit improvement
to464 in the project. No search result is used to claim the first such
idea or best known bound in the entire literature.
