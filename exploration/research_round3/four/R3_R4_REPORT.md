# R3-R4 distance-profile and endpoint capacity improvement

| Field | Value |
|---|---|
| Sub-Task ID | R3-R4 |
| Assigned Model | GPT-5.6 Sol, xhigh |
| Task Statement | Replace the uniform inner multiplicity cap by the actual residual-span profile, select outer rank-neighbor parameters per span, incorporate the endpoint neighbor correction, and produce an exact R4 certificate. |
| Result | **PROVED in the author phase, pending the mandated fresh cross-reviews:** `R_4(L)<=21991300`, improving `22006246` by 14946. |
| Self-Check | `exact-verify` self-test returned `ENVIRONMENT OK`. The independent verifier used three-prime NTT/CRT correlations, exhaustive Golomb threshold scans, all 561 capacity runs, all 35999 distances, and all 111 declared outer parameters per distance; status `PASS`. |
| Confidence | High in the finite certificate and the two new elementary inequalities. Cross-review of the endpoint lemma and integrated proof remains required by the campaign protocol. |
| Dependencies | Accepted Round-2 FM1, FM2-4, FM3 and bound `22006246`; root's endpoint identity, reproved below. No external Golomb table or unproved 45-cap lemma is used. |

## 1. OBJECTIVE

Fix `t=36000`, `w_i=i(36001-i)`, and
`a_d=sum_{i=1}^{t-d}w_iw_{i+d}`.  For every tested integer `n`, maximize
the exact signed margin

```text
M(n)=2*sum_{d=1}^{35999}(n-d-48*K_d(n))*a_d-3*n*a_0,
```

where larger is favorable and `M(n)>0` contradicts the inherited FM2-4
inequality.  The bounded outer decision at each span is `c in 650..760`;
`K_d(n)` is the least capacity obtained in that declared set.  The global
Golomb sub-cap is optimized over every admissible integer neighbor parameter.
The incumbent target is `n<22006246`, with gap `22006246-n`.

### New structural input 1: actual residual-span multiplicities

Let `B={b_1<...<b_s}` be a monochromatic diagonal set of span at most `L`
inside a completion-closed three-color region.  Fix an internal difference
`h`.  FM1 partitions the left endpoints of pairs `x,x+h in B` by the two
possible completion colors.  Each color fiber is Golomb and its left
endpoints have span at most `L-h`.  If `Q(S)` is any proved Golomb-order cap
at span `S`, then

```text
r_B(h) <= 2*Q(L-h).                                      (R4-P1)
```

This is strictly more informative than the inherited uniform
`r_B(h)<=2Q(L)`.  It uses the actual region span and does not assert that a
four-color fiber is itself Golomb.

### New structural input 2: profile neighbor capacity with endpoints

For `1<=c<s`, collect all rank-neighbor differences
`b_{i+j}-b_i`, `1<=j<=c`.  Their number is

```text
H=c*s-c*(c+1)/2.
```

If positive distance `h` occurs at most `V_h` times, let `P(H;V)` be the
sum of the first `H` entries of the ordered multiset containing `V_h` copies
of each `h`.  The collected sum is at least `P(H;V)`.

For the upper bound, cancellation at each rank gives

```text
T_c=sum_{i=0}^{c-1}(c-i)*(b_{s-i}-b_{i+1}).
```

The first and last `i+1` distinct integer marks each span at least `i`, even
when the two endpoint blocks overlap.  Therefore

```text
T_c <= L*c*(c+1)/2 - 2*sum_{i=0}^{c-1}(c-i)*i
    =  L*c*(c+1)/2 - 2*binom(c+1,3).
```

Combining and doubling yields the exact necessary condition

```text
2*P(H;V) <= L*c*(c+1)-4*binom(c+1,3).                   (R4-P2)
```

Consequently, if the reverse strict inequality holds at size `K+1`, then
`s<=K`.  Monotonicity in `s` excludes every larger size.  This proof uses
only distinct integer marks; no window-profile or 45-cap hypothesis enters.

### Exact Golomb sub-cap

For a Golomb ruler, `V_h=1`, so `2P(H;V)=H(H+1)`.  For target size `s`, set

```text
Tau(s)=max_{1<=c<s} floor(
  (H_s(c)*(H_s(c)+1)+4*binom(c+1,3)-1)/(c*(c+1))
),
H_s(c)=c*s-c*(c+1)/2.
```

Then `Q(S)` is the first `s-1` for which `Tau(s)>=S`.  The certificate and
checker exhaust every `c` for target sizes 4600 through 4900.  All used
values are `Q=4750,...,4758`; their maximizing Golomb parameter is `c=68`.
The transition spans are serialized in the certificate.

## 2. CONSTRAINTS

The legitimate constraints are integer `n>=t`, positive integer weights,
`1<=d<t`, `1<=h<=n-d-1`, `1<=c<K+1`, globally valid Golomb caps `Q`, the
actual residual profile `V_{d,h}=2Q(n-d-1-h)`, and the exact strict
first-forbidden comparison R4-P2.  Every autocorrelation is positive, so the
capacity substitution in FM2-4 is valid.

The artificial search bounds were `21950000<=n<=22006246` and outer
`650<=c<=760`.  The final theorem needs only the listed valid `c` witness for
each capacity run.  Exhausting this box supports the per-span selection claim
inside the box; it does not prove optimality for `c` outside the box, other
windows, other weights, or all smaller `n`.

## 3. SCAN/OPTIMIZATION RESULT (heuristic)

The search variables are finite integers, so no floating optimizer was used.
Every declared outer value was evaluated exactly: 111 independent `c` starts
per distance, 35999 distances per candidate.  This exhaustive finite grid has
no convergence tolerance or local basin ambiguity.  The selected parameters
range from 696 to 740; the winner is not on the declared boundary.

The principal exact scout values were:

| Variant | `n` | Doubled margin | Scout sign |
|---|---:|---:|---|
| Profile + endpoint | 21991200 | -959596049982389043035428416 | nonpositive |
| Profile + endpoint | 21991300 | 551211731377452489346057152 | positive |
| Profile + endpoint | 21991500 | 3572064084430380575832634176 | positive |
| Profile without endpoint | 21991500 | -11890396232887423924221142080 | nonpositive |

The first frozen profile-only bracket underestimated the gain and crossed its
predicted lower edge; `R3_R4_R10.md` records the halt and revised prediction.
The endpoint candidate and the 100-step follow-up matched their frozen signs.
The pair `21991200,21991300` is only the neighboring tested sign bracket;
capacity cliffs prevent a monotonicity or global-minimum claim.

## 4. CERTIFIED WINNER

The exact candidate is

```text
n=21991300,  t=36000,  w_i=i(36001-i),
Q(S)=global endpoint-refined Golomb cap,
V_{d,h}=2Q(n-d-1-h),
K_d=min over every integer c in 650..760.
```

For each constant-`K` run `[lo,hi]`, the certificate stores a `c` witness and
checks R4-P2 at `d=lo`, the longest span.  For later `d` in the run, `L_d`
decreases and every `Q(L_d-h)` weakly decreases.  Hence the profile minimum
weakly increases while the right side decreases; the first comparison proves
the whole run.  The 561 runs cover `d=1,...,35999` without gaps or overlap.

Representative interval rows are:

| `lo..hi` | `K` | `c` | `H` | frontier | exact run margin |
|---|---:|---:|---:|---:|---:|
| 1..46 | 458058 | 719 | 329085581 | 34598 | 103004 |
| 47..108 | 458057 | 737 | 337316793 | 35463 | 172350 |
| 109..170 | 458056 | 738 | 337773375 | 35511 | 155962 |
| 35827..35890 | 457500 | 738 | 337363047 | 35497 | 63342 |
| 35891..35954 | 457499 | 738 | 337362309 | 35497 | 77962 |
| 35955..35999 | 457498 | 738 | 337361571 | 35497 | 158118 |

The full run table is in `r4_profile_endpoint_21991300.json`.  Exact
polynomial summation by the claimant and independent NTT/CRT by the checker
give

```text
a_0 = 2015819151552432004800,
2*sum_d (n-d-48*K_d)*a_d
    = 133542662853982446330820777152,
3*n*a_0
    = 132991451122604993841474720000,
margin
    = 551211731377452489346057152 > 0.
```

This contradicts FM2-4 and proves, subject to the campaign's fresh reviews,

```text
R_4(L) <= 21991300.
```

The improvement over `22006246` is exactly 14946.  The support size is 36000.
Active constraints are integer parameters, positive weights, 561 strict
first-forbidden run inequalities, and the final strict score comparison.

Certificate SHA-256:
`7adbd5d660f735997213fbbef6c6d214e3b802cec4611259de600e7e42bd9562`.
Independent-result SHA-256:
`88c301df99dd33dccb2ecbff0303b017f9c9ee00ac3591ab69e30162f57f6e0e`.

### Certificate pseudocode

```text
build Tau(s) for s=4600..4900 by exhausting c=1..s-1
Q(S) := first s-1 with Tau(s)>=S

for d=1..35999:
    L := n-d-1
    for h>=1: V[h] := 2*Q(L-h)
    for c=650..760:
        binary-search first K+1 satisfying
          2*ProfileMin(c*(K+1)-c*(c+1)/2,V)
            > L*c*(c+1)-4*binom(c+1,3)
    K[d] := minimum K over the declared c range
    score += (n-d-48*K[d])*a[d]
assert 2*score-3*n*a[0] > 0
compress consecutive equal K[d] values into interval runs
```

The independent checker rebuilds `Tau`, `Q`, and profile prefix sums; verifies
both allowed size `K` and forbidden size `K+1` for all 111 `c` values at every
distance; checks each serialized run; reconstructs correlations by three NTTs
and exact CRT; and recomputes the final integers.  It returned `PASS`.

Global-bound status for the optimization problem: no optimum is claimed over
`n`, `t`, weight profiles, or `c` outside 650..760.  The displayed Ramsey
upper bound needs only one valid exact candidate, not such an optimum.

## 5. SENSITIVITY TABLE

| Item | Exact baseline / perturbation | Exact effect on signed margin | Nearest tested flip or limitation |
|---|---|---|---|
| `n` | 21991300; reoptimized step to 21991200 | backward 100-step change is -1510807781359841532381485568 | tested sign bracket `[21991200,21991300]`; no monotonicity claim |
| `t` | 36000 | unavailable; changing `t` changes every correlation and was outside the frozen follow-up | no certified threshold |
| Weight scale `lambda` | `lambda=1` | fixed capacities give `M(lambda)=lambda^2 M(1)`; change `1->2` is +1653635194132357468038171456 | sign cannot flip for nonzero real scale |
| Weight shape | polynomial-1 | not varied in this structural iteration | global profile optimization open |
| Outer `c` | per-span minimum in 650..760 | fixing `c=662` changes margin to -9977307308410619136074470080; adaptive gain is 10528519039788071625420527232 | selection ranges 696..740; behavior outside search box open |
| Endpoint correction | doubled subtraction `4*binom(c+1,3)` | at `n=21991500`, removal changes margin from 3572064084430380575832634176 to -11890396232887423924221142080, loss 15462460317317804500053776256 | discrete capacity transition; no per-unit linear marginal |
| Inner cap profile | `2Q(L-h)` | replacing the complete refinement by the inherited uniform profile at final `n` gives -229539654091296653200482883776; adaptive refined gain is 230090865822674105689828940928 | all 35999 `K_d` improve by 53..102; sum of drops 2828289 |
| Coefficient `48` | 48, winner fixed | exact derivative `-2 sum K_d a_d = -27691952608782000641625769513376` | continuous fixed-winner flip at `48 + 551211731377452489346057152/27691952608782000641625769513376`; integer increase to 49 flips |
| RHS factor `3` | 3, winner fixed | exact derivative `-n*a_0 = -44330483707534997947158240000` | continuous fixed-winner flip at `3 + 551211731377452489346057152/44330483707534997947158240000`; integer increase to 4 flips |
| Golomb parameter | global scan of all admissible `c`; used `Q=4750..4758` | reoptimized discrete values serialized by transition | no external Golomb optimum is assumed |

## 6. VERDICT

**PROVED (author phase; mandated independent agent reviews pending):** the
distance-dependent multiplicity profile R4-P1 and endpoint capacity R4-P2,
together with the accepted FM1/FM2-4/FM3 machinery and the independently
verified exact certificate, imply `R_4(L)<=21991300`.

The optimization verdict is **HEURISTIC** beyond that candidate: the bounded
scan does not certify a global minimum over side lengths, weights, windows, or
outer parameters outside 650 through 760.

Artifacts:

- `r4_profile_endpoint_21991300.json` — exact 561-run certificate.
- `r4_profile_endpoint_21991300_verified.json` — independent `PASS` result.
- `generate_r4_profile_certificate.py` — claimant/generator.
- `verify_r4_profile_certificate.py` — independent checker.
- `R3_R4_FOLLOWUP_RESULTS.json` — focused descent and alternate-profile data.
- Frozen predictions and append-only corrections in this directory.

CLAIM: The endpoint/profile certificate implies R_4(L)<=21991300 from the inherited FM1/FM2-4/FM3 machinery | MY VALUE: doubled margin 551211731377452489346057152 with 133542662853982446330820777152>132991451122604993841474720000 | THEIR VALUE: frozen candidate margin 551211731377452489346057152 | VERDICT: PASS | METHOD: Independent Golomb and outer-c exhaustion, run verification, and three-prime NTT/CRT autocorrelations

CLAIM: The certified bound improves 22006246 by 14946 | MY VALUE: 22006246-21991300=14946 | THEIR VALUE: improvement 14946 | VERDICT: PASS | METHOD: Exact integer subtraction after certificate verification
