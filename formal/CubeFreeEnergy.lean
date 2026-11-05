import CubeAlteration
import EnergyMomentLower
import G9Consequences

set_option autoImplicit false

namespace EnergyForcing.CubeAlteration

open EnergyForcing.Counting
open Filter

theorem coefficient_margin : (1 : ℝ) < 32/31-(32/31 : ℝ)^32/720 := by norm_num

/-- A subsequence of the paper's random constructions avoids fractional powers
in the selection probability: N=s^31 and p=(32/31)/s^5. -/
theorem large_cube_free_set (s : ℕ) (hs : 2 ≤ s) :
    ∃A⊆interval (s^31), CubeFree A ∧ (s : ℝ)^26 ≤ (A.card : ℝ) := by
  have hsR : (2 : ℝ) ≤ s := by exact_mod_cast hs
  have hspos : (0 : ℝ) < s := by linarith
  let p : ℝ := (32/31)/(s : ℝ)^5
  have hp : 0 ≤ p := by dsimp [p]; positivity
  have hp1 : p ≤ 1 := by
    have hpow := pow_le_pow_left₀ (by norm_num : (0 : ℝ) ≤ 2) hsR 5
    norm_num at hpow
    dsimp [p]
    apply (div_le_one (by positivity)).mpr
    linarith
  obtain ⟨A,hA,hfree,hcard⟩ := cube_free_alteration (s^31) p hp hp1
  have he : ((s^31 : ℕ) : ℝ)*p - ((s^31 : ℕ) : ℝ)^6*p^32/720 =
      (32/31-(32/31 : ℝ)^32/720)*(s : ℝ)^26 := by
    push_cast
    dsimp [p]
    field_simp
    ring
  rw [he] at hcard
  refine ⟨A,hA,hfree,?_⟩
  have hm := mul_le_mul_of_nonneg_right coefficient_margin.le (pow_nonneg hspos.le 26)
  linarith

theorem interval_energy_bound (N : ℕ) (hN : 1 ≤ N) (A : Finset ℤ)
    (hA : A ⊆ interval N) : (A.card : ℝ)^4/(2*(N : ℝ)) ≤ (E A : ℝ) := by
  have hs : span A ≤ N-1 := EnergyForcing.G9Formal.span_le_of_interval A 1 (N-1) (by
    intro a ha
    have hh := Finset.mem_Icc.mp (hA ha)
    exact ⟨hh.1,by omega⟩)
  have he := energy_fourth_lower A (N-1) hs
  have hNr : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hden : 2*((N-1 : ℕ) : ℝ)+1=2*(N : ℝ)-1 := by
    rw [Nat.cast_sub hN]; norm_num; ring
  rw [hden] at he
  exact (div_le_div_of_nonneg_left (by positivity) (by linarith) (by linarith)).trans he

theorem energy_exponent_bound (s : ℕ) (hs : 2 ≤ s) (A : Finset ℤ)
    (hA : A ⊆ interval (s^31)) (hcard : (s : ℝ)^26 ≤ (A.card : ℝ)) :
    (1/2 : ℝ)*(A.card : ℝ)^(73/26 : ℝ) ≤ (E A : ℝ) := by
  have hsR : (2 : ℝ) ≤ s := by exact_mod_cast hs
  have hspos : (0 : ℝ) < s := by linarith
  have hn : (0 : ℝ) < A.card := lt_of_lt_of_le (by positivity) hcard
  have hN : (s : ℝ)^31 ≤ (A.card : ℝ)^(31/26 : ℝ) := by
    have hh := Real.rpow_le_rpow (pow_nonneg hspos.le 26) hcard (by norm_num : (0 : ℝ) ≤ 31/26)
    have he : ((s : ℝ)^26)^(31/26 : ℝ)=(s : ℝ)^31 := by
      rw [← Real.rpow_natCast_mul hspos.le]
      norm_num
      exact Real.rpow_natCast _ 31
    rwa [he] at hh
  have he := interval_energy_bound (s^31) (Nat.succ_le_of_lt (pow_pos (by omega) _)) A hA
  push_cast at he
  have hprod : (A.card : ℝ)^(73/26 : ℝ)*(A.card : ℝ)^(31/26 : ℝ)=(A.card : ℝ)^4 := by
    rw [← Real.rpow_add hn]
    norm_num
    exact Real.rpow_natCast _ 4
  have hid : (1/2 : ℝ)*(A.card : ℝ)^(73/26 : ℝ)=
      (A.card : ℝ)^4/(2*(A.card : ℝ)^(31/26 : ℝ)) := by
    rw [← hprod]
    field_simp
    ring
  rw [hid]
  apply le_trans _ he
  exact div_le_div_of_nonneg_left (by positivity) (by positivity) (by linarith)

/-- The complete existence and energy assertion of prop:cube-free-energy. -/
theorem cube_free_high_energy_sequence :
    ∃A : ℕ → Finset ℤ,
      Tendsto (fun j => (A j).card) atTop atTop ∧
      ∀j, CubeFree (A j) ∧ (1/2 : ℝ)*((A j).card : ℝ)^(73/26 : ℝ) ≤ (E (A j) : ℝ) := by
  choose A hA hfree hcard using fun j : ℕ => large_cube_free_set (j+2) (by omega)
  refine ⟨A,?_,?_⟩
  · apply tendsto_atTop_mono (f:=fun j : ℕ => j)
    · intro j
      have hh := hcard j
      have hp : (j+2 : ℕ) ≤ (j+2)^26 := Nat.le_pow (by omega)
      have hh' : (j+2)^26 ≤ (A j).card := by exact_mod_cast hh
      omega
    · exact tendsto_id
  · intro j
    exact ⟨hfree j,energy_exponent_bound (j+2) (by omega) (A j) (hA j) (hcard j)⟩

/-- Cube exclusion admits no uniform quadratic energy or linear corner bound,
even after excluding all sets below any prescribed cardinality. -/
theorem cube_exclusion_no_uniform_bound (K : ℝ) (hK : 0 ≤ K) (m : ℕ) :
    ∃A : Finset ℤ, m ≤ A.card ∧ CubeFree A ∧
      K*(A.card : ℝ)^2 < (E A : ℝ) ∧ K*(M A : ℝ) < (T A : ℝ) := by
  obtain ⟨A,hlim,hA⟩ := cube_free_high_energy_sequence
  have hr : Tendsto (fun j => ((A j).card : ℝ)) atTop atTop :=
    tendsto_natCast_atTop_atTop.comp hlim
  have hp : Tendsto (fun j => ((A j).card : ℝ)^(21/26 : ℝ)) atTop atTop :=
    (tendsto_rpow_atTop (by norm_num : (0 : ℝ) < 21/26)).comp hr
  obtain ⟨j,hj,hm⟩ := ((hp.eventually (eventually_gt_atTop (4*K+4))).and
    (hlim.eventually (eventually_ge_atTop m))).exists
  have hn : (0 : ℝ) < (A j).card := by
    by_contra h
    have hz : ((A j).card : ℝ)=0 := le_antisymm (by linarith) (by positivity)
    rw [hz,Real.zero_rpow (by norm_num : (21/26 : ℝ) ≠ 0)] at hj
    linarith
  have hsq : 0 < ((A j).card : ℝ)^2 := sq_pos_of_pos hn
  have hfactor : ((A j).card : ℝ)^(73/26 : ℝ) =
      ((A j).card : ℝ)^2 * ((A j).card : ℝ)^(21/26 : ℝ) := by
    rw [← Real.rpow_natCast _ 2, ← Real.rpow_add hn]
    congr 1
    norm_num
  have he := (hA j).2
  rw [hfactor] at he
  have hbig := mul_lt_mul_of_pos_left hj hsq
  have hstrong : (2*K+2)*((A j).card : ℝ)^2 < (E (A j) : ℝ) := by nlinarith
  have hcountN : E (A j)=(A j).card^2+2*(M (A j)+2*T (A j)) := by
    rw [energy_count,sum_r_sq]
  have hcount : (E (A j) : ℝ)=((A j).card : ℝ)^2+2*((M (A j) : ℝ)+2*(T (A j) : ℝ)) :=
    by exact_mod_cast hcountN
  have hpair : ((A j).card : ℝ)^2=((A j).card : ℝ)+2*(M (A j) : ℝ) :=
    by exact_mod_cast square_eq_self_add_twice_choose (A j).card
  have hKM := mul_le_mul_of_nonneg_left (show 2*(M (A j) : ℝ) ≤ ((A j).card : ℝ)^2 by linarith) hK
  refine ⟨A j,hm,(hA j).1,?_,?_⟩ <;> nlinarith

end EnergyForcing.CubeAlteration
