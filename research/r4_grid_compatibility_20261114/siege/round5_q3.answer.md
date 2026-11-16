# round5_q3 answer: MS' (joint prefix fiber deficit with slack S/100)

## 0. Verdict (summary)

- **MS' is NOT settled.** I give neither a proof with explicit (delta, S_0) nor a counterexample family. What follows is a partial result and is labelled as such.
- **Proved (partial).**
  - (P1) MS' holds for every delta in (0,1) and every S >= 1 on the small-lag range lambda <= lambda_triv(S) := S / (600 (sqrt(2S)+1)). This range comes from the slack alone.
  - (P2) If MS' fails at (d, lambda, delta), then each of the three classes is individually prefix-saturated: C_{r_e}(lambda) > (1-3delta) C_v(lambda) + S/100.
  - (P3) Explicit size consequence. Each class then has size > (1-3delta) lambda sqrt(S-lambda-1) / (2 sqrt(lambda(sqrt(2lambda)+1))), which is about 0.42 (1-3delta) sqrt(S) lambda^{1/4}. So any counterexample in the range the chain needs (lambda of order S^{5/8}) needs three binary sources of size at least about S^{0.656} at a single shift.
- **The chain from MS' to (D-a).** I re-checked steps 2-5 (Theorem A, Lemma A1, the branch algebra and the delta' formula) and found them correct. Step 6 has a real but repairable flaw: the lower bound K^Pi(S) >= c_1 S^{3/4} is justified in the wrong direction. It needs a *lower* bound on Q, not the upper bound v_l <= 2Q(S). It also has a circular choice of rho. I give the repair (Lemma 1.2), and a caveat on the comparison base (Section 1.3).
- **Open.** MS' on the critical range lambda_triv(S) < lambda <= Lambda_0(S). Here Lambda_0 is of order S^{5/8}, and this is the only range that Theorem A consumes.

---

## 1. Audit of the chain MS' => (D-a)

### 1.1 Steps re-checked and found correct

- **Theorem A, branch algebra.** rho s - 3rho(rho+1)/2 - E_0 > 3 sqrt(alpha) rho s* + 3(1-sqrt alpha) rho(rho+1)/2 - 3 rho(rho+1)/2 = 3 sqrt(alpha) H*. Correct.
- **Chain of inequalities.** P(H_tot; w) >= sum_lambda (H_tot - E_0 - 3alpha C_v(lambda))_+ >= 3alpha Pi((H_tot - E_0)/(3alpha)) >= 3alpha Pi(H*/sqrt alpha) >= 3 Pi(H*).
  - The second step is A1(c): the function x -> (H' - beta C~(x))_+ is nonincreasing, and C~ = C_v at the integers.
  - The fourth step is A1(b) with t = alpha^{-1/2}. It uses C~(t mu) <= t C~(mu), which holds because C~ is concave with C~(0) = 0.
  - Correct.
- **Lambda_0 = S with H_tot - E_0 > 3alpha C_v(S).** Here the right side is +infinity. This is still a contradiction: MS' at lambda = S would give H_tot > C_w(lambda) for every lambda, so H_tot would exceed the total number of available pairs. The selected differences are actual pairs, so that is impossible. Theorem A therefore stands.
- **K^Pi is a valid cap.** Pi is increasing, so the certificate, once it holds, holds for all larger s. With Pi <= P (A1(a)) and F4, every binary source of span <= S has size <= K^Pi(S). K^Pi(S) is nondecreasing in S: a larger S gives a larger v, hence a smaller Pi, and a larger right-hand side. So using K^Pi(S) with S = span F_d(D_c) <= n-d-1 is compatible with the consumer.
- **Step 5 formula.** I re-derived delta' from both branches; it matches.
- **Step 4.** The use of MS' with E_0 = S/100 and Lambda_0 <= S is correct.
- **Regime numbers.** With rho ≈ 675, S ≈ 2.2e7 and K ≈ 4.58e5, the term S/(300 rho K) is about 2.4e-4. This matches the stated "-2.5e-4" (estimate).

### 1.2 Flaw in step 6 (wrong-direction justification; repairable)

**The problem.** Step 6 needs K^Pi(S) >= c_1 S^{3/4}, so that the term S/(300 rho K^Pi) tends to 0 when rho ~ K^{1/2}. A *lower* bound on K^Pi means the certificate *fails* at s_1 = c_1 S^{3/4}. That requires an *upper* bound on Pi(H_1), i.e. a *lower* bound on the multiplicities v_l, i.e. a lower bound on Q.

The cited input "v_l <= 2Q(S) <= 2(sqrt S + S^{1/4} + 1)" gives a lower bound on Pi, hence an upper bound on K^Pi. That is the wrong direction.

There is also a circularity: rho = floor(K^Pi(S)^{1/2}), but K^Pi is defined at the chosen rho. Fix this by setting rho := floor(S^{3/8}), an explicit function of S.

**Lemma 1.1 (elementary Sidon bounds).**
- (a) Q(m) <= sqrt(2m) + 1 for m >= 0.
- (b) Q(m) >= sqrt(m)/2 + 1/4 for m >= 6. This uses Bertrand's postulate and Singer's theorem, both cited from memory. Singer: for a prime p there is a set of p+1 residues mod p^2+p+1 with all differences distinct.

*Proof.*
- (a) A Sidon set of k points in m+1 consecutive integers has k(k-1)/2 distinct positive differences, all <= m. So k <= 1/2 + sqrt(2m + 1/4) <= sqrt(2m) + 1.
- (b) A Singer set, read as integers in [0, p^2+p], is Sidon in Z: a coincidence of differences in Z is also one mod p^2+p+1. So Q(p^2+p) >= p+1.
  - Let y >= 2 be the largest integer with y^2 + y <= m. Then y > sqrt(m + 1/4) - 3/2.
  - Bertrand gives a prime p in (floor(y/2), 2 floor(y/2)], so y/2 <= p <= y.
  - Q is nondecreasing. Hence Q(m) >= p+1 >= y/2 + 1 > sqrt(m)/2 + 1/4. ∎

**Lemma 1.2 (lower bound on K^Pi; repair of step 6).** Take rho = floor(S^{3/8}). Suppose the certificate's span bounds satisfy e_j <= E(j), where E(j) := (2j+2)^2 is the span of a Singer-derived Sidon set with j marks. (Admissible e_j are lower bounds on spans, so a certificate may use any admissible e_j <= the true minimum, which is <= E(j).) Then there are explicit c_1 > 0 and S_2 such that K^Pi(S) >= c_1 S^{3/4} for S >= S_2. Any c_1 < 2^{-1/4} · 2^{-1/2} ≈ 0.59 works for S large.

*Proof sketch* (the constants are elementary; I did not optimise S_2).
- For l <= S/2 - 1 we have v_l >= 2Q(S/2 - 1) >= V_0 := sqrt(S/2 - 1) + 1/2, by Lemma 1.1(b).
- If H <= V_0 (S/2 - 1), then P(H; v) <= sum_{lambda >= 0} (H - V_0 lambda)_+ <= H^2/(2V_0) + H.
- So the certificate fails, i.e. 2Pi(H) + 4E_rho <= S rho(rho+1), whenever H^2/V_0 + 2H + 4E_rho <= S rho^2.
- With H ≈ rho s, this reads s^2 <= V_0 S - O(V_0 s/rho) - O(V_0 E_rho/rho^2).
- Bound E_rho <= sum_{i<rho} (rho-i) E(i+1) = O(rho^4). Then V_0 E_rho/rho^2 = O(S^{1/2} S^{3/4}) = o(S^{3/2}).
- Hence the certificate fails at s = (1-o(1)) sqrt(V_0 S) ≈ 2^{-1/4} S^{3/4}, and H = rho s = O(S^{9/8}) <= V_0 S/2 for large S. ∎

With this, delta' >= delta/2 - O(S^{-1/8}) follows exactly as step 6 says. The dominant error is S/(300 rho K^Pi) = O(S^{1 - 3/8 - 3/4}) = O(S^{-1/8}). So step 6 holds once this lemma replaces the cited justification.

### 1.3 Caveat on the comparison base (not a flaw in logic; quantitative)

Step 6 measures the saving against 3 K^Pi(S; rho). The outer inequality uses U_d, built from the consumer's K, certified at the consumer's own rank. The saving against the consumer is

delta'_cons = delta' - (K^Pi(S; rho) - K_cons)/K_cons.

The safest fix is to run Theorem A at the consumer's own rank. The rho-dependent terms then stay negligible even for rho ~ 7e3: (rho+1)/(2K) ≈ 0.008 enters only multiplied by (1 - sqrt(alpha)), and S/(300 rho K) is about 2e-5.

A heuristic model (not a proof) for how K depends on the rank c:
- With v constant, K(c) ≈ sqrt(LV) + c/2 + sqrt(LV)/(2c).
- With v_l ≈ V sqrt(1 - l/L), the correction is -c/12.
- So K(c) ≈ sqrt(LV) + 5c/12 + K/(2c), which is optimal near c ≈ sqrt(6K/5) ≈ 740.
- On this model, rho ≈ 675 is near-optimal, and ranks around 7e3 cost about 0.5%. That is comparable to the target delta' ≈ 0.0115.

So the rank must be fixed explicitly, and the same rank must be used on both sides of the comparison.

---

## 2. Partial results on MS' (proved)

Notation: X_e = S_e(d), C_r(lambda) = sum_{l<=lambda} r(l), C_v(lambda) = sum_{l<=lambda} v_l.

**Per-fiber cap.** r_{X_e}(l) <= v_l. *Proof.* F_l(X_e) lies in [min F_d(D), max F_d(D) - l], an interval of span S-l. By (iv.2) it is the disjoint union of two Sidon sets. They cannot both contain both endpoints of the interval, so one of them lies in S-l consecutive integers. Since Q is monotone, r <= Q(S-l) + Q(S-l-1). ∎

**Proposition P1 (trivial range).** For every proper ternary source, every d with S >= 1, every delta in (0,1), and every lambda <= lambda_triv(S) := S / (600(sqrt(2S)+1)), MS' holds.

*Proof.* By Lemma 1.1(a), the left side is <= sum_{l<=lambda} 3 v_l <= 6 lambda Q(S) <= 6 lambda (sqrt(2S)+1) <= S/100. ∎

lambda_triv(S) ≈ sqrt(S)/849. At S = 2.2e7 it is about 5.5.

**Proposition P2 (slack transfer).** If MS' fails at (d, lambda) with constant delta, then for each e,

C_{r_e}(lambda) > (1-3delta) C_v(lambda) + S/100.

*Proof.* The total exceeds 3(1-delta) C_v + S/100. The other two classes contribute at most C_v each, by the per-fiber cap. ∎

**Lemma P3a (window cap).** Let Y be a subset of some class X = S_e(d), and suppose Y lies in m+1 consecutive integers. Then |Y| <= 1 + 2 sqrt(m (sqrt(2m)+1)).

*Proof.*
- By heredity (Lemma B1), F_g(Y) ⊆ F_g(X), and F_g(Y) lies in an interval of span <= m-g. The two Golomb classes of F_g(X) restrict to Sidon sets. So r_Y(g) <= 2Q(m) <= V := 2(sqrt(2m)+1).
- Let k = |Y|. The k-1 consecutive gaps of Y are positive integers summing to <= m, and each value g occurs at most r_Y(g) <= V times among them.
- Write k-1 = qV + t with 0 <= t < V. The minimal possible sum is V q(q+1)/2 + t(q+1). This is >= (k-1)^2/(2V): the difference equals Vq/2 + t - t^2/(2V) >= 0.
- So (k-1)^2 <= 2Vm. ∎

**Proposition P3 (size of a prefix-saturated class).** Suppose MS' fails at (d, lambda) with delta < 1/3, and S - lambda - 1 >= 6. Then each class satisfies

|X_e| > (1-3delta) lambda (sqrt(S-lambda-1) + 1/2) / (2 sqrt(lambda (sqrt(2lambda)+1))).

*Proof.*
- C_{r_e}(lambda) = #{(x,y) in X_e^2 : 0 < y-x <= lambda} <= |X_e| · 2 sqrt(lambda(sqrt(2lambda)+1)). Apply P3a with m = lambda to Y = X_e ∩ [x, x+lambda], and do not count x itself.
- v is nonincreasing, so C_v(lambda) >= lambda v_lambda >= 2 lambda Q(S-lambda-1) >= lambda (sqrt(S-lambda-1) + 1/2), by Lemma 1.1(b).
- Combine these with P2. ∎

For lambda << S the bound is about 0.42 (1-3delta) sqrt(S) lambda^{1/4}. At the critical lambda ~ S^{5/8} it is of order S^{0.656}.

So a counterexample family in the consumed range must exhibit three binary sources at one shift, each of size >> sqrt(S), each with fibers saturating the cap v_l for most l <= lambda. In particular, all six Golomb pieces must be near-maximal Sidon sets (entry 47). I know of no binary-source construction with size growing faster than about sqrt(S). Constructing a counterexample is therefore beyond any method I have.

**Remark (large lambda; sketch only, irrelevant to the chain).** For lambda >= theta S with theta ≈ 0.7, MS' follows from the capacity alone: C_r <= s^2/2 with s ≈ sqrt(2) S^{3/4}, against C_v(lambda) ≈ (4/3)(S^{3/2} - (S-lambda)^{3/2}). Making this explicit for all S needs Q(m) >= (1-o(1)) sqrt(m) with explicit error. That needs explicit short prime intervals (for example Schoenfeld's interval (x, x(1+1/16597)] for x > 2,010,760, cited from memory), and pushes S_0 to about 1e13. Theorem A uses only lambda <= Lambda_0 ~ S^{5/8}, so I did not complete this.

---

## 3. What remains open (precise)

**OPEN (MS'_crit).** There are explicit delta > 0 and S_0 such that, for every proper ternary source, every d with S >= S_0, and every lambda with lambda_triv(S) < lambda <= Lambda_0(S),

sum_{l<=lambda} sum_e r_{S_e(d)}(l) <= (1-delta) 3 C_v(lambda) + S/100.

- Here Lambda_0(S) is the least lambda with 3(1-delta) C_v(lambda) >= 3 rho (K^Pi(S)+1) + S/100, which is of order S^{5/8}.
- By P1, this is exactly the part of MS' that Theorem A consumes and that is not trivial.

**Why the available tools do not reach it** (from the proved record plus this round):
- Each single-lag layer can be exactly saturated at small m (entry 54).
- Disjoint near-maximal Sidon pieces are compatible lag by lag (entry 49).
- Uniformity of the individual pieces cannot help (translate obstruction, entry 48).
- Window or heredity arguments lose because the local cap K(lambda) ~ lambda^{3/4} is far weaker than the global fiber cap 2Q(S). P3 is the strongest consequence I could extract from them.

**Open sub-questions.**
- (a) Is there any binary source (a subset of some S_e(d) in a proper ternary source) of span S and size >= S^{1/2 + epsilon}? If every binary source had size O(S^{0.65}), then P3 would prove MS'_crit outright at lambda ~ S^{5/8}. It would not cover the whole range above lambda_triv.
- (b) TSD (entry 45) in its asymptotic form.
- (c) The director's finite-gadget mechanism (an unsatisfiable W(a)/W(b) configuration together with a counting lemma). I did not find a gadget.

No statement here is a bound on R_4. The chain gives R_4 consequences only conditionally on MS'_crit, with step 6 repaired by Lemma 1.2 and the rank fixed as in Section 1.3.

=== END OF ANSWER round5_q3 ===
