import TwoDistanceGeometry

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators InnerProductSpace
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]

theorem orthogonal_sum_norm {k : ℕ} (p : Fin k→V) (tau : ℝ)
    (hn : ∀i, ‖p i‖^2=tau/2) (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0)
    (a : Fin k→ℝ) : ‖∑i,a i • p i‖^2=(tau/2)*∑i,(a i)^2 := by
  have hi (i j : Fin k) : ⟪p i,p j⟫_ℝ=if i=j then tau/2 else 0 := by
    split_ifs with he
    · subst j; simpa only [real_inner_self_eq_norm_sq] using hn i
    · exact ho i j he
  rw [← real_inner_self_eq_norm_sq]
  simp_rw [sum_inner,inner_sum,real_inner_smul_left,real_inner_smul_right,hi]
  simp only [mul_ite,mul_zero,Finset.sum_ite_eq',Finset.sum_ite_eq,Finset.mem_univ,if_true]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

theorem orthogonal_residual {k : ℕ} (p : Fin k→V) (tau : ℝ)
    (hn : ∀i, ‖p i‖^2=tau/2) (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0)
    (q : V) (a : Fin k→ℝ) :
    ‖q-∑i,a i • p i‖^2=‖q‖^2+(tau/2)*∑i,(a i)^2-2*∑i,a i*⟪q,p i⟫_ℝ := by
  rw [norm_sub_sq_real,orthogonal_sum_norm p tau hn ho]
  simp_rw [inner_sum,real_inner_smul_right]
  ring

noncomputable def radiusProjection {k : ℕ} (p : Fin k→V) (tau : ℝ) (q : V) : V :=
  ∑i,((2/tau)*⟪q,p i⟫_ℝ) • p i

theorem radius_projection_identity {k : ℕ} (p : Fin k→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0) (q : V) :
    (tau/2)*‖q-radiusProjection p tau q‖^2=
      (tau/2)*‖q‖^2-∑i,⟪q,p i⟫_ℝ^2 := by
  rw [radiusProjection,orthogonal_residual p tau hn ho]
  have hsq : (tau/2)*(tau/2)*(∑i,((2/tau)*⟪q,p i⟫_ℝ)^2)=∑i,⟪q,p i⟫_ℝ^2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i hi
    field_simp
    ring
  have hlin : tau*(∑i,(2/tau)*⟪q,p i⟫_ℝ * ⟪q,p i⟫_ℝ)=2*∑i,⟪q,p i⟫_ℝ^2 := by
    rw [Finset.mul_sum,Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i hi
    field_simp
    ring
  nlinarith

theorem outside_radius_cases {k : ℕ} (hk : 0 < k) (p : Fin k→V) (tau : ℝ)
    (hn : ∀i, ‖p i‖^2=tau/2) (q : V)
    (hm : ∀i, ‖q-p i‖^2=tau ∨ ‖q-p i‖^2=2*tau)
    (hp : ∀i, ‖q+p i‖^2=tau ∨ ‖q+p i‖^2=2*tau) :
    (‖q‖^2=tau/2 ∧ ∀i, ⟪q,p i⟫_ℝ=0) ∨
    (‖q‖^2=tau ∧ ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4) ∨
    (‖q‖^2=3*tau/2 ∧ ∀i, ⟪q,p i⟫_ℝ=0) := by
  have hcase : ‖q‖^2=tau/2 ∨ ‖q‖^2=tau ∨ ‖q‖^2=3*tau/2 := by
    let i : Fin k := ⟨0,hk⟩
    have he₁ := norm_sub_sq_real q (p i)
    have he₂ := norm_add_sq_real q (p i)
    rw [hn] at he₁ he₂
    rcases hm i with h|h <;> rcases hp i with h'|h' <;>
      first | (left; linarith) | (right; left; linarith) | (right; right; linarith)
  rcases hcase with h|h|h
  · left; refine ⟨h,?_⟩; intro i
    have he₁ := norm_sub_sq_real q (p i)
    have he₂ := norm_add_sq_real q (p i)
    rw [hn] at he₁ he₂
    rcases hm i with h'|h' <;> rcases hp i with h''|h'' <;> linarith
  · right; left; refine ⟨h,?_⟩; intro i
    have he₁ := norm_sub_sq_real q (p i)
    rw [hn] at he₁
    rcases hm i with h'|h'
    · left; linarith
    · right; linarith
  · right; right; refine ⟨h,?_⟩; intro i
    have he₁ := norm_sub_sq_real q (p i)
    have he₂ := norm_add_sq_real q (p i)
    rw [hn] at he₁ he₂
    rcases hm i with h'|h' <;> rcases hp i with h''|h'' <;> linarith

theorem middle_radius_identity {k : ℕ} (p : Fin k→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0) (q : V)
    (hq : ‖q‖^2=tau) (hi : ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4) :
    (tau/2)*‖q-radiusProjection p tau q‖^2=(8-(k : ℝ))*tau^2/16 := by
  have hs : (∑i,⟪q,p i⟫_ℝ^2)=(k : ℝ)*tau^2/16 := by
    have he (i : Fin k) : ⟪q,p i⟫_ℝ^2=tau^2/16 := by rcases hi i with h|h <;> rw [h] <;> ring
    simp_rw [he]
    simp only [Finset.sum_const,Finset.card_univ,Fintype.card_fin,nsmul_eq_mul]
    ring
  rw [radius_projection_identity p tau ht hn ho,hq,hs]
  ring

theorem nine_radius_orthogonal {k : ℕ} (hk : 9 ≤ k) (p : Fin k→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0) (q : V)
    (hm : ∀i, ‖q-p i‖^2=tau ∨ ‖q-p i‖^2=2*tau)
    (hp : ∀i, ‖q+p i‖^2=tau ∨ ‖q+p i‖^2=2*tau) : ∀i, ⟪q,p i⟫_ℝ=0 := by
  rcases outside_radius_cases (by omega) p tau hn q hm hp with h|h|h
  · exact h.2
  · have he := middle_radius_identity p tau ht hn ho q h.1 h.2
    have hkR : (9:ℝ) ≤ k := by exact_mod_cast hk
    have hpos : 0 < tau^2 := sq_pos_of_pos ht
    have hnon := mul_nonneg (show 0 ≤ tau/2 by positivity) (sq_nonneg ‖q-radiusProjection p tau q‖)
    have hneg := mul_neg_of_neg_of_pos (show 8-(k : ℝ)<0 by linarith) hpos
    nlinarith
  · exact h.2

theorem eight_radius_reconstruction (p : Fin 8→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0) (q : V)
    (hq : ‖q‖^2=tau) (hi : ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4) :
    q=radiusProjection p tau q := by
  have he := middle_radius_identity p tau ht hn ho q hq hi
  norm_num at he
  exact sub_eq_zero.mp (he.resolve_left (ne_of_gt ht))

#print axioms nine_radius_orthogonal
#print axioms eight_radius_reconstruction
end EnergyForcing.TwoDistance
