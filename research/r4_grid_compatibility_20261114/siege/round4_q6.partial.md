# round4_q6 answer: does the missing statement MS settle Part D (D-a), and an attack on MS

Plan. (A) Prove rigorously that MS, and even a weaker form MS' with additive slack and a restricted
lambda-range, together with the listed summed rank inequality and prefix formula, gives
sum_e |S_e(d)| <= (1-delta') * 3K(S) with an explicit delta' ~ delta/2. (B) Attack MS. First move:
**corner-colour coupling reduction**. Classify every L meeting diagonal d by which of its cells lie on
diagonal d, show that the three classes at the same d are never coupled directly, and reduce MS to a
self-contained statement PU about the union of the two Golomb pieces that share a corner colour. Then
attack PU.

Notation. Cell (v,u) lies on diagonal v-u. z_h(u) = chi(u+h,u). The rank is written rho, so that c can
remain the name of a colour. C_w(lambda) = sum_{l<=lambda} w_l, and (x)_+ = max(x,0).

---

## Part A. MS implies (D-a), with an explicit delta'

### A.1 Facts used, all from the brief

- (F1) The summed rank inequality. Take classes S_e(d) of sizes s_e and spans <= S, and a rank rho with
  1 <= rho < min_e s_e. Put H_tot = sum_e (rho s_e - rho(rho+1)/2), w_l = sum_e r_{S_e(d)}(l) and
  E_rho = sum_{i=0}^{rho-1} (rho-i) e_{i+1} >= 0. Then
  `2P(H_tot; w) + 12 E_rho <= 3 S rho(rho+1)`.
- (F2) The prefix formula `P(H;w) = sum_{lambda>=0} (H - C_w(lambda))_+`.
- (F3) v_l = Q(S-l) + Q(S-l-1) is nonincreasing in l, because Q is nondecreasing. It is >= 0, and it
  is 0 for l > S.
- The single-class cap K(S) on |S_e(d)|. The consumer certifies it from the rank inequality.

### A.2 A continuous comparison functional

Let C~ be the piecewise-linear interpolation of lambda -> C_v(lambda) on [0, infinity), with
C~(0) = 0. Its slopes v_1 >= v_2 >= ... >= 0 are nonincreasing (F3), so C~ is concave. Define
`Pi(H) = int_0^infinity (H - C~(x))_+ dx`, with values in [0, infinity]. Pi is nondecreasing in H.

**Lemma A1.**
(a) For every integer H >= 0, `P(H;v) - H <= Pi(H) <= P(H;v)`.
(b) For t >= 1, `Pi(tH) >= t^2 Pi(H)`.
(c) For beta > 0 and real H' >= 0, `sum_{lambda>=0} (H' - beta C_v(lambda))_+ >= beta Pi(H'/beta)`.

*Proof.*
- (a), upper bound. Let f(x) = (H - C~(x))_+. It is nonincreasing, and f(lambda) = (H - C_v(lambda))_+
  at integers. Then sum_{lambda>=0} f(lambda) >= sum_lambda int_lambda^{lambda+1} f = int_0^infinity f.
- (a), lower bound. For x in [lambda-1, lambda] we have C~(x) <= C_v(lambda), so
  int_0^infinity f >= sum_{lambda>=1} (H - C_v(lambda))_+ = P(H;v) - H. Here the lambda = 0 term of
  (F2) equals H.
- (b) Concavity and C~(0) = 0 give C~(t mu) <= t C~(mu) for t >= 1. Substitute x = t mu:
  Pi(tH) = t int (tH - C~(t mu))_+ d mu >= t int (tH - t C~(mu))_+ d mu = t^2 Pi(H).
- (c) The same monotone-sum argument applied to x -> (H' - beta C~(x))_+ gives a lower bound of
  int_0^infinity (H' - beta C~(x))_+ dx = beta int (H'/beta - C~(x))_+ dx = beta Pi(H'/beta). ∎

### A.3 The implication theorem

Define the weakened hypothesis

**MS'(alpha, E_0, Lambda)**: `C_w(lambda) <= alpha * C_{3v}(lambda) + E_0` for 1 <= lambda <= Lambda.

MS with constant delta is the case MS'(1-delta, 0, S).

**Theorem A.** Fix a proper ternary source and d. Let S, v_l, s_e and w_l be as above, and let alpha
be in (0,1]. Let rho >= 1 and s_1 > rho be integers, and put H_1 = rho s_1 - rho(rho+1)/2. Assume the
**Pi-certificate** `2 Pi(H_1) + 4 E_rho > S rho(rho+1)` holds. Assume MS'(alpha, E_0, Lambda) holds
with Lambda >= Lambda_0, where Lambda_0 is the least lambda with
3 alpha C_v(lambda) >= 3 rho s_1 + E_0. If Lambda_0 does not exist, take Lambda = infinity. If
min_e s_e > rho, then

`s_0 + s_1' + s_2 < 3 sqrt(alpha) s_1 + E_0/rho + 3(1 - sqrt(alpha))(rho+1)/2`.

Here s_e' denotes the class sizes, written apart from the certificate size s_1.

*Proof.* Write s = sum_e s_e. Suppose s is at least the right-hand side. Then H_tot = rho s - 3rho(rho+1)/2
satisfies

H_tot - E_0 >= 3 sqrt(alpha) rho s_1 + 3(1-sqrt(alpha)) rho(rho+1)/2 - 3 rho(rho+1)/2 = 3 sqrt(alpha) H_1.

We may assume s <= 3 rho s_1 (rough bound; otherwise use H_tot capped, see below). For lambda <= Lambda,
MS' gives (H_tot - C_w(lambda))_+ >= (H_tot - E_0 - 3 alpha C_v(lambda))_+. For lambda > Lambda >= Lambda_0
the right-hand side is 0, so the inequality holds trivially. By (F2) and Lemma A1(c) with beta = 3 alpha:

P(H_tot; w) >= sum_lambda (H_tot - E_0 - 3 alpha C_v(lambda))_+ >= 3 alpha Pi((H_tot - E_0)/(3 alpha))
>= 3 alpha Pi(H_1/sqrt(alpha)) >= 3 alpha * alpha^{-1} Pi(H_1) = 3 Pi(H_1).

This uses monotonicity of Pi and Lemma A1(b) with t = alpha^{-1/2}. Then (F1) gives
3 S rho(rho+1) >= 2P(H_tot; w) + 12 E_rho >= 6 Pi(H_1) + 12 E_rho > 3 S rho(rho+1), a contradiction.

The restriction to Lambda_0 needs one remark. Lambda_0 is defined from 3 rho s_1 + E_0, and this
dominates H_tot whenever s <= 3 s_1. If s > 3 s_1, then some class has size > s_1. That class is a
binary source with a firing single-class certificate, so this already contradicts the single-class
bound. If one prefers not to use that, take Lambda = S. ∎

**Corollary A2 (D-a from MS).** Let s_1 = K^Pi(S) + 1. Here K^Pi(S) is the cap certified from the
Pi-form with rank rho. By Lemma A1(a), K^Pi(S) <= K^+(S), where K^+ is certified from the consumer's
P-form with the right-hand side enlarged by 2H_1. Then every proper ternary source satisfies

`sum_e |S_e(d)| <= max{ 2K(S) + rho, 3 sqrt(alpha)(K^Pi(S)+1) + E_0/rho + 3(1-sqrt(alpha))(rho+1)/2 }`.

The first branch covers the unbalanced case min_e s_e <= rho. Dividing by 3K(S):

delta' = 1 - max{...}/(3K(S)) ≈ (1 - sqrt(1-delta)) (1 - (rho+1)/(2K)) - E_0/(3 rho K) - (K^Pi/K - 1),

which is ≈ delta/2.

Numerical orientation (estimates, not computed). The regime of the brief has K ≈ 4.58e5 and fibres
saturated up to lambda ≈ 3.5e5 with 3v ≈ 2.8e4. This corresponds to H ≈ rho K ≈ 3.3e9, so
rho ≈ 7e3. Hence (rho+1)/(2K) ≈ 0.008.

The P-to-Pi correction is also negligible: 2H_1 ≈ 7e9, against S rho(rho+1) ≈ 1e15. The additive slack
E_0 is harmless up to E_0 ≈ 1e-3 rho K ≈ 3e6.

So MS with delta ≈ 0.023 would give delta' ≈ 0.0115. By the stated sensitivity this is the size
needed to move the excluded side from about 21.99M to about 21.0M. That figure is HYPOTHETICAL and
conditional on MS; it is not a bound. To apply this to the square, take each diagonal colour c
separately with S_c <= n-d-1. Then X_d <= 4 max{...} <= (1-delta' + O(1e-6)) U_d. The O(1e-6) term
is the staggering difference between K(n-d-1) and K(n-d-j-1) for j <= 11.

### A.4 Verdict on (A)

- MS is in exactly the form the consumer uses, as prefix sums of w. The rank machinery turns a
  proportional prefix deficiency delta into a proportional size deficiency of about delta/2.
- MS is not vacuous. It has content when S is at least about 100, and it is far from trivial at
  S ~ 2.2e7.
- MS is stronger than needed in two ways, and it is safer to target MS'.
  - It asks for every lambda, but only lambda <= Lambda_0 ≈ 3.5e5/alpha matters.
  - It has no additive slack. An additive error E_0 up to about 1e-3 rho K costs nothing. So
    counterexamples to MS at small lambda, or at small S, would not damage the programme.
- MS is implied by a single-class statement. This is SC(delta): sum_{l<=lambda} r_X(l) <=
  (1-delta) sum_{l<=lambda} v_l for every class X. SC has nothing to do with requests.
- Conversely, if a source has prefix ratio >= 1-delta in MS, then each of the three classes has
  single-class prefix ratio >= 1-3delta. So **any counterexample to MS needs three simultaneously
  near-saturated binary sources**, and no construction is known that saturates even one.
- Whether MS is true is OPEN. Part B reduces it to a cleaner sufficient statement.

