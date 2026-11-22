# Lane B round 2: proof attempt on NTSD-F

**Status: NTSD-F is not proved.**

- **Proved:** the local obstruction G1+, with a four-L proof. As corrected below, it coincides with the round-1 gadget G1 for sets with no small differences, so the proof is an independent re-derivation.
- **Reduced:** for translate pairs (the case Theorem P leaves open), NTSD follows from a single explicit counting statement about Sidon sets, CL(β, t) below.
- **Open:** CL(β, t), and the collision-free pairs that are not translates.
- **No claim about R_4.**

Notation is that of `../siege/proof.md` §4.9–4.10. A TSD instance is (A, B, c) with A and B disjoint Sidon sets, and c a 2-coloring of the pairs of U = A ∪ B with these properties:
- c = 0 on A-pairs;
- c = 1 on B-pairs;
- for all u < v in U and g > 0 with u+g, v+g ∈ U, the values c(u,u+g), c(v,v+g) and c(u,v+g) are not all equal.

## 1. Statement under attack

**NTSD-F.** For small β and m ≥ m_0, every collision-free pair of disjoint Sidon sets with |A|, |B| ≥ (1−β)Q(m) contains one of the following:
- a type I or type II conflict (Proposition 2G);
- a mixed cell both of whose values lead to such a conflict after one propagation step.

By Theorem P, the collision-free pairs are exactly those that first-generation forcing cannot refute. Proposition O shows that translates B = A + t (with A free of differences in [1, 2t]) are collision-free. This attempt treats that family.

## 2. Proposition G1+ (PROVED)

**Proposition G1+.** Let t ≥ 1, and let A be a set of integers with A ∩ (A+t) = ∅. Put B = A + t and U = A ∪ B. Suppose that x < z in A, b, d ∈ A satisfy

- x + t < b < z and a := x + z + t − b ∈ A,
- x < d < z − t and e := x + z − t − d ∈ A.

Then no 2-coloring c of the pairs of U with c = 0 on A-pairs, c = 1 on B-pairs, and no monochromatic L exists. In particular, if A and B are Sidon, (A, B) carries no TSD coloring.

*Proof.* Put g_1 = z − b > 0 and g_2 = z − t − d > 0. The target is the mixed cell (x+t, z): x+t ∈ B and z ∈ A. Every L below is checked against the definition: u < v, u + g ∈ U and v + g ∈ U.

1. **L1:** u = x+t, v = b+t, g = g_1.
   - The cells are (x+t, a), (b+t, z+t) and (x+t, z+t). Note x+t+g_1 = a and b+t+g_1 = z+t.
   - The last two are B-pairs, so both equal 1. Hence c(x+t, a) = 0.
2. **L2:** u = x+t, v = b, g = g_1. It is valid because x+t < b.
   - The cells are (x+t, a) = 0, (b, z), which is an A-pair equal to 0, and (x+t, z).
   - Hence **c(x+t, z) = 1**.
3. **L3:** u = x, v = d+t, g = g_2. It is valid because x < d < d+t.
   - The cells are (x, e), (d+t, z) and (x, z). Note x+g_2 = e and d+t+g_2 = z.
   - The first and the last are A-pairs, so both equal 0. Hence c(d+t, z) = 1.
4. **L4:** u = x+t, v = d+t, g = g_2.
   - The cells are (x+t, e+t), a B-pair equal to 1, then (d+t, z) = 1, then (x+t, z).
   - Hence **c(x+t, z) = 0**.

Steps 2 and 4 contradict each other. ∎

**Remarks.**
- Only A ∩ (A+t) = ∅ and the stated memberships and orders are used. The Sidon property is needed only for (A, B) to be a TSD instance.
- If A has no difference in [1, 2t], then x + t < b holds automatically for every b ∈ A with b > x.
- **Correction (2026-11-22, see `CL_ATTACK.md` §1).** An earlier version of this note claimed that G1+ strictly contains the round-1 gadget G1, because a and e could lie outside (x, z). That claim is **false**.
  - If x+t < b < z, then a = x+z+t−b also lies in (x+t, z).
  - If x < d < z−t, then e = x+z−t−d also lies in (x, z−t).
  - So for A with no difference in [1, 2t], G1+ is exactly the base form of G1.
  - The four-L proof above is an independent re-derivation of round 1's G1 result, not a new obstruction. The larger G1+ coverage counts in this note, compared with round 1's G1 counts, come from different samples and from round 1's separate treatment of mirror forms, not from a more general gadget.
- In the language of Proposition 2G, G1+ is a type II conflict on the cell (x+t, z):
  - it is forced to 1 from lag g_1, by the BA start x+t and the AA start b;
  - it is forced to 0 from lag g_2, by the BB start x+t and the BA start d+t.

**Computer check (evidence only).** `g1plus_check.py` (seed 20261123, 600 s) ran on 245,099 translate instances: random Sidon sets with no small differences, plus Bose-derived sets.
- 76,694 of them contain a G1+ configuration. None of these 76,694 is colorable, as the proposition requires. Every coloring found elsewhere was re-checked against every L.

## 3. Reduction for translates

Consider the **counting lemma CL(β, t, m_0)**: every Sidon set A in m+1 consecutive integers, m ≥ m_0, with no positive difference in [1, 2t] and |A| ≥ (1−β)Q(m), contains x < z, b and d as in Proposition G1+.

**Corollary (PROVED from Proposition G1+).** CL(β, t, m_0) implies that no translate pair (A, A+t) with |A| ≥ (1−β)Q(m) and m ≥ m_0 is a TSD instance. This is the translate part of NTSD, and of NTSD-F (a type II conflict).

Equivalently, CL asks for x < z in A such that
- x + z + t ∈ A + (A ∩ (x+t, z)), and
- x + z − t ∈ A + (A ∩ (x, z−t)).

That is, for a pair whose sum s = x + z has both neighbors s ± t in the restricted sumsets.

**Why CL is not immediate.**
- For a Sidon set of size about sqrt(m), A + A has density about 1/4 in [0, 2m]. A set of density 1/4 can avoid every pattern s, s+t, s−t.
- The Sidon property alone therefore does not give CL. Near-maximality must be used, for example through equidistribution of A in intervals and residue classes.
- CL is a triple correlation of the sumset indicator r_A = 1_A * 1_A, namely Σ_s r_A(s) r_A(s+t) r_A(s−t) with order restrictions. Additive energy controls only pair correlations of r_A, which is why the round-1 energy and Fourier-magnitude methods could not decide it.

**Evidence on Bose-derived sets** (`g1plus_counts.json`, 6 sets per row). This is the mean number of pairs (x, z) carrying a G1+ configuration:

| q | span ≈ | t = 1 | t = 3 |
|---:|---:|---:|---:|
| 13 | 150 | 0.7 | 0.0 |
| 17 | 250 | 2.5 | 0.3 |
| 19 | 320 | 3.8 | 0.3 |
| 23 | 485 | 5.2 | 0.8 |
| 29 | 785 | 9.0 | 4.7 |
| 31 | 905 | 9.8 | 3.5 |
| 37 | 1290 | 20.2 | 8.7 |

The count grows with the span; at q ≥ 29 every sampled set contains a G1+ configuration. For uncolorable Bose-derived translate instances, the share explained by G1+ alone also rises: 10/37 at q = 13, 24/44 at q = 17, 33/45 at q = 19 and 42/45 at q = 23. Type I/II conflicts and unit propagation explain the rest (`g1plus_results.json`). This is evidence only, for exactly these sets.

## 4. What remains

1. **CL(β, t, m_0) itself.** This is the cleanest open statement on this route: a lower bound on a restricted triple correlation of A + A for near-maximal Sidon sets with no small differences. A natural proof strategy is to model A by a density-(Q(m)/m) subset of [0, m], and to bound the error with equidistribution of near-maximal Sidon sets in intervals. That would need an explicit equidistribution theorem with constants, which is cited from memory in the round-1 notes, not proved there.
2. **Collision-free pairs that are not translates.** Neither Proposition G1+ nor CL addresses them. Theorem P says they must be refuted through L's with mixed spanning cells, but no structural description of such pairs beyond translates is known.
3. **The R_4 consumer is unchanged.** Even NTSD in full would help R_4 only through Theorem R, whose constants are vacuous below spans of about 1.7·10^9 (`../siege/proof.md` §4.9). Any R_4 use would need an NTSD with β > 0.046 at spans near 2.2·10^7, together with the certified constants listed there.

## Reproduction

```text
python research/r4_grid_compatibility_20261114/round2/g1plus_check.py 600
```

The counts table was produced by the inline script recorded in the session log. Its output is stored in `g1plus_counts.json`. Seeds are fixed.
