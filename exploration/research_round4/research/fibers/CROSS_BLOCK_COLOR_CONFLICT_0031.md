# Cross-block color conflict in a cube-free source

## 1. Two blocks at one physical output

Let \(A\) be a finite integer source and write

\[
 z(v,u)\in\{0,1\},\qquad u<v,
\]

for the color of its actual cell. Fix an output cell

\[
 q=(u+e,u),\qquad e>0.                                 \tag{1}
\]

For an endpoint offset \(0<d<e\), the only possible corner of block
\((d,e)\) having output \(q\) is

\[
 K_d(q)=\{L_d,q,R_d\},                                 \tag{2}
\]

where

\[
 L_d=(u+d,u),
 \qquad
 R_d=(u+e,u+e-d).                                     \tag{3}
\]

All four coordinates in (3) must of course belong to the source. If
every overlap \(F_d=A\cap(A-d)\) is Golomb, then a block indexed only
by \((d,e)\) contains at most one corner: its two starts have prescribed
gap \(e-d\), and two such start-pairs would repeat that gap in \(F_d\).

For two offsets \(d\ne f\), the blocks \(K_d(q),K_f(q)\) give the
immediate conditional conflict

\[
 z(L_d)=z(R_d)=c,\qquad
 z(L_f)=z(R_f)=1-c.                                   \tag{4}
\]

Indeed, properness of \(K_d(q)\) forces \(z(q)=1-c\), while properness
of \(K_f(q)\) forces \(z(q)=c\). The issue is to make the two endpoint
equalities and their opposite signs unavoidable using other actual
corners.

## 2. A six-corner equality core

The following linear three-uniform gadget forces three signal cells to
have one color. Let the signals be \(s_1,s_2,s_3\), introduce four
private cells \(a,b,c,d\), and require the six corner constraints

\[
\begin{array}{lll}
 \{s_1,a,b\},&\{s_1,c,d\},&\{s_2,a,c\},\\
 \{s_2,b,d\},&\{s_3,a,d\},&\{s_3,b,c\}.
\end{array}                                            \tag{5}
\]

Every displayed triple is required to be nonmonochromatic. These are
the seven lines of the Fano plane with the line
\(\{s_1,s_2,s_3\}\) deleted.

To see directly that (5) forces

\[
 z(s_1)=z(s_2)=z(s_3),                                 \tag{6}
\]

suppose instead that the signal triple were nonmonochromatic. Adding it
to (5) would give a proper two-coloring of all seven Fano lines. Such a
coloring does not exist. In any coloring, one color occupies at least
four points. If those four contain a line, that line is monochromatic.
If they contain no line, their six pairs lie on six distinct Fano lines;
the seventh line avoids all four points and is monochromatic in the
other color. This proves (6).

The core itself is consistent: color all three signals alike and all
four private cells oppositely. Each edge in (5) then has one signal and
two private cells. Also, none of the three signal pairs occurs in (5),
so each remains available for one actual corner without violating the
unique-pair property of source corners.

## 3. The smallest concrete symbolic conflict isolated here

Attach the three unused signal pairs as follows. Introduce cells
\(p,q,r\) and the four additional corners

\[
 \{s_1,s_2,q\},\qquad
 \{s_1,s_3,p\},\qquad
 \{s_2,s_3,r\},\qquad
 \{p,q,r\}.                                           \tag{7}
\]

Equations (5)-(6) give a color \(c_0\) common to the three signals.
The first three corners in (7) force

\[
 z(p)=z(q)=z(r)=1-c_0,
\]

making the last corner monochromatic. Thus (5) and (7) form an explicit
ten-corner symbolic obstruction.

It has the desired two-block interpretation: the first corner in (7)
is one completion block with output \(q\), and the last is a different
completion block with the same physical output. The middle two corners
route the equality (6) to the two endpoints \(p,r\) of the second block.
Consequently the first block forces \(q=1-c_0\), while the second would
force \(q=c_0\).

No absolute minimality among all NAE gadgets is claimed. The point of
(5)-(7) is that it is a small linear motif with a complete pencil-and-paper
forcing derivation and with all three signal pairs used exactly once.

## 4. Positive oriented realization of the four-corner shell

The color logic above is not yet a source motif. Its four-corner shell
(7) must occur with the rigid row, column, and diagonal incidences of
actual positive cells. That requirement exposes a precise obstruction.

Assume without loss of generality that the first block has the smaller
endpoint offset,

\[
 0<d<f<e.
\]

Take

\[
 s_1=L_d,\quad s_2=R_d,\quad p=L_f,\quad r=R_f          \tag{8}
\]

in the notation (3). The pair \(s_1,p\) shares column \(u\). If it is
to lie in a corner whose third cell is \(s_3\), positivity and the
corner orientation uniquely force

\[
 s_3=(u+f,u+f-d).                                     \tag{9}
\]

Likewise, \(s_2,r\) shares row \(u+e\). Its unique third cell is

\[
 s'_3=(u+e-f+d,u+e-f).                                \tag{10}
\]

The two routing corners in (7) share one physical cell precisely when
\(s_3=s'_3\). Equating either coordinate in (9)-(10) gives

\[
 e=2f-d.                                              \tag{11}
\]

Put \(g=f-d>0\). Under (11), the six cells of the shell are

\[
\begin{array}{lll}
 s_1=(u+d,u),&p=(u+d+g,u),&q=(u+d+2g,u),\\
 s_3=(u+d+g,u+g),&r=(u+d+2g,u+g),&
 s_2=(u+d+2g,u+2g).
\end{array}                                            \tag{12}
\]

All are positively oriented. But the three signal cells

\[
 s_1, s_3, s_2
\]

have common offset \(d\) and starts

\[
 u,\quad u+g,\quad u+2g.                              \tag{13}
\]

Thus \(F_d\) contains two distinct pairs with the same gap \(g\). It
is not Golomb. Equivalently, the six source marks supporting (12) form
the two translated three-term progressions generated by \(d\) and
\(g\), which is exactly the local additive-cube configuration.

If \(f<d\), the same calculation with the blocks exchanged puts the
three-term progression in \(F_f\). Therefore:

**Shell lemma.** If two distinct completion blocks share an output and
their like-side endpoints are joined through one common third cell as
in (7), then the overlap fiber of the smaller endpoint offset is not
Golomb.

## 5. Exact remaining gap

The ten-corner hypergraph (5)-(7) is an unconditional symbolic color
conflict, but its direct four-corner cross-block shell is excluded by
cube-freeness before colors are considered. The failure is geometric,
not logical: sharing the same bridge cell in the column link and row
link forces the arithmetic relation (11), and hence the repeated gap
(13).

A realizable cube-free conflict must therefore replace at least one of
the two direct routing corners in (7) by a longer equality route through
additional outputs. That route must force the endpoint colors while
avoiding a common bridge cell whose two line completions create a
three-term progression in one endpoint fiber. No such longer positive
oriented route is derived here, and no global cube-free source bound is
claimed.
