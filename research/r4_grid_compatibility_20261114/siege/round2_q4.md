kind: attempt

Open question attempted (flagged OPEN by this run): a JOINT fiber bound for the three completion classes at one shift. Fix d and a lag l. Is there an explicit delta > 0 with

  sum_{e in P} r_{S_e(d)}(l) <= (1-delta) * 3 v_l

(here v_l is the single-class fiber cap; in the near-cap regime v_l ≈ 2 sqrt(L)), under a stated hypothesis or unconditionally? More generally: is there any L-forced constraint coupling the six Golomb pieces of the three fibers that lowers their joint size, which the rank-neighbor inequality summed over the three classes could consume? Settle it either way: prove such a coupling with explicit constants, or show by explicit proper ternary sources (checkable L by L) that the six pieces can be jointly as large as separately.

## Facts you may use (proved earlier in this run)
- Lemma 0. Every directed L in V(D) is L(u,d,h) for exactly one triple with 1 <= d < h. Its horizontal end is (u+d,u), its corner (u+h,u), its vertical end (u+h,u+h-d), and its arm length h-d. It lies in V(D) iff u, u+d, u+h-d, u+h are in D, with d over all of [1,h-1]. For p0 < p3 with p0+p3 = p1+p2 and p1 ≠ p2 there are TWO L's with corner (p3,p0); constructions must handle both.
- (i) L(u,d,h) is monochromatic of color e iff u ∈ F_{h-d}(S_e(d)) ∩ S_e(h); chi is proper iff S_e(h) ∩ R_e(h) = ∅ for all h,e.
- The single-class Golomb split, quoted verbatim from an earlier answer in this run (checked):
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

--- end quote ---

## The six pieces, and what is already known about them
Fix d, l, h = d+l. For e ≠ f put G_e^f = F_l(S_e(d)) ∩ S_f(h) = {u : u, u+l ∈ S_e(d), chi(u+h,u) = f}.
- The six pieces are pairwise disjoint subsets of F_h(D). Their total is sum_e r_{S_e(d)}(l), which is the lag-l agreement count of the 3-colored word z_d(u) = chi(u+d,u) on F_d(D).
- Each piece is Sidon (quote above).
- The two pieces with the same corner color f, coming from the two classes e ≠ f, both lie in S_f(h). Their UNION need NOT be Sidon. Explicit proper witness: D = [0,10), where row u lists chi(v,u) for v = u+1,...,9:
  u=0: 2 0 0 2 2 1 1 2 1; u=1: 2 2 2 1 0 0 1 0; u=2: 1 0 2 1 1 0 2; u=3: 1 0 1 2 0 2; u=4: 1 0 1 0 1; u=5: 2 0 2 0; u=6: 2 1 0; u=7: 0 2; u=8: 2.
  With d = 1, l = 1, f = 0, the starts 0, 2, 3, 5 lie in classes 2, 1, 1, 2 and satisfy 0+5 = 2+3.
- Evidence only (random proper sources on [0,n), n <= 16). Consider additive quadruples a, a+r, a+s, a+r+s (0 < r <= s) inside G_e^f ∪ G_{e'}^f, labelled by class, with A = the class of a. The observed patterns were ABBA 22, AAAB 18, ABBB 13, AABB 4, ABAB 1. No AABA or ABAA occurred; AAAA is impossible.
  Partial forcing seen at the planning step, for the pattern AABB (a, a+r in class e; a+s, a+r+s in class e'; corner color f):
  - L(a,h,h+r) gives chi(a+h+r,a) ≠ f, and since a, a+r+l ∈ S_e(d) it is ≠ e. So it equals e'.
  - Likewise chi(a+s+h+r, a+s) = e.
  - These differ, so the single-class closing step (L3 in the quote) does not apply.
- Consumption. The rank-neighbor inequality (quoted below) holds for each class separately. Summing it over the three classes S_e(d), each a binary source of span <= L', gives
  2 sum_e P_e + (terms in e_j) <= 3 L' c(c+1),
  and the sum of the three sets of selected differences is at least the cheapest 3H terms of the multiset in which lag l has JOINT multiplicity w_l >= sum_e r_{S_e(d)}(l). So a joint bound w_l <= (1-delta) 3 v_l on enough lags lowers the joint cap on sum_e |S_e(d)|, hence U_d. Check this deduction and make it exact, including the case of unequal class sizes.
--- quoted: the rank-neighbor inequality, from the certifying project record ---
Consider a hereditary family of finite sets of integers. Let $b_1<\dots<b_s$ be a member of span $L$. Suppose a member with $j$ marks must have span at least $e_j$, for the smaller ranks used below. Choose $1\le c<s$ and take all differences of rank at most $c$, numbering $H=cs-c(c+1)/2$ of them. If the multiplicity of positive difference $h$ is bounded by $v_h$, let $P(H;v)$ be the sum of the cheapest $H$ terms in the multiset containing $v_h$ copies of $h$. Then
$$
 2P(H;v)+4\sum_{i=0}^{c-1}(c-i)e_{i+1}\ \le\ Lc(c+1).
$$
Indeed the sum of the selected differences telescopes to $\sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1})$. The first and last $i+1$ marks each have span at least $e_{i+1}$, so their endpoint difference in this expression is at most $L-2e_{i+1}$. This remains true when the blocks overlap. The sum is at least $P$ by construction. The archive used $e_{i+1}=i$. Here the endpoint blocks belong to the same family as the original set, allowing an induction on cardinality. [Earlier rank-neighbor inequality](../../exploration/research_round3/four/R3_R4_REPORT.md)
--- end quote ---

## Task
1. Classify the mixed additive quadruples. For a quadruple a, a+r, a+s, a+r+s (r, s > 0, r = s allowed) inside the union of the six pieces, consider every assignment of pieces (class e and corner color f for each point). Decide which assignments are FORBIDDEN by L's, and give the explicit L's. Use the L's of the single-class proof, L's through cells on offsets d, h, h+r, h+s, h+r+s, and L's with arm length l or d. Prove each forbidden pattern; for patterns you believe allowed, give an explicit proper witness or say they are open.
2. From the forbidden patterns, derive the strongest joint bound you can on |G_e^f| + |G_{e'}^f|, or on the sum of all six, in terms of the span S = L - h. Caution on classical tools: if two Sidon sets A, B ⊆ [0,S] merely have disjoint positive-difference sets, plain counting gives only C(|A|,2) + C(|B|,2) <= S, i.e. |A| + |B| <~ 2 sqrt(S). That is NO saving over 2Q ≈ 2 sqrt(S), because a single maximal Sidon set uses only about half of the differences in [1,S]. A saving needs either a finer (Erdos-Turan / interval-counting) argument applied to the pair, or a stronger forbidden structure, e.g. A ∪ B having few additive quadruples. State exactly what you use and prove it. Find out which forbidden patterns suffice for a saving of this kind, and give the explicit delta.
3. If no pattern beyond the single-class ones is forbidden, prove it by explicit proper sources realizing each mixed pattern. Then show that the joint bound fails, or state precisely what extra hypothesis would rescue it.
4. If you get a joint bound, carry it through the summed rank inequality to an explicit statement of the form sum_e |S_e(d)| <= (1-delta')(sum of the three single-class caps), and say which consumer quantity it lowers. The R4 consumer uses U_d = sum over the twelve classes at shift d of K; the twelve are four main colors times three completion colors.

Rules: every proof complete; every counterexample explicit and checkable L by L; finite computations are evidence only; do not import three-color facts. End with the exact statements proved and what stays open.
