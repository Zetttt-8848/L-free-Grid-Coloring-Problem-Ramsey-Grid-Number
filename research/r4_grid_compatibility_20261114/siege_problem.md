# Request geometry inside a three-colored diagonal class (directed L, four colors)

## Background (fixed; do not change the definitions)

**Forbidden configuration.** Cells are `(x,y)`: `x` is the column, `y` the row, both zero-based integers. A directed L is a triple of cells `(x,y), (x+t,y), (x+t,y+t)` with integer `t > 0`. A coloring of a set of cells is **proper** if no directed L lying inside that set is monochromatic. `R_4` is the least `n` such that no proper coloring of the full square `[0,n)^2` uses at most four colors.

**Diagonal classes.** Let `chi` be a proper four-coloring of `[0,n)^2`, and let `z_u = chi(u,u)` be the main-diagonal colors. Let `D = D_c = {u : z_u = c}`.

- For `u < v` in `D`, the cell `(v,u)` cannot have color `c`, because of the L `(u,u),(v,u),(v,v)`.
- So the **strict source** `V(D) = {(v,u) : u < v, u,v in D}` is properly colored with the three colors other than `c`.

More generally, call `(D, chi)` a **ternary source** when `D` is any finite set of integers and `chi` is a proper coloring of `V(D)` with palette `P = {0,1,2}`.

**Notation for a ternary source `(D, chi)`.**

- Fiber: `F_t(X) = {u : u in X, u+t in X}`, and `r_X(t) = |F_t(X)|`.
- Completion classes: for `d >= 1` and `e in P`, `S_e(d) = {u in F_d(D) : chi(u+d, u) = e}`. For each `d`, the three sets `S_0(d), S_1(d), S_2(d)` partition `F_d(D)`. In the square application these are the classes `S_{c,e}(d)` of the R4 proof: equal-colored main-diagonal pairs `(u,u),(u+d,u+d)` of color `c`, sorted by the color `e` of their completion cell `(u+d,u)`.
- Requests: for `h >= 2`, `R_e(h) = union over 1 <= d < h of F_{h-d}(S_e(d))`.
- Request multiplicity: `m_{e,h}(u) = #{d in [1, h-1] : u in F_{h-d}(S_e(d))}`.
- Request count: `N_e(h) = sum_u m_{e,h}(u) = sum_{d<h} r_{S_e(d)}(h-d)`.

**The R4 consumer (established inputs; status as stated).**

- **Binary-source cap.** Each class `X = S_e(d)` has its own strict source shifted by `d`. The cells `(v+d, u)` with `u < v` in `X` avoid two colors. So `X` is a set "with a properly two-colored strict source" (a binary source).
- **Golomb split.** For such a set, each fiber `F_l(X)` splits into two Golomb (Sidon) sets according to the color of `(u+d+l, u)`.
- **Capacity.** A capacity function `K(L)` (the maximum size of a binary source of span at most `L`) is certified by an elementary rank inequality. Near `L ≈ 2.2*10^7` it gives `K ≈ 4.58*10^5`. The per-fiber multiplicity caps are `v_l = Q(L-l) + Q(L-l-1) ≈ 9.4*10^3`, where `Q` is the Golomb cap, about `sqrt(L)`.
- **Staggering.** The twelve classes at main shift `d` have distinct minima. Hence `X_d := sum_{c,e} |S_{c,e}(d)| <= U_d = sum_{j=0}^{11} K(n-d-j-1)`.
- **Outer inequality.** For the parabola window `a_d = sum_i w_i w_{i+d}`, `w_i = i(t+1-i)`, `t = 35,000`, every four-coloring of `[0,n)^2` satisfies `-3 n a_0 + 2 sum_{d=1}^{t-1} (n - d - 4 X_d) a_d <= 0`. With `X_d <= U_d` this excludes `n = 21,987,409`. This is PROVED, elementary, and independently reviewed.
- **What the chain uses.** Each class `S_{c,e}(h)` is bounded only as a binary source in isolation. Nothing in the chain uses that `S_e(h)` must avoid the requests from lower shifts, or how requests of different colors interact.

**Sensitivity (computed exactly; HYPOTHETICAL, not a bound).**

- Suppose `X_d <= (1-delta) U_d` held for every `d` in the window, with capacities recertified at the smaller spans.
- Then the excluded side would drop roughly by a factor `1 - 3.9 delta` for small `delta`. For example, `delta = 0.0115` gives about 21.0 million instead of 21.99 million.
- An additive saving of `Delta` starts at every shift is much weaker: about 63 starts per shift moves the side by only about 1,000.
- Only a proportional saving in `X_d` matters at this scale.

**Heuristic regime (not a theorem).** If all current caps were nearly attained:

- `|S_e(d)| ≈ 4.6*10^5` and `r_{S_e(d)}(l) ≈ 9.4*10^3` for `l` up to about `3.5*10^5`;
- `|F_h(D_c)| ≈ 1.37*10^6`;
- `N_e(h) ≈ 9.4*10^3 * h`, so `N_e(h) / |F_h(D)| ≈ h/146`, which is about 240 at `h = 35,000`.

**Pre-registered candidates that are already REFUTED.** Both are refuted by explicit witnesses, found by a bounded local search and checked against every L. The witness files are `C:\Users\ZhuanZ\Desktop\lgrid-r4-ternary\research\r4_grid_compatibility_20261114\d1\d1_search_seed20261114.json`, checked by `d1\check_witness.py` in the same directory.

- **U1 (refuted).** Claim: `sum_u m_{e,h}(u)^2 <= (3/2) (N_e(h) + N_e(h)^2 / |F_h(D)|)` for all `(D, chi, e, h)`.
  Witness: `D = [0,14)`, `h = 5`, `e = 1`, `|F_5(D)| = 9`. One start carries all four requests: `N = 4`, `sum m^2 = 16 > 26/3`.
- **UW(1) (refuted).** Claim: `min_e N_e(h) <= |F_h(D)|`.
  Witness: `D = [0,18)`, `h = 15`, `|F_15(D)| = 3`, `N_e = (5,5,5)`.
- Both witnesses are small-count or boundary effects (`N` comparable to `|F_h|`, or `h` close to the span). They do not touch the regime in which `N_e(h)/|F_h(D)|` is large.

## Task

**Part P1 (must be proved completely, from the cell coordinates).** For every ternary source `(D, chi)` and every `h >= 2`:

- **(i) Exact reformulation.** `chi` is proper if and only if, for every `h >= 2` and every `e`, `S_e(h) ∩ R_e(h) = ∅`. Here the `S_e(h)` are defined from `chi`, so they automatically partition `F_h(D)`. State precisely which L's this uses: their corner, their arms, and their arm length.
- **(ii) Containment.** `R_e(h) ⊆ F_h(D)`.
- **(iii) Double cover.** Every `u ∈ F_h(D)` lies in at most two of `R_0(h), R_1(h), R_2(h)`. If `u ∈ R_e(h) ∩ R_{e'}(h)` with `e ≠ e'`, then `u ∈ S_{e''}(h)`, where `{e,e',e''} = P`. Consequently
  `sum_e |R_e(h)| <= 2 |F_h(D)| - #{u in F_h(D) : u lies in at most one R_e(h)}`.
- **(iv) Inside one class.** Fix a class `X = S_e(d)`, an internal lag `l >= 1`, and set `h = d+l`. Then `F_l(X) ⊆ R_e(h)`. For `u ∈ F_l(X)`, the color `chi(u+h, u)` is the color of the Golomb class of `F_l(X)` containing `u`. Show: `F_l(X) ∩ R_{e'}(h)` lies in the Golomb class of color `e''`, and `F_l(X) ∩ R_{e'}(h) ∩ R_{e''}(h) = ∅`.
- **(v) Accounting.** State exactly which of (i)–(iv) the R4 chain above already uses, and which content is new.

**Part D (the missing statement; choose the goal).** The consumer needs an inequality valid for every ternary source in the large-ratio regime. Combined with (iii), it should force a proportional loss, in the form

`sum_{e} |S_e(h)| <= (1 - delta) * (sum of the separate binary-source caps)` for an explicit `delta > 0`,

either for each `h` or on average against the weights `a_h`. It may use, as hypotheses, the class sizes and the fiber multiplicities `r_{S_e(d)}(l)` of the regime above, stated as inequalities. Any near-extremality hypothesis must be named.

Settle as much of the following as possible, in order of preference:

- **(D-a)** Prove such an inequality, or a union-growth or anti-collision lemma that implies it, with every constant explicit. Examples: a lower bound on `|R_e(h)|`, an upper bound on the request energy `sum_u m_{e,h}(u)^2`, or a window-averaged version over `h`.
- **(D-b)** Or show that no inequality of this kind can hold. Do this by an explicit construction, or a family of ternary sources with complete proofs of properness, in which `N_e(h)/|F_h(D)|` is large for all three `e` and many `h`, and yet `sum_e |R_e(h)|` stays at most `2|F_h(D)|` with the classes as large as the regime requires. Check whether the construction can sit inside a four-colored square as a diagonal class. Say which variants survive it.
- **(D-c)** Or formulate precisely, and then prove or refute, the forced-color alternative. By (iv), foreign requests fix the Golomb-class membership inside each class's binary source. Are the forced sets themselves Golomb, so that `|F_l(X) ∩ R_{e'}(h)| <= Q(span)`? Does that force an imbalance between the two Golomb classes of `F_l(X)` that lowers `r_X(l)` below `v_l`? State which consumer quantity it would lower.

**Rules.**

- Every claimed counterexample must be an explicit object, checkable L by L.
- Every proof must be complete. A finite computation is evidence only for exactly what it checks.
- Do not import three-color facts: in three colors a fiber start can be requested by only one color. That bound becomes "at most two of three" here and must be rederived.
- Report any result about `R_4` itself only as an implication from stated hypotheses, never as a new bound unless every step is proved.
