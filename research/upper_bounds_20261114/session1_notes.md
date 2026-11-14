# Working notes, upper_bounds_20261114

Session date 2026-11-14. Worktree `C:\Users\ZhuanZ\Desktop\lgrid-ub-20261114`,
branch `claude/upper-bounds-20261114`, based on
`origin/claude/upper-bound-skills-20261113` = `6630b5e27a07a35ac5a06af325551265a692daf6`
(PR 10, stacked on checkpoint `dc1cbe6daf7d9816329217a511741fbeabd726b3`).

## 0. Refresh (done)

- `refresh_state.py --fetch`: only moved item is PR 10 itself (unpinned, contains
  checkpoint). No other remote branch is newer than the snapshot of 2026-11-13.
- Remote branches and heads recorded in section 0.1 of README (to write).
- Baseline: 21 <= R_3 <= 464 (external OGR inputs), 21 <= R_4 <= 21991300
  (round-2 lemmas not re-audited), fallback 22049225 elementary.

## 1. Plan (written before derivations)

Selected task: **exact finite capacities of binary (and ternary) sources, and
the three-class partition relaxation, as an independent route to upper bounds.**

Definitions (k colors):
- `A` subset of integers; strict source `V(A) = {(v,u): u<v in A}`; a proper
  j-coloring of V(A) is a map to j colors with no monochromatic
  `(v,u),(v+d,u),(v+d,u+d)` with all three cells in V(A). Equivalent pair form:
  no u<v, d>0 with u,u+d,v,v+d in A and z{u,v}=z{u,v+d}=z{u+d,v+d}.
- `f_j(L)` = max |A| over A in {0..L} with V(A) properly j-colorable.
- `P_k(n)`: there is a partition {0..n-1} = A_1 u ... u A_k such that each
  V(A_c) is properly colored with the k-1 colors other than c. (Relaxation of a
  proper k-coloring of the n x n square: diagonal classes + diagonal exclusion.)

Implications (to be proved in proof.md):
- (I1) If P_k(n) fails then R_k <= n.
- (I2) If f_{k-1}(n-1) < ceil(n/k) then P_k(n) fails, hence R_k <= n.

Cheapest discriminating test: compute f_2(L) for small L and P_3(n) for n near 21
by SAT, timing growth. Stop rule: if P_3(n) is SAT for every n up to ~40 with
easy solves, the relaxation threshold is beyond cheap reach -> record growth and
switch to structural use of the extremal sets. If UNSAT appears at moderate n,
produce DRAT certificates, check with an independent checker, and audit the
encoding.

## 2. First computations (capacity_sat.py, CaDiCaL 1.9.5 via python-sat 1.9.dev15)

Encodings: `partition` (P_k(n)), `capacity` (f_j(L) >= s ?), `grid` (full square),
`triangle` (weak lower triangle x >= y; every L with corner x >= y lies inside it).
All SAT answers are decoded and the partition answers re-checked by `check_partition`.

- k=2: partition SAT for n<=7, UNSAT n=8; triangle SAT n=4, UNSAT n=5..10; grid UNSAT n=5,6.
  So for two colors the triangle relaxation is exact (threshold 5 = grid threshold),
  the partition relaxation is weaker (threshold 8).
- k=3 partition: SAT (checked) at n = 5..60 (n=56: 2.3 s, 58: 4.2 s, 60: 47.5 s).
  So the partition relaxation threshold is > 60: it cannot give R_3 <= 60.
- f_2 exact (no symmetry breaking; UNSAT answers not yet certified):
  f_2(10)=9, f_2(15)=11, f_2(19)=13, f_2(24)=15 (s=16 UNSAT in 71 s), f_2(29)>=16.
  M/L = 3.6, 3.67, 4.1, 4.4. Binary sources are dense at small span (|A|/L ~ 0.6),
  so route (I2) (single class) is hopeless at computable spans: f_2(L) < L/3 would need
  L far beyond reach. The S21 coefficient 21 is not threatened at these spans.
- k=3 triangle: n=15 SAT instantly; n=20 not solved in 200 s (known SAT, since the 20x20
  square from Canakci et al. restricts to it). Background runs n=20..32 (3500 s limit).
