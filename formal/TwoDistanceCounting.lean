import MidpointBlocks

set_option autoImplicit false
namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.PairCollisions
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
noncomputable local instance : DecidableEq V := Classical.decEq V
attribute [local instance] Classical.propDecidable

noncomputable def longPairs (X : Finset V) (tau : ℝ) : Finset (Finset V) :=
  (X.powersetCard 2).filter (LongPair tau)

noncomputable def shortPairs (X : Finset V) (tau : ℝ) : Finset (Finset V) :=
  (X.powersetCard 2).filter (fun P=>¬LongPair tau P)

noncomputable def pairMidpoint (P : Finset V) : V := (1/2:ℝ) • ∑x∈P,x
noncomputable def midpointKeys (X : Finset V) (tau : ℝ) : Finset V :=
  (longPairs X tau).image pairMidpoint
noncomputable def midpointVertices (X : Finset V) (tau : ℝ) (c : V) : Finset V :=
  (midpointPairs X tau c).biUnion id
noncomputable def geometricCollisions (X : Finset V) (tau : ℝ) : Finset (Finset (Finset V)) :=
  (midpointKeys X tau).biUnion fun c=>(midpointPairs X tau c).powersetCard 2
noncomputable def geomT (X : Finset V) (tau : ℝ) : ℕ := 2*(geometricCollisions X tau).card

@[simp] theorem mem_longPairs (X : Finset V) (tau : ℝ) (P : Finset V) :
    P∈longPairs X tau ↔ P∈X.powersetCard 2 ∧ LongPair tau P := by simp [longPairs]
@[simp] theorem mem_shortPairs (X : Finset V) (tau : ℝ) (P : Finset V) :
    P∈shortPairs X tau ↔ P∈X.powersetCard 2 ∧ ¬LongPair tau P := by simp [shortPairs]

theorem pairMidpoint_eq_iff (P : Finset V) (c : V) :
    pairMidpoint P=c ↔ (∑x∈P,x)=(2:ℝ) • c := by
  constructor
  · intro h
    rw [← h,pairMidpoint,smul_smul]
    norm_num
  · intro h
    rw [pairMidpoint,h,smul_smul]
    norm_num

theorem midpointPairs_filter (X : Finset V) (tau : ℝ) (c : V) :
    midpointPairs X tau c=(longPairs X tau).filter (fun P=> pairMidpoint P=c) := by
  ext P
  simp [midpointPairs,pairMidpoint_eq_iff,and_left_comm,and_assoc,and_comm]

theorem midpoint_key_of_pair (X : Finset V) (tau : ℝ) (c : V)
    (P : Finset V) (hP:P∈midpointPairs X tau c) : c∈midpointKeys X tau := by
  rw [midpointPairs_filter] at hP
  rcases Finset.mem_filter.mp hP with ⟨hp,he⟩
  exact Finset.mem_image.mpr ⟨P,hp,he⟩

theorem midpoint_fiber_unique (X : Finset V) (tau : ℝ) (c d : V)
    (P : Finset V) (hc:P∈midpointPairs X tau c) (hd:P∈midpointPairs X tau d) : c=d := by
  rw [midpointPairs_filter] at hc hd
  exact (Finset.mem_filter.mp hc).2.symm.trans (Finset.mem_filter.mp hd).2

theorem long_short_card (X : Finset V) (tau : ℝ) :
    (longPairs X tau).card+(shortPairs X tau).card=X.card.choose 2 := by
  have h:=Finset.filter_card_add_filter_neg_card_eq_card (s:=X.powersetCard 2) (LongPair tau)
  simpa [longPairs,shortPairs] using h

theorem midpoint_total_mass (X : Finset V) (tau : ℝ) :
    (∑c∈midpointKeys X tau,(midpointPairs X tau c).card)=(longPairs X tau).card := by
  simp only [midpointPairs_filter,midpointKeys]
  exact (Finset.card_eq_sum_card_image pairMidpoint (longPairs X tau)).symm

theorem geometricCollisions_card (X : Finset V) (tau : ℝ) :
    (geometricCollisions X tau).card=
      ∑c∈midpointKeys X tau,((midpointPairs X tau c).card).choose 2 := by
  unfold geometricCollisions
  rw [Finset.card_biUnion]
  · simp
  · intro c hc d hd hcd
    apply Finset.disjoint_left.mpr
    intro S hS hS'
    rcases Finset.mem_powersetCard.mp hS with ⟨hs,hcard⟩
    rcases Finset.mem_powersetCard.mp hS' with ⟨hs',_⟩
    have hn:S.Nonempty:=Finset.card_pos.mp (by omega)
    obtain ⟨P,hP⟩:=hn
    exact hcd (midpoint_fiber_unique X tau c d P (hs hP) (hs' hP))

theorem geomT_moment (X : Finset V) (tau : ℝ) :
    geomT X tau=∑c∈midpointKeys X tau,
      (midpointPairs X tau c).card*((midpointPairs X tau c).card-1) := by
  rw [geomT,geometricCollisions_card,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro c hc
  let n:=(midpointPairs X tau c).card
  change 2*n.choose 2=n*(n-1)
  have hh:=square_eq_self_add_twice_choose n
  by_cases hn:n=0
  · simp [hn]
  · have hn1:n-1+1=n:=by omega
    nlinarith

theorem mem_geometricCollisions (X : Finset V) (tau : ℝ) (S : Finset (Finset V)) :
    S∈geometricCollisions X tau ↔ S∈(longPairs X tau).powersetCard 2 ∧
      ∀P∈S,∀Q∈S,(∑x∈P,x)=∑x∈Q,x := by
  constructor
  · intro hS
    obtain ⟨c,hc,hS⟩:=Finset.mem_biUnion.mp hS
    rcases Finset.mem_powersetCard.mp hS with ⟨hsub,hcard⟩
    constructor
    · apply Finset.mem_powersetCard.mpr
      refine ⟨?_,hcard⟩
      intro P hP
      rw [midpointPairs_filter] at hsub
      exact (Finset.mem_filter.mp (hsub hP)).1
    · intro P hP Q hQ
      have hp:=(Finset.mem_filter.mp (hsub hP)).2.1
      have hq:=(Finset.mem_filter.mp (hsub hQ)).2.1
      exact hp.trans hq.symm
  · rintro ⟨hS,hsum⟩
    rcases Finset.mem_powersetCard.mp hS with ⟨hsub,hcard⟩
    have hn:S.Nonempty:=Finset.card_pos.mp (by omega)
    obtain ⟨P,hP⟩:=hn
    refine Finset.mem_biUnion.mpr ⟨pairMidpoint P,Finset.mem_image.mpr ⟨P,hsub hP,rfl⟩,?_⟩
    apply Finset.mem_powersetCard.mpr
    refine ⟨?_,hcard⟩
    intro Q hQ
    rw [midpointPairs_filter]
    apply Finset.mem_filter.mpr
    refine ⟨hsub hQ,?_⟩
    unfold pairMidpoint
    rw [hsum Q hQ P hP]

theorem geomT_cap_seven (X : Finset V) (tau : ℝ)
    (hcap:∀c:V,(midpointPairs X tau c).card≤7) : geomT X tau≤6*X.card.choose 2 := by
  rw [geomT_moment]
  calc
    (∑c∈midpointKeys X tau,(midpointPairs X tau c).card*((midpointPairs X tau c).card-1))
      ≤∑c∈midpointKeys X tau,6*(midpointPairs X tau c).card := by
        apply Finset.sum_le_sum
        intro c hc
        have h:=hcap c
        have hm:(midpointPairs X tau c).card-1≤6:=by omega
        have hh:=Nat.mul_le_mul_left (midpointPairs X tau c).card hm
        nlinarith
    _=6*(longPairs X tau).card := by rw [← Finset.mul_sum,midpoint_total_mass]
    _≤6*X.card.choose 2 := by have h:=long_short_card X tau;omega

end EnergyForcing.TwoDistance
