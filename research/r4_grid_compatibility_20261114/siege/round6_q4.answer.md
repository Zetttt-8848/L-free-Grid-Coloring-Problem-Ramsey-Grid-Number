# round6_q4 answer: the fibre-size deficit FD

## Verdict

**FD: NOT SETTLED.** I did not refute it, and I did not prove it.

What this file establishes:

- **R1 (PROVED).** A two-sided reduction. FD is implied by a deficit for single binary sources (BD), and refuting FD needs binary sources that violate BD at every level. So refuting FD needs, at minimum, an answer to the open binary-source question: are there binary sources of size near sqrt(2) S^{3/4}?
- **R2 (PROVED).** Properness of a binary source restated through start sets (the binary form of P1(i)), plus the pair-witness form of the same condition.
- **R3 (PROVED).** Binary sources colored by difference: the forced sign rule f(d) = f(t) ≠ f(d+t), the ban on 3-dimensional Hilbert cubes, and the factor-1/sqrt 2 Fejér cap.
- **R4 (PROVED, negative).** Two attempted constructions fail, with explicit reasons:
  - the base-M product does not raise the exponent above 1/2;
  - the doubling D = Y ∪ (Y+d) turns the converse of R1 into a full-grid coloring problem.
- **R5 (HEURISTIC).** Why a random-like near-Fejér binary source cannot exist, and why this does not give a proof.

Conventions are as in the task. Q is nondecreasing. v_1(S) = Q(S-1) + Q(S-2). g(S) := sqrt(v_1(S) S) is nondecreasing in S. K_F is the Fejér cap of Corollary F0, and K_F(S) >= g(S).

## R1. Reduction: FD sits between a binary deficit and its failure (PROVED)

**BD(eta, S_1).** Every binary source X (a finite set with a proper 2-coloring of V(X)) with span X = S' >= S_1 has |X| <= (1-eta) g(S').

**Claim 1.** BD(eta, S_1) implies FD(eta', S_0) for every eta' < eta and S_0 large enough (explicit below).

*Proof.*
- Fix a proper ternary source, a shift d, and S = span F_d(D) >= S_0.
- Each class X_e = S_e(d) is a binary source of span S_e <= S, by (iv.0).
- If S_e >= S_1, then |X_e| <= (1-eta) g(S_e) <= (1-eta) g(S), since g is monotone.
- If S_e < S_1, then |X_e| <= S_1.
- Summing over the three classes: |F_d(D)| <= 3(1-eta) g(S) + 3 S_1.
- By Section 0 of 3.2, g(S) >= S^{3/4}/sqrt 2 for S >= 34. So 3 S_1 <= 3(eta-eta') g(S) once S^{3/4} >= sqrt2 S_1/(eta-eta').
- So FD(eta', S_0) holds with S_0 = max(34, (sqrt2 S_1/(eta-eta'))^{4/3}). ∎

**Claim 2.** Suppose FD fails for every eta. That is, for every eta and S_0 there is an instance with S >= S_0 and |F_d(D)| > 3(1-eta) g(S). Then for every eta there are binary sources X with span S' -> infinity and |X| > (1-eta) g(S').

*Proof.*
- The largest class satisfies |X_e| > (1-eta) g(S) >= (1-eta) g(S'), where S' = span X_e <= S.
- span X_e -> infinity: by Lemma K, |X_e| <= sqrt(16 S' Q(S')) <= C S'^{3/4}, while |X_e| > (1-eta) S^{3/4}/sqrt 2 -> infinity. ∎

So the problem has three layers:

- BD is the single-class question.
- FD is the same question for three classes jointly.
- A refutation of FD needs near-Fejér binary sources first. The run knows none; it knows nothing beyond Sidon size ~sqrt S.

## R2. Binary form of properness (PROVED)

Let X be finite and psi a coloring of V(X) = {(v,u): u<v in X} with colors {a,b}; write c̄ for the other color. For l >= 1 put A^c_l = {u : u, u+l in X, psi(u+l,u) = c}. So F_l(X) = A^a_l ⊔ A^b_l.

**Lemma 2.1.** psi is proper iff for all d, t >= 1 and each c, F_t(A^c_d) ∩ A^c_{d+t} = ∅. Equivalently, F_t(A^c_d) ⊆ A^{c̄}_{d+t}.

*Proof.* By Lemma 0, the L's of V(X) are exactly L(u,d,d+t) with u, u+d, u+t, u+d+t in X. Its cells are:

- (u+d,u): color c iff u ∈ A^c_d;
- (u+t+d, u+t): color c iff u+t ∈ A^c_d;
- (u+d+t, u): color c iff u ∈ A^c_{d+t}.

So L(u,d,d+t) is monochromatic of color c iff u ∈ F_t(A^c_d) ∩ A^c_{d+t}. For the "equivalently": u ∈ F_t(A^c_d) gives u, u+d+t ∈ X, so u ∈ F_{d+t}(X) = A^a_{d+t} ⊔ A^b_{d+t}. ∎

**Corollary 2.2 (pair-witness form).** For u < v in X put W(u,v) = {w ∈ X : u < w < v, u+v-w ∈ X}. psi is proper iff for every pair u<v and every w in W(u,v), the three cells (w,u), (v,u+v-w), (v,u) are not all one color.

In words: the pair (u,v) may take color c only if no witness w has both arm pairs (u,w) and (u+v-w,v) of color c.

*Proof.* This is Lemma 2.1 with d = w-u and t = v-w. ∎

Counting: sum over u<v of |W(u,v)| = #{(u,d,t): d,t >= 1, u,u+d,u+t,u+d+t ∈ X} = sum_{d,t>=1} Phi(d,t), where Phi(d,t) = r_{F_d(X)}(t), which is symmetric in d and t.

## R3. Binary sources colored by difference (PROVED)

Suppose psi(v,u) = f(v-u) for some f : Z_{>0} -> {a,b}. Call (d,t) **realized** if some u has u, u+d, u+t, u+d+t ∈ X.

**Lemma 3.1.** psi is proper iff f(d) = f(t) ≠ f(d+t) for every realized (d,t). This includes d = t, where the condition reads f(d) ≠ f(2d) on 3-APs.

*Proof.*
- Only if: realized (d,t) gives the L(u,d,d+t). Its arms have lag d and its corner has lag d+t, so f(d) ≠ f(d+t).
- Realized is a symmetric relation (swap d and t), so also f(t) ≠ f(d+t).
- With two colors, these two facts force f(d) = f(t).
- If: every L is some L(u,d,d+t) with (d,t) realized, and its colors are f(d), f(d), f(d+t). ∎

**Lemma 3.2 (no 3-cube).** A binary source colored by difference contains no Hilbert cube {u + e1 d1 + e2 d2 + e3 d3 : e_i ∈ {0,1}} with d_1, d_2, d_3 >= 1. Coincident points are allowed.

*Proof.* The pairs (d1,d2), (d1,d3), (d2,d3) and (d1+d2, d3) are all realized with base u. Lemma 3.1 gives:

- f(d1) = f(d2) = f(d3), from the first three pairs;
- f(d1+d2) ≠ f(d1), from (d1,d2);
- f(d1+d2) = f(d3) = f(d1), from (d1+d2, d3).

The last two contradict each other. ∎

**Remark (size).** Every fiber of a difference-colored source is a single Golomb class. So r_X(l) <= Q(S-l), and Lemma F gives |X| <= (1+o(1)) sqrt(Q(S) S). That is a factor 1/sqrt 2 + o(1) below g(S).

So difference-colored binary sources cannot refute BD, nor through R1 FD. This is the binary analogue of 5.1. Lemma 3.2 does not lower the exponent: from memory (Szemerédi's cube lemma, CITED), sets without a 3-cube can have size up to order N^{3/4}. I did not settle whether difference-colored binary sources of size S^{1/2+epsilon} exist.

For general colorings, the analogue of Lemma 3.2 fails at the fiber level. A 3-cube inside a fiber F_l(X) needs a 2-coloring of {0,1}^3 in which none of the 12 parallelograms (the 6 faces and the 6 diagonal rectangles) is monochromatic. The parity coloring does this: each parallelogram is an affine plane of F_2^3 other than the two parity planes, so it meets both parities. So I found no forbidden finite configuration for general binary sources beyond the Golomb split.

## R4. Failed construction routes (PROVED negative statements)

**4.1 Base-M products.** Let X = A + M B with M > 2 span A and B Sidon with no 3-AP. Decoding the identity u + (u+h) = (u+d) + (u+h-d) by blocks gives b1+b4 = b2+b3 and a1+a4 = a2+a3. With B Sidon, the block pattern is one of three types:

- all four points in one block: an L inside A's strict source;
- b1=b2 < b3=b4: two inner arms and an outer corner;
- b1=b3 < b2=b4: an L inside the full grid A×A of the block pair.

So each block pair needs a proper 2-coloring of the full grid A×A. For A Sidon with no 3-AP, the only grid L's are (x,x),(x+t,x),(x+t,x+t). The coloring "diagonal a, off-diagonal b, inner κ ≡ a" is proper, but then |X| ~ sqrt(span X / 2).

For |A| >> sqrt(span A), the full-grid 2-coloring is a full-square-type problem. That is strictly harder than the strict source. Combined with Proposition P (ratio <= Q(ρ)/sqrt M), products neither raise the exponent nor reach the Fejér constant.

**4.2 Converse of R1 via doubling.** Take D = Y ∪ (Y+d) with d > 2 span Y. Then F_d(D) = Y exactly. The L's of V(D) have block patterns (0000), (1111), (0101) and (0011), by the same decoding with b_i ∈ {0,1}.

Pattern (0101) is an L in the full product grid {(v+d,u): u,v ∈ Y}. So building a ternary source from three near-Fejér binary sources requires a proper 3-coloring of the full grid Y×Y with a prescribed diagonal. That is the original square problem on Y. So the converse of Claim 1 (BD failing implies FD failing) is NOT proved. FD might hold even if BD fails.

## R5. Why a near-Fejér binary source must be highly structured (HEURISTIC)

Near-Fejér size forces density p ≈ sqrt2 S^{-1/4} in every window of length >> S^{3/4} (equality in Lemma F) and r_X(l) ≈ 2 sqrt S for l <= eps S (Theorem N). Then the typical witness count is |W(u,v)| ≈ p^2 (v-u), which is of order sqrt S for v-u of order S.

If arm colors were independent fair coins, a pair would have no witness of its own color with probability about (3/4)^{|W|}. So Corollary 2.2 cannot be met by anything random-like. The coloring must correlate N^+(u) with the reflection of N^-(v) for almost every pair.

This is the request-collision picture of Theorem N. It gives no contradiction: a rigorous version would be a relative corners theorem for the sparse, structured set X×X. I could not prove one, and any constant it gave would be far from explicit.

## Consequence for R_4 (implication only)

FD(eta) gives, at each shift, sum_e |S_e(d)| <= 3(1-eta) g(S) <= 3(1-eta) K_F(S). The consumer uses the rank cap K. Using the problem's own estimates (HEURISTIC), g(S) and K differ by about 1% at the working scale. So FD(eta) yields the hypothetical X_d <= (1-delta) U_d only with delta ≈ eta - 0.01; it must be recertified exactly. No bound on R_4 is claimed.

## Open questions

1. **BD:** is every binary source of span S of size <= (1-eta) g(S)? Is it o(S^{3/4})? Is it S^{1/2+o(1)}?
2. Does any binary source of size >= S^{1/2+epsilon} exist, even one colored by difference (Lemma 3.1 gives the exact combinatorial condition)?
3. The converse of Claim 1: do three disjoint near-Fejér binary sources fit as the classes of one proper ternary source? R4.2 reduces this to a full-grid 3-coloring of Y×Y.
4. A relative corners theorem for X×X with near-Sidon fibers. This would prove BD, and hence FD.

=== END OF ANSWER round6_q4 ===
