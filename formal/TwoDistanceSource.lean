import TwoDistanceCounting

set_option autoImplicit false
namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.PairCollisions
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
attribute [local instance] Classical.propDecidable
noncomputable local instance : DecidableEq V := Classical.decEq V

theorem image_collision_mem (A : Finset ℤ) (phi : ℤ→V) (tau : ℝ)
    (h:Hypotheses A phi tau) (S : Finset (Finset ℤ)) (hS:S∈collisions A) :
    S.image (fun P=> points P phi)∈geometricCollisions (points A phi) tau := by
  rcases Finset.mem_filter.mp hS with ⟨hS,hfour,hsum⟩
  rcases Finset.mem_powersetCard.mp hS with ⟨hsub,hcard⟩
  apply (mem_geometricCollisions _ _ _).mpr
  constructor
  · apply Finset.mem_powersetCard.mpr
    constructor
    · intro R hR
      obtain ⟨P,hP,rfl⟩:=Finset.mem_image.mp hR
      obtain ⟨Q,hQ,hQP⟩:=Finset.exists_mem_ne (by omega:1< S.card) P
      apply (mem_longPairs _ _ _).mpr
      exact ⟨pair_image_mem A phi tau h P (hsub hP),
        collision_pairs_long A phi tau h P Q (hsub hP) (hsub hQ) (Ne.symm hQP) (hsum P hP Q hQ)⟩
    · rw [Finset.card_image_iff.mpr]
      · exact hcard
      · intro P hP Q hQ he
        exact pair_image_injective A phi tau h P Q
          (Finset.mem_powersetCard.mp (hsub hP)).1 (Finset.mem_powersetCard.mp (hsub hQ)).1 he
  · intro R hR S' hS'
    obtain ⟨P,hP,rfl⟩:=Finset.mem_image.mp hR
    obtain ⟨Q,hQ,rfl⟩:=Finset.mem_image.mp hS'
    exact equal_pair_sums_preserved A phi tau h P Q (hsub hP) (hsub hQ) (hsum P hP Q hQ)

theorem image_collision_injective (A : Finset ℤ) (phi : ℤ→V) (tau : ℝ)
    (h:Hypotheses A phi tau) :
    Set.InjOn (fun S:Finset (Finset ℤ)=> S.image (fun P=> points P phi)) (collisions A) := by
  intro S hS R hR he
  dsimp only at he
  have hs: S⊆A.powersetCard 2:=(Finset.mem_powersetCard.mp (Finset.mem_filter.mp hS).1).1
  have hr: R⊆A.powersetCard 2:=(Finset.mem_powersetCard.mp (Finset.mem_filter.mp hR).1).1
  ext P
  constructor
  · intro hP
    have hi:points P phi∈R.image (fun Q=> points Q phi):=by rw [←he];exact Finset.mem_image_of_mem _ hP
    obtain ⟨Q,hQ,hQP⟩:=Finset.mem_image.mp hi
    have hEq:Q=P:=pair_image_injective A phi tau h Q P
      (Finset.mem_powersetCard.mp (hr hQ)).1 (Finset.mem_powersetCard.mp (hs hP)).1 hQP
    simpa [hEq] using hQ
  · intro hP
    have hi:points P phi∈S.image (fun Q=> points Q phi):=by rw [he];exact Finset.mem_image_of_mem _ hP
    obtain ⟨Q,hQ,hQP⟩:=Finset.mem_image.mp hi
    have hEq:Q=P:=pair_image_injective A phi tau h Q P
      (Finset.mem_powersetCard.mp (hs hQ)).1 (Finset.mem_powersetCard.mp (hr hP)).1 hQP
    simpa [hEq] using hQ

theorem source_corner_le_geomT (A : Finset ℤ) (phi : ℤ→V) (tau : ℝ)
    (h:Hypotheses A phi tau) : T A≤ geomT (points A phi) tau := by
  rw [corner_count_no_progression A (no_progression A phi tau h),geomT]
  apply Nat.mul_le_mul_left
  exact Finset.card_le_card_of_injOn _ (image_collision_mem A phi tau h) (image_collision_injective A phi tau h)

theorem points_card (A : Finset ℤ) (phi : ℤ→V) (tau : ℝ)
    (h:Hypotheses A phi tau) : (points A phi).card=A.card :=
  Finset.card_image_of_injOn h.injective

theorem points_twoDistances (A : Finset ℤ) (phi : ℤ→V) (tau : ℝ)
    (h:Hypotheses A phi tau) : TwoDistances (points A phi) tau := by
  intro x hx y hy hxy
  obtain ⟨a,ha,rfl⟩:=Finset.mem_image.mp hx
  obtain ⟨b,hb,rfl⟩:=Finset.mem_image.mp hy
  exact h.distances a ha b hb (by intro he;subst b;contradiction)

end EnergyForcing.TwoDistance
