# MX stage 2: what outside cells do (exact at k = 2, one instance at k = 3)

The entry point is set in `MX_STAGE1_RESULT.md`. **No claim about R_3 or R_4.**

## 1. k = 2: the outside-cell mechanism is TSD forcing (exact)

`mx_stage2_k2.py` takes every relaxed-feasible diagonal word with n = 5, 6, 7, up to swapping colors: 14 words. For each it finds a minimum-cardinality set of L's that already refutes the full square with that diagonal, using OptUx. Every core is re-checked by complete enumeration, both for UNSAT and for minimality. Results are in `mx_stage2_k2.json`.

**Observations (exact, for these 14 words).**
1. **No smallest core uses an upper-triangle cell.** All of them live on the diagonal, the same-class lower cells (S) and the mixed lower cells (M).
2. **Core sizes:** 9–10 L's at n = 5, 6–9 at n = 6, and 7 at n = 7.
3. **The smallest cores, 6 L's** (n = 6, words 001011 and 011001), are one mixed cell forced both ways. For 001011, A = {0,1,3} and B = {2,4,5}:
   - Corner L's force the A-pairs to color 1 and the B-pairs to color 0.
   - (1,0),(3,0),(3,2): (3,2) ≠ 1.
   - (3,2),(5,2),(5,4): (3,2) ≠ 0.
   - **General form.** A mixed cell (x, y), with x ∈ A and y ∈ B, is killed when x − a = y − u = d > 0 for some u < a in A, and b_1 − x = b_2 − y = d' > 0 for some b_2 < b_1 in B. In words: an A-pair, the mixed pair and a B-pair are translates of one another, in that order.
4. **The catalogue explains everything.** With the diagonal fixed, the lower-triangle problem at k = 2 is exactly a round-1 TSD instance on U = [0, n), with A and B the two diagonal classes. All 14 words are refuted by unit propagation alone (`conflict_check.analyse` and `propagation_and_search`):
   - at n = 6 by a C-collision or a type II conflict;
   - at n = 7 by type I and type II conflicts;
   - at n = 5 by longer propagation chains.

**Reading.** At k = 2 the information that the same-class relaxation discards is exactly the TSD forcing calculus that lane B already developed (`../siege/proof.md` §4.9–4.10, `PILOT2_RESULT.md`). It works because at k = 2 every same-class cell has a forced color.

## 2. k = 3: one refuted diagonal, no local gadget

`mx_stage2_k3_core.py` treats the n = 21 relaxed diagonal with no full extension: class sizes 10, 6, 5, from `mx_extension_probe.json`. Results are in `mx_stage2_k3_core.json`.
- **Core:** solving under assumptions gives a core of 856 L's. The time-limited deletion pass, which did not finish, reduced it to **828 L's** out of about 3,000. Glucose 4 confirms the restricted formula UNSAT.
- **Cells touched:** 87 mixed, 49 same-class, 17 diagonal and **19 upper** cells.
- **L types:** mixed cells dominate (MMM 176, MSM 124, SMM 100, ...).

So at k = 3 this refutation is global, not local, and upper cells take part. The k = 2 gadget does not transfer directly, because same-class cells now have two free colors and nothing forces them.

This is one instance with a non-minimal core: evidence only.

## 3. Consequence for the R_4 route

- At k = 4, same-class cells have three free colors. The k = 2 mechanism needs forced same-class colors.
- At k = 4 such forcing appears only through near-extremal rigidity: inside one fibre, the colors are constant on Golomb classes (P1 (iv); round 1, Prop. 4.7). That is exactly the setting of the TSD/NTSD analysis, whose consumer is vacuous at the R_4 scale (Theorem R).
- Cross-class mixed cells between different diagonal classes D_c and D_{c'} add new L's. On this evidence, though, they are refuted only by large global cores, not by a local lemma that could be counted.

**Recommendation.**
- **Stop MX as an R_4 route here.** Stage 2 found no local mechanism beyond the one lane B already had, and that one has no near-scale consumer.
- **Keep two durable outputs:**
  - the floor statement (`MX_STAGE1_RESULT.md` §Reading 3): any method using only same-class information cannot beat n_rel(k) + 1;
  - the identification of k = 2 outside-cell forcing with TSD forcing.
- **R_3 note (outside the R_4 pair campaign):**
  - The 3-color chain's best reported value, R_3 ≤ 144 (PR 11 head, not adopted here), sits well above the floor of 62.
  - The exact value of n_rel(3) would show how much of that chain is slack inside the relaxation itself, which more same-class analysis could still remove.
  - Computing it means pushing the stage-1 SAT scan past n = 61. That is the only cheap follow-up with a concrete consumer.

## Reproduction

```text
python mx_stage2_k2.py
python mx_stage2_k3_core.py 520
```

Both run from this directory. The second reads `mx_extension_probe.json`.
