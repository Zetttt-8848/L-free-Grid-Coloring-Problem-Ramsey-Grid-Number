# Affine-slope coupling in a four-corner zero packet

Let (F:S_9\to\mathbb F_3), and for every available positive step write

\[
 g_d(p)=F(p)+F(p+d e_x)+F(p+d e_y)\in\mathbb F_3.
\tag{1}
\]

For a zero corner (g_d(p)=0) with (3\nmid d), define its excluded
affine slope

\[
 \sigma_d(p)=-\frac{F(p+d e_x)-F(p)}d\in\mathbb F_3.
\tag{2}
\]

Adding (eta(x-y)) makes this corner monochromatic exactly when
(eta=sigma_d(p)). In a proper lift normalized to (eta=0), every
zero corner is rainbow, so every defined slope lies in
({1,-1}).

This note derives a translated composition law that couples four actual
positive oriented corners and their excluded slopes.

## 1. Affine-orbit discrepancy identity

First record a global identity that makes the slope multiplicities
visible. Let

\[
 F_\beta(x,y)=F(x,y)+\beta(x-y),\qquad \beta\in\mathbb F_3.
\tag{3}
\]

All corner sums (g_d) are invariant under (3). Let (Z) be their
total number of zeros. Assume every zero whose step is divisible by
three is rainbow; this is necessary for any proper affine lift. For
(3\nmid d), let

\[
 k_\beta=\#\{(p,d):g_d(p)=0,\ \sigma_d(p)=\beta\}.
\tag{4}
\]

Then (F_\beta) has exactly (k_\beta) monochromatic corners and
(Z-k_\beta) rainbow corners. The (T_{11}) line-energy identity
therefore gives

\[
 \boxed{V(F_\beta)=110-2Z+6k_\beta.}
\tag{5}
\]

In particular, a proper affine lift exists exactly when some
(k_\beta=0), and for that lift

\[
 V=110-2Z.
\tag{6}
\]

If (r) is the number of zero corners at steps divisible by three,
then summing (5) and using
(sum_\beta k_\beta=Z-r) yields

\[
 \sum_{\beta\in\mathbb F_3}V(F_\beta)=330-6r.
\tag{7}
\]

Thus, under (Z\le4), a slope-covering proof has sharply limited
possibilities. If (q=Z-r) is the number of zeros with defined slope,
then all three slopes can be excluded only when

\[
 q=3\text{ with multiplicities }(1,1,1),
 \quad\text{or}\quad
 q=4\text{ with multiplicities }(2,1,1).
\tag{8}
\]

For (q\le2), slope coverage is impossible by cardinality alone. A
complete low-zero argument must separately rule out those cases or
force additional zero corners.

## 2. A translated four-corner stencil

Write the discrete increments

\[
 \Delta_x^dF(p)=F(p+d e_x)-F(p),
 \qquad
 \Delta_y^dF(p)=F(p+d e_y)-F(p).
\]

Since (3F(p)=0), equation (1) is equivalently

\[
 g_d(p)=\Delta_x^dF(p)+\Delta_y^dF(p).
\tag{9}
\]

Suppose (d,e>0), (d+e) is available at (p), and the following
three actual corners have zero sum:

\[
 g_d(p)=0,\qquad
 g_e(p+d e_x)=0,\qquad
 g_e(p+d e_y)=0.
\tag{10}
\]

Assume (3\nmid de), and denote their slopes by

\[
 \alpha=\sigma_d(p),\qquad
 \beta_x=\sigma_e(p+d e_x),\qquad
 \beta_y=\sigma_e(p+d e_y).
\tag{11}
\]

From (2) and (9), a zero corner of slope (sigma) has increments

\[
 \Delta_x^d=-\sigma d,\qquad
 \Delta_y^d=\sigma d.
\tag{12}
\]

Telescoping the two coordinate increments from (p) to distance
(d+e) gives

\[
\begin{aligned}
 \Delta_x^{d+e}F(p)&=-\alpha d-\beta_x e,\\
 \Delta_y^{d+e}F(p)&= \alpha d+\beta_y e.
\end{aligned}
\tag{13}
\]

Consequently the outer corner satisfies the exact identity

\[
 \boxed{g_{d+e}(p)=e(\beta_y-\beta_x).}
\tag{14}
\]

This is a slope-sensitive refinement of the commuting-operator
identity: it retains the physical horizontal and vertical increments,
not only the six corner sums.

**Four-corner packet lemma.** Under (10), if the two translated
(e)-corner slopes agree,

\[
 \beta_x=\beta_y=\beta,
\tag{15}
\]

then the outer corner (g_{d+e}(p)) also vanishes. If the coloring is
proper, its outer corner is rainbow exactly when

\[
 \boxed{\alpha d=\beta e\quad\text{in }\mathbb F_3.}
\tag{16}
\]

If (16) fails, the forced outer zero is monochromatic.

**Proof.** Equation (14) proves the outer zero. Its horizontal
increment is, by (13),

\[
 -\alpha d-\beta e.
\]

A zero-sum corner is monochromatic exactly when this increment is zero.
The two quantities (alpha d) and (eta e) are nonzero elements of
(mathbb F_3); their sum is nonzero exactly when they are equal. This
is (16). \(\square\)

The residue consequences are concrete.

* If (d\equiv e\not\equiv0\pmod3), properness forces
  (alpha=eta). Here (d+e\not\equiv0), and the outer zero has the
  same excluded slope (alpha).
* If (d\equiv-e\not\equiv0\pmod3), properness forces
  (alpha=-eta). Here (3\mid d+e); the outer zero is a rainbow
  whose type is invariant under every affine lift.

Thus three zeros in the translated L-stencil (10), with equal slopes on
the two parallel translated corners, force a fourth zero and determine
the only slope relation compatible with properness.

## 3. Consequence for a four-zero candidate

Normalize a putative proper coloring with (Z\le4) so that its allowed
affine slope is (0). If it contains a stencil (10)--(15), then the
four corners in the packet exhaust the entire zero budget unless some
of them coincide.

The packet does not by itself force all three affine exclusions. In
the equal-residue case its three defined input slopes and its outer
slope are all the same after applying (16); it can contribute only one
excluded slope. In the opposite-residue case the input slopes use the
two values (1,-1), while the outer step is divisible by three; it can
contribute exactly the two nonzero exclusions and still omit the proper
slope (0).

This is an explicit obstruction to closing the theorem with one
composition stencil: a locally proper four-zero packet is compatible
with the missing-slope condition in both residue cases. A successful
argument must make two such packets overlap incompatibly, force a fifth
outer zero, or rule out configurations in which no three zeros occupy
the translated positions (10).

The exact remaining geometric question is therefore whether every
proper (S_9) signature with at most four zeros necessarily contains
enough translated-zero incidences to invoke the packet lemma twice.
No such incidence theorem is proved here. Equations (5) and (14)--(16)
are the new supported slope couplings; they do not by themselves prove
the five-rainbow lower bound.
