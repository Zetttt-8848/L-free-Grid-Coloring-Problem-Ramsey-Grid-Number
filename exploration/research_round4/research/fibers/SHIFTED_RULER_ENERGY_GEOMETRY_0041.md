# Shifted-ruler energy through adjacent and distance-two sum geometry

Let (P\subset\mathbb Z) be Golomb, let (n=|P|\ge2), and assume
(1\notin\Delta P). Put

\[
 S=P\sqcup(P+1),\qquad M=\binom n2,
\]

and define

\[
 A_1=|\{d:d,d+1\in\Delta P\}|,
 \qquad
 A_2=|\{d:d,d+2\in\Delta P\}|,
 \qquad
 \varepsilon _2=\mathbf1_{\{2\in\Delta P\}}.
\]

The difference-fiber decomposition supplied for this task is

\[
 \boxed{\ T(S)=n(n-1)+4A_1+A_2+n\varepsilon _2.\ }  \tag{1}
\]

The purpose here is to rewrite its last two terms in the geometry of the
represented pair sums, where properness of the weak two-copy coloring gives
the valley law.

Let

\[
 \Sigma=\{a+b:a,b\in P,\ a\le b\},
 \qquad N=|\Sigma|=\binom{n+1}{2}=M+n.
\]

For (j=1,2), write

\[
 E_j=|\{t:t,t+j\in\Sigma\}|.                         \tag{2}
\]

Let (Z_j) count those pairs (t,t+j\in\Sigma) for which the shorter of
the two uniquely representing intervals is doubled. Thus (Z_1) is exactly
the double-valley defect from the adjacent-difference run ledger.

## 0. Derivation of the source-corner formula

Here is the root derivation of (1), so that the supplied input is fully
included. Define r_P(t)=|P intersect(P-t)| for every integer t. Disjointness
of P and P+1 makes the indicator of S the sum of their indicators. Hence

\[
r_S(t)=2r_P(t)+r_P(t-1)+r_P(t+1).
\]

Writing C_j(P)=sum_t r_P(t)r_P(t+j), expansion and translation of the
finite sums give

\[
E(S)=6E(P)+8C_1(P)+2C_2(P).
\]

Golombness gives r_P(0)=n and r_P(t)=1 exactly at the nonzero signed
differences. The absence of difference1 therefore gives

\[
E(P)=2n^2-n,\qquad C_1(P)=2A_1,\qquad
C_2(P)=2A_2+2n\varepsilon_2.
\]

For the last identity the nonzero same-sign terms give 2A_2; the two
terms meeting zero give 2n epsilon2; the only potential opposite-sign
term is r_P(-1)r_P(1)=0. Thus

\[
E(S)=12n^2-6n+16A_1+4A_2+4n\varepsilon_2.
\]

Finally |S|=2n and E(S)=2|S|^2-|S|+4T(S). Subtracting this exact
baseline proves (1), with no coloring assumption needed for that formula.

## 1. Exact distance-two correspondence

Consider (t,t+2\in\Sigma), represented by intervals (I,J). Their lengths
have the same parity. They cannot be equal: translating both endpoints of
one representation by one would put two consecutive marks in (P). Hence
the shorter interval lies inside the longer interval, possibly sharing one
endpoint.

Write the outer interval as ([u,v]) and the inner one as ([x,y]), with

\[
 u\le x\le y\le v.
\]

The two cross pairings satisfy, up to reversing the displayed differences,

\[
 (v-y)-(x-u)=2,
 \qquad
 (v-x)-(y-u)=2.                                     \tag{3}
\]

Thus they normally produce two pairs of represented differences separated
by two. There is one loss when (x=y), because the two cross pairings then
coincide. There is also one loss when the intervals share an endpoint,
because one cross pairing contains a zero-length edge. If both events occur,
both losses occur and there is no positive-difference pair from that
pairing.

Conversely, intervals representing (d,d+2\in\Delta P) give complementary
endpoint sums separated by two. Hence (3) is an exact correspondence.

Let (H_2) count pairs of represented sums at distance two whose intervals
share an endpoint. Then

\[
 A_2=2E_2-Z_2-H_2.                                  \tag{4}
\]

The shared-endpoint defect is explicit. If two representations at distance
two share the mark (a), their other endpoints are the unique pair of marks
at distance two. Conversely, if (b,b+2\in P), then for every (a\in P),
the sums (a+b) and (a+b+2) give one such shared-endpoint pair. Uniqueness
of pair sums prevents repetitions. Therefore

\[
 \boxed{\ H_2=n\varepsilon _2.\ }                   \tag{5}
\]

Combining (4)--(5) yields the cancellation built into (1):

\[
 \boxed{\ A_2+n\varepsilon _2=2E_2-Z_2.\ }          \tag{6}
\]

Together with the completed adjacent ledger

\[
 A_1=2E_1-Z_1,                                      \tag{7}
\]

equation (1) becomes

\[
 \boxed{\ T(S)=2M+8E_1-4Z_1+2E_2-Z_2.\ }           \tag{8}
\]

This is the requested complete source-corner formula in pair-sum geometry.

## 2. Coupling through the valley runs

Assume now that the weak triangle on (P\sqcup(P+1)), with the two copies as
diagonal color classes, is properly colored. On every consecutive run in
(Sigma), the representing interval lengths strictly decrease to one
valley and then strictly increase.

Let

* (r_\Sigma) be the number of consecutive runs in (Sigma);
* (s_\Sigma) be the number of singleton runs;
* (g_\Sigma) be the number of gaps of exactly one missing integer between
  consecutive runs.

A distance-two pair of represented sums is either contained in one run or
crosses one such one-point gap. A run of length (k) contains
(max(k-2,0)) internal distance-two pairs. Consequently

\[
 \boxed{\ E_2=N-2r_\Sigma+s_\Sigma+g_\Sigma.\ }      \tag{9}
\]

Since (E_1=N-r_\Sigma), substitution in (8) gives

\[
 \boxed{
 T(S)=2M+10N-12r_\Sigma
      +2(s_\Sigma+g_\Sigma)-4Z_1-Z_2.
 }                                                   \tag{10}
\]

One may instead retain the run structure of the difference set. If
(r_D) is the number of consecutive runs in (Delta P), the previous exact
ledger says

\[
 M-r_D=2(N-r_\Sigma)-Z_1.
\]

Eliminating (r_\Sigma) from (9) gives the new coupled identity

\[
 \boxed{\ E_2=Z_1+s_\Sigma+g_\Sigma-n-r_D.\ }        \tag{11}
\]

and therefore

\[
 \boxed{
 T(S)=6M-6r_D-2n
      +2(Z_1+s_\Sigma+g_\Sigma)-Z_2.
 }                                                   \tag{12}
\]

Formula (12) isolates the precise remaining budget. Long adjacent-difference
runs lower (r_D), but they can raise the energy only insofar as the sum set
has many doubled-valley incidences, singleton runs, or one-point gaps. The
distance-two doubled defect (Z_2) always subtracts.

## 3. Three consecutive sums and doubled pairs

Suppose (t,t+1,t+2\in\Sigma). The valley law leaves exactly three shapes
for their interval lengths: strictly decreasing, strictly increasing, or a
strict valley at (t+1). A strict local maximum is impossible.

If the middle representation is the doubled pair ({p,p}), it is the
valley. Each adjacent sum edge then has only one adjacent-difference
preimage, so this three-term window contributes two to (Z_1). The endpoint
sums at distance two have two difference-gap-two preimages unless their
representations share an endpoint. In the shared-endpoint case one raw
preimage is lost, but it is exactly one of the (n\varepsilon _2) incidences
in (5). Thus after the cancellation in (6), this distance-two endpoint pair
still contributes two. In the combined term

\[
 4A_1+(A_2+n\varepsilon _2),
\]

such a three-sum window therefore contributes (4\cdot2+2=10) through its
two adjacent edges and its endpoint distance-two edge.

If instead one endpoint representation of a distance-two pair is doubled,
that pair contributes one to (Z_2). It has one effective preimage after the
shared-endpoint cancellation, exactly as (6) records.

The analogous statement for three consecutive represented differences is
less rigid. If the interval of length (d+i) starts at (a_i), the two
adjacent-difference pairs and the distance-two pair map respectively to sum
pairs based at

\[
 a_0+a_1+d,\qquad
 a_1+a_2+d+1,\qquad
 a_0+a_2+d.                                          \tag{13}
\]

These three locations need not themselves be consecutive. Hence the valley
law cannot be applied to them as one three-term sum window without an extra
relation among (a_0,a_1,a_2).

## 4. Precise remaining defect

Equations (10)--(12) reduce the desired geometric budget to controlling

\[
 Z_1+s_\Sigma+g_\Sigma
\]

relative to (r_D), while (Z_2) is favorable. The valley theorem itself
controls the order of lengths inside each sum run, but it does not restrict
the number of singleton runs or one-point gaps between runs. Nor does it
couple the three sum locations in (13). Thus no coefficient bound follows
from the valley law alone.

A further improvement must charge either singleton/one-gap sum components,
or force many distance-two doubled defects (Z_2), using cells that connect
distinct sum runs. Formula (12) identifies that requirement without
discarding any of the adjacent or distance-two geometry.
