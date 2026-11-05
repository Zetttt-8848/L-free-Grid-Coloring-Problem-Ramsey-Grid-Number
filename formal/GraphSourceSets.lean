import GraphSourceDigits

set_option autoImplicit false

namespace EnergyForcing.GraphSources

open Finset
open scoped BigOperators

theorem degree_union_inter {r : ℕ} (e f g h : Finset (Fin r))
    (he : ∀i, edgeDigits e i+edgeDigits f i=edgeDigits g i+edgeDigits h i) :
    e∪f=g∪h ∧ e∩f=g∩h := by
  constructor
  all_goals
    ext i
    have hi := he i
    simp only [edgeDigits] at hi
    by_cases hie : i∈e <;> by_cases hif : i∈f <;>
      by_cases hig : i∈g <;> by_cases hih : i∈h <;> simp_all

theorem repeated_pair_unique {r : ℕ} (e f g : Finset (Fin r))
    (he : ∀i, edgeDigits e i+edgeDigits e i=edgeDigits f i+edgeDigits g i) :
    e=f ∧ e=g := by
  constructor
  all_goals
    ext i
    have hi := he i
    simp only [edgeDigits] at hi
    by_cases hie : i∈e <;> by_cases hif : i∈f <;> by_cases hig : i∈g <;> simp_all

theorem edge_with_vertex {r : ℕ} (e : Finset (Fin r)) (he : e.card=2)
    (a : Fin r) (ha : a∈e) : ∃b, a≠b ∧ e={a,b} := by
  obtain ⟨u,v,huv,rfl⟩ := Finset.card_eq_two.mp he
  simp only [Finset.mem_insert,Finset.mem_singleton] at ha
  rcases ha with rfl | rfl
  · exact ⟨v,huv,rfl⟩
  · exact ⟨u,huv.symm,by simp [Finset.pair_comm]⟩

theorem star_digits {r : ℕ} (a b i : Fin r) (hab : a≠b) :
    edgeDigits {a,b} i=(if i=a then 1 else 0)+(if i=b then 1 else 0) := by
  by_cases hia : i=a <;> by_cases hib : i=b <;> simp_all [edgeDigits]

theorem two_singleton_counts {r : ℕ} (b c d e : Fin r)
    (he : ∀i, (if i=b then (1:ℕ) else 0)+(if i=c then 1 else 0)=
      (if i=d then 1 else 0)+(if i=e then 1 else 0)) :
    (b=d ∧ c=e) ∨ (b=e ∧ c=d) := by
  have hb : b=d ∨ b=e := by
    by_contra hh
    have hbd : b≠d := by tauto
    have hbe : b≠e := by tauto
    have h := he b
    simp only [if_pos rfl,if_neg hbd,if_neg hbe,ite_true,zero_add] at h
    omega
  rcases hb with rfl | rfl
  · left
    refine ⟨rfl,?_⟩
    have hh := Nat.add_left_cancel (he c)
    by_cases hce : c=e
    · exact hce
    · simp [hce] at hh
  · right
    refine ⟨rfl,?_⟩
    have hh := he c
    by_cases hcd : c=d
    · exact hcd
    · simp only [if_pos rfl,if_neg hcd,ite_true,zero_add] at hh
      omega

/-- With a common vertex, a sum of two edges has a unique unordered representation. -/
theorem intersecting_pair_unique {r : ℕ} (e f g h : Finset (Fin r))
    (he : e.card=2) (hf : f.card=2) (hg : g.card=2) (hh : h.card=2)
    (hdeg : ∀i, edgeDigits e i+edgeDigits f i=edgeDigits g i+edgeDigits h i)
    (hne : (e∩f).Nonempty) : (e=g ∧ f=h) ∨ (e=h ∧ f=g) := by
  obtain ⟨a,ha⟩ := hne
  have hu := degree_union_inter e f g h hdeg
  have ha' : a∈g∩h := by rw [← hu.2]; exact ha
  obtain ⟨b,hab,rfl⟩ := edge_with_vertex e he a (Finset.mem_inter.mp ha).1
  obtain ⟨c,hac,rfl⟩ := edge_with_vertex f hf a (Finset.mem_inter.mp ha).2
  obtain ⟨d,had,rfl⟩ := edge_with_vertex g hg a (Finset.mem_inter.mp ha').1
  obtain ⟨v,hav,rfl⟩ := edge_with_vertex h hh a (Finset.mem_inter.mp ha').2
  have ht : ∀i, (if i=b then (1:ℕ) else 0)+(if i=c then 1 else 0)=
      (if i=d then 1 else 0)+(if i=v then 1 else 0) := by
    intro i
    have hi := hdeg i
    rw [star_digits a b i hab,star_digits a c i hac,
      star_digits a d i had,star_digits a v i hav] at hi
    omega
  rcases two_singleton_counts b c d v ht with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩
  · exact Or.inl ⟨rfl,rfl⟩
  · exact Or.inr ⟨rfl,rfl⟩

/-- Every nontrivial collision consists of two perfect matchings on one four-set. -/
theorem nontrivial_pair_disjoint {r : ℕ} (e f g h : Finset (Fin r))
    (he : e.card=2) (hf : f.card=2) (hg : g.card=2) (hh : h.card=2)
    (hdeg : ∀i, edgeDigits e i+edgeDigits f i=edgeDigits g i+edgeDigits h i)
    (hneg : e≠g) (hneh : e≠h) : Disjoint e f ∧ Disjoint g h := by
  have hdis : Disjoint e f := by
    by_contra hn
    have hne : (e∩f).Nonempty := Finset.not_disjoint_iff_nonempty_inter.mp hn
    rcases intersecting_pair_unique e f g h he hf hg hh hdeg hne with heq | heq
    · exact hneg heq.1
    · exact hneh heq.1
  have hu := degree_union_inter e f g h hdeg
  constructor
  · exact hdis
  · apply Finset.disjoint_iff_inter_eq_empty.mpr
    rw [← hu.2,Finset.disjoint_iff_inter_eq_empty.mp hdis]

theorem cross_pair_not_disjoint {r : ℕ} (e f g h : Finset (Fin r))
    (he : e.card=2) (hg : g.card=2)
    (hdeg : ∀i, edgeDigits e i+edgeDigits f i=edgeDigits g i+edgeDigits h i)
    (hneg : e≠g) : ¬ Disjoint e h := by
  intro hdis
  have hunion := (degree_union_inter e f g h hdeg).1
  have hsub : e⊆g := by
    intro i hi
    have hu : i∈g∪h := by rw [← hunion]; exact Finset.mem_union_left _ hi
    rcases Finset.mem_union.mp hu with hg | hh
    · exact hg
    · exact False.elim (Finset.disjoint_left.mp hdis hi hh)
  exact hneg (Finset.eq_of_subset_of_card_le hsub (by omega))

end EnergyForcing.GraphSources
