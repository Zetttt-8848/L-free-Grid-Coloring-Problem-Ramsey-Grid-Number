# Unique-outer differences: bounded additive-structure input

## Target property

For a finite integer set \(A\), property \(P\) says that whenever

\[
x,\ x+d,\ x+h,\ x+d+h\in A\qquad(d,h>0),
\]

the outer difference \(d+h\) has exactly one positive representation in
\(A\).  Equivalently, every nontrivial additive parallelogram carries a
unique long diagonal.  The desired external input would represent such an
\(A\), up to Freiman-2 equivalence, by two-atom sums or a relation graph, or
would directly bound its additive energy.

The four focused queries produced the following neighboring results.  They do
not supply that representation or an energy theorem for \(P\).

## 1. Freiman dimension preserves all order-two relations, but does not classify \(P\)

The standard Freiman-dimension definition is recorded explicitly in
[this primary-source discussion](https://ems.press/content/serial-article-files/29829?nt=1),
Section 2: a bijection \(F:S\to A\subset\mathbb Z^r\) is a Freiman
2-isomorphism when, for **all** \(g_1,g_2,g_3,g_4\in S\),

\[
g_1+g_2=g_3+g_4
\quad\Longleftrightarrow\quad
F(g_1)+F(g_2)=F(g_3)+F(g_4).
\]

Thus \(P\), being a condition on selected nontrivial four-term additive
relations plus the representation count of their outer differences, is
invariant under a suitable Freiman-2 isomorphism when the uniqueness count is
included in the relation data.

**Limit.**  Freiman dimension measures the largest affine rank of such a
model; it does not say that a set with \(P\) has dimension two, is a subset of
\(X+Y\) for independent atoms, or has a graph-edge presentation.  The usual
Freiman inverse theorems require small doubling, whereas \(P\) alone is not a
small-doubling hypothesis.  This supplies a language for an attempted model,
not the requested structure theorem.

## 2. Unique-difference theorems give one difference, not unique outer diagonals

**Tai Do Duc and Bernhard Schmidt, [*Unique Differences in Symmetric Subsets
of \(\mathbb F_p\)*](https://arxiv.org/abs/1902.05195), Theorem 1.2.**

For \(p\ge5\), the paper proves that a symmetric subset
\(A\subset\mathbb F_p\) with \(|A\setminus\{0\}|\le2\log_3p\) has *an*
element with a unique representation as a difference of two elements of
\(A\).  This is an existence statement for one difference, in a finite cyclic
group and under both a symmetry and a size hypothesis.

**Limit.**  Property \(P\) instead asks for a unique representation of the
specific sum \(d+h\) for every supported positive parallelogram.  It neither
assumes symmetry nor works modulo a prime.  One globally unique difference
cannot control all outer diagonals, so the theorem gives no energy bound or
two-sum representation for the source class.

## 3. Standard energy formalism records the right statistic but imposes no unique-outer theorem

The relation

\[
E(A)=\#\{(a,b,c,d)\in A^4:a+b=c+d\}
\]

and its connection with sum representations are summarized in the
[set-addition source](https://epublications.vu.lt/object/elaba%3A2056828/2056828.pdf):
energy counts collisions of pair sums, and small sumset forces large energy.
Freiman-type inverse theorems then begin from a small-doubling assumption.

**Limit.**  The source does not state a bound for sets in which only the
outer difference of every nontrivial parallelogram is uniquely represented.
That condition still permits repeated shorter differences and has a directed
order feature absent from ordinary energy.  Consequently generic energy or
small-doubling results cannot be imported as the proposed \(E(A)\le C|A|^2\)
statement.

## 4. Sidon/2-sum language is stricter than \(P\)

The standard additive Sidon condition makes every two-sum unique up to order.
The focused search found this terminology and Freiman-2 models, but no
primary theorem identifying \(P\)-sets with subfamilies of sums of two
independent atoms or with graph edge-label sets.  A Sidon conclusion would be
far stronger than \(P\): it forbids all nontrivial additive quadruples, while
\(P\) explicitly allows them so long as their outer diagonal is unique.

## Bounded conclusion

Freiman-2 equivalence is the correct relation-preserving framework, and
unique-difference results show that single-difference uniqueness has its own
literature.  Within this four-query search, neither produces a representation
theorem or a general additive-energy inequality for property \(P\).  This is a
bounded source finding only; it does not rule out a more specialized result.
