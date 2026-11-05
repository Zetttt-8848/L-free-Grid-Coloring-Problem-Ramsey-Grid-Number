# Independent finite verification

This directory contains a standalone Python standard-library verifier for the
semifinal-oriented revised manuscript. It reads the numerical certificates directly from
the supplied TeX source. No previous working directory, supplementary module,
SAT solver, or third-party Python package is required. Use Python 3.10 or newer.

Run from the directory containing the delivered files:

```bash
python verify_directed_L_manuscript.py --source main.tex --bib references.bib --output verification_results.json
```

The source may also be supplied positionally. The `--bib` option is optional;
without it, inline bibliography keys are checked when present. If the source
uses an external bibliography and `--bib` is omitted, the report explicitly
records that citation-key integrity was not checked.

Do not run Python with `-O`: this validator uses assertions and rejects an
optimized run. A numerical or parsing mismatch raises an exception and writes
a failed JSON report. A successful report records the exact source,
bibliography, and verifier SHA-256 digests, the timestamp, the execution
environment, the checked domains, and numerical results. Rerun after changing
any delivered source, bibliography, or verifier file.

## Certificate coverage

- The seven-mark Golomb witness, all 21 printed positive differences, and
  uniqueness of pair sums with repeated marks allowed.
- The full four-by-four grid crop: 16 cells, all 14 directed corners, and the
  three printed fiber lists.
- The twelve-mark weak coloring: all 78 cells, 140 weak corners, 74 strict
  corners, every printed equal-color completion group, and all fiber counts.
- The two-Golomb concentrated-deficit example: the complete distance and
  incidence tables and the values `rho=5, N=29, Q=11, T=50`.
  The added explanation's same-direction, opposite-direction and
  repeated-mark incidences are checked explicitly; they are already
  included in the complete incidence-table checks.
- The four-cube L/U/X arrays for weights `(1,3,9,27)`: 120 cells, 200 corners,
  every printed word-multiplicity row, `D_z=26`, `R_z=25`, `P_z=8`, actual
  `K3=120`, the printed old/new branch table 387/325 to 379/317, and the
  exact reduction of the combined bound from 325 to 317.
- The three-cube table and subset-label rule, all 24 printed corner records,
  nine mixed corners, and 15 forcing corners.
- The new six-mark witness on `{0,1,2,3,4,6}`: every source-cell row and every
  printed corner word by common leg length. Direct enumeration gives `T=16`
  and `E=130` with no monochromatic corner. In the refinement, all four-,
  five- and six-mark sets of minimum zero and span at most 20 are also
  enumerated against the endpoint-loss identity and the printed equality
  types. Eighteen translated, dilated and reflected copies of the six-mark
  coloring check the transport of properness. These are bounded supporting
  checks; the universal upper bound and full equality classification use
  the printed proofs.
- The 11-, 12-, and 13-mark three-colorings, respectively three, six, and 14
  rainbows, all printed zero-sum records and all 286 modular corner sums for
  the 13-mark example. The three-color line identity is also checked.
- The four printed structured examples and further finite instances of
  `A_r={+/-5^i:0<=i<r}` and `B_r={5^i+5^j:0<=i<j<r}`, at `r=4,6,8,10`.
- Every labeled simple graph on zero through five vertices (1,100 in total,
  including all 1,024 five-vertex graphs), and seven six-vertex representatives.
  The zero-vertex graph is included in that total as a degenerate test. An independent
  adjacency/common-neighbor formula counts unoriented four-cycles, allowing
  chords. Tests compare `T=2*C4` with integer differences and direct coordinate
  corner enumeration, and check the distance coloring, long-pair midpoint
  multiplicity, pair-sum preservation, energy identity, and `M<=5L`.
  The printed `K4` example is checked against the six marks
  `{6,26,30,126,130,150}`, the three pair representations of 156,
  `C4=3`, `T=6`, and `E=90`. The additional squared-distance coloring
  gives `K3=0`, `D_z=12`, `R_z=0`, `P_z=6`; both moment branches move
  from 6 to 0 and attain the exact value. This is not a strict switch
  between branches. This graph case was already included in the
  exhaustive small-graph check; the extra check binds the explanatory
  display to its numerical values.
- On the tested strict binary colorings: simplicity of the forcing graph,
  its global identity, pointwise signed-completion identity, degree identity,
  and the new `Q`, `eta`, and `P_z` bounds on the actual fiber partitions.
- Both systems of 42 dilation weights. The compact current weight table and
  the earlier expanded table format are supported. Every recurrence term is
  recomputed, as are copy factors, summands, totals, and every potentially
  nonzero load through 378 or 420. All printed smooth-step loads and their
  complete smooth-integer ranges are checked. The compact table no longer
  prints individual copy factors or summands; the report distinguishes their
  recomputation from comparison with printed entries.
- The arithmetic of the conditional three-color bounds 361 and 379, the new
  four-color profile giving 98,777 with gap `3,161,813,264`, and the rejected
  459/455 rainbow routes with gaps `5,959,890` and `578,300`.
- Uniqueness of source labels, definition of reference targets, and citation
  keys against `references.bib` when supplied. These checks concern key
  integrity, not bibliographic accuracy or research priority.

## Limits

Finite checks do not certify proofs for arbitrary sets, weights, graphs, or
values of `r`. The general results, including the universal six-mark maximum and its equality classification,
the direct-sum bound, the two-distance coefficient six, and the midpoint-three
coefficient two, rely on their mathematical proofs. Tests on small instances
do not establish their optimality.

The validator proves no open assertion and claims no new unconditional Ramsey
bound. The 459/455 arithmetic does not restore the local rainbow premises,
which the printed colorings refute. Verification of a positive `P_z` correction
does not supply an example in which the `D_z` correction changes which branch
is smaller. No such example is claimed here.

This is a newly written independent validator, not a claim to have run an
unavailable original search pipeline. Separate SAT encoding/model-validation
tools have their own instructions and reports. No external literature-content
or priority audit is performed by this program.
