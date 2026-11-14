# Review of pull request 11

PR 11: "Certify directed-L upper bounds of 462 and 21,987,409", from
`TommyMaHaoKun:research/directed-l-boundary-20261115`, head
`b3941b3ad1d669bad7d3f849a28aebb486b178c2` (parent `f8126a895efc`), stacked on
`6630b5e27a07` (PR 10). Reviewed 2026-11-14. This is an in-repository review,
not an external referee report.

## Read in full

`README.md`, `FOUR_COLOR.md`, `verify_462.c`, `verify_four_rank.py`.
Inventoried only: `verify_bounds.py`, `verify_followups.py`, `verify_mixed.py`,
`completion_witnesses.json`, `mixed_461.rup.xz` (the fixed-word RUP refutation
at 461 was **not** re-checked: no DRAT checker was available).

## Mathematical check

Both proofs are correct as written; `../proof.md` Sections 2-5 restate them in
full. Points checked explicitly:

* Six-class lemma and its four-color analogue (twelve binary-source classes);
  the coordinate translation `(v,u) -> (v+d,u)` preserves Ls.
* Rank-neighbor inequality: the telescoping identity
  `sum_{j<=c} sum_i (b_{i+j}-b_i) = sum_{k<c} (c-k)(b_{s-k}-b_{k+1})` and the
  endpoint-block estimate, which holds also for overlapping blocks.
* Recursions: every rejected span stays rejected when the rank changes; the
  uniform cap uses `Q(L-1)`; the staggered profile `Q(L-h)+Q(L-h-1)` uses
  distinct minima of the two Golomb start classes.
* Outer staggering: rank-`j` class lies in `n-d-j` positions.
* Cauchy inequality with `k` colors and `a_d >= 0`.
* Three colors: the partial-word bound
  `min(k, 6, sum_c min(2,|P_c|), |union P_c|)` is a valid upper bound on `T_k`
  for every completion; the color-permutation multiplicities `3`, then `1`/`2`,
  then `1` partition all `3^b` labeled words.

One gap in PR 11's own verification, closed here: `verify_four_rank.py`
checks the closed form of `a_d` only at `d = 0`. `independent_r4_check.py`
checks it at twelve lags by literal summation; since `a_d` is a polynomial of
degree at most 5 in `d` on `0 <= d <= t`, this proves it for every lag.

## Execution (2026-11-14; gcc 16.2.0 MSYS2 UCRT64; Python 3.13.5)

| Check | Result |
|---|---|
| `verify_462.c` | small check 417/2187; 463: margin `+439,391,258`; 462 (36 layers): `words = 3^37`, `remaining = 0`, margin `+23,276,682`; 462 (23 layers): margin `+3`; 461 witness check passes. PASS |
| `verify_four_rank.py` | margin `2,727,455,661,705,377,936,113,840`. PASS |
| `independent_r4_check.py` (this directory; no shared code) | 608 rows proved, identical margin. PASS |
| `../prefix461/count_bad_words.c` at 462, 36 layers (independent enumerator, different symmetry reduction) | `bad_orbits = 0`. PASS |

SHA-256 of the PR 11 inputs: `four_capacity_runs.json`
`2a782fbd81e5c7013ae057a4604bd360d541d3f0e80bd08ef5a349b567a8bfd0`;
`verify_462.c` `b8146c17f7b3e9e1d2f9eaeae9a089dc6d13dc477094c0e24d5fa7718fbce1d7`;
`verify_four_rank.py` `e2a91b2438ad0263f59c917a6bc0b15ba9daff33528d780b5b563632ef09b696`.

## Verdict

`R_4 <= 21,987,409`: PROVED (elementary, self-contained).
`R_3 <= 462`: PROVED with the external inputs `G(24) >= 425`, `G(25) >= 480`.
Neither is merged; neither appears in the manuscript.
