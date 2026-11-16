# round5_q4: attempt to refute MS' (answer)

## Plan / status line (written first)
Target: refute MS' (ledger 52) by an explicit family, or prove it. Working plan:
1. Sharpen what any refuting family must satisfy (quantitative necessary conditions), all proved.
2. Test the natural "lifting / digit-product / block" constructions against MS' rigorously.
3. Record the precise obstruction met and the open core.

**Verdict (summary).** MS' is neither refuted nor proved here. What is proved:
- Theorem N: any refuting family needs lambda_k / sqrt(S_k) -> infinity and each of the three classes
  S_e(d_k) to be a binary source of size >= c(eps) sqrt(S_k) with c(eps) -> infinity, whose fibre prefix
  is saturated; and (Lemma G) the six Golomb pieces must, on most lags, represent almost every gap in
  a range [omega sqrt S, S/omega].
- Proposition P: block-placed sources (F_d(D) inside Sidon-placed blocks of width rho, block step
  M > 2 rho; this contains every digit-product D = M B + R at every shift d <= rho) have joint prefix
  ratio at most theta + kappa with theta = beta Q(rho)/Q(S-rho-1) ~ sqrt(rho/M) < 1/sqrt 2 + o(1); so
  they never refute MS' at the top scale. This is a rigorous replacement of the unproved
  "(1+o(1))/sqrt M" claim of the brief (weaker constant, but complete proof, and for all lambda).
- Hence refuting MS' requires, as a sub-construction, a single binary source with saturated fibre
  prefix beyond lag sqrt(S) (problem SAT below), which is not known to exist.

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

