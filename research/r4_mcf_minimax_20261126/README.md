# Unconditional four-color upper bound $R_4(L) \le 21{,}947{,}741$ via exact integer min-cost-flow Farkas duality and three-segment KD-tree outer matching

Every four-coloring of the full square $[n]^2$ of side **$n = 21{,}947{,}741$** contains a monochromatic directed equal-leg $L$ $\{(x, y), (x + d, y), (x + d, y + d)\}$ with integer $d > 0$.

This improves the previous unconditional verified bound of $21{,}947{,}830$ ([`r4_stratified_farkas_20261124`](../r4_stratified_farkas_20261124/README.md)) by **89**, the subadditive Farkas bound of $21{,}947{,}834$ ([`r4_subadditive_farkas_20261124`](../r4_subadditive_farkas_20261124/README.md)) by **93**, the disjoint-bin bound of $21{,}947{,}855$ ([`r4_disjoint_edge_bins_20261123`](../r4_disjoint_edge_bins_20261123/README.md)) by **114**, and the round-3 bound of $21{,}947{,}865$ by **124**.

Following repository governance (`AGENTS.md` and `lgrid-research`), this bound is **100% unconditional and verified** in exact integer and rational arithmetic (`int` and `fractions.Fraction`) by a standalone Python standard-library checker ([`verify.py`](verify.py)) with all upstream window matrices and finite binary-source RUP proofs vendored in-tree. Conditional bounds (such as $98{,}777$ under open conjecture `S21`) play zero role here.

Below, **New Mechanisms**, **Technical Improvements**, **Numerical Bound**, and **Obstruction Closure** are separated explicitly.

---

## 1. New mechanisms

### 1.1 Exact-integer min-cost-flow (MCF) Farkas dual with reversed partial-bin span and direct fixed-point scalar

Let $A \subseteq \{0, \dots, p - 1\}$ have $|A| = k$ marks in a hereditary family with interval capacity cap $\operatorname{cap}(u)$, and let $S_i = \mathbf{1}_A * w_i$ be the discrete convolution against the $B$-replicated Carter–O'Bryant–Tao window row $G_i$ against expanded table $T_i$ of total length $p + m B$ ($m = 200$, $p - 1 \ge 400 B$).

1. **Exact integer transshipment formulation**: Every entry in all six rows of `G.txt` is an exact integer multiple of $2^{-20}$ with uniform row mass $\sum_{r=0}^{199} G_{i,r} = 20$. Hence the normalized coarse weights satisfy
   $$\bar G_{i,r} = \frac{G_{i,r}}{20} = \frac{G^{\mathrm{int}}_{i,r}}{20{,}971{,}520}, \qquad G^{\mathrm{int}}_{i,r} \in \mathbb{Z}_{\ge 0}.$$
   Introducing prefix potentials on bin $j \in \{0, \dots, 199\}$ turns the contiguous multi-bin covering LP
   $$\min \sum_{0 \le a \le b \le j} C_{a,b} y_{a,b} \quad \text{s.t.} \quad \sum_{a \le r \le b} y_{a,b} \ge \bar G_{i,r} \;\; (0 \le r \le j), \;\; y_{a,b} \ge 0$$
   into an uncapacitated min-cost flow problem with integer node supplies summing to $20{,}971{,}520$, producing **exact 64-bit integer multipliers** $y^{\mathrm{int}}_{a,b} \in \mathbb{Z}_{\ge 0}$ with zero floating-point LP rounding loss.

2. **Exact reversed partial-bin span**: In the indexing $A \subseteq [0, p - 1]$ with table positions $0, \dots, p + m B - 1$, left-end position $y = j B + (k_{\mathrm{step}} - 1)$ ($1 \le k_{\mathrm{step}} \le B_0$) sees marks in $[0, j B + k_{\mathrm{step}} - 1]$ (partial bin $I_j = [0, k_{\mathrm{step}} - 1]$ of length $k_{\mathrm{step}}$). At right-end position $y = (p + m B - 1) - (j B + k_{\mathrm{step}} - 1)$, window support $y - x \le m B - 1$ restricts coarse bin $j$ to $[p - (k_{\mathrm{step}} - 1), p - 1]$, which is **empty at $k_{\mathrm{step}} = 1$** and has exact length $k_{\mathrm{step}} - 1$ for $k_{\mathrm{step}} \ge 2$; its union with earlier reversed bins $I_a \cup \dots \cup I_j = [p - (j - a)B - (k_{\mathrm{step}} - 1), p - 1]$ has exact cardinality $(j - a)B + (k_{\mathrm{step}} - 1) \le (j - a)B_1 + (k_r - 1)$.

3. **Direct non-circular test scalar $\lambda^*$**: On any parameter band $B_0 \le B \le B_1$, $D^* < p \le P_1$, $k \ge K_0$, put $P = p + B \alpha \le P_1 + B_1 \alpha$ and test the positive scalar $\lambda = k / (P - D^*)$. Monotonicity gives
   $$\frac{1}{B \lambda} = \frac{P - D^*}{B k} \le \frac{P_1 + B_1 \alpha - D^*}{B_0 K_0} =: \lambda_{\mathrm{inv}}.$$
   Whenever the summed squared positive shortfalls across disjoint left and right edge bins ($p - 1 \ge 400 B > 200 B$) certify $\mathbf{E}\|S_i - \lambda T_i\|_2^2 \ge \lambda^2 D^*$, substituting $\lambda = k / (P - D^*)$ into $\mathbf{E}\|S_i - \lambda T_i\|_2^2 \le E - 2\lambda k + \lambda^2 P$ yields $k^2 \le (P - D^*) E$ directly in one algebraic step.

### 1.2 Three-segment KD-tree histogram-stratified outer matching DP

At an isolated unit drop in $C(p)$ from $K + 1$ to $K$ with preceding gap at least $S = 3 M$ ($M = 13, S = 39$), two length-$3M$ four-color words $P, T \in \{0, 1, 2, 3\}^{3M}$ govern the total excess above $12 K$:
$$M(P, T) = \sum_{s=1}^{3M} \sum_{c=0}^3 \min\bigl(3,\; \#\{0 \le i < s : P_i = T_{3M - s + i} = c\}\bigr).$$
Single-segment rank-split DP ([`r4_stratified_farkas_20261124`](../r4_stratified_farkas_20261124/README.md)) caps out at $75$ missing matches ($S = 35$), and two-segment rank-split DP ($S = 36 = 18 + 18$) caps out at $90$ missing matches because balanced segments of length $18$ already contain $\ge 4 > 3$ occurrences of every color.

Choosing segment length $M = 13$ ($S = 39 = 13 + 13 + 13$) keeps balanced segments near the per-color cap of $3$ while extending total block length to $39 \le \min\operatorname{gap}_{\mathrm{prev}} = 59$. Split $P = P^{(0)} P^{(1)} P^{(2)}$ with $n_0 = \operatorname{hist}(P^{(0)})$ sorted $n_{0,0} \le n_{0,1} \le n_{0,2} \le n_{0,3}$ by palette permutation and $(n_1, n_2) \in \Delta_{13} \times \Delta_{13}$, and assign six nondecreasing integer weight families $b_{a,b}[c][r] \in [0, \Delta]$ ($0 \le a \le b < 3$, $\Delta = 60{,}000$) to match pairs $(i, k = 3M - s + i)$ according to $a = \lfloor i / M \rfloor$ and $b = \lfloor k / M \rfloor$.

In shift band $u \in \{0, 1, 2\}$ ($s = u M + t$, $1 \le t \le M$):
- **Earlier segments $0 \le a < u$**: Writing $i = a M + \iota$ ($0 \le \iota < M$) gives $k = (3 - u + a)M + (\iota - t)$ with $-M \le \iota - t \le M - 2$, so $\lfloor k / M \rfloor \in \{2 - u + a, \; 3 - u + a\}$ takes **at most two adjacent super-diagonal values**! Specifically, $w(i, k)$ is bounded by $T_{0,1} = \max(b_{0,1}, b_{0,2})$ in Band 1 ($a = 0$), and by $T_{0,0} = \max(b_{0,0}, b_{0,1})$ ($a = 0$, never touching $b_{0,2}$!) and $T_{1,1} = \max(b_{1,1}, b_{1,2})$ ($a = 1$) in Band 2.
- **Active segment $a = u$**: Every counted match satisfies $i = u M + \iota < u M + t = s \implies \iota < t$, forcing $k = 3M + (\iota - t) \in [2M, 3M - 1]$ ($\lfloor k / M \rfloor = 2$ **uniquely**, using $b_{u,2}$ with zero $\max$ relaxation!).
- **Columns $k = u M + t - 1$**: Bounded by $\max_c \bigl[\sum_{a < u} \sum_{r < \mathrm{hi}_a[c]} (\Delta - b_{a,u}[c][r]) + \sum_{r < h^{(u)}_c(t)} (\Delta - b_{u,u}[c][r])\bigr]$.

Thus all three bands decouple completely into three fast four-count integer DPs over reachable prefix states $\sum_c \max(0, \mathrm{lo}_u[c] - h_c) \le M - t$. Across all **39** sorted first-segment partitions $n_0$, partitioning $(n_1, n_2) \in \Delta_{13} \times \Delta_{13}$ via **102,416 integer-verified KD-boxes** (exhaustively verified over all $39 \times 560 \times 560 = 12{,}230{,}400$ histogram triples via 560-bit simplex masks, with 16 single-point leaves on $n_0 = [0, 0, 5, 8]$ certified to $\ge 99$ via their exact 36-shift prefix $P[0..35] = 12 + 12 + 12$) proves **at least 99 missing matches** in every isolated 39-shift drop block (`+24` over `d18a965`'s `75`, `+42` over `c5a6394`'s `57`). Three boundary 2-segment fallback tiers ($S = 32 \to 80$, $S = 28 \to 77$, $S = 26 \to 75$) plus $S = 20 \to 41$ are also included.

---

## 2. Technical improvements

1. **First-principles finite seeds & full 200-bin span tables**:
   - Optimal small Golomb spans $g_2 = 1, g_3 = 3, g_4 = 6, g_5 = 11, g_6 = 17, g_7 = 25, g_8 = 34, g_9 = 44, g_{10} = 55$ are proved directly inside `verify.py` via explicit rulers and bitwise exhaustive search, seeding rank-neighbor Golomb lower spans through $56{,}000$ marks ($\text{max span } 3{,}109{,}581{,}842 > 200 \times 16{,}600$).
   - Exact finite binary-source lower spans $e_2 \dots e_{16} = (1, 2, 3, 4, 6, 7, 9, 10, 12, 14, 17, 19, 21, 24, 26)$ are certified in [`rup_manifest.json`](rup_manifest.json) + 11 compressed RUP proofs in [`rup_proofs/`](rup_proofs/) (verified independently by both zero-dependency C99 [`rup_check.c`](rup_check.c) and `drat-trim`, with an embedded pure-Python 2-watched-literal RUP fallback in `verify.py`).
   - Full **nonuniform** rank-neighbor binary-source spans (replacing the previous uniform extension beyond 600 marks) are computed and audited through $22{,}000$ marks ($\text{max span } 375{,}461 > 200 \times 1{,}800$) in $< 0.1\text{ s}$ via $O(\log M)$ prefix-sum pricing and multiset monotonicity.
   - All **200 disjoint edge bins** (up from 150) at both ends of all 6 window rows are activated.

2. **Exact-band discrepancy stratification**:
   - **Inner Golomb**: 18 tight sub-bands across $4{,}600 \le k \le 4{,}800$ raise the active inner Golomb discrepancy from $56.125897$ to **$D_{\mathrm{inn}} \approx 79.113300$** ($+22.99$), advancing each of the 201 Golomb thresholds by $\sim 23$ positions.
   - **Proper binary strict sources**: Grouping the 570 staggered binary capacity witnesses by their **exact integer block width $B_0 = B_1 = B \in [1770, 1790]$** across 38 bands eliminates $B$-interval dilution completely and raises the binary-source discrepancy from $230.442028$ to **$D_{\mathrm{bin}} \in [260.105895, 265.054033]$** (mean $262.36$, $+31.92$), advancing the binary capacity profile by $\sim 82$ positions.

---

## 3. Numerical bound & status layering

| Claim | Value | Status | Verified by |
| --- | ---: | --- | --- |
| Unconditional 4-color upper bound $R_4(L)$ | **$21{,}947{,}741$** | **Verified** | `python3 verify.py` |
| Exact integer margin at $n = 21{,}947{,}741$ | `+67,076,013,380,690,640,788,136,578,854,518,589,429,308,720` | **Verified** | `python3 verify.py` |
| Exact integer margin at $n = 21{,}947{,}740$ | `-916,940,407,726,135,389,747,853,775,262,441,260,974,083,408` | **Verified** | `python3 verify.py` |
| Outer drop blocks credited ($S = 39$, loss $\ge 99$) | $562$ pairwise disjoint blocks | **Verified** | `python3 verify.py` |
| Finite binary-source spans $e_2 \dots e_{16}$ | $1,2,3,4,6,7,9,10,12,14,17,19,21,24,26$ | **Verified** | `rup_check.c` + `drat-trim` + `verify.py` |
| Zero-rainbow 4-color square witnesses $\rho_6^{(4)} = \dots = \rho_{10}^{(4)} = 0$ | Explicit proper 4-colorings of $S_6 \dots S_{10}$ | **Verified** | `verify.py` + `check_coloring.py` |

*(Note: Conditional bounds such as $98{,}777$ under open hypothesis `S21` remain strictly conditional and are never conflated with the unconditional bound certified here.)*

---

## 4. Obstruction record: closing the direct 4-color triangle rainbow route (`1da352c`)

In three colors, strict-lower-triangle rainbow $L$ minima $r_m^{(3)} > 0$ ($m \ge 5$) and the parity-forcing ceiling $r_m^{(3)} \le U_m^{(3)} \approx m^2 / 2$ drive the translated-triangle LP proof of $R_3(L) \le 139$ ([`weak_triangle_20261123`](../weak_triangle_20261123/README.md)). Kimi Round 5 (`1da352c`) derived the 4-color parity-forcing ceiling $\rho_m^{(4)} \le U_m^{(4)} = \lfloor (H_m - E_m^{(4)}) / 2 \rfloor \sim m^3 / 24$ ($U_8^{(4)} = 38$, $U_{10}^{(4)} = 72$) but left the actual minimum $\rho_m^{(4)}$ open.

In [`zero_rainbow_witnesses.json`](zero_rainbow_witnesses.json) (verified by both `verify.py` and `.agents/skills/directed-l-grid-research/scripts/check_coloring.py`), we exhibit explicit $L$-free 4-colorings of the full $m \times m$ square $S_m$ achieving:
- **Zero rainbow $L$s across the entire square $S_m$** for $m = 6, 7$, and
- **Zero rainbow $L$s across the strict lower triangle $T_m \subset S_m$** ($\rho_m^{(4)} = 0$) for $m = 6, 7, 8, 9, 10$!

Because four colors allow two disjoint color pairs $\{0, 1\}$ and $\{2, 3\}$ to absorb repeated horizontal/vertical differences as 2-colored $(a, a, b)$ triples without creating either monochromatic $(a, a, a)$ or rainbow $(a, b, c)$ $L$s, small-order 4-color triangle rainbow floors vanish identically ($\rho_m^{(4)} = 0$ for $m \le 10$), explaining structurally why unconditional 4-color bounds require the two-level binary-source Sidon/Golomb convolution bridge.

---

## 5. Self-contained reproduction & file manifest

Run the standalone standard-library verifier directly from this directory (writes zero files to the repository tree; compiles `rup_check.c` inside a temporary directory if a C99 compiler is present, or pass `--pure-python` for 100% pure-Python RUP verification):

```sh
python3 verify.py
```

| Path | Description |
| --- | --- |
| [`verify.py`](verify.py) | Standalone Python standard-library exact verifier (`int` + `fractions.Fraction`, zero research imports) |
| [`certificate.json.xz`](certificate.json.xz) | Compressed exact certificate: Golomb & binary spans, 18 inner + 38 exact-$B$ binary MCF Farkas bands, 201 inner thresholds, 570 binary rows, 3-segment ($S=39$, loss $\ge 99$) + 3 boundary 2-segment KD-tree outer DP tiers, and side $21{,}947{,}741$ margins |
| [`window_tables/`](window_tables/) | Vendored Carter–O'Bryant–Tao rational matrices (`G.txt`, `H.txt`, `p.txt` at commit `ff5b032fc3745140549777a96a9ec3ba7f8dd954`) + [`provenance.json`](window_tables/provenance.json) |
| [`rup_manifest.json`](rup_manifest.json), [`rup_proofs/`](rup_proofs/), [`rup_check.c`](rup_check.c) | Exact SAT witnesses and 11 compressed UNSAT RUP proofs certifying $e_2 \dots e_{16}$, with zero-dependency C99 forward RUP checker |
| [`zero_rainbow_witnesses.json`](zero_rainbow_witnesses.json) | Explicit proper 4-colorings of $S_6 \dots S_{10}$ with $\rho_m^{(4)} = 0$ in $T_m$ |
