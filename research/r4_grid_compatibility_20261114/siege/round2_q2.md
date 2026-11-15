kind: attempt

Open question attempted (flagged OPEN by this run): Part (D-c). Do the foreign requests inside a binary-source fiber force an imbalance between its two Golomb classes that lowers r_X(l) below v_l? Settle it either way. Either:
- prove an explicit imbalance statement from the L's that GENERATE the foreign requests; or
- give an explicit proper ternary source, checkable L by L, in which a fiber F_l(X) has two Golomb classes of equal (or nearly equal) size k, for every k, with each class entirely (or in a fixed positive proportion) foreign-requested. That would show no such imbalance can be forced, at least in absolute terms.

## Facts you may use (proved earlier in this run)
- Lemma 0. Every directed L in V(D) is L(u,d,h) for exactly one triple with 1 <= d < h. It has horizontal end (u+d,u), corner (u+h,u), vertical end (u+h,u+h-d), and arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are all in D. Here d ranges over ALL of [1,h-1]. For p0 < p3 with middle pair p1 ≠ p2 and p0+p3 = p1+p2, there are TWO L's with corner (p3,p0): one with arm ends (p1,p0),(p3,p2), and one with arm ends (p2,p0),(p3,p1). A previous construction in this run failed exactly by forgetting the second one, so any construction you give must handle both.
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h). So chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h,e. (ii) R_e(h) ⊆ F_h(D). (iii) Every start lies in at most two R_e(h); if u ∈ R_e ∩ R_{e'} then u ∈ S_{e''}(h).

The following is quoted verbatim from an earlier answer in this run. It is checked; use it freely.
--- begin quote ---
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
--- end quote ---

## Additional facts found at the planning step (proved; short proofs given)
- Collision lemma. Suppose u ∈ F_{h-d}(S_e(d)) ∩ F_{h-d'}(S_e(d')) with d < d'. Then u+(d'-d) ∉ S_e(d) and u+(h-d') ∉ S_e(d).
  Proof: L(u,d,d') has horizontal end (u+d,u) of color e and corner (u+d',u) of color e. So its vertical end (u+d', u+d'-d) is not e. Next, L(u+h-d',d,d') has corner (u+h,u+h-d') of color e and vertical end (u+h,u+h-d) of color e. So its horizontal end (u+h-d'+d, u+h-d') is not e.
- The two same-corner-color Golomb pieces need not have a Sidon union. Here G_e^f = F_l(S_e(d)) ∩ S_f(d+l), for the two classes e ≠ f. Explicit proper witness: D = [0,10), where row u lists chi(v,u) for v = u+1,...,9:
  u=0: 2 0 0 2 2 1 1 2 1; u=1: 2 2 2 1 0 0 1 0; u=2: 1 0 2 1 1 0 2; u=3: 1 0 1 2 0 2; u=4: 1 0 1 0 1; u=5: 2 0 2 0; u=6: 2 1 0; u=7: 0 2; u=8: 2.
  With d = 1, l = 1, f = 0, the starts 0, 2, 3, 5 lie in classes 2, 1, 1, 2 and satisfy 0+5 = 2+3.

## Task
Fix X = S_e(d), lag l, h = d+l, and G' = G_{e'}, G'' = G_{e''} (the Golomb classes of F_l(X) by the color of (u+h,u)). Put A = F_l(X) ∩ R_{e'}(h) ⊆ G'' and B = F_l(X) ∩ R_{e''}(h) ⊆ G'.
1. Write out every L among the cells spanned by the points involved when u ∈ A has a witness d' (u, u+h-d' ∈ S_{e'}(d')), together with a second point of F_l(X), in either Golomb class. Decide whether these L's constrain |G'| in terms of |A|. A target statement would be:
   - (D-c+) if |A| >= alpha Q(L-l), then |G'| <= (1-beta) Q(L-l), with explicit beta(alpha) > 0;
   - or a weaker averaged version over l.
   Here Q(S) is the largest Sidon set of span S.
2. If no such statement holds, build an explicit counterexample family. For every k, give an explicit proper ternary source with a class X, a lag l, and |G'| = |G''| = k, with A = G'' and B = G' (or a fixed positive fraction of each), and give a complete properness proof covering every L. Base-B digit designs are one tool: choose D so that the only additive relations p0+p3 = p1+p2 are the designed ones, and color the free cells to avoid every monochromatic L. With digit designs, Sidon classes are far smaller than sqrt(span). Say whether a relative version, with |G'|, |G''| >= c sqrt(span), can be reached by an algebraic Sidon construction (Singer or Erdos-Turan type) or is out of reach.
3. State exactly which consumer quantity a positive result would lower: v_l, K through the rank-neighbor inequality, or U_d. Also state which named near-extremality hypothesis it needs.

Rules: every claimed counterexample must be explicit and checkable L by L; every proof complete; finite computations are evidence only. Do not import three-color facts. End with the exact statements proved and what stays open.
