# Ordered Q-constraints on one mixed offset

Let \(B,C\subset\mathbb Z\) be disjoint Golomb diagonal classes in a proper
weak source. Fix \(d>0\), and define the two orientation sets of mixed cells
at offset \(d\):

\[
 X_d=\{u\in B:u+d\in C\},\qquad
 Y_d=\{v\in C:v+d\in B\}.                            \tag{1}
\]

Write \(x_u\) for the cell \((u+d,u)\), \(u\in X_d\), and \(y_v\) for
\((v+d,v)\), \(v\in Y_d\). Their starts are all distinct because
\(B\cap C=\varnothing\).

## 1. The ordered bipartite Q-graph

For \(u\in X_d\), \(v\in Y_d\), the two mixed cells have opposite
orientations. If \(u<v\), their completion \((v+d,u)\) is a \(B\)-to-\(B\)
cell of fixed color \(C\). If \(v<u\), their completion \((u+d,v)\) is a
\(C\)-to-\(C\) cell of fixed color \(B\). Thus the complete Q-system at
offset \(d\) is

\[
\begin{array}{c|c|c}
\text{order}&\text{forbidden endpoint colors}&\text{binary clause}\\ \hline
u<v&(C,C)&x_u=B\ \text{or}\ y_v=B,\\
v<u&(B,B)&x_u=C\ \text{or}\ y_v=C.
\end{array}                                           \tag{2}
\]

This is a signed complete bipartite graph whose sign is determined solely by
the order of its two starts.

## 2. Exact threshold characterization

For a full assignment, split the starts into

\[
 X_B,X_C\subseteq X_d,\qquad Y_B,Y_C\subseteq Y_d
\]

according to their actual cell colors. Then (2) is satisfied if and only if

\[
 \boxed{
 \max Y_C<\min X_C,\qquad
 \max X_B<\min Y_B.
 }                                                     \tag{3}
\]

Empty sets use the evident infinite conventions. Indeed, two \(C\)-colored
opposite-orientation cells are allowed exactly when the \(Y\)-start lies to
the left of the \(X\)-start. Likewise, two \(B\)-colored cells are allowed
exactly when the \(X\)-start lies to the left of the \(Y\)-start. Mixed
colors always satisfy the Q-clause.

Equivalently, every allowable assignment admits two real cuts
\(\tau_B,\tau_C\), chosen away from all starts, such that

\[
\begin{array}{c|cc}
&B\text{ is allowed}&C\text{ is allowed}\\ \hline
x_u,\ u\in X_d&u<\tau_B&u>\tau_C\\
y_v,\ v\in Y_d&v>\tau_B&v<\tau_C.
\end{array}                                           \tag{4}
\]

Every vertex must have at least one allowed color, so

\[
 X_d\subset(-\infty,\tau_B)\cup(\tau_C,\infty),
\qquad
 Y_d\subset(-\infty,\tau_C)\cup(\tau_B,\infty).       \tag{5}
\]

This is also a complete extension test after reflection units or N-forest
propagation have fixed some colors. If the prescribed sets are
\(X_B^0,X_C^0,Y_B^0,Y_C^0\), a Q-extension exists exactly when cuts can be
chosen satisfying (5) and

\[
 \max X_B^0<\tau_B<\min Y_B^0,\qquad
 \max Y_C^0<\tau_C<\min X_C^0.                       \tag{6}
\]

Once such cuts are chosen, every unprescribed vertex may independently take
any color allowed by (4). Conversely, cuts placed between the extrema in
(3) certify every full extension. Hence (5)--(6) are necessary and
sufficient, rather than merely propagation rules.

The equivalent ray implications are

\[
\begin{array}{ll}
x_u=C\Longrightarrow y_v=B&\text{for every }v>u,\\
x_u=B\Longrightarrow y_v=C&\text{for every }v<u,\\
y_v=C\Longrightarrow x_u=B&\text{for every }u<v,\\
y_v=B\Longrightarrow x_u=C&\text{for every }u>v.
\end{array}                                           \tag{7}
\]

For example, prescribed \(X_C\)-starts on the left and prescribed
\(X_B\)-starts on the right are incompatible precisely when \(Y_d\) meets
the open interval between the earliest such \(X_C\)-start and the latest
such \(X_B\)-start after the ray implications close. The cut test performs
the full closure without choosing a propagation order.

## 3. Interface with the forward N-forests

Every vertex in this Q-layer has interval weight \(d\). An N-forest
successor, when it exists, has strictly larger weight. Thus Q-edges are
horizontal links between equal-weight states, while N-edges route states
outward to unsupported sinks.

In a fixed actual coloring, a Q-clause has one active implication exactly
when its endpoint colors differ. If they agree in the permitted order, no
actual literal forces the other. Consequently the exact number of active
Q-links at offset \(d\) is

\[
 R_d=|X_B||Y_C|+|X_C||Y_B|.                           \tag{8}
\]

Summing over offsets gives the explicit global term

\[
 \boxed{
 R_Q(z)=\sum_{d>0}
 \bigl(|X_{d,B}||Y_{d,C}|+|X_{d,C}||Y_{d,B}|\bigr).
 }                                                     \tag{9}
\]

It counts active logical implications rather than all
\(\sum_d|X_d||Y_d|\) Q-corners. Same-color Q-pairs account for the remaining
corners and are certified by the threshold orders in (3).

For each mixed vertex \(v\), follow its actual N-forest path to its sink
\(\sigma(v)\), and let \(p(v)\in\{0,1\}\) be the path length modulo two.
Every N-edge reverses color, so

\[
 \operatorname{col}(v)
 =\operatorname{col}(\sigma(v))\oplus p(v).           \tag{10}
\]

Contracting the N-forest paths sends each active Q-link \(vw\) to a signed
edge between \(\sigma(v)\) and \(\sigma(w)\), with exact condition

\[
 \operatorname{col}(\sigma(v))\oplus
 \operatorname{col}(\sigma(w))
 =1\oplus p(v)\oplus p(w).                            \tag{11}
\]

Loops are impossible under this contraction. An N-parent enlarges an
interval by moving one endpoint outward, so every N-path preserves the mixed
orientation (B<C) or (C<B). Every Q-link joins opposite orientations;
its two endpoints therefore drain to distinct sinks of opposite orientation.
The contracted Q-graph is bipartite by sink orientation. Equation (11)
retains the exact sign on each such nonloop edge. Thus an unsupported N-sink
is terminal for N-propagation but need not be isolated in the full binary
system: Q-links couple its basin to opposite-orientation sink basins at the
same initial weight.

The threshold cuts also constrain which layer vertices can themselves be
sinks. A \(B\)-colored vertex of weight \(d\) is an N-sink exactly when
\(d\notin\Delta C\), and a \(C\)-colored vertex is a sink exactly when
\(d\notin\Delta B\). Therefore:

* if \(d\in\Delta B\setminus\Delta C\), all layer sinks are \(B\)-colored;
  their \(X\)-starts lie on the left side of the \(B\)-cut and their
  \(Y\)-starts on the right;
* if \(d\in\Delta C\setminus\Delta B\), all layer sinks are \(C\)-colored;
  their \(Y\)-starts lie on the left side of the \(C\)-cut and their
  \(X\)-starts on the right;
* if \(d\) lies in neither difference set, every layer vertex is already an
  N-sink, and (3) is the complete constraint on those sink colors;
* if \(d\) lies in both difference sets, no vertex of this layer is an
  N-sink, so every state routes outward before Q-links are contracted.

## 4. Scope of the interface

The two-cut theorem is exact for the Q-clauses at one offset and for any
partial colors supplied by units or N-propagation. Equations (9)--(11) give
an exact global interface with the unsupported forward sinks.

The contraction has no loops and is bipartite by sink orientation. The
two-cut theorem alone does not bound the multiplicity of signed edges between
two opposite-orientation sink basins. Many equal-weight vertices can drain to
one unsupported sink, and the threshold theorem controls their start order
rather than their basin sizes. A separate interval-forest capacity estimate
is needed to bound that contraction multiplicity; none is asserted here.
