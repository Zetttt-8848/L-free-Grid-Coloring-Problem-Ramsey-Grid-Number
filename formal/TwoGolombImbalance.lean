import TwoGolomb

set_option autoImplicit false

namespace EnergyForcing.Counting

def imbalance (B C : Finset ℤ) : ℝ := |(B.card:ℝ)-(C.card:ℝ)|

noncomputable def imbalanceEta (B C : Finset ℤ) : ℝ :=
  ((B.card:ℝ)+(C.card:ℝ))*max (imbalance B C-1) 0/2

theorem real_M (A : Finset ℤ) :
    (M A:ℝ)=(A.card:ℝ)*((A.card:ℝ)-1)/2 := Nat.cast_choose_two ℝ A.card

theorem real_E (A : Finset ℤ) :
    (E A:ℝ)=2*(A.card:ℝ)^2-(A.card:ℝ)+4*(T A:ℝ) := by
  have hn := square_eq_self_add_twice_choose A.card
  have he := energy_corner_identity A
  have ha : E A+A.card=2*A.card^2+4*T A := by omega
  have hr : (E A:ℝ)+(A.card:ℝ)=2*(A.card:ℝ)^2+4*(T A:ℝ) := by exact_mod_cast ha
  linarith

theorem size_Q_deficit (b c U q : ℝ) (hb:0≤b) (hc:0≤c)
    (hU:2*U=b*(b-1)+c*(c-1)) (hqU:q≤U) (hqb:q≤b^2) (hqc:q≤c^2) :
    (b+c)*max (|b-c|-1) 0/2≤U-q := by
  by_cases hbc : b≤c
  · rw [abs_of_nonpos (by linarith : b-c≤0)]
    by_cases hs : -(b-c)-1≤0
    · rw [max_eq_right hs]; nlinarith
    · rw [max_eq_left (by linarith : 0≤-(b-c)-1)]
      nlinarith
  · rw [abs_of_nonneg (by linarith : 0≤b-c)]
    by_cases hs : b-c-1≤0
    · rw [max_eq_right hs]; nlinarith
    · rw [max_eq_left (by linarith : 0≤b-c-1)]
      nlinarith

theorem size_rho_deficit (b c U ρ : ℝ)
    (hU:2*U=b*(b-1)+c*(c-1))
    (hρb:2*ρ≤b*(b-1)) (hρc:2*ρ≤c*(c-1)) :
    (b+c-1)*|b-c|/2≤U-2*ρ := by
  by_cases hbc : b≤c
  · rw [abs_of_nonpos (by linarith : b-c≤0)]
    nlinarith
  · rw [abs_of_nonneg (by linarith : 0≤b-c)]
    nlinarith

theorem Q_imbalance_deficit (B C : Finset ℤ)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    imbalanceEta B C≤(M B:ℝ)+(M C:ℝ)-(Q B C:ℝ) := by
  have hU := Q_le_U B C hB hC
  have hb := Q_le_B_sq B C hC
  have hc := Q_le_C_sq B C hB
  apply size_Q_deficit (B.card:ℝ) (C.card:ℝ) ((M B:ℝ)+(M C:ℝ)) (Q B C:ℝ)
      (by positivity) (by positivity)
  · rw [real_M,real_M]; ring
  · exact_mod_cast hU
  · exact_mod_cast hb
  · exact_mod_cast hc

theorem rho_imbalance_deficit (B C : Finset ℤ)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    ((B.card:ℝ)+(C.card:ℝ)-1)*imbalance B C/2≤
      (M B:ℝ)+(M C:ℝ)-2*(rho B C:ℝ) := by
  have hb : (rho B C:ℝ)≤(M B:ℝ) := by exact_mod_cast rho_le_M_left B C hB
  have hc : (rho B C:ℝ)≤(M C:ℝ) := by exact_mod_cast rho_le_M_right B C hC
  apply size_rho_deficit (B.card:ℝ) (C.card:ℝ) ((M B:ℝ)+(M C:ℝ)) (rho B C:ℝ)
  · rw [real_M,real_M]; ring
  · rw [real_M] at hb; linarith
  · rw [real_M] at hc; linarith

theorem imbalance_T_first (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (T (B∪C):ℝ)≤2*(M (B∪C):ℝ)-
      ((B.card:ℝ)+(C.card:ℝ)-1)*imbalance B C/2-imbalanceEta B C := by
  have ht : (T (B∪C):ℝ)=2*(rho B C:ℝ)+(Ncross B C:ℝ)+(Q B C:ℝ) := by
    exact_mod_cast two_golomb_corner_identity B C hBC hB hC
  have hn : (Ncross B C:ℝ)≤2*((B.card:ℝ)*(C.card:ℝ)) := by
    exact_mod_cast Ncross_le_twice_cross_mass B C hBC hB hC
  have hm : (M (B∪C):ℝ)=(M B:ℝ)+(M C:ℝ)+(B.card:ℝ)*(C.card:ℝ) := by
    exact_mod_cast M_union B C hBC
  have hq := Q_imbalance_deficit B C hB hC
  have hr := rho_imbalance_deficit B C hB hC
  linarith

theorem imbalance_T_second (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (T (B∪C):ℝ)≤(M (B∪C):ℝ)+5*(rho B C:ℝ)-imbalanceEta B C := by
  have ht : (T (B∪C):ℝ)=2*(rho B C:ℝ)+(Ncross B C:ℝ)+(Q B C:ℝ) := by
    exact_mod_cast two_golomb_corner_identity B C hBC hB hC
  have hn : (Ncross B C:ℝ)≤(B.card:ℝ)*(C.card:ℝ)+3*(rho B C:ℝ) := by
    exact_mod_cast Ncross_le_cross_mass_add_rho B C hBC hB hC
  have hm : (M (B∪C):ℝ)=(M B:ℝ)+(M C:ℝ)+(B.card:ℝ)*(C.card:ℝ) := by
    exact_mod_cast M_union B C hBC
  have hq := Q_imbalance_deficit B C hB hC
  linarith

theorem imbalance_T_bound (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (T (B∪C):ℝ) ≤ min (2*(M (B∪C):ℝ)-
      ((B.card:ℝ)+(C.card:ℝ)-1)*imbalance B C/2)
      ((M (B∪C):ℝ)+5*(rho B C:ℝ))-imbalanceEta B C := by
  have h1 := imbalance_T_first B C hBC hB hC
  have h2 := imbalance_T_second B C hBC hB hC
  rw [min_def]
  split_ifs <;> assumption

theorem imbalance_energy_bound (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (E (B∪C):ℝ)≤6*((B.card:ℝ)+(C.card:ℝ))^2-5*((B.card:ℝ)+(C.card:ℝ))-
      2*((B.card:ℝ)+(C.card:ℝ)-1)*imbalance B C-4*imbalanceEta B C := by
  have ht := imbalance_T_first B C hBC hB hC
  have he := real_E (B∪C)
  have hm := real_M (B∪C)
  rw [Finset.card_union_of_disjoint hBC,Nat.cast_add] at he hm
  nlinarith

theorem imbalance_stability (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) (ε : ℝ)
    (hn : 2≤B.card+C.card) (hε : 0≤ε)
    (hnear : (2-ε)*(M (B∪C):ℝ)≤(T (B∪C):ℝ)) :
    imbalance B C ≤ min (ε*((B.card:ℝ)+(C.card:ℝ)))
      ((((B.card:ℝ)+(C.card:ℝ))+ε*((B.card:ℝ)+(C.card:ℝ))*((B.card:ℝ)+(C.card:ℝ)-1))/
        (2*((B.card:ℝ)+(C.card:ℝ))-1)) := by
  have hn' : (2:ℝ)≤(B.card:ℝ)+(C.card:ℝ) := by exact_mod_cast hn
  have ht := imbalance_T_first B C hBC hB hC
  have hm := real_M (B∪C)
  rw [Finset.card_union_of_disjoint hBC,Nat.cast_add] at hm
  have heta : 0≤ imbalanceEta B C := by unfold imbalanceEta; positivity
  have he : ((B.card:ℝ)+(C.card:ℝ))*(imbalance B C-1)/2≤ imbalanceEta B C := by
    unfold imbalanceEta
    exact div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left (le_max_left _ _) (by positivity)) (by norm_num)
  apply le_min
  · nlinarith
  · apply (le_div_iff₀ (by linarith : (0:ℝ)<2*((B.card:ℝ)+(C.card:ℝ))-1)).mpr
    nlinarith

end EnergyForcing.Counting

