# An abstract ordered-group counterexample

## 1. Ordered-group condition

Consider a finite set of vertices partitioned into linearly ordered groups
\[
G_1<G_2<\cdots<G_N.
\]
For every unordered pair \(\{x,y\}\subset G_i\), require exactly one
three-edge
\[
\{x,y,z_{xy}\},
\qquad z_{xy}\in G_j,\quad j>i.
\tag{1}
\]
For fixed ordered group indices \(i<j\), at most one pair in \(G_i\) may have
its output in \(G_j\). Outputs may be reused by pairs belonging to different
lower groups.

This is the abstract ordered-group property supplied by cube-free source
fibers. It does **not** imply two-colorability.

## 2. The local \(C_5\) obstruction

We first record the five-vertex gadget used at the bottom layer. Let
\(L=\{x_0,x_1,x_2,x_3,x_4\}\), with indices modulo five. Suppose the outputs
of the five cycle pairs
\[
\{x_j,x_{j+1}\}
\]
all have color \(c\), while the outputs of the five diagonal pairs
\[
\{x_j,x_{j+2}\}
\]
all have color \(1-c\).

In any proper coloring of the three-edges (1), the vertices of \(L\) colored
\(c\) must be an independent set in the cycle \(C_5\), so there are at most
two of them. The vertices colored \(1-c\) must be independent in the graph of
the five diagonals, which is another \(C_5\), so there are at most two of
those as well. This accounts for at most four vertices, contradicting
\(|L|=5\).

Equivalently, the output colors label the edges of \(K_5\) by a cycle and its
complement. A coloring of the five lower vertices would have to split one
label graph into a clique and an independent set, and \(C_5\) is not split.

## 3. Finite three-layer construction

Create nine top singleton groups
\[
T_i=\{t_i\},
\qquad 1\le i\le9.
\]

For every five-subset
\[
I=\{i_0,i_1,i_2,i_3,i_4\}\subset[9],
\]
create five intermediate groups
\[
M_{I,0},M_{I,1},M_{I,2},M_{I,3},M_{I,4},
\]
each containing three vertices. For each \(M_{I,j}\), biject its three
unordered pairs with the three distinct top groups
\[
T_{i_0},T_{i_1},T_{i_2},
\]
and use the corresponding vertices \(t_{i_0},t_{i_1},t_{i_2}\) as outputs.
Thus every pair in an intermediate group has exactly one output, and no two
pairs from that group output into the same higher group.

Next, for every transversal
\[
\mathbf v=(v_0,v_1,v_2,v_3,v_4),
\qquad v_j\in M_{I,j},
\]
create a bottom group
\[
L_{I,\mathbf v}=\{x_0,x_1,x_2,x_3,x_4\}.
\]
Assign its ten pair outputs as follows:

- biject the five cycle pairs \(\{x_j,x_{j+1}\}\) with the five top
  vertices \(t_{i_0},\ldots,t_{i_4}\);
- send the diagonal pair \(\{x_j,x_{j+2}\}\) to the chosen intermediate
  vertex \(v_j\in M_{I,j}\).

These ten outputs lie in ten distinct higher groups: five distinct top
singletons and five distinct intermediate groups. Hence the injectivity
condition holds for every bottom group.

Order all bottom groups first, all intermediate groups next, and the nine top
singletons last. The construction is finite. Explicitly, it has
\[
\binom95=126
\]
choices of \(I\), five intermediate triples for each \(I\), and
\(3^5=243\) bottom groups for each \(I\). The size is immaterial to the proof,
but these numbers make the construction completely specified.

Every pair inside every nonsingleton group has now received exactly one
higher output. Top groups have no internal pairs. For each ordered pair of
group indices there is at most one three-edge, while the same output vertex
may be reused by different lower groups as allowed.

## 4. Direct non-two-colorability proof

Assume that all vertices have been two-colored with no monochromatic
three-edge. Among the nine top vertices, some five have one common color
\(c\). Let their indices form \(I\).

In each intermediate triple \(M_{I,j}\), every pair has an output among
\(t_{i_0},t_{i_1},t_{i_2}\), all of color \(c\). Therefore
\(M_{I,j}\) can contain at most one vertex of color \(c\); two such vertices,
together with their output, would form a monochromatic edge. Consequently
each of the five groups \(M_{I,j}\) contains a vertex \(v_j\) of color
\(1-c\).

The construction contains the bottom group \(L_{I,\mathbf v}\) for this
particular transversal \(\mathbf v=(v_0,\ldots,v_4)\). Its cycle-pair outputs
are the five top vertices of color \(c\), while its diagonal-pair outputs are
the five selected intermediate vertices of color \(1-c\). Section 2 proves
that this bottom group cannot be colored without a monochromatic three-edge,
a contradiction.

Thus the ordered-group condition alone does not ensure property B. The
counterexample is purely abstract: no claim is made that its group labels,
output assignments, or extensive reuse of top vertices can be realized by
the numerical difference geometry of one integer source.

