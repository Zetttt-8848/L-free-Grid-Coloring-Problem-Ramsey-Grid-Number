# Side-21 SAT encoding and cube split

Variable `X[x,y,c]`, numbered `3*(21*x+y)+c+1`, means cell `(x,y)` receives
zero-based color `c`, for `0<=x,y<21` and `c in {0,1,2}`.

Each cell has one ternary at-least-one clause and three binary at-most-one
clauses.  For every mandated geometric corner and color `c`, one negative
ternary clause forbids all three cells receiving `c`.  These clauses are
equivalent in both directions to a total three-color corner-free matrix.

Color symmetry is reduced by fixing `(0,0)` to color 0 and requiring color 2
not to occur before the first row-major occurrence of color 1.  Every color
orbit retains a representative: first permute the color at `(0,0)` to 0, then
swap the two residual colors if needed.  The exact clause accounting is:

| Family | Clauses |
|---|---:|
| exactly-one cell clauses | `4*441=1764` |
| monochromatic-corner clauses | `3*2870=8610` |
| before symmetry | `10374` |
| color-symmetry clauses | `441` |
| total | `10815` |

There are 1323 variables.  The deterministic DIMACS file has SHA-256
`49a989044d4255e7aba75a0b45256a7b480172b8f121545eeaf350164177f8e5`.

The split cells are `(0,1),(1,0),(1,1),(20,20)`.  The 81 cubes are every
element of `{0,1,2}^4`, expressed as four positive unit literals.  Restricting
any total coloring to these cells selects exactly one cube, so the cubes cover
the base instance and are pairwise disjoint.  The independent instance audit
reconstructed every clause from the property, compared the full clause
multiset, and separately checked the exact tuple set and literal map.

