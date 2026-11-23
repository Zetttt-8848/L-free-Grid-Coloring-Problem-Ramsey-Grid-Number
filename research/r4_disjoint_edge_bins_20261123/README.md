# Four-color bound at side 21,947,855

Every coloring of the full square of side 21,947,855 with at most four
colors has a monochromatic directed equal-leg L. The improvement uses
the exact rank and outer consumer at [round 3][round3], the verified
20-position binary-source capacity, and a larger disjoint part of the
endpoint variance already present in the window proof.

## Endpoint variance

For each of the six weighted window rows, use bins 0 through 149 measured
from each end. At an integer position within one bin, the earlier
coefficients see at most the binary-source capacity of a full block.
The current coefficient sees at most the capacity of the partial block.
Apply the inherited squared positive-part shortfall using these caps,
the minimum allowed block width, and the lower bound on the multiplier.
The first 1,720 positions in each bin are valid throughout the certified
range of block widths.

In each row, the sampled positions of different bins are disjoint. The
two end bands are disjoint because each checked interval has
`p - 1 >= 400 B`. Row probabilities therefore weight a sum of supported
discrepancies. With `C(20)=13`, the binary span recursion uses
`e_14 >= 20`. Checking all 27,132 normalized 14-subsets and a complete
13-mark witness reproduces this capacity. [Upstream capacity review][c20]

Evaluate each integer position and round each nonnegative weighted bin
contribution downward to multiples of `10^-9`. The sum gives the exact
lower bound `D = 112363395573 / 500000000 = 224.726791146`.
Sixty bins contribute positively. The verifier reconstructs the original
rational window and all 401 coarse coverage checks from the pinned
[source matrices][tables].

## Full-square contradiction

The stored certificate transports the larger correction into each binary
capacity interval and keeps the original ordinary Golomb thresholds.
The independent checker verifies the rank recursion, every binary
interval, the quartic correlations, and the twenty-shift losses. It
uses interval integration for the final ranks and checks that the 562
credited twenty-shift blocks are disjoint.

The resulting exact positive margin at side 21,947,855 is
`978462482258825932730147067816013031680524048`. The same certificate's
margin at the preceding side is negative. The proof improves the
round-3 upper bound of 21,947,865 by ten.

## Reproduction

Use a worktree at round-3 commit
`14647e607c2525b0cd12081b03899827d306a030` and the upstream
`asymptotic` directory at `ff5b032fc3745140549777a96a9ec3ba7f8dd954`.

```sh
python3 verify_c20.py
python3 verify.py --round3 /path/to/round3 --window /path/to/asymptotic
```

The certificate identifies the exact matrices by SHA-256. The original
proof of the local capacity and the inherited consumer are cited at
their pinned revisions. The checker performs the arithmetic with the
Python standard library.

[round3]: https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/tree/14647e607c2525b0cd12081b03899827d306a030/research/r4_local_capacity_round3_20261114
[tables]: https://github.com/dcartermath/sidon-error/tree/ff5b032fc3745140549777a96a9ec3ba7f8dd954/asymptotic
[c20]: https://github.com/Zetttt-8848/L-free-Grid-Coloring-Problem-Ramsey-Grid-Number/tree/deb5097/research/r4_grid_compatibility_20261114/review_codex_r3
