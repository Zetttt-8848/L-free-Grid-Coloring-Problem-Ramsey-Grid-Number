import Mathlib
import UniversalCounting

set_option autoImplicit false

namespace EnergyForcing.GeneralBound

open EnergyForcing

/-- Canonical integer representatives of a corner-free subset of (Z/mZ)^2.
The step is nonzero modulo m, exactly as in the external theorem. -/
def CyclicCornerFree (m : ℕ) (S : Finset Point) : Prop :=
  (∀ p ∈ S, 0 ≤ p.1 ∧ p.1 < m ∧ 0 ≤ p.2 ∧ p.2 < m) ∧
  ∀ a b d : ℤ, d % (m : ℤ) ≠ 0 →
    ¬ ((a,b) ∈ S ∧ ((a+d) % m,b) ∈ S ∧ (a,(b+d) % m) ∈ S)

/-- The cyclic-group specialization of JLLOS25 v2, Theorem 1.1.
This is an explicit hypothesis, not an axiom or a theorem proved here. -/
def ExternalCyclicCornersBound (c : ℝ) : Prop :=
  ∀ (m : ℕ) (S : Finset Point), 2 ≤ m → CyclicCornerFree m S →
    (S.card : ℝ) ≤ (m : ℝ)^2 * Real.exp (-c * (Real.log m)^(1/600 : ℝ))

noncomputable def bound (c : ℝ) (k : ℕ) : ℕ :=
  ⌈Real.exp ((Real.log (8*(k : ℝ)^2)/c)^600)⌉₊

theorem signed_to_cyclic (N : ℕ) (hN : 1 ≤ N) (S : Finset Point)
    (hs : ∀ p ∈ S, square (N : ℤ) p)
    (hc : noSignedCorners (fun p => p ∈ S)) : CyclicCornerFree (2*N) S := by
  constructor
  · intro p hp
    have h := hs p hp
    simp only [square] at h
    push_cast
    omega
  · intro a b d hd h
    have hn : (1 : ℤ) ≤ N := by exact_mod_cast hN
    have he := cyclic_embedding_no_corner (N : ℤ) hn (fun p => p ∈ S) hs hc
      a b d (by simpa using hd)
    apply he
    simpa only [image_eq_source (N : ℤ) hn (fun p => p ∈ S) hs,
      Nat.cast_mul, Nat.cast_ofNat] using h

theorem paired_density_bound (c : ℝ) (hext : ExternalCyclicCornersBound c)
    (N k : ℕ) (hN : 1 ≤ N) (hk : 0 < k)
    (z : Point → Fin k) (hz : properL (N : ℤ) z) :
    (N : ℝ)^2 ≤ (k : ℝ)^2 * ((2*(N : ℝ))^2 *
      Real.exp (-c * (Real.log (2*(N : ℝ)))^(1/600 : ℝ))) := by
  let f := fun p => z (H (N : ℤ) p)
  have hf : properCorner (N : ℤ) f := (reflection_proper (N : ℤ) z).mp hz
  obtain ⟨i,hi,hnd,hl,hcorner⟩ := (paired_color_class_complete N k hk f hf).2
  let L := (squareList N).filter fun p => pairedCode (N : ℤ) k f p == i
  let S := L.toFinset
  have hcard : S.card = L.length := List.toFinset_card_of_nodup hnd
  have hs : ∀ p ∈ S, square (N : ℤ) p := by
    intro p hp
    exact (mem_squareList N p).mp (List.mem_filter.mp (List.mem_toFinset.mp hp)).1
  have hcyc := signed_to_cyclic N hN S hs (by simpa [S, L] using hcorner)
  have he := hext (2*N) S (by omega) hcyc
  have hlr : (N : ℝ)^2 ≤ (k : ℝ)^2 * (S.card : ℝ) := by
    rw [hcard]
    have hl' : N^2 ≤ k^2 * L.length := by simpa only [pow_two, L] using hl
    exact_mod_cast hl'
  calc
    (N : ℝ)^2 ≤ (k : ℝ)^2 * (S.card : ℝ) := hlr
    _ ≤ _ := by simpa only [Nat.cast_mul, Nat.cast_ofNat] using
      mul_le_mul_of_nonneg_left he (sq_nonneg (k : ℝ))

theorem bound_positive (c : ℝ) (k : ℕ) : 1 ≤ bound c k := by
  have he := Real.exp_pos ((Real.log (8*(k : ℝ)^2)/c)^600)
  have hn := Nat.le_ceil (Real.exp ((Real.log (8*(k : ℝ)^2)/c)^600))
  have hb : (0 : ℝ) < bound c k := lt_of_lt_of_le he hn
  exact_mod_cast hb

theorem decay_at_bound (c : ℝ) (hc : 0 < c) (k : ℕ) (hk : 1 ≤ k) :
    Real.exp (-c * (Real.log (2*(bound c k : ℝ)))^(1/600 : ℝ)) ≤
      1/(8*(k : ℝ)^2) := by
  have hkr : (1 : ℝ) ≤ k := by exact_mod_cast hk
  have harg : 1 ≤ 8*(k : ℝ)^2 := by nlinarith
  have hlog : 0 ≤ Real.log (8*(k : ℝ)^2) := Real.log_nonneg harg
  let x := Real.log (8*(k : ℝ)^2)/c
  have hx : 0 ≤ x := div_nonneg hlog hc.le
  have hN : (1 : ℝ) ≤ bound c k := by exact_mod_cast bound_positive c k
  have he : Real.exp (x^600) ≤ 2*(bound c k : ℝ) := by
    have hceil := Nat.le_ceil (Real.exp (x^600))
    change Real.exp (x^600) ≤ (bound c k : ℝ) at hceil
    linarith
  have hpow : x^600 ≤ Real.log (2*(bound c k : ℝ)) :=
    (Real.le_log_iff_exp_le (by positivity)).mpr he
  have hroot : x ≤ (Real.log (2*(bound c k : ℝ)))^(1/600 : ℝ) := by
    have hr := Real.rpow_le_rpow (pow_nonneg hx 600) hpow (by norm_num : (0 : ℝ) ≤ 1/600)
    have hid : (x^600)^(1/600 : ℝ) = x := by
      rw [← Real.rpow_natCast_mul hx]
      norm_num
    rwa [hid] at hr
  have hprod : Real.log (8*(k : ℝ)^2) ≤
      c*(Real.log (2*(bound c k : ℝ)))^(1/600 : ℝ) := by
    have hh := mul_le_mul_of_nonneg_left hroot hc.le
    dsimp [x] at hh
    field_simp at hh
    nlinarith
  calc
    Real.exp (-c*(Real.log (2*(bound c k : ℝ)))^(1/600 : ℝ))
      ≤ Real.exp (-Real.log (8*(k : ℝ)^2)) := Real.exp_le_exp.mpr (by linarith)
    _ = 1/(8*(k : ℝ)^2) := by rw [Real.exp_neg, Real.exp_log (by positivity), one_div]

theorem general_ramsey_bound (c : ℝ) (hc : 0 < c)
    (hext : ExternalCyclicCornersBound c) (k : ℕ) (hk : 1 ≤ k) :
    ramseyL k (bound c k) := by
  intro z hz
  have hN := bound_positive c k
  have hd := paired_density_bound c hext (bound c k) k hN (by omega) z hz
  have he := decay_at_bound c hc k hk
  have hkr : (1 : ℝ) ≤ k := by exact_mod_cast hk
  have hNr : (1 : ℝ) ≤ bound c k := by exact_mod_cast hN
  have hmul := mul_le_mul_of_nonneg_left he
    (show 0 ≤ (k : ℝ)^2 * (2*(bound c k : ℝ))^2 by positivity)
  have hhalf : (k : ℝ)^2 * (2*(bound c k : ℝ))^2 * (1/(8*(k : ℝ)^2)) =
      (bound c k : ℝ)^2/2 := by field_simp; ring
  rw [hhalf] at hmul
  nlinarith

theorem quasipolynomial_ceiling_bound (c : ℝ) (hc : 0 < c)
    (k : ℕ) (hk : 1 ≤ k) :
    bound c k ≤ ⌈Real.exp ((3/c)^600 * (Real.log (2*(k : ℝ)))^600)⌉₊ := by
  have hkr : (1 : ℝ) ≤ k := by exact_mod_cast hk
  have ha : 0 < 8*(k : ℝ)^2 := by positivity
  have hl : Real.log (8*(k : ℝ)^2) ≤ 3*Real.log (2*(k : ℝ)) := by
    have hh : 8*(k : ℝ)^2 ≤ (2*(k : ℝ))^3 := by nlinarith [sq_nonneg ((k : ℝ)-1)]
    have hh' := Real.log_le_log ha hh
    simpa only [Real.log_pow, Nat.cast_ofNat] using hh'
  have hb : 0 ≤ Real.log (8*(k : ℝ)^2)/c := by
    apply div_nonneg _ hc.le
    exact Real.log_nonneg (by nlinarith)
  have hp := pow_le_pow_left₀ hb (div_le_div_of_nonneg_right hl hc.le) 600
  apply Nat.ceil_mono
  apply Real.exp_le_exp.mpr
  dsimp [bound]
  calc
    (Real.log (8*(k : ℝ)^2)/c)^600 ≤ (3*Real.log (2*(k : ℝ))/c)^600 := hp
    _ = (3/c)^600 * (Real.log (2*(k : ℝ)))^600 := by rw [← mul_pow]; congr 1; ring

end EnergyForcing.GeneralBound
