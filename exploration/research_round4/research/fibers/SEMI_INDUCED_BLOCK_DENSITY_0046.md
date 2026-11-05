# Dense abstract partial block under the one-sided matching rule (0046)

This construction concerns only the partial ordered-label block from the
current root mechanism. It is **not** a proper coloring of a whole strict
source triangle.

Fix \(d\ge1\), put \(N=3^d\), and let
\[
 I=\{1,\ldots,N\},\qquad B=\{3N+1,\ldots,4N\},\qquad
 A=\{0,\ldots,4N\},\qquad u=0.
\]
Let \(S\) be the \(2^d\) integers whose length-\(d\) base-three expansion
uses only digits \(0,1\). Thus \(S\subseteq[0,(N-1)/2]\). Select an edge
\((a,b)\in I\times B\) precisely when
\[
 a+b=4N+s\quad\hbox{for some }s\in S.
\tag{1}
\]
Its partial-block label is
\[
 c=u+b-a=b-a\in[2N+1,4N-1]\subseteq A.
\tag{2}
\]
Hence the number \(\ell\) of labels is at most \(|A|=m=4N+1\).

Each fixed label is automatically a matching. To check the retained
one-sided condition, take two distinct selected edges of a common label,
say \((a,b),(a',b')\), with \(a<a'\). Then \(b<b'\). Write their selected
sums as \(4N+s\) and \(4N+s'\). The forbidden outer cross edge \((a,b')\)
has sum
\[
 a+b'=\frac{(a+b)+(a'+b')}{2}=4N+\frac{s+s'}2.
\tag{3}
\]
If it were selected, its sum would be \(4N+r\) for \(r\in S\), so
\(s,r,s'\) would be a nonconstant three-term progression. This is
impossible: in base three, the digits of two elements of \(S\) are 0 or 1;
the coordinatewise average is an integer with digits 0 or 1 only when the
two endpoint digits agree in every coordinate. There are no carries, since
their digit sums are at most two. Thus \(s=s'\), contradicting distinct
common-label edges. The cross edge is absent, exactly as required.

For each \(s\in S\), the equation \(a+b=4N+s\) has at least
\((N-1)/2\) solutions with \(a\in I\), \(b\in B\): choose
\(a\in[\max\{1,s\},N]\), then \(b=4N+s-a\). Therefore the selected block
has at least
\[
 |S|\frac{N-1}{2}=2^{d-1}(N-1)
\tag{4}
\]
edges, while \(m=4N+1\). This is
\(\Omega(m^{1+\log_3 2})\) along \(N=3^d\).

The construction shows only that the matching labels, common-source output
labels, and one-sided outer-cross exclusion do not alone force a linear
edge bound. It does not assert the remaining corners, colors, or global
properness required of an actual source.
