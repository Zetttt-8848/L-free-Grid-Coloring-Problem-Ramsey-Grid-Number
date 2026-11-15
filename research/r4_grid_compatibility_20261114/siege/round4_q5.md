kind: attempt

Open question attempted (flagged OPEN by this run, ledger entry 41): the missing statement MS below. Give a complete proof of exactly MS, or an explicit counterexample, BY A NAMED APPROACH NOT YET TRIED IN THIS RUN: an analytic / Fourier-uniformity argument (the earlier attempts used local pattern-forbidding of additive quadruples, request-energy bounds, and a corner-exclusion independence heuristic, none of which closed). The approach to pursue:
(1) Quantitative structure of near-maximal Sidon sets: a Sidon set A in an interval of length N with |A| >= (1-eta) sqrt(N) is equidistributed in subintervals and has small nontrivial Fourier coefficients (Erdos-Turan / Lindstrom-type bounds, with explicit dependence on eta; prove what you use).
(2) The color Cauchy-Schwarz identity and its equality case (stated in the suggestion section below): saturation of MS forces the three classes S_e(d) to be locally equidistributed in F_d(D) at every window scale, and forces the agreement of z_d at lag l to be near the cap 3 v_l.
(3) A counting lemma for directed L's whose arm cells and corner cells are prescribed by membership in the (uniform) Golomb pieces and the classes: combine Lemma F, the corner exclusion (an L with both arms e has corner != e) and uniformity to show that saturation forces a positive density of monochromatic L's, or that some request set R_e(h) must exceed (2/3)|F_h(D)| for all three e, contradicting the double cover (iii). Track every constant so delta is explicit.
You may depart from this approach if you say why.

A proof of MS for only some of the cases it covers - a sub-class of sources (e.g. sources under an extra near-extremality or density hypothesis) or a sub-range of its parameters (some d, some lambda, some S) - does NOT answer the question, though it should be reported if it is all you found (in particular: a proof under a stated saturation-at-every-lag hypothesis, with explicit constants, is worth reporting). A non-explicit delta does not answer it.

**Missing statement (MS).** Let Q(m), for m >= 0, be the largest size of a Sidon set (no a+b = c+d except trivially, 3-term progressions included) contained in m+1 consecutive integers, and put Q(m) = 0 for m < 0. Then there is an explicit absolute constant delta > 0 such that the following holds for every proper ternary source (D, chi), i.e. every finite set D of integers with a coloring chi of V(D) = {(v,u) : u < v, u,v in D} by P = {0,1,2} having no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0. For every d >= 1 with F_d(D) nonempty, write
- S = max F_d(D) - min F_d(D);
- v_l = Q(S-l) + Q(S-l-1), the per-class fiber cap of the consumer;
- S_e(d) = {u in F_d(D) : chi(u+d,u) = e};
- r_X(l) = #{u in X : u+l in X}.

Then for every integer lambda with 1 <= lambda <= S,

    sum_{l=1}^{lambda} sum_{e in P} r_{S_e(d)}(l)  <=  (1-delta) * sum_{l=1}^{lambda} 3 v_l.

Equivalently: the lag-l agreement counts of the 3-colored word z_d(u) = chi(u+d,u) on F_d(D), summed over l <= lambda, fall a fixed proportion short of three times the summed single-class caps. (Each single class satisfies r_{S_e(d)}(l) <= v_l, by the Golomb split below, so the statement asks that the three classes cannot be jointly saturated, in the prefix-averaged sense, for any lambda.) For small S it holds trivially (r_{F_d(D)}(l) <= S-l+1 is far below 3v_l); its content is at large S, in particular at the scale S ~ 2.2*10^7 of the problem.

## How MS would settle Part D at level (D-a) (the chain; check it, and say so if it is flawed)
1. P1 (i)-(v) is proved (below, Part A).
2. Fix a shift d; the three classes S_e(d) partition F_d(D) and each is a binary source of span <= S. Summing the rank-neighbor inequality over the three classes (quoted below, "consumer deduction") gives 2P(H_tot; w) + 12 sum_i (c-i) e_{i+1} <= 3 S c(c+1) with joint multiplicity w_l = sum_e r_{S_e(d)}(l).
3. By the prefix lemma (quoted below), if C_w(lambda) <= C_{w'}(lambda) for every lambda, with w'_l = (1-delta) 3 v_l, the same inequality holds with w replaced by w'. MS gives exactly this domination.
4. No rounding is needed: the sum of the H cheapest selected differences is at least sum_{lambda>=0} max(0, H - C_w(lambda)) (prefix lemma), and MS bounds this below by P*(H) := sum_{lambda>=0} max(0, H - (1-delta) C_{3v}(lambda)), a real-valued functional with the exact scaling P*(H) = (1-delta) P_{3v}(H/(1-delta)), where P_{3v}(x) := sum_{lambda>=0} max(0, x - C_{3v}(lambda)).
5. Optimizing the rank c as in the certification of the single-class cap K then gives sum_e |S_e(d)| <= (1-delta') * 3K(S) with explicit delta' > 0 (heuristically delta' ~ 1 - sqrt(1-delta), from P(H;w) ~ H^2/(2w)). That is the (D-a) inequality per shift, for every proper ternary source, without hypotheses; in the square it lowers U_d by the factor (1-delta').
6. After MS, only the explicit computation of delta' in steps 4-5 would remain; it is elementary. If you prove MS, also carry out steps 4-5 if you can, with explicit constants.

## Proved results you may use (spliced verbatim from earlier answers in this run; all checked)

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

### Context: what is already known NOT to work (statements only)
- Per-start or per-shift request inequalities (UW(lambda): min_e N_e(h) <= lambda|F_h(D)|; energy bounds sum_u m_{e,h}(u)^2 <= C(N_e + N_e^2/|F_h|); union growth |R_e(h)| >= f(N_e/|F_h|)|F_h|) are all false over arbitrary proper ternary sources, by explicit sparse digit-type families (also lifted by a fine Sidon block so that class sizes and fibers at the request lags reach span^{1/2-o(1)} with a tiny constant). These families have fibers far below v_l, so they do NOT contradict MS.
- The union of the two same-corner-color pieces G_e^f ∪ G_{e'}^f need not be Sidon (explicit proper source on D = [0,10)). Two disjoint Sidon sets can each be near-maximal (e.g. a Singer set and a translate minus one point), so plain disjointness gives no saving.
- Forbidding AABA/ABAA (if it were true; it is open) gives no saving by counting alone.
- For fixed density rho > 0 there are no proper ternary sources of density rho on arbitrarily long intervals (corners theorem), but that is non-explicit and useless at the scale 2.2*10^7.

## The director's heuristic, including the color Cauchy-Schwarz identity (you are free to discard the heuristic parts)
- Equality in MS needs all six Golomb pieces G_e^f(l) = F_l(S_e(d)) ∩ S_f(d+l), e != f, to be near-maximal Sidon sets for most l <= lambda. Near-maximal Sidon sets are Fourier-uniform and equidistributed in intervals (Erdos-Turan / Lindstrom type facts; prove what you use).
- Color Cauchy-Schwarz (proved, elementary): for Y = F_d(D), w >= 0 supported on [1,t], a_k = sum_i w_i w_{i+|k|}, one has sum_{k in Z} a_k r_Y(k) <= 3 sum_e sum_{k in Z} a_k r_{S_e(d)}(k) (with r_X(0) = |X|, r_X(-k) = r_X(k)), because sum_k a_k r_X(k) = sum_x (1_X * w)(x)^2 and (y_0+y_1+y_2)^2 <= 3(y_0^2+y_1^2+y_2^2) pointwise. With the per-class caps this gives sum_{l>=1} a_l r_{F_d(D)}(l) <= a_0|F_d(D)| + 9 sum_{l>=1} a_l v_l. In the heuristic regime of the problem both sides are about 8.5*10^4, i.e. the regime sits at near-equality: the three classes must be locally equidistributed in F_d(D) at window scale t, and the agreement rate of z_d is about 1/3, the random rate.
- Corner exclusion: for every start u of G_e^f(l) the corner (u+h,u) has color f while both arms have color e; more generally (row/column form) for u < v in D with v-u = h, and d with u+d, v-d in D, never w_u(d) = c_v(d) = w_u(h), where w_u(x) = chi(u+x,u), c_v(x) = chi(v,v-x). If saturation (uniformity) made the row word w_u and the column word c_v asymptotically independent on the two non-corner colors, the agreement rate would be about 2/9, not 1/3 - a proportional deficit.
- Concretely: show that saturation of the six pieces at lags l <= lambda forces two pieces with the same corner color f to share additive quadruples at a positive rate; with Lemma F and the forced AABA/ABAA triangles (below), that would have to yield monochromatic L's at a positive rate. Or show that saturation makes |R_e(h)| > (2/3)|F_h(D)| for all three e on many h, contradicting the double cover (iii).
- Risk: MS may be false if near-cap ternary sources with perfectly random-like 1/3 agreement exist. None is known and none is excluded; if you find the statement false, a counterexample (explicit, checkable L by L) is a full answer.

## What to return
1. A complete proof of MS with an explicit delta, or an explicit counterexample with a complete L-by-L properness proof. If neither, the strongest rigorous partial result, clearly labelled as partial, and the precise obstruction you met.
2. If MS is proved: steps 4-5 of the chain with explicit constants (delta' as a function of delta), if you can.
3. If you find the chain from MS to (D-a) flawed, say exactly where.
Rules: every proof complete; every counterexample explicit and checkable L by L; finite computations are evidence only; do not import three-color facts; no claim about R_4 except as an implication from stated hypotheses.
