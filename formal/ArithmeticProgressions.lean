import SmallFactorBounds

set_option autoImplicit false

namespace EnergyForcing.Counting

def progressionSet (a d : ℤ) (n : ℕ) : Finset ℤ :=
  (Finset.range n).image fun i:ℕ=>a+d*(i:ℤ)

def IsArithmeticProgression (A : Finset ℤ) : Prop :=
  ∃a d:ℤ,0<d ∧ A=progressionSet a d A.card

@[simp] theorem mem_progressionSet (a d x : ℤ) (n : ℕ) :
    x∈progressionSet a d n ↔ ∃i:ℕ,i<n ∧ a+d*(i:ℤ)=x := by
  simp [progressionSet]

theorem progressionSet_card (a d : ℤ) (hd:0<d) (n : ℕ) :
    (progressionSet a d n).card=n := by
  unfold progressionSet
  rw [Finset.card_image_iff.mpr,Finset.card_range]
  intro i _ j _ he
  have hh : d*(i:ℤ)=d*(j:ℤ) := by dsimp at he; omega
  have hij := mul_left_cancel₀ (ne_of_gt hd) hh
  exact_mod_cast hij

theorem progressionSet_zero (a d : ℤ) : progressionSet a d 0=∅ := by simp [progressionSet]

theorem progressionSet_one (a d : ℤ) : progressionSet a d 1={a} := by simp [progressionSet]

theorem progressionSet_succ (a d : ℤ) (n : ℕ) :
    progressionSet a d (n+1)=insert a (progressionSet (a+d) d n) := by
  ext x
  simp only [mem_progressionSet,Finset.mem_insert]
  constructor
  · rintro ⟨i,hi,he⟩
    cases i with
    | zero => left; simpa using he.symm
    | succ i =>
      right
      refine ⟨i,by omega,?_⟩
      push_cast at he
      nlinarith
  · rintro (rfl|⟨i,hi,he⟩)
    · exact ⟨0,by omega,by simp⟩
    · refine ⟨i+1,by omega,?_⟩
      push_cast
      nlinarith

theorem progressionSet_succ_right (a d : ℤ) (n : ℕ) :
    progressionSet a d (n+1)=insert (a+d*(n:ℤ)) (progressionSet a d n) := by
  simp [progressionSet,Finset.range_succ]

theorem progressionSet_min (a d : ℤ) (hd:0<d) (n : ℕ) (hn:0<n)
    (hP:(progressionSet a d n).Nonempty) : (progressionSet a d n).min' hP=a := by
  apply le_antisymm
  · apply Finset.min'_le
    exact (mem_progressionSet a d a n).mpr ⟨0,hn,by simp⟩
  · apply Finset.le_min'
    intro x hx
    obtain ⟨i,_,rfl⟩ := (mem_progressionSet a d x n).mp hx
    have hi : (0:ℤ)≤ i := by positivity
    nlinarith

theorem progressionSet_max (a d : ℤ) (hd:0<d) (n : ℕ) (hn:0<n)
    (hP:(progressionSet a d n).Nonempty) :
    (progressionSet a d n).max' hP=a+d*((n-1:ℕ):ℤ) := by
  apply le_antisymm
  · apply Finset.max'_le
    intro x hx
    obtain ⟨i,hi,rfl⟩ := (mem_progressionSet a d x n).mp hx
    have hin : (i:ℤ)≤(n-1:ℕ) := by omega
    nlinarith
  · apply Finset.le_max'
    exact (mem_progressionSet a d _ n).mpr ⟨n-1,by omega,rfl⟩

/-- A finite nonempty set with one positive successor step and one terminal
    point is exactly a complete arithmetic progression. -/
theorem successor_closed_progression (A : Finset ℤ) (hA:A.Nonempty) (d : ℤ) (hd:0<d)
    (hnext:∀x∈A,x<A.max' hA → x+d∈A) :
    A=progressionSet (A.min' hA) d A.card := by
  have hmain : ∀n:ℕ,∀B:Finset ℤ,B.card=n → ∀hB:B.Nonempty,
      (∀x∈B,x<B.max' hB → x+d∈B) → B=progressionSet (B.min' hB) d B.card := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro B hcard hB hnextB
      let m:=B.min' hB
      have hm:m∈B := Finset.min'_mem B hB
      by_cases hsmall:B.card≤1
      · have hset : B={m} := by
          ext x
          simp only [Finset.mem_singleton]
          constructor
          · intro hx; exact Finset.card_le_one.mp hsmall x hx m hm
          · intro he; simpa [he] using hm
        have hc:B.card=1 := by rw [hset]; simp
        rw [hc,progressionSet_one]
        exact hset
      · let C:=B.erase m
        have hCcard : C.card+1=B.card := by
          dsimp [C]
          have hh := Finset.card_erase_of_mem hm
          omega
        have hC:C.Nonempty := Finset.card_pos.mp (by omega)
        have hminmax : m<B.max' hB := by
          have hle : m≤B.max' hB := Finset.le_max' B m hm
          by_contra hn
          have he:m=B.max' hB := le_antisymm hle (le_of_not_gt hn)
          have hleone:B.card≤1 := by
            apply Finset.card_le_one.mpr
            intro x hx y hy
            have hxl := Finset.min'_le B x hx
            have hxu := Finset.le_max' B x hx
            have hyl := Finset.min'_le B y hy
            have hyu := Finset.le_max' B y hy
            change m≤ x at hxl
            change m≤ y at hyl
            omega
          omega
        have hmaxC:B.max' hB∈C := Finset.mem_erase.mpr ⟨ne_of_gt hminmax,Finset.max'_mem B hB⟩
        have hmaxeq:C.max' hC=B.max' hB := by
          apply le_antisymm
          · exact Finset.le_max' B _ (Finset.mem_of_mem_erase (Finset.max'_mem C hC))
          · exact Finset.le_max' C _ hmaxC
        have hnextC : ∀x∈C,x<C.max' hC → x+d∈C := by
          intro x hx hxmax
          have hxB := Finset.mem_of_mem_erase hx
          have hxmin := Finset.min'_le B x hxB
          change m≤ x at hxmin
          have hxmax' : x<B.max' hB := by simpa [hmaxeq] using hxmax
          exact Finset.mem_erase.mpr ⟨by omega,hnextB x hxB hxmax'⟩
        have hrepr := ih C.card (by omega) C rfl hC hnextC
        have hmnext : m+d∈C := Finset.mem_erase.mpr ⟨by omega,hnextB m hm hminmax⟩
        obtain ⟨i,hi,he⟩ := (mem_progressionSet (C.min' hC) d (m+d) C.card).mp
          (by rw [← hrepr]; exact hmnext)
        have hcmem := Finset.min'_mem C hC
        have hcmin : m<C.min' hC := by
          have hbase := Finset.min'_le B _ (Finset.mem_of_mem_erase hcmem)
          have hne := (Finset.mem_erase.mp hcmem).1
          change m≤ C.min' hC at hbase
          omega
        have hi0:i=0 := by
          by_contra hn
          have hip : (1:ℤ)≤ i := by omega
          nlinarith
        have hcm:C.min' hC=m+d := by simpa [hi0] using he
        have hset:B=insert m C := (Finset.insert_erase hm).symm
        change B=progressionSet m d B.card
        calc
          B=insert m C := hset
          _=insert m (progressionSet (m+d) d C.card) := by
            apply congrArg (insert m)
            calc C=progressionSet (C.min' hC) d C.card := hrepr
                 _=progressionSet (m+d) d C.card := by rw [hcm]
          _=progressionSet m d (C.card+1) := (progressionSet_succ m d C.card).symm
          _=progressionSet m d B.card := by rw [hCcard]
  exact hmain A.card A rfl hA hnext

theorem progressionSet_erase_first (a d : ℤ) (hd:0<d) (n : ℕ) (hn:0<n) :
    (progressionSet a d n).erase a=progressionSet (a+d) d (n-1) := by
  have hni : a∉progressionSet (a+d) d (n-1) := by
    intro ha
    obtain ⟨i,_,he⟩ := (mem_progressionSet _ _ _ _).mp ha
    have hi : (0:ℤ)≤ i := by positivity
    nlinarith
  have hn' : n=(n-1)+1 := by omega
  rw [hn',progressionSet_succ,Finset.erase_insert hni]
  congr 1 <;> omega

theorem progressionSet_erase_last (a d : ℤ) (hd:0<d) (n : ℕ) (hn:0<n) :
    (progressionSet a d n).erase (a+d*((n-1:ℕ):ℤ))=progressionSet a d (n-1) := by
  have hni : a+d*((n-1:ℕ):ℤ)∉progressionSet a d (n-1) := by
    intro ha
    obtain ⟨i,hi,he⟩ := (mem_progressionSet _ _ _ _).mp ha
    have hi' : (i:ℤ)<(n-1:ℕ) := by exact_mod_cast hi
    nlinarith
  have hn' : n=(n-1)+1 := by omega
  conv_lhs => arg 1; rw [hn',progressionSet_succ_right]
  rw [Finset.erase_insert hni]

theorem min_lt_max_of_card_two (A : Finset ℤ) (hA:A.Nonempty) (hn:2≤ A.card) :
    A.min' hA<A.max' hA := by
  have hp := ((mem_posDiffs A (span A:ℤ)).mp (span_mem_posDiffs A hn)).1
  have hs := span_cast A hA
  omega

theorem erase_max_min (A : Finset ℤ) (hA:A.Nonempty) (hn:2≤ A.card)
    (hB:(A.erase (A.max' hA)).Nonempty) :
    (A.erase (A.max' hA)).min' hB=A.min' hA := by
  have hmin := Finset.min'_mem A hA
  have hlt := min_lt_max_of_card_two A hA hn
  apply le_antisymm
  · exact Finset.min'_le _ _ (Finset.mem_erase.mpr ⟨ne_of_lt hlt,hmin⟩)
  · exact Finset.min'_le A _ (Finset.mem_of_mem_erase (Finset.min'_mem _ hB))

theorem erase_min_max (A : Finset ℤ) (hA:A.Nonempty) (hn:2≤ A.card)
    (hB:(A.erase (A.min' hA)).Nonempty) :
    (A.erase (A.min' hA)).max' hB=A.max' hA := by
  have hmax := Finset.max'_mem A hA
  have hlt := min_lt_max_of_card_two A hA hn
  apply le_antisymm
  · exact Finset.le_max' A _ (Finset.mem_of_mem_erase (Finset.max'_mem _ hB))
  · exact Finset.le_max' _ _ (Finset.mem_erase.mpr ⟨ne_of_gt hlt,hmax⟩)

theorem both_endpoint_deletions_AP (A : Finset ℤ) (hA:A.Nonempty) (hn:4≤ A.card)
    (hleft:IsArithmeticProgression (A.erase (A.max' hA)))
    (hright:IsArithmeticProgression (A.erase (A.min' hA))) : IsArithmeticProgression A := by
  let B:=A.erase (A.max' hA)
  let C:=A.erase (A.min' hA)
  let D:=B.erase (A.min' hA)
  have hmax := Finset.max'_mem A hA
  have hmin := Finset.min'_mem A hA
  have hlt := min_lt_max_of_card_two A hA (by omega)
  have hBcard:B.card=A.card-1 := Finset.card_erase_of_mem hmax
  have hCcard:C.card=A.card-1 := Finset.card_erase_of_mem hmin
  have hminB:A.min' hA∈B := Finset.mem_erase.mpr ⟨ne_of_lt hlt,hmin⟩
  have hDcard:D.card=A.card-2 := by
    have hh := Finset.card_erase_of_mem hminB
    change D.card=B.card-1 at hh
    omega
  have hB:B.Nonempty := Finset.card_pos.mp (by omega)
  have hC:C.Nonempty := Finset.card_pos.mp (by omega)
  have hD:D.Nonempty := Finset.card_pos.mp (by omega)
  obtain ⟨a,d,hd,hBrepr⟩ := hleft
  obtain ⟨b,e,he,hCrepr⟩ := hright
  change B=progressionSet a d B.card at hBrepr
  change C=progressionSet b e C.card at hCrepr
  rw [hBcard] at hBrepr
  rw [hCcard] at hCrepr
  have ham:A.min' hA=a := by
    have hm := erase_max_min A hA (by omega) hB
    change B.min' hB=A.min' hA at hm
    have hh : B.min' hB=(progressionSet a d (A.card-1)).min' (hBrepr ▸ hB) := by simp only [← hBrepr]
    rw [progressionSet_min a d hd (A.card-1) (by omega)] at hh
    exact hm.symm.trans hh
  have hcm:A.max' hA=b+e*((C.card-1:ℕ):ℤ) := by
    have hm := erase_min_max A hA (by omega) hC
    change C.max' hC=A.max' hA at hm
    have hh : C.max' hC=(progressionSet b e (A.card-1)).max' (hCrepr ▸ hC) := by simp only [← hCrepr]
    rw [progressionSet_max b e he (A.card-1) (by omega)] at hh
    simpa only [hCcard] using hm.symm.trans hh
  have hDrepr1:D=progressionSet (a+d) d (A.card-2) := by
    change B.erase (A.min' hA)=_
    rw [ham,hBrepr,progressionSet_erase_first a d hd (A.card-1) (by omega)]
    congr 1 <;> omega
  have hDrepr2:D=progressionSet b e (A.card-2) := by
    have hDC:D=C.erase (A.max' hA) := Finset.erase_right_comm
    rw [hDC,hcm,hCcard,hCrepr,progressionSet_erase_last b e he (A.card-1) (by omega)]
    congr 1 <;> omega
  have hbase:a+d=b := by
    have hh : (progressionSet (a+d) d (A.card-2)).min' (hDrepr1 ▸ hD)=
        (progressionSet b e (A.card-2)).min' (hDrepr2 ▸ hD) := by
      simp only [← hDrepr1,← hDrepr2]
    simpa only [progressionSet_min (a+d) d hd (A.card-2) (by omega),progressionSet_min b e he (A.card-2) (by omega)] using hh
  have hlast:(a+d)+d*((A.card-3:ℕ):ℤ)=b+e*((A.card-3:ℕ):ℤ) := by
    have hh : (progressionSet (a+d) d (A.card-2)).max' (hDrepr1 ▸ hD)=
        (progressionSet b e (A.card-2)).max' (hDrepr2 ▸ hD) := by
      simp only [← hDrepr1,← hDrepr2]
    have heq:(A.card-2)-1=A.card-3 := by omega
    simpa only [progressionSet_max (a+d) d hd (A.card-2) (by omega),progressionSet_max b e he (A.card-2) (by omega),heq] using hh
  have hde:d=e := by
    have hpos : (0:ℤ)<(A.card-3:ℕ) := by omega
    apply mul_right_cancel₀ (ne_of_gt hpos)
    linarith [hlast,hbase]
  refine ⟨a,d,hd,?_⟩
  have hset:A=insert (A.min' hA) C := (Finset.insert_erase hmin).symm
  have hc:A.card=C.card+1 := by omega
  calc
    A=insert (A.min' hA) C := hset
    _=insert a (progressionSet (a+d) d (A.card-1)) := by rw [ham,hCrepr,← hde,← hbase]
    _=progressionSet a d ((A.card-1)+1) := (progressionSet_succ a d (A.card-1)).symm
    _=progressionSet a d A.card := by congr 1; omega

end EnergyForcing.Counting

