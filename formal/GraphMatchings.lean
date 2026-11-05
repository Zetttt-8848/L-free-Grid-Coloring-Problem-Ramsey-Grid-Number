import GraphSourceColoring
import SourcePairCollisions

set_option autoImplicit false

namespace EnergyForcing.GraphSources

open Finset
open scoped BigOperators
open EnergyForcing.PairCollisions

/-- An edge pair on four distinct vertices has one of the three perfect-matching forms. -/
theorem matching_with_vertex {r : ℕ} (a b c d : Fin r)
    (hab : a≠b) (hac : a≠c) (had : a≠d) (hbc : b≠c) (hbd : b≠d) (hcd : c≠d)
    (g h : Finset (Fin r)) (hg : g.card=2) (hh : h.card=2) (ha : a∈g)
    (he : mark {a,b}+mark {c,d}=mark g+mark h) :
    (g={a,b} ∧ h={c,d}) ∨ (g={a,c} ∧ h={b,d}) ∨ (g={a,d} ∧ h={b,c}) := by
  obtain ⟨u,hau,rfl⟩ := edge_with_vertex g hg a ha
  have hu : u∈({a,b}:Finset (Fin r))∪{c,d} := by
    rw [(degree_union_inter {a,b} {c,d} {a,u} h ((pair_sum_fidelity _ _ _ _).mp he)).1]
    simp
  simp only [Finset.mem_union,Finset.mem_insert,Finset.mem_singleton] at hu
  rcases hu with (hua | hub) | huc | hud
  · exact False.elim (hau hua.symm)
  · subst u
    left
    refine ⟨rfl,mark_injective (by omega)⟩
  · subst u
    right; left
    refine ⟨rfl,mark_injective ?_⟩
    rw [mark_pair a b hab,mark_pair c d hcd,mark_pair a c hac] at he
    rw [mark_pair b d hbd]
    omega
  · subst u
    right; right
    refine ⟨rfl,mark_injective ?_⟩
    rw [mark_pair a b hab,mark_pair c d hcd,mark_pair a d had] at he
    rw [mark_pair b c hbc]
    omega

theorem matching_on_four {r : ℕ} (a b c d : Fin r)
    (hab : a≠b) (hac : a≠c) (had : a≠d) (hbc : b≠c) (hbd : b≠d) (hcd : c≠d)
    (g h : Finset (Fin r)) (hg : g.card=2) (hh : h.card=2)
    (he : mark {a,b}+mark {c,d}=mark g+mark h) :
    ({g,h}:Finset (Finset (Fin r)))∈
      ({{{a,b},{c,d}},{{a,c},{b,d}},{{a,d},{b,c}}} : Finset (Finset (Finset (Fin r)))) := by
  have ha : a∈g ∨ a∈h := by
    have hu := (degree_union_inter {a,b} {c,d} g h ((pair_sum_fidelity _ _ _ _).mp he)).1
    have ha : a∈g∪h := by rw [← hu]; simp
    exact Finset.mem_union.mp ha
  rcases ha with ha | ha
  · rcases matching_with_vertex a b c d hab hac had hbc hbd hcd g h hg hh ha he with
      ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ <;> simp
  · have he' : mark {a,b}+mark {c,d}=mark h+mark g := by omega
    rcases matching_with_vertex a b c d hab hac had hbc hbd hcd h g hh hg ha he' with
      ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ <;> simp [Finset.pair_comm]

end EnergyForcing.GraphSources


namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators
open EnergyForcing.PairCollisions
open EnergyForcing.Counting

theorem sumPair_representation {r : ℕ} (edges : Finset (Finset (Fin r)))
    (s : ℤ) (P : Finset ℤ) (hP : P∈sumPairs (graphSource edges) s) :
    ∃e∈edges, ∃f∈edges, e≠f ∧ P={mark e,mark f} ∧ mark e+mark f=s := by
  rcases Finset.mem_filter.mp hP with ⟨hP,hs⟩
  rcases Finset.mem_powersetCard.mp hP with ⟨hsub,hcard⟩
  obtain ⟨x,y,hxy,rfl⟩ := Finset.card_eq_two.mp hcard
  obtain ⟨e,he,rfl⟩ := Finset.mem_image.mp (hsub (by simp : x∈({x,y}:Finset ℤ)))
  obtain ⟨f,hf,rfl⟩ := Finset.mem_image.mp (hsub (by simp : y∈({mark e,y}:Finset ℤ)))
  refine ⟨e,he,f,hf,?_,rfl,?_⟩
  · intro heq; subst f; exact hxy rfl
  · simpa [hxy] using hs

theorem graph_sumPairs_card_le_three {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) (s : ℤ) :
    (sumPairs (graphSource edges) s).card ≤ 3 := by
  by_cases hn : (sumPairs (graphSource edges) s).Nonempty
  · obtain ⟨P,hP⟩ := hn
    obtain ⟨e,he,f,hf,hef,rfl,hs⟩ := sumPair_representation edges s P hP
    by_cases hd : Disjoint e f
    · obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp (hedges e he)
      obtain ⟨c,d,hcd,rfl⟩ := Finset.card_eq_two.mp (hedges f hf)
      have hac : a≠c := by intro hh; subst c; exact (Finset.disjoint_left.mp hd) (show a∈({a,b}:Finset (Fin r)) by simp) (by simp)
      have had : a≠d := by intro hh; subst d; exact (Finset.disjoint_left.mp hd) (show a∈({a,b}:Finset (Fin r)) by simp) (by simp)
      have hbc : b≠c := by intro hh; subst c; exact (Finset.disjoint_left.mp hd) (show b∈({a,b}:Finset (Fin r)) by simp) (by simp)
      have hbd : b≠d := by intro hh; subst d; exact (Finset.disjoint_left.mp hd) (show b∈({a,b}:Finset (Fin r)) by simp) (by simp)
      have hsub : sumPairs (graphSource edges) s ⊆
          {{mark {a,b},mark {c,d}},{mark {a,c},mark {b,d}},{mark {a,d},mark {b,c}}} := by
        intro Q hQ
        obtain ⟨g,hg,h,hh,hgh,rfl,hs'⟩ := sumPair_representation edges s Q hQ
        have hc := matching_on_four a b c d hab hac had hbc hbd hcd g h
          (hedges g hg) (hedges h hh) (by omega)
        simp only [Finset.mem_insert,Finset.mem_singleton] at hc
        rcases hc with hc | hc | hc
        all_goals have hh := congrArg (Finset.image (@mark r)) hc
        all_goals simp only [Finset.image_insert,Finset.image_singleton] at hh
        all_goals rw [hh]; simp
      exact (Finset.card_le_card hsub).trans Finset.card_le_three
    · have hsub : sumPairs (graphSource edges) s ⊆ {{mark e,mark f}} := by
        intro Q hQ
        obtain ⟨g,hg,h,hh,hgh,rfl,hs'⟩ := sumPair_representation edges s Q hQ
        have hc := intersecting_pair_unique e f g h (hedges e he) (hedges f hf)
          (hedges g hg) (hedges h hh) ((pair_sum_fidelity _ _ _ _).mp (by omega))
          (Finset.not_disjoint_iff_nonempty_inter.mp hd)
        rcases hc with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ <;> simp [Finset.pair_comm]
      exact (Finset.card_le_card hsub).trans (by simp)
  · rw [Finset.not_nonempty_iff_eq_empty.mp hn]
    simp

theorem graphSource_corner_bound {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) : T (graphSource edges) ≤ 2*M (graphSource edges) := by
  apply pair_sum_cap_bound
  · intro a ha b hb c hc he
    exact (graphSource_no_progression edges a b c ha hb hc he).1
  · exact graph_sumPairs_card_le_three edges hedges

theorem graphSource_span_bound {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) : (M (graphSource edges):ℝ) ≤ 5*span (graphSource edges) := by
  have hh := span_pair_bound (graphSource edges) 2 (by norm_num)
    (by exact_mod_cast graphSource_corner_bound edges hedges)
  norm_num at hh ⊢
  exact hh

end EnergyForcing.GraphSources

