# Cross-scale majority transport on \(S_9\)

Let
\[
g_d=D_dF,\qquad D_d=1+X^d+Y^d
\]
for \(F:S_9\to\mathbb F_3\). The Frobenius chains by themselves admit the
zero-free sign pattern recorded in
`FROBENIUS_SIGN_STENCILS_0045.md`. This note adds one
full-domain consequence of the common-\(F\) compatibility and follows it
through two overlapping packets.

## 1. Cross-scale majority transport

Operator commutation gives
\[
D_2g_3=D_3g_2
\]
on the full common base domain \(S_4\). Thus, for every \(p\in S_4\),
\[
\boxed{
g_3(p)+g_3(p+2e_x)+g_3(p+2e_y)
=g_2(p)+g_2(p+3e_x)+g_2(p+3e_y).
}                                                   \tag{1}
\]
This is genuinely additional to the separate identities
\(g_3=D_1^2g_1\) and \(g_6=D_2^2g_2\).

When the three entries of a triple are nonzero, define its sign type by
\[
\theta(a,b,c)=a+b+c\in\mathbb F_3.
\]
For signs in \(\{1,-1\}\), type \(0\) means unanimous, type \(1\) means
two \(+1\)'s, and type \(-1\) means one \(+1\). Therefore (1) proves:

**Cross-scale majority lemma.** If the six entries in (1) are nonzero,
then the \(g_3\)-triple at step \(2\) and the \(g_2\)-triple at step \(3\)
have the same sign type.

No properness assumption beyond nonvanishing is used. In a low-zero proper
lift, the lemma applies to every packet avoiding the zero set.

## 2. Two-packet cancellation

For \(p\in S_2\), write (1) both at \(p\) and at \(p+2e_x\). The two
left sides share the actual corner sum \(g_3(p+2e_x)\). Subtracting the
identities cancels it and gives
\[
\begin{aligned}
&g_3(p)+g_3(p+2e_y)
 -g_3(p+4e_x)-g_3(p+2e_x+2e_y)\\
={}&g_2(p)+g_2(p+3e_x)+g_2(p+3e_y)\\
&-g_2(p+2e_x)-g_2(p+5e_x)-g_2(p+2e_x+3e_y).
\end{aligned}                                      \tag{2}
\]
Every displayed \(g_3\)-base lies in \(S_6\), and every displayed
\(g_2\)-base lies in \(S_7\); \(p\in S_2\) is the exact common domain.

Let \(\Theta_2(q)\) denote the sum of the three \(g_2\) entries on the
right side of (1) based at \(q\). Equation (2) has the following
sign-level consequence.

**Overlapping-packet balance lemma.** Suppose all entries in the two
packets based at \(p,p+2e_x\) are nonzero. If
\[
\Theta_2(p)=\Theta_2(p+2e_x),                      \tag{3}
\]
then
\[
g_3(p)+g_3(p+2e_y)
=g_3(p+4e_x)+g_3(p+2e_x+2e_y).                    \tag{4}
\]
For two signs, their sum in \(\mathbb F_3\) uniquely determines whether
they contain zero, one, or two \(+1\)'s. Hence the two exterior pairs in
(4) have exactly the same number of positive signs.

There is an identical statement in the \(e_y\) direction. There is also
a transverse version: subtract (1) at \(p+2e_x\) and \(p+2e_y\). Their
\(g_3\)-triples share \(g_3(p+2e_x+2e_y)\), so equality of the corresponding
\(g_2\)-types balances the two remaining exterior \(g_3\)-pairs.

## 3. Contact with the top \(g_9\) packet

The three interior entries in the top Frobenius stencil are
\[
g_3(3,0),\qquad g_3(0,3),\qquad g_3(3,3).          \tag{5}
\]
Each is the shared term of two actual cross-scale packets:
\[
\begin{array}{c|c}
\text{shared }g_3\text{ entry}&\text{packet bases}\\ \hline
g_3(3,0)&(1,0),(3,0)\\
g_3(0,3)&(0,1),(0,3)\\
g_3(3,3)&(1,3),(3,1).
\end{array}                                        \tag{6}
\]
All six bases lie in \(S_4\). The first two rows are the parallel
two-packet cancellation above. The last row is transverse: the packets
based at \((1,3)\) and \((3,1)\) share their respective \(2e_x\)- and
\(2e_y\)-shifted entry \(g_3(3,3)\).

Consequently, equality of the paired \(g_2\)-types in any row of (6)
forces a four-sign balance among exterior \(g_3\) values surrounding the
corresponding top-packet entry. This is a concrete propagation from the
full-domain \(2\)--\(3\) compatibility into the otherwise one-sided
\(3\)-to-\(9\) boundary stencil.

## 4. Exact remaining gap

Equations (1)--(6) do not themselves force a zero. Their new content is
conditional balance: a repeated \(g_2\)-majority type across an indicated
overlap forces equality of two exterior sign-pair weights. The three
possible types \(0,1,-1\) can be assigned differently to the two packet
bases in each row of (6), so pigeonhole alone does not produce any one of
the equalities (3).

To turn this packet into a zero budget, one still needs a relation that
forces one paired type equality in (6), or a closed cycle of type
transports whose exterior pair balances contradict the top \(g_9\) type.
The identities \(D_2g_1=D_1g_2\) on \(S_6\) are the natural remaining
source of such a restriction, but no forced coincidence among the six
types in (6) is derived here.

Thus the strengthened packet yields the exact new majority transport
(1) and the cancellation law (4), reaching every interior top-stencil
entry. It does not yet force a fifth zero or exclude the low-zero proper
case.
