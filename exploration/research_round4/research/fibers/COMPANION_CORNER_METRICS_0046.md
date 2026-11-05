# Companion-corner metrics from saved strict witnesses (0046)

For an additive parallelogram
\[
u, u+d, u+h, u+d+h\qquad(0<d<h),
\]
the two companion corners share outer cell \((u+d+h,u)\). Each is marked
**F** when its equal-offset endpoint colors agree and **M** otherwise; the
JSON reports the resulting FF/FM/MM inventory. An AP3
\(u,u+d,u+2d\) contributes one analogous forcing or mixed corner.

“Forcing endpoint triples” means the actual forcing corners, grouped by the
color and size of their outer-anchor cell class. The JSON also records each
anchor-color class's forcing-load histogram and the count of pairs of
forcing triples sharing an outer anchor.

The inputs are exactly three saved symbolic constructions:

- the 2-dissociated three-cube rule in
  **THREE_CUBE_MIXED_CORNER_MINIMUM_0046.md**;
- the separated four-cube tables in
  **FOUR_CUBE_NONLINEAR_CONSTRUCTION_0045.md**;
- the weight-two layer rule in **WEIGHT_TWO_LAYER.md**, evaluated at its
  stated powers-of-five family with \(r=5\).

No solver assignment was read, no new coloring was searched, and the script
does not test properness. This is a finite inventory for designing possible
global identities, not a universal companion-block assertion.

## Recorded inventory

| witness | corners (F/M) | FF / FM / MM | AP3 F/M |
|---|---:|---:|---:|
| separated three-cube | 24 (15 / 9) | 6 / 3 / 3 | 0 / 0 |
| separated four-cube | 200 (75 / 125) | 15 / 45 / 40 | 0 / 0 |
| weight-two layer, \(r=5\) | 30 (30 / 0) | 15 / 0 / 0 | 0 / 0 |

Forcing endpoint triples grouped by outer color are recorded in full in the
adjacent JSON. Their total counts are respectively \((9,6)\), \((37,38)\),
and \((0,30)\) for outer colors \((0,1)\). The corresponding numbers of
pairs sharing an outer anchor are \((10,3)\), \((39,40)\), and \((0,35)\).

