import Mathlib
import ShiftCounting
import UniversalCounting
set_option autoImplicit false

namespace EnergyForcing.S21Four

open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.ShiftCounting

def eraseFourth (c₀ c : Fin 4) : Fin 3 :=
  ⟨(if c.val<c₀.val then c.val else c.val-1)%3, Nat.mod_lt _ (by decide)⟩

theorem eraseFourth_injective : ∀ c₀ a b : Fin 4, a≠c₀ → b≠c₀ →
    eraseFourth c₀ a=eraseFourth c₀ b → a=b := by decide

theorem proper_after_remove_fourth (D : Point → Prop) (c : Point → Fin 4)
    (c₀ : Fin 4) (hp : properOn D c) (ha : ∀ p, D p → c p≠c₀) :
    properOn D (fun p => eraseFourth c₀ (c p)) := by
  intro x y d hd h₁ h₂ h₃ he
  apply hp x y d hd h₁ h₂ h₃
  exact ⟨eraseFourth_injective c₀ _ _ (ha _ h₁) (ha _ h₂) he.1,
    eraseFourth_injective c₀ _ _ (ha _ h₂) (ha _ h₃) he.2⟩

theorem finset_span_estimate (q Lmax : ℕ) (hs : ActualSpanEstimateOn q Lmax)
    (A : Finset ℤ) (lo : ℤ) (ell : ℕ) (he : ell≤Lmax)
    (hA : ∀a∈A, lo≤a ∧ a≤lo+(ell:ℤ))
    (hp : ∃c : Point → Bool, properOn (strictSource (fun a => a∈A)) c) :
    A.card*(A.card-1)≤2*q*ell := by
  have hh := ((span_estimate_iff_interval q Lmax).mp hs) A.toList lo ell
    A.nodup_toList he (by simpa only [Finset.mem_toList] using hA)
    (by simpa only [Finset.mem_toList] using hp)
  simpa only [Finset.length_toList] using hh

def fiberColorPart (A : Finset ℤ) (c : Point → Fin 3) (h : ℤ) (i : Fin 3) : Finset ℤ :=
  (positiveFiber A h).filter fun u => c (u+h,u)=i

theorem fiberColorPart_binary (A : Finset ℤ) (c : Point → Fin 3) (h : ℤ)
    (hh : 0<h) (hc : properOn (strictSource (fun a => a∈A)) c) (i : Fin 3) :
    ∃ b : Point → Bool, properOn (strictSource (fun a => a∈fiberColorPart A c h i)) b := by
  let F : ℤ → Prop := fun u => u∈A ∧ u+h∈A
  let z : Point → Fin 3 := fun p => c (p.1+h,p.2)
  have hf : properOn (weakSource F) z := fiber_restriction (fun a => a∈A) c hc h hh
  have hpart : ∀u∈fiberColorPart A c h i, F u ∧ z (u,u)=i := by
    intro u hu
    simpa [fiberColorPart,F,z] using hu
  have hp : properOn (strictSource (fun a => a∈fiberColorPart A c h i)) z := by
    apply properOn_mono _ (weakSource F) z _ hf
    intro p hp
    exact ⟨(hpart _ hp.1).1,(hpart _ hp.2.1).1,le_of_lt hp.2.2⟩
  have ha : ∀p, strictSource (fun a => a∈fiberColorPart A c h i) p → z p≠i := by
    intro p hp
    have h₁ := hpart _ hp.1
    have h₂ := hpart _ hp.2.1
    have he := diagonal_exclusion F z hf p.2 p.1 h₂.1 h₁.1 hp.2.2
      (h₂.2.trans h₁.2.symm)
    simpa only [h₂.2] using he
  exact ⟨_,proper_after_remove_color _ z i hp ha⟩

theorem fiberColorPart_span (A : Finset ℤ) (c : Point → Fin 3)
    (lo : ℤ) (ell h : ℕ) (hh : h≤ell)
    (hA : ∀a∈A, lo≤a ∧ a≤lo+(ell:ℤ)) (i : Fin 3) :
    ∀u∈fiberColorPart A c h i, lo≤u ∧ u≤lo+((ell-h:ℕ):ℤ) := by
  intro u hu
  have hf := (Finset.mem_filter.mp hu).1
  rcases (mem_positiveFiber A h u).mp hf with ⟨hu,hu'⟩
  have hl := hA u hu
  have hr := hA (u+h) hu'
  constructor
  · exact hl.1
  · omega

theorem integer_tangent (s : ℕ) : 4070*s≤s*(s-1)+2035*2036 := by
  by_cases hz : s=0
  · simp [hz]
  have hs : 1≤s := by omega
  have ht : (0:ℤ)≤((s:ℤ)-2035)*((s:ℤ)-2036) := by
    by_cases hl : s≤2035
    · exact mul_nonneg_of_nonpos_of_nonpos (by omega) (by omega)
    · exact mul_nonneg (by omega) (by omega)
  zify [hs]
  nlinarith [ht]

theorem fiberColorPart_total (A : Finset ℤ) (c : Point → Fin 3) (h : ℤ) :
    ∑i : Fin 3, (fiberColorPart A c h i).card = r A h := by
  simp only [fiberColorPart, Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  simp [r]

/-- The complete S21-derived offset profile, including its three color classes. -/
theorem S21_fiber_profile (Lmax : ℕ) (hs : ActualSpanEstimateOn 21 Lmax)
    (A : Finset ℤ) (c : Point → Fin 3) (lo : ℤ) (ell h : ℕ)
    (hpos : 1≤h) (hhe : h≤ell) (hmax : ell-h≤Lmax)
    (hA : ∀a∈A, lo≤a ∧ a≤lo+(ell:ℤ))
    (hc : properOn (strictSource (fun a => a∈A)) c) :
    4070*r A h ≤ 126*(ell-h)+12429780 := by
  have hb : ∀i : Fin 3, 4070*(fiberColorPart A c h i).card ≤
      42*(ell-h)+2035*2036 := by
    intro i
    have hh := finset_span_estimate 21 Lmax hs (fiberColorPart A c h i) lo (ell-h)
      hmax (fiberColorPart_span A c lo ell h hhe hA i)
      (fiberColorPart_binary A c h (by omega) hc i)
    have ht := integer_tangent (fiberColorPart A c h i).card
    omega
  have he := fiberColorPart_total A c h
  rw [Fin.sum_univ_three] at he
  have h₀ := hb 0
  have h₁ := hb 1
  have h₂ := hb 2
  omega

theorem six_weighted_index_sum (n : ℕ) :
    6*(∑h ∈ Finset.Ico 1 (n+1), (n+1-h)*h)=(n+1)*n*(n+2) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hstep := weighted_positive_sum_succ (fun h => h) (n+1) (by omega)
    have hs := Finset.sum_range_id_mul_two (n+2)
    rw [Finset.sum_range_eq_add_Ico (fun h : ℕ => h) (by omega)] at hs
    simp only [zero_add,Nat.add_sub_cancel] at hs
    rw [hstep]
    rw [show n+2-1=n+1 by omega] at hs
    simp only [show n+1+1=n+2 by omega,show n+1+2=n+3 by omega]
    nlinarith

/-- Exact evaluation of the two polynomial weight sums used at t=600. -/
theorem weighted_profile_eval :
    2*(∑h ∈ Finset.Ico 1 600, (600-h)*(126*(98776-h)+12429780))=
      600*599*24850314 := by
  have hw := twice_weight_sum 600 (by decide)
  have hi := six_weighted_index_sum 599
  have he : (∑h ∈ Finset.Ico 1 600, (600-h)*(126*(98776-h)+12429780))+
      126*(∑h ∈ Finset.Ico 1 600, (600-h)*h)=
      (126*98776+12429780)*(∑h ∈ Finset.Ico 1 600, (600-h)) := by
    simp only [Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro h hh
    have hbound := (Finset.mem_Ico.mp hh).2
    have hc : 98776-h+h=98776 := by omega
    nlinarith
  norm_num only at hw hi
  omega

theorem profile_excludes_large_source (hs : ActualSpanEstimateOn 21 98775)
    (A : Finset ℤ) (lo : ℤ)
    (hcard : A.card=24695) (hA : ∀a∈A, lo≤a ∧ a≤lo+98776)
    (c : Point → Fin 3) (hc : properOn (strictSource (fun a => a∈A)) c) : False := by
  have hp := finite_shift_profile_interval A lo 98776 600 (by decide) (by simpa using hA)
  rw [hcard] at hp
  have hbound : 4070*(∑h ∈ Finset.Ico 1 (600:ℕ), (600-h)*r A (h:ℤ)) ≤
      ∑h ∈ Finset.Ico 1 600, (600-h)*(126*(98776-h)+12429780) := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro h hh
    have hh' := Finset.mem_Ico.mp hh
    have hprof := S21_fiber_profile 98775 hs A c lo 98776 h hh'.1 (by omega)
      (by omega) (by simpa using hA) hc
    have hmul := Nat.mul_le_mul_left (600-h) hprof
    nlinarith [hmul]
  have heval := weighted_profile_eval
  nlinarith [hp,hbound,heval]

/-- A proper four-color square would contain the source excluded by the full profile. -/
theorem S21_four (hs : ActualSpanEstimateOn 21 98775) : ramseyL 4 98777 := by
  intro c hc
  let diag := diagonalList 98777
  let color := fun a : ℤ => (c (a,a)).val
  obtain ⟨i,hi,hlarge⟩ := largest_color_class 4 (by decide) (diag.map color) (by
    intro a ha
    obtain ⟨x,_,rfl⟩ := List.mem_map.mp ha
    exact (c (x,x)).isLt)
  let marks := diag.filter fun a => color a==i
  have hn : 98777≤4*marks.length := by
    rw [List.count_eq_countP,List.countP_map,List.countP_eq_length_filter] at hlarge
    simpa only [List.length_map,diag,diagonalList,List.length_range,
      Function.comp_def,marks,color] using hlarge
  have hnodup : marks.Nodup := List.Pairwise.filter _ (diagonalList_nodup 98777)
  have hsize : 24695 ≤ marks.toFinset.card := by
    rw [List.toFinset_card_of_nodup hnodup]
    omega
  obtain ⟨A,hsub,hcard⟩ := Finset.exists_subset_card_eq hsize
  have hA : ∀a∈A, 1≤a ∧ a≤(98777:ℤ) := by
    intro a ha
    have hm : a∈marks := List.mem_toFinset.mp (hsub ha)
    exact (diagonalList_mem 98777 a).mp (List.mem_filter.mp hm).1
  let c₀ : Fin 4 := ⟨i,hi⟩
  have hdiag : ∀a∈A, c (a,a)=c₀ := by
    intro a ha
    have hm : a∈marks := List.mem_toFinset.mp (hsub ha)
    apply Fin.ext
    exact of_decide_eq_true (List.mem_filter.mp hm).2
  have hr := square_diagonal_restriction 98777 (fun a => a∈A) c c₀ hA hc hdiag
  have hproper := proper_after_remove_fourth _ c c₀ hr.1 hr.2
  exact profile_excludes_large_source hs A 1 hcard (by simpa using hA) _ hproper

theorem S21_four_full (hs : ActualSpanEstimateOn 21 99994) : ramseyL 4 98777 := by
  apply S21_four
  apply (span_estimate_iff_interval 21 98775).mpr
  exact spanEstimate_restrict 21 98775 99994 (by decide)
    ((span_estimate_iff_interval 21 99994).mp hs)

end EnergyForcing.S21Four
