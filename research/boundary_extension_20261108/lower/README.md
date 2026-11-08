# A frozen 20-square is not an extendable seed

**The R3 lower bound does not change.** This directory develops an exact
boundary-signature reduction and certifies that the published 20-by-20
matrix cannot be extended even by one full row or column on any side.
For extension to a 21-square, certified disjoint obstruction supports also
give necessary interior-repair lower bounds. These statements concern this
specific frozen matrix, not every 20-square and not nonexistence of a 21-square.

Base checkpoint: `080822bb1d434b164a1f42ea159d0bf148396b71`.
Owner: lower-bound work package in the 2026-11-08 boundary-extension research.
Coordinates are zero-based. Exactly `(x,y),(x+d,y),(x+d,y+d)`, d>0,
is forbidden; rotated shapes are not silently added.

## Results and their logical scope

1. **PROVED (elementary geometric reduction).** A bottom/right extension
   factors into independent right-column color lists and a color-labelled
   complete graph on the new row. Other placements have the exact residual
   hyperedge description in [THEOREM.md](THEOREM.md); in particular, a
   bottom/left shell includes genuine three-new-cell constraints. This is
   not a claim of literature priority, nor a universally binary encoding.
2. **FINITE-CHECKED.** The input is a proper 20-square: all 400 cells and
   2,470 directed L's were checked, with zero monochromatic L's.
3. **FINITE-CHECKED.** The top and right extensions have direct three-color
   exclusions. The bottom and left extensions fail for nonlocal reasons:
   an unsatisfiable binary core has respectively 41 edges on 14 row cells,
   and 38 edges on 15 column cells. Their complete branching certificates
   have 24 and 18 nodes. Each edge has a witness showing the remaining core
   is satisfiable after that edge is deleted: the cores are inclusion-minimal,
   **not proved minimum-cardinality**.
4. **PROVED implication + FINITE-CHECKED certificates.** Any successful
   extension must change an old cell from each obstruction's old-cell support.
   Pairwise disjoint supports force the following repair lower bounds:

| Old-matrix offset in 21-square | New sides | Disjoint certified cores | At least this many old colors must change |
|---|---|---:|---:|
| `(0,0)` | bottom and right | 10 | 10 |
| `(0,1)` | bottom and left | 2 | 2 |
| `(1,0)` | top and right | 14 | 14 |
| `(1,1)` | top and left | 8 | 8 |

An offset means old cell `(x,y)` is fixed at `(x+ox,y+oy)`. These are lower
bounds on changed old cells, not the number of new shell cells. The packing
is greedy and has no maximum-packing claim. Meeting a bound is not sufficient
to make an extension possible. In particular, a successful 21-square in any
of these four placements must differ from this seed in at least two old cells;
this does not address embeddings with inserted interior rows/columns.

## Evidence and independent checking

`paper20.json` reproduces the matrix attributed to Mammel–Smith–Yerger,
[arXiv:2502.05162v1, Figure 3](https://arxiv.org/html/2502.05162v1#S3).
It was obtained from the project skill's attributed benchmark; this package
does not claim a fresh transcription audit of that figure. Input SHA-256:
`98d96c87b67a539151b40159fec4d399eb8a205e6769271eaeec4b7240c2cccd`.

`extension.py` reduces actual geometric L's to residual forbidden-color
constraints. PySAT/Glucose is used to discover and shrink cores and produce
positive deletion witnesses. A separate finite backtracker produces proof
trees. `pack_cores.py` removes all constraints touching already-used old cells
and extracts additional cores with disjoint supports.

`verify.py` uses only the Python standard library and imports neither discovery
script. It regenerates the input L's from their bends, validates each certificate
triple directly, checks every fixed color, recomputes constraint propagation
using sets, verifies that each branch covers every remaining color, checks
all positive deletion witnesses, and checks the exact old-cell support and
disjointness of every packed core. The complete stored package requires
239 proof-tree nodes, in addition to the positive witnesses. Correctness of
the negative claims therefore does not rely on a solver's UNSAT status.

This is a separate implementation by the same work-package author. Fresh-agent
and root reviews are recorded in the parent research directory, separately from
this implementation check. Neither these scripts nor the theorem were Lean-formalized.

## Reproduce

From the repository root, use Python 3.10 or later:

```sh
python research/boundary_extension_20261108/lower/verify.py --output /path/to/fresh_lower_verification.json
```

To rediscover certificates, PySAT is also required. Write to a fresh directory
and copy `paper20.json` there for the independent checker:

```sh
python research/boundary_extension_20261108/lower/extension.py --output /path/to/new_run/extension_results.json
python research/boundary_extension_20261108/lower/pack_cores.py --output /path/to/new_run/packing_results.json
python research/boundary_extension_20261108/lower/verify.py --directory /path/to/new_run --output /path/to/new_run/verification_results.json
```

Executed environment: Python 3.13.5, python-sat 1.9.dev15, Glucose 4.1 (`g4`),
Windows 11. No random sampling or symmetry constraints were used. Recorded
discovery times were about 0.062 s and 0.111 s in this environment; these are
provenance only, not a speed comparison. Core-deletion solver calls had no
per-call time limit; each proof-tree attempt had a 60-second check and packing
had a 15-core iteration cap. The recorded runs finished normally before either
cap. Independent verification is fast and deterministic; its actual run
manifest and review hashes are maintained by the parent checkpoint.

## Research consequence and next discriminator

The existing seed is locally saturated in all four axial directions. Freezing
it and repeatedly restarting a shell solver cannot produce a new lower bound.
The next construction experiment should allow actual interior changes and use
the certified support sets as necessary hitting conditions for choosing a
repair neighborhood. This is a new diagnostic for this package, not a claimed
new general SAT technique. It remains necessary to recheck every L wholly
inside the old region as well as every crossing L after repair.

No relaxed 21-square construction search was run in this package; its
existence remains UNDECIDED. A useful next test is whether neighborhoods that
meet all certified supports admit a proper repaired interior and extension,
compared with the same number of freely selected old cells under equal total
budgets. Failure of one such neighborhood would constrain that neighborhood
only. The universal extension reduction works for any k, but these finite
cores and repair bounds are certified for k=3 only.
