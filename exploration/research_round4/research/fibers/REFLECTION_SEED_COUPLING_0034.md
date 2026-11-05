# Coupling reflected seeds at the cell \((96,5)\)

## 1. Four transports with one completion triangle

Work in the source

\[
\begin{split}
 A=\{&0,4,5,15,19,20,24,29,32,37,44,48,58,59,62,65,\\
     &66,67,69,76,82,91,92,96,114,124\}.
\end{split}                                            \tag{1}
\]

Set

\[
 P=(91,0),\qquad Q=(96,0),\qquad Z=(96,5).             \tag{2}
\]

For each

\[
 d\in D:=\{29,59,67,76\},                             \tag{3}
\]

the three starts

\[
 0<91-d<96-d                                           \tag{4}
\]

belong to \(F_d\). Denote their offset-\(d\) cells by

\[
 S_d={A_d,B_d,C_d\}
 =\{(d,0),(91,91-d),(96,96-d)\}.                       \tag{5}
\]

Explicitly,

\[
\begin{array}{c|ccc}
d&A_d&B_d&C_d\\ \hline
29&(29,0)&(91,62)&(96,67)\\
59&(59,0)&(91,32)&(96,37)\\
67&(67,0)&(91,24)&(96,29)\\
76&(76,0)&(91,15)&(96,20).
\end{array}                                            \tag{6}
\]

Each reflected triple uses the following three-corner pattern, sharing
the intermediate cells P,Q and the last corner:

\[
 \{A_d,P,B_d\},\qquad
 \{A_d,Q,C_d\},\qquad
 \{P,Q,Z\}.                                           \tag{7}
\]

The first two corner identities follow from
\(d+(91-d)=91\) and \(d+(96-d)=96\). For the reflected corner,

\[
 0+(96-d)-(91-d)=5,                                   \tag{8}
\]

so the reflected mark is the same actual mark \(5\) for every
\(d\in D\).

If all three cells of \(S_d\) have color \(c_d\), the first two
corners in (7) force

\[
 z(P)=z(Q)=1-c_d,
\]

and the last forces

\[
 z(Z)=c_d.                                            \tag{labsync}
\]

This proves the following unconditional exclusion, valid in every
proper coloring of the source:

\[
 \boxed{\text{Any two monochromatic triples among the four }S_d
 \text{ have the same color.}}                         \tag{9}
\]

Equivalently, no pair \(S_d,S_{d'}\) can be monochromatic in opposite
colors. This is stronger than saying merely that two transports have a
common target: they also share both intermediate completions \(P,Q\).
If at least one \(S_d\) is monochromatic, its color determines all three
cells in (2), with \(P,Q\) opposite and \(Z\) equal to that seed.

## 2. A transport crossing two blocks of the \(Z\)-fan

There is a second reflected transport based on offset \(27\). Its
three seed cells are

\[
 U_0=(32,5),\qquad U_1=(59,32),\qquad U_2=(96,69),     \tag{10}
\]

corresponding to the starts

\[
 5<32<69\quad\hbox{in }F_{27}.                         \tag{11}
\]

Here

\[
 w=5+69-32=42,\qquad w+27=69\in A,                    \tag{12}
\]

so the row-oriented reflected transport is supported. Put

\[
 V=(69,5),\qquad R=(96,32).                            \tag{13}
\]

The three corners needed for this transport are

\[
 \{U_0,Z,U_2\},\qquad
 \{U_1,R,U_2\},\qquad
 \{V,Z,R\}.                                          \tag{14}
\]

If

\[
 z(U_0)=z(U_1)=z(U_2)=t,                              \tag{15}
\]

then the first two corners in (14) give

\[
 z(Z)=z(R)=1-t,
\]

and the reflected corner gives

\[
 z(V)=t.                                              \tag{16}
\]

The first corner in (14) is exactly the endpoint-offset-\(27\) block
with output \(Z\). The last corner is the endpoint-offset-\(64\) block
with the same output \(Z\), because

\[
 \operatorname{offset}(V)=\operatorname{offset}(R)=64.
\]

Thus a monochromatic reflected seed containing both endpoints of the
offset-\(27\) block does not make the next block monochromatic. It
forces its two endpoints to opposite colors:

\[
 \boxed{z(V)=t,\qquad z(R)=1-t.}                       \tag{17}
\]

This is a complete two-block transport relation on actual cells.

## 3. Composition with the original offset-76 seed

The seed singled out in `CUBE_FREE_SOURCE_FORCING_0032.md` is

\[
 S_{76}=\{(76,0),(91,15),(96,20)\}.                   \tag{18}
\]

Suppose it is monochromatic of color \(c\). By (7),

\[
 z(P)=z(Q)=1-c,\qquad z(Z)=c.                          \tag{19}
\]

If the offset-\(27\) seed (10) is also monochromatic, its color \(t\)
is no longer free: the first corner in (14), or equivalently (16) and
(19), forces

\[
 t=1-c.                                               \tag{20}
\]

Substitution into (17) gives the fully determined endpoint colors

\[
 \boxed{
 z(69,5)=1-c,\qquad z(96,32)=c.}                       \tag{21}
\]

These are the two endpoints of the offset-\(64\) block at \(Z\). Hence
the composition of the two transports makes that endpoint pair
bichromatic. It satisfies the block automatically instead of creating
a color conflict.

The conclusion (20)-(21) is an unconditional implication between two
explicit seed patterns: whenever both triples (18) and (10) are
monochromatic, their colors are opposite and the offset-\(64\) pair is
split in the displayed order.

## 4. The shortest unresolved pattern in this transport family

The synchronization rule (9) excludes opposite monochromatic colors
among four actual seed triples, but it does not force any one of them
to be monochromatic. Each triple may use both colors. Likewise, the
crossing transport (10) is conditional on all three of its seed cells
having one color.

After assuming the original seed (18) has color \(c\), the target
\(Z\) has color \(c\). A contradiction still requires one endpoint
pair at \(Z\) to be entirely color \(c\). The only reflected transport
among the displayed cells that contains a whole such pair is (10): it
contains the offset-\(27\) pair \(U_0,U_2\). If that transport fires,
(20)-(21) show that it routes the opposite color into the offset-\(64\)
pair and leaves that pair split. Thus this shortest two-transport
composition cannot close the conflict.

The remaining local pattern is now precise. One needs either

1. an actual corner chain forcing one of the four triples (6), in
   particular (18), to be monochromatic; or
2. conditional on (18), a chain forcing both endpoints of one of the
   offset-\(14,27,64,77\) blocks at \(Z\) to color \(c\).

The five transports above impose (9) and (20)-(21), but neither condition
1 nor condition 2. No claim that the full source is uncolorable follows
from this bounded family alone; further routing through a different
physical output is required.
