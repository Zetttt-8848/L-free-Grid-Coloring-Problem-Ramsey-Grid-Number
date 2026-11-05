import Std
namespace EnergyForcing

/- These are arithmetic lemmas only. They do not formalize the combinatorial
   arguments that produce their hypotheses. -/

theorem progression_polynomial_identity (x : Int) :
    6*(5+x)^3 - 44*(5+x)^2 + 81*(5+x) - 34 =
      6*x^3 + 46*x^2 + 91*x + 21 := by
  simp only [Int.pow_succ, Int.pow_zero, Int.mul_one, Int.one_mul, Int.mul_add, Int.add_mul,
    Int.mul_assoc, Int.mul_comm, Int.mul_left_comm]
  have h46 : x*(x*46)=46*(x*x) := by simp [Int.mul_assoc,Int.mul_comm,Int.mul_left_comm]
  have h30 : x*(x*(5*6))=30*(x*x) := by simp [Int.mul_assoc,Int.mul_comm,Int.mul_left_comm]
  have h44 : x*(x*44)=44*(x*x) := by simp [Int.mul_assoc,Int.mul_comm,Int.mul_left_comm]
  omega

theorem progression_polynomial_positive (x : Nat) :
    0 < 6*x^3 + 46*x^2 + 91*x + 21 := by omega

theorem progression_t3_numerator (b : Int) (hb : 3 ≤ b) : 0 ≤ 15*b-40 := by omega
theorem progression_t4_numerator (b : Int) (hb : 2 ≤ b) : 0 ≤ 90*b-120 := by omega

theorem progression_exception_3_1 : 19 ≤ 9*3^2-15*3 := by decide
theorem progression_exception_3_2 : 114 ≤ 9*6^2-15*6 := by decide
theorem progression_exception_4_1 : 44 ≤ 9*4^2-15*4 := by decide

theorem conditional_361_gap : (121*120)/2 > 20*(361-1) := by decide
theorem conditional_379_gap : (127*126)/2 > 21*(379-1) := by decide
theorem conditional_99996_gap :
    24999*24999*550 > (99995+550)*(24999+6153*(550-1)) := by decide

theorem conditional_99000_cap_numeric : 2040*2039 > 42*98998 := by decide

theorem conditional_99000_fiber_cap (s : Nat) (h : s*(s-1) ≤ 42*98998) : s ≤ 2039 := by
  by_cases hn : s ≤ 2039
  · exact hn
  · have hs : 2040 ≤ s := by omega
    have hs1 : 2039 ≤ s-1 := by omega
    have hm := Nat.mul_le_mul hs hs1
    omega

theorem conditional_99000_gap :
    24750*24750*575 - (98999+575)*(24750+6117*(575-1)) = 138934308 := by decide

theorem conditional_99000_contradiction :
    24750*24750*575 > (98999+575)*(24750+6117*(575-1)) := by decide

theorem rejected_weight_gap_11 :
    5*944436978 - 45000*104805 = 5959890 := by decide
theorem rejected_weight_gap_12 :
    7*809226900 - 55000*102982 = 578300 := by decide

#print axioms progression_polynomial_identity
#print axioms progression_polynomial_positive
#print axioms conditional_361_gap
#print axioms conditional_379_gap
#print axioms conditional_99996_gap
#print axioms conditional_99000_fiber_cap
#print axioms conditional_99000_contradiction
#print axioms rejected_weight_gap_11
#print axioms rejected_weight_gap_12
/-- Consecutive integer roots leave no integer in the negative interval. -/
theorem consecutive_integer_product (s k : Int) : 0≤(s-k)*(s-(k+1)) := by
  by_cases h : s≤k
  · exact Int.mul_nonneg_of_nonpos_of_nonpos (by omega) (by omega)
  · exact Int.mul_nonneg (by omega) (by omega)

/-- Universal tangent inequality used in the improved conditional four-color bound. -/
theorem integer_quadratic_tangent (s k : Int) :
    (2*k)*s≤s*(s-1)+k*(k+1) := by
  have hp := consecutive_integer_product s k
  have he : (s-k)*(s-(k+1))=s*(s-1)+k*(k+1)-(2*k)*s := by
    simp only [Int.mul_sub,Int.sub_mul,Int.mul_add,Int.add_mul,Int.mul_one]
    rw [Int.mul_comm s k,Int.mul_assoc 2 k s]
    omega
  omega

theorem tangent_2035 (s ℓ h : Int) (hs : s*(s-1)≤42*(ℓ-h)) :
    4070*s≤42*(ℓ-h)+4143260 := by
  have ht := integer_quadratic_tangent s 2035
  omega

theorem three_class_tangent (s₁ s₂ s₃ ℓ h : Int)
    (h₁ : s₁*(s₁-1)≤42*(ℓ-h)) (h₂ : s₂*(s₂-1)≤42*(ℓ-h))
    (h₃ : s₃*(s₃-1)≤42*(ℓ-h)) :
    4070*(s₁+s₂+s₃)≤126*(ℓ-h)+12429780 := by
  have := tangent_2035 s₁ ℓ h h₁
  have := tangent_2035 s₂ ℓ h h₂
  have := tangent_2035 s₃ ℓ h h₃
  omega

theorem conditional_98777_gap :
    (4070*24695^2*600 : Int)-
      99376*(4070*24695+599*24850314)=3161813264 := by decide

theorem conditional_98777_contradiction :
    (4070*24695^2*600 : Int)>
      99376*(4070*24695+599*24850314) := by decide

/-- Exact arithmetic used by the revised alteration construction. -/
theorem alteration_q_power_bound : (32:Nat)^32<3*31^32 := by decide
theorem alteration_expectation_margin : (32:Nat)*720-3*31>31*720 := by decide
theorem alteration_energy_exponent : (4:Nat)*26-31=73 := by decide

#print axioms integer_quadratic_tangent
#print axioms three_class_tangent
#print axioms conditional_98777_contradiction
#print axioms alteration_q_power_bound
#print axioms alteration_expectation_margin
end EnergyForcing
