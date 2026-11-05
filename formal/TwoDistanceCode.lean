import Mathlib

set_option autoImplicit false
set_option maxHeartbeats 3000000
set_option maxRecDepth 10000

namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators

abbrev SignLabel := Fin 8→Bool
def sign (v : SignLabel) (i : Fin 8) : ℝ := if v i then 1 else -1
theorem sign_sq (v : SignLabel) (i : Fin 8) : (sign v i)^2=1 := by
  simp only [sign]; split_ifs <;> norm_num
theorem sign_ne_zero (v : SignLabel) (i : Fin 8) : sign v i≠0 := by
  simp only [sign]; split_ifs <;> norm_num
def signDot (v w : SignLabel) : ℝ := ∑i,sign v i*sign w i

def signFeature (v : SignLabel) : Fin 37→ℝ := ![1, sign v 0, sign v 1, sign v 2, sign v 3, sign v 4, sign v 5, sign v 6, sign v 7, sign v 0*sign v 1, sign v 0*sign v 2, sign v 0*sign v 3, sign v 0*sign v 4, sign v 0*sign v 5, sign v 0*sign v 6, sign v 0*sign v 7, sign v 1*sign v 2, sign v 1*sign v 3, sign v 1*sign v 4, sign v 1*sign v 5, sign v 1*sign v 6, sign v 1*sign v 7, sign v 2*sign v 3, sign v 2*sign v 4, sign v 2*sign v 5, sign v 2*sign v 6, sign v 2*sign v 7, sign v 3*sign v 4, sign v 3*sign v 5, sign v 3*sign v 6, sign v 3*sign v 7, sign v 4*sign v 5, sign v 4*sign v 6, sign v 4*sign v 7, sign v 5*sign v 6, sign v 5*sign v 7, sign v 6*sign v 7]
def signCoefficient (v : SignLabel) : Fin 37→ℝ := ![8, -4*sign v 0, -4*sign v 1, -4*sign v 2, -4*sign v 3, -4*sign v 4, -4*sign v 5, -4*sign v 6, -4*sign v 7, 2*sign v 0*sign v 1, 2*sign v 0*sign v 2, 2*sign v 0*sign v 3, 2*sign v 0*sign v 4, 2*sign v 0*sign v 5, 2*sign v 0*sign v 6, 2*sign v 0*sign v 7, 2*sign v 1*sign v 2, 2*sign v 1*sign v 3, 2*sign v 1*sign v 4, 2*sign v 1*sign v 5, 2*sign v 1*sign v 6, 2*sign v 1*sign v 7, 2*sign v 2*sign v 3, 2*sign v 2*sign v 4, 2*sign v 2*sign v 5, 2*sign v 2*sign v 6, 2*sign v 2*sign v 7, 2*sign v 3*sign v 4, 2*sign v 3*sign v 5, 2*sign v 3*sign v 6, 2*sign v 3*sign v 7, 2*sign v 4*sign v 5, 2*sign v 4*sign v 6, 2*sign v 4*sign v 7, 2*sign v 5*sign v 6, 2*sign v 5*sign v 7, 2*sign v 6*sign v 7]

theorem sign_dot_self (v : SignLabel) : signDot v v=8 := by
  simp only [signDot,← pow_two,sign_sq,Finset.sum_const,Finset.card_univ,
    Fintype.card_fin,nsmul_eq_mul,mul_one]
  norm_num

theorem sign_polynomial_identity (v w : SignLabel) :
    dotProduct (signCoefficient v) (signFeature w)=signDot v w*(signDot v w-4) := by
  norm_num [dotProduct,signCoefficient,signFeature,signDot,Fin.sum_univ_succ]
  simp only [show (2 : Fin 7).succ=(3 : Fin 8) by decide,
    show (2 : Fin 6).succ.succ=(4 : Fin 8) by decide,
    show (2 : Fin 5).succ.succ.succ=(5 : Fin 8) by decide,
    show (2 : Fin 4).succ.succ.succ.succ=(6 : Fin 8) by decide,
    show (2 : Fin 3).succ.succ.succ.succ.succ=(7 : Fin 8) by decide]
  ring_nf
  simp only [sign_sq]
  norm_num
  ring

theorem sign_code_card_le (C : Finset SignLabel)
    (hC : ∀v∈C, ∀w∈C, v≠w → signDot v w=0 ∨ signDot v w=4) : C.card ≤ 37 := by
  classical
  have hlin : LinearIndependent ℝ (fun v : C => signCoefficient v.val) := by
    apply Fintype.linearIndependent_iff.mpr
    intro a ha v
    have he : (∑w : C,a w*dotProduct (signCoefficient w.val) (signFeature v.val))=0 := by
      calc
        _ = dotProduct (∑w : C,a w • signCoefficient w.val) (signFeature v.val) := by
          simp only [dotProduct,Finset.mul_sum,Finset.sum_apply,Pi.smul_apply,
            smul_eq_mul,Finset.sum_mul]
          rw [Finset.sum_comm]
          apply Finset.sum_congr rfl
          intro j hj
          apply Finset.sum_congr rfl
          intro w hw
          ring
        _ = 0 := by rw [ha]; simp
    have hdot (w : C) : dotProduct (signCoefficient w.val) (signFeature v.val)=
        if w=v then 32 else 0 := by
      rw [sign_polynomial_identity]
      split_ifs with hw
      · subst w; rw [sign_dot_self]; norm_num
      · have hne : w.val≠v.val := fun hh => hw (Subtype.ext hh)
        rcases hC w.val w.property v.val v.property hne with hh|hh <;> rw [hh] <;> norm_num
    simp_rw [hdot] at he
    simp only [smul_eq_mul,mul_ite,mul_zero,Finset.sum_ite_eq',Finset.mem_univ,if_true,
      zero_dotProduct] at he
    linarith
  have hh := hlin.fintype_card_le_finrank
  simpa using hh

#print axioms sign_code_card_le
end EnergyForcing.TwoDistance
