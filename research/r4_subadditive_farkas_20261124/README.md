# Four-color upper bound of 21,947,834 via subadditive Farkas duality and rank-weighted outer matching

Every four-coloring of the full square of side **21,947,834** contains a
monochromatic directed equal-leg L `{(x, y), (x + d, y), (x + d, y + d)}`
with `d > 0`. This improves the previous verified bound of `21,947,855`
([`r4_disjoint_edge_bins_20261123`](../r4_disjoint_edge_bins_20261123/README.md))
by **21** (and round 3's `21,947,865` by **31**), using two new elementary
combinatorial counting arguments and zero additional SAT searches beyond the
already verified finite binary-source capacity `C(20) = 13` (`e_14 >= 20`).

## 1. Subadditive contiguous multi-bin Farkas dual on endpoint discrepancies

In the discrete convolution `S_i = 1_A * w_i` at output offset `j * B + t`
(`0 <= t < B`) from either end of the interval, the marks seen by bins
`0, 1, ..., j - 1` occupy adjacent, pairwise disjoint contiguous intervals
`I_0, I_1, ..., I_{j-1}` of length `B <= B_1`, and bin `j` sees the adjacent
partial interval `I_j` of length `k = t + 1 <= B_0`.

Previous certificates bounded each prior bin separately by `|A cap I_r| <= Q(B_1)`.
Because `I_a union ... union I_b` is itself a contiguous interval of length
`(b - a + 1) * B <= (b - a + 1) * B_1`, any nonnegative rational multipliers
`y_{a,b} >= 0` (`0 <= a <= b < j`) satisfying

```text
sum_{a <= r <= b} y_{a,b} >= g_r    for every 0 <= r < j
```

certify by elementary linear combination (Farkas duality) that

```text
sum_{r=0}^{j-1} g_r * |A cap I_r| <= sum_{0 <= a <= b < j} y_{a,b} * Q((b - a + 1) * B_1).
```

Combining this with the full-span bound `max_{0 <= r <= j} g_r * Q(j * B_1 + k)`
and extending the uniform rank-neighbor binary-source span recursion through
size `18,000` (covering span `285,845 > 150 * 1820`), all 150 disjoint edge
bins at both ends of all six pinned Carter-O'Bryant-Tao windows yield exact
rational discrepancy lower bounds for **both** levels of the proof:

| Family | Previous certified `D` | New Farkas certified `D` | Gain |
| --- | ---: | ---: | ---: |
| Ordinary Golomb sets (`B in [15000, 16600]`) | `52` | `28062948563 / 500000000` (`56.125897126`) | `+4.125897` |
| Proper binary strict sources (`B in [1720, 1820]`) | `224.726791146` | `115221013939 / 500000000` (`230.442027878`) | `+5.715237` |

The stronger inner discrepancy shifts all 201 certified Golomb thresholds
(`4600 <= k <= 4800`) upward by 4 to 5 positions. Together with per-row
block-width optimization `B in [1720, 1820]`, the 566 binary-source interval
witnesses advance by 5 to 6 positions each, already reducing the four-color
bound from `21,947,855` to `21,947,838` under the existing 20-shift outer
recurrence.

## 2. Twenty-six-shift rank-weighted Lagrangian outer matching recurrence

At an isolated capacity drop from `K + 1` to `K` separated by at least `S = 26`
preceding shifts and `12` subsequent shifts, the ordinary distinct-minima
allowance over `d = D - s` (`1 <= s <= 26`) is `sum_{s=1}^{26} min(s, 12) = 246`,
while the true count above `12 K` is bounded by `sum_{s=1}^{26} M_s(P, T)` for
two length-26 four-color words `P, T`, where each row `s` caps every color `c`
at `3` matches.

Previously, [`FOUR_COLOR_TWENTY.md`](../boundary_certificates_20261115/FOUR_COLOR_TWENTY.md)
split every match evenly `(1/2, 1/2)` between rows and columns at `S = 20`,
proving at least `41` missing matches per block. Instead, fix any nondecreasing
rational weights `0 <= beta_1 <= beta_2 <= ... <= beta_S <= 1` indexed by the
occurrence rank `r(i)` of color `P_i` within the prefix `P[0..i]`. Splitting
each counted match `(s, i)` as `1 = beta_{r(i)} + (1 - beta_{r(i)})` assigns:

- to row `s` and color `c` (at most 3 matches): at most the sum of the
  `min(3, h_{s,c})` largest weights among `{beta_1, ..., beta_{h_{s,c}}}`;
- to column `k` of `T` (which has one color `c = T_k` and receives only
  `i <= k`): at most `max_c sum_{r=1}^{h_{k+1,c}} (1 - beta_r)`.

Both terms depend only on the unordered four-color prefix histogram `h_j(P)` of
length `j`, preserving the exact four-tuple dynamic program. With denominator
`120` and rank weights `[26, 34, 46, 58, 70, 84, 86, 104, 115, 120, ...]` at
`S = 26`, the exact integer recurrence bounds `120 * sum_{s=1}^{26} M_s(P, T)`
by `22,774`, hence `sum M_s <= floor(22774 / 120) = 189`, proving at least
`246 - 189 = 57` missing matches in every one of the 562 disjoint complete
blocks.

Combining both methods gives the exact positive outer margin

```text
+143,415,804,935,709,339,398,828,685,820,858,713,008,448,240
```

at side **21,947,834**, while the same certificate gives a negative margin
(`-839,829,696,770,912,013,587,014,085,554,694,602,065,439,344`) at side
`21,947,833`.

## Reproduction

Run the standalone Python standard-library verifier against the pinned upstream
`asymptotic` directory (`ff5b032fc3745140549777a96a9ec3ba7f8dd954`):

```sh
python3 ../r4_disjoint_edge_bins_20261123/verify_c20.py
python3 verify.py --window /path/to/asymptotic
```
