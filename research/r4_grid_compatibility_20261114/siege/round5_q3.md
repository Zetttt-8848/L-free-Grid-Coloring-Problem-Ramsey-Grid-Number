kind: attempt

Open question attempted (flagged OPEN by this run, ledger entry 52): the missing statement MS' below, a joint prefix-averaged fiber deficit, with additive slack, for the three completion classes at one shift. Give a complete proof of exactly MS' with explicit constants delta and S_0, or an explicit counterexample to it (a family of proper ternary sources with S -> infinity, checkable L by L, violating it for every delta > 0).

A proof of MS' for only some of the cases it covers - a sub-class of sources (for example under an extra near-extremality or density hypothesis) or a sub-range of its parameters (some d, some lambda, some S) - does NOT answer the question, though it should be reported if it is all you found. A non-explicit delta or S_0 does not answer it either.

**Missing statement (MS'; ledger entry 52, OPEN, locator round5_plan).**
Let Q(m), m >= 0, be the largest size of a Sidon set (all positive differences distinct; 3-term progressions excluded) contained in m+1 consecutive integers; Q(m) = 0 for m < 0. MS' asserts: there are explicit constants delta in (0,1) and S_0 >= 1 such that for every proper ternary source (D, chi) — a finite D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v; u, v in D} by P = {0,1,2} with no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D) — and every d >= 1 with F_d(D) = {u : u, u+d in D} nonempty and S := max F_d(D) - min F_d(D) >= S_0, writing v_l = Q(S-l) + Q(S-l-1), S_e(d) = {u in F_d(D) : chi(u+d,u) = e}, r_X(l) = #{u in X : u+l in X}, one has for every integer lambda with 1 <= lambda <= S:

    sum_{l=1}^{lambda} sum_{e in P} r_{S_e(d)}(l)  <=  (1-delta) · sum_{l=1}^{lambda} 3 v_l  +  S/100.

- It is universal (no hypothesis besides S >= S_0). It is weaker than MS (entry 41): the slack S/100 absorbs complete saturation of all lags up to about sqrt(S)/600, and moderate spans are exempt. It is implied by MS, by SC(delta), and (for large S) by TSD.


## How MS' settles Part D at level (D-a) (the chain; check it, and say exactly where if it is flawed)

1. Entry 9 settles P1 (i)-(v) as posed. It remains to settle Part D at (D-a).
2. Fix a proper ternary source and a shift d with S = span F_d(D) >= S_0. The three classes S_e(d) are binary sources of span <= S (entry 9 (iv.0); heredity, round4_q6 Lemma B1). Let K^Pi(S) be the Pi-form rank-certificate cap at a chosen rank rho (entry 42): every binary source of span <= S has size <= K^Pi(S), and K^Pi >= K.
3. Entry 27 (summed rank-neighbor inequality) and entry 33 (prefix formula) feed Theorem A (entry 42).
4. MS' (below, entry 52) gives the hypothesis of Theorem A with alpha = 1-delta, E_0 = S/100, Lambda_0 <= S.
5. Theorem A with s* = K^Pi(S)+1 gives sum_e |S_e(d)| <= max{2K^Pi(S) + rho, 3 sqrt(1-delta)(K^Pi(S)+1) + S/(100 rho) + 3(1-sqrt(1-delta))(rho+1)/2}. Hence sum_e |S_e(d)| <= (1-delta')·3K^Pi(S) with the explicit
   delta' = min{ 1/3 - rho/(3K^Pi), (1-sqrt(1-delta))(1-(rho+1)/(2K^Pi)) - sqrt(1-delta)/K^Pi - S/(300 rho K^Pi) }.
6. Elementary remaining step (to be written out in the final document, not structural): an explicit lower bound K^Pi(S) >= c_1 S^{3/4} (from v_l <= 2Q(S) <= 2(sqrt S + S^{1/4} + 1) and the definition of the certificate), and the choice rho = floor(K^Pi(S)^{1/2}), make delta' >= delta/2 - O(S^{-1/8}) explicitly, so delta' >= delta/4 for all S >= S_1 with S_1 explicit. At the regime scale (estimates: K ≈ 4.58e5, rho ≈ 675) delta' >= 0.4996 delta - 2.5e-4. This is the (D-a) inequality per shift, with the named span hypothesis S >= S_1, compared to the sum of the three separate (Pi-form certified) binary-source caps.
   - If step 6's lower bound on K^Pi were not available, the inequality still holds at each S with the displayed delta'(S), explicit in terms of the certificate value.


## Proved results you may use (spliced verbatim from earlier answers in this run; each was checked)

(Entry numbers such as "entry 42" refer to this run's internal ledger; every result they name is reproduced below.)

### Part A: P1 (i)-(v), from an earlier answer
### Lemma 0 (parametrization of the L's in V(D))
For integers `u`, `1 <= d < h`, let `L(u,d,h)` be the triple
`(u+d,u)` (horizontal arm end), `(u+h,u)` (corner), `(u+h,u+h-d)` (vertical arm end), arm length `t = h-d`.

(a) `L(u,d,h)` is a directed L: take `x=u+d, y=u, t=h-d>0`. Then `(x+t,y) = (u+h,u)` and `(x+t,y+t) = (u+h,u+h-d)`.

(b) `L(u,d,h) ⊆ V(D)` iff `u, u+d, u+h-d, u+h` all lie in `D`. Proof: `(u+d,u) in V(D)` iff `u,u+d in D` (because `u+d>u`). `(u+h,u) in V(D)` iff `u,u+h in D` (because `h>0`). `(u+h,u+h-d) in V(D)` iff `u+h-d, u+h in D` (because `u+h > u+h-d`, since `d>0`). The point `u+h-d > u` because `h>d`. Collecting these gives the claim.

(c) Every directed L inside `V(D)` equals `L(u,d,h)` for exactly one triple. Proof: let `(x,y),(x+t,y),(x+t,y+t)` lie in `V(D)`. Since `(x,y) in V(D)` we have `x>y`. Put `d = x-y >= 1`, `u = y`, `h = d+t > d`. Then the triple is `L(u,d,h)`. Conversely, `L(u,d,h)` determines `y=u`, `x=u+d`, `t=h-d`. So the map `(u,d,h) -> L(u,d,h)` is a bijection from `{1<=d<h}` with condition (b) onto the L's in `V(D)`.

**Edge cases.** If `d = h-d` or `u+d = u+h-d`, the four points in (b) are not distinct. Condition (b) is still a membership condition on the set `{u,u+d,u+h-d,u+h}`, so nothing changes. The three cells of the L are always distinct, since their x-coordinates are `u+d < u+h` and the last two differ in y (`h-d > 0`). Also `d = t` is allowed: nothing in the argument requires `d ≠ h-d`.

### (i) Exact reformulation
**Claim.** `chi` is proper iff `S_e(h) ∩ R_e(h) = ∅` for all `h >= 2` and all `e in P`.

**Colors of the three cells of `L(u,d,h)`.**
- `chi(u+d,u) = e` iff `u in S_e(d)`.
- Write `w = u+(h-d)`. The vertical arm end is `(u+h,u+h-d) = (w+d,w)`, so `chi(w+d,w) = e` iff `u+(h-d) in S_e(d)`.
- `chi(u+h,u) = e` iff `u in S_e(h)`.

So `L(u,d,h)` lies in `V(D)` and is monochromatic of color `e` iff
`u in S_e(d)`, `u+(h-d) in S_e(d)` and `u in S_e(h)`,
that is, iff `u in F_{h-d}(S_e(d)) ∩ S_e(h)`. These memberships imply condition (b): `S_e(d) ⊆ F_d(D)` gives `u, u+d, u+h-d, u+h in D`.

Taking the union over `1 <= d < h` shows that there is a monochromatic e-colored L with corner row `u` and corner column `u+h` iff `u in S_e(h) ∩ R_e(h)`. By Lemma 0(c), every L in `V(D)` has this form for exactly one `(u,d,h)`. Hence chi has a monochromatic L iff some `S_e(h) ∩ R_e(h)` is nonempty. Both directions follow.

**L's used.** All L's in `V(D)`, in the form `L(u,d,h)`. The corner is `(u+h,u)`, the arms end at `(u+d,u)` and `(u+h,u+h-d)`, and the arm length is `h-d`. The term `d` of `R_e(h)` is exactly the set of L's with corner on diagonal offset `h` and arm length `h-d`.

### (ii) Containment `R_e(h) ⊆ F_h(D)`
Let `u in F_{h-d}(S_e(d))`.
- Then `u in S_e(d) ⊆ F_d(D)`, so `u in D`.
- Also `u+h-d in S_e(d) ⊆ F_d(D)`, so `u+h = (u+h-d)+d in D`.

Hence `u in F_h(D)`. ∎

### (iii) Double cover
Let `k(u) = #{e : u in R_e(h)}` for `u in F_h(D)`. Since `S_0(h), S_1(h), S_2(h)` partition `F_h(D)`, `u` lies in `S_f(h)` for exactly one `f`. By (i), `u ∉ R_f(h)`, so `k(u) <= 2`. If `u in R_e(h) ∩ R_{e'}(h)` with `e ≠ e'`, then `f ∉ {e,e'}`, so `f = e''`.

By (ii), every request lies in `F_h(D)`, so `sum_e |R_e(h)| = sum_{u in F_h(D)} k(u)`. Pointwise, `k(u) <= 2 - [k(u) <= 1]`: if `k(u) = 2` both sides equal 2, and if `k(u) <= 1` the right side is 1. Summing gives the inequality **as posed, which is correct**:
`sum_e |R_e(h)| <= 2|F_h(D)| - #{u in F_h(D) : k(u) <= 1}`.

The sharp form is the identity
`sum_e |R_e(h)| = 2|F_h(D)| - 2·#{k=0} - #{k=1}`.

### (iv) Inside one class
Fix `X = S_e(d)`, `l >= 1`, `h = d+l`. Define `psi(a,b) = chi(b+d,a)` for `a<b` in `X`. These are the cells of the shifted source; they lie in `V(D)` because `a, b+d in D`.

**(iv.0) The shifted source avoids `e`.** For `a<b` in `X`, `L(a,d,d+(b-a))` has horizontal arm end `(a+d,a)` of color `e` (because `a in X`), vertical arm end `(b+d,b)` of color `e` (because `b in X`), and corner `(b+d,a)`. So `psi(a,b) ≠ e`. This is (i) applied to the `d`-term of `R_e(d+b-a)`. Hence `psi` takes values in `{e',e''}`.

**(iv.1) `F_l(X) ⊆ R_e(h)`.** `F_l(X) = F_{h-d}(S_e(d))` is the `d`-term of `R_e(h)`. ∎

**Color identification.** For `u in F_l(X)` we have `u, u+l in X`, so `chi(u+h,u) = psi(u,u+l)`, which lies in `{e',e''}`. Put `G_f = {u in F_l(X) : chi(u+h,u) = f}` for `f in {e',e''}`. These two sets partition `F_l(X)`, and `G_f = F_l(X) ∩ S_f(h)`.

**(iv.2) Golomb split, proved from scratch.** Each `G_f` is a Sidon set. More precisely, there are no `u_1` and `r, s > 0` with `u_1, u_1+s, u_1+r, u_1+r+s` all in `G_f`. The case `r = s` (a 3-term progression) is included. This is equivalent to all positive differences within `G_f` being distinct, including pairs that share an element, i.e. `a+b = a'+b'` only trivially.

*Proof.* Suppose such points exist. Let `g` be the other color of `{e',e''}` and put `u_2 = u_1+r`. All points `u_1+r+s+l`, `u_1+r+l`, `u_1+s+l`, `u_1+l` lie in `X`, since the four points lie in `F_l(X)`. Four L's:
- **L1** `= L(u_1, h, h+r)`: cells `(u_1+h,u_1)` [color f], corner `(u_1+h+r,u_1)`, `(u_1+h+r,u_1+r)` [color f, since `u_2 in G_f`]. So `chi(u_1+h+r,u_1) ≠ f`. This cell is `psi(u_1,u_1+l+r)`, so it is not `e` by (iv.0). Hence it is `g`.
- **L2** `= L(u_1+s, h, h+r)`: same argument with the pair `u_1+s, u_2+s in G_f`. So `chi(u_1+s+h+r, u_1+s) = g`.
- **L3** `= L(u_1, h+r, h+r+s)`: cells `(u_1+h+r,u_1)` [g by L1], corner `(u_1+h+r+s,u_1)`, `(u_1+h+r+s,u_1+s)` [g by L2]. So the corner is not `g`. It equals `psi(u_1,u_1+l+r+s)`, so it is not `e`. Hence it is `f`.
- **L4** `= L(u_1, h, h+r+s)`: cells `(u_1+h,u_1)` [f], corner `(u_1+h+r+s,u_1)` [f by L3], `(u_1+h+r+s,u_1+r+s)` [f, since `u_2+s in G_f`]. This L is monochromatic, a contradiction. ∎

The L's used are L1–L4, all of the form `L(·, h', h'')` with base offset `h' in {h, h+r}`, together with the source-avoidance L's of (iv.0).

**(iv.3)** Put `A = F_l(X) ∩ R_{e'}(h)`. For `u in A`:
- `u in R_{e'}(h)`, so `u ∉ S_{e'}(h)` by (i);
- `u in R_e(h)` by (iv.1), so `u ∉ S_e(h)`.

Hence `u in S_{e''}(h)`, that is, `u in G_{e''}`. Likewise `B = F_l(X) ∩ R_{e''}(h) ⊆ G_{e'}`. Finally, `A ∩ B ⊆ R_e ∩ R_{e'} ∩ R_{e''} = ∅` by (iii). ∎

### (v) Accounting
- **Binary-source property** of `S_e(d)`. This is (iv.0), i.e. the `d`-term of (i): the L's `L(a,d,h')` whose arms both lie on diagonal offset `d`.
- **Golomb split.** This is (iv.2), i.e. L's `L(u,h,·)` and `L(u,h+r,·)` whose arm ends lie in the shifted source of a single class.
- **Capacity `K`, staggering, outer inequality.** These are consequences of the above together with combinatorics on the diagonal.

So the chain already uses (i) only for the **same-shift, same-class** terms. It also uses the fact that `chi(u+h,u) ∉ {e}` on `F_l(S_e(d))`, which is the inclusion (iv.1) read for one `d`.

**New content:**
- the full request sets `R_e(h)`, i.e. the union over all `d < h` and the interaction of different `d` of the same color;
- the containment (ii);
- the at-most-two-of-three cover and its sharp identity (iii);
- the cross-color facts (iv.3): foreign requests fix Golomb-class membership, and `A ∩ B = ∅`.

No three-color fact was imported: (iii) was derived from the partition of `F_h(D)` and from (i).


### Lemma F and the AABA forcing (from an earlier answer). Notation: d, l, h = d+l fixed; a point u of piece G_e^f satisfies u, u+l in S_e(d) and chi(u+h,u) = f; C(p,q) = (q+h,p) for p < q.
## Basic forcing lemma (proved)
**Lemma F.** Let p < q be points in pieces with the same corner colour f, with p in class e and q in class e_q.
Then the cell C(p,q) = (q+h, p) is the corner of L(p,h,h+q-p). Its two ends are (p+h,p) and (q+h,q), and both
have colour f. So chi(C(p,q)) != f. If moreover e_q = e, then p and q+l are both in S_e(d). So
C(p,q) = (q+l+d, p) is a cell of the d-shifted source of S_e(d), and by (iv.0) it is != e.
Hence C(p,q) is the third colour. ∎
- **AABA** (the points a, a+r, a+r+s in class e and a+s in class e'): Lemma F gives C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = e'
  (the last uses r<s or r=s). Then:
  - L(a,h+r,h+r+s) has ends C(a,a+r)=e' and vertical end (a+h+r+s, a+s). Its corner is C(a,a+r+s)=e'.
    So (a+h+r+s,a+s) != e'.
  - That cell is C(a+s,a+r+s), and by the first half of Lemma F it is != f. Hence it is e.
  - L(a,h+s,h+r+s) has ends (a+h+s,a) and (a+h+r+s,a+r)=C(a+r,a+r+s)=e', and its corner is e'. So C(a,a+s) != e'.
    By Lemma F, C(a,a+s) is also != f. Hence C(a,a+s) = e.

  So every cell of the quadruple's corner triangle has a forced colour. I did not find a monochromatic L
  among these cells and the d-cells. Whether AABA is forbidden (it was not observed, which is suggestive) is **OPEN**.

### The r = s case and the ABAA forcing (from a later answer)
## 1. Degenerate case r = s (PROVED)
For AABA the points a+r and a+s coincide when r = s, but they must lie in class e and in class e'. The pieces G_e^f and G_{e'}^f are disjoint, so this is impossible. The same holds for ABAA. So only r < s matters.

## 2. AABA forcing (PROVED; reproduces the previous round)
Here a, a+r, a+r+s are in e and a+s is in e', with r<s. Lemma F gives C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = e'. Two further L's give the rest.
- L(a,h+r,h+r+s) forces C(a+s,a+r+s) = e.
- L(a,h+s,h+r+s) forces C(a,a+s) = e.

The remaining cell C(a+r,a+s) joins different classes, so it is only known to be in {e,e'}.

Checks run without a contradiction:
- every L with corner (a+h+r+s,a) and arm x in {h, h+r, h+s, d}, using the cells (p+h,p+l) whose colour is the class of p;
- the four corners C(.,.) among themselves.

## 3. ABAA forcing (PROVED, new)
Here a, a+s, a+r+s are in e and a+r is in e'. Lemma F on the same-class pairs gives C(a,a+s) = C(a,a+r+s) = C(a+s,a+r+s) = e'.
- **L(a,h+s,h+r+s).** Its arm cells are C(a,a+s) = e' and the vertical end (a+h+r+s, a+r) = C(a+r,a+r+s). Its corner is C(a,a+r+s) = e'. So C(a+r,a+r+s) ≠ e'. Lemma F (first half) gives ≠ f. Hence it is e.
- **L(a,h+r,h+r+s).** Its arm cells are C(a,a+r) and (a+h+r+s,a+s) = C(a+s,a+r+s) = e'. Its corner is e'. So C(a,a+r) ≠ e', and it is ≠ f. Hence it is e.

ABAA is the mirror image of AABA under r <-> s: the roles of the two middle points swap, and the forced triangle is the same up to that swap. Hence any forbidding proof or witness for one transfers formally to the other, provided the extra cells used are mirrored as well. This last point is NOT proved in general.


### The rank-neighbor inequality (the consumer's single-class tool, quoted from the certifying project record)
Consider a hereditary family of finite sets of integers. Let $b_1<\dots<b_s$ be a member of span $L$. Suppose a member with $j$ marks must have span at least $e_j$, for the smaller ranks used below. Choose $1\le c<s$ and take all differences of rank at most $c$, numbering $H=cs-c(c+1)/2$ of them. If the multiplicity of positive difference $h$ is bounded by $v_h$, let $P(H;v)$ be the sum of the cheapest $H$ terms in the multiset containing $v_h$ copies of $h$. Then
$$
 2P(H;v)+4\sum_{i=0}^{c-1}(c-i)e_{i+1}\ \le\ Lc(c+1).
$$
Indeed the sum of the selected differences telescopes to $\sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1})$. The first and last $i+1$ marks each have span at least $e_{i+1}$, so their endpoint difference in this expression is at most $L-2e_{i+1}$. This remains true when the blocks overlap. The sum is at least $P$ by construction. The archive used $e_{i+1}=i$. Here the endpoint blocks belong to the same family as the original set, allowing an induction on cardinality.

### The consumer deduction summed over the three classes (from an earlier answer)
Let the three classes X_e = S_e(d) have sizes s_e and spans <= L'. Use a common rank c < min s_e.
The rank-neighbour inequality for each class gives
2 Σ_sel(X_e) + 4Σ_i(c-i)e_{i+1} <= L'c(c+1), where Σ_sel(X_e) is the sum of the selected differences.
The selected differences of X_e at lag l are pairs in X_e at distance l, at most r_{X_e}(l) of them.
So the union multiset (over e) of selected differences has multiplicity at lag l at most
w_l := Σ_e r_{X_e}(l). Its cardinality is H_tot = Σ_e (c s_e - c(c+1)/2). Hence
Σ_e Σ_sel(X_e) >= P(H_tot; w). Summing over e gives
**2P(H_tot; w) + 12Σ_i(c-i)e_{i+1} <= 3L'c(c+1)**, which is valid for unequal sizes.
If a joint bound w_l <= (1-delta)3v_l holds on all lags used, then P(H_tot; w) >= P(H_tot; (1-delta)·3v).
Since P is evaluated on a thinner multiset, it grows. This caps Σ_e s_e, and so it lowers the per-main-colour
triple inside U_d = Σ_{12 classes} K. Here U_d must be replaced by Σ_c(joint cap of the triple at main colour c).
In the sensitivity model this is exactly the X_d <= (1-delta')U_d input. The size of delta' as a function of delta was not computed.

### The prefix lemma (from a later answer)
**Lemma (prefix form of P).** Take a multiset with w_l copies of each lag l >= 1, and suppose H <= sum_l w_l. Write C_w(λ) = sum_{l<=λ} w_l. Then

    P(H; w) = sum_{λ>=0} max(0, H - C_w(λ)).

*Proof.* Let the H cheapest terms be t_1 <= ... <= t_H. Then sum_k t_k = sum_k #{λ >= 0 : λ < t_k} = sum_{λ>=0} #{k : t_k > λ}. Exactly min(H, C_w(λ)) of the cheapest H terms are <= λ. Hence #{k : t_k > λ} = max(0, H - C_w(λ)). ∎

**Corollary (what suffices).** Suppose that for every λ up to the largest lag used,

    C_w(λ) <= C_{w'}(λ),   with w'_l = (1-δ)·3v_l.

Then P(H_tot; w) >= P(H_tot; w'), because max(0, H - C) is decreasing in C. So the summed rank-neighbour inequality 2P(H_tot;w) + 12Σ_i(c-i)e_{i+1} <= 3L'c(c+1) holds with w replaced by w'. The conclusion is a cap on Σ_e s_e at that main colour and shift.

The hypothesis needed is therefore weaker than a per-lag deficit. It is only a **prefix-averaged deficit**: for every λ,

    Σ_{l<=λ} Σ_e r_{S_e(d)}(l) <= (1-δ) Σ_{l<=λ} 3v_l.

This is a deficit in the lag-l agreement counts of the word z_d, summed over l <= λ. For each fixed d it is a statement about sums over h = d+l of agreement counts. A window-weighted (AD) in the a_h form does **not** directly give prefix domination. One would additionally need (AD) on every initial segment of lags, uniformly in d. The value of δ' (the loss in U_d) as a function of δ is still not computed.

### Theorem A: the conversion from a prefix joint deficit to a cap loss (from an earlier answer; entry 42; re-checked step by step by the director)
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


### Lemma B1 (heredity, from the same answer)
**Lemma B1 (heredity).** If X = S_e(d) and Y ⊆ X, then Y is a binary source of span <= span(Y).

*Proof.* For a < b in Y, the L (a+d,a),(b+d,a),(b+d,b) lies in V(D). Its two ends have colour e, so
chi(b+d,a) != e. The coloring of the cells (b+d,a), a < b in Y, restricted from chi is still proper,
because every L among those cells is an L of V(D). ∎

### The lag-l start set as a 3-colored source; no single pattern forbidden; the TSD reduction (from an earlier answer; entries 43-45)
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


### Near-extremality transfer and lag-1 facts (from an earlier answer; entry 47)
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


### Pair language, Sidon equidistribution, binary reduction, no-collision lemma, and the translate obstruction (from an earlier answer; entry 48)
## 0. Notation and the L's in pair language

Write a cell `(y,x)` with `x<y`, both in D, as the pair `{x<y}`, and write `col(x,y) = chi(y,x)`.
By Lemma 0 of Part A, the directed L's inside V(D) are exactly the triples

    (a, a+delta), (c, c+delta), (a, c+delta),   with a < c, delta > 0, and a, a+delta, c, c+delta in D,

where each entry is a pair (smaller, larger). Proof: L(u,d,h) has cells `(u+d,u), (u+h,u), (u+h,u+h-d)`, i.e. the pairs
`(u,u+d), (u,u+h), (u+h-d,u+h)`. Put `a=u`, `c=u+h-d`, `delta=d`. Then `c > a` because `h>d`, and `c+delta = u+h`. The map is reversible.
So chi is proper iff **no two pairs of equal length delta with distinct left ends a<c have the same colour as the pair
(a, c+delta) that spans them.** In the z-notation this says: never `z_delta(a) = z_delta(c) = z_{c-a+delta}(a)`.

Fix d, a lag l and h = d+l. As in Lemma F, a point u is in the piece `G_x^f` (class x, corner colour f, x != f) iff
`z_d(u)=z_d(u+l)=x` and `z_h(u)=f`. For p<q put `C(p,q) = col(p, q+h)` (this is the cell `(q+h,p)`).

## 1. Reduction R0 (proved)

MS asserts the inequality for every lambda in [1,S]. At lambda = 1 it says
`sum_e r_{S_e(d)}(1) <= (1-delta) 3 v_1`. This is a special case, so MS implies it. Also, if some source has
`sum_e r_{S_e(d)}(1) / (3 v_1)` arbitrarily close to 1, then MS fails for every delta. Conversely, the lag-1 statement does not imply MS.
Hence **the cleanest open core of MS is the lag-1 statement**: the six lag-1 pieces `G_x^f(1)` (six Sidon sets) cannot all be
near-maximal in the span of `F_d(D)`.

## 2. Lemma E: near-maximal Sidon sets are equidistributed (proved, explicit)

**Lemma E.** Let `A ⊆ [0,N]` be a Sidon set with |A| = k, and let T >= 1 be an integer. For integers x in [-(T-1), N]
(there are N+T of them), put `a(x) = |A ∩ [x, x+T)|` and `abar = Tk/(N+T)`. Then

    sum_x (a(x) - abar)^2  <=  T ( k + T - 1 - T k^2/(N+T) ).

In particular, if `k >= (1-eta) sqrt(N)` with `0 <= eta <= 1` and `T <= N`, the relative mean-square deviation satisfies

    (1/(N+T)) sum_x (a(x)-abar)^2 / abar^2  <=  (1+T/N)^2 * ( sqrt(N)/((1-eta)^2 T) + 2eta/(1-eta)^2 + T/((1-eta)^2 N) ).

*Proof.* `sum_x a(x) = Tk`, because each element lies in exactly T windows. Next, `sum_x a(x)(a(x)-1)` counts ordered pairs
(a,a') with a != a' together with a window containing both. That number is `sum_{a != a'} (T-|a-a'|)_+`. Since A is Sidon, every
positive difference g occurs for at most one ordered pair, and so does every negative one. Hence the sum is at most `2 sum_{g=1}^{T-1}(T-g) = T(T-1)`.
So `sum a^2 <= Tk + T(T-1)`, and `sum (a-abar)^2 = sum a^2 - (Tk)^2/(N+T)`. This gives the first claim.
For the second claim, `T k^2/(N+T) >= T(1-eta)^2 N/(N+T) >= T(1-eta)^2 (1 - T/N)`. So the bracket is at most
`k + T(1-(1-eta)^2) + T^2/N <= sqrt(N)+1 + 2 eta T + T^2/N`, using `k <= sqrt(N)+1`, which itself follows from
the first claim (the left side is >= 0) up to lower-order terms. The `+1` is absorbed after dividing. Dividing by `(N+T) abar^2 = T^2k^2/(N+T)`
and using `k^2 >= (1-eta)^2 N` gives the bound. ∎

With `T = N^{3/4}` the relative mean-square deviation is at most `(2eta + 2N^{-1/4})/(1-eta)^2 + o(1)`. So near-maximal Sidon sets
are equidistributed in windows of length `>> sqrt(N)`, in mean square, with explicit dependence on eta. (The `+1` bookkeeping in the
second display is crude. The first display is the exact statement to cite.)

**Remark.** Lemma E is invariant under translation: A and A+t are equally uniform. Section 5 shows why this matters.

## 3. Lemma B: binary reduction of the same-corner union (proved)

**Lemma B.** Fix d, l, h = d+l and a corner colour f. Let `Y = G_x^f ∪ G_{x'}^f` with `{x,x',f} = P`, and put
`beta(p,q) = C(p,q) = col(p, q+h)` for p<q in Y. Then:
(a) beta takes values in `{x,x'}`;
(b) beta(p,q) = x' if p,q are both in `G_x^f`, and beta(p,q) = x if both are in `G_{x'}^f`;
(c) beta is a proper colouring of the strict source V(Y): for p1<p3 in Y and g>0 with p1+g, p3+g in Y, the three values
   beta(p1,p1+g), beta(p3,p3+g), beta(p1,p3+g) are not all equal;
(d) consequently, for every m >= 1, `F_m(Y)` is the union of two Sidon sets, so `r_Y(m) <= 2 Q(span Y)`.

*Proof.* (a) and (b) are Lemma F; I re-derive it. For p<q in Y, the L with `a=p, c=q, delta=h` consists of `col(p,p+h)=f`, `col(q,q+h)=f`
and `col(p,q+h)`, so `C(p,q) != f`. If p and q are both in class x, the L with `a=p, c=q+l, delta=d` consists of `col(p,p+d)=x`,
`col(q+l,q+h)=z_d(q+l)=x` and `col(p,q+h)`. So `C(p,q) != x`, hence it is the third colour.
(c) Take `a=p1`, `c=p3`, `delta=g+h`. The pairs are `(p1,p1+g+h) = C(p1,p1+g)`, `(p3,p3+g+h)=C(p3,p3+g)` and `(p1,p3+g+h)=C(p1,p3+g)`.
All endpoints lie in D, since `p+h` is in D for every p in Y. This is an L of V(D).
(d) Split `F_m(Y)` by the value of beta(p,p+m) into `Z_x, Z_{x'}`. For p<q in Z_y, part (c) with g=m and (a) give `beta(p,q+m) = ybar`, the other colour.
If `p1<p3`, `p1+g = p2`, `p3+g = p4` are all in Z_y (g>0; p2 = p3 is allowed), then (c) with gap g+m gives the three values
`beta(p1,p2+m), beta(p3,p4+m), beta(p1,p4+m)`, all equal to ybar. This contradicts (c). So Z_y is Sidon. ∎

(d) only bounds the cross-correlation `#{(a,b) in A x B : b-a = ±m} <= 2Q-2`. That is far above the random value of about 1,
so it gives no saving. Likewise the binary-source cap `|Y| <= K(span)` is about span/48, far above 2 sqrt(span). **Lemma B gives no saving by itself.**

## 4. Lemma C: complete first-generation forcing and no-collision (proved)

Keep the setting of Lemma B. Write `A = G_x^f` (class colour x) and `B = G_{x'}^f`.

**Lemma C1 (forcing).** Let p in A and q in B.
- If p<q and there is r>0 with p+r and q+r in A, then `C(p,q) = x`.
- If q<p and there is r>0 with q-r and p-r in A, then `C(q,p) = x`.
- With A and B swapped (and x and x' swapped): if p<q and there is r>0 with p-r and q-r in B, then `C(p,q) = x'`;
  if q<p and there is r>0 with q+r and p+r in B, then `C(q,p) = x'`.

*Proof (re-derived; no earlier text is relied on).* **AABA lemma:** let a, a+r, a+r+s be in A and a+s in B, with r,s>0
(r ≠ s is automatic, because A and B are disjoint). Lemma B(b) gives `C(a,a+r) = C(a,a+r+s) = C(a+r,a+r+s) = x'`.
- The L with `(a, c, delta) = (a, a+s, r+h)` has pairs `C(a,a+r)=x'`, `C(a+s,a+r+s)` and `C(a,a+r+s)=x'`. So `C(a+s,a+r+s) != x'`, and with
  Lemma B(a) this gives `C(a+s,a+r+s) = x`.
- The L with `(a, c, delta) = (a, a+r, s+h)` has pairs `C(a,a+s)`, `C(a+r,a+r+s)=x'` and `C(a,a+r+s)=x'`. So `C(a,a+s) = x`.

For the first bullet, take `a=p` and `s=q-p`. For the second, take `a = q-r`, `s = r` and `r_new = p-q`: then `a+r_new = p-r` is in A, `a+s = q` is in B,
and `a+r_new+s = p` is in A, so `C(q,p) = C(a+s, a+r_new+s) = x`. The swapped statements follow by symmetry. ∎

**Lemma C (no-collision).** There are no p in A, q in B, p<q, with r,s>0 such that p+r, q+r are in A and p-s, q-s are in B.
There are no q in B, p in A, q<p, with r,s>0 such that q-r, p-r are in A and q+s, p+s are in B.
Equivalently, for each Delta>0, let `alpha` be the start of the (at most one) A-pair at difference Delta, and `beta0` the start of the
B-pair at difference Delta. If `beta0 < alpha`, no AB-crossing `p` (p in A, p+Delta in B) lies strictly between them.
If `alpha < beta0`, no BA-crossing `q` (q in B, q+Delta in A) lies strictly between them. *Proof:* Lemma C1 would force two different colours on the same cell. ∎

**Heuristic only.** If A and B were independent "random-like" near-maximal Sidon sets in [0,N], each small Delta would have an A-pair, a
B-pair and a crossing with constant probability, and a collision would occur at a positive rate. That would give a
proportional saving. This is the director's heuristic in concrete form.

## 5. Obstruction O: translate pairs defeat the uniformity route (proved)

**Proposition O.** Let A be a Sidon set with no positive difference in {1,2,3,4}, and put B = A+2. (Every Sidon set loses at most
4 points when this condition is imposed, since each difference occurs at most once.) Then A ∩ B = ∅, and the pair (A,B) has **no** configuration
excluded by Lemma C.

*Proof.* (AB case) Suppose p in A, q = a'+2 in B, p<q, p+r and q+r in A, and p-s and q-s in B, i.e. p-s-2 and q-s-2 in A. Then `(p+r, q+r)` and
`(p-s-2, q-s-2)` are two A-pairs with the same difference q-p, and their left ends differ (`p+r > p > p-s-2`). This contradicts Sidon.
(BA case) Suppose q = a1+2 in B, p = a2 in A, q<p, q-r and p-r in A, and q+s and p+s in B, i.e. a1+s and a2+s-2 in A. The A-pairs
`(a1+2-r, a2-r)` and `(a1+s, a2+s-2)` have the same difference a2-a1-2. Sidon forces them to coincide, so `r+s = 2`, i.e. r = s = 1.
Then a1, a1+1 are in A, which is a difference 1 in A, excluded. ∎

**Consequence for the suggested approach.** If A is near-maximal, then by Lemma E both A and A+2 are near-maximal and equidistributed.
Translation does not change any Fourier magnitude: `|hat 1_{A+2}| = |hat 1_A|`. Yet the pair has zero Lemma C collisions. So
**no argument whose only inputs are (i) uniformity of the individual pieces and (ii) Lemma F with the AABA/ABAA forcing can
produce a positive density of contradictions.** Step (3) of the suggested approach needs, in addition, a *cross-uniformity*
statement: the pieces are not translate-correlated. Near-maximality does not supply that.

The translate pattern is also locally consistent with the lag-1 definitions. If A = G_x^f(1) and B = A+2 = G_{x'}^f(1), then for each u in A,
`z_d(u..u+3) = x x x' x'`. No contradiction arises inside the four-point window. (`B = A+1` would be impossible, since
`z_d(u+1)` would have to equal both x and x'.)

**What Proposition O does NOT show.** It is not a counterexample to MS. It checks only the Lemma C constraints. It does not check
the full binary system of Lemma B(c) on Y = A ∪ (A+2), and it does not check the rest of V(D). I began checking whether the whole Lemma B(c)
system on `A ∪ (A+2)` is satisfiable. The non-accidental quadruples reduce to one family:
for a1<a3 in A, the values beta(a1,a1+2), beta(a3,a3+2), beta(a1,a3+2) are not all equal. "Accidental" quadruples
`a1+a4-a2-a3 in {±2,±4}` occur about N times each for near-maximal A, and they impose constraints that depend on position on the
mixed pairs. I did not settle whether the system is satisfiable (**OPEN**). If it is satisfiable for some family of near-maximal A,
the whole same-corner binary layer is powerless, and MS would have to come from cross-corner or cross-lag interactions.


### Six disjoint near-maximal Sidon sets (from an earlier answer; entry 49)
For every prime power q >= 7 there are six pairwise disjoint Sidon sets B_0,...,B_5 in [0, q^2-2], each of size q (B_j = B + j(q+1) mod q^2-1, B a Bose set). Hence at a single lag the constraints "six pairwise disjoint Sidon pieces in an interval of length S-l" are compatible with total piece size (1-o(1))·3v_l: no proof can use only disjointness and the Sidon property of the pieces lag by lag.

### A finite computation (director's check; evidence only for exactly what it checks; entry 54)
Exhaustive search over pairs of disjoint Sidon sets A, B in [0,m] for the maximum of |A|+|B| subject to the TSD hypotheses (a proper 2-coloring c of V(A ∪ B), i.e. no p1 < p3 and g > 0 with p1+g, p3+g in A ∪ B and c(p1,p1+g) = c(p3,p3+g) = c(p1,p3+g), with c constant alpha on A-pairs and constant beta != alpha on B-pairs): the maximum is Q(m)+Q(m-1)-1 or -2 for 7 <= m <= 22, and equals Q(m)+Q(m-1) = 12 at m = 23 and m = 24. Explicit equality instance at m = 23: A = {0,1,4,13,15,21}, B = {2,5,7,16,22,23}, with alpha = 0 on A-pairs, beta = 1 on B-pairs and the mixed pairs colored
(0,2)1 (0,5)1 (0,7)0 (0,16)1 (0,22)1 (0,23)0 (1,2)0 (1,5)1 (1,7)1 (1,16)1 (1,22)0 (1,23)0 (2,4)0 (2,13)0 (2,15)1 (2,21)0 (4,5)0 (4,7)0 (4,16)1 (4,22)1 (4,23)0 (5,13)1 (5,15)0 (5,21)0 (7,13)0 (7,15)0 (7,21)1 (13,16)0 (13,22)0 (13,23)1 (15,16)0 (15,22)0 (15,23)0 (16,21)0 (21,22)1 (21,23)0;
it was checked against all 76 L's of V(A ∪ B). So a single same-corner layer of a single lag can be exactly saturated at small m; TSD can hold only asymptotically, if at all. (This is a U-structure only, not a full ternary source.)

### Context: what is already known NOT to work (statements only)
- Per-start or per-shift request inequalities (UW, request-energy, union growth) are false over arbitrary proper ternary sources (explicit sparse digit families, also lifted so that classes reach span^{1/2-o(1)} with a tiny constant); these have fibers far below v_l, so they do not contradict MS'.
- Pattern-by-pattern forbidding of mixed quadruples cannot work (no mixed pattern is forbidden in the U-structure); uniformity of the individual pieces cannot work (translate obstruction above); hereditary window induction on K reproduces not even the fiber caps; 4-point counts (energy, box counts) are consistent with saturation.

## A suggested mechanism (the director's sketch; you are free to discard it)
- If MS' fails, entry 47 makes all six pieces G_e^f(l), l <= lambda, near-maximal Sidon sets on average, and Corollary U (entry 43) makes each U_f(l) = G_e^f(l) ⊔ G_{e'}^f(l) a binary source of size about 2Q(S-l) whose coloring kappa_l(p,q) = chi(q+d+l,p) is constant on each piece. The m = 23 instance (entry 54) shows one U_f at one lag can be saturated, so no deficit comes from a single small (f, l).
- Cross-lag collisions are too rare at the lags the chain needs: kappa_l(p,p+j) is the cell z_{d+l+j}(p) (z_m(p) = chi(p+m,p)), shared by the structures of all lags l' <= l+j; but a cell lies in about 36 lambda/S of them, so forced-value collisions number about lambda^3/S, negligible against C_w ≈ 6 sqrt(S) lambda unless lambda >~ S^{3/4}, while Theorem A at the optimal rank needs lambda up to about S^{5/8} (estimates). Raising the rank to push Lambda_0 to order S makes the needed statement equivalent to the conclusion itself, so it does not help.
- So the deficit must come from a single lag, asymptotically: the three binary sources U_0, U_1, U_2 of one lag, coupled by Lemma W(a) with mixed diagonal colors and by Lemma W(b). Single-lag first moment (heuristic): U_f has about 2m L-constraints on about m free mixed cells, each forbidding about 1/4 of assignments (units forbid 1/2), so the count of colorings is about (2·(3/4)^2)^m ≈ 1.1^m — borderline. The cross-f constraints of W(a) (cells kappa(p,q) with p in U_f, q in U_{f'}, f != f', constrained by triples mixing three diagonal colors) and W(b) are what could push it below 1.
- Candidate mechanism: a finite gadget — a configuration of O(1) points of W in prescribed pieces with prescribed additive relations — whose W(a)/W(b) constraints are jointly unsatisfiable, plus a counting lemma that six near-maximal Sidon pieces in an interval contain such a configuration at a rate proportional to sqrt(S) per lag (near-maximal Sidon sets realize almost half of all differences, so configurations defined by few difference coincidences occur at a predictable rate; Lemma E gives the needed equidistribution). Each gadget forces one point deleted, and the rate gives delta.
- Risk: the borderline first moment means MS' may be false; a refutation needs a full proper ternary source, not just a lag structure.

## What to return
1. A complete proof of MS' with explicit delta and S_0, or an explicit counterexample family with a complete L-by-L properness proof. If neither, the strongest rigorous partial result, clearly labelled as partial, and the precise obstruction you met.
2. If you find the chain from MS' to (D-a) flawed, say exactly where.
Rules: every proof complete; every counterexample explicit and checkable L by L; finite computations are evidence only for what they check; do not import three-color facts; no claim about R_4 except as an implication from stated hypotheses.
