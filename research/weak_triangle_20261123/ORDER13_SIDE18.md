# Low-rainbow order-13 triangles in the 18-square

Of the 28 placements up to antidiagonal reflection, 26 exclude every
proper triangle coloring with at most twelve rainbows. The placement at
(3, 2) admits exactly three palette-normalized oriented triangle words,
each with twelve rainbows. The corner placement at (0, 6) remains open.

The [baseline proof](README.md) excludes offsets (0, 0), (3, 3) and
(6, 0). The [placement manifest](data/order13_side18_profiles.json.xz)
covers the remaining 23 excluded offsets and the exact result at (3, 2).
Use coordinates and reflection representatives from [the placement
table](PLACEMENTS.md).

Expand and sort the 2,928 palette-normalized orientations of the complete
[order-13 catalog](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md).
At each offset, split this ordered list into consecutive blocks of 96.
At (3, 2), remove the three witnessed words from their respective blocks
before forming the refutations. The manifest gives a complete square
coloring for each surviving word. It records the exact formula and proof
digests for the remaining 744 blocks, covering 70,269 negative
word-placement pairs. Every block has a checked RUP refutation.
The original placement ZIP has SHA-256
`6c15ab8d1835bc05aeabb0bff35796a122034f176747a14c0feaf484b4abba21`.

The three survivors have distinct rainbow profiles. The following
multisets give the zero-based indices in the sorted list of corner keys
`(step, sorted gaps)`. Each repeated index counts a different corner.

| Sorted word index | Rainbow corner-key indices |
| ---: | --- |
| 2103 | 1, 8, 11, 20, 21, 22, 24, 24, 24, 27, 40, 41 |
| 2300 | 3, 8, 8, 20, 20, 21, 21, 22, 23, 23, 24, 41 |
| 2337 | 3, 8, 8, 20, 21, 21, 22, 23, 23, 24, 41, 59 |

Consequently a nonnegative position-weighted lower bound at this placement
can take the minimum of the three literal profile scores and the sum of
the thirteen smallest physical corner weights. The latter covers all
colorings beyond the catalog cutoff.

The first command reconstructs all formula hashes and checks the three
literal square witnesses. To check the proof bytes, extract the placement
ZIP and run the second command. Add `--generate-missing` with python-sat
installed to produce missing refutations from the catalog.

```sh
python3 verify_order13_placements.py --jobs 4
python3 verify_order13_placements.py --proof-dir /path/to/placement-proofs \
    --drat-trim /path/to/drat-trim --rup-check ./rup_check --jobs 4
```
