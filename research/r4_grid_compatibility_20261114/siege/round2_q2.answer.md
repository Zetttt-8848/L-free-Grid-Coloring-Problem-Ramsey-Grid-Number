# round2_q2 answer: (D-c) imbalance from foreign requests

Notation as in the query: X = S_e(d), lag l, h = d+l, G' = G_{e'}, G'' = G_{e''}
(the classes of F_l(X) by the color of (u+h,u)), A = F_l(X) ∩ R_{e'}(h) ⊆ G'',
B = F_l(X) ∩ R_{e''}(h) ⊆ G'. Every L is L(p0; corner (p3,p0); horizontal end
(p1,p0); vertical end (p3,p2)), with p3-p1 = p2-p0 > 0.

## 1. Single-L coupling lemma (PROVED)

Fix u ∈ A with witness d' < h, d' ≠ d is not needed: u, u+h-d' ∈ S_{e'}(d'). The
witness cells are W1 = (u+d',u) and W2 = (u+h,u+h-d'), both of color e'; the
own cells of u are (u+d,u), (u+h,u+l) (color e) and (u+h,u) (color e'').
Let w ∈ F_l(X), w ≠ u, with Golomb cell C_w = (w+h,w).

**Lemma 1.** An L containing C_w and a witness cell W1 or W2 of u exists only in
the following two shapes, both of which are L(w, d', h):
- w = u-(h-d'): the L has ends (w+d',w), (w+h,w+h-d') = W1 and corner C_w;
- w = u+(h-d'): the L has ends (w+d',w) = W2, (w+h,w+h-d') and corner C_w.

In each case the L is the d'-term request L of w itself, i.e. it constrains C_w only
when w ∈ F_{h-d'}(S_{e'}(d')), and then forces w ∉ S_{e'}(h), i.e. (since w ∈ R_e(h))
w ∈ G''. It never constrains membership in G'.

*Proof.* An L has two cells in its bottom row p0 (corner, horizontal end) and one
cell in row p2 > p0 in the corner's column. We check all role pairs.

(a) W1 = (u+d',u) and C_w = (w+h,w), rows u ≠ w.
- C_w corner, W1 horizontal end: same row needed, u = w; excluded.
- C_w corner, W1 vertical end: column u+d' = w+h, and arm equality: horizontal end
  (p1,w) with p1 = w+h-(u-w)... precisely p3-p1 = u-w, so p1 = w+h-(u-w) = w+d'
  using u = w+h-d'. This is the first listed shape.
- C_w horizontal end, W1 corner: same row, excluded. W1 vertical end: corner
  (u+d',w) with u+d' > w+h, arms u+d'-w-h and u-w; equal iff d' = h; excluded.
- C_w vertical end: corner (w+h,p0), p0 < w. W1 corner: u+d' = w+h and u < w give
  d' > h; excluded. W1 horizontal end: p0 = u, arms (w+h)-(u+d') and w-u, equal iff
  d' = h; excluded.

(b) W2 = (u+h,u+h-d') and C_w, columns u+h ≠ w+h.
- C_w corner: W2 vertical end needs column w+h, excluded; W2 horizontal end needs
  row w = u+h-d', horizontal arm (w+h)-(u+h) = w-u = h-d', so the vertical end is
  (w+h, w+h-d') and the horizontal end (u+h,w) = (w+d',w) = W2. Second shape.
- C_w horizontal end (row w, corner column p3 > w+h): W2 corner needs row w,
  i.e. u+h-d' = w, column u+h = w+d' < w+h; excluded. W2 vertical end: p3 = u+h,
  arms u-w and u+h-d'-w, equal iff d' = h; excluded.
- C_w vertical end (corner (w+h,p0), p0<w): W2 corner needs column w+h; excluded.
  W2 horizontal end: p0 = u+h-d', arms (w+h)-(u+h) = w-u and w-(u+h-d'), equal iff
  d' = h; excluded. ∎

Also (proved in the quoted (iv.2) argument, restated): the L's containing the
own cell (u+h,u) of u ∈ A and C_w are L(min, h, h+|w-u|); when both lie in G''
they force the corner to be e' (via (iv.0)); when w ∈ G' they force nothing. So
no single L joins "u is foreign-requested" with "w ∈ G'".

**Consequence.** Any implication "|A| large ⇒ |G'| small" must pass through
chains of at least two L's sharing a cell that is not one of the listed
determined cells (free cells, each a priori with two admissible colors). The
one-step argument (C4)–(C6) of the earlier answer therefore cannot give D-c+;
this is now a proof, not an impression, for single L's.

## 2. Target D-c+ and counterexample family: OPEN

- D-c+ (|A| >= alpha Q ⇒ |G'| <= (1-beta)Q): not proved, not refuted.
- I did not build an explicit proper ternary source with |G'| = |G''| = k,
  A = G'', B = G' for all k. Lemma 1 indicates the obstruction (if any) is a
  multi-L chain through free cells; a digit design in which D has only the
  designed additive relations would make all such chains absent, so I expect
  (CONJECTURE, unproved) such a family exists in absolute terms, with Sidon
  classes of size only about log-scale in the span. Whether |G'|,|G''| >= c sqrt(span)
  with full foreign requesting can be realized (Singer/Erdos-Turan classes force
  many additive relations among D, hence many additional L's to check) is OPEN;
  I consider it out of reach of this hand analysis.

## 3. Consumer quantity (statement only)

A positive D-c+ would lower the per-fiber caps v_l = Q(L-l)+Q(L-l-1) for fibers
with |A| >= alpha Q; through the rank-neighbor inequality this lowers K(L), and
hence U_d = sum_j K(n-d-j-1). It needs the named near-extremality hypothesis
H_req: "for a positive proportion of lags l in the window, |F_l(X) ∩ R_{e'}(h)|
>= alpha Q(L-l)" (plausible in the regime N_e(h)/|F_h(D)| ≈ 240, unverified).
Any R_4 consequence is only an implication from D-c+ and H_req; no new bound.

## Summary
Proved: Lemma 1 (single-L coupling is only the request L itself) plus B1 of the
earlier answer. Open: D-c+, the averaged version, and an explicit counterexample
family (absolute or sqrt-scale).

=== END OF ANSWER round2_q2 ===
