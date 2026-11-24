# Extending the 20 by 21 rectangle requires changes across the board

Any proper 21 by 21 square obtained by appending a row to the [specified rectangle](RECTANGLE_20_21.md) and recoloring existing cells must change cells in **at least 14 of the 20 old rows and 15 of the 21 columns**. In particular a search that retains seven whole original rows or seven whole original columns can end immediately. The new row may use arbitrary colors. In the column claim the comparison uses only the 20 original cells. Both conclusions also apply after any common renaming of the palette.

## Formula

Introduce three Boolean variables per cell of the 21 by 21 square. Exactly one is true. For each of the 2,870 directed equal-leg Ls and each color, forbid assigning that color to all three of its cells. A separate selector for each original line implies all its old cell colors. Assert that at least seven selectors are true. If this formula has a model, its grid is a completion retaining at least seven specified lines. Conversely, any such completion produces a model by selecting its unchanged lines.

The cardinality flags use prefixes of the selector sequence. A true flag at $(i,k)$ requires either a true flag at $(i-1,k)$, or the selection of line $i$ together with a true flag at $(i-1,k-1)$. The latter flag is automatic when $k=1$. Induction proves that each true flag witnesses at least $k$ selections. Given enough selected lines, their actual prefix counts supply flags satisfying every clause. The last flag requires seven retained lines.

## Checked refutations

Both formulas were refuted by Glucose 4 using python-sat 1.9.dev17. The proofs were trimmed and independently checked in RUP-only mode with drat-trim. The compact checker in this directory rebuilds them from the literal grid. The successful run produced these trimmed proof digests.

| Fixed lines | Uncompressed RUP bytes | RUP SHA-256 |
|---|---:|---|
| Rows | 34,832,122 | `ded3340ea665bab55d43d385805869967e7eaeff96e32e76e88b2e899c7323da` |
| Columns | 80,064,771 | `f3189f859b1a8c5e05bfd217a184b70b740d5156efff03b9167a38eb0de7c678` |

Install python-sat and build [drat-trim](https://github.com/marijnheule/drat-trim). Run **python verify_rectangle_lines.py /path/to/drat-trim**. The option **--cache /path/to/proofs** retains compressed proofs for later RUP-only verification with the Python standard library. The checker accepts any independently valid refutation of the same reconstructed formula, including one produced by a different solver version.
