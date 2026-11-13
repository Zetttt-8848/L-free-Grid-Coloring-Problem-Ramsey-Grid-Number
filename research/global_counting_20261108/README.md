# Global count: cross-source conflicts, double-ended resources and the cost of extreme shapes

This round explores pure mathematical upper bound counting in parallel according to user requirements, and does not carry out lower bound SAT search.
**No Ramsey upper bound smaller than 464 has yet been proven; the project interval remains`21 <= R3 <= 464`.**
The advance here are three sets of counts that preserve common constraints, and their proven stringent consequences.
Their unresolved unified estimates cannot be replaced by small examples or computational quantities.

Basic submission:`5b5db22c3c65123193cb31f2aa5bd949b3075e1a`, which is the previous research checkpoint.
All coordinates start from zero, the only forbidden direction is`(x,y),(x+d,y),(x+d,y+d)`,`d>0`.
The main manuscript has not been mathematically revised; the results of this round and independent review are kept in this directory.

## 1. Switch from source-by-source counting to color requests for the same grid

Each of the three diagonal color classes generates a strictly dichromatic source. Even though these three sources are each legitimate, they
Requests made to the same square outside the source may still exclude all three colors.
[Full derivation](completion/COUNTING.md)Preserve these requests until after the summation:

`C_mix = sum_q V_q^a H_q^b (H_q^e + V_q^e)`.

Among them, the colors of the two diagonal endpoints of q are a and b, and e is the third color; H and V are counted respectively.
Two sources make input requests of the same color to q in the horizontal and vertical directions. Every non-zero product number is
A set of three-color exclusions formed by six real input cells. A complete normal square must satisfy`C_mix=0`.
Furthermore, for any continuation, the total number of monochromatic L satisfies

`N_mono >= sum_q min(V_q^a, H_q^b, H_q^e+V_q^e)`.

Here the true multiplicity is given: each L counted has only one unfilled cell q,
Not double-counted under other q's. This is the exact minimum cost of the request family listed; it does not
contains all cross-sources L, so zero cost cannot be regarded as a sufficient condition for full square continuation.

We are given a partial coloring of order ten: all three sources and L on all filled cells are legal,
but`(8,3)`When a request is received to exclude three colors at the same time, any continuation will result in a single color L.
It strictly demonstrates the information lost when processing three sources independently, and is not proof that the tenth-order square does not exist.
**To turn this method into a smaller upper bound for R3, it is still necessary to prove that any three compatible sources that are large enough must
Make the above global cost positive. ** This step remains open.

## 2. Calculate all size levels and head-to-tail matching at the same time

[Full level count](multilayer/THEOREM.md)Keep each diagonal color, each step size
The first two same color return positions. The capacity of two perfect color classes is equal to all nestings of the same diagonal word
Prefix truncates the sum of autocorrelations instead of just counting the 24th token.

The new paired-ended matching further requires that the minimum and maximum points of the same class are paired. a clear
The ten-point set is checked for capacity by calculating the head, end, and span separately (all 10),
However, the common capacity of both ends is only 9, so it is impossible to divide it into two Golomb classes.

[Information gap testimony](information_gap.json)Two nine-character color words are also given, all scalar
autocorrelation`R_d`are exactly the same, while the new paired-ended counts are 4 and 3 respectively at d=3.
So this count does preserve the old`R_d`Array of unrecoverable information.
What has not yet been completed is the unified control of weighted capacity for any long diagonal word, which cannot be replaced by the mean of random words.

## 3. Calculate extra spans for mutually exclusive extreme shapes

[Span Cost Proof](multiscale/THEOREM.md)Use the minimum and maximum points of various types at the same time:
If the minimum span of t disjoint m label classes is g, and at most a can reach g at the same time, then

`t*g + max(0,t-a) <= t*(p-t)`.

Applying OGR-24's published optimal ruler uniqueness and its difference set, the four Category 6 capacities can be strictly reduced:

| Number of available positions p | Capacity of the previous round | Capacity of this round |
|---|---:|---:|
| 428 | 141 | 140 |
| 429 | 142 | 141 |
| 430 | 143 | 142 |
| 431 | 144 | 143 |

This application uses more published “uniqueness” conclusions than the previous round. Only the given ruler is checked locally.
Difference and derivation without re-executing the OGR exhaustive search. Translation of the same extreme shape step length
It is also subject to the same diagonal color and overlapping moment budget constraints: if there are t occurrence positions in the same direction,
Its grid point coverage multiplicity satisfies`sum r=24t`,`sum r^2=t(t+23)`.
The diagonal color class size obtained by combining one-class convolution counting is at most 164, which can be deduced: Assume that there
For a normal square of order 463, there are at most **56 steps with a span of exactly 425 in total.
Complete class**, while progressively longer independent budget allows for 74. Level 464 corresponds to an independent budget of 76.
This is the upper limit of the overall number of occurrences, and there is no unified lower bound of the number of occurrences that contradicts it.

When using only the four new capacities with the original integer weights, the contradiction for n=463 is still
`-2534488525`, 463 cannot be ruled out; the amount of contradiction for n=464 is`1433217328`.
This capacity improvement involves the same penalties as colored boundary counting, and its gains cannot be directly stacked.

## Evidence and next steps

- [Independent review](review/REVIEW.md)Reconstruct code with independent integers; not Lean formal authentication.
- [Sources compared with old and new methods](COUNTING_COMPARISON.md): Not to rediscover classic tools
The historical conclusion or unfinished necessary conditions are called global original breakthroughs.
- [Target Contract](CONTRACT.md), the original certificate, complete witness and inspection output of each package are retained.
- `threshold_scan.py`Only scout full level **scalar** capacity and limited weight range; floating point output
No new theorem is involved, and no better weights or other methods are excluded.

Run from the repository root directory`python research/global_counting_20261108/verify_release.py`
All accurate checks can be reproduced on a temporary copy and 13 sets of limited checks on the main draft can be re-run. original
Research records remain unchanged; results are written with file-by-file hashes`release_validation.json`,
The version, actual command and run scope are documented in`release_manifest.json`.

The next main focus is the unified positive cost lower bound for cross-source requests, as well as the double-ended,
Common capacity across tiers. Global overlap budgets for extreme scale translations are available as a third independent input.
These directions are still open; this checkpoint is not the completion of the research goal of "further compressing the upper bound".
