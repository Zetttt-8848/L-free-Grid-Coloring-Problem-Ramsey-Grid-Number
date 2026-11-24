# Four-color upper bound at side 21,947,830

Every coloring of the full square of side **21,947,830** with at most four
colors contains a monochromatic directed equal-leg L. This lowers the
[side-21,947,834 Farkas bound](../r4_subadditive_farkas_20261124/README.md) by
**4**, the [side-21,947,855 disjoint-bin bound](../r4_disjoint_edge_bins_20261123/README.md)
by **25**, and the [round-3 bound][round3] of 21,947,865 by **35**.

Following `lgrid-research`, the Mechanisms, Technical Improvements, and
Numerical Bound are recorded separately below.

## 1. New mechanisms

### 1.1 Histogram-stratified rank-split Lagrangian outer matching deficit

Consider an isolated unit decrease in the nondecreasing binary-source capacity
profile $C(p)$ from $K + 1$ on $[p_0 + 1, p_0 + S]$ to $K$ on
$[p_0 - 11, p_0]$, centered at outer main-diagonal lag $D = n - p_0$. At lags
$d = D - s$ ($1 \le s \le S$), the distinct-minima baseline charges
$12 K + \min(s, 12)$ equal-colored endpoint pairs across the twelve ordered
color-completion classes $\mathcal C_{c, c'}$ ($c \ne c' \in \{0, 1, 2, 3\}$).
Because every class has properly binary-colored strict source and capacity at
most $K$ on any subinterval of $p_0$ positions, any class of size $K + 1$ at
lag $D - s$ must have its minimum mark $i = \min \mathcal C_{c, c'}$ in
$\{0, \dots, s - 1\}$, forcing the main-diagonal match
$z_i = z_{D - s + i} = c$, with at most three classes per original color $c$.
Putting $P_i = z_i$ and $T_k = z_{D - S + k}$ ($0 \le i, k < S$), the total
excess above $12 K$ across the $S$ shifts is at most

$$
M(P, T) = \sum_{s=1}^S \sum_{c=0}^3
  \min\bigl(3,\; \#\{0 \le i < s : P_i = T_{S - s + i} = c\}\bigr).
$$

Prior bounds ([`FOUR_COLOR_TWENTY.md`](../boundary_certificates_20261115/FOUR_COLOR_TWENTY.md))
split each match uniformly ($1/2 + 1/2$ between row $s$ and column
$k = S - s + i$), proving at least $41$ missing matches at $S = 20$. Any single
color-symmetric rank-split vector must simultaneously defend against
monochromatic words $P = 0^S$ and balanced words $P = (0123)^{S/4}$, capping
out at $57$ missing matches at $S = 26$.

To overcome this barrier, permute the palette $\{0, 1, 2, 3\}$ once for $P$ so
that the **final** color counts of $P$ at length $S$ satisfy

$$
0 \le n_0 \le n_1 \le n_2 \le n_3, \qquad n_0 + n_1 + n_2 + n_3 = S.
$$

For each fixed 4-partition $n^* = (n_0, n_1, n_2, n_3)$ of $S$, choose four
color-specific nondecreasing integer weight sequences
$0 \le b_{c, 0} \le b_{c, 1} \le \dots \le b_{c, n_c - 1} \le \Delta$
($c \in \{0, 1, 2, 3\}$). Let $r(i) = \#\{0 \le i' < i : P_{i'} = P_i\}$ be the
0-based occurrence rank of position $i$ in $P$ (which depends only on $i$ and
$P$), and split each selected match $(i, s)$ of color $c = P_i$ as
$\Delta = b_{c, r(i)} + (\Delta - b_{c, r(i)})$:

- **Row $s$ ($1 \le s \le S$)**: let $h_{s, c} = \#\{0 \le i < s : P_i = c\}$.
  The available positions of color $c$ in $\{0, \dots, s - 1\}$ have ranks
  $\{0, \dots, h_{s, c} - 1\}$. Since $b_{c, r}$ is nondecreasing in $r$ and at
  most three positions of color $c$ are selected, their row-weight sum is at
  most $\operatorname{rc}_c(h_{s, c}) = \sum_{r = \max(0, h_{s, c} - 3)}^{h_{s, c} - 1} b_{c, r}$.
- **Column $j - 1$ ($1 \le j \le S$)**: any match landing in column
  $j - 1 = S - s + i$ satisfies $s = S - j + 1 + i \le S$, hence $0 \le i < j$,
  with at most one row $s$ per $i$, and all matches in column $j - 1$ share the
  single color $c^* = T_{j - 1}$. Since $\Delta - b_{c^*, r} \ge 0$, their
  column-weight sum is at most
  $\operatorname{cc}_{c^*}(h_{j, c^*}) = \sum_{r = 0}^{h_{j, c^*} - 1} (\Delta - b_{c^*, r})
   \le \max_{0 \le c \le 3} \operatorname{cc}_c(h_{j, c})$.

Summing over $j = 1, \dots, S$ bounds $\Delta \cdot M(P, T)$ by the finite
four-count dynamic program over $0 \le h_c \le n_c$ ending at $n^*$. At
$S = 35$ and $\Delta = 12{,}000$, checking all **441** sorted 4-partitions of
$35$ proves $M(P, T) \le 291$ against the distinct-minima allowance
$\sum_{s=1}^{35} \min(s, 12) = 366$, establishing **at least 75 missing
matches** in every isolated 35-shift capacity drop block.

### 1.2 Joint contiguous multi-bin subadditive Farkas endpoint discrepancy

At an edge position $j B + t$ ($0 \le j < 150$, $0 \le t < B_0$) of a dilated
rational window row, bins $0, \dots, j - 1$ occupy adjacent disjoint intervals
$I_0, \dots, I_{j-1}$ of length $B \le B_1$ and bin $j$ occupies the adjacent
partial interval $I_j$ of length $k = t + 1 \le B_0$. For any subinterval
$[a, b] \subseteq \{0, \dots, j\}$, the union $\bigcup_{r=a}^b I_r$ is a single
contiguous interval of length at most $(b - a + 1) B_1$ when $b < j$, and at
most $(j - a) B_1 + k$ when $b = j$. Consequently, any nonnegative rational
multipliers $y_{a, b} \ge 0$ ($0 \le a \le b \le j$) satisfying the covering
inequalities

$$
\sum_{a \le r \le b} y_{a, b} \ge \bar G_r \qquad (0 \le r \le j)
$$

certify the exact upper bound

$$
\sum_{r=0}^j \bar G_r |A \cap I_r|
  \le \sum_{0 \le a \le b < j} y_{a, b} \operatorname{cap}\bigl((b - a + 1) B_1\bigr)
    + \sum_{0 \le a \le j} y_{a, j} \operatorname{cap}\bigl((j - a) B_1 + k\bigr),
$$

which strictly improves upon bounding prior bins individually by
$j \cdot \operatorname{cap}(B_1)$.

## 2. Technical improvements

1. **Both inner Golomb and binary endpoint discrepancies upgraded**: applying
   the joint Farkas dual across all 12 oriented rows and 150 edge bins, together
   with Golomb lower spans and uniform rank-neighbor binary spans extended
   through $18{,}000$ marks (span $285{,}845$, seeded at $C(20) = 13$ via
   [`verify_c20.py`](../r4_disjoint_edge_bins_20261123/verify_c20.py)), raises
   the inner Golomb discrepancy from $52$ to
   $D_{\text{inn}} = 28{,}062{,}948{,}563 / 500{,}000{,}000 = 56.125897126$ and
   the binary-source discrepancy from $224.726791146$ to
   $D_{\text{bin}} = 115{,}221{,}013{,}939 / 500{,}000{,}000 = 230.442027878$.
2. **Inner thresholds and per-row block widths**: all 201 Golomb thresholds
   ($4{,}600 \le k \le 4{,}800$) are recomputed with $D_{\text{inn}}$, and each
   of the 566 binary capacity witnesses optimizes its integer block width
   $B \in [1720, 1820]$.
3. **Multi-scale disjoint outer blocks**: 561 interior drop blocks use the
   35-shift stratified deficit (75 missing matches each) and the single
   near-origin boundary block uses the 20-shift deficit (41 missing matches),
   for 562 pairwise disjoint blocks in total.

## 3. Exact integer verification

The standalone checker [`verify.py`](verify.py) uses only the Python standard
library and imports no research modules. At side **21,947,830**, the exact
integer margin is

$$
+539{,}056{,}291{,}270{,}052{,}110{,}977{,}393{,}673{,}395{,}176{,}886{,}945{,}095{,}280 > 0,
$$

while at side 21,947,829 the same certificate has negative margin
$-443{,}088{,}924{,}391{,}375{,}103{,}797{,}412{,}570{,}614{,}119{,}901{,}020{,}127{,}344$.

## Reproduction

```sh
python3 ../r4_disjoint_edge_bins_20261123/verify_c20.py
python3 verify.py --window /path/to/sidon-error/asymptotic
```

Passing `--window` checks the SHA-256 digests of the pinned upstream window
matrices (`G.txt`, `H.txt`, `p.txt` at revision
`ff5b032fc3745140549777a96a9ec3ba7f8dd954`), recomputes all 200 rational
correlations, the table excess $\alpha$, all 401 coarse coverage alignments, and
both Farkas discrepancies directly from the source tables. Running `python3
verify.py` without `--window` still checks all span recursions, inner
thresholds, 566 binary interval witnesses, all 441 stratified outer DP
certificates, and the final integer contradiction in ~4 seconds.

[round3]: https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/tree/14647e607c2525b0cd12081b03899827d306a030/research/r4_local_capacity_round3_20261114
