# Four colors: what a binary-source bound is worth, and an elementary baseline

Date: 2026-11-13. Base commit: `dc1cbe6daf7d9816329217a511741fbeabd726b3`.
Coordinates are integers; the forbidden configuration is
`(x,y), (x+d,y), (x+d,y+d)` with `d > 0` and one color.

**Outcome.** No new unconditional bound for `R_4`. This package gives (1) an
exact, parametrized version of the manuscript's conditional four-color
theorem, (2) the largest binary-source coefficient that would still improve
the archived unconditional bound, and (3) a short self-contained proof of
`R_4 <= 22049225` as an independent cross-check of that archive. Items (1)
and (2) are a parameter generalization of `thm:s21four`, not a new
mechanism; item (3) reuses `lem:shift` three times.

## Candidate card

```text
Limitation:   the four-color recursion bounds a set with a binary source only
              through "each fiber is two Golomb sets", which yields capacity
              of order L^(3/4); the conditional figure 98777 assumes S21
              with q = 21 and says nothing about weaker hypotheses
Mechanism:    treat the binary-source coefficient q as a parameter and
              propagate it exactly through the fiber partition and lem:shift
Statement:    Theorem A below (k = 4; hypothesis on binary sources)
Cheapest test: exact integer evaluation; reproduce 98777 at q = 21; compare
              the q -> infinity end with the archived unconditional bound
Consequence:  identifies the weakest binary-source statement that improves
              R_4, hence which kinds of lemma are worth attempting
```

## 1. Theorem A (conditional, proved implication)

Write `M(A) = |A|(|A|-1)/2` and `L(A) = max A - min A`. For integers
`q >= 1`, `L >= 0` let `S_q(L)` be the largest integer `s` with
`s(s-1) <= 2qL`.

**Hypothesis `H(q, L*)`.** Every finite `A` in the integers with
`L(A) <= L*` whose strict source `V(A)` admits a proper two-coloring
satisfies `M(A) <= q L(A)`.

**Theorem A.** Let `n >= 2`, `a = ceil(n/4)`, `l = n - 1`, and assume
`H(q, n-2)`. If some integer `t` with `1 <= t <= l + 1` satisfies

```text
a^2 t^2 > (l + t) * [ a t + 6 * sum_{h=1}^{t-1} (t - h) * S_q(l - h) ],   (A)
```

then every coloring of the `n x n` square with at most four colors contains
a monochromatic directed L, that is, `R_4 <= n`.

*Proof.* Suppose a proper coloring `chi` exists. Some color `c0` occupies at
least `a` main-diagonal cells; let `D` be a set of exactly `a` of their
positions, so `L(D) <= l`. For `u < v` in `D`, the cell `(v,u)` is not `c0`,
since `(u,u),(v,u),(v,v)` is a directed L of step `v-u`.

Fix `h` with `1 <= h <= t-1` and partition `F_h(D) = {u : u, u+h in D}` by
the color `b` of `(u+h, u)`; `b != c0`, so there are at most three parts.
Let `E` be one part and define `w(v,u) = chi(v+h, u)` for `u < v` in `E`.
Translating the first coordinate maps directed Ls to directed Ls, so `w` has
no monochromatic L in `V(E)`. It avoids `c0` because `u` and `v+h` lie in
`D` with `u < v+h`. It avoids `b` because
`(u+h,u), (v+h,u), (v+h,v)` is a directed L whose first and third cells have
color `b`. Hence `V(E)` is properly two-colored. Since `L(E) <= l - h <= n-2`,
the hypothesis gives `|E|(|E|-1) <= 2q(l-h)`, so `|E| <= S_q(l-h)` and
`r_h(D) <= 3 S_q(l-h)`. Inserting this into the shift count
`a^2 t^2 <= (l+t)[a t + 2 sum_{h<t} (t-h) r_h(D)]` (`manuscript/main.tex`,
`lem:shift`, applied with span bound `l`) contradicts (A). QED

Inherited: the argument is that of `thm:s21four`. Modified: the hypothesis
is parametrized, the exact integer cap `S_q` replaces the linearization used
there, and `t` is optimized. Nothing here is a new mechanism.

## 2. Exact evaluation

`python sensitivity.py` (about one minute, standard library) writes
`results.json`; `python check.py` recomputes every decisive inequality with
separately written code and writes `check_results.json` (status PASS).

| `q` | certified `n` (so `H(q, n-2)` implies `R_4 <= n`) | `t` | `n / q` |
|---:|---:|---:|---:|
| 10 | 47441 | 419 | 4744.1 |
| 21 | 98733 | 601 | 4701.6 |
| 25 | 117345 | 654 | 4693.8 |
| 50 | 233437 | 921 | 4668.7 |
| 100 | 465093 | 1299 | 4650.9 |
| 250 | 1158789 | 2047 | 4635.2 |
| 500 | 2313601 | 2891 | 4627.2 |
| 1000 | 4621577 | 4084 | 4621.6 |
| 2000 | 9235201 | 5771 | 4617.6 |
| 3000 | 13847517 | 7065 | 4615.8 |
| 4000 | 18459149 | 8157 | 4614.8 |
| 4500 | 20764797 | 8651 | 4614.4 |

Each row is a certificate for that one `n`. The side `n - 1` has no positive
margin for any `t <= n/40`; that is a statement about this inequality, not
about `R_4`. No monotonicity in `n` is claimed or needed.

The row `q = 21` gives `98733` under S21 restricted to spans up to `98731`,
against `98777` in the manuscript. The difference comes only from exact
versus linearized caps and the choice of `t`. It is a technical improvement
of a **conditional** statement and changes no established bound.

**Threshold.** At `n = 21991299` inequality (A) holds with `q = 4765`,
`t = 8903` (margin `247484481219945548`), and the scan finds no certificate
at `q = 4766`. Therefore:

> If `M(A) <= 4765 L(A)` for every `A` with properly two-colorable strict
> source and `L(A) <= 21991297`, then `R_4 <= 21991299`, improving the
> archived unconditional bound `21991300`.

Since (A) only becomes easier as `q` decreases, any proved `q <= 4765` on
that span range improves `R_4`, and by the table the improvement is roughly
proportional to `q`.

## 3. Proposition B (unconditional, elementary): `R_4 <= 22049225`

Let `l = 22049224`. The uniform form of `lem:shift` states: if a set of `s`
integers has span at most `l` and every positive difference occurs at most
`W` times, then `s^2 t <= (l + t)(s + W(t-1))` for every integer `t >= 1`.
A subset of a set with these properties has them too, so one violated
instance at `s0` excludes every `s >= s0`.

1. *Golomb sets* (`W = 1`): `s0 = 4765` violates the inequality at
   `t = 296892`. A Golomb set of span at most `l` has at most 4764 marks.
2. *Sets with a properly two-colored strict source*: for such `E` and any
   `h > 0`, the weak triangle on `F_h(E)` with `w(v,u) = z(v+h,u)` is
   properly two-colored and each of its two diagonal color classes is Golomb
   (`research/coupled_budget_20261108/numeric_upper/THEOREM.md`, section 2).
   So `W = 2 * 4764`; `s0 = 459021` violates the inequality at `t = 31870`.
   Such a set of span at most `l` has at most 459020 marks.
3. *Sets with a properly three-colored strict source*: by the partition in
   the proof of Theorem A, `W = 3 * 459020`; `s0 = 5512307` violates the
   inequality at `t = 7923`. Such a set has at most 5512306 marks.
4. A proper four-coloring of the square of side `22049225` would have a
   diagonal color class with at least `ceil(22049225/4) = 5512307` marks,
   span at most `l`, and properly three-colored strict source. Contradiction.

No external input is used. All four inequalities are checked exactly by
`check.py`. This bound is weaker than the archived `21991300` by `0.26%`;
its purpose is that every step has been checked in one place. The archive
additionally uses distance profiles, an endpoint correction, polynomial
weights, and joint Cauchy over the four diagonal classes
(`exploration/research_round3/four/R3_R4_REPORT.md`).

## 4. What this does and does not establish

- **Established**: Theorem A; the twelve conditional certificates and the
  threshold statement; Proposition B.
- **Not established**: any instance of `H(q, L*)`. Whether any finite
  uniform coefficient exists is open (manuscript, closing section). The
  threshold `4765` is the largest value certified by this inequality with
  `t <= n/40`; other inequalities could give a different threshold.
- **Evidence level**: author derivation plus a separately written checker in
  the same session. No independent reviewer has read this package.
- **Scope**: `k = 4` only. Theorem A's hypothesis is about binary sources,
  the same objects that govern `R_3`, but in a different regime: `R_3` needs
  `q <= 25` on spans up to 450, while `R_4` gains from `q` in the thousands
  on spans up to `2.2 * 10^7`.

## 5. Sharply stated next step

**Target statement.** There exist explicit `C` and `gamma < 3/4` such that
every finite `A` with properly two-colorable `V(A)` has
`|A| <= C * L(A)^gamma`; or, more modestly, `M(A) <= q L(A)` with an explicit
`q <= 4765` for `L(A) <= 21991297`.

**Why the current method cannot reach it.** Using only "every fiber of `A`
is a union of two Golomb sets" gives exponent `3/4` (item 2 above), and the
two-Golomb corner accounting summed over lags returns the same exponent.
A proof must use the compatibility of the two-class splittings of different
fibers, which share completion cells.

**Cheapest discriminating test.** First search `exploration/` for existing
enumerations of small binary sources and reuse any that are complete. Then
compute exactly, for small `L`, the
maximum `f(L)` of `|A|` over `A` in `{0,...,L}` with properly two-colorable
strict source, together with the extremal sets, and compare the growth with
`sqrt(42 L)` (S21) and with the elementary cap. If `f(L)^2 / L` stays
bounded on the computed range the linear conjecture gains support and the
extremal sets show which structure a proof must exploit; if it grows, S21 is
in doubt and the exponent question becomes the primary target. Either result
changes the plan; a larger scan of weight families would not.
