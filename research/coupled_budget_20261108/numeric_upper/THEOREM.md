# Joint diagonal counting: a 466 rearrangement proof and restored 465 certificate

Date: 2026-11-08. All grid coordinates below belong to `{0,...,n-1}`. The forbidden directed L is `(x,y),(x+d,y),(x+d,y+d)` for integer `d>0`. We prove that every three-coloring of the square of side 465 contains one, using two established external Golomb results. This restores an archived proof; the separate rearrangement argument gives 466.

## 1. External inputs and evidence standard

Let `G(m)` be the minimum **span** of an integer Golomb set with `m` marks. The only non-elementary numerical inputs needed are

\[
G(24)\ge425,\qquad G(25)\ge480. \tag{E}
\]

The primary [OGR-24 completion report](https://blogs.distributed.net/2004/11/) dated 2004-11-01 describes completion of the exhaustive search, its verification passes, and the final verified work unit on 2004-10-13. Its accompanying explanation identifies the optimum span as 425. The [OGR-25 completion report](https://blogs.distributed.net/2008/10/) dated 2008-10-25 identifies optimum span 480 and completion of the exhaustive search after the final verified work unit on 2008-10-24. These are optimality reports, not merely examples of rulers; examples alone would give the wrong inequality direction for (E).

The [2025 published paper](https://math.colgate.edu/~integers/z21/z21.pdf), *Integers* 25, A21, Theorem 6 and Algorithm 3, also contains these values. Its table uses one plus span: entries 426 and 481 at orders 24 and 25. The corresponding [arXiv v1](https://arxiv.org/html/2502.05162v1) agrees. No newer unverified OGR table is used in either numerical certificate here.

The status is **PROVED using cited external computational theorems**, under the usual standard permitting established external results. It is not conditional on an open conjecture. The local checker independently verifies the finite arithmetic and explicit small cases; it does **not** repeat the distributed exhaustive searches or provide a self-contained certificate for (E). A policy requiring local replay of every computational dependency must keep that separate evidence limitation visible.

## 2. Geometric reduction, valid for every diagonal color class

Suppose a square coloring avoids monochromatic Ls. Partition the main diagonal positions into `A_1,A_2,A_3`, allowing initially empty classes. For a fixed class `A=A_i`, all strict-source cells `(v,u)` with `u<v` in `A` avoid color `i`: otherwise `(u,u),(v,u),(v,v)` is a forbidden L. Thus these cells use at most the other two colors.

For `d>0`, let

\[
F_d(A)=\{u:u,u+d\in A\},\qquad r_d(A)=|F_d(A)|.
\]

On the weak source `W(F_d)={(v,u):u<=v; u,v in F_d}`, define
`w(v,u)=chi(v+d,u)`. This is well defined in the strict source of `A`, and the translation of the first coordinate preserves every directed L. Consequently `w` is a proper coloring with at most two colors.

Each diagonal color class `B` of a proper two-coloring of `W(F_d)` is a Golomb set. Indeed all strict cells with both coordinates in `B` must have the other color. If `a,a+h,a+t,a+t+h` belong to `B`, with `h,t>0`, then the strict cells

\[
(a+h,a),\quad (a+t+h,a),\quad (a+t+h,a+t)
\]

have that other color and form an L of step `t`. Distinct equal-difference pairs can always be ordered to have this form, including the three-mark overlap case `h=t`. Hence repeated positive differences are impossible.

The set `F_d` therefore partitions into two Golomb sets in `n-d` available positions, of span at most `n-1-d`. This proves the difference-capacity lemma used in Mammel--Smith--Yerger's Theorem 6, with the source restriction made explicit. At any `n<=481`, input (E) gives the convenient (possibly nonsharp) bound

\[
r_d(A_i)\le C_d:=\min\{n-d,\;48\text{ if }n-1-d\ge425,
\;46\text{ if }n-1-d<425\}. \tag{1}
\]

The notation inside the minimum means to choose the applicable one of 48 and 46. This argument applies independently to all three original diagonal colors, so
`R_d:=sum_i r_d(A_i) <= 3 C_d`. It uses neither a rainbow-minimization theorem nor extension of a sparse source to a square.

## 3. Joint endpoint rearrangement

**Lemma.** Partition `{0,...,n-1}` into `k` classes `A_i`, with each size `m_i>=2c`. Write each class increasingly as `a_(i,1),...,a_(i,m_i)`. The total distance of all same-class pairs whose rank difference is at most `c` satisfies

\[
D_c:=\sum_{i=1}^{k}\sum_{j=1}^{c}\sum_{r=1}^{m_i-j}
(a_{i,r+j}-a_{i,r})
\le {k c(c+1)\over2}n-{k^2c(c+1)(2c+1)\over6}. \tag{2}
\]

**Proof.** In one class, the coefficient of its `r`-th position is
`min(c,r-1)-min(c,m_i-r)`. Since `m_i>=2c`, the nonzero coefficients are exactly `-c,...,-1,1,...,c`, each once, with zeros elsewhere. Thus the global multiset contains `k` copies of every nonzero coefficient. By the rearrangement inequality its scalar product with the distinct positions `0,...,n-1` is maximized when the coefficients are sorted. For a positive coefficient `t`, `1<=t<=c`, pair its `k` positions near the upper endpoint with those of coefficient `-t` near the lower endpoint. Their contribution is `k*t*(n-k*(2*(c-t)+1))`. Summing over `t` gives (2). This also gives an elementary adjacent-swap proof of the rearrangement step. For `k=3`, (2) simplifies to

\[
D_c\le {3\over2}c(c+1)(n-2c-1). \tag{3}
\]

The pair count is `K=cn-3c(c+1)/2`. At most `3 C_d` selected pairs have distance `d`. Therefore a lower bound for `D_c` is obtained by filling the cheapest distances first, with capacities `3 C_d`. The greedy rule follows by moving any available unit from a higher distance to a lower unsaturated distance; it is an exact integer minimum for this relaxation.

**Consequence at 466.** From `r_d(A_i)<=48` and `sum_d r_d(A_i)=binom(m_i,2)`, each `m_i` satisfies

\[
\binom{m_i}{2}\le465\cdot48=22320<\binom{212}{2}=22366.
\]

Hence `m_i<=211`, and since their sum is 466, every `m_i>=44`. We may use `c=22` without assuming balanced color sizes. There are `K=9493` selected pairs. The relevant capacities are 144 for `d=1,...,40` and 138 for `d=41,...,68`. Greedy filling uses all 144 slots at distances 1 through 40, all 138 at distances 41 through 67, and seven at distance 68. Thus

\[
D_{22}\ge144\sum_{d=1}^{40}d+138\sum_{d=41}^{67}d+7\cdot68
=319760.
\]

But (3) gives `D_22<=319539`. The contradiction gap is 221, proving `R_3<=466` from (E). The new ingredient relative to a separately bounded single color class is the competition of all three classes for the same diagonal endpoints. This is a reusable combinatorial lemma, not evidence that 466 is the best bound obtainable by all interval methods.

## 4. Independent reconstruction of the archived 465 proof

For each `i=1,2,3`, let `f_i` be the indicator of `A_i`, extended by zero to the integers. Let `w` be any finite nonnegative real weight sequence of length at most `n`, and put

\[
a_d=\sum_t w_t w_{t+d},\qquad g_i=f_i*w,\qquad H=\mathbf1_{\{0,...,n-1\}}*w.
\]

Because `sum_i f_i` is the indicator of the complete diagonal, `sum_i g_i=H`. Pointwise Cauchy gives `3 sum_i g_i(x)^2 >= H(x)^2`. Summing and expanding both convolutions yields

\[
\sum_i\|g_i\|_2^2=n a_0+2\sum_{d\ge1}a_d R_d,
\qquad
\|H\|_2^2=n a_0+2\sum_{d\ge1}(n-d)a_d.
\]

Using `R_d<=3 C_d` and `a_d>=0`, a necessary condition is

\[
\boxed{\quad\sum_{d\ge1}(n-d-9C_d)a_d\le n a_0.\quad} \tag{4}
\]

There is no assumption on individual color-class sizes in (4). The identity `sum_i f_i=1` supplies the joint constraint missing from separate color estimates.

Set `n=465` and `w_i=min(i,94-i)` for `i=1,...,93`, zero otherwise. Let `P=sum_(d=1)^39 a_d`, `Q=sum_(d=40)^92 a_d`, and `D=sum_(d=1)^92 d*a_d`. Exact reconstruction from the 93 weights gives

| Quantity | Integer value |
|---|---:|
| `a_0` | 69231 |
| `P` | 2038439 |
| `Q` | 366786 |
| `D` | 53496528 |

At this side length, (1) permits `C_d=48` through `d=39`, and `C_d=46` from `d=40` through 92. The left side of (4) minus its right side equals

\[
465(P+Q)-D-18(24P+23Q)-465a_0=285630>0.
\]

This proves `R_3<=465`. The checker additionally constructs `H` by literal convolution and verifies the equivalent Cauchy gap `||H||_2^2 - 3[n a_0+6 sum C_d a_d]=571260`, independently of the grouped expression. All arithmetic is exact.

The same weight and grouped certificate already appear in `exploration/research_round4/checks/build_verification_report.py` under “Direct conditional proof of the inherited three-color bound.” That report reserved the external-input verification question. The present work checks the primary optimality reports and reconstructs the proof; it must be called a restored earlier result, not a newly discovered 465 bound. Invalidating the separate G9/rainbow route does not invalidate this direct proof.

## 5. Scope of computation and remaining work

Run `python verify.py` in this directory. `results.json` pins input and proof hashes, lists the exact endpoint scan, and records an exhaustive supplement over three-color diagonal partitions through length nine. The small enumeration supports the implementation; the general proof of (2) supplies the universal statement.

The endpoint scan covers `300<=n<=480` and every `c` certified by the sufficient size bound `2c<=n-2M(n)`, where `M(n)` is the largest integer with `binom(M(n),2)<=sum C_d`. A nonpositive gap means only that this specified sufficient inequality fails to exclude that side; it is neither a coloring witness nor a lower bound. In particular it is not a proof that every possible endpoint or transport inequality stops at 466.

Integer rounding can strengthen (4): if the weights are integers and `J` counts positions where `H(x)` is not divisible by three, pointwise minimization gives `3 sum_i g_i(x)^2 >= H(x)^2+2` at those positions. Therefore the contradiction expression in (4) can be increased by `J`. This refinement is checked numerically, but does not by itself claim a bound below 465.

The general endpoint lemma applies to any `k`; the fiber decomposition into **Golomb** classes uses a two-color weak source and hence is specific to three square colors. For four colors, diagonal elimination leaves three colors and the complementary-color argument is unavailable. No four-color numerical bound is asserted.

The source comparison covers the cited 2025 paper and the repository's archived interval/convolution routes. The endpoint presentation is newly developed in this work package, but no global novelty priority claim is made. Further progress needs a constraint beyond individually capped difference counts and these particular joint inequalities, or an independently certified stronger weight/cut.
