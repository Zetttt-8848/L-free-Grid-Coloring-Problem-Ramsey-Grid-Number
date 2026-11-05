import CompleteGraphCounts

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators
open EnergyForcing.Counting

 theorem cycleShape_mem {r : ℕ} (edges : Finset (Finset (Fin r)))
    (C : Finset (Finset (Finset (Fin r)))) (hC : CycleShape edges C) : C∈graphCycles edges := by
  classical
  obtain ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩ := hC
  have hP := canonical_pairing_mem a b c d hab hac had hbc hbd hcd
  have hQ : ({{a,c},{b,d}}:Finset (Finset (Fin r)))∈pairings {a,b,c,d} := by
    rw [pairings_four a b c d hab hac had hbc hbd hcd]
    simp
  have h4 : ({a,b,c,d}:Finset (Fin r)).card=4 := by simp [hab,hac,had,hbc,hbd,hcd]
  have habac : ({a,b}:Finset (Fin r))≠{a,c} := by
    simpa only [Finset.pair_comm b a] using pair_ne_of_left_ne b a a c hab.symm hbc
  have habbd := pair_ne_of_left_ne a b b d hab had
  have hPQ := pair_ne_of_left_ne ({a,b}:Finset (Fin r)) {c,d} {a,c} {b,d} habac habbd
  apply Finset.mem_filter.mpr
  constructor
  · apply Finset.mem_powersetCard.mpr
    refine ⟨?_,by simp [hPQ]⟩
    intro P hPC
    simp only [Finset.mem_insert,Finset.mem_singleton] at hPC
    rcases hPC with rfl | rfl
    · exact Finset.mem_powersetCard.mpr ⟨by simpa only [Finset.subset_iff,Finset.mem_insert,Finset.mem_singleton,or_imp,forall_and,forall_eq] using And.intro he hf, pairing_card _ _ hP⟩
    · exact Finset.mem_powersetCard.mpr ⟨by simpa only [Finset.subset_iff,Finset.mem_insert,Finset.mem_singleton,or_imp,forall_and,forall_eq] using And.intro hg hh, pairing_card _ _ hQ⟩
  · intro P hPC Q hQC
    have hsub : ({{{a,b},{c,d}},{{a,c},{b,d}}}:Finset (Finset (Finset (Fin r))))⊆pairings {a,b,c,d} := by
      intro R hR
      simp only [Finset.mem_insert,Finset.mem_singleton] at hR
      rcases hR with rfl | rfl
      · exact hP
      · exact hQ
    exact pairing_degree _ h4 P Q (hsub hPC) (hsub hQC)

 theorem graphCycle_pair_four {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges,e.card=2) (C : Finset (Finset (Finset (Fin r))))
    (hC : C∈graphCycles edges) (P : Finset (Finset (Fin r))) (hP : P∈C) :
    (P.biUnion id).card=4 := by
  obtain ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩ := graphCycles_shape edges hedges C hC
  simp only [Finset.mem_insert,Finset.mem_singleton] at hP
  rcases hP with rfl | rfl <;>
    simp [Finset.biUnion_insert,Finset.singleton_biUnion,hab,hac,had,hbc,hbd,hcd,
      hab.symm,hac.symm,had.symm,hbc.symm,hbd.symm,hcd.symm]

 theorem cycle_matching_unique {r : ℕ} (a b c d : Fin r) (e f : Finset (Fin r))
    (he : e∈({{a,b},{c,d},{a,c},{b,d}}:Finset (Finset (Fin r))))
    (hf : f∈({{a,b},{c,d},{a,c},{b,d}}:Finset (Finset (Fin r))))
    (hd : Disjoint e f) :
    ({e,f}:Finset (Finset (Fin r)))={{a,b},{c,d}} ∨ ({e,f}:Finset (Finset (Fin r)))={{a,c},{b,d}} := by
  simp only [Finset.mem_insert,Finset.mem_singleton] at he hf
  rcases he with rfl | rfl | rfl | rfl <;>
    rcases hf with rfl | rfl | rfl | rfl <;>
    simp_all [Finset.disjoint_left,Finset.pair_comm]

/-- Forgetting alternating-edge labels does not identify distinct cycles. -/
theorem graphCycles_union_injective {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges,e.card=2) :
    Set.InjOn (fun C : Finset (Finset (Finset (Fin r))) => C.biUnion id) (↑(graphCycles edges)) := by
  classical
  intro C hC D hD hCD
  dsimp at hCD
  have hc := (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hC).1).2
  have hd := (Finset.mem_powersetCard.mp (Finset.mem_filter.mp hD).1).2
  apply Eq.symm
  apply Finset.eq_of_subset_of_card_le _ (by omega)
  obtain ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩ := graphCycles_shape edges hedges C hC
  intro P hP
  have hp := Finset.mem_powersetCard.mp ((Finset.mem_powersetCard.mp (Finset.mem_filter.mp hD).1).1 hP)
  obtain ⟨e,f,hef,rfl⟩ := Finset.card_eq_two.mp hp.2
  have heE := hp.1 (by simp : e∈({e,f}:Finset (Finset (Fin r))))
  have hfE := hp.1 (by simp : f∈({e,f}:Finset (Finset (Fin r))))
  have h4 := graphCycle_pair_four edges hedges D hD {e,f} hP
  simp only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq] at h4
  have hi := Finset.card_union_add_card_inter e f
  rw [h4,hedges e heE,hedges f hfE] at hi
  have hdis : Disjoint e f := Finset.disjoint_iff_inter_eq_empty.mpr (Finset.card_eq_zero.mp (by omega))
  have heU : e∈D.biUnion id := Finset.mem_biUnion.mpr ⟨{e,f},hP,by simp⟩
  have hfU : f∈D.biUnion id := Finset.mem_biUnion.mpr ⟨{e,f},hP,by simp⟩
  rw [← hCD] at heU hfU
  have hu : ({{{a,b},{c,d}},{{a,c},{b,d}}}:Finset (Finset (Finset (Fin r)))).biUnion id=
      {{a,b},{c,d},{a,c},{b,d}} := by
    ext x
    simp [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq,or_assoc,or_comm,or_left_comm]
  rw [hu] at heU hfU
  have hp := cycle_matching_unique a b c d e f heU hfU hdis
  simpa only [Finset.mem_insert,Finset.mem_singleton] using hp

noncomputable def simpleFourCycles {r : ℕ} (edges : Finset (Finset (Fin r))) :=
  (graphCycles edges).image (fun C => C.biUnion id)

 theorem simpleFourCycles_card {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges,e.card=2) : (simpleFourCycles edges).card=(graphCycles edges).card :=
  Finset.card_image_of_injOn (graphCycles_union_injective edges hedges)

 theorem graph_source_four_cycles {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges,e.card=2) :
    T (graphSource edges)=2*(simpleFourCycles edges).card ∧
    E (graphSource edges)=2*edges.card^2-edges.card+8*(simpleFourCycles edges).card := by
  rw [simpleFourCycles_card edges hedges]
  exact ⟨graphSource_corner_count edges,graphSource_energy_count edges⟩

end EnergyForcing.GraphSources

namespace EnergyForcing.GraphSources
open Finset

/-- Literal simple four-cycle edge sets; additional graph edges do not matter. -/
theorem mem_simpleFourCycles_iff {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges,e.card=2) (U : Finset (Finset (Fin r))) :
    U∈simpleFourCycles edges ↔
      ∃a b c d : Fin r, a≠b ∧ a≠c ∧ a≠d ∧ b≠c ∧ b≠d ∧ c≠d ∧
        {a,b}∈edges ∧ {c,d}∈edges ∧ {a,c}∈edges ∧ {b,d}∈edges ∧
        U={{a,b},{c,d},{a,c},{b,d}} := by
  classical
  constructor
  · intro hU
    obtain ⟨C,hC,rfl⟩ := Finset.mem_image.mp hU
    obtain ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩ := graphCycles_shape edges hedges C hC
    refine ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,?_⟩
    ext e
    simp [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq,or_assoc,or_comm,or_left_comm]
  · rintro ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩
    apply Finset.mem_image.mpr
    refine ⟨{{{a,b},{c,d}},{{a,c},{b,d}}},?_,?_⟩
    · exact cycleShape_mem edges _ ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hg,hh,rfl⟩
    · ext e
      simp [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq,or_assoc,or_comm,or_left_comm]

end EnergyForcing.GraphSources


