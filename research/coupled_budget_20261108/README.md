# Three-color joint constraints, historical 465 review and structural repair obstacles

Date: 2026-11-08. Basic submission:`df6e35cfff68580dc78aa91bc35d4c6399a6464a`, undertake PR4. Fixed positive step length equi-arm directed L:`(x,y),(x+d,y),(x+d,y+d)`,`d>0`, the code coordinates start from 0.

In this round, the range adopted for the project is:`21≤R3≤493`updated to **`21≤R3≤465`**. 465 from a re-verified historical direct convolution proof: its external Golomb input is now verified to the original calculation completion announcement, and the full derivation and integer calculations are independently reviewed. It is not a new discovery this round, nor does it rely on G9, S21 or the failed rainbow hypothesis. The lower bound is still 21; no normal 21×21 square has been found, and the exact value is still undetermined.

## Results and scope of evidence

| Results | Status | Location |
|---|---|---|
| Restore historical upper bound 465; convolution contradiction 285630 | PROVED, using certified external computation theorem | [Proof and source](numeric_upper/THEOREM.md),[Independent review](structural/UPPER_PROOF_REVIEW.md) |
| General k-type joint endpoint lemma, three colors give 466; contradiction amount 221 | PROVED, the expression of new derivation in this round; no global priority is claimed | [Lemma and complete application](numeric_upper/THEOREM.md) |
| 34 proven boundary kernels generate 22680 full 21 square valid redundant constraints | PROVED mechanism and FINITE-CHECKED instances; no speedup demonstrated | [Construction route](lower/README.md), [strict proposition](lower/THEOREMS.md) |
| The complete 21 square has only one single color L, but there is no normal repair within a radius of 10 | FINITE-CHECKED; the candidate itself is illegal, any repair will change at least 11 squares | [Full certificate](lower/defect_certified.json),[independent verifier](lower/verify_defect.py) |
| Forced local imbalances in nine-mark sources are canceled in ten-mark extensions | FINITE-CHECKED counterexample; secure full-fiber billing lemma to be listed separately | [Structural Proofs and Certificates](structural/README.md) |
| n=464 three-color joint autocorrelation constraints, n=492 single-class constraint exploration | UNDECIDED; no exact infeasibility certificate or valid construction | [Operating ranges and identities](spectral/README.md) |

## Upper bound: let three colors share the same set of endpoints and windows

The old single-class interval estimation uses the two ends of the diagonal separately. The new endpoint lemma treats the three categories as divisions of the same diagonal: the endpoint position can only be occupied once. Each class selects point pairs whose rank difference does not exceed c, and the maximum value of the sum of the lengths of all point pairs is obtained by rearranging three identical positive and negative coefficients; this controls competition missed by class-by-class estimation. Taking n=466 and c=22, the sum of the lengths is at least 319760 and at most 319539, resulting in a contradiction. The class size lower bound is derived from the capacity constraint without assuming equal distribution of the three colors.

Joint convolution also utilizes the sum of three color indicator functions equal to the complete diagonal. historical triangle weight`w_i=min(i,94-i)`,`1≤i≤93`, the positive contradiction quantity has been given at n=465. A review found that this proof is independent of the failed rainbow route; the previous classification that dismissed all historical small upper bounds was too broad. This time, only 465, which has been reviewed item by item, will be restored, and other old numbers such as 459, 455, 454, etc. will not be restored.

Both proofs require only outer span lower bounds`G(24)≥425`,`G(25)≥480`, respectively by [OGR-24](https://blogs.distributed.net/2004/11/)With [OGR-25](https://blogs.distributed.net/2008/10/)The original completion announcement is supported and cross-checked with the position number table in the 2025 paper. Using established external theorems does not make the conclusion a conditional bound that relies on open conjectures; but there is no local rerun of its massive exhaustive search this round. This evidence boundary was retained for both the full paper and the independent review.

The author's implementation and independent review of the implementation are consistent with Wolfram's integer complex calculations. The seven values ​​returned by Wolfram are, in order`69231,2038439,366786,53496528,285630,319760,319539`;This is just an arithmetic cross-check and does not replace the geometric proof or the proof of external Golomb optimality.

## Lower bound and structure: convert failure into reusable constraints

The lower bound work freed up the old 20-square internal grid, running adaptive repairs, full 21-square SAT, and full-square local searches. A complete candidate is only in`((14,6),(17,6),(17,9))`Produces a single color L. However, the complete branch certificate proves that there is no normal coloring within a radius of 10, and the maximum certificate covers 1235525 branch nodes. The number of monochromatic angles and the repair distance must therefore be measured separately. This conclusion is for a fixed candidate, not the general impossibility of the 21-square.

Structure route found`B={0,1,2,3,4,6,7,9,10}`: Its 36-grid complete strict source has exactly four normal two-colors, all with a potential of 8, which is higher than the odd-even lower limit of 4. However, after adding the mark 14, the complete 45-grid source has a potential of 7, which is exactly equal to the lower parity limit of 7 for all sources; the external same-fiber grid offsets the local forced imbalance. This again denies direct accumulation of local costs, while giving the metachromatic component constraint and fractional packing lemma that should be used on intact fibers. To deduce the general source boundary, the total amount of forced edges must still be controlled independently.

The auxiliary variable numbering error in the discovery phase is clearly marked as an implementation error and cannot be used as a counterexample. Modified limited classification uses independent full branch certificate. All timeouts, incomplete solutions, and floating point explorations retain the actual scope and are not upgraded to impossibility proofs.

## Reproduction and verification

Exact verification uses the Python standard library. Optional dependencies and commands for the discovery phase are found in the respective subdirectories; there is no requirement to install a solver to check the master certificate.

```sh
python research/coupled_budget_20261108/numeric_upper/verify.py
python research/coupled_budget_20261108/lower/verify.py
python research/coupled_budget_20261108/lower/verify_defect.py
python research/coupled_budget_20261108/structural/check_branch_proof.py
python research/coupled_budget_20261108/structural/verify_extension.py
python research/coupled_budget_20261108/structural/audit_joint_bound.py
python research/coupled_budget_20261108/structural/audit_convolution.py
python research/coupled_budget_20261108/spectral/verify.py
```

There are also Mathbox bounded run lists in the Nether and Structure subdirectories. The endpoint implementation checks 15168 small split/truncation instances for precision; the autocorrelation implementation checks 88533 small sequence/kernel instances. Realization is verified by limited inspection, and universal propositions are undertaken by written proofs. There is no claim to have completed Lean formalization, complete main manuscript review, or global literature priority review in this round. The main manuscript remains as is, and new proofs are available for review in this research directory.

## Next step of identification task

1. **Upper bound 464:** Retain signed autocorrelation constraints on three-color joint difference variables and find derivable rational dual certificates; must be accurately verified coefficient by coefficient. If finite relaxation is still feasible, analyze the higher-order dependencies or shared completion conditions it violates.
2. **Lower bound 22:** Continue from the complete 21 candidates with different structures or the joint color change of at least 11 grids, and use the certified kernel to screen the neighborhood; only the complete grid points that pass the verification can be written`R3≥22`. The current certificate does not indicate that 11 squares are sufficient.
3. **Source structure: **Only charge the complete fiber including external contributions, and find the forced edge budget that is established at the same time; the local imbalance lower bound alone cannot compress R3.

Generally, the endpoint lemma of the k class can be directly generalized; the two-Golomb decomposition in three-color numerical applications essentially uses two-color weak sources. This capacity conclusion cannot be directly applied to the four colors, and no independent four-color large-scale search was launched in this round.
