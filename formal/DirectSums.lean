import SmallFactorCompletion
import DirectComparison

set_option autoImplicit false
namespace EnergyForcing.Counting
open scoped BigOperators

theorem energy_from_multiplicity_cap (A : Finset ℤ) (k : ℕ)
    (hcap:∀d:ℤ,0< d → r A d≤ k) :
    (E A:ℝ)≤((k:ℝ)+1)*(A.card:ℝ)^2-(k:ℝ)*(A.card:ℝ) := by
  have hs : (∑d∈posDiffs A,r A d^2)≤ k*M A := by
    calc
      (∑d∈posDiffs A,r A d^2)≤∑d∈posDiffs A,k*r A d := by
        apply Finset.sum_le_sum
        intro d hd
        have hk:=hcap d ((mem_posDiffs A d).mp hd).1
        nlinarith
      _=k*M A := by rw [← Finset.mul_sum,sum_r]
  have hsR : (∑d∈posDiffs A,(r A d:ℝ)^2)≤(k:ℝ)*(M A:ℝ) := by exact_mod_cast hs
  have he : (E A:ℝ)=(A.card:ℝ)^2+2*∑d∈posDiffs A,(r A d:ℝ)^2 := by
    exact_mod_cast energy_count A
  have hm:=real_M A
  nlinarith

theorem proper_small_energy_profile (A : Finset ℤ) (z : Point→Bool)
    (hz:properOn (strictSource (·∈A)) z) : (E A:ℝ)≤ smallEnergyProfile A.card := by
  unfold smallEnergyProfile
  split_ifs with h6
  · exact_mod_cast (six_mark_proper_bounds A h6 z hz).2
  · have he:=energy_le_interval_energy A
    linarith

theorem direct_sum_energy_bound (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)< Q) (hB:2≤ B.card) (hC:2≤ C.card)
    (z : Point→Bool) (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    2*(E (scaledSum B C Q):ℝ)≤27*((B.card:ℝ)*C.card)^2-25*((B.card:ℝ)*C.card) := by
  obtain ⟨hprod,hpartB,hpartC,hC2,hB2,hC4,hB4⟩:=complete_overlap_restrictions B C Q hQ hB hC z hz
  obtain ⟨zb,hzb⟩:=left_factor_proper B C Q (Finset.card_pos.mp (by omega)) z hz
  obtain ⟨zc,hzc⟩:=right_factor_proper B C Q (by omega) (Finset.card_pos.mp (by omega)) z hz
  have hbSmall:=proper_small_energy_profile B zb hzb
  have hcSmall:=proper_small_energy_profile C zc hzc
  have hbGolomb:=energy_bound_of_twoGolomb B hpartB
  have hcGolomb:=energy_bound_of_twoGolomb C hpartC
  have hbCap:7≤ C.card → (E B:ℝ)≤3*(B.card:ℝ)^2-2*B.card:=by
    intro h
    convert energy_from_multiplicity_cap B 2 (hB2 h) using 1 <;> norm_num
  have hcCap:7≤ B.card → (E C:ℝ)≤3*(C.card:ℝ)^2-2*C.card:=by
    intro h
    convert energy_from_multiplicity_cap C 2 (hC2 h) using 1 <;> norm_num
  have hbCap4:5≤ C.card → (E B:ℝ)≤5*(B.card:ℝ)^2-4*B.card:=by
    intro h
    convert energy_from_multiplicity_cap B 4 (hB4 h) using 1 <;> norm_num
  have hcCap4:5≤ B.card → (E C:ℝ)≤5*(C.card:ℝ)^2-4*C.card:=by
    intro h
    convert energy_from_multiplicity_cap C 4 (hC4 h) using 1 <;> norm_num
  have hbFour:B.card=4 → 7≤ C.card → (E B:ℝ)≤36:=by
    intro hn h
    exact_mod_cast (four_mark_cap_two B hn (hB2 h)).2
  have hcFour:C.card=4 → 7≤ B.card → (E C:ℝ)≤36:=by
    intro hn h
    exact_mod_cast (four_mark_cap_two C hn (hC2 h)).2
  rw [hprod,Nat.cast_mul]
  by_cases hbc:B.card≤ C.card
  · simpa only [mul_assoc] using direct_energy_comparison B.card C.card hB hbc (E B) (E C) (by positivity) (by positivity)
      (fun _=> hbSmall) (fun _=> hcSmall) hcGolomb hbCap hcCap4 hcCap hbFour
  · have hcb:C.card≤ B.card:=by omega
    have hh:=direct_energy_comparison C.card B.card hC hcb (E C) (E B) (by positivity) (by positivity)
      (fun _=> hcSmall) (fun _=> hbSmall) hbGolomb hcCap hbCap4 hbCap hcFour
    nlinarith

/-- All three manuscript direct-sum conclusions, on the actual integer source. -/
theorem direct_sum_bounds (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)< Q) (hB:2≤ B.card) (hC:2≤ C.card)
    (z : Point→Bool) (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    let A:=scaledSum B C Q
    (E A:ℝ)≤(27*(A.card:ℝ)^2-25*(A.card:ℝ))/2 ∧
    (T A:ℝ)≤(23/4:ℝ)*(M A:ℝ) ∧ (M A:ℝ)≤(25/2:ℝ)*(span A:ℝ) := by
  dsimp
  let A:=scaledSum B C Q
  have hn:(A.card:ℝ)=(B.card:ℝ)*C.card:=by exact_mod_cast scaledSum_card B C Q hQ
  have he:=direct_sum_energy_bound B C Q hQ hB hC z hz
  rw [← hn] at he
  have hE:=real_E A
  have hM:=real_M A
  have hT:(T A:ℝ)≤(23/4:ℝ)*(M A:ℝ):=by nlinarith
  refine ⟨by linarith,hT,?_⟩
  have hs:=span_pair_bound A (23/4:ℝ) (by norm_num) hT
  norm_num at hs
  exact hs

end EnergyForcing.Counting
