# Three-color bound at side 140

Every three-coloring of the full 140-by-140 square contains a monochromatic
directed equal-leg L. Using the weak-triangle bijection
$W_{140} \cong T_{141}$ from the [side-143 proof](README.md), this establishes

$$
R_3(\mathcal L) \le 140.
$$

## Certified local inputs beyond side 141

In addition to the ten baseline square patches and the two side-18 patches
from the [side-141 proof](SIDE_141.md), the [side-140 certificate](data/side_140_integer.json.xz)
uses two further RUP-verified ambient-square exclusions together with the
boundary-weighted local inequalities developed in this package:

| Source | Square side | Step | Offset | Rainbow lower bound | Oriented words | RUP groups |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| Order 11 | 18 | 1 | `(0, 0)` | 6 | 16,452 | 172 |
| Order 13 | 23 | 2 | `(0, 0)` | 13 | 2,928 | 31 |

Notice that a weak $T_{13}$ at dilation $d$ spans `11 * d` steps on each axis,
and at any even dilation `d = 2 * u` a stride-2 square of side 23 at `(0, 0)`
spans `(23 - 1) * u = 22 * u = 11 * d`, matching the bounding box of $T_{13}$
itself. Consequently `(13, 12, 23, 0, 0, 2)` upgrades **every** copy of
$T_{13}$ at every even dilation `d in {2, 4, 6, 8, 10, 12}` across the entire
host square to at least 13 rainbows, with zero boundary loss.

All 203 new RUP groups passed both `drat-trim` and the standalone C99 checker
`rup_check`; their reconstructed formula and proof SHA-256 digests are recorded
in [`data/side_140_patch_manifest.json.xz`](data/side_140_patch_manifest.json.xz).

On the local source side, the certificate activates:

1. The three embedded-subtriangle weighted inequalities on $T_{14}$ from
   [the sharp order-14 extension table](ORDER14_EXTENSIONS.md) (`20 r_14 + 3 sum r_11 >= 490`,
   `24 r_14 + 5 sum r_12 >= 636`, and `6 r_14 + 5 sum r_13 >= 279`).
2. The boundary-layer weighted inequalities `2 r + s_1 >= 2 m + 2` and
   `3 r - d_2 - 2 d_3 >= 3 m` across $14 \le m \le 18$ (plus
   `r + s_1 + d_2 + d_3 >= m + 2` at $m \in \{17, 18\}$) from
   [the outer-side structure proof](BOUNDARY_LAYERS.md).
3. The rounded unconditional and seven-step-clearance floors at orders 20 and 21
   from [`data/local_boundary_packings.json`](data/local_boundary_packings.json),
   which `global_certificate.py` re-verifies directly from physical incidences
   on every run (and explicitly checks that the side-18 `(0, 0)` patches at
   orders 12 and 13 required by the clearance condition are present in the
   certificate's patch list).

## Exact integer contradiction

On the upper side, nonnegative integer coefficients charge the line-identity
ceilings $U_m = \binom{m}{2} - (m - 1) + \lfloor (m - 1)/3 \rfloor$ of
unit-step and dilated subtriangles, and sum the largest $U_{141} = 9{,}776$
remaining positive corner incidences on $W_{140} \cong T_{141}$. Both
independent coordinate verifiers in [`global_certificate.py`](global_certificate.py)
(direct physical square coordinates in `{0, ..., 139}^2` and barycentric
coordinates on $T_{141}$) produce the exact same integers:

| Quantity | Exact integer |
| --- | ---: |
| Weighted lower score | 99,967,973,695 |
| Weighted upper score | 99,629,279,874 |
| Difference | **338,693,821** |

(Including the remaining 24 excluded side-18 $T_{13}$ offsets and `(12, 9, 18, 0, 1, 1)`
increases the lower score to `99,999,848,337` and the positive difference to
`370,568,463`; the minimal four-patch certificate above requires only the
two side-141 patches plus the two new patches in `side_140_patches.json`.)

## Reproduction

```sh
python3 global_certificate.py verify data/side_140_integer.json.xz
python3 verify_new_patches.py --collection side-140
cc -O3 -std=c99 rup_check.c -o rup_check
python3 verify_new_patches.py --collection side-140 --proof-dir /path/to/extra-proofs \
    --drat-trim /path/to/drat-trim --rup-check ./rup_check --jobs 8
```
