import MidpointThree
import GraphSourceEuclidean
import GraphMatchings

set_option autoImplicit false

namespace EnergyForcing.TwoDistance

open Finset
open scoped BigOperators
open EnergyForcing.PairCollisions EnergyForcing.GraphSources

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

theorem image_pair_preimage (A : Finset ℤ) (phi : ℤ → E)
    (P : Finset E) (hP : P∈(points A phi).powersetCard 2) :
    ∃Q∈A.powersetCard 2, points Q phi=P := by
  classical
  rcases Finset.mem_powersetCard.mp hP with ⟨hsub,hcard⟩
  obtain ⟨x,y,hxy,rfl⟩ := Finset.card_eq_two.mp hcard
  obtain ⟨a,ha,rfl⟩ := Finset.mem_image.mp (hsub (by simp : x∈({x,y}:Finset E)))
  obtain ⟨b,hb,rfl⟩ := Finset.mem_image.mp (hsub (by simp : y∈({phi a,y}:Finset E)))
  have hab : a≠b := fun h => hxy (congrArg phi h)
  refine ⟨{a,b},Finset.mem_powersetCard.mpr ⟨?_,by simp [hab]⟩,?_⟩
  · intro t ht
    simp only [Finset.mem_insert,Finset.mem_singleton] at ht
    rcases ht with rfl|rfl
    · exact ha
    · exact hb
  · simp [points]

theorem image_pair_sum_reflect (A : Finset ℤ) (phi : ℤ → E)
    (hinj : Set.InjOn phi (A:Set ℤ))
    (hreflect : ∀a∈A, ∀b∈A, ∀c∈A, ∀d∈A,
      phi a+phi b=phi c+phi d → a+b=c+d)
    (P Q : Finset ℤ) (hP : P∈A.powersetCard 2) (hQ : Q∈A.powersetCard 2)
    (hs : (∑x∈points P phi,x)=∑x∈points Q phi,x) :
    (∑x∈P,x)=∑x∈Q,x := by
  classical
  rcases Finset.mem_powersetCard.mp hP with ⟨hPA,hPc⟩
  rcases Finset.mem_powersetCard.mp hQ with ⟨hQA,hQc⟩
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hPc
  obtain ⟨c,d,hcd,rfl⟩ := Finset.card_eq_two.mp hQc
  have ha := hPA (by simp : a∈({a,b}:Finset ℤ))
  have hb := hPA (by simp : b∈({a,b}:Finset ℤ))
  have hc := hQA (by simp : c∈({c,d}:Finset ℤ))
  have hd := hQA (by simp : d∈({c,d}:Finset ℤ))
  have hab' : phi a≠phi b := fun h => hab (hinj ha hb h)
  have hcd' : phi c≠phi d := fun h => hcd (hinj hc hd h)
  simp only [points,Finset.image_insert,Finset.image_singleton,
    Finset.sum_pair hab',Finset.sum_pair hcd'] at hs
  simpa only [Finset.sum_pair hab,Finset.sum_pair hcd] using
    hreflect a ha b hb c hc d hd hs

theorem midpoint_cap_of_pair_sum_cap (A : Finset ℤ) (phi : ℤ → E)
    (hinj : Set.InjOn phi (A:Set ℤ))
    (hreflect : ∀a∈A, ∀b∈A, ∀c∈A, ∀d∈A,
      phi a+phi b=phi c+phi d → a+b=c+d)
    (hcap : ∀s, (sumPairs A s).card≤3) (tau : ℝ) (c : E) :
    (midpointPairs (points A phi) tau c).card≤3 := by
  classical
  by_cases hne : (midpointPairs (points A phi) tau c).Nonempty
  · obtain ⟨P,hP⟩ := hne
    obtain ⟨Q,hQ,hQP⟩ := image_pair_preimage A phi P (Finset.mem_filter.mp hP).1
    have hsub : midpointPairs (points A phi) tau c ⊆
        (sumPairs A (∑x∈Q,x)).image (fun R => points R phi) := by
      intro R hR
      obtain ⟨S,hS,hSR⟩ := image_pair_preimage A phi R (Finset.mem_filter.mp hR).1
      refine Finset.mem_image.mpr ⟨S,?_,hSR⟩
      apply Finset.mem_filter.mpr
      refine ⟨hS,image_pair_sum_reflect A phi hinj hreflect S Q hS hQ ?_⟩
      rw [hSR,hQP]
      exact (Finset.mem_filter.mp hR).2.1.trans (Finset.mem_filter.mp hP).2.1.symm
    exact (Finset.card_le_card hsub).trans (Finset.card_image_le.trans (hcap _))
  · rw [Finset.not_nonempty_iff_eq_empty.mp hne]
    simp

theorem graph_embedding_hypotheses {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) :
    Hypotheses (graphSource edges) (graphEmbedding r) 2 := by
  refine ⟨by norm_num,graphEmbedding_injective edges,?_,?_⟩
  · intro a ha b hb c hc d hd hs
    exact (graphEmbedding_pair_fidelity edges a b c d ha hb hc hd).mp hs
  · intro a ha b hb hne
    simpa only [show (2:ℝ)*2=4 by norm_num] using
      graphEmbedding_two_distances edges hedges a b ha hb hne

theorem graph_midpoint_cap {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) (c : EuclideanSpace ℝ (Fin r)) :
    (midpointPairs (points (graphSource edges) (graphEmbedding r)) 2 c).card≤3 := by
  apply midpoint_cap_of_pair_sum_cap _ _ (graphEmbedding_injective edges)
  · intro a ha b hb d hd e he hs
    exact (graphEmbedding_pair_fidelity edges a b d e ha hb hd he).mpr hs
  · exact graph_sumPairs_card_le_three edges hedges

end EnergyForcing.TwoDistance
