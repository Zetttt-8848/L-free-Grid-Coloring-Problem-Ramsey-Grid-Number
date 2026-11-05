import CubeOccupancy
import ForcingCounting

set_option maxHeartbeats 4000000

namespace EnergyForcing.ThreeCube

open EnergyForcing.Counting EnergyForcing.FiberDominance EnergyForcing.Forcing
open EnergyForcing.Capacity
open scoped BigOperators

def mixedCorners (A : Finset ℤ) (z : Point → Bool) : Finset (ℤ×ℤ×ℤ) :=
  (sourceCorners A).filter fun p => z (p.1,p.2.1)≠z (p.2.2,p.2.1+p.2.2-p.1)

def mixedCount (A : Finset ℤ) (z : Point → Bool) : ℕ := (mixedCorners A z).card

theorem mixed_partition (A : Finset ℤ) (z : Point → Bool) :
    F A z+mixedCount A z=T A := by
  exact Finset.filter_card_add_filter_neg_card_eq_card
    (s := sourceCorners A) (fun p => z (p.1,p.2.1)=z (p.2.2,p.2.1+p.2.2-p.1))

theorem choose_two_add (b c : ℕ) :
    (b+c).choose 2=b.choose 2+c.choose 2+b*c := by
  have hb := square_eq_self_add_twice_choose b
  have hc := square_eq_self_add_twice_choose c
  have hbc := square_eq_self_add_twice_choose (b+c)
  nlinarith

theorem mixed_fiber_count (A : Finset ℤ) (z : Point → Bool) :
    mixedCount A z=∑ d∈posDiffs A,
      (fiberClass A z d false).card*(fiberClass A z d true).card := by
  have ht : T A=F A z+∑ d∈posDiffs A,
      (fiberClass A z d false).card*(fiberClass A z d true).card := by
    rw [corner_count,forcing_count,← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro d hd
    rw [← class_partition A z d,choose_two_add]
    rfl
  have hp := mixed_partition A z
  omega

theorem four_fiber_not_uniform (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource (fun n => n∈A)) z) (d x t s : ℤ)
    (hd : 0<d) (ht : 0<t) (hs : 0<s)
    (h₀ : x∈positiveFiber A d) (h₁ : x+t∈positiveFiber A d)
    (h₂ : x+s∈positiveFiber A d) (h₃ : x+t+s∈positiveFiber A d)
    (c : Bool) (hc : ∀ u∈positiveFiber A d, z (u+d,u)=c) : False := by
  have hg := fiber_class_golomb (fun n => n∈A) z hz d hd c
  have h := hg x (x+t) (x+s) (x+t+s)
    ⟨(mem_positiveFiber A d x).mp h₀,hc x h₀⟩
    ⟨(mem_positiveFiber A d (x+t)).mp h₁,hc (x+t) h₁⟩
    ⟨(mem_positiveFiber A d (x+s)).mp h₂,hc (x+s) h₂⟩
    ⟨(mem_positiveFiber A d (x+t+s)).mp h₃,hc (x+t+s) h₃⟩
    (by omega) (by omega) (by omega)
  have := h.1
  omega

theorem four_fiber_product (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource (fun n => n∈A)) z) (d x t s : ℤ)
    (hd : 0<d) (ht : 0<t) (hs : 0<s) (hts : t≠s)
    (h₀ : x∈positiveFiber A d) (h₁ : x+t∈positiveFiber A d)
    (h₂ : x+s∈positiveFiber A d) (h₃ : x+t+s∈positiveFiber A d) :
    3≤(fiberClass A z d false).card*(fiberClass A z d true).card := by
  have hpos : ∀ c : Bool, 0<(fiberClass A z d c).card := by
    intro c
    apply Finset.card_pos.mpr
    by_contra hn
    have hempty := Finset.not_nonempty_iff_eq_empty.mp hn
    apply four_fiber_not_uniform A z hz d x t s hd ht hs h₀ h₁ h₂ h₃ (!c)
    intro u hu
    apply bool_eq_not_of_ne
    intro he
    have hm : u∈fiberClass A z d c := Finset.mem_filter.mpr ⟨hu,he⟩
    rw [hempty] at hm
    simpa using hm
  let S : Finset ℤ := {x,x+t,x+s,x+t+s}
  have hcard : S.card=4 := by
    simp [S,show x≠x+t by omega,show x≠x+s by omega,
      show x≠x+t+s by omega,show x+t≠x+s by omega,
      show x+t≠x+t+s by omega,show x+s≠x+t+s by omega]
  have hsub : S⊆positiveFiber A d := by
    intro u hu
    simp only [S,Finset.mem_insert,Finset.mem_singleton] at hu
    rcases hu with rfl | rfl | rfl | rfl <;> assumption
  have hr : 4≤r A d := by
    have h := Finset.card_le_card hsub
    simpa only [hcard,r] using h
  have hc := class_partition A z d
  have hb := hpos false
  have ht' := hpos true
  by_cases hb3 : 3≤(fiberClass A z d false).card
  · nlinarith
  · have hcases : (fiberClass A z d false).card=1 ∨
        (fiberClass A z d false).card=2 := by omega
    rcases hcases with h | h
    · have hc' := hc
      rw [h] at hc'
      rw [h]
      nlinarith
    · have hc' := hc
      rw [h] at hc'
      rw [h]
      nlinarith

def unitLabel {d : ℕ} (i : Fin d) : Label d := fun j => decide (j=i)

theorem integerValue_unit {d : ℕ} (a : ℤ) (w : Fin d → ℤ) (i : Fin d) :
    integerValue a w (unitLabel i)=a+w i := by
  simp [integerValue,unitLabel,bitZ]

theorem generator_injective {d : ℕ} (a : ℤ) (w : Fin d → ℤ)
    (hinj : Function.Injective (integerValue a w)) : Function.Injective w := by
  intro i j he
  have hv : integerValue a w (unitLabel i)=integerValue a w (unitLabel j) := by
    simp only [integerValue_unit,he]
  have hl := congrFun (hinj hv) i
  simpa [unitLabel] using hl

theorem cube_vertex_three (a : ℤ) (w : Fin 3 → ℤ) (b₀ b₁ b₂ : Bool) :
    a+bitZ b₀*w 0+bitZ b₁*w 1+bitZ b₂*w 2∈integerCube a w := by
  apply Finset.mem_image.mpr
  refine ⟨![b₀,b₁,b₂],Finset.mem_univ _,?_⟩
  simp [integerValue,Fin.sum_univ_succ]
  ring

theorem generator_fiber_product (a : ℤ) (w : Fin 3 → ℤ)
    (hw : ∀ i,0<w i) (hinj : Function.Injective (integerValue a w))
    (z : Point → Bool) (hz : properOn (strictSource (fun n => n∈integerCube a w)) z)
    (i : Fin 3) :
    3≤(fiberClass (integerCube a w) z (w i) false).card*
      (fiberClass (integerCube a w) z (w i) true).card := by
  have h000 := cube_vertex_three a w false false false
  have h001 := cube_vertex_three a w true false false
  have h010 := cube_vertex_three a w false true false
  have h011 := cube_vertex_three a w true true false
  have h100 := cube_vertex_three a w false false true
  have h101 := cube_vertex_three a w true false true
  have h110 := cube_vertex_three a w false true true
  have h111 := cube_vertex_three a w true true true
  norm_num [bitZ] at h000 h001 h010 h011 h100 h101 h110 h111
  have hi := generator_injective a w hinj
  have h01 : w 0≠w 1 := fun h => (by decide : (0:Fin 3)≠1) (hi h)
  have h02 : w 0≠w 2 := fun h => (by decide : (0:Fin 3)≠2) (hi h)
  have h12 : w 1≠w 2 := fun h => (by decide : (1:Fin 3)≠2) (hi h)
  fin_cases i
  · apply four_fiber_product (integerCube a w) z hz (w 0) a (w 1) (w 2)
      (hw 0) (hw 1) (hw 2) h12
    all_goals apply (mem_positiveFiber _ _ _).mpr
    all_goals constructor <;> first | assumption |
      (simpa [add_assoc,add_comm,add_left_comm] using h011) |
      (simpa [add_assoc,add_comm,add_left_comm] using h101) |
      (simpa [add_assoc,add_comm,add_left_comm] using h111)
  · apply four_fiber_product (integerCube a w) z hz (w 1) a (w 0) (w 2)
      (hw 1) (hw 0) (hw 2) h02
    all_goals apply (mem_positiveFiber _ _ _).mpr
    all_goals constructor <;> first | assumption |
      (simpa [add_assoc,add_comm,add_left_comm] using h011) |
      (simpa [add_assoc,add_comm,add_left_comm] using h110) |
      (simpa [add_assoc,add_comm,add_left_comm] using h111)
  · apply four_fiber_product (integerCube a w) z hz (w 2) a (w 0) (w 1)
      (hw 2) (hw 0) (hw 1) h01
    all_goals apply (mem_positiveFiber _ _ _).mpr
    all_goals constructor <;> first | assumption |
      (simpa [add_assoc,add_comm,add_left_comm] using h101) |
      (simpa [add_assoc,add_comm,add_left_comm] using h110) |
      (simpa [add_assoc,add_comm,add_left_comm] using h111)

theorem injective_three_cube_nine (a : ℤ) (w : Fin 3 → ℤ)
    (hw : ∀ i,0<w i) (hinj : Function.Injective (integerValue a w))
    (z : Point → Bool) (hz : properOn (strictSource (fun n => n∈integerCube a w)) z) :
    9 ≤ mixedCount (integerCube a w) z := by
  let G := Finset.univ.image w
  have hcard : G.card=3 := by
    simp [G,Finset.card_image_of_injective _ (generator_injective a w hinj)]
  have hsub : G⊆posDiffs (integerCube a w) := by
    intro d hd
    obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hd
    apply (mem_posDiffs (integerCube a w) (w i)).mpr
    refine ⟨hw i,a,?_,?_⟩
    · apply Finset.mem_image.mpr
      exact ⟨(fun _ => false),Finset.mem_univ _,by simp [integerValue,bitZ]⟩
    · apply Finset.mem_image.mpr
      exact ⟨unitLabel i,Finset.mem_univ _,integerValue_unit a w i⟩
  rw [mixed_fiber_count]
  calc
    9 = ∑ d∈G, (3:ℕ) := by simp [hcard]
    _ ≤ ∑ d∈G, (fiberClass (integerCube a w) z d false).card*
        (fiberClass (integerCube a w) z d true).card := by
      apply Finset.sum_le_sum
      intro d hd
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hd
      exact generator_fiber_product a w hw hinj z hz i
    _ ≤ _ := Finset.sum_le_sum_of_subset_of_nonneg hsub (by intros; exact Nat.zero_le _)

#print axioms injective_three_cube_nine

end EnergyForcing.ThreeCube
