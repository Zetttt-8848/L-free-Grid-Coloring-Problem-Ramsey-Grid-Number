# Erratum: Q3a and its averaging proof are withdrawn

Date: 2026-11-15. Author: Kimi.

The round-1 Q3a statement

```text
sum_(d=1)^4 P_d/(5-d)^2 >= 3(n-4)^2
```

is **REFUTED**. See `research/kimi_r4_multiscale_20261115/THEOREM.md` for the
complete proof and independently checked witness. A proper 6 by 6 four-coloring
has `P_d=(6-d)^2`, making the left side `1381/144`, strictly below 12.

There are two errors in the old proof:

1. A fixed L does not generally lie in exactly `(5-d)^2` contiguous blocks;
   boundary truncations matter. For `L(0,0;1)` at side 5 or 6, the count is 1.
2. The aggregate incidence has multiplicative copy multiplicities, not divisors
   of the claimed form. More decisively, every L in every four-coloring is
   pair-tight for some quotient, so `P_d=(n-d)^2` and the proposed count retains
   no coloring information.

The old unweighted inequality is true but trivial: the first three terms of
`sum_(d=1)^4(n-d)^2` already give at least `3(n-4)^2`. Its old derivation and
claimed structural significance are withdrawn.

Q1, Q2, and the obstruction to arbitrary unequal row/column selection are
separate statements and are not refuted by this erratum. The old averaging
scripts and their PASS labels are historical only; use the new independent
checkers in `research/kimi_r4_multiscale_20261115/`.

No numerical Ramsey bound changes.
