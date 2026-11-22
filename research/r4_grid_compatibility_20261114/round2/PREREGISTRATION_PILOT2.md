# Lane B round 2, pilot 2: are the catalogued conflicts complete on small translate pairs? (pre-registered)

- **Date:** 2026-11-22.
- **Written:** before the check was run.
- **Owner instruction:** "Yes, run it".
- **Budget:** one worker, under 1 GiB, at most 15 minutes elapsed.

## Question

Round 1 recorded two uncolorable small-translate TSD instances with no G1 gadget:
- q = 17, t = 3, |A| = 12;
- q = 19, t = 3, |A| = 14.

The question was whether they contain a type I or type II conflict (`../siege/proof.md` §4.10, Proposition 2G).

The exact sets were not stored. Only their construction was:
1. take a Bose Sidon set mod q^2−1, viewed in [0, q^2−2];
2. delete points until no difference lies in [1, 2t];
3. put B = A + t.

So the check is run on the **whole family** of instances built that way, which is a strict superset of what the original question asked.

## Family

For q ∈ {13, 17, 19} and t ∈ {1, 2, 3}, and for random units u and shifts s mod q^2−1:
- A_0 = u·Bose(q) + s mod q^2−1, a Sidon set in Z inside [0, q^2−2] (verified for each instance);
- A is A_0 with points deleted greedily until no difference lies in [1, 2t];
- B = A + t.

## Measurements, per instance

1. TSD-colorable, by complete backtracking. Colorings are re-checked against every L.
2. C-collision present. Proposition O predicts none.
3. Type I conflict present, and type II conflict present. Both are computed exactly from the definitions of Proposition 2G: first-generation forced values φ_g, then one forcing step.
4. For uncolorable instances with no C-collision, type I or type II conflict: does full unit propagation from the fixed A-pairs and B-pairs (no branching) reach a contradiction? If not, how many branch decisions does the complete search use?

## Decision rules (fixed now)

- **Every uncolorable instance has a C-collision, type I or type II conflict.** The catalogue is complete on this family. Recommend stating NTSD's proof target as "near-maximality forces a type I or II conflict", and attacking that.
- **Some uncolorable instance has none of them, but unit propagation still refutes it.** Higher-generation forcing is needed. Record the shortest refuting chain found, and recommend extending the catalogue by one generation before any proof attempt.
- **Some uncolorable instance needs branching.** The obstruction is not a fixed-depth forcing chain. Record this as evidence against any local-gadget proof strategy for NTSD.

These are finite facts about the stated family only.
