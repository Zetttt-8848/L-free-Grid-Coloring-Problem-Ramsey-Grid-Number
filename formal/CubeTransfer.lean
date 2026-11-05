import Mathlib
import SourceCertificates
import Geometry

set_option maxHeartbeats 4000000

namespace EnergyForcing.Cubes

open EnergyForcing.Sources

/-- The paper's four successive separation conditions. -/
def Separated4 (a b c d : ℤ) : Prop :=
  0 < a ∧ 2*a < b ∧ 2*(a+b) < c ∧ 2*(a+b+c) < d

def bit (i : Fin 16) (j : ℕ) : ℤ := ((i.val / 2^j) % 2 : ℕ)

def value (a b c d : ℤ) (i : Fin 16) : ℤ :=
  bit i 0*a + bit i 1*b + bit i 2*c + bit i 3*d

def representative (i : Fin 16) : ℕ :=
  i.val%2 + (i.val/2)%2*3 + (i.val/4)%2*9 + (i.val/8)%2*27

theorem bit_bounds (i : Fin 16) (j : ℕ) : 0 ≤ bit i j ∧ bit i j ≤ 1 := by
  unfold bit
  have := Nat.mod_lt (i.val / 2^j) (by decide : 0 < 2)
  omega

theorem bounded_product (t w : ℤ) (ht : -2 ≤ t ∧ t ≤ 2) (hw : 0 ≤ w) :
    -2*w ≤ t*w ∧ t*w ≤ 2*w :=
  ⟨mul_le_mul_of_nonneg_right ht.1 hw, mul_le_mul_of_nonneg_right ht.2 hw⟩

theorem leading_zero (w s z t : ℤ) (hs : 0 ≤ s) (hw : 2*s < w)
    (ht : -2*s ≤ t ∧ t ≤ 2*s) (he : t + z*w = 0) : z = 0 := by
  have hw0 : 0 ≤ w := by omega
  by_contra hz
  rcases lt_or_gt_of_ne hz with hneg | hpos
  · have hz' : z ≤ -1 := by omega
    have hp := mul_le_mul_of_nonneg_right hz' hw0
    omega
  · have hz' : 1 ≤ z := by omega
    have hp := mul_le_mul_of_nonneg_right hz' hw0
    omega

/-- No relation with coefficients in [-2,2] survives separation. -/
theorem separated_relation (a b c d u v w z : ℤ) (h : Separated4 a b c d)
    (hu : -2 ≤ u ∧ u ≤ 2) (hv : -2 ≤ v ∧ v ≤ 2)
    (hw : -2 ≤ w ∧ w ≤ 2) (hz : -2 ≤ z ∧ z ≤ 2)
    (he : u*a + v*b + w*c + z*d = 0) : u=0 ∧ v=0 ∧ w=0 ∧ z=0 := by
  rcases h with ⟨ha,hb,hc,hd⟩
  have ha0 : 0 ≤ a := by omega
  have hb0 : 0 ≤ b := by omega
  have hc0 : 0 ≤ c := by omega
  have hua := bounded_product u a hu ha0
  have hvb := bounded_product v b hv hb0
  have hwc := bounded_product w c hw hc0
  have ez : z=0 := leading_zero d (a+b+c) z (u*a+v*b+w*c) (by omega) hd (by omega) he
  subst z
  have ew : w=0 := leading_zero c (a+b) w (u*a+v*b) (by omega) hc (by omega) (by simpa using he)
  subst w
  have ev : v=0 := leading_zero b a v (u*a) ha0 hb hua (by simpa using he)
  subst v
  have eu : u=0 := (mul_eq_zero.mp (by simpa using he : u*a=0)).resolve_right (by omega)
  exact ⟨eu,rfl,rfl,rfl⟩

theorem representative_cast (i : Fin 16) :
    (representative i : ℤ) = value 1 3 9 27 i := by
  simp [representative, value, bit]

/-- The finite reference marks list contains precisely these sixteen labels. -/
theorem representative_mem (i : Fin 16) : representative i ∈ fourMarks := by
  fin_cases i <;> decide

theorem representative_strictMono : StrictMono representative := by
  intro i j hij
  fin_cases i <;> fin_cases j <;> norm_num [representative] at *

theorem value_strictMono (a b c d : ℤ) (h : Separated4 a b c d) :
    StrictMono (value a b c d) := by
  intro i j hij
  rcases h with ⟨ha,hb,hc,hd⟩
  fin_cases i <;> fin_cases j <;> norm_num [value, bit] at * <;> omega

/-- Any equality of pair sums in a separated cube holds in the base-three model. -/
theorem pair_sum_transfer (a b c d : ℤ) (h : Separated4 a b c d)
    (i j k l : Fin 16)
    (he : value a b c d i + value a b c d j = value a b c d k + value a b c d l) :
    representative i + representative j = representative k + representative l := by
  have hb0 := bit_bounds i 0; have hb1 := bit_bounds j 0
  have hb2 := bit_bounds k 0; have hb3 := bit_bounds l 0
  have hc0 := bit_bounds i 1; have hc1 := bit_bounds j 1
  have hc2 := bit_bounds k 1; have hc3 := bit_bounds l 1
  have hd0 := bit_bounds i 2; have hd1 := bit_bounds j 2
  have hd2 := bit_bounds k 2; have hd3 := bit_bounds l 2
  have hf0 := bit_bounds i 3; have hf1 := bit_bounds j 3
  have hf2 := bit_bounds k 3; have hf3 := bit_bounds l 3
  have hr := separated_relation a b c d
      (bit i 0+bit j 0-bit k 0-bit l 0)
      (bit i 1+bit j 1-bit k 1-bit l 1)
      (bit i 2+bit j 2-bit k 2-bit l 2)
      (bit i 3+bit j 3-bit k 3-bit l 3) h
      (by omega) (by omega) (by omega) (by omega) (by dsimp [value] at he; linear_combination he)
  have er : (representative i : ℤ) + representative j = representative k + representative l := by
    simp only [representative_cast, value]
    omega
  exact_mod_cast er

/-- All entries used by the reference table are binary, including the unused diagonal. -/
theorem reference_binary : ∀ i j : Fin 16,
    fourColor (representative i) (representative j) < 2 := by decide

def labelColor (i j : Fin 16) : Fin 2 :=
  ⟨fourColor (representative i) (representative j), reference_binary i j⟩

theorem separated_labels_proper (a b c d : ℤ) (h : Separated4 a b c d)
    (i j k l : Fin 16) (hji : value a b c d j < value a b c d i)
    (hik : value a b c d i < value a b c d k)
    (he : value a b c d i + value a b c d l = value a b c d k + value a b c d j) :
    ¬ (labelColor i j = labelColor k j ∧ labelColor k j = labelColor k l) := by
  have hji' : representative j < representative i :=
    representative_strictMono ((value_strictMono a b c d h).lt_iff_lt.mp hji)
  have hik' : representative i < representative k :=
    representative_strictMono ((value_strictMono a b c d h).lt_iff_lt.mp hik)
  have hs := pair_sum_transfer a b c d h i l k j he
  have hk : representative i + (representative k-representative i) = representative k := by omega
  have hl : representative j + (representative k-representative i) = representative l := by omega
  have hc := fourCubeProper (representative i) (representative j)
      (representative k-representative i) (by omega)
      (representative_mem i) (representative_mem j) hji'
      (by rw [hk]; exact representative_mem k)
      (by rw [hl]; exact representative_mem l)
  rw [hk,hl] at hc
  intro hh
  exact hc ⟨congrArg Fin.val hh.1,congrArg Fin.val hh.2⟩

def cube (x a b c d : ℤ) : Finset ℤ :=
  Finset.univ.image fun i : Fin 16 => x + value a b c d i

theorem bits_cover : ∀ e₀ e₁ e₂ e₃ : Fin 2, ∃ i : Fin 16,
    bit i 0=e₀.val ∧ bit i 1=e₁.val ∧ bit i 2=e₂.val ∧ bit i 3=e₃.val := by
  decide

/-- The mask representation is exactly the paper's set of all binary subset sums. -/
theorem mem_cube_iff_binary (x a b c d y : ℤ) : y ∈ cube x a b c d ↔
    ∃ e₀ e₁ e₂ e₃ : Fin 2,
      y = x + (e₀.val:ℤ)*a + (e₁.val:ℤ)*b + (e₂.val:ℤ)*c + (e₃.val:ℤ)*d := by
  constructor
  · intro hy
    obtain ⟨i,_,he⟩ := Finset.mem_image.mp hy
    refine ⟨⟨i.val%2,Nat.mod_lt _ (by decide)⟩,
      ⟨(i.val/2)%2,Nat.mod_lt _ (by decide)⟩,
      ⟨(i.val/4)%2,Nat.mod_lt _ (by decide)⟩,
      ⟨(i.val/8)%2,Nat.mod_lt _ (by decide)⟩,?_⟩
    simp only [value,bit] at he
    norm_num at he ⊢
    omega
  · rintro ⟨e₀,e₁,e₂,e₃,he⟩
    obtain ⟨i,h₀,h₁,h₂,h₃⟩ := bits_cover e₀ e₁ e₂ e₃
    apply Finset.mem_image.mpr
    refine ⟨i,Finset.mem_univ _,?_⟩
    dsimp [value]
    rw [h₀,h₁,h₂,h₃]
    omega

noncomputable def index (x a b c d y : ℤ) : Fin 16 :=
  if h : ∃ i : Fin 16, x + value a b c d i = y then Classical.choose h else 0

theorem index_correct (x a b c d y : ℤ) (hy : y ∈ cube x a b c d) :
    x + value a b c d (index x a b c d y) = y := by
  have he : ∃ i : Fin 16, x + value a b c d i = y := by
    simpa only [cube,Finset.mem_image,Finset.mem_univ,true_and] using hy
  simp only [index,dif_pos he]
  exact Classical.choose_spec he

noncomputable def cubeColor (x a b c d : ℤ) (p : Point) : Fin 2 :=
  labelColor (index x a b c d p.1) (index x a b c d p.2)

/-- Full universal four-cube theorem: the printed table gives a proper binary
    coloring for every separated positive integer quadruple and every integer translate. -/
theorem separated_four_cube (x a b c d : ℤ) (h : Separated4 a b c d) :
    properOn (strictSource fun y => y ∈ cube x a b c d) (cubeColor x a b c d) := by
  intro v u step hstep hp hq hr
  rcases hp with ⟨hv,hu,huv⟩
  rcases hq with ⟨hw,_,_⟩
  rcases hr with ⟨_,ht,_⟩
  have ev := index_correct x a b c d v hv
  have eu := index_correct x a b c d u hu
  have ew := index_correct x a b c d (v+step) hw
  have et := index_correct x a b c d (u+step) ht
  exact separated_labels_proper a b c d h
      (index x a b c d v) (index x a b c d u)
      (index x a b c d (v+step)) (index x a b c d (u+step))
      (by omega) (by omega) (by omega)

theorem cube_card (x a b c d : ℤ) (h : Separated4 a b c d) :
    (cube x a b c d).card = 16 := by
  have hi : Function.Injective (fun i : Fin 16 => x + value a b c d i) := by
    intro i j hij
    apply (value_strictMono a b c d h).injective
    dsimp at hij
    omega
  simp [cube,Finset.card_image_of_injective _ hi]

end EnergyForcing.Cubes
