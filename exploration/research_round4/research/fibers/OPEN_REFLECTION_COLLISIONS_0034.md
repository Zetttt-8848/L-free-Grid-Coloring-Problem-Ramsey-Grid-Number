# Open reflected transports colliding with an ordinary fan

## 1. Coordinates at one target

Let \(A\) have a proper coloring \(z:V(A)\to\{\pm1\}\), and fix a target
cell
\[
q=(v,u),
\qquad e=v-u>0,
\qquad s=z(q).
\]

Consider a column-open reflected transport into \(q\), coming from a signed
triple
\[
a<b<c\quad\text{in }F_d^s.
\]
Writing \(w=a+c-b\), the target is
\[
(c+d,w)=(v,u).
\]
Put \(h=b-a\). The coordinate equations become
\[
w=u,
\qquad c=u+h=v-d,
\qquad h=e-d.
\tag{1}
\]
Column-openness is exactly
\[
u\in A,\qquad u+d\notin A.
\tag{2}
\]
The last seed cell is the actual row cell
\[
\rho_d=(v,v-d)=(c+d,c),
\qquad z(\rho_d)=s.
\tag{3}
\]

Similarly, a row-open reflected transport at lower offset \(d\) has
\[
a=u,
\qquad w=v-d=u+(e-d),
\qquad v-d\notin A,
\tag{4}
\]
and exposes the actual column cell
\[
\kappa_d=(u+d,u),
\qquad z(\kappa_d)=s.
\tag{5}
\]

An ordinary completion pair at \(q\) and lower offset \(f<e\) consists of
\[
\ell_f=(u+f,u),
\qquad
r_f=(v,v-f).
\tag{6}
\]
If this pair is monochromatic, properness forces
\[
z(\ell_f)=z(r_f)=-s.
\tag{7}
\]

## 2. Uniqueness at fixed target and lower offset

For fixed \(q,d\), there is at most one column-open seed triple of sign
\(s\). Indeed, (1) fixes \(h=e-d\) and \(c=v-d\). The remaining starts
\(a,b=a+h\) would be a pair of gap \(h\) in the Golomb set \(F_d^s\), so
there is at most one such pair.

The row-open statement is symmetric: equations (4) fix \(a=u\) and
\(h=e-d\), while the remaining pair \(b,c=b+h\) is unique in \(F_d^s\).

Moreover, an open transport at offset \(d\) cannot coexist with an ordinary
fan pair at the same offset. For a column-open transport, (2) says
\(u+d\notin A\), while the fan needs \(u+d\in A\). For a row-open transport,
(4) says \(v-d\notin A\), while the fan needs \(v-d\in A\).

Thus all offsets appearing in the collision below are distinct.

## 3. Two-open/one-fan injection

Let \(C_q\) be the set of lower offsets of column-open transports into \(q\),
and let \(R_q\) be the analogous row-open set. Let \(H_q\) be the number of
monochromatic ordinary fan pairs completed by \(q\), equivalently the number
of offsets \(f\) satisfying (6)--(7).

**Row collision lemma.** The map
\[
\bigl(\{d_1,d_2\},f\bigr)
\longmapsto
\bigl(\{\rho_{d_1},\rho_{d_2}\},r_f\bigr)
\tag{8}
\]
injects the configurations consisting of two distinct column-open transports
and one monochromatic fan pair at \(q\) into triples of distinct cells on row
\(v\), two of color \(s\) and one of color \(-s\).

The color assertion is (3) and (7). The cells are distinct because their
lower coordinates are \(v-d_1,v-d_2,v-f\), and Section 2 makes the three
offsets distinct. The image recovers the offsets from those lower
coordinates. Once \(q,d_i\) is known, the corresponding open seed is unique
by Section 2, while \(q,f\) uniquely determines the fan pair. Hence (8) is
injective.

There is a symmetric **column collision lemma**:
\[
\bigl(\{d_1,d_2\},f\bigr)
\longmapsto
\bigl(\{\kappa_{d_1},\kappa_{d_2}\},\ell_f\bigr)
\tag{9}
\]
injects two row-open transports and one fan pair at \(q\) into a triple of
distinct cells on column \(u\), again with colors \(s,s,-s\).

If
\[
N_v^\sigma=|\{x\in A:x<v,\ z(v,x)=\sigma\}|,
\qquad
N_u^\sigma=|\{y\in A:y>u,\ z(y,u)=\sigma\}|,
\]
then the two injections give the concrete pointwise bounds
\[
\boxed{
\binom{|C_q|}{2}H_q
\le \binom{N_v^s}{2}N_v^{-s},
\qquad
\binom{|R_q|}{2}H_q
\le \binom{N_u^s}{2}N_u^{-s}.
}
\tag{10}
\]
These bounds use the actual colors on the physical row and column; they do
not replace them by an absolute cap.

## 4. Exact scope of the charge

The lemma handles two open transports of the same orientation. One
column-open and one row-open transport expose cells on different physical
lines, so the same three-cell injection does not combine them.

Nor is (8) a global injection after summing over targets. The same colored
triple on row \(v\) can be used by targets \((v,u)\) with different lower
marks \(u\); changing \(u\) changes the reflected seed gap
\(h=e-d=v-u-d\) without changing the three displayed row cells. The column
statement has the analogous reuse across different upper endpoints.

Thus (10) is a genuine collision restriction at one target and gives a
color-sensitive row/column charge for the requested narrow configuration.
A global estimate would still need to control reuse of one line triple across
different targets, or combine the mixed-orientation collisions with another
source identity.
