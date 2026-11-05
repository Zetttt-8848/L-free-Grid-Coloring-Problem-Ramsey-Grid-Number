# R3-SETUP target audit

| Field | Value |
|---|---|
| Sub-Task ID | R3-SETUP |
| Assigned Model | GPT-5.6 Sol, xhigh |
| Task Statement | Independently verify the Round-3 A.7 capacity thresholds, source-position indexing, the `n=450..465` conditional ladder, cap-profile sensitivity, and the dual-bracket status. |
| Result | All finite capacity arithmetic passes after the recorded source-index repair. The rigorous status of the decimal dual lower endpoint is UNDECIDED. No new Ramsey bound is claimed because the improved cap profile remains hypothetical. |
| Self-Check | `exact-verify` environment self-test printed `ENVIRONMENT OK`; cumulative-capacity claimant and explicit-multiset checker agree with zero discrepancies. |
| Confidence | High for finite integer claims; high that the decimal bracket lacks a rigorous lower endpoint from the supplied inputs. |
| Dependencies | Base `R3-CP0`; accepted Round-2 Lemma 6.1 and report indexing convention; literal `H_0,...,H_28` from the Round-3 mandate. No inherited theorem was rederived. |

## Pinned inputs and convention

The literal position-count table is

```text
(0,1,2,4,7,12,18,26,35,45,56,73,86,107,128,152,178,200,
 217,247,284,334,357,373,426,481,493,554,586).
```

For `m` possible positions, `q(m)=max{j:H_j<=m}`.  A fiber at lag `d`
has `n-d` positions and span `n-d-1`, so its inherited cap is
`2q(n-d)`.  At `n=465,d=39`, the accepted argument is 426 and gives
`q(426)=24`, hence cap 48.  The mandate's literal `q(n-1-d)` uses 425,
gives `q(425)=23`, and hence cap 46.  This source discrepancy was halted
and recorded as `R3-SETUP-E0` before dependent execution.

For a distance profile `V_d`, the independent calculation forms the least
possible sum of `H` positive differences by filling distance classes in the
order `1,2,...`, taking at most `V_d` copies of `d`.  Lemma 6.1 then requires

```text
2*minsum_profile(H) <= L*c*(c+1),
H = c*s-c*(c+1)/2.
```

The claimant computes cumulative capacities.  The checker instead expands
the complete sorted multiset containing `V_d` copies of each distance and
sums its first `H` entries.  It imports no claimant code and computes all
expected values before reading the JSON certificate.

## Uniform and inherited capacities at span 463

| Profile | Exact best bound on `s` | All optimizing `c` values | Boundary certificate at the lowest optimizing `c` |
|---|---:|---|---|
| Uniform `V=48` | 159 | 7--13 | `s=160`: `H=1092`, `2 minsum=25944>25928`; `s=159`: `25622<25928` |
| Uniform `V=45` | 154 | 8--12 | `s=155`: `H=1204`, `2 minsum=33426>33336`; `s=154`: `32994<33336` |
| Uniform `V=46` | 156 | 7--14 | `s=157`: `H=1071`, `2 minsum=26016>25928`; `s=156`: `25680<25928` |

The inherited distance-refined profile at `n=464` also has exact best bound
159, with optimizing `c=7,...,13`.  At the `c=7` boundary its allocation
uses only distances 1 through 23, all of which have inherited cap 48, so the
refinement cannot improve the uniform-48 calculation.

Thus the mandate's phrases “best `c=7`” and “`c=8`” identify valid lowest
optimizers, not unique optimizers.

## The 45 and 46 partial profiles at `n=464`

For target size `s=155`, span `L=463`, and `c=8`, one has `H=1204`.

| Low-distance hypothesis | `minsum` | Doubled value | Right side | Margin | Exact outcome |
|---|---:|---:|---:|---:|---|
| `V_d<=45` for `d<=27` | 16713 | 33426 | 33336 | 90 | excludes 155; best bound 154 |
| `V_d<=46` for `d<=27` | 16362 | 32724 | 33336 | -612 | does not exclude 155; best bound 156 |

For the 45 profile, the minimizing allocation takes 45 copies of each
distance 1 through 26 and 34 copies of distance 27.  Consequently, cap 45
at distance 27 is not used: caps 45 only through distance 26, with the
inherited cap 48 at distance 27, give the same 16713 and the same margin 90.

The supplied `d<=27` target is therefore sufficient but not componentwise
minimal.  Reoptimizing the full lemma gives sharper conditional thresholds:

- Starting from the inherited profile, cap 45 through distance 21 gives
  exact equality `2 minsum=33336` at `c=8` and best bound 155, so it does
  not close.  Cap 45 through distance 22 gives `2 minsum=33366`, margin 30,
  and best bound 154 at `c=8,9`; it closes.
- Starting from cap 46 through distance 27, additionally lowering the first
  16 distances to 45 leaves best bound 155.  Lowering the first 17 closes at
  `c=9`: `H=1350`, `minsum=20841`, and `41682>41670`, margin 12.  At the
  mandate's fixed `c=8`, 17 reductions only reach equality and 18 are needed.
- If unit reductions may concentrate at distance 1, the cap-46 profile needs
  12 units (`V_1:46->34`) to close at `c=8`; 11 units do not.  From the
  inherited profile, the global threshold is 35 units (`V_1:48->13`) and
  closes at `c=5` with `H=760`, `13904>13890`, margin 14; 34 units do not.

The prefix minimality statements use the exchange fact that, for a fixed
number of equal cap reductions, moving a reduction to an earlier distance
can only increase every relevant prefix minimum.  These are diagnostics for
future cap lemmas, not proved geometric caps.

## Exact conditional ladder, `n=450..465`

For each `n`, the profile is cap 45 through distance 27 and inherited
`2q(n-d)` elsewhere.  “Closes” means the neighbor lemma's exact best bound
is strictly below `ceil(n/3)`.

| `n` | `ceil(n/3)` | Exact best bound | Lowest optimizing `c` | Closes? |
|---:|---:|---:|---:|---|
| 450 | 150 | 152 | 7 | No |
| 451 | 151 | 152 | 7 | No |
| 452 | 151 | 152 | 8 | No |
| 453 | 151 | 152 | 8 | No |
| 454 | 152 | 153 | 7 | No |
| 455 | 152 | 153 | 7 | No |
| 456 | 152 | 153 | 7 | No |
| 457 | 153 | 153 | 7 | No |
| 458 | 153 | 153 | 8 | No |
| 459 | 153 | 153 | 8 | No |
| 460 | 154 | 154 | 7 | No |
| 461 | 154 | 154 | 7 | No |
| 462 | 154 | 154 | 7 | No |
| 463 | 155 | 154 | 7 | Yes |
| 464 | 155 | 154 | 8 | Yes |
| 465 | 155 | 154 | 8 | Yes |

The boundary arithmetic is:

- `n=462`: target 154, `c=7`, `H=1050`, `2 minsum=25560<25816`;
  the exact best bound is 154, so the method does not exclude the target.
- `n=463`: target 155, `c=7`, `H=1057`, `2 minsum=25896>25872`,
  margin 24, so the exact best bound is 154.
- `n=464`: target 155, `c=8`, margin 90.
- `n=465`: target 155, `c=8`, `33426>33408`, margin 18.

No row proves a new Ramsey upper bound until its stated low-distance cap is
proved geometrically.  In particular, failure at `n=462` is a failure of
this conditional capacity certificate, not evidence that a 154-set exists.

## Dual bracket status

The accepted rational dual certifies the exact statement
`sup S_464(w)/a_0(w) <= -16` on its inherited domain.  The token `-17.29`
is explicitly labeled heuristic in the mandate.  No literal feasible vector
and no exact score realizing or exceeding that lower endpoint were supplied.
Therefore the rigorous two-sided bracket `[-17.29,-16]` is UNDECIDED from
the pinned inputs; only its upper endpoint is certified.  A vector plus an
exact rational score would be required to promote the lower endpoint.

## R10 and reproducibility

`R3_SETUP_R10.md` records three pre-resumption items: the source indexing
discrepancy; a claimant boundary bug that raised an exception when total
profile capacity was already insufficient; and the frozen sensitivity miss
caused by checking only `c=8`.  The code bug was repaired before numerical
output, and the sensitivity conclusion was globally reoptimized before the
independent check.

Artifacts:

- `a7_exact_results.json`: exact certificate and full ladder.
- `a7_claimant.py`: cumulative-capacity claimant.
- `a7_independent_check.py`: independent explicit-multiset checker.
- `a7_independent_check.json`: checker result, `PASS`, zero errors.
- `R3_SETUP_PREDICTIONS.md`: frozen pre-execution predictions.
- `R3_SETUP_R10.md`: append-only discrepancies and dispositions.

Reproduce from the workspace root:

```text
python research_round3/setup/a7_claimant.py
python research_round3/setup/a7_independent_check.py research_round3/setup/a7_exact_results.json
```

CLAIM: Module A.2's literal q(n-1-d) gives cap 48 at n=465,d=39 | MY VALUE: q(425)=23, hence cap 46 | THEIR VALUE: cap 48 | VERDICT: FAIL | METHOD: Direct lookup in the literal H table

CLAIM: The accepted position-count convention uses q(n-d), corresponding to span n-d-1 | MY VALUE: at n=465,d=39, q(426)=24 and cap 48, with span 425 | THEIR VALUE: accepted Round-2 convention q(n-d) and cap 48 | VERDICT: PASS | METHOD: Independent source-position indexing and literal H-table lookup

CLAIM: At L=463, uniform cap 48 gives size bound 159 with c=7 | MY VALUE: bound 159; optimizing c values are 7 through 13 | THEIR VALUE: bound 159, best c=7 | VERDICT: PASS | METHOD: Exact first-forbidden-size scan for every admissible c

CLAIM: At n=464, the inherited distance-refined caps still give size bound 159 | MY VALUE: bound 159; the binding allocation uses only cap-48 distances 1 through 23 | THEIR VALUE: bound 159 | VERDICT: PASS | METHOD: Exact greedy profile minimum independently checked by explicit multiset expansion

CLAIM: At L=463, uniform cap 45 gives size bound 154 with c=8 | MY VALUE: bound 154; optimizing c values are 8 through 12 | THEIR VALUE: bound 154, c=8 | VERDICT: PASS | METHOD: Exact first-forbidden-size scan for every admissible c

CLAIM: At L=463, uniform cap 46 gives size bound 156 | MY VALUE: bound 156; optimizing c values are 7 through 14 | THEIR VALUE: bound 156 | VERDICT: PASS | METHOD: Exact first-forbidden-size scan for every admissible c

CLAIM: At n=464, cap 45 through d=27 gives H=1204 and 33426>33336 at c=8 | MY VALUE: minsum=16713, doubled value 33426, right side 33336, margin 90 | THEIR VALUE: minsum=16713 and 33426>33336 | VERDICT: PASS | METHOD: Exact per-distance prefix fill with independent expanded-multiset check

CLAIM: At n=464, cap 46 through d=27 gives doubled minimum 32724<33336 and does not close size 155 | MY VALUE: minsum=16362, doubled value 32724, right side 33336, best bound 156 | THEIR VALUE: 32724<33336 and failure | VERDICT: PASS | METHOD: Exact per-distance prefix fill and global scan over c

CLAIM: The cap-45-through-27 profile closes n=463 but not n=462 | MY VALUE: n=463 has bound 154<155 with margin 24 at c=7; n=462 has bound 154=ceil(462/3) | THEIR VALUE: 463 closure and 462 failure | VERDICT: PASS | METHOD: Exact profile capacity scan over all c at both spans

CLAIM: In the conditional ladder n=450..465, the cap-45-through-27 profile closes exactly n=463,464,465 | MY VALUE: closing set {463,464,465}; all n=450..462 have best bound at least ceil(n/3) | THEIR VALUE: 463 and 464 close, 462 fails; remaining ladder requested | VERDICT: PASS | METHOD: Sixteen-row exact scan with independently expanded distance multisets

CLAIM: The relaxation optimum has a rigorous bracket [-17.29,-16] from the supplied inputs | MY VALUE: not established; only the exact upper bound sup S_464/a_0<=-16 is certified | THEIR VALUE: heuristic bracket [-17.29,-16] | VERDICT: UNDECIDED | METHOD: Source audit found no literal feasible vector or exact score for the decimal lower endpoint
