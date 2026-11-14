# Upper bounds for the directed equal-leg L: verified statements and an exhausted route at side 461

Session of 2026-11-14. Attribution: Theorems 1 and 2 were first claimed in the
collaborator pull request 11 of the project repository (head commit
`b3941b3ad1d669bad7d3f849a28aebb486b178c2`, author TommyMaHaoKun). This document
gives a complete, self-contained proof of both, records an independent
re-execution of their finite certificates, and then reports a new attempt at
side 461 (Propositions 5 and 6), which does **not** succeed.

Status summary.

| Statement | Status |
|---|---|
| Theorem 1: `R_4 <= 21,987,409` | PROVED; elementary; finite certificate re-executed twice (two independent programs agree) |
| Theorem 2: `R_3 <= 462` | PROVED **with external inputs** `G(24) >= 425`, `G(25) >= 480` (exhaustive optimal-Golomb-ruler searches, not replayed); finite certificate re-executed |
| `R_3 <= 461` | UNDECIDED. The prefix-inequality method of Theorem 2 does not reach it, even with word-adaptive kernels (Section 6, numerical evidence) |

## 1. Problem and conventions

A cell is `(x,y)` with `0 <= x,y <= n-1`. The forbidden configuration is
`(x,y), (x+d,y), (x+d,y+d)` with integer `d > 0`, all three cells in the grid and
of one color ("an L"). `R_k` is the least `n` such that every coloring of the
`n x n` grid with at most `k` colors contains a monochromatic L. A coloring is
*proper* if it has no monochromatic L. To prove `R_k <= n` we show that no proper
`k`-coloring of the `n x n` grid exists.

Fix a proper coloring `chi` of the `n x n` grid. Write `z_i = chi(i,i)` (the
diagonal word). For `u < v` the triple `(u,u), (v,u), (v,v)` is an L with step
`v-u`, so

> (1.1) if `z_u = z_v` then `chi(v,u) != z_u`.

For a finite set `A` of integers, the strict source is
`V(A) = {(v,u) : u < v, u,v in A}`, a set of cells of the plane. A coloring of
`V(A)` is proper if no L has all three cells in `V(A)` and one color.
Translations `(x,y) -> (x+s, y+t)` map Ls to Ls.

A *Golomb set* (Sidon set) is a set of integers all of whose positive
differences are distinct. `G(m)` denotes the least span of an `m`-mark Golomb set.

## 2. Two structural lemmas

**Lemma 2.1 (lag classes).** Let `d > 0` and `c` a color. Let
`F = {u : 0 <= u <= n-1-d, z_u = z_{u+d} = c}` and for a color `e != c` let
`B_e = {u in F : chi(u+d,u) = e}`. Then the sets `B_e` partition `F`, and for
`u < v` in `B_e` the cell `(v+d,u)` has a color different from `c` and from `e`.

*Proof.* `chi(u+d,u) != c` by (1.1) applied to `u < u+d`, so the `B_e` partition
`F`. For `u < v` in `B_e`: the cells `(u,u), (v+d,u), (v+d,v+d)` form an L of
step `v+d-u`, and `z_u = z_{v+d} = c`, so `chi(v+d,u) != c`. The cells
`(u+d,u), (v+d,u), (v+d,v)` form an L of step `v-u`; the first and last have
color `e`, so `chi(v+d,u) != e`. ∎

The map `(v,u) -> (v+d,u)` is a translation, so it carries an L inside `V(B_e)`
to an L inside the grid. Hence:

**Corollary 2.2.** With `k` colors, `V(B_e)` carries the proper coloring
`(v,u) -> chi(v+d,u)` using at most `k-2` colors. For `k = 3` this coloring is
constant (one color, call it `e'`); for `k = 4` it uses two colors.

**Lemma 2.3 (binary fibers are Golomb).** Let `A` be finite and let `psi` be a
proper coloring of `V(A)` with colors `{0,1}`. For `h > 0` and `e in {0,1}` put
`C_h^e = {u : u, u+h in A, psi(u+h,u) = e}`. Then `C_h^e` is a Golomb set.

*Proof.* For `u < v` in `C_h^e` the cells `(u+h,u), (v+h,u), (v+h,v)` form an L
of step `v-u` whose first and last cells have color `e`, so `psi(v+h,u) = 1-e`.
Suppose `C_h^e` had two pairs with the same positive difference `g`. Write
them `a, a+g` and `a+t, a+t+g` with `t > 0` (if they share an element then
`t = g`). The cells `(a+g+h, a), (a+t+g+h, a), (a+t+g+h, a+t)` form an L of step
`t`; each has the form `(v+h,u)` with `u < v` in `C_h^e` (namely `(u,v) = (a,a+g)`,
`(a,a+t+g)`, `(a+t,a+t+g)`), so all three have color `1-e`, a contradiction. ∎

**Corollary 2.4 (three colors, six Golomb classes).** For `k = 3`, the set
`B_e` of Lemma 2.1 is a Golomb set. Indeed, for `u < v` in `B_e` the cell
`(v+d,u)` has the unique remaining color `e'`. Two pairs `a, a+g` and
`a+t, a+t+g` in `B_e` with `t > 0` give the L `(a+g+d,a), (a+t+g+d,a),
(a+t+g+d,a+t)` of step `t`; each cell has the form `(v+d,u)` with `u < v` in
`B_e`, so all three have color `e'`, a contradiction. ∎

Thus for three colors, at each lag `d` the starts `u` with `z_u = z_{u+d}` split
into **six** disjoint Golomb sets `B_{c,e}` (`c` the diagonal color, `e != c`),
all contained in `[0, n-1-d]`. For four colors they split into **twelve**
disjoint sets `B_{c,e}`, each carrying a proper two-coloring of its strict
source (Corollary 2.2). This is exactly where the two arguments differ: the
Golomb property at the outer level is a three-color fact; for four colors the
Golomb property enters one level lower, through Lemma 2.3.

## 3. The averaging inequality

Let `w_1, ..., w_t >= 0` (and `w_i = 0` otherwise) and `a_d = sum_i w_i w_{i+d}`
for `d >= 0`; `a_d >= 0`, `a_d = 0` for `d >= t`. Let
`R_d = #{u : 0 <= u <= n-1-d, z_u = z_{u+d}}`.

**Lemma 3.1.** If `n >= t` and the diagonal uses at most `k` colors, then

    (k-1) n a_0  >=  2 sum_{d>=1} (n - d - k R_d) a_d.

*Proof.* Let `f_c` be the indicator of `{i : z_i = c}` on `[0,n-1]` and
`X_c(x) = sum_i f_c(x-i) w_i`. Pointwise `(sum_c X_c)^2 <= k sum_c X_c^2`. Summing
over all integers `x`: the left side is
`sum_{p,q in [0,n-1]} sum_{i,j} w_i w_j [p+i = q+j] = n a_0 + 2 sum_{d>=1} (n-d) a_d`
(each ordered pair `(p,q)` with `|p-q| = d` contributes `a_d`, and there are
`n-d` unordered pairs at distance `d >= 1`, valid since `d < t <= n`). The right
side is `k (n a_0 + 2 sum_{d>=1} R_d a_d)` by the same computation restricted to
pairs of equal color. Rearranging gives the claim. ∎

Since `a_d >= 0`, any upper bounds `R_d <= U_d` give the necessary condition

    (3.2)  -(k-1) n a_0 + 2 sum_{d>=1} (n - d - k U_d) a_d  <=  0.

A proper coloring is excluded as soon as the left side of (3.2) is positive.

## 4. Theorem 1: `R_4 <= 21,987,409`

### 4.1 A rank inequality

**Lemma 4.1.** Let `b_1 < ... < b_s` have span `L = b_s - b_1`, let
`1 <= c < s`, and let `H = cs - c(c+1)/2`. Suppose every positive difference `h`
occurs at most `m_h` times among pairs of the set, and let `P` be the least
possible sum of `H` positive integers in which each value `h` is used at most
`m_h` times. Suppose also that any `j` consecutive marks of the set (for
`j <= c`) span at least `e_j`. Then

    2P + 4 sum_{i=0}^{c-1} (c-i) e_{i+1}  <=  L c (c+1).

*Proof.* The `H` pairs `(b_i, b_{i+j})` with `1 <= j <= c` have positive
differences with the stated multiplicity limits, so their sum is at least `P`.
For fixed `j`, `sum_i (b_{i+j} - b_i)` equals (sum of the last `j` marks) minus
(sum of the first `j` marks) `= sum_{k=0}^{j-1} (b_{s-k} - b_{k+1})`. Summing over
`j = 1..c` gives `sum_{k=0}^{c-1} (c-k)(b_{s-k} - b_{k+1})`. Since the first
`k+1` marks span at least `e_{k+1}` and so do the last `k+1`,
`b_{s-k} - b_{k+1} <= L - 2 e_{k+1}` (also when the blocks overlap, since then
the bound is implied by `b_{s-k} - b_{k+1} = L - (b_{k+1}-b_1) - (b_s - b_{s-k})`).
Hence `P <= L c(c+1)/2 - 2 sum (c-k) e_{k+1}`. ∎

The families used below are hereditary (closed under subsets, after
translation), so the `e_j` may be taken from the same family.

### 4.2 Golomb level

For a Golomb set every `m_h <= 1`, so `P = H(H+1)/2`. Define `g_1 = 0` and, for
`s >= 2`, `g_s = max(g_{s-1}+1, max_{1<=c<=min(130,s-1)} ceil((H(H+1) + 4 sum_{i<c}(c-i) g_{i+1}) / (c(c+1))))`.
By Lemma 4.1 and deletion of the largest mark, every `s`-mark Golomb set has
span `>= g_s`. Put `Q(S) = max{s : g_s <= S}`: a Golomb set of span `<= S` has at
most `Q(S)` marks. (The certificate computes `g_s` for `s <= 4900` and checks
`g_4900 > 21,991,300`, so `Q` is determined on every span used.)

### 4.3 Binary-source level

Call `A` a *binary-source set* if `V(A)` has a proper two-coloring. The family
is hereditary. Let `A` have span `L` and `h > 0`. By Lemma 2.3 the pairs of `A`
at difference `h` split into the two Golomb start sets `C_h^0, C_h^1`, contained
in `[b_1, b_s - h]` (span `<= L-h`). They are disjoint; if both are nonempty,
the one with the larger minimum lies in an interval of span `<= L-h-1`. Hence

    (4.4)  m_h  <=  Q(L-h) + Q(L-h-1),   and uniformly  m_h <= 2 Q(L-1).

*Small spans.* Define `e_1 = 0`; for `s >= 2` start from `L = e_{s-1}+1` and, for
each rank `c <= min(80, s-1)` in turn, increase `L` while Lemma 4.1 with the
uniform cap `M = 2Q(L-1)` and the already computed `e_j` is violated (the least
sum is `P = M q(q+1)/2 + r(q+1)` where `H = Mq + r`, `0 <= r < M`). Every rejected
value of `L` is impossible as the exact span of an `s`-mark binary-source set,
and a value rejected at one rank stays rejected, so the final `L =: e_s` is a
lower bound on the span of every `s`-mark binary-source set.

*Large spans.* Let `N = 21,991,300` (an index origin only). The certificate
file `four_capacity_runs.json` lists 608 triples `(v, K, c)`. For each, with
`L = N - v - 1` and `s = K+1`, Lemma 4.1 with the profile (4.4) and the small
spans `e_j` is violated at rank `c`. Hence a binary-source set of span `<= L`
has at most `K` marks (a larger set would contain a `K+1`-mark subset of span
`<= L`; a smaller span only lowers the right side and the profile). Each row is
valid for all indices from `v` up to the next row's `v`. Write `K_j` for the
resulting cap on binary-source sets lying in `N - j` consecutive integers.

### 4.5 The square

Let `n = 21,987,409` and suppose a proper four-coloring exists. Fix `d > 0`.
By Lemma 2.1 and Corollary 2.2 the starts counted by `R_d` split into twelve
disjoint binary-source sets in `[0, n-1-d]`. Order the nonempty ones by their
(distinct) minima; the one of rank `j` (from `0`) lies in `n - d - j` consecutive
integers. Therefore

    R_d  <=  U_d := sum_{j=0}^{11} K_{N - n + d + j}.

Take `t = 35,000`, `w_i = i(t+1-i)`. Then (3.2) with `k = 4` requires
`-3 n a_0 + 2 sum_{d=1}^{t-1} (n-d-4U_d) a_d <= 0`. The exact value of the left
side is `2,727,455,661,705,377,936,113,840 > 0`. This contradiction proves
**Theorem 1: `R_4 <= 21,987,409`.** ∎

Certificate checks (2026-11-14): `verify_four_rank.py` (PR 11) and
`pr11_review/independent_r4_check.py` (written for this review; no shared code;
direct loops over `h`; `a_d` from literal sums at twelve lags plus the fact that
`a_d` is a polynomial of degree at most 5 in `d` on `0 <= d <= t`) both
re-prove all 608 rows and return the identical margin above.
`four_capacity_runs.json` SHA-256 `2a782fbd81e5c7013ae057a4604bd360d541d3f0e80bd08ef5a349b567a8bfd0`.

## 5. Theorem 2: `R_3 <= 462` (with external inputs)

External inputs: `G(25) >= 480` and `G(24) >= 425` (exhaustive searches by
distributed.net, OGR-25 and OGR-24). Not replayed here.

Let `n <= 479`, a proper three-coloring, and `b = n - 425`. By Corollary 2.4 each
of the six classes `B_{c,e}` at lag `d` is a Golomb set in `[0, n-1-d]`, so has at
most 24 marks; a 24-mark class has span `>= 425`, so its minimum is `< k := b - d`.
Distinct classes have distinct minima, and a 24-mark class `B_{c,e}` has its
minimum `u < k` with `z_u = z_{u+d} = c`. For each `c` at most two classes
(`e != c`) exist, and their minima are distinct starts. Hence, with
`m_c(k) = #{i < k : z_i = z_{i+d} = c}` and `T_k = sum_c min(2, m_c(k))`,

    (5.1)  R_d  <=  138 + T_k  =  U_d - delta_k,   U_d = 138 + min(6, max(0, b-d)),
           delta_k = min(k,6) - T_k >= 0      (1 <= d <= b-1, k = b-d),

and `R_d <= 138` for `d >= b`. Note `T_k` depends only on the prefix
`z_0 ... z_{b-1}`. Insert (5.1) into (3.2) with `k = 3`:

    (5.2)  G_0(w) + 3 D(w,z) <= 0,   G_0 = -n a_0 + sum_{d>=1} (n - d - 3U_d) a_d,
                                      D = sum_{k=1}^{b-1} a_{b-k} delta_k(z).

For `n = 462` (`b = 37`) and `w_i = i(86-i)`, `1 <= i <= 85`, one has
`G_0 = -7,476,723,318`. The program `verify_462.c` (PR 11) enumerates all `3^37`
words `z` by branch and bound and proves `D >= 2,500,000,000` for every one:
for a partial word it uses the valid upper bound
`min(k, 6, sum_c min(2,|P_c|), |union_c P_c|)` on `T_k`, where `P_c` is the set of
starts `i < k` neither of whose endpoints is assigned a color other than `c`;
leaves are disjoint and are counted with their color-permutation multiplicities
(3 for the first letter, then 1 or 2, then 1), and the total is required to equal
`3^37`. Then `G_0 + 3D >= 23,276,682 > 0`, contradicting (5.2). This proves
**Theorem 2: `R_3 <= 462`, given `G(24) >= 425` and `G(25) >= 480`.** ∎

Re-execution (2026-11-14, gcc 16.2.0): all internal checks pass
(`words = 450,283,905,890,997,363 = 3^37`, `remaining = 0`, margin `+23,276,682`;
also the 23-layer variant, margin `+3`, and the 463 run).
`verify_462.c` SHA-256 `b8146c17f7b3e9e1d2f9eaeae9a089dc6d13dc477094c0e24d5fa7718fbce1d7`.
An independent enumerator written for this session (`prefix461/count_bad_words.c`,
different symmetry reduction: canonical first-appearance labeling) also finds
no surviving word at 462 with all 36 layers.

## 6. New attempt: side 461

### 6.1 Word-adaptive kernels

**Proposition 6.1.** Let `z` be the diagonal prefix (length `b`) of a proper
three-coloring of the `n x n` grid, `n <= 479`. Then for **every** nonnegative
vector `w` of support size `W <= n`,

    Q_z(w) := -2n a_0 + 2 sum_{d=1}^{W-1} (n - d - 3 Uhat_d(z)) a_d  <=  0,

with `Uhat_d = U_d - delta_{b-d}(z)` for `d < b` and `Uhat_d = 138` otherwise.

*Proof.* (5.2) holds for every nonnegative `w` (Lemma 3.1 and (5.1) use only
`a_d >= 0`); multiply by 2. ∎

So a prefix is excluded if **some** kernel `w >= 0` makes the Toeplitz quadratic
form `Q_z` positive; the kernel may depend on `z`. This strictly extends the
fixed-kernel test of Theorem 2. Our code (`prefix461/adaptive_kernel.py`)
reproduces PR 11's value for its 461 witness `122120100110100020212021121202210012`
exactly (`-863,712,470` for `w_i = i(86-i)`).

Findings at `n = 461` (`b = 36`), **numerical and exploratory**:

* The fixed-kernel test leaves many prefixes: the enumerator found at least
  **62,547** color-permutation classes of 36-letter words with
  `G_0 + 3D <= 0` before it was stopped (incomplete; the true number is larger).
* Projected power iteration for `max {Q_z(w) : w >= 0, |w| = 1}` (support 110)
  excluded, with exact integer re-evaluation, 20 of 300 randomly sampled such
  words (about 7%). For PR 11's witness the maximum found is negative
  (about `-10.8` at unit norm). A numerical local maximum is not a proof that
  no kernel works; but the evidence indicates that the prefix-inequality family
  (5.1)-(5.2) cannot by itself prove `R_3 <= 461`.

### 6.2 Local window refutations

**Proposition 6.2.** If `chi` is proper on the `n x n` grid and `0 <= p`,
`p + m <= n`, then `chi` restricted to the triangle
`{(x,y) : p <= y <= x <= p+m-1}` is a proper coloring of that triangle (every L
starting in it stays in it) with diagonal `z_p ... z_{p+m-1}`. Hence any window
of the diagonal whose triangle admits no proper coloring is forbidden everywhere
in the diagonal. The anti-transpose `(x,y) -> (n-1-y, n-1-x)` maps Ls to Ls, so a
window is forbidden iff its reversal is.

*Proof.* If `p <= y <= x` and `x + d <= p+m-1`, then all of `(x,y)`, `(x+d,y)`,
`(x+d,y+d)` satisfy the defining inequalities. The anti-transpose sends the L
`(x,y),(x+d,y),(x+d,y+d)` to the L based at `(n-1-y-d, n-1-x-d)` with step `d`. ∎

Findings (solver status only; **no checked refutation is claimed**): the
36-letter triangles of PR 11's witness and of the first enumerated bad word are
UNSAT for CaDiCaL 1.9.5 (about 9e4 and 1.8e5 conflicts; 5.5 s and 16 s). A
DRUP proof pipeline with an independent forward RUP checker was built and
validated on pigeonhole instances, but checking proofs of this size in Python
was too slow to complete in the session. Short windows rarely help: only 3 of 26
sampled bad words contain an UNSAT window of length 16 (1 of length 14).
Random windows of length 18-20 are mostly UNSAT or undecided within 1e5
conflicts (length 20: 18 UNSAT, 22 undecided, 0 SAT of 40).

Consequence: proving `R_3 <= 461` along this line requires a complete list of
the bad 36-letter prefixes (or a smarter enumeration that interleaves local
refutation) and a checked UNSAT certificate for the 36-triangle of each, at a
cost of roughly 10 s of solving per word before proof checking. With at least
`6 * 10^4` words this is a multi-day computation, not attempted.

## 7. What remains open

* `R_3 <= 461`: undecided. The obstacle is quantified in Section 6.
* `R_4`: no improvement below `21,987,409`. The three-level structure
  (Golomb, binary-source, outer twelve classes) loses a factor through each cap;
  the binary-source capacity is the main lever (the bound behaves like the
  square of the binary fiber cap), and no bound beating the `L^{3/4}` order of
  binary-source sets is known.
