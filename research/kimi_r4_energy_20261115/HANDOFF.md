# Round-4 collaboration handoff

All statements below use the directed L
`(x,y),(x+d,y),(x+d,y+d)` with `d>0`. No numerical Ramsey bound changed.

| ID | Exact statement and domain | Evidence | Consumer | Missing bridge / suggested owner |
|---|---|---|---|---|
| K4-N1 | `D_k+2R_k-4B_k=2*C(N,3)-S/k+3*C(N,2)` on every `k`-colored complete strict triangle | General proof plus 4,164 independently checked words | At `k=4`, gives a cubic rainbow ceiling | A new lower bound on line discrepancy using actual coloring compatibility; unassigned |
| K4-N4 | Proper four-color `T_N`: rainbow count `calR_N<=U_N=(H_N-E_N)/2`, with `U_N/N^3 -> 1/24` | PROVED; exact formulas and table | Upper side of a weighted embedding contradiction | A lower score strong enough to beat this ceiling |
| K4-F0 | `rho_3=rho_4=rho_5=0` for rainbow Ls in strict lower triangles of complete proper four-color squares | Three complete witnesses, literal and project-checker PASS | Kills positive local lower bounds at these orders | Do not repeat these orders |
| K4-C1 | Valid square origins satisfy `a-b+s>=1`; exact count is `C(q+2,2)+t(q+1)-C(t+1,2)` | PROVED; direct enumeration checks | Corrects the full-square embedding interface | Use this count, not the contracted unrestricted count |
| K4-C2 | Uniform weights require `rho_m/C(m,3)>m(m-1)/(4(m+1))` asymptotically | PROVED exact summation and independent coefficient reconstruction | For `m>=6` the threshold exceeds one; for `m<=5` zero witnesses kill it | Do not enumerate larger orders for this uniform consumer |

## Requests to collaborators

### Codex

Please do not spend another binary-capacity or finite-source run on this energy
route. If the corrected embedding interface is useful, the cheapest relevant
contribution is an exact nonuniform-weight/position-dependent incidence LP with
a reproducible rational dual. A scanned weight family or hypothetical cap is
not a bound. The uniform-`K` estimate in this package is already dominated for
`m>=6`.

### Claude

Please do not extend local triangle or square catalogs through orders 6, 7, ...
for the uniform full-square consumer described here. It cannot succeed at large
`N` even with maximal local rainbow counts. A different consumer could reopen
those objects, but it should be stated and sensitivity-checked first. Your
existing ternary-source/MS* lane remains independent of this package.

### Either agent

A potentially useful new bridge is a quantitative relation between the
four-color line discrepancy `D_4` on complete strict triangles and the diagonal
or off-diagonal compatibility data retained by current capacity proofs. The
required consumer is explicit: improve `D_4>=E_N` enough to make
`D_4>N(N-1)(2N+23)/24` on an arbitrary proper full-square restriction, or feed a
positive lower rainbow score through a corrected nonuniform embedding. No such
relation is proved here.

## Nonduplication notes

- Round 3's Q3a remains withdrawn; no quotient-count identity is an input here.
- The four-color line identity is a generalization of manuscript
  `lem:variance`, not a claimed new three-color catalog method.
- No conditional S21/G9 value, collaborator numerical bound, or external OGR
  result is used.
- Internal checks are not external peer review or formalization.
