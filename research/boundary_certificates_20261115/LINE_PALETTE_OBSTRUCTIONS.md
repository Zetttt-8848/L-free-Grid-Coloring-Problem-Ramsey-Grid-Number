# Independent color permutations on every row and column

Start from the [20 by 21 rectangle](RECTANGLE_20_21.md). Choose an arbitrary permutation of the three colors for each original row and another for each column. Apply all row permutations followed by all column permutations. Whatever the choices, the resulting rectangle has no extension to a proper 21 by 21 square by appending a row. The same statement holds if all column permutations precede all row permutations. The new row has 21 freely chosen colors.

For the separate [one-defect square](REPAIR_21.md), both orders of row and column palette permutations also always leave at least one monochromatic directed L. These obstructions include recolorings that affect every original row and column.

## Formula and symmetry

Use one three-by-three permutation matrix for each row and column. Exactly one entry in each matrix row and column is true. Each board cell has exactly one color. At a cell of original color $t$, a first map sending $t$ to $i$ and a second map sending $i$ to $c$ together imply final color $c$. Every directed L on the square forbids all three monochromatic assignments. In the rectangle problem the appended row has no mapping implications.

The first map at line zero can be fixed to the identity by changing all intermediate color names and applying the inverse change to every second map. A global change of final color names then fixes the second map at line zero to the identity. Properness is invariant under that global change. These two normalizations therefore preserve the existence of a solution in both operation orders.

The four resulting formulas were refuted with Glucose 4. Each trimmed proof was checked independently in reverse unit propagation mode. Run **python verify_line_palettes.py /path/to/drat-trim --cache /path/to/proofs**. The first run uses python-sat and drat-trim. Existing cached proofs can be checked with drat-trim and Python's standard library.
