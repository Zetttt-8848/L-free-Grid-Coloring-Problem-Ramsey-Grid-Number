import ForcingCounting

namespace EnergyForcing.G9Formal

open EnergyForcing.Counting
open EnergyForcing.Forcing

def G9 : Prop := ∀ (A : Finset ℤ) (z : Point → Bool),
  properOn (strictSource fun a => a∈A) z → (edges A z).card≤9*M A

def G9ExistsOn (Lmax : ℕ) : Prop := ∀ A : Finset ℤ, span A≤Lmax →
  (∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) →
  ∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z ∧ (edges A z).card≤9*M A

def G9Exists : Prop := ∀ A : Finset ℤ,
  (∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) →
  ∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z ∧ (edges A z).card≤9*M A

theorem bounds_of_edge_bound (A : Finset ℤ) (z : Point → Bool)
    (he : (edges A z).card≤9*M A) : 2*T A≤19*M A ∧ M A≤20*span A := by
  have hi := forcing_identity A z
  have hn := imbalanceSq_nonneg A z
  have he' : ((edges A z).card:ℤ)≤9*(M A:ℤ) := by exact_mod_cast he
  have ht : 2*(T A:ℤ)≤19*(M A:ℤ) := by omega
  have htN : 2*T A≤19*M A := by exact_mod_cast ht
  have htR : (T A:ℝ)≤(19/2:ℝ)*(M A:ℝ) := by
    have hh : 2*(T A:ℝ)≤19*(M A:ℝ) := by exact_mod_cast htN
    linarith
  have hs := span_pair_bound A (19/2) (by norm_num) htR
  norm_num at hs
  exact ⟨htN,by exact_mod_cast hs⟩

/-- The universal and finite-range G9 reductions use the actual physical edge set. -/
theorem g9_consequences (hg : G9) (A : Finset ℤ)
    (hz : ∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) :
    2*T A≤19*M A ∧ M A≤20*span A := by
  obtain ⟨z,hz⟩ := hz
  exact bounds_of_edge_bound A z (hg A z hz)

theorem g9_exists_consequences (hg : G9Exists) (A : Finset ℤ)
    (hz : ∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) :
    2*T A≤19*M A ∧ M A≤20*span A := by
  obtain ⟨z,_,he⟩ := hg A hz
  exact bounds_of_edge_bound A z he

theorem g9_exists_on_consequences (Lmax : ℕ) (hg : G9ExistsOn Lmax) (A : Finset ℤ)
    (hspan : span A≤Lmax)
    (hz : ∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) :
    2*T A≤19*M A ∧ M A≤20*span A := by
  obtain ⟨z,_,he⟩ := hg A hspan hz
  exact bounds_of_edge_bound A z he

theorem g9_implies_exists_on (hg : G9) (Lmax : ℕ) : G9ExistsOn Lmax := by
  intro A hA hz
  obtain ⟨z,hz⟩ := hz
  exact ⟨z,hz,hg A z hz⟩

theorem span_le_of_interval (A : Finset ℤ) (lo : ℤ) (ell : ℕ)
    (hA : ∀ a∈A, lo≤a ∧ a≤lo+(ell:ℤ)) : span A≤ell := by
  by_cases h : A.Nonempty
  · have hmin := hA (A.min' h) (A.min'_mem h)
    have hmax := hA (A.max' h) (A.max'_mem h)
    simp only [span,dif_pos h]
    omega
  · simp [span,h]

/-- The Finset span estimate is translated to the prior exact list formulation.
    Duplicate-free lists preserve cardinality; containing intervals only enlarge span. -/
theorem finset_span_bridge (q Lmax : ℕ)
    (hs : ∀ A : Finset ℤ, span A≤Lmax →
      (∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) → M A≤q*span A) :
    SpanEstimateOn q Lmax := by
  intro A lo ell hnodup hell hA hz
  let S := A.toFinset
  have hc : S.card=A.length := List.toFinset_card_of_nodup hnodup
  have hspan : span S≤ell := span_le_of_interval S lo ell (by
    intro a ha
    exact hA a (List.mem_toFinset.mp ha))
  have hzS : ∃ z : Point → Bool, properOn (strictSource fun a => a∈S) z := by
    simpa only [S,List.mem_toFinset] using hz
  have hb := (hs S (hspan.trans hell) hzS).trans (Nat.mul_le_mul_left q hspan)
  have hp : A.length*(A.length-1)=2*M S := by
    have he := square_eq_self_add_twice_choose S.card
    rw [hc,pow_two] at he
    dsimp [M]
    rw [hc,Nat.mul_sub_left_distrib,Nat.mul_one]
    omega
  rw [hp]
  nlinarith

/-- Full conditional 361 bound; the existential G9 premise is not asserted. -/
theorem g9_three (hg : G9ExistsOn 360) : ramseyL 3 361 := by
  apply three_color_span_reduction_interval 20 (by decide)
  apply finset_span_bridge 20 360
  intro A hspan hz
  exact (g9_exists_on_consequences 360 hg A hspan hz).2

theorem g9_three_universal (hg : G9) : ramseyL 3 361 :=
  g9_three (g9_implies_exists_on hg 360)

theorem g9_s21 (hg : G9ExistsOn 99994) (A : Finset ℤ) (hspan : span A≤99994)
    (hz : ∃ z : Point → Bool, properOn (strictSource fun a => a∈A) z) :
    M A≤21*span A := by
  have hs := (g9_exists_on_consequences 99994 hg A hspan hz).2
  omega

end EnergyForcing.G9Formal
