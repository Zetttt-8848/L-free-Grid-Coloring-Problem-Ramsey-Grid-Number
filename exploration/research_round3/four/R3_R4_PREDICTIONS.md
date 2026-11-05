# R3-R4 frozen predictions

Frozen after pinning the objective and before running any new capacity or
score program.

1. **Structural profile.**  The valid internal multiplicity profile will be
   `V_h=2Q(L-h)`, where `Q(S)` is a Golomb-order cap at the actual residual
   span `S`.  It will weakly dominate the inherited uniform profile
   `V_h=2Q(L)` and will strictly reduce many `K_d` values in the active
   `d=1..35999` score window.
2. **Neighbor parameters.**  Optimizing the Golomb neighbor parameter per
   relevant span and selecting the outer rank-neighbor parameter per span
   will give a further nonnegative improvement.  I expect lowest Golomb
   optimizers near 60--80 and outer optimizers near 600--750, but make no
   global-optimality claim before the exact scan.
3. **Bound movement.**  With the inherited `t=36000` polynomial weights, I
   predict a strict certified improvement below `22006246`, likely between
   `21995000` and `22006245`.  The first exact candidate integer will be
   frozen separately after scouting and before independent validation.
4. **Scale.**  I expect the profile frontier to use roughly 30000--35000
   internal distances and to lower active three-color capacities by tens,
   making the improvement structural rather than a weight-only cosmetic step.
5. **Iteration.**  If a candidate passes, one further downward candidate and
   one alternate-profile check will be frozen and evaluated.  I predict the
   immediate lower neighbor may fail because of capacity cliffs, but do not
   assume monotonicity.

Honesty label: **CONJECTURE / pre-execution prediction**.
