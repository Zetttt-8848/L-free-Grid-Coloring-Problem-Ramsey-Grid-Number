kind: attempt

# Task: REFUTE the fibre-size deficit FD exactly as stated (or show why it must hold)

Open question attempted: the missing statement FD (OPEN in the run's ledger), whose wording is new this round. Your first job is to try to REFUTE it by an explicit construction, or by deriving from it something known to be false. Earlier material is spliced in below with its proofs. The problem statement itself follows this task.

## TASK PART 1. The statement (FD)

Let Q(m) (m >= 0) be the largest size of a Sidon set (all positive differences distinct; 3-term progressions excluded) inside m+1 consecutive integers, Q(m) = 0 for m < 0. FD asserts: there are explicit constants eta in (0,1) and S_0 >= 1 such that for every proper ternary source (D, chi) — a finite D ⊂ Z with a coloring chi of V(D) = {(v,u) : u < v; u, v in D} by P = {0,1,2} with no monochromatic directed L (x,y),(x+t,y),(x+t,y+t), t > 0, all three cells in V(D) — and every d >= 1 such that F_d(D) = {u : u, u+d in D} is nonempty and S := max F_d(D) - min F_d(D) >= S_0, one has

    |F_d(D)|  <=  3 (1 - eta) sqrt( v_1 S ),   where v_1 = Q(S-1) + Q(S-2).

A refutation is an explicit family of proper ternary sources (D_k, chi_k) and shifts d_k, with complete proofs of properness checkable L by L (Lemma 0 below lists every L of V(D)), spans S_k -> infinity, and |F_{d_k}(D_k)| / (3 sqrt(v_1 S_k)) -> 1 (or exceeding 1 - eta for each fixed eta along the family). Weaker but valuable partial results, to be reported clearly labelled: (a) an explicit family of binary sources (sets X with a proper 2-colouring of V(X)) of size >= c S^{1/2+epsilon} for some epsilon > 0, or of size >= c S^{3/4}; (b) an explicit proper ternary source family with |F_d(D)| >= c S^{3/4}. If you find no counterexample, say precisely what obstruction you met, and if you can, prove FD, or a statement that implies it (for example that every binary source of span S has size <= (1-eta) sqrt(v_1 S), or o(S^{3/4})). Label every claim PROVED, CITED (classical theorem, by name) or HEURISTIC. Nothing about R_4 except as an implication from stated hypotheses.

## TASK PART 2. Why FD matters, and what is already known about a counterexample

- Chain (proved pieces): P1 holds; each class S_e(d) is a binary source of span <= S (cells (v+d,u), u < v in S_e(d), avoid colour e); Corollary F0 below gives the binary-source cap K_F(S) >= sqrt(v_1 S); so FD is the (D-a) inequality sum_e |S_e(d)| <= (1-eta) 3K_F(S) per shift. A refutation of FD would show that no inequality of this per-shift, size-only kind holds (a (D-b)-type result at regime-sized classes).
- Necessary conditions (proved, below): in a counterexample all three classes at the shift have size about sqrt(v_1 S) ≈ sqrt(2) S^{3/4}, with fibres r_{S_e(d)}(l) close to the cap v_l = Q(S-l)+Q(S-l-1) for most lags l up to a constant fraction of S (Lemma F). Each fibre F_l(S_e(d)) is the union of two Sidon sets (the Golomb split), so near-saturation means two near-maximal Sidon sets at almost every lag.
- Excluded constructions (proved, below): block-placed and digit-product sources (D = M·B + R, B Sidon, M > 2rho) have joint prefix ratio at most about Q(rho)/sqrt(M); difference colourings chi(v,u) = phi(v-u) put each F_d(D) into one class; Sidon D gives trivial fibres. Earlier digit families (proper for every parameter choice) have |F_h(D)| = 3 or classes of size span^{1/2-o(1)}, far too small.
- Known binary sources: Sidon sets (size about sqrt S; their strict source contains no L at all). The run knows no binary source of size >= S^{1/2+epsilon}; whether one exists is open, and settling it either way is a strong partial result.

## TASK PART 3. Prior results with proofs (spliced verbatim)

### 3.1 Lemma 0 and Part P1 (from one earlier answer; its headings are kept)

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


### 3.2 Q bounds, Lemma F, Corollary F0, Proposition C, and what a refutation requires (from one earlier answer)

("Cited item 1" there is the per-fibre cap r_X(l) <= v_l, re-proved as Fact 0 in Section 3.3. MS'(delta, S_0) is an earlier, stronger target: for all lambda <= S, sum_{l<=lambda} sum_e r_{S_e(d)}(l) <= (1-delta) sum_{l<=lambda} 3 v_l + S/100.)


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

### 3.3 Necessary conditions for counterexamples, and excluded construction types (from one earlier answer, written against MS'; the brief it cites is the run's earlier query, whose Lemma 3.1 is re-derived inside Theorem N(d))

## 0. Conventions and cited facts
Fix a proper ternary source (D, chi), a shift d, Y = F_d(D), S = span Y, X_e = S_e(d),
w_l = sum_e r_{X_e}(l), C(lambda) = sum_{l<=lambda} 3 v_l, C_v(lambda) = C(lambda)/3.
"Joint prefix ratio" at lambda means sum_{l<=lambda} w_l / C(lambda).

Cited from memory (not proved here):
- (Q+) Lindstrom / Erdos-Turan: Q(m) <= sqrt(m) + m^{1/4} + 1.
- (Q-) Singer/Bose sets plus prime gaps: Q(m) >= (1 - o(1)) sqrt(m).
- (Tab) optimal Golomb ruler lengths 0,1,3,6,11,17,25,34,44,55,72 for 1..11 marks (as in the brief).
Everything else below is proved from the definitions and the proved inputs spliced in the task
(Golomb split (iv.2), heredity B1, Lemma 3.1).

**Fact 0 (fibre cap, re-proved).** r_X(l) <= v_l for each class X = X_e and each l >= 1, and
w_l <= 3 v_l. Proof: F_l(X) is the disjoint union of two Sidon sets (iv.2) inside the interval
[min Y, max Y - l] of S-l+1 integers. At most one of the two contains the right endpoint, so one of
them lies in S-l consecutive integers: sizes <= Q(S-l) and <= Q(S-l-1). Hence LHS of MS' <= C(lambda)
for every lambda. ∎

## 1. Lemma K (an explicit O(L^{3/4}) cap for binary sources; proved)
**Lemma K.** A binary source Y of span L >= 1 has |Y| <= max(1, sqrt(16 L Q(L))).

*Proof.* Let s = |Y| >= 2, Y = {y_1 < ... < y_s}, c = floor(s/2) >= 1. Take the H = c s - c(c+1)/2
pairs (y_i, y_{i+j}), 1 <= j <= c. Their gaps sum to sum_{j<=c} sum_i (y_{i+j} - y_i)
<= sum_{j<=c} j L = L c(c+1)/2 (each inner sum telescopes into j differences of length <= L).
By Fact 0 (applied to Y as a binary source, whose fibres are unions of two Sidon sets) each gap occurs
in at most V := 2Q(L) pairs. The H smallest numbers of a multiset with V copies of each positive
integer sum to at least sum_{t>=0} (H - V t)_+ >= int_0^inf (H - V x)_+ dx = H^2/(2V).
So H^2/(2V) <= L c(c+1)/2. Since c <= s/2, s - (c+1)/2 >= 3s/4 - 1/2 >= s/2, so H >= c s/2, giving
c^2 s^2/4 <= 2 Q(L) L c(c+1), i.e. s^2 <= 8 Q(L) L (c+1)/c <= 16 L Q(L). ∎

With (Q+): |Y| <= 4 L^{3/4} (1+o(1)). (Constant crude; the certified rank-inequality cap is ~1.4 L^{3/4}.)

## 2. Lemma G (near-maximal Sidon sets represent almost every small gap; proved)
**Lemma G.** Let Z ⊂ [0,m] be Sidon, |Z| = k, 2 <= T <= m, and let M_T be the set of g in [1,T-1]
that are NOT differences of Z. Then
    sum_{g in M_T} (T - g) <= T(T-1)/2 - ( T^2 k^2/(m+T) - T k )/2.
If k >= (1-eta) sqrt(m) with 0 <= eta <= 1, the weighted missing fraction
mu_T := sum_{g in M_T}(T-g) / (T(T-1)/2) satisfies
    mu_T <= (T/(T-1)) (2 eta + T/m) + (k-1)/(T-1),
and #(M_T ∩ [1, T/2]) <= mu_T (T-1).

*Proof.* For integers x in [-(T-1), m] put a(x) = |Z ∩ [x, x+T)|. Each z lies in T windows, so
sum a(x) = T k; by Cauchy-Schwarz over the m+T windows, sum a(x)^2 >= T^2k^2/(m+T).
sum a(x)(a(x)-1) counts ordered pairs z != z' with a window containing both, i.e.
sum_{z != z'} (T - |z-z'|)_+ = 2 sum_{g in [1,T-1] \ M_T} (T - g), because (Sidon) each gap is the
difference of at most one pair. Since sum_{g=1}^{T-1}(T-g) = T(T-1)/2, the first display follows.
For the second: k^2/(m+T) >= (1-eta)^2 m/(m+T) >= (1-2eta)(1 - T/m) >= 1 - 2eta - T/m, so the bound is
<= (T^2/2)(2eta + T/m) + T(k-1)/2; divide by T(T-1)/2. Gaps g <= T/2 have weight T-g >= T/2. ∎

So a Sidon set of size (1-eta) sqrt m (eta small) represents all but a fraction
O(eta + T/m + sqrt(m)/T) of the gaps in [1, T/2] whenever sqrt(m) << T << m.

## 3. Theorem N (necessary conditions for a refuting family; proved)
**Theorem N.** Let 0 < eps < 1/3 and suppose a proper ternary source, a shift d with S >= 2 and some
1 <= lambda <= S satisfy
    sum_{l<=lambda} w_l - S/100 >= (1 - eps) C(lambda).                  (*)
Then:
(a) lambda >= S / (600 eps Q(S-1)); with (Q+) this is >= (1-o(1)) sqrt(S)/(600 eps).
(b) For each e: sum_{l<=lambda} r_{X_e}(l) >= (1 - 3eps) C_v(lambda) + S/100.
(c) For each e: |X_e| (|X_e| - 1)/2 >= (1-3eps) S/(300 eps) + S/100; in particular
    |X_e| >= sqrt( (1-3eps)/(150 eps) ) sqrt(S).
(d) For each of the six pieces G_e^f(l), with the two pieces of F_l(X_e):
    sum_{l<=lambda} ( Q(S-l) - |G_e^f(l)| ) <= 3 eps C_v(lambda) + lambda.

*Proof.* (a) By Fact 0, sum w_l <= C(lambda), so (*) gives eps C(lambda) >= S/100. Also
C(lambda) <= 3 lambda max_l v_l <= 6 lambda Q(S-1). (b) Each class has prefix <= C_v(lambda) (Fact 0);
subtract the two others from (*): >= 3(1-eps)C_v + S/100 - 2C_v. (c) The left side of (b) is at most
the number of pairs of X_e, and C_v(lambda) = C(lambda)/3 >= S/(300 eps) by the proof of (a).
(d) This is Lemma 3.1(b) of the brief, re-derived: |G_e^{f'}(l)| <= Q(S-l), so
sum_l |G_e^f(l)| >= (b) - sum_l Q(S-l) >= (1-3eps)C_v - sum_l Q(S-l); and
sum_l Q(S-l) <= (C_v + lambda)/2 because Q(m-1) >= Q(m) - 1; hence
sum_l (Q(S-l) - |G_e^f(l)|) <= 2 sum_l Q(S-l) - (1-3eps) C_v <= 3eps C_v + lambda. ∎

**Reading.** A family with eps_k -> 0 (the form required by the task) therefore needs:
- lambda_k / sqrt(S_k) -> infinity (in fact >= sqrt(S_k)/(600 eps_k)); the violation is a
  long-prefix phenomenon, never a small-lag one;
- every class X_e to be a binary source of size >> sqrt(S_k) (far beyond any Sidon set) whose
  fibres F_l(X_e), l <= lambda, are on average unions of two near-maximal Sidon sets;
- by (d), Markov, and Lemma G (with m = S-l and T in [omega sqrt S, S/omega]): for all lags l <= lambda
  outside a set of Q-weight O((eps + lambda/C_v)/eta) * sum Q, all six pieces G_e^f(l) represent all
  but a fraction O(eta + 1/omega) of the gaps g in [1, T/2]. Each such gap-g pair in G_e^f(l) forces,
  by Lemma F, a point of G_e^{f'}(l+g) (f' the third colour): about lambda forced incidences land in
  each Sidon set G_e^{f'}(H), which has size <= Q(S): so each forced point is hit about
  lambda/sqrt(S) -> infinity times on average. This is a consistency requirement, not a contradiction
  (it is the request picture; one start can absorb many requests).

**Problem SAT (open core of any refutation).** Does there exist a family of binary sources X_k with
span S_k -> infinity and lambda_k with lambda_k/sqrt(S_k) -> infinity such that
sum_{l<=lambda_k} r_{X_k}(l) >= (1 - o(1)) C_v(lambda_k)? By Theorem N(b), a "yes" is NECESSARY for
refuting MS' (each class must be such an X). It is not known to be sufficient: one still needs three
such classes at a common shift inside a full proper ternary source. A uniform "no" of the form
"every binary source X of span S >= S_0 (inside a ternary source, as a class S_e(d)) satisfies
sum_{l<=lambda} r_X(l) <= (1-delta) C_v(lambda) + S/300 for all lambda" implies MS' by summing over
the three classes (this is SC with slack).
(In SAT, C_v is taken with respect to an ambient span S_k >= span X_k; taking S_k = span X_k is the
strongest form.)

## 4. Proposition P (block-placed and digit-product sources cannot refute MS'; proved)
**Setting.** Integers rho >= 1 and M > 2 rho; a Sidon set B ⊂ Z (all positive differences b'-b of
pairs distinct, so also no 3-AP). Fix a proper ternary source and a shift d such that
    Y = F_d(D) ⊂ union_{b in B} I_b,   I_b = [M b, M b + rho].
Let B' = {b : Y ∩ I_b nonempty}, beta = |B'| >= 2, g = max B' - min B'. Then g >= beta(beta-1)/2
(the beta(beta-1)/2 positive differences of B' are distinct and <= g) and S = span Y >= M g - rho > rho.
Put
    theta = beta Q(rho) / Q(S - rho - 1),
    kappa = max{ 8 Q(rho)/Q(floor(S/2) - 1) ,  4 beta^2 rho Q(rho) / ( floor(S/2) Q(floor(S/2) - 1) ) }
(assume S >= 4 so floor(S/2) - 1 >= 1).

**Proposition P.** For every 1 <= lambda <= S:  sum_{l<=lambda} w_l <= (theta + kappa) C(lambda).

*Proof.* Step 1 (lag decoding). Let u in I_b, u' = u + l in I_{b'}, l >= 1. Then
l = M(b'-b) + (y'-y) with y, y' in [0,rho]. If b' < b then l <= -M + rho < 0, impossible. If b' = b
then l <= rho. If b' > b then l >= M - rho > rho, and k := b'-b is the unique integer with
|l - kM| <= rho (unique because M > 2 rho). Because B is Sidon, for each k >= 1 there is at most one
pair (b, b+k) in B' x B'.

Step 2 (within-block lags l <= rho). Here every pair u, u+l of X_e lies in one block. For each block
b, F_l(X_e) ∩ I_b is contained in F_l(X_e), so it is the union of two Sidon sets (subsets of the two
Golomb pieces, (iv.2)), and it lies in [Mb, Mb + rho - l]: so |F_l(X_e) ∩ I_b| <= 2 Q(rho - l)
<= 2Q(rho). Summing over the beta blocks and the three classes: w_l <= 6 beta Q(rho). On the other
hand v_l = Q(S-l) + Q(S-l-1) >= 2 Q(S-l-1) >= 2 Q(S - rho - 1) for l <= rho (Q nondecreasing). So
w_l <= theta * 3 v_l for l <= rho.

Step 3 (cross lags l > rho). By Step 1 such a lag uses a unique block pair (b, b+k) with |l-kM| <= rho.
Hence, for each k >= 1,
    sum_{l : |l - kM| <= rho} w_l <= sum_e |X_e ∩ I_b| |X_e ∩ I_{b+k}| <= 3 K_*^2,
where X_e ∩ I_b is a binary source of span <= rho (heredity B1), so by Lemma K
|X_e ∩ I_b| <= K_* with K_*^2 <= 16 rho Q(rho) (rho >= 1 makes the max in Lemma K equal to this).
Let Cross(lambda) be the part of sum_{l<=lambda} w_l from lags l > rho, and Within(lambda) the rest.

Step 4 (bounds). Within(lambda) <= theta sum_{l<=min(lambda,rho)} 3v_l <= theta C(lambda).
If Cross(lambda) > 0 then lambda >= M - rho > rho, the relevant k satisfy kM - rho <= lambda, so their
number is <= (lambda + rho)/M < 2 lambda/M.
 - Case lambda <= S/2: C(lambda) >= 3 lambda v_lambda >= 6 lambda Q(S - lambda - 1)
   >= 6 lambda Q(floor(S/2) - 1) (v nonincreasing). So
   Cross/C <= (2lambda/M) 3 K_*^2 / (6 lambda Q(floor(S/2)-1)) <= 16 rho Q(rho)/(M Q(floor(S/2)-1))
   < 8 Q(rho)/Q(floor(S/2)-1), using rho/M < 1/2.
 - Case lambda > S/2: Cross(lambda) <= (number of block pairs) 3K_*^2 <= (beta^2/2) 48 rho Q(rho), and
   C(lambda) >= C(floor(S/2)) >= 6 floor(S/2) Q(ceil(S/2) - 1) >= 6 floor(S/2) Q(floor(S/2)-1).
   So Cross/C <= 4 beta^2 rho Q(rho)/(floor(S/2) Q(floor(S/2)-1)).
In both cases Cross(lambda) <= kappa C(lambda). Add Within. ∎

**Asymptotics (uses (Q+), (Q-)).** Since B' is Sidon in an interval of g+1 integers, beta <= Q(g); and
S >= Mg - rho >= rho(2g - 1). As g -> infinity:
- theta <= Q(g) Q(rho)/Q(Mg - 2rho - 1) = (1+o(1)) Q(rho)/sqrt(M);
- kappa -> 0: the first term is O(sqrt(rho/S)) = O(g^{-1/2}); the second is
  O(beta^2 rho^{3/2}/S^{3/2}) = O(g rho^{3/2} /(M g)^{3/2}) = O(g^{-1/2}).
So the joint prefix ratio of a block-placed source is at most (1+o(1)) Q(rho)/sqrt(M) + O(g^{-1/2}),
uniformly in lambda. With M >= 2rho + 1:
- if rho -> infinity as well, this is <= 1/sqrt(2) + o(1);
- for fixed rho it is < 1 strictly whenever Q(rho)^2 < 2 rho + 1; by (Tab) this holds for
  18 <= rho <= 72, and by (Q+) for rho >= 103 (since then sqrt(rho)+rho^{1/4}+1 < sqrt(2 rho + 1)).
  (It fails for some small rho, e.g. rho = 17: Q = 6, 36 > 35; those cases are not covered.)

**Consequences.**
1. Digit-product sources D = M B + R with R ⊂ [0, rho], M > 2 rho, B Sidon: for every shift d <= rho,
   F_d(D) ⊂ M B + [0, rho] is block-placed with beta = number of blocks met; Proposition P applies and
   gives ratio <= theta + kappa (< 1 by a margin in the regimes listed). For d > rho with
   |d - kM| <= rho, k >= 1, Step 1 shows F_d(D) lies in a single block I_b (unique pair (b,b+k)):
   that instance has span <= rho, i.e. it is an instance at the inner scale, not at the top scale.
   So lifting/digit-product constructions never produce a violation at a scale larger than the
   inner blocks: any violation they contain is already a violation of span <= rho. This proves a
   version of the unfinished brief claim (bound (1+o(1)) Q(rho)/sqrt M instead of (1+o(1))/sqrt M,
   for all lambda, not only lambda = 1).
2. More precisely, Step 2 gives a multiplicative transfer: if each block's own profile satisfies
   w^{(b)}_l <= alpha 3 v^{(rho)}_l with v^{(rho)}_l = Q(rho-l)+Q(rho-l-1), then the top-level ratio is
   <= alpha theta + kappa (Step 2 with 2Q(rho-l) replaced by alpha v^{(rho)}_l <= 2 alpha Q(rho)).
   This is a per-lag hypothesis; for the prefix form only the weaker statement "ratio <= theta + kappa"
   is proved. Products shrink the ratio by about sqrt(rho/M); they cannot amplify it.

## 5. Two further exclusions of candidate types (proved)
**5.1 Difference colorings.** If chi(v,u) = phi(v-u) for some phi (e.g. quadratic-residue type
colorings of differences, or any coloring constant on each diagonal offset), then for every d one
class S_{phi(d)}(d) = F_d(D) and the other two are empty. So w_l = r_{F_d(D)}(l) and, F_d(D) being a
single class, Fact 0 gives w_l <= v_l: the joint prefix ratio is <= 1/3 for every lambda.
More generally, by Theorem N(c) a refuting instance needs, at the shift d, all three colours on the
offset-d cells (u+d,u), u in Y, each on >= c(eps) sqrt(S) cells with c(eps) -> infinity. Any coloring
rule in which the offset-d cells of most of Y carry one or two colours is excluded:
if |X_e| < sqrt(2(1-3eps)S/(300eps)) for some e, (*) fails.

**5.2 Sidon-type sources.** If D is Sidon then V(D) contains no L at all (an L needs a, a+delta, c,
c+delta in D with a < c, a repeated difference or a 3-AP when a+delta = c), but then |F_d(D)| <= 1 for
every d >= 1 and the instance is trivial (S = 0). So all the mass of a counterexample must come from
the additive energy of D; by Theorem N(c), D needs |F_d(D)| >= 3 c(eps) sqrt(S).

## 6. Where the attempts stopped (precise obstruction)
- All proved inputs available here (Golomb split, Lemma F, AABA/ABAA forcing, no-collision, gap
  coverage, equidistribution, binary cap) are single-lag or single-pair-of-lags statements, and each
  is consistent with saturation at a single lag (director's m = 23 instance; six disjoint Bose
  translates; translate obstruction O). Theorem N shows a refutation is a statement about
  lambda >> sqrt(S) lags simultaneously, so none of the single-lag constructions transfers.
- Every explicit construction type I could analyse rigorously (block/digit product, difference
  colorings, Sidon-type) has joint prefix ratio bounded away from 1 (Prop. P, 5.1, 5.2).
- A sumset-type class X ⊇ C + T (C a near-maximal Sidon set with all small gaps, T a short set with
  r_T(l) = 2 for l <= lambda) would give r_X(l) ~ 2|C| ~ v_l at those lags. HEURISTIC ONLY: the cross
  terms sum_j r_T(j) 1[l - j in C - C] are about |T|^2/2 >= 2 lambda >> sqrt(S) = v_l/2 per lag
  (Lemma G: C - C contains almost every small gap), contradicting Fact 0; so this type cannot be a
  binary source when lambda >> sqrt(S), and the only way out (C - C avoiding small gaps) is the block
  type of Prop. P. I did not write this as a theorem (representation multiplicities in C + T make
  the lower bound on r_X(l) need care).

## TASK PART 4. Deliverable

State at the top: FD REFUTED (with the family and its properness proof), FD PROVED (with eta, S_0), or NOT SETTLED. Then the construction or proof in full; then any labelled partial results of the kinds listed in Task Part 1.
