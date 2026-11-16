# round5_q6 answer: MS' => (D-a), and an attack on MS'

Plan (written first): Task 1: derive MS' => (D-a) in two independent ways:
Route A through the cited Theorem A (re-derived), and Route B through a
sliding-window second-moment (Fejer) identity that needs neither ranks nor
e_j. Task 2: the first move is that same sliding-window identity in physical
space. It shows that MS' is at least as strong as a proportional size deficit
for the three classes. So MS' is a restatement of the target, not a reduction
of it.

Conventions. In this file, X_e := S_e(d), s_e := |X_e|, T := sum_e s_e,
w_l := sum_e r_{X_e}(l), C_w(lambda) := sum_{l<=lambda} w_l, and S is the span
of F_d(D). Every X_e lies in F_d(D), so span X_e <= S. Also v_l = Q(S-l)+Q(S-l-1).
Q is nondecreasing, so v_l is nonincreasing in l, C_v is concave, and
v_l <= v_1 for every l.

## 0. Elementary facts about Q (proved here)

(Q-up) Q(m) <= sqrt(2m)+1. Proof: a Sidon set of size q in m+1 consecutive
integers has q(q-1)/2 distinct positive differences, all <= m.

(Q-low) Q(m) > sqrt(m/8) for m >= 32. Proof: Bertrand's postulate (cited from
memory) gives a prime p with x < p <= 2x, where x = sqrt(m/8) >= 2, so p is odd.
The Erdos-Turan set A = {2pk + (k^2 mod p) : 0 <= k < p} lies in
[0, 2p^2-p-1] ⊂ [0, m]. Suppose a_i + a_j = a_k + a_l. Each residue part is < p,
so the two residue sums are < 2p. Reducing mod 2p gives i+j = k+l and
i^2+j^2 ≡ k^2+l^2 (mod p), hence {i,j} = {k,l}. A 3-AP a_i + a_k = 2a_j forces
i+k = 2j and 2(i-j)^2 ≡ 0, so i = j = k. So A is Sidon with no 3-AP, and |A| = p.

Consequence: for S >= 34, sqrt(S)/2 <= sqrt((S-2)/2) <= v_1 <= 2 sqrt(2S) + 2.

## 1. Lemma F (sliding-window second moment). PROVED.

For a finite X ⊂ Z with |X| = s, span X <= S, and an integer lambda >= 0, set
Lam = lambda+1 and N = S+Lam. Then

  s*Lam + 2 sum_{l=1}^{lambda} (Lam - l) r_X(l) >= s^2 Lam^2 / N.

Proof. Let f(x) = |X ∩ [x, x+lambda]| for integer x. Then sum_x f(x) = s*Lam.
Moreover f vanishes outside an integer interval of length span X + Lam <= N.
Next, sum_x f(x)^2 = sum_{a,b in X} #{x : a,b in [x,x+lambda]}
= sum_{a,b} (Lam - |a-b|)_+ = s*Lam + 2 sum_{l=1}^{lambda}(Lam-l) r_X(l).
Cauchy-Schwarz over the at most N points of the support finishes the proof. QED

Summation by parts: sum_{l<=lambda}(Lam-l) w_l = sum_{mu=1}^{lambda} C_w(mu).

Corollary F0 (Fejer single-class cap, PROVED). Every binary source X of span
<= S satisfies s <= K_F(S) := min_{1<=lambda<=S} [N/Lam + sqrt(v_1 N)].
Also K_F(S) >= sqrt(v_1 S).
Proof. By cited item 1, r_X(l) <= v_l <= v_1. So
2 sum_{l<=lambda}(Lam-l) r_X(l) <= v_1 lambda Lam, and Lemma F gives
s^2 <= N s/Lam + v_1 N. Since s^2 - bs - c <= 0 implies s <= b + sqrt(c), the
bound follows. N > S gives the lower bound on K_F. QED
(At the stated scale, sqrt(v_1 S) ≈ 4.55*10^5 against the rank cap
K ≈ 4.58*10^5. The two caps agree to within about 1%. This comparison is HEURISTIC:
the numbers are the problem's estimates.)

## 2. Task 1, Route B: MS' => (D-a) against the Fejer caps. PROVED.

Theorem B. Assume MS'(delta, S_0). Let (D, chi) be any proper ternary source
and d a shift with span S >= S_0, S >= 34. Then for every integer
lambda in [1, S], with Lam = lambda+1,

  T <= 3 sqrt(v_1 S) * (1 - delta/2 + E(Lam)),
  E(Lam) = [sqrt(S/v_1) + S/(300 v_1)]/Lam + Lam/(2S) + 1/sqrt(v_1 S) + 1/(600 v_1).

Hence T <= (1 - delta') * 3 K_F(S), where delta' = delta/2 - min_Lam E(Lam).

Explicit version: take Lam = ceil(S^{3/4}/10). For
S >= S_1(delta) := max{S_0, 10^4, delta^{-4}, 16384 delta^{-2}},
this gives delta' >= delta/4.

Proof. Summing MS' over mu = 1..lambda and using C_v(mu) <= mu v_1 gives
  sum_mu C_w(mu) <= 3(1-delta) v_1 lambda Lam/2 + lambda S/100.
Apply Lemma F to each X_e, add over e, and use the summation by parts:
  sum_e s_e^2 Lam^2/N - T Lam <= 3(1-delta) v_1 lambda Lam + lambda S/50.
Multiply by N/Lam^2 and use lambda < Lam:
  sum_e s_e^2 <= N T/Lam + 3(1-delta) v_1 N + N S/(50 Lam).
Since T^2 <= 3 sum s_e^2, we get T^2 <= bT + c with b = 3N/Lam and
c = 9 v_1 N (1 - delta + S/(150 v_1 Lam)). Hence T <= b + sqrt(c).
Now use sqrt(1+y) <= 1+y/2 for y >= -1, twice, with N = S(1+Lam/S):
  T/(3 sqrt(v_1 S)) <= (S/Lam + 1)/sqrt(v_1 S)
                       + (1 + Lam/(2S))(1 - delta/2 + S/(300 v_1 Lam)).
Expanding, and using Lam/(2S) * S/(300 v_1 Lam) = 1/(600 v_1), gives the
displayed E. Finally K_F >= sqrt(v_1 S) (Corollary F0).

Explicit constants. Take Lam = ceil(S^{3/4}/10) and use 1/v_1 <= 2/sqrt(S)
from Section 0. Then:
- sqrt(S/v_1)/Lam <= 10 sqrt(2) S^{-1/2};
- S/(300 v_1 Lam) <= S^{-1/4}/15;
- Lam/(2S) <= S^{-1/4}/20 + 1/(2S);
- 1/sqrt(v_1 S) <= sqrt(2) S^{-3/4};
- 1/(600 v_1) <= S^{-1/2}/300.
For S >= 10^4 this gives E <= 0.12 S^{-1/4} + 16 S^{-1/2}.
If S >= delta^{-4}, then 0.12 S^{-1/4} <= delta/8. If S >= 16384 delta^{-2},
then 16 S^{-1/2} <= delta/8. Hence E <= delta/4 and delta' >= delta/4.
Note that 2 <= Lam <= S+1, so lambda is in the range of MS'. QED

Numerics at the stated scale (HEURISTIC inputs S = 2.2*10^7, v_1 ≈ 9.4*10^3).
The optimal Lam ≈ sqrt(2SM) with M = sqrt(S/v_1) + S/(300 v_1) ≈ 56.2. This gives
min E ≈ sqrt(2M/S) ≈ 2.3*10^{-3}, so delta' ≈ delta/2 - 0.0023 against K_F.
Route B is fully explicit, but it costs about 0.0023 at this scale.

## 3. Task 1, Route A: through Theorem A, against the chain's own rank caps.

Check of Theorem A (re-derived in outline; I find it correct). Suppose every
class has more than rho elements and T exceeds the second term of the max.
Then H_tot - E_0 >= 3 sqrt(alpha) H*. The hypothesis on C_w up to Lambda_0
covers every lambda with H_tot - C_w(lambda) > 0, because each s_e <= s*-1.
Combine three facts:
- the prefix formula;
- sum >= integral for the nonincreasing function (H - C~)_+;
- Pi(tH) >= t^2 Pi(H) for t >= 1, which holds because C~ is concave with C~(0) = 0.
They give 2P(H_tot; w) >= 6 alpha Pi(H*/sqrt(alpha)) >= 6 Pi(H*). Then cited
item 4 contradicts the Pi-certificate. If some class has at most rho elements,
then T <= 2(s*-1) + rho.

Lemma A1 (P-certificate to Pi-certificate, PROVED). Suppose the chain's cap at
rank rho is K = s_P - 1. This means the rank-rho inequality (cited item 3) with
P(.; v) fails at size s_P and span S. Then, by heredity, every class has size
<= K. Define H_P = rho s_P - rho(rho+1)/2, t = 1 + v_1/H_P and s* = ceil(t s_P).
Then the Pi-certificate holds at (rho, s*).
Proof. Two bounds are needed.
- P(H; v) <= H + Pi(H). The lambda = 0 term of the prefix formula is H, and for
  lambda >= 1 each term is at most the integral over [lambda-1, lambda].
- Pi(H) >= H^2/(2 v_1), because C~(x) <= v_1 x.
Since H(s*) >= t H_P, we get
2Pi(H(s*)) >= 2t^2 Pi(H_P) >= 2Pi(H_P) + (4v_1/H_P) H_P^2/(2v_1) = 2Pi(H_P) + 2H_P >= 2P(H_P; v).
QED

Theorem A' (MS' => (D-a), PROVED given cited items 1-6). Apply Theorem A with
alpha = 1-delta and E_0 = S/100. MS' supplies its hypothesis for every
lambda <= S, hence up to Lambda_0. Using sqrt(alpha) <= 1 - delta/2,

  T <= 3K (1 - delta'_A),
  delta'_A = min{ 1/3 - (2(s*-1) - 2K + rho)/(3K),
                  delta/2 - (t-1) - (t+1)/K - S/(300 rho K) - delta(rho+1)/(2K) }.

The rank enters only through S/(300 rho K). This is exactly where the
derivation can fail: if the chain's cap were certified at a small rank, with
rho K << S/delta, Route A would give nothing.

Numerics at the stated scale. The inputs are heuristic: K ≈ 4.58*10^5 and
rho ≈ 675 are the problem's estimates, not checked here. They give:
- t-1 ≈ 3*10^{-5};
- S/(300 rho K) ≈ 2.4*10^{-4};
- delta(rho+1)/(2K) ≈ 7.4*10^{-4} delta.
Hence delta'_A ≈ 0.499 delta - 2.7*10^{-4}, which is positive for
delta > 5.5*10^{-4}. A uniform explicit S_1 for Route A would need a proved lower
bound on rho K / S for the chain's certificates. I do not have one. Route B
supplies the explicit S_1 instead.

Conclusion of Task 1: MS' => (D-a). The result is delta' = delta/4 against the
Fejer caps K_F(S), for S >= S_1(delta) (Theorem B). Against the chain's rank
caps it is delta'_A ≈ delta/2 - O(S/(rho K)) (Theorem A'). None of the cited
statements looks false.

## 4. Task 2: attack on MS'

First move (not in the used list): the physical-space sliding-window second
moment (Lemma F). This is Cauchy-Schwarz over the windows [x, x+lambda]. It is
not Fourier uniformity, not request energy, and not a pattern classification.
Its use here is to locate MS' relative to the target.

### 4.1 Proposition W (where MS' has content). PROVED.

(W1) MS' holds automatically for every lambda <= S/(300 delta v_1). Reason:
w_l <= 3 v_l (cited item 1), so C_w(lambda) - 3(1-delta)C_v(lambda)
<= 3 delta C_v(lambda) <= 3 delta lambda v_1 <= S/100.

(W2) The consumers need MS' only on a bounded window:
- Theorem A uses it only for lambda <= Lambda_0, and
  Lambda_0 >= rho s*/(alpha v_1) roughly;
- Theorem B uses it only for lambda <= ceil(S^{3/4}/10) - 1.

At the stated scale (heuristic numbers), the nontrivial window is about
7.8/delta < lambda <= 3.3*10^4 ≈ 7 sqrt(S). So the only lags that matter are
short lags, below 10 sqrt(S).

(W3) Why short-lag saturation is generic at this scale (heuristic). Suppose a
class has size equal to the cap and is spread evenly. It has
r(l) ≈ s^2/S ≈ K^2/S. At the stated numbers,
K^2/S ≈ (4.58*10^5)^2/(2.2*10^7) ≈ 9.5*10^3 ≈ v_l. So near-saturation of the
short fibers needs no special structure. It is forced by size alone, and
Lemma F makes this exact. This is the reason for 4.2.

### 4.2 Proposition C (MS' is at least as strong as a size deficit). PROVED.

Define SD(eta), "Fejer size deficit at level eta": for every proper ternary
source and shift d of span S (large),

  sum_e |S_e(d)|^2 < 3 (1-eta) v_1 S.

Claim. Assume MS'(delta, S_0) and 0 <= eta < delta. Then SD(eta) holds for all
S >= max{S_0, 100, 276/(delta-eta)^4}.

Proof. Suppose the contrary: sum_e s_e^2 >= 3(1-eta) v_1 S. Put
Lam = floor(S(delta-eta)/2). Then Lam >= S(delta-eta)/4 >= 2 and
Lam/S <= (delta-eta)/2.
Lower side. By Lemma F and summation by parts,
  sum_{mu<=lambda} C_w(mu) >= (1/2)[3(1-eta) v_1 S Lam^2/N - T Lam].
Upper side. MS' at every mu <= lambda would give
  sum_{mu<=lambda} C_w(mu) <= (1/2)[3(1-delta) v_1 lambda Lam + lambda S/50].
So it suffices to show
  3(1-eta) v_1 S Lam/N - T > 3(1-delta) v_1 Lam + S/50.
Since S/N >= 1 - Lam/S, the left side minus 3(1-delta)v_1 Lam is at least
3 v_1 Lam (delta - eta - Lam/S) >= 3 v_1 Lam (delta-eta)/2 >= (3/8) v_1 S (delta-eta)^2.
By Section 0 this is >= (3/16) S^{3/2}(delta-eta)^2. On the other side,
T + S/50 <= 3(S+1) + S/50 <= 3.1 S for S >= 100. The inequality holds once
sqrt(S)(delta-eta)^2 > 16.6, and S >= 276/(delta-eta)^4 ensures this.
Hence MS' fails at some mu <= lambda <= S, a contradiction. QED

Corollary C1 (PROVED). SD(eta) implies (D-a) with no further input:
T <= sqrt(3 sum s_e^2) < 3 sqrt((1-eta) v_1 S) <= (1 - eta/2) * 3 K_F(S).
This gives a third proof of MS' => (D-a): delta' = eta/2 for any eta < delta.

Reading of 4.2. The chain is MS'(delta) => SD(eta) => (D-a). So every proof of
MS' contains a proof of SD, which is a proportional upper bound on the class
sizes themselves. MS' carries no information beyond SD that the consumer
needs. SD is the weaker and sufficient target. I recommend registering
SD(eta), or the even weaker T^2 <= 9(1-eta) v_1 S, in place of MS'. MS' is not
implausible. But it is not a reduction: it is at least as hard as (D-a) itself.

### 4.3 What a refutation would require (PROVED reduction, OPEN content)

Refuting MS' for every delta needs sources at large S with near-saturated
prefixes. Refuting SD (hence (D-a) in Fejer form) needs three disjoint binary
sources, each of size >= sqrt((1-eta) v_1 S) ≈ sqrt(2) S^{3/4}, living in
F_d(D) and compatible with a proper ternary coloring of V(D).

The only binary sources I can certify are Sidon sets, of size about sqrt(S).
A Sidon set with no 3-AP contains no directed L in its strict source: an L
needs a + b' = a' + b with a < b < b' and a' = a + b' - b < b', and Sidon
(with 3-APs excluded) rules this out. I know of no construction of binary
sources of size of order S^{3/4}; this statement is from memory and is not a
search result.

Consequently:
- if the true maximum binary-source size is <= sqrt((1-eta) v_1 S) for
  large S, then SD(eta) holds trivially;
- a counterexample to MS' would first need a single binary source within a
  factor 1 - o(1) of the Fejer cap. That is a necessary condition, proved in
  4.2 for SD.

This is the obstruction I met: no known object comes near the regime where
MS' could fail. Also, a proof of MS' must beat the single-class Fejer/rank
capacity by a proportional factor for the three classes jointly. No local
(single-lag) argument can do that by W3: at cap size, short-lag saturation
is generic.

### 4.4 Status summary

PROVED:
- Section 0 (bounds on Q).
- Lemma F and Corollary F0 (Fejer cap K_F(S) for binary sources).
- Theorem B: MS' => T <= (1-delta/4) 3K_F(S) for S >= S_1(delta) =
  max{S_0, 10^4, delta^{-4}, 16384 delta^{-2}}.
- Lemma A1 and Theorem A' (Route A, with delta'_A explicit, conditional only
  on cited items 1-6).
- Proposition W.
- Proposition C: MS'(delta) => SD(eta) for eta < delta, S >= 276/(delta-eta)^4.
- Corollary C1.

HEURISTIC (problem's estimated numbers only):
- the scale numerics: delta' ≈ delta/2 - 0.0023 (Route B), and
  delta'_A ≈ 0.499 delta - 2.7*10^{-4} (Route A);
- the window 7.8/delta < lambda <= about 7 sqrt(S);
- K ≈ sqrt(v_1 S).

NOT ACHIEVED: neither a proof nor a refutation of MS'.

OPEN:
- (O1) MS' itself.
- (O2) SD(eta) for some explicit eta > 0. It is weaker than MS' and suffices
  for (D-a).
- (O3) Does a binary source of span S and size >= c S^{3/4} exist for some
  c > 0? A negative answer with c -> 0 makes SD trivially true. A positive
  answer near the Fejer constant sqrt(2) is necessary for any counterexample.
- (O4) A proved lower bound on rho K/S for the chain's rank certificates,
  which would make Route A uniform in S.

Nothing here is a claim about R_4. Under MS' (or SD), the consumer could
replace U_d by (1-delta') U_d with delta' as above. The cap K_F differs from
the rank cap by about 1% at the stated scale (heuristic). So the consumer
should use min(K, K_F) and subtract that difference from delta'.

=== END OF ANSWER round5_q6 ===
