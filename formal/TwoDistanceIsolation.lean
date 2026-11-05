import MidpointBlocks
import TwoDistanceExceptional

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace EnergyForcing.TwoDistance
open Finset
open scoped BigOperators InnerProductSpace
variable {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
noncomputable local instance : DecidableEq V := Classical.decEq V

namespace RadiusBlock
variable {X : Finset V} {tau : ℝ} {c : V} {k : ℕ}

noncomputable def vertices (B : RadiusBlock X tau c k) : Finset V :=
  Finset.univ.image (endpoint c B.radii)

theorem vertices_eq (B : RadiusBlock X tau c k) :
    B.vertices=(midpointPairs X tau c).biUnion id := B.endpoint_image

theorem vertices_subset (B : RadiusBlock X tau c k) : B.vertices⊆X := by
  intro x hx
  obtain ⟨q,hq,rfl⟩ := Finset.mem_image.mp hx
  exact B.endpoints_mem q

theorem vertices_card (B : RadiusBlock X tau c k) : B.vertices.card=2*k := by
  rw [vertices,Finset.card_image_of_injective _ B.endpoints_injective]
  simp
  omega

theorem antipode_pair (B : RadiusBlock X tau c k) (x : V) (hx : x∈B.vertices) :
    ({x,(2:ℝ) • c-x} : Finset V)∈midpointPairs X tau c := by
  classical
  rw [B.vertices_eq] at hx
  obtain ⟨P,hP,hxP⟩ := Finset.mem_biUnion.mp hx
  have hh := Finset.mem_filter.mp hP
  have he := pair_from_sum_and_member P (Finset.mem_powersetCard.mp hh.1).2 x hxP
  rw [hh.2.1] at he
  exact he ▸ hP

theorem antipode_mem (B : RadiusBlock X tau c k) (x : V) (hx : x∈B.vertices) :
    (2:ℝ) • c-x∈B.vertices := by
  rw [B.vertices_eq]
  exact Finset.mem_biUnion.mpr ⟨_,B.antipode_pair x hx,by simp⟩

theorem antipode_long (B : RadiusBlock X tau c k) (x : V) (hx : x∈B.vertices) :
    x≠(2:ℝ) • c-x ∧ ‖x-((2:ℝ) • c-x)‖^2=2*tau := by
  classical
  have hh := Finset.mem_filter.mp (B.antipode_pair x hx)
  have hc := (Finset.mem_powersetCard.mp hh.1).2
  have hne : x≠(2:ℝ) • c-x := by
    intro he
    rw [Finset.card_insert_of_mem (Finset.mem_singleton.mpr he),Finset.card_singleton] at hc
    omega
  exact ⟨hne,hh.2.2 x (by simp) _ (by simp) hne⟩

def OutsideOrthogonal (B : RadiusBlock X tau c k) : Prop :=
  ∀x∈X, x∉B.vertices → ∀i, ⟪x-c,B.radii i⟫_ℝ=0

theorem endpoint_radius_sq (B : RadiusBlock X tau c k) (q : Fin k×Bool) :
    ‖endpoint c B.radii q-c‖^2=tau/2 := by
  rcases q with ⟨i,b⟩
  cases b <;> simp [endpoint,B.radius_sq]

theorem endpoint_exposes (B : RadiusBlock X tau c k) (ht : 0 < tau)
    (hout : B.OutsideOrthogonal) (q : Fin k×Bool) (x : V) (hx : x∈X)
    (hne : x≠endpoint c B.radii q) : ⟪x-c,endpoint c B.radii q-c⟫_ℝ ≤ 0 := by
  by_cases hy : x∈B.vertices
  · obtain ⟨r,hr,rfl⟩ := Finset.mem_image.mp hy
    rcases q with ⟨i,b⟩
    rcases r with ⟨j,d⟩
    by_cases hij : j=i
    · subst j
      cases b <;> cases d <;>
        simp only [endpoint,Bool.false_eq_true,if_false,if_true,add_sub_cancel_left,
          inner_neg_left,inner_neg_right,real_inner_self_eq_norm_sq,B.radius_sq] at hne ⊢ <;>
        first | contradiction | linarith
    · have ho := B.orthogonal j i hij
      cases b <;> cases d <;>
        simp only [endpoint,Bool.false_eq_true,if_false,if_true,add_sub_cancel_left,
          inner_neg_left,inner_neg_right,ho,neg_zero,le_refl]
  · have hh := hout x hx hy q.1
    rcases q with ⟨i,b⟩
    cases b <;> simp [endpoint,inner_neg_right,hh]

theorem endpoint_outside_inner (B : RadiusBlock X tau c k)
    (hout : B.OutsideOrthogonal) (q : Fin k×Bool) (x : V) (hx : x∈X) (hy : x∉B.vertices) :
    ⟪x-c,endpoint c B.radii q-c⟫_ℝ=0 := by
  have hh := hout x hx hy q.1
  rcases q with ⟨i,b⟩
  cases b <;> simp [endpoint,inner_neg_right,hh]

theorem equal_pair_no_mixed (B : RadiusBlock X tau c k) (ht : 0 < tau)
    (hout : B.OutsideOrthogonal) (P Q : Finset V)
    (hP : P∈X.powersetCard 2) (hQ : Q∈X.powersetCard 2)
    (hne : P≠Q) (hs : (∑x∈P,x)=∑x∈Q,x)
    (a b : V) (hab : a≠b) (hPe : P={a,b}) (ha : a∈B.vertices) : b∈B.vertices := by
  by_contra hb
  obtain ⟨q,hq,he⟩ := Finset.mem_image.mp ha
  have hPX := (Finset.mem_powersetCard.mp hP).1
  have hQX := (Finset.mem_powersetCard.mp hQ).1
  have haP : a∈P := by rw [hPe]; simp
  have hbP : b∈P := by rw [hPe]; simp
  have haQ : a∉Q := by
    intro hh
    exact hne (pairs_equal_of_shared P Q (Finset.mem_powersetCard.mp hP).2
      (Finset.mem_powersetCard.mp hQ).2 hs a haP hh)
  obtain ⟨u,v,huv,hQe⟩ := Finset.card_eq_two.mp (Finset.mem_powersetCard.mp hQ).2
  have hu : u∈Q := by rw [hQe]; simp
  have hv : v∈Q := by rw [hQe]; simp
  have huc := B.endpoint_exposes ht hout q u (hQX hu) (by intro hh; exact haQ ((hh.trans he) ▸ hu))
  have hvc := B.endpoint_exposes ht hout q v (hQX hv) (by intro hh; exact haQ ((hh.trans he) ▸ hv))
  have hbc := B.endpoint_outside_inner hout q b (hPX hbP) hb
  have hac : ⟪a-c,endpoint c B.radii q-c⟫_ℝ=tau/2 := by
    rw [← he,real_inner_self_eq_norm_sq,B.endpoint_radius_sq]
  have hvec : (a-c)+(b-c)=(u-c)+(v-c) := by
    rw [hPe,hQe,Finset.sum_pair hab,Finset.sum_pair huv] at hs
    calc
      _ = (a+b)-(c+c) := by abel
      _ = (u+v)-(c+c) := by rw [hs]
      _ = _ := by abel
  have hi := congrArg (fun x => ⟪x,endpoint c B.radii q-c⟫_ℝ) hvec
  simp only [inner_add_left,hac,hbc] at hi
  linarith

theorem long_endpoints_sum (B : RadiusBlock X tau c k) (ht : 0 < tau)
    (q r : Fin k×Bool) (hne : endpoint c B.radii q≠endpoint c B.radii r)
    (hl : ‖endpoint c B.radii q-endpoint c B.radii r‖^2=2*tau) :
    endpoint c B.radii q+endpoint c B.radii r=(2:ℝ) • c := by
  rcases q with ⟨i,b⟩
  rcases r with ⟨j,d⟩
  by_cases hij : i=j
  · subst j
    cases b <;> cases d <;> simp only [endpoint,Bool.false_eq_true,if_false,if_true] at hne ⊢
    · contradiction
    · rw [two_smul]; abel
    · rw [two_smul]; abel
    · contradiction
  · have ho := B.orthogonal i j hij
    have hinner : ⟪endpoint c B.radii (i,b)-c,endpoint c B.radii (j,d)-c⟫_ℝ=0 := by
      cases b <;> cases d <;> simp [endpoint,inner_neg_left,inner_neg_right,ho]
    have hv : endpoint c B.radii (i,b)-endpoint c B.radii (j,d)=
        (endpoint c B.radii (i,b)-c)-(endpoint c B.radii (j,d)-c) := by abel
    rw [hv,norm_sub_sq_real,B.endpoint_radius_sq,B.endpoint_radius_sq,hinner] at hl
    linarith

theorem block_long_pairs_iff (B : RadiusBlock X tau c k) (ht : 0 < tau) (P : Finset V) :
    (P∈B.vertices.powersetCard 2 ∧ LongPair tau P) ↔ P∈midpointPairs X tau c := by
  classical
  constructor
  · rintro ⟨hP,hL⟩
    have hsub := (Finset.mem_powersetCard.mp hP).1
    have hcard := (Finset.mem_powersetCard.mp hP).2
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_powersetCard.mpr ⟨hsub.trans B.vertices_subset,hcard⟩,?_,hL⟩
    obtain ⟨x,y,hxy,rfl⟩ := Finset.card_eq_two.mp hcard
    obtain ⟨q,hq,hqx⟩ := Finset.mem_image.mp (hsub (by simp : x∈({x,y}:Finset V)))
    obtain ⟨r,hr,hry⟩ := Finset.mem_image.mp (hsub (by simp : y∈({x,y}:Finset V)))
    have hh := B.long_endpoints_sum ht q r (by rw [hqx,hry]; exact hxy)
      (by rw [hqx,hry]; exact hL x (by simp) y (by simp) hxy)
    rw [Finset.sum_pair hxy]
    rwa [hqx,hry] at hh
  · intro hP
    have hh := Finset.mem_filter.mp hP
    refine ⟨Finset.mem_powersetCard.mpr ⟨?_,(Finset.mem_powersetCard.mp hh.1).2⟩,hh.2.2⟩
    intro x hx
    rw [B.vertices_eq]
    exact Finset.mem_biUnion.mpr ⟨P,hP,hx⟩

theorem touching_pair_midpoint (B : RadiusBlock X tau c k) (ht : 0 < tau)
    (hout : B.OutsideOrthogonal) (P Q : Finset V)
    (hP : P∈X.powersetCard 2) (hQ : Q∈X.powersetCard 2)
    (hne : P≠Q) (hs : (∑x∈P,x)=∑x∈Q,x) (hL : LongPair tau P)
    (htouch : ¬Disjoint P B.vertices) : P∈midpointPairs X tau c := by
  classical
  obtain ⟨a,haP,haY⟩ := Finset.not_disjoint_iff.mp htouch
  have hPc := (Finset.mem_powersetCard.mp hP).2
  obtain ⟨x,y,hxy,hPe⟩ := Finset.card_eq_two.mp hPc
  have ha : a=x ∨ a=y := by simpa [hPe] using haP
  have hsub : P⊆B.vertices := by
    rcases ha with hax|hay
    · subst a
      have hy := B.equal_pair_no_mixed ht hout P Q hP hQ hne hs x y hxy hPe haY
      rw [hPe]; exact Finset.insert_subset haY (Finset.singleton_subset_iff.mpr hy)
    · subst a
      have hx := B.equal_pair_no_mixed ht hout P Q hP hQ hne hs y x hxy.symm
        (hPe.trans (Finset.pair_comm x y)) haY
      rw [hPe]; exact Finset.insert_subset hx (Finset.singleton_subset_iff.mpr haY)
  exact (B.block_long_pairs_iff ht P).mp ⟨Finset.mem_powersetCard.mpr ⟨hsub,hPc⟩,hL⟩

theorem equal_long_pairs_block_dichotomy (B : RadiusBlock X tau c k) (ht : 0 < tau)
    (hout : B.OutsideOrthogonal) (P Q : Finset V)
    (hP : P∈X.powersetCard 2) (hQ : Q∈X.powersetCard 2)
    (hne : P≠Q) (hs : (∑x∈P,x)=∑x∈Q,x) (hLP : LongPair tau P) (hLQ : LongPair tau Q) :
    (P∈midpointPairs X tau c ∧ Q∈midpointPairs X tau c) ∨
      (Disjoint P B.vertices ∧ Disjoint Q B.vertices) := by
  classical
  by_cases hp : Disjoint P B.vertices
  · by_cases hq : Disjoint Q B.vertices
    · exact Or.inr ⟨hp,hq⟩
    · have hQm := B.touching_pair_midpoint ht hout Q P hQ hP hne.symm hs.symm hLQ hq
      left
      refine ⟨Finset.mem_filter.mpr ⟨hP,?_,hLP⟩,hQm⟩
      exact hs.trans (Finset.mem_filter.mp hQm).2.1
  · have hPm := B.touching_pair_midpoint ht hout P Q hP hQ hne hs hLP hp
    left
    refine ⟨hPm,Finset.mem_filter.mpr ⟨hQ,?_,hLQ⟩⟩
    exact hs.symm.trans (Finset.mem_filter.mp hPm).2.1

end RadiusBlock
#print axioms RadiusBlock.equal_long_pairs_block_dichotomy
end EnergyForcing.TwoDistance
