kind: attempt

# Task: prove the fibre-size deficit FD, or give an explicit counterexample

Open question attempted: the missing statement FD (the run's ledger lists it as OPEN). It is the last statement standing between the proved Part P1 and level (D-a) of Part D of the problem below. Everything you need from earlier work is spliced in further down, with its proof. The problem statement itself follows this task.

## TASK PART 1. The statement to settle (FD)

Let Q(m) (m >= 0) be the largest size of a Sidon set (all positive differences distinct; 3-term progressions excluded) inside m+1 consecutive integers, Q(m) = 0 for m < 0. FD asserts: there are explicit constants eta in (0,1) and S_0 >= 1 such that for every proper ternary source (D, chi) — a finite D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v; u, v in D} by P = {0,1,2} with no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D) — and every d >= 1 such that F_d(D) = {u : u, u+d in D} is nonempty and S := max F_d(D) - min F_d(D) >= S_0, one has

    |F_d(D)|  <=  3 (1 - eta) sqrt( v_1 S ),   where v_1 = Q(S-1) + Q(S-2).

(Equivalently sum_e |S_e(d)| <= 3(1-eta) sqrt(v_1 S), since the three classes S_e(d) = {u in F_d(D) : chi(u+d,u) = e} partition F_d(D).)

**What counts as an answer.** Either (a) a complete proof of FD with eta and S_0 explicit numbers (or explicit functions you then evaluate), every step proved or citing a named classical theorem; or (b) an explicit family of proper ternary sources (D_k, chi_k), with complete proofs of properness checkable L by L, with spans S_k -> infinity and |F_{d_k}(D_k)| / (3 sqrt(v_1 S_k)) -> 1 (or > 1 - eta for every fixed eta, along the family). A proof of the statement for only some of the cases it covers — a sub-class of the sources (for example sources with some additional structure, or classes with some additional regularity) or a sub-range of the parameters — does not answer the question, though it should be reported if it is all that was found. Label every claim PROVED, CITED (classical theorem, by name) or HEURISTIC. Do not claim anything about R_4 except as an implication from stated hypotheses.

## TASK PART 2. What FD is for (the chain; check it, and say so if it is flawed)

1. Part P1 (i)-(v) is proved (Task Part 3, Section 3.1 below).
2. Fix a proper ternary source and a shift d with S = span F_d(D) >= S_0. Each class S_e(d) is a binary source of span <= S (P1 (iv.0) below: the cells (v+d,u), u < v in S_e(d), avoid colour e; any subset of a binary source is a binary source, by restricting the colouring), and every fibre satisfies r_{S_e(d)}(l) <= v_l <= v_1 (Section 3.3, Proposition 2.1(a)).
3. Corollary F0 (Section 3.2): every binary source of span <= S has size <= K_F(S) := min_{1<=lambda<=S} [N/Lam + sqrt(v_1 N)] (Lam = lambda+1, N = S+Lam), and K_F(S) >= sqrt(v_1 S). So 3K_F(S) is the sum of three separate certified binary-source caps.
4. FD gives sum_e |S_e(d)| = |F_d(D)| <= 3(1-eta) sqrt(v_1 S) <= (1-eta)·3K_F(S): the (D-a) inequality per shift with delta = eta and the single named hypothesis S >= S_0.
- Context (proved, Section 3.2, Proposition C): every earlier, more local target of this run (a joint prefix deficit on the fibre multiplicities sum_{l<=lambda} sum_e r_{S_e(d)}(l), with slack) implies a size deficit of this very kind, so FD is the weakest form; no local fibre statement is easier.
- Necessary for a counterexample (proved, Section 3.4 and Section 3.2 4.3): three binary sources at one shift, each of size about sqrt(v_1 S) ≈ sqrt(2) S^{3/4}; the largest binary sources the run knows are Sidon sets (about sqrt S) and digit-type families (span^{1/2-o(1)}).

## TASK PART 3. Prior results, with their proofs (spliced verbatim from earlier answers)

### 3.1 Part P1 (i)-(v), with Lemma 0 (the L's of V(D))

(From one earlier answer; its own headings are kept.)

Throughout, `(D, chi)` is a ternary source: `V(D) = {(v,u) : u<v, u,v in D}`, `chi : V(D) -> P = {0,1,2}`. A directed L is `(x,y),(x+t,y),(x+t,y+t)`, `t>0`. The **corner** is `(x+t,y)`. The **horizontal arm end** is `(x,y)` (same row as the corner). The **vertical arm end** is `(x+t,y+t)` (same column as the corner). For `{e,e',e''} = P` the letters always denote three distinct colors.
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


### 3.2 The Fejer (sliding-window) material: Q bounds, Lemma F, Corollary F0, Proposition C

(From one earlier answer; "cited item 1" there is the per-fibre cap r_X(l) <= v_l of Section 3.3, Proposition 2.1(a). Its MS'(delta, S_0) is the earlier joint prefix target: for all lambda <= S, sum_{l<=lambda} sum_e r_{S_e(d)}(l) <= (1-delta) sum_{l<=lambda} 3 v_l + S/100.)


Conventions. In this file, X_e := S_e(d), s_e := |X_e|, T := sum_e s_e,
w_l := sum_e r_{X_e}(l), C_w(lambda) := sum_{l<=lambda} w_l, and S is the span
of F_d(D). Every X_e lies in F_d(D), so span X_e <= S. Also v_l = Q(S-l)+Q(S-l-1).
Q is nondecreasing, so v_l is nonincreasing in l, C_v is concave, and
v_l <= v_1 for every l.

## 0. Elementary facts about Q (proved here)

(Q-up) Q(m) <= sqrt(2m)+1. Proof: a Sidon set of size q in m+1 consecutive
integers has q(q-1)/2 distinct positive differences, all <= m.

(Q-low) Q(m) > sqrt(m/8) for m >= 32. Proof: Bertrand's postulate (cited from
memory) gives a prime p with x < p <= 2x, where x = sqrt(m/8) >= 2, so p is odd.
The Erdos-Turan set A = {2pk + (k^2 mod p) : 0 <= k < p} lies in
[0, 2p^2-p-1] ⊂ [0, m]. Suppose a_i + a_j = a_k + a_l. Each residue part is < p,
so the two residue sums are < 2p. Reducing mod 2p gives i+j = k+l and
i^2+j^2 ≡ k^2+l^2 (mod p), hence {i,j} = {k,l}. A 3-AP a_i + a_k = 2a_j forces
i+k = 2j and 2(i-j)^2 ≡ 0, so i = j = k. So A is Sidon with no 3-AP, and |A| = p.

Consequence: for S >= 34, sqrt(S)/2 <= sqrt((S-2)/2) <= v_1 <= 2 sqrt(2S) + 2.

## 1. Lemma F (sliding-window second moment). PROVED.

For a finite X ⊂ Z with |X| = s, span X <= S, and an integer lambda >= 0, set
Lam = lambda+1 and N = S+Lam. Then

  s*Lam + 2 sum_{l=1}^{lambda} (Lam - l) r_X(l) >= s^2 Lam^2 / N.

Proof. Let f(x) = |X ∩ [x, x+lambda]| for integer x. Then sum_x f(x) = s*Lam.
Moreover f vanishes outside an integer interval of length span X + Lam <= N.
Next, sum_x f(x)^2 = sum_{a,b in X} #{x : a,b in [x,x+lambda]}
= sum_{a,b} (Lam - |a-b|)_+ = s*Lam + 2 sum_{l=1}^{lambda}(Lam-l) r_X(l).
Cauchy-Schwarz over the at most N points of the support finishes the proof. QED

Summation by parts: sum_{l<=lambda}(Lam-l) w_l = sum_{mu=1}^{lambda} C_w(mu).

Corollary F0 (Fejer single-class cap, PROVED). Every binary source X of span
<= S satisfies s <= K_F(S) := min_{1<=lambda<=S} [N/Lam + sqrt(v_1 N)].
Also K_F(S) >= sqrt(v_1 S).
Proof. By cited item 1, r_X(l) <= v_l <= v_1. So
2 sum_{l<=lambda}(Lam-l) r_X(l) <= v_1 lambda Lam, and Lemma F gives
s^2 <= N s/Lam + v_1 N. Since s^2 - bs - c <= 0 implies s <= b + sqrt(c), the
bound follows. N > S gives the lower bound on K_F. QED
(At the stated scale, sqrt(v_1 S) ≈ 4.55*10^5 against the rank cap
K ≈ 4.58*10^5. The two caps agree to within about 1%. This comparison is HEURISTIC:
the numbers are the problem's estimates.)
### 4.2 Proposition C (MS' is at least as strong as a size deficit). PROVED.

Define SD(eta), "Fejer size deficit at level eta": for every proper ternary
source and shift d of span S (large),

  sum_e |S_e(d)|^2 < 3 (1-eta) v_1 S.

Claim. Assume MS'(delta, S_0) and 0 <= eta < delta. Then SD(eta) holds for all
S >= max{S_0, 100, 276/(delta-eta)^4}.

Proof. Suppose the contrary: sum_e s_e^2 >= 3(1-eta) v_1 S. Put
Lam = floor(S(delta-eta)/2). Then Lam >= S(delta-eta)/4 >= 2 and
Lam/S <= (delta-eta)/2.
Lower side. By Lemma F and summation by parts,
  sum_{mu<=lambda} C_w(mu) >= (1/2)[3(1-eta) v_1 S Lam^2/N - T Lam].
Upper side. MS' at every mu <= lambda would give
  sum_{mu<=lambda} C_w(mu) <= (1/2)[3(1-delta) v_1 lambda Lam + lambda S/50].
So it suffices to show
  3(1-eta) v_1 S Lam/N - T > 3(1-delta) v_1 Lam + S/50.
Since S/N >= 1 - Lam/S, the left side minus 3(1-delta)v_1 Lam is at least
3 v_1 Lam (delta - eta - Lam/S) >= 3 v_1 Lam (delta-eta)/2 >= (3/8) v_1 S (delta-eta)^2.
By Section 0 this is >= (3/16) S^{3/2}(delta-eta)^2. On the other side,
T + S/50 <= 3(S+1) + S/50 <= 3.1 S for S >= 100. The inequality holds once
sqrt(S)(delta-eta)^2 > 16.6, and S >= 276/(delta-eta)^4 ensures this.
Hence MS' fails at some mu <= lambda <= S, a contradiction. QED

Corollary C1 (PROVED). SD(eta) implies (D-a) with no further input:
T <= sqrt(3 sum s_e^2) < 3 sqrt((1-eta) v_1 S) <= (1 - eta/2) * 3 K_F(S).
This gives a third proof of MS' => (D-a): delta' = eta/2 for any eta < delta.

Reading of 4.2. The chain is MS'(delta) => SD(eta) => (D-a). So every proof of
MS' contains a proof of SD, which is a proportional upper bound on the class
sizes themselves. MS' carries no information beyond SD that the consumer
needs. SD is the weaker and sufficient target. I recommend registering
SD(eta), or the even weaker T^2 <= 9(1-eta) v_1 S, in place of MS'. MS' is not
implausible. But it is not a reduction: it is at least as hard as (D-a) itself.

### 4.3 What a refutation would require (PROVED reduction, OPEN content)

Refuting MS' for every delta needs sources at large S with near-saturated
prefixes. Refuting SD (hence (D-a) in Fejer form) needs three disjoint binary
sources, each of size >= sqrt((1-eta) v_1 S) ≈ sqrt(2) S^{3/4}, living in
F_d(D) and compatible with a proper ternary coloring of V(D).

The only binary sources I can certify are Sidon sets, of size about sqrt(S).
A Sidon set with no 3-AP contains no directed L in its strict source: an L
needs a + b' = a' + b with a < b < b' and a' = a + b' - b < b', and Sidon
(with 3-APs excluded) rules this out. I know of no construction of binary
sources of size of order S^{3/4}; this statement is from memory and is not a
search result.

Consequently:
- if the true maximum binary-source size is <= sqrt((1-eta) v_1 S) for
  large S, then SD(eta) holds trivially;
- a counterexample to MS' would first need a single binary source within a
  factor 1 - o(1) of the Fejer cap. That is a necessary condition, proved in
  4.2 for SD.

This is the obstruction I met: no known object comes near the regime where
MS' could fail. Also, a proof of MS' must beat the single-class Fejer/rank
capacity by a proportional factor for the three classes jointly. No local
(single-lag) argument can do that by W3: at cap size, short-lag saturation
is generic.

### 3.3 Per-fibre cap, the inscribed-pair rule, and difference coverage

(From one earlier answer. X_e = S_e(d), Y = F_d(D), w_l = sum_e r_{X_e}(l); "Lemma B1" is heredity: a subset of a binary source, with the restricted colouring, is a binary source.)

### 2.1 The window in which MS' has content

**Proposition 2.1.** Fix a proper ternary source, a shift d, and delta in (0,1].

(a) For every e and l >= 1, r_{X_e}(l) <= v_l. Hence w_l <= 3v_l and C_w <= 3C_v.

(b) The MS' inequality holds, for this delta and every S >= 1, at every lambda <= lambda_triv := S/(600 delta Q(S)).

(c) Theorem A consumes MS' only for lambda <= Lambda_0. Here Lambda_0 is the least lambda with 3 alpha C_v(lambda) >= 3 rho s* + E_0. Since C_v(lambda) >= lambda v_lambda, we get Lambda_0 <= (3 rho s* + E_0)/(3 alpha v_{Lambda_0}).

*Proof.* (a) F_l(X_e) lies in [min Y, max Y - l], an interval of S-l+1 integers. By (iv.2) it is the union of two disjoint Sidon sets. They cannot both contain the left endpoint, so one of them lies in S-l consecutive integers. Hence r_{X_e}(l) <= Q(S-l) + Q(S-l-1) = v_l.

(b) By (a), C_w(lambda) <= (1-delta) 3C_v(lambda) + 3 delta C_v(lambda). Since Q is nondecreasing, v_l <= v_1 <= 2Q(S), so 3 delta C_v(lambda) <= 6 delta lambda Q(S). This is at most S/100 when lambda <= lambda_triv.

(c) This is the definition of Lambda_0, together with the fact that v is nonincreasing. ∎

**At the regime (estimates).** Take delta = 0.0235, which by step 5 gives delta' ≈ 0.0115.
- lambda_triv ≈ sqrt(S)/(600·0.0235) ≈ 0.07 sqrt(S) ≈ 330.
- Lambda_0 ≈ 3.4e4 ≈ 7 sqrt(S) for rho = 675.

So the entire content of MS' used by the chain lies in **0.07 sqrt(S) < lambda <= 7 sqrt(S)**, a range of two decades of lags at the scale sqrt(S). The query's phrase "about sqrt(S)/600" is the delta = 1 value. For small delta the slack covers up to sqrt(S)/(600 delta).
### 2.3 The inscribed-pair rule for binary sources

Let (X, psi) be a binary source: a finite X ⊂ Z and psi on pairs a<b of X with values in a 2-element palette {f, fbar}, such that there are no a<c and t>0 with a, a+t, c, c+t in X and psi(a,a+t) = psi(c,c+t) = psi(a,c+t). For a class X_x = S_x(d), psi(a,b) = chi(b+d,a) and {f, fbar} = P \ {x}; this is (iv.0) together with Lemma B1. For p<y in X put

    I(p,y) = {t : 0 < t < y-p, p+t in X, y-t in X}.

**Lemma 2.3 (inscribed-pair rule).** psi is proper iff for every p<y in X and every t in I(p,y),

    NOT ( psi(p,p+t) = psi(y-t,y) = psi(p,y) ).

Equivalently, for each pair (p,y), every inscribed pair (p,p+t),(y-t,y) whose two colours agree has the colour opposite to psi(p,y).

*Proof.* Put a = p, c = y-t; then a < c iff t < y-p. The triple (a,a+t),(c,c+t),(a,c+t) is (p,p+t),(y-t,y),(p,y). Every triple in the definition of properness arises exactly once in this way, from (p,y) = (a,c+t). ∎

**Corollary 2.4 (parallel-pair agreement and Golomb-class transport).** Write Z_j(l) = {u : u, u+l in X, psi(u,u+l) = j}. These are the two Golomb classes of F_l(X).

(a) Let p, p+l, p+g, p+l+g lie in X, with l, g >= 1 (l = g allowed). If psi(p,p+l) = psi(p+g,p+g+l) = j and psi(p,p+g) = psi(p+l,p+l+g) = j', then j = j', and psi(p,p+l+g) is the other colour.

(b) Transport: Z_j(l) ∩ (Z_j(l) - g) ⊆ Z_{jbar}(l+g) for all l, g >= 1.

(c) Cross-lag consistency: for each m >= 2, the sets T_j(m) := union over 1<=l<m of Z_j(l) ∩ (Z_j(l) - (m-l)) satisfy T_j(m) ⊆ Z_{jbar}(m), and T_0(m) ∩ T_1(m) = ∅. Hence |T_0(m)| + |T_1(m)| <= r_X(m) <= v_m.

*Proof.*
- (a) Apply Lemma 2.3 to (p, y = p+l+g) with t = l and with t = g; both lie in I(p,y). Neither inscribed pair can have the colour kappa = psi(p,y), so j ≠ kappa and j' ≠ kappa. With two colours, j = j' = kappa-bar.
- (b) If p, p+g are in Z_j(l), apply Lemma 2.3 to (p, p+g+l) with t = l. This gives psi(p, p+l+g) ≠ j. The pair (p, p+l+g) is in X, since p and p+g+l lie in X. So p is in Z_{jbar}(l+g).
- (c) The inclusion is (b) with g = m-l. Then T_0(m) ⊆ Z_1(m) and T_1(m) ⊆ Z_0(m), which are disjoint. ∎

**Ternary form (Corollary 2.5).** Fix a class x at shift d. Let p<q in G_x^f(l), and p<q' in G_x^{f'}(l'), with q+l = q'+l'. Then f = f'. Here G_x^f(l) = F_l(X_x) ∩ S_f(d+l).

*Proof.* Corollary 2.4(c) with psi(a,b) = chi(b+d,a), applied at the pair (p, q+l). Note that psi(u,u+l) = chi(u+d+l,u) = z_{d+l}(u). ∎

In words: the Lemma B forcings C_l(p,q) = third(x,f) and C_{l'}(p,q') = third(x,f') fall on the same cell (q+d+l, p). They are consistent iff the corner colours of p at the two lags agree. Whenever they hit the same cell, this forces z_{d+l}(p) = z_{d+l'}(p).

**Why Corollary 2.4 does not yet give a deficit.** It is locally satisfiable at saturation. Example: for each (l,g), the 00-parallelogram has all four edges 0 and diagonal 1, and the 11-parallelogram has all edges 1 and diagonal 0. Then (a) holds.

For (c), count at fixed m. By Sidon, each Z_j(l) contributes at most one start to T_j(m). So |T_j(m)| <= m-1, while |Z_{jbar}(m)| <= Q(S-m). The constraint bites only through multiplicities: T_j(m) can be small only if many l send their pair to the same start p. That requires p+l, p+m-l in X for many l. At density rho = |X|/S, the available multiplicity per start is about rho^2 m ≈ 2m/sqrt(S) at saturation. Over about sqrt(S) starts this totals about 2m, against a demand of about m. That is a factor-2 margin, not a contradiction (heuristic).

### 2.4 Difference coverage of Sidon sets (explicit)

**Lemma 2.6.** Let A ⊆ [0,N] be Sidon, |A| = k, and T >= 2. Then

    sum_{g=1}^{T-1} (T-g)·[g is not a difference of A]  <=  T(T-1)/2 - T^2 k^2 / (2(N+T)) + T k/2.

*Proof.* For the N+T integers x in [-(T-1), N], let a(x) = |A ∩ [x, x+T)|.
- Each element lies in exactly T windows, so sum a(x) = Tk.
- sum a(x)(a(x)-1) counts ordered pairs a ≠ a' together with a window containing both. This equals sum over a≠a' of (T - |a-a'|)_+ = 2 sum_{g=1}^{T-1} (T-g) r_A(g), with r_A(g) in {0,1} by Sidon.
- Cauchy-Schwarz gives sum a(x)^2 >= (Tk)^2/(N+T).

Hence 2 sum (T-g) r_A(g) >= T^2k^2/(N+T) - Tk. Subtract from sum_{g<T} (T-g) = T(T-1)/2. ∎

Suppose k >= (1-eta) sqrt(N) and sqrt(N) <= T <= N. Then the (T-g)-weighted fraction of missing differences below T is at most about 2 eta + T/N + sqrt(N)/T. So the six near-maximal pieces of Proposition 2.2 realize almost every difference g with sqrt(S) << g << S. Corollary 2.4(b) then applies at almost every (l, g) in that range. This is the "predictable rate" of the director's sketch, made explicit. What is missing is an unsatisfiable gadget to feed it (Section 3).

### 3.4 The lag-l start set as a three-coloured structure (Lemma W, Corollary U)

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

### 3.5 Window-energy identity, local cap, and the size of any counterexample

(From one earlier answer. Its (Q1) is Q(m) >= sqrt(m/8) for m >= 72, proved as (Q-low) in Section 3.2; "Lemma 3.1(a)" is the per-class transfer re-proved inside Proposition N; WE(Lambda; alpha, E) means sum_{l<Lambda} (Lambda-l) sum_e r_{S_e(d)}(l) <= 3 alpha sum_{l<Lambda} (Lambda-l) v_l + E; MS' is as in 3.2; M_u(Lambda) := sum_{l=1}^{Lambda-1} (Lambda-l) u_l for a sequence u, and C_u(lambda) := sum_{l<=lambda} u_l.)

## 3. What MS' contains: the window-energy identity (PROVED)

**Lemma W1.** Let X ⊆ [m, m+S] be finite with |X| = s and Lambda >= 1. Put a(x) = |X ∩ [x, x+Lambda)|. The windows that meet X have x in [m-Lambda+1, m+S], and there are S+Lambda of them. Put abar = Lambda s/(S+Lambda). Then

`sum_x a(x)^2 = Lambda s + 2 M_{r_X}(Lambda)`, and hence
`2 M_{r_X}(Lambda) = Lambda^2 s^2/(S+Lambda) - Lambda s + Var_Lambda(X)`, where `Var_Lambda(X) = sum_{x=m-Lambda+1}^{m+S} (a(x) - abar)^2 >= 0`.

*Proof.* sum_x a(x)^2 = sum_{p,q in X} #{x : p,q in [x,x+Lambda)} = sum_{p,q} (Lambda - |p-q|)_+ = Lambda s + 2 sum_{l=1}^{Lambda-1} (Lambda-l) r_X(l). The second identity is the variance decomposition, using sum_x a(x) = Lambda s. ∎

**Proposition E (WE splits into a size part and a dispersion part).** For the three classes X_e = S_e(d) of sizes s_e, all in an interval of span S, the hypothesis WE(Lambda; alpha, E) is equivalent to

`sum_e [ Lambda^2 s_e^2/(S+Lambda) + Var_Lambda(X_e) ] <= 6 alpha M_v(Lambda) + Lambda s + 2E`.

Consequences:
- (E-a) **WE alone already caps the sizes** by Cauchy-Schwarz (drop Var). Using M_v(Lambda) <= Q(S) Lambda(Lambda-1):
  sum_e s_e^2 <= (S+Lambda)(s/Lambda + 6 alpha Q(S) + 2E/Lambda^2).
  In the regime this gives s <= sqrt(3 sum s_e^2) ≈ 3 sqrt(alpha) sqrt(2Q(S) S) ≈ 3 sqrt(alpha) K. This is a cruder relative of Theorem B.
- (E-b) **Conversely, for equidistributed classes WE is the size bound itself.** If Var_Lambda(X_e) <= eta Lambda^2 s_e^2/(S+Lambda) for each e, then WE(Lambda; alpha, E) holds as soon as
  (1+eta) sum_e s_e^2 <= (S+Lambda)(6 alpha M_v(Lambda) + 2E)/Lambda^2.
  Hence any proof of MS' (or of WE at Lambda ≈ Lambda_c) contains a proof that well-spread triples of binary sources have sum_e s_e^2 <= (1+o(1)) 6 alpha M_v(Lambda_c) S/Lambda_c^2. In the regime, that is a size deficit of the very kind (D-a) asks for.

**Interpretation (calibration, not a theorem).**
- The prefix/window formulation does **not** reduce the problem. It is (D-a) plus a dispersion term.
- It is the natural currency only for *local* proofs: lag-by-lag deficits at lags <= Lambda_c.
- Any such local proof must be strong enough to give the global size deficit for equidistributed classes.
- By Lemma E of entry 48, near-maximal Sidon pieces are equidistributed. So near-extremal configurations are exactly the case in which (E-b) applies.

## 4. Partial results on MS' itself (PROVED)

**Lemma T (trivial range).** MS' holds, for every delta in (0,1), at every lambda <= S/(600 delta (sqrt(2S)+1)).

*Proof.*
- w_l <= 3v_l, so C_w(lambda) <= (1-delta) 3C_v(lambda) + 3 delta C_v(lambda).
- v_l <= 2Q(S), and Q(S) <= 1/2 + sqrt(2S+1/4) <= sqrt(2S) + 1. The middle bound holds because k Sidon points in [0,S] have k(k-1)/2 distinct positive differences, all <= S.
- Hence 3 delta C_v(lambda) <= 6 delta lambda (sqrt(2S)+1) <= S/100. ∎

**Lemma K0 (elementary local cap).** Every binary source Y of span <= lambda (lambda >= 1) has |Y| <= 1 + 2 sqrt(lambda Q(lambda)) <= 1 + 3.108 lambda^{3/4}.

*Proof.*
- The |Y|-1 consecutive gaps of Y are positive integers summing to <= lambda.
- The gaps equal to g are pairs at lag g, so there are at most r_Y(g) <= 2Q(lambda) of them (Golomb split; both Sidon parts lie in an interval of <= lambda+1 integers).
- H positive integers, each value used at most V times, have sum >= H^2/(2V). (Write H = kV + r, 0 <= r < V. The minimum is V k(k+1)/2 + r(k+1), which exceeds H^2/(2V) by Vk/2 + r - r^2/(2V) >= 0.)
- So (|Y|-1)^2 <= 4 lambda Q(lambda). Finally Q(lambda) <= sqrt(2 lambda) + 1 <= (sqrt 2 + 1) sqrt(lambda), and 2 sqrt(sqrt 2 + 1) < 3.108. ∎

**Proposition N (a counterexample needs three large binary sources).** Let 0 < delta <= 1/6 and S >= 146. Suppose MS' fails at (d, lambda), that is,
C_w(lambda) > (1-delta) 3 C_v(lambda) + S/100. Then **every** class X_e = S_e(d) satisfies

`|X_e| > ((1-3delta) C_v(lambda) + S/100) / (3.108 lambda^{3/4})`, and in particular `|X_e| > S^{5/8}/16`.

Each X_e is a binary source contained in an interval of S+1 integers (heredity, Lemma B1).

*Proof.*
- (Transfer, Lemma 3.1(a) with slack.) Each class has C_{r_e}(lambda) <= C_v(lambda), because r_X(l) <= v_l. Hence C_{r_e} > (3-3delta)C_v + S/100 - 2C_v = (1-3delta)C_v + S/100.
- (Upper count.) C_{r_X}(lambda) = sum_{a in X} (|X ∩ [a, a+lambda]| - 1). Each X ∩ [a, a+lambda] is a binary source of span <= lambda (heredity and translation invariance of L's). So by K0, C_{r_X}(lambda) <= 3.108 |X| lambda^{3/4}. This gives the first bound.
- (Lower count, lambda <= S/2.) For l <= lambda we have S-l-1 >= S/2 - 1 >= 72. So by (Q1) of Sec. 1, v_l >= 2Q(S-l-1) >= sqrt(S-2)/2, and C_v(lambda) >= lambda sqrt(S-2)/2.
  - With 1 - 3delta >= 1/2: |X| > (a lambda^{1/4} + b lambda^{-3/4})/3.108, where a = sqrt(S-2)/4 and b = S/100.
  - By AM-GM on three copies of a lambda^{1/4}/3 and one copy of b lambda^{-3/4}, this is >= 4 * 3^{-3/4} a^{3/4} b^{1/4}/3.108 >= 0.0631 (S-2)^{3/8} S^{1/4}.
  - For S >= 146, (S-2)^{3/8} >= 0.9948 S^{3/8}. So the bound is > 0.0628 S^{5/8} > S^{5/8}/16.
- (lambda > S/2.) C_v(lambda) >= C_v(floor(S/2)) >= (S-1) sqrt(S-2)/4 and lambda^{3/4} <= S^{3/4}. Dropping S/100:
  |X| > (S-1) sqrt(S-2)/(8 * 3.108 S^{3/4}) >= S^{3/4}/26 >= S^{5/8}/16, since S^{1/8} >= 1.625 for S >= 49. ∎

**Corollary N1 (sufficient condition for MS').** Fix delta <= 1/6 and suppose that, for some S >= 146, every binary source contained in S+1 consecutive integers has at most S^{5/8}/16 elements. Then MS' holds at that S, for every d and every lambda. Proof: the contrapositive of N.

**Reading of N.**
- Refuting MS' requires, at arbitrarily large S, three disjoint binary sources (the three classes at one shift) of size > S^{5/8}/16 each.
- At the scale lambda ≈ S they must be of size ≈ S^{3/4}.
- The brief mentions no known construction of binary sources beyond span^{1/2+o(1)}: Sidon sets, the lifted digit families, and the 12-point m=23 instance. So no refutation is within reach of the known constructions.
- Conversely, an upper bound K_true(S) <= S^{5/8}/16 would prove MS', but it would also improve the consumer directly and by far. So N gives no proof route.
- At the regime, S^{5/8}/16 ≈ 2.4e3, far below K ≈ 4.6e5. N is a structural statement, not a regime statement.
- Hedge on the third bullet: I know of no family of binary sources of size >= span^{1/2+epsilon}, and the brief cites none. I have not proved that none exists.

### 3.5b A heuristic from an earlier answer: the multi-lag system inside one class is dense (HEURISTIC)

**Neither direction is reachable with present tools.**
- *Refutation.* By Proposition 2.2, a refutation needs three binary sources at one shift with near-saturated fibers over lags up to more than sqrt(S)/(600 delta). No such binary source is known even in isolation (Section 2.2).
- *Proof.* A proof must be global, because every single-layer statement is saturable:
  - the m = 23 U-structure (entry 54);
  - six disjoint Bose sets (entry 49);
  - the translate obstruction (entry 48);
  - the local satisfiability of Corollary 2.4 (Section 2.3).

**Correction: cross-lag interactions are not rare in the range that matters.** The sketch estimates that a cell lies in about 36 lambda/S lag structures, and concludes that cross-lag collisions number about lambda^3/S. That figure is the density over *all* cells. The relevant quantity is conditional: given a cell already lies in the lag-l structure, how many other lags l' <= lambda also contain it?

Take a forced cell C_l(p,q) = (q+d+l, p), with p, q in the same piece G_x^f(l). It is also a forced cell of lag l' iff:
- p + l' lies in X_x;
- q' = q+l-l' lies in X_x (then q'+l' = q+l is automatically in X_x);
- z_{d+l'}(p) = z_{d+l'}(q').

At class density rho ≈ |X_x|/S ≈ 0.021 (regime), this has probability about rho^2/2 per lag l'. Here rho^2 ≈ 2/sqrt(S).

There are about 3S same-piece forced cells per lag. So the number of forced-forced coincidences over lags up to lambda is about
3S · lambda · lambda rho^2/2 ≈ 3 lambda^2 sqrt(S).
That is about lambda/2 times C_w(lambda) ≈ 6 lambda sqrt(S).

By Corollary 2.5, each coincidence imposes a corner agreement z_{d+l}(p) = z_{d+l'}(p). At lambda ≈ Lambda_0 ≈ 7 sqrt(S) a typical forced cell is shared by about 15 lag structures. So the cross-lag system is dense, not sparse.

Two caveats:
- These coincidences lie **inside one class**. They are consequences of properness of the single binary source X_x (Lemma 2.3). So they bear on the single-class statement SC, which implies MS, and not specifically on the cross-class coupling.
- A coincidence is a consistency condition, not a contradiction. Whether the dense system of corner agreements, together with near-maximality of all Golomb classes at all lags l <= lambda, is unsatisfiable is exactly the open core.

Given this, the director's conclusion ("the deficit must come from a single lag") should be withdrawn. The multi-lag single-class structure is the natural candidate source of a deficit.

### 3.6 A finite datum (checked by script against all 76 L's; evidence only)

A = {0,1,4,13,15,21}, B = {2,5,7,16,22,23} are disjoint Sidon sets in [0,23] whose union carries a proper 2-colouring of its strict source that is constant on A-pairs and constant (the other colour) on B-pairs, with |A|+|B| = 12 = Q(23)+Q(22). So a single lag-structure of the type in 3.4 can be exactly saturated at small span; any deficit must be global.

## TASK PART 4. A suggested route (the director's sketch; you are free to discard it)

- **Contrapositive and saturation.** If |F_d(D)| >= 3(1-eta) sqrt(v_1 S), then T^2 <= 3 sum s_e^2 and Lemma F (Section 3.2) with windows Lam up to epsilon S force each class X_e to have s_e >= (1-O(eta)) sqrt(v_1 S) (each s_e <= K_F), small window variance (Section 3.5, Lemma W1), and fibres r_{X_e}(l) >= (1-O(sqrt eta + epsilon)) v_l for most l <= epsilon S. So each F_l(X_e) is two near-maximal Sidon sets (its Golomb classes) at almost every lag up to a constant fraction of S.
- **Many inscribed pairs.** A pair p < y in X_e with y - p = L then has about rho^2 L ≈ 2L/sqrt(S) inscribed pairs (p,p+t),(y-t,y) (rho = s/S ≈ sqrt(2) S^{-1/4}); typically many.
- **Separation lemma (PROVED; immediate from Lemma 2.3 of Section 3.3).** In a binary source (X, psi), for p < y in X and t, t' in I(p,y), it is impossible that psi(p,p+t) = psi(y-t,y) = 0 and psi(p,p+t') = psi(y-t',y) = 1 (the first forces psi(p,y) != 0, the second psi(p,y) != 1). So at each outer pair all agreeing inscribed pairs have one colour, 1 - psi(p,y). Equivalently, with S_{t,t'} = {p : psi(p,p+t) = 0, psi(p,p+t') = 1} and E_{t,t'} = {y : psi(y-t,y) = 0, psi(y-t',y) = 1}, every p in S_{t,t'} and y in E_{t,t'} satisfy y <= p + max(t,t'), for every ordered lag pair t != t'.
- **Where a contradiction should come from.** Under saturation the Golomb classes Z_0(t), Z_1(t) are near-maximal Sidon sets for every t <= epsilon S, so for random-like psi an outer pair would see agreeing pairs of both colours with probability 1 - O((3/4)^{rho^2 L}). The separation lemma forces, for each lag pair, the pattern-(0,1) ends to lie left of the pattern-(0,1) starts (up to max(t,t')); points of X in the middle third are both starts and ends, and their start rows psi(p, p+.) and end rows psi(. , y) are tied together by the Sidon property of every Z_j(t) and by transport (Corollary 2.4(b)). A counting argument over lag pairs might show that the patterns cannot be so separated for a positive proportion of lag pairs; that would be a single-class deficit |X| <= (1-eta) sqrt(v_1 S), which implies FD at once.
- **Three-class fallback.** The upper-row sets F_l(X_e), e in P, are pairwise disjoint subsets of F_{d+l}(D), each avoids colour e at shift d+l (P1 (iv.1)), and the corners mixing classes (Lemma W(a), Section 3.4) couple their colourings. A joint version of the separation lemma for the coupled structure (W, kappa) is the natural three-class mechanism.
- **Risk.** A single-class deficit improves the binary-source capacity itself and may hold only with tiny eta; FD may also be false, but a counterexample needs three binary sources of size about sqrt(2) S^{3/4} at one shift.

## TASK PART 5. Deliverable

State at the top: FD PROVED (with eta, S_0), FD REFUTED (with the family), or NOT SETTLED. Then the proof or construction in full. If not settled, give the strongest rigorous partial result you obtained, the exact point where the argument stops, and whether you believe FD (or the single-class deficit) is true.
