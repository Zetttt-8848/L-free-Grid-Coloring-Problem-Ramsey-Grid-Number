# round6_q2 answer: the fibre-size deficit FD

## STATUS: FD NOT SETTLED

I have neither a proof of FD nor a counterexample. This file gives:

- a check of the chain in Task Part 2, with four flags (Section 1);
- rigorous partial results (Section 2): the exact reduction between FD and the single-class deficit; an explicit necessary condition on any FD-counterexample (all three classes within 3 eta + O(S^{-3/8}) of the cap); an explicit saturation lemma; and FD for two structured sub-classes. As the task says, the sub-classes do **not** answer the question;
- the point where every argument I tried stops, and my belief (Section 3);
- the open questions (Section 4).

Notation is the task's: c(S) := sqrt(v_1 S) with v_1 = Q(S-1)+Q(S-2), K_F(S) is the Fejer cap of Corollary F0, and K*(S) is the largest binary source in S+1 consecutive integers. Corollary F0 gives K*(S) <= K_F(S).

Labels: PROVED, CITED (from memory, by name), HEURISTIC.

---

## 1. Check of the chain (Task Part 2)

Steps 1-3 are correct as stated. I re-derived P1, Lemma F, Corollary F0, Proposition 2.1(a) and Lemma W from the spliced proofs and found no gap. Step 4 is correct as an inequality, but four points must be closed before FD can be fed to the R4 consumer.

**F1 (caps compared: K_F versus the rank cap K).** FD gives |F_d(D)| <= 3(1-eta) c(S), and c(S) <= K_F(S). The consumer, however, uses the rank cap K(L), not K_F. A saving of eta against the consumer's U_d needs c(S) <= K(S), or else costs the ratio c(S)/K(S).

- The problem's figure c ≈ 4.55*10^5 uses an *estimated* Q.
- A certified upper bound must be used instead. CITED (Lindstrom; Erdos-Turan): Q(m) <= sqrt(m) + m^{1/4} + 1.
- At S = 2.2*10^7 this gives Q <= 4690 + 68.5 + 1 ≈ 4760, so v_1 <= 9520 and c <= sqrt(9520 * 2.2*10^7) ≈ 4.576*10^5. That is essentially equal to K ≈ 4.58*10^5 (HEURISTIC arithmetic; it must be redone with exact numbers).
- So the effective delta is eta - O(10^{-3}). This is harmless if eta >= 0.01, but it has to be certified.

**F2 (monotonicity in S).** c(S) is nondecreasing in S, because Q is. So in the square the bound may be applied with S replaced by n-d-1 >= span F_d(D_c). PROVED (immediate). FD loses the staggering (the 12 distinct minima) but keeps the factor 12 (4 colours c times 3 classes). The staggering gain is additive and negligible at this scale (see the problem's sensitivity note).

**F3 (S_0).** The window d <= t-1 = 34,999 has S >= n - 35,000 ≈ 2.2*10^7. So any explicit S_0 below about 2*10^7 suffices.

**F4 (step 2, the per-fibre cap).** The cap r <= v_l uses v_l relative to S = span F_d(D), and every S_e(d) lies inside F_d(D). This is correct.

No flaw beyond F1-F4.

---

## 2. Proved partial results

### 2.1 Elementary constants (PROVED, from Section 3.2 of the brief, re-checked)

For S >= 34: v_1 >= 2Q(S-2) > sqrt((S-2)/2) >= sqrt(S)/2. Hence c(S) >= S^{3/4}/sqrt 2.

**Lemma A (K_F is asymptotically c).** For S >= 34,
K_F(S) <= (1 + xi(S)) c(S), with xi(S) := 3.83 S^{-3/8}.

*Proof.*
- Take Lam = ceil(S^{5/8}) and lambda = Lam - 1. Then 2 <= Lam <= S, and Lam <= S^{5/8} + 1 <= 2 S^{5/8}.
- With N = S + Lam: N/Lam <= S^{3/8} + 1, and sqrt(v_1 N) = c sqrt(1 + Lam/S) <= c (1 + Lam/(2S)) <= c (1 + S^{-3/8}).
- Also (S^{3/8} + 1)/c <= sqrt 2 (S^{3/8} + 1) S^{-3/4} <= 2 sqrt 2 S^{-3/8}.
- Together, K_F <= c(1 + (1 + 2 sqrt 2) S^{-3/8}), and 1 + 2 sqrt 2 < 3.83. ∎

### 2.2 FD versus the single-class deficit (PROVED)

Define **SCD(eta')**: there is S_1 such that every binary source X in S+1 consecutive integers, with S >= S_1, satisfies |X| <= (1-eta') c(S).

**Proposition 1.**
(a) SCD(eta') implies FD with eta = eta' and S_0 = S_1.
(b) Contrapositive form of the necessary condition. Let (D, chi, d) satisfy |F_d(D)| >= 3(1-eta) c(S) with S >= 34. Then **every** class satisfies |S_e(d)| >= (1 - 3 eta - 2 xi(S)) c(S).
(c) Consequently, a family refuting FD for every eta yields three pairwise disjoint binary sources at one shift, all in the same interval of S+1 integers, each of size (1 - o(1)) c(S). In particular it refutes SCD(eta') for every eta' > 0.

*Proof.*
- (a) Each S_e(d) is a binary source inside an interval of span <= S (P1 (iv.0) and heredity), and c is monotone in the span (F2). Summing the three bounds gives |F_d(D)| <= 3(1-eta') c(S).
- (b) Each s_f <= K*(S) <= (1 + xi) c by Lemma A. So s_e >= 3(1-eta) c - 2(1+xi) c.
- (c) follows from (b), since xi(S) -> 0. ∎

**Reading.** FD is implied by SCD, and the three-class structure enters FD only through the requirement that all three classes be simultaneously near the cap. The converse (FD implies SCD) is OPEN. It would need an embedding of an arbitrary near-cap binary source, three times and interleaved, as the classes of one shift of a ternary source. I could not build one: the interleaving creates parallelograms across the copies, and these must be coloured properly with the cross-class constraints of Lemma W.

### 2.3 Saturation lemma (PROVED, explicit)

**Proposition 2.** Let X be a binary source of span <= S with s = |X| >= (1-theta) c(S), 0 <= theta < 1. Let 1 <= lambda <= S, Lam = lambda + 1, N = S + Lam, and
Delta := sum_{l=1}^{lambda} (Lam - l)(v_1 - r_X(l)).
Every summand is >= 0, because r_X(l) <= v_l <= v_1. Then

2 Delta <= v_1 Lam (2 theta Lam + Lam^2/S - 1) + s Lam.

With weight W = lambda Lam/2, the weighted relative deficiency satisfies

Delta/(v_1 W) <= [2 theta Lam + Lam^2/S + s/v_1]/lambda, and s/v_1 <= (1 + xi) sqrt(2) S^{1/4} (for S >= 34).

*Proof.*
- Lemma F gives 2 sum (Lam-l) r_X(l) >= s^2 Lam^2/N - s Lam.
- Also s^2 >= (1-2theta) v_1 S, and S Lam/(S+Lam) = Lam - Lam^2/(S+Lam) >= Lam - Lam^2/S.
- So s^2 Lam^2/N >= v_1 Lam (Lam - Lam^2/S - 2 theta Lam).
- Hence 2 Delta = v_1 lambda Lam - 2 sum (Lam-l) r_X(l) <= v_1 Lam (lambda - Lam + Lam^2/S + 2 theta Lam) + s Lam.
- For the last bound: s <= K_F <= (1+xi) c, and c/v_1 = sqrt(S/v_1) <= sqrt 2 S^{1/4}. ∎

**Corollary 2' (both Golomb classes near-maximal at most lags).** Let beta > 0. The (Lam - l)-weighted proportion of lags l <= lambda with r_X(l) < (1-beta) v_1 is at most Delta/(beta v_1 W).

At every other lag, both Golomb classes Z_0(l) and Z_1(l) are Sidon sets (no 3-AP) in an interval of S-l+1 integers. Each has size >= r_X(l) - Q(S-l) >= Q(S-2) - beta v_1.

*Example of use:* take Lam ≈ epsilon S, so that the bound is ≈ (2 theta + epsilon + O(S^{-3/4}/epsilon))/beta.

Combined with Proposition 1(b) (theta = 3 eta + 2 xi), an FD-counterexample at level eta has, in **each** of its three classes and at all but a fraction O((eta + epsilon)/beta) of lags l <= epsilon S, two disjoint Sidon sets each of size >= (1 - 2 beta - o(1)) sqrt(S). This uses CITED: Q(m) = sqrt(m)(1+o(1)), with the upper bound by Lindstrom and the lower bound by Singer together with prime gaps (Baker-Harman-Pintz).

This is the director's "saturation" step, made rigorous with explicit constants.

### 2.4 FD on two structured sub-classes (PROVED; does not answer the question)

**Proposition 3 (translation-invariant colourings).** Suppose chi(v,u) = phi(v-u) for all cells of V(D). Then for every d, F_d(D) = S_{phi(d)}(d) is a single class. So |F_d(D)| <= K_F(S) <= (1+xi) c(S). FD therefore holds with eta = (2 - xi(S_0))/3. For example, eta = 0.6 for S_0 = 2700, where xi(2700) < 0.2.

*Proof.* The class is determined by chi(u+d,u) = phi(d). Then apply Corollary F0 and Lemma A. For the numbers: 2700^{3/8} = e^{(3/8) ln 2700} ≈ e^{2.964} ≈ 19.4, so xi ≈ 0.197. ∎

**Proposition 4 (difference-coloured classes).** Suppose the shifted source of a class X = S_e(d) is difference-coloured: psi(a,b) = chi(b+d,a) = f(b-a). Then each F_l(X) is entirely one Golomb class. So r_X(l) <= Q(S-l), and Lemma F gives

|X| <= min_lambda [N/Lam + sqrt(Q(S-1) N)] = (1/sqrt 2 + o(1)) c(S).

Any ternary source in which all three classes at shift d are difference-coloured satisfies FD with eta = 1 - 1/sqrt 2 - o(1) ≈ 0.29.

*Proof.* If f(l) = j, then Z_{jbar}(l) is empty. Rerun Corollary F0 with v_1 replaced by Q(S-1), and note Q(S-1)/v_1 -> 1/2 (CITED asymptotics). ∎

*Side remark (PROVED).* For a difference colouring, the binary-source condition is equivalent to f(x) = f(y) ≠ f(x+y) for every parallelogram a, a+x, a+y, a+x+y of X (with x <= y). This follows from Lemma 2.3, using d - a = (b-a) + (c-a). So a difference-coloured near-cap source would need every small difference pair (x,y) to lie in one colour class with x+y in the other. That is impossible at positive density by the Fejer count, which is why the deficit 1/sqrt 2 appears.

### 2.5 (D-c) remark (PROVED, immediate)

By P1 (iv.3), F_l(X) ∩ R_{e'}(h) lies in G_{e''}, which is a Sidon set. So it is Golomb, and |F_l(X) ∩ R_{e'}(h)| <= Q(S-l) holds trivially.

This bound is never stronger than the per-fibre cap. It lowers r_X(l) only if the forced sets make one Golomb class *small*. Nothing proved here forces that.

---

## 3. Where the argument stops, and what I believe

**Stopping point.** By Propositions 1-2, an FD-counterexample is equivalent (up to o(1)) to three disjoint binary sources at one shift with the following property: for almost every lag l in [S^{1/4+o(1)}, epsilon S], every fibre F_l(X_e) is the union of two near-maximal Sidon sets.

Every constraint I could extract is locally satisfiable at this density:
- Corollary 2.4(a): no parallelogram has l-edges both j and g-edges both jbar. For fixed (l,g), each Sidon class supplies about one doubly-agreeing parallelogram, and the collision needed for a violation has probability about S^{-1/2} per pair.
- Transport (Corollary 2.4(c)): about m forced incidences land in a set of size about sqrt S, with a factor-2 margin (Section 2.3 of the brief).
- Parallelogram count: for each (l,g), P(l,g) = r_{F_l X}(g) is about 4, and the agreeing ones are at most 2 + 2 by Sidon. Doubly-disagreeing parallelograms carry no constraint.

A proof must therefore be global (multi-lag). I found no such argument.

**Why a refutation is also out of reach (HEURISTIC).**
- FD asks for asymptotic constant 1, so a counterexample must attain the Fejer cap c(S) ≈ sqrt 2 S^{3/4} with constant 1 + o(1).
- Every construction I know (Sidon sets; digit or product lifts; the finite 12-point datum) either has size about span^{1/2} or loses a constant factor per digit, for example through carry-avoidance.
- A random-like set of density sqrt 2 S^{-1/4} has fibres of size about 2 sqrt S with about 16 S additive quadruples each. Such a fibre is very far from splitting into two Sidon sets. So any counterexample would have to be highly algebraic.

**Belief (HEURISTIC).** I believe FD is true, and indeed that SCD holds, probably with K*(S) = S^{1/2+o(1)}. A proof of SCD would improve the binary-source capacity itself, and would make the three-class mechanism unnecessary for FD.

---

## 4. Open questions

- **O1 (FD itself).** Prove or refute FD for some explicit eta > 0.
- **O2 (SCD).** Is there eta' > 0 with K*(S) <= (1-eta') sqrt(v_1 S) for all large S? By Proposition 1(a), this implies FD.
- **O3 (converse reduction).** Does FD imply SCD? That is, can any near-cap binary source be realised three times, interleaved, as the three classes of one shift of a proper ternary source?
- **O4 (multi-lag rigidity).** Is the system "F_l(X) is the union of two Sidon sets of size >= (1-beta) sqrt S for all l in [S^{0.3}, epsilon S]" (ignoring colours) satisfiable for a set X of size ≈ sqrt 2 S^{3/4}? A negative answer, even without the colouring, would prove SCD and hence FD.
- **O5 (consumer certification, F1).** Certify c(S) <= K(S) at S ≈ 2.2*10^7 using a proven upper bound on Q.

Nothing here is a new bound on R_4. The only implication is the hypothetical one: FD(eta) together with F1-F3 gives the problem's sensitivity gain with delta ≈ eta - O(10^{-3}).

=== END OF ANSWER round6_q2 ===
