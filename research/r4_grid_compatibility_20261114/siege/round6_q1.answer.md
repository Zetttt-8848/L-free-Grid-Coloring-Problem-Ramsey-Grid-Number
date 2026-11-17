# round6_q1 answer: the fibre-size deficit FD

## Verdict

**FD: NOT SETTLED.** I found neither a proof nor a counterexample family.

What this file gives:
- a check of the chain in Task Part 2: it is valid, with two bookkeeping remarks (Section 1);
- explicit, PROVED sharpenings of what a counterexample would have to look like (Section 2);
- a PROVED structural lemma, the "band lemma". It states the whole cross-class coupling at one shift as a proper 3-coloring of a sparse grid. It contains Lemma W and (iv.0) as special cases (Section 3);
- a PROVED counting identity together with a HEURISTIC balance computation. Together they show why counting arguments that use only lag pairs fail to give a deficit (Section 4);
- where the argument stops, and what I believe (Section 5).

Labels: PROVED, CITED (from memory), HEURISTIC.

Notation: `A := sqrt(v_1 S)`, `X_e = S_e(d)`, `s_e = |X_e|`, `T = sum_e s_e = |F_d(D)|`, `Y = F_d(D)`.

---

## 1. Check of the chain (Task Part 2)

Steps 1 to 4 are correct as stated. I checked them against Sections 3.1 to 3.3.
- Heredity gives span `X_e <= S`.
- Proposition 2.1(a) gives `r_{X_e}(l) <= v_l <= v_1`.
- Corollary F0 gives `s_e <= K_F(S)` and `K_F(S) >= A`.

So FD implies `T <= (1-eta) 3A <= (1-eta) 3K_F(S)`.

Remarks for the consumer. Neither is a flaw in the logic.

1. **Which caps.** The consumer's `U_d` is built from the rank caps `K(n-d-j-1)`, not from `K_F`. FD gives the bound relative to `3A`. To use it, one needs `A <= K(span)` at the spans involved, with `Q` replaced by a certified upper bound `Q_cert`. The RHS of FD is increasing in `v_1`, so this replacement is legitimate. The problem's estimates give `A ≈ 4.55*10^5 < K ≈ 4.58*10^5`. Then the saving relative to `U_d` is at least `eta`, and slightly more. This comparison has to be certified numerically by the consumer. I have not done it.
2. **Monotonicity and the hypothesis `S >= S_0`.** FD is applied to each `F_d(D_c)` with its own span `S_c <= n-d-1`. Both `A(S)` and `K_F(S)` are nondecreasing in `S`, because `Q` is nondecreasing. Shifts where `S_c < S_0` satisfy `|F_d(D_c)| <= S_c + 1 <= S_0`, which is negligible against `U_d`. Staggering inside one `c` (the three classes have distinct minima) is lost when FD is used. Over at most 12 unit shifts this is a lower-order loss.

So the implication "FD(eta) implies (D-a) per shift with delta ≈ eta" stands. It is conditional on FD.

---

## 2. Explicit form of the Fejer cap, and what a violator must contain (PROVED)

**Lemma 2.1.** Assume `v_1 <= S` (true for `S >= 16`, by (Q-up): `v_1 <= 2 sqrt(2S) + 2`). Then
`A <= K_F(S) <= A + sqrt(2A) + 3/2`.

*Proof.*
- For `Lam >= 1` and `N = S + Lam` we have `N/Lam = S/Lam + 1`.
- Also `sqrt(v_1 N) = A sqrt(1 + Lam/S) <= A (1 + Lam/(2S))`.
- Let `Lam* = S sqrt(2/A)` and take the integer `Lam` in `[Lam*, Lam*+1)`. Then `S/Lam <= sqrt(A/2)` and `A Lam/(2S) <= sqrt(A/2) + A/(2S)`.
- So the bracket in `K_F` is at most `A + sqrt(2A) + 1 + A/(2S)`, and `A/(2S) <= 1/2` because `A <= S`.
- Admissibility, i.e. `1 <= lambda = Lam - 1 <= S`:
  - `Lam* >= 2` iff `A <= S^2/2`, which holds;
  - `Lam <= S + 1` holds because `Lam* <= S` iff `A >= 2`, and `A >= sqrt(S) >= 2`.
- The lower bound is Corollary F0. ∎

**Corollary 2.2 (each class of a violator is near-extremal).** Suppose `T >= 3(1-eta) A`. Then every class satisfies
`s_e >= (1 - 3 eta) A - 2 sqrt(2A) - 3`.

*Proof.* `s_e = T - sum_{e' ≠ e} s_{e'} >= 3(1-eta) A - 2 K_F(S)`. Apply Lemma 2.1. ∎

**Corollary 2.3 (FD reduces to a single-class deficit; the converse is open).**
- Single-class deficit SCD(eta'): every binary source of span `<= S` has size `<= (1-eta') A`. If SCD(eta') holds for `S >= S_0`, then FD(eta') holds for `S >= S_0`. *Proof:* sum over the three classes.
- Conversely, if FD(eta) fails at span `S`, then three pairwise disjoint binary sources of size `>= (1 - 3 eta - O(A^{-1/2})) A` exist in one interval of `S+1` integers. These are the three classes, and they are coupled as in Section 3.
- What is not proved: that three such near-extremal sources can always be coupled into a ternary source. If they could, FD would be equivalent to SCD. I could not build the coupling. The obstruction is the band coloring of Section 3, which must be a proper 3-coloring of `V(Y)` and of the band jointly.

At the regime, `sqrt(2A) ≈ 954 ≈ 0.0021 A`. So Lemma 2.1 shows `K_F` is within 0.21% of `A`. This is a numerical evaluation of a proved bound; the value of `A` is the problem's estimate.

---

## 3. The band lemma: the full cross-class coupling at one shift (PROVED)

Fix a proper ternary source `(D, chi)` and a shift `d`. Put `Y = F_d(D)` and `cls(y) = e` for `y ∈ X_e`. For `y, a ∈ Y` with `a + d > y`, define `beta(y, a) := chi(a + d, y)`. This is a cell of `V(D)`, because `y ∈ D`, `a + d ∈ D` and `a + d > y`.

**Lemma 3.1 (band lemma).**

(a) `beta(y, y) = cls(y)`.

(b) Let `y, a, b ∈ Y` with `a < b` and `a + d > y`, and suppose `y' := y + (b - a) ∈ Y`. Then the colors `beta(y, a)`, `beta(y, b)`, `beta(y', b)` are not all equal.

So `beta` is a proper 3-coloring of the sparse grid
`B_d(Y) = {(column a, row y) : a, y ∈ Y, a > y - d}`.
Here a directed L is `(a,y),(a+t,y),(a+t,y+t)` with all of `a, a+t, y, y+t` in `Y`. The diagonal classes of this grid are exactly the completion classes `X_e`.

*Proof.*
- (a) This is the definition of `S_e(d)`.
- (b) The three cells `(a+d, y)`, `(b+d, y)`, `(b+d, y+(b-a))` form the directed L with `x = a+d`, `y`, and `t = b-a > 0`.
- All three cells lie in `V(D)`:
  - `y, y' ∈ Y ⊆ D` and `a+d, b+d ∈ D`;
  - `a + d > y`, and `b + d > a + d > y`;
  - `b + d > y'` iff `a + d > y`.
- Properness of `chi` gives (b). ∎

**Special cases.**
- Rows `y = u` and `y' = v` in `X_e`, with `a = u` and `b = v`, give (iv.0): `beta(u, v) = chi(v+d, u) ≠ e`.
- Restricting to rows `p ∈ F_l(X_e)` and columns `q + l` gives `kappa`, hence Lemma W and Corollary U.
- New compared with Lemma W:
  - columns `a < y` inside the band `y - d < a < y`;
  - the case where the column index `a` is not of the form `q + l` with `q ∈ W`.

  When `d << S` (the regime: `d <= 35,000`, `S ≈ 2.2*10^7`) the band below the diagonal is thin. So the new content is small there.

**Reading.** At one shift the problem "one level down" is exactly the following. A sparse grid `Y × Y` (upper triangle plus a band of width `d`) carries a proper 3-coloring with prescribed diagonal. FD asks whether all three diagonal classes can simultaneously reach the binary cap `A`. In a 3-colored grid, every diagonal class has a binary strict source. The "at most two of three" request fact is (iii). The one-color-per-start fact of 3-colored *squares* does not apply here: one class sees only two colors on its strict source, so at most one of those two requests a start. That is Corollary 2.4(c). It is rederived here and not imported.

---

## 4. Lag-pair counting: an exact identity and a balance obstruction

Fix one binary source `(X, psi)` with palette `{0,1}`. Let `Z_j(l)` be its Golomb classes and `z_j(l) = |Z_j(l)|`.

**Parallelograms.** A parallelogram with sides `(l, g)` is a start `u` with `u, u+l, u+g, u+l+g ∈ X`. Let `P(l,g)` be their number; it equals `r_{F_l(X)}(g)`. Call a parallelogram *l-agreeing* if `psi(u,u+l) = psi(u+g,u+g+l)`. Let `Ag(l,g)` be the number of l-agreeing parallelograms.

**Lemma 4.1 (PROVED).**

(a) `Ag(l,g) <= 2` for every `(l,g)`: at most one parallelogram agrees in each color, by the Sidon property of `Z_j(l)` (iv.2).

(b) For every `l`: `sum_{g>=1} Ag(l,g) = sum_j C(z_j(l), 2) >= (1/2) C(r_X(l), 2) - r_X(l)/4`. Also `sum_{g>=1} P(l,g) = C(r_X(l), 2)`.

(c) An l-agreeing parallelogram of color `j` forces `psi(u, u+l+g) = 1-j`, i.e. `u ∈ Z_{1-j}(l+g)` (Corollary 2.4(b)). Fix `m`. The l-agreeing parallelograms of color `j` with `l + g = m` have at most `m-1` distinct starts, one per `l`. All of them lie in `Z_{1-j}(m)`.

*Proof.*
- (a) is the Sidon property.
- (b) The l-agreeing parallelograms of color `j` correspond to ordered pairs `u < u+g` in `Z_j(l)`. Then use `z_0 + z_1 = r` and `z_0^2 + z_1^2 >= r^2/2`, which give `sum_j z_j(z_j-1)/2 >= r^2/4 - r/2 = (1/2) C(r,2) - r/4`.
- (c) is Corollary 2.4(b), together with (a). ∎

So, unconditionally, at least half (up to `r/4` per lag) of all lag-l parallelogram incidences are agreeing. Each agreement forces one cell, and all agreements at one outer pair carry the same color. That is the separation lemma.

**Balance computation (HEURISTIC).** Take the saturated profile that a violator needs: `r(l) ≈ 2 sqrt(S)` and density `rho^2 ≈ 2/sqrt(S)`.
- Fejer (Lemma F applied to `F_l(X)`; this lower bound is PROVED for weighted averages over `g`) gives an average of `P(l,g)` over small `g` that is at least about `r(l)^2/S ≈ 4`.
- Lemma 2.6 gives `Ag(l,g) ≈ 2`, its maximum, at almost every small `g`.
- So about half of the incidences agree. This is exactly the proportion a random 2-coloring gives.
- At lag `m`, color `j` must supply about `m - 1` forcings into a Sidon set of size about `sqrt(S)`. The available inscribed multiplicity is about `2m/sqrt(S)` per start over about `2 sqrt(S)` starts. That totals `4m` slots against a demand of `2m` agreeing slots.

All lag-pair constraints are met with equality in proportion; none is violated. So no argument that uses only the quantities `P`, `Ag`, Sidon, transport and separation, counted lag pair by lag pair, can give `eta > 0`. This is a DEAD END for counting proofs. It is heuristic because it assumes random-like distributions.

**Structured colorings ruled out (PROVED, small claims).** All of the following force a loss of a constant factor, so none of them yields a counterexample:
- (1) `psi(a,b) = phi(b-a)`: every `F_t(X)` must be Sidon, so `r <= Q` and `s <= (1+o(1)) A/sqrt(2)`.
- (2) `psi(a,b) = phi(a+b)`: the three cells of a corner have sums `2a+t`, `a+c+t`, `2c+t`, a 3-AP with difference `c-a`. So `phi` must avoid monochromatic 3-APs on every realized difference.
- (3) `psi = f(a) + g(b) + h(b-a) mod 2` with `h` the parity: within each `f`-class, `F_t(X)` must have all differences odd. Since `odd + odd = even`, each such class has at most 2 elements.

Item (3) is proved only for parity `h`. For block-periodic `h` the same parity-at-scale argument is only HEURISTIC.

---

## 5. Where the argument stops; open questions; belief

**Stopping point.** A proof of FD must do one of two things:
- (A) prove a single-class deficit SCD(eta). This would improve the binary-source capacity itself. No known argument beats the Fejer/rank cap by a constant factor, and by Section 4 lag-pair counting cannot.
- (B) exploit the band coupling of Lemma 3.1 across the three classes. I found no inequality in which the coupling enters quantitatively. The coupling cells `beta(y,a)` with `cls(y) ≠ cls(a)` are free of the (iv.0) constraint, and the mixed corners of Lemma W(a) impose only non-monochromaticity of triples with three distinct cells.

A refutation would need binary sources of size about `sqrt(2) S^{3/4}`, three of them coupled. None is known: the known constructions have size `span^{1/2+o(1)}`, as stated in the brief and from memory.

**Open questions, stated precisely.**
- (O1) SCD: is there `eta > 0` with `|X| <= (1-eta) sqrt(v_1 S)` for every binary source of span `S >= S_0`?
- (O2) Is the maximal binary-source size `O(S^{3/4 - c})` for some `c > 0`, or even `S^{1/2+o(1)}`? Either answer would settle FD at once, with `eta -> 1`.
- (O3) Converse coupling: can three disjoint near-extremal binary sources in one interval always be realized as the classes at one shift of a proper ternary source? A yes would make FD equivalent to SCD.

**Belief (not evidence).** I think FD is true, and more strongly that binary sources are far below `S^{3/4}`. The reason is that every structured candidate fails by a constant factor (Section 4), and the dense cross-lag system of Section 3.5b looks overdetermined. But I have no proof, and the counting heuristics are exactly balanced. Nothing here implies a new bound on `R_4`.

=== END OF ANSWER round6_q1 ===
