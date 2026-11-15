# A proper 21-square differs from the one-defect grid in at least 18 cells

The [one-defect grid](../coupled_budget_20261108/lower/runs/local71.json) has one monochromatic directed equal-leg L, with cells \((14,6),(17,6),(17,9)\). For each of the three colors, **at least 12 cells must change their membership in that color** on the way to any proper 21-square. Each cell recoloring changes the membership of exactly two colors. Hence at least \(3\cdot12/2=18\) cells must change. The [earlier deletion search](../coupled_budget_20261108/lower/THEOREMS.md) excluded changes in at most ten cells. Both results concern the specified full grid.

Fix a color \(c\) and write \(S\) for the cells that would use \(c\) in a proper coloring. Every geometric L must have a cell outside \(S\). Conversely, every subset \(P\) that cannot be properly colored using two colors must meet \(S\). These are necessary conditions for the entire grid. Both kinds of condition are disjunctions in the 441 variables indicating whether membership in \(c\) changes relative to the seed.

**repair_21_cores.json.xz** lists 1,450, 1,668, and 821 such subsets for the three respective colors. The verifier checks every one directly. Within each subset it reconstructs every directed L and tries both colors. Two equal cells in a triple force the opposite color on its third cell. When propagation ends, the verifier branches on both possibilities for an uncolored cell. Fixing one cell's color uses the global exchange of the two colors.

The full-grid check starts with no membership edits. Whenever a required disjunction fails, any successful continuation must change at least one still available cell in it. The checker orders these alternatives and branches by the first one changed. Pairwise disjoint sets of available cells in failed disjunctions give a lower bound on the additional number of edits. The exhaustive search gives the following counts.

| Color | Two-color obstructions | Total disjunctions | Nodes at edit budget 11 | Feasible |
|---:|---:|---:|---:|---|
| 0 | 1,450 | 4,320 | 4,548,791 | No |
| 1 | 1,668 | 4,538 | 3,510,705 | No |
| 2 | 821 | 3,691 | 1,048,867 | No |

Compile **verify_repair_master.c** with an optimizing C99 compiler. Run **python verify_projected_repair.py ./verify_repair_master**, supplying the compiled executable's path. The verification uses the Python standard library and the C checker. The 3,939 sets were found by alternating a proposed color class with a search for a two-color obstruction in its complement.
