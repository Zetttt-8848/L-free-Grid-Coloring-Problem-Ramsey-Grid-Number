import ThreeCubeMixedCollisions
import SourceCertificates

set_option maxRecDepth 100000
set_option maxHeartbeats 40000000

namespace EnergyForcing.ThreeCube

open EnergyForcing.Counting EnergyForcing.Forcing EnergyForcing.Capacity
open scoped BigOperators

def referenceMark (v : Label 3) : ℕ := ∑ i, if v i then 3^i.val else 0

/-- The displayed three-cube table is used as a rule on unordered label pairs. -/
def templateColor (v u : Label 3) : Bool :=
  decide (EnergyForcing.Sources.threeColor (max (referenceMark v) (referenceMark u))
    (min (referenceMark v) (referenceMark u))=1)

theorem template_symmetric (v u : Label 3) : templateColor v u=templateColor u v := by
  simp only [templateColor,max_comm,min_comm]

def CoordinateLe (v u : Label 3) : Prop := ∀ i, bitZ (v i) ≤ bitZ (u i)

def CoordinateBalance (p : (Label 3 × Label 3) × (Label 3 × Label 3)) : Prop :=
  ∀ i, bitZ (p.1.1 i)-bitZ (p.1.2 i)=bitZ (p.2.1 i)-bitZ (p.2.2 i)

instance coordinateLe_decidable (v u : Label 3) : Decidable (CoordinateLe v u) := by
  unfold CoordinateLe
  infer_instance

instance coordinateBalance_decidable (p : (Label 3 × Label 3) × (Label 3 × Label 3)) :
    Decidable (CoordinateBalance p) := by
  unfold CoordinateBalance
  infer_instance

def labelEnergy : Finset ((Label 3 × Label 3) × (Label 3 × Label 3)) :=
  Finset.univ.filter CoordinateBalance

def labelMixed : Finset ((Label 3 × Label 3) × (Label 3 × Label 3)) :=
  labelEnergy.filter fun p => p.1.1≠p.1.2 ∧
    templateColor p.1.1 p.1.2≠templateColor p.2.1 p.2.2

/-- All4096 label quadruples are checked by the kernel. A monochromatic candidate
    violates one of the two strict inequalities of a positive corner. -/
theorem template_bad_order : ∀ i j k l : Label 3,
    CoordinateBalance ((i,j),(k,l)) →
    (templateColor i j=templateColor k j ∧ templateColor k j=templateColor k l) →
    CoordinateLe i j ∨ CoordinateLe k i := by decide

theorem label_energy_card : labelEnergy.card=216 := by decide
theorem label_mixed_card : labelMixed.card=36 := by decide

def TwoDissociated (w : Fin 3 → ℤ) : Prop :=
  ∀ c : Fin 3 → ℤ, (∀ i,-2 ≤ c i ∧ c i ≤ 2) →
    (∑ i,c i*w i)=0 → ∀ i,c i=0

theorem bitZ_bounds (b : Bool) : 0 ≤ bitZ b ∧ bitZ b ≤ 1 := by cases b <;> simp [bitZ]

theorem two_diss_difference_iff (a : ℤ) (w : Fin 3 → ℤ) (hd : TwoDissociated w)
    (i j k l : Label 3) :
    integerValue a w i-integerValue a w j=integerValue a w k-integerValue a w l ↔
      CoordinateBalance ((i,j),(k,l)) := by
  constructor
  · intro he
    have hc := hd (fun n => bitZ (i n)-bitZ (j n)-bitZ (k n)+bitZ (l n))
      (by intro n; dsimp; have := bitZ_bounds (i n); have := bitZ_bounds (j n)
          have := bitZ_bounds (k n); have := bitZ_bounds (l n); omega)
      (by simp_rw [add_mul,sub_mul,Finset.sum_add_distrib,Finset.sum_sub_distrib]
          dsimp [integerValue] at he; omega)
    intro n
    have h := hc n
    dsimp at h ⊢
    omega
  · intro hc
    have he : (∑ n, (bitZ (i n)-bitZ (j n))*w n)=
        ∑ n,(bitZ (k n)-bitZ (l n))*w n := by
      apply Finset.sum_congr rfl
      intro n _
      rw [hc n]
    simp_rw [sub_mul,Finset.sum_sub_distrib] at he
    dsimp [integerValue]
    omega

theorem two_diss_injective (a : ℤ) (w : Fin 3 → ℤ) (hd : TwoDissociated w) :
    Function.Injective (integerValue a w) := by
  intro v u he
  have hc := (two_diss_difference_iff a w hd v u u u).mp (by omega)
  funext n
  have h := hc n
  dsimp at h
  cases hv : v n <;> cases hu : u n <;> simp_all [bitZ]

theorem coordinate_value_mono (a : ℤ) (w : Fin 3 → ℤ) (hw : ∀ n,0<w n)
    (v u : Label 3) (hle : CoordinateLe v u) : integerValue a w v ≤ integerValue a w u := by
  unfold integerValue
  apply add_le_add_left
  apply Finset.sum_le_sum
  intro n _
  exact mul_le_mul_of_nonneg_right (hle n) (le_of_lt (hw n))

noncomputable def cubeIndex (a : ℤ) (w : Fin 3 → ℤ) (x : ℤ) : Label 3 :=
  if h : ∃ v : Label 3, integerValue a w v=x then Classical.choose h else fun _ => false

theorem cubeIndex_correct (a : ℤ) (w : Fin 3 → ℤ) (x : ℤ)
    (hx : x∈integerCube a w) : integerValue a w (cubeIndex a w x)=x := by
  have h : ∃ v : Label 3, integerValue a w v=x := by
    obtain ⟨v,_,he⟩ := Finset.mem_image.mp hx
    exact ⟨v,he⟩
  simp only [cubeIndex,dif_pos h]
  exact Classical.choose_spec h

theorem cubeIndex_value (a : ℤ) (w : Fin 3 → ℤ)
    (hinj : Function.Injective (integerValue a w)) (v : Label 3) :
    cubeIndex a w (integerValue a w v)=v := by
  apply hinj
  exact cubeIndex_correct a w _ (Finset.mem_image_of_mem _ (Finset.mem_univ v))

noncomputable def attainableColor (a : ℤ) (w : Fin 3 → ℤ) (p : Point) : Bool :=
  templateColor (cubeIndex a w p.1) (cubeIndex a w p.2)

theorem attainableColor_symmetric (a : ℤ) (w : Fin 3 → ℤ) (x y : ℤ) :
    attainableColor a w (x,y)=attainableColor a w (y,x) := template_symmetric _ _

@[simp] theorem attainableColor_value (a : ℤ) (w : Fin 3 → ℤ)
    (hinj : Function.Injective (integerValue a w)) (i j : Label 3) :
    attainableColor a w (integerValue a w i,integerValue a w j)=templateColor i j := by
  simp only [attainableColor,cubeIndex_value a w hinj]

theorem attainableColor_proper (a : ℤ) (w : Fin 3 → ℤ) (hw : ∀ n,0<w n)
    (hd : TwoDissociated w) :
    properOn (strictSource (fun n => n∈integerCube a w)) (attainableColor a w) := by
  intro x y h hh h₁ h₂ h₃ hm
  let i := cubeIndex a w x
  let j := cubeIndex a w y
  let k := cubeIndex a w (x+h)
  let l := cubeIndex a w (y+h)
  have hi : integerValue a w i=x := cubeIndex_correct a w x h₁.1
  have hj : integerValue a w j=y := cubeIndex_correct a w y h₁.2.1
  have hk : integerValue a w k=x+h := cubeIndex_correct a w (x+h) h₂.1
  have hl : integerValue a w l=y+h := cubeIndex_correct a w (y+h) h₃.2.1
  have hb : CoordinateBalance ((i,j),(k,l)) :=
    (two_diss_difference_iff a w hd i j k l).mp (by omega)
  change templateColor i j=templateColor k j ∧ templateColor k j=templateColor k l at hm
  have hyx := h₁.2.2
  rcases template_bad_order i j k l hb hm with hbad | hbad
  · have h := coordinate_value_mono a w hw i j hbad
    omega
  · have h := coordinate_value_mono a w hw k i hbad
    omega

def valueQuad (a : ℤ) (w : Fin 3 → ℤ)
    (p : (Label 3 × Label 3) × (Label 3 × Label 3)) : (ℤ×ℤ)×(ℤ×ℤ) :=
  ((integerValue a w p.1.1,integerValue a w p.1.2),
    (integerValue a w p.2.1,integerValue a w p.2.2))

theorem valueQuad_injective (a : ℤ) (w : Fin 3 → ℤ)
    (hinj : Function.Injective (integerValue a w)) : Function.Injective (valueQuad a w) := by
  rintro ⟨⟨i,j⟩,k,l⟩ ⟨⟨i',j'⟩,k',l'⟩ he
  simp only [valueQuad,Prod.mk.injEq] at he ⊢
  exact ⟨⟨hinj he.1.1,hinj he.1.2⟩,hinj he.2.1,hinj he.2.2⟩

theorem labelEnergy_image (a : ℤ) (w : Fin 3 → ℤ) (hd : TwoDissociated w) :
    labelEnergy.image (valueQuad a w)=energySet (integerCube a w) := by
  ext ⟨⟨x,y⟩,u,v⟩
  constructor
  · intro h
    obtain ⟨⟨⟨i,j⟩,k,l⟩,hp,he⟩ := Finset.mem_image.mp h
    have hb := (Finset.mem_filter.mp hp).2
    have hc := (two_diss_difference_iff a w hd i j k l).mpr hb
    have hmem : ∀ q : Label 3, integerValue a w q∈integerCube a w :=
      fun q => Finset.mem_image_of_mem _ (Finset.mem_univ q)
    have hq := (mem_energySet (integerCube a w) _ _ _ _).mpr
      ⟨hmem i,hmem j,hmem k,hmem l,hc⟩
    exact he ▸ hq
  · intro h
    rcases (mem_energySet (integerCube a w) x y u v).mp h with ⟨hx,hy,hu,hv,he⟩
    obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨j,_,rfl⟩ := Finset.mem_image.mp hy
    obtain ⟨k,_,rfl⟩ := Finset.mem_image.mp hu
    obtain ⟨l,_,rfl⟩ := Finset.mem_image.mp hv
    exact Finset.mem_image.mpr ⟨((i,j),(k,l)),Finset.mem_filter.mpr
      ⟨Finset.mem_univ _,(two_diss_difference_iff a w hd i j k l).mp he⟩,rfl⟩

theorem labelMixed_image (a : ℤ) (w : Fin 3 → ℤ) (hd : TwoDissociated w) :
    labelMixed.image (valueQuad a w)=
      orderedMixedCollisions (integerCube a w) (attainableColor a w) := by
  have hinj := two_diss_injective a w hd
  ext ⟨⟨x,y⟩,u,v⟩
  constructor
  · intro h
    obtain ⟨⟨⟨i,j⟩,k,l⟩,hp,he⟩ := Finset.mem_image.mp h
    rcases Finset.mem_filter.mp hp with ⟨hp,hne,hcol⟩
    have hb := (Finset.mem_filter.mp hp).2
    have hc := (two_diss_difference_iff a w hd i j k l).mpr hb
    have hmem : ∀ q : Label 3, integerValue a w q∈integerCube a w :=
      fun q => Finset.mem_image_of_mem _ (Finset.mem_univ q)
    have hq := (mem_orderedMixedCollisions (integerCube a w) (attainableColor a w) _ _ _ _).mpr
      ⟨hmem i,hmem j,hmem k,hmem l,hc,fun he => hne (hinj he),
        by simpa only [attainableColor_value a w hinj] using hcol⟩
    exact he ▸ hq
  · intro h
    rcases (mem_orderedMixedCollisions (integerCube a w) (attainableColor a w) x y u v).mp h with
      ⟨hx,hy,hu,hv,he,hne,hcol⟩
    obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨j,_,rfl⟩ := Finset.mem_image.mp hy
    obtain ⟨k,_,rfl⟩ := Finset.mem_image.mp hu
    obtain ⟨l,_,rfl⟩ := Finset.mem_image.mp hv
    apply Finset.mem_image.mpr
    refine ⟨((i,j),(k,l)),Finset.mem_filter.mpr ⟨?_,?_,?_⟩,rfl⟩
    · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,(two_diss_difference_iff a w hd i j k l).mp he⟩
    · intro hij
      exact hne (congrArg (integerValue a w) hij)
    · simpa only [attainableColor_value a w hinj] using hcol

theorem two_diss_cube_counts (a : ℤ) (w : Fin 3 → ℤ) (hd : TwoDissociated w) :
    M (integerCube a w)=28 ∧ T (integerCube a w)=24 ∧
      mixedCount (integerCube a w) (attainableColor a w)=9 ∧
      F (integerCube a w) (attainableColor a w)=15 := by
  have hinj := two_diss_injective a w hd
  have hcard : (integerCube a w).card=8 := by
    simp [integerCube,Finset.card_image_of_injective _ hinj,Label]
  have henergy : E (integerCube a w)=216 := by
    unfold E
    rw [← labelEnergy_image a w hd,
      Finset.card_image_of_injective _ (valueQuad_injective a w hinj),label_energy_card]
  have hQ : (orderedMixedCollisions (integerCube a w) (attainableColor a w)).card=36 := by
    rw [← labelMixed_image a w hd,
      Finset.card_image_of_injective _ (valueQuad_injective a w hinj),label_mixed_card]
  have hT := energy_corner_identity (integerCube a w)
  rw [henergy,hcard] at hT
  have hmix := ordered_mixed_fourfold (integerCube a w) (attainableColor a w)
    (attainableColor_symmetric a w)
  rw [hQ] at hmix
  have hp := mixed_partition (integerCube a w) (attainableColor a w)
  refine ⟨?_,by omega,by omega,by omega⟩
  simp only [M,hcard]
  decide

/-- Universal attainment for every positive2-dissociated generator triple,
    with no ordering or separation hypothesis on the weights. -/
theorem three_cube_attainment (a : ℤ) (w : Fin 3 → ℤ) (hw : ∀ n,0<w n)
    (hd : TwoDissociated w) :
    ∃ z : Point → Bool,
      properOn (strictSource (fun n => n∈integerCube a w)) z ∧
      M (integerCube a w)=28 ∧ T (integerCube a w)=24 ∧
      mixedCount (integerCube a w) z=9 ∧ F (integerCube a w) z=15 := by
  exact ⟨attainableColor a w,attainableColor_proper a w hw hd,two_diss_cube_counts a w hd⟩

#print axioms template_bad_order
#print axioms label_energy_card
#print axioms label_mixed_card
#print axioms three_cube_attainment

end EnergyForcing.ThreeCube
