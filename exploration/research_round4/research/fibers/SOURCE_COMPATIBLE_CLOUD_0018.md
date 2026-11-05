# A source-compatible support-cloud inequality

## 1. Geometry of one anchored cloud

Let (A=B\sqcup C) with every element of (B) smaller than every element of (C), and let (z(v,u)\in\{\pm1\}) be one proper coloring of the strict source (V(A)).

Fix (u\in B), (c\in C), and write

\[
p=(c,u),\qquad \sigma=z(p).
\]

For (d>0) with (u+d\in B) and (c+d\in C), define the two internal child cells

\[
a_d=(u+d,u)\in V(B),
\qquad
b_d=(c+d,c)\in V(C),
\]

the outer cross cell

\[
x_d=(c+d,u),
\]

and the translated cross support

\[
q_d=(c+d,u+d).
\]

Consider the offsets whose two child cells have the color of the anchored support:

\[
G=G(u,c)=\{d:z(a_d)=z(b_d)=\sigma\}.
\tag{1}
\]

For every (d\in G), the corner (a_d,x_d,b_d), whose step is (c-u), forces

\[
z(x_d)=-\sigma.
\tag{2}
\]

The step-(d) corner (p,x_d,q_d) is therefore supported by (p).  These are precisely the same-color child coincidences that can pile onto the one fixed cross support (p).

Partition them according to the translated-support color:

\[
G_\tau=\{d\in G:z(q_d)=\tau\},
\qquad \tau\in\{+1,-1\},
\]

and put (k_\tau=|G_\tau|), (k=k_++k_-).

## 2. Pairwise child payment lemma

**Lemma.**  If (d<e) belong to the same (G_\tau), then at least one of

\[
A_{d,e}=(u+e,u+d)\in V(B),
\qquad
B_{d,e}=(c+e,c+d)\in V(C)
\tag{3}
\]

has color (	au).

**Proof.**  The cells (q_d,q_e) lie on the same numerical diagonal and both have color (	au).  Their step-((e-d)) completion is

\[
r_{d,e}=(c+e,u+d).
\]

Properness of the corner (q_d,r_{d,e},q_e) forces

\[
z(r_{d,e})=-\tau.
\tag{4}
\]

Now (A_{d,e},r_{d,e},B_{d,e}) is a corner of step (c-u).  If both child cells in (3) had color (-\tau), this corner would be monochromatic by (4).  Hence at least one has color (	au).  \(\square\)

Define the actual child-color payment counts

\[
\begin{aligned}
\Pi^B_\tau(u,c)
&=\sum_{\substack{d<e\\d,e\in G_\tau}}
\mathbf 1_{\{z(A_{d,e})=\tau\}},\\
\Pi^C_\tau(u,c)
&=\sum_{\substack{d<e\\d,e\in G_\tau}}
\mathbf 1_{\{z(B_{d,e})=\tau\}}.
\end{aligned}
\tag{5}
\]

The lemma gives the finite inequality

\[
{k_\tau\choose2}
\le
\Pi^B_\tau(u,c)+\Pi^C_\tau(u,c).
\tag{6}
\]

This uses the colors in the two internal source triangles (V(B)) and (V(C)); it has no analogue for a standalone Cartesian coloring.

There is also a signed-Golomb refinement.  For fixed (	au), all differences (e-d) arising from pairs in (G_\tau) are distinct.  Indeed, the (q_d) form one signed color class on the cross diagonal (v-u=c-u), and that class is Golomb.  Hence the payer cells in (3) selected by (6) occupy distinct child difference fibers within this anchored ((u,c,\tau))-cloud.

## 3. A linear repeated-load inequality

Let

\[
W(u,c)=\mathbf 1_{\{k_+>0\text{ and }k_->0\}}.
\tag{7}
\]

The elementary two-bin inequality

\[
(k-1)_+
\le
{k_+\choose2}+{k_-\choose2}+W(u,c)
\tag{8}
\]

is exact in the small balanced cases that lose one unit from the quadratic terms.  To see it, if only one bin is occupied then ({k\choose2}\ge k-1).  If both are occupied, writing (k_+=a\ge1), (k_-=b\ge1), the right side minus (k-1) is

\[
{a\choose2}+{b\choose2}+1-(a+b-1)
=
\frac{(a-1)(a-2)+(b-1)(b-2)}2\ge0.
\]

Combining (6) and (8) proves the local support-cloud bound

\[
\boxed{
(|G(u,c)|-1)_+
\le
W(u,c)
+\sum_{\tau\in\{\pm1\}}
\bigl(\Pi^B_\tau(u,c)+\Pi^C_\tau(u,c)\bigr).
}
\tag{9}
\]

Thus the first offset charging (p) is free.  Every further offset is paid either by the single bit saying that both translated-support colors occur, or by an explicitly identified internal child cell of the required color.  A weaker version without the switch bit is

\[
(|G(u,c)|-2)_+
\le
\sum_\tau(\Pi^B_\tau+\Pi^C_\tau).
\tag{10}
\]

## 4. What remains after summing clouds

Summing (9) over all cross supports (p=(c,u)) gives

\[
\sum_{u\in B,c\in C}(|G(u,c)|-1)_+
\le
\sum_{u,c}W(u,c)
+\sum_{u,c,\tau}
\bigl(\Pi^B_\tau(u,c)+\Pi^C_\tau(u,c)\bigr).
\tag{11}
\]

The left side is the repeated load from same-color child coincidences whose common color agrees with the anchored cross support.  The first term on the right retains one genuine color-switch statistic per cloud.  The second term is a child-color budget, but it is presently counted with multiplicity.

That multiplicity is the exact obstruction to a global linear estimate.  For example, a fixed (B)-child cell ((v,u')) can occur as (A_{d,e}) for different anchors (u<u') and different (c\in C): one has (d=u'-u) and (e=v-u), while the conditions (c+d,c+e\in C) select translated copies in (C).  Signed-Golomb uniqueness makes the gap (e-d=v-u') occur at most once inside any one fixed signed cloud, but it does not prevent the same physical child cell from paying clouds with different anchors.

Equivalently, define

\[
\mu^B_\tau(v,u')
=\#\{(u,c): (v,u')\text{ is selected in (5) as a (B)-payer of sign }\tau\},
\tag{12}
\]

and analogously (mu^C_\tau).  Then the final term of (11) is exactly

\[
\sum_{(v,u')\in V(B)}\mu^B_{z(v,u')}(v,u')
+
\sum_{(v,u')\in V(C)}\mu^C_{z(v,u')}(v,u').
\tag{13}
\]

A source-level all-cloud inequality now needs to bound (13), together with the switch term in (11), by an available internal-corner or child-color budget.  The local geometry alone does not give a constant bound on (mu): different anchors use different translated copies even though their payer is the same cell.

## 5. Scope

Inequality (9) is the completed local mechanism.  It couples repeated cross-support load to the actual shared coloring on (V(B)\cup V(C)), and it uses only legal equal-step corners.  It does not by itself bound (U) or (2U+V), because the child-payment multiplicities in (13) remain unamortized.  The exact next requirement is a global estimate for those multiplicities, with the retained switch statistic (W), from the internal source corner budget.
