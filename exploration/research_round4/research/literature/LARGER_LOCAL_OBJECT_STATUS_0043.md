# Larger local whole-triangle status (0043)

Scope: six local files only; no solver was run. “Closed” below means a saved mathematical construction or multiplicity calculation, not an optimization/minimum claim.

## 1. The general whole-corner scalar mechanism

LARGER_TRIANGLE_AMPLIFICATION.md gives the retained-dilation embedding count

    C(N,m)=sum_(d=1)^floor((N-2)/(m-2)) binom(N-d(m-2),2)

and a corner-incidence upper multiplicity b_trunc(N,m). If every proper T_m has at least rho rainbow corners, scalar amplification requires rho C(N,m)>b_trunc(N,m) binom(N,2). This is conditional only. At host N=464 the file records calculations for m=11,12,13, not for T14, T15, T16, or a larger local triangle.

The same file proves the exact boundary-sensitive maximum multiplicity only for (N,m)=(464,13): b_exact=223. This is an actual completed finite multiplicity theorem. It is not stated for larger local sizes.

## 2. Literal low-rainbow local colorings: T11, T12, T13

fibers/LARGER_TRIANGLE_RAINBOW_PROBE.md supplies complete endpoint-group properness certificates and explicit rainbow lists for:

* T11 with five rainbow corners;
* T12 with ten rainbow corners;
* an older T13 example with twenty-one rainbow corners.

Those are literal constructions and upper bounds on the possible local minimum. The file makes no lower theorem for any of the three sizes. Its stated bounded T13 search with rainbow budget at most 16 was undecided; that raw status is not a theorem.

THIRTEEN_TRIANGLE_FOURTEEN_RAINBOW.md supersedes the older T13 rainbow count with a complete proper T13 construction having fourteen rainbows. Therefore the proposed lower statement “every proper T13 has at least 17 rainbows” is false. Combined with the proved C(464,13) and b_exact=223, LARGER_TRIANGLE_AMPLIFICATION.md closes the *uniform all-corner scalar* T13 route at side 464: even rho=14 cannot meet its incidence budget. This does not address selected/signed weights or an inequality coupled to the host colors.

## 3. Earlier small-object scalar routes

TRIANGLE_RAINBOW_ENERGY.md proves the full-triangle line-discrepancy identity and the conditional local-to-global embedding criterion. It records that the all-corner T10 requirement of at least seven rainbows is contradicted by TEN_TRIANGLE_ONE_RAINBOW.md (cited there). It also records bounded raw outcomes for exact-two-color formulations through T10, but does not promote those outcomes to a finite local theorem. Its later weighted T10 barriers concern that particular local size and do not supply a T14--T16 theorem.

rainbow_budget_probe.py is the bounded discovery encoding for T10 budgets 6, 2, and 1. It categorizes a run as literal coloring, raw negative, or undecided and stores any witness. The source code is a record of the attempted budgets, not a proof or a general large-triangle result.

## 4. Zero-sum whole-corner attempts

zero_sum_scale_probe.py encodes the stronger local condition that every tested corner has nonzero F3 color sum. It schedules only these bounded instances:

* steps {1,2,3} at triangle sizes 10, 16, 24;
* steps {1,2,3,4} at sizes 12, 18.

These are restricted step-set calculations, not an all-corner T16, T18, or T24 condition. The script labels outcomes literal coloring, raw negative, or undecided and writes them to its adjacent JSON, but neither the script nor the six-file map proves a full whole-triangle zero-sum lower bound.

## 5. T14, T15, T16 and larger: bounded status

The filename/text search found no saved T14, T15, or T16 whole-corner rainbow lower theorem, exact copy-multiplicity calculation, literal full proper coloring, or all-corner zero-sum impossibility theorem. The only appearances near those sizes are the restricted-step zero-sum script instances above (including n=16) and route-level warnings that no T14 zero-sum-free impossibility theorem is claimed. Accordingly, no larger-object finite lower theorem is already available from this local record.

## Consequence for route selection

What is mathematically closed is the uniform scalar all-corner route at T13, together with the earlier T10 scalar/weight barriers in their stated classes. T11 and T12 have explicit low-rainbow counterexamples to their then-relevant scalar thresholds, but their exact-boundary scalar routes were not separately developed as the T13 one was. T14 and above remain unattempted in the precise whole-corner amplification sense; the restricted-step zero-sum probes do not fill that gap.
