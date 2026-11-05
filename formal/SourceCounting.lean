import Mathlib

namespace EnergyForcing.Counting

open scoped BigOperators

/-- Starts of the difference-d fiber. Only positive d are summed below. -/
def positiveFiber (A : Finset ℤ) (d : ℤ) : Finset ℤ :=
  A.filter fun u => u+d∈A

def r (A : Finset ℤ) (d : ℤ) : ℕ := (positiveFiber A d).card

def posDiffs (A : Finset ℤ) : Finset ℤ :=
  ((A.product A).image fun p => p.1-p.2).filter fun d => 0<d

def sourceCells (A : Finset ℤ) : Finset (ℤ × ℤ) :=
  (A.product A).filter fun p => p.2<p.1

/-- The tuple (x,y,z) represents the three cells (x,y),(z,y),(z,y+z-x).
    The positive corner step is z-x. -/
def sourceCorners (A : Finset ℤ) : Finset (ℤ × ℤ × ℤ) :=
  (A.product (A.product A)).filter fun p =>
    p.2.1<p.1 ∧ p.1<p.2.2 ∧ p.2.1+p.2.2-p.1∈A

/-- Ordered equal-difference quadruples, with no positivity restriction. -/
def energySet (A : Finset ℤ) : Finset ((ℤ × ℤ) × (ℤ × ℤ)) :=
  ((A.product A).product (A.product A)).filter fun p =>
    p.1.1-p.1.2=p.2.1-p.2.2

def M (A : Finset ℤ) : ℕ := A.card.choose 2
def T (A : Finset ℤ) : ℕ := (sourceCorners A).card
def E (A : Finset ℤ) : ℕ := (energySet A).card

def span (A : Finset ℤ) : ℕ :=
  if h : A.Nonempty then (A.max' h-A.min' h).toNat else 0

@[simp] theorem mem_positiveFiber (A : Finset ℤ) (d u : ℤ) :
    u∈positiveFiber A d ↔ u∈A ∧ u+d∈A := by
  simp [positiveFiber]

@[simp] theorem mem_sourceCells (A : Finset ℤ) (x y : ℤ) :
    (x,y)∈sourceCells A ↔ x∈A ∧ y∈A ∧ y<x := by
  simp [sourceCells,and_assoc]

@[simp] theorem mem_sourceCorners (A : Finset ℤ) (x y z : ℤ) :
    (x,y,z)∈sourceCorners A ↔
      x∈A ∧ y∈A ∧ z∈A ∧ y<x ∧ x<z ∧ y+z-x∈A := by
  simp [sourceCorners,and_assoc]

@[simp] theorem mem_energySet (A : Finset ℤ) (a b c d : ℤ) :
    ((a,b),(c,d))∈energySet A ↔
      a∈A ∧ b∈A ∧ c∈A ∧ d∈A ∧ a-b=c-d := by
  simp [energySet,and_assoc]

@[simp] theorem r_zero (A : Finset ℤ) : r A 0=A.card := by
  unfold r positiveFiber
  congr 1
  ext u
  simp

theorem r_neg (A : Finset ℤ) (h : ℤ) : r A (-h)=r A h := by
  unfold r
  refine Finset.card_nbij' (fun x : ℤ => x-h) (fun x : ℤ => x+h) ?_ ?_ ?_ ?_
  · intro x hx
    rcases (mem_positiveFiber A (-h) x).mp hx with ⟨hx,hx'⟩
    apply (mem_positiveFiber A h (x-h)).mpr
    exact ⟨by simpa [sub_eq_add_neg] using hx',by simpa using hx⟩
  · intro x hx
    rcases (mem_positiveFiber A h x).mp hx with ⟨hx,hx'⟩
    apply (mem_positiveFiber A (-h) (x+h)).mpr
    exact ⟨hx',by simpa using hx⟩
  · intros; simp
  · intros; simp

theorem r_eq_card_difference_pairs (A : Finset ℤ) (h : ℤ) :
    r A h=((A.product A).filter fun p => p.2-p.1=h).card := by
  unfold r
  refine Finset.card_nbij' (fun u : ℤ => (u,u+h)) Prod.fst ?_ ?_ ?_ ?_
  · intro u hu
    rcases (mem_positiveFiber A h u).mp hu with ⟨hu,hu'⟩
    simp [hu,hu']
  · rintro ⟨a,b⟩ hp
    simp only [Finset.mem_filter,Finset.product_eq_sprod,Finset.mem_product] at hp
    apply (mem_positiveFiber A h a).mpr
    exact ⟨hp.1.1,by convert hp.1.2 using 1 <;> omega⟩
  · intros; rfl
  · rintro ⟨a,b⟩ hp
    simp only [Finset.mem_filter,Finset.product_eq_sprod,Finset.mem_product] at hp
    apply Prod.ext <;> dsimp <;> omega

theorem mem_posDiffs (A : Finset ℤ) (d : ℤ) :
    d∈posDiffs A ↔ 0<d ∧ ∃ u∈A, u+d∈A := by
  simp only [posDiffs,Finset.mem_filter,Finset.mem_image,Finset.product_eq_sprod,Finset.mem_product]
  constructor
  · rintro ⟨⟨⟨x,y⟩,⟨hx,hy⟩,he⟩,hd⟩
    exact ⟨hd,y,hy,by convert hx using 1 <;> dsimp at he <;> omega⟩
  · rintro ⟨hd,u,hu,hu'⟩
    exact ⟨⟨(u+d,u),⟨hu',hu⟩,by simp⟩,hd⟩

theorem r_eq_zero_of_not_mem_posDiffs (A : Finset ℤ) (d : ℤ)
    (hd : 0<d) (h : d∉posDiffs A) : r A d=0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro u hu
  exact h ((mem_posDiffs A d).mpr ⟨hd,u,(mem_positiveFiber A d u).mp hu⟩)

/-- One increasing orientation of every unordered pair of distinct marks. -/
theorem sourceCells_card (A : Finset ℤ) : (sourceCells A).card=M A := by
  have hleft : A.offDiag.filter (fun p : ℤ×ℤ => p.2<p.1)=sourceCells A := by
    ext ⟨x,y⟩
    simp only [Finset.mem_filter,Finset.mem_offDiag,mem_sourceCells]
    constructor
    · rintro ⟨⟨hx,hy,_⟩,hxy⟩; exact ⟨hx,hy,hxy⟩
    · rintro ⟨hx,hy,hxy⟩; exact ⟨⟨hx,hy,by omega⟩,hxy⟩
  have hright : (A.offDiag.filter (fun p : ℤ×ℤ => ¬p.2<p.1)).card=(sourceCells A).card := by
    refine Finset.card_nbij' Prod.swap Prod.swap ?_ ?_ ?_ ?_
    · rintro ⟨x,y⟩ hp
      simp only [Finset.mem_filter,Finset.mem_offDiag] at hp
      exact (mem_sourceCells A y x).mpr ⟨hp.1.2.1,hp.1.1,by omega⟩
    · rintro ⟨x,y⟩ hp
      rcases (mem_sourceCells A x y).mp hp with ⟨hx,hy,hxy⟩
      simp only [Finset.mem_filter,Finset.mem_offDiag,Prod.swap]
      exact ⟨⟨hy,hx,by omega⟩,by omega⟩
    · intros; rfl
    · intros; rfl
  have hsplit := Finset.filter_card_add_filter_neg_card_eq_card (s:=A.offDiag)
    (fun p : ℤ×ℤ => p.2<p.1)
  rw [hleft,hright,Finset.offDiag_card] at hsplit
  have hmul : A.card*(A.card-1)=2*(sourceCells A).card := by
    rw [Nat.mul_sub_left_distrib,Nat.mul_one]
    omega
  rw [M,Nat.choose_two_right,hmul,Nat.mul_div_cancel_left _ (by decide : 0<2)]

theorem source_fiber_card (A : Finset ℤ) (d : ℤ) (hd : 0<d) :
    ((sourceCells A).filter fun p => p.1-p.2=d).card=r A d := by
  unfold r
  symm
  refine Finset.card_nbij' (fun u : ℤ => (u+d,u)) Prod.snd ?_ ?_ ?_ ?_
  · intro u hu
    rcases (mem_positiveFiber A d u).mp hu with ⟨hu,hu'⟩
    simp only [Finset.mem_filter,mem_sourceCells]
    exact ⟨⟨hu',hu,by omega⟩,by omega⟩
  · rintro ⟨x,y⟩ hp
    simp only [Finset.mem_filter,mem_sourceCells] at hp
    exact (mem_positiveFiber A d y).mpr ⟨hp.1.2.1,by convert hp.1.1 using 1 <;> omega⟩
  · intros; rfl
  · rintro ⟨x,y⟩ hp
    simp only [Finset.mem_filter,mem_sourceCells] at hp
    apply Prod.ext <;> dsimp <;> omega

theorem sum_r (A : Finset ℤ) : ∑ d∈posDiffs A, r A d=M A := by
  have hc := Finset.card_eq_sum_card_fiberwise (s:=sourceCells A) (t:=posDiffs A)
    (f:=fun p => p.1-p.2) (by
      rintro ⟨x,y⟩ hp
      rcases (mem_sourceCells A x y).mp hp with ⟨hx,hy,hxy⟩
      exact (mem_posDiffs A (x-y)).mpr ⟨by omega,y,hy,by simpa using hx⟩)
  rw [sourceCells_card] at hc
  symm
  calc
    M A = _ := hc
    _ = _ := Finset.sum_congr rfl (fun d hd => source_fiber_card A d ((mem_posDiffs A d).mp hd).1)

theorem corner_fiber_card (A : Finset ℤ) (d : ℤ) (hd : 0<d) :
    ((sourceCorners A).filter fun p => p.1-p.2.1=d).card=(r A d).choose 2 := by
  change _=M (positiveFiber A d)
  rw [← sourceCells_card]
  symm
  refine Finset.card_nbij' (fun p : ℤ×ℤ => (p.2+d,p.2,p.1+d))
    (fun p : ℤ×ℤ×ℤ => (p.2.1+p.2.2-p.1,p.2.1)) ?_ ?_ ?_ ?_
  · rintro ⟨v,u⟩ hp
    rcases (mem_sourceCells (positiveFiber A d) v u).mp hp with ⟨hv,hu,huv⟩
    rcases (mem_positiveFiber A d v).mp hv with ⟨hv,hvd⟩
    rcases (mem_positiveFiber A d u).mp hu with ⟨hu,hud⟩
    simp only [Finset.mem_filter,mem_sourceCorners]
    refine ⟨⟨hud,hu,hvd,by omega,by omega,?_⟩,by omega⟩
    convert hv using 1 <;> omega
  · rintro ⟨x,y,z⟩ hp
    simp only [Finset.mem_filter,mem_sourceCorners] at hp
    rcases hp with ⟨⟨hx,hy,hz,hxy,hxz,hw⟩,hoff⟩
    apply (mem_sourceCells (positiveFiber A d) _ _).mpr
    simp only [mem_positiveFiber]
    refine ⟨⟨hw,?_⟩,⟨hy,?_⟩,by omega⟩
    · convert hz using 1 <;> omega
    · convert hx using 1 <;> omega
  · rintro ⟨v,u⟩ _
    apply Prod.ext <;> dsimp <;> omega
  · rintro ⟨x,y,z⟩ hp
    have hoff := (Finset.mem_filter.mp hp).2
    apply Prod.ext
    · dsimp at *; omega
    · apply Prod.ext <;> dsimp at * <;> omega

theorem corner_count (A : Finset ℤ) : T A=∑ d∈posDiffs A, (r A d).choose 2 := by
  have hc := Finset.card_eq_sum_card_fiberwise (s:=sourceCorners A) (t:=posDiffs A)
    (f:=fun p => p.1-p.2.1) (by
      rintro ⟨x,y,z⟩ hp
      rcases (mem_sourceCorners A x y z).mp hp with ⟨hx,hy,_,hxy,_⟩
      exact (mem_posDiffs A (x-y)).mpr ⟨by omega,y,hy,by simpa using hx⟩)
  change (sourceCorners A).card=_
  rw [hc]
  exact Finset.sum_congr rfl (fun d hd => corner_fiber_card A d ((mem_posDiffs A d).mp hd).1)

theorem square_eq_self_add_twice_choose (n : ℕ) : n^2=n+2*n.choose 2 := by
  have hc := Nat.cast_choose_two ℚ n
  have he : (n:ℚ)^2=(n:ℚ)+2*(n.choose 2:ℚ) := by rw [hc]; ring
  exact_mod_cast he

theorem sum_r_sq (A : Finset ℤ) : ∑ d∈posDiffs A, (r A d)^2=M A+2*T A := by
  simp_rw [square_eq_self_add_twice_choose]
  rw [Finset.sum_add_distrib,← Finset.mul_sum,sum_r,← corner_count]

def allDiffs (A : Finset ℤ) : Finset ℤ :=
  insert 0 ((A.product A).image fun p => p.1-p.2)

theorem mem_allDiffs (A : Finset ℤ) (d : ℤ) :
    d∈allDiffs A ↔ d=0 ∨ ∃u∈A,u+d∈A := by
  simp only [allDiffs,Finset.mem_insert,Finset.mem_image,Finset.product_eq_sprod,Finset.mem_product]
  constructor
  · rintro (hd|⟨⟨x,y⟩,⟨hx,hy⟩,he⟩)
    · exact Or.inl hd
    · exact Or.inr ⟨y,hy,by convert hx using 1 <;> dsimp at he <;> omega⟩
  · rintro (hd|⟨u,hu,hu'⟩)
    · exact Or.inl hd
    · exact Or.inr ⟨(u+d,u),⟨hu',hu⟩,by simp⟩

theorem neg_mem_allDiffs (A : Finset ℤ) (d : ℤ) :
    -d∈allDiffs A ↔ d∈allDiffs A := by
  simp only [mem_allDiffs]
  constructor
  · rintro (hd|⟨u,hu,hu'⟩)
    · exact Or.inl (by omega)
    · exact Or.inr ⟨u-d,by simpa [sub_eq_add_neg] using hu',by simpa using hu⟩
  · rintro (hd|⟨u,hu,hu'⟩)
    · exact Or.inl (by omega)
    · exact Or.inr ⟨u+d,hu',by simpa using hu⟩

theorem allDiffs_pos (A : Finset ℤ) :
    (allDiffs A).filter (fun d => 0<d)=posDiffs A := by
  ext d
  simp only [Finset.mem_filter,mem_allDiffs,mem_posDiffs]
  constructor
  · rintro ⟨hd,hpos⟩
    exact ⟨hpos,hd.resolve_left (by omega)⟩
  · rintro ⟨hpos,hw⟩
    exact ⟨Or.inr hw,hpos⟩

theorem energy_fiber_card (A : Finset ℤ) (d : ℤ) :
    ((energySet A).filter fun p => p.1.1-p.1.2=d).card=(r A d)^2 := by
  rw [pow_two]
  change _=(positiveFiber A d).card*(positiveFiber A d).card
  rw [← Finset.card_product]
  symm
  refine Finset.card_nbij' (fun p : ℤ×ℤ => ((p.1+d,p.1),(p.2+d,p.2)))
    (fun p : (ℤ×ℤ)×(ℤ×ℤ) => (p.1.2,p.2.2)) ?_ ?_ ?_ ?_
  · rintro ⟨u,v⟩ hp
    simp only [Finset.product_eq_sprod,Finset.mem_product,mem_positiveFiber] at hp
    simp only [Finset.mem_filter,mem_energySet]
    exact ⟨⟨hp.1.2,hp.1.1,hp.2.2,hp.2.1,by omega⟩,by omega⟩
  · rintro ⟨⟨a,b⟩,⟨c,e⟩⟩ hp
    simp only [Finset.mem_filter,mem_energySet] at hp
    rcases hp with ⟨⟨ha,hb,hc,he,heq⟩,hd⟩
    simp only [Finset.product_eq_sprod,Finset.mem_product,mem_positiveFiber]
    exact ⟨⟨hb,by convert ha using 1 <;> omega⟩,⟨he,by convert hc using 1 <;> omega⟩⟩
  · intros; rfl
  · rintro ⟨⟨a,b⟩,⟨c,e⟩⟩ hp
    simp only [Finset.mem_filter,mem_energySet] at hp
    apply Prod.ext <;> apply Prod.ext <;> dsimp <;> omega

theorem energy_all_count (A : Finset ℤ) : E A=∑d∈allDiffs A,(r A d)^2 := by
  have hc := Finset.card_eq_sum_card_fiberwise (s:=energySet A) (t:=allDiffs A)
    (f:=fun p => p.1.1-p.1.2) (by
      rintro ⟨⟨a,b⟩,⟨c,e⟩⟩ hp
      rcases (mem_energySet A a b c e).mp hp with ⟨ha,hb,_⟩
      exact (mem_allDiffs A (a-b)).mpr (Or.inr ⟨b,hb,by simpa using ha⟩))
  change (energySet A).card=_
  rw [hc]
  exact Finset.sum_congr rfl (fun d _ => energy_fiber_card A d)

theorem energy_count (A : Finset ℤ) :
    E A=A.card^2+2*∑d∈posDiffs A,(r A d)^2 := by
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
  rw [energy_all_count,hs,Finset.sum_insert hz,Finset.sum_union hd]
  rw [Finset.sum_image (by intro a _ b _ h; exact neg_injective h)]
  simp_rw [r_neg]
  rw [r_zero]
  omega

theorem energy_corner_identity (A : Finset ℤ) :
    E A=2*A.card^2-A.card+4*T A := by
  rw [energy_count,sum_r_sq]
  have hm := square_eq_self_add_twice_choose A.card
  change A.card^2=A.card+2*M A at hm
  omega

theorem span_cast (A : Finset ℤ) (h : A.Nonempty) :
    (span A:ℤ)=A.max' h-A.min' h := by
  have hm : A.min' h≤A.max' h := Finset.min'_le A _ (Finset.max'_mem A h)
  simp [span,h,Int.toNat_of_nonneg (by omega : 0≤A.max' h-A.min' h)]

theorem posDiffs_subset_interval (A : Finset ℤ) :
    posDiffs A ⊆ Finset.Icc (1:ℤ) (span A:ℤ) := by
  intro d hd
  rcases (mem_posDiffs A d).mp hd with ⟨hd,u,hu,hu'⟩
  have hA : A.Nonempty := ⟨u,hu⟩
  have hlo := Finset.min'_le A u hu
  have hhi := Finset.le_max' A (u+d) hu'
  have hs := span_cast A hA
  apply Finset.mem_Icc.mpr
  omega

theorem posDiffs_card_le_span (A : Finset ℤ) : (posDiffs A).card≤span A := by
  have h := Finset.card_le_card (posDiffs_subset_interval A)
  simpa [Int.card_Icc] using h

theorem moment_cauchy (A : Finset ℤ) :
    (M A:ℝ)^2 ≤ (span A:ℝ)*((M A:ℝ)+2*(T A:ℝ)) := by
  have h := Finset.sum_mul_sq_le_sq_mul_sq (R:=ℝ) (posDiffs A)
    (fun _ => (1:ℝ)) (fun d => (r A d:ℝ))
  have hsum : (∑ d∈posDiffs A,(r A d:ℝ))=(M A:ℝ) := by
    exact_mod_cast sum_r A
  have hsq : (∑ d∈posDiffs A,(r A d:ℝ)^2)=(M A:ℝ)+2*(T A:ℝ) := by
    exact_mod_cast sum_r_sq A
  simp only [one_mul,one_pow,Finset.sum_const,nsmul_eq_mul,mul_one] at h
  rw [hsum,hsq] at h
  have hcard : ((posDiffs A).card:ℝ)≤(span A:ℝ) := by
    exact_mod_cast posDiffs_card_le_span A
  exact h.trans (mul_le_mul_of_nonneg_right hcard (by positivity))

theorem span_pair_bound (A : Finset ℤ) (κ : ℝ) (hκ : 0≤κ)
    (hT : (T A:ℝ)≤κ*(M A:ℝ)) :
    (M A:ℝ)≤(2*κ+1)*(span A:ℝ) := by
  have hc := moment_cauchy A
  have hm : (0:ℝ)≤M A := by positivity
  have hl : (0:ℝ)≤span A := by positivity
  have ht := mul_le_mul_of_nonneg_left hT hl
  by_cases hz : (M A:ℝ)=0
  · rw [hz]; positivity
  · have hp : (0:ℝ)<M A := lt_of_le_of_ne hm (Ne.symm hz)
    nlinarith

theorem span_card_bound (A : Finset ℤ) (κ : ℝ) (hκ : 0≤κ)
    (hT : (T A:ℝ)≤κ*(M A:ℝ)) :
    (A.card:ℝ)≤(1+Real.sqrt (1+8*(2*κ+1)*(span A:ℝ)))/2 := by
  have hp := span_pair_bound A κ hκ hT
  have hc := Nat.cast_choose_two ℝ A.card
  change (M A:ℝ)=(A.card:ℝ)*((A.card:ℝ)-1)/2 at hc
  have hs := Real.sq_sqrt (by positivity : (0:ℝ)≤1+8*(2*κ+1)*(span A:ℝ))
  have hsn := Real.sqrt_nonneg (1+8*(2*κ+1)*(span A:ℝ))
  nlinarith

theorem span_card_bound_simple (A : Finset ℤ) (κ : ℝ) (hκ : 0≤κ)
    (hT : (T A:ℝ)≤κ*(M A:ℝ)) :
    (A.card:ℝ)≤1+Real.sqrt (2*(2*κ+1)*(span A:ℝ)) := by
  have hp := span_pair_bound A κ hκ hT
  have hc := Nat.cast_choose_two ℝ A.card
  change (M A:ℝ)=(A.card:ℝ)*((A.card:ℝ)-1)/2 at hc
  have hs := Real.sq_sqrt (by positivity : (0:ℝ)≤2*(2*κ+1)*(span A:ℝ))
  have hsn := Real.sqrt_nonneg (2*(2*κ+1)*(span A:ℝ))
  have hn : (0:ℝ)≤A.card := by positivity
  by_cases hsmall : (A.card:ℝ)≤1
  · linarith
  · nlinarith

/-- Conventional equal-sum and equal-difference definitions count the same
    ordered quadruples, by exchanging the two negative coordinates. -/
theorem energy_eq_additive_quadruples (A : Finset ℤ) :
    E A=(((A.product A).product (A.product A)).filter
      (fun p => p.1.1+p.1.2=p.2.1+p.2.2)).card := by
  unfold E
  refine Finset.card_nbij' (fun p : (ℤ×ℤ)×(ℤ×ℤ) => ((p.1.1,p.2.2),(p.2.1,p.1.2)))
    (fun p : (ℤ×ℤ)×(ℤ×ℤ) => ((p.1.1,p.2.2),(p.2.1,p.1.2))) ?_ ?_ ?_ ?_
  · rintro ⟨⟨a,b⟩,⟨c,d⟩⟩ hp
    have hm := (mem_energySet A a b c d).mp hp
    simp only [Finset.mem_filter,Finset.product_eq_sprod,Finset.mem_product]
    exact ⟨⟨⟨hm.1,hm.2.2.2.1⟩,⟨hm.2.2.1,hm.2.1⟩⟩,by omega⟩
  · rintro ⟨⟨a,b⟩,⟨c,d⟩⟩ hp
    simp only [Finset.mem_filter,Finset.product_eq_sprod,Finset.mem_product] at hp
    exact (mem_energySet A a d c b).mpr
      ⟨hp.1.1.1,hp.1.2.2,hp.1.2.1,hp.1.1.2,by omega⟩
  · intros; rfl
  · intros; rfl

end EnergyForcing.Counting

