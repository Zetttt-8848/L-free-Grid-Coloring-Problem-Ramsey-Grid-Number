# Label collisions in a partial separated forcing block

Fix a source column \(u\). Let
\[
I=\{a_1<\cdots<a_p\},\qquad
B=\{b_1<\cdots<b_q\},\qquad
\max I<\min B,
\]
where all input cells \((a_i,u)\) have one color and all output cells
\((b_j,u)\) have the opposite color. Let
\[
E\subseteq I\times B
\]
be the actual forcing incidences in this ordered block. Label an edge
\(e=(a,b)\) by the required source mark
\[
\lambda(e)=u+b-a\in A.                             \tag{1}
\]
Write \(\Lambda\) for the set of labels used by \(E\),
\(\ell=|\Lambda|\), and
\[
m_c=|\{e\in E:\lambda(e)=c\}|,\qquad
\ell_2=|\{c:m_c\geq2\}|.                           \tag{2}
\]

The same-label contradiction from
`ANCHORED_REFLECTED_PRODUCT_FORCING_0045.md` is used as
input: if \((a,b),(a',b')\in E\) have the same label and \(a<a'\), then
\(b<b'\) and the northeast cross edge \((a,b')\) is absent from \(E\).

## 1. The tagged collision injection

For a fixed label \(c\), list its edges in increasing order:
\[
(a_1^c,b_1^c),\ldots,(a_{m_c}^c,b_{m_c}^c).
\]
Equality of labels gives
\[
b_j^c-b_i^c=a_j^c-a_i^c,
\]
so both coordinates increase together. For \(i<j\), define
\[
\Phi(c,i,j)=(a_i^c,b_j^c).                         \tag{3}
\]
The image is a nonedge by the same-label contradiction.

For fixed \(c\), the map (3) is injective. More strongly, the tagged map
\[
(c,i,j)\longmapsto\bigl(c,\Phi(c,i,j)\bigr)         \tag{4}
\]
is injective over all labels. Indeed, from a target nonedge
\((a,b')\) and the label \(c\), the two original edges are uniquely
recovered as
\[
(a,c-u+a),\qquad (u+b'-c,b').                      \tag{5}
\]
Thus a label class of size \(m_c\) forces exactly
\(\binom{m_c}{2}\) distinct northeast nonedges, although different labels
may force the same nonedge.

## 2. Exact reuse ledger

For a missing edge \(f=(a,b')\in(I\times B)\setminus E\), let
\[
r_f=
|\{c\in\Lambda:\text{the two edges in (5) belong to }E
                 \text{ in increasing order}\}|.  \tag{6}
\]
Counting the tagged collisions first by labels and then by their untagged
images gives the exact identity
\[
\boxed{
\sum_{c\in\Lambda}\binom{m_c}{2}
=\sum_{f\in(I\times B)\setminus E}r_f.
}                                                   \tag{7}
\]

At most one collision of a fixed label can map to \(f\). Distinct labels
mapping to \(f=(a,b')\) use distinct first edges incident with row \(a\)
and distinct second edges incident with column \(b'\). Hence
\[
r_f\leq
\min\{\ell_2,\deg_E(a),\deg_E(b'),p-1,q-1\}.        \tag{8}
\]
Here \(\deg_E(a)\) is the degree of the input row and \(\deg_E(b')\) the
degree of the output column. The final two bounds use the strict
inequalities \(a<a'\) and \(b<b'\).

Combining (7)--(8) yields the finite partial-block inequality
\[
\boxed{
\sum_c\binom{m_c}{2}
\leq
\sum_{(a,b')\notin E}
\min\{\ell_2,\deg_E(a),\deg_E(b')\}
\leq R(pq-|E|),
}                                                   \tag{9}
\]
where
\[
R=\min\{\ell_2,p-1,q-1\}.                          \tag{10}
\]
It also gives the per-label lower bound
\[
pq-|E|\geq\max_c\binom{m_c}{2}.                    \tag{11}
\]

Since \(\sum_cm_c=|E|\), Cauchy--Schwarz gives
\[
\sum_c\binom{m_c}{2}
=\frac12\left(\sum_cm_c^2-|E|\right)
\geq\frac12\left(\frac{|E|^2}{\ell}-|E|\right).
                                                            \tag{12}
\]
Therefore (9) implies
\[
\boxed{
|E|^2+(2R-1)\ell|E|-2R\ell pq\leq0.
}                                                   \tag{13}
\]
Equations (7) and (9), rather than only (13), retain the useful degree and
label multiplicities.

## 3. The reuse factor is sharp

There is no label-free injection of collision pairs into missing northeast
edges. Fix \(k\geq1\), take
\[
u=0,\qquad
I=\{1,2,\ldots,k+1\},
\]
and, for any \(N>2k+1\), take
\[
B=\{N-k,N-k+1,\ldots,N\}.                          \tag{14}
\]
Let \(E\) consist of the \(2k\) edges
\[
(1,N-t),\qquad(1+t,N),
\qquad 1\leq t\leq k.                              \tag{15}
\]
For each \(t\), the two displayed edges have the common label
\[
c_t=N-t-1,
\]
and labels for different \(t\) are distinct. Thus there are \(k\) repeated
labels, each of multiplicity two, and no other label collision.

Every one of these \(k\) collision pairs maps under (3) to the same missing
edge
\[
f=(1,N).                                           \tag{16}
\]
Consequently
\[
r_f=k=\ell_2=p-1=q-1.                              \tag{17}
\]
This attains every universal factor in (10) simultaneously. The pattern
preserves the required southwest-to-northeast direction and all its labels
can be included as source marks. It is a partial-block configuration; no
claim is made that it is the complete forcing graph of a proper source.

## 4. Bounded conclusion

Same-label collision pairs do force missing northeast incidences
injectively within each label. Across labels, the optimal multiplicity at
one missing edge is unbounded and equals
\(\min\{\ell_2,p-1,q-1\}\) in the worst case. Thus the sharp reusable
resource is a label--nonedge pair, not a bare missing edge.

Any global application of (9) must either pay the factor \(R\), exploit
the degree-sensitive middle sum, or obtain an independent restriction on
how many repeated labels can converge at one absent incidence. Properness
of each individual same-label pair supplies no stronger untagged
multiplicity bound.
