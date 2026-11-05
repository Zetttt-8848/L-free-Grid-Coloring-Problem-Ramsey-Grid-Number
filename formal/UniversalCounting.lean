import Geometry

namespace EnergyForcing

def sumRange (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => sumRange f n + f n

theorem count_sum_cons (k a : Nat) (l : List Nat) :
    sumRange (fun i => (a::l).count i) k =
      sumRange (fun i => l.count i) k + if a<k then 1 else 0 := by
  induction k with
  | zero => simp [sumRange]
  | succ k ih =>
    change sumRange (fun i => (a::l).count i) k + (a::l).count k =
      sumRange (fun i => l.count i) k + l.count k + if a<k+1 then 1 else 0
    rw [ih,List.count_cons]
    simp only [beq_iff_eq]
    by_cases h : a<k
    · have hne : a≠k := by omega
      simp [h,hne,show a<k+1 by omega]
      omega
    · by_cases he : a=k
      · subst a; simp [h,Nat.add_assoc]
      · simp [h,he,show ¬a<k+1 by omega]

theorem count_sum_eq_length (k : Nat) (l : List Nat)
    (h : ∀ a, a∈l → a<k) : sumRange (fun i => l.count i) k=l.length := by
  induction l with
  | nil =>
    induction k with
    | zero => rfl
    | succ k ih => simpa [sumRange] using ih
  | cons a l ih =>
    rw [count_sum_cons,if_pos (h a (by simp)),ih (fun b hb => h b (by simp [hb]))]
    rfl

def maxRange (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => max (maxRange f n) (f n)

theorem le_maxRange (f : Nat → Nat) (k i : Nat) (hi : i<k) : f i≤maxRange f k := by
  induction k with
  | zero => omega
  | succ k ih =>
    by_cases he : i=k
    · subst i; exact Nat.le_max_right _ _
    · exact Nat.le_trans (ih (by omega)) (Nat.le_max_left _ _)

theorem maxRange_attained (f : Nat → Nat) (k : Nat) (hk : 0<k) :
    ∃ i, i<k ∧ maxRange f k=f i := by
  cases k with
  | zero => omega
  | succ k =>
    induction k with
    | zero => exact ⟨0,by omega,by simp [maxRange]⟩
    | succ k ih =>
      obtain ⟨i,hi,he⟩ := ih (by omega)
      by_cases h : f (k+1)≤maxRange f (k+1)
      · refine ⟨i,by omega,?_⟩
        change max (maxRange f (k+1)) (f (k+1))=f i
        rw [Nat.max_eq_left h,he]
      · refine ⟨k+1,by omega,?_⟩
        change max (maxRange f (k+1)) (f (k+1))=f (k+1)
        exact Nat.max_eq_right (by omega)

theorem sumRange_le_bound (f : Nat → Nat) (k b : Nat)
    (h : ∀ i, i<k → f i≤b) : sumRange f k≤k*b := by
  induction k with
  | zero => simp [sumRange]
  | succ k ih =>
    have hprev := ih (fun i hi => h i (by omega))
    have hlast := h k (by omega)
    simp only [sumRange,Nat.succ_mul]
    omega

/-- Finite pigeonhole principle with the exact multiplicative cardinality bound. -/
theorem largest_color_class (k : Nat) (hk : 0<k) (colors : List Nat)
    (h : ∀ a, a∈colors → a<k) :
    ∃ i, i<k ∧ colors.length≤k*colors.count i := by
  obtain ⟨i,hi,he⟩ := maxRange_attained (fun i => colors.count i) k hk
  refine ⟨i,hi,?_⟩
  rw [← count_sum_eq_length k colors h,← he]
  exact sumRange_le_bound (fun i => colors.count i) k _
    (fun j hj => le_maxRange (fun i => colors.count i) k j hj)

theorem nodup_map_injective {α β : Type} (f : α → β)
    (hf : ∀ a b, f a=f b → a=b) (l : List α) (hl : l.Nodup) : (l.map f).Nodup := by
  induction l with
  | nil => simp
  | cons a l ih =>
    have h := List.nodup_cons.mp hl
    apply List.nodup_cons.mpr
    constructor
    · intro hm
      obtain ⟨b,hb,he⟩ := List.mem_map.mp hm
      exact h.1 (by simpa only [hf b a he] using hb)
    · exact ih h.2

def squareList (N : Nat) : List Point :=
  (List.range N).flatMap fun (i : Nat) =>
    (List.range N).map fun (j : Nat) => ((i:Int)+1,(j:Int)+1)

theorem mem_squareList (N : Nat) (p : Point) : p∈squareList N ↔ square (N:Int) p := by
  simp only [squareList,List.mem_flatMap,List.mem_map,List.mem_range]
  constructor
  · rintro ⟨i,hi,j,hj,he⟩
    subst p
    simp only [square]
    omega
  · intro hp
    refine ⟨p.1.toNat-1,?_,p.2.toNat-1,?_,?_⟩
    · have := hp.1; have := hp.2.1; omega
    · have := hp.2.2.1; have := hp.2.2.2; omega
    · apply Prod.ext <;> dsimp
      · have := hp.1; omega
      · have := hp.2.2.1; omega

theorem length_flatMap_const {α β : Type} (l : List α) (f : α → List β) (n : Nat)
    (h : ∀ a, a∈l → (f a).length=n) : (l.flatMap f).length=n*l.length := by
  induction l with
  | nil => simp
  | cons a l ih =>
    simp only [List.flatMap_cons,List.length_append,List.length_cons]
    rw [h a (by simp),ih (fun b hb => h b (by simp [hb])),Nat.mul_succ]
    omega

theorem squareList_length (N : Nat) : (squareList N).length=N*N := by
  unfold squareList
  rw [length_flatMap_const _ _ N (by intros; simp),List.length_range]

theorem squareList_nodup (N : Nat) : (squareList N).Nodup := by
  unfold squareList List.Nodup
  apply List.pairwise_flatMap.mpr
  constructor
  · intro i _
    exact nodup_map_injective (fun j : Nat => ((i:Int)+1,(j:Int)+1))
      (by intro a b he; have := congrArg Prod.snd he; dsimp at this; omega)
      (List.range N) List.nodup_range
  · apply List.Pairwise.imp _ List.nodup_range
    intro i j hij p hp q hq he
    obtain ⟨a,_,rfl⟩ := List.mem_map.mp hp
    obtain ⟨b,_,rfl⟩ := List.mem_map.mp hq
    apply hij
    have := congrArg Prod.fst he
    dsimp at this
    omega

def pairedCode (N : Int) (k : Nat) (c : Point → Fin k) (p : Point) : Nat :=
  k*(c p).val+(c (J N p)).val

theorem pairedCode_bound (N : Int) (k : Nat) (c : Point → Fin k) (p : Point) :
    pairedCode N k c p<k*k := by
  have h1 := (c p).isLt
  have h2 := (c (J N p)).isLt
  have hm := Nat.mul_le_mul_left k (show (c p).val+1≤k by omega)
  simp only [Nat.mul_add,Nat.mul_one] at hm
  unfold pairedCode
  omega

theorem pairedCode_eq (N : Int) (k : Nat) (hk : 0<k) (c : Point → Fin k)
    (p q : Point) (he : pairedCode N k c p=pairedCode N k c q) :
    paired N c p=paired N c q := by
  have hfst := congrArg (fun a => a/k) he
  have hsnd := congrArg (fun a => a%k) he
  simp only [pairedCode,Nat.mul_add_div hk,Nat.div_eq_of_lt (c (J N p)).isLt,
    Nat.div_eq_of_lt (c (J N q)).isLt,Nat.add_zero] at hfst
  simp only [pairedCode,Nat.mul_add_mod,Nat.mod_eq_of_lt (c (J N p)).isLt,
    Nat.mod_eq_of_lt (c (J N q)).isLt] at hsnd
  exact Prod.ext (Fin.ext hfst) (Fin.ext hsnd)

/-- Complete lem:J: the paired palette, its signed-corner exclusion, and the
    cardinality of a largest class. The size bound is cleared of denominators. -/
theorem paired_color_class_complete (N k : Nat) (hk : 0<k) (c : Point → Fin k)
    (hc : properCorner (N:Int) c) :
    (∀ p, pairedCode (N:Int) k c p<k*k) ∧
    ∃ i, i<k*k ∧
      let S := (squareList N).filter fun p => pairedCode (N:Int) k c p==i
      S.Nodup ∧ N*N≤(k*k)*S.length ∧
      noSignedCorners (fun p => p∈S) := by
  refine ⟨pairedCode_bound (N:Int) k c,?_⟩
  let code := pairedCode (N:Int) k c
  obtain ⟨i,hi,hlen⟩ := largest_color_class (k*k) (Nat.mul_pos hk hk)
    ((squareList N).map code) (by
      intro a ha
      obtain ⟨p,_,rfl⟩ := List.mem_map.mp ha
      exact pairedCode_bound _ _ _ _)
  refine ⟨i,hi,?_⟩
  dsimp
  constructor
  · exact List.Pairwise.filter _ (squareList_nodup N)
  constructor
  · rw [List.count_eq_countP,List.countP_map,List.countP_eq_length_filter] at hlen
    simpa only [List.length_map,squareList_length,Function.comp_def,code] using hlen
  · intro a b d hd hh
    have hp := List.mem_filter.mp hh.1
    have hq := List.mem_filter.mp hh.2.1
    have hr := List.mem_filter.mp hh.2.2
    have ep : code (a,b)=i := by simpa [code] using hp.2
    have eq : code (a+d,b)=i := by simpa [code] using hq.2
    have er : code (a,b+d)=i := by simpa [code] using hr.2
    apply paired_no_signed_corner (N:Int) c hc a b d hd
      ((mem_squareList N _).mp hp.1) ((mem_squareList N _).mp hq.1)
      ((mem_squareList N _).mp hr.1)
    exact ⟨pairedCode_eq _ k hk c _ _ (ep.trans eq.symm),
      pairedCode_eq _ k hk c _ _ (eq.trans er.symm)⟩

def diagonalList (N : Nat) : List Int :=
  (List.range N).map fun (a : Nat) => (a:Int)+1

theorem diagonalList_mem (N : Nat) (a : Int) :
    a∈diagonalList N ↔ 1≤a ∧ a≤(N:Int) := by
  simp only [diagonalList,List.mem_map,List.mem_range]
  constructor
  · rintro ⟨b,hb,he⟩; omega
  · intro h
    exact ⟨a.toNat-1,by omega,by omega⟩

theorem diagonalList_nodup (N : Nat) : (diagonalList N).Nodup :=
  nodup_map_injective (fun a : Nat => (a:Int)+1)
    (by intro a b he; dsimp at he; omega) _ List.nodup_range

def eraseThird (c₀ c : Fin 3) : Bool := c.val==(c₀.val+1)%3

theorem eraseThird_injective : ∀ c₀ a b : Fin 3, a≠c₀ → b≠c₀ →
    eraseThird c₀ a=eraseThird c₀ b → a=b := by decide

theorem proper_after_remove_color (D : Point → Prop) (c : Point → Fin 3)
    (c₀ : Fin 3) (hp : properOn D c) (ha : ∀ p, D p → c p≠c₀) :
    properOn D (fun p => eraseThird c₀ (c p)) := by
  intro x y d hd h₁ h₂ h₃ he
  apply hp x y d hd h₁ h₂ h₃
  exact ⟨eraseThird_injective c₀ _ _ (ha _ h₁) (ha _ h₂) he.1,
    eraseThird_injective c₀ _ _ (ha _ h₂) (ha _ h₃) he.2⟩

/-- Interval formulation of the manuscript's span estimate. A finite set is a
    duplicate-free list. Allowing any containing interval is equivalent to the
    actual-span formulation: apply it to the minimum containing interval, or
    enlarge that interval using monotonicity. -/
def SpanEstimateOn (q Lmax : Nat) : Prop :=
  ∀ (A : List Int) (lo : Int) (ell : Nat), A.Nodup → ell≤Lmax →
    (∀ a, a∈A → lo≤a ∧ a≤lo+(ell:Int)) →
    (∃ c : Point → Bool, properOn (strictSource (fun a => a∈A)) c) →
    A.length*(A.length-1)≤2*q*ell

theorem finite_integer_extrema (A : List Int) (hA : A≠[]) :
    ∃ lo hi, lo∈A ∧ hi∈A ∧ ∀ a, a∈A → lo≤a ∧ a≤hi := by
  induction A with
  | nil => contradiction
  | cons x A ih =>
    by_cases hnil : A=[]
    · subst A
      exact ⟨x,x,by simp,by simp,by intro a ha; simp only [List.mem_singleton] at ha; omega⟩
    · obtain ⟨lo,hi,hlo,hhi,hbounds⟩ := ih hnil
      refine ⟨min x lo,max x hi,?_,?_,?_⟩
      · by_cases hx : x≤lo
        · simp [Int.min_eq_left hx]
        · simpa [Int.min_eq_right (by omega : lo≤x)] using List.mem_cons_of_mem x hlo
      · by_cases hx : hi≤x
        · simp [Int.max_eq_left hx]
        · simpa [Int.max_eq_right (by omega : x≤hi)] using List.mem_cons_of_mem x hhi
      · intro a ha
        rcases List.mem_cons.mp ha with rfl|ha
        · exact ⟨Int.min_le_left _ _,Int.le_max_left _ _⟩
        · have h := hbounds a ha
          exact ⟨Int.le_trans (Int.min_le_right _ _) h.1,
            Int.le_trans h.2 (Int.le_max_right _ _)⟩

/-- Actual-span formulation: lo and hi are attained extrema, with ell=hi-lo.
    Empty sets satisfy the numerical estimate automatically. -/
def ActualSpanEstimateOn (q Lmax : Nat) : Prop :=
  ∀ (A : List Int) (lo hi : Int) (ell : Nat), A.Nodup →
    lo∈A → hi∈A → (∀ a, a∈A → lo≤a ∧ a≤hi) →
    hi-lo=(ell:Int) → ell≤Lmax →
    (∃ c : Point → Bool, properOn (strictSource (fun a => a∈A)) c) →
    A.length*(A.length-1)≤2*q*ell

theorem span_estimate_iff_interval (q Lmax : Nat) :
    ActualSpanEstimateOn q Lmax ↔ SpanEstimateOn q Lmax := by
  constructor
  · intro hs A m ell hn he hb hp
    by_cases hnil : A=[]
    · subst A; simp
    · obtain ⟨lo,hi,hlo,hhi,hbounds⟩ := finite_integer_extrema A hnil
      have hnonneg : 0≤hi-lo := by have := hbounds lo hlo; omega
      have hwidth : (hi-lo).toNat≤ell := by
        have := hb lo hlo; have := hb hi hhi; omega
      have hh := hs A lo hi (hi-lo).toNat hn hlo hhi hbounds (by omega)
        (Nat.le_trans hwidth he) hp
      exact Nat.le_trans hh (Nat.mul_le_mul_left (2*q) hwidth)
  · intro hs A lo hi ell hn hlo hhi hb he hmax hp
    exact hs A lo ell hn hmax (by intro a ha; have := hb a ha; omega) hp

/-- Proposition prop:span-r3 in its equivalent interval formulation. -/
theorem three_color_span_reduction_interval (q : Nat) (hq : 1≤q)
    (hspan : SpanEstimateOn q (18*q)) : ramseyL 3 (18*q+1) := by
  intro c hc
  let N := 18*q+1
  let diag := diagonalList N
  let color := fun a : Int => (c (a,a)).val
  obtain ⟨i,hi,hlarge⟩ := largest_color_class 3 (by decide) (diag.map color) (by
    intro a ha
    obtain ⟨x,_,rfl⟩ := List.mem_map.mp ha
    exact (c (x,x)).isLt)
  let A := diag.filter fun a => color a==i
  have hn : N≤3*A.length := by
    rw [List.count_eq_countP,List.countP_map,List.countP_eq_length_filter] at hlarge
    simpa only [List.length_map,diag,diagonalList,List.length_map,List.length_range,
      Function.comp_def,A,color] using hlarge
  have hA : ∀ a, a∈A → 1≤a ∧ a≤(N:Int) := by
    intro a ha
    exact (diagonalList_mem N a).mp (List.mem_filter.mp ha).1
  let c₀ : Fin 3 := ⟨i,hi⟩
  have hdiag : ∀ a, a∈A → c (a,a)=c₀ := by
    intro a ha
    apply Fin.ext
    exact of_decide_eq_true (List.mem_filter.mp ha).2
  have hr := square_diagonal_restriction (N:Int) (fun a => a∈A) c c₀ hA hc hdiag
  have hbinary := proper_after_remove_color (strictSource (fun a => a∈A)) c c₀ hr.1 hr.2
  have hbound := hspan A 1 (18*q) (List.Pairwise.filter _ (diagonalList_nodup N))
    (by omega) (by intro a ha; have := hA a ha; dsimp [N] at this; omega)
    ⟨_,hbinary⟩
  have hlen : 6*q+1≤A.length := by dsimp [N] at hn; omega
  have hmul := Nat.mul_le_mul hlen (show 6*q≤A.length-1 by omega)
  have he : (6*q+1)*(6*q)=2*q*(18*q)+6*q := by
    simp only [Nat.add_mul,Nat.one_mul]
    have heq : (6*q)*(6*q)=2*q*(18*q) := by
      simp [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]
    rw [heq]
  rw [he] at hmul
  omega

theorem spanEstimate_restrict (q L₁ L₂ : Nat) (h : L₁≤L₂)
    (hs : SpanEstimateOn q L₂) : SpanEstimateOn q L₁ := by
  intro A lo ell hn he hb hp
  exact hs A lo ell hn (Nat.le_trans he h) hb hp

theorem three_color_span_reduction (q : Nat) (hq : 1≤q)
    (hs : ActualSpanEstimateOn q (18*q)) : ramseyL 3 (18*q+1) :=
  three_color_span_reduction_interval q hq ((span_estimate_iff_interval q (18*q)).mp hs)

/-- S21's three-color consequence, with S21 retained as a hypothesis. -/
theorem S21_three (hs : ActualSpanEstimateOn 21 99994) : ramseyL 3 379 := by
  exact three_color_span_reduction_interval 21 (by decide)
    (spanEstimate_restrict 21 378 99994 (by decide)
      ((span_estimate_iff_interval 21 99994).mp hs))

#print axioms largest_color_class
#print axioms paired_color_class_complete
#print axioms three_color_span_reduction
#print axioms S21_three
end EnergyForcing
