# Finite Golomb/reflection inputs (0042)

Scope: local dependency map only. The formulas below are already recorded inputs; no ruler minima or example counts were recomputed here. The first four apply directly to two disjoint Golomb classes of sizes `b,c` (including the contemplated `23,24` range), subject to their stated integer-span hypotheses.

## 1. Single-class reflection multiplicity

`fibers/GOLOMB_REFLECTION_MULTIPLICITY_0040.md`, Sections 1--5, fixes, for a Golomb set `B`, `T_r(B)={(a,b,c):a<b<c in B, r=a+c-b}` and `mu_B(r)=|T_r(B)|`. Its normal form is `(a,b,c)=(r-p,r+q-p,r+q)` with `0<p<q`; hence `mu_B(r) <= min(|B<r|,|B>r|) <= floor(|B|/2)`. For fixed `r`, the outer pairs form a matching and any one mark has triple-degree at most two. These are universal finite integer statements. The note records arbitrarily large sharp examples and a six-mark quotient cycle: neither matching nor degree two supplies a forest/expansion conclusion.

## 2. Two-class positional reflection budget

`WEAK_REFLECTION_POSITION_BUDGET_0040.md`, Sections 1--4, gives the universal cross-class first-moment bound for disjoint Golomb `B,C`:
`K = sum_{r in C} mu_B(r) + sum_{r in B} mu_C(r) <= floor(bc/2)`.
It comes from symmetric rank intervals on the line. The note also records the unsupported-triple inventory `binom(b,3)+binom(c,3)-K`; its recurrences do not presently turn that inventory into a span bound. Its one-point-extension observation says every Golomb `B` can be extended by a single proper weak-source mark, so a fixed uniform improvement of the `1/2` coefficient cannot follow from coloring alone.

## 3. Span-sensitive shadow/hole inequalities

`NESTED_REFLECTION_HOLE_BUDGET_0041.md`, Sections 2--6, strengthens the preceding positional input when the opposite class supplies actual holes. For `r` in the other class, the two reflection shadows are disjoint and have exact size `|H_B(r)| = 2 binom(mu_B(r),2)`. With `n=b+c` and ambient interval length `L`, it records `mu(mu-1) <= L+1-n`, the localized refinement `mu(mu-1) <= alpha+beta+1-|S cap I_r|`, and, after summing mixed outputs, `F=sum binom(mu,2) <= H^+`, `F <= H^-`, and `2F <= n(L+1-n)`. The directional quantities `H^+,H^-` are expressed by ranks. Combining the first-moment bound with Cauchy yields `K^2-nK <= n^2(L+1-n)`. These are the strongest saved finite-span reflection inputs found. The same file explicitly leaves the reflection-output graph without an expansion/independence estimate.

## 4. Exact difference/sum representation dictionary

`TWO_GOLOMB_MIXED_ENERGY_0040.md`, Sections 1--5, is the complete saved ordered pair-level convolution dictionary. With `beta_d,gamma_d` the within-class difference indicators and `x_d,y_d` the directed mixed start counts, `r_{B union C}(d)=beta_d+gamma_d+x_d+y_d` and `sum_d(x_d+y_d)=bc`. It defines `rho`, `N=sum_d(beta_d+gamma_d)(x_d+y_d)`, and `Q=sum_d x_dy_d`; then exactly
`sum_d[binom(x_d,2)+binom(y_d,2)]=rho`, `T(B union C)=2rho+N+Q`.
Here `Q` is the equal-sum mixed-pair term, through `u+(v+d)=(u+d)+v`. The universal bounds recorded are `2rho <= binom(b,2)+binom(c,2)`, `N<=2bc`, and `Q<=binom(b,2)+binom(c,2)`, giving `T<=2 binom(b+c,2)` and `E<=6n^2-5n`. This is an exact counting input, not a solver example. The note's proposed stronger deficit in `N` is explicitly falsified by one displayed finite construction, so is not a universal input.

## 5. Shifted-window positional moment inequality

`research_round3/cap/endpoint_neighbor.md`, Sections 1--3, gives the saved finite-window mechanism. For ordered marks `a_1<...<a_s` of span `L`, contiguous-block minima `ell_i`, and `c` endpoint layers,
`T_c=sum_{i=0}^{c-1}(c-i)(a_{s-i}-a_{i+1}) <= Lc(c+1)/2 - 2sum_{i=0}^{c-1}(c-i)ell_i`.
If difference multiplicities are bounded by a profile `v_d`, the profile total `M(H)` must not exceed this endpoint capacity, with `H=cs-c(c+1)/2`. The note also records window-to-gap implications (`h(w)<=i` gives `ell_i>=w`) and `ell_{i+j}>=ell_i+ell_j`. This is universal once its multiplicity/window premise is supplied. Any particular profile in that cap work is conditional or inherited, rather than a general Golomb-minimum theorem.

## 6. Status of full ordered triple convolution

The closest single-class object is the exact normal parametrization of each reflected triple in `GOLOMB_REFLECTION_MULTIPLICITY_0040.md`; it is an ordered reflection enumerator, not a global triple-convolution decomposition over shifts. The two-class note above gives the complete saved *pair* sum-versus-difference dictionary. Among these six mapped sources, no full ordered triple-convolution/reflection decomposition for one Golomb class was found.

`CORNER_SUM_COORDINATES.md` is not such an input: it concerns triangular-grid shifts over `F_3` (`D_d=I+X^d+Y^d` and reconstruction identities). Its restricted-step construction is a documented mismatch, not an integer Golomb or shifted-window estimate.
