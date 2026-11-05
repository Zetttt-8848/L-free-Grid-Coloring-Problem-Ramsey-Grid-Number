# Aggregating common-completion fans into signed-fiber energy (checkpoint 0019)

Let
\[
A=\{a_1<\cdots<a_m\},\qquad
M=\binom m2,\qquad
L=\max A-\min A,
\]
and suppose that the strict source triangle
\[
V(A)=\{(y,x):x,y\in A,\ x<y\}
\]
has a proper coloring \(z:V(A)\to\{-1,+1\}\). Put
\[
F_d=\{x:x,x+d\in A\},\qquad r_d=|F_d|,
\]
and let \(F_d^\sigma\) be the starts whose offset-\(d\) cell has sign
\(\sigma\):
\[
F_d^\sigma=\{x\in F_d:z(x+d,x)=\sigma\}.
\]
Each signed fiber \(F_d^\sigma\) is Golomb.

The aim here is to aggregate the common-outer-cell rule from
fibers/SOURCE_SEPARATOR_SWITCH_0018.md. The result retains two quantities
that are lost in a standalone Cartesian estimate: bichromatic pairs inside
the actual signed fibers, and missing source translates at the two
boundaries of a fan.

## 1. Fans in reflection notation

Fix an outer cell
\[
Q=(v,u),\qquad u<v,\qquad q=z(Q).
\]
For an interior mark \(t\), write
\[
\bar t=u+v-t.
\]
Whenever
\[
u<t<v,\qquad t,\bar t\in A, \tag{1}
\]
the cells
\[
S_t=(t,u),\qquad T_t=(v,\bar t),\qquad Q=(v,u) \tag{2}
\]
form an original positive corner, because
\[
t-u=v-\bar t.
\]
Thus
\[
\operatorname{NAE}(S_t,T_t,Q).
\]

One may use all \(t\) satisfying (1), or any chosen subfamily. In
particular, a separator quadruple
\[
u<b<c<v,\qquad u+v=b+c
\]
contributes the two indices \(t=b,c\): these are respectively its child
pair \((\alpha,\beta)\) and cross-support pair \((X,Y)\).

Let \(\mathcal I_Q\) be the chosen fan index set and put
\[
e_{Q,t}
 =\operatorname{Eq}(S_t,T_t)
 =\frac{1+z(S_t)z(T_t)}2,
\qquad
H_Q=\sum_{t\in\mathcal I_Q}e_{Q,t}. \tag{3}
\]
The common-completion identity says
\[
q\bigl(z(S_t)+z(T_t)\bigr)=-2e_{Q,t}. \tag{4}
\]
Consequently, if \(e_{Q,t}=1\), then both endpoint cells have sign
\(-q\). All \(H_Q\) monochromatic fan pairs therefore supply
same-colored representatives on column \(u\), and same-colored partners
on row \(v\).

Let
\[
H=\sum_{Q\in V(A)}H_Q,
\]
taking \(H_Q=0\) for outer cells with no selected fan pair. Cauchy--Schwarz
gives the second-moment lower bound
\[
\boxed{
\sum_Q\binom{H_Q}{2}
\ge \frac12\left(\frac{H^2}{M}-H\right).
} \tag{5}
\]

## 2. Closing a same-column charge into a signed fiber

Consider two monochromatic pairs in one fan, indexed by
\[
t<t',\qquad \delta=t'-t.
\]
Write
\[
\bar t=u+v-t,\qquad \bar t'=u+v-t';
\]
then \(\bar t'<\bar t\) and \(\bar t-\bar t'=\delta\). By (4), all four
cells
\[
(t,u),\ (t',u),\ (v,\bar t),\ (v,\bar t')
\]
have one sign, say \(s=-q\).

There are two ways to close this common-line equality into an original
corner.

If \(u+\delta\in A\), then
\[
(t,u),\qquad (t',u),\qquad (t',u+\delta) \tag{6}
\]
is a positive corner of step \(\delta\). Its first two cells have sign
\(s\), so
\[
z(t',u+\delta)=-s. \tag{7}
\]
Put \(d=t-u\). The cells \((t,u)\) and \((t',u+\delta)\) both have offset
\(d\), with starts \(u,u+\delta\), and have opposite signs. Hence (6)
creates a bichromatic pair at gap \(\delta\) inside \(F_d\).

Similarly, if \(v-\delta\in A\), then
\[
(v-\delta,\bar t'),\qquad
(v,\bar t'),\qquad
(v,\bar t) \tag{8}
\]
is a positive corner of step \(\delta\). The last two cells have sign
\(s\), so the first has sign \(-s\). The first cell in (8) and
\((v,\bar t)\) again lie in one offset-\(d\) fiber, now with starts
\(\bar t',\bar t\), and form a bichromatic pair at gap \(\delta\).

Thus every pair of monochromatic fan pairs for which at least one of
\[
u+\delta,\qquad v-\delta \tag{9}
\]
belongs to \(A\) can be charged to a bichromatic pair in an actual signed
difference fiber.

## 3. Multiplicity and the boundary-open remainder

Define the weighted bichromatic fiber energy
\[
\mathcal B(A,z)
=
\sum_{d>0}
\ \sum_{\substack{\{x,y\}\subset F_d\\
                    z(x+d,x)\ne z(y+d,y)}}
r_A(|x-y|). \tag{10}
\]
Charge a closed fan pair through the left closure in (6) when available,
and otherwise through the right closure in (8).

A fixed bichromatic fiber pair at gap \(\delta\) receives at most
\(r_A(\delta)\) left charges. For a left charge, the target determines
\(u,t,t'\); the remaining outer endpoint \(v\) is determined by the
reflected start \(\bar t'\), and the possible pairs
\(\bar t',\bar t'+\delta\) are counted by \(r_A(\delta)\). For a right
charge the target determines \(v,\bar t',\bar t\), while the possible
pairs \(t,t+\delta\) are again counted by \(r_A(\delta)\). The two
orientations need not be disjoint for a fixed unordered target.
Therefore their safe combined multiplicity is \(2r_A(\delta)\), and all
closed charges together are at most \(2\mathcal B(A,z)\).

It remains to count charges for which both marks in (9) are absent. For a
fixed \(\delta\), there are
\[
m-r_A(\delta)
\]
choices of \(u\in A\) with \(u+\delta\notin A\), and the same number of
choices of \(v\in A\) with \(v-\delta\notin A\). Once \(u,v,t\) are fixed,
the other three marks \(t'=t+\delta,\bar t,\bar t'\) are determined.
Dropping their membership and order restrictions leaves at most
\(r_A(\delta)\) choices for \(t,t+\delta\). Hence the number of
boundary-open charges of gap \(\delta\) is at most
\[
r_A(\delta)\bigl(m-r_A(\delta)\bigr)^2. \tag{11}
\]

Combining the closed and open parts gives the aggregate fan bound
\[
\boxed{
\sum_Q\binom{H_Q}{2}
\le
2\mathcal B(A,z)
+
\sum_{\delta>0}
r_A(\delta)\bigl(m-r_A(\delta)\bigr)^2.
} \tag{12}
\]
Together with (5),
\[
\boxed{
\frac12\left(\frac{H^2}{M}-H\right)
\le
2\mathcal B(A,z)
+
\sum_{\delta>0}
r_A(\delta)\bigl(m-r_A(\delta)\bigr)^2.
} \tag{13}
\]
This is a second-moment inequality for any selected collection of source
fans. For a separator \(A=B\sqcup C\), selecting the child and
cross-support pairs of every crossing source quadruple gives exactly
\(2U(B,C)\) fan-pair incidences before the monochromatic restriction in
(3).

## 4. Explicit Golomb/span budget

Let
\[
H_{\rm all}
=\sum_{d>0}
\left[
\binom{|F_d^+|}{2}+\binom{|F_d^-|}{2}
\right]. \tag{14}
\]
The total number of bichromatic unordered pairs within the difference
fibers is
\[
\sum_d |F_d^+||F_d^-|=T-H_{\rm all}, \tag{15}
\]
where
\[
T=\sum_d\binom{r_d}{2}.
\]
If
\[
R=\max_{\delta>0}r_A(\delta),
\]
then (10) and (15) give
\[
\mathcal B(A,z)\le R\,(T-H_{\rm all}). \tag{16}
\]

Golombness supplies an explicit span estimate for \(R\). Since
\(F_d^\sigma\) lies in an interval of span at most \(L-d\), its distinct
positive differences give
\[
\binom{|F_d^\sigma|}{2}\le L-d.
\]
Thus
\[
r_d
\le 1+\sqrt{1+8(L-d)}
\le 1+\sqrt{1+8L}, \tag{17}
\]
and hence \(R\le1+\sqrt{1+8L}\).

Substituting (16)--(17) into (13) yields the fully explicit form
\[
\boxed{
\frac12\left(\frac{H^2}{M}-H\right)
\le
2\bigl(1+\sqrt{1+8L}\bigr)(T-H_{\rm all})
+
\sum_{\delta>0}
r_\delta(m-r_\delta)^2.
} \tag{18}
\]
If all source corners are included rather than only one separator family,
then \(H=H_{\rm all}\): every same-colored pair in a signed difference
fiber has a unique completion \(Q\) and appears in exactly one fan.

## 5. Quantitative scope

Inequality (18) is the requested source-specific second-moment route. Its
closed part is paid for by bichromatic energy in the actual signed
fibers, with the maximum multiplicity controlled by their Golomb/span
bound, including the factor \(2\) for the two closure orientations. The
binary-strip construction has no child fibers and therefore
has neither (7) nor the budget (10).

The remaining obstruction is explicit: a common-column equal pair is not
an \(L\)-pair when both translated boundary marks in (9) are absent. The
last sum in (18) pays for exactly those unsupported closures. Golombness
alone does not make
\[
\sum_\delta r_\delta(m-r_\delta)^2
\]
linear in \(M\); discarding the actual shift profile gives only much
larger bounds. Consequently (18) does not by itself prove \(T\le10M\) or
\(M\le21L\). A successful continuation must either amortize this
boundary-open term through a rank cut, or combine it with another source
identity that forces color structure when both boundary translates are
missing.

The factor \(2\) in (12), (13), and (18) is a scope correction: the
left-closure and right-closure multiplicity estimates are separate, and
no union injection or cancellation between them is used.
