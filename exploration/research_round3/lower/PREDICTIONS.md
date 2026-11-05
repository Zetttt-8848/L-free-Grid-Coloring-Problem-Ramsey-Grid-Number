# Frozen Route-5 predictions — R3-R5-L2

Frozen before every solver or construction attempt on 2026-09-10.

## P5.0 exact instance bookkeeping

For the orientation
`((x,y),(x+d,y),(x+d,y+d))`, with zero-based `0 <= x,y < 21` and
`1 <= d < min(21-x,21-y)`, predict exactly

- `T_21 = sum_{m=1}^{20} m^2 = 20*21*41/6 = 2870` geometric corners;
- `3*21^2 = 1323` one-hot variables;
- `4*21^2 = 1764` exactly-one cell clauses;
- `3*T_21 = 8610` monochromatic-corner clauses;
- `10374` clauses before color symmetry and `10815` after the `441`
  color-permutation symmetry clauses.

The four split cells `(0,1),(1,0),(1,1),(20,20)` have exactly `3^4=81`
assignments.  Predict a mechanical coverage audit will find 81 distinct cubes,
one cube for every total assignment's restriction, and no overlap.

## P5.1 first escalated cube stage

Use MapleChrono only after an interrupt-interface smoke test.  Revisit all 81
cubes in the Round-2 seed order.  Give each of the 33 formerly immediate raw
UNSAT cubes at most 2 seconds and each of the 48 formerly open cubes at most
10 seconds, for a nominal cap of `33*2+48*10 = 546` solver seconds and an
overall stage cap of 600 wall seconds.

Prediction: no SAT witness appears; at least 33 cubes again return raw internal
UNSAT; at least 35 cubes remain interrupted/UNDECIDED.  Even if every cube
returns raw UNSAT, the mathematical result remains UNDECIDED unless all cube
proofs are retained and checked independently against the exact CNF.

## P5.2 proof-capable tooling

Predict the installed PySAT bundle can emit a proof from at least one solver on
a tiny UNSAT smoke instance, but that no independent DRAT/LRAT checker is
already present on `PATH` or in the Anaconda installation.  Therefore no
negative bound movement is predicted in this checkpoint.

## P5.3 restricted construction channels

Test two new, explicitly restricted premises:

1. modular affine colorings `chi(x,y)=f(a*x+b*y mod m)` for stated finite
   parameter ranges;
2. one-dimensional circulant specializations, with their induced literal
   constraint systems checked independently on every candidate matrix.

Prediction: no side-21 coloring is found in the first bounded modular scan.
The scan is only a finite-family decision and will not be generalized beyond
its logged parameter range.  The separated coordinate-injective product
family and naive alteration route remain closed and will not be retried.

Before the modular attempt, freeze its first range as every integer modulus
`2 <= m <= 50` and every ordered coefficient pair `(a,b) in Z_m^2`, exactly
`sum_{m=2}^{50} m^2 = 42924` parameter pairs.  For each pair, solve for every
total map `f:Z_m->{0,1,2}` with `f(0)=0`, which is sound under color
permutation.  Cap the complete scan at 180 wall seconds and each SAT call at a
100000-conflict budget.  Predict zero SAT pairs and zero interrupted pairs;
because negative solver statuses have no retained checked proofs, even a full
raw-UNSAT scan will be reported as UNDECIDED for nonexistence in this family.

## R10 trigger

Any disagreement in a count, cube literal, coverage result, solver interface,
declared parameter range, matrix color domain, or direct corner check halts the
affected route.  The discrepancy is appended to `ERRATA.md` before resuming.

## P5.5 directed hard-cube portfolio

Frozen after the first-stage checkpoint and exact API smoke, before any new
hard-cube solve.  The 48 cubes whose Round-2 and Round-3 MapleChrono runs both
interrupted are partitioned by parity of their position in that 48-record list:
24 cubes to Glucose4 and 24 to MapleCM.  Both passed construction,
`set_phases`, interrupt, and `solve_limited` on PHP(5).  Glucose4 additionally
returned a nonempty proof trace; MapleCM returned an empty trace and therefore
has no general proof-output claim.  Lingeling is excluded under R3-R5-E2.

Each cube receives 60 seconds, `120` times the original `1/2`-second Round-2
cap.  Two workers give a nominal maximum of `24*60 = 1440` seconds per worker,
within the directed 1800-second stage wall cap.  The same exact CNF, the same
four cube literals conjoined as unit clauses, and the domain-valid eight-
conflict side-21 phase hint are used.

Prediction: zero SAT witnesses; between 0 and 5 raw solver-UNSAT cubes; at
least 43 interrupted cubes.  Any raw UNSAT cube changes mathematical status
only after its trace is independently checked or the augmented CNF directly
unit-propagates to contradiction.  The global side-21 result is predicted to
remain UNDECIDED.

## P5.6 modular-affine continuation

The first 180-second epoch attempted the first 18916 of 42924 ordered
parameter pairs, leaving exactly `42924-18916=24008`.  Before resumption,
freeze a second epoch starting at deterministic pair index 18916 with a
300-second wall cap and the same 100000-conflict per-call cap.  Predict all
24008 remaining pairs are attempted, with zero SAT and zero conflict-budget
interruptions.  Negative family status still remains UNDECIDED without checked
proofs, even if every raw status is UNSAT.

## P5.7 portfolio recovery after R3-R5-E3

MapleCM returned exactly five shard-1 records before its sixth solve violated
the live cap.  Freeze the recovery target as the remaining `24-5=19` shard-1
cubes, preserving their original order and assumptions.  Glucose3 receives 60
seconds per cube, hence at most `19*60=1140` nominal solver seconds.  Together
with the already-running Glucose4 shard, this keeps the portfolio checkpoint
within the directed 1800-second overall wall window from its initial launch.

Prediction: zero SAT; between 0 and 3 raw UNSAT; at least 16 interruptions on
the 19 recovery cubes.  Across all 48 hard cubes, predict zero SAT, at most 5
raw UNSAT, and global status UNDECIDED.

## P5.8 modular-affine final continuation

After Glucose4 released one portfolio core, exactly 19810 deterministic pairs
remain at indices 23114 through 42923.  Freeze a third epoch starting at index
23114 with a 300-second wall cap and the unchanged 100000-conflict per-call
cap.  The host now runs only one hard-cube worker in parallel, matching the
first affine epoch's one-worker contention level.  Predict all 19810 pairs are
attempted, with zero SAT and zero conflict-budget interruptions.  A complete
raw-UNSAT scan remains UNDECIDED as a negative family claim because no checked
proofs are retained.
