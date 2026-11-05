import GraphSourceColoring

set_option autoImplicit false

namespace EnergyForcing.GraphSources

open Finset
open scoped BigOperators

noncomputable def edgePoint {r : ℕ} (e : Finset (Fin r)) : EuclideanSpace ℝ (Fin r) :=
  (WithLp.equiv 2 _).symm (vertexVector e)

theorem edgePoint_apply {r : ℕ} (e : Finset (Fin r)) (i : Fin r) :
    edgePoint e i=(edgeDigits e i:ℝ) := rfl

theorem edgePoint_injective {r : ℕ} : Function.Injective (@edgePoint r) := by
  intro e f he
  apply vertexVector_injective
  funext i
  exact congrArg (fun p : EuclideanSpace ℝ (Fin r) => p i) he

theorem edgePoint_pair_fidelity {r : ℕ} (e f g h : Finset (Fin r)) :
    mark e+mark f=mark g+mark h ↔ edgePoint e+edgePoint f=edgePoint g+edgePoint h := by
  rw [vector_pair_sum_fidelity]
  constructor
  · intro hh
    apply PiLp.ext
    intro i
    exact congrFun hh i
  · intro hh
    funext i
    exact congrArg (fun p : EuclideanSpace ℝ (Fin r) => p i) hh

theorem sum_edgeDigits {r : ℕ} (e : Finset (Fin r)) :
    (∑i, (edgeDigits e i:ℝ))=(e.card:ℝ) := by
  have hn : (∑i, edgeDigits e i)=e.card := by
    simp [edgeDigits,← Finset.card_filter]
  exact_mod_cast hn

theorem edgePoint_distance {r : ℕ} (e f : Finset (Fin r)) :
    ‖edgePoint e-edgePoint f‖^2=(e.card:ℝ)+f.card-2*(e∩f).card := by
  rw [PiLp.norm_sq_eq_of_L2]
  have he : (∑i : Fin r, ‖(edgePoint e-edgePoint f) i‖^2)=
      ∑i : Fin r, ((edgeDigits e i:ℝ)+edgeDigits f i-2*edgeDigits (e∩f) i) := by
    apply Finset.sum_congr rfl
    intro i hi
    simp only [PiLp.sub_apply,edgePoint_apply,Real.norm_eq_abs,sq_abs,edgeDigits,
      Finset.mem_inter]
    by_cases hie : i∈e <;> by_cases hif : i∈f <;> norm_num [hie,hif]
  rw [he]
  simp only [Finset.sum_sub_distrib,Finset.sum_add_distrib,← Finset.mul_sum,sum_edgeDigits]

theorem edge_inter_card {r : ℕ} (e f : Finset (Fin r))
    (he : e.card=2) (hf : f.card=2) (hne : e≠f) : (e∩f).card ≤ 1 := by
  have hle := Finset.card_le_card (Finset.inter_subset_left : e∩f⊆e)
  by_contra hn
  have hh : (e∩f).card=2 := by omega
  have he' : e∩f=e := Finset.eq_of_subset_of_card_le Finset.inter_subset_left (by omega)
  have hf' : e∩f=f := Finset.eq_of_subset_of_card_le Finset.inter_subset_right (by omega)
  exact hne (he'.symm.trans hf')

theorem edgePoint_two_distances {r : ℕ} (e f : Finset (Fin r))
    (he : e.card=2) (hf : f.card=2) (hne : e≠f) :
    ‖edgePoint e-edgePoint f‖^2=if Disjoint e f then 4 else 2 := by
  classical
  have hi := edge_inter_card e f he hf hne
  rw [edgePoint_distance,he,hf]
  by_cases hd : Disjoint e f
  · rw [if_pos hd,Finset.disjoint_iff_inter_eq_empty.mp hd]
    norm_num
  · have hn : (e∩f).Nonempty := Finset.not_disjoint_iff_nonempty_inter.mp hd
    have hc : (e∩f).card=1 := by have := Finset.card_pos.mpr hn; omega
    rw [if_neg hd,hc]
    norm_num

noncomputable def graphEmbedding (r : ℕ) (x : ℤ) : EuclideanSpace ℝ (Fin r) := edgePoint (@decode r x)

theorem graphEmbedding_mark {r : ℕ} (e : Finset (Fin r)) : graphEmbedding r (mark e)=edgePoint e := by
  simp [graphEmbedding,decode_mark]

theorem graphEmbedding_injective {r : ℕ} (edges : Finset (Finset (Fin r))) :
    Set.InjOn (graphEmbedding r) (↑(graphSource edges):Set ℤ) := by
  intro x hx y hy he
  obtain ⟨e,he',rfl⟩ := Finset.mem_image.mp hx
  obtain ⟨f,hf',rfl⟩ := Finset.mem_image.mp hy
  simp only [graphEmbedding_mark] at he
  exact congrArg mark (edgePoint_injective he)

theorem graphEmbedding_pair_fidelity {r : ℕ} (edges : Finset (Finset (Fin r)))
    (x y u v : ℤ) (hx : x∈graphSource edges) (hy : y∈graphSource edges)
    (hu : u∈graphSource edges) (hv : v∈graphSource edges) :
    x+y=u+v ↔ graphEmbedding r x+graphEmbedding r y=graphEmbedding r u+graphEmbedding r v := by
  obtain ⟨e,he',rfl⟩ := Finset.mem_image.mp hx
  obtain ⟨f,hf',rfl⟩ := Finset.mem_image.mp hy
  obtain ⟨g,hg',rfl⟩ := Finset.mem_image.mp hu
  obtain ⟨h,hh',rfl⟩ := Finset.mem_image.mp hv
  simpa only [graphEmbedding_mark] using edgePoint_pair_fidelity e f g h

theorem graphEmbedding_two_distances {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) (x y : ℤ) (hx : x∈graphSource edges)
    (hy : y∈graphSource edges) (hne : x≠y) :
    ‖graphEmbedding r x-graphEmbedding r y‖^2=2 ∨
      ‖graphEmbedding r x-graphEmbedding r y‖^2=4 := by
  obtain ⟨e,he,rfl⟩ := Finset.mem_image.mp hx
  obtain ⟨f,hf,rfl⟩ := Finset.mem_image.mp hy
  have hef : e≠f := fun h => hne (congrArg mark h)
  simp only [graphEmbedding_mark]
  rw [edgePoint_two_distances e f (hedges e he) (hedges f hf) hef]
  split_ifs <;> simp

end EnergyForcing.GraphSources
