# round3_q2: an explicit family refuting (D-c+) for arbitrary ternary sources

Colors: e = 0, e' = 1, e'' = 2. Everything below is proved from the cell coordinates. No computation was run.

## 1. Construction

Fix k >= 1 and B = 100. Index the blocks by i = 1..2k.
- d'_i = B^i, d = B^{2k+1}, l = B^{2k+2}, h = d + l, u_i = B^{2k+2+i}.
- U = {u_i}, U'' = {u_1..u_k}, U' = {u_{k+1}..u_{2k}}.
- For each block i, put w_i = h - d'_i and Delta_i = {0, d'_i, d, l, w_i, h}. Note 0 < d'_i < d < l < w_i < h.
- Let D = union over i of (u_i + Delta_i). This set is disjoint, and blocks are ordered by i, because the gaps between consecutive u_i are far larger than h.
- For each block, let c_i = 2 if u_i is in U'' and c_i = 1 if u_i is in U'. Put c̄_i = 3 - c_i, the other nonzero color.

**Same-block cells.** Write [a,b]_i for the cell (u_i+a, u_i+b).

| cell | color |
|---|---|
| [d,0], [h,l] | 0 (the X-completions) |
| [h,0] | c_i (the Golomb cell) |
| [d'_i,0], [h,w_i] | c̄_i (the witness cells) |
| [l,0], [w_i,0], [w_i,d'_i] | 0 |
| [d,d'_i], [l,d'_i] | 1 |
| every other same-block cell | 0 |

**Cross cells.** For i < j, write (u_j+α, u_i+β). If α or β is not in Delta0 = {0,d,l,h}, the color is 0. Otherwise the color is kappa_{ij}(α,β), defined as follows:
- kappa(0,·) = 0;
- kappa(d,·) = 1;
- kappa(l,·) = 2;
- kappa(h,d) = 1, kappa(h,l) = 2, kappa(h,h) = 0;
- kappa(h,0) = s_{ij}, where s_{ij} = c̄ if c_i = c_j = c, and s_{ij} = 1 if c_i ≠ c_j.

## 2. Additive structure (Lemma A)

Every L comes from four points p0 < p3 and an ordered middle pair (x,y), all in D, with x + y = p0 + p3 and p0 < x, y < p3.

Each point is a single u-digit plus an offset whose digits have coefficients in {-1,0,1}. In p0 + p3 - x - y, every power of B therefore has a coefficient of absolute value at most 4, which is less than B/2. Take the least power whose coefficient is nonzero. Reducing modulo the next power of B gives a contradiction. So every digit coefficient is 0.

**The u-digits.** They give {u(p0), u(p3)} = {u(x), u(y)}.

**Same block i.** In the basis (d, l, d'_i) the offsets are
- 0 = (0,0,0), d'_i = (0,0,1), d = (1,0,0), l = (0,1,0), w_i = (1,1,-1), h = (1,1,0).

Go through all 21 pair sums, including the six doubles. The only coincidence is (1,1,0) = 0+h = d+l = d'_i+w_i. Using the order of the offsets, the same-block L's are exactly these six:
- L_a: [d,0], corner [h,0], [h,l]. Colors 0, c_i, 0.
- L_b: [l,0], corner [h,0], [h,d]. Colors 0, c_i, 0.
- L_c: [d'_i,0], corner [h,0], [h,w_i]. Colors c̄_i, c_i, c̄_i.
- L_d: [w_i,0], corner [h,0], [h,d'_i]. Colors 0, c_i, 0.
- L_e: outer pair (d'_i, w_i). Cells [d,d'_i], corner [w_i,d'_i], [w_i,l]. Colors 1, 0, 0.
- L_f: outer pair (d'_i, w_i). Cells [l,d'_i], corner [w_i,d'_i], [w_i,d]. Colors 1, 0, 0.

None of the six is monochromatic, since c_i ≠ 0, c̄_i ≠ c_i and 1 ≠ 0.

**Cross blocks.** Take p0 in block i and p3 in block j with i < j. Block order forces one middle point u_i+δy with δy > δ0, and the other u_j+δz with δz < δ3. The digits d'_i and d'_j are distinct, so each cancels on its own. Hence δ0 and δy have equal d'_i-coefficient. Since they are distinct, both lie in Delta0, and likewise δz and δ3 lie in Delta0. Also δy - δ0 = δ3 - δz =: g > 0.

There are two kinds of cross L:
- **Order 1:** H = (u_i+δy, u_i+δ0) [same block], corner (u_j+δ3, u_i+δ0), V = (u_j+δ3, u_j+δz) [same block].
- **Order 2:** H = (u_j+δz, u_i+δ0), corner (u_j+δ3, u_i+δ0), V = (u_j+δ3, u_i+δy). All three cells are cross cells.

There are no other L's. ∎

## 3. Theorem B: the source is proper

The same-block L's were checked above. It remains to check the cross L's.

**Order 1.** On Delta0 the only nonzero same-block cell is [h,0], and it occurs only when g = h.
- If g ≠ h, then H = V = 0. The corner is (δ3, δ0) with δ3 in {d,l,h} and δ0 in {0,d,l}. Every kappa value there is nonzero (1, 2, s, 1, 2). So the L is not monochromatic.
- If g = h, then H = c_i, V = c_j and the corner is s_{ij}. If c_i = c_j = c, then s_{ij} = c̄ ≠ c. Otherwise H ≠ V.

**Order 2.**
- If δz = 0, then H = 0. The corner (δ3, δ0) has δ3 > 0 and δ0 ≠ h, so it is nonzero.
- Otherwise (δz, δ3) is one of (d,l), (d,h), (l,h). Check each:
  - (d,l), g = l-d, so (δ0, δy) = (d,l): H = 1, corner = 2.
  - (d,h), g = l, (δ0, δy) = (0,l): H = 1, corner = s, V = kappa(h,l) = 2. Since s = 1 forces V ≠ 1, the L is not monochromatic.
  - (d,h), g = l, (δ0, δy) = (d,h): H = 1, corner = 1, V = kappa(h,h) = 0.
  - (l,h), g = d, (δ0, δy) = (0,d): H = 2, corner = s, V = kappa(h,d) = 1. Since s = 2 forces V ≠ 2, the L is not monochromatic.
  - (l,h), g = d, (δ0, δy) = (l,h): H = 2, corner = 2, V = 0.

All L's are non-monochromatic, so chi is proper. ∎

## 4. The required fiber

**The class X.** In D, the points x with x+d in D are exactly the points with offsets 0 and l in a block. Offset pairs that differ by d are (0,d) and (l,h). A cross-block difference d is impossible.
- Both completion cells [d,0] and [h,l] have color 0.
- So X = S_0(d) = {u_i, u_i+l}, and F_l(X) = U, with |U| = 2k.

**The Golomb classes.** The Golomb cell of u_i is [h,0] = c_i. Hence G'' = G_2 = U'' and G' = G_1 = U', with k points each. Both are Sidon, because they are sets of distinct powers of B. This agrees with (iv.2).

**The foreign requests.**
- Take u in U''. The cells [d'_i,0] and [h,w_i] both have color 1 = e', and u_i + d'_i, u_i + w_i, u_i + h all lie in D. So u_i is in S_1(d'_i), and u_i + h - d'_i is in S_1(d'_i). Hence u_i is in R_1(h). So A = G''.
- Symmetrically, for u in U' the witness color is 2, so B = G'.

## 5. Consequences for (D-c)

**REFUTED: (D-c+) for arbitrary ternary sources.** The family has, for every k:
- |G'| = |G''| = k;
- A = G'' and B = G' (every fiber point is foreign-requested);
- a proper coloring, proved L by L in Sections 2 and 3, with both middle orders covered.

So no implication "|A| >= alpha|G''| implies |G'| <= (1-beta)|G''|" holds, for any alpha <= 1 and beta > 0. Being foreign-requested, even with full coverage, forces no Golomb imbalance.

**Scale.** The construction is sparse:
- r_X(l) = 2k, which is much smaller than Q(span) ~ sqrt(B^{4k+2});
- the classes are tiny, and m <= 1.

So the refutation does not touch statements that assume near-extremality.

**Hypotheses a positive (D-c) would still need, all named and all OPEN.**
- (H1) Fiber near-extremality: r_X(l) >= (1-eps) v_l, so that both Golomb classes are near Q(span).
- (H2) Class near-extremality: |S_e(d)| >= (1-eps) K(span).
- (H3) The large-ratio request regime N_e(h)/|F_h(D)| >> 1.

Under these, an imbalance would lower the per-fiber cap v_l. Through the rank inequality it would then lower K, and hence U_d and X_d. That is the proportional saving the consumer needs.

**Does it fit inside a four-colored square as a diagonal class?** Not checked. The construction is a ternary source only.

## 6. Status summary

- **PROVED:** the family in Section 1 is proper (Theorem B) and realizes the requested fiber for every k (Section 4).
- **REFUTED:** (D-c+) without near-extremality hypotheses.
- **OPEN:**
  - (D-c+) under (H1)–(H3);
  - whether chains of two or more L's force an imbalance in the dense regime;
  - (D-a) and (D-b) in the large-ratio regime;
  - embedding the family in a four-colored square.

=== END OF ANSWER round3_q2 ===
