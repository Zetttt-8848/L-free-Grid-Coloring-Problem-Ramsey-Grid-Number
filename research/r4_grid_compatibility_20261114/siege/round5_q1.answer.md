# round5_q1 answer: MS' (joint prefix-averaged fibre deficit)

## Plan (written first)
1. Audit the chain MS' => (D-a) step by step.
2. Look for a simpler conversion that needs less than MS' (a single window scale).
3. Calibrate what MS' contains (window-energy identity).
4. Necessary conditions for a counterexample, with explicit constants.
5. State clearly what stays OPEN.

## 0. Verdict
- **MS' is NOT settled here** (neither proved nor refuted). It stays OPEN.
- Everything below is partial and is labelled. Proved results:
  - (Sec. 1) The chain MS' => (D-a) is valid in steps 1-5. Step 6 contains a **direction error**: an upper bound on v_l is used where a lower bound is needed. A corrected version is given. Its explicit S_1(delta) is about (1/delta)^8, which is far above the regime scale. So at the regime the numeric certificate value has to be used, as the step-6 bullet already allows.
  - (Sec. 2, Theorem B) A simpler, exact conversion. It needs the joint deficit at **one** window length Lambda only, in the summed form M_w(Lambda) <= 3 alpha M_v(Lambda) + E. It gives an explicit delta' of about delta/2. It needs no Pi-form recertification: the comparison cap is exactly the P-form cap at the same rank. MS' implies its hypothesis.
  - (Sec. 3) Window-energy identity. The hypothesis of Theorem B equals (class sizes)^2 term + (local variance) term. So for well-spread classes, MS' at the critical scale is **equivalent** to the size deficit it is meant to give. A prefix formulation does not make the problem easier.
  - (Sec. 4, Proposition N) Any failure of MS' with delta <= 1/6 and S >= 146 forces **all three** classes S_e(d) to have more than S^{5/8}/16 elements. MS' holds trivially for lambda <= S/(600 delta (sqrt(2S)+1)).

Conventions used throughout. C_w(lambda) = sum_{l<=lambda} w_l with w_l = sum_e r_{S_e(d)}(l). C_v likewise. C(0) = 0. Also
M_w(Lambda) := sum_{lambda=0}^{Lambda-1} C_w(lambda) = sum_{l=1}^{Lambda-1} (Lambda-l) w_l, and M_v likewise.
Rank rho, span lower bounds e_j, E_rho = sum_{i=0}^{rho-1}(rho-i)e_{i+1}, and Phi := S rho(rho+1) - 4E_rho.
F1 (summed rank inequality, quoted input) reads 2P(H_tot; w) <= 3 Phi. F4 (single class) reads 2P(H;v) <= Phi.

**Input check: the cap v_l.** Every class X = S_e(d) satisfies r_X(l) <= v_l = Q(S-l) + Q(S-l-1). This is an established input of the brief; here is a one-line proof.
F_l(X) lies in [m, m+S-l], where m = min F_d(D). It splits into two disjoint Sidon sets (Golomb split, P1 (iv.2)). At most one of them contains m, so the other lies in [m+1, m+S-l]. Hence the bound is Q(S-l) + Q(S-l-1). ∎

## 1. Audit of the chain MS' => (D-a)

**Steps 1-5 are correct.** I re-derived Theorem A's algebra:
- the second branch, times rho, minus 3rho(rho+1)/2, minus E_0, equals 3 sqrt(alpha) H*;
- the chain P(H_tot;w) >= 3 alpha Pi((H_tot-E_0)/(3alpha)) >= 3 alpha Pi(H*/sqrt alpha) >= 3 Pi(H*);
- the delta' formula of step 5.

All of these check. Monotonicity in S, which is needed to pass from S_c = span F_d(D_c) to n-d-1, also holds. Larger S makes every v_l larger (Q is nondecreasing) and the right side S rho(rho+1) larger, so the certificate becomes harder to satisfy. Hence K^Pi(S) and both branches are nondecreasing in S.

Two bookkeeping points in step 5 must be stated:
- if S_c < S_0, then MS' does not apply, and that colour contributes only the trivial 3K(S_0) (additive, negligible);
- passing from 4 * 3K(n-d-1) to U_d gives up the staggering. The brief says this is negligible (estimate).

**Step 6 has a direction error (FLAW, fixable).** Step 6 derives the lower bound K^Pi(S) >= c_1 S^{3/4} "from v_l <= 2Q(S) <= 2(sqrt S + S^{1/4} + 1)". That cannot work.
- K^Pi(S) is the largest s at which the certificate fails, that is, 2 Pi(H*) + 4E_rho <= S rho(rho+1).
- Making v larger makes Pi smaller. So an **upper** bound on v gives a lower bound on Pi. That shows the certificate *succeeds*, which is an **upper** bound on K^Pi.
- A lower bound on K^Pi needs a **lower** bound on v_l (hence on Q) and an **upper** bound on E_rho.

Corrected version (proved; I state it for the P-form cap K^flat of Sec. 2, which is <= K^Pi, so it also bounds K^Pi from below):
- (Q1) Q(m) >= sqrt(m/8) for m >= 72.
  - Proof: put x = sqrt(m/8) >= 3. Bertrand (cited) gives a prime p with x < p <= 2x, so p >= 5.
  - The Erdos-Turan set A_p = {2pk + (k^2 mod p) : 0 <= k < p} is Sidon. Proof: if a_i + a_j = a_k + a_l, then the residues add to less than 2p, so r_i + r_j = r_k + r_l and i + j = k + l. Then i^2 + j^2 ≡ k^2 + l^2, so ij ≡ kl (mod p), and {i,j} = {k,l} as root pairs of the same quadratic. The case i = j covers 3-APs.
  - A_p lies in [0, 2p^2-p-1] ⊆ [0, 8x^2] = [0, m]. ∎
- (E1) Every valid span lower bound satisfies e_j <= 8j^2.
  - Proof: a Sidon set is a binary source, because its strict source contains no L at all.
  - Take the first j elements of A_p, with p in [j, 2j]; their span is < 2p^2 <= 8j^2. Then e_j cannot exceed the minimum span, which is at most this value.
  - Consequently 4E_rho <= 32 rho^4.
- (K1) Let S >= 1490 and rho = floor(S^{3/8}/12). Then K^flat(S) >= floor((S-2)^{1/4} S^{1/2}/2) >= S^{3/4}/3.
  - Proof: for l <= S/2 we have v_l >= 2Q(S-l-1) >= V := sqrt(S-2)/2, by (Q1). Hence C_v(lambda) >= V lambda for lambda <= S/2.
  - Therefore, for H <= V floor(S/2): P(H;v) <= sum_{lambda>=0} (H - V lambda)_+ <= H + H^2/(2V).
  - So s is not excluded at rank rho if 2 rho s + rho^2 s^2/V <= S rho^2 - 32 rho^4, i.e. if s^2/V + 2s/rho + 32 rho^2 <= S.
  - Take s = floor(sqrt(VS/2)), so that s^2/V <= S/2. With the stated rho one checks 32 rho^2 <= S/4 and 2s/rho <= 24 S^{3/8} <= S/4; the latter holds for S >= 1490. Also rho s <= V floor(S/2). ∎
- **Consequence.** With Theorem B below, the delta' error terms are:
  - (rho+1)/(2K^flat) = O(S^{-3/8});
  - S/(300 rho K^flat) <= 0.24 S^{-1/8}.
  So delta' >= delta/4 once 0.24 S^{-1/8} <= delta/4 - O(S^{-3/8}), roughly S >= (1.2/delta)^8.
  - For delta = 0.023 this is about 5*10^13. That is **far above** the regime S ≈ 2.2*10^7.
  - So the asymptotic step 6 is irrelevant at the regime scale. There one must evaluate delta' from the actual certificate numbers, as the step-6 bullet allows.
  - Estimate (not computed exactly): with rho ≈ 700 and K ≈ 4.58e5, S/(300 rho K) ≈ 2.3e-4, so delta' ≈ delta/2 - 2.3e-4.
- **Rank bookkeeping.** The comparison cap must be the certificate at the rank actually used by the consumer.
  - Theorem A's orientation (rho ≈ 7e3, saturation to lambda ≈ 3.5e5) and step 6 (rho ≈ 675) disagree. My estimate of the optimal rank in the saturated model is rho ≈ (vS)^{1/4} ≈ 700.
  - Any fixed rho gives a valid cap. Theorem B gives delta' relative to the P-form cap at that same rho, so no further correction is needed.

## 2. Theorem B: a single-window conversion (PROVED, given F1 and F4)

**Lemma B0 (linear duality for P).** Let w_l >= 0 and 0 <= H <= sum_l w_l. Then for every integer Lambda >= 1,
`P(H; w) >= Lambda H - M_w(Lambda)`, and `P(H; w) = max_{Lambda >= 1} (Lambda H - M_w(Lambda))`.

*Proof.* By the prefix formula, P = sum_{lambda>=0} (H - C_w(lambda))_+. This is >= sum_{lambda=0}^{Lambda-1} (H - C_w(lambda)) = Lambda H - M_w(Lambda), because (y)_+ >= y and the dropped terms are >= 0.

C_w is nondecreasing. So the partial sums sum_{lambda<Lambda}(H - C_w(lambda)) grow exactly while C_w(lambda) < H. The maximum is therefore attained at Lambda = #{lambda >= 0 : C_w(lambda) < H}, where it equals P. (This count is >= 1, since C_w(0) = 0 < H when H > 0. The case H = 0 is trivial.) ∎

**Definition.** For Lambda >= 1 put
`K^lin(Lambda) := (rho+1)/2 + (Phi/2 + M_v(Lambda)) / (rho Lambda)`, and `K^flat(S) := inf_{Lambda >= 1} K^lin(Lambda)`.

**Lemma B1' (K^flat is exactly the P-form cap).** A binary source of span <= S and size s > rho satisfies s <= K^flat(S). Conversely, a real s > rho passes the P-form test 2P(rho s - rho(rho+1)/2; v) <= Phi iff s <= K^lin(Lambda) for every Lambda.

*Proof.* By F4 and Lemma B0, 2(Lambda H - M_v(Lambda)) <= Phi for every Lambda, with H = rho s - rho(rho+1)/2. Solving for s gives s <= K^lin(Lambda). The converse is the "max" half of B0. ∎

So K^flat is the consumer's own rank-rho cap. No Pi-form and no recertification is needed.

**Theorem B.** Fix a proper ternary source, a shift d with span S, a rank rho >= 1, and Lambda >= 1, alpha in (0,1], E >= 0. Assume the single-window hypothesis

`WE(Lambda; alpha, E):   M_w(Lambda) <= 3 alpha M_v(Lambda) + E`, i.e. `sum_{l<Lambda} (Lambda-l) sum_e r_{S_e(d)}(l) <= 3 alpha sum_{l<Lambda} (Lambda-l) v_l + E`.

Then, with s = sum_e |S_e(d)|,

`s <= max{ 2 max(rho, K^flat) + rho ,  3 K^lin(Lambda) - (3(1-alpha) M_v(Lambda) - E) / (rho Lambda) }`.

*Proof.*
- If some class has size <= rho, then the other two have size <= max(rho, K^flat) by B1'. This gives the first branch.
- Otherwise F1 applies. Using B0 for w, then WE:
  3 Phi >= 2P(H_tot; w) >= 2 Lambda H_tot - 2M_w(Lambda) >= 2 Lambda H_tot - 6 alpha M_v(Lambda) - 2E.
- Substitute H_tot = rho s - 3rho(rho+1)/2 and divide by 2 rho Lambda. This gives
  s <= 3(rho+1)/2 + (3Phi/2 + 3 alpha M_v(Lambda) + E)/(rho Lambda) = 3K^lin(Lambda) - (3(1-alpha)M_v(Lambda) - E)/(rho Lambda). ∎

**Corollary B2 (explicit delta').** Let Lambda_c >= 2 be an integer minimizer of K^lin, assuming one exists; otherwise use any Lambda and the general formula. Then, whenever min_e s_e > rho,

`s <= (1 - delta') 3 K^flat`, with `delta' = (1-alpha)(1 - 1/Lambda_c)(1 - (rho+1)/(2K^flat))/2 - E/(3 rho Lambda_c K^flat)`.

*Proof.* Put g(Lambda) = (Phi/2 + M_v(Lambda))/Lambda.
- Minimality gives g(Lambda_c) <= g(Lambda_c + 1). Since M_v(Lambda+1) = M_v(Lambda) + C_v(Lambda), this is equivalent to Phi/2 + M_v(Lambda_c) <= Lambda_c C_v(Lambda_c), that is, g(Lambda_c) <= C_v(Lambda_c).
- v is nonincreasing (F3), so C_v is concave with C_v(0) = 0. Hence C_v(lambda) >= (lambda/Lambda) C_v(Lambda) for lambda <= Lambda, and M_v(Lambda) >= (Lambda-1) C_v(Lambda)/2.
- So M_v(Lambda_c)/Lambda_c >= (1 - 1/Lambda_c) g(Lambda_c)/2.
- Also rho K^flat = rho(rho+1)/2 + g(Lambda_c), so g(Lambda_c)/(rho K^flat) = 1 - (rho+1)/(2K^flat).
- Insert these into Theorem B. ∎

**Relation to MS' and to Theorem A.**
- MS' implies WE(Lambda; 1-delta, (Lambda-1)S/100) for every Lambda: sum MS' over lambda = 1..Lambda-1.
- Then E/(3 rho Lambda K^flat) <= S/(300 rho K^flat), and delta' ≈ delta/2 minus the same error terms as in Theorem A. This confirms step 5 by a shorter route.
- The factor 1/2 is again intrinsic: in the saturated model M_v(Lambda_c)/Lambda_c ≈ g/2.
- **The hypothesis actually needed is one inequality, at the one scale Lambda_c**, the crossing point of the single-class certificate. Estimate: Lambda_c ≈ sqrt(Phi/v) ≈ rho sqrt(S/v), about 3.4e4 at rho ≈ 700 in the regime.
- MS' (all lambda in [1,S], pointwise prefixes) is much stronger than this. **Recommended target:** WE(Lambda_c(S); 1-delta, Lambda_c S/100), or WE on a short range of Lambda around Lambda_c.
- In Corollary B2, the overall bound is s <= max{2 max(rho,K^flat) + rho, (1-delta') 3K^flat}.

## 3. What MS' contains: the window-energy identity (PROVED)

**Lemma W1.** Let X ⊆ [m, m+S] be finite with |X| = s and Lambda >= 1. Put a(x) = |X ∩ [x, x+Lambda)|. The windows that meet X have x in [m-Lambda+1, m+S], and there are S+Lambda of them. Put abar = Lambda s/(S+Lambda). Then

`sum_x a(x)^2 = Lambda s + 2 M_{r_X}(Lambda)`, and hence
`2 M_{r_X}(Lambda) = Lambda^2 s^2/(S+Lambda) - Lambda s + Var_Lambda(X)`, where `Var_Lambda(X) = sum_{x=m-Lambda+1}^{m+S} (a(x) - abar)^2 >= 0`.

*Proof.* sum_x a(x)^2 = sum_{p,q in X} #{x : p,q in [x,x+Lambda)} = sum_{p,q} (Lambda - |p-q|)_+ = Lambda s + 2 sum_{l=1}^{Lambda-1} (Lambda-l) r_X(l). The second identity is the variance decomposition, using sum_x a(x) = Lambda s. ∎

**Proposition E (WE splits into a size part and a dispersion part).** For the three classes X_e = S_e(d) of sizes s_e, all in an interval of span S, the hypothesis WE(Lambda; alpha, E) is equivalent to

`sum_e [ Lambda^2 s_e^2/(S+Lambda) + Var_Lambda(X_e) ] <= 6 alpha M_v(Lambda) + Lambda s + 2E`.

Consequences:
- (E-a) **WE alone already caps the sizes** by Cauchy-Schwarz (drop Var). Using M_v(Lambda) <= Q(S) Lambda(Lambda-1):
  sum_e s_e^2 <= (S+Lambda)(s/Lambda + 6 alpha Q(S) + 2E/Lambda^2).
  In the regime this gives s <= sqrt(3 sum s_e^2) ≈ 3 sqrt(alpha) sqrt(2Q(S) S) ≈ 3 sqrt(alpha) K. This is a cruder relative of Theorem B.
- (E-b) **Conversely, for equidistributed classes WE is the size bound itself.** If Var_Lambda(X_e) <= eta Lambda^2 s_e^2/(S+Lambda) for each e, then WE(Lambda; alpha, E) holds as soon as
  (1+eta) sum_e s_e^2 <= (S+Lambda)(6 alpha M_v(Lambda) + 2E)/Lambda^2.
  Hence any proof of MS' (or of WE at Lambda ≈ Lambda_c) contains a proof that well-spread triples of binary sources have sum_e s_e^2 <= (1+o(1)) 6 alpha M_v(Lambda_c) S/Lambda_c^2. In the regime, that is a size deficit of the very kind (D-a) asks for.

**Interpretation (calibration, not a theorem).**
- The prefix/window formulation does **not** reduce the problem. It is (D-a) plus a dispersion term.
- It is the natural currency only for *local* proofs: lag-by-lag deficits at lags <= Lambda_c.
- Any such local proof must be strong enough to give the global size deficit for equidistributed classes.
- By Lemma E of entry 48, near-maximal Sidon pieces are equidistributed. So near-extremal configurations are exactly the case in which (E-b) applies.

## 4. Partial results on MS' itself (PROVED)

**Lemma T (trivial range).** MS' holds, for every delta in (0,1), at every lambda <= S/(600 delta (sqrt(2S)+1)).

*Proof.*
- w_l <= 3v_l, so C_w(lambda) <= (1-delta) 3C_v(lambda) + 3 delta C_v(lambda).
- v_l <= 2Q(S), and Q(S) <= 1/2 + sqrt(2S+1/4) <= sqrt(2S) + 1. The middle bound holds because k Sidon points in [0,S] have k(k-1)/2 distinct positive differences, all <= S.
- Hence 3 delta C_v(lambda) <= 6 delta lambda (sqrt(2S)+1) <= S/100. ∎

**Lemma K0 (elementary local cap).** Every binary source Y of span <= lambda (lambda >= 1) has |Y| <= 1 + 2 sqrt(lambda Q(lambda)) <= 1 + 3.108 lambda^{3/4}.

*Proof.*
- The |Y|-1 consecutive gaps of Y are positive integers summing to <= lambda.
- The gaps equal to g are pairs at lag g, so there are at most r_Y(g) <= 2Q(lambda) of them (Golomb split; both Sidon parts lie in an interval of <= lambda+1 integers).
- H positive integers, each value used at most V times, have sum >= H^2/(2V). (Write H = kV + r, 0 <= r < V. The minimum is V k(k+1)/2 + r(k+1), which exceeds H^2/(2V) by Vk/2 + r - r^2/(2V) >= 0.)
- So (|Y|-1)^2 <= 4 lambda Q(lambda). Finally Q(lambda) <= sqrt(2 lambda) + 1 <= (sqrt 2 + 1) sqrt(lambda), and 2 sqrt(sqrt 2 + 1) < 3.108. ∎

**Proposition N (a counterexample needs three large binary sources).** Let 0 < delta <= 1/6 and S >= 146. Suppose MS' fails at (d, lambda), that is,
C_w(lambda) > (1-delta) 3 C_v(lambda) + S/100. Then **every** class X_e = S_e(d) satisfies

`|X_e| > ((1-3delta) C_v(lambda) + S/100) / (3.108 lambda^{3/4})`, and in particular `|X_e| > S^{5/8}/16`.

Each X_e is a binary source contained in an interval of S+1 integers (heredity, Lemma B1).

*Proof.*
- (Transfer, Lemma 3.1(a) with slack.) Each class has C_{r_e}(lambda) <= C_v(lambda), because r_X(l) <= v_l. Hence C_{r_e} > (3-3delta)C_v + S/100 - 2C_v = (1-3delta)C_v + S/100.
- (Upper count.) C_{r_X}(lambda) = sum_{a in X} (|X ∩ [a, a+lambda]| - 1). Each X ∩ [a, a+lambda] is a binary source of span <= lambda (heredity and translation invariance of L's). So by K0, C_{r_X}(lambda) <= 3.108 |X| lambda^{3/4}. This gives the first bound.
- (Lower count, lambda <= S/2.) For l <= lambda we have S-l-1 >= S/2 - 1 >= 72. So by (Q1) of Sec. 1, v_l >= 2Q(S-l-1) >= sqrt(S-2)/2, and C_v(lambda) >= lambda sqrt(S-2)/2.
  - With 1 - 3delta >= 1/2: |X| > (a lambda^{1/4} + b lambda^{-3/4})/3.108, where a = sqrt(S-2)/4 and b = S/100.
  - By AM-GM on three copies of a lambda^{1/4}/3 and one copy of b lambda^{-3/4}, this is >= 4 * 3^{-3/4} a^{3/4} b^{1/4}/3.108 >= 0.0631 (S-2)^{3/8} S^{1/4}.
  - For S >= 146, (S-2)^{3/8} >= 0.9948 S^{3/8}. So the bound is > 0.0628 S^{5/8} > S^{5/8}/16.
- (lambda > S/2.) C_v(lambda) >= C_v(floor(S/2)) >= (S-1) sqrt(S-2)/4 and lambda^{3/4} <= S^{3/4}. Dropping S/100:
  |X| > (S-1) sqrt(S-2)/(8 * 3.108 S^{3/4}) >= S^{3/4}/26 >= S^{5/8}/16, since S^{1/8} >= 1.625 for S >= 49. ∎

**Corollary N1 (sufficient condition for MS').** Fix delta <= 1/6 and suppose that, for some S >= 146, every binary source contained in S+1 consecutive integers has at most S^{5/8}/16 elements. Then MS' holds at that S, for every d and every lambda. Proof: the contrapositive of N.

**Reading of N.**
- Refuting MS' requires, at arbitrarily large S, three disjoint binary sources (the three classes at one shift) of size > S^{5/8}/16 each.
- At the scale lambda ≈ S they must be of size ≈ S^{3/4}.
- The brief mentions no known construction of binary sources beyond span^{1/2+o(1)}: Sidon sets, the lifted digit families, and the 12-point m=23 instance. So no refutation is within reach of the known constructions.
- Conversely, an upper bound K_true(S) <= S^{5/8}/16 would prove MS', but it would also improve the consumer directly and by far. So N gives no proof route.
- At the regime, S^{5/8}/16 ≈ 2.4e3, far below K ≈ 4.6e5. N is a structural statement, not a regime statement.
- Hedge on the third bullet: I know of no family of binary sources of size >= span^{1/2+epsilon}, and the brief cites none. I have not proved that none exists.

## 5. The gadget route: a necessary feature (PROVED)

This concerns the single-lag W-structure of entry 43, with all three diagonal colours. Give each point p in W its type (cls(p), diag(p)), where diag(p) = kappa(p,p).

The unary domain of a pair p < q is D_pq = P minus {f, if diag(p) = diag(q) = f} minus {e, if cls(p) = cls(q) = e}. These unary domains come from Lemma W(a) with x = 0 and from Lemma W(b). Every D_pq is nonempty, and |D_pq| = 1 iff p and q have the same type.

**Lemma G.** Take one additive quadruple P1 < P2 <= P3 < P4 in W with P1 + P4 = P2 + P3, and keep only its two Lemma-W(a) constraints, T1 = {k12, k34, k14} and T2 = {k13, k24, k14}, together with the unary domains. This system is unsatisfiable iff all four points have the same type. When P2 = P3 there is one constraint, and the same statement holds.

*Proof.*
- The cells k12, k34, k13, k24 each occur in only one constraint.
- Fix k14 = gamma. Then T1 fails for every choice iff D12 = D34 = {gamma}, and T2 fails for every choice iff D13 = D24 = {gamma}.
- Case |D14| >= 2. Unsatisfiability needs both kinds of failure, one for each of two values gamma_1 != gamma_2. Then P1~P2 and P1~P3 have the same type, so all four points share one type and gamma_1 = gamma_2, a contradiction.
- Case |D14| = 1. Then P1~P4 have the same type. Failure needs P1~P2 and P3~P4, or P1~P3 and P2~P4, of the same type. Either way all four points share one type.
- The converse is the Sidon property of a single type. ∎

**Consequences.**
- A forbidden finite gadget of the kind the director's sketch asks for must involve at least two overlapping additive relations that share cells. In the full source it may instead involve cells outside the lag-l W-structure.
- Entry 43 already showed that no mixed U-structure pattern is forbidden. Lemma G extends this to the full three-colour W-structure for single quadruples.
- I did not find a forbidden multi-relation gadget. That remains OPEN.

## 6. What remains OPEN (explicit)
1. **MS'** itself, as stated: OPEN. Neither a proof nor a counterexample is given here.
2. **The weaker, sufficient target WE(Lambda_c)** of Sec. 2: OPEN. It needs the inequality only at the single window scale Lambda_c(S). By Sec. 3 it is equivalent, for equidistributed classes, to a size deficit sum_e s_e^2 <= (1-delta)(1+o(1)) * (saturated value).
3. Whether binary sources of size >= span^{1/2+epsilon} exist. A family with size > S^{5/8}/16 is necessary for any counterexample (Prop. N).
4. TSD and the AABA question of earlier entries: still OPEN. They are not touched here, beyond Lemma G.

## 7. Status table
- PROVED here:
  - the audit of steps 1-5, which are correct;
  - the step-6 flaw and its correction (Q1, E1, K1);
  - Lemma B0, Lemma B1', Theorem B, Corollary B2;
  - Lemma W1 and Proposition E;
  - Lemma T, Lemma K0, Proposition N, Corollary N1;
  - Lemma G.
- CITED from memory: Bertrand's postulate, and the Erdos-Turan Sidon construction (whose proof is reproduced). Also the brief's established inputs: F1, F4, the prefix formula, the Golomb split and heredity.
- ESTIMATES (not proved): the regime values (rho ≈ 700, Lambda_c ≈ 3.4e4, delta' ≈ delta/2 - 2.3e-4) and the remark that S_1 ≈ (1.2/delta)^8.
- No claim about R_4 is made. Every R_4 consequence remains conditional on MS' or on WE(Lambda_c).

=== END OF ANSWER round5_q1 ===





