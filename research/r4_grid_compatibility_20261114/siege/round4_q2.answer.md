# round4_q2 answer: the joint prefix-averaged fiber deficit MS

## 0. Verdict (read first)

- **MS is neither proved nor refuted here.** I found no proof with an explicit delta and no explicit counterexample. MS remains **OPEN**.
- **Proved (new), Section 1.** The lag-l start set carries a structure exactly analogous to the original problem, one level down. The set W of all lag-l starts at shift d, with the cells kappa(p,q) = chi(q+h,p), behaves like a "square" with a 3-colored diagonal. Each of its three diagonal classes U_f is a **binary source** whose 2-coloring is constant on the pairs inside each of its two Golomb pieces. The Golomb split (iv.2), Lemma F, and the AABA/ABAA forcings are all special cases of this one statement.
- **Proved, Section 2.** Inside this structure, no single mixed additive-quadruple pattern is forbidden. The only patterns it forbids are the pure ones AAAA and BBBB. So no proof of MS can work by forbidding patterns one quadruple at a time. It has to be a global (density or counting) argument.
- **Proved reduction, Section 3.** MS would follow from a purely 2-color statement, the **two-Sidon binary-source deficit (TSD)**. Section 3 states it precisely and gives the derivation of MS from it. TSD is open.
- **Chain check, Section 4.** Steps 2–5 are correct with two repairs:
  - (a) the common-rank requirement `c < min_e s_e` needs a case split;
  - (b) staggering inside a triple is lost, but this costs only an additive amount.
- **Step 5 made rigorous, Section 4.** Under MS, the joint triple satisfies the single-class certification inequality with its right side multiplied by `(1-delta)`, up to an explicit additive slack. The final number delta' still needs the project's certification data (the e_j and the rank c), which I do not have. Heuristically `delta' ≈ 1 - sqrt(1-delta)`.

Nothing here is a statement about R_4 beyond implications from stated hypotheses.

---

## 1. The lag-l start set is a 3-colored weak source (PROVED)

Fix a proper ternary source (D, chi), a shift d >= 1 and a lag l >= 1, and put h = d+l.

**Definitions.**
- `X_e = S_e(d)` and `A^e = F_l(X_e)`. The sets A^0, A^1, A^2 are pairwise disjoint, because the X_e are.
- `W = A^0 ∪ A^1 ∪ A^2`, and `cls(p) = e` for p in A^e.
- For p <= q in W, `kappa(p,q) := chi(q+h, p)`.

**This is a cell of V(D).** We have p in D. Also q+l is in X_e, which lies in F_d(D), so q+h = (q+l)+d is in D. Finally q+h > p.

**Lemma W.**

(a) **Properness.** Let p in W and 0 <= x < y be such that p+x, p+y-x and p+y all lie in W. Then the three values kappa(p,p+x), kappa(p,p+y), kappa(p+y-x,p+y) are not all equal.

(b) **In-class constraints.** If p <= q both lie in A^e, then kappa(p,q) != e. In particular the diagonal value kappa(p,p) = chi(p+h,p) is != cls(p).

*Proof of (a).* Consider L(u,d1,h1) of Lemma 0 with u = p, d1 = h+x, h1 = h+y. Then 1 <= d1 < h1. Its three cells are:
- the horizontal arm end (p+h+x, p) = kappa(p,p+x);
- the corner (p+h+y, p) = kappa(p,p+y);
- the vertical arm end (p+h+y, p+y-x) = kappa(p+y-x, p+y).

By Lemma 0(b), it lies in V(D) iff p, p+h+x, p+y-x and p+h+y are all in D. This holds:
- p and p+y-x lie in W, which is contained in D;
- p+x lies in W, so p+x+h is in D by the remark above;
- likewise p+y lies in W, so p+y+h is in D.

Properness of chi gives the claim. ∎

*Proof of (b).* Let p <= q be in A^e. Then p and q+l lie in X_e, and p < q+l. By (iv.0), psi(p,q+l) = chi(q+l+d, p) = kappa(p,q) is != e. ∎

**Diagonal classes.** Put `U_f = {p in W : kappa(p,p) = f}`. By (b), U_f is contained in the union of the A^e with e != f. Writing `{e,e'} = P \ {f}`, U_f is the disjoint union of
- `A_f := A^e ∩ U_f = G_e^f` and
- `B_f := A^{e'} ∩ U_f = G_{e'}^f`.

For every lag l, the six pieces partition W, and
`sum_e r_{S_e(d)}(l) = |W| = |U_0| + |U_1| + |U_2|`.

**Corollary U (each U_f is a binary source with constant internal colors).** Write c(p,q) = kappa(p,q) for p < q in U_f.

1. c takes values in P \ {f} = {e, e'}.
2. For all p1 < p2 <= p3 < p4 in U_f with p1+p4 = p2+p3, the two triples
   `T1 = {c(p1,p2), c(p1,p4), c(p3,p4)}` and `T2 = {c(p1,p3), c(p1,p4), c(p2,p4)}`
   are both non-monochromatic. When p2 = p3 they coincide.
   Equivalently, by Lemma 0 applied to U_f, the coloring (q,p) -> c(p,q) of V(U_f) is proper. So U_f is a binary source.
3. c is identically e' on pairs inside A_f, and identically e on pairs inside B_f.
4. Consequently A_f and B_f are Sidon sets, including 3-term progressions. This is the Golomb split (iv.2).

*Proof.*
- **Item 1.** Apply Lemma W(a) with x = 0 and y = q-p. This gives kappa(p,p), kappa(p,q), kappa(q,q) not all equal. The first and last both equal f, so c(p,q) != f.
- **Item 2.** Apply Lemma W(a) at p = p1. For T1 take x = p2-p1 and y = p4-p1; then p1+y-x = p3. For T2 take x = p3-p1 and the same y; then p1+y-x = p2. All four points lie in W.
- **Item 3.** For p < q in A_f, c(p,q) != f by item 1, and != e by Lemma W(b). So c(p,q) = e'. The same argument gives the value e on B_f.
- **Item 4.** Any additive quadruple or 3-AP inside A_f would make T1 monochromatic of color e'. ∎

**Special cases.**
- Lemma F is item 1 together with item 3.
- The AABA and ABAA forcings of the earlier answers are item 2 applied to a single mixed quadruple, given item 3. See Section 2.

**Remark: one level down.** (W, kappa) is the exact analogue of the square, one level down:
- the "diagonal" kappa(p,p) is 3-colored;
- each diagonal class has a strict source avoiding its own diagonal color, hence 2-colored;
- the class labels cls add the constraints of Lemma W(b).

MS at a single lag asks whether the three binary sources U_f can each be as large as two near-maximal Sidon sets.

## 2. No single mixed quadruple pattern is forbidden (PROVED)

Write α = e' (the color inside A_f) and β = e (the color inside B_f). Take a quadruple p1 < p2 <= p3 < p4 in U_f with p1+p4 = p2+p3, and list the classes in the order p1 p2 p3 p4.

- **AAAA, BBBB:** forbidden (item 4).
- **AABA:** T1 = {α, α, c(p3,p4)} and T2 = {c(p1,p3), α, α}. Both are non-monochromatic iff c(p3,p4) = c(p1,p3) = β. This is satisfiable, and it is exactly the AABA forcing.
- **ABAA:** symmetrically, it forces c(p1,p2) = c(p2,p4) = β. Satisfiable.
- **AAAB, ABBB and their A/B swaps:** satisfiable. For AAAB, take c(p1,p4) = β; then each triple contains both β and α.
- **AABB:** T1 = {α, *, β} holds automatically. T2 consists of three free mixed cells; make them not all equal.
- **ABAB, ABBA and the like:** each triple contains at least two free cells, so it is satisfiable.

**Explicit complete instance.** Take U = {0,1,2,3}, A = {0,1,3} (Sidon: its differences are 1, 2, 3), B = {2}. Color the cells:
- c(0,1) = c(0,3) = c(1,3) = α;
- c(0,2) = c(2,3) = β;
- c(1,2) = α.

The L's of V(U) are:
- the 3-AP 0,1,2, with triple {α, β, α};
- the 3-AP 1,2,3, with triple {α, α, β};
- the quadruple 0+3 = 1+2, with triples {c01, c03, c23} = {α, α, β} and {c02, c03, c13} = {β, α, α}.

None is monochromatic. Here |U| = 4 against Q(3)+Q(2) = 5.

This instance is a valid U-structure only. Realizing it inside a full ternary source is a separate question that I have not settled. That AABA is forbidden in ternary sources remains OPEN, as in the earlier answer.

**Consequence.** Any proof of MS through the U_f has to be global. It must show that two near-maximal Sidon sets A, B force too many mixed constraints to be satisfied simultaneously.

There are Θ(m) mixed quadruples whatever A and B are, since E(A∪B) >= |A∪B|^4/|2(A∪B)|. Each difference x in Δ(A)∩Δ(B) gives exactly one quadruple {a, a+x, b, b+x}. This is because A and B are Sidon.

**Heuristic only (not a proof).** For random-like A and B the counts are:
- about 2|A||B| ≈ 2m free mixed cells;
- about 1.2m mixed quadruples, which give about 2.3m triple constraints, each forbidding 2 of the 8 color patterns.

This density is in the range where NAE-type constraint systems pass from satisfiable to unsatisfiable. So neither outcome of MS looks clearly favoured.

## 3. Reduction of MS to a 2-color statement (PROVED implication; hypothesis OPEN)

**TSD(m0, δ).** Let U = A ∪ B, with A and B disjoint Sidon sets, U contained in an interval of m+1 consecutive integers, and m >= m0. Suppose there is a proper 2-coloring c of V(U) (in the sense of Corollary U, item 2) that is constant α on pairs inside A and constant β != α on pairs inside B. Then
`|U| <= (1-δ)(Q(m)+Q(m-1))`.

**Proposition.** Assume TSD(m0, δ). Then for every proper ternary source, every d, and every λ with 1 <= λ <= S,

`sum_{l<=λ} sum_e r_{S_e(d)}(l) <= (1-δ) sum_{l<=λ} 3v_l + δ·E(S, λ)`,

where `E(S,λ) = sum_{l<=λ, S-l<m0} 3v_l <= 3 sum_{j<m0} (Q(j)+Q(j-1))`.

Hence MS holds, with any δ_MS < δ, for all S >= S_1(m0, δ, δ_MS).

*Proof.*
- Fix a lag l. The sets U_f(l) lie in [min F_d(D), max F_d(D) - l], an interval of span m = S-l.
- By Section 1, the triple (U_f, A_f, B_f, kappa) satisfies the TSD hypotheses.
- If m >= m0, TSD gives |U_f(l)| <= (1-δ)v_l. Otherwise |U_f(l)| <= v_l, by the single-class Golomb cap applied to each piece.
- Sum over f and over l <= λ.
- The error term is a constant depending only on m0. The main sum satisfies sum_{l<=λ} 3v_l >= 3v_1 >= 3Q(S-2), which tends to infinity with S. ∎

**What the proposition does not cover.**
- For S below S_1 (and above about 60, where the trivial bound r_Y(l) <= S-l+1 stops beating 3v_l), MS would need TSD down to m0 = 1. TSD might fail at particular small m: a 2-coloring of a 7-point U = A∪B, A = {0,1,4,6}, B = {2,3,5}, would give |U| = Q(6)+Q(5). I have not checked whether such a coloring exists.
- **TSD is sufficient, not necessary.** It discards the couplings between different U_f, namely Lemma W(a) for mixed diagonal colors and Lemma W(b) for mixed corners, and every other L of V(D).

TSD is **OPEN**.

## 4. Check of the chain from MS to (D-a)

**Step 2 (summed rank-neighbour inequality).** Correct, but only when the common rank satisfies c < min_e s_e.
- **Repair.** Let k be the number of classes with s_e > c. The classes with s_e <= c contribute at most (3-k)c in total.
- For k < 3 the joint inequality is weaker than the single-class one, since the multiset θ·3v is thicker than v. So one uses single-class caps: `sum_e s_e <= (3-k)c + kK(S) <= 2K(S) + c`.
- This is <= 3(1-δ')K(S) only if c <= (1-3δ')K(S).
- This condition must be checked against the rank c used in the certification. It is a genuine gap in the chain as written, and it may be closed by choosing c.

**Staggering.** The joint bound uses the common span S of F_d(D_c) for all three classes of main color c. It therefore loses the 12-way staggering inside each triple, which is an additive loss of a few starts per shift. By the sensitivity data, this is negligible.

**Step 3.** Correct. MS at λ = S also gives H_tot <= C_w(S) <= θC_{3v}(S), where θ = 1-δ. This is needed so that the comparison multiset is large enough.

**Steps 4–5, made rigorous (PROVED).** Put θ = 1-δ and E_c = sum_{i<c}(c-i)e_{i+1}. Let C_v(λ) = sum_{l<=λ} v_l, and P_v(x) = sum_{λ>=0} (x - C_v(λ))_+ for 0 <= x <= C_v(S).

- **Prefix lemma.** If all three classes have size > c, the prefix lemma and MS give
  `P(H_tot; w) >= sum_λ (H_tot - θC_{3v}(λ))_+ = 3θ P_v(y/θ)`, with `y = c·s̄ - c(c+1)/2` and s̄ the mean class size.
- **Joint inequality.** Hence `2θ P_v(y/θ) + 4E_c <= S c(c+1)`.
- **Scaling.** Let C̃ be the piecewise-linear interpolation of C_v. It is concave with C̃(0) = 0, because v_l = Q(S-l)+Q(S-l-1) is nonincreasing in l. So θC̃(λ) <= C̃(θλ).
  - Put P̃(x) = ∫_0^∞ (x - C̃(λ))_+ dλ. Then `P̃(x/θ) = θ^{-1}∫(x - θC̃(λ))_+ dλ >= θ^{-1}∫(x - C̃(θλ))_+ dλ = θ^{-2}P̃(x)`.
  - The integrand is nonincreasing in λ, so `P_v(x) - x <= P̃(x) <= P_v(x)`.
- **Conclusion.**

  **`2(P_v(y) - y) <= θ (S c(c+1) - 4E_c)`.**

  This is the single-class certification inequality with its right side multiplied by (1-δ), up to the additive slack 2y.
- **Recertification.** Define K_θ(S) as the largest s for which this inequality holds with y = cs - c(c+1)/2, for the certification's rank c. Then under MS, `sum_e s_e <= 3K_θ(S)`, subject to the repair of Step 2.

**Size of δ'.** In the regime P_v(y) ≈ y^2/(2v̄), y scales like sqrt(θ). This gives `δ' ≈ 1 - sqrt(1-δ) ≈ δ/2` on the y-part. This is a heuristic estimate, not a computed constant. The exact δ' needs the certified e_j and c.

## 5. Open questions (explicit)

1. **MS** itself, with an explicit δ.
2. **TSD(m0, δ)**: the two-Sidon binary-source deficit of Section 3, a purely 2-color problem.
3. Whether the cross-f couplings of Lemma W give a deficit even if TSD fails.
4. Whether AABA (or ABAA) is realizable in an actual proper ternary source.
5. Whether the certification's rank c satisfies c <= (1-3δ')K. This is needed for the Step 2 repair.

=== END OF ANSWER round4_q2 ===
