# A dissociated-cube counterexample to a universal row-column sign bound

**Status:** proved for an explicit sign family.  The signs are arbitrary
and are not asserted to define a proper coloring.

## 1. Source and sign rule

For \(r\ge1\), put

\[
W(X)=\sum_{i\in X}5^i,
\qquad
A_r=\{W(X):X\subseteq[r]\}.
\tag{1}
\]

The powers of five make all signed source differences coordinatewise
unique.  Indeed, equality of two differences gives
\(\sum_i c_i5^i=0\) with \(|c_i|\le2\); the largest nonzero term has
absolute value greater than the sum of all preceding terms.

The source has \(2^r\) marks and

\[
M_r=|T(A_r)|=\binom{2^r}{2}
=\frac{4^r-2^r}{2}.
\tag{2}
\]

Define

\[
q_r=\left\lfloor\frac r4\right\rfloor,
\qquad
h_r(k)=
\begin{cases}
+1,&k\le q_r,\\
-1,&k>q_r.
\end{cases}
\tag{3}
\]

For every cell with \(W(X)<W(Y)\), assign the sign

\[
\boxed{z_r(W(Y),W(X))=h_r(|X\cap Y|).}
\tag{4}
\]

This is a nonlinear intersection-threshold rule, rather than a linear
Boolean character.

Let \(Q_r(z)\) denote the sum of the row and column pair correlations,
excluding the offset-diagonal pair.  Thus a corner with endpoint cells
\(P,R\) and completion cell \(C\) contributes

\[
z_C(z_P+z_R).
\tag{5}
\]

We prove

\[
Q_r(z_r)
=-\left(\frac12+o(1)\right)6^r
\tag{6}
\]

and consequently

\[
\boxed{
\frac{Q_r(z_r)}{M_r}
=-(1+o(1))\left(\frac32\right)^r.}
\tag{7}
\]

In particular, \(Q_r(z_r)/M_r\) is unbounded below.

## 2. Exact corner sum on one difference fiber

Fix a nonzero signed coordinate difference.  Let \(P\) be its positive
support, \(N\) its negative support, and put

\[
s=|P|+|N|,
\qquad
t=r-s.
\]

Every representation of this difference is uniquely

\[
X_U=N\cup U,
\qquad
Y_U=P\cup U,
\qquad
U\subseteq[r]\setminus(P\cup N).
\tag{8}
\]

Thus its difference fiber has \(2^t\) cells.  Two distinct
representations indexed by \(U,V\) give one corner.  Whichever
representation is lower in the scalar order, the two endpoint signs
are

\[
h_r(|U|),\qquad h_r(|V|),
\]

and the completion sign is

\[
h_r(|U\cap V|).
\]

The last equality follows from

\[
(N\cup U)\cap(P\cup V)=U\cap V.
\]

The contribution of the unordered pair \(\{U,V\}\) is therefore

\[
h_r(|U\cap V|)
\bigl(h_r(|U|)+h_r(|V|)\bigr).
\tag{9}
\]

Define the exact ordered-pair sum

\[
F_{r,t}
=
\sum_{U,V\subseteq[t]}
h_r(|U\cap V|)h_r(|U|).
\tag{10}
\]

The two terms in (9) have the same total after exchanging \(U,V\).
The diagonal ordered pairs \(U=V\) contribute \(2\) each to their
sum.  Hence the total of (9) over all unordered distinct pairs is

\[
S_{r,t}=F_{r,t}-2^t.
\tag{11}
\]

This identity is exact.

## 3. Exact global reduction

For a support of size \(s\), there are

\[
\binom rs2^s
\]

nonzero signed coordinate vectors.  Negation pairs them, with exactly
one member of each pair giving a positive integer difference.
Therefore the number of positive differences with support size \(s\)
is

\[
\frac12\binom rs2^s.
\tag{12}
\]

Combining (11) and (12) gives

\[
\begin{aligned}
Q_r(z_r)
&=\frac12\sum_{s=1}^r
\binom rs2^s\left(F_{r,r-s}-2^{r-s}\right)\\
&=-M_r+
\frac12\sum_{s=1}^r\binom rs2^sF_{r,r-s}.
\end{aligned}
\tag{13}
\]

The second equality uses

\[
\frac12\sum_{s=1}^r\binom rs2^s2^{r-s}
=\frac{2^r(2^r-1)}2=M_r.
\]

## 4. The six-state count

It remains to estimate the last sum in (13).  First include its
\(s=0\) term:

\[
\Sigma_r
=
\sum_{s=0}^r\binom rs2^sF_{r,r-s}.
\tag{14}
\]

Expansion of (10) gives six equally weighted choices at each
coordinate:

- the coordinate lies in \(P\);
- it lies in \(N\);
- it lies outside the difference support and its \((U,V)\)-state is
  \(00,01,10\), or \(11\).

Let

\[
\mathsf A=|U\cap V|,
\qquad
\mathsf B=|U|.
\]

Among the six coordinate states, only \(11\) increments
\(\mathsf A\), while \(10\) and \(11\) increment \(\mathsf B\).
Consequently, under the uniform six-state product measure,

\[
\mathsf A\sim\operatorname{Bin}\left(r,\frac16\right),
\qquad
\mathsf B\sim\operatorname{Bin}\left(r,\frac13\right),
\tag{15}
\]

although the two variables are not independent.  Equation (14)
becomes

\[
\Sigma_r
=6^r\,
\mathbb E\!\left[h_r(\mathsf A)h_r(\mathsf B)\right].
\tag{16}
\]

The threshold \(r/4\) lies strictly between the two means \(r/6\)
and \(r/3\).  We only need Chebyshev's inequality.  From (15),

\[
\operatorname{Var}(\mathsf A)=\frac{5r}{36},
\qquad
\operatorname{Var}(\mathsf B)=\frac{2r}{9}.
\tag{17}
\]

For \(r\ge24\), the floor in \(q_r\) gives

\[
q_r-\frac r6\ge\frac r{24},
\qquad
\frac r3-q_r\ge\frac r{12}.
\]

Consequently,

\[
\Pr(\mathsf A>q_r)\le\frac{80}{r},
\qquad
\Pr(\mathsf B\le q_r)\le\frac{32}{r}.
\tag{18}
\]

Outside the union of the two exceptional events in (18),

\[
h_r(\mathsf A)=+1,
\qquad
h_r(\mathsf B)=-1.
\]

Since their product is always a sign, (16) and (18) yield the elementary
bound

\[
\Sigma_r
\le
\left(-1+\frac{224}{r}\right)6^r
\qquad(r\ge24).
\tag{19}
\]

The reverse bound \(\Sigma_r\ge-6^r\) is immediate because the
expectation in (16) is at least \(-1\).  Hence (19) squeezes the ratio
and gives

\[
\Sigma_r=-(1+o(1))6^r.
\tag{20}
\]

The omitted \(s=0\) term in (14) has absolute value at most \(4^r\),
because (10) contains \(4^r\) signs.  It follows that

\[
\sum_{s=1}^r\binom rs2^sF_{r,r-s}
=-(1+o(1))6^r.
\tag{21}
\]

Substitution into (13), together with \(M_r=O(4^r)=o(6^r)\), proves
(6).  Dividing by (2) proves (7).

There is also a concrete finite consequence.  If \(r\ge256\), then
\(-1+224/r\le-1/8\).  Removing the \(s=0\) term and using (13) gives

\[
Q_r(z_r)
\le
-M_r-\frac{6^r}{16}+\frac{4^r}{2}.
\tag{22}
\]

Since \(M_r<4^r/2\),

\[
Q_r(z_r)+\frac92M_r
<
\frac94\,4^r-\frac1{16}\,6^r<0;
\tag{23}
\]

the final inequality follows from
\((3/2)^r>36\).  Hence the proposed bound with constant \(9/2\)
already fails throughout this explicit family for every \(r\ge256\).

## 5. Consequence and scope

The explicit family (1), (3), (4) falsifies every universal inequality
of the form

\[
Q(z)\ge-C\binom{|A|}{2}
\]

with an absolute constant \(C\), when the inequality is required for
all sign assignments.  In particular, it falsifies the proposed
constant \(C=9/2\).

The rule \(z_r\) is not proper.  For \(r\ge4\), take signed-difference
support \(P=\{2\}\), \(N=\varnothing\), and the two common sets
\(U=\varnothing\), \(V=\{1\}\).  The resulting corner has cells

\[
\bigl(W(\{2\}),W(\varnothing)\bigr),\qquad
\bigl(W(\{1,2\}),W(\varnothing)\bigr),\qquad
\bigl(W(\{1,2\}),W(\{1\})\bigr).
\]

Their endpoint intersections have sizes \(0,0,1\), respectively.
Since \(q_r\ge1\), all three signs are \(+1\).  Thus the rule was built
only to make the aggregate \(Q\) negative and contains monochromatic
corners explicitly.

The argument therefore does not settle any inequality restricted to
signs arising from proper two-colorings, and it makes no claim about
the core source-energy hypothesis.
