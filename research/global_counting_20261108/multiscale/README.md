# Extremal-shape span and occurrence costs

The [theorem](THEOREM.md) charges every non-optimal Golomb class one extra
unit of span. Uniqueness of the optimal24 ruler limits how many classes can
avoid that charge, while disjoint minima and maxima bound their combined
span. This lowers the six-class capacities at428 through431 positions by
one each. It does not by itself improve the Ramsey bound464 or achieve the
requested large improvement.

The theorem also retains all occurrences of each optimal-ruler orientation
across the full diagonal. All occurrences of one orientation have one common
original color. Their pairwise intersections give an exact second-moment
identity, limiting how many occurrences can coexist in that color class.
Extremal completion classes at different offsets must draw pairs from these
same occurrence sets. This global constraint has not yet been converted into
a Ramsey contradiction.

Run from the repository root:

```text
python research/global_counting_20261108/multiscale/verify.py
```

The standard-library checker verifies the literal ruler and the consecutive
differences needed in the proof, the two-ruler packing example, every
capacity for1<=p<=480, the old/new polynomial-kernel margins, and the
occurrence-count arithmetic. The [result](verification.json) is exact.
OGR24 uniqueness and OGR25 optimality remain cited established external
computational results.

The discovery-only `rank_probe.py` tests a stronger rank-distance transport
relaxation for six24-mark classes. If x_(r,j,d) counts classes where the
marks at ranks r and r+j differ by d, then

* `sum_d x_(r,j,d)=6`;
* `sum_(r,j) x_(r,j,d)<=6`, since one Golomb class uses d at most once;
* `G(j+1)<=d<=p-1-G(r+1)-G(24-r-j)`;
* for s=min(j,24-j), `sum_(r,d) d*x_(r,j,d)<=6*s*(p-6*s)`.

Ranks are zero-based. The last inequality follows by counting the distinct
6s lower and6s upper endpoints of rank-j pairs. The old full table of Golomb
span inputs is used only for this probe and has not been independently
reauthenticated here. The probe requires NumPy and SciPy. It reports
floating infeasibility at p=425,426,430 and floating feasibility at
p=431,435,440,450,460,463. Neither status is promoted to an exact theorem or
an actual disjoint-ruler construction. The solver outputs are retained in
`rank_probe.json`; they are not a dependency of the span-cost theorem.

Rank counts use possible distances without retaining the entire extremal
shape. The new shape cost cannot be inferred from a numerical status, and
the proof needs the separate uniqueness statement. No claim of universal
novelty or optimality of this counting method is made.
