# A common-outer-cell switch across a source separator (checkpoint 0018)

Let \(A=B\sqcup C\) with \(B<C\), and let
\[
V(A)=\{(y,x):x,y\in A,\ x<y\}
\]
have a proper two-coloring \(z:V(A)\to\{-1,+1\}\). For cells \(P,R\), write
\[
\operatorname{Eq}(P,R)=\frac{1+z(P)z(R)}2.
\]

A source quadruple
\[
u<b<c<v,\qquad u+v=b+c \tag{1}
\]
supplies the cells
\[
\begin{array}{lll}
\alpha=(b,u),&\beta=(v,c),&Q=(v,u),\\
X=(c,u),&Y=(v,b),&Z=(c,b).
\end{array} \tag{2}
\]
The two repeated-difference corners give
\[
\operatorname{NAE}(\alpha,\beta,Q),
\qquad
\operatorname{NAE}(X,Y,Q). \tag{3}
\]
The inner cell \(Z\) is part of the full source triangle but is not used in either corner in (3).

## 1. The common-completion identity

The following elementary form of a two-color NAE constraint will be used repeatedly.

**Lemma.** Suppose \(S,T,Q\) are signs with \(\operatorname{NAE}(S,T,Q)\). Put
\[
e=\frac{1+ST}{2}.
\]
Then
\[
Q(S+T)=-2e. \tag{4}
\]
Equivalently:

- if \(S\ne T\), then \(e=0\) and \(S+T=0\);
- if \(S=T\), then \(e=1\) and \(S=T=-Q\).

Indeed, the sign-product form of NAE is
\[
ST+QT+QS=-1.
\]
Adding \(1\) and using \(1+ST=2e\) gives (4).

Now fix outer marks \(u<v\), hence a fixed outer cell
\[
Q=(v,u).
\]
Let \(\mathcal R_Q\) be any collection of inner pairs \((b_i,c_i)\) satisfying
\[
u<b_i<c_i<v,\qquad b_i+c_i=u+v. \tag{5}
\]
For each \(i\), define the two endpoint pairs
\[
(\alpha_i,\beta_i)=((b_i,u),(v,c_i)),
\qquad
(X_i,Y_i)=((c_i,u),(v,b_i)). \tag{6}
\]
Every one of these pairs has the same completion \(Q\). Index the resulting \(2|\mathcal R_Q|\) pairs by \(p\), writing a pair as \((S_p,T_p)\), and put
\[
q=z(Q),\qquad
e_p=\operatorname{Eq}(S_p,T_p).
\]
Applying (4) to every pair gives the exact **common-outer-cell fan identity**
\[
\boxed{
q\sum_p\bigl(z(S_p)+z(T_p)\bigr)
  =-2\sum_p e_p.
} \tag{7}
\]
In particular, every monochromatic endpoint pair in the fan has color \(-q\). Monochromatic child pairs from different source quadruples cannot have opposite colors.

## 2. A two-quad quadratic switch

Take two distinct inner pairs in (5). After relabeling, their six source marks have the order
\[
u<b_1<b_2<c_2<c_1<v,
\qquad b_1+c_1=b_2+c_2=u+v. \tag{8}
\]
Choose any two endpoint pairs completed by \(Q\), for example the two child pairs
\[
(\alpha_1,\beta_1),\qquad(\alpha_2,\beta_2).
\]
If both are monochromatic, the lemma forces all four endpoint cells to have color \(-q\). Therefore
\[
\operatorname{Eq}(\alpha_1,\beta_1)
+\operatorname{Eq}(\alpha_2,\beta_2)
-\operatorname{Eq}(\alpha_1,\alpha_2)
\le1. \tag{9}
\]
In signed form this is the small quadratic inequality
\[
\boxed{
z(\alpha_1)z(\beta_1)
+z(\alpha_2)z(\beta_2)
-z(\alpha_1)z(\alpha_2)
\le1.
} \tag{10}
\]
The same statement holds if either child pair is replaced by its cross-support pair \((X_i,Y_i)\), and either endpoint of each pair may be used in the final equality term.

There is useful geometry behind the displayed choice. All representatives
\[
\alpha_i=(b_i,u),\qquad X_i=(c_i,u) \tag{11}
\]
lie on the single source column \(u\), while all partners
\[
\beta_i=(v,c_i),\qquad Y_i=(v,b_i) \tag{12}
\]
lie on the single source row \(v\). Thus (9) converts two monochromatic completed pairs into an equal-color pair on an actual source line.

More generally, let
\[
H_Q=\sum_p e_p
\]
be the number of monochromatic endpoint pairs among the child and cross-support pairs in the fan. Since all representatives of those \(H_Q\) pairs have color \(-q\),
\[
\boxed{
\binom{H_Q}{2}
\le
\sum_{p<p'}\operatorname{Eq}(S_p,S_{p'}).
} \tag{13}
\]
With the representatives chosen as in (11), the right side counts equal-color pairs entirely on column \(u\). One may instead use (12) and charge them to row \(v\).

Equations (7), (10), and (13) retain the child colors. They provide a local mechanism for summing source-quadruple contributions by their common outer cell: repeated monochromatic contributions create quadratic congestion on a single source line. This is the type of term absent from a count that treats the two triangular children and the cross rectangle independently.

## 3. Why the standalone binary strip does not satisfy this bridge

In the Cartesian cut \(B<C\), the cells \(X_i,Y_i,Q\) lie in the cross rectangle \(C\times B\), but
\[
\alpha_i\in V(B),\qquad \beta_i\in V(C). \tag{14}
\]
A standalone Cartesian strip contains the first triple and therefore enforces
\(\operatorname{NAE}(X_i,Y_i,Q)\). It contains neither child edge in (14), so it has no constraint
\(\operatorname{NAE}(\alpha_i,\beta_i,Q)\).

For example, two absent child pairs could be assigned opposite monochromatic signs,
\[
z(\alpha_1)=z(\beta_1)=+1,\qquad
z(\alpha_2)=z(\beta_2)=-1,
\]
without changing any strip cell. This assignment violates (10), because its left side is \(3\). A full source forbids it through the common completion \(Q\). Hence (10) is a genuine source-separator compatibility rule and is invisible to the binary-strip construction.

## 4. The same-inner-cell limitation

If two source quadruples share the inner cell \(Z=(c,b)\), their outer endpoints can be written
\[
u_i=b-p_i,\qquad v_i=c+p_i,\qquad p_i>0.
\]
Their mandatory corner pairs are completed by different cells
\[
Q_i=(v_i,u_i).
\]
The shared cell \(Z\) occurs in neither of the two NAE constraints in (3). Therefore the common-completion argument above gives no analogous rule from these constraints alone: one child pair may be monochromatic \(+1\), with \(Q_1=-1\), while another is monochromatic \(-1\), with \(Q_2=+1\); choosing each cross-support pair bichromatic satisfies all four displayed NAE constraints, and \(Z\) remains free.

Additional source corners supported by further coincidences among the marks may couple such a same-\(Z\) family, but shared \(Z\) by itself does not. The reusable unconditional result of this note is consequently the common-\(Q\) fan rule (7)--(13). Turning its line congestion into a global bound for \(U\) or \(2U+V\) requires a separate amortization over the shared source rows and columns.
