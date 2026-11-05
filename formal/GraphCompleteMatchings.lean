import GraphCycles

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators

 theorem degree_of_disjoint_union {r : ℕ} (e f g h : Finset (Fin r))
    (hef : Disjoint e f) (hgh : Disjoint g h) (hu : e∪f=g∪h) :
    ∀i, edgeDigits e i+edgeDigits f i=edgeDigits g i+edgeDigits h i := by
  intro i
  have hu' : i∈e∪f ↔ i∈g∪h := by rw [hu]
  have h₁ := Finset.disjoint_left.mp hef
  have h₂ := Finset.disjoint_left.mp hgh
  simp only [Finset.mem_union] at hu'
  by_cases he : i∈e <;> by_cases hf : i∈f <;>
    by_cases hg : i∈g <;> by_cases hh : i∈h <;> simp_all [edgeDigits]

 def pairings {r : ℕ} (S : Finset (Fin r)) :=
  ((S.powersetCard 2).powersetCard 2).filter (fun P => P.biUnion id=S)

 theorem four_set_labels {r : ℕ} (S : Finset (Fin r)) (hS : S.card=4) :
    ∃a b c d : Fin r, a≠b ∧ a≠c ∧ a≠d ∧ b≠c ∧ b≠d ∧ c≠d ∧ S={a,b,c,d} := by
  obtain ⟨a,U,ha,hU,hUc⟩ := Finset.card_eq_succ.mp hS
  obtain ⟨b,V,hb,hV,hVc⟩ := Finset.card_eq_succ.mp hUc
  obtain ⟨c,d,hcd,hW⟩ := Finset.card_eq_two.mp hVc
  subst S; subst U; subst V
  simp only [Finset.mem_insert,Finset.mem_singleton,not_or] at ha hb
  exact ⟨a,b,c,d,ha.1,ha.2.1,ha.2.2,hb.1,hb.2,hcd,rfl⟩

 theorem canonical_pairing_mem {r : ℕ} (a b c d : Fin r)
    (hab : a≠b) (hac : a≠c) (had : a≠d) (hbc : b≠c) (hbd : b≠d) (hcd : c≠d) :
    ({{a,b},{c,d}} : Finset (Finset (Fin r)))∈pairings {a,b,c,d} := by
  have hne : ({a,b}:Finset (Fin r))≠{c,d} := by
    intro he
    have ha : a∈({c,d}:Finset (Fin r)) := by rw [← he]; simp
    simp [hac,had] at ha
  apply Finset.mem_filter.mpr
  constructor
  · apply Finset.mem_powersetCard.mpr
    refine ⟨?_,by simp [hne]⟩
    intro e he
    simp only [Finset.mem_insert,Finset.mem_singleton] at he
    rcases he with rfl | rfl
    · simp [Finset.mem_powersetCard,Finset.subset_iff,hab]
    · simp [Finset.mem_powersetCard,Finset.subset_iff,hcd]
  · ext i
    simp [or_assoc,or_comm,or_left_comm]

 theorem pairings_four {r : ℕ} (a b c d : Fin r)
    (hab : a≠b) (hac : a≠c) (had : a≠d) (hbc : b≠c) (hbd : b≠d) (hcd : c≠d) :
    pairings {a,b,c,d}={{{a,b},{c,d}},{{a,c},{b,d}},{{a,d},{b,c}}} := by
  ext P
  constructor
  · intro hP
    rcases Finset.mem_filter.mp hP with ⟨hP,hunion⟩
    rcases Finset.mem_powersetCard.mp hP with ⟨hsub,hcard⟩
    obtain ⟨e,f,hef,rfl⟩ := Finset.card_eq_two.mp hcard
    have he := Finset.mem_powersetCard.mp (hsub (by simp : e∈({e,f}:Finset (Finset (Fin r)))))
    have hf := Finset.mem_powersetCard.mp (hsub (by simp : f∈({e,f}:Finset (Finset (Fin r)))))
    have hun : e∪f={a,b,c,d} := by simpa only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq] using hunion
    have hun4 : (e∪f).card=4 := by rw [hun]; simp [hab,hac,had,hbc,hbd,hcd]
    have hci := Finset.card_union_add_card_inter e f
    rw [hun4,he.2,hf.2] at hci
    have hdis : Disjoint e f := Finset.disjoint_iff_inter_eq_empty.mpr (Finset.card_eq_zero.mp (by omega))
    have href : Disjoint ({a,b}:Finset (Fin r)) {c,d} := by
      simp [Finset.disjoint_left,hac,had,hbc,hbd]
    have hu : ({a,b}:Finset (Fin r))∪{c,d}=e∪f := by rw [hun]; ext i; simp [or_assoc,or_comm,or_left_comm]
    exact matching_on_four a b c d hab hac had hbc hbd hcd e f he.2 hf.2
      ((pair_sum_fidelity _ _ _ _).mpr (degree_of_disjoint_union _ _ _ _ href hdis hu))
  · intro hP
    simp only [Finset.mem_insert,Finset.mem_singleton] at hP
    rcases hP with rfl | rfl | rfl
    · exact canonical_pairing_mem a b c d hab hac had hbc hbd hcd
    · have hh := canonical_pairing_mem a c b d hac hab had hbc.symm hcd hbd
      have hs : ({a,c,b,d}:Finset (Fin r))={a,b,c,d} := by
        ext i; simp only [Finset.mem_insert,Finset.mem_singleton,or_assoc,or_comm,or_left_comm]
      rw [hs] at hh
      exact hh
    · have hh := canonical_pairing_mem a d b c had hab hac hbd.symm hcd.symm hbc
      have hs : ({a,d,b,c}:Finset (Fin r))={a,b,c,d} := by
        ext i; simp only [Finset.mem_insert,Finset.mem_singleton,or_assoc,or_comm,or_left_comm]
      rw [hs] at hh
      exact hh

 theorem pair_ne_of_left_ne {α : Type*} [DecidableEq α] (a b c d : α)
    (hac : a≠c) (had : a≠d) : ({a,b}:Finset α)≠{c,d} := by
  intro he
  have hh : a∈({c,d}:Finset α) := by rw [← he]; simp
  simp [hac,had] at hh

 theorem pairings_card {r : ℕ} (S : Finset (Fin r)) (hS : S.card=4) : (pairings S).card=3 := by
  obtain ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,rfl⟩ := four_set_labels S hS
  rw [pairings_four a b c d hab hac had hbc hbd hcd]
  have habac : ({a,b}:Finset (Fin r))≠{a,c} := by
    simpa only [Finset.pair_comm b a] using pair_ne_of_left_ne b a a c hab.symm hbc
  have habbd := pair_ne_of_left_ne a b b d hab had
  have habad : ({a,b}:Finset (Fin r))≠{a,d} := by
    simpa only [Finset.pair_comm b a] using pair_ne_of_left_ne b a a d hab.symm hbd
  have habbc := pair_ne_of_left_ne a b b c hab hac
  have hacad : ({a,c}:Finset (Fin r))≠{a,d} := by
    simpa only [Finset.pair_comm c a] using pair_ne_of_left_ne c a a d hac.symm hcd
  have hacbc := pair_ne_of_left_ne a c b c hab hac
  have h01 := pair_ne_of_left_ne ({a,b}:Finset (Fin r)) {c,d} {a,c} {b,d} habac habbd
  have h02 := pair_ne_of_left_ne ({a,b}:Finset (Fin r)) {c,d} {a,d} {b,c} habad habbc
  have h12 := pair_ne_of_left_ne ({a,c}:Finset (Fin r)) {b,d} {a,d} {b,c} hacad hacbc
  simp [h01,h02,h12]

end EnergyForcing.GraphSources


