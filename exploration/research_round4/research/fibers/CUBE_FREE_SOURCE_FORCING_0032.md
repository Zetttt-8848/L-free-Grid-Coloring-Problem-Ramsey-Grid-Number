# A reflected cross-block forcing path in the 26-mark source

## 1. A general one-sided reflection lemma

Let \(A\) be a source for which every overlap

\[
 F_d=A\cap(A-d)=\{x:x,x+d\in A\}
\]

is Golomb. Fix

\[
 x_0<x_1<x_2\quad\hbox{in }F_d                         \tag{1}
\]

and denote the three cells on offset \(d\) by

\[
 X_i=(x_i+d,x_i)\qquad(0\le i\le2).                   \tag{2}
\]

Their pairwise corner completions are

\[
 P=(x_1+d,x_0),\quad
 Q=(x_2+d,x_0),\quad
 R=(x_2+d,x_1).                                       \tag{3}
\]

Put

\[
 w=x_0+x_2-x_1=x_0+(x_2-x_1).                         \tag{4}
\]

If \(w\in A\), then the actual cell

\[
 Z=(x_2+d,w)                                          \tag{5}
\]

exists and

\[
 \{P,Q,Z\}                                            \tag{6}
\]

is a positive oriented corner. Indeed, starting from
\(P=(x_1+d,x_0)\) and using step \(x_2-x_1>0\) produces exactly
\(Q\) and \(Z\).

Similarly, if \(w+d\in A\), then

\[
 W=(w+d,x_0)                                          \tag{7}
\]

exists and

\[
 \{W,Q,R\}                                            \tag{8}
\]

is a corner, now with step \(x_1-x_0\).

The two reflected corners cannot both exist. If \(w,w+d\in A\), then
\(w\in F_d\), and the two pairs

\[
 \{x_0,w\},\qquad\{x_1,x_2\}                         \tag{9}
\]

have the same positive difference \(x_2-x_1\). They are distinct:
equality \(w=x_1\) would make the successive gaps in (1) equal, already
contradicting the Golomb property of \(F_d\). Thus (9) would make
\(F_d\) non-Golomb. We have proved:

**One-sided reflection lemma.** For three starts (1), at most one of
the support marks \(w,w+d\) can occur. Each one that occurs creates the
corresponding reflected corner (6) or (8).

This has a direct color consequence. If

\[
 z(X_0)=z(X_1)=z(X_2)=c,                              \tag{10}
\]

then their three completion corners force

\[
 z(P)=z(Q)=z(R)=1-c.                                  \tag{11}
\]

Hence (6), when present, forces \(z(Z)=c\), and (8), when present,
forces \(z(W)=c\). A one-sided reflected corner therefore copies a
monochromatic diagonal triple onto a cell in a different completion
block. This is an equality propagation mechanism, rather than a
difference-constant coloring assumption.

## 2. A concrete reflected path in the reduced source

Use the source

\[
\begin{split}
 A=\{&0,4,5,15,19,20,24,29,32,37,44,48,58,59,62,65,\\
     &66,67,69,76,82,91,92,96,114,124\}.
\end{split}                                            \tag{12}
\]

Take

\[
 d=76,\qquad (x_0,x_1,x_2)=(0,15,20).                 \tag{13}
\]

The six endpoint marks \(0,15,20,76,91,96\) belong to \(A\), so the
three offset-\(76\) cells are

\[
 X_0=(76,0),\qquad X_1=(91,15),\qquad X_2=(96,20).    \tag{14}
\]

Their three actual completions are

\[
 P=(91,0),\qquad Q=(96,0),\qquad R=(96,15).            \tag{15}
\]

Here the reflected mark (4) is

\[
 w=0+20-15=5\in A,                                    \tag{16}
\]

whereas \(w+d=81\notin A\). Thus precisely the first reflection in
the lemma is available, giving

\[
 Z=(96,5)                                              \tag{17}
\]

and the four actual corners

\[
\begin{array}{lll}
 \{(76,0),(91,0),(91,15)\},\\
 \{(76,0),(96,0),(96,20)\},\\
 \{(91,15),(96,15),(96,20)\},\\
 \{(91,0),(96,0),(96,5)\}.
\end{array}                                            \tag{18}
\]

All cells in (18) are positively oriented. The first three corners are
three different completion blocks with endpoint offset \(76\); the
last has endpoint offset \(91\) and output offset \(96\). Therefore
(18) joins distinct blocks exactly as follows:

\[
 z(76,0)=z(91,15)=z(96,20)=c
 \quad\Longrightarrow\quad
 z(96,5)=c.                                            \tag{19}
\]

The missing mirror cell would be \((81,0)\). Its absence is not an
accident of the forcing calculation: adjoining the mark \(81=5+76\)
would place both pairs \(\{0,5\}\) and \(\{15,20\}\) of gap five in
\(F_{76}\), violating cube-freeness.

## 3. Four blocks that can conflict with the copied color

The copied cell \(Z=(96,5)\) is itself the physical output of the four
actual completion blocks

\[
\begin{array}{c|c}
 \text{endpoint offset}&\text{two endpoint cells}\ \hline
 14&(19,5),\ (96,82),\\
 27&(32,5),\ (96,69),\\
 64&(69,5),\ (96,32),\\
 77&(82,5),\ (96,19).
\end{array}                                            \tag{20}
\]

Consequently (19) yields a concrete cross-block conflict as soon as
one row of (20) has both endpoint cells colored \(c\). That block would
force \(z(Z)=1-c\), while the reflected path (18) forces
\(z(Z)=c\).

Equivalently, every proper coloring satisfying the monochromatic seed
hypothesis in (19) must obey all four restrictions

\[
\begin{aligned}
 &\neg[z(19,5)=z(96,82)=c],\\
 &\neg[z(32,5)=z(96,69)=c],\\
 &\neg[z(69,5)=z(96,32)=c],\\
 &\neg[z(82,5)=z(96,19)=c].                           \tag{21}
\end{aligned}
\]

Thus the lead contains an explicit four-corner equality repeater feeding
a four-block fan at one physical output.

## 4. Exact remaining forcing gap

The local mechanism is conditional in two places. First, the three
cells in (14) are not forced monochromatic by the corners in (18).
Second, conditional on their common color, the four endpoint pairs in
(20) are disjoint at the cell level and can each satisfy (21) by placing
the opposite color on at least one endpoint. Other corners of the source
couple those choices, but no short symbolic chain forcing one complete
pair in (20) to color \(c\) is derived here.

Accordingly, (18)-(21) are not a proof that (12) is uncolorable. They
isolate a precise local route that would prove a conflict: force the
offset-\(76\) seed triple monochromatic and force one of the four pairs
in (20) to that same color. The one-sided reflection lemma also explains
why the obvious mirror closure is unavailable in any cube-free source;
a successful completion must route through further distinct outputs.
