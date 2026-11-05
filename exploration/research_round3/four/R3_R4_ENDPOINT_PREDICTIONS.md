# R3-R4 endpoint iteration predictions

Frozen after receiving `research_round3/cap/endpoint_neighbor.md` and before
executing any endpoint-corrected capacity calculation.

The inherited doubled neighbor comparison is refined from

```text
2*M(H) <= L*c*(c+1)
```

to

```text
2*M(H) <= L*c*(c+1) - 4*binom(c+1,3)
```

using only distinct integer marks (`ell_i=i`).  I predict:

1. Globally optimized Golomb caps `Q(S)` weakly improve, but only at some
   span thresholds because the inner optimizing `c` is about 70.
2. Outer capacities improve by several marks at most active distances because
   the optimizing `c` is about 700.
3. With the same weights and window, the resulting certified candidate will
   be strictly below the already frozen profile-only candidate `21992400`,
   likely in `21990000..21992399`.
4. The endpoint correction remains secondary to the distance-dependent
   multiplicity profile; an alternate run without it will quantify that split.

Honesty label: **CONJECTURE / frozen before endpoint execution**.
