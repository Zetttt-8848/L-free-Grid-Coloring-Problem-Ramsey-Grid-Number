# Reflection shadows can have unbounded reuse

There is no absolute reuse bound for one hole, even when both diagonal
classes are Golomb and the entire weak source is properly colored. The
following family gives arbitrarily many distinct opposite-color outputs whose
lower shadow sets all contain the same missing mark.

Fix integers (m\ge1) and (N\ge10). For (1\le i\le m), put

\[
 h_i=N^{2i},\qquad k_i=N^{2i+1}=Nh_i,
\]

and define the five-mark gadget

\[
 G_i=\{-h_i,\ k_i-h_i,\ k_i,\ 2k_i,\ 2k_i+h_i\}.
\]

Let the two diagonal classes be

\[
 B=\bigcup_{i=1}^m
   \{-h_i,\ k_i-h_i,\ 2k_i,\ 2k_i+h_i\},
 \qquad
 C=\{k_i:1\le i\le m\},                              \tag{1}
\]

and put (S=B\sqcup C). The mark (0) does not belong to (S).

## 1. Difference separation

Within one gadget, abbreviate (h=h_i), (k=k_i), and write

\[
 a=-h,quad b=k-h,quad r=k,quad c=2k,quad e=2k+h.
\]

Since (k>2h>0), their order is

\[
 a<b<r<c<e.
\]

The ten positive differences within this gadget are

\[
\begin{array}{c|c}
\text{difference}&\text{representing pairs}\ \hline
h&(b,r),(c,e)\\
k&(a,b),(r,c)\\
k+h&(a,r),(b,c),(r,e)\\
2k+h&(a,c)\\
2k+2h&(a,e)\\
k+2h&(b,e).
\end{array}                                           \tag{2}
\]

Thus the four (B)-marks in a gadget are Golomb.

The powers of (N) ensure that no unwanted equality of differences occurs
between gadgets. One direct way to see this is to retain (k_i) and (h_i)
as separate formal coordinates. Every gadget mark has coefficient vector

\[
 (0,-1),(1,-1),(1,0),(2,0),(2,1)
\]

in its own ((k_i,h_i))-plane. Inspection shows that the only nontrivial
formal repeated differences are the three rows (h_i,k_i,k_i+h_i) in (2).
A difference involving two distinct gadget planes determines both of its
endpoints from its two nonzero coordinate blocks.

After substituting (h_i=N^{2i}), (k_i=N^{2i+1}), an accidental numerical
equality of two differences would give a nonzero base-(N) relation whose
coefficients have magnitude at most four. Its highest term dominates all
lower terms because (N\ge10). Hence no formal distinctions collapse.
It follows that:

* (B) is Golomb;
* (C=\{N^{2i+1}}) is Golomb;
* every positive difference involving distinct gadgets occurs only once in
  the full source (S);
* the only positive fibers of (S) with at least two cells are exactly the
  three local fibers displayed in (2).

## 2. A proper weak coloring

Color every diagonal mark of (B) blue and every diagonal mark of (C)
red. Color an off-diagonal cell according to the diagonal classes of its two
source marks:

\[
 z(v,u)=
 \begin{cases}
 \text{red},&u,v\in B,\\
 \text{blue},&u,v\in C,\\
 \text{blue},&\text{one of }u,v\text{ lies in each class}.
 \end{cases}                                          \tag{3}
\]

Every offset-zero corner is proper: equal blue diagonal endpoints in (B)
have a red completion, equal red diagonal endpoints in (C) have a blue
completion, and mixed diagonal endpoints already differ.

Every cross-gadget positive fiber has only one cell, so it supports no
corner. It remains only to inspect the three repeated fibers of one gadget.
Using the start of an offset cell to identify it, their endpoint colors are

\[
\begin{array}{c|c|c}
\text{offset}&\text{cells}&\text{colors}\ \hline
h&(r,b),(e,c)&\text{blue},\text{red}\\
k&(b,a),(c,r)&\text{red},\text{blue}\\
k+h&(r,a),(c,b),(e,r)&\text{blue},\text{red},\text{blue}.
\end{array}                                           \tag{4}
\]

The first two fibers have differently colored endpoints. In the last fiber,
the only equal-color endpoint pair is ((r,a),(e,r)); its completion is
((e,a)), a (B)-to-(B) cell colored red. Thus every positive corner is
proper. Equations (3)--(4) prove directly that (W(S)) is properly colored.

## 3. One hole reused by every output

For the output (r_i=k_i\in C), the class (B) contains the two reflection
triples

\[
 (-h_i,\ k_i-h_i,\ 2k_i),
 \qquad
 (k_i-h_i,\ 2k_i,\ 2k_i+h_i).                       \tag{5}
\]

Both have reflection output (k_i):

\[
 -h_i+2k_i-(k_i-h_i)=k_i,
\]

\[
 (k_i-h_i)+(2k_i+h_i)-2k_i=k_i.
\]

The difference separation above excludes any further reflection triple at
this output, so (mu_B(k_i)=2). Its lower extreme and upper extreme sets are

\[
 A_B(k_i)=\{-h_i,k_i-h_i\},
 \qquad
 Q_B(k_i)=\{2k_i,2k_i+h_i\}.
\]

Therefore

\[
 k_i-\Delta A_B(k_i)=\{k_i-k_i\}=\{0\},             \tag{6}
\]

while the upper shadow is

\[
 k_i+\Delta Q_B(k_i)=\{k_i+h_i\}.                   \tag{7}
\]

In particular,

\[
 0\in H_B(k_i)\qquad(1\le i\le m),                  \tag{8}
\]

and (0\notin S). The same missing source mark is consequently reused by
all (m) distinct outputs in the opposite diagonal class. Since (m) is
arbitrary, shadow-overlap multiplicity is unbounded under the actual proper
weak-coloring hypothesis.

The construction does not weaken the ordered hole-output injection: the
charges ((0,k_i)) remain distinct ordered pairs. It shows precisely why an
expansion argument cannot replace those ordered pairs by bare holes with a
constant loss. Any global improvement must retain the output coordinate or
impose an additional restriction tying different output gadgets together.
