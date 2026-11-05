import Mathlib

set_option autoImplicit false

namespace EnergyForcing.Alteration

open Finset
open scoped BigOperators

variable {α β : Type*} [DecidableEq α] [DecidableEq β]

/-- Product Bernoulli weight, defined by a finite polynomial. -/
noncomputable def weight (A X : Finset α) (p : ℝ) : ℝ :=
  (∏ _a ∈ X, p) * ∏ _a ∈ A \ X, (1-p)

theorem weight_nonneg (A X : Finset α) (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) :
    0 ≤ weight A X p := by
  unfold weight
  exact mul_nonneg (Finset.prod_nonneg (fun _ _ => hp))
    (Finset.prod_nonneg (fun _ _ => sub_nonneg.mpr hp1))

/-- Probability that every point of Q is retained, with no independence axiom. -/
theorem containment_mass (A Q : Finset α) (hQ : Q ⊆ A) (p : ℝ) :
    (∑ X ∈ A.powerset, if Q ⊆ X then weight A X p else 0) = p^Q.card := by
  classical
  have hprod : (∏ a ∈ A, (p + if a ∈ Q then 0 else 1-p)) = p^Q.card := by
    calc
      _ = ∏ a ∈ Q, (p + if a ∈ Q then 0 else 1-p) := by
        exact (Finset.prod_subset hQ (fun a ha hnot => by simp [hnot])).symm
      _ = ∏ _a ∈ Q, p := Finset.prod_congr rfl (fun a ha => by rw [if_pos ha, add_zero])
      _ = _ := by simp
  rw [← hprod, Finset.prod_add]
  apply Finset.sum_congr rfl
  intro X hX
  have hXA := Finset.mem_powerset.mp hX
  by_cases h : Q ⊆ X
  · rw [if_pos h]
    unfold weight
    congr 1
    apply Finset.prod_congr rfl
    intro a ha
    rw [if_neg (fun hq => (Finset.mem_sdiff.mp ha).2 (h hq))]
  · rw [if_neg h]
    obtain ⟨a,haQ,haX⟩ := Finset.not_subset.mp h
    have hz : (∏ a ∈ A \ X, if a ∈ Q then (0 : ℝ) else 1-p)=0 := by
      exact Finset.prod_eq_zero (Finset.mem_sdiff.mpr ⟨hQ haQ,haX⟩) (if_pos haQ)
    rw [hz, mul_zero]

theorem total_mass (A : Finset α) (p : ℝ) :
    (∑ X ∈ A.powerset, weight A X p)=1 := by
  simpa using containment_mass A ∅ (Finset.empty_subset A) p

theorem retained_card_expectation (A : Finset α) (p : ℝ) :
    (∑ X ∈ A.powerset, weight A X p * (X.card : ℝ)) = (A.card : ℝ)*p := by
  classical
  have hc (X : Finset α) (hX : X ⊆ A) :
      (X.card : ℝ) = ∑a∈A, if a ∈ X then (1 : ℝ) else 0 := by
    rw [← Finset.sum_filter]
    have hh : A.filter (fun a => a∈X)=X := by ext a; simp; exact fun ha => hX ha
    simp [hh]
  calc
    _ = ∑X∈A.powerset, ∑a∈A, if ({a} : Finset α) ⊆ X then weight A X p else 0 := by
      apply Finset.sum_congr rfl
      intro X hX
      rw [hc X (Finset.mem_powerset.mp hX), Finset.mul_sum]
      simp
    _ = ∑a∈A, ∑X∈A.powerset, if ({a} : Finset α) ⊆ X then weight A X p else 0 := Finset.sum_comm
    _ = ∑a∈A, p := Finset.sum_congr rfl (fun a ha => by
      rw [containment_mass A {a} (Finset.singleton_subset_iff.mpr ha), Finset.card_singleton, pow_one])
    _ = _ := by simp

theorem retained_edge_expectation (A : Finset α) (H : Finset β) (V : β → Finset α)
    (hV : ∀e∈H, V e ⊆ A) (p : ℝ) :
    (∑X∈A.powerset, weight A X p * ((H.filter fun e => V e ⊆ X).card : ℝ)) =
      ∑e∈H, p^(V e).card := by
  classical
  calc
    _ = ∑X∈A.powerset, ∑e∈H, if V e ⊆ X then weight A X p else 0 := by
      apply Finset.sum_congr rfl
      intro X hX
      simp only [Finset.card_eq_sum_ones, Nat.cast_sum, Nat.cast_one,
        Finset.sum_filter, Finset.mul_sum, Nat.cast_ite, mul_ite, mul_one, mul_zero, Nat.cast_zero]
    _ = ∑e∈H, ∑X∈A.powerset, if V e ⊆ X then weight A X p else 0 := Finset.sum_comm
    _ = _ := Finset.sum_congr rfl (fun e he => containment_mass A (V e) (hV e he) p)

/-- A finite weighted average never exceeds all of its summands. -/
theorem exists_score_ge_mean (A : Finset α) (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1)
    (score : Finset α → ℝ) :
    ∃X∈A.powerset, (∑Y∈A.powerset, weight A Y p * score Y) ≤ score X := by
  classical
  obtain ⟨X,hX,hmax⟩ := Finset.exists_max_image A.powerset score
    (by exact ⟨∅, Finset.mem_powerset.mpr (Finset.empty_subset A)⟩)
  refine ⟨X,hX,?_⟩
  calc
    _ ≤ ∑Y∈A.powerset, weight A Y p * score X :=
      Finset.sum_le_sum (fun Y hY => mul_le_mul_of_nonneg_left (hmax Y hY)
        (weight_nonneg A Y p hp hp1))
    _ = score X := by rw [← Finset.sum_mul, total_mass, one_mul]

/-- General finite alteration: delete a specified point of each retained edge. -/
theorem finite_alteration (A : Finset α) (H : Finset β) (V : β → Finset α)
    (root : β → α) (hV : ∀e∈H, V e ⊆ A) (hroot : ∀e∈H, root e ∈ V e)
    (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) :
    ∃B⊆A, (∀e∈H, ¬ V e ⊆ B) ∧
      (A.card : ℝ)*p - (∑e∈H, p^(V e).card) ≤ (B.card : ℝ) := by
  classical
  let retained := fun X => H.filter (fun e => V e ⊆ X)
  let score := fun X => (X.card : ℝ) - ((retained X).card : ℝ)
  obtain ⟨X,hX,hm⟩ := exists_score_ge_mean A p hp hp1 score
  have hmean : (∑Y∈A.powerset, weight A Y p * score Y) =
      (A.card : ℝ)*p - ∑e∈H, p^(V e).card := by
    simp only [score, retained, mul_sub, Finset.sum_sub_distrib]
    rw [retained_card_expectation, retained_edge_expectation A H V hV]
  rw [hmean] at hm
  let D := (retained X).image root
  let B := X \ D
  have hBX : B ⊆ X := Finset.sdiff_subset
  refine ⟨B, hBX.trans (Finset.mem_powerset.mp hX), ?_, ?_⟩
  · intro e he hVB
    have heX : e∈retained X := Finset.mem_filter.mpr ⟨he,hVB.trans hBX⟩
    have hd : root e∈D := Finset.mem_image.mpr ⟨e,heX,rfl⟩
    exact (Finset.mem_sdiff.mp (hVB (hroot e he))).2 hd
  · have hc : X.card ≤ B.card + (retained X).card := by
      have hD := Finset.card_image_le (s:=retained X) (f:=root)
      have hsd := Finset.card_sdiff_add_card_inter X D
      have hi := Finset.card_le_card (Finset.inter_subset_right : X∩D ⊆ D)
      dsimp [B, D] at *
      omega
    have hcr : (X.card : ℝ) ≤ (B.card : ℝ) + ((retained X).card : ℝ) := by exact_mod_cast hc
    dsimp [score] at hm
    linarith

end EnergyForcing.Alteration
