# Mixed-defect/span inputs for weak sources (0044)

Scope: targeted local map only. Let S=B disjoint union C be the diagonal classes of a proper weak two-color source, so B,C are disjoint Golomb sets, b=|B|, c=|C|, n=b+c, and

    delta(S)=2 binom(n,2)-T(S).

The two-Golomb statements below hold for arbitrary disjoint Golomb B,C; the later hole/support statements use the actual weak-source coloring.

## 1. Complete two-Golomb identity and exact defect split

[TWO_GOLOMB_MIXED_ENERGY_0040.md](../TWO_GOLOMB_MIXED_ENERGY_0040.md), Sections 1--3, defines shared within-class difference support rho, mixed supported-query mass N, and opposite-orientation mixed collision count Q, and proves exactly

    T(S)=2rho+N+Q.

With U=binom(b,2)+binom(c,2), it proves

    2rho<=U,  N<=2bc,  Q<=U,

where Q is charged injectively to cross-class equal-sum pair matches, with the repeated-pair cases included. Therefore

    delta(S)=(U-2rho)+(2bc-N)+(U-Q)>=0.

[WEAK_FIBER_CUBE_BALANCE_0041.md](../WEAK_FIBER_CUBE_BALANCE_0041.md), Section 3, records this same three-resource equality fiberwise as delta_d. This is the complete saved exact mixed-defect decomposition. It contains no span term and no claimed positive lower bound on delta beyond nonnegativity.

The attempted standalone strengthening N<=2bc-min(b,c) is explicitly false in TWO_GOLOMB_MIXED_ENERGY_0040.md, Section 4. Thus a linear N-deficit is unavailable without additional premises. The valid H2 bound instead uses Q and N jointly.

## 2. Actual weak properness: reflection shadows paid by geometric holes

[NESTED_REFLECTION_HOLE_BUDGET_0041.md](../NESTED_REFLECTION_HOLE_BUDGET_0041.md), Sections 2--5, uses the actual mixed cells and properness, beyond the Golomb partition. For every internal-reflection multiplicity mu_B(r) at an opposite-color mark, it forces two disjoint missing shadows of total size

    2 binom(mu_B(r),2).

For H=L+1-n interval holes and

    F=sum_(r in C) binom(mu_B(r),2)+sum_(r in B) binom(mu_C(r),2),

the saved exact packing is

    F<=H^+,  F<=H^-,  2F<=n(L+1-n).

The localized version is

    mu(mu-1)<=alpha+beta+1-|S intersect I_r|.

These are the strongest saved actual-color finite-span inequalities. They lower-bound required holes from *reflection multiplicities*, not any one of U-2rho, 2bc-N, or U-Q. The note states that no lower bound on the first reflection moment K is available, so they do not currently yield a positive universal lower bound on delta.

## 3. Actual weak properness: supported-difference missing positions

[WEAK_SOURCE_SUPPORTED_DIFFERENCES_0039.md](../WEAK_SOURCE_SUPPORTED_DIFFERENCES_0039.md), Sections 1--4, says that at an actual anchor a, same-diagonal-color later labels P have supported differences D which are Golomb and sum-free, with both endpoint/cross-cell colors forced. Its exact local missing-support count is

    binom(|P|,2)-|D|,

and its triangle-free/codegree-two support graph bound is

    |D| <= |P|/4 [1+sqrt(8|P|-7)].

This is a genuine properness refinement over arbitrary B,C. Its stated obstacle is overlap: missing numerical positions from different anchors need not be distinct. Consequently it has not been converted into a global span lower bound for delta or N.

## 4. Difference-support span bookkeeping, including a finite counter-limit

[fibers/WEAK_SOURCE_PRODUCT_SPAN_0035.md](../fibers/WEAK_SOURCE_PRODUCT_SPAN_0035.md), Section 3, gives the exact difference-support identity

    L-(b-1)(c-1)
      = U_0 + [(b-c)^2+b+c-2]/2 - R,

where R=|Delta B intersect Delta C| and U_0 is the number of positive interval lengths used by neither class. This is an exact span-versus-shared-difference dictionary, but R is a support count, not rho/N/Q and hence not delta.

The same file supplies a complete proper weak twelve-mark example violating the proposed product-span inequality by one, and proves only conditional replacements: hull overlap at most [(b-c)^2+b+c-2]/2, or the stated highly unbalanced regime. Thus the identity cannot be promoted to a general finite span lower bound on mixed defect.

## 5. Triple/query identities available for a weighted refinement

[GOLOMB_TRIPLE_FOREST_DICTIONARY_0042.md](../GOLOMB_TRIPLE_FOREST_DICTIONARY_0042.md), Sections 1--5, gives for one Golomb B the exact outside-query decomposition

    lambda_B(r)=2mu_B(r)+2nu_B(r)+delta_B(r),

its global totals, and the weighted identity

    sum_(r notin B) Q_B(r)=2(b-1) sum_(d in Delta B)d.

For a second class C, its selected contribution is N_B=sum_(r in C)lambda_B(r). It maps the unit reflection count to 2 sum_(r in C)mu_B(r). The file explicitly warns that restriction to C can discard much of the global total; it supplies no lower bound for N_B, selected reflection mass, or a weighted defect.

## Bounded conclusion

The saved exact defect identity is complete, and actual weak properness supplies two independent finite-span resources: reflection-shadow holes and anchor-supported missing differences. Neither resource has an established global injection into the three defect summands. Accordingly, the strongest recorded general lower bound on delta(S) remains delta(S)>=0; the displayed span inequalities are conditional/local refinements or bounds on reflection statistics, not a proved positive defect theorem.
