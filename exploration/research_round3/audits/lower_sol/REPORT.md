# Independent review of Round-3 cores J and F

Reviewer: `lower_sol`  
Assignment source: `research_round3/audits/reviewer_assignment.json`  
Method: independent reimplementation; no claimant checker was imported or run  
Verdicts: **J — PASS. F — PASS.**

## Core J: joint obstruction and window certificates — PASS

I rebuilt the strict-completion triangle from its definition.  For a support
`B`, variables are the ordered cells `(x,y)` with `x>y` in `B`.  A corner is
the three cells `(x,y),(x+d,y),(x+d,y+d)` whenever
`y,y+d,x,x+d` lie in `B`.  Each corner gives the two signed three-literal
clauses, and variable 1 is pinned to remove global color complementation.
My CNFs agree as clause multisets with all four serialized CNFs.  A new unit
propagation implementation checked every RUP addition, including the final
empty clause:

| Core | Cells | Corners | Clauses | RUP additions | Result |
|---|---:|---:|---:|---:|---|
| `triangle_core` | 36 | 55 | 111 | 151 | PASS |
| `triangle_core_v2` | 45 | 79 | 159 | 427 | PASS |
| `triangle_core_v3` | 45 | 51 | 103 | 1,297 | PASS |
| `triangle_core_v4` | 36 | 46 | 93 | 157 | PASS |

For the width-13 classification, I reconstructed the CNF for each support
rather than reading an author-generated corner list.  All 109 minimal-bad
proofs pass, totaling 31,605 RUP additions; all external CNF/RUP pairs match
the embedded certificate.  Each of the 334 maximal-good color vectors has
the correct `binomial(|B|,2)` length and satisfies every rebuilt clause.
Containment by the two boundary antichains classifies every one of the 8,192
masks on exactly one side, giving 7,147 good and 1,045 bad masks.  The
independently recomputed capacities are

```text
(1,2,3,4,5,5,6,7,7,8,9,9,10).
```

Normalizing the 109 minimal-bad supports by translation and positive gcd
produces exactly the serialized 56 patterns and source-mask groups.  Direct
enumeration gives 543,170 positive affine copies in `[464]`; neither
strengthened witness contains one.

For each of the base, intermediate window/AP5, and final parametric 155-sets,
I checked all 463 distance caps and all 21,298 possible positive-step 6-APs.
The two strengthened sets also pass all 26,680 possible 5-AP occurrences in
115 step groups, with at most one contained occurrence per step.  Their
largest difference multiplicity is 48 and every cap violation list is empty.

For the first parametric family, I materialized the actual `L`, `K`, and `J`
block starts of the final set for every `h=1,...,42`.  The totals were 2, 125,
and 142 respectively.  Both the forward relation `z>i+6h` and reflected
relation `i>y+5h` have zero violating pairs.  At `h=43`, the minimum required
distance `11h+1=474` exceeds the available distance 463.

I represented each source mark in the v3 and v4 cores as its coefficient
triple in `(x,h,b)`.  All 51 v3 corner differences and all 46 v4 corner
differences agree coefficient by coefficient on their two arms.  Consecutive
images remain strictly ordered for all integer `h>=1`, respectively
`b>6h` and `b>4h`; the specializations `(x,h,b)=(2,1,20)` and `(1,1,9)`
recover the serialized cores.  Negating coordinates preserves every arm
equality, so the reflected abstract CNF is isomorphic and the same RUP trace
applies after relabeling.

The final parametric witness contains the literal v4 set
`{1,2,3,5,10,11,12,13,14}`.  It therefore violates the newly discovered
second hook/AP5 family.  This agrees with the author report: the saved set
predates that premise and is only a YES for its explicitly recorded earlier
predicates.  The PASS verdict confirms the stated obstruction and the stated
scope; it does not upgrade this surrogate to a triangle or grid coloring.

## Core F: profile/endpoint four-color certificate — PASS

I derived each autocorrelation from the quartic identity

```text
i(A-i)(i+d)(A-i-d),  A=36001,
```

and exact formulas for sums of powers through degree four.  Direct summation
at nine boundary and interior distances agrees with the closed form.  The
full 36,000-entry vector is positive and has the claimant's SHA-256.  Its
distinguished values are

```text
a_0    = 2015819151552432004800
a_1    = 2015819143775783992800
a_35999= 1296000000.
```

For every excluded size 4,600 through 4,900, I exhausted all
`1<=c<s`, totaling 1,429,449 exact threshold evaluations.  The nine used
transitions for excluded sizes 4,751 through 4,759 agree exactly; each has
unique maximizer `c=68`.  Thus all residual profile values used in the
certificate have independently established Golomb caps.

All 561 constant-capacity runs pass.  For each run I recomputed
`L=n-lo-1`, `H=c(K+1)-c(c+1)/2`, the ordered profile minimum, its frontier,
the doubled endpoint correction, both sides, and the strict margin.  The
runs cover distances 1 through 35,999 exactly once.  The smallest run margin
is 244, attained on `24828..24893` with `K=457671` and `c=734`; it is still
strict.  The expanded cap vector and maximum frontier 35,605 match the
certificate.

As an additional check, I inverted the ordered profile exactly and evaluated
all 111 declared parameters `c=650,...,760` at every distance: 3,995,889
comparisons.  The selected `K_d` vector, first-minimizer `c` vector, hashes,
counts, and range 696 through 740 all match.  This verifies the finite scan at
the fixed candidate.  It gives no global optimum over other `c`, `n`, `t`,
weights, or profiles, consistent with the report's disclaimer.  The theorem
only needs one valid serialized `c` witness per run, which the preceding
561-run check supplies independently of this optimization claim.

The independently reconstructed weighted arithmetic is

```text
sum_d (n-d-48K_d)a_d = 66771331426991223165410388576
2*sum_d (...)         = 133542662853982446330820777152
3*n*a_0               = 132991451122604993841474720000
margin                 =    551211731377452489346057152 > 0.
```

The new structural steps are sound.  If `x,x+h` lie in a span-`L` diagonal
set, each left endpoint lies between the first mark and the last mark minus
`h`, so each of the two FM1 completion-color fibers has span at most `L-h`.
Their Golomb caps sum to `r_B(h)<=2Q(L-h)`; this does not assert that their
union is Golomb.

For ordered marks `b_1<...<b_s`, summing neighbor gaps with index distance at
most `c` cancels to

```text
T_c=sum_{i=0}^{c-1}(c-i)(b_{s-i}-b_{i+1}).
```

Distinct integral endpoints give each difference at most `L-2i`, including
when the endpoint blocks overlap.  Hence the undoubled correction is
`2*binomial(c+1,3)` and the certificate's doubled correction is
`4*binomial(c+1,3)`.  The strict Golomb exclusion is
`H(H+1)>L*c(c+1)-4*binomial(c+1,3)`, so the largest excluded integer span has
the claimed numerator minus one before floor division.  For general profile
minima, comparison with `floor(RHS/2)` handles odd right sides exactly.
Finally, within a run, increasing `d` decreases `L=n-d-1` and each residual
cap, which weakly raises the ordered profile minimum while lowering the
endpoint right side.  The check at `lo` is therefore the weakest member of
the run.

The F verdict is conditional only on the campaign's accepted inherited FM1,
FM2-4, and FM3 implications.  Within that declared dependency boundary, the
certificate proves `R_4(L)<=21991300`, improving 22,006,246 by 14,946.

## Reproducibility

Run from the workspace root with the stated Anaconda Python:

```text
LOCAL_RESEARCH_ROOT\anaconda3\python.exe research_round3\audits\lower_sol\selftest.py
LOCAL_RESEARCH_ROOT\anaconda3\python.exe research_round3\audits\lower_sol\audit_joint.py
LOCAL_RESEARCH_ROOT\anaconda3\python.exe research_round3\audits\lower_sol\audit_four.py
```

`selftest.py` includes known-positive and known-negative RUP cases, direct
small autocorrelations, exhaustive small endpoint identities (including
overlap), and brute checks of the Golomb floor rounding.  It reports
`SELFTEST PASS`.  Machine-readable exact results are in `joint_audit.json`
and `four_audit.json`; `manifest.json` records hashes of the review code,
outputs, reports, and principal frozen inputs.
