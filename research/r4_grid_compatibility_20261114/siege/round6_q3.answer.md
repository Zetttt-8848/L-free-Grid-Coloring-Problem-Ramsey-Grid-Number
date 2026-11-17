# round6_q3 answer: the fibre-size deficit FD

## STATUS: FD NOT SETTLED

I have neither a proof of FD nor a counterexample family. This file gives:

- a check of the Task Part 2 chain (it is valid, with three caveats, Section 1);
- one new rigorous result with explicit constants: Proposition S (the saturation structure that any counterexample to FD must have, Section 2);
- two routes that turn out to carry no information, each with the reason (Section 3);
- a precise statement of what is still missing, and my opinion (Section 4).

Labels: PROVED (complete proof in this file, or a re-checked proof from the brief); CITED; HEURISTIC.

I re-checked the following inputs from the brief and use them: Lemma F, Corollary F0, Section 0 (Q-up and Q-low), Proposition 2.1(a), Lemma 2.3, and Corollary 2.4. I found no error in their proofs. In Lemma F the window support count of span + Lam <= N is correct, and so is the identity sum f^2 = sum_{a,b} (Lam-|a-b|)_+.

## 1. Check of the chain (Task Part 2)

Steps 1-4 are logically correct. Three caveats concern how the result is consumed.

**(C1) The cap FD competes with is the rank cap K, not K_F.** The consumer's U_d is built from the rank capacity K. FD gives |F_d(D_c)| <= 3(1-eta) sqrt(v_1 S). This is a proportional saving against K only if K(S') >= sqrt(v_1(S) S) is certified at the relevant spans S' = S-j, j <= 11. The brief's numbers, K ≈ 4.58e5 against sqrt(v_1 S) ≈ 4.55e5, suggest a margin of about 0.7%. Those numbers are HEURISTIC estimates, so the inequality must be certified numerically. If it is, the effective saving relative to U_d is at least eta. The staggering loss (spans S-j with j <= 11) is of relative size about 11/S ≈ 5e-7.

**(C2) Q must be certified.** FD is stated with the true Sidon maximum Q. Any certified upper bound Qhat >= Q enlarges the right-hand side, so FD with Q implies FD with Qhat. The consumer needs explicit values, so it should use Qhat. This is harmless.

**(C3) Scope.** FD is applied per main-diagonal colour c, to the ternary source D_c with S_c = span F_d(D_c) <= n-1-d. The function S -> sqrt(v_1(S) S) is nondecreasing, because Q is. So FD gives X_d = sum_c |F_d(D_c)| <= 12(1-eta) sqrt(v_1(n-1-d)(n-1-d)), which is what the sensitivity computation needs.

Two remarks:
- FD is a statement about |F_d(D)| for a ternary source. The binary-source decomposition enters only in proofs.
- FD is implied by the single-class deficit SC(eta): every binary source of span <= S >= S_0 has size <= (1-eta) sqrt(v_1 S). The converse fails: FD does not imply SC.

## 2. Proposition S: saturation structure of any counterexample (PROVED, explicit constants)

Notation:
- X_e = S_e(d), s_e = |X_e|, and r_e(l) = r_{X_e}(l).
- S = span F_d(D), v_1 = Q(S-1) + Q(S-2).
- Z_0^e(l), Z_1^e(l) are the two Golomb classes of F_l(X_e).

**Lemma S0 (K_F is asymptotically sqrt(v_1 S)).** For S >= 2^16 we have K_F(S) <= (1+eps_S) sqrt(v_1 S), where eps_S := 2 S^{-3/8}.

*Proof.*
- Take Lam_0 = ceil(S^{5/8}) <= S and N = S + Lam_0 in the definition of K_F.
- sqrt(v_1 N) = sqrt(v_1 S) sqrt(1 + Lam_0/S) <= sqrt(v_1 S)(1 + Lam_0/(2S)), and Lam_0/(2S) <= S^{-3/8}/2 + 1/(2S).
- N/Lam_0 <= S/Lam_0 + 1 <= S^{3/8} + 1.
- By Section 0, v_1 >= 2Q(S-2) > sqrt((S-2)/2) >= sqrt(S)/2. Hence sqrt(v_1 S) >= S^{3/4}/sqrt 2, and (N/Lam_0)/sqrt(v_1 S) <= sqrt2 (S^{-3/8} + S^{-3/4}).
- Adding up, eps <= (sqrt2 + 1/2) S^{-3/8} + sqrt2 S^{-3/4} + 1/(2S). For S >= 2^16 we have S^{-3/4} <= S^{-3/8}/64, so eps <= 1.94 S^{-3/8}. ∎

**Proposition S.** Let S >= 2^16 and eta >= 0. Let (D, chi) be a proper ternary source, and let d be a shift with |F_d(D)| >= 3(1-eta) sqrt(v_1 S). Put theta = 3 eta + 2 eps_S, and assume theta < 1. Then for every e:

(a) (1-theta) sqrt(v_1 S) <= s_e <= (1+eps_S) sqrt(v_1 S).

(b) For every integer lambda >= 1 with Lam = lambda+1 <= S, define the weighted fibre deficit
  Dbar_e(lambda) := 2 sum_{l=1}^{lambda} (Lam-l)(v_1 - r_e(l)) / (v_1 lambda Lam), which lies in [0,1].
  Then Dbar_e(lambda) <= 2 theta + Lam/S + 1.5 S^{1/4}/lambda.

(c) For every l, both Golomb classes satisfy |Z_j^e(l)| >= Q(S-2) - (v_1 - r_e(l)). Their imbalance satisfies | |Z_0^e(l)| - |Z_1^e(l)| | <= Q(S-1) - Q(S-2) + (v_1 - r_e(l)).

(d) For lambda = ceil(S^{5/8}): Dbar_e(lambda) <= 6 eta + 10.6 S^{-3/8}. For lambda = floor(epsilon S) with epsilon in (0,1): Dbar_e <= 6 eta + epsilon + 8 S^{-3/8} + 1/S + 1.5 S^{1/4}/lambda. Also sum_{l <= lambda/2} (v_1 - r_e(l)) <= Dbar_e(lambda) v_1 lambda: the unweighted deficit over the first half of the window is controlled by the same quantity.

*Proof.*

(a) Each X_e is a binary source of span <= S (P1 (iv.0) with heredity), so s_e <= K_F(S) <= (1+eps) sqrt(v_1 S) by F0 and S0. Then
s_e >= |F_d(D)| - sum_{e' ≠ e} s_{e'} >= (3(1-eta) - 2(1+eps)) sqrt(v_1 S) = (1-theta) sqrt(v_1 S).

(b) Dbar lies in [0,1] because r_e(l) <= v_l <= v_1 (Proposition 2.1(a)) and sum_{l=1}^{lambda} (Lam-l) = lambda Lam/2.
- Lemma F gives s Lam + 2 sum (Lam-l) r(l) >= s^2 Lam^2/N with N = S+Lam. Hence
  2 sum (Lam-l)(v_1 - r(l)) <= v_1 lambda Lam + s Lam - s^2 Lam^2/N.
- Dividing by v_1 lambda Lam gives Dbar <= 1 + s/(v_1 lambda) - s^2 Lam/(v_1 lambda N).
- Since Lam >= lambda and s^2 >= (1-theta)^2 v_1 S >= (1-2theta) v_1 S, the subtracted term is >= (1-2theta) S/(S+Lam) >= (1-2theta)(1 - Lam/S).
- Hence Dbar <= 2theta + Lam/S + s/(v_1 lambda).
- Finally s/v_1 <= (1+eps) sqrt(S/v_1) <= (1+eps) sqrt2 S^{1/4} <= 1.5 S^{1/4}, using v_1 >= sqrt(S)/2 and eps <= 2^{-5}.

(c) F_l(X_e) = Z_0 ⊔ Z_1, and each Z_j is a Sidon set inside [min F_d(D), max F_d(D) - l] (Golomb split, P1 (iv.2)).
- As in Proposition 2.1(a), one of the two classes misses the left endpoint, so the larger class is <= Q(S-1) and the smaller is <= Q(S-2) (no ordering is assumed beyond this).
- So |Z_j| >= r_e(l) - Q(S-1) = Q(S-2) - (v_1 - r_e(l)).
- The imbalance bound follows from |Z_0| - |Z_1| <= Q(S-1) - (Q(S-2) - (v_1 - r)).

(d) Substitute into (b):
- For lambda = ceil(S^{5/8}): Lam/S <= S^{-3/8} + 2/S, 1.5 S^{1/4}/lambda <= 1.5 S^{-3/8}, and 2theta = 6eta + 8 S^{-3/8}. The total is <= 6eta + 10.6 S^{-3/8}.
- The second case is direct.
- For the last claim, (Lam-l) >= Lam/2 when l <= lambda/2, so (Lam/2) sum_{l<=lambda/2} (v_1-r) <= Dbar v_1 lambda Lam/2. ∎

**Reading (HEURISTIC estimates).** At the regime S ≈ 2.2e7 we have S^{-3/8} ≈ 1/567 and eps_S ≈ 0.0035. A counterexample to FD with eta = 0.01 would therefore need, for each of the three classes:
- size within about 3.7% of sqrt(v_1 S);
- weighted mean fibre deficit below about 8% over every lag window up to 2% of S;
- at such lags, two Golomb classes that are each Sidon sets of size near Q(S).

By Lemma 2.6 of the brief (re-checked), near-maximal Sidon sets realize almost every difference g with sqrt(S) << g << S. So, at almost every pair of lags (l,g) in that range, both Golomb classes of F_l(X_e) contain a pair at difference g. Transport (Corollary 2.4(b)) then fires at almost every (l, g).

## 3. Routes examined and found empty (both are dead ends; I record them so they are not repeated)

**3.1 The ±1 L-identity is bookkeeping.**
- Write M(a,b) = ±1 for the colour of the pair a<b in a binary source X.
- For each L with arms (a,b), (c,e) (where e-c = b-a) and corner (a,e), "not monochromatic" is equivalent to M_ab M_ce + M_ab M_ae + M_ce M_ae = -1.
- Summing over all Lambda = sum_t C(r_t,2) L's gives Sigma_A + Sigma_B + Sigma_C = -Lambda, with Sigma_A = (1/2) sum_t (Delta_t^2 - r_t) and Delta_t = |Z_0(t)| - |Z_1(t)|. This is PROVED and correct.

It carries no new information, for the following reason:
- On a mixed L (M_ab ≠ M_ce) the identity holds for either corner value.
- On a pure L it says only that the corner is opposite to the arms.
- So the summed identity reduces to #pure L's = sum_t [C(|Z_0(t)|,2) + C(|Z_1(t)|,2)].
- Any contradiction must therefore come from the forced corners colliding inconsistently. That is Corollary 2.4(c) and Lemma 2.3, which is the whole property again.

The possible non-trivial use I see is spectral:
- Sigma_B = (1/2) sum_a m_a^T A_a m_a, where A_a is the adjacency matrix of the graph on X_{>a} with b ~ e iff a + |e-b| ∈ X.
- Near-extremality forces each such graph, on average, to have max-cut fraction >= 3/4 - o(1), with degrees about 2 sqrt S.
- To use this one needs a "relative positivity" lemma for Cayley-type graphs restricted to the sparse set X. I could not prove one (OPEN).
- The heuristic support: at a common frequency theta, the average over a of the Fourier eigenvalue is (|Xhat(theta)|^2 - s)/(2s) >= -1/2, which is negligible against the degree. But the restriction to X_{>a}, and the frequency depending on a, block this argument.

**3.2 Energy and Gowers counts are consistent at saturation.**
- Let N(l,g) = #{u : u, u+l, u+g, u+l+g ∈ X}.
- Lemma F applied to the fibre F_l(X), with |F_l| ≈ 2 sqrt S, forces the (Lam-g)-weighted mean of N(l,g) over g <= lambda to be at least about 4.
- The Sidon property allows at most 2 pure quadruples per (l,g). So at least half the quadruples are mixed.
- That is not a contradiction: N(l,g) = 4, with 2 quadruples pure in l and 2 pure in g, is locally admissible. Quadruples pure in both directions must have one common colour, with the opposite diagonal (Corollary 2.4(a)), and that is satisfiable.
- Additive energies are also compatible. E(F_l) lies between about 8S (Cauchy-Schwarz) and 32S (Minkowski over two Sidon sets).

## 4. What remains open, and my opinion

**Open (precise).** Either
- (SC) there are explicit eta, S_0 > 0 such that every binary source of span S >= S_0 has size <= (1-eta) sqrt(v_1 S); or
- the three-class version FD.

By Proposition S, a counterexample to either must have every class near-extremal in the strong sense of (a)-(d). The concrete missing lemma is an anti-saturation statement. Here is one sufficient form, OPEN: for some fixed epsilon, a positive proportion of lags l <= epsilon S have r_X(l) <= (1-c) v_1, for every binary source X of size >= (1-c') sqrt(v_1 S). By Proposition S(b), any such statement with explicit c, c' gives SC and hence FD.

**Construction side.** Refuting FD needs three binary sources of size about sqrt2 S^{3/4} at one shift. No binary source of size span^{1/2+epsilon} is known to me. This is from memory and is not a search result.

**Opinion (HEURISTIC).** I believe FD is true, and probably SC as well.
- In a near-extremal X the L-hypergraph on the pairs has about 2 sqrt S edges per vertex.
- A random-like 3-uniform hypergraph stops being 2-colourable at bounded edge density. This is the classical random-hypergraph threshold, recalled from memory as about 2.4 edges per vertex.
- So any example must be highly structured, for instance Fourier-biased. For that kind of structure the positivity heuristic of 3.1 points the other way.

None of this is a proof. Nothing here is a statement about R_4 beyond the conditional chain of Section 1: FD with eta implies X_d <= (1-eta) U_d up to (C1), and then the sensitivity estimate of the brief.

=== END OF ANSWER round6_q3 ===
