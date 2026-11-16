# round5_q2 answer: attempt on MS' (joint prefix-averaged fiber deficit with additive slack)

## 0. Verdict

**MS' is neither proved nor refuted here. It remains OPEN.** This file contains:

1. an audit of the chain MS' => (D-a). The chain is sound, with three repairable gaps (A1-A3, Section 1). None of them is structural;
2. rigorous partial results (Section 2):
   - the exact parameter window in which MS' still has content;
   - a necessary-size lemma for any counterexample;
   - an inscribed-pair rule for binary sources, with its cross-lag corollary;
   - an explicit difference-coverage lemma for Sidon sets;
3. the obstruction met, including a correction to the director's cross-lag heuristic (Section 3), and the open questions (Section 4).

Nothing here is a bound on R_4.

Conventions are those of the query. X_e = S_e(d). Y = F_d(D), of span S. C_u(lambda) = sum_{l<=lambda} u_l. w_l = sum_e r_{X_e}(l). Q is the true Sidon cap of the query.

## 1. Audit of the chain MS' => (D-a)

I re-derived Theorem A step by step:
- the reduction to the prefix formula;
- Lemma A1(a)-(c);
- the algebra of the second branch (rho times the branch, minus 3rho(rho+1)/2, minus E_0, equals 3 sqrt(alpha) H*);
- the treatment of lambda > Lambda_0;
- the final contradiction with the Pi-certificate.

All of these are correct. The delta' of step 5 is also correct: divide both branches by 3K^Pi. The asymptotics of step 6 are right: with K^Pi ~ S^{3/4} and rho ~ S^{3/8}, the slack term S/(300 rho K^Pi) is of order S^{-1/8}. The regime value S/(300·675·4.58e5) ≈ 2.4e-4 matches the stated 2.5e-4.

Three points must be repaired or made explicit.

**A1 (computability of the certificate).** MS' is stated with the true Q, which is not known exactly. If Theorem A is run with the true v, then K^Pi(S) and delta' are not computable numbers.

Repair: run Theorem A with a certified, monotonized upper profile. Take Q^+ >= Q, nondecreasing; for example, the certified Golomb table together with Lindstrom's bound, cited from memory: a Sidon subset of [1,n] has at most n^{1/2} + n^{1/4} + 1 elements. Put v^+_l = Q^+(S-l) + Q^+(S-l-1).
- v^+ is nonincreasing, so its piecewise-linear prefix C~ is concave and Lemma A1 holds.
- F4 holds with v^+, because r_X(l) <= v_l <= v^+_l.
- MS' with v implies MS' with v^+ (same alpha and E_0), because C_v <= C_{v^+}.

So the chain should read "MS' (true Q) => hypothesis of Theorem A for v^+". The certificate K^Pi is then a computable number. Step 6 already uses Lindstrom's bound, so it implicitly uses v^+.

**A2 (which K is being beaten).** Step 5 gives sum_e |S_e(d)| <= (1-delta') 3 K^Pi_rho(S), where K^Pi_rho is the Pi-form certificate *at the chosen rank rho*. The outer inequality uses U_d built from the consumer's certified K, which may be optimized over the rank and may use other refinements.
- The saving is real only if K^Pi_rho(S) <= (1+eps) K_consumer(S) with eps much smaller than delta'.
- Corollary A2 quotes a relative gap of about 1e-5 between the Pi-form and the P-form *at the same rank*. That does not cover a change of rank. The query says rho = floor(K^{1/2}) ≈ 675, while entry 42 uses rho ≈ 7e3.
- Repair: recertify K at the rho actually used, or take rho equal to the consumer's rank. The cost is a longer prefix: Lambda_0 grows linearly with rho. See Proposition 2.1(c).

This is a numerical item, not a structural flaw. Until it is computed, "delta' >= 0.4996 delta - 2.5e-4" is relative to K^Pi_675, not to the consumer's K.

**A3 (monotonicity and feeding U_d; now proved).** To feed the outer inequality, the chain needs K^Pi_rho(S_c(d)) <= K^Pi_rho(n-d-1) whenever S_c(d) <= n-d-1.

*Proof.* For fixed l, v^+_l(S) is nondecreasing in S. So C~ is pointwise nondecreasing in S, Pi(H) is nonincreasing in S, and the right side S rho(rho+1) is increasing. Hence if the certificate fails at (s, S), it fails at (s, S') for every S' >= S. So K^Pi_rho(S) <= K^Pi_rho(S'). ∎

Shifts with S_c(d) < S_1 contribute at most 3K^Pi(S_1), an absolute constant. Replacing the staggered sum by 4·3K^Pi(n-d-1) loses the staggering, which is negligible (as the query says; estimate).

**Conclusion of the audit.** Given MS' with explicit (delta, S_0), the chain yields (D-a) with explicit delta'(S), subject to A1 (proved above), A2 (a numerical recertification) and step 6 (elementary, still to be written). Only the prefix lambda <= Lambda_0 is used. At the regime this is about 7 sqrt(S) for rho = 675, and about 73 sqrt(S) for rho ≈ 7e3 (estimates).

## 2. Rigorous partial results (all PROVED)

### 2.1 The window in which MS' has content

**Proposition 2.1.** Fix a proper ternary source, a shift d, and delta in (0,1].

(a) For every e and l >= 1, r_{X_e}(l) <= v_l. Hence w_l <= 3v_l and C_w <= 3C_v.

(b) The MS' inequality holds, for this delta and every S >= 1, at every lambda <= lambda_triv := S/(600 delta Q(S)).

(c) Theorem A consumes MS' only for lambda <= Lambda_0. Here Lambda_0 is the least lambda with 3 alpha C_v(lambda) >= 3 rho s* + E_0. Since C_v(lambda) >= lambda v_lambda, we get Lambda_0 <= (3 rho s* + E_0)/(3 alpha v_{Lambda_0}).

*Proof.* (a) F_l(X_e) lies in [min Y, max Y - l], an interval of S-l+1 integers. By (iv.2) it is the union of two disjoint Sidon sets. They cannot both contain the left endpoint, so one of them lies in S-l consecutive integers. Hence r_{X_e}(l) <= Q(S-l) + Q(S-l-1) = v_l.

(b) By (a), C_w(lambda) <= (1-delta) 3C_v(lambda) + 3 delta C_v(lambda). Since Q is nondecreasing, v_l <= v_1 <= 2Q(S), so 3 delta C_v(lambda) <= 6 delta lambda Q(S). This is at most S/100 when lambda <= lambda_triv.

(c) This is the definition of Lambda_0, together with the fact that v is nonincreasing. ∎

**At the regime (estimates).** Take delta = 0.0235, which by step 5 gives delta' ≈ 0.0115.
- lambda_triv ≈ sqrt(S)/(600·0.0235) ≈ 0.07 sqrt(S) ≈ 330.
- Lambda_0 ≈ 3.4e4 ≈ 7 sqrt(S) for rho = 675.

So the entire content of MS' used by the chain lies in **0.07 sqrt(S) < lambda <= 7 sqrt(S)**, a range of two decades of lags at the scale sqrt(S). The query's phrase "about sqrt(S)/600" is the delta = 1 value. For small delta the slack covers up to sqrt(S)/(600 delta).

### 2.2 What a counterexample must contain

**Proposition 2.2.** Let delta < 1/3, and suppose MS' fails at (d, lambda). Then lambda > lambda_triv, and for each e:

(a) C_{r_{X_e}}(lambda) > (1-3delta) C_v(lambda) + S/100;

(b) |X_e| · (M_lambda(X_e) - 1) >= C_{r_{X_e}}(lambda), where M_lambda(X) = max_u |X ∩ [u, u+lambda]|;

(c) M_lambda(X_e) <= K*(lambda), the largest size of a binary source of span <= lambda. Hence
|X_e| > ((1-3delta) C_v(lambda) + S/100) / (K*(lambda) - 1).

*Proof.*
- (a) We have C_w > 3(1-delta) C_v + S/100, and C_{r_{X_{e'}}} <= C_v for the other two classes by 2.1(a).
- (b) C_{r_X}(lambda) counts pairs a < b in X with b - a <= lambda. For each a, the partners b lie in X ∩ (a, a+lambda], and there are at most M_lambda - 1 of them.
- (c) By heredity (Lemma B1), X_e ∩ [u, u+lambda] is a binary source of span <= lambda. ∎

So a counterexample needs, in **each** of the three classes, about (1-3delta) of the full fiber budget summed over lags up to more than sqrt(S)/(600 delta). By Lemma 3.1(b) of entry 47, all six Golomb pieces must be near-maximal Sidon sets on average over those lags.

I know of no construction of a binary source in which even one class has fibers r_X(l) >= c·v_l for all l up to C sqrt(S) with C large. This is from memory and is not a proof of non-existence. Such a construction would need size of order S^{3/4}, the order of K itself. So refuting MS' requires first solving the open lower-bound problem for binary sources near the rank-certificate scale.

The size requirement can be made explicit. Rigorously, (c) together with C_v(lambda) >= lambda v_lambda gives |X_e| >~ (1-3delta)·2 sqrt(S)·lambda / K*(lambda). This is of order sqrt(S)·lambda^{1/4}, i.e. at least about S^{5/8} for lambda of order sqrt(S), using K*(lambda) = O(lambda^{3/4}) from the rank inequality. For a class spread evenly over its span, the heuristic order is S^{3/4}.

### 2.3 The inscribed-pair rule for binary sources

Let (X, psi) be a binary source: a finite X ⊂ Z and psi on pairs a<b of X with values in a 2-element palette {f, fbar}, such that there are no a<c and t>0 with a, a+t, c, c+t in X and psi(a,a+t) = psi(c,c+t) = psi(a,c+t). For a class X_x = S_x(d), psi(a,b) = chi(b+d,a) and {f, fbar} = P \ {x}; this is (iv.0) together with Lemma B1. For p<y in X put

    I(p,y) = {t : 0 < t < y-p, p+t in X, y-t in X}.

**Lemma 2.3 (inscribed-pair rule).** psi is proper iff for every p<y in X and every t in I(p,y),

    NOT ( psi(p,p+t) = psi(y-t,y) = psi(p,y) ).

Equivalently, for each pair (p,y), every inscribed pair (p,p+t),(y-t,y) whose two colours agree has the colour opposite to psi(p,y).

*Proof.* Put a = p, c = y-t; then a < c iff t < y-p. The triple (a,a+t),(c,c+t),(a,c+t) is (p,p+t),(y-t,y),(p,y). Every triple in the definition of properness arises exactly once in this way, from (p,y) = (a,c+t). ∎

**Corollary 2.4 (parallel-pair agreement and Golomb-class transport).** Write Z_j(l) = {u : u, u+l in X, psi(u,u+l) = j}. These are the two Golomb classes of F_l(X).

(a) Let p, p+l, p+g, p+l+g lie in X, with l, g >= 1 (l = g allowed). If psi(p,p+l) = psi(p+g,p+g+l) = j and psi(p,p+g) = psi(p+l,p+l+g) = j', then j = j', and psi(p,p+l+g) is the other colour.

(b) Transport: Z_j(l) ∩ (Z_j(l) - g) ⊆ Z_{jbar}(l+g) for all l, g >= 1.

(c) Cross-lag consistency: for each m >= 2, the sets T_j(m) := union over 1<=l<m of Z_j(l) ∩ (Z_j(l) - (m-l)) satisfy T_j(m) ⊆ Z_{jbar}(m), and T_0(m) ∩ T_1(m) = ∅. Hence |T_0(m)| + |T_1(m)| <= r_X(m) <= v_m.

*Proof.*
- (a) Apply Lemma 2.3 to (p, y = p+l+g) with t = l and with t = g; both lie in I(p,y). Neither inscribed pair can have the colour kappa = psi(p,y), so j ≠ kappa and j' ≠ kappa. With two colours, j = j' = kappa-bar.
- (b) If p, p+g are in Z_j(l), apply Lemma 2.3 to (p, p+g+l) with t = l. This gives psi(p, p+l+g) ≠ j. The pair (p, p+l+g) is in X, since p and p+g+l lie in X. So p is in Z_{jbar}(l+g).
- (c) The inclusion is (b) with g = m-l. Then T_0(m) ⊆ Z_1(m) and T_1(m) ⊆ Z_0(m), which are disjoint. ∎

**Ternary form (Corollary 2.5).** Fix a class x at shift d. Let p<q in G_x^f(l), and p<q' in G_x^{f'}(l'), with q+l = q'+l'. Then f = f'. Here G_x^f(l) = F_l(X_x) ∩ S_f(d+l).

*Proof.* Corollary 2.4(c) with psi(a,b) = chi(b+d,a), applied at the pair (p, q+l). Note that psi(u,u+l) = chi(u+d+l,u) = z_{d+l}(u). ∎

In words: the Lemma B forcings C_l(p,q) = third(x,f) and C_{l'}(p,q') = third(x,f') fall on the same cell (q+d+l, p). They are consistent iff the corner colours of p at the two lags agree. Whenever they hit the same cell, this forces z_{d+l}(p) = z_{d+l'}(p).

**Why Corollary 2.4 does not yet give a deficit.** It is locally satisfiable at saturation. Example: for each (l,g), the 00-parallelogram has all four edges 0 and diagonal 1, and the 11-parallelogram has all edges 1 and diagonal 0. Then (a) holds.

For (c), count at fixed m. By Sidon, each Z_j(l) contributes at most one start to T_j(m). So |T_j(m)| <= m-1, while |Z_{jbar}(m)| <= Q(S-m). The constraint bites only through multiplicities: T_j(m) can be small only if many l send their pair to the same start p. That requires p+l, p+m-l in X for many l. At density rho = |X|/S, the available multiplicity per start is about rho^2 m ≈ 2m/sqrt(S) at saturation. Over about sqrt(S) starts this totals about 2m, against a demand of about m. That is a factor-2 margin, not a contradiction (heuristic).

### 2.4 Difference coverage of Sidon sets (explicit)

**Lemma 2.6.** Let A ⊆ [0,N] be Sidon, |A| = k, and T >= 2. Then

    sum_{g=1}^{T-1} (T-g)·[g is not a difference of A]  <=  T(T-1)/2 - T^2 k^2 / (2(N+T)) + T k/2.

*Proof.* For the N+T integers x in [-(T-1), N], let a(x) = |A ∩ [x, x+T)|.
- Each element lies in exactly T windows, so sum a(x) = Tk.
- sum a(x)(a(x)-1) counts ordered pairs a ≠ a' together with a window containing both. This equals sum over a≠a' of (T - |a-a'|)_+ = 2 sum_{g=1}^{T-1} (T-g) r_A(g), with r_A(g) in {0,1} by Sidon.
- Cauchy-Schwarz gives sum a(x)^2 >= (Tk)^2/(N+T).

Hence 2 sum (T-g) r_A(g) >= T^2k^2/(N+T) - Tk. Subtract from sum_{g<T} (T-g) = T(T-1)/2. ∎

Suppose k >= (1-eta) sqrt(N) and sqrt(N) <= T <= N. Then the (T-g)-weighted fraction of missing differences below T is at most about 2 eta + T/N + sqrt(N)/T. So the six near-maximal pieces of Proposition 2.2 realize almost every difference g with sqrt(S) << g << S. Corollary 2.4(b) then applies at almost every (l, g) in that range. This is the "predictable rate" of the director's sketch, made explicit. What is missing is an unsatisfiable gadget to feed it (Section 3).

## 3. The obstruction, and a correction to the director's heuristic (HEURISTIC; labelled)

**Neither direction is reachable with present tools.**
- *Refutation.* By Proposition 2.2, a refutation needs three binary sources at one shift with near-saturated fibers over lags up to more than sqrt(S)/(600 delta). No such binary source is known even in isolation (Section 2.2).
- *Proof.* A proof must be global, because every single-layer statement is saturable:
  - the m = 23 U-structure (entry 54);
  - six disjoint Bose sets (entry 49);
  - the translate obstruction (entry 48);
  - the local satisfiability of Corollary 2.4 (Section 2.3).

**Correction: cross-lag interactions are not rare in the range that matters.** The sketch estimates that a cell lies in about 36 lambda/S lag structures, and concludes that cross-lag collisions number about lambda^3/S. That figure is the density over *all* cells. The relevant quantity is conditional: given a cell already lies in the lag-l structure, how many other lags l' <= lambda also contain it?

Take a forced cell C_l(p,q) = (q+d+l, p), with p, q in the same piece G_x^f(l). It is also a forced cell of lag l' iff:
- p + l' lies in X_x;
- q' = q+l-l' lies in X_x (then q'+l' = q+l is automatically in X_x);
- z_{d+l'}(p) = z_{d+l'}(q').

At class density rho ≈ |X_x|/S ≈ 0.021 (regime), this has probability about rho^2/2 per lag l'. Here rho^2 ≈ 2/sqrt(S).

There are about 3S same-piece forced cells per lag. So the number of forced-forced coincidences over lags up to lambda is about
3S · lambda · lambda rho^2/2 ≈ 3 lambda^2 sqrt(S).
That is about lambda/2 times C_w(lambda) ≈ 6 lambda sqrt(S).

By Corollary 2.5, each coincidence imposes a corner agreement z_{d+l}(p) = z_{d+l'}(p). At lambda ≈ Lambda_0 ≈ 7 sqrt(S) a typical forced cell is shared by about 15 lag structures. So the cross-lag system is dense, not sparse.

Two caveats:
- These coincidences lie **inside one class**. They are consequences of properness of the single binary source X_x (Lemma 2.3). So they bear on the single-class statement SC, which implies MS, and not specifically on the cross-class coupling.
- A coincidence is a consistency condition, not a contradiction. Whether the dense system of corner agreements, together with near-maximality of all Golomb classes at all lags l <= lambda, is unsatisfiable is exactly the open core.

Given this, the director's conclusion ("the deficit must come from a single lag") should be withdrawn. The multi-lag single-class structure is the natural candidate source of a deficit.

## 4. Status summary and open questions

**PROVED here.**
- The chain audit (Section 1), including the monotonicity of K^Pi_rho in S (A3) and the v^+ repair (A1).
- Proposition 2.1: the exact window of content of MS' and the trivial range.
- Proposition 2.2: necessary structure of any counterexample.
- Lemma 2.3 and Corollaries 2.4 and 2.5: the inscribed-pair rule, transport and cross-lag corner agreement.
- Lemma 2.6: difference coverage.

**Not done (numerical or elementary).**
- A2: recertify K^Pi at the rank rho actually used, and compare it with the consumer's K.
- Step 6: the explicit lower bound K^Pi >= c_1 S^{3/4}.

**OPEN.**
1. **MS'** itself, with explicit delta and S_0. Only the range sqrt(S)/(600 delta) < lambda <= Lambda_0 = O(S^{5/8}) matters to the chain.
2. **SC'(delta)** (sufficient; single class). Every binary source X of span <= S, with S >= S_0, satisfies C_{r_X}(lambda) <= (1-delta) C_v(lambda) + S/300 for all lambda <= S. Summing over the three classes gives MS'.
3. **Lower-bound problem.** Do binary sources exist with r_X(l) >= c v_l for all l <= C sqrt(S), for some fixed c > 0 and arbitrarily large C? A positive answer with c -> 1 is necessary for any refutation of MS'.
4. **Multi-lag gadget.** Is there a finite configuration in a binary source, spread over two or more lags, whose Lemma 2.3 constraints are unsatisfiable when all Golomb classes involved realize the prescribed differences? Lemma 2.6 supplies the occurrence rate.

**Cheapest discriminating test (proposed; not run).** For small m, compute exactly
max sum_{l<=lambda} r_X(l) / sum_{l<=lambda} v_l
over all binary sources X ⊆ [0,m], for lambda = 2, 3, 4, by SAT or exhaustive search. Entry 54 is the lambda = 1 analogue for U-structures. A ratio that stays bounded below 1 as lambda grows would support SC'. Ratios reaching 1 at several lags would point toward refutation. Either outcome is evidence only for the sizes checked.

No statement about R_4 is made, except as an implication from the stated hypotheses.

=== END OF ANSWER round5_q2 ===

