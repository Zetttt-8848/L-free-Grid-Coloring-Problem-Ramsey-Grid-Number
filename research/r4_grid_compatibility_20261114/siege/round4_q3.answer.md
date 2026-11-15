# round4_q3 answer: the missing statement MS (joint prefix-averaged fiber deficit)

## 0. Outcome

**MS is not settled.** I found neither a proof nor a counterexample. Section 4 says where both attempts stopped. What is proved:

1. **Chain audit (Section 1, proved).** The chain from MS to (D-a) is correct, but MS as stated asks for more than the consumer needs, and in a fragile way.
   - (a) Only lags `lambda` with `(1-delta) C_{3v}(lambda) < H_tot` are used. At the problem's scale these are the lags up to about `S^{5/8}`, roughly `3*10^4`, not all `lambda <= S`.
   - (b) Only shifts `d < t = 35,000` and only large spans are used.
   - (c) MS requires one `delta` for all `S`. So one proper source that attains equality at one `(d, lambda)`, at any finite `S`, would refute MS for every `delta`, even though such a source would not matter to the consumer.
   - I state the weaker sufficient form MS* and prove that it suffices (Lemma 1.1).
2. **Steps 4–5 with explicit constants (Section 2, proved as an implication).** MS* with `delta` gives
   `sum_e |S_e(d)| <= 3 sqrt((1-delta) V S (1+1/c)) + 3(c+1)/2` for every admissible rank `c`, where `V` is any upper bound for `v_1`.
   - Relative to the simplified single-class cap made by the same method, this is a proportional saving `delta' >= (1 - sqrt(1-delta)) (1 - (c+1)/(2 K_simp))`. At `S ≈ 2.2*10^7` that is `delta' >= 0.999 (1 - sqrt(1-delta))`, about `delta/2`.
   - So MS would have to hold with `delta ≈ 0.023` to give the hypothetical 21.0M figure.
3. **Near-extremality transfer (Section 3, proved).** If MS fails at `(d, lambda)` with defect `delta`, then each of the six Golomb pieces `G_e^f(l)` is near-maximal on average over `l <= lambda`.
4. **Small-scale exclusions (Section 3, proved).** I prove lower bounds on `S` that any violation of MS at `lambda = 1` must exceed.

Open: MS itself, MS*, and the single-lag version at `lambda = 1`. The obstruction is in Section 4.

## 1. Chain audit

Notation. Fix a proper ternary source `(D, chi)` and a shift `d`. Put:
- `X_e = S_e(d)`, `s_e = |X_e|`, `sigma = s_0 + s_1 + s_2`;
- `S` = the span of `F_d(D)`;
- `w_l = sum_e r_{X_e}(l)` and `C_w(lambda) = sum_{l<=lambda} w_l`;
- `w'_l = (1-delta) 3 v_l`.

For a common rank `c` with `1 <= c <= min_e s_e - 1`, put `H = H_tot = c sigma - 3c(c+1)/2`.

**Steps 1–3 are correct.** The summed rank-neighbour inequality is valid, because each `X_e ⊆ F_d(D)` has span at most `S`. It reads
`2 P(H; w) + 12 sum_i (c-i) e_{i+1} <= 3 S c(c+1)`.
- The union multiset of the selected differences of the three classes has at most `w_l` elements at lag `l`, since these are distinct pairs of a single class.
- `H <= C_w(S)`, since the selected differences are actual pairs. So the prefix lemma applies in the form `P(H; w) = sum_{lambda>=0} max(0, H - C_w(lambda))`.
- The `e_j` are lower bounds on spans and are `>= 0`. Dropping them weakens the inequality, so it stays valid.

**Lemma 1.1 (MS* suffices; proved).** Suppose that **MS\*(H)** holds: for every `lambda >= 0` with `(1-delta) C_{3v}(lambda) < H`, we have `C_w(lambda) <= (1-delta) C_{3v}(lambda)`. Then

`P(H; w) >= P*(H) := sum_{lambda>=0} max(0, H - (1-delta) C_{3v}(lambda))`,

and the right side is a finite sum.

*Proof.* First, finiteness. If `(1-delta) C_{3v}(lambda) < H` held for every `lambda`, then MS\* would give `C_w(S) <= (1-delta) C_{3v}(S) < H`. This contradicts `H <= C_w(S)`. So there is a `lambda_0` with `(1-delta) C_{3v}(lambda_0) >= H`. Since `C_{3v}` is nondecreasing, the terms of `P*` vanish for `lambda >= lambda_0`.

Next, compare the two sums term by term in `lambda`. If `(1-delta) C_{3v}(lambda) >= H`, the `P*` term is `0`, which is at most `max(0, H - C_w(lambda))`. Otherwise MS\* gives `C_w(lambda) <= (1-delta) C_{3v}(lambda)`, so `H - C_w(lambda) >= H - (1-delta) C_{3v}(lambda) > 0`. Now sum and use the prefix lemma for `P(H; w)`. ∎

**Consequences for the formulation.**

(a) **Only short lags matter.** Since `v_l` is nonincreasing in `l` (because `Q` is nondecreasing), `C_{3v}(lambda) >= 3 lambda v_lambda`. MS\* therefore only involves `lambda < H / (3(1-delta) v_lambda)`.

At the problem's scale the following are estimates, not certified numbers:
- `sigma <= 3K ≈ 1.37*10^6`;
- `c ≈ (VS)^{1/4} ≈ 675`, the optimal rank in Section 2;
- `v_lambda ≈ 9.4*10^3`.

This gives `H < 9.3*10^8` and `lambda < about 3.3*10^4`, of order `S^{5/8}`. So MS is needed only for `lambda` up to about `1.5*10^{-3} S`, not up to `S`.

A sufficient **uniform** replacement is **MS_Lambda**: MS for `lambda <= Lambda(S)`, where `Lambda(S)` is any integer with `(1-delta) C_{3v}(Lambda) >= 3 c K(S)`. That inequality implies `>= H`, because `sigma <= 3K(S)` by the single-class cap.

(b) **Only the window and large spans matter.** The outer inequality uses `X_d` only for `1 <= d <= t-1 = 34,999`. There the span satisfies `S <= n-d-1`, and `S` is large for the diagonal classes of a near-extremal square.

If `S` is small, then `sigma` is small. The joint bound of Section 2 is then not needed, because `U_d` uses `K` at the maximal span and `K` is monotone. So a version **MS_{S_0}**, MS only for `S >= S_0` with `S_0` explicit (for instance `S_0 = 10^6`), suffices for the consumer.

(c) **Fragility of MS as stated.** MS asks for one `delta > 0` that is valid for all `S` and all `lambda`. A single proper ternary source with `C_w(lambda) >= C_{3v}(lambda)` for one `d` and one `lambda` therefore refutes MS for every `delta`. Such a source could even sit at moderate `S` and be harmless to the consumer. Any counterexample search should be read with this in mind. Conversely, a proof of MS_{S_0, Lambda} answers the consumer's need without settling MS.

(d) **Staggering.** The joint bound is per main colour `c`, so it replaces three of the twelve terms `K(n-d-j-1)` by one joint term at span `<= n-d-1`. The staggering offsets `j <= 11` change `U_d` only additively, by `O(11 K'(n))`. By the sensitivity note this is negligible.

**I found no flaw in the chain beyond (a)–(d)**, which are refinements rather than errors.

## 2. Steps 4–5 with explicit constants (an implication from MS\*; proved)

Let `V` be any number with `V >= v_1 = Q(S-1) + Q(S-2)`. Then `v_l <= V` for all `l`, so `C_{3v}(lambda) <= 3 V lambda`.

**Theorem 2.1.** Assume MS\*(H) holds at shift `d` with constant `delta in [0,1)`, for every admissible `c`. Then for every integer `c >= 1`:
- either `min_e s_e <= c`, and then `sigma <= c + 2 K(S)`;
- or `sigma <= J_c := 3 sqrt((1-delta) V S (1 + 1/c)) + 3(c+1)/2`.

*Proof.* Suppose `c <= min_e s_e - 1`, and assume `H > 0`; otherwise `sigma <= 3(c+1)/2` and we are done.

By Lemma 1.1 and `C_{3v}(lambda) <= 3V lambda`,
`P(H; w) >= sum_{lambda>=0} max(0, H - a lambda)` with `a = 3(1-delta) V`.

The function `x -> max(0, H - a x)` is nonincreasing on `[0, infinity)`, so its sum over the integers `lambda >= 0` is at least its integral, `H^2/(2a)`.

Insert this into `2 P(H; w) <= 3 S c(c+1)` (the e-terms are dropped). This gives `H^2 <= 9(1-delta) V S c(c+1)`. With `H = c sigma - 3c(c+1)/2`, dividing by `c` gives `J_c`.

In the case `min s_e <= c`, the other two classes are each at most `K(S)`, by the single-class cap at span `<= S`. ∎

**Single-class comparison.** The same argument for one class, with `delta = 0`, gives `s <= K_simp,c := sqrt(V S (1+1/c)) + (c+1)/2`. This is the simplified certified cap. With `V` an upper bound for `2Q(S)`, for instance `V = 2(sqrt(S) + S^{1/4} + 1)` by Lindström's bound (cited from memory), it reproduces `K ≈ 4.58*10^5` at `S ≈ 2.2*10^7`.

From the definitions,
`J_c = 3 sqrt(1-delta) (K_simp,c - (c+1)/2) + 3(c+1)/2 = 3 [ sqrt(1-delta) K_simp,c + (1 - sqrt(1-delta)) (c+1)/2 ]`.

Hence `J_c <= (1-delta') 3 K_simp,c`, with

`delta' = (1 - sqrt(1-delta)) (1 - (c+1)/(2 K_simp,c))`.

The case `min s_e <= c` is harmless: it gives `sigma <= c + 2K`, which is about `(2/3) 3K`.

**Numbers (estimates, not certified).** At `S ≈ 2.2*10^7`, `V ≈ 9.5*10^3` and `c = 675`:
- `(c+1)/(2 K_simp) ≈ 7.4*10^{-4}`;
- so `delta' >= 0.99926 (1 - sqrt(1-delta)) = delta/2 + delta^2/8 + ...` (to first order).

Combined with the sensitivity factor `1 - 3.9 delta'`, the hypothetical 21.0M side, which needs `delta' ≈ 0.0115`, would require MS\* with **`delta ≈ 0.0229`**.

The certified `K` also uses the exact `P_v` and the `e_j`. Redoing that certification with `P*` in place of `P(.; v)` gives a slightly better `delta'` and changes nothing structural.

Both `K_simp` and `J` are monotone in `S`, so they can be applied at span `n-d-1`.

## 3. Partial results on MS (proved)

Notation. For `e != f`, put `G_e^f(l) = F_l(X_e) ∩ S_f(d+l)`. By (iv), `F_l(X_e)` is the disjoint union of the two Sidon sets `G_e^f(l)` and `G_e^{f'}(l)`, where `{e,f,f'} = P`. Both lie in an interval of `S-l+1` integers.

**Lemma 3.1 (near-extremality transfer).** Suppose MS fails at `(d, lambda)` with constant `delta`, that is, `C_w(lambda) > (1-delta) C_{3v}(lambda)`. Then:
- (a) for each `e`: `sum_{l<=lambda} r_{X_e}(l) > (1-3delta) C_v(lambda)`;
- (b) for each of the six pieces: `sum_{l<=lambda} |G_e^f(l)| > (1/2 - 3delta) C_v(lambda) - lambda/2`.

For comparison, `|G_e^f(l)| <= Q(S-l)` and `sum_{l<=lambda} Q(S-l) <= (C_v(lambda) + lambda)/2`. So all six pieces are, on average over `l <= lambda`, within a factor `1 - O(delta) - O(lambda/C_v)` of the Sidon cap.

*Proof.* (a) Each class satisfies `sum_{l<=lambda} r_{X_e}(l) <= C_v(lambda)`. If one class had at most `(1-3delta) C_v`, the total would be at most `(3 - 3delta) C_v = (1-delta) C_{3v}`, a contradiction.

(b) We have `|G_e^{f'}(l)| <= Q(S-l)`. So `sum_l |G_e^f(l)| > (1-3delta) C_v - sum_l Q(S-l) = sum_l Q(S-l-1) - 3delta C_v`.

Deleting one point from a Sidon set in `m+1` consecutive integers leaves one in `m` consecutive integers, so `Q(m-1) >= Q(m) - 1`. Hence `sum_l Q(S-l-1) >= (C_v - lambda)/2`, which gives (b).

The two comparison facts follow from the same inequality `Q(m-1) >= Q(m) - 1`. ∎

So any counterexample family to MS must make all six Golomb pieces near-maximal Sidon sets simultaneously, on average over the prefix of lags. The hypothesis "MS fails" is therefore itself a named near-extremality hypothesis of exactly this form.

**Lemma 3.2 (lag 1: no small violations).** Let `Y = F_d(D)`.

(a) `w_1 <= (8/9)|Y| <= (8/9)(S+1)`.

(b) An instance with `w_1 >= 3 v_1` (equality at `lambda = 1`, which would refute MS for every `delta`) requires `S >= 67`. This uses the optimal Golomb ruler lengths 0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72 for 1 to 11 marks, cited from memory.

*Proof.* (a) `w_1 = #{u in Y : u+1 in Y, z(u) = z(u+1)}`. Cut `Y` into maximal runs of consecutive integers on which `z` is constant. A run of length `rho` contributes `rho - 1` to `w_1`. It also yields `rho - 1` consecutive integers in `A_e = F_1(X_e)`.

`A_e` is a union of two Sidon sets. Nine consecutive integers contain at most `Q(8) = 4` points of each Sidon set, because a 5-mark ruler needs length 11. So `A_e` contains no 9 consecutive integers, and `rho <= 9`. Hence `w_1 = sum (rho - 1) <= (8/9) sum rho = (8/9)|Y|`.

(b) Equality needs `S + 1 >= (27/8) v_1`, where `v_1 = Q(S-1) + Q(S-2)`. Check against the Golomb table:
- For `57 <= S <= 72`: `v_1 = 20`, which forces `S >= 67`.
- For `S = 56`: `v_1 = 19` and `57 < 64.1`.
- For `46 <= S <= 55`: `v_1 >= 18` and `S + 1 <= 56 < 60.75`.
- For `S = 45`: `v_1 = 17` and `46 < 57.4`.
- For `S <= 44`: use `v_1 >= 2Q(S-2)` on each plateau of `Q`. In every case `(27/8) v_1 > S + 1`; for example, `S - 2 in [34,43]` gives `54 > 46`.
- For `S = 1, 2`: `v_1 = 1` and `3` respectively, and `(27/8) v_1` exceeds `S + 1` in both cases. ∎

These exclusions are weak, and the realistic counterexample scale is far larger. Lemma 3.2 only fixes where a finite search for an equality instance must start.

## 4. Where the attempts stopped (the obstruction)

**4.1 Proof side.**

Every proved local fact at a fixed `(d, l)` is compatible with six disjoint near-maximal Sidon pieces. These facts are (iv), Lemma F, and the forced AABA/ABAA triangles. Concretely, take six small translates of one near-maximal Sidon set and make them pairwise disjoint by deleting `O(1)` points each. This satisfies:
- disjointness of the pieces;
- the Sidon property of each piece;
- the no-crossing condition at lag 1 (`u in A_e` implies `u+1 not in A_{e'}`), after spacing.

This is a statement about these constraints only, not a proper source. So no deficit can come from a single lag. Any proof of MS must use cells at the shifts `h + (q-p)`, that is, corners `C(p,q)` far from the `d`- and `h`-diagonals. It must also show that they cannot be consistently coloured when all six pieces are saturated for all `l <= lambda`.

The suggested 2/9-versus-1/3 heuristic makes this precise. For the pair `(u, v = u+h)`, write `f = w_u(h)`. Corner exclusion forbids agreement of the row word `w_u` and the column word `c_v` in colour `f` only. Summing over `(u, h)` gives exactly the total agreement count `sum_{d', l} w_l(d')`; this is (iv) again.

So an agreement rate of 1/3 needs a **positive correlation** between `w_u` and `c_v` on the two non-`f` colours, of size `1/3 - 2/9 = 1/9` per position, for most pairs. Nothing proved excludes such correlation. The missing lemma is an **anti-correlation statement for row and column words of a proper ternary source** in the saturated regime. I could not prove it, and I do not know an explicit form of it that is not equivalent to MS.

The Fourier route needs it too. Near-maximal Sidon pieces are equidistributed (Erdős–Turán / Lindström type facts, cited from memory), but equidistribution of each piece separately is consistent with any correlation between pieces of different lags.

**4.2 Counterexample side.**

- **Dead end: Sidon-block lifting.** Take `D' = D + M B` with `B` a Sidon set and `M > 2 span(D)`. The L's of `V(D')` are:
  - internal L's;
  - "type I" L's: two arm points in one block and two in a later block, with `chi(y_2,y_1)`, `phi(y_4,y_1)`, `chi(y_4,y_3)` not monochromatic whenever `y_2 - y_1 = y_4 - y_3 > 0`;
  - "type II" L's: all three cells across blocks.

  Type II requires the cross colouring `phi` to be a proper 3-colouring of the full product `D x D` with respect to the directed L. That is a three-colour square problem in its own right. Worse, even when it exists, the ratio falls:
  - internal fibers scale by `|B|`;
  - `v` scales to about `2 sqrt(M span B) >= 2 sqrt(2 span D) |B|`;
  - so `C_w / C_{3v}` drops by a factor of at least about `1/sqrt 2` at internal lags.

  Lifting cannot produce ratio-to-1 families, which is consistent with the earlier digit families.
- **Not attempted: direct constructions** with all six pieces saturated, such as `D ⊇ B + {0, 1, d, d+1}` with `B` a union of six Sidon translates. They require a proper 3-colouring of `V(D)` with on the order of `|B|^2` structured L's. I could not produce one by hand. Lemma 3.2 shows that equality instances at `lambda = 1` need `S >= 67`.

## 5. Summary of status

**PROVED**
- The chain from MS to (D-a) is correct (Section 1).
- The weaker MS\* suffices (Lemma 1.1). Only `lambda` up to about `S^{5/8}`, `d < 35,000` and large `S` are needed.
- Explicit conditional cap (Theorem 2.1): `sigma <= 3 sqrt((1-delta) V S (1+1/c)) + 3(c+1)/2`. This gives `delta' >= (1 - sqrt(1-delta)) (1 - (c+1)/(2 K_simp))`, about `delta/2`.
- Lemma 3.1 (near-extremality transfer to all six pieces).
- Lemma 3.2 (lag-1 equality needs `S >= 67`; uses Golomb values cited from memory).

**ESTIMATED, not certified**
- The numerical values at `S ≈ 2.2*10^7`: `c ≈ 675`, `lambda* ≈ 3.3*10^4`, `delta' ≈ 0.9993 (1 - sqrt(1-delta))`.
- The requirement `delta ≈ 0.023` for the 21.0M figure (this also uses the stated sensitivity factor 3.9).

**OPEN**
- MS.
- MS\*, and MS_{S_0, Lambda}.
- The single-lag statement `w_1 <= (1-delta) 3 v_1`.
- Whether any proper ternary source attains `C_w(lambda) >= C_{3v}(lambda)`.
- The row/column anti-correlation lemma of Section 4.1.

No claim about `R_4` is made, except the implication: MS_{S_0, Lambda} with `delta` implies `X_d <= (1-delta') U_d` (up to the additive staggering term), with `delta'` as in Theorem 2.1.

=== END OF ANSWER round4_q3 ===

