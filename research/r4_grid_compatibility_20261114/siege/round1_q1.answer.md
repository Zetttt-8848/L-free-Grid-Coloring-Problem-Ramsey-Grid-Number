# round1_q1 answer: P1 (i)-(v) proofs, and the forced-color alternative (D-c)

Throughout, `(D, chi)` is a ternary source: `V(D) = {(v,u) : u<v, u,v in D}`, `chi : V(D) -> P = {0,1,2}`. A directed L is `(x,y),(x+t,y),(x+t,y+t)`, `t>0`. The **corner** is `(x+t,y)`. The **horizontal arm end** is `(x,y)` (same row as the corner). The **vertical arm end** is `(x+t,y+t)` (same column as the corner). For `{e,e',e''} = P` the letters always denote three distinct colors.

## PART A

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

## PART B (D-c)

**B1 (proved; immediate).** `A ⊆ G_{e''}` and `B ⊆ G_{e'}`, so `A` and `B` are Sidon sets. If `span` denotes the span of `F_l(X)`, then `|A|, |B| <= Q(span)`, and `|A| + |B| <= |F_l(X)|` because `A ∩ B = ∅`. This follows immediately from (iv.3) and (iv.2), since subsets of Sidon sets are Sidon. It gives nothing beyond the existing cap `r_X(l) = |G_{e'}| + |G_{e''}| <= 2Q`-type bounds.

**B2 (imbalance): not proved; OPEN.** I could not derive any statement of the form "if `|A| >= alpha·Q` then `r_X(l) <= (1-delta)v_l`".

Why the constraints listed in (i)–(iv) cannot give this by themselves: here is an abstract model that satisfies every constraint (ii)–(iv) places on one fiber. Take
- any partition `F_l(X) = G' ⊔ G''` into two Sidon sets, each of maximum size `Q`;
- any `A ⊆ G''` and `B ⊆ G'`, for example `A = G''` and `B = G'`, so that a full proportion of the fiber is foreign-requested.

The constraints (ii)–(iv) on this fiber are exactly:
- (C1) `A ⊆ G''` and `B ⊆ G'`;
- (C2) `A ∩ B = ∅`;
- (C3) `G'` and `G''` are Sidon.

All three hold, and `r_X(l)` attains `2Q`. So imbalance cannot follow from (i)–(iv) as stated. As the task note says, containing a large prescribed Sidon subset does not shrink a Sidon set.

The model ignores the genuine L-constraints that **generate** `A`. Each `u in A` has a witness `d' < h` with `u, u+h-d' in S_{e'}(d')`. So, beyond (C1)–(C3), the following hold for each such `u`:
- (C4) `chi(u+d',u) = chi(u+h,u+h-d') = e'` and `chi(u+h,u) = e''`;
- (C5) the binary-source/Golomb structure of the foreign class `S_{e'}(d')` at lag `h-d'`, which contains `u` in its own Golomb class of color `e''` (by (iv.3) applied to `S_{e'}(d')`);
- (C6) the L's `L(u, h, h+s)` mixing the fiber `G''` with cells of the foreign source.

The unresolved question is whether (C4)–(C6), applied simultaneously for all `d'`, constrain `|G'|`. I found no joint configuration of L's that bounds `|G'| + |G''|` in terms of `|A|`. The four-L argument of (iv.2) only uses same-color cells. Foreign requests contribute cells of color `e'` at positions `(u+d',u)`, which lie on rows `u` but off the offsets `h + r` that the Golomb L's use. So I see no direct interaction.

I did not construct an explicit ternary source realizing the model. That would need many classes and a full properness check, which I could not do reliably by hand. The existence of a genuine counterexample is therefore also OPEN.

**B3. Consumer quantity.** A positive imbalance result `r_X(l) <= (1-delta)v_l` would lower the per-fiber caps `v_l`. Through the rank inequality it would lower `K`, and so `U_d`.

*Heuristic, not proved:* if the rank inequality's output scales roughly linearly in the fiber caps, `K` and `U_d` drop by about a factor `(1-delta)`. By the stated sensitivity this moves the excluded side by a factor of about `1 - 3.9 delta`; e.g. `delta ≈ 0.0115` gives about 21.0M. In the regime, `N_e(h)/|F_h(D)| ≈ 240`, so foreign requests are dense. The hypothesis "`|A| >= alpha Q` for a positive proportion of fibers" is therefore plausible, but it is unverified and is the near-extremality hypothesis that must be named.

## Exact statements proved
1. Lemma 0: the L's in `V(D)` correspond bijectively to triples `(u,d,h)` with `1<=d<h` and `u,u+d,u+h-d,u+h in D`, with corner `(u+h,u)`, arm ends `(u+d,u)` and `(u+h,u+h-d)`, arm length `h-d`. Coincident points are harmless.
2. (i) `chi` is proper iff `S_e(h) ∩ R_e(h) = ∅` for all `h>=2` and all `e`.
3. (ii) `R_e(h) ⊆ F_h(D)`.
4. (iii) `k(u) <= 2`; `k(u) = 2` with requests `{e,e'}` forces `u in S_{e''}(h)`; the inequality as posed holds; the sharp identity is `sum|R_e| = 2|F_h| - 2#{k=0} - #{k=1}`.
5. (iv) The shifted source of `S_e(d)` avoids `e`. `F_l(X) ⊆ R_e(h)`. `G_{e'}` and `G_{e''}` are Sidon (B2 sense, with 3-APs excluded) via L1–L4. `A ⊆ G_{e''}`, `B ⊆ G_{e'}`, and `A ∩ B = ∅`.
6. B1: `|A|, |B| <= Q(span)`.

**Open:** (D-c) imbalance under foreign-request density; an explicit realization of the abstract model as a proper ternary source; (D-a) and (D-b), which were not attempted in this round.

=== END OF ANSWER round1_q1 ===
