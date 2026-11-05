import GraphMatchings

set_option autoImplicit false

namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators
open EnergyForcing.PairCollisions
open EnergyForcing.Counting

theorem powersetCard_image_injective {α β : Type*} [DecidableEq α] [DecidableEq β]
    (f : α→β) (hf : Function.Injective f) (S : Finset α) (n : ℕ) :
    (S.image f).powersetCard n=(S.powersetCard n).image (Finset.image f) := by
  let e : α↪β := ⟨f,hf⟩
  have hh := Finset.powersetCard_map e n S
  have hfun : (⇑(Finset.mapEmbedding e) : Finset α→Finset β)=Finset.image f := by
    funext P
    exact Finset.map_eq_image e P
  simpa only [Finset.map_eq_image,RelEmbedding.coe_toEmbedding,hfun] using hh

theorem collisions_filter (A : Finset ℤ) : collisions A=
    ((A.powersetCard 2).powersetCard 2).filter (fun C =>
      ∀P∈C, ∀Q∈C, (∑x∈P,x)=∑x∈Q,x) := by
  ext C
  simp only [collisions,Finset.mem_filter]
  constructor
  · rintro ⟨hC,h4,he⟩; exact ⟨hC,he⟩
  · rintro ⟨hC,he⟩
    refine ⟨hC,?_,he⟩
    rcases Finset.mem_powersetCard.mp hC with ⟨hsub,hcard⟩
    obtain ⟨P,Q,hPQ,rfl⟩ := Finset.card_eq_two.mp hcard
    have hP := Finset.mem_powersetCard.mp (hsub (by simp : P∈({P,Q}:Finset (Finset ℤ))))
    have hQ := Finset.mem_powersetCard.mp (hsub (by simp : Q∈({P,Q}:Finset (Finset ℤ))))
    have hd := equal_sum_pairs_disjoint P Q hP.2 hQ.2 hPQ (he P (by simp) Q (by simp))
    simp only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq]
    rw [Finset.card_union_of_disjoint hd,hP.2,hQ.2]

def pairDegreeEqual {r : ℕ} (P Q : Finset (Finset (Fin r))) : Prop :=
  ∀i, (∑e∈P,edgeDigits e i)=∑e∈Q,edgeDigits e i

/-- An unoriented four-cycle is encoded by its two alternating perfect matchings.
The degree-equality predicate is entirely on graph edges. -/
noncomputable def graphCycles {r : ℕ} (edges : Finset (Finset (Fin r))) := by
  classical
  exact ((edges.powersetCard 2).powersetCard 2).filter (fun C => ∀P∈C, ∀Q∈C, pairDegreeEqual P Q)

def markPair {r : ℕ} (P : Finset (Finset (Fin r))) : Finset ℤ := P.image mark
def markCycle {r : ℕ} (C : Finset (Finset (Finset (Fin r)))) := C.image markPair

theorem markPair_injective {r : ℕ} : Function.Injective (@markPair r) :=
  Finset.image_injective mark_injective

theorem markCycle_injective {r : ℕ} : Function.Injective (@markCycle r) :=
  Finset.image_injective markPair_injective

theorem pairDegree_fidelity {r : ℕ} (P Q : Finset (Finset (Fin r)))
    (hP : P.card=2) (hQ : Q.card=2) :
    (∑x∈markPair P,x)=(∑x∈markPair Q,x) ↔ pairDegreeEqual P Q := by
  obtain ⟨e,f,hef,rfl⟩ := Finset.card_eq_two.mp hP
  obtain ⟨g,h,hgh,rfl⟩ := Finset.card_eq_two.mp hQ
  have hef' : mark e≠mark f := mark_injective.ne hef
  have hgh' : mark g≠mark h := mark_injective.ne hgh
  simp only [markPair,Finset.image_insert,Finset.image_singleton,
    Finset.sum_pair hef',Finset.sum_pair hgh',pairDegreeEqual,
    Finset.sum_pair hef,Finset.sum_pair hgh]
  exact pair_sum_fidelity e f g h

theorem graphCycles_image {r : ℕ} (edges : Finset (Finset (Fin r))) :
    (graphCycles edges).image markCycle=collisions (graphSource edges) := by
  classical
  rw [collisions_filter]
  have hp : ((graphSource edges).powersetCard 2).powersetCard 2=
      ((edges.powersetCard 2).powersetCard 2).image markCycle := by
    unfold graphSource
    rw [powersetCard_image_injective mark mark_injective,
      powersetCard_image_injective (Finset.image mark) (Finset.image_injective mark_injective)]
    rfl
  rw [hp]
  ext C
  simp only [Finset.mem_image,graphCycles,Finset.mem_filter]
  constructor
  · rintro ⟨D,⟨hD,hdeg⟩,rfl⟩
    refine ⟨⟨D,hD,rfl⟩,?_⟩
    intro P hP Q hQ
    obtain ⟨U,hU,rfl⟩ := Finset.mem_image.mp hP
    obtain ⟨V,hV,rfl⟩ := Finset.mem_image.mp hQ
    have hsub := (Finset.mem_powersetCard.mp hD).1
    exact (pairDegree_fidelity U V (Finset.mem_powersetCard.mp (hsub hU)).2
      (Finset.mem_powersetCard.mp (hsub hV)).2).mpr (hdeg U hU V hV)
  · rintro ⟨⟨D,hD,rfl⟩,hsum⟩
    refine ⟨D,⟨hD,?_⟩,rfl⟩
    intro U hU V hV
    have hsub := (Finset.mem_powersetCard.mp hD).1
    exact (pairDegree_fidelity U V (Finset.mem_powersetCard.mp (hsub hU)).2
      (Finset.mem_powersetCard.mp (hsub hV)).2).mp
      (hsum (markPair U) (Finset.mem_image.mpr ⟨U,hU,rfl⟩)
        (markPair V) (Finset.mem_image.mpr ⟨V,hV,rfl⟩))

theorem graphSource_corner_count {r : ℕ} (edges : Finset (Finset (Fin r))) :
    T (graphSource edges)=2*(graphCycles edges).card := by
  rw [corner_count_no_progression (graphSource edges) (by
    intro a ha b hb c hc he
    exact (graphSource_no_progression edges a b c ha hb hc he).1)]
  rw [← graphCycles_image,Finset.card_image_of_injective _ markCycle_injective]

theorem graphSource_energy_count {r : ℕ} (edges : Finset (Finset (Fin r))) :
    E (graphSource edges)=2*edges.card^2-edges.card+8*(graphCycles edges).card := by
  rw [energy_corner_identity,graphSource_card,graphSource_corner_count]
  omega

end EnergyForcing.GraphSources

namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators

def CycleShape {r : ℕ} (edges : Finset (Finset (Fin r)))
    (C : Finset (Finset (Finset (Fin r)))) : Prop :=
  ∃a b c d : Fin r, a≠b ∧ a≠c ∧ a≠d ∧ b≠c ∧ b≠d ∧ c≠d ∧
    {a,b}∈edges ∧ {c,d}∈edges ∧ {a,c}∈edges ∧ {b,d}∈edges ∧
    C={{{a,b},{c,d}},{{a,c},{b,d}}}

/-- Every encoded cycle is a literal simple four-cycle a-b-d-c-a.
Changing its start or direction preserves the two alternating matchings. -/
theorem graphCycles_shape {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges,e.card=2) (C : Finset (Finset (Finset (Fin r))))
    (hC : C∈graphCycles edges) : CycleShape edges C := by
  classical
  rcases Finset.mem_filter.mp hC with ⟨hC,hdeg⟩
  rcases Finset.mem_powersetCard.mp hC with ⟨hsub,hcard⟩
  obtain ⟨P,Q,hPQ,rfl⟩ := Finset.card_eq_two.mp hcard
  have hP := Finset.mem_powersetCard.mp (hsub (by simp : P∈({P,Q}:Finset (Finset (Finset (Fin r))))))
  have hQ := Finset.mem_powersetCard.mp (hsub (by simp : Q∈({P,Q}:Finset (Finset (Finset (Fin r))))))
  obtain ⟨e,f,hef,rfl⟩ := Finset.card_eq_two.mp hP.2
  obtain ⟨g,h,hgh,rfl⟩ := Finset.card_eq_two.mp hQ.2
  have he : e∈edges := hP.1 (by simp)
  have hf : f∈edges := hP.1 (by simp)
  have hg : g∈edges := hQ.1 (by simp)
  have hh : h∈edges := hQ.1 (by simp)
  have hds := hdeg {e,f} (by simp) {g,h} (by simp)
  simp only [pairDegreeEqual,Finset.sum_pair hef,Finset.sum_pair hgh] at hds
  have hsum := (pair_sum_fidelity e f g h).mpr hds
  have heg : e≠g := by
    intro heq; subst g
    have hfh : f=h := mark_injective (by omega)
    exact hPQ (by rw [hfh])
  have heh : e≠h := by
    intro heq; subst h
    have hfg : f=g := mark_injective (by omega)
    exact hPQ (by rw [hfg,Finset.pair_comm])
  have hdis := (nontrivial_pair_disjoint e f g h (hedges e he) (hedges f hf)
    (hedges g hg) (hedges h hh) hds heg heh).1
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp (hedges e he)
  obtain ⟨c,d,hcd,rfl⟩ := Finset.card_eq_two.mp (hedges f hf)
  have hac : a≠c := by intro heq; subst c; exact (Finset.disjoint_left.mp hdis) (show a∈({a,b}:Finset (Fin r)) by simp) (by simp)
  have had : a≠d := by intro heq; subst d; exact (Finset.disjoint_left.mp hdis) (show a∈({a,b}:Finset (Fin r)) by simp) (by simp)
  have hbc : b≠c := by intro heq; subst c; exact (Finset.disjoint_left.mp hdis) (show b∈({a,b}:Finset (Fin r)) by simp) (by simp)
  have hbd : b≠d := by intro heq; subst d; exact (Finset.disjoint_left.mp hdis) (show b∈({a,b}:Finset (Fin r)) by simp) (by simp)
  have hm := matching_on_four a b c d hab hac had hbc hbd hcd g h (hedges g hg) (hedges h hh) hsum
  simp only [Finset.mem_insert,Finset.mem_singleton] at hm
  rcases hm with hm | hm | hm
  · exact False.elim (hPQ hm.symm)
  · have hge : {a,c}∈edges := hQ.1 (by rw [hm]; simp)
    have hhe : {b,d}∈edges := hQ.1 (by rw [hm]; simp)
    exact ⟨a,b,c,d,hab,hac,had,hbc,hbd,hcd,he,hf,hge,hhe,by rw [hm]⟩
  · have hge : {a,d}∈edges := hQ.1 (by rw [hm]; simp)
    have hhe : {b,c}∈edges := hQ.1 (by rw [hm]; simp)
    refine ⟨a,b,d,c,hab,had,hac,hbd,hbc,hcd.symm,he,?_,hge,hhe,?_⟩
    · simpa [Finset.pair_comm] using hf
    · rw [hm,Finset.pair_comm d c]

end EnergyForcing.GraphSources


