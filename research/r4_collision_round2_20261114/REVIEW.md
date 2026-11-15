# Internal mathematical and implementation review

Reviewer: separate read-only theory agent, 2026-11-14.
Scope: `SHORT_DEMAND.md`, `build_duals.py`, `verify_round2.py`, and
`translated_probe.json`, read in full. No numerical jobs were run by this
reviewer. Execution results are supplied by the main agent's recorded runs.
This is not external peer review or Lean formalization.

## Findings

No mathematical defect was found in the sliding-window demand inequality,
the rounded short-pair consequence, or the weighted-dual charging argument.
There are exactly n+s windows in the stated index range, each start occurs
s+1 times, and a pair at distance delta occurs s+1-delta times when
1 <= delta <= s. Each request retains its originating lag and pair, so
condition (D) is the required safeguard against charging the same pair
multiple times at different window widths.

The generating linear program is used only for discovery. The rational
certificate verifier checks every integer delta through the largest width.
Its recurrence subtracts the current slope and then removes widths ending
at that delta, which correctly evaluates the triangular pair-cost kernels.
It separately recomputes the occupancy objective. This certification does
not rely on the optimizer's termination status or on the breakpoint argument.

The explicit witness contains every strict-source cell on its ten marks.
The verification code enumerates physical directed Ls in that domain and
computes the actual request set from the colors. The lower-half repeated
difference refutes Golombness even when attention is restricted to one
half of the requests. The field H in the input is a prescribed subset;
the computed actual request set can be larger. No full-square extension
or stronger partition obstruction is implied.

The exponent warning is correct: from
R >= M^2/(4L)-M/2 and the hypothetical bound R <= C*sqrt(L)*M,
division by M>0 gives M <= 4C*L^(3/2)+2L. Empty or singleton sources are
trivial separately. This route alone retains the three-quarter-power
cardinality exponent.

## Verification limits

- The independent checker treats the supplied coarse correlations, dilation,
  normalization, and hypothetical fiber cardinalities as inputs. It does not
  independently regenerate their source certificates or the staggered profile.
- The added `gate()` routine independently recomputes the `rectangular_gate`
  aggregate demand, hypothetical budget, and their exact ratio from serialized
  profile runs. It checks contiguous coverage through the stated support.
  Its alternate integer-square-root calculation correctly reconstructs
  2*ceil(sqrt(h)). This closes the earlier aggregate-arithmetic checking gap;
  the profile's capacity derivation remains an inherited input.
- The finite occupancy tests cover only their stated finite domain; the general
  statement is supported by the written convexity/counting proof.
- A valid dual for a hypothetical saturated profile does not show that the
  profile is realizable or excluded, and supplies no new binary capacity cap.
- A single-width fallback is a valid certificate but is not evidence that
  multiple widths improved the objective or that the finite optimization is
  globally optimal.

Conclusion: the proof and certificate-checking logic support the stated
structural demand interface and checked counterexample, with the limits above.
No numerical Ramsey-bound improvement is established by this package.
