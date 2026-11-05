import TwoDistanceIncidence
import TwoDistanceSource
import TwoDistanceBlockGeometry

set_option autoImplicit false
namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators
open EnergyForcing.Counting
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
attribute [local instance] Classical.propDecidable
noncomputable local instance : DecidableEq V := Classical.decEq V

theorem longPairs_mono {X Y : Finset V} (tau : ℝ) (hXY:X⊆Y) : longPairs X tau⊆longPairs Y tau := by
  intro P hP
  rcases (mem_longPairs X tau P).mp hP with ⟨hP,hL⟩
  rcases Finset.mem_powersetCard.mp hP with ⟨hsub,hcard⟩
  exact (mem_longPairs Y tau P).mpr ⟨Finset.mem_powersetCard.mpr ⟨hsub.trans hXY,hcard⟩,hL⟩

theorem geometricCollisions_mono {X Y : Finset V} (tau : ℝ) (hXY:X⊆Y) :
    geometricCollisions X tau⊆geometricCollisions Y tau := by
  intro S hS
  rcases (mem_geometricCollisions X tau S).mp hS with ⟨hS,hs⟩
  rcases Finset.mem_powersetCard.mp hS with ⟨hsub,hcard⟩
  exact (mem_geometricCollisions Y tau S).mpr
    ⟨Finset.mem_powersetCard.mpr ⟨hsub.trans (longPairs_mono tau hXY),hcard⟩,hs⟩

theorem longPair_sdiff {X Y : Finset V} (tau : ℝ) (P : Finset V)
    (hP:P∈longPairs X tau) (hdis:Disjoint P Y) : P∈longPairs (X\Y) tau := by
  rcases (mem_longPairs X tau P).mp hP with ⟨hP,hL⟩
  rcases Finset.mem_powersetCard.mp hP with ⟨hsub,hcard⟩
  apply (mem_longPairs _ tau P).mpr
  refine ⟨Finset.mem_powersetCard.mpr ⟨?_,hcard⟩,hL⟩
  intro x hx
  exact Finset.mem_sdiff.mpr ⟨hsub hx,fun hy=> Finset.disjoint_left.mp hdis hx hy⟩

theorem isolated_collision_partition (X : Finset V) (tau : ℝ) (ht:0< tau)
    (c : V) (k : ℕ) (B : RadiusBlock X tau c k) (hout:B.OutsideOrthogonal) :
    geometricCollisions X tau=(midpointPairs X tau c).powersetCard 2 ∪
      geometricCollisions (X\B.vertices) tau := by
  ext S
  constructor
  · intro hS
    rcases (mem_geometricCollisions X tau S).mp hS with ⟨hS,hs⟩
    rcases Finset.mem_powersetCard.mp hS with ⟨hsub,hcard⟩
    obtain ⟨P,Q,hPQ,hrepr⟩:=Finset.card_eq_two.mp hcard
    have hP:P∈longPairs X tau:=hsub (by rw [hrepr];simp)
    have hQ:Q∈longPairs X tau:=hsub (by rw [hrepr];simp)
    have hsum:(∑x∈P,x)=∑x∈Q,x:=hs P (by rw [hrepr];simp) Q (by rw [hrepr];simp)
    rcases B.equal_long_pairs_block_dichotomy ht hout P Q
      ((mem_longPairs X tau P).mp hP).1 ((mem_longPairs X tau Q).mp hQ).1 hPQ hsum
      ((mem_longPairs X tau P).mp hP).2 ((mem_longPairs X tau Q).mp hQ).2 with hin|hout'
    · apply Finset.mem_union_left
      apply Finset.mem_powersetCard.mpr
      refine ⟨?_,hcard⟩
      rw [hrepr]
      exact Finset.insert_subset hin.1 (Finset.singleton_subset_iff.mpr hin.2)
    · apply Finset.mem_union_right
      apply (mem_geometricCollisions _ tau S).mpr
      refine ⟨Finset.mem_powersetCard.mpr ⟨?_,hcard⟩,hs⟩
      rw [hrepr]
      exact Finset.insert_subset (longPair_sdiff tau P hP hout'.1)
        (Finset.singleton_subset_iff.mpr (longPair_sdiff tau Q hQ hout'.2))
  · intro hS
    rcases Finset.mem_union.mp hS with hi|ho
    · rcases Finset.mem_powersetCard.mp hi with ⟨hsub,hcard⟩
      have hn:S.Nonempty:=Finset.card_pos.mp (by omega)
      obtain ⟨P,hP⟩:=hn
      exact Finset.mem_biUnion.mpr ⟨c,midpoint_key_of_pair X tau c P (hsub hP),
        Finset.mem_powersetCard.mpr ⟨hsub,hcard⟩⟩
    · exact geometricCollisions_mono tau Finset.sdiff_subset ho

theorem isolated_collision_disjoint (X : Finset V) (tau : ℝ)
    (c : V) (k : ℕ) (B : RadiusBlock X tau c k) :
    Disjoint ((midpointPairs X tau c).powersetCard 2) (geometricCollisions (X\B.vertices) tau) := by
  apply Finset.disjoint_left.mpr
  intro S hi ho
  rcases Finset.mem_powersetCard.mp hi with ⟨hi,hcard⟩
  have hh:=(mem_geometricCollisions _ tau S).mp ho
  have hsub: S⊆longPairs (X\B.vertices) tau:=(Finset.mem_powersetCard.mp hh.1).1
  obtain ⟨P,hP⟩:=Finset.card_pos.mp (by omega:0< S.card)
  have hPc:P.card=2:=(Finset.mem_powersetCard.mp (Finset.mem_filter.mp (hi hP)).1).2
  obtain ⟨x,hx⟩:=Finset.card_pos.mp (by omega:0< P.card)
  have hxY:x∈B.vertices:=by
    rw [B.vertices_eq]
    exact Finset.mem_biUnion.mpr ⟨P,hi hP,hx⟩
  have hxR:x∈X\B.vertices:=
    (Finset.mem_powersetCard.mp ((mem_longPairs _ tau P).mp (hsub hP)).1).1 hx
  exact (Finset.mem_sdiff.mp hxR).2 hxY

theorem isolated_geomT_add (X : Finset V) (tau : ℝ) (ht:0< tau)
    (c : V) (k : ℕ) (B : RadiusBlock X tau c k) (hout:B.OutsideOrthogonal) :
    geomT X tau=2*((midpointPairs X tau c).card.choose 2)+geomT (X\B.vertices) tau := by
  rw [geomT,isolated_collision_partition X tau ht c k B hout,
    Finset.card_union_of_disjoint (isolated_collision_disjoint X tau c k B),Finset.card_powersetCard]
  unfold geomT
  omega

theorem disjoint_choose_bound (X Y : Finset V) (hYX:Y⊆X) :
    Y.card.choose 2+(X\Y).card.choose 2≤ X.card.choose 2 := by
  have hcard:=Finset.card_sdiff_add_card_eq_card hYX
  have hy:=Nat.cast_choose_two ℝ Y.card
  have hz:=Nat.cast_choose_two ℝ (X\Y).card
  have hx:=Nat.cast_choose_two ℝ X.card
  have hc:(X.card:ℝ)=(Y.card:ℝ)+((X\Y).card:ℝ):=by exact_mod_cast hcard.symm.trans (Nat.add_comm _ _)
  have hh:(Y.card.choose 2:ℝ)+((X\Y).card.choose 2:ℝ)≤(X.card.choose 2:ℝ):=by
    nlinarith [mul_nonneg (Nat.cast_nonneg Y.card : (0:ℝ)≤ Y.card) (Nat.cast_nonneg (X\Y).card : (0:ℝ)≤(X\Y).card)]
  exact_mod_cast hh

theorem geomT_six_bound (X : Finset V) (tau : ℝ) (ht:0< tau) (hX:TwoDistances X tau) :
    geomT X tau≤6*X.card.choose 2 := by
  have main : ∀n:ℕ,∀X:Finset V,X.card=n → TwoDistances X tau → geomT X tau≤6*X.card.choose 2 := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro X hn hX
      by_cases hremove:∃c:V,∃B:RadiusBlock X tau c (midpointPairs X tau c).card,
          8≤(midpointPairs X tau c).card ∧ B.OutsideOrthogonal
      · obtain ⟨c,B,hk,hout⟩:=hremove
        have hy:=B.vertices_card
        have hsplit:=Finset.card_sdiff_add_card_eq_card B.vertices_subset
        have hrest:(X\B.vertices).card< n:=by omega
        have hrestDist:TwoDistances (X\B.vertices) tau:=by
          intro x hx y hy hne
          exact hX x (Finset.mem_sdiff.mp hx).1 y (Finset.mem_sdiff.mp hy).1 hne
        have hind:=ih (X\B.vertices).card hrest (X\B.vertices) rfl hrestDist
        have hchoose: (midpointPairs X tau c).card.choose 2≤ B.vertices.card.choose 2:=
          Nat.choose_le_choose 2 (by omega)
        have hpair:=disjoint_choose_bound X B.vertices B.vertices_subset
        rw [isolated_geomT_add X tau ht c _ B hout]
        omega
      · have hcap:∀c:V,(midpointPairs X tau c).card≤8:=by
          intro c
          by_contra hn8
          obtain ⟨B⟩:=midpoint_block X tau ht hX c
          exact hremove ⟨c,B,by omega,B.nine_outside_orthogonal ht hX (by omega)⟩
        by_cases hcap7:∀c:V,(midpointPairs X tau c).card≤7
        · exact geomT_cap_seven X tau hcap7
        · push_neg at hcap7
          obtain ⟨c,hc⟩:=hcap7
          have h8:(midpointPairs X tau c).card=8:=by have hh:=hcap c;omega
          obtain ⟨B⟩:=midpoint_block X tau ht hX c
          have hnon:¬B.OutsideOrthogonal:=fun ho=> hremove ⟨c,B,by omega,ho⟩
          have hcard:X.card≤53:=by
            have bridge:∀j:ℕ,∀BB:RadiusBlock X tau c j,j=8 → ¬BB.OutsideOrthogonal → X.card≤53:=by
              intro j BB hj hno
              subst j
              exact BB.exceptional_eight_card_le ht hX hno
            exact bridge _ B h8 hnon
          exact geomT_small_cap_eight X tau ht hX hcard hcap
  exact main X.card X rfl hX

/-- Full thm:two_distance on arbitrary finite integer sources and real inner-product targets. -/
theorem two_distance_bounds (A : Finset ℤ) (phi : ℤ→V) (tau : ℝ) (h:Hypotheses A phi tau) :
    T A≤6*M A ∧ (M A:ℝ)≤13*(span A:ℝ) ∧
      EnergyForcing.properOn (EnergyForcing.strictSource (·∈A)) (distanceColor phi tau) := by
  have hg:=geomT_six_bound (points A phi) tau h.positive (points_twoDistances A phi tau h)
  rw [points_card A phi tau h] at hg
  have ht:T A≤6*M A:=(source_corner_le_geomT A phi tau h).trans hg
  refine ⟨ht,?_,squared_distance_coloring_proper A phi tau h⟩
  have hs:=span_pair_bound A 6 (by norm_num) (by exact_mod_cast ht)
  norm_num at hs
  exact hs

end EnergyForcing.TwoDistance
