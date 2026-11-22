# Lane B, round 1: final report (R4-PAIR-20261114-v2)

**Outcome.** No new bound on `R_4`. The P1 package is fully proved. Part D (a proportional joint saving) is reduced to precisely stated open statements and is not settled.

- **Branch:** `claude/r4-grid-compatibility-20261114`
- **Base commit:** `726998b9` (PR #11 head as pinned in the agreement).
- **Owner:** Claude (lane B).
- **Main document:** `siege/proof.md`. It is self-contained, and its Status section is authoritative for this round.
- **Verify report:** a step-by-step check of the draft found no fatal error. One Status overclaim was repaired in the final version.

## Status by deliverable

| Item | Status | Where |
|---|---|---|
| B0: exact sensitivity of the outer inequality to `X_d <= (1-delta) U_d` | Computed exactly; HYPOTHETICAL | `b0/` |
| D1: pre-registered U1 and UW(1) | REFUTED by checked witnesses | `D1_PREREGISTRATION.md`, `d1/` |
| P1 (i)–(v): request reformulation, double cover, forced Golomb membership | PROVED | `proof.md`, Theorem 1 |
| (D-b) over arbitrary ternary sources | PROVED | `proof.md`, Section 2 |
| (D-c) forced-color alternative | Settled as stated: forced sets are Sidon, and there is no imbalance without near-extremality | `proof.md`, Section 3 |
| Reduction of per-shift (D-a) to FD | PROVED, with error `O(S^{-3/8})` | `proof.md`, Section 4 |
| NTSD implies FD | PROVED, but vacuous at the R4 scale (`S_0 > 1.7*10^9`) | `proof.md`, Section 4.9 |
| FD, NTSD, SCD | OPEN | `proof.md`, Status |

## B0 (hypothetical; computed exactly)

**Caps held at their certified values** (`b0/b0_sensitivity.py`). The reproduction of both certified margins is exact.
- Elementary chain, delta = 1/100: excluded side 21,748,312.
- Window chain, delta = 1/100: excluded side 21,708,379.
- The window chain's twenty-shift correction is equivalent to delta ≈ 1.2·10^-7.

**Caps re-proved at the needed spans** (`b0/b0_recertified.py`, elementary chain). The certified table rows are reproduced exactly at three indices. The side falls by about 3.9·delta:

| Target side | Required delta |
|---|---|
| 21.9M | 0.00101 |
| 21.5M | 0.00565 |
| 21.0M | 0.01154 |
| 20.0M | 0.02364 |

**Additive savings.** About 63 starts per shift moves the side by about 1,000.

## D1

- **U1 refuted:** `D = [0,14)`, `h = 5`, `sum m^2 = 16 > 26/3`.
- **UW(1) refuted:** `D = [0,18)`, `h = 15`, `N_e = (5,5,5)`, `|F_h| = 3`.
- Both witnesses are checked by `d1/check_witness.py`, which shares no code with the search. The pre-registration was committed before the search.

## Main mathematical results (`proof.md`)

1. **Theorem 1 (P1).**
   - Every L of `V(D)` is `L(u,d,h)` for exactly one triple `1 <= d < h`, with corner `(u+h,u)`, arms `(u+d,u)` and `(u+h,u+h-d)`, and arm length `h-d`.
   - Properness is equivalent to `S_e(h) ∩ R_e(h) = ∅` for every `h` and `e`.
   - The double cover is a sharp identity: each start is requested by at most two colors, and a start requested twice is forced to the third color.
   - Foreign requests inside a class fix its Golomb-class membership.
   - The PR #11 chain uses only the same-class, same-shift case.
2. **Section 2: request counting fails for arbitrary sources.**
   - Digit families, proved proper L by L, refute UW(λ) for every λ, U1-type energy bounds for every C, and union growth, on any finite set of shifts.
   - A lifted family reaches class and fiber sizes of `span^{1/2-o(1)}`.
   - The Theorem 2.6 families (span ≥ 10^8) and the high-ratio lifted instances cannot be diagonal classes of a four-colored square. Embedding of small lifted members is not settled.
3. **Section 3: the forced-color route gives nothing alone.** An explicit proper family has full foreign coverage and balanced Golomb classes.
4. **Section 4: exact reduction.** Per shift and against the Fejér single-class cap `K_F ≈ sqrt(v_1 S)`, (D-a) is equivalent to:
   - **FD:** `|F_d(D)| <= 3(1-eta) sqrt(v_1 S)` for span `S >= S_0`.
   - Any violation needs three classes at one shift, each near the single-class cap, with saturated fibers.
5. **Section 4.9, Theorem R:** NTSD(β, m_0) implies FD(β/48, S_0), where NTSD says two disjoint near-maximal Sidon sets carry no TSD coloring. The constants are explicit but vacuous at span 2.2·10^7.
6. **Section 4.10, Theorem P:** the first-generation part of NTSD is decided exactly by collisions. This was checked on 2,990 random instances, as evidence only.

## Exports to Codex (interface fields)

| ID | Domain | Statement | Evidence | Consumer and bridge | Near-extremality |
|---|---|---|---|---|---|
| B-P1 | Ternary source `V(D)` | Theorem 1 | PROVED; verify report positive | Structural | None |
| B-FD-RED | Ternary source, one shift | Per-shift (D-a) is equivalent to FD up to `O(S^{-3/8})` (Theorem 4.5) | PROVED | U_d; FD missing | None |
| B-SCD | Binary source, span `S` | SCD (a single-class deficit `(1-eta) sqrt(v_1 S)`) implies FD (Prop. 4.6) | PROVED implication | **Lane A question** | None |
| B-NTSD | Two disjoint near-maximal Sidon sets | NTSD implies FD (Theorem R) | PROVED; vacuous at this scale | Missing NTSD | Named in the statement |
| B-B0 | Outer inequality | Response to `(1-delta) U_d` | HYPOTHETICAL | — | — |

**Hand-offs to lane A.**
- **SCD.** The single-binary-source deficit is the cleanest sufficient statement, and it lies in Codex's lane. The round-6 query on it (`siege/round6_q5.md`) was deliberately not run here.
- **Fejér cap remark.** The final document records a fragile heuristic: the Fejér-type cap `K_F` is about 0.3–0.8% below the rank cap `K` at this scale, depending on the certified Q-bound. If certified, this would be a single-class proportional saving. It is a lane-A matter; nothing here certifies it. **Update 2026-11-22:** recomputed with Codex's certified profile, K_F^♯ is 0.05% *above* the certified K, so there is no saving (`round2/NEXT_TARGETS.md` §1).

## Not done, and verification limits

- Two commit-wave queries (`r3_q2`, `r3_q3`, the two halves of an NTSD attack) were stopped by API safeguards and have no answer. Their work was not redone.
- No consumer comparison of the Fejér scale with the rank caps and staggering was certified.
- The window chain was not audited here. That audit belongs to Codex.
- The proof-attack workers could not run code. Computational claims in `proof.md` were rechecked by the judging steps with Python, as listed in its preamble.
- Project instructions observed on 2026-11-15 cite a Codex branch (`codex/r4-local-capacity-round3-20261114`) reporting `R_4 <= 21,947,865`. It was not reviewed in this round.

## Recommendation

Pivot. The request-union mechanism as such is closed for arbitrary sources, and its per-shift content reduces exactly to FD.

The concrete next task is one of the following:
- (a) Lane A attacks SCD at span about 2.2·10^7. This is also where the Fejér-versus-rank comparison should be certified.
- (b) Lane B runs a bounded exact search for NTSD failures at spans 30–200, to measure the largest β that NTSD could have. This is a falsification test only.

Which one to run is a joint decision for round 2.
