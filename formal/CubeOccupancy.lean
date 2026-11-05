import CubeCapacity
import CubeTransfer

namespace EnergyForcing.Capacity

open scoped BigOperators

def RealMark (A : ℤ → Prop) (x : ℝ) : Prop := ∃ n : ℤ, A n ∧ (n:ℝ)=x

noncomputable def occupiedMarks {d : ℕ} (A : ℤ → Prop) (a : ℝ) (w : Fin d → ℝ) :
    Finset ℝ := by
  classical
  exact (realCube a w).filter (RealMark A)

noncomputable def occupiedLabels {d : ℕ} (A : ℤ → Prop) (a : ℝ) (w : Fin d → ℝ) :
    Finset (Label d) := by
  classical
  exact Finset.univ.filter fun v => RealMark A (weightedValue a w v)

@[simp] theorem mem_occupiedLabels {d : ℕ} (A : ℤ → Prop) (a : ℝ)
    (w : Fin d → ℝ) (v : Label d) :
    v∈occupiedLabels A a w ↔ RealMark A (weightedValue a w v) := by
  classical
  simp [occupiedLabels]

theorem occupied_card {d : ℕ} (A : ℤ → Prop) (a : ℝ) (w : Fin d → ℝ)
    (hinj : Function.Injective (weightedValue a w)) :
    (occupiedLabels A a w).card=(occupiedMarks A a w).card := by
  classical
  have hsub : occupiedMarks A a w ⊆ realCube a w := Finset.filter_subset _ _
  have he : labelsOf a w (occupiedMarks A a w)=occupiedLabels A a w := by
    ext v
    simp only [mem_labelsOf,mem_occupiedLabels,occupiedMarks,Finset.mem_filter]
    have hv : weightedValue a w v∈realCube a w :=
      Finset.mem_image_of_mem _ (Finset.mem_univ v)
    simp [hv]
  simpa only [he] using labelsOf_card a w (occupiedMarks A a w) hsub hinj

theorem real_cast_golomb (A : ℤ → Prop) (h : Golomb A) : RealGolomb (RealMark A) := by
  intro a b c e ha hb hc he hab hce hdiff
  rcases ha with ⟨a,ha,rfl⟩
  rcases hb with ⟨b,hb,rfl⟩
  rcases hc with ⟨c,hc,rfl⟩
  rcases he with ⟨e,he,rfl⟩
  have hp := h a b c e ha hb hc he (by exact_mod_cast hab)
    (by exact_mod_cast hce) (by exact_mod_cast hdiff)
  exact ⟨by exact_mod_cast hp.1,by exact_mod_cast hp.2⟩

theorem occupied_golomb_bound (A : ℤ → Prop) (h : Golomb A)
    (a : ℝ) (w : Fin 4 → ℝ) (hinj : Function.Injective (weightedValue a w)) :
    (occupiedMarks A a w).card≤7 := by
  classical
  apply real_four_cube_golomb_bound a w _ (Finset.filter_subset _ _) hinj
  intro x y u v hx hy hu hv hxy huv he
  exact real_cast_golomb A h x y u v
    (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2
    (Finset.mem_filter.mp hu).2 (Finset.mem_filter.mp hv).2 hxy huv he

/-- The fourteen bound concerns the actual finite intersection of the real cube
    with the integer source, including cubes with nonintegral generators. -/
theorem weak_four_cube_occupancy (A : ℤ → Prop) (z : Point → Bool)
    (hz : properOn (weakSource A) z) (a : ℝ) (w : Fin 4 → ℝ)
    (hinj : Function.Injective (weightedValue a w)) :
    (occupiedMarks A a w).card≤14 := by
  classical
  let B : ℤ → Prop := fun n => A n ∧ z (n,n)=false
  let C : ℤ → Prop := fun n => A n ∧ z (n,n)=true
  have hb := occupied_golomb_bound B (diagonal_class_golomb A z hz false) a w hinj
  have hc := occupied_golomb_bound C (diagonal_class_golomb A z hz true) a w hinj
  have hu : occupiedMarks A a w=occupiedMarks B a w ∪ occupiedMarks C a w := by
    ext x
    simp only [occupiedMarks,Finset.mem_filter,Finset.mem_union]
    constructor
    · rintro ⟨hx,n,hn,hcast⟩
      cases he : z (n,n)
      · exact Or.inl ⟨hx,n,⟨hn,he⟩,hcast⟩
      · exact Or.inr ⟨hx,n,⟨hn,he⟩,hcast⟩
    · rintro (⟨hx,n,hn,hcast⟩ | ⟨hx,n,hn,hcast⟩)
      · exact ⟨hx,n,hn.1,hcast⟩
      · exact ⟨hx,n,hn.1,hcast⟩
  rw [hu]
  exact (Finset.card_union_le _ _).trans (by omega)

theorem weak_four_label_occupancy (A : ℤ → Prop) (z : Point → Bool)
    (hz : properOn (weakSource A) z) (a : ℝ) (w : Fin 4 → ℝ)
    (hinj : Function.Injective (weightedValue a w)) :
    (occupiedLabels A a w).card≤14 := by
  rw [occupied_card A a w hinj]
  exact weak_four_cube_occupancy A z hz a w hinj

def headSection {d : ℕ} (C : Finset (Label (d+1))) (b : Bool) : Finset (Label d) :=
  Finset.univ.filter fun v => Fin.cons b v∈C

@[simp] theorem mem_headSection {d : ℕ} (C : Finset (Label (d+1)))
    (b : Bool) (v : Label d) : v∈headSection C b ↔ Fin.cons b v∈C := by
  simp [headSection]

theorem head_section_card {d : ℕ} (C : Finset (Label (d+1))) (b : Bool) :
    (C.filter fun v => v 0=b).card=(headSection C b).card := by
  refine Finset.card_bij' (fun v _ => Fin.tail v) (fun v _ => Fin.cons b v) ?_ ?_ ?_ ?_
  · intro v hv
    rcases Finset.mem_filter.mp hv with ⟨hv,hb⟩
    apply (mem_headSection C b _).mpr
    simpa only [← hb,Fin.cons_self_tail] using hv
  · intro v hv
    exact Finset.mem_filter.mpr ⟨(mem_headSection C b v).mp hv,by simp⟩
  · intro v hv
    have hb := (Finset.mem_filter.mp hv).2
    simpa only [← hb] using Fin.cons_self_tail v
  · intro v _; simp

theorem head_count {d : ℕ} (C : Finset (Label (d+1))) :
    C.card=(headSection C false).card+(headSection C true).card := by
  have hn : C.filter (fun v => ¬v 0=false)=C.filter (fun v => v 0=true) := by
    ext v
    cases he : v 0 <;> simp [he]
  have h := Finset.filter_card_add_filter_neg_card_eq_card (s := C) (fun v => v 0=false)
  rw [hn,head_section_card,head_section_card] at h
  omega

theorem weightedValue_cons {d : ℕ} (a : ℝ) (w : Fin (d+1) → ℝ)
    (b : Bool) (v : Label d) :
    weightedValue a w (Fin.cons b v)=
      weightedValue a (fun i => w i.succ) v+(if b then w 0 else 0) := by
  cases b <;> simp [weightedValue,Fin.sum_univ_succ,bitZ,add_comm,add_left_comm,add_assoc]

theorem face_injective {d : ℕ} (a : ℝ) (w : Fin (d+1) → ℝ)
    (hinj : Function.Injective (weightedValue a w)) :
    Function.Injective (weightedValue a (fun i : Fin d => w i.succ)) := by
  intro v u he
  have hh : weightedValue a w (Fin.cons false v)=weightedValue a w (Fin.cons false u) := by
    simpa only [weightedValue_cons,Bool.false_eq_true,if_false,add_zero] using he
  have h := hinj hh
  exact congrArg Fin.tail h

theorem strict_five_cube_occupancy (A : ℤ → Prop) (z : Point → Bool)
    (hz : properOn (strictSource A) z) (a : ℝ) (w : Fin 5 → ℝ)
    (hw : 0<w 0) (hinj : Function.Injective (weightedValue a w)) :
    (occupiedMarks A a w).card≤30 := by
  classical
  let C := occupiedLabels A a w
  let C₀ := headSection C false
  let C₁ := headSection C true
  let wt : Fin 4 → ℝ := fun i => w i.succ
  have hface : Function.Injective (weightedValue a wt) := face_injective a w hinj
  have hzero : ∀ v∈C₀, ∃ n : ℤ, A n ∧ (n:ℝ)=weightedValue a wt v := by
    intro v hv
    have hm := (mem_occupiedLabels A a w _).mp ((mem_headSection C false v).mp hv)
    simpa only [weightedValue_cons,Bool.false_eq_true,if_false,add_zero] using hm
  have hone : ∀ v∈C₁, ∃ n : ℤ, A n ∧ (n:ℝ)=weightedValue a wt v+w 0 := by
    intro v hv
    have hm := (mem_occupiedLabels A a w _).mp ((mem_headSection C true v).mp hv)
    simpa only [weightedValue_cons,if_true] using hm
  have hcomplete : (C₀∩C₁).card≤14 := by
    by_cases hwint : ∃ d : ℤ, (d:ℝ)=w 0
    · obtain ⟨d,hd⟩ := hwint
      have hdp : 0<d := by exact_mod_cast (show (0:ℝ)<(d:ℝ) by linarith)
      let F : ℤ → Prop := fun n => A n ∧ A (n+d)
      have hsub : C₀∩C₁ ⊆ occupiedLabels F a wt := by
        intro v hv
        obtain ⟨n,hn,hnv⟩ := hzero v (Finset.mem_inter.mp hv).1
        obtain ⟨m,hm,hmv⟩ := hone v (Finset.mem_inter.mp hv).2
        have he : m=n+d := by
          have heR : (m:ℝ)=(n:ℝ)+(d:ℝ) := by linarith
          exact_mod_cast heR
        exact (mem_occupiedLabels F a wt v).mpr ⟨n,⟨hn,by simpa only [he] using hm⟩,hnv⟩
      have hb := weak_four_label_occupancy F (fun p => z (p.1+d,p.2))
        (fiber_restriction A z hz d hdp) a wt hface
      exact (Finset.card_le_card hsub).trans hb
    · have he : C₀∩C₁=∅ := by
        apply Finset.eq_empty_iff_forall_not_mem.mpr
        intro v hv
        obtain ⟨n,hn,hnv⟩ := hzero v (Finset.mem_inter.mp hv).1
        obtain ⟨m,hm,hmv⟩ := hone v (Finset.mem_inter.mp hv).2
        apply hwint
        refine ⟨m-n,?_⟩
        push_cast
        linarith
      simp [he]
  have hunion : (C₀∪C₁).card≤16 := by
    have h := Finset.card_le_univ (C₀∪C₁)
    simpa [Label] using h
  have hadd := Finset.card_union_add_card_inter C₀ C₁
  have hcount := head_count C
  change C.card=C₀.card+C₁.card at hcount
  rw [← occupied_card A a w hinj]
  change C.card≤30
  omega

theorem no_full_five_cube (A : ℤ → Prop) (z : Point → Bool)
    (hz : properOn (strictSource A) z) (a : ℝ) (w : Fin 5 → ℝ)
    (hw : 0<w 0) (hinj : Function.Injective (weightedValue a w))
    (hfull : ∀ v : Label 5, RealMark A (weightedValue a w v)) : False := by
  have hc := strict_five_cube_occupancy A z hz a w hw hinj
  have he : occupiedLabels A a w=Finset.univ := by
    ext v
    simp [mem_occupiedLabels,hfull v]
  rw [← occupied_card A a w hinj,he] at hc
  norm_num [Label] at hc

def integerValue {d : ℕ} (a : ℤ) (w : Fin d → ℤ) (v : Label d) : ℤ :=
  a+∑ i, bitZ (v i)*w i

def integerCube {d : ℕ} (a : ℤ) (w : Fin d → ℤ) : Finset ℤ :=
  Finset.univ.image (integerValue a w)

theorem integerValue_cast {d : ℕ} (a : ℤ) (w : Fin d → ℤ) (v : Label d) :
    (integerValue a w v : ℝ)=weightedValue (a:ℝ) (fun i => (w i:ℝ)) v := by
  simp [integerValue,weightedValue]

theorem integer_real_injective {d : ℕ} (a : ℤ) (w : Fin d → ℤ)
    (hinj : Function.Injective (integerValue a w)) :
    Function.Injective (weightedValue (a:ℝ) (fun i => (w i:ℝ))) := by
  intro v u he
  apply hinj
  have hc : (integerValue a w v : ℝ)=(integerValue a w u : ℝ) := by
    simpa only [integerValue_cast] using he
  exact_mod_cast hc

theorem integerValue_append_false {d k : ℕ} (a : ℤ) (w : Fin (d+k) → ℤ)
    (v : Label d) :
    integerValue a w (Fin.append v (fun _ : Fin k => false))=
      integerValue a (fun i => w (Fin.castAdd k i)) v := by
  simp [integerValue,Fin.sum_univ_add,Fin.append_left,Fin.append_right,bitZ]

theorem integer_face_injective {d k : ℕ} (a : ℤ) (w : Fin (d+k) → ℤ)
    (hinj : Function.Injective (integerValue a w)) :
    Function.Injective (integerValue a (fun i : Fin d => w (Fin.castAdd k i))) := by
  intro v u he
  have hh : integerValue a w (Fin.append v (fun _ : Fin k => false))=
      integerValue a w (Fin.append u (fun _ : Fin k => false)) := by
    simpa only [integerValue_append_false] using he
  have h := hinj hh
  funext i
  simpa only [Fin.append_left] using congrFun h (Fin.castAdd k i)

theorem no_integer_cube_five_add (k : ℕ) (a : ℤ) (w : Fin (5+k) → ℤ)
    (hw : ∀ i, 0<w i) (hinj : Function.Injective (integerValue a w))
    (z : Point → Bool) (hz : properOn (strictSource (fun n => n∈integerCube a w)) z) :
    False := by
  let wt : Fin 5 → ℤ := fun i => w (Fin.castAdd k i)
  have hface : Function.Injective (integerValue a wt) := integer_face_injective a w hinj
  apply no_full_five_cube (fun n => n∈integerCube a w) z hz (a:ℝ)
    (fun i => (wt i:ℝ)) (by
      change (0:ℝ)<(w (Fin.castAdd k 0):ℝ)
      exact_mod_cast hw (Fin.castAdd k 0))
    (integer_real_injective a wt hface)
  intro v
  refine ⟨integerValue a wt v,?_,integerValue_cast a wt v⟩
  apply Finset.mem_image.mpr
  refine ⟨Fin.append v (fun _ : Fin k => false),Finset.mem_univ _,?_⟩
  exact integerValue_append_false a w v

theorem integer_cube_dimension_bound {d : ℕ} (a : ℤ) (w : Fin d → ℤ)
    (hw : ∀ i, 0<w i) (hinj : Function.Injective (integerValue a w))
    (z : Point → Bool) (hz : properOn (strictSource (fun n => n∈integerCube a w)) z) :
    d≤4 := by
  by_contra hn
  have h5 : 5≤d := by omega
  obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le h5
  exact no_integer_cube_five_add k a w hw hinj z hz

def CubeAttainable (d : ℕ) : Prop :=
  ∃ a : ℤ, ∃ w : Fin d → ℤ, ∃ z : Point → Bool,
    (∀ i, 0<w i) ∧ Function.Injective (integerValue a w) ∧
      properOn (strictSource (fun n => n∈integerCube a w)) z

theorem fin_two_bool_injective : Function.Injective (fun i : Fin 2 => decide (i=1)) := by
  intro i j he
  fin_cases i <;> fin_cases j <;> simp_all

theorem properOn_fin_two_bool (D : Point → Prop) (z : Point → Fin 2)
    (hz : properOn D z) : properOn D (fun p => decide (z p=1)) := by
  intro x y d hd h₁ h₂ h₃ hm
  exact hz x y d hd h₁ h₂ h₃
    ⟨fin_two_bool_injective hm.1,fin_two_bool_injective hm.2⟩

theorem integer_four_cube_attainable : CubeAttainable 4 := by
  let w : Fin 4 → ℤ := fun i => 3^i.val
  have hcube : integerCube 0 w=EnergyForcing.Cubes.cube 0 1 3 9 27 := by decide
  have hsep : EnergyForcing.Cubes.Separated4 1 3 9 27 := by
    norm_num [EnergyForcing.Cubes.Separated4]
  refine ⟨0,w,(fun p => decide (EnergyForcing.Cubes.cubeColor 0 1 3 9 27 p=1)),?_,?_,?_⟩
  · intro i
    fin_cases i <;> norm_num [w]
  · decide
  · rw [hcube]
    exact properOn_fin_two_bool _ _ (EnergyForcing.Cubes.separated_four_cube 0 1 3 9 27 hsep)

/-- Four is attained and no larger injective positive integer cube is attainable. -/
theorem exact_cube_dimension : CubeAttainable 4 ∧ ∀ d, CubeAttainable d → d≤4 := by
  refine ⟨integer_four_cube_attainable,?_⟩
  intro d hd
  obtain ⟨a,w,z,hw,hinj,hz⟩ := hd
  exact integer_cube_dimension_bound a w hw hinj z hz

#print axioms weak_four_cube_occupancy
#print axioms strict_five_cube_occupancy
#print axioms no_full_five_cube
#print axioms integer_cube_dimension_bound
#print axioms integer_four_cube_attainable
#print axioms exact_cube_dimension

end EnergyForcing.Capacity
