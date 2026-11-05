# R3-R4 post-certificate follow-up freeze

Frozen after the independent PASS for `n=21991500` and before executing the
mandated one-step descent and alternate-profile comparison.

1. **Descent candidate.**  Test `n=21991300` with all other certified inputs
   unchanged: `t=36000`, polynomial weights, endpoint-refined globally
   optimized Golomb profile, and outer `c=650..760`.  Prediction: exact
   margin remains positive, producing a further 200-unit descent.
2. **Alternate profile.**  At `n=21991500`, remove the endpoint correction
   from both the Golomb and outer neighbor inequalities while retaining the
   distance-dependent profile and the same outer `c=650..760`.  Prediction:
   exact margin is negative.  This isolates the endpoint lemma's contribution.
3. **Fixed outer parameter sensitivity.**  The generated certificate already
   predicts that retaining the endpoint/profile refinement but fixing
   `c=662` gives the negative margin
   `-6962898885780397033435934400`; the independent follow-up will verify the
   role of per-span parameter selection.

Honesty label: **CONJECTURE / frozen before follow-up execution**.
