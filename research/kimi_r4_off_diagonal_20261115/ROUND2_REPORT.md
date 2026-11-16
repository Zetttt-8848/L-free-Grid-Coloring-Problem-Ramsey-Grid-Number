# Round 2 report: two-diagonal product classes

**No new Ramsey bound is established.** The proposed two-diagonal fiber
reduction was refuted by a complete proper 3 by 3 four-coloring before any
large capacity computation was run.

Branch: `kimi/r4-off-diagonal-20261115`.
Base: `252bdcfb9da09eb149a7e5c0505d512fbd907405`.
Date: 2026-11-15. Author: Kimi.

## Outcome

The route attempted to retain joint membership in a main-diagonal color class
and an off-diagonal color class. The desired stronger statement O1 would have
reduced the palette of every joint fiber's main completion colors and enabled
sixteen product-class capacities.

A coordinate expansion shows that the main pair uses completion `W_h[u]`,
whereas the off-diagonal pair uses `W_(c+h)[u]`. These are distinct for `c>0`.
The stored 3 by 3 witness realizes `c=h=1`, `a=0`, `b=1`, and has main
completion color `b`, directly violating O1.

The independent verifier checked all five geometric Ls, all nine cells, the
prescribed diagonal-word entries, and the two distinct completion locations.
Status: PASS.

## Pivot

The sixteen-class capacity consumer was cancelled because its only enabling
lemma is false. No numerical scan, solver search, or larger random sample was
run. The surviving identity `F_c(J_(a,a))=empty` is the standard single-lag
source restriction and does not justify the cancelled consumer.

The next candidate lane is explicit multiscale recursion using only subdomains
that preserve equal-leg geometry. Shared-completion arguments across different
lags overlap existing cross-source work and require a fresh nonduplication
check before use.

## Reproduction

From the repository root with Python 3.12.16 and only the standard library:

```text
python research/kimi_r4_off_diagonal_20261115/find_counterexample.py
python research/kimi_r4_off_diagonal_20261115/verify_counterexample.py
```

Expected independent status: PASS. This is an internal reproducibility check,
not external peer review or Lean formalization.
