# Lane B round 2: attack on the counting lemma CL

**Status: CL is not proved.**

- **Proved:** an exact reformulation of CL as a statement about the sum/width map of a Sidon set (Theorem W).
- **Corrected:** an overclaim in `NTSD_F_ATTEMPT.md` (§1 below).
- **Isolated:** two obstacles that rule out the standard tools (§3).
- **No claim about R_4.**

## 1. Correction: G1+ is G1

Suppose A has no difference in [1, 2t].
- If a + b = x + z + t and x + t < b < z, then a = x + z + t − b also lies in (x+t, z).
- If c + d = x + z − t and x < d < z − t, then c also lies in (x, z − t).

So the G1+ configuration has all four summands strictly between x and z. That is exactly round 1's gadget G1: y_1 + y_2 = x + y − t and z_1 + z_2 = x + y + t, all four strictly between x and y.

The earlier claim that G1+ strictly contains G1 is withdrawn. The four-L proof stands as a re-derivation. CL is therefore the round-1 "Counting Lemma G1(t)".

## 2. Theorem W: the width reformulation (PROVED)

Let A be a Sidon set, meaning all positive differences are distinct, with no positive difference in [1, 2t]. Let S = {p + q : p ≤ q in A}.

**Facts.**
- (a) Every s ∈ S has a unique representation s = p + q with p ≤ q.
  - If s = p + q = p' + q' with p < p' ≤ q' < q, then q − q' = p' − p.
  - If p' < q', that is a repeated positive difference.
  - If p' = q', then p' − p = q − p' is a positive difference occurring for both pairs (p, p') and (p', q).
- (b) Define the width w(s) = q − p ≥ 0. Then w is injective on {s ∈ S : w(s) > 0}, since equal widths are equal differences.

**Theorem W.** A contains x < z, b and d with
- x + t < b < z and x + z + t − b ∈ A, and
- x < d < z − t and x + z − t − d ∈ A,

if and only if there is s ∈ S with w(s) > 0, s − t ∈ S, s + t ∈ S and

  w(s) ≥ max(w(s−t), w(s+t)) + t + 1.

Call such an s a **t-peak**. The doubles s ± t = 2y, of width 0, are allowed.

*Proof.* Put s = x + z and w = z − x, so x = (s−w)/2 and z = (s+w)/2.
- Let s + t = a + b with a ≤ b and width w' = b − a. Both summands lie in (x+t, z) iff b < z and a > x + t. Writing a = (s+t−w')/2 and b = (s+t+w')/2, each of the two inequalities is equivalent to w' < w − t.
- By §1, some summand lies in (x+t, z) iff both do.
- Likewise, let s − t = c + d with width w''. Both summands lie in (x, z−t) iff w'' < w − t.
- Since widths are integers, w' < w − t means w' ≤ w − t − 1. ∎

**Computer check.** The two counts agree exactly. Over 81 Bose-derived sets and 400 random Sidon sets, the number of t-peaks equals the number of pairs (x, z) carrying a G1 configuration, with 0 mismatches (`cl_peak_stats.json`).

**Consequence.** CL(β, t, m_0) is equivalent to the following statement: every near-maximal Sidon set with no small differences has a t-peak. The statement now involves only the sum/width map of A. That map is the bijection between the representable sums (other than doubles) and the positive differences, s ↦ w(s).

## 3. Obstacles (why the standard tools do not reach CL)

1. **Density of A + A is not enough.** A peak needs a three-term progression s − t, s, s + t inside S.
   - For a Sidon set of size about sqrt(m), S has density about 1/4 in [0, 2m].
   - A set of density 2/3 can contain no such progression, e.g. {s : ⌊s/t⌋ ≢ 2 mod 3}.
   - So the existence of progressions in S needs the Sidon structure, not just the size of S.
2. **Linear Fourier counting is at the wrong scale.**
   - The data below suggest about 0.01·|A|^2 peaks, which is of order m.
   - Counting the six-variable G1 system by Fourier analysis bounds the error by roughly sup_ξ |f̂(ξ)|·|A|^3, where f is the balanced indicator of A.
   - Dense Sidon sets in an interval can have |f̂(ξ)| of order |A| at nonzero frequencies; Erdős–Turán type sets concentrate near multiples of 2p. Even the square-root-cancellation size sqrt(|A|) would leave the error about |A|^{3.5}, far above |A|^2.
   - So no Fourier-uniformity hypothesis of the usual strength can give CL. This is an order-of-magnitude argument, not a theorem.
3. **Pair statistics do not see peaks.** Energy and difference counts are symmetric under re-pairing structures that preserve multiplicities. A peak is an order relation among three widths, which those statistics do not record.

## 4. Evidence

Bose-derived sets with small differences removed, three sets per row (`cl_peak_stats.json`):

| q | \|A\| ≈ | span ≈ | t | min #peaks | mean peaks/\|A\|^2 | mean t-progressions in S per \|A\|^2 |
|---:|---:|---:|---:|---:|---:|---:|
| 23 | 21 | 482 | 1 | 2 | 0.015 | 0.038 |
| 29 | 27 | 793 | 1 | 6 | 0.009 | 0.030 |
| 37 | 35 | 1256 | 1 | 14 | 0.014 | 0.045 |
| 41 | 39 | 1631 | 1 | 12 | 0.012 | 0.039 |
| 43 | 41 | 1771 | 1 | 22 | 0.017 | 0.046 |
| 43 | 38 | 1800 | 3 | 13 | 0.009 | 0.027 |

- At q ≥ 23, every sampled set has a peak.
- The proportion of progressions that are peaks is about 0.3–0.4, close to the 1/3 a random order of three widths would give.
- The peak count scales like |A|^2.

This is evidence only, for these sets.

## 5. Assessment and recommendation

On this evidence CL looks true, with about 0.01|A|^2 peaks. Proving it is a problem of counting a sparse additive pattern inside a sparse set:
- the first difficulty is proving that A + A contains many t-progressions;
- the second is proving that the widths along them are not monotone.

No route through density, energy or linear Fourier methods exists, for the reasons in §3. I found no combinatorial argument that uses the sum/width bijection strongly enough.

**Payoff for R_4 is remote.** CL would settle only the translate part of NTSD. NTSD helps R_4 only through Theorem R, which is vacuous below spans of about 1.7·10^9.

**Recommendation.** Stop the NTSD/CL line in lane B here, and record CL as an open problem with the reformulation above. Spend lane-B effort on a statement with a nearer R_4 consumer. The candidates are:
- certifying the single-class Fejér-versus-rank comparison, which needs coordination with lane A;
- revisiting the outer aggregation.

The choice should be made jointly with Codex.
