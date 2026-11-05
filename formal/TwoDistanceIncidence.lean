import TwoDistanceCounting
import TwoDistanceIsolation

set_option autoImplicit false
namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
attribute [local instance] Classical.propDecidable
noncomputable local instance : DecidableEq V := Classical.decEq V

noncomputable def eightMidpoints (X : Finset V) (tau : ℝ) : Finset V :=
  (midpointKeys X tau).filter fun c=>(midpointPairs X tau c).card=8

noncomputable def shortPairCenters (X : Finset V) (tau : ℝ) (P : Finset V) : Finset V :=
  (eightMidpoints X tau).filter fun c=> P⊆midpointVertices X tau c

theorem shortPairCenters_bound (X : Finset V) (tau : ℝ) (ht:0< tau)
    (hX:TwoDistances X tau) (P : Finset V) (hP:P∈shortPairs X tau) :
    (shortPairCenters X tau P).card≤ X.card-2 := by
  rcases (mem_shortPairs X tau P).mp hP with ⟨hP,hshort⟩
  rcases Finset.mem_powersetCard.mp hP with ⟨hPX,hPc⟩
  obtain ⟨x,y,hxy,rfl⟩:=Finset.card_eq_two.mp hPc
  have hxX:x∈X:=hPX (by simp)
  have hyX:y∈X:=hPX (by simp)
  have hmap:∀c∈shortPairCenters X tau {x,y},(2:ℝ) • c-x∈(X.erase x).erase y:=by
    intro c hc
    obtain ⟨B⟩:=midpoint_block X tau ht hX c
    have hsub:({x,y}:Finset V)⊆B.vertices:=by
      rw [B.vertices_eq]
      exact (Finset.mem_filter.mp hc).2
    have hxY:x∈B.vertices:=hsub (by simp)
    have hp:=B.antipode_pair x hxY
    have ha:=B.antipode_long x hxY
    have hv:(2:ℝ) • c-x∈X:=B.vertices_subset (B.antipode_mem x hxY)
    apply Finset.mem_erase.mpr
    refine ⟨?_,Finset.mem_erase.mpr ⟨Ne.symm ha.1,hv⟩⟩
    intro he
    rw [he] at hp
    exact hshort (Finset.mem_filter.mp hp).2.2
  have hinj:Set.InjOn (fun c:V=>(2:ℝ) • c-x) (shortPairCenters X tau {x,y}) :=by
    intro c hc d hd he
    dsimp at he
    have hh:(2:ℝ) • c=(2:ℝ) • d:=sub_left_injective he
    have hj:=congrArg (fun v:V=>(1/2:ℝ) • v) hh
    simpa [smul_smul] using hj
  have hh:=Finset.card_le_card_of_injOn _ hmap hinj
  have hyerase:y∈X.erase x:=Finset.mem_erase.mpr ⟨Ne.symm hxy,hyX⟩
  rw [Finset.card_erase_of_mem hyerase,Finset.card_erase_of_mem hxX] at hh
  omega

theorem shortPairs_subset_filter (X Y : Finset V) (tau : ℝ) (hYX:Y⊆X) :
    shortPairs Y tau=(shortPairs X tau).filter (fun P=> P⊆Y) := by
  ext P
  simp only [mem_shortPairs,Finset.mem_filter,Finset.mem_powersetCard]
  constructor
  · rintro ⟨⟨hPY,hc⟩,hs⟩
    exact ⟨⟨⟨hPY.trans hYX,hc⟩,hs⟩,hPY⟩
  · rintro ⟨⟨⟨_,hc⟩,hs⟩,hPY⟩
    exact ⟨⟨hPY,hc⟩,hs⟩

theorem eight_midpoint_short_count (X : Finset V) (tau : ℝ) (ht:0< tau)
    (hX:TwoDistances X tau) (c : V) (hc:c∈eightMidpoints X tau) :
    ((shortPairs X tau).filter (fun P=> P⊆midpointVertices X tau c)).card=112 := by
  obtain ⟨B⟩:=midpoint_block X tau ht hX c
  have hk:(midpointPairs X tau c).card=8:=(Finset.mem_filter.mp hc).2
  have hv:B.vertices.card=16:=by rw [B.vertices_card,hk]
  have hl:longPairs B.vertices tau=midpointPairs X tau c:=by
    ext P
    exact (mem_longPairs B.vertices tau P).trans (B.block_long_pairs_iff ht P)
  have hls:=long_short_card B.vertices tau
  rw [hl,hv] at hls
  have hc16:Nat.choose 16 2=120:=by decide
  rw [hc16] at hls
  have hvEq:B.vertices=midpointVertices X tau c:=B.vertices_eq
  rw [←hvEq,←shortPairs_subset_filter X B.vertices tau B.vertices_subset]
  omega

theorem eight_midpoint_incidence (X : Finset V) (tau : ℝ) (ht:0< tau)
    (hX:TwoDistances X tau) :
    112*(eightMidpoints X tau).card≤(X.card-2)*(shortPairs X tau).card := by
  have hswap:
      (∑c∈eightMidpoints X tau,((shortPairs X tau).filter (fun P=> P⊆midpointVertices X tau c)).card)=
      ∑P∈shortPairs X tau,(shortPairCenters X tau P).card := by
    simp only [shortPairCenters,Finset.card_eq_sum_ones,Finset.sum_filter]
    exact Finset.sum_comm
  have hleft:
      (∑c∈eightMidpoints X tau,((shortPairs X tau).filter (fun P=> P⊆midpointVertices X tau c)).card)=
      112*(eightMidpoints X tau).card:=by
    calc
      _=∑c∈eightMidpoints X tau,112:=by
        apply Finset.sum_congr rfl
        intro c hc
        exact eight_midpoint_short_count X tau ht hX c hc
      _=_:=by simp [Nat.mul_comm]
  rw [←hleft,hswap]
  calc
    (∑P∈shortPairs X tau,(shortPairCenters X tau P).card)≤∑P∈shortPairs X tau,(X.card-2):=by
      apply Finset.sum_le_sum
      intro P hP
      exact shortPairCenters_bound X tau ht hX P hP
    _=_:=by simp [Nat.mul_comm]

theorem geomT_cap_eight_bound (X : Finset V) (tau : ℝ)
    (hcap:∀c:V,(midpointPairs X tau c).card≤8) :
    geomT X tau≤6*(longPairs X tau).card+8*(eightMidpoints X tau).card := by
  rw [geomT_moment]
  have hpoint:∀c∈midpointKeys X tau,
      (midpointPairs X tau c).card*((midpointPairs X tau c).card-1)≤
      6*(midpointPairs X tau c).card+(if (midpointPairs X tau c).card=8 then 8 else 0):=by
    intro c hc
    have hn:=hcap c
    interval_cases hk:(midpointPairs X tau c).card <;> norm_num
  calc
    _≤∑c∈midpointKeys X tau,
      (6*(midpointPairs X tau c).card+(if (midpointPairs X tau c).card=8 then 8 else 0)):=
      Finset.sum_le_sum hpoint
    _=6*(longPairs X tau).card+8*(eightMidpoints X tau).card:=by
      rw [Finset.sum_add_distrib,←Finset.mul_sum,midpoint_total_mass]
      congr 1
      have hh : (∑c∈midpointKeys X tau,if (midpointPairs X tau c).card=8 then 8 else 0)=
          ∑c∈eightMidpoints X tau,8 := by
        rw [eightMidpoints,Finset.sum_filter]
      rw [hh]
      simp [Nat.mul_comm]

theorem geomT_small_cap_eight (X : Finset V) (tau : ℝ) (ht:0< tau)
    (hX:TwoDistances X tau) (hcard:X.card≤53)
    (hcap:∀c:V,(midpointPairs X tau c).card≤8) : geomT X tau≤6*X.card.choose 2 := by
  have hi:=eight_midpoint_incidence X tau ht hX
  have hn:X.card-2≤51:=by omega
  have hi':112*(eightMidpoints X tau).card≤51*(shortPairs X tau).card:=
    hi.trans (Nat.mul_le_mul_right _ hn)
  have hh:=geomT_cap_eight_bound X tau hcap
  have hp:=long_short_card X tau
  omega

end EnergyForcing.TwoDistance
