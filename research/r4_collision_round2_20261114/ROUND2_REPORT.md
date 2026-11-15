# Codex lane A, round 2

**No new R4 numerical upper bound is established.** This round supplies a
proved short-request demand interface, exact feasible certificates, a checked
counterexample to a local Golomb shortcut, and a quantitative reason not to
expand the coarse collision route. Work is local to binary sources.

Base: fb33871768bd94fd8e88452ac62ac2789eb0e882.
Branch: codex/r4-collision-round2-20261114. Date: 2026-11-14.
The owner explicitly authorized continuation before external Claude's result
and authorized pushing this round. The earlier integration wait is superseded.
Claude's ternary lane is not duplicated; no unseen result is assumed.

## 1. Proved demand interface

[SHORT_DEMAND.md](SHORT_DEMAND.md) proves, for colored starts at lag h in
n=p-h positions,

    B_h(s)=bal(2(n+s),(s+1)r_h)
       <= sum_(same-color pairs at separation delta) (s+1-delta)_+.

If nonnegative rational coefficients satisfy

    sum_(s>=delta) lambda_(h,s)*(s+1-delta) <= w_(h+delta)

for every positive delta, then

    R_w >= sum_h sum_s lambda_(h,s)*B_h(s).

This controls requests within the support of a specified consumer. It repairs
the unsupported replacement of pair weights w_(h+delta) by w_h. Multiple
widths may be combined only under the displayed coefficient constraint.
An internal independent reviewer checked the proof and implementation; this
is not Lean formalization, external peer review, or a proof of a Ramsey bound.

The elementary lemma was also checked on all 9,840 words over
{absent,color0,color1} of lengths 1 through 8, for all widths s+1 with
1<=s<=length: 73,812 exact checks. This finite test supplements the proof.

## 2. Exact finite certificate experiment

The current window input at p=21,947,996, dilation 1,792, has support through
358,399. Its original binary cap is 457,154. The new experiment does not
alter that cap. It uses the existing rational correlation data at the base.

For h=1, 89,599, and 179,199, a finite linear program proposed coefficients.
They were converted to rationals and checked against the actual weight.
The final accepted certificate in every case is the exact single-width
fallback; **no multiwidth improvement was demonstrated**. Neither the finite
width list nor the floating optimizer is claimed optimal.

The independent standard-library checker verifies every integer coefficient
constraint: respectively 358,398, 268,800, and 179,200 inequalities, totaling
806,398. It does not trust the optimizer or the breakpoint shortcut. It also
recomputes every recorded objective. The underlying imported correlation and
capacity derivations were not independently reimplemented in this round.

The certificates are valid demand inequalities for any permitted r_h; the
reported objectives evaluate them at hypothetical saturated-profile values.
They do not show that a source attaining those values exists.

## 3. Quantitative consumer gate

With rectangular target weights on 1<=t<=358,399, take r_h equal to the
staggered capacity profile on that support. Additionally suppose, for this
diagnostic only, m_t^e(u)<=2*ceil(sqrt(t)). The latter is not proved.

| Quantity | Exact value |
|---|---:|
| Lower request count supplied by the sliding-window formula | 63,626,655,522 |
| Upper request budget under the extra collision hypothesis | 2,707,527,284,138 |

The ratio is 31813327761/1353763642069, about 2.35%. These inequalities do
not exclude this abstract saturated profile. This is a failure of this
particular consumer test, not proof that all collision methods fail. Stronger
demand, different weights, or an averaged collision theorem remain possible.

The checker independently recomputes both totals from the serialized profile.
That arithmetic check does not independently establish the profile's origin.
No subtraction of this diagnostic from the existing certificate is valid.

## 4. Checked obstruction and unresolved candidate

The complete 45-cell binary coloring in `translated_probe.json` uses

    A={0,11,12,14,15,85,86,88,89,100}.

All 32 physical directed Ls were checked literally. At target (100,0), its
color-0 requests have offsets {11,12,14,15,85,86,88,89}. The lower half
{11,12,14,15} has repeated difference 1. Thus the proposed shortcut that each
half of the request offsets is Golomb is **refuted**. The source is not a
construction on a full square. Translation matters: differences of the low
marks need not themselves be marks, so putative forcing cells can be absent.

The weaker R2-C1 claim that all request offsets partition into two Golomb
sets remains **UNDECIDED**. This witness even has such a partition:
{11,15,86,88,89} and {12,14,85}. The finite reconnaissance found no witness
against R2-C1; it supplied no checked impossibility certificates.

Reconnaissance coverage: 281 nonpartitionable subsets of {1,...,12}, sizes
7 through 10, at three choices of T (843 solver calls); their translated
versions at T=200 (281 calls); and 1,200 seeded random draws giving 183
nonpartitionable candidates at T=1000. Negative solver replies are not
accepted as mathematical infeasibility. The successful 10-mark witness is
accepted only through the separate literal checker.

## 5. Decision and handoff

Mechanism: a short-demand and coefficient-domination interface, based on
ordinary occupancy convexity. No worldwide novelty claim.
Technical result: exact coefficient certification and a concrete local
counterexample. Numerical bound: unchanged by this round.

Do not expand the unrestricted collision or two-Golomb search merely because
it ran quickly. The coarse consumer remains far too weak even under an
optimistic extra hypothesis. The next useful question is a bound on weighted
collision cost in the near-saturated regime, retaining the actual set and
color geometry; it must be tested with this demand interface before scaling.
External Claude's eventual inter-class result may supply a stronger consumer.

For integration, export the domain (binary strict sources), no extra
near-extremality premise for the demand theorem, the explicit coefficient
condition, and the need for a matching upper request estimate. Saturation
and the square-root cap belong only to the diagnostic, not the theorem.
Review Claude's actual package before composing any savings.

## Reproduce and evidence scope

From this worktree root:

```text
python research/r4_collision_round2_20261114/verify_round2.py
python research/r4_collision_round2_20261114/build_duals.py
python research/r4_collision_round2_20261114/pilot.py
python research/r4_collision_round2_20261114/random_probe.py
```

The verifier needs only the Python standard library. Certificate discovery
uses SciPy; witness discovery uses PySAT. Numerical jobs ran sequentially,
with one worker, and completed in seconds. The HiGHS `threads=1` option is
passed through by SciPy; BLAS thread environment limits are also set to one.
No background research process is asserted. See REVIEW.md, verification.json,
demand_certificates.json, and manifest.json for evidence and scope.
