# Upper-bound research, 2026-11-14

Branch `claude/upper-bounds-20261114`, based on
`origin/claude/upper-bound-skills-20261113` (`6630b5e27a07`, PR 10), which
contains the research checkpoint `dc1cbe6daf7d`. Exploratory work is marked as
such below; `proof.md` is the self-contained write-up.

## Results

| Item | Status | Where |
|---|---|---|
| `R_4 <= 21,987,409` (PR 11, head `b3941b3ad1d6`) | PROVED, elementary; finite certificate re-executed by PR 11's verifier **and** by an independent re-implementation (identical margin `2,727,455,661,705,377,936,113,840`) | `proof.md` Section 4; `pr11_review/` |
| `R_3 <= 462` (PR 11) | PROVED with external inputs `G(24) >= 425`, `G(25) >= 480`; C certificate re-executed (all `3^37` words, margin `+23,276,682`); an independent enumerator also finds no surviving word | `proof.md` Section 5; `pr11_review/` |
| Word-adaptive kernels for the prefix inequality (any `w >= 0`) | PROVED as a necessary condition (Prop. 6.1); **numerically insufficient** at side 461 | `proof.md` 6.1; `prefix461/adaptive_kernel.py` |
| Window relaxation (any diagonal window's triangle must be colorable) | PROVED as a necessary condition (Prop. 6.2); **exploratory** solver data only | `proof.md` 6.2; `prefix461/` |
| `R_3 <= 461` | UNDECIDED | `proof.md` Section 6 |

Working interval after this checkpoint (none of it merged to `main`):
`21 <= R_3 <= 462` (external OGR inputs), `21 <= R_4 <= 21,987,409`.

## Negative findings worth keeping (side 461, `b = 36`, kernel `i(86-i)`)

* At least **62,547** color-permutation classes of 36-letter prefixes satisfy
  `G_0 + 3D <= 0` (enumeration stopped early; list in
  `prefix461/data/bad_words_461_partial.txt.xz`, SHA-256 of the decompressed
  text `c9dac2fad1507ada2242ea0f6c615be27b5660721bbc608938566c0b2f08b4bb`).
* Optimizing the kernel per word excludes only about 7% of sampled bad words
  (20 of 300, exact integer check); PR 11's witness
  `122120100110100020212021121202210012` survives every kernel found
  (numerical maximum negative). The fixed-diagonal prefix family is close to
  exhausted at 461.
* Local triangle refutations: the 36-triangle of two bad words is UNSAT for
  CaDiCaL (5.5 s and 16 s; proofs **not** checked). Short windows rarely
  suffice (3 of 26 bad words have an UNSAT 16-window).

Session 1 (same date, `session1_notes.md`): the partition relaxation `P_3(n)`
is satisfiable for `n <= 62` (witnesses decoded and checked, `runs/`), so it
cannot give `R_3 <= 62`; exact small binary-source capacities `f_2(L)`
(UNSAT side not certified).

## Reproduce

```sh
cd prefix461
gcc -std=c99 -O3 count_bad_words.c -o count_bad_words
./count_bad_words 462 36 85 0 /dev/null      # bad_orbits=0
./count_bad_words 461 35 85 100000 out.txt   # long; stop at will
python -I adaptive_kernel.py                  # library; see proof.md 6.1
python -I ../pr11_review/independent_r4_check.py path/to/four_capacity_runs.json
```

`four_capacity_runs.json` and `verify_462.c` are PR 11 files (not copied here);
fetch with `git fetch origin pull/11/head` and use
`research/boundary_certificates_20261115/`.

## Next research actions

1. Certify triangle refutations quickly (a C RUP checker or drat-trim), then
   interleave window refutation into the prefix branch and bound at depth
   about 2m, m = 18-20, with a cache of certified infeasible windows.
2. Four colors: the dominant loss is the binary fiber cap
   `Q(L-h)+Q(L-h-1) ~ 2 sqrt(L)` at spans near `2.2 * 10^7`; the doubled Golomb
   construction (round 4) shows the true cap is at least about `sqrt(2L)`.
   A proved cap `c sqrt(L)` with `c < 2` would lower the bound by a factor of
   about `(c/2)^2`.
