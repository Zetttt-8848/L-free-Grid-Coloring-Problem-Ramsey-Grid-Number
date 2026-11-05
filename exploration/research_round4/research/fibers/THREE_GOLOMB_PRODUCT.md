# Three Golomb factors under no-carry encoding

**Status:** a proper symbolic coloring is proved when one factor is
arbitrary and the other two are binary.  Two direct extensions of that
rule are proved impossible once the alphabets grow.  A proper coloring
for three arbitrary Golomb alphabets is not established here.

## 1. No-carry rectangle structure

Let \(B_1,B_2,B_3\subset\mathbb Z\) be finite nonempty Golomb sets,
with spans \(S_1,S_2,S_3\).  Choose positive integers \(H,K\) such that

\[
H>2S_1,
\qquad
K>2(S_1+HS_2),
\tag{1}
\]

and encode

\[
E(x_1,x_2,x_3)=x_1+Hx_2+Kx_3,
\qquad
A=E(B_1\times B_2\times B_3).
\tag{2}
\]

Successive use of (1) shows that equality of two encoded differences
implies equality in each coordinate.  It also makes \(E\) injective, so

\[
|A|=|B_1||B_2||B_3|.
\tag{3}
\]

Consider two representations of one nonzero encoded difference:

\[
x\longmapsto x',
\qquad
y\longmapsto y',
\qquad
E(x')-E(x)=E(y')-E(y)>0.
\tag{4}
\]

Coordinatewise equality of the differences has a particularly rigid
form.  If \(x_i'-x_i\ne0\), Golomb uniqueness fixes both endpoints of
that signed difference, and hence

\[
x_i=y_i,\qquad x_i'=y_i'.
\tag{5}
\]

If \(x_i'-x_i=0\), then \(x_i'=x_i\) and \(y_i'=y_i\).
After ordering the representations so that \(E(x)<E(y)\), define

\[
S=\{i:x_i\ne x_i'\},
\qquad
T=\{i:x_i\ne y_i\}.
\tag{6}
\]

The step is nonzero and the representations are distinct, so \(S,T\)
are nonempty.  Equation (5) gives

\[
S\cap T=\varnothing.
\tag{7}
\]

The corner cells are

\[
(E(y),E(x)),\qquad
(E(y'),E(x)),\qquad
(E(y'),E(x')).
\tag{8}
\]

Their coordinate-change supports are \(T,S\cup T,T\), respectively.
Conversely, every axis-disjoint rectangle of this form gives such a
corner.  This is the only structural fact about the Golomb alphabets
used below.

## 2. A construction for one arbitrary and two binary factors

Assume \(B_1\) is an arbitrary finite Golomb set and

\[
B_2=\{b_2^0,b_2^1\},
\qquad
B_3=\{b_3^0,b_3^1\}.
\]

Label the two elements of each binary alphabet by \(0,1\).  For a
strict cell from \(x\) to \(y\), define

\[
\boxed{
\chi(E(y),E(x))
=
\mathbf 1_{\{x_1\ne y_1\}}
\mathbin{\oplus} y_2
\mathbin{\oplus} x_3.}
\tag{9}
\]

Here \(x_2,y_2,x_3,y_3\) denote the binary labels, and
\(\oplus\) is addition modulo two.

### Theorem

The coloring (9) is proper on \(T(A)\).

### Proof

Take the arbitrary corner (8), and let its three colors be
\(C_0,C_1,C_2\) in that order.  Put

\[
s_i=\mathbf 1_{\{i\in S\}}.
\]

Between the first and second cells only the upper endpoint changes,
from \(y\) to \(y'\), in the coordinates of \(S\).  In coordinate
one, the indicator in (9) changes exactly when \(1\in S\): it goes
from comparing the equal pair \(x_1=y_1\) to comparing the distinct
step endpoints \(x_1\ne y_1'\).  In binary coordinate two, a nonzero
step toggles the upper bit.  The lower coordinate-three bit is fixed.
Therefore

\[
C_0\mathbin{\oplus}C_1=s_1\mathbin{\oplus}s_2.
\tag{10}
\]

Between the second and third cells only the lower endpoint changes,
from \(x\) to \(x'\).  The coordinate-one indicator again toggles
exactly when \(1\in S\), the upper coordinate-two bit is fixed, and a
nonzero binary step toggles the lower coordinate-three bit.  Hence

\[
C_1\mathbin{\oplus}C_2=s_1\mathbin{\oplus}s_3.
\tag{11}
\]

If the corner were monochromatic, (10) and (11) would give

\[
s_1=s_2=s_3.
\]

The support \(S\) is nonempty, so this would force
\(S=\{1,2,3\}\).  That is impossible because the nonempty support
\(T\) is disjoint from \(S\) by (7).  Thus every corner is
nonmonochromatic.

When \(B_1\) is also binary, the indicator in (9) is
\(x_1\oplus y_1\), and (9) becomes exactly the affine Boolean-cube
rule

\[
x_1\oplus x_3\oplus y_1\oplus y_2.
\]

Permuting the coordinate roles gives the same conclusion whenever any
one factor is arbitrary and the other two have size two.

## 3. Exact size and corner ratio of the constructed family

For general factor sizes \(n_i=|B_i|\), a fixed nonempty change support
\(S\subseteq[3]\) supplies

\[
2^{|S|-1}\prod_{i\in S}\binom{n_i}{2}
\tag{12}
\]

positive coordinatewise differences.  Each such difference has

\[
\prod_{j\notin S}n_j
\]

representations.  Hence the exact number of corners in the no-carry
product source is

\[
T(A)
=
\sum_{\varnothing\ne S\subseteq[3]}
2^{|S|-1}
\left(\prod_{i\in S}\binom{n_i}{2}\right)
\binom{\prod_{j\notin S}n_j}{2}.
\tag{13}
\]

For the proved construction with

\[
(n_1,n_2,n_3)=(m,2,2),
\]

this becomes

\[
|A|=4m,
\qquad
T(A)=12\binom m2+2\binom{2m}{2}
=2m(5m-4).
\tag{14}
\]

Writing \(M(A)=\binom{|A|}{2}\), one obtains the actual ratio

\[
\frac{T(A)}{M(A)}
=
\frac{5m-4}{4m-1}
\longrightarrow\frac54.
\tag{15}
\]

Thus the construction supplies arbitrarily large source sets by taking
arbitrarily large Golomb \(B_1\), but its corner-to-cell ratio stays
bounded and tends to \(5/4\).  It gives no source-energy counterexample
and no conclusion about the shared-color span target.  Its encoded span
is exactly

\[
S_1+HS_2+KS_3,
\]

so the separation itself also supplies no density improvement.

## 4. Why support-only coloring cannot work

Assume here that every alphabet has at least two elements.  Suppose a
coloring depends only on the nonempty coordinate-change
support:

\[
\chi(E(y),E(x))=f(\{i:x_i\ne y_i\}).
\tag{16}
\]

For a rectangle with disjoint nonempty side supports \(S,T\), the two
outer cells in (8) both have color \(f(T)\), while the completion has
color \(f(S\cup T)\).  Properness would require

\[
f(T)\ne f(S\cup T)
\tag{17}
\]

for every disjoint nonempty \(S,T\).

Already inside a binary subcube, use successively

\[
(T,S)=(\{1\},\{2\}),\quad
(\{1\},\{2,3\}),\quad
(\{1,2\},\{3\}).
\]

The first two instances of (17) imply

\[
f(\{1,2\})=f(\{1,2,3\}),
\]

while the third requires these two colors to differ.  This is a
contradiction.  Thus even the Boolean case needs absolute endpoint
information; coloring only the support cannot extend the
two-factor rule.

## 5. Obstruction to every endpoint-separable bit formula

A broad direct generalization of the Boolean affine rule would have the
form

\[
\chi(E(y),E(x))
=
\phi_1(x_1,y_1)
\mathbin{\oplus}\phi_2(x_2,y_2)
\mathbin{\oplus}\phi_3(x_3,y_3),
\tag{18}
\]

where each \(\phi_i:B_i^2\to\{0,1\}\) is arbitrary.

For \(a<b\) in \(B_i\), set

\[
\begin{aligned}
L_i(a,b)&=\phi_i(a,a)\mathbin{\oplus}\phi_i(a,b),\\
R_i(a,b)&=\phi_i(a,b)\mathbin{\oplus}\phi_i(b,b),\\
v_i(a,b)&=(L_i(a,b),R_i(a,b)).
\end{aligned}
\tag{19}
\]

A corner whose step support is the singleton \(\{i\}\) has its two
adjacent color changes equal to the entries of \(v_i(a,b)\).
Properness therefore forces

\[
v_i(a,b)\ne(0,0).
\tag{20}
\]

A corner whose step support is \(\{i,j\}\), with both coordinate steps
oriented upward, has adjacent color-change vector

\[
v_i(a,b)\mathbin{\oplus}v_j(c,d).
\]

Taking the offset support to be the remaining coordinate is allowed by
(7).  Properness consequently requires

\[
v_i(a,b)\ne v_j(c,d)
\tag{21}
\]

for every positive pair in two different coordinates.

Now suppose \(|B_i|\ge3\).  Among three ordered marks, two have the
same diagonal bit \(\phi_i(a,a)\).  For their positive pair \(a<b\),
(19) gives

\[
L_i(a,b)\mathbin{\oplus}R_i(a,b)
=\phi_i(a,a)\mathbin{\oplus}\phi_i(b,b)=0.
\]

Together with (20), this forces

\[
v_i(a,b)=(1,1).
\tag{22}
\]

If all three alphabets have at least two marks and two different
alphabets both have at least three marks, (22)
produces the vector \((1,1)\) in both coordinates, contradicting
(21).  We have proved:

> If all three factors have size at least two, no endpoint-separable
> coloring of the form (18) can be proper when at least two of the
> three Golomb alphabets have size at least three.

This is a literal two-coordinate rectangle obstruction.  It explains
why the binary affine proof does not extend by replacing its bits with
arbitrary two-label functions.

## 6. Bounded discovery and exact remaining question

A bounded two-color search on the abstract no-carry rectangle
hypergraphs returned literal colorings for factor sizes
\(3\times3\times3\) and \(4\times4\times2\).  It returned a raw
negative answer for \(4\times3\times3\).  No short mathematical
derivation of that negative was obtained, so it is not asserted as an
uncolorability theorem and is not used above.

The proved conclusions are the construction (9), its exact ratio
(15), and the obstructions to the formula classes (16) and (18).
Whether colorings beyond these formula classes give a proper
two-coloring for every triple of arbitrary Golomb alphabets remains
unresolved in this note.
