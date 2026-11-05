# A nonconstant proper coloring of a cube-free two-layer source

## 1. The source and the coloring

Let
\[
B=\{0,1,3,4\},
\qquad
C=\{0,1,4,5\},
\qquad
A=B\cup(Q+C),
\]
where \(Q>20\). The marks occur in the order
\[
0<1<3<4<Q<Q+1<Q+4<Q+5.
\]

The following table gives a color \(z(v,u)\in\{0,1\}\) for every strict
cell \(u<v\). Each row is indexed by its lower mark \(u\); the entries list
the colors at the successive upper marks shown in the middle column.

\[
\begin{array}{c|c|c}
u&v\text{ in order}&z(v,u)\text{ in the same order}\\ \hline
0&1,3,4,Q,Q+1,Q+4,Q+5&0,1,1,1,0,0,1\\
1&3,4,Q,Q+1,Q+4,Q+5&0,0,0,1,1,0\\
3&4,Q,Q+1,Q+4,Q+5&1,1,0,1,0\\
4&Q,Q+1,Q+4,Q+5&0,0,0,0\\
Q&Q+1,Q+4,Q+5&1,1,0\\
Q+1&Q+4,Q+5&0,0\\
Q+4&Q+5&0.
\end{array}
\tag{1}
\]

The coloring is deliberately not constant on numerical differences. That
freedom is necessary here: a difference-constant coloring is contradicted by
the two four-point rectangles in \(B\) and \(C\). The remainder of the note
proves directly that (1) is proper for every \(Q>20\).

Here is the precise difference-constant contradiction. Write \(\gamma_d\)
for the proposed common color of every cell of offset \(d\). In the
rectangle on \(B\), the two source corners have offset patterns
\((1,4,1)\) and \((3,4,3)\). Properness forces
\(\gamma_1=\gamma_3\ne\gamma_4\). In the rectangle on \(Q+C\),
the patterns are \((1,5,1)\) and \((4,5,4)\). They force
\(\gamma_1=\gamma_4\ne\gamma_5\). These requirements contradict
each other in two colors. Thus a theorem that first canonicalizes every
proper source coloring to a function of the numerical difference would
fail even on this explicit family.

## 2. Complete no-carry fiber classification

All same-layer differences are at most \(5\). A cross-layer difference is
\(Q+\delta\), where \(\delta=c-b\) with \(b\in B,c\in C\), so
\(-4\le\delta\le5\). Since \(Q>20\), the two ranges are disjoint, and equality
of cross differences is exactly equality of \(\delta\).

The complete list of nonempty positive-difference start sets is
\[
\begin{array}{c|c@{\qquad}c|c}
d&F_d&d&F_d\\ \hline
1&\{0,3,Q,Q+4\}&Q-4&\{4\}\\
2&\{1\}&Q-3&\{3,4\}\\
3&\{0,1,Q+1\}&Q-2&\{3\}\\
4&\{0,Q,Q+1\}&Q-1&\{1\}\\
5&\{Q\}&Q&\{0,1,4\}\\
&&Q+1&\{0,3,4\}\\
&&Q+2&\{3\}\\
&&Q+3&\{1\}\\
&&Q+4&\{0,1\}\\
&&Q+5&\{0\}.
\end{array}
\tag{2}
\]
The right half of (2) retains every signed displacement \(\delta\), including
the negative values. Fibers not displayed are empty.

Only seven fibers have at least two starts and hence supply corners:
\[
d=1,3,4,Q-3,Q,Q+1,Q+4.
\]
Their respective numbers of corners are
\[
6,3,3,1,3,3,1,
\]
for a total of twenty.

## 3. Symbolic corner check

For starts \(x<y\) in \(F_d\), record the corner colors in the order
\[
\bigl(z(x+d,x),\ z(y+d,x),\ z(y+d,y)\bigr).
\tag{3}
\]
Reading (1) gives the following complete list.

\[
\begin{array}{c|c|c}
d&\{x,y\}&\text{colors in (3)}\\ \hline
1&\{0,3\}&(0,1,1)\\
 &\{0,Q\}&(0,0,1)\\
 &\{0,Q+4\}&(0,1,0)\\
 &\{3,Q\}&(1,0,1)\\
 &\{3,Q+4\}&(1,0,0)\\
 &\{Q,Q+4\}&(1,0,0)\\ \hline
3&\{0,1\}&(1,1,0)\\
 &\{0,Q+1\}&(1,0,0)\\
 &\{1,Q+1\}&(0,1,0)\\ \hline
4&\{0,Q\}&(1,0,1)\\
 &\{0,Q+1\}&(1,1,0)\\
 &\{Q,Q+1\}&(1,0,0)\\ \hline
Q-3&\{3,4\}&(1,0,0)\\ \hline
Q&\{0,1\}&(1,0,1)\\
 &\{0,4\}&(1,0,0)\\
 &\{1,4\}&(1,1,0)\\ \hline
Q+1&\{0,3\}&(0,0,1)\\
 &\{0,4\}&(0,1,0)\\
 &\{3,4\}&(1,0,0)\\ \hline
Q+4&\{0,1\}&(0,1,0).
\end{array}
\tag{4}
\]

Every row of (4) contains both colors. By (2), the table exhausts all corners,
so (1) is a proper two-coloring of the full strict source triangle \(V(A)\)
for every \(Q>20\).

## 4. Every overlap \(F_d\) is Golomb

Singleton and two-point start sets in (2) are automatically Golomb. The five
larger sets have the following positive internal differences:
\[
\begin{array}{c|c}
F_1=\{0,3,Q,Q+4\}
&3,\ Q,\ Q+4,\ Q-3,\ Q+1,\ 4\\
F_3=\{0,1,Q+1\}
&1,\ Q+1,\ Q\\
F_4=\{0,Q,Q+1\}
&Q,\ Q+1,\ 1\\
F_Q=\{0,1,4\}
&1,\ 4,\ 3\\
F_{Q+1}=\{0,3,4\}
&3,\ 4,\ 1.
\end{array}
\tag{5}
\]
Within each row the listed values are distinct when \(Q>20\). Thus every
nonempty \(F_d\), including every signed cross-layer overlap, is Golomb.

Consequently this same family is cube-free in the three-generator sense: an
additive cube would put a parallelogram, hence two equal-gap pairs, inside one
of the sets \(F_d\). The example therefore shows concretely that local
Golombness is compatible with a proper coloring whose cells vary inside a
single numerical-difference fiber; difference-constant colorings miss this
behavior.
