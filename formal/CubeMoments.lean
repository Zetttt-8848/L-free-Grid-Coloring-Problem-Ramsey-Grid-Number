import TwoGolombImbalance
import FiberDominance

set_option autoImplicit false

namespace EnergyForcing.Counting
open scoped BigOperators

/-- An ordered list of j integer generators followed by its integer base. -/
def CubeTuple : ℕ → Type
  | 0 => ℤ
  | j+1 => Σ _ : ℤ, CubeTuple j

instance cubeTupleDecidableEq (j : ℕ) : DecidableEq (CubeTuple j) := by
  induction j with
  | zero => exact inferInstanceAs (DecidableEq ℤ)
  | succ j ih =>
    letI := ih
    exact inferInstanceAs (DecidableEq (Σ _ : ℤ, CubeTuple j))

def cubeVertex : (j : ℕ) → CubeTuple j → (Fin j → Bool) → ℤ
  | 0,p,_ => p
  | j+1,p,bits => cubeVertex j p.2 (fun i => bits i.succ)+(if bits 0 then p.1 else 0)

def cubePositive : (j : ℕ) → CubeTuple j → Prop
  | 0,_ => True
  | j+1,p => 0<p.1 ∧ cubePositive j p.2

def cubeBase : (j : ℕ) → CubeTuple j → ℤ
  | 0,p => p
  | j+1,p => cubeBase j p.2

def cubeGenerator : (j : ℕ) → CubeTuple j → Fin j → ℤ
  | 0,_,i => Fin.elim0 i
  | j+1,p,i => Fin.cases p.1 (cubeGenerator j p.2) i

/-- The recursive vertex test is exactly x plus the selected generators. -/
theorem cubeVertex_eq_sum (j : ℕ) (p : CubeTuple j) (bits : Fin j→Bool) :
    cubeVertex j p bits=cubeBase j p+∑i:Fin j,if bits i then cubeGenerator j p i else 0 := by
  induction j with
  | zero => simp [cubeVertex,cubeBase]
  | succ j ih =>
    rw [Fin.sum_univ_succ]
    simp only [cubeVertex,cubeBase,cubeGenerator,Fin.cases_zero,Fin.cases_succ,ih]
    omega

theorem cubePositive_iff (j : ℕ) (p : CubeTuple j) :
    cubePositive j p ↔ ∀i:Fin j,0<cubeGenerator j p i := by
  induction j with
  | zero => simp [cubePositive]
  | succ j ih =>
    simp only [cubePositive,Fin.forall_fin_succ,cubeGenerator,Fin.cases_zero,Fin.cases_succ,ih]

def cubeFromParameters : (j : ℕ) → ℤ → (Fin j→ℤ) → CubeTuple j
  | 0,x,_ => x
  | j+1,x,h => ⟨h 0,cubeFromParameters j x (fun i=>h i.succ)⟩

theorem cubeFromParameters_base (j : ℕ) (x : ℤ) (h : Fin j→ℤ) :
    cubeBase j (cubeFromParameters j x h)=x := by
  induction j with
  | zero => rfl
  | succ j ih => exact ih _

theorem cubeFromParameters_generator (j : ℕ) (x : ℤ) (h : Fin j→ℤ) :
    cubeGenerator j (cubeFromParameters j x h)=h := by
  induction j with
  | zero => funext i; exact Fin.elim0 i
  | succ j ih =>
    funext i
    refine Fin.cases ?_ (fun k=>?_) i
    · rfl
    · exact congrFun (ih (fun k=>h k.succ)) k

theorem cubeFromParameters_inverse (j : ℕ) (p : CubeTuple j) :
    cubeFromParameters j (cubeBase j p) (cubeGenerator j p)=p := by
  induction j with
  | zero => rfl
  | succ j ih =>
    rcases p with ⟨d,p⟩
    simp only [cubeFromParameters,cubeBase,cubeGenerator,Fin.cases_zero,Fin.cases_succ,ih]

/-- Explicit equivalence to the manuscript's base and ordered generator tuple. -/
def cubeParametersEquiv (j : ℕ) : CubeTuple j ≃ (ℤ×(Fin j→ℤ)) where
  toFun p := (cubeBase j p,cubeGenerator j p)
  invFun p := cubeFromParameters j p.1 p.2
  left_inv := cubeFromParameters_inverse j
  right_inv := by
    rintro ⟨x,h⟩
    exact Prod.ext (cubeFromParameters_base j x h) (cubeFromParameters_generator j x h)

def positiveCubes : (j : ℕ) → Finset ℤ → Finset (CubeTuple j)
  | 0,A => A
  | j+1,A => (posDiffs A).sigma fun d => positiveCubes j (positiveFiber A d)

def signedCubes : (j : ℕ) → Finset ℤ → Finset (CubeTuple j)
  | 0,A => A
  | j+1,A => (allDiffs A).sigma fun d => signedCubes j (positiveFiber A d)

/-- Membership is exactly positivity and all 2^j vertex tests. No distinctness
    of generators or vertices is imposed. -/
theorem mem_positiveCubes_iff (j : ℕ) (A : Finset ℤ) (p : CubeTuple j) :
    p∈positiveCubes j A ↔ cubePositive j p ∧ ∀bits, cubeVertex j p bits∈A := by
  induction j generalizing A with
  | zero => simp [positiveCubes,cubePositive,cubeVertex]
  | succ j ih =>
    rcases p with ⟨d,p⟩
    change (⟨d,p⟩ : Σ _ : ℤ,CubeTuple j)∈
      (posDiffs A).sigma (fun d=>positiveCubes j (positiveFiber A d)) ↔ _
    rw [Finset.mem_sigma]
    simp only [ih,cubePositive]
    constructor
    · rintro ⟨hd,hp,hv⟩
      refine ⟨⟨((mem_posDiffs A d).mp hd).1,hp⟩,?_⟩
      intro bits
      have hh := (mem_positiveFiber A d _).mp (hv (fun i => bits i.succ))
      cases hb : bits 0
      · simpa [cubeVertex,hb] using hh.1
      · simpa [cubeVertex,hb] using hh.2
    · rintro ⟨⟨hd,hp⟩,hv⟩
      have hv0 (bits : Fin j→Bool) : cubeVertex j p bits∈A := by
        simpa [cubeVertex] using hv (Fin.cases false bits)
      have hv1 (bits : Fin j→Bool) : cubeVertex j p bits+d∈A := by
        simpa [cubeVertex] using hv (Fin.cases true bits)
      refine ⟨(mem_posDiffs A d).mpr ⟨hd,cubeVertex j p (fun _=>false),hv0 _,hv1 _⟩,hp,?_⟩
      intro bits
      exact (mem_positiveFiber A d _).mpr ⟨hv0 bits,hv1 bits⟩

theorem mem_signedCubes_iff (j : ℕ) (A : Finset ℤ) (p : CubeTuple j) :
    p∈signedCubes j A ↔ ∀bits, cubeVertex j p bits∈A := by
  induction j generalizing A with
  | zero => simp [signedCubes,cubeVertex]
  | succ j ih =>
    rcases p with ⟨d,p⟩
    change (⟨d,p⟩ : Σ _ : ℤ,CubeTuple j)∈
      (allDiffs A).sigma (fun d=>signedCubes j (positiveFiber A d)) ↔ _
    rw [Finset.mem_sigma]
    simp only [ih]
    constructor
    · rintro ⟨_,hv⟩ bits
      have hh := (mem_positiveFiber A d _).mp (hv (fun i => bits i.succ))
      cases hb : bits 0
      · simpa [cubeVertex,hb] using hh.1
      · simpa [cubeVertex,hb] using hh.2
    · intro hv
      have hv0 (bits : Fin j→Bool) : cubeVertex j p bits∈A := by
        simpa [cubeVertex] using hv (Fin.cases false bits)
      have hv1 (bits : Fin j→Bool) : cubeVertex j p bits+d∈A := by
        simpa [cubeVertex] using hv (Fin.cases true bits)
      refine ⟨(mem_allDiffs A d).mpr (Or.inr ⟨cubeVertex j p (fun _=>false),hv0 _,hv1 _⟩),?_⟩
      intro bits
      exact (mem_positiveFiber A d _).mpr ⟨hv0 bits,hv1 bits⟩

def K (j : ℕ) (A : Finset ℤ) : ℕ := (positiveCubes j A).card
def Ccube (j : ℕ) (A : Finset ℤ) : ℕ := (signedCubes j A).card

theorem K_succ (j : ℕ) (A : Finset ℤ) :
    K (j+1) A=∑d∈posDiffs A,K j (positiveFiber A d) := Finset.card_sigma ..

theorem K_one (A : Finset ℤ) : K 1 A=M A := by
  rw [K_succ]
  exact sum_r A

theorem K_two (A : Finset ℤ) : K 2 A=T A := by
  rw [K_succ]
  simp_rw [K_one]
  exact (corner_count A).symm

theorem K_three (A : Finset ℤ) :
    K 3 A=∑d∈posDiffs A,T (positiveFiber A d) := by
  rw [K_succ]
  simp_rw [K_two]

def cubeTranslate : (j : ℕ) → ℤ → CubeTuple j → CubeTuple j
  | 0,a,p => Int.add p a
  | j+1,a,p => ⟨p.1,cubeTranslate j a p.2⟩

theorem cubeVertex_translate (j : ℕ) (a : ℤ) (p : CubeTuple j) (bits : Fin j→Bool) :
    cubeVertex j (cubeTranslate j a p) bits=cubeVertex j p bits+a := by
  induction j with
  | zero => rfl
  | succ j ih =>
    simp only [cubeVertex,cubeTranslate,ih]
    omega

theorem cubeTranslate_inverse (j : ℕ) (a : ℤ) (p : CubeTuple j) :
    cubeTranslate j (-a) (cubeTranslate j a p)=p := by
  induction j with
  | zero => simp [cubeTranslate]
  | succ j ih =>
    rcases p with ⟨d,p⟩
    simp only [cubeTranslate,ih]

theorem Ccube_translate (j : ℕ) (A : Finset ℤ) (a : ℤ) :
    Ccube j (A.image (·+a))=Ccube j A := by
  unfold Ccube
  symm
  refine Finset.card_nbij' (cubeTranslate j a) (cubeTranslate j (-a)) ?_ ?_ ?_ ?_
  · intro p hp
    rw [mem_signedCubes_iff] at hp ⊢
    intro bits
    rw [cubeVertex_translate]
    exact Finset.mem_image.mpr ⟨_,hp bits,rfl⟩
  · intro p hp
    rw [mem_signedCubes_iff] at hp ⊢
    intro bits
    obtain ⟨x,hx,he⟩ := Finset.mem_image.mp (hp bits)
    rw [cubeVertex_translate]
    convert hx using 1 <;> omega
  · intro p _; exact cubeTranslate_inverse j a p
  · intro p _
    simpa using cubeTranslate_inverse j (-a) p

theorem fiber_neg_translate (A : Finset ℤ) (d : ℤ) :
    positiveFiber A (-d)=(positiveFiber A d).image (·+d) := by
  ext u
  simp only [mem_positiveFiber,Finset.mem_image]
  constructor
  · rintro ⟨hu,hu'⟩
    exact ⟨u-d,⟨by simpa [sub_eq_add_neg] using hu',by simpa using hu⟩,by simp⟩
  · rintro ⟨v,hv,rfl⟩
    exact ⟨hv.2,by simpa using hv.1⟩

theorem Ccube_neg_fiber (j : ℕ) (A : Finset ℤ) (d : ℤ) :
    Ccube j (positiveFiber A (-d))=Ccube j (positiveFiber A d) := by
  rw [fiber_neg_translate,Ccube_translate]

theorem sum_allDiffs_even (A : Finset ℤ) (f : ℤ→ℕ) (heven:∀d,f (-d)=f d) :
    (∑d∈allDiffs A,f d)=f 0+2*∑d∈posDiffs A,f d := by
  have hpos (d : ℤ) : d∈posDiffs A ↔ d∈allDiffs A ∧ 0<d := by
    rw [← allDiffs_pos,Finset.mem_filter]
  have hs : allDiffs A=insert 0 (posDiffs A ∪ (posDiffs A).image Neg.neg) := by
    ext d
    simp only [Finset.mem_insert,Finset.mem_union,Finset.mem_image]
    constructor
    · intro hd
      rcases lt_trichotomy d 0 with hn|hz|hp
      · right; right
        exact ⟨-d,(hpos (-d)).mpr ⟨(neg_mem_allDiffs A d).mpr hd,by omega⟩,by simp⟩
      · exact Or.inl hz
      · exact Or.inr (Or.inl ((hpos d).mpr ⟨hd,hp⟩))
    · rintro (hz|hp|⟨e,he,rfl⟩)
      · subst d; exact (mem_allDiffs A 0).mpr (Or.inl rfl)
      · exact ((hpos d).mp hp).1
      · exact (neg_mem_allDiffs A e).mpr (((hpos e).mp he).1)
  have hd : Disjoint (posDiffs A) ((posDiffs A).image Neg.neg) := by
    apply Finset.disjoint_left.mpr
    intro d hdp hdn
    obtain ⟨e,he,heq⟩ := Finset.mem_image.mp hdn
    have hp := ((hpos d).mp hdp).2
    have he' := ((hpos e).mp he).2
    omega
  have hz : (0:ℤ)∉posDiffs A ∪ (posDiffs A).image Neg.neg := by
    intro h
    rcases Finset.mem_union.mp h with hp|hn
    · have := ((hpos 0).mp hp).2; omega
    · obtain ⟨e,he,heq⟩ := Finset.mem_image.mp hn
      have := ((hpos e).mp he).2
      omega
  rw [hs,Finset.sum_insert hz,Finset.sum_union hd]
  rw [Finset.sum_image (by intro a _ b _ h; exact neg_injective h)]
  simp_rw [heven]
  omega

theorem Ccube_succ (j : ℕ) (A : Finset ℤ) :
    Ccube (j+1) A=Ccube j A+2*∑d∈posDiffs A,Ccube j (positiveFiber A d) := by
  change (signedCubes (j+1) A).card=_
  rw [signedCubes,Finset.card_sigma]
  change (∑d∈allDiffs A,Ccube j (positiveFiber A d))=_
  rw [sum_allDiffs_even A _ (Ccube_neg_fiber j A)]
  have hf : positiveFiber A 0=A := by ext u; simp
  rw [hf]

theorem Ccube_one (A : Finset ℤ) : Ccube 1 A=A.card+2*M A := by
  rw [Ccube_succ]
  change A.card+2*(∑d∈posDiffs A,r A d)=_
  rw [sum_r]

theorem Ccube_two (A : Finset ℤ) : Ccube 2 A=A.card+4*M A+4*T A := by
  rw [Ccube_succ,Ccube_one]
  simp_rw [Ccube_one]
  rw [Finset.sum_add_distrib,← Finset.mul_sum]
  change A.card+2*M A+2*((∑d∈posDiffs A,r A d)+2*(∑d∈posDiffs A,(r A d).choose 2))=_
  rw [sum_r,← corner_count]
  ring

theorem Ccube_three (A : Finset ℤ) :
    Ccube 3 A=A.card+6*M A+12*T A+8*K 3 A := by
  rw [Ccube_succ,Ccube_two]
  simp_rw [Ccube_two]
  simp only [Finset.sum_add_distrib,← Finset.mul_sum]
  change A.card+4*M A+4*T A+2*((∑d∈posDiffs A,r A d)+
    4*(∑d∈posDiffs A,(r A d).choose 2)+4*(∑d∈posDiffs A,T (positiveFiber A d)))=_
  rw [sum_r,← corner_count,← K_three]
  ring

abbrev momentClass := EnergyForcing.FiberDominance.fiberClass

theorem moment_classes_disjoint (A : Finset ℤ) (z : Point→Bool) (d : ℤ) :
    Disjoint (momentClass A z d false) (momentClass A z d true) := by
  apply Finset.disjoint_left.mpr
  intro x hx hy
  have hf := (Finset.mem_filter.mp hx).2
  have ht := (Finset.mem_filter.mp hy).2
  rw [hf] at ht
  contradiction

theorem moment_classes_union (A : Finset ℤ) (z : Point→Bool) (d : ℤ) :
    momentClass A z d false∪momentClass A z d true=positiveFiber A d := by
  ext u
  simp only [momentClass,EnergyForcing.FiberDominance.fiberClass,Finset.mem_union,Finset.mem_filter]
  cases h : z (u+d,u) <;> simp [h]

theorem moment_class_golomb (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) (d : ℤ) (hd:0<d) (b : Bool) :
    Golomb (·∈momentClass A z d b) := by
  have hg := fiber_class_golomb (·∈A) z hz d hd b
  simpa only [momentClass,EnergyForcing.FiberDominance.fiberClass,Finset.mem_filter,
    mem_positiveFiber] using hg

noncomputable def Dmoment (A : Finset ℤ) (z : Point→Bool) : ℝ :=
  ∑d∈posDiffs A,((r A d:ℝ)-1)*imbalance (momentClass A z d false) (momentClass A z d true)

noncomputable def Pmoment (A : Finset ℤ) (z : Point→Bool) : ℝ :=
  ∑d∈posDiffs A,imbalanceEta (momentClass A z d false) (momentClass A z d true)

noncomputable def Rmoment (A : Finset ℤ) (z : Point→Bool) : ℝ :=
  ∑d∈posDiffs A,(rho (momentClass A z d false) (momentClass A z d true):ℝ)

theorem nat_dist_real (b c : ℕ) : (Nat.dist b c:ℝ)=|(b:ℝ)-(c:ℝ)| := by
  rcases le_total b c with h|h
  · rw [Nat.dist_eq_sub_of_le h,Nat.cast_sub h,abs_of_nonpos (by exact_mod_cast (show (b:ℤ)-c≤0 by omega))]
    ring
  · rw [Nat.dist_comm,Nat.dist_eq_sub_of_le h,Nat.cast_sub h,
      abs_of_nonneg (by exact_mod_cast (show (0:ℤ)≤(b:ℤ)-c by omega))]

theorem nat_sub_one_real (n : ℕ) : ((n-1:ℕ):ℝ)=max ((n:ℝ)-1) 0 := by
  cases n with
  | zero => norm_num
  | succ n =>
    have hn : (0:ℝ)≤(n:ℝ) := by positivity
    rw [Nat.cast_sub (by omega : 1≤n+1),Nat.cast_one,
      max_eq_left (by simp only [Nat.cast_add,Nat.cast_one]; linarith)]

theorem Dmoment_eq (A : Finset ℤ) (z : Point→Bool) :
    Dmoment A z=(EnergyForcing.FiberDominance.D A z:ℝ) := by
  unfold Dmoment EnergyForcing.FiberDominance.D
  rw [Nat.cast_sum]
  apply Finset.sum_congr rfl
  intro d hd
  obtain ⟨hpos,u,hu,hud⟩ := (mem_posDiffs A d).mp hd
  have hr : 1≤r A d := Finset.card_pos.mpr ⟨u,(mem_positiveFiber A d u).mpr ⟨hu,hud⟩⟩
  rw [Nat.cast_mul,Nat.cast_sub hr,Nat.cast_one,nat_dist_real]
  rfl

theorem Pmoment_eq (A : Finset ℤ) (z : Point→Bool) :
    Pmoment A z=EnergyForcing.FiberDominance.P A z := by
  unfold Pmoment EnergyForcing.FiberDominance.P
  rw [Finset.sum_div]
  apply Finset.sum_congr rfl
  intro d hd
  unfold imbalanceEta imbalance
  rw [nat_sub_one_real,nat_dist_real]
  have hc : ((momentClass A z d false).card:ℝ)+((momentClass A z d true).card:ℝ)=(r A d:ℝ) := by
    exact_mod_cast EnergyForcing.FiberDominance.class_partition A z d
  rw [hc]

theorem Rmoment_eq (A : Finset ℤ) (z : Point→Bool) :
    Rmoment A z=(EnergyForcing.FiberDominance.R A z:ℝ) := by
  unfold Rmoment EnergyForcing.FiberDominance.R
  rw [Nat.cast_sum]
  rfl

theorem moment_fiber_T_first (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) (d : ℤ) (hd:0<d) :
    (T (positiveFiber A d):ℝ)≤2*(M (positiveFiber A d):ℝ)-
      ((r A d:ℝ)-1)*imbalance (momentClass A z d false) (momentClass A z d true)/2-
      imbalanceEta (momentClass A z d false) (momentClass A z d true) := by
  have ht := imbalance_T_first (momentClass A z d false) (momentClass A z d true)
    (moment_classes_disjoint A z d) (moment_class_golomb A z hz d hd false)
    (moment_class_golomb A z hz d hd true)
  rw [moment_classes_union] at ht
  have hc : ((momentClass A z d false).card:ℝ)+((momentClass A z d true).card:ℝ)=(r A d:ℝ) := by
    exact_mod_cast EnergyForcing.FiberDominance.class_partition A z d
  rw [hc] at ht
  exact ht

theorem moment_fiber_T_second (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) (d : ℤ) (hd:0<d) :
    (T (positiveFiber A d):ℝ)≤(M (positiveFiber A d):ℝ)+
      5*(rho (momentClass A z d false) (momentClass A z d true):ℝ)-
      imbalanceEta (momentClass A z d false) (momentClass A z d true) := by
  have ht := imbalance_T_second (momentClass A z d false) (momentClass A z d true)
    (moment_classes_disjoint A z d) (moment_class_golomb A z hz d hd false)
    (moment_class_golomb A z hz d hd true)
  rw [moment_classes_union] at ht
  exact ht

theorem K_three_bound_first (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (K 3 A:ℝ)≤2*(T A:ℝ)-Dmoment A z/2-Pmoment A z := by
  have hk : (K 3 A:ℝ)=∑d∈posDiffs A,(T (positiveFiber A d):ℝ) := by exact_mod_cast K_three A
  have hm : (T A:ℝ)=∑d∈posDiffs A,(M (positiveFiber A d):ℝ) := by exact_mod_cast corner_count A
  rw [hk,hm]
  unfold Dmoment Pmoment
  rw [Finset.mul_sum,Finset.sum_div,← Finset.sum_sub_distrib,← Finset.sum_sub_distrib]
  apply Finset.sum_le_sum
  intro d hd
  exact moment_fiber_T_first A z hz d ((mem_posDiffs A d).mp hd).1

theorem K_three_bound_second (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (K 3 A:ℝ)≤(T A:ℝ)+5*Rmoment A z-Pmoment A z := by
  have hk : (K 3 A:ℝ)=∑d∈posDiffs A,(T (positiveFiber A d):ℝ) := by exact_mod_cast K_three A
  have hm : (T A:ℝ)=∑d∈posDiffs A,(M (positiveFiber A d):ℝ) := by exact_mod_cast corner_count A
  rw [hk,hm]
  unfold Rmoment Pmoment
  rw [Finset.mul_sum,← Finset.sum_add_distrib,← Finset.sum_sub_distrib]
  apply Finset.sum_le_sum
  intro d hd
  exact moment_fiber_T_second A z hz d ((mem_posDiffs A d).mp hd).1

theorem K_three_bound (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (K 3 A:ℝ) ≤ min (2*(T A:ℝ)-Dmoment A z/2) ((T A:ℝ)+5*Rmoment A z)-Pmoment A z := by
  have h1 := K_three_bound_first A z hz
  have h2 := K_three_bound_second A z hz
  rw [min_def]
  split_ifs <;> assumption

theorem Ccube_three_bound (A : Finset ℤ) (z : Point→Bool)
    (hz : properOn (strictSource (·∈A)) z) :
    (Ccube 3 A:ℝ)≤7*(E A:ℝ)-11*(A.card:ℝ)^2+5*(A.card:ℝ)-
      4*Dmoment A z-8*Pmoment A z := by
  have hc : (Ccube 3 A:ℝ)=(A.card:ℝ)+6*(M A:ℝ)+12*(T A:ℝ)+8*(K 3 A:ℝ) := by
    exact_mod_cast Ccube_three A
  have hk := K_three_bound_first A z hz
  have he := real_E A
  have hm := real_M A
  nlinarith

end EnergyForcing.Counting
