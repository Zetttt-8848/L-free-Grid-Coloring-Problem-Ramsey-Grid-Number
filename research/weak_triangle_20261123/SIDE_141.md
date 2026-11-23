# Three-color bound at side 141

Every three-coloring of the full 141 by 141 square contains a monochromatic
directed equal-leg L. This uses the same weak embedding as the
[side-143 proof](README.md) and an exact, position-weighted certificate.

The additional ambient squares are both of side 18. The coordinates are the
lower-left point of the weak triangle in the square, and the step is one.

| Source | Offset | Rainbow lower bound | Catalog orientations | RUP groups |
| --- | --- | ---: | ---: | ---: |
| Order 12 | (0, 0) | 10 | 96,360 | 1,004 |
| Order 13 | (2, 0) | 13 | 2,928 | 31 |

The [PR 11 catalogs](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md)
list the complete proper triangle colorings at or below 9 and 12 rainbows,
respectively. Expand their geometric orientations and normalize colors.
For each group, the DIMACS formula asks for a proper square coloring
extending at least one listed triangle. Exactly-one clauses assign colors
and the directed-L clauses test all steps. Palette renaming in the full
square preserves properness, so the normalized groups cover every case.
A checked refutation for each group supplies both local lower bounds.

All 1,035 proof groups passed drat-trim and the C99 RUP checker during
generation. During review, all groups were matched to freshly reconstructed
formula hashes and the archived proof hashes. Both checkers were independently rerun on
all 31 order-13 groups and all 1,004 order-12 groups. The compressed
[manifest](data/side_141_patch_manifest.json.xz) records the coverage and
hashes. The replay and regeneration command below reconstructs every input.

The certificate charges a nonnegative weight to each allowed source
corner. Translation triples encode exact placements and expand the
antidiagonal reflection orbit. A local floor is the smaller of the
minimum score across remaining catalog profiles and the minimum
per-corner weight times the guaranteed number of rainbows outside the
catalog. The full square certifies which ambient-square floors apply.

For the upper score, nonnegative coefficients charge the line-identity
limits of the recorded translated and dilated subtriangles. Subtract the
charge from every covered corner and sum the largest positive remaining
incidences, up to the line-identity limit of the whole weak host. Each
subtriangle's affine embedding preserves the directed L with positive
equal steps. Both coordinate enumerations reproduce the scores below
using the same disclosed local facts.

| Quantity | Exact integer |
| --- | ---: |
| Weighted lower score | 99,946,393,340 |
| Weighted upper score | 99,905,858,109 |
| Difference | **40,535,231** |

The contradiction excludes every proper coloring of the full square.
The side-141 weights use the ten baseline square patches and the two
additional patches above. The empty catalog entries at orders 17 and 18
use the archived [boundary and interior refutations](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md#fourteen-through-eighteen-rainbows-at-orders-14-through-18).

## Reproduction

```sh
python3 global_certificate.py verify data/side_141_integer.json.xz
cc -O3 -std=c99 rup_check.c -o rup_check
python3 verify_new_patches.py --proof-dir /path/to/extra-proofs \
    --drat-trim /path/to/drat-trim --rup-check ./rup_check --jobs 8
```

The proof traces are indexed in the manifest. Pass `--generate-missing`
with python-sat installed to generate and check absent traces into the
chosen directory. Baseline replay is documented in the side-143 package.
The arithmetic check is independent of the floating-point search.

The stage-2 all-offset catalog and stage-3 side-140 target remain open.
