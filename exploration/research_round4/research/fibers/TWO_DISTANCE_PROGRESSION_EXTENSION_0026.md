# A three-point progression over a two-distance base

## 1. Model and notation

Let \(X\) be a finite Euclidean set whose nonzero squared distances
belong to \(\{\tau,2\tau\}\).  Let \(e\) be a unit vector orthogonal to
the ambient space of \(X\), and fix \(h>0\).  Consider an arbitrary
subset

\[
 Y\subset X+\{0,h,2h\}e.
 \tag{1}
\]

Write its three layers as

\[
 Y_i=X_i+ihe,\qquad X_i\subset X,qquad n_i=|X_i|quad(0\le i\le2),
\]

and put

\[
 N=n_0+n_1+n_2,qquad M(Y)={N\choose2}.
\]

For any finite vector set \(S\), let

\[
 T(S)=\sum_d {r_S(d)\choose2},                         \tag{2}
\]

where one orientation is chosen from each pair \(\{d,-d\}\) of
nonzero vector differences, and \(r_S(d)\) is its number of ordered
representations.  This definition is independent of the choices of
orientation.

Every \(X_i\) remains a two-distance set.  The theorem in
`TWO_DISTANCE_SOURCE_ENERGY_0025.md` therefore gives

\[
 T(X_i)\le7M_i,
 \qquad M_i={n_i\choose2}.                              \tag{3}
\]

No coloring hypothesis is used below.

## 2. Two norm bounds for difference counts

For a finite set \(S\), define the ordered difference count

\[
 q_S(v)=|\{(x,y)\in S^2:y-x=v\}|
\]

and its ordered additive energy

\[
 \mathcal E(S)=\sum_v q_S(v)^2.
\]

If \(|S|=n\), then

\[
 \mathcal E(S)
 =n^2+2\sum_{d}r_S(d)^2
 =2n^2-n+4T(S).                                        \tag{4}
\]

Consequently (3) gives

\[
 \mathcal E(X_i)
 \le16n_i^2-15n_i
 \le16n_i^2.                                           \tag{5}
\]

For two sets \(S,R\), let

\[
 q_{S,R}(v)=|\{(x,y)\in S\times R:y-x=v\}|.
\]

Expanding an equality of two cross differences and then applying
Cauchy--Schwarz gives

\[
 \begin{aligned}
 \sum_vq_{S,R}(v)^2
 &=\sum_vq_S(v)q_R(v)\\
 &\le\sqrt{\mathcal E(S)\mathcal E(R)}.
 \end{aligned}                                         \tag{6}
\]

By (5), in this model

\[
 \|q_{X_i,X_j}\|_2\le4\sqrt{n_in_j}.                   \tag{7}
\]

For nonzero unoriented difference counts within one layer, (3) also
gives the sharper norm identity

\[
 \sum_d r_{X_i}(d)^2=M_i+2T(X_i)\le15M_i.              \tag{8}
\]

## 3. Exact separation by vertical difference

Orthogonality of \(e\) makes the vertical difference
\(j-i\in\{0,\pm1,\pm2\}\) visible in every vector difference.  Thus
collisions with different vertical differences never mix.  Write

\[
 T(Y)=T_0+T_1+T_2,                                     \tag{9}
\]

where the subscript is the absolute vertical layer gap.

Set

\[
 I=M_0+M_1+M_2,qquad
 A=n_0n_1+n_1n_2,qquad
 O=n_0n_2.                                             \tag{10}
\]

These are respectively the numbers of physical pairs within one
layer, across adjacent layers, and across the two outer layers, so

\[
 M(Y)=I+A+O.                                           \tag{11}
\]

For vertical gap zero, a base direction \(d\) has total multiplicity
\(r_{X_0}(d)+r_{X_1}(d)+r_{X_2}(d)\).  Equations (8), the triangle
inequality in \(\ell^2\), and \(\sqrt{M_i}\le n_i/\sqrt2\) give

\[
 \begin{aligned}
 T_0
 &\le\frac12\left[
 15\bigl(\sqrt{M_0}+\sqrt{M_1}+\sqrt{M_2}\bigr)^2-I
 \right]\\
 &\le\frac{15}{4}N^2-\frac12I.                         \tag{12}
\end{aligned}
\]

For vertical gap one, the multiplicity sequence is
\(q_{X_0,X_1}+q_{X_1,X_2}\).  Its total mass is \(A\).  Applying
(7) and the \(\ell^2\) triangle inequality yields

\[
 \begin{aligned}
 T_1
 &\le\frac12\left[
 16n_1(\sqrt{n_0}+\sqrt{n_2})^2-A
 \right]\\
 &=\frac{15}{2}A+16n_1\sqrt{n_0n_2}.                   \tag{13}
\end{aligned}
\]

For vertical gap two there is only the cross-difference sequence
\(q_{X_0,X_2}\).  Equations (6)-(7), after retaining its total mass
\(O\), give

\[
 T_2\le\frac12(16O-O)=\frac{15}{2}O.                   \tag{14}
\]

Equations (12)-(14) are valid even when the three base subsets overlap.
That overlap merely contributes to the zero base-vector entry of the
appropriate cross-difference sequence.

## 4. A uniform constant for every subset

Put

\[
 S_2=n_0^2+n_1^2+n_2^2.
\]

From (10),

\[
 I=\frac{S_2-N}{2},qquad A+O=\frac{N^2-S_2}{2}.
\]

Adding (12)-(14) therefore gives

\[
 T(Y)
 \le\frac{15}{2}N^2-4S_2+rac14N
       +16n_1\sqrt{n_0n_2}.                            \tag{15}
\]

The remaining quadratic expression has an exact maximum.  Let
\(p=n_0+n_2\) and \(q=\sqrt{n_0n_2}\le p/2\).  For fixed \(p,n_1\),
the expression

\[
 -4S_2+16n_1q
 =-4n_1^2-4p^2+8q^2+16n_1q
\]

is increasing in \(q\), so its maximum occurs at \(q=p/2\).  With
\(p=N-n_1\), the resulting quadratic is

\[
 -14n_1^2+12Nn_1-2N^2
 \le\frac47N^2,                                       \tag{16}
\]

with equality in the real relaxation at
\((n_0,n_1,n_2)=(2N/7,3N/7,2N/7)\).  Hence

\[
 T(Y)\le\frac{113}{14}N^2+\frac14N.                   \tag{17}
\]

For \(N\ge21\), the right side of (17) is at most
\(17{N\choose2}\), since the difference is

\[
 17{N\choose2}
 -\left(\frac{113}{14}N^2+\frac14N\right)
 =\frac{N(12N-245)}{28}\ge0.                           \tag{18}
\]

For \(N\le20\), the general bound \(r_d\le N-1\) gives

\[
 T(Y)=\sum_d{r_d\choose2}
 \le\frac{N-2}{2}\sum_dr_d
 =\frac{N-2}{2}M(Y)le9M(Y).                           \tag{19}
\]

We have proved the complete model theorem

\[
 \boxed{T(Y)\le17M(Y)}                                 \tag{20}
\]

for every subset (1).  In particular every single-band energy obeys
\(T_H(Y)\le17M(Y)\).

## 5. The full product has the better constant sixteen

There is an exact formula when all three layers equal the same
\(n\)-point base \(X\).  For a nonzero base direction of multiplicity
\(r\), the layer gaps \(0,1,2\) give multiplicities \(3r,2r,r\), with
both base orientations occurring at positive vertical gaps.  The zero
base vector contributes multiplicities \(2n,n\) at gaps one and two.
Summing the corresponding binomial coefficients gives

\[
 \boxed{
 T\bigl(X+\{0,h,2h\}e\bigr)
 =19T(X)+10M(X)+n.}                                    \tag{21}
\]

Using \(T(X)\le7M(X)\),

\[
 T\bigl(X+\{0,h,2h\}e\bigr)
 \le143{n\choose2}+n
 \le16{3n\choose2}.                                  \tag{22}
\]

Thus the complete product satisfies the stronger constant sixteen.

## 6. A lower obstruction from the weight-two base

The progression factor does not preserve a small total-energy
coefficient.  Take

\[
 X_r=\{e_i+e_j:1\le i<j\le r\}.
\]

Its squared distances are \(2\) and \(4\), and its repeated vector
directions are the coordinate exchanges.  With
\(n={r\choose2}\), one has

\[
 T(X_r)=n{r-2\choose2},
 \qquad
 \frac{T(X_r)}{M(X_r)}\longrightarrow2.                \tag{23}
\]

Applying the exact product formula (21) gives

\[
 \frac{T(X_r+\{0,h,2h\}e)}{{3n\choose2}}
 \longrightarrow\frac{19\cdot2+10}{9}
 =\frac{16}{3}.                                        \tag{24}
\]

Therefore no universal total-energy constant below \(16/3\) can hold
for this three-layer representation class.  This obstruction is purely
additive; no proper strict-source coloring of the full product is
asserted here.

## 7. Integer-source consequence and remaining implication

Suppose an integer source \(A\) admits an injective Freiman-2 map into
a subset \(Y\) of (1).  Every equal-difference collision of \(A\) maps
to an equal-vector collision of \(Y\), and injectivity keeps distinct
physical pairs distinct.  Since \(|A|=|Y|\), (20) gives

\[
 \boxed{T(A)\le17M(A),\qquad T_H(A)\le17M(A).}          \tag{25}
\]

This remains true if \(A\) also carries an inherited proper coloring;
the proof does not need to discard any color information.  The constant
seventeen is above the current total-energy target \(10\), and the
single-band consequence is above \(7/5\), so (25) does not by itself
close the source-size problem.

The precise missing general-source implication is an embedding or
decomposition theorem placing every relevant properly colored source
inside this three-layer model with enough additional compatibility to
improve (20).  Proper sources are not shown to have such a Freiman
representation, and the product itself is not shown to inherit a proper
strict-source coloring.  Neither assertion is assumed.
