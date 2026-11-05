import EnergyUnion
import EnergyMomentLower

set_option autoImplicit false

namespace EnergyForcing.Translation

open Finset
open scoped BigOperators
open EnergyForcing.Counting
open EnergyForcing.EnergyUnion

def translate (B : Finset ℤ) (d : ℤ) := B.image (fun x => x+d)

theorem mem_translate (B : Finset ℤ) (d x : ℤ) : x∈translate B d ↔ x-d∈B := by
  simp only [translate,Finset.mem_image]
  constructor
  · rintro ⟨y,hy,rfl⟩; simpa using hy
  · intro hx; exact ⟨x-d,hx,by omega⟩

theorem translate_card (B : Finset ℤ) (d : ℤ) : (translate B d).card=B.card := by
  exact Finset.card_image_of_injective _ (fun x y h => by omega)

theorem r_translate (B : Finset ℤ) (d t : ℤ) : r (translate B d) t=r B t := by
  unfold r
  refine Finset.card_nbij' (fun x : ℤ => x-d) (fun x : ℤ => x+d) ?_ ?_ ?_ ?_
  · intro x hx
    simp only [mem_positiveFiber,mem_translate] at hx ⊢
    exact ⟨hx.1,by convert hx.2 using 1 <;> omega⟩
  · intro x hx
    simp only [mem_positiveFiber,mem_translate] at hx ⊢
    exact ⟨by simpa using hx.1, by convert hx.2 using 1 <;> omega⟩
  · intros; dsimp; omega
  · intros; dsimp; omega

theorem cross_translate (X Y : Finset ℤ) (a b t : ℤ) :
    EnergyUnion.crossCount (translate X a) (translate Y b) t=
      EnergyUnion.crossCount X Y (t+a-b) := by
  unfold EnergyUnion.crossCount
  refine Finset.card_nbij' (fun p : ℤ×ℤ => (p.1-a,p.2-b))
    (fun p : ℤ×ℤ => (p.1+a,p.2+b)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y⟩ hp
    simp only [mem_crossPairs,mem_translate] at hp ⊢
    exact ⟨hp.1,hp.2.1,by omega⟩
  · rintro ⟨x,y⟩ hp
    simp only [mem_crossPairs,mem_translate] at hp ⊢
    exact ⟨by simpa using hp.1,by simpa using hp.2.1,by omega⟩
  · rintro ⟨x,y⟩ _; simp
  · rintro ⟨x,y⟩ _; simp

theorem translate_zero (B : Finset ℤ) : translate B 0=B := by simp [translate]

theorem doubled_difference (B : Finset ℤ) (d t : ℤ) (hd : Disjoint B (translate B d)) :
    r (B∪translate B d) t=2*r B t+r B (t-d)+r B (t+d) := by
  rw [union_difference B (translate B d) hd,r_translate]
  have h₁ := cross_translate B B 0 d t
  have h₂ := cross_translate B B d 0 t
  simp only [translate_zero,add_zero,sub_zero] at h₁ h₂
  rw [h₁,h₂]
  change r B t+r B t+((B.product B).filter (fun p => p.2-p.1=t-d)).card+
    ((B.product B).filter (fun p => p.2-p.1=t+d)).card = _
  rw [← r_eq_card_difference_pairs,← r_eq_card_difference_pairs]
  omega

noncomputable def correlation (B : Finset ℤ) (h : ℤ) : ℝ :=
  ∑'t : ℤ,(r B t : ℝ)*(r B (t+h) : ℝ)

theorem summable_shift_product (B : Finset ℤ) (a b : ℤ) :
    Summable (fun t : ℤ => (r B (t+a) : ℝ)*(r B (t+b) : ℝ)) := by
  apply summable_of_ne_finset_zero (s:=(allDiffs B).image (fun u => u-a))
  intro t ht
  have hn : t+a∉allDiffs B := by
    intro h
    exact ht (Finset.mem_image.mpr ⟨t+a,h,by omega⟩)
  simp [r_zero_outside B (t+a) hn]

theorem correlation_sum (B : Finset ℤ) (h : ℤ) :
    correlation B h=∑t∈allDiffs B,(r B t : ℝ)*(r B (t+h) : ℝ) := by
  apply tsum_eq_sum
  intro t ht
  simp [r_zero_outside B t ht]

theorem shift_product_sum (B : Finset ℤ) (a b : ℤ) :
    (∑'t : ℤ,(r B (t+a) : ℝ)*(r B (t+b) : ℝ))=correlation B (b-a) := by
  have hh := (Equiv.addRight a).tsum_eq (fun t : ℤ => (r B t : ℝ)*(r B (t+(b-a)) : ℝ))
  simpa [correlation,add_sub_assoc,add_sub_cancel_left] using hh

theorem correlation_neg (B : Finset ℤ) (h : ℤ) : correlation B (-h)=correlation B h := by
  have hh := (Equiv.neg ℤ).tsum_eq (fun t : ℤ => (r B t : ℝ)*(r B (t+(-h)) : ℝ))
  have hp (t : ℤ) : (r B (-t) : ℝ)*(r B (-t+-h) : ℝ)=(r B t : ℝ)*(r B (t+h) : ℝ) := by
    rw [show -t+-h=-(t+h) by omega,r_neg,r_neg]
  simpa only [Equiv.neg_apply,hp,correlation] using hh.symm

theorem correlation_zero (B : Finset ℤ) : correlation B 0=(E B : ℝ) := by
  rw [correlation_sum]
  simp only [add_zero,← pow_two]
  exact energy_sum_on B B (Finset.Subset.refl _)

theorem energy_tsum (B : Finset ℤ) :
    (E B : ℝ)=∑'t : ℤ,(r B t : ℝ)^2 := by
  rw [← correlation_zero B]
  simp only [correlation,add_zero,pow_two]

theorem doubled_energy (B : Finset ℤ) (d : ℤ) (hd : Disjoint B (translate B d)) :
    (E (B∪translate B d) : ℝ)=6*(E B : ℝ)+8*correlation B d+2*correlation B (2*d) := by
  have he (t : ℤ) : (r (B∪translate B d) t : ℝ)^2=
      4*((r B t : ℝ)*(r B t : ℝ))+
      (r B (t-d) : ℝ)*(r B (t-d) : ℝ)+
      (r B (t+d) : ℝ)*(r B (t+d) : ℝ)+
      4*((r B t : ℝ)*(r B (t-d) : ℝ))+
      4*((r B t : ℝ)*(r B (t+d) : ℝ))+
      2*((r B (t-d) : ℝ)*(r B (t+d) : ℝ)) := by
    rw [doubled_difference B d t hd]
    push_cast
    ring
  have h₁ := (summable_shift_product B 0 0).mul_left 4
  have h₂ := summable_shift_product B (-d) (-d)
  have h₃ := summable_shift_product B d d
  have h₄ := (summable_shift_product B 0 (-d)).mul_left 4
  have h₅ := (summable_shift_product B 0 d).mul_left 4
  have h₆ := (summable_shift_product B (-d) d).mul_left 2
  simp only [add_zero,← sub_eq_add_neg] at h₁ h₂ h₄ h₅ h₆
  rw [energy_tsum]
  simp_rw [he]
  rw [Summable.tsum_add ((((h₁.add h₂).add h₃).add h₄).add h₅) h₆,
    Summable.tsum_add (((h₁.add h₂).add h₃).add h₄) h₅,
    Summable.tsum_add ((h₁.add h₂).add h₃) h₄,
    Summable.tsum_add (h₁.add h₂) h₃, Summable.tsum_add h₁ h₂]
  simp only [tsum_mul_left,sub_eq_add_neg]
  have h₀ := shift_product_sum B 0 0
  have h0m := shift_product_sum B 0 (-d)
  have h0p := shift_product_sum B 0 d
  simp only [add_zero,sub_zero,sub_self] at h₀ h0m h0p
  rw [h₀,shift_product_sum B (-d) (-d),shift_product_sum B d d,h0m,h0p,
    shift_product_sum B (-d) d]
  simp only [sub_self,sub_neg_eq_add,correlation_neg,correlation_zero]
  rw [show d+d=2*d by ring]
  ring

theorem golomb_r_nonzero (B : Finset ℤ) (hB : Golomb (·∈B)) (t : ℤ) (ht : t≠0) : r B t ≤ 1 := by
  by_cases hp : 0<t
  · exact golomb_r_le_one B hB t hp
  · have hh := golomb_r_le_one B hB (-t) (by omega)
    simpa only [r_neg] using hh

/-- This slightly weaker correlation bound avoids a largest-difference exception
and is sufficient for the complete matching theorem. -/
theorem golomb_correlation_bound (B : Finset ℤ) (hB : Golomb (·∈B))
    (h : ℤ) (hh : 0<h) :
    correlation B h ≤ (B.card : ℝ)^2-B.card+2*(B.card : ℝ)*(r B h : ℝ) := by
  have hp (t : ℤ) : r B t*r B (t+h)+(if t=0 then B.card else 0) ≤
      r B t+(if t=0 then B.card*r B h else 0)+(if t=-h then B.card*r B h else 0) := by
    by_cases hz : t=0
    · subst t; simp [r_zero,ne_of_gt hh,ne_of_lt (neg_neg_of_pos hh)]; omega
    · by_cases hn : t=-h
      · subst t; simp [r_neg,r_zero,ne_of_lt (neg_neg_of_pos hh)]; nlinarith
      · have hb := golomb_r_nonzero B hB (t+h) (by omega)
        simp only [if_neg hz,if_neg hn,add_zero]
        nlinarith
  have hs := Finset.sum_le_sum (fun t (_ : t∈allDiffs B) => hp t)
  have hz : (0 : ℤ)∈allDiffs B := (mem_allDiffs B 0).mpr (Or.inl rfl)
  simp only [Finset.sum_add_distrib,Finset.sum_ite_eq',if_pos hz,all_diff_mass] at hs
  have hbound : (∑t∈allDiffs B,r B t*r B (t+h))+B.card ≤
      B.card^2+2*B.card*r B h := by
    by_cases hn : -h∈allDiffs B <;> simp [hn] at hs <;> nlinarith
  rw [correlation_sum]
  have hboundR : (∑t∈allDiffs B,(r B t : ℝ)*(r B (t+h) : ℝ))+(B.card : ℝ) ≤
      (B.card : ℝ)^2+2*(B.card : ℝ)*(r B h : ℝ) := by exact_mod_cast hbound
  linarith

theorem golomb_energy (B : Finset ℤ) (hB : Golomb (·∈B)) :
    (E B : ℝ)=2*(B.card : ℝ)^2-B.card := by
  have ht : T B=0 := by
    rw [corner_count]
    apply Finset.sum_eq_zero
    intro t ht
    have hr := golomb_r_le_one B hB t ((mem_posDiffs B t).mp ht).1
    exact Nat.choose_eq_zero_of_lt (by omega)
  have he := energy_count B
  rw [sum_r_sq,ht] at he
  have hp := square_eq_self_add_twice_choose B.card
  have heR : (E B : ℝ)=(B.card : ℝ)^2+2*(M B : ℝ) := by exact_mod_cast he
  have hpR : (B.card : ℝ)^2=(B.card : ℝ)+2*(M B : ℝ) := by exact_mod_cast hp
  linarith

theorem disjoint_translation_r_zero (B : Finset ℤ) (d : ℤ) (hd : Disjoint B (translate B d)) :
    r B d=0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro u hu
  have hh := (mem_positiveFiber B d u).mp hu
  exact Finset.disjoint_left.mp hd hh.2 ((mem_translate B d (u+d)).mpr (by simpa using hh.1))

theorem doubled_golomb_energy (B : Finset ℤ) (hB : Golomb (·∈B)) (d : ℤ)
    (hd : 0<d) (hdis : Disjoint B (translate B d)) :
    (E (B∪translate B d) : ℝ) ≤ 22*(B.card : ℝ)^2-12*B.card := by
  have h₁ := golomb_correlation_bound B hB d hd
  have h₂ := golomb_correlation_bound B hB (2*d) (by omega)
  have hz := disjoint_translation_r_zero B d hdis
  rw [hz,Nat.cast_zero,mul_zero,add_zero] at h₁
  have hr : (r B (2*d) : ℝ) ≤ 1 := by exact_mod_cast golomb_r_le_one B hB (2*d) (by omega)
  have hm := mul_le_mul_of_nonneg_left hr (show 0 ≤ 2*(B.card : ℝ) by positivity)
  rw [doubled_energy B d hdis,golomb_energy B hB]
  nlinarith

end EnergyForcing.Translation
