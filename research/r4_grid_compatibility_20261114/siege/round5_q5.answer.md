# round5_q5 answer: single-lag joint deficit SL, the TSD route, and the translate model

## Plan (written first)
1. Check the derivation SL => MS' (Section 1).
2. Settle the part of Proposition O that was left OPEN: whether the translate pair B = A + t can carry a TSD coloring. Reduce it exactly to conditions on A (Section 2), and extract an explicit unsatisfiable gadget (Section 3). The gadget's contradiction is also proved directly from the L's of V(U), in a form that is valid for general TSD instances.
3. Give the small-difference saturation lemma, which is the input any counting lemma would use (Section 4), plus one new constraint family for route (b) (Section 5).
4. Status, the precise obstruction, and the open statements (Section 6).

Outcome in one line: SL and TSD remain OPEN. Proved here: the derivation SL => MS' (with explicit S_0); an exact finite reformulation of TSD for translate pairs; an explicit 6-point gadget G1 that rules out the translate pair (A, A+t) whenever A contains it; the general-TSD form of the gadget. The missing piece is a counting lemma saying near-maximal Sidon sets contain G1. That lemma is OPEN.

## 1. The derivation SL => MS' (checked; PROVED, with one correction of bookkeeping)

**Per-lag trivial cap.** Fix d, a lag l <= S, and m = S - l. Each U_f(l) = A_f ⊔ B_f is a union of two disjoint Sidon sets inside I = [min F_d(D), max F_d(D) - l], an interval of m+1 integers (Corollary U). If one of them contains min I, the other does not, so it lies in m consecutive integers. If neither contains min I, both do. Hence |U_f(l)| <= Q(m) + Q(m-1) = v_l. This holds for every m >= 0, with Q(-1) = 0. So w_l := sum_e r_{S_e(d)}(l) = sum_f |U_f(l)| <= 3 v_l for every l.

**Summation.** Assume SL(m0, delta). For 1 <= lambda <= S, split the lags l <= lambda into those with S - l >= m0 and the rest. The rest are the lags l in (S - m0, lambda], so there are at most m0 of them, with S - l = j in {0, ..., m0-1}, each value of j occurring at most once. Then

    sum_{l<=lambda} w_l <= (1-delta) sum_{l<=lambda, S-l>=m0} 3v_l + sum_{l<=lambda, S-l<m0} 3v_l
                         = (1-delta) sum_{l<=lambda} 3v_l + delta sum_{l<=lambda, S-l<m0} 3v_l
                        <= (1-delta) sum_{l<=lambda} 3v_l + 3 delta sum_{j=0}^{m0-1} (Q(j)+Q(j-1)).

Since Q(j) <= j+1, the last sum is at most sum_{j<m0} (2j+1) = m0^2. So the error is at most 3 delta m0^2, and it is <= S/100 as soon as S >= S_0 := max(1, 300 delta m0^2). Hence **SL(m0, delta) implies MS' with the same delta and S_0 = max(1, ceil(300 delta m0^2))**. The derivation in the query is correct. The only point to add is that the small-m lags need the per-lag cap above. That cap needs the "one of two disjoint sets misses an endpoint" argument, not just Q(m) for each piece. Without it the error term would be 2Q(m) per lag. That would still be a constant, so nothing breaks.

**Also checked:** TSD(m0, delta) => SL(m0, delta). By Corollary U each U_f(l) with its kappa-coloring is a TSD instance in an interval of span m. So |U_f(l)| <= (1-delta)(Q(m)+Q(m-1)) for each f. Sum over f. Conversely, a refutation of SL yields near-saturated TSD instances. So **TSD is the weakest single-layer statement that implies SL, and every refutation of SL passes through a refutation of TSD.**

## 2. The translate model, reduced exactly (PROVED)

This section settles the question left OPEN at the end of Proposition O: is the whole binary system on A ∪ (A+t) satisfiable? The answer is that it reduces to a finite list of order conditions on the pair starts of A. Section 3 extracts a configuration of A that makes it unsatisfiable.

**Setting.** Let t >= 1. Let A be a finite Sidon set (all positive differences distinct, 3-APs excluded) with no positive difference in [1, 2t]. Put B = A + t and U = A ∪ B. Let Δ be the set of positive differences of A. For δ in Δ let α_δ be the unique a in A with a + δ in A. Write the colors as 0 (= α, the color on A-pairs) and 1 (= β, the color on B-pairs). A **TSD coloring** is a map c on pairs x < y of U with c = 0 on A-pairs and c = 1 on B-pairs. It must be proper: for all u < v in U and g > 0 with u+g, v+g in U, the values c(u,u+g), c(v,v+g), c(u,v+g) are not all equal. (These are exactly the L's of V(U), by Lemma 0 in pair language.)

**Facts used repeatedly (from "no difference in [1,2t]").**
- A ∩ B = ∅, since t ∉ Δ.
- If a1, a2 in A and a1 ≠ a2, then |a1 - a2| > 2t.
- In particular α_g ≠ α_{g±t}. Also α_{g-t} ≠ α_{g+t}, since otherwise A would contain two points at distance 2t. Any two distinct starts differ by more than 2t. So comparisons such as "α_{g-t} < α_g + t" are equivalent to "α_{g-t} < α_g".

**The mixed cells.** A mixed pair (x < y, one point in A and one in B) is one of the following.
- An **AB pair** (a1, a2 + t), with a1 < a2 + t. If a1 > a2, then a1 - a2 would be a difference in [1, t-1]. So a1 <= a2.
  - If a1 = a2, write φ(a) := c(a, a+t).
  - If a1 < a2, then δ = a2 - a1 is in Δ, a1 = α_δ, and we write X_δ := c(α_δ, α_δ + δ + t).
- A **BA pair** (a1 + t, a2), with a1 + t < a2. Then δ = a2 - a1 > t is in Δ, and we write Y_δ := c(α_δ + t, α_δ + δ).

So the free variables are φ(a) (a in A), X_δ and Y_δ (δ in Δ). Their number is |A| + 2|Δ| = |A|^2 = |A||B|.

**Pairs of U of a given length g.**
- Length g = t: only the |A| pairs (a, a+t). The candidates A_t and B_t need t in Δ, and BA_t needs 2t in Δ; neither holds.
- Length g ≠ t: at most four pairs.
  - A_g = (α_g, α_g+g), color 0, if g in Δ.
  - B_g = (α_g+t, α_g+t+g), color 1, if g in Δ.
  - AB_g = (α_{g-t}, α_{g-t}+g), color X_{g-t}, if g-t in Δ.
  - BA_g = (α_{g+t}+t, α_{g+t}+t+g), color Y_{g+t}, if g+t in Δ.

  Uniqueness holds because each of these is determined by an A-pair of a prescribed difference, and A is Sidon.

Every L of V(U) consists of two pairs of the same length g and their spanning pair. So the constraint system is the list of all pairs of pairs below.

**Order bit.** For δ with δ, δ+t both in Δ (write δ in T), put σ(δ) := 1 if α_δ < α_{δ+t}, and σ(δ) := 0 otherwise. For δ in T define the **outer span** D(δ) := max(α_δ + δ, α_{δ+t} + δ + t) - min(α_δ, α_{δ+t}). Concretely, D = α_{δ+t} + δ + t - α_δ if σ = 1, and D = α_δ + δ - α_{δ+t} if σ = 0. In both cases D(δ) is in Δ, and its start α_{D(δ)} is min(α_δ, α_{δ+t}).

**Theorem T.** A TSD coloring of U = A ∪ (A+t) exists iff there are values φ: A -> {0,1}, X, Y: Δ -> {0,1} satisfying the following conditions.

- (T1) For each δ in T: X_δ = σ(δ) and X_{D(δ)} = 1 - σ(δ).
- (T2) For each g in T: Y_{g+t} = σ(g) and Y_{D(g)} = 1 - σ(g).
- (T3) For each g > t with g-t and g+t in Δ:
  - if α_{g-t} < α_{g+t}, then not (X_{g-t} = 0 and Y_{g+t} = 0);
  - otherwise, not (X_{g-t} = 1 and Y_{g+t} = 1).
- (T4) For each δ in Δ: φ(α_δ), φ(α_δ+δ) and X_δ are not all equal.

*Proof.* We go through all pairs of same-length pairs.

**Length t.** For a1 < a2 in A, the pairs (a1,a1+t) and (a2,a2+t) span (a1, a2+t). This is the cell X_{a2-a1}. Running over all A-pairs gives (T4).

**Length g ≠ t.**

- **(A_g, B_g).** The colors are 0 and 1, so this pair imposes no constraint.

- **(A_g, AB_g)** (g and g-t in Δ; put δ = g-t).
  - If α_δ < α_g: the spanning pair (α_δ, α_g+g) has both ends in A, so its color is 0. This forces X_δ = 1.
  - If α_g < α_δ: the spanning pair (α_g, α_δ+g) = (α_g, (α_δ+δ)+t) is an AB pair. Its A-difference is α_δ+δ-α_g. Its color is X_{α_δ+δ-α_g}, and the constraint is that 0, X_δ, X_{α_δ+δ-α_g} are not all equal.

- **(B_g, AB_g).**
  - If α_δ < α_g, then α_δ < α_g + t. The spanning pair (α_δ, α_g+g+t) is the AB pair X_{α_g+g-α_δ}, and the constraint is that 1, X_δ and this cell are not all equal.
  - If α_g < α_δ, then α_g + t < α_δ. The spanning pair (α_g+t, α_δ+g) has both ends in B, so its color is 1. This forces X_δ = 0.

  Combining the two cases:
  - When α_δ < α_g = α_{δ+t}, i.e. σ(δ) = 1: X_δ = 1 and X_{α_{δ+t}+δ+t-α_δ} = 0.
  - When σ(δ) = 0: X_δ = 0 and X_{α_δ+δ-α_{δ+t}} = 1.

  The indices are D(δ). This is exactly (T1).

- **(A_g, BA_g)** (g and g+t in Δ).
  - If α_g < α_{g+t}: the spanning pair (α_g, α_{g+t}+t+g) is an AA pair, so its color is 0. This forces Y_{g+t} = 1.
  - If α_{g+t} < α_g: then α_{g+t} + t < α_g. The spanning pair (α_{g+t}+t, α_g+g) is the BA cell Y_{α_g+g-α_{g+t}}, and the constraint is that Y_{g+t}, 0 and this cell are not all equal.

- **(B_g, BA_g).**
  - If α_g < α_{g+t}: the spanning pair (α_g+t, α_{g+t}+g+t) is the BA cell Y_{α_{g+t}+g+t-α_g}, and the constraint is that 1, Y_{g+t} and this cell are not all equal.
  - If α_{g+t} < α_g: the spanning pair (α_{g+t}+t, α_g+g+t) is a BB pair, so its color is 1. This forces Y_{g+t} = 0.

  Combining the two cases gives Y_{g+t} = σ(g) and Y_{D(g)} = 1 - σ(g). This is (T2).

- **(AB_g, BA_g)** (g-t and g+t in Δ).
  - If α_{g-t} < α_{g+t}, the spanning pair (α_{g-t}, α_{g+t}+g+t) is an AA pair, so its color is 0.
  - Otherwise α_{g+t} + t < α_{g-t}, and the spanning pair (α_{g+t}+t, α_{g-t}+g) is a BB pair, so its color is 1.

  This is (T3).

No other pairs of equal-length pairs exist. Each identification of a spanning pair as a named variable uses the uniqueness of α. ∎

**Reading of Theorem T.** In the translate model every X_δ with δ in T, and every Y_δ with δ - t in T, is forced to an order bit of A. The remaining conditions say that these forced values never clash. The system is a finite 2-SAT/NAE system determined by the order of the starts of A-pairs at differences δ and δ ± t. This order is exactly the "cross" information that Fourier magnitudes of A cannot see.

## 3. Gadget G1: an unsatisfiable configuration (PROVED)

**Definition (G1 in A, step t).** Points x < y in A, together with y1, y2, z1, z2 in A ∩ (x, y), such that

    y1 + y2 = x + y - t,     z1 + z2 = x + y + t.

**Proposition G1.** Let A be a Sidon set with no positive difference in [1, 2t]. If A contains a G1 configuration, then U = A ∪ (A+t) has no TSD coloring.

*Direct proof from the L's of V(U).* This proof does not use Theorem T. Let c be a TSD coloring.

Part 1. Put g = y - y2. Then g = y1 + t - x, because y1 + y2 = x + y - t. The pairs of length g that we use are:
- (x, y1+t): an AB pair, with color X;
- (y2, y): an AA pair, with color 0;
- (y2+t, y+t): a BB pair, with color 1.

We use two L's.
- The L with u = x < v = y2: here u + g = y1 + t and v + g = y. Its cells have colors X, 0, and c(x, y) = 0. So X = 1.
- The L with u = x < v = y2 + t: here u + g = y1 + t and v + g = y + t. Its cells have colors X = 1, 1, and c(x, y+t). So **c(x, y+t) = 0**.

The orders x < y2 and x < y2 + t hold because y2 > x.

Part 2. Put g' = z1 - x. Then g' = y + t - z2, because z1 + z2 = x + y + t. The pairs of length g' that we use are:
- (x, z1): an AA pair, with color 0;
- (x+t, z1+t): a BB pair, with color 1;
- (z2, y+t): an AB pair, with color X'.

Since z2 - x is a difference of A, it is larger than 2t, so x + t < z2. We use two L's.
- The L with u = x + t < v = z2: here u + g' = z1 + t and v + g' = y + t. Its spanning pair (x+t, y+t) is a BB pair. So its cells have colors 1, X', 1, and X' = 0.
- The L with u = x < v = z2: here u + g' = z1 and v + g' = y + t. Its cells have colors 0, X' = 0, and c(x, y+t). So **c(x, y+t) = 1**.

The two parts contradict each other. ∎

Every point used is in U: x, y, y2, z1 and z2 are in A, and y1+t, y2+t, x+t, y+t and z1+t are in B = A+t. Every L used is of the form (u,u+g),(v,v+g),(u,v+g) with u < v, so it is an L of V(U). The proof can be checked cell by cell.

**General-TSD form (PROVED by the same argument).** The proof uses only the following memberships. So it applies to an arbitrary TSD instance U = A ⊔ B, not only to translates. Fix x < y and t > 0, and suppose:
- x, y, p, z1, z2 are in A;
- q, p + t, x + t, y + t and z1 + t are in B;
- q + p = x + y and z1 + z2 = x + y + t (here q plays the role of y1 + t and p the role of y2);
- x < p and x + t < z2.

Then no TSD coloring exists.

The mirror image (exchange A and B, and the colors 0 and 1) and the reflection x -> -x give three more gadgets. Under reflection, AB pairs become BA pairs.

**Consequence for Proposition O.** The translate pair (A, A+2) of Proposition O survives every Lemma C test. But it fails as soon as A contains a G1 configuration with t = 2: an A-pair (x, y) such that both x + y - 2 and x + y + 2 are sums of two elements of A strictly between x and y. So the translate obstruction is an obstruction only to first-generation arguments. It is not an obstruction to TSD.

**What remains for the translate family (OPEN, precise).** This is the *Counting Lemma G1(t)*. There should be eta > 0 and N_0 such that every Sidon set A ⊆ [0,N] with N >= N_0, |A| >= (1-eta) sqrt(N), and no difference in [1,2t] contains a G1 configuration of step t. A positive-density version (at least c N disjoint copies) would be needed to turn G1 into a proportional deficit for translate-correlated pairs.
- The statement is about the 3-point correlation sum_s 1[s in A+A] r_in(s-t) r_in(s+t) of the sumset. Here r_in counts representations by elements strictly inside the A-pair that realises s. It is not controlled by the pair-correlation (energy, Lemma E) estimates available here.
- *Heuristic only.* For random-like A, about a constant fraction of the ~N/2 A-pairs (x,y) with y - x ≍ N have both x+y±t in the inner sumset, each with probability about 1/16. So Θ(N) copies are expected.
- I could not prove it. I also found no structured near-maximal Sidon family that avoids it. Residue-class restrictions would avoid it, but they cost a constant factor in size.

## 4. Small-difference saturation (PROVED; the input for any counting lemma)

**Lemma S.** Let A ⊆ [0,N] be Sidon with |A| = k, and let 1 <= T <= N. Then

    sum_{g=1}^{T-1} (T-g) · 1[g ∉ Δ(A)]  <=  T(T-1)/2 - T^2 k^2 / (2(N+T)) + Tk/2.

If k >= (1-eta) sqrt(N), then the right-hand side, divided by the maximal weight T(T-1)/2, is at most 1 - (1-eta)^2 N/(N+T) · T/(T-1) + k/(T-1). This is at most 2eta + T/N + 2(sqrt(N)+1)/(T-1) for T >= 2.

*Proof.* Put a(x) = |A ∩ [x, x+T)| for the N+T integers x in [-(T-1), N]. Then sum_x a(x) = Tk. Also sum_x a(x)(a(x)-1) = sum_{a≠a'} (T - |a-a'|)_+ = 2 sum_{g=1}^{T-1} (T-g) 1[g in Δ], because A is Sidon. By Cauchy-Schwarz, sum a^2 >= (Tk)^2/(N+T). Hence

    2 sum_{g<T} (T-g) 1[g in Δ] >= T^2k^2/(N+T) - Tk.

Subtract this from the total weight 2 sum_{g<T}(T-g) = T(T-1). For the second form:
- The ratio equals 1 - T k^2/((N+T)(T-1)) + k/(T-1).
- Use k^2 >= (1-eta)^2 N >= (1-2eta) N, N/(N+T) >= 1 - T/N, and T/(T-1) >= 1.
- Use k <= N^{1/2} + N^{1/4} + 1 <= 2(sqrt(N)+1). This is the classical Erdős–Turán/Lindström bound, cited from memory.

∎

**Corollary S2.** Take a TSD instance in an interval of span m with |A| + |B| >= (1-eta)(Q(m)+Q(m-1)). Then each of |A|, |B| is >= (1-2eta) Q(m) - 2 >= (1-3eta) sqrt(m) for m large. This is because each is at most Q(m). Hence, for sqrt(m) << T << m, all but a fraction O(eta + T/m + sqrt(m)/T) of the weight sum_{g<T}(T-g) lies on differences g common to A and B.
- At each such g, Lemma C gives the no-collision constraint.
- Section 3 shows that the dangerous case where A-starts and B-starts are aligned (translates) is handled by G1 instead.

This is the precise sense in which a proof of TSD has to be a **dichotomy**:
- either A and B are not translate-correlated, and then Lemma C collisions should occur at a positive rate;
- or they are translate-correlated, and then G1-type gadgets should occur at a positive rate.

Neither half is proved. The dichotomy itself is a heuristic organisation, not a theorem.

## 5. A further constraint family for route (b) (PROVED, small)

**Lemma W(a') (negative inner lag).** In the setting of Lemma W, extend kappa(p,q) := chi(q+h, p) to all p, q in W with q + h > p. This is a cell of V(D): p is in D, q+h = (q+l)+d is in D, and q+h > p. Then for all p < p' in W and all integers g with h + g > 0 and p+g, p'+g in W, the values kappa(p,p+g), kappa(p',p'+g), kappa(p,p'+g) are not all equal.

*Proof.* Take the L (a, a+δ), (c, c+δ), (a, c+δ) of pair language with a = p, c = p', δ = h + g > 0. All four points p, p+g+h, p', p'+g+h lie in D, because p+g and p'+g are in W. The three cells are the three kappa values listed. ∎

For g >= 0 this is Lemma W(a), with p' = p + y - x and g = x. For -h < g < 0 it is new. It couples "backward" cells kappa(q,p), q > p, into the system. In the regime h << m it only affects inner distances below h. I did not find a use for it. I record it because route (b) must use some constraint outside Corollary U, and this is one.

## 6. Status

**PROVED here.**
1. SL(m0, delta) => MS' with the same delta and S_0 = max(1, ceil(300 delta m0^2)). TSD => SL, and every refutation of SL yields near-saturated TSD instances (Section 1).
2. Theorem T: an exact reformulation of TSD for translate pairs (A, A+t), where A is Sidon with no difference in [1,2t]. It is a finite system of order conditions (T1)-(T4) on the starts of A-pairs (Section 2).
3. Proposition G1: the explicit gadget. Its general-TSD form, with a direct cell-by-cell proof, is valid for arbitrary TSD instances (Section 3). This settles, negatively for every A containing G1, the satisfiability question that Proposition O left OPEN.
4. Lemma S, Corollary S2 (small-difference saturation, explicit) and Lemma W(a') (Sections 4-5).

**OPEN (named).**
- **SL** and **TSD**: not proved and not refuted. No near-saturated family was found. The translate family, the natural candidate, is now reduced to the Counting Lemma G1(t).
- **Counting Lemma G1(t)** (Section 3): near-maximal Sidon sets contain the G1 configuration, preferably Θ(N) disjoint copies.
- **The non-translate half of the dichotomy** (Section 4): if A and B are near-maximal and not translate-correlated in a quantified sense, Lemma C collisions occur at a positive rate.
- Whether the full system (T1)-(T4) can be satisfied for some near-maximal Sidon A that avoids G1 and its mirror images. A positive answer would refute TSD and kill route (a).

**Not claimed.** Nothing here is a bound on R_4. Every R_4 consequence passes through SL or MS', which remain hypotheses. No computation was run in this answer. The finite data quoted in the query (TSD saturated at m = 23, 24) is consistent with all the statements above, since G1 needs six A-points in specific additive position and was not required there.

=== END OF ANSWER round5_q5 ===
