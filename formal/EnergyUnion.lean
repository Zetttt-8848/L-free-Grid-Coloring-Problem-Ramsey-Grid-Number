import SourceCounting
import Mathlib

set_option autoImplicit false

namespace EnergyForcing.EnergyUnion

open Finset
open scoped BigOperators
open EnergyForcing.Counting

def crossPairs (X Y : Finset ℤ) (d : ℤ) :=
  (X.product Y).filter (fun p => p.2-p.1=d)
def crossCount (X Y : Finset ℤ) (d : ℤ) := (crossPairs X Y d).card
def mixedQuads (X Y : Finset ℤ) :=
  ((X.product Y).product (X.product Y)).filter (fun p => p.1.2-p.1.1=p.2.2-p.2.1)

theorem mem_crossPairs (X Y : Finset ℤ) (d x y : ℤ) :
    (x,y)∈crossPairs X Y d ↔ x∈X ∧ y∈Y ∧ y-x=d := by simp [crossPairs,and_assoc]

theorem mem_mixedQuads (X Y : Finset ℤ) (x y u v : ℤ) :
    ((x,y),(u,v))∈mixedQuads X Y ↔ x∈X ∧ y∈Y ∧ u∈X ∧ v∈Y ∧ y-x=v-u := by
  simp [mixedQuads,and_assoc]

theorem allDiffs_mono (X A : Finset ℤ) (h : X ⊆ A) : allDiffs X ⊆ allDiffs A := by
  intro d hd
  rcases (mem_allDiffs X d).mp hd with hd|⟨u,hu,hud⟩
  · exact (mem_allDiffs A d).mpr (Or.inl hd)
  · exact (mem_allDiffs A d).mpr (Or.inr ⟨u,h hu,h hud⟩)

theorem r_zero_outside (X : Finset ℤ) (d : ℤ) (hd : d∉allDiffs X) : r X d=0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro u hu
  exact hd ((mem_allDiffs X d).mpr (Or.inr ⟨u,(mem_positiveFiber X d u).mp hu⟩))

theorem energy_sum_on (X A : Finset ℤ) (h : X ⊆ A) :
    (∑d∈allDiffs A,(r X d : ℝ)^2)=(E X : ℝ) := by
  have he : (∑d∈allDiffs X,(r X d : ℝ)^2)=(E X : ℝ) := by exact_mod_cast (energy_all_count X).symm
  rw [← he]
  symm
  apply Finset.sum_subset (allDiffs_mono X A h)
  intro d hd hnot
  simp [r_zero_outside X d hnot]

theorem cross_square_fiber (X Y : Finset ℤ) (d : ℤ) :
    ((mixedQuads X Y).filter (fun p => p.1.2-p.1.1=d)).card=(crossCount X Y d)^2 := by
  rw [crossCount,pow_two,← Finset.card_product]
  congr 1
  ext p
  rcases p with ⟨⟨x,y⟩,⟨u,v⟩⟩
  simp only [Finset.mem_filter,mem_mixedQuads,Finset.product_eq_sprod,
    Finset.mem_product,mem_crossPairs]
  constructor
  · rintro ⟨⟨hx,hy,hu,hv,he⟩,hd⟩
    exact ⟨⟨hx,hy,hd⟩,⟨hu,hv,by omega⟩⟩
  · rintro ⟨⟨hx,hy,hd⟩,⟨hu,hv,hd'⟩⟩
    exact ⟨⟨hx,hy,hu,hv,by omega⟩,hd⟩

theorem common_difference_fiber (X Y : Finset ℤ) (d : ℤ) :
    ((mixedQuads X Y).filter (fun p => p.2.1-p.1.1=d)).card=r X d*r Y d := by
  unfold r
  rw [← Finset.card_product]
  refine Finset.card_nbij' (fun p : (ℤ×ℤ)×(ℤ×ℤ) => (p.1.1,p.1.2))
    (fun p : ℤ×ℤ => ((p.1,p.2),(p.1+d,p.2+d))) ?_ ?_ ?_ ?_
  · rintro ⟨⟨x,y⟩,⟨u,v⟩⟩ hp
    simp only [Finset.mem_filter,mem_mixedQuads] at hp
    simp only [Finset.product_eq_sprod,Finset.mem_product,mem_positiveFiber]
    refine ⟨⟨hp.1.1,?_⟩,⟨hp.1.2.1,?_⟩⟩
    · convert hp.1.2.2.1 using 1 <;> omega
    · convert hp.1.2.2.2.1 using 1 <;> omega
  · rintro ⟨x,y⟩ hp
    simp only [Finset.product_eq_sprod,Finset.mem_product,mem_positiveFiber] at hp
    simp only [Finset.mem_filter,mem_mixedQuads]
    exact ⟨⟨hp.1.1,hp.2.1,hp.1.2,hp.2.2,by omega⟩,by omega⟩
  · rintro ⟨⟨x,y⟩,⟨u,v⟩⟩ hp
    simp only [Finset.mem_filter,mem_mixedQuads] at hp
    apply Prod.ext
    · rfl
    · apply Prod.ext <;> dsimp <;> omega
  · intros; rfl

theorem cross_square_identity (X Y A : Finset ℤ) (hX : X ⊆ A) (hY : Y ⊆ A) :
    (∑d∈allDiffs A,(crossCount X Y d)^2)=∑d∈allDiffs A,r X d*r Y d := by
  have hleft := Finset.card_eq_sum_card_fiberwise (s:=mixedQuads X Y) (t:=allDiffs A)
    (f:=fun p => p.1.2-p.1.1) (by
      rintro ⟨⟨x,y⟩,⟨u,v⟩⟩ hp
      have hh := (mem_mixedQuads X Y x y u v).mp hp
      exact (mem_allDiffs A (y-x)).mpr (Or.inr ⟨x,hX hh.1,by simpa using hY hh.2.1⟩))
  have hright := Finset.card_eq_sum_card_fiberwise (s:=mixedQuads X Y) (t:=allDiffs A)
    (f:=fun p => p.2.1-p.1.1) (by
      rintro ⟨⟨x,y⟩,⟨u,v⟩⟩ hp
      have hh := (mem_mixedQuads X Y x y u v).mp hp
      exact (mem_allDiffs A (u-x)).mpr (Or.inr ⟨x,hX hh.1,by simpa using hX hh.2.2.1⟩))
  simp_rw [cross_square_fiber] at hleft
  simp_rw [common_difference_fiber] at hright
  exact hleft.symm.trans hright

theorem cross_square_cauchy (X Y A : Finset ℤ) (hX : X ⊆ A) (hY : Y ⊆ A) :
    (∑d∈allDiffs A,(crossCount X Y d : ℝ)^2)^2 ≤ (E X : ℝ)*(E Y : ℝ) := by
  have hid : (∑d∈allDiffs A,(crossCount X Y d : ℝ)^2)=
      ∑d∈allDiffs A,(r X d : ℝ)*(r Y d : ℝ) := by exact_mod_cast cross_square_identity X Y A hX hY
  rw [hid]
  have hh := Finset.sum_mul_sq_le_sq_mul_sq (R:=ℝ) (allDiffs A)
    (fun d => (r X d : ℝ)) (fun d => (r Y d : ℝ))
  rwa [energy_sum_on X A hX,energy_sum_on Y A hY] at hh

theorem crossCount_sum (X Y : Finset ℤ) (d : ℤ) :
    crossCount X Y d=∑x∈X,∑y∈Y,if y-x=d then 1 else 0 := by
  simp only [crossCount,crossPairs,Finset.card_eq_sum_ones,Finset.sum_filter,
    Finset.product_eq_sprod,Finset.sum_product]

theorem union_difference (X Y : Finset ℤ) (hXY : Disjoint X Y) (d : ℤ) :
    r (X∪Y) d=r X d+r Y d+crossCount X Y d+crossCount Y X d := by
  have hself (S : Finset ℤ) : r S d=crossCount S S d := r_eq_card_difference_pairs S d
  simp_rw [hself,crossCount_sum]
  rw [Finset.sum_union hXY]
  simp_rw [Finset.sum_union hXY,Finset.sum_add_distrib]
  omega

noncomputable def l2 (D : Finset ℤ) (f : ℤ → ℝ) : ℝ := Real.sqrt (∑d∈D,(f d)^2)

theorem l2_add (D : Finset ℤ) (f g : ℤ → ℝ) : l2 D (fun d => f d+g d) ≤ l2 D f+l2 D g := by
  let v : (ℤ → ℝ) → EuclideanSpace ℝ D := fun h => (WithLp.equiv 2 (D → ℝ)).symm (fun d => h d)
  have hn (h : ℤ → ℝ) : ‖v h‖=l2 D h := by
    rw [EuclideanSpace.norm_eq]
    simp [v,l2,Real.norm_eq_abs,sq_abs]
    congr 1
    exact Finset.sum_attach D (fun d => (h d)^2)
  have ha : v (fun d => f d+g d)=v f+v g := by ext d; rfl
  rw [← hn,ha]
  have hh := norm_add_le (v f) (v g)
  rwa [hn f,hn g] at hh

theorem l2_cross_bound (X Y A : Finset ℤ) (hX : X ⊆ A) (hY : Y ⊆ A) :
    l2 (allDiffs A) (fun d => (crossCount X Y d : ℝ)) ≤
      Real.sqrt (Real.sqrt (E X : ℝ))*Real.sqrt (Real.sqrt (E Y : ℝ)) := by
  have hc := cross_square_cauchy X Y A hX hY
  have hs : (∑d∈allDiffs A,(crossCount X Y d : ℝ)^2) ≤ Real.sqrt ((E X : ℝ)*(E Y : ℝ)) :=
    Real.le_sqrt_of_sq_le hc
  have hh := Real.sqrt_le_sqrt hs
  rw [Real.sqrt_mul (by positivity),Real.sqrt_mul (Real.sqrt_nonneg _)] at hh
  exact hh

/-- The actual fourth-root energy triangle inequality, written with nested roots. -/
theorem energy_fourth_root_triangle (X Y : Finset ℤ) (hXY : Disjoint X Y) :
    Real.sqrt (Real.sqrt (E (X∪Y) : ℝ)) ≤
      Real.sqrt (Real.sqrt (E X : ℝ))+Real.sqrt (Real.sqrt (E Y : ℝ)) := by
  let D := allDiffs (X∪Y)
  let f := fun d => (r X d : ℝ)
  let g := fun d => (r Y d : ℝ)
  let q := fun d => (crossCount X Y d : ℝ)
  let q' := fun d => (crossCount Y X d : ℝ)
  have hsum : (fun d => (r (X∪Y) d : ℝ))=(fun d => f d+g d+q d+q' d) := by
    funext d
    dsimp [f,g,q,q']
    exact_mod_cast union_difference X Y hXY d
  have hnorm : Real.sqrt (E (X∪Y) : ℝ) ≤ l2 D f+l2 D g+l2 D q+l2 D q' := by
    have hh := l2_add D (fun d => f d+g d+q d) q'
    have hh' := l2_add D (fun d => f d+g d) q
    have hh'' := l2_add D f g
    have he : Real.sqrt (E (X∪Y) : ℝ)=l2 D (fun d => (r (X∪Y) d : ℝ)) := by
      unfold l2
      rw [energy_sum_on (X∪Y) (X∪Y) (Finset.Subset.refl _)]
    rw [he,hsum]
    linarith
  have hf : l2 D f=Real.sqrt (E X : ℝ) := by unfold l2; rw [energy_sum_on X (X∪Y) Finset.subset_union_left]
  have hg : l2 D g=Real.sqrt (E Y : ℝ) := by unfold l2; rw [energy_sum_on Y (X∪Y) Finset.subset_union_right]
  have hq := l2_cross_bound X Y (X∪Y) Finset.subset_union_left Finset.subset_union_right
  have hq' := l2_cross_bound Y X (X∪Y) Finset.subset_union_right Finset.subset_union_left
  rw [hf,hg] at hnorm
  have hsx := Real.sq_sqrt (Real.sqrt_nonneg (E X : ℝ))
  have hsy := Real.sq_sqrt (Real.sqrt_nonneg (E Y : ℝ))
  apply (Real.sqrt_le_left (by positivity)).mpr
  dsimp [D,q,q'] at hnorm ⊢
  nlinarith

end EnergyForcing.EnergyUnion
