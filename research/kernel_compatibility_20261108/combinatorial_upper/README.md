# Pure colored-boundary counting

The new object is a family of capped same-color comparisons between two
short boundary words. Large Golomb classes must use these actual endpoint
pairs, with at most two classes paid by each original diagonal color.
Neighboring comparison layers form one path, so their capacities cannot
be simultaneously optimized independently.

[THEOREM.md](THEOREM.md) supplies the full charging proof, the path lemma,
and an explicit three-multiplier weighted corollary. This strengthens the
new side-464 contradiction margin from 477965143 to **1199151808**.
The same displayed weight at side463 has a negative margin; no463 result
is claimed. External Golomb inputs are inherited from the authenticated
[previous checkpoint](../../coupled_budget_20261108/numeric_upper/THEOREM.md).

The universal proof uses no solver and no square-coloring enumeration.
The separate finite diagnostic exhausts177147 normalized pairs of length6
words and obtains the sharp local maximum14. It is labeled finite evidence,
not a proof of a general arbitrary-length formula. Further length5–9
diagnostics are owned by the neighboring `kernel_upper/` package.

Run from the repository root:

```sh
python research/kernel_compatibility_20261108/combinatorial_upper/verify.py
```

The standard-library checker records exact arithmetic, all finite
maximizers, actual Python version, and hashes of its source, theorem and
contract in [results.json](results.json). It independently reconstructs
the path graphs for sizes2 through20, all autocorrelation coefficients,
and every coefficient of the three displayed charging multipliers.
The general proof establishes unbounded validity; those checks audit
its finite instantiation. No external Golomb exhaustion was replayed.

The first unresolved step is a readable sharp count for many comparison
layers jointly. The short-word experiments suggest a stronger inequality,
but this package stops before asserting that unproved extension. No global
novelty priority or algorithmic speedup claim is made.
