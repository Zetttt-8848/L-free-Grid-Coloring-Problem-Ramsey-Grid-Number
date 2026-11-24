# Low-rainbow order-13 triangles in the 16-, 17-, and 18-squares

## Complete classification in the 18-square

Of the 28 placements up to antidiagonal reflection, **27 exclude every
proper triangle coloring with at most twelve rainbows**, and the single
remaining placement at `(3, 2)` admits **exactly three** palette-normalized
oriented triangle words, each with twelve rainbows. No placement remains open.

The [baseline proof](README.md) excludes offsets `(0, 0)`, `(3, 3)`, and
`(6, 0)`. The [placement manifest](data/order13_side18_profiles.json.xz)
covers all remaining 24 excluded offsets (including the corner offset
`(0, 6)`) and the exact three-survivor result at `(3, 2)`. Use coordinates
and reflection representatives from [the placement table](PLACEMENTS.md).

Expand and sort the 2,928 palette-normalized orientations of the complete
[order-13 catalog](../boundary_certificates_20261115/LOCAL_RAINBOW_MINIMA.md).
At each offset, split this ordered list into consecutive blocks of 96.
At `(3, 2)`, remove the three witnessed words from their respective blocks
before forming the refutations. The manifest gives a complete square
coloring for each surviving word and records the exact formula and proof
digests for all **775** blocks, covering **73,197** negative
word-placement pairs. Every block has a checked RUP refutation.
The complete placement ZIP `side-18-T13-placement-proofs.zip` has SHA-256
`d263369a7d9c65d00f8dd0f841c9b9258dca5c8424d3a59b5543828d9b0bf03d`.

The three survivors at `(3, 2)` have distinct rainbow profiles. The following
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

## Complete survivor lists in the 16- and 17-squares

Every reflection orbit in the 16-square (15 orbits) and 17-square (21 orbits)
has at least one proper extension with at most twelve rainbows, and every
such orbit is now completely classified into witnessed survivors and RUP-refuted
complements:

- **17-square** ([`data/order13_side17_profiles.json.xz`](data/order13_side17_profiles.json.xz)):
  2,925 surviving `(offset, word)` pairs (each stored with an explicit proper
  17-by-17 witness) and 651 RUP refutation blocks covering the remaining
  58,563 excluded pairs. Several boundary offsets leave very few surviving
  orientations out of 2,928, notably `(5, 0)` with **8** survivors (2 distinct
  rainbow profiles), `(4, 0)` with **14**, `(0, 2)` with **36**, `(1, 4)` with
  **44**, `(0, 3)` with **45**, and `(0, 0)` with **49**.
- **16-square** ([`data/order13_side16_profiles.json.xz`](data/order13_side16_profiles.json.xz)):
  23,417 surviving `(offset, word)` pairs (each stored with an explicit proper
  16-by-16 witness) and 458 RUP refutation blocks covering the remaining
  20,503 excluded pairs, with survivor counts ranging from **814** at `(4, 0)`
  to **2,596** at `(0, 4)`.

## Reproduction

The commands below check every literal square witness and reconstruct all
DIMACS formula hashes across all three square sizes. Supply `--proof-dir`,
`--drat-trim`, and `--rup-check` to replay the archived RUP traces directly,
or add `--generate-missing` with `python-sat` installed to regenerate traces.

```sh
python3 verify_order13_placements.py --side 18 --jobs 4
python3 verify_order13_placements.py --side 17 --jobs 4
python3 verify_order13_placements.py --side 16 --jobs 4
python3 verify_order13_placements.py --side 18 --proof-dir /path/to/placement-proofs \
    --drat-trim /path/to/drat-trim --rup-check ./rup_check --jobs 4
```
