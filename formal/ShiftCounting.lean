import Mathlib
import SourceCounting
set_option autoImplicit false

namespace EnergyForcing.ShiftCounting

open Finset
open scoped BigOperators Pointwise
open EnergyForcing.Counting

/-- The consecutive shifts used in the manuscript, represented as integers. -/
def shifts (t : ℕ) : Finset ℤ := (Finset.range t).image (fun i : ℕ => (i : ℤ))

@[simp] theorem mem_shifts (t : ℕ) (x : ℤ) :
    x ∈ shifts t ↔ 0 ≤ x ∧ x < (t : ℤ) := by
  simp only [shifts, Finset.mem_image, Finset.mem_range]
  constructor
  · rintro ⟨i, hi, rfl⟩
    omega
  · rintro ⟨hx, ht⟩
    exact ⟨x.toNat, by omega, by omega⟩

@[simp] theorem card_shifts (t : ℕ) : (shifts t).card = t := by
  rw [shifts, Finset.card_image_of_injective _ Nat.cast_injective, Finset.card_range]

/-- Count the mixed additive energy by the difference between its two shifts. -/
theorem mixed_energy_eq_difference_sum (A B : Finset ℤ) :
    Finset.addEnergy A B = ∑ i ∈ B, ∑ j ∈ B, r A (i-j) := by
  classical
  rw [Finset.addEnergy_comm]
  unfold Finset.addEnergy
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter, Finset.product_eq_sprod,
    Finset.sum_product]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  rw [r_eq_card_difference_pairs]
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter, Finset.product_eq_sprod,
    Finset.sum_product]
  apply Finset.sum_congr rfl
  intro a ha
  apply Finset.sum_congr rfl
  intro b hb
  have he : i+a=j+b ↔ b-a=i-j := by omega
  simp only [he]

theorem mixed_energy_shifts (A : Finset ℤ) (t : ℕ) :
    Finset.addEnergy A (shifts t) =
      ∑ i ∈ Finset.range t, ∑ j ∈ Finset.range t, r A ((i:ℤ)-(j:ℤ)) := by
  rw [mixed_energy_eq_difference_sum]
  simp only [shifts]
  rw [Finset.sum_image]
  · apply Finset.sum_congr rfl
    intro i hi
    rw [Finset.sum_image]
    intro a ha b hb hab
    exact Nat.cast_injective hab
  · intro a ha b hb hab
    exact Nat.cast_injective hab

theorem reversed_positive_sum (f : ℕ → ℕ) (t : ℕ) :
    (∑ i ∈ Finset.range t, f (t-i)) = ∑ h ∈ Finset.Ico 1 (t+1), f h := by
  simpa only [Nat.Ico_zero_eq_range, Nat.add_sub_cancel_left, Nat.sub_zero]
    using (Finset.sum_Ico_reflect f 0 (m:=t) (n:=t) (by omega))

theorem weighted_positive_sum_succ (f : ℕ → ℕ) (t : ℕ) (ht : 1 ≤ t) :
    (∑ h ∈ Finset.Ico 1 (t+1), (t+1-h)*f h) =
      (∑ h ∈ Finset.Ico 1 t, (t-h)*f h) +
        ∑ h ∈ Finset.Ico 1 (t+1), f h := by
  rw [Finset.sum_Ico_succ_top ht, Finset.sum_Ico_succ_top ht f]
  have he : (∑ h ∈ Finset.Ico 1 t, (t+1-h)*f h) =
      (∑ h ∈ Finset.Ico 1 t, (t-h)*f h) + ∑ h ∈ Finset.Ico 1 t, f h := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro h hh
    have hh' := (Finset.mem_Ico.mp hh).2
    rw [show t+1-h=(t-h)+1 by omega]
    ring
  rw [he]
  simp only [Nat.add_sub_cancel_left, one_mul]
  omega

/-- The exact triangular weights, with no bound on the set or its differences. -/
theorem interval_energy_profile (A : Finset ℤ) (t : ℕ) (ht : 1 ≤ t) :
    Finset.addEnergy A (shifts t) =
      A.card*t + 2*∑ h ∈ Finset.Ico 1 t, (t-h)*r A (h:ℤ) := by
  rw [mixed_energy_shifts]
  induction t, ht using Nat.le_induction with
  | base => simp [r_zero]
  | succ t ht ih =>
    have hsym : (∑ i ∈ Finset.range t, r A ((i:ℤ)-(t:ℤ))) =
        ∑ i ∈ Finset.range t, r A ((t:ℤ)-(i:ℤ)) := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [show (i:ℤ)-(t:ℤ)=-((t:ℤ)-(i:ℤ)) by ring, r_neg]
    have hpos : (∑ i ∈ Finset.range t, r A ((t:ℤ)-(i:ℤ))) =
        ∑ h ∈ Finset.Ico 1 (t+1), r A (h:ℤ) := by
      calc
        _ = ∑ i ∈ Finset.range t, r A ((t-i:ℕ):ℤ) := by
          apply Finset.sum_congr rfl
          intro i hi
          congr 1
          have hi' := Finset.mem_range.mp hi
          omega
        _ = _ := reversed_positive_sum (fun h => r A (h:ℤ)) t
    simp only [Finset.sum_range_succ]
    rw [Finset.sum_add_distrib, ih, hsym, hpos]
    simp only [sub_self, r_zero]
    rw [weighted_positive_sum_succ _ t ht]
    ring

/-- Translation intervals contain every possible shifted mark. -/
theorem shifted_sumset_card_bound (A : Finset ℤ) (lo : ℤ) (ell t : ℕ)
    (hA : ∀ a ∈ A, lo ≤ a ∧ a ≤ lo+(ell:ℤ)) :
    (A + shifts t).card ≤ ell+t := by
  have hsub : A + shifts t ⊆ Finset.Ico lo (lo+(ell:ℤ)+(t:ℤ)) := by
    intro x hx
    obtain ⟨a, ha, i, hi, rfl⟩ := Finset.mem_add.mp hx
    have ha' := hA a ha
    have hi' := mem_shifts t i |>.mp hi
    simp only [Finset.mem_Ico]
    omega
  have hh := Finset.card_le_card hsub
  simpa only [Int.card_Ico, show lo+(ell:ℤ)+(t:ℤ)-lo=((ell+t:ℕ):ℤ) by push_cast; ring,
    Int.toNat_natCast] using hh

/-- Exact finite-shift inequality for an arbitrary integer set in an interval. -/
theorem finite_shift_profile_interval (A : Finset ℤ) (lo : ℤ) (ell t : ℕ)
    (ht : 1 ≤ t) (hA : ∀ a ∈ A, lo ≤ a ∧ a ≤ lo+(ell:ℤ)) :
    A.card^2*t^2 ≤ (ell+t)*
      (A.card*t + 2*∑ h ∈ Finset.Ico 1 t, (t-h)*r A (h:ℤ)) := by
  have hcs := Finset.le_card_add_mul_addEnergy A (shifts t)
  rw [card_shifts] at hcs
  have hbound := Nat.mul_le_mul_right (Finset.addEnergy A (shifts t))
    (shifted_sumset_card_bound A lo ell t hA)
  exact (hcs.trans hbound).trans_eq (by rw [interval_energy_profile A t ht])

/-- The manuscript's intrinsic span supplies a genuine enclosing interval. -/
theorem interval_of_span_le (A : Finset ℤ) (ell : ℕ) (hs : span A ≤ ell) :
    ∃ lo : ℤ, ∀ a ∈ A, lo ≤ a ∧ a ≤ lo+(ell:ℤ) := by
  by_cases hne : A.Nonempty
  · refine ⟨A.min' hne, ?_⟩
    intro a ha
    have hlo := A.min'_le a ha
    have hhi := A.le_max' a ha
    simp only [span, dif_pos hne] at hs
    exact ⟨hlo, by omega⟩
  · refine ⟨0, ?_⟩
    intro a ha
    exact (hne ⟨a,ha⟩).elim

/-- Equation (shift-profile), for every finite integer set of bounded span. -/
theorem finite_shift_profile (A : Finset ℤ) (ell t : ℕ)
    (hs : span A ≤ ell) (ht : 1 ≤ t) :
    A.card^2*t^2 ≤ (ell+t)*
      (A.card*t + 2*∑ h ∈ Finset.Ico 1 t, (t-h)*r A (h:ℤ)) := by
  obtain ⟨lo,hA⟩ := interval_of_span_le A ell hs
  exact finite_shift_profile_interval A lo ell t ht hA

theorem twice_weight_sum (t : ℕ) (ht : 1 ≤ t) :
    2*(∑ h ∈ Finset.Ico 1 t, (t-h))=t*(t-1) := by
  induction t, ht using Nat.le_induction with
  | base => simp
  | succ t ht ih =>
    have hstep := weighted_positive_sum_succ (fun _ => 1) t ht
    simp only [mul_one, Finset.sum_const, Nat.card_Ico, smul_eq_mul, mul_one,
      Nat.add_sub_cancel] at hstep
    rw [hstep]
    have he : t-1+1=t := Nat.sub_add_cancel ht
    simp only [Nat.add_sub_cancel]
    nlinarith

/-- Equation (shift-count), including arbitrary real nonnegative multiplicity caps. -/
theorem finite_shift_count (A : Finset ℤ) (ell t : ℕ) (W : ℝ)
    (hs : span A ≤ ell) (ht : 1 ≤ t) (hW : 0 ≤ W)
    (hcap : ∀ h : ℤ, 0<h → (r A h : ℝ) ≤ W) :
    (A.card:ℝ)^2*t ≤ (ell+t)*((A.card:ℝ)+W*(t-1)) := by
  have hp := finite_shift_profile A ell t hs ht
  have hp' : (A.card:ℝ)^2*(t:ℝ)^2 ≤ ((ell:ℝ)+t)*
      ((A.card:ℝ)*t+2*∑ h ∈ Finset.Ico 1 t, ((t-h:ℕ):ℝ)*(r A (h:ℤ):ℝ)) := by
    exact_mod_cast hp
  have hb : (∑ h ∈ Finset.Ico 1 t, ((t-h:ℕ):ℝ)*(r A (h:ℤ):ℝ)) ≤
      (∑ h ∈ Finset.Ico 1 t, ((t-h:ℕ):ℝ))*W := by
    rw [Finset.sum_mul]
    apply Finset.sum_le_sum
    intro h hh
    apply mul_le_mul_of_nonneg_left (hcap h (by
      have := (Finset.mem_Ico.mp hh).1
      omega)) (by positivity)
  have hw : 2*(∑ h ∈ Finset.Ico 1 t, ((t-h:ℕ):ℝ))=(t:ℝ)*(t-1) := by
    have hn := twice_weight_sum t ht
    have hn' : 2*(∑ h ∈ Finset.Ico 1 t, ((t-h:ℕ):ℝ))=(t:ℝ)*((t-1:ℕ):ℝ) := by
      exact_mod_cast hn
    rw [hn', Nat.cast_sub ht]
    norm_num
  have ht' : (0:ℝ)<t := by exact_mod_cast (by omega : 0<t)
  have hf : (A.card:ℝ)^2*(t:ℝ)^2 ≤ ((ell:ℝ)+t)*
      ((A.card:ℝ)*t+W*((t:ℝ)*(t-1))) := by
    apply hp'.trans
    apply mul_le_mul_of_nonneg_left _ (by positivity)
    nlinarith [hb, hw]
  apply (mul_le_mul_right ht').mp
  nlinarith [hf]

end EnergyForcing.ShiftCounting
