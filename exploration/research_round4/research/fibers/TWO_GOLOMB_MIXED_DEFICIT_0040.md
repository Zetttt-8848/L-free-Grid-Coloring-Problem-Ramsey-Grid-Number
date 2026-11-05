# The proposed two-Golomb mixed deficit is false

Let

\[
 B=\{0,2,5,6\},\qquad C=\{1,3,4,8\}.
\]

These sets are disjoint and have (b=c=4). Both are Golomb. Their positive
difference sets, with every difference occurring exactly once, are

\[
 \Delta B=\{1,2,3,4,5,6\},
 \qquad
 \Delta C=\{1,2,3,4,5,7\}.
\]

Indeed, the six differences of (B) are

\[
 2,5,6,3,4,1,
\]

and those of (C) are

\[
 2,3,7,1,5,4.
\]

For a positive distance (d), write

\[
 m_d=x_d+y_d
   =|\{(p,q)\in B\times C:|p-q|=d\}|.
\]

The sixteen mixed distances, displayed by the element of (B), are

\[
\begin{array}{c|cccc}
 p\in B & q=1&q=3&q=4&q=8\\ \hline
 0&1&3&4&8\\
 2&1&1&2&6\\
 5&4&2&1&3\\
 6&5&3&2&2
\end{array}
\]

Consequently

\[
\begin{array}{c|rrrrrrrr}
 d&1&2&3&4&5&6&7&8\\ \hline
 m_d&4&4&3&2&1&1&0&1\\
 \mathbf 1_{d\in\Delta B}+\mathbf 1_{d\in\Delta C}
     &2&2&2&2&2&1&1&0
\end{array}
\]

and hence

\[
\begin{aligned}
 N
 &=\sum_d
   (\mathbf 1_{d\in\Delta B}+\mathbf 1_{d\in\Delta C})m_d\\
 &=2(4+4+3+2+1)+1\\
 &=29.
\end{aligned}
\]

The proposed bound would give

\[
 N\le 2bc-b=2\cdot4\cdot4-4=28,
\]

so this pair is a direct counterexample.

Equivalently, measure the deficit of a mixed pair by

\[
 2-\mathbf 1_{|p-q|\in\Delta B}
  -\mathbf 1_{|p-q|\in\Delta C}.
\]

Fourteen mixed pairs have distance in
(Delta B\cap\Delta C=\{1,2,3,4,5\}) and therefore deficit zero. The pair
((2,8)), of distance (6), has deficit one, while ((0,8)), of distance
(8), has deficit two. Thus the total deficit is only

\[
 2bc-N=3<b=4.
\]

This also identifies the obstruction to a matching or ordering proof that
charges one missing incidence to every mark of the smaller ruler. All three
missing incidences are concentrated on two mixed pairs, both incident with
the single mark (8\in C); the marks (5,6\in B) meet no deficient mixed
pair at all. Disjointness, linear order, and Golomb uniqueness therefore do
not distribute the deficit across (B).

The counterexample only refutes the proposed universal estimate
(N\le2bc-b), and hence the suggested derivation of
(T(B\cup C)\le2\binom{b+c}{2}) from that estimate. It does not decide that
energy inequality by another route. Any repaired mixed-incidence bound must
allow at least the one-unit loss exhibited here, or add a hypothesis that
prevents this concentration.

Root continuation: TWO_GOLOMB_MIXED_ENERGY_0040.md proves the energy
inequality T(B union C)<=2 binom(b+c,2) by a different joint count.
It retains N<=2bc and charges Q=sum x_d y_d to the combined inventory
of distinct unordered pairs from both classes, giving
Q<=binom(b,2)+binom(c,2). Thus no repair of the refuted separate
linear deficit is needed. This example remains a valid limitation
of that separate estimate, not of the completed energy theorem.
