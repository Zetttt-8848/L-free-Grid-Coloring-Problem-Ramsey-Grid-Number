import TwoDistanceGeometry
import SourcePairCollisions

set_option autoImplicit false

namespace EnergyForcing.TwoDistance

open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.PairCollisions

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable def points (A : Finset ℤ) (phi : ℤ → E) : Finset E := by
  classical
  exact A.image phi

def LongPair (tau : ℝ) (P : Finset E) : Prop :=
  ∀x∈P, ∀y∈P, x≠y → ‖x-y‖^2=2*tau

/-- Actual unordered pairs of image points whose midpoint is c and which are long. -/
noncomputable def midpointPairs (X : Finset E) (tau : ℝ) (c : E) : Finset (Finset E) := by
  classical
  exact (X.powersetCard 2).filter (fun P => (∑x∈P,x)=(2 : ℝ) • c ∧ LongPair tau P)

theorem pair_image_mem (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (P : Finset ℤ) (hP : P∈A.powersetCard 2) :
    points P phi∈(points A phi).powersetCard 2 := by
  classical
  rcases Finset.mem_powersetCard.mp hP with ⟨hsub,hcard⟩
  apply Finset.mem_powersetCard.mpr
  constructor
  · exact Finset.image_subset_image hsub
  · rw [points,Finset.card_image_of_injOn (fun a ha b hb he => h.injective (hsub ha) (hsub hb) he)]
    exact hcard

theorem pair_image_injective (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (P Q : Finset ℤ) (hP : P⊆A) (hQ : Q⊆A)
    (he : points P phi=points Q phi) : P=Q := by
  classical
  ext a
  constructor
  · intro ha
    have hi : phi a∈points Q phi := he ▸ Finset.mem_image_of_mem phi ha
    obtain ⟨b,hb,hab⟩ := Finset.mem_image.mp hi
    have heq : b=a := h.injective (hQ hb) (hP ha) hab
    simpa only [heq] using hb
  · intro ha
    have hi : phi a∈points P phi := he.symm ▸ Finset.mem_image_of_mem phi ha
    obtain ⟨b,hb,hab⟩ := Finset.mem_image.mp hi
    have heq : b=a := h.injective (hP hb) (hQ ha) hab
    simpa only [heq] using hb

theorem equal_pair_sums_preserved (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (P Q : Finset ℤ)
    (hP : P∈A.powersetCard 2) (hQ : Q∈A.powersetCard 2)
    (he : (∑x∈P,x)=∑x∈Q,x) :
    (∑x∈points P phi,x)=∑x∈points Q phi,x := by
  classical
  rcases Finset.mem_powersetCard.mp hP with ⟨hPA,hPc⟩
  rcases Finset.mem_powersetCard.mp hQ with ⟨hQA,hQc⟩
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hPc
  obtain ⟨c,e,hce,rfl⟩ := Finset.card_eq_two.mp hQc
  have ha := hPA (by simp : a∈({a,b} : Finset ℤ))
  have hb := hPA (by simp : b∈({a,b} : Finset ℤ))
  have hc := hQA (by simp : c∈({c,e} : Finset ℤ))
  have he' := hQA (by simp : e∈({c,e} : Finset ℤ))
  have hab' : phi a≠phi b := fun hh => hab (h.injective ha hb hh)
  have hce' : phi c≠phi e := fun hh => hce (h.injective hc he' hh)
  simp only [Finset.sum_pair hab,Finset.sum_pair hce] at he
  simpa only [points,Finset.image_insert,Finset.image_singleton,Finset.sum_pair hab',Finset.sum_pair hce'] using
    h.freiman a ha b hb c hc e he' he

theorem collision_pairs_long (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (P Q : Finset ℤ)
    (hP : P∈A.powersetCard 2) (hQ : Q∈A.powersetCard 2)
    (hne : P≠Q) (he : (∑x∈P,x)=∑x∈Q,x) : LongPair tau (points P phi) := by
  classical
  rcases Finset.mem_powersetCard.mp hP with ⟨hPA,hPc⟩
  rcases Finset.mem_powersetCard.mp hQ with ⟨hQA,hQc⟩
  have hd := equal_sum_pairs_disjoint P Q hPc hQc hne he
  obtain ⟨a,e,hae,rfl⟩ := Finset.card_eq_two.mp hPc
  obtain ⟨b,c,hbc,rfl⟩ := Finset.card_eq_two.mp hQc
  have ha := hPA (by simp : a∈({a,e} : Finset ℤ))
  have he' := hPA (by simp : e∈({a,e} : Finset ℤ))
  have hb := hQA (by simp : b∈({b,c} : Finset ℤ))
  have hc := hQA (by simp : c∈({b,c} : Finset ℤ))
  have hab : a≠b := by
    intro hh; subst b
    exact Finset.disjoint_left.mp hd (by simp : a∈({a,e} : Finset ℤ)) (by simp)
  have hac : a≠c := by
    intro hh; subst c
    exact Finset.disjoint_left.mp hd (by simp : a∈({a,e} : Finset ℤ)) (by simp)
  simp only [Finset.sum_pair hae,Finset.sum_pair hbc] at he
  have hs := parallelogram_square A phi tau h a b c e ha hb hc he' hab hac hae hbc he
  intro x hx y hy hxy
  simp only [points,Finset.image_insert,Finset.image_singleton,Finset.mem_insert,Finset.mem_singleton] at hx hy
  rcases hx with rfl|rfl <;> rcases hy with rfl|rfl
  · contradiction
  · rw [norm_sub_rev]; exact hs.2.2.1
  · exact hs.2.2.1
  · contradiction

/-- The geometric midpoint bound controls the actual integer pair-sum fibers. -/
theorem midpoint_cap_pair_sum_cap (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau)
    (hcap : ∀c : E, (midpointPairs (points A phi) tau c).card ≤ 3) :
    ∀s : ℤ, (sumPairs A s).card ≤ 3 := by
  classical
  intro s
  by_cases hsmall : (sumPairs A s).card ≤ 1
  · omega
  have hn : (sumPairs A s).Nonempty := Finset.card_pos.mp (by omega)
  obtain ⟨R,hR⟩ := hn
  let c : E := (1/2 : ℝ) • (∑x∈points R phi,x)
  have hc : (2 : ℝ) • c=∑x∈points R phi,x := by dsimp [c]; rw [smul_smul]; norm_num
  have hmap : ∀P∈sumPairs A s, points P phi∈midpointPairs (points A phi) tau c := by
    intro P hP
    obtain ⟨Q,hQ,hPQ⟩ := Finset.exists_mem_ne (by omega : 1 < (sumPairs A s).card) P
    have hp' := Finset.mem_filter.mp hP
    have hq' := Finset.mem_filter.mp hQ
    have hr' := Finset.mem_filter.mp hR
    apply Finset.mem_filter.mpr
    refine ⟨pair_image_mem A phi tau h P hp'.1,?_,?_⟩
    · rw [hc]
      exact equal_pair_sums_preserved A phi tau h P R hp'.1 hr'.1 (hp'.2.trans hr'.2.symm)
    · exact collision_pairs_long A phi tau h P Q hp'.1 hq'.1 (Ne.symm hPQ) (hp'.2.trans hq'.2.symm)
  have hinj : Set.InjOn (fun P => points P phi) (sumPairs A s : Set (Finset ℤ)) := by
    intro P hP Q hQ he
    exact pair_image_injective A phi tau h P Q
      (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hP).1).1
      (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hQ).1).1 he
  exact (Finset.card_le_card_of_injOn _ hmap hinj).trans (hcap c)

/-- The numerical and coloring conclusions of thm:midpoint-three.
The graph-family module supplies its separate sharpness assertion. -/
theorem midpoint_three_bounds (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau)
    (hcap : ∀c : E, (midpointPairs (points A phi) tau c).card ≤ 3) :
    T A ≤ 2*M A ∧ (M A : ℝ) ≤ 5*(span A : ℝ) ∧
      properOn (strictSource (fun a => a∈A)) (distanceColor phi tau) := by
  have hT := pair_sum_cap_bound A (no_progression A phi tau h)
    (midpoint_cap_pair_sum_cap A phi tau h hcap)
  refine ⟨hT,?_,squared_distance_coloring_proper A phi tau h⟩
  have hh := span_pair_bound A 2 (by norm_num) (by exact_mod_cast hT)
  norm_num at hh
  exact hh

end EnergyForcing.TwoDistance
