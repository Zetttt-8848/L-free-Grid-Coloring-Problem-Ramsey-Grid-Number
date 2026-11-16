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



