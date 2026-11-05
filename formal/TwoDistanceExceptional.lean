import TwoDistanceProjection
import TwoDistanceCode

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators InnerProductSpace
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]

noncomputable def radiusLabel (p : Fin 8→V) (q : V) : SignLabel := by
  classical
  exact fun i => decide (0 < ⟪q,p i⟫_ℝ)

theorem radius_sign_coefficient (p : Fin 8→V) (tau : ℝ) (ht : 0 < tau) (q : V)
    (hi : ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4) (i : Fin 8) :
    (2/tau)*⟪q,p i⟫_ℝ=sign (radiusLabel p q) i/2 := by
  classical
  rcases hi i with hh|hh
  · simp only [sign,radiusLabel,hh]
    have hpos : 0 < tau/4 := by positivity
    simp only [hpos,decide_true,if_true]
    field_simp
    norm_num
  · simp only [sign,radiusLabel,hh]
    have hnot : ¬0 < -tau/4 := by linarith
    simp only [hnot,decide_false,Bool.false_eq_true,if_false]
    field_simp
    ring

theorem radius_sign_representation (p : Fin 8→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0) (q : V)
    (hq : ‖q‖^2=tau) (hi : ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4) :
    q=∑i,(sign (radiusLabel p q) i/2) • p i := by
  calc
    q = radiusProjection p tau q := eight_radius_reconstruction p tau ht hn ho q hq hi
    _ = _ := by unfold radiusProjection; simp_rw [radius_sign_coefficient p tau ht q hi]

theorem orthogonal_sum_inner {k : ℕ} (p : Fin k→V) (tau : ℝ)
    (hn : ∀i, ‖p i‖^2=tau/2) (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0)
    (a b : Fin k→ℝ) :
    ⟪∑i,a i • p i,∑i,b i • p i⟫_ℝ=(tau/2)*∑i,a i*b i := by
  have hi (i j : Fin k) : ⟪p i,p j⟫_ℝ=if i=j then tau/2 else 0 := by
    split_ifs with he
    · subst j; simpa only [real_inner_self_eq_norm_sq] using hn i
    · exact ho i j he
  simp_rw [sum_inner,inner_sum,real_inner_smul_left,real_inner_smul_right,hi]
  simp only [mul_ite,mul_zero,Finset.sum_ite_eq,Finset.mem_univ,if_true]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

theorem radius_sign_inner (p : Fin 8→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0) (q r : V)
    (hq : ‖q‖^2=tau) (hr : ‖r‖^2=tau)
    (hi : ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4)
    (hj : ∀i, ⟪r,p i⟫_ℝ=tau/4 ∨ ⟪r,p i⟫_ℝ= -tau/4) :
    ⟪q,r⟫_ℝ=(tau/8)*signDot (radiusLabel p q) (radiusLabel p r) := by
  conv_lhs => rw [radius_sign_representation p tau ht hn ho q hq hi,
    radius_sign_representation p tau ht hn ho r hr hj]
  rw [orthogonal_sum_inner p tau hn ho]
  unfold signDot
  rw [Finset.mul_sum,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

theorem middle_outside_card (Q : Finset V) (p : Fin 8→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0)
    (hq : ∀q∈Q, ‖q‖^2=tau)
    (hi : ∀q∈Q, ∀i, ⟪q,p i⟫_ℝ=tau/4 ∨ ⟪q,p i⟫_ℝ= -tau/4)
    (hQ : ∀q∈Q, ∀r∈Q, q≠r → ‖q-r‖^2=tau ∨ ‖q-r‖^2=2*tau) : Q.card ≤ 37 := by
  classical
  let C := Q.image (radiusLabel p)
  have hinj : Set.InjOn (radiusLabel p) (Q : Set V) := by
    intro q hq' r hr' he
    rw [radius_sign_representation p tau ht hn ho q (hq q hq') (hi q hq'),
      radius_sign_representation p tau ht hn ho r (hq r hr') (hi r hr'),he]
  have hc : C.card=Q.card := Finset.card_image_of_injOn hinj
  rw [← hc]
  apply sign_code_card_le
  intro v hv w hw hvw
  obtain ⟨q,hq',rfl⟩ := Finset.mem_image.mp hv
  obtain ⟨r,hr',rfl⟩ := Finset.mem_image.mp hw
  have hne : q≠r := fun hh => hvw (congrArg (radiusLabel p) hh)
  have hid := radius_sign_inner p tau ht hn ho q r (hq q hq') (hq r hr') (hi q hq') (hi r hr')
  have he := norm_sub_sq_real q r
  rw [hq q hq',hq r hr',hid] at he
  rcases hQ q hq' r hr' hne with hd|hd
  · right; nlinarith
  · left; nlinarith

theorem exceptional_eight_outside_card (Q : Finset V) (p : Fin 8→V) (tau : ℝ)
    (ht : 0 < tau) (hn : ∀i, ‖p i‖^2=tau/2)
    (ho : ∀i j, i≠j → ⟪p i,p j⟫_ℝ=0)
    (hm : ∀q∈Q, ∀i, ‖q-p i‖^2=tau ∨ ‖q-p i‖^2=2*tau)
    (hp : ∀q∈Q, ∀i, ‖q+p i‖^2=tau ∨ ‖q+p i‖^2=2*tau)
    (hQ : ∀q∈Q, ∀r∈Q, q≠r → ‖q-r‖^2=tau ∨ ‖q-r‖^2=2*tau)
    (hex : ∃q∈Q, ∃i, ⟪q,p i⟫_ℝ≠0) : Q.card ≤ 37 := by
  classical
  obtain ⟨q,hq,i,hi⟩ := hex
  have hqm : ‖q‖^2=tau ∧ ∀j, ⟪q,p j⟫_ℝ=tau/4 ∨ ⟪q,p j⟫_ℝ= -tau/4 := by
    rcases outside_radius_cases (by decide) p tau hn q (hm q hq) (hp q hq) with hh|hh|hh
    · exact False.elim (hi (hh.2 i))
    · exact hh
    · exact False.elim (hi (hh.2 i))
  have hmiddle (r : V) (hr : r∈Q) :
      ‖r‖^2=tau ∧ ∀j, ⟪r,p j⟫_ℝ=tau/4 ∨ ⟪r,p j⟫_ℝ= -tau/4 := by
    have hno (hnorm : ‖r‖^2=tau/2 ∨ ‖r‖^2=3*tau/2)
        (horth : ∀j, ⟪r,p j⟫_ℝ=0) : False := by
      have hqr : ⟪q,r⟫_ℝ=0 := by
        rw [radius_sign_representation p tau ht hn ho q hqm.1 hqm.2]
        simp only [sum_inner,real_inner_smul_left]
        apply Finset.sum_eq_zero
        intro j hj
        rw [real_inner_comm,horth,mul_zero]
      have hne : q≠r := by
        intro he; subst r
        rcases hnorm with hh|hh <;> nlinarith [hqm.1]
      have hd := hQ q hq r hr hne
      have he := norm_sub_sq_real q r
      rw [hqr,hqm.1] at he
      rcases hnorm with hh|hh <;> rcases hd with h|h <;> linarith
    rcases outside_radius_cases (by decide) p tau hn r (hm r hr) (hp r hr) with hh|hh|hh
    · exact False.elim (hno (Or.inl hh.1) hh.2)
    · exact hh
    · exact False.elim (hno (Or.inr hh.1) hh.2)
  exact middle_outside_card Q p tau ht hn ho (fun r hr => (hmiddle r hr).1)
    (fun r hr => (hmiddle r hr).2) hQ

#print axioms exceptional_eight_outside_card
end EnergyForcing.TwoDistance
