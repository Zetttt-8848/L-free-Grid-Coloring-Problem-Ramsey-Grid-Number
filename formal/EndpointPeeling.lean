import EndpointCounting

namespace EnergyForcing.Counting

theorem endpoint_corners_mono {A B : Finset ℤ} (h : A ⊆ B) :
    sourceCorners A ⊆ sourceCorners B := by
  rintro ⟨x,y,w⟩ hp
  rcases (mem_sourceCorners A x y w).mp hp with ⟨hx,hy,hw,hyx,hxw,hz⟩
  exact (mem_sourceCorners B x y w).mpr ⟨h hx,h hy,h hw,hyx,hxw,h hz⟩

theorem endpoint_T_mono {A B : Finset ℤ} (h : A ⊆ B) : T A ≤ T B :=
  Finset.card_le_card (endpoint_corners_mono h)

theorem endpoint_proper_restrict {A B : Finset ℤ} (h : A ⊆ B)
    (z : Point → Bool) (hz : properOn (strictSource (fun a => a ∈ B)) z) :
    properOn (strictSource (fun a => a ∈ A)) z := by
  intro x y d hd h₁ h₂ h₃
  exact hz x y d hd ⟨h h₁.1,h h₁.2.1,h₁.2.2⟩
    ⟨h h₂.1,h h₂.2.1,h₂.2.2⟩ ⟨h h₃.1,h h₃.2.1,h₃.2.2⟩

theorem endpoint_T_of_card_le_one (A : Finset ℤ) (h : A.card ≤ 1) : T A = 0 := by
  unfold T
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  rintro ⟨x,y,w⟩ hp
  rcases (mem_sourceCorners A x y w).mp hp with ⟨hx,hy,hw,hyx,hxw,hz⟩
  have hxy := (Finset.card_le_one.mp h) x hx y hy
  omega

/-- An endpoint is an attained minimum or maximum, stated without partial operations. -/
def IsEndpoint (A : Finset ℤ) (a : ℤ) : Prop :=
  a ∈ A ∧ ((∀ x ∈ A, a ≤ x) ∨ (∀ x ∈ A, x ≤ a))

/-- The manuscript's EP10 hypothesis, with actual finite corner counts. -/
def EP10 : Prop :=
  ∀ A : Finset ℤ, 2 ≤ A.card →
    (∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) →
    ∃ a, IsEndpoint A a ∧ T A - T (A.erase a) ≤ 10*(A.card-1)

/-- The same hypothesis restricted to any class hereditary under single deletion. -/
def EP10On (P : Finset ℤ → Prop) : Prop :=
  ∀ A : Finset ℤ, P A → 2 ≤ A.card →
    (∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) →
    ∃ a, IsEndpoint A a ∧ T A - T (A.erase a) ≤ 10*(A.card-1)

theorem endpoint_reduction_on (P : Finset ℤ → Prop)
    (hereditary : ∀ A a, P A → P (A.erase a)) (hep : EP10On P)
    (A : Finset ℤ) (hPA : P A)
    (hz : ∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) :
    T A ≤ 10*M A := by
  have hmain : ∀ n : ℕ, ∀ B : Finset ℤ, B.card = n → P B →
      (∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ B)) z) →
      T B ≤ 10*M B := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro B hcard hPB hzB
      by_cases hn : B.card ≤ 1
      · rw [endpoint_T_of_card_le_one B hn]
        exact Nat.zero_le _
      · obtain ⟨a,ha,hdel⟩ := hep B hPB (by omega) hzB
        have hca := Finset.card_erase_of_mem ha.1
        have hlt : (B.erase a).card < n := by omega
        obtain ⟨z,hz⟩ := hzB
        have hsmall := ih (B.erase a).card hlt (B.erase a) rfl
          (hereditary B a hPB)
          ⟨z,endpoint_proper_restrict (Finset.erase_subset a B) z hz⟩
        have hmono := endpoint_T_mono (Finset.erase_subset a B)
        have hcs : B.card = (B.erase a).card+1 := by omega
        have hM : M B = M (B.erase a)+(B.erase a).card := by
          unfold M
          rw [hcs,Nat.choose_succ_succ']
          simp [Nat.add_comm]
        omega
  exact hmain A.card A rfl hPA hz

/-- EP10 implies H10 by actual finite deletion, without a recurrence assumption on T. -/
theorem endpoint_reduction (hep : EP10) (A : Finset ℤ)
    (hz : ∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) :
    T A ≤ 10*M A := by
  apply endpoint_reduction_on (fun _ => True) (by simp) _ A trivial hz
  intro B _ hn hzB
  exact hep B hn hzB

theorem endpoint_span_mono {A B : Finset ℤ} (h : A ⊆ B) : span A ≤ span B := by
  by_cases hA : A.Nonempty
  · have hB : B.Nonempty := hA.mono h
    have hmin : B.min' hB ≤ A.min' hA :=
      Finset.min'_le B _ (h (Finset.min'_mem A hA))
    have hmax : A.max' hA ≤ B.max' hB :=
      Finset.le_max' B _ (h (Finset.max'_mem A hA))
    simp only [span,dif_pos hA,dif_pos hB]
    omega
  · simp [span,hA]

/-- The finite-range part of peeling: each deleted set stays in the original span range. -/
theorem endpoint_reduction_bounded_span (Lmax : ℕ)
    (hep : EP10On (fun A => span A ≤ Lmax)) (A : Finset ℤ)
    (hspan : span A ≤ Lmax)
    (hz : ∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) :
    T A ≤ 10*M A := by
  apply endpoint_reduction_on (fun B => span B ≤ Lmax) _ hep A hspan hz
  intro B a hB
  exact (endpoint_span_mono (Finset.erase_subset a B)).trans hB

/-- The second conclusion of the endpoint reduction: the actual span estimate. -/
theorem endpoint_span_bound (hep : EP10) (A : Finset ℤ)
    (hz : ∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) :
    M A ≤ 21*span A := by
  have hT := endpoint_reduction hep A hz
  have hTR : (T A : ℝ) ≤ (10 : ℝ)*(M A : ℝ) := by exact_mod_cast hT
  have h := span_pair_bound A 10 (by norm_num) hTR
  norm_num at h
  exact_mod_cast h

theorem endpoint_span_bound_bounded (Lmax : ℕ)
    (hep : EP10On (fun A => span A ≤ Lmax)) (A : Finset ℤ)
    (hspan : span A ≤ Lmax)
    (hz : ∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) :
    M A ≤ 21*span A := by
  have hT := endpoint_reduction_bounded_span Lmax hep A hspan hz
  have hTR : (T A : ℝ) ≤ (10 : ℝ)*(M A : ℝ) := by exact_mod_cast hT
  have h := span_pair_bound A 10 (by norm_num) hTR
  norm_num at h
  exact_mod_cast h

/-- The manuscript's finite S21 conclusion follows from EP10 only in that same range. -/
theorem endpoint_s21
    (hep : EP10On (fun A => span A ≤ 99994)) (A : Finset ℤ)
    (hspan : span A ≤ 99994)
    (hz : ∃ z : Point → Bool, properOn (strictSource (fun a => a ∈ A)) z) :
    M A ≤ 21*span A :=
  endpoint_span_bound_bounded 99994 hep A hspan hz

#print axioms endpoint_reduction_on
#print axioms endpoint_reduction
#print axioms endpoint_reduction_bounded_span
#print axioms endpoint_span_bound
#print axioms endpoint_s21

end EnergyForcing.Counting
