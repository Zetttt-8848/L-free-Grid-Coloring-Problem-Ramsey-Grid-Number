# round5_q1 answer: MS' (joint prefix-averaged fibre deficit)

## Plan (written first)
1. Audit the chain MS' => (D-a) step by step.
2. Look for a simpler conversion that needs less than MS' (a single window scale).
3. Calibrate what MS' contains (window-energy identity).
4. Necessary conditions for a counterexample, with explicit constants.
5. State clearly what stays OPEN.

## 0. Verdict
- **MS' is NOT settled here** (neither proved nor refuted). It stays OPEN.
- Everything below is partial and is labelled. Proved results:
  - (Sec. 1) The chain MS' => (D-a) is valid in steps 1-5. Step 6 contains a **direction error**: an upper bound on v_l is used where a lower bound is needed. A corrected version is given. Its explicit S_1(delta) is about (1/delta)^8, which is far above the regime scale. So at the regime the numeric certificate value has to be used, as the step-6 bullet already allows.
  - (Sec. 2, Theorem B) A simpler, exact conversion. It needs the joint deficit at **one** window length Lambda only, in the summed form M_w(Lambda) <= 3 alpha M_v(Lambda) + E. It gives an explicit delta' of about delta/2. It needs no Pi-form recertification: the comparison cap is exactly the P-form cap at the same rank. MS' implies its hypothesis.
  - (Sec. 3) Window-energy identity. The hypothesis of Theorem B equals (class sizes)^2 term + (local variance) term. So for well-spread classes, MS' at the critical scale is **equivalent** to the size deficit it is meant to give. A prefix formulation does not make the problem easier.
  - (Sec. 4, Proposition N) Any failure of MS' with delta <= 1/6 and S >= 146 forces **all three** classes S_e(d) to have more than S^{5/8}/16 elements. MS' holds trivially for lambda <= S/(600 delta (sqrt(2S)+1)).

