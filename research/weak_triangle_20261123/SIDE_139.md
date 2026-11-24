# Full-square shifted-triangle bound at side 139

Every three-coloring of the full 139-by-139 square contains a monochromatic
directed equal-leg L. This establishes

$$
R_3(\mathcal L) \le 139.
$$

Following `lgrid-research`, the New Mechanism, Certified Local Inputs, and
Exact Integer Contradiction are reported separately below.

## 1. New mechanism: full-square cross-diagonal shifted-triangle coupling

The [side-143](README.md), [side-141](SIDE_141.md), and [side-140](SIDE_140.md)
certificates restrict every source placement and every upper-bound subtriangle
ceiling to the lower weak triangle
$W_N = \{(x, y) \in \{0, \dots, N - 1\}^2 : y \le x\} \cong T_{N + 1}$. Inside
$W_N$, corners near the main diagonal $y = x$ lie on an artificial boundary of
the triangle domain and receive roughly half as many subtriangle incidences as
interior corners. Even after upgrading $r_{14} \ge 15$ and adding the stride-2
order-12 exclusion below, the $W_{139}$-restricted dual LP has lower bound
`1.001936 > 1`.

In the full square $S_N = \{0, \dots, N - 1\}^2$, however, the main diagonal
$y = x$ is an interior line rather than a boundary. For **any** integer shift
$(x_0, y_0)$ with $0 \le x_0, y_0 \le N - 1 - d(m - 2)$—including cross-diagonal
placements with $y_0 > x_0$—the affine map

$$
(i, j) \longmapsto (x_0 + d i,\; y_0 + d j) \qquad (0 \le j \le i \le m - 2)
$$

embeds a dilated weak triangle $W_{m - 1}(x_0, y_0, d) \cong T_m$ inside $S_N$
and preserves every directed equal-leg L $((x, y), (x + h, y), (x + h, y + h))$
with positive step $h = d j_0 > 0$. Consequently:

1. **Cross-diagonal lower-bound rules**: every certified source inequality on
   $T_m$ (catalog profiles, ambient-square exclusions, boundary-layer rays, and
   clearance-upgraded packings) applies verbatim to $W_{m - 1}(x_0, y_0, d)$
   across $y_0 > x_0$, charging corners on both sides of $y = x$.
2. **Cross-diagonal upper-bound caps**: for any stride $s \ge 1$, order
   $m_{\text{sub}} \ge 3$, and $(X_0, Y_0)$ with
   $0 \le X_0, Y_0 \le N - 1 - s(m_{\text{sub}} - 2)$ (including $Y_0 > X_0$),
   the pullback coloring on $W_{m_{\text{sub}} - 1}(X_0, Y_0, s) \cong T_{m_{\text{sub}}}$
   is proper and therefore contains at most
   $U_{m_{\text{sub}}} = \binom{m_{\text{sub}}}{2} - (m_{\text{sub}} - 1) + \lfloor (m_{\text{sub}} - 1)/3 \rfloor$
   rainbow Ls by the line identity.
3. **Full-square residual decomposition**: after subtracting nonnegative cap
   multiples from the accumulated corner weights $I(X, Y, h)$ across all
   directed Ls of $S_N$, every L with $Y \le X$ has all three vertices inside
   $W_N \cong T_{N + 1}$, so at most $U_{N + 1}$ of them can be rainbow, while
   every L with $Y > X$ has indicator in $\{0, 1\}$ and contributes at most
   $\max(0, \text{res}(X, Y, h))$.

Allowing both lower rules and upper line-identity caps to straddle the main
diagonal drops the side-139 dual lower bound from `1.001936` on $W_{139}$ to
below `0.995` on $S_{139}$.

## 2. Certified local inputs beyond side 140

In addition to the patches from [side 140](SIDE_140.md), the [order-13 side-18
exclusions](ORDER13_SIDE18.md), and [`(12, 9, 18, 0, 1, 1)`](PLACEMENTS.md), the
[side-139 certificate](data/side_139_integer.json.xz) uses:

1. **Exclusion of fourteen rainbows at order 14 ($r_{14} \ge 15$)**: the
   20 RUP-verified two- and three-side coarse-subtriangle refutations in
   [`ORDER14_MIN15.md`](ORDER14_MIN15.md) ([`data/order14_min15.json`](data/order14_min15.json))
   raise the unconditional minima on $T_{14}, \dots, T_{18}$ to
   `15, 16, 17, 18, 19`, strengthen the embedded-subtriangle rays at orders 14
   and 15 and the multi-side ray $3 r_m - d_2 - 2 d_3 \ge 3 m + 1$ ($15 \le m \le 18$),
   and raise the Chvatal-Gomory local bounds in
   [`data/local_boundary_packings_15.json`](data/local_boundary_packings_15.json)
   (in particular $r_{21} \ge 29$ and $r_{24} \ge 44$ unconditionally).
2. **Stride-2 order-12 exclusion `(12, 6, 21, 0, 0, 2)`**: all 204
   palette-normalized oriented words of $T_{12}$ with at most six rainbows are
   excluded in 34 consecutive six-word RUP groups inside the 21-square at
   stride 2 (`(21 - 1) * u = 10 * d` at $d = 2 u$, upgrading every even-dilation
   copy of $T_{12}$ across $S_{139}$ to at least seven rainbows with zero
   boundary loss). All 34 groups passed both `drat-trim` and `rup_check` and are
   recorded in [`data/stride2_order12_21_manifest.json.xz`](data/stride2_order12_21_manifest.json.xz).

## 3. Exact integer contradiction

Both independent verifiers in [`verify_full_square.py`](verify_full_square.py)
— Verifier 1 (explicit physical square array on $S_{139} = \{0, \dots, 138\}^2$)
and Verifier 2 (signed-gap antidiagonal-orbit coordinates) — re-verify
`local_boundary_packings_15.json` from physical incidences and produce the
exact same integers:

| Quantity | Exact integer |
| --- | ---: |
| Weighted lower score | 99,999,938,352 |
| Weighted upper score | 99,615,568,291 |
| Difference | **384,370,061** |

## Reproduction

```sh
python3 verify_full_square.py verify data/side_139_integer.json.xz
python3 verify_order14_min15.py --jobs 4
python3 verify_local_packing.py
python3 verify_new_patches.py --collection stride2-order12
```
