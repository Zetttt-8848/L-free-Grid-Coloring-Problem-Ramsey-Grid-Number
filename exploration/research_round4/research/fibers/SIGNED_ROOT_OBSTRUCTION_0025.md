# Signed-root obstruction: the exact one-fiber limitation at rank four

## 1. Source and dissociation

Let
\[
 A_4=\{\sigma w_i+\tau w_j:1\le i<j\le4,\ \sigma,\tau\in\{\pm1\}\},
\]
where
\[
w_i=D+9^i,
\qquad D=3H/4,
\qquad H>8\sum_{i=1}^4 9^i.
\]
It is useful to label a mark by its signed coordinate vector
\(\sigma e_i+\tau e_j\). The numerical map from the coordinate vectors is
dissociated for all relations used below. Indeed, a putative equality of two
absolute differences gives
\[
 \sum_i c_iw_i=0,
 \qquad |c_i|\le4.
\]
If \(C=\sum_i c_i\ne0\), the term \(CD\) has magnitude at least \(3H/4\),
whereas \(|\sum_i c_i9^i|<H/2\). If \(C=0\), the largest nonzero base-nine
term dominates all lower terms because
\[
 9^j>4\sum_{i<j}9^i.
\]
Thus every \(c_i\) vanishes. Consequently, equalities of distances among the
marks can be checked directly in the free coordinate lattice, up to reversing
the sign of the whole difference.

For \(d>0\), let
\[
 F_d=\{x\in A_4:x+d\in A_4\},
 \qquad p_d(x)=z(x+d,x).
\]
The question is whether properness of the source triangle can be contradicted
inside one of these diagonals. The following lemma is the exact consequence
available from one diagonal alone.

## 2. Every diagonal color class must be Golomb

**Diagonal Golomb lemma.** In a proper two-coloring, for every \(d>0\), each
color class of the map \(x\mapsto p_d(x)\) on \(F_d\) is a Golomb set.

To prove this, suppose one color \(c\) contains two distinct pairs
\[
 x,x+s\in F_d,
 \qquad y,y+s\in F_d,
 \qquad s>0.
\]
Exchange the pairs if necessary so that \(x<y\). The corner made by
\(p_d(x),p_d(x+s)\) forces
\[
 p_{d+s}(x)=z(x+d+s,x)=-c,
\]
and the pair at \(y\) similarly forces \(p_{d+s}(y)=-c\). These two cells now
force
\[
 z(y+d+s,x)=c.
\]
But the original cells \(p_d(x)\) and \(p_d(y+s)\), both of color \(c\), have
the same completion \(z(y+d+s,x)\) and force its color to be \(-c\). This is a
contradiction.

Hence a one-fiber obstruction is exactly a failure to partition \(F_d\) into
two Golomb sets. This criterion proves the elementary high-rank capacity
obstruction, but at rank four every fiber passes it.

## 3. Complete rank-four fiber census

Subtracting two signed two-atom roots gives, up to negating the whole vector,
one of the following coefficient types. The table also gives the number of
positive numerical difference fibers and the size of each start set.

\[
\begin{array}{c|c|c}
\text{coefficient type}&\text{number of positive fibers}&|F_d|\\ \hline
(1,1)&12&8\\
(2)&4&6\\
(1,1,1,1)&8&6\\
(2,1,1)&48&2\\
(2,2)&12&1
\end{array}
\]

For example, a root direction has eight representations: after signed
relabeling, for \(d=w_i-w_j\),
\[
 F_d=(w_j+C)\cup(-w_i+C),
 \qquad C=\{\pm w_k,\pm w_l\},
 \qquad \{i,j,k,l\}=[4].
\]
A vector \(2e_i\) has the six representations obtained by choosing one of the
three other axes and either sign. A four-coordinate \((\pm1)^4\) vector has
six representations, one for each choice of the two coordinates assigned to
the upper root. The remaining coefficient types visibly have two and one
representations. Counting signed vectors up to global negation gives the
middle column, and the five rows total all \(84\) positive difference fibers.

## 4. Explicit two-Golomb partitions of every type

Fibers of size one or two are immediate. The two six-point types also admit
uniform partitions.

- For a \((2)\)-fiber, translate its starts to
  \[
  \{\pm e_j:j\ne i\}.
  \]
  Put the three positive axes in one class and the three negative axes in the
  other. Within either class every difference has a distinct signed support,
  so both classes are Golomb.

- For a \((1,1,1,1)\)-fiber, translate and sign the coordinates so that the
  starts are the six two-subsets of \([4]\). Color the three subsets containing
  coordinate \(1\) with one color and the three not containing it with the
  other. Differences within the first class are the distinct exchanges among
  coordinates \(2,3,4\); the same is true in the second class. Both are
  Golomb.

It remains to treat the eight-point exchange fiber. After translation write
\[
 F=\{\pm a,\pm b,G\pm a,G\pm b\},
 \qquad G=e_i+e_j,quad a=e_k,quad b=e_l.
\]
The following partition works:
\[
 R=\{-b,-a,a,G-b,G+b\},
 \qquad
 B=\{b,G-a,G+a\}.
\tag{1}
\]
Up to sign, the ten differences inside \(R\) have coordinate vectors
\[
\begin{gathered}
a-b, a+b, G, G+2b, 2a,\\
G+a-b, G+a+b, G-a-b, G-a+b, 2b.
\end{gathered}
\]
They are pairwise distinct by the dissociation in Section 1. The three
differences inside \(B\) are
\[
 G-a-b,qquad G+a-b,qquad 2a,
\]
and are likewise distinct. Thus both classes in (1) are Golomb.

This gives a symbolic two-Golomb partition for every one of the five fiber
types. In particular, neither the exchange fiber nor any other single
difference fiber can supply the rank-four obstruction.

## 5. The exact compatibility still missing

The partitions above cannot be selected independently. Fix a completion cell
\[
 Q=z(v,u),\qquad u<v.
\]
Every \(d>0\) for which
\[
 u,u+d,v-d,v\in A_4,
 qquad u<v-d,
\]
gives a corner with endpoint cells
\[
 p_d(u)=z(u+d,u),
 \qquad p_d(v-d)=z(v,v-d).
\]
Properness says
\[
 p_d(u)=p_d(v-d)quad\Longrightarrow\quad
 p_d(u)=p_d(v-d)=-Q.
\tag{2}
\]
Consequently, if two different directions \(d,e\) give monochromatic endpoint
pairs at the same \(Q\), their common colors must agree. Equivalently, a single
completion can never receive a red monochromatic pair from one diagonal and a
blue monochromatic pair from another. This common-completion coherence is the
first condition that genuinely couples the locally feasible Golomb
partitions.

Antipodal symmetry of \(A_4\) does not close this gap by itself: reflection
sends \(z(v,u)\) to \(z(-u,-v)\), but properness imposes no equality or
inequality between those two colors. Likewise, completions of pairs in an
exchange fiber generally leave the exchange-cell family, so the exchange
variables do not form a closed forcing subsystem.

Thus the bounded one-fiber route has a precise endpoint. A direct rank-four
proof must show that the \(84\) locally two-Golomb diagonals cannot be chosen
so that (2) is coherent at every shared completion, or must add a further
weak-triangle identity that links a completion to its antipodal reflection.
The explicit partitions above show why the existing exchange-fiber capacity
argument alone cannot provide that step.

