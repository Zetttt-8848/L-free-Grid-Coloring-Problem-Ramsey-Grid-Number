# Adjacent ruler differences in a two-copy weak source

Let \(P\) be Golomb and suppose \(1\notin\Delta P\).  Put

\[
S=P\sqcup(P+1),
\]

with diagonal color \(0\) on \(P\) and diagonal color \(1\) on
\(P+1\).  In any proper coloring of \(W(S)\), for \(p<q\) in \(P\),

\[
z(q,p)=1,\qquad z(q+1,p+1)=0.
\tag{1}
\]

Retain the cross-copy cells

\[
\alpha_p=z(p+1,p),\qquad
u_{pq}=z(q+1,p),\qquad
v_{pq}=z(q,p+1).
\tag{2}
\]

The last cell exists because \(q-p\ne1\).

There is one immediate constraint involving the \(\alpha\)'s:

\[
\boxed{
\alpha_p=\alpha_q=\varepsilon
\quad\Longrightarrow\quad
u_{pq}=1-\varepsilon.
}
\tag{3}
\]

Indeed, \((p+1,p)\) and \((q+1,q)\) are parallel endpoint cells of
offset \(1\), and their completion is \((q+1,p)\).

Now fix two ruler edges

\[
q-p=d,\qquad s-r=d+1,
\qquad p<q,\quad r<s,
\tag{4}
\]

with all four endpoints in \(P\).  Golombness permits \(q=r\) or
\(p=s\), but \(p=r\) would put the difference \(1\) between \(q,s\),
and \(q=s\) would put the difference \(1\) between \(r,p\).
Consequently exactly one of \(p<r\) and \(r<p\) holds.

## 1. The shorter edge starts first

Assume \(p<r\).  Put

\[
U=u_{pq},\qquad V=v_{rs},\qquad
X=z(s,p),\quad Y=z(s+1,p),\quad Z=z(s,p+1).
\tag{5}
\]

The following are all positive corners:

\[
\begin{array}{c|ccc|c}
&\text{first}&\text{completion}&\text{third}&\text{step}\\ \hline
(i)&(q+1,p)=U&(s,p)=X&(s,r)=1&r-p\\
(ii)&(q,p)=1&(s,p)=X&(s,r+1)=V&r-p+1\\
(iii)&(q+1,p)=U&(s+1,p)=Y&(s+1,r+1)=0&r+1-p\\
(iv)&(s,p)=X&(s+1,p)=Y&(s+1,p+1)=0&1.
\end{array}
\tag{6}
\]

They give the local implications

\[
U=1\Longrightarrow X=0,\qquad
V=1\Longrightarrow X=0,
\tag{7}
\]

\[
U=0\Longrightarrow Y=1,\qquad
X=0\Longrightarrow Y=1.
\tag{8}
\]

If \(U=0\), the first implication in (8) applies.  If \(U=1\), then
(7) gives \(X=0\), and the second implication in (8) applies.
Therefore

\[
\boxed{p<r\quad\Longrightarrow\quad z(s+1,p)=1.}
\tag{9}
\]

The other cross cell is not discarded.  Comparing
\((q+1,p+1)=0\) with \(V=(s,r+1)\), both of offset \(d\), gives

\[
V=0\Longrightarrow Z=1.
\tag{10}
\]

Thus the complete immediately forced alternatives retained by the
shared completion \(X\) are

\[
X=1\Longrightarrow U=V=0,
\qquad
V=0\Longrightarrow Z=1,
\qquad
Y=1.
\tag{11}
\]

No value of \(U,V,X,Z\) beyond these implications is asserted.

## 2. The longer edge starts first

Assume \(r<p\).  Since \(1\notin\Delta P\), in fact \(r+1<p\).  Put

\[
U=u_{pq},\qquad V=v_{rs},\qquad
C=z(q+1,r),\quad D=z(q+1,r+1),\quad E=z(q,r+1).
\tag{12}
\]

The relevant positive corners are

\[
\begin{array}{c|ccc|c}
&\text{first}&\text{completion}&\text{third}&\text{step}\\ \hline
(i)&(s,r)=1&(q+1,r)=C&(q+1,p)=U&p-r\\
(ii)&(s+1,r+1)=0&(q+1,r+1)=D&(q+1,p)=U&p-r-1\\
(iii)&(q,r)=1&(q+1,r)=C&(q+1,r+1)=D&1.
\end{array}
\tag{13}
\]

If \(U=1\), corner (i) forces \(C=0\).  If \(U=0\), corner (ii)
forces \(D=1\), after which corner (iii) forces \(C=0\).  Hence

\[
\boxed{r<p\quad\Longrightarrow\quad z(q+1,r)=0.}
\tag{14}
\]

The cell \(V\) participates in the two additional implications

\[
V=1\Longrightarrow E=0,\qquad
V=0\Longrightarrow D=1.
\tag{15}
\]

Together with corner (ii), this also says

\[
D=0\Longrightarrow U=V=1.
\tag{16}
\]

Again, these are the complete local consequences used here; no
unlisted color is inferred.

## 3. A bounded-multiplicity forced-cell charge

Associate to the adjacent-difference pair in (4) the physical cell

\[
\Phi(p,q;r,s)=
\begin{cases}
(s+1,p),&p<r,\\
(q+1,r),&r<p.
\end{cases}
\tag{17}
\]

By (9) and (14), the first type always has color \(1\), while the
second always has color \(0\).

This map has multiplicity at most two.  For the first type, a cell
\((R,T)\) determines

\[
p=T,\qquad s=R-1,\qquad q+r=p+s-1=R+T-2.
\tag{18}
\]

A Golomb set is also Sidon for unordered sums: two distinct unordered
pairs with the same sum would give two representations of the same
positive difference.  Hence (18) determines the unordered pair
\(\{q,r\}\) uniquely, and there are at most two assignments of its
members to \(q,r\).

For the second type, \((R,T)\) determines

\[
r=T,\qquad q=R-1,\qquad p+s=q+r+1=R+T.
\tag{19}
\]

The same Sidon argument determines \(\{p,s\}\) uniquely, again leaving
at most two assignments.  Finally, one physical cell cannot receive
both types of charge, because the first type forces its color to be
\(1\) and the second forces it to be \(0\).  Thus

\[
\boxed{|\Phi^{-1}(R,T)|\le2.}
\tag{20}
\]

The bound two can occur at the level of Golomb arithmetic: swapping the
two inner marks in (18), or in (19), can produce two different adjacent
difference pairs without repeating a difference.

## 4. Exact remaining graph gap

Equations (9), (14), and (20) give an actual-cell charge for every pair
of ruler differences whose lengths differ by one.  They also retain
the local \(u_{pq},v_{rs}\), \(\alpha\), and shared-completion
constraints rather than assigning colors independently.

The target set of \(\Phi\), however, consists of long cross-copy cells
and can be quadratic in \(|P|\).  Bounded multiplicity alone therefore
does not prove that the number of adjacent-difference pairs is
\(O(|P|)\).  Such a linear conclusion would require another restriction
on how many forced cells of the forms \((s+1,p)\) and \((q+1,r)\) can
coexist in one proper coloring, or a span-sensitive packing of those
cells.  No universal linear bound is assumed here.
