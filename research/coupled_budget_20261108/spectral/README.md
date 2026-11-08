# Autocorrelation cuts: a tested continuation, still undecided

This route tests whether diagonal difference counts satisfying the usual
capacity and interval inequalities can also be the autocorrelation of actual
color classes. The runs did not produce an exact contradiction or a coloring.
They do not improve the restored bound 465.

## Necessary inequalities

For one color indicator f, extended by zero outside a diagonal of length n,
write r_h=sum_x f(x)f(x+h), with r_0=m. Every integer vector z satisfies

`m sum_i z_i^2 + 2 sum_(h>0) r_h sum_i z_i z_(i+h)
 = sum_x (sum_i z_i f(x+i))^2 >= 0`.

Thus its Toeplitz autocorrelation matrix is positive semidefinite. The
single-class scout uses m=ceil(n/3): any larger class can be restricted to
exactly m positions, preserving the necessary Golomb fiber capacities.

For a complete partition into three diagonal classes f_1,f_2,f_3, put
R_h=sum_c sum_x f_c(x)f_c(x+h). The centered correlation sequence is

`q_0=2n, q_h=3R_h-(n-h)` for `0<h<n`, zero outside this range.

It is positive semidefinite because it is the sum of the autocorrelations
of `f_1-f_2`, `f_1-f_3`, and `f_2-f_3`. In particular, with
`a_h=sum_i z_i z_(i+h)`, every integer vector z gives the exact inequality

`-6 sum_(h>0) a_h R_h <= 2n sum_i z_i^2 - 2 sum_(h>0)(n-h)a_h`.

This permits signed weights. Merely substituting upper bounds for R_h into
an expression with negative a_h would be invalid; the scout instead keeps
R_h as shared variables in all inequalities. Negative eigenvectors of a
floating candidate suggest cuts, and rounded integer vectors retain the
universally valid identity above. The LP solve and its status remain
floating computations, so infeasibility would still require an exact dual
certificate before becoming mathematical evidence.

The interval inequalities are also necessary. A length-t window has total
occupancy g across the three classes, so its squared class occupancies sum
to at least `(3-r)q^2+r(q+1)^2`, where `g=3q+r`, `0<=r<3`.
Sum this over every translated window and expand to obtain the rows in
`joint_scout.py`. The single-class version minimizes the analogous integer
sum of squares under pointwise window capacities and total mass mt.

## Executed runs

| Script and arguments | Actual time | Outcome |
|---|---:|---|
| `scout.py --n 492 --seconds 90 --output scout492.json` | See stored elapsed_seconds | UNDECIDED; floating outer approximation, no certificate |
| `joint_scout.py --n 464 --seconds 120 --output joint464.json` | See stored elapsed_seconds | UNDECIDED; floating outer approximation, no certificate |

Both were run from the repository root with their full relative paths and
`OPENBLAS_NUM_THREADS=1`. The second run stored 1164 integer cuts; its last
evaluated profile, after 1156 cuts, still had a negative centered eigenvalue. This is not a
feasible diagonal and is not evidence that the complete relaxation is
feasible. Time limits end exploration, not the mathematical question.

The joint scout's two-threshold capacities are valid only for `n<=481`,
using the two external Golomb inputs documented in
[`../numeric_upper/THEOREM.md`](../numeric_upper/THEOREM.md). Its executed
value is n=464. The single-class run uses the published 2025 occupied-position
table up through the thresholds needed at n=492; it is exploratory and is
not a dependency of either the 465 or 466 proof. Neither script is a general
unbounded-n capacity oracle.

`verify.py` uses only the Python standard library. It verifies executed
source hashes, all stored cut-vector domains, and the autocorrelation
identity by two independent sums for every three-color diagonal word
through n=7 and all kernel vectors in {-1,0,1}^3. These finite checks audit
the implementation formula; the squared-convolution proof supplies the
universal statement. It also checks that the stored runs make no exact
infeasibility claim.

## Next discriminating step

Seek an exact rational dual of a strengthened n=464 joint system, retaining
signed autocorrelation cuts and integer window corrections. If the finite
relaxation becomes infeasible, export rational multipliers and independently
verify every coefficient and contradiction. If it remains feasible, examine
its unrealizable higher correlations or cross-fiber completion conflicts.
No claim of optimality for this family of relaxations follows from these runs.
