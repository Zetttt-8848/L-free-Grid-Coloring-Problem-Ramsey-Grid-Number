# The completion-incidence cut of one source band (checkpoint 0021)

Let \(A\) be a finite integer source with
\[
M=\binom{|A|}{2},
\qquad
F_d=\{x:x,x+d\in A\},
\qquad
r_d=|F_d|,
\]
and suppose that \(V(A)\) has a proper coloring
\(z:V(A)\to\{-1,+1\}\). Fix the band
\[
I_H=\{d:H\le d<2H\},
\]
and put
\[
T_H=\sum_{d\in I_H}\binom{r_d}{2},
\qquad
R_H=\sum_{d\in I_H}r_d. \tag{1}
\]

This note keeps the actual completion color of every band corner. The
result is an exact cut and operator formulation of the band energy. It
does not use the boundary-translate closure route.

## 1. Pointwise output linearization

Fix an outer cell
\[
Q=(v,u),\qquad q=z(Q).
\]
For every \(d\in I_H\) such that
\[
u+d\in A,\qquad v-d\in A,\qquad u<v-d,
\]
the two parallel boundary cells
\[
P_d=(u+d,u),\qquad R_d=(v,v-d) \tag{2}
\]
form a corner with completion \(Q\). Write their signs as \(p_d,r_d'\),
and put
\[
e_{Q,d}=\frac{1+p_dr_d'}2.
\]
The NAE identity is
\[
p_dr_d'+q(p_d+r_d')=-1,
\]
so
\[
\boxed{
\frac{p_d+r_d'}2=-q\,e_{Q,d}.
} \tag{3}
\]
Thus a bichromatic parallel pair contributes zero to the boundary sum,
while a monochromatic pair contributes exactly \(-q\).

Let \(\mathcal K_H\) be the linear completion operator on cell-sign
vectors defined by
\[
(\mathcal K_H z)_Q
=\frac12
\sum_{\substack{d\in I_H\\
                 u+d,v-d\in A\\
                 u<v-d}}
\bigl[z(u+d,u)+z(v,v-d)\bigr]. \tag{4}
\]
If \(H_Q\) is the number of monochromatic active parallel pairs completed
by \(Q\), then summing (3) gives the pointwise relation
\[
\boxed{
(\mathcal K_Hz)_Q=-z(Q)H_Q.
} \tag{5}
\]
In particular,
\[
\|\mathcal K_Hz\|_1=\sum_QH_Q,
\qquad
\|\mathcal K_Hz\|_2^2=\sum_QH_Q^2. \tag{6}
\]
The sign in (5) retains information that is absent after merely
eliminating \(Q\).

For example, if a source parallelogram has boundary signs \(a,b,c,d\) in
its two parallel pairs and common completion sign \(q\), then
\[
q(a+b)=-2e_1,\qquad q(c+d)=-2e_2,
\]
and hence
\[
(a+b)(c+d)=4e_1e_2\ge0. \tag{7}
\]
The usual no-alternating-boundary condition is only the product
consequence (7); equation (5) keeps the one shared output sign across
all parallelograms completed by \(Q\).

## 2. The completion-incidence graph

Define an undirected graph \(\Gamma_H(A)\) whose vertices are the \(M\)
cells of \(V(A)\). For every active-band corner with parallel endpoints
\(P,R\) and completion \(Q\), add the two edges
\[
\{Q,P\},\qquad\{Q,R\}. \tag{8}
\]

These physical pair edges are all distinct. Indeed, if \(Q=(v,u)\) and
\(P=(w,u)\) share column \(u\), then their rows determine the corner step
\(v-w\) and its third cell uniquely. If they share row \(v\), their
columns determine the corner uniquely. Moreover the completion has
strictly larger offset \(y-x\) than either parallel endpoint, so the two
roles cannot be reversed. Consequently,
\[
|E(\Gamma_H)|=2T_H. \tag{9}
\]

Let \(C_H\) be the number of edges of \(\Gamma_H\) crossing the actual
two-color cut. A band corner contributes:

- two cut edges when its parallel endpoints are monochromatic, because
  \(Q\) has the opposite color;
- one cut edge when its parallel endpoints are bichromatic, because
  \(Q\) agrees with exactly one endpoint.

Let
\[
A_H=\sum_QH_Q
\]
be the number of band corners of the first type. The preceding
classification gives the exact identities
\[
\boxed{
C_H=T_H+A_H,
\qquad
2T_H-C_H=T_H-A_H.
} \tag{10}
\]
Thus the cut edges record the actual output forcing, while the uncut
edges record the bichromatic parallel pairs.

If \(\mathscr L_H\) and \(\mathscr Q_H\) are respectively the Laplacian
and signless Laplacian of \(\Gamma_H\), then (10) is equivalently
\[
\boxed{
z^{\mathsf T}\mathscr L_Hz=4(T_H+A_H),
\qquad
z^{\mathsf T}\mathscr Q_Hz=4(T_H-A_H).
} \tag{11}
\]
Equation (5) gives the companion nonsymmetric form
\[
\boxed{
A_H=-\langle z,\mathcal K_Hz\rangle.
} \tag{12}
\]
All three formulas use one global sign variable for each physical
completion cell, even when that cell completes corners from several
active offsets.

## 3. An explicit graph budget sufficient for \(D(7/5)\)

For \(d\in I_H\), let \(a_d,b_d\) be the two color-class sizes in
\(F_d\). The monochromatic parallel-pair count in that fiber is
\[
A_d=\binom{a_d}{2}+\binom{b_d}{2}.
\]
Since
\[
a_db_d-A_d
=\frac{r_d-(a_d-b_d)^2}{2}
\le\frac{r_d}{2},
\]
we have
\[
T_H\le2A_H+\frac{R_H}{2}. \tag{13}
\]
Substitute \(A_H=C_H-T_H\) from (10). This yields the new cut form
\[
\boxed{
T_H\le\frac23C_H+\frac16R_H.
} \tag{14}
\]

It follows that the desired band estimate
\[
T_H\le\frac75M \tag{15}
\]
would follow from the concrete actual-color cut bound
\[
\boxed{
C_H\le\frac{21}{10}M-\frac14R_H.
} \tag{16}
\]
Since \(R_H\le M\), the uniform estimate
\[
C_H\le\frac{37}{20}M \tag{17}
\]
is a simpler sufficient condition. In graph language, (17) asks that
the opposite-color completion-incidence graph have average degree at
most \(37/10\).

There is also a spectral sufficient form. By (11), condition (16) is
\[
z^{\mathsf T}\mathscr L_Hz
\le\frac{42}{5}M-R_H. \tag{18}
\]
In particular,
\[
\lambda_{\max}(\mathscr L_H)\le\frac{37}{5} \tag{19}
\]
would imply (17), hence (15). The full eigenvalue condition (19) is
stronger than needed: (18) concerns only the actual proper source
coloring vector.

## 4. Ordered geometry retained by the graph

Every incidence edge in (8) joins an active endpoint cell of offset
\(d\in[H,2H)\) to a completion cell of offset
\[
d+s>d,
\]
where \(s\) is the separation of the two starts in \(F_d\). Orienting
each graph edge from the completion to the endpoint therefore strictly
decreases the cell offset. Completions of offset at least \(2H\) lie
above the active band and can never serve as active endpoints in
\(\Gamma_H\); completions still inside the band have a strictly larger
rank than their endpoints.

When one source parallelogram has both leg lengths \(d,e\in I_H\), its
two active corners give four incidence edges sharing the outer cell of
offset
\[
d+e\ge2H.
\]
Its inner cross cell has offset
\[
|d-e|<H.
\]
Thus the common outer and inner cells lie on opposite sides of the
active scale. The graph records the outer output and all four boundary
cells. The inner cell is not inserted artificially, because neither
original NAE constraint contains it.

## 5. Precise remaining limitation

Pair-edge uniqueness and strict offset descent do not alone prove
(16). An ordered acyclic orientation can still have a high-degree
completion star, and if all its active boundary neighbors have the
opposite color, every incident graph edge belongs to the cut while all
corresponding corners remain proper. The no-alternating condition (7)
does not prevent this: it says only that monochromatic boundary pairs at
one completion use a common sign, which is already encoded by (5).

Accordingly, the missing statement is now a graph inequality about the
actual source realization, not an independent Cartesian bound:
one must show that a cut subgraph of \(\Gamma_H(A)\) with more than
\[
\frac{21}{10}M-\frac14R_H
\]
edges forces additional source-corner constraints among its repeatedly
used boundary vertices or its higher-rank completion vertices.
Equations (14), (16), and (18) are exact targets for such an argument.
The present derivation does not establish that cut bound and therefore
does not prove \(D(7/5)\).
