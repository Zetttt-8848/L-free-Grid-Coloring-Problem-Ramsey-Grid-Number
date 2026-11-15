# round4_q6 answer: does MS settle (D-a), and an attack on MS

Plan. (A) Rederive, and repair where needed, the implication "MS (even a weakened MS') + summed rank
inequality + prefix formula => sum_e |S_e(d)| <= (1-delta') * 3K(S)", with delta' about delta/2.
I re-checked every step of the earlier worker's Part A myself. I keep its idea (a concave interpolation
and quadratic scaling), and I restate the theorem cleanly, because its statement was garbled
("s_0 + s_1' + s_2"). (B) Attack MS. FIRST MOVE: **hereditary window induction**. A binary source
restricted to a window is a binary source, so pairs at lag <= lambda can be counted window by window
against the capacity K. After that I use a second move, the **shear-to-corners reformulation with the
box symmetry T(l,m) = T(m,l)**. Neither appears on the excluded list.

Notation. C_w(lambda) = sum_{l=1}^{lambda} w_l. (x)_+ = max(x,0). The rank is rho, which keeps c free
as a colour name. s_e = |S_e(d)|. w_l = sum_e r_{S_e(d)}(l). E_rho = sum_{i=0}^{rho-1} (rho-i) e_{i+1}.

---

## Part A. MS implies (D-a): derivation

### A.1 Inputs (from the brief)

- (F1) Summed rank inequality. If 1 <= rho < min_e s_e, put H_tot = sum_e (rho s_e - rho(rho+1)/2). Then
  `2 P(H_tot; w) + 12 E_rho <= 3 S rho(rho+1)`.
- (F2) Prefix formula. `P(H; w) = sum_{lambda >= 0} (H - C_w(lambda))_+`, with C_w(0) = 0.
- (F3) Q is nondecreasing. Hence v_l = Q(S-l) + Q(S-l-1) is nonincreasing in l, and v_l = 0 for l > S.
  Also w_l = 0 for l > S, because every class lies in F_d(D), whose span is S.
- (F4) The single-class rank inequality. A binary source of size s > rho and span <= S satisfies
  `2P(rho s - rho(rho+1)/2; v) + 4E_rho <= S rho(rho+1)`. This is the source of K(S).

### A.2 Lemma A1 (continuous comparison)

Let C~ be the piecewise-linear interpolation of the integer points (lambda, C_v(lambda)), with
C~(0) = 0. Its slopes are v_1 >= v_2 >= ... >= 0, so C~ is concave and nondecreasing. Put
`Pi(H) = int_0^inf (H - C~(x))_+ dx`. This is finite for H < C_v(S), and +inf otherwise.

(a) For every integer H >= 0: `P(H;v) - H <= Pi(H) <= P(H;v)`.

(b) For t >= 1: `Pi(tH) >= t^2 Pi(H)`.

(c) For beta > 0 and real H' >= 0: `sum_{lambda>=0} (H' - beta C_v(lambda))_+ >= beta Pi(H'/beta)`.

*Proof.*

- (a) The function f(x) = (H - C~(x))_+ is nonincreasing, and f(lambda) is the lambda-th term of (F2).
  Hence sum_{lambda>=0} f(lambda) >= int_0^inf f. On [lambda-1, lambda] we have C~ <= C_v(lambda),
  so int f >= sum_{lambda>=1} f(lambda) = P(H;v) - H.
- (b) A concave function with C~(0) = 0 has C~(x)/x nonincreasing, so C~(t mu) <= t C~(mu).
  Substituting x = t mu gives Pi(tH) = t int (tH - C~(t mu))_+ d mu >= t int (tH - t C~(mu))_+ d mu = t^2 Pi(H).
- (c) Apply the monotone sum-integral comparison to x -> (H' - beta C~(x))_+, then rescale. ∎

### A.3 Theorem A (proved, given F1-F4)

Weakened hypothesis **MS'(alpha, E_0, Lambda)**: `C_w(lambda) <= 3 alpha C_v(lambda) + E_0` for
1 <= lambda <= Lambda. MS with constant delta is exactly MS'(1-delta, 0, S).

**Theorem A.** Fix a proper ternary source, a shift d, and S as in MS. Let 0 < alpha <= 1 and E_0 >= 0.
Let rho >= 1 and the integer s* > rho satisfy:

1. **Pi-certificate:** `2 Pi(H*) + 4 E_rho > S rho(rho+1)`, where H* = rho s* - rho(rho+1)/2.
2. Every class satisfies s_e <= s* - 1. This holds whenever s* - 1 >= K(S).

Let Lambda_0 be the least lambda <= S with 3 alpha C_v(lambda) >= 3 rho s* + E_0, and Lambda_0 = S if
there is none. Assume MS'(alpha, E_0, Lambda_0). Then

`sum_e s_e <= max{ 2(s*-1) + rho ,  3 sqrt(alpha) s* + E_0/rho + 3(1 - sqrt(alpha))(rho+1)/2 }`.

*Proof.*

- If min_e s_e <= rho, then hypothesis 2 bounds the sum by the first branch.
- Otherwise F1 applies. Write s = sum_e s_e and suppose s is strictly larger than the second branch.
  Then H_tot = rho s - 3rho(rho+1)/2 satisfies `H_tot - E_0 > 3 sqrt(alpha) H*`. This is direct
  algebra: rho times the second branch, minus 3rho(rho+1)/2, minus E_0, equals
  3 sqrt(alpha)(rho s* - rho(rho+1)/2).
- For 0 <= lambda <= Lambda_0, MS' gives `(H_tot - C_w(lambda))_+ >= (H_tot - E_0 - 3 alpha C_v(lambda))_+`.
  The case lambda = 0 is trivial.
- For lambda > Lambda_0, the right-hand side is 0. If Lambda_0 < S, then 3 alpha C_v(lambda)
  >= 3 rho s* + E_0 > H_tot + E_0, because s <= 3(s*-1). If Lambda_0 = S, both C_w and C_v are
  constant beyond S, so the lambda = S case of MS' covers every lambda.
- Hence, by (F2), Lemma A1(c) with beta = 3 alpha, monotonicity of Pi, and Lemma A1(b) with
  t = alpha^{-1/2}:
  `P(H_tot; w) >= 3 alpha Pi((H_tot - E_0)/(3 alpha)) >= 3 alpha Pi(H*/sqrt(alpha)) >= 3 Pi(H*)`.
- F1 then gives 3 S rho(rho+1) >= 6 Pi(H*) + 12 E_rho > 3 S rho(rho+1), by the certificate.
  This is a contradiction. ∎

**Corollary A2.** Take s* = K^Pi(S) + 1, where K^Pi(S) is the largest s for which the Pi-certificate
fails at the chosen rho.

- By Lemma A1(a), K(S) <= K^Pi(S) <= K^+(S). Here K^+ is the P-form cap with the right-hand side
  enlarged by 2H*, a relative change of about 2H*/(S rho^2), which is about 1e-5 in the regime below.
- Therefore MS with constant delta (alpha = 1 - delta, E_0 = 0) gives

  `sum_e |S_e(d)| <= (1 - delta') * 3 K(S)` with
  `delta' = (1 - sqrt(1-delta)) (1 - (rho+1)/(2K)) - (K^Pi - K + 1)/K`,

  provided 2K + rho is below the second branch. This holds for small delta, since K >> rho.
- So delta' ≈ delta/2 (for example 1 - sqrt(1-delta) >= delta/2).

**The factor 1/2 is intrinsic to this route.** In a saturated model, P(H) grows like H^2/(2 * 3 alpha v).
Scaling the prefix by alpha therefore scales the certified size by sqrt(alpha). So MS must be asked
with delta ≈ 2 delta'.

**Numerical orientation (estimates, not computed).**

- In the regime of the brief, K ≈ 4.58e5, v ≈ 9.4e3, and saturation runs to lambda ≈ 3.5e5, so
  rho ≈ 7e3 and (rho+1)/(2K) ≈ 0.008.
- delta' = 0.0115, which is what the sensitivity table needs to bring the excluded side to about
  21.0M, requires delta ≈ 0.023 in MS. The additive slack is harmless up to E_0 ≈ 1e-3 rho K.
- This is HYPOTHETICAL and conditional on MS. It is not a bound on R_4.
- To feed the outer inequality, apply Corollary A2 to each diagonal colour c, with S_c(d) <= n-d-1.
  Then compare 4 * 3K(n-d-1) with U_d = sum_{j=0}^{11} K(n-d-j-1). The difference is the staggering
  term, which is negligible at this scale (estimate).

### A.4 Verdict on (A)

1. **MS is exactly in the consumer's currency.** It concerns prefix sums of the summed fibre profile
   w, which is what the rank inequality consumes. Theorem A turns delta into delta' ≈ delta/2. So MS
   would settle (D-a), on the condition that K is certified by the rank inequality in the Pi-form
   (a negligible change).
2. **MS is stronger than needed.** Only lambda <= Lambda_0 matters (about 3.5e5/alpha in the regime),
   and an additive slack E_0 up to about 1e-3 rho K is free.
   - MS as stated quantifies over all lambda >= 1, with no slack. At lambda = 1 it says that the
     three lag-1 fibres cannot all be near-maximal unions of two Sidon sets. That is a single-lag
     local statement, and the consumer does not need it.
   - I regard the exact form of MS as the riskiest part of it. A counterexample at small lambda would
     not damage the programme. **The target should be MS'(1-delta, E_0, Lambda_0).**
3. **MS is not vacuous, and it sits strictly between known statements.**
   - It follows from the single-class statement SC(delta): C_{r_X}(lambda) <= (1-delta) C_v(lambda)
     for every class X. Proof: sum over e.
   - Conversely, if MS fails at lambda with ratio >= 1-delta, then each class has single-class ratio
     >= 1 - 3delta. Proof: C_{r_e} >= 3(1-delta)C_v - 2C_v, because each C_{r_{e'}} <= C_v.
   - So a counterexample to MS needs **three simultaneously near-saturated binary sources at the same
     shift**. No construction is known that saturates even one.
4. **MS is a single-shift statement.** It does not mention requests from lower shifts. Its only link
   to the request geometry of P1 is through the corner colours of the fibres
   (F_l(S_e(d)) ⊆ S_{≠e}(d+l)). So if MS is true, the proportional loss it records may come entirely
   from single-class structure (SC), not from request interaction. I cannot rule out either possibility.

---

## Part B. Attack on MS

### B.1 First move: hereditary window induction. Result: proved inequality, DEAD as a route

**Lemma B1 (heredity).** If X = S_e(d) and Y ⊆ X, then Y is a binary source of span <= span(Y).

*Proof.* For a < b in Y, the L (a+d,a),(b+d,a),(b+d,b) lies in V(D). Its two ends have colour e, so
chi(b+d,a) != e. The coloring of the cells (b+d,a), a < b in Y, restricted from chi is still proper,
because every L among those cells is an L of V(D). ∎

**Lemma B2 (window count).** For every class X of span <= S and every 1 <= lambda <= S:

`C_{r_X}(lambda) <= ceil((S+1)/lambda) * C(K(2lambda-1), 2)`.

*Proof.*

- Cut [min X, min X + S] into J = ceil((S+1)/lambda) consecutive blocks I_j of length lambda.
- A pair a < b in X with b - a <= lambda and a in I_j has b in I_j ∪ I_{j+1}. So it is a pair inside
  Y_j = X ∩ (I_j ∪ I_{j+1}), which has span <= 2lambda - 1.
- By Lemma B1 and the definition of K, |Y_j| <= K(2lambda-1). Summing over j gives the bound. ∎

**Why it is dead (estimate, not a proof).**

- Take K(L) ≈ kappa L^{3/4}, with kappa ≈ 1.43. This kappa is read off the brief's figures,
  K(2.2e7) ≈ 4.58e5.
- Lemma B2 then gives C_{r_X}(lambda) ≲ (S/lambda) * kappa^2 (2lambda)^{3/2}/2 ≈ 2.9 S lambda^{1/2}.
- Against C_v(lambda) ≈ 2 sqrt(S) lambda, the ratio is about 1.45 sqrt(S/lambda) > 1 for all
  lambda <= S.
- So the hereditary capacity cannot even reproduce the fibre caps, let alone improve on them by a
  proportion. The reason is that K scales as L^{3/4} at every scale, so it carries no lag-specific
  information. Any induction on S that uses only K on sub-windows inherits this loss. To be useful it
  would have to carry the whole fibre profile as its induction hypothesis, and that is MS itself.

### B.2 Second move: shear to corners, and the box symmetry

**Lemma B3 (shear; proved).** Put Z(d,u) = chi(u+d,u), defined on Omega = {(d,u) : d >= 1, u, u+d in D}.

- The directed L (x,y),(x+t,y),(x+t,y+t) maps to {(d,u),(d+t,u),(d,u+t)} with d = x - y and u = y.
  This is an axis-parallel right-isosceles corner.
- So chi is proper if and only if Z has no monochromatic corner inside Omega.
- In these coordinates S_e(d) = {u : Z(d,u) = e}, the binary-source property reads
  `Z(d,a) = Z(d,b) = e => Z(d+b-a, a) != e`, and the fibres satisfy F_l(S_e(d)) ⊆ {u : Z(d+l,u) != e}.

*Proof.* (x,y) -> (x-y, y) sends (x+t,y) to (d+t,u) and (x+t,y+t) to (d,u+t). ∎

**Lemma B4 (box symmetry; proved).** For any set X and l, m >= 1, put
T(l,m) = #{u : u, u+l, u+m, u+l+m in X}. Then

`T(l,m) = r_{F_l(X)}(m) = r_{F_m(X)}(l)`.

*Proof.* Both sides count the same set of u. ∎

**Consequence for a class X = S_e(d) with Golomb pieces A_l, B_l (proved).**

Write r_{A,B}(m) = #{a in A : a+m in B}. Then

`sum_{m<=lambda} r_{F_l(X)}(m) <= 2lambda + #{(a,b) in A_l x B_l ∪ B_l x A_l : 0 < b-a <= lambda}`.

The term 2lambda holds because each Sidon piece realises every difference at most once.

**Dead end (estimate).**

- Suppose the pieces are near-maximal, of size about sqrt(S). Near-extremal Sidon sets are
  equidistributed in long intervals. I cite this from memory as Erdős–Turán/Lindström-type
  distribution results, stated qualitatively; this is not a precise citation.
- Then the cross term is about 2lambda, so sum_{l,m<=lambda} T(l,m) ≈ 4 lambda^2.
- A random set of density p = sqrt(2) S^{-1/4} gives r(l) ≈ 2 sqrt(S) = v_l and T ≈ p^4 S = 4. That
  is also 4 lambda^2.
- So **every count of quadruples (energy, box, or Sidon-piece counts) is consistent with saturation.**
  The saturated regime looks pseudo-random at the level of 4-point statistics.
- Hence no proof of MS can come from 4-point additive counts and the Sidon property of the pieces
  alone. It must use colour constraints that involve shifts other than d and d+l, through corners
  that leave the two rows d and d+l. This agrees with the earlier refuted energy-based candidates.

### B.3 What an argument for MS must use (a structural remark; proved part marked)

- **Proved.** The only constraints that couple the three classes at the same shift d are corners with
  two cells in row d, at (d,a) and (d,b). Their third cell (d+b-a, a) is in row d + (b-a), so it lies
  off row d. A corner with all three cells in row d does not exist.
- So at a fixed d the three classes interact only through the colours of rows d' > d, with each
  pair a < b of row d feeding the single cell (d+b-a, a).
- Pairs of different classes (Z(d,a) != Z(d,b)) impose no constraint at all on (d+b-a, a). Hence:
  - **Proved.** The classes at shift d are coupled only through disjointness and through cells
    (d+l, u) shared by fibres of different classes. A cell (d+l,u) belongs to F_l of at most one
    class, since u must then lie in that class.
  - So at the level of "who constrains which cell" through corners with two cells in row d, **the
    three classes at one shift are decoupled apart from disjointness.**
  - Caveat (proved). Every corner {(a,b),(a+t,b),(a,b+t)} has two cells in row a and one cell in
    row a+t. A cell (d,u) is therefore either one of the two base cells of a corner based at row d,
    or the apex (d,u) = (a+t,b) of a corner based at row a = d-t, whose base cells are (d-t,u) and
    (d-t,u+t). The apex type couples row d to lower rows; it is exactly the request condition
    S_e(d) ∩ R_e(d) = ∅ of P1(i). The remark above does not cover it. It belongs to item 3 below.
- Any proportional joint loss in MS must therefore come from one of two places:
  1. single-class deficiency (SC); or
  2. disjointness, meaning three near-saturated binary sources, each of density about
     sqrt(2) S^{-1/4} ≈ 0.02, cannot be packed disjointly into one interval. Packing does not look
     obstructive at density 0.02 (heuristic), which points back to SC.
  3. Or the constraints come through the rows d' > d, where the cells (d+l, u) of different classes'
     fibres sit in the same rows. Their joint properness, as classes at shift d+l, is the request
     geometry of P1. This is where any genuine inter-class content would live.
- I could not turn this into an inequality.

---

## Summary: proved / estimated / open

**Proved (complete proofs above, from the stated inputs F1-F4).**
- Lemma A1.
- Theorem A and Corollary A2. MS'(1-delta, E_0, Lambda_0) implies
  sum_e |S_e(d)| <= (1-delta')3K(S), with delta' = (1 - sqrt(1-delta))(1 - (rho+1)/(2K)) minus
  negligible certificate and slack terms, so delta' ≈ delta/2. The square-root loss is intrinsic to
  the rank-inequality route.
- SC(delta) implies MS(delta).
- If MS fails with ratio >= 1-delta, then every class has ratio >= 1-3delta.
- Lemmas B1 to B4: heredity; the window count; the shear to corners; the box symmetry.
- The decoupling remark of B.3: at one shift, the three classes constrain disjoint sets of cells.

**Estimates and heuristics (not proofs).**
- The numerical orientation: delta ≈ 0.023 is needed for delta' = 0.0115.
- Window induction is dead: its ratio is about 1.45 sqrt(S/lambda) > 1.
- 4-point counts are consistent with saturation (pseudo-random check).

**Open.**
- (O1) MS itself, and the weaker sufficient MS'(1-delta, E_0, Lambda_0). Neither is proved nor refuted.
- (O2) SC(delta): can a single binary source saturate the fibre caps v_l in prefix average for
  lambda up to about 3.5e5? A negative answer gives MS and hence (D-a) through Theorem A.
- (O3) Whether MS as stated fails at small lambda. For example, can the three lag-1 fibres all be
  near-maximal unions of two Sidon sets? This is harmless for the consumer if MS' holds.
- No new bound on R_4 is claimed. Every R_4 figure above is an implication from the stated
  hypotheses only.

=== END OF ANSWER round4_q6 ===
