# Cross-anchor overlap of supported weak differences

Let \(W(S)\) have one proper two-coloring.  Name its diagonal classes
\(B\) and \(C\), and also use \(B,C\) for their colors.  For
\(a\in B\), set

\[
P_a=\{b-a:b\in B,\ b>a\},
\qquad
D_a=\Delta P_a\cap(S-a).
\tag{1}
\]

The supported-difference theorem gives, for every \(h\in D_a\),

\[
a+h\in C,\qquad z(a+h,a)=B.
\tag{2}
\]

Each \(D_a\) is Golomb and sum-free.  This note compares (2) at
different anchors.

## 1. A shared supported length has one common completion

**Cross-anchor lemma.**  Let \(a<a'\) belong to \(B\), put
\(\delta=a'-a\), and suppose

\[
h\in D_a\cap D_{a'}.
\tag{3}
\]

Then the actual cell

\[
Q=(a'+h,a)
\tag{4}
\]

has color \(C\), and consequently

\[
\boxed{h+\delta\notin D_a.}
\tag{5}
\]

**Proof.**  By (2), the two cells

\[
(a+h,a),\qquad(a'+h,a')
\tag{6}
\]

have color \(B\).  They lie on the same positive offset \(h\).  Their
positive corner is

\[
(a+h,a),\qquad(a'+h,a),\qquad(a'+h,a'),
\tag{7}
\]

so properness forces its completion \(Q\) to have color \(C\).

If \(h+\delta\) belonged to \(D_a\), equation (2) at anchor \(a\)
would apply to the same physical cell, because

\[
a+(h+\delta)=a'+h.
\]

It would give \(z(Q)=B\), a contradiction.  \(\square\)

Equivalently, the overlap of two supported-difference sets obeys

\[
\boxed{
D_a\cap D_{a'}\cap(D_a-\delta)=\varnothing,
\qquad
D_a-\delta=\{h:h+\delta\in D_a\}.
}
\tag{8}
\]

This is a cross-anchor exclusion.  The single-anchor facts that
\(D_a\) is Golomb and sum-free do not imply it unless
\(\delta\in D_a\), which need not hold.

## 2. Several anchors hitting the same diagonal output

For \(r\in C\), define its supported anchor set

\[
\mathcal A(r)=\{a\in B:a<r,\ r-a\in D_a\},
\qquad m_r=|\mathcal A(r)|.
\tag{9}
\]

Every \(a\in\mathcal A(r)\) supplies the actual \(B\)-colored cell
\((r,a)\).  Take \(a<a'\) in \(\mathcal A(r)\), and put

\[
\delta=a'-a,\qquad h=r-a'.
\tag{10}
\]

Then

\[
h\in D_{a'},\qquad h+\delta=r-a\in D_a.
\tag{11}
\]

If \(h\) also belonged to \(D_a\), the cross-anchor lemma would give a
contradiction.  Hence

\[
\boxed{r-a'\notin D_a\qquad(a<a'\text{ in }\mathcal A(r)).}
\tag{12}
\]

The physical form is slightly stronger.  If

\[
t=r-\delta=a+h
\tag{13}
\]

is a source mark, the positive corner

\[
(t,a),\qquad(r,a),\qquad(r,a')
\tag{14}
\]

forces

\[
z(t,a)=C.
\tag{15}
\]

If \(t\notin S\), the same ordered pair of anchors records an actual
source hole.  Thus (12) separates exactly into:

* \(a+(r-a')\notin S\); or
* that mark exists, but \(r-a'\notin\Delta P_a\), and its cell over
  \(a\) is forced to color \(C\).

For fixed \(r\), the map

\[
\{a,a'\}\longmapsto (r-a'+a,a),\qquad a<a',
\tag{16}
\]

is injective: the cell and \(r\) recover
\(\delta=r-\text{row}\) and then \(a'=a+\delta\).  Therefore a
supported output of multiplicity \(m_r\) produces

\[
\binom{m_r}{2}
\tag{17}
\]

distinct hole-or-\(C\)-cell exclusions at that output.  This goes beyond
the single-anchor common-neighbor bound: it uses the shared physical row
\(r\) and all pairs of anchors in \(\mathcal A(r)\).

## 3. Exact structure when the same completion is reused

The cells in (16) need not be distinct for different outputs \(r\).
Their reuse nevertheless has a further restriction.

Fix \(a\in B\) and \(h>0\), and define

\[
E_{a,h}=
\{a'>a:h\in D_{a'},\ h+(a'-a)\in D_a\}.
\tag{18}
\]

Every \(a'\in E_{a,h}\) gives the common output

\[
r=a'+h
\]

at anchors \(a,a'\), and charges the same potential cell

\[
(a+h,a).
\tag{19}
\]

The cross-anchor lemma first shows

\[
E_{a,h}\ne\varnothing\quad\Longrightarrow\quad h\notin D_a,
\tag{20}
\]

so when the cell in (19) exists its color is \(C\), not the \(B\) color
that membership \(h\in D_a\) would force.

Moreover, the affine map

\[
a'\longmapsto h+(a'-a)
\tag{21}
\]

sends \(E_{a,h}\) injectively into \(D_a\).  If
\(a'_1<a'_2\) belong to \(E_{a,h}\), write

\[
H_i=h+(a'_i-a)\in D_a,\qquad
d=a'_2-a'_1=H_2-H_1.
\]

If \(d\in D_a\), then \(H_1,d,H_1+d=H_2\) all lie in \(D_a\),
contradicting its sum-free property.  Hence

\[
\boxed{\Delta E_{a,h}\cap D_a=\varnothing.}
\tag{22}
\]

Thus high reuse of one physical completion requires a translated
subset of \(D_a\) whose every internal difference avoids \(D_a\).
This is an actual cross-anchor restriction, not an independent
recoloring of the sets \(D_a\).

## 4. Relation to reflected triples and the remaining gap

Membership \(h\in D_a\) is originally witnessed by a reflected triple
of later \(B\)-marks at anchor \(a\).  The lemma above does not merely
repeat that transport.  It takes two already transported cells
\((a+h,a)\) and \((a'+h,a')\), uses them as parallel endpoints on the
same physical offset \(h\), and identifies their shared completion
\((a'+h,a)\).  Equation (5) comes from the competition between this
pair completion and a third supported-difference transport.

The charge (16) is injective only after the output \(r\) is retained.
Across different outputs, one cell \((a+h,a)\) can be reused by every
anchor in \(E_{a,h}\).  Equation (22) constrains this reuse, but does not
give a constant bound: a sum-free Golomb set can contain a large subset
whose differences avoid itself.  A global capacity estimate would need
either a bound on these sets \(E_{a,h}\) using further mixed-cell colors,
or an amortization of their missing differences against source holes.
No such bounded multiplicity, finite-cap inequality, or S21 conclusion
is asserted here.
