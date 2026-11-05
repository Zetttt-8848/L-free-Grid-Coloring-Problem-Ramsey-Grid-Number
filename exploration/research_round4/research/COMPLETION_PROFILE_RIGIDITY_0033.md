# Rigidity of a completion profile

Root integration of `fibers/FIBER_COLOR_RIGIDITY_0033.md` and
`fibers/ORDERED_GROUP_HYPERGRAPH_0031.md`. These statements describe the
shared-color constraints of a source; they do not give a size bound.

Let A be a finite integer source of span L, and let r_d count its
positive-difference pairs. An offset-d input is a cell (u+d,u), with
u in F_d. For two starts u<v, the fixed pair output is the actual cell
(v+d,u), whose offset d+v-u is strictly greater than d.

## 1. Exact local reconstruction problem

Suppose the colors of all greater-offset cells have been fixed. On F_d
put an edge uv exactly when its pair output has color 1. The offset-d
input cells can be colored properly with these fixed outputs exactly
when this graph admits a partition

    F_d=K disjoint union I,

where K is a clique and I is independent. Assign input color 0 on K
and input color 1 on I. Pairs crossing the partition impose no further
restriction, and pairs within either part have the opposite output
color required for their completion corner.

The auxiliary rigidity lemma proves, by an elementary set-family
argument, that there are at most r_d+1 such partitions. Moreover any
two of them differ on at most one input of each old color. Thus fixing
the higher cells restricts an entire fiber much more sharply than
choosing arbitrary two-Golomb classes would suggest.

There are simple finite output obstructions. An induced four-vertex
output graph consisting of two disjoint edges has no such partition:
a clique of size two must be one edge, leaving the other edge in the
independent part; a smaller clique also leaves an edge there. Its
complement is likewise forbidden by exchanging the parts. An induced
five-cycle is forbidden because both its largest clique and its
largest independent set have size two. These give explicit restrictions
on six or ten shared completion colors even when F_d itself is Golomb
and its strict triangle contains no corners.

## 2. A complete counting corollary

Let N(A) be the number of proper two-colorings of V(A), and use
N(A)=1 for the empty cell set. Process offsets in decreasing order.
Once all offsets greater than d are colored, the preceding local
statement gives at most r_d+1 possible assignments to offset d that
satisfy every corner whose parallel endpoints have that offset.
Every corner has exactly one such endpoint offset. Consequently

    N(A)<=product_(d=1)^L (r_d+1).                     (1)

No extension is assumed to exist; a branch with zero local extensions
contributes zero. The product is an upper bound obtained from the
entire descending decision tree.

For L>0, sum r_d=M=binom(|A|,2), so the arithmetic-geometric mean
inequality further gives

    N(A)<=(1+M/L)^L.                                  (2)

For L=0 there are no cells, and the empty product in (1) is one.
Both (1) and (2) count assignments to actual source cells; they never
identify two cells merely because their numerical offsets agree.

## 3. Why the reconstruction bound does not give nonexistence

The product in (1) is not a lower bound on N(A). Even a very small
positive number of globally compatible colorings would be enough for
the source to exist. No lower bound large enough to contradict (1)
has been derived for the sources relevant to S21.

Also, choosing one local partition does not preserve arbitrary lower
constraints. The cells just colored are outputs for smaller offsets,
whose split-partition requirements are still to be imposed. The
three-layer abstract construction in
`fibers/ORDERED_GROUP_HYPERGRAPH_0031.md` shows that these future
requirements can be incompatible even when every lower pair outputs
to a different higher group. Thus neither a greedy extension nor a
difference-constant canonicalization follows from local rigidity.

The quantitative open question is how integer source geometry forces
an incompatible output pattern in one of these linked split problems
when M is large relative to L. The reflected-triple constraints in
`REFLECTION_COMPLETION_COMPATIBILITY_0033.md` provide additional
relations among exactly those output colors, but no uniform closure
has yet been proved.
