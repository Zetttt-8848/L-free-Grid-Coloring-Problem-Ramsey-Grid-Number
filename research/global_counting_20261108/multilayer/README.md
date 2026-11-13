# All-level colored recurrence and two-end counting

The new count keeps the first two return positions of each diagonal color
at every lag. Their Golomb capacities are exactly a sum of capped colored
autocorrelations over **all nested cardinality thresholds**, not only the
24-mark threshold. A second theorem matches the first two returns to the
last two returns, so the two ends cannot be assigned independently.

[THEOREM.md](THEOREM.md) proves the first-return count, the exact layercake
identity, the two-end transport count, and the convolution bridge to the
square. This gives a concrete nonlinear word extremum whose universal
bound would imply a numerical improvement. That extremum remains open;
this package claims no improvement below the existing side-464 bound.

Run from the repository root:

```sh
python research/global_counting_20261108/multilayer/verify.py
```

The standard-library checker computes the exact small Golomb capacities,
checks every pair of disjoint Golomb classes in at most ten positions,
and checks the literal all-level identity on every three-color word of
length at most eight. It also records examples where the two-end count is
strictly stronger than either separate endpoint count. These finite
checks audit the formulas; they do not replace the displayed general
proof or revalidate externally established large Golomb ruler bounds.

One concrete ten-mark set passes both separate endpoint capacities and
the independent span capacity (all equal 10), whereas the two-end matching
capacity is 9. The checker independently verifies all 1024 attempted
partitions of this set. This certifies a strict difference between the
new resource count and those earlier tests, with its exact limited scope.

The user requested new counting methods with substantial upper-bound
potential. Accordingly this package makes no lower-bound search and
does not present another one-position boundary enumeration as a general
solution. The first unresolved step is a universal count for the common
nested-word resource retained by these inequalities.
