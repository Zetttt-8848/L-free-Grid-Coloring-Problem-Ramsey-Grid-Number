# Binary lifts of complete weight-two layers

## Statement

Let \(r\ge6\), let \(w_1,\ldots,w_r\) satisfy coordinatewise dissociation for
relations among sums of two atoms, and put
\[
B=\{w_i+w_j:1\le i<j\le r\}.
\]
Choose \(Q>2\operatorname{span}(B)\) and form the binary no-carry lift
\[
A=B+Q\{0,1\}.
\]

**Theorem.** The strict source triangle \(V(A)\) has no proper two-coloring.

The obstruction uses only the vertical difference fiber of step \(Q\). It
does not depend on a proposed product-coloring formula.

## 1. The vertical colors split \(B\) into two Golomb sets

For each \(b\in B\), let
\[
p(b)=z(b+Q,b)
\]
be the vertical cell over \(b\). We first prove that, in any proper coloring,
the set of \(b\)'s receiving either fixed color under \(p\) is Golomb.

Suppose instead that one color \(c\) contains two distinct equal-gap pairs
\[
x,x+d,qquad y,y+d,qquad d>0.
\]
Interchange the pairs if necessary so that \(x<y\). The two vertical cells at
\(x,x+d\) force
\[
z(x+d+Q,x)=-c,
\]
and those at \(y,y+d\) force
\[
z(y+d+Q,y)=-c.
\]
These last two cells have the same difference \(Q+d\), so their corner forces
\[
z(y+d+Q,x)=c.
\]
On the other hand, the original vertical cells at \(x\) and \(y+d\) both have
color \(c\); their completion is the same cell \(z(y+d+Q,x)\), which they
force to have color \(-c\). This contradiction proves the claim.

Thus the vertical colors give a partition
\[
B=B_0\sqcup B_1
\tag{1}
\]
in which both \(B_0\) and \(B_1\) are Golomb sets.

## 2. Golomb subsets are exactly \(C_4\)-free edge subsets

Identify the mark \(w_i+w_j\) with the edge \(ij\) of \(K_r\). For a subset
\(S\subseteq B\), let \(E(S)\) be the corresponding edge set.

If \(E(S)\) contains a four-cycle on distinct vertices \(i,j,k,l\), with
cycle edges
\[
ik, jk, jl, il,
\]
then
\[
(w_j+w_k)-(w_i+w_k)
=(w_j+w_l)-(w_i+w_l)=w_j-w_i.
\]
Hence \(S\) is not Golomb.

Conversely, suppose \(S\) has two distinct representations of one positive
difference. After moving the negative terms to the other side, dissociation
gives an equality of incidence vectors
\[
\mathbf 1_{e_1}+\mathbf 1_{e_2}
=\mathbf 1_{e_3}+\mathbf 1_{e_4},
\tag{2}
\]
where all \(e_i\) are edges of \(E(S)\), and the two unordered pairs of edges
in (2) differ. In the two-edge multigraph on either side, every vertex has the
same degree. Therefore the symmetric difference of the two sides is a
nonempty alternating even cycle. It uses at most four edges, and it cannot be
a doubled single edge because the representations were distinct. It is
therefore a four-cycle in \(E(S)\).

We have proved the exact equivalence
\[
S\text{ is Golomb}
\quad\Longleftrightarrow\quad
E(S)\text{ is }C_4\text{-free}.
\tag{3}
\]

Under the partition (1), coloring edge \(ij\) by the color of
\(p(w_i+w_j)\) would consequently give a red-blue coloring of \(K_r\) with no
monochromatic four-cycle.

## 3. Direct two-color \(K_6\) lemma

**Lemma.** Every red-blue coloring of the edges of \(K_6\) contains a
monochromatic \(C_4\).

Choose a vertex \(v\). At least three of its five incident edges have one
color; call that color red and let \(R\) be a set of red neighbors.

If \(|R|\ge4\), consider the red graph induced by four vertices of \(R\). To
avoid a red four-cycle through \(v\), no one of these four vertices can have
two red neighbors among the other three: such a red path of length two,
together with \(v\), would close a red \(C_4\). Thus the red edges on these
four vertices form a matching. Their blue complement is \(K_4\) with at most
a matching removed, and it contains a blue \(C_4\).

It remains that \(v\) has exactly three red neighbors \(a,b,c\) and two blue
neighbors \(d,e\). If \(d\) had red edges to two of \(a,b,c\), those two
edges together with the corresponding red edges from \(v\) would form a red
\(C_4\). Hence \(d\) has at most one red edge into \(\{a,b,c\}\), and the
same is true of \(e\). There are therefore at most two red edges from
\(\{d,e\}\) to \(\{a,b,c\}\).

But avoiding a blue four-cycle through \(v,d,e\) requires, for each
\(x\in\{a,b,c\}\), at least one of \(dx,ex\) to be red; otherwise
\[
v-d-x-e-v
\]
is a blue \(C_4\). This requires at least three red cross edges, contradicting
the preceding upper bound of two. The lemma follows.

## 4. Deduction for the binary lift

Assume that \(V(A)\) had a proper two-coloring. By Section 1, its vertical
cells would partition \(B\) into two Golomb sets. By (3), these colors would
partition the edges of \(K_r\) into two \(C_4\)-free graphs. Restricting to
any six coordinate vertices contradicts the lemma in Section 3. Therefore
\(V(A)\) is not properly two-colorable for every \(r\ge6\).

The base weight-two layer itself admits the usual proper strict-source
coloring by whether its two edge labels intersect. The theorem shows that
adjoining one binary no-carry factor destroys proper two-colorability once
the complete coordinate graph contains \(K_6\). It is a structural product
obstruction, independent of any global source-energy estimate.

