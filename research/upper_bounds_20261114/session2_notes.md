# Notes, run upper_bounds_20261114 (session 2, 2026-11-14)

Run files (problem.md, notes.md, proof.md) live in the primary working
directory as the run directory. The tracked research copy is made on branch
`claude/upper-bounds-20261114` (worktree `C:\Users\ZhuanZ\Desktop\lgrid-ub-20261114`),
whose `research/upper_bounds_20261114/` already holds an earlier session's
notes (problem text differs: an earlier, longer prompt). Those earlier
results are reused, not overwritten.

## 0. Refresh (2026-11-14)

- `refresh_state.py --fetch`: HEAD of primary tree is 080822b (old, 27
  uncommitted entries of someone else's work; untouched). Pinned checkpoint
  `dc1cbe6daf7d`. New: `origin/claude/upper-bound-skills-20261113` = 6630b5e (PR 10).
- New since snapshot: **PR 11** (fork TommyMaHaoKun:research/directed-l-boundary-20261115),
  head `b3941b3ad1d669bad7d3f849a28aebb486b178c2`, parent f8126a8, stacked on 6630b5e.
  Claims: R_3 <= 462 (external inputs G(24)>=425, G(25)>=480; exhaustive
  3^37-word prefix certificate, C checker) and R_4 <= 21,987,409 (self-contained,
  recursive span bounds, Python verifier, 608 rows).
- PRs 1-7 open (codex research line), 8-9 merged (translations), 10 open (skills), 11 open.
- Earlier session today (same branch, untracked): partition relaxation P_3(n)
  SAT for n <= 60 (cannot give R_3 <= 60); f_2(10)=9, f_2(15)=11, f_2(19)=13,
  f_2(24)=15 (UNSAT not certified).
- Round 4 (exploration/research_round4) already studied two-color weak
  triangles heavily: doubled Golomb construction S={2a,2a+1} (w_2 >= ~sqrt(2L)),
  two-Golomb energy theorem E(S) <= 6n^2-5n, cube capacities. No bound improvement.

## 1. Plan

Step A. Independently verify PR 11 (read proofs, read checkers, rerun).
Step B. Research cycle on a new mechanism (to be chosen after A; candidates in
section 3).

## 2. Step A result: PR 11 review (head b3941b3)

Read in full: README.md, FOUR_COLOR.md, verify_462.c, verify_four_rank.py.
Proof checks (my reading):
- R_3 <= 462: six-class Golomb lemma; 24-mark class min in first k=b-d starts;
  per color at most min(2, m_c(k)) such classes; 3-color Cauchy with
  w_i=i(86-i); partial-word bound T^ = min(k,6,sum min(2,|P_c|),|union P_c|) is a
  valid upper bound on T_k for all completions; color-permutation quotient
  multiplicities 3, then 1/2, then 3 are correct; leaves disjoint and counted.
  All sound. External inputs G(24)>=425, G(25)>=480 (OGR-24/25).
- R_4 <= 21,987,409: rank-neighbor inequality (telescoping identity checked),
  Golomb lower spans g_s, binary-source lower spans e_s with uniform cap
  2Q(L-1), staggered profile Q(L-h)+Q(L-h-1), 12 staggered outer classes,
  4-color Cauchy.  All sound; self-contained (no external input).
Executed 2026-11-14 (gcc 16.2.0 MSYS2, Python 3.13.5):
- verify_462.c: small check 417/2187; 463 margin +439391258; 462 (36 layers)
  remaining=0 margin +23276682, words=3^37; 462 (23 layers) margin +3. PASS.
- verify_four_rank.py: margin 2,727,455,661,705,377,936,113,840. PASS.
- my independent_r4_check.py (no shared code; direct loops; a_d by literal
  sums + degree-5 interpolation): identical margin. PASS.
Note: the closed form for a_d was checked by PR 11 only at d=0; my check
covers all d (polynomial identity through 12 literal values).
SHA-256: four_capacity_runs.json 2a782fbd..., verify_462.c b8146c17...,
verify_four_rank.py e2a91b24...
Status: R_3 <= 462 PROVED with external inputs (same inputs as 464);
R_4 <= 21,987,409 PROVED (elementary, self-contained). Both independently
re-run here; not merged.

## 3. Step B plan: prefix word + local triangle refutation for R_3 <= 461

Claim attempted (461): every proper 3-coloring of the 461-square has a
36-letter diagonal prefix z with G_0 + 3 D_35(z) <= 0 ("bad word"). The
lower triangle {(x,y): 0<=y<=x<=35} of the square is properly colored with
diagonal z. If for every bad word the prefix triangle (and/or the suffix
triangle by the anti-transpose symmetry) has no proper coloring, then
R_3 <= 461.
Discriminating test: count bad words at 461 (orbits under color
permutation). If small, SAT-check each triangle with checked DRAT proofs.

## 4. Step B results (all exploratory unless stated)

- count_bad_words.c: 462/K=36 -> 0 bad orbits (agrees with PR 11); 462/K=22 -> 4
  orbits (24 labeled). 461/K=35, W=85 kernel: >= 62,547 bad orbits when stopped
  (DFS still in the subtree z_0=z_1=z_2=0); total unknown, larger.
- Adaptive kernels (Prop. 6.1 of proof.md): model reproduces PR 11's -863,712,470
  exactly; PR 11 witness: max over w>=0 numerically negative (-10.8 unit norm);
  random 300 bad words: 20 excluded with exact integer check (~7%).
- Window triangles (Prop. 6.2): 36-triangles of two bad words UNSAT by CaDiCaL
  (5.5 s, 16 s), proofs not checked (Python forward RUP checker too slow).
  Short windows: 3/26 bad words have an UNSAT 16-window, 1/26 a 14-window.
  Random windows: m=16 7/40 UNSAT, m=18 1 SAT 8 UNSAT 31 undecided, m=20 18 UNSAT
  22 undecided (1e5-conflict budget).
- Tooling: rup_check.py (independent forward RUP checker; deletions ignored, which
  is sound), CaDiCaL proof capture via pysolvers.cadical195_del flush, DPLL
  completion emitting RUP lemmas. Validated on PHP(6,5), PHP(7,6); corrupted
  proofs rejected.

Conclusion: R_3 <= 461 by "prefix inequality + local 36-triangle refutation"
needs the full bad-word list and ~10 s solving per word; not feasible in session.

## 5. Next actions

1. Fast proof checking: build drat-trim (or cake_lpr) locally (needs a download,
   not authorized this session) or port rup_check to C; then certify triangle
   refutations.
2. Interleave: in the B&B, when positions 0..m-1 (m ~ 18-20) are assigned, test
   the prefix window triangle against a cache of certified infeasible windows.
   Measure the distinct m-prefixes reaching that depth first.
3. R_4: the dominant loss is the binary fiber cap Q(L-h)+Q(L-h-1) ~ 2 sqrt(L);
   doubled Golomb gives ~sqrt(2L) lower bound (round 4). Any cap c*sqrt(L),
   c < 2, valid at spans ~ 2e7 cuts n by about (c/2)^2.

Session state: proof.md written; complete as a write-up of what was achieved.
