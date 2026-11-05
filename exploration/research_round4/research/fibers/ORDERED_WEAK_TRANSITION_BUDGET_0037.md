# An ordered transition budget for a properly colored weak source

Let \(S=B\sqcup C\subseteq[0,L]\cap\mathbb Z\), where \(B\) and \(C\)
are the two diagonal color classes of one proper two-coloring of
\(W(S)\).  Both \(B\) and \(C\) are Golomb.  Put

\[
\mathcal R=\Delta B\cap\Delta C,\qquad \rho=|\mathcal R|.
\tag{1}
\]

For each positive integer \(k\), retain the orientation of every mixed
pair by defining

\[
X_k=\{u:u\in B, u+k\in C\},\qquad
Y_k=\{u:u\in C, u+k\in B\},
\tag{2}
\]

and write \(x_k=|X_k|\), \(y_k=|Y_k|\).  Since every pair in
\(B\times C\) has exactly one positive absolute difference and one of
the two orientations,

\[
\sum_{k=1}^L(x_k+y_k)=bc,\qquad b=|B|,\quad c=|C|.
\tag{3}
\]

## 1. Shared monochromatic lengths are exactly mixed collisions

There is an exact identity

\[
\boxed{
\rho=
\sum_{k=1}^L
\left[\binom{x_k}{2}+\binom{y_k}{2}\right].
}
\tag{4}
\]

Indeed, take two starts \(u<v\) in \(X_k\).  Then

\[
u,v\in B,\qquad u+k,v+k\in C,
\]

so \(h=v-u\) belongs to \(\Delta B\cap\Delta C\).  The same conclusion
holds for two starts in \(Y_k\).  No two different pairs so obtained
can give the same \(h\), because that would give two representations of
\(h\) inside \(B\), or inside \(C\).

Conversely, for \(h\in\mathcal R\), let \(p_B(h)\) and \(p_C(h)\) be
the unique starts of the \(B\)- and \(C\)-edges of length \(h\).  If
\(p_B<p_C\), set \(k=p_C-p_B\).  The two starts

\[
p_B,\qquad p_B+h
\]

belong to \(X_k\).  If \(p_C<p_B\), the analogous two starts belong to
\(Y_k\).  This is inverse to the preceding construction and proves
(4).

Thus the common-difference count is not merely bounded by a mixed
energy: it is exactly the collision energy of the oriented mixed
difference bins.

## 2. Rotation inside the ordered gap

For \(h\in\mathcal R\), define

\[
k_h=|p_B(h)-p_C(h)|.
\tag{5}
\]

Suppose first that \(p_B<p_C\).  The ordered mixed-interval theorem
forbids every \(C\mathbin{\to}B\) edge of length \(h\) whose start lies
strictly between \(p_B\) and \(p_C\).  A fully occupied length-\(h\)
edge at such a start cannot be monochromatic either, since the unique
monochromatic starts are the two boundary starts \(p_B,p_C\).
Consequently every fully occupied interior edge must point

\[
B\mathbin{\to}C.
\tag{6}
\]

If \(p_C<p_B\), the color-reversed argument says that every fully
occupied interior edge must point \(C\mathbin{\to}B\).

Let \(a_h\) be the number of these fully occupied interior edges, in
the forced orientation, and define the missing-pair defect

\[
d_h=
\#\left\{
w:\min(p_B,p_C)<w<\max(p_B,p_C),\
\{w,w+h\}\not\subseteq S
\right\}.
\tag{7}
\]

There are exactly \(k_h-1\) integer starts in the open interval, so the
ordered theorem gives the exact local partition

\[
\boxed{k_h-1=a_h+d_h.}
\tag{8}
\]

This is the promised rotation mechanism: the pair of equal-orientation
mixed \(k_h\)-edges that creates the shared length \(h\) forces every
available edge obtained by rotating the rectangle into its interior to
have the same lower-to-upper color orientation as those mixed
\(k_h\)-edges. The forbidden orientation is the opposite one.

## 3. Global weighted collision identity

Put

\[
A=\sum_{h\in\mathcal R}a_h,\qquad
D=\sum_{h\in\mathcal R}d_h,\qquad
P_{\mathcal R}=\sum_{h\in\mathcal R}(x_h+y_h).
\tag{9}
\]

Every edge counted by \(A\) is a mixed pair whose length is the
corresponding shared length \(h\).  Distinct \(h\)'s give distinct
mixed pairs, hence

\[
A\le P_{\mathcal R}\le bc.
\tag{10}
\]

Under the bijection proving (4), a pair of starts in \(X_k\) or
\(Y_k\) has \(k_h=k\).  Summing (8) therefore yields

\[
\boxed{
\sum_{k=1}^L (k-1)
\left[\binom{x_k}{2}+\binom{y_k}{2}\right]
=A+D
\le P_{\mathcal R}+D.
}
\tag{11}
\]

In particular, for every integer \(K\ge2\),

\[
\boxed{
\sum_{k=K}^L
\left[\binom{x_k}{2}+\binom{y_k}{2}\right]
\le \frac{P_{\mathcal R}+D}{K-1}.
}
\tag{12}
\]

Thus repeated oriented mixed differences with a large spatial gap have
a genuine global budget.  They must be paid either by distinct mixed
pairs at shared lengths or by missing translated pairs inside their
ordered rectangles.

If \(H=(L+1)-(b+c)\) is the number of absent marks of \([0,L]\), then
a coarse bound on the explicit defect is

\[
d_h\le2H,\qquad D\le2\rho H.
\tag{13}
\]

For fixed \(h\), this follows by charging an incomplete start \(w\) to
one of the absent marks \(w,w+h\); each absent mark has at most the two
possible preimages.  Estimate (13) is generally too large, but records
that \(D\) is precisely a sparse-source term rather than an unexplained
loss.

## 4. Span form

Let

\[
U=L-|\Delta B\cup\Delta C|
\tag{14}
\]

be the number of lengths used by neither diagonal class.  Golombness
and inclusion-exclusion give

\[
L=\binom b2+\binom c2+U-\rho.
\tag{15}
\]

Combining (12) with (15), and writing

\[
R_{<K}=\sum_{1\le k<K}
\left[\binom{x_k}{2}+\binom{y_k}{2}\right],
\]

gives the valid parameterized span bound

\[
\boxed{
L\ge
\binom b2+\binom c2+U
-R_{<K}-\frac{P_{\mathcal R}+D}{K-1}.
}
\tag{16}
\]

This retains both kinds of slack that an ordered argument must handle:
collisions at short mixed gaps and missing translated pairs at long
gaps.

## 5. Exact remaining obstruction

The ordered-transition rule alone gives no charge when \(k_h=1\): the
open interval between the two monochromatic starts is empty, and the
coefficient \(k-1\) in (11) vanishes.  More generally, a sparse source
can have \(d_h=k_h-1\), so a large-gap collision can be paid entirely by
\(D\).  These are structural limitations, not losses from the
summation.

Consequently, (11) does not prove the open bound
\(L\ge bc-b-c\).  To obtain such an unweighted span estimate from this
mechanism, one still needs a separate bound for

\[
R_{<K}+\frac{D}{K-1}
\tag{17}
\]

at some useful scale \(K\), using further completion colors or a new
injection into unused lengths.  The ordered six-mark theorem supplies
the term \(P_{\mathcal R}\) in (11), but it does not by itself control
the two terms in (17).
