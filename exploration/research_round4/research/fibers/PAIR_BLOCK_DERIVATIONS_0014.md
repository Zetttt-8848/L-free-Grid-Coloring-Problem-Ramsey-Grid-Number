# Three two-start pair-potential block inequalities

This note derives only the three blocks left open in the bounded request:

\[
B_{1,6}\ge 5,\qquad B_{1,7}\ge 3,\qquad B_{2,6}\ge 5.
\tag{1}
\]

The other listed blocks are owned by the root derivation and are not repeated
here.  The coefficients below come from
`PAIR_POTENTIAL_CANDIDATE_0014.json` by multiplying every recorded fraction
by 5, placing it with positive sign at its reference factor and negative sign
at its other factor, and combining coefficients belonging to the same
physical pair.  The targets in (1) are 5 times the corresponding
normalization fractions.

## 1. Common two-start geometry

For one block `B_{d,e}`, write the three signs at a start `z` as

\[
(L_z,Q_z,R_z)=(\ell_z,q_z,r_z).
\]

Each of the three blocks in (1) has exactly two starts `x<y`, and its six
cells are distinct:

\[
\begin{array}{c|c|c}
\text{block}&(x,y)&e-d\\ \hline
B_{1,6}&(1,2)&5\\
B_{1,7}&(0,1)&6\\
B_{2,6}&(0,2)&4.
\end{array}
\tag{2}
\]

Put

\[
(\ell,q,r)=(L_x,Q_x,R_x),\qquad
(\ell',q',r')=(L_y,Q_y,R_y).
\]

For a proper corner, fixing `q=s` in `{−1,+1}` leaves exactly the three
types from the admissible-block definition:

\[
\begin{array}{c|ccc}
\text{type}&\ell&q&r\\ \hline
J_s&-s&s&-s\\
C_s&s&s&-s\\
R_s&-s&s&s.
\end{array}
\tag{3}
\]

Indeed these are exactly the three ways for a sign triple to be
nonmonochromatic, classified by its outer sign `q=s`.

Let `T,U` in `{J,C,R}` be the types at `x,y`, and put

\[
\rho=q q'\in\{-1,+1\}.
\tag{4}
\]

All potentials under consideration contain only pair products, so global
sign reversal changes no value.  We may therefore take `q=+1`, after
which `q'=rho`.  Thus `(T,U,rho)` determines all six signs up to the
irrelevant global reversal.

There are only two forbidden type triples.  The case
`(T,U,rho)=(J,J,+1)` would put both starts in `J_+`, contrary to
`|J_+|<=1`.  The case `(R,C,+1)` violates ordered routing: its row
pair at `x`, column pair at `y`, and outer pair `{Q_x,Q_y}` are all
equal-sign pairs, whereas

\[
X_{\rm row}(x)+X_{\rm col}(y)+X_{\rm diag}(Q_x,Q_y)\le2.
\tag{5}
\]

The remaining `18-2=16` triples are the complete admissible state list for
these two disjoint corners, modulo global reversal.

## 2. The three integer potentials

After combining physical-pair coefficients, the block potentials are

\[
\begin{aligned}
\Phi_{16}={}&
 3\ell\ell'-4\ell q-3\ell r+2\ell r'+\ell'r
 -4\ell'q'-2\ell'r'-4qr-4q'r',\\[2mm]
\Phi_{17}={}&
 -\ell\ell'-2\ell q-\ell r+2\ell r'
 -3\ell'q'-4\ell'r'-3qr+qq'+2rr'-4q'r',\\[2mm]
\Phi_{26}={}&
 \ell\ell'-3\ell q-3\ell r+\ell r'
 -3\ell'q'-2\ell'r'-3qr-3q'r'.
\end{aligned}
\tag{6}
\]

Here the subscripts indicate `B_{1,6},B_{1,7},B_{2,6}`, respectively.
No cell copy has been split: every variable in (6) is the sign of one
physical cell in its block.

## 3. Complete algebraic cases

Substitute (3) into (6), taking `q=+1` and `q'=rho`.  The table gives
the three excesses over the targets in (1).  A minus or plus in the third
column means `rho=-1` or `rho=+1`.

\[
\begin{array}{cc|c|ccc}
T&U&\rho&\Phi_{16}-5&\Phi_{17}-3&\Phi_{26}-5\\ \hline
J&J&-&0&0&0\\
J&C&-&4&0&0\\
J&C&+&0&12&0\\
J&R&-&0&8&0\\
J&R&+&4&0&0\\
C&J&-&8&0&4\\
C&J&+&0&4&0\\
C&C&-&0&4&0\\
C&C&+&0&4&0\\
C&R&-&0&0&0\\
C&R&+&0&4&0\\
R&J&-&0&0&0\\
R&J&+&8&0&4\\
R&C&-&0&0&0\\
R&R&-&0&0&0\\
R&R&+&0&0&0
\end{array}
\tag{7}
\]

For illustration, the row `(J,C,-)` substitutes

\[
(\ell,q,r)=(-1,1,-1),\qquad
(\ell',q',r')=(-1,-1,1)
\]

into (6), giving excesses `(4,0,0)`.  Every other row is the same direct
pair-product substitution.  The omitted triples `(J,J,+)` and
`(R,C,+)` are precisely the two inadmissible cases identified above, so
the table is complete.

Every entry in (7) is nonnegative.  Therefore every admissible state of the
three blocks satisfies

\[
\boxed{\Phi_{16}\ge5,\qquad \Phi_{17}\ge3,\qquad \Phi_{26}\ge5.}
\tag{8}
\]

These are local block inequalities only.  Their combination with the other
factor bounds and the global ordered-completion budget remains with the root
argument.
