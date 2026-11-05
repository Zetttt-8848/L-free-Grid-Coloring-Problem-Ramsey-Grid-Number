import GraphCompleteMatchings

set_option autoImplicit false

namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators
open EnergyForcing.Counting

def completeEdges (r : ℕ) : Finset (Finset (Fin r)) := Finset.univ.powersetCard 2

theorem completeEdges_card (r : ℕ) : (completeEdges r).card=r.choose 2 := by
  simp [completeEdges]

theorem completeEdges_edge_card {r : ℕ} (e : Finset (Fin r)) (he : e∈completeEdges r) : e.card=2 :=
  (Finset.mem_powersetCard.mp he).2

theorem pairing_card {r : ℕ} (S : Finset (Fin r)) (P : Finset (Finset (Fin r)))
    (hP : P∈pairings S) : P.card=2 :=
  (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hP).1).2

theorem pairing_union {r : ℕ} (S : Finset (Fin r)) (P : Finset (Finset (Fin r)))
    (hP : P∈pairings S) : P.biUnion id=S := (Finset.mem_filter.mp hP).2

theorem pairing_complete {r : ℕ} (S : Finset (Fin r)) (P : Finset (Finset (Fin r)))
    (hP : P∈pairings S) : P∈(completeEdges r).powersetCard 2 := by
  have h := Finset.mem_powersetCard.mp (Finset.mem_filter.mp hP).1
  apply Finset.mem_powersetCard.mpr
  refine ⟨?_,h.2⟩
  intro e he
  exact Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _,(Finset.mem_powersetCard.mp (h.1 he)).2⟩

theorem pairing_degree {r : ℕ} (S : Finset (Fin r)) (hS : S.card=4)
    (P Q : Finset (Finset (Fin r))) (hP : P∈pairings S) (hQ : Q∈pairings S) :
    pairDegreeEqual P Q := by
  have hp := Finset.mem_powersetCard.mp (Finset.mem_filter.mp hP).1
  have hq := Finset.mem_powersetCard.mp (Finset.mem_filter.mp hQ).1
  obtain ⟨e,f,hef,rfl⟩ := Finset.card_eq_two.mp hp.2
  obtain ⟨g,h,hgh,rfl⟩ := Finset.card_eq_two.mp hq.2
  have he := (Finset.mem_powersetCard.mp (hp.1 (by simp : e∈({e,f}:Finset (Finset (Fin r)))))).2
  have hf := (Finset.mem_powersetCard.mp (hp.1 (by simp : f∈({e,f}:Finset (Finset (Fin r)))))).2
  have hg := (Finset.mem_powersetCard.mp (hq.1 (by simp : g∈({g,h}:Finset (Finset (Fin r)))))).2
  have hh := (Finset.mem_powersetCard.mp (hq.1 (by simp : h∈({g,h}:Finset (Finset (Fin r)))))).2
  have hu₁ : e∪f=S := by simpa only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq] using pairing_union S _ hP
  have hu₂ : g∪h=S := by simpa only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq] using pairing_union S _ hQ
  have hi₁ := Finset.card_union_add_card_inter e f
  have hi₂ := Finset.card_union_add_card_inter g h
  rw [hu₁,hS,he,hf] at hi₁
  rw [hu₂,hS,hg,hh] at hi₂
  have hd₁ : Disjoint e f := Finset.disjoint_iff_inter_eq_empty.mpr (Finset.card_eq_zero.mp (by omega))
  have hd₂ : Disjoint g h := Finset.disjoint_iff_inter_eq_empty.mpr (Finset.card_eq_zero.mp (by omega))
  simp only [pairDegreeEqual,Finset.sum_pair hef,Finset.sum_pair hgh]
  exact degree_of_disjoint_union e f g h hd₁ hd₂ (hu₁.trans hu₂.symm)

theorem complete_cycles_union (r : ℕ) : graphCycles (completeEdges r)=
    (Finset.univ.powersetCard 4).biUnion (fun S : Finset (Fin r) => (pairings S).powersetCard 2) := by
  classical
  ext C
  constructor
  · intro hC
    obtain ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩ :=
      graphCycles_shape (completeEdges r) (fun e he => completeEdges_edge_card e he) C hC
    apply Finset.mem_biUnion.mpr
    refine ⟨{a,b,c,d},?_,?_⟩
    · simp [Finset.mem_powersetCard,hab,hac,had,hbc,hbd,hcd]
    · apply Finset.mem_powersetCard.mpr
      have hc := (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hC).1).2
      refine ⟨?_,hc⟩
      intro P hP
      rw [pairings_four a b c d hab hac had hbc hbd hcd]
      simp only [Finset.mem_insert,Finset.mem_singleton] at hP ⊢
      tauto
  · intro hC
    obtain ⟨S,hS,hC⟩ := Finset.mem_biUnion.mp hC
    have hs := (Finset.mem_powersetCard.mp hS).2
    have hc := Finset.mem_powersetCard.mp hC
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_powersetCard.mpr ⟨?_,hc.2⟩,?_⟩
    · intro P hP
      exact pairing_complete S P (hc.1 hP)
    · intro P hP Q hQ
      exact pairing_degree S hs P Q (hc.1 hP) (hc.1 hQ)

theorem complete_cycles_card (r : ℕ) : (graphCycles (completeEdges r)).card=3*r.choose 4 := by
  classical
  rw [complete_cycles_union]
  have hd : (↑((Finset.univ : Finset (Fin r)).powersetCard 4) : Set (Finset (Fin r))).PairwiseDisjoint
      (fun S => (pairings S).powersetCard 2) := by
    intro S hS U hU hne
    apply Finset.disjoint_left.mpr
    intro C hC hC'
    have hc := Finset.mem_powersetCard.mp hC
    have hc' := Finset.mem_powersetCard.mp hC'
    obtain ⟨P,hP⟩ := Finset.card_pos.mp (by omega : 0<C.card)
    exact hne ((pairing_union S P (hc.1 hP)).symm.trans (pairing_union U P (hc'.1 hP)))
  rw [Finset.card_biUnion hd]
  calc
    _ = ∑S∈Finset.univ.powersetCard 4, 3 := by
      apply Finset.sum_congr rfl
      intro S hS
      rw [Finset.card_powersetCard,pairings_card S (Finset.mem_powersetCard.mp hS).2]
      decide
    _ = _ := by simp [Nat.mul_comm]

 theorem complete_source_card (r : ℕ) : (graphSource (completeEdges r)).card=r.choose 2 := by
  rw [graphSource_card,completeEdges_card]

 theorem complete_source_corners (r : ℕ) : T (graphSource (completeEdges r))=6*r.choose 4 := by
  rw [graphSource_corner_count,complete_cycles_card]
  omega

 theorem complete_source_energy (r : ℕ) : E (graphSource (completeEdges r))=
    2*(r.choose 2)^2-r.choose 2+24*r.choose 4 := by
  rw [graphSource_energy_count,completeEdges_card,complete_cycles_card]
  omega

end EnergyForcing.GraphSources

