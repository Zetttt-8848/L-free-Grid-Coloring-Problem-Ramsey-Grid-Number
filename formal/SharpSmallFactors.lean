import ArithmeticProgressions

set_option autoImplicit false
namespace EnergyForcing.Counting

 theorem reflectedSource_card (A : Finset ℤ) (q : ℤ) :
    (reflectedSource A q).card=A.card := by
  unfold reflectedSource
  exact Finset.card_image_of_injective _ (by intro a b h; dsimp at h; omega)

theorem reflectedSource_involutive (A : Finset ℤ) (q : ℤ) :
    reflectedSource (reflectedSource A q) q=A := by
  ext x
  simp

theorem progressionSet_reflect (a d q : ℤ) (n : ℕ) (hn:0< n) :
    reflectedSource (progressionSet a d n) q=
      progressionSet (q-a-d*((n-1:ℕ):ℤ)) d n := by
  ext x
  simp only [mem_reflectedSource,mem_progressionSet]
  constructor
  · rintro ⟨i,hi,he⟩
    refine ⟨n-1-i,by omega,?_⟩
    have hij : ((n-1-i:ℕ):ℤ)+(i:ℤ)=((n-1:ℕ):ℤ) := by omega
    have hm:=congrArg (fun v:ℤ=> d*v) hij
    dsimp at hm
    nlinarith [hm]
  · rintro ⟨i,hi,he⟩
    refine ⟨n-1-i,by omega,?_⟩
    have hij : ((n-1-i:ℕ):ℤ)+(i:ℤ)=((n-1:ℕ):ℤ) := by omega
    have hm:=congrArg (fun v:ℤ=> d*v) hij
    dsimp at hm
    nlinarith [hm]

theorem arithmeticProgression_reflect (A : Finset ℤ) (q : ℤ)
    (hAP:IsArithmeticProgression A) : IsArithmeticProgression (reflectedSource A q) := by
  obtain ⟨a,d,hd,h⟩:=hAP
  by_cases hn:0< A.card
  · refine ⟨q-a-d*((A.card-1:ℕ):ℤ),d,hd,?_⟩
    rw [reflectedSource_card]
    calc reflectedSource A q=reflectedSource (progressionSet a d A.card) q := congrArg (fun X=> reflectedSource X q) h
         _=_ := progressionSet_reflect a d q A.card hn
  · have hA:A=∅ := Finset.card_eq_zero.mp (by omega)
    refine ⟨0,1,by omega,?_⟩
    simp [hA,reflectedSource,progressionSet]

theorem reflectedSource_max (A : Finset ℤ) (q : ℤ) (hA:A.Nonempty)
    (hR:(reflectedSource A q).Nonempty) :
    (reflectedSource A q).max' hR=q-A.min' hA := by
  apply le_antisymm
  · apply Finset.max'_le
    intro x hx
    have h:=Finset.min'_le A (q-x) ((mem_reflectedSource A q x).mp hx)
    omega
  · apply Finset.le_max'
    simpa using Finset.min'_mem A hA

theorem reflectedSource_erase (A : Finset ℤ) (q a : ℤ) :
    reflectedSource (A.erase a) q=(reflectedSource A q).erase (q-a) := by
  ext x
  simp only [mem_reflectedSource,Finset.mem_erase]
  constructor <;> rintro ⟨h,hx⟩ <;> exact ⟨by omega,hx⟩

def topCornerPairs (A : Finset ℤ) (m : ℤ) : Finset (ℤ×ℤ) :=
  (sourceCells (A.erase m)).filter fun p=> p.2+m-p.1∈A

theorem topCornerPairs_card (A : Finset ℤ) (hA:A.Nonempty) :
    (topCornerPairs A (A.max' hA)).card=
      ((sourceCorners A).filter fun p=> p.2.2=A.max' hA).card := by
  refine Finset.card_bij' (fun p _=>(p.1,p.2,A.max' hA)) (fun p _=>(p.1,p.2.1)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y⟩ hp
    simp only [topCornerPairs,Finset.mem_filter,mem_sourceCells,Finset.mem_erase] at hp
    apply Finset.mem_filter.mpr
    refine ⟨(mem_sourceCorners A x y _).mpr ?_,rfl⟩
    have hxmax:=Finset.le_max' A x hp.1.1.2
    exact ⟨hp.1.1.2,hp.1.2.1.2,Finset.max'_mem A hA,hp.1.2.2,by omega,hp.2⟩
  · rintro ⟨x,y,z⟩ hp
    rcases Finset.mem_filter.mp hp with ⟨hp,hz⟩
    dsimp at hz
    subst z
    rcases (mem_sourceCorners A x y _).mp hp with ⟨hx,hy,_,hyx,hxm,hw⟩
    simp only [topCornerPairs,Finset.mem_filter,mem_sourceCells,Finset.mem_erase]
    exact ⟨⟨⟨by omega,hx⟩,⟨by omega,hy⟩,hyx⟩,hw⟩
  · rintro ⟨x,y⟩ _; rfl
  · rintro ⟨x,y,z⟩ hp
    have hz: z=A.max' hA:=(Finset.mem_filter.mp hp).2
    simp [hz]

theorem corners_erase_max (A : Finset ℤ) (hA:A.Nonempty) :
    sourceCorners (A.erase (A.max' hA))=
      (sourceCorners A).filter (fun p=> p.2.2≠A.max' hA) := by
  ext ⟨x,y,z⟩
  simp only [mem_sourceCorners,Finset.mem_filter,Finset.mem_erase]
  constructor
  · rintro ⟨hx,hy,hz,hyx,hxz,hw⟩
    exact ⟨⟨hx.2,hy.2,hz.2,hyx,hxz,hw.2⟩,hz.1⟩
  · rintro ⟨⟨hx,hy,hz,hyx,hxz,hw⟩,hzm⟩
    have hzmax:=Finset.le_max' A z hz
    exact ⟨⟨by omega,hx⟩,⟨by omega,hy⟩,⟨hzm,hz⟩,hyx,hxz,⟨by omega,hw⟩⟩

theorem top_deletion_identity (A : Finset ℤ) (hA:A.Nonempty) :
    T A=T (A.erase (A.max' hA))+(topCornerPairs A (A.max' hA)).card := by
  have h:=Finset.filter_card_add_filter_neg_card_eq_card (s:=sourceCorners A)
    (fun p=> p.2.2=A.max' hA)
  rw [← corners_erase_max A hA,← topCornerPairs_card A hA] at h
  unfold T
  omega

theorem all_top_pairs_AP (A : Finset ℤ) (hA:A.Nonempty) (hn:2≤ A.card)
    (hfull:topCornerPairs A (A.max' hA)=sourceCells (A.erase (A.max' hA))) :
    IsArithmeticProgression A := by
  let m:=A.max' hA
  let B:=A.erase m
  have hm:m∈A:=Finset.max'_mem A hA
  have hbcard:B.card=A.card-1:=Finset.card_erase_of_mem hm
  have hB:B.Nonempty:=Finset.card_pos.mp (by omega)
  let b:=B.max' hB
  have hb:b∈B:=Finset.max'_mem B hB
  have hbA:b∈A:=Finset.mem_of_mem_erase hb
  have hbmax:=Finset.le_max' A b hbA
  have hbne:b≠m:=(Finset.mem_erase.mp hb).1
  have hbm:b< m:=by omega
  have hnext:∀x∈A,x< m→x+(m-b)∈A:=by
    intro x hx hxm
    have hxB:x∈B:=Finset.mem_erase.mpr ⟨ne_of_lt hxm,hx⟩
    have hxb:x≤ b:=Finset.le_max' B x hxB
    by_cases he:x=b
    · simpa [he] using hm
    · have hcell:(b,x)∈sourceCells B:=(mem_sourceCells B b x).mpr ⟨hb,hxB,by omega⟩
      have ht:(b,x)∈topCornerPairs A m:=by rw [hfull];exact hcell
      have hw: x+m-b∈A:=(Finset.mem_filter.mp ht).2
      convert hw using 1 <;> omega
  exact ⟨A.min' hA,m-b,by omega,successor_closed_progression A hA (m-b) (by omega) hnext⟩

theorem nonAP_top_deletion (A : Finset ℤ) (hA:A.Nonempty) (hn:2≤ A.card)
    (hAP:¬IsArithmeticProgression A) :
    T A+1≤ T (A.erase (A.max' hA))+M (A.erase (A.max' hA)) := by
  have hsub:topCornerPairs A (A.max' hA)⊆sourceCells (A.erase (A.max' hA)):=Finset.filter_subset _ _
  have hlt:(topCornerPairs A (A.max' hA)).card<(sourceCells (A.erase (A.max' hA))).card:=by
    by_contra h
    exact hAP (all_top_pairs_AP A hA hn (Finset.eq_of_subset_of_card_le hsub (by omega)))
  rw [sourceCells_card] at hlt
  rw [top_deletion_identity A hA]
  omega

theorem nonAP_bottom_deletion (A : Finset ℤ) (hA:A.Nonempty) (hn:2≤ A.card)
    (hAP:¬IsArithmeticProgression A) :
    T A+1≤ T (A.erase (A.min' hA))+M (A.erase (A.min' hA)) := by
  let R:=reflectedSource A 0
  have hrcard:R.card=A.card:=reflectedSource_card A 0
  have hR:R.Nonempty:=Finset.card_pos.mp (by omega)
  have hnot:¬IsArithmeticProgression R:=by
    intro hh
    have ht:=arithmeticProgression_reflect R 0 hh
    rw [reflectedSource_involutive] at ht
    exact hAP ht
  have h:=nonAP_top_deletion R hR (by omega) hnot
  have hm:R.max' hR=0-A.min' hA:=reflectedSource_max A 0 hA hR
  have he:R.erase (R.max' hR)=reflectedSource (A.erase (A.min' hA)) 0:=by
    rw [hm,reflectedSource_erase]
  rw [he] at h
  dsimp [R] at h
  simp only [reflected_T,M,reflectedSource_card] at h
  exact h

/-- Every nonprogression loses at least n−2 of the potential increasing triples. -/
theorem nonAP_corner_deficit (A : Finset ℤ) (hn:3≤ A.card)
    (hAP:¬IsArithmeticProgression A) : T A+(A.card-2)≤ A.card.choose 3 := by
  have main : ∀n:ℕ,∀A:Finset ℤ,A.card=n → 3≤ n →
      ¬IsArithmeticProgression A → T A+(A.card-2)≤ A.card.choose 3 := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro A hcard hn hnot
      have hA:A.Nonempty:=Finset.card_pos.mp (by omega)
      have hm:=Finset.max'_mem A hA
      have hl:=Finset.min'_mem A hA
      have htcard:(A.erase (A.max' hA)).card=A.card-1:=Finset.card_erase_of_mem hm
      have hbcard:(A.erase (A.min' hA)).card=A.card-1:=Finset.card_erase_of_mem hl
      by_cases h3:n=3
      · have ha:A.card=3:=by omega
        have hb:(A.erase (A.max' hA)).card=2:=by omega
        have ht:=T_zero_of_card_le_two (A.erase (A.max' hA)) (by omega)
        have h:=nonAP_top_deletion A hA (by omega) hnot
        rw [ht,M,hb] at h
        have hchoose2:Nat.choose 2 2=1:=by decide
        have hchoose3:Nat.choose 3 3=1:=by decide
        rw [hchoose2] at h
        rw [ha,hchoose3]
        omega
      · have hn4:4≤ A.card:=by omega
        have hx : ∃B:Finset ℤ,B.card=A.card-1 ∧ ¬IsArithmeticProgression B ∧
            T A+1≤ T B+M B := by
          by_cases htop:IsArithmeticProgression (A.erase (A.max' hA))
          · have hbottom:¬IsArithmeticProgression (A.erase (A.min' hA)):=by
              intro hh
              exact hnot (both_endpoint_deletions_AP A hA hn4 htop hh)
            exact ⟨A.erase (A.min' hA),hbcard,hbottom,nonAP_bottom_deletion A hA (by omega) hnot⟩
          · exact ⟨A.erase (A.max' hA),htcard,htop,nonAP_top_deletion A hA (by omega) hnot⟩
        obtain ⟨B,hBcard,hnotB,hstep⟩:=hx
        have hbound:=ih B.card (by omega) B rfl (by omega) hnotB
        have hpascal:A.card.choose 3=(A.card-1).choose 3+(A.card-1).choose 2:=by
          conv_lhs => rw [show A.card=(A.card-1)+1 by omega]
          simpa [Nat.add_comm] using (Nat.choose_succ_succ (A.card-1) 2)
        dsimp [M] at hstep
        rw [hBcard] at hbound hstep
        rw [hpascal]
        omega
  exact main A.card A rfl hn hAP

theorem two_mark_AP (A : Finset ℤ) (hn:A.card=2) : IsArithmeticProgression A := by
  have hA:A.Nonempty:=Finset.card_pos.mp (by omega)
  apply all_top_pairs_AP A hA (by omega)
  have hb:(A.erase (A.max' hA)).card=1:=by
    rw [Finset.card_erase_of_mem (Finset.max'_mem A hA),hn]
  have he:sourceCells (A.erase (A.max' hA))=∅:=by
    apply Finset.card_eq_zero.mp
    rw [sourceCells_card,M,hb]
    decide
  simp [topCornerPairs,he]

theorem maximal_corner_AP (A : Finset ℤ) (hn:2≤ A.card)
    (he:T A=A.card.choose 3) : IsArithmeticProgression A := by
  by_cases h2:A.card=2
  · exact two_mark_AP A h2
  · by_contra hnot
    have h:=nonAP_corner_deficit A (by omega) hnot
    omega

theorem nonAP_energy_deficit (A : Finset ℤ) (hn:3≤ A.card)
    (hAP:¬IsArithmeticProgression A) :
    3*(E A:ℝ)+12*((A.card:ℝ)-2)≤(A.card:ℝ)*(2*(A.card:ℝ)^2+1) := by
  have h:=nonAP_corner_deficit A hn hAP
  have hcast:(T A:ℝ)+(A.card:ℝ)-2≤(A.card.choose 3:ℝ):=by
    have hc:(A.card-2:ℕ)=A.card-2:=rfl
    have hreal : (T A:ℝ)+((A.card-2:ℕ):ℝ)≤(A.card.choose 3:ℝ):=by exact_mod_cast h
    rw [Nat.cast_sub (by omega:2≤ A.card),Nat.cast_ofNat] at hreal
    linarith
  have hchoose:=real_choose_three A.card
  have he:=real_E A
  nlinarith

theorem six_mark_nonAP_bounds (A : Finset ℤ) (hn:A.card=6)
    (hAP:¬IsArithmeticProgression A) : T A≤16 ∧ E A≤130 := by
  have h:=nonAP_corner_deficit A (by omega) hAP
  rw [hn] at h
  have hc:Nat.choose 6 3=20:=by decide
  rw [hc] at h
  have he:=energy_corner_identity A
  rw [hn] at he
  constructor <;> omega

end EnergyForcing.Counting
