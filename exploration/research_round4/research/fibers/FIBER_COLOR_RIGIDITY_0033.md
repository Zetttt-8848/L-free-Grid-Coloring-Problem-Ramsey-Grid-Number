# Fiber color rigidity for fixed pair outputs

## 1. Fixed-output input problem

Let \(V\) be a set of \(r\) input vertices. For every unordered pair
\(uv\in\binom V2\), fix an output color
\[
\lambda(uv)\in\{0,1\}.
\]
An input assignment \(c:V\to\{0,1\}\) is **valid** when
\[
\operatorname{NAE}\bigl(c(u),c(v),\lambda(uv)\bigr)
\qquad\text{for every }uv\in\binom V2.
\tag{1}
\]

This is the local problem at one offset group after all of its pair-output
colors have been fixed.

## 2. Split-partition formulation

Let \(G\) be the graph on \(V\) whose edges are the pairs with output color
\(1\):
\[
uv\in E(G)\quad\Longleftrightarrow\quad\lambda(uv)=1.
\]
For an assignment \(c\), put
\[
K=c^{-1}(0),
\qquad
I=c^{-1}(1).
\]
If two vertices of \(K\) were joined by an output-\(0\) pair, the
corresponding triple would be monochromatic \(0\). Hence every pair inside
\(K\) is an edge of \(G\), so \(K\) is a clique. Similarly, every pair inside
\(I\) has output color \(0\), so \(I\) is an independent set of \(G\).
Conversely, those two properties make every triple in (1)
nonmonochromatic. Therefore
\[
\boxed{
c\text{ is valid}
\quad\Longleftrightarrow\quad
V=K\sqcup I, K\text{ a clique of }G, I\text{ independent in }G.
}
\tag{2}
\]

Thus valid assignments are exactly the ordered clique--independent-set
partitions of the fixed output graph. In particular, a valid assignment
exists exactly when \(G\) is a split graph.

## 3. Pairwise switch rigidity

Let \(c,c'\) be two valid assignments. There cannot be two vertices \(u,v\)
with
\[
c(u)=c(v)=0,
\qquad
c'(u)=c'(v)=1.
\]
Validity of \(c\) would require \(\lambda(uv)=1\), while validity of \(c'\)
would require \(\lambda(uv)=0\). Hence at most one vertex switches from
\(0\) to \(1\). Interchanging \(c,c'\) gives the same statement for switches
from \(1\) to \(0\).

In the set notation of (2), if \(K,K'\) are the zero-sets of two valid
assignments, then
\[
\boxed{|K\setminus K'|\le1,\qquad |K'\setminus K|\le1.}
\tag{3}
\]
In particular, two valid assignments have Hamming distance at most two, and
their numbers of zeroes differ by at most one.

## 4. Sharp counting bound

**Theorem.** For arbitrary fixed pair-output colors on \(r\) inputs, the
number of valid input assignments is at most
\[
\boxed{r+1.}
\tag{4}
\]

Let \(\mathcal K\) be the family of zero-sets of all valid assignments and
choose \(K_0\in\mathcal K\) of minimum size \(k\). By (3), every member of
\(\mathcal K\) has size \(k\) or \(k+1\).

Every \((k+1)\)-member must be
\[
K_0\cup\{a\},\qquad a\in V\setminus K_0,
\tag{5}
\]
and every other \(k\)-member must be a one-for-one exchange
\[
K_0-\{b\}+\{a\},
\qquad b\in K_0,\quad a\in V\setminus K_0.
\tag{6}

There are three cases.

1. If at least two distinct extensions \(K_0+a_1,K_0+a_2\) occur, no
   exchange (6) can occur: comparison with the extension whose added element
   differs from \(a\) would give two elements on one side of the set
   difference, contrary to (3). Hence
   \[
   |\mathcal K|\le1+(r-k)\le r+1.
   \]

2. If exactly one extension \(K_0+a_0\) occurs, every exchange must add that
   same \(a_0\), again by comparison with the extension and (3). There are at
   most \(k\) exchanges, so
   \[
   |\mathcal K|\le1+1+k=k+2\le r+1,
   \]
   because \(a_0\notin K_0\).

3. If no extension occurs, all members have size \(k\). Fix one exchange
   \(K_0-b_0+a_0\), if any. Comparison using (3) shows that every further
   exchange must either remove the same \(b_0\) or add the same \(a_0\).
   Moreover, exchanges of both kinds cannot coexist unless they are the fixed
   exchange itself: one with a new added element and one with a new removed
   element would differ in two elements in each direction. Thus all exchanges
   form one star, of size at most \(r-k\) or at most \(k\). Including \(K_0\),
   \[
   |\mathcal K|\le\max(r-k+1,k+1)\le r.
   \]
   The case with no exchange at all is smaller.

This proves (4).

The bound is sharp in two complementary ways. If every pair output has color
\(1\), then \(G=K_r\), and the valid zero-sets are
\[
V,\qquad V\setminus\{v\}\quad(v\in V),
\]
giving \(r+1\) assignments. If every pair output has color \(0\), then
\(G\) is empty, and the valid zero-sets are
\[
\varnothing,\qquad\{v\}\quad(v\in V),
\]
again giving \(r+1\).

## 5. Small groups and scope

For \(r=0\), there is one empty assignment, equal to \(r+1\). For \(r=1\),
both colors are valid, again giving \(r+1=2\). For \(r=2\), the one fixed
output color forbids exactly the monochromatic input pair of that color, so
three assignments remain; this is \(r+1\).

The lemma is entirely local. Replacing one valid assignment by another can
change the colors of vertices that serve as outputs for lower groups. Thus
the \(r+1\) bound does not justify independently canonicalizing or recoloring
groups inside an ordered-group hypergraph, and it supplies no global source
coloring theorem by itself.

