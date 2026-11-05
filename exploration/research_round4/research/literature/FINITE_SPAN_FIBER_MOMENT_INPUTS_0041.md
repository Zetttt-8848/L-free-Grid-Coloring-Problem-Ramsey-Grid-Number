# Finite-span fiber-moment inputs (0041)

This six-file local map separates already-derived ingredients from the new question of summing weak-fiber \(H2\) information at span at most \(99994\). No calculation or proof review is performed here.

## 1. The new weak-fiber energy input is already a class theorem

`TWO_GOLOMB_MIXED_ENERGY_0040.md` proves for a disjoint union \(S=B\sqcup C\) of two integer Golomb classes, \(n=|S|\),
\[
T(S)\le2{n\choose2},\qquad E(S)\le6n^2-5n.
\]
Every proper weak two-color source has its two diagonal color classes in this form. Thus, for a proper strict source, the actual translated weak fiber \(W(F_d)\) has this \(H2\) bound with \(n=r_d\). The note explicitly says this does not by itself give an energy or source-size bound after summing over the different \(d\)'s.

## 2. Existing finite-span moment transfer is a shifted-window inequality

`FINITE_SOURCE_SIZE_TARGET_0018.md` records the finite shift-count formula: if a mark set \(D\) of size \(a\), span at most \(L\), has \(r_D(h)\le W\) for every positive \(h\), then for every integer \(t\ge1\),
\[
a^2t\le(L+t)[a+W(t-1)].
\]
It follows by summing the square of \(g(x)=\sum_{i=0}^{t-1}{\bf1}_D(x-i)\). This is the existing finite-span double count used in the S21 conditional four-color transfer. That transfer obtains a *uniform* \(W\) by applying S21 separately to signed subfibers; it does not sum \(E(F_d)\), \(T(F_d)\), cube counts, or Gowers norms across \(d\).

## 3. Local weak supported-difference capacity, with its overlap warning

`WEAK_SOURCE_SUPPORTED_DIFFERENCES_0039.md` proves in one weak source \(W(S)\), at each diagonal anchor \(a\), that a same-diagonal-color label set \(P\) has supported difference set \(D\) which is Golomb and sum-free. Its support graph is triangle-free with codegree at most two and satisfies
\[
|D|\le {t\over4}(1+\sqrt{8t-7}),\qquad
\#\{h\in\Delta P:a+h\notin S\}={t\choose2}-|D|,
\quad t=|P|.
\]
The note expressly says the excluded numerical positions can recur for different anchors, so these local deficits cannot simply be summed. Its four-cycle construction also survives in the weak formulation.

## 4. Internal reflection moment and the one-output limit

`WEAK_REFLECTION_POSITION_BUDGET_0040.md` gives a two-color positional reflection bound. For diagonal Golomb classes \(B,C\), it defines \(\mu_B(r)=\#\{a<t<q\in B:r=a+q-t\}\) and proves
\[
K=\sum_{r\in C}\mu_B(r)+\sum_{r\in B}\mu_C(r)
\le\left\lfloor{ |B||C|\over2}\right\rfloor.
\]
It also records the pointwise bound \(\mu_B(r)\le\min(|B<r|,|B>r|)\), with sharp coefficient \(1/2\) in the stated sense. Its construction extends any Golomb \(B\) by one opposite diagonal mark to a proper weak source, so no better fixed-output coefficient follows from weak properness alone. The missing reflected outputs can still recur, and outside-hull reflections are outside this budget.

## 5. Strongest inherited R3 two-color capacity target and its transfer

`fibers/R3_FINITE_CAP_INPUTS_0034.md` identifies the strongest recorded two-color strict-source capacity input used for the old \(n=464\) R3 route:
\[
r_A(d)\le46\ (1\le d\le27),\qquad r_A(d)\le45\ (d=1,2,3),
\]
for a 155-mark \(A\subseteq\{0,\ldots,463\}\) with proper strict \(V(A)\). This is a requested conditional lemma, not already proved. The cited inherited mixed-profile transfer combines it with window-13 spacing and excludes 155 marks via its recorded distance-sum comparison. It must retain \(V(A)\) as a strict two-color source; the individual \(F_d\)'s are instead weak two-color sources.

`research_round3/cap/endpoint_neighbor.md` is the capacity formula behind that transfer. For ordered marks with contiguous-block span minima \(\ell_i\), it gives
\[
T_c\le L{c(c+1)\over2}-2\sum_{i=0}^{c-1}(c-i)\ell_i,
\]
while the sum of the \(H=cs-c(c+1)/2\) smallest distances allowed by multiplicities \(v_d\) is at most \(T_c\). The file labels itself “candidate pending independent reviews”; here it is recorded only as the inherited formula/status. Its finite position minima \(H_j\)/window data are part of that route.

## 6. What is not already present

Among these six directly relevant notes, there is no derived finite-span cube/box double count, classical successive-differencing inequality, or Gowers-norm estimate that takes \(T(F_d)\le2{r_d\choose2}\) (or \(E(F_d)\le6r_d^2-5r_d\)) simultaneously over all fibers and produces a new source-size constant. The existing results identify possible extra local inputs—supported-difference holes, internal reflections, and finite position capacities—but do not combine them into such a moment bound. Developing that combination is the new question, rather than a theorem already available for transfer.
