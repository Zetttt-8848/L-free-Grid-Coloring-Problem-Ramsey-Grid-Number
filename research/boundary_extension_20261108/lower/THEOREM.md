# Exact boundary signatures for one-layer extensions

Base: `080822bb1d434b164a1f42ea159d0bf148396b71`. This is an elementary
geometric reduction and its application to a published matrix, not a claim
of literature priority or a new bound on R3. The original target remains open.

## 1. Bottom/right extension theorem (all n and k)

Let c be any proper k-coloring of `{0,...,n-1}^2`, where the only forbidden
triple is `(x,y),(x+d,y),(x+d,y+d)`, d a positive integer. Extend to
`{0,...,n}^2` while fixing all old colors. Write `b_j=c'(n,j)` for
`0<=j<=n` and `r_i=c'(i,n)` for `0<=i<n`. Define

```
F_i = {c(i-d,n-d): 1<=d<=i and c(i-d,n-d)=c(i,n-d)}.
```

**Theorem (PROVED).** Such an extension exists if and only if:

1. each right-column list `[k] \ F_i` is nonempty; and
2. the vertices `0,...,n` can be assigned colors b such that for each
   `0<=j<l<=n`, the pair `(b_j,b_l)` is not `(a,a)`, where
   `a=c(n-l+j,j)`.

The choices of the r_i are mutually independent and independent of the b_j.

**Proof.** An L not wholly old must have bend row x+d=n or completion
column y+d=n. If x+d=n, let j=y and l=y+d; it is precisely
`(n-l+j,j),(n,j),(n,l)`, giving condition 2. If x+d=i<n and y+d=n,
then d<=i, and the L is `(i-d,n-d),(i,n-d),(i,n)`. Its first two
colors are old. It restricts r_i exactly when they agree, giving condition 1.
The two cases are disjoint and cover all new L's. Conversely, either condition
prevents every L in its case from being monochromatic, and the old square
was proper. This proves both directions without a symmetry restriction. ∎

For k=3 this is a color-labelled graph constraint problem, not automatically
2-SAT: a vertex may retain all three colors. If additional valid constraints
leave at most two colors per vertex, introducing a Boolean choice for each
two-element list converts every forbidden equal-color pair into a clause of
length at most two. Empty lists refute extension; singleton lists propagate.
No unproved symmetry, periodicity, or omitted cross-boundary step is used.

## 2. All placements and single-side versions

For offset `(ox,oy)` in `{0,1}^2`, fix the old matrix at
`c'(x+ox,y+oy)=c(x,y)`. The residual boundary signature consists, for each
actual L, of the following exact constraints:

- old fixed colors contain two distinct colors: discard that L;
- old fixed colors are nonempty and all equal a: forbid all remaining
  boundary cells of this L from simultaneously receiving a;
- no fixed cell: forbid the boundary triple from being monochromatic in
  each of k colors.

If all cells are fixed the old properness check applies. This is necessary
and sufficient simply by conditioning each original L constraint on the fixed
assignment. In particular, placement `(0,1)` (new left column and bottom row)
has L's with three boundary cells, so a universal pairwise reduction would be
incorrect. Its boundary triple `(n-d,0),(n,0),(n,d)` must be retained.

The *single bottom row* of an n-by-n square is simpler: vertices `0,...,n-1`
have the forbidden equal-color pair labelled `c(n-l+j,j)` for every j<l.
The *single left column*, after moving the old matrix one column right, has
vertices `0,...,n-1` and label `c(l,l-j-1)` on j<l. Each has exactly one
old cell per crossing L, so these conditions are both necessary and sufficient.
The top and right single-side extensions have independent unary exclusion
lists (two old cells and one new cell per crossing L).

## 3. Obstruction and repair consequence

Let H be any unsatisfiable subset of a residual signature. Every proper
extension must change at least one old color used to justify a constraint in H.
Otherwise all H constraints remain enforced on the new cells, contradicting
their unsatisfiability. For several such cores the changed old cells must hit
the support of every core. This is a necessary repair condition, not sufficient:
changing those cells can create other L's, including wholly old L's.

For single-row/column binary cores, every edge depends on exactly one old
cell. Distinct edges have distinct old cells by the displayed formulas.
An edge-deletion-minimal core therefore gives an irredundant *sub-obstruction*:
every retained edge is necessary within that core. This does not establish
minimum cardinality among all cores or a minimum number of interior changes.

The theorem holds for arbitrary k. The finite application in this directory
uses k=3 only. A valid constructed n-square gives R_k>=n+1; a frozen
extension obstruction has no global Ramsey-bound implication.
