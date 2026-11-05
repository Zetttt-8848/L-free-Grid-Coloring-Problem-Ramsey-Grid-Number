# R3-SETUP append-only R10 record

## R3-SETUP-E0 — source-position indexing discrepancy (pre-execution)

**Detected before dependent execution.**  Module A.1 defines `H_j` as a
position count and `q(m)=max{j:H_j<=m}`.  Module A.2 nevertheless writes
`q(n-1-d)`.  At `n=465,d=39`, that literal argument is `425`, hence
`q(425)=23` because `H_23=373<=425<H_24=426`; it gives cap `46`, contrary
to the same sentence's cap `48`.  The accepted Round-2 report instead uses
`q(n-d)`: here `q(426)=24`, giving cap `48`.  Equivalently, `n-d`
possible positions have span `n-d-1`.

**Disposition.**  Halt the literal `q(n-1-d)` branch.  All repaired setup
computations will use the accepted position-count convention `q(n-d)` and
will retain the span `n-d-1`.  This duplicates the root record R3-E0 here
so the setup artifacts are independently auditable; it does not alter an
accepted Round-2 theorem.

## R3-SETUP-E1 — claimant total-capacity boundary (first frozen run)

**Detected on the first post-prediction claimant run, before any numerical
output.**  The profile-bound scan eventually requested more collected
differences than the sum of all per-distance caps.  The first implementation
raised `ValueError("profile has insufficient total capacity")`.  This is an
implementation/specification mismatch: if the requested count exceeds the
total permitted multiplicity, the candidate size is already impossible and
must be treated as the first forbidden size, not as an undefined minimum.

**Root cause.**  `minsum_profile` correctly rejected an unavailable prefix,
but `bound_for_c_profile` omitted the logically prior total-capacity check.

**Disposition before repaired rerun.**  Add an exact integer check
`H > sum(caps)`, returning `s-1` immediately.  Keep `minsum_profile` strict
so accidental uses outside the bound scan still fail loudly.  No claimant
JSON existed and no quantitative verdict was issued from the failed run.

## R3-SETUP-E2 — frozen sensitivity prediction used only `c=8`

**Detected in the first completed claimant output, before independent
checking.**  The frozen prediction said that at least 18 distinct one-unit
shaves are needed when passing from cap 46 to cap 45.  That statement is
true for the advertised `c=8` comparison: 17 shaves raise the one-sided
minimum by 306 to 16668, giving equality `33336=33336`, while 18 shaves
give a strict inequality.  It is false for the full neighbor lemma because
the profile with 17 earliest shaves already has best bound 154 at `c=9`.

**Root cause.**  I optimized the perturbation against the mandate's fixed
`c=8` witness rather than reoptimizing `c` after changing the profile.

**Disposition before repaired rerun/check.**  Preserve the `c=8` threshold
as a labeled fixed-parameter sensitivity only.  Recompute every claimed
minimum reduction across all admissible `c`, record its actual witness
parameter, and have the independent expanded-multiset checker compare that
global result.  The uniform-cap and main 45/46 arithmetic did not disagree
with the frozen predictions.
