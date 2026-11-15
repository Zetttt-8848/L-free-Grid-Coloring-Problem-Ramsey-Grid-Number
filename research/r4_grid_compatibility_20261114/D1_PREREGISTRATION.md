# D1 pre-registration (written before any D1 search was run)

Date: 2026-11-14. Lane B, round 1, plan R4-PAIR-20261114-v2. Base commit 726998b9.

## Conventions

- Cells are `(x,y)`, where `x` is the column, `y` is the row, and both are zero-based. The forbidden L is `(x,y),(x+d,y),(x+d,y+d)` with `d>0`.
- Fix a finite set `D` of integers and a proper coloring `chi` of its strict source `V(D) = {(v,u) : u<v, u,v in D}`, with palette `{0,1,2}`.
  - "Proper" means that no three cells of `V(D)` forming an L have one color.
  - In the square application, `D = D_c` is the set of main-diagonal positions of color `c`, and the palette is the three other colors.
- Fibers: `F_d(X) = {u : u, u+d in X}`.
- Classes: `S_e(d) = {u in F_d(D) : chi(u+d,u) = e}`.
- Requests: `R_e(h) = union_{1<=d<h} F_{h-d}(S_e(d))`.
- Request multiplicity: `m_{e,h}(u) = #{d in [1,h-1] : u in F_{h-d}(S_e(d))}`.
- Request count: `N_e(h) = sum_u m_{e,h}(u) = sum_{d<h} r_{S_e(d)}(h-d)`, where `r_X(l) = |F_l(X)|`.

## Candidates

### U1 (pointwise-in-h concentration bound with the consumer constant)

For every such `(D,chi)`, every `e` and every `h >= 2`:

`sum_u m_{e,h}(u)^2 <= (3/2) * ( N_e(h) + N_e(h)^2 / |F_h(D)| )`, whenever `F_h(D)` is nonempty.

**Consumer.** By Cauchy, `|R_e(h)| >= N^2 / sum m^2`. U1 would then give `|R_e(h)| > (2/3)|F_h(D)|` for each `e` once `N_e(h)` is much larger than `|F_h(D)|`. That contradicts the double-cover bound `sum_e |R_e(h)| <= 2|F_h(D)|` (P1). In the extremal regime of the R4 chain, where `N_e(h)` is about `9,400 h` and `|F_h| ≈ 1.4 * 10^6`, it would force a loss in the joint class count.

**What counts against U1.** Any checked `(D, chi, e, h)` violating the inequality.

### UW(lambda0) (bounded request ratio), probed at lambda0 = 1

For every such `(D,chi)` and every `h` with `F_h(D)` nonempty:

`min_e N_e(h) <= lambda0 * |F_h(D)|`.

**Consumer.** In the extremal regime the ratio `N_e(h)/|F_h(D)|` is about `h/150`. A UW with an absolute `lambda0` would therefore bound the window-weighted fiber multiplicities of the classes far below the current caps.

**What counts against UW(1).** Any checked `(D, chi, h)` with `N_e(h) > |F_h(D)|` for all three colors `e`.

**Scope.** A finite witness refutes only UW(1). UW with an unspecified absolute constant concerns arbitrarily large sparse sources. A bounded search cannot refute it; that would need a family.

## Search plan (bounded; at most 15 minutes, 1 worker, under 1 GiB)

1. Generate L-free three-colorings of `V(D)` for intervals `D = [0,m)` and for random subsets `D` of `[0,L]`, by randomized min-conflict local search.
2. Re-check every reported coloring directly against every L of `V(D)`.
3. For every `(e,h)`, compute both U1 ratios and the UW ratio, and keep the extreme witnesses.

A pass in these finite cases does not support U1 or UW at the R4 scale. A violation closes exactly the stated candidate.
