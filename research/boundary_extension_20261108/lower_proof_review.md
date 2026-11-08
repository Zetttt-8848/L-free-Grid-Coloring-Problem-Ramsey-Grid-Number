# Independent review: exact boundary extension theorem

Verdict: **proved as written**, with the usual domain n≥1 and k≥1 understood
for an n-square and k-coloring. The source reviewed is `lower/THEOREM.md`,
in the new research package based on commit
`080822bb1d434b164a1f42ea159d0bf148396b71`.

Review provenance: upper-route researcher, separately assigned to reconstruct
the lower theorem directly from the geometric definition. The lower author's
implementation and finite results were not used in the derivation below.
This reviews the theorem, not the author's separate core certificates or
discovery claims. The independent review does not establish novelty.

## Claim and dependency chain

A proper coloring of the old n-square is frozen. Every new equal-leg directed
L must either have its bend in the new bottom row or have its final point in
the new right column above that row. This partition gives independent unary
right-column exclusions and binary bottom-row constraints. Other placements
follow by conditioning each geometric constraint. A surviving unsatisfiable
subcollection forces a change to at least one old support cell.

All leaves are elementary geometry or Boolean conditioning. No outside theorem,
solver status, symmetry reduction, or inherited Ramsey bound is used.

## Obligation checks

| Obligation | Status | Independent derivation |
|---|---|---|
| Completeness of bottom/right partition | passed | If the bend row x+d<n and final column y+d<n, all three points are old. Otherwise bend row is n, or final column is n with bend row<n. |
| Bottom label and range | passed | Write j=y, l=y+d. Then x=n−l+j and 0≤j<l≤n. Thus x is an old row, j an old column, and the two other vertices are bottom cells. |
| Right unary exclusions | passed | For bend row i<n, y+d=n gives first two cells (i−d,n−d),(i,n−d), with 1≤d≤i. Exactly their equal colors are excluded from r_i. |
| Corner-cell overlap | passed | (n,n) is b_n; r_i is defined only for i<n. The partition never adds a unary constraint to b_n or a bottom constraint to r_i. |
| Independence of right choices | passed | An L in the right case contains exactly one right variable and two old cells. No L mixes a right variable above row n with a bottom variable. |
| Single-bottom formula | passed | Same label c(n−l+j,j), now with 0≤j<l<n because the width remains n. |
| Single-left formula | passed | New cells (j,0),(l,0) give d=l−j; completion (l,d) is old original cell (l,d−1), giving c(l,l−j−1). |
| Single-top and single-right unary form | passed | A top L contains one new first point; a right L contains one new final point. The other two points are old. |
| All-placement conditioning | passed | Distinct fixed colors discharge the NAE condition; equal nonempty fixed colors forbid the remaining cells all taking that color; no fixed colors retain the full NAE. All-fixed conditions are covered by properness. |
| Three-boundary-cell case | passed | For placement (0,1), (n−d,0),(n,0),(n,d) are all new when 1≤d≤n. It is essential that these constraints are retained. |
| 2-SAT qualification | passed | With at most two admissible colors per vertex, each forbidden pair assignment maps to a Boolean clause of length ≤2. Three unrestricted colors do not meet this condition. |
| Necessary repair consequence | passed | If every old support color of an unsatisfiable residual core stays fixed, the same core remains enforced; a proper extension would contradict its unsatisfiability. Hitting the supports need not suffice. |
| Distinct edges have distinct old support cells | passed | Bottom map (j,l)→(n−l+j,j) and left map (j,l)→(l,l−j−1) each have an explicit inverse. |
| Minimal-core wording | passed | Edge-deletion minimality is stated only within the selected core; no minimum-cardinality or minimum-repair inference is made. |

## Finite cross-check

`audit_lower_theorem.py` is a separate standard-library implementation. For
each listed (n,k), it visits every proper old matrix and every full assignment
of the newly introduced cells, comparing the explicit formulas against direct
geometric testing of the full rectangle. Results are in
`lower_theorem_audit.json`.

| n | k | Proper old matrices | Bottom/right assignments | Single-bottom assignments | Single-left assignments |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 16 | 4 | 4 |
| 2 | 2 | 12 | 384 | 48 | 48 |
| 3 | 2 | 108 | 13,824 | 864 | 864 |
| 1 | 3 | 3 | 81 | 9 | 9 |
| 2 | 3 | 72 | 17,496 | 648 | 648 |

All comparisons passed. This corroborates indexing and boundary cases;
the universal theorem rests on the geometric derivation, not on these finite
counts. The all-placement generic residual claim was checked analytically;
this independent script does not claim exhaustive all-placement enumeration.

Command from the repository root:

```sh
python research/boundary_extension_20261108/audit_lower_theorem.py
```

Remaining mathematical gap to a new R3 result: an obstruction to extension of
one frozen matrix does not exclude all larger squares. Conversely, candidate
repairs must satisfy all original constraints, including those wholly inside
the old region after recoloring. The reviewed theorem correctly retains both
limitations.
