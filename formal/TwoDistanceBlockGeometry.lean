import TwoDistanceIsolation

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace EnergyForcing.TwoDistance.RadiusBlock
open Finset
open scoped BigOperators InnerProductSpace
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
noncomputable local instance : DecidableEq V := Classical.decEq V
variable {X : Finset V} {tau : ℝ} {c : V} {k : ℕ}

theorem outside_endpoint_distances (B : RadiusBlock X tau c k) (hX : TwoDistances X tau)
    (x : V) (hx : x∈X) (hy : x∉B.vertices) :
    (∀i, ‖(x-c)-B.radii i‖^2=tau ∨ ‖(x-c)-B.radii i‖^2=2*tau) ∧
    (∀i, ‖(x-c)+B.radii i‖^2=tau ∨ ‖(x-c)+B.radii i‖^2=2*tau) := by
  have hne (q : Fin k×Bool) : x≠endpoint c B.radii q := by
    intro he
    exact hy (he ▸ Finset.mem_image_of_mem _ (Finset.mem_univ q))
  constructor
  · intro i
    have hh := hX x hx (endpoint c B.radii (i,true)) (B.endpoints_mem (i,true)) (hne (i,true))
    have he : x-endpoint c B.radii (i,true)=(x-c)-B.radii i := by simp [endpoint]; abel
    rwa [he] at hh
  · intro i
    have hh := hX x hx (endpoint c B.radii (i,false)) (B.endpoints_mem (i,false)) (hne (i,false))
    have he : x-endpoint c B.radii (i,false)=(x-c)+B.radii i := by simp [endpoint]; abel
    rwa [he] at hh

theorem nine_outside_orthogonal (B : RadiusBlock X tau c k) (ht : 0 < tau)
    (hX : TwoDistances X tau) (hk : 9 ≤ k) : B.OutsideOrthogonal := by
  intro x hx hy
  have hh := B.outside_endpoint_distances hX x hx hy
  exact nine_radius_orthogonal hk B.radii tau ht B.radius_sq B.orthogonal (x-c) hh.1 hh.2

theorem exceptional_eight_card_le (B : RadiusBlock X tau c 8) (ht : 0 < tau)
    (hX : TwoDistances X tau) (hnon : ¬B.OutsideOrthogonal) : X.card ≤ 53 := by
  classical
  let Q := (X\B.vertices).image (fun x => x-c)
  have hmem (q : V) : q∈Q ↔ ∃x, x∈X ∧ x∉B.vertices ∧ x-c=q := by
    simp [Q,Finset.mem_image,Finset.mem_sdiff,and_assoc]
  have hm : ∀q∈Q, ∀i, ‖q-B.radii i‖^2=tau ∨ ‖q-B.radii i‖^2=2*tau := by
    intro q hq
    obtain ⟨x,hx,hy,rfl⟩ := (hmem q).mp hq
    exact (B.outside_endpoint_distances hX x hx hy).1
  have hp : ∀q∈Q, ∀i, ‖q+B.radii i‖^2=tau ∨ ‖q+B.radii i‖^2=2*tau := by
    intro q hq
    obtain ⟨x,hx,hy,rfl⟩ := (hmem q).mp hq
    exact (B.outside_endpoint_distances hX x hx hy).2
  have hQQ : ∀q∈Q, ∀r∈Q, q≠r → ‖q-r‖^2=tau ∨ ‖q-r‖^2=2*tau := by
    intro q hq r hr hne
    obtain ⟨x,hx,hy,rfl⟩ := (hmem q).mp hq
    obtain ⟨y,hy,hy',rfl⟩ := (hmem r).mp hr
    have he : (x-c)-(y-c)=x-y := by abel
    rw [he]
    exact hX x hx y hy (by intro hh; exact hne (by rw [hh]))
  have hex : ∃q∈Q, ∃i, ⟪q,B.radii i⟫_ℝ≠0 := by
    unfold OutsideOrthogonal at hnon
    push_neg at hnon
    obtain ⟨x,hx,hy,i,hi⟩ := hnon
    exact ⟨x-c,(hmem _).mpr ⟨x,hx,hy,rfl⟩,i,hi⟩
  have hc := exceptional_eight_outside_card Q B.radii tau ht B.radius_sq B.orthogonal hm hp hQQ hex
  have hcard : Q.card=(X\B.vertices).card := Finset.card_image_of_injective _ (by intro x y he; exact sub_left_injective he)
  have hsplit := Finset.card_sdiff_add_card_eq_card B.vertices_subset
  have hverts := B.vertices_card
  rw [hcard] at hc
  omega

#print axioms nine_outside_orthogonal
#print axioms exceptional_eight_card_le
end EnergyForcing.TwoDistance.RadiusBlock
