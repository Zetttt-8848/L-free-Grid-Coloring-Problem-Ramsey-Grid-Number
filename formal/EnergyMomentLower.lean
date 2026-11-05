import CubeMoments

set_option autoImplicit false

namespace EnergyForcing.Counting
open scoped BigOperators

theorem allDiffs_card_le (A : Finset ℤ) : (allDiffs A).card≤2*span A+1 := by
  have hsub : allDiffs A⊆Finset.Icc (-(span A:ℤ)) (span A:ℤ) := by
    intro d hd
    by_cases hp : 0<d
    · have hd' : d∈posDiffs A := by rw [← allDiffs_pos]; exact Finset.mem_filter.mpr ⟨hd,hp⟩
      have hh := Finset.mem_Icc.mp (posDiffs_subset_interval A hd')
      apply Finset.mem_Icc.mpr; omega
    · by_cases hn : d<0
      · have hd' : -d∈posDiffs A := by
          rw [← allDiffs_pos]
          exact Finset.mem_filter.mpr ⟨(neg_mem_allDiffs A d).mpr hd,by omega⟩
        have hh := Finset.mem_Icc.mp (posDiffs_subset_interval A hd')
        apply Finset.mem_Icc.mpr; omega
      · apply Finset.mem_Icc.mpr; omega
  have hc := Finset.card_le_card hsub
  rw [Int.card_Icc] at hc
  omega

theorem all_diff_mass (A : Finset ℤ) : (∑d∈allDiffs A,r A d)=A.card^2 := by
  rw [sum_allDiffs_even A (r A) (r_neg A),r_zero,sum_r]
  exact (square_eq_self_add_twice_choose A.card).symm

theorem energy_fourth_lower (A : Finset ℤ) (ell : ℕ) (hspan:span A≤ell) :
    (A.card:ℝ)^4/(2*(ell:ℝ)+1)≤(E A:ℝ) := by
  have hs : (∑d∈allDiffs A,(r A d:ℝ))=(A.card:ℝ)^2 := by exact_mod_cast all_diff_mass A
  have he : (∑d∈allDiffs A,(r A d:ℝ)^2)=(E A:ℝ) := by exact_mod_cast (energy_all_count A).symm
  have hc := Finset.sum_mul_sq_le_sq_mul_sq (R:=ℝ) (allDiffs A)
    (fun _ => (1:ℝ)) (fun d => (r A d:ℝ))
  simp only [one_mul,one_pow,Finset.sum_const,nsmul_eq_mul,mul_one] at hc
  rw [hs,he] at hc
  have hcard : ((allDiffs A).card:ℝ)≤2*(ell:ℝ)+1 := by
    exact_mod_cast (show (allDiffs A).card≤2*ell+1 from (allDiffs_card_le A).trans (by omega))
  have hprod := mul_le_mul_of_nonneg_right hcard (show (0:ℝ)≤E A by positivity)
  apply (div_le_iff₀ (by positivity : (0:ℝ)<2*(ell:ℝ)+1)).mpr
  nlinarith

theorem energy_minus_square_nonneg (A : Finset ℤ) :
    0≤(E A:ℝ)-(A.card:ℝ)^2 := by
  have he : (E A:ℝ)=(A.card:ℝ)^2+2*(∑d∈posDiffs A,(r A d:ℝ)^2) := by
    exact_mod_cast energy_count A
  have hs : (0:ℝ)≤∑d∈posDiffs A,(r A d:ℝ)^2 := Finset.sum_nonneg (fun _ _ => sq_nonneg _)
  linarith

theorem energy_zero_separated_lower (A : Finset ℤ) (ell : ℕ)
    (hspan:span A≤ell) (hell:0<ell) :
    2*(M A:ℝ)^2/(ell:ℝ)≤(E A:ℝ)-(A.card:ℝ)^2 := by
  have hc := moment_cauchy A
  have hspan' : (span A:ℝ)≤(ell:ℝ) := by exact_mod_cast hspan
  have hm := mul_le_mul_of_nonneg_right hspan' (show (0:ℝ)≤(M A:ℝ)+2*(T A:ℝ) by positivity)
  have he := real_E A
  have hM := real_M A
  apply (div_le_iff₀ (by exact_mod_cast hell : (0:ℝ)<ell)).mpr
  nlinarith

theorem positiveFiber_span_le (A : Finset ℤ) (d : ℤ) (hd:0<d) :
    span (positiveFiber A d)≤span A-d.toNat := by
  by_cases hF : (positiveFiber A d).Nonempty
  · have hmin := (mem_positiveFiber A d _).mp (Finset.min'_mem _ hF)
    have hmax := (mem_positiveFiber A d _).mp (Finset.max'_mem _ hF)
    have hA : A.Nonempty := ⟨_,hmin.1⟩
    have hlo := Finset.min'_le A _ hmin.1
    have hhi := Finset.le_max' A _ hmax.2
    have hsF := span_cast (positiveFiber A d) hF
    have hsA := span_cast A hA
    omega
  · simp [span,hF]

theorem moment_fiber_energy_upper (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) (d : ℤ) (hd:0<d) :
    (E (positiveFiber A d):ℝ)≤6*(r A d:ℝ)^2-5*(r A d:ℝ)-
      2*((r A d:ℝ)-1)*imbalance (momentClass A z d false) (momentClass A z d true)-
      4*imbalanceEta (momentClass A z d false) (momentClass A z d true) := by
  have ht := moment_fiber_T_first A z hz d hd
  have he := real_E (positiveFiber A d)
  have hm := real_M (positiveFiber A d)
  change (E (positiveFiber A d):ℝ)=2*(r A d:ℝ)^2-(r A d:ℝ)+4*(T (positiveFiber A d):ℝ) at he
  change (M (positiveFiber A d):ℝ)=(r A d:ℝ)*((r A d:ℝ)-1)/2 at hm
  nlinarith

theorem fiber_energy_sum_upper (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (∑d∈posDiffs A,(E (positiveFiber A d):ℝ))≤
      (M A:ℝ)+12*(T A:ℝ)-2*Dmoment A z-4*Pmoment A z := by
  have hp := Finset.sum_le_sum (s:=posDiffs A) (fun d hd =>
    moment_fiber_energy_upper A z hz d ((mem_posDiffs A d).mp hd).1)
  simp only [Finset.sum_sub_distrib,← Finset.mul_sum] at hp
  have hr : (∑d∈posDiffs A,(r A d:ℝ))=(M A:ℝ) := by exact_mod_cast sum_r A
  have hr2 : (∑d∈posDiffs A,(r A d:ℝ)^2)=(M A:ℝ)+2*(T A:ℝ) := by exact_mod_cast sum_r_sq A
  have hd : (∑d∈posDiffs A,2*((r A d:ℝ)-1)*
      imbalance (momentClass A z d false) (momentClass A z d true))=2*Dmoment A z := by
    unfold Dmoment
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intros; ring
  rw [hr,hr2,hd] at hp
  change _≤6*((M A:ℝ)+2*(T A:ℝ))-5*(M A:ℝ)-2*Dmoment A z-4*Pmoment A z at hp
  linarith

theorem fourth_moment_support_bound (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (∑d∈posDiffs A,(r A d:ℝ)^4/(2*((span A-d.toNat:ℕ):ℝ)+1))≤
      (M A:ℝ)+12*(T A:ℝ)-2*Dmoment A z-4*Pmoment A z := by
  apply le_trans (Finset.sum_le_sum (fun d hd =>
    energy_fourth_lower (positiveFiber A d) (span A-d.toNat)
      (positiveFiber_span_le A d ((mem_posDiffs A d).mp hd).1)))
  exact fiber_energy_sum_upper A z hz

theorem sum_positive_extension (A : Finset ℤ) (f : ℤ→ℝ)
    (hf : ∀d,0<d → d∉posDiffs A → f d=0) :
    (∑d∈Finset.Icc (1:ℤ) (span A:ℤ),f d)=∑d∈posDiffs A,f d := by
  symm
  apply Finset.sum_subset (posDiffs_subset_interval A)
  intro d hd hn
  exact hf d (by have := (Finset.mem_Icc.mp hd).1; omega) hn

theorem cast_span_sub (A : Finset ℤ) (d : ℤ) (hd:0≤d) (hL:d≤(span A:ℤ)) :
    ((span A-d.toNat:ℕ):ℝ)=(span A:ℝ)-(d:ℝ) := by
  have hdn : d.toNat≤span A := by omega
  have hdcast : (d.toNat:ℤ)=d := Int.toNat_of_nonneg hd
  have hr : (d.toNat:ℝ)=(d:ℝ) := by exact_mod_cast hdcast
  rw [Nat.cast_sub hdn,hr]

theorem fourth_moment_bound (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (∑d∈Finset.Icc (1:ℤ) (span A:ℤ),(r A d:ℝ)^4/(2*((span A:ℝ)-(d:ℝ))+1))≤
      (M A:ℝ)+12*(T A:ℝ)-2*Dmoment A z-4*Pmoment A z := by
  have he : (∑d∈Finset.Icc (1:ℤ) (span A:ℤ),(r A d:ℝ)^4/(2*((span A:ℝ)-(d:ℝ))+1))=
      ∑d∈Finset.Icc (1:ℤ) (span A:ℤ),(r A d:ℝ)^4/(2*((span A-d.toNat:ℕ):ℝ)+1) := by
    apply Finset.sum_congr rfl
    intro d hd
    obtain ⟨h1,h2⟩ := Finset.mem_Icc.mp hd
    rw [cast_span_sub A d (by omega) h2]
  rw [he,sum_positive_extension]
  · exact fourth_moment_support_bound A z hz
  · intro d hd hn
    rw [r_eq_zero_of_not_mem_posDiffs A d hd hn]
    simp

theorem zero_separated_support_bound (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (∑d∈posDiffs A,2*((r A d).choose 2:ℝ)^2/((span A-d.toNat:ℕ):ℝ))≤
      10*(T A:ℝ)-2*Dmoment A z-4*Pmoment A z := by
  have hp : (∑d∈posDiffs A,2*((r A d).choose 2:ℝ)^2/((span A-d.toNat:ℕ):ℝ))≤
      ∑d∈posDiffs A,((E (positiveFiber A d):ℝ)-(r A d:ℝ)^2) := by
    apply Finset.sum_le_sum
    intro d hd
    by_cases hL : span A-d.toNat=0
    · simp only [hL,Nat.cast_zero,div_zero]
      exact energy_minus_square_nonneg (positiveFiber A d)
    · exact energy_zero_separated_lower (positiveFiber A d) (span A-d.toNat)
        (positiveFiber_span_le A d ((mem_posDiffs A d).mp hd).1) (by omega)
  rw [Finset.sum_sub_distrib] at hp
  have hr2 : (∑d∈posDiffs A,(r A d:ℝ)^2)=(M A:ℝ)+2*(T A:ℝ) := by exact_mod_cast sum_r_sq A
  rw [hr2] at hp
  have he := fiber_energy_sum_upper A z hz
  linarith

theorem zero_separated_moment_bound (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (∑d∈Finset.Ico (1:ℤ) (span A:ℤ),2*((r A d).choose 2:ℝ)^2/((span A:ℝ)-(d:ℝ)))≤
      10*(T A:ℝ)-2*Dmoment A z-4*Pmoment A z := by
  have he : (∑d∈Finset.Ico (1:ℤ) (span A:ℤ),2*((r A d).choose 2:ℝ)^2/((span A:ℝ)-(d:ℝ)))=
      ∑d∈Finset.Ico (1:ℤ) (span A:ℤ),2*((r A d).choose 2:ℝ)^2/((span A-d.toNat:ℕ):ℝ) := by
    apply Finset.sum_congr rfl
    intro d hd
    obtain ⟨h1,h2⟩ := Finset.mem_Ico.mp hd
    rw [cast_span_sub A d (by omega) (by omega)]
  rw [he]
  have hext : (∑d∈Finset.Ico (1:ℤ) (span A:ℤ),2*((r A d).choose 2:ℝ)^2/((span A-d.toNat:ℕ):ℝ))=
      ∑d∈Finset.Icc (1:ℤ) (span A:ℤ),2*((r A d).choose 2:ℝ)^2/((span A-d.toNat:ℕ):ℝ) := by
    apply Finset.sum_subset
    · intro d hd
      obtain ⟨h1,h2⟩ := Finset.mem_Ico.mp hd
      exact Finset.mem_Icc.mpr ⟨h1,le_of_lt h2⟩
    · intro d hd hn
      have hh := Finset.mem_Icc.mp hd
      have heq : d=(span A:ℤ) := by
        by_contra hne
        exact hn (Finset.mem_Ico.mpr ⟨hh.1,by omega⟩)
      have hdcast : d.toNat=span A := by omega
      simp [hdcast]
  rw [hext,sum_positive_extension]
  · exact zero_separated_support_bound A z hz
  · intro d hd hn
    rw [r_eq_zero_of_not_mem_posDiffs A d hd hn]
    simp

end EnergyForcing.Counting
