import SeparatedProducts

set_option autoImplicit false

namespace EnergyForcing.Counting
open scoped BigOperators

def intervalMarks (s : ℕ) : Finset ℤ := Finset.Ico 0 (s:ℤ)

@[simp] theorem mem_intervalMarks (s : ℕ) (x : ℤ) :
    x∈intervalMarks s ↔ 0≤x ∧ x<(s:ℤ) := Finset.mem_Ico

@[simp] theorem intervalMarks_card (s : ℕ) : (intervalMarks s).card=s := by
  simp [intervalMarks,Int.card_Ico]

theorem interval_posDiffs (s : ℕ) (d : ℤ) :
    d∈posDiffs (intervalMarks s) ↔ 0<d ∧ d<(s:ℤ) := by
  rw [mem_posDiffs]
  simp only [mem_intervalMarks]
  constructor
  · rintro ⟨hd,u,hu,hud⟩; omega
  · rintro ⟨hd,hs⟩
    exact ⟨hd,0,⟨by omega,by omega⟩,by simpa using And.intro (le_of_lt hd) hs⟩

theorem interval_r (s : ℕ) (d : ℤ) (hd:0≤d) :
    r (intervalMarks s) d=s-d.toNat := by
  have hf : positiveFiber (intervalMarks s) d=Finset.Ico (0:ℤ) ((s:ℤ)-d) := by
    ext u
    simp only [mem_positiveFiber,mem_intervalMarks,Finset.mem_Ico]
    omega
  unfold r
  rw [hf,Int.card_Ico]
  omega

theorem interval_square_sum (s : ℕ) :
    (∑d∈posDiffs (intervalMarks s),(r (intervalMarks s) d)^2)=∑k∈Finset.range s,k^2 := by
  have hs : (∑d∈posDiffs (intervalMarks s),(r (intervalMarks s) d)^2)=
      ∑k∈Finset.Ico 1 s,k^2 := by
    refine Finset.sum_bij (fun d _ => s-d.toNat) ?_ ?_ ?_ ?_
    · intro d hd
      have hh := (interval_posDiffs s d).mp hd
      change s-d.toNat∈Finset.Ico 1 s
      apply Finset.mem_Ico.mpr
      omega
    · intro d hd e he hde
      have hh := (interval_posDiffs s d).mp hd
      have hh' := (interval_posDiffs s e).mp he
      change s-d.toNat=s-e.toNat at hde
      omega
    · intro k hk
      have hh := Finset.mem_Ico.mp hk
      refine ⟨((s-k:ℕ):ℤ),(interval_posDiffs s _).mpr ?_,?_⟩
      · omega
      · change s-((s-k:ℕ):ℤ).toNat=k
        omega
    · intro d hd
      rw [interval_r s d (le_of_lt ((interval_posDiffs s d).mp hd).1)]
  rw [hs]
  apply Finset.sum_subset (f:=fun k:ℕ=>k^2) (s₁:=Finset.Ico 1 s) (s₂:=Finset.range s)
  · intro k hk
    exact Finset.mem_range.mpr (Finset.mem_Ico.mp hk).2
  · intro k hk hn
    have hr := Finset.mem_range.mp hk
    have hz : k=0 := by
      by_contra hne
      exact hn (Finset.mem_Ico.mpr ⟨by omega,hr⟩)
    simp [hz]

theorem square_sum_polynomial (s : ℕ) :
    3*(s^2+2*∑k∈Finset.range s,k^2)=s*(2*s^2+1) := by
  induction s with
  | zero => simp
  | succ s ih =>
    rw [Finset.sum_range_succ]
    nlinarith

theorem interval_energy (s : ℕ) :
    3*E (intervalMarks s)=s*(2*s^2+1) := by
  rw [energy_count,intervalMarks_card,interval_square_sum]
  exact square_sum_polynomial s

theorem interval_fiber_one (s : ℕ) :
    positiveFiber (intervalMarks s) 1=intervalMarks (s-1) := by
  ext u
  simp only [mem_positiveFiber,mem_intervalMarks]
  omega

theorem progression_fiber (B : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q) (s : ℕ) :
    positiveFiber (scaledSum B (intervalMarks s) Q) Q=
      scaledSum B (intervalMarks (s-1)) Q := by
  have h := separated_scaled_fiber B (intervalMarks s) Q 1 hQ
  simpa only [mul_one,interval_fiber_one] using h

theorem T_zero_of_card_le_two (B : Finset ℤ) (hb:B.card≤2) : T B=0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  rintro ⟨x,y,z⟩ hp
  rcases (mem_sourceCorners B x y z).mp hp with ⟨hx,hy,hz,hyx,hxz,_⟩
  have hsub : ({x,y,z}:Finset ℤ)⊆B := by
    intro u hu
    simp only [Finset.mem_insert,Finset.mem_singleton] at hu
    rcases hu with rfl|rfl|rfl <;> assumption
  have hcard := Finset.card_le_card hsub
  have h3 : ({x,y,z}:Finset ℤ).card=3 := by
    simp [ne_of_lt hyx,ne_of_gt hyx,ne_of_lt hxz,ne_of_gt hxz,ne_of_lt (lt_trans hyx hxz)]
  omega

theorem energy_small_card (B : Finset ℤ) (hb:B.card≤2) :
    (E B:ℝ)=2*(B.card:ℝ)^2-(B.card:ℝ) := by
  rw [real_E,T_zero_of_card_le_two B hb]
  simp

theorem progression_gap (b t : ℝ)
    (hcase : t=2 ∨ (t=3 ∧ 3≤b) ∨ (t=4 ∧ 2≤b) ∨ (5≤t ∧ 1≤b)) :
    (2*(t-1)^2+1)*(27*t*b^2-45*b)-(2*t^2+1)*(18*(t-1)*b^2-15*b)≥0 := by
  have he : (2*(t-1)^2+1)*(27*t*b^2-45*b)-(2*t^2+1)*(18*(t-1)*b^2-15*b)=
      3*b*(t-2)*(6*b*t^2-12*b*t-3*b-20*t+20) := by ring
  rw [he]
  rcases hcase with ht|⟨ht,hb⟩|⟨ht,hb⟩|⟨ht,hb⟩
  · rw [ht]; norm_num
  · rw [ht]; norm_num
    have h1 : 0≤3*b*(3-2) := by positivity
    have h2 : 0≤6*b*3^2-12*b*3-3*b-20*3+20 := by nlinarith
    nlinarith
  · rw [ht]; norm_num
    have h1 : 0≤3*b*(4-2) := by positivity
    have h2 : 0≤6*b*4^2-12*b*4-3*b-20*4+20 := by nlinarith
    nlinarith
  · have hq : 0≤6*t^2-12*t-3 := by nlinarith [sq_nonneg (t-5)]
    have hbq := mul_le_mul_of_nonneg_right hb hq
    have hi : 0≤6*b*t^2-12*b*t-3*b-20*t+20 := by
      nlinarith [mul_nonneg (show 0≤t-5 by linarith) (show 0≤6*t-2 by linarith)]
    exact mul_nonneg (mul_nonneg (mul_nonneg (by norm_num) (by linarith)) (by linarith)) hi

theorem progression_comparison_main (b t e f g : ℝ) (ht:2≤t)
    (hf:3*f=e*(t-1)*(2*(t-1)^2+1)) (hg:3*g=e*t*(2*t^2+1))
    (hbound:f≤6*(t-1)^2*b^2-5*(t-1)*b)
    (hgap:(2*(t-1)^2+1)*(27*t*b^2-45*b)-(2*t^2+1)*(18*(t-1)*b^2-15*b)≥0) :
    g≤9*(t*b)^2-15*(t*b) := by
  have hu : 0<t-1 := by linarith
  have hD : 0<2*(t-1)^2+1 := by positivity
  have hA : 0≤2*t^2+1 := by positivity
  have he : e*(2*(t-1)^2+1)≤18*(t-1)*b^2-15*b := by
    apply (mul_le_mul_left hu).mp
    nlinarith [hf,hbound]
  have hea : e*(2*t^2+1)≤27*t*b^2-45*b := by
    apply (mul_le_mul_left hD).mp
    have hh := mul_le_mul_of_nonneg_left he hA
    nlinarith [hgap]
  have hfinal := mul_le_mul_of_nonneg_left hea (show 0≤t by linarith)
  nlinarith [hg]

theorem progression_comparison (b t : ℕ) (e f g : ℝ) (hb:1≤b) (ht:2≤t)
    (hf:3*f=e*((t:ℝ)-1)*(2*((t:ℝ)-1)^2+1))
    (hg:3*g=e*(t:ℝ)*(2*(t:ℝ)^2+1))
    (hbound:f≤6*((t:ℝ)-1)^2*(b:ℝ)^2-5*((t:ℝ)-1)*(b:ℝ))
    (hsmall:b≤2 → e=2*(b:ℝ)^2-(b:ℝ)) :
    g≤9*((t:ℝ)*(b:ℝ))^2-15*((t:ℝ)*(b:ℝ)) := by
  by_cases h3 : t=3 ∧ b≤2
  · obtain ⟨rfl,hb2⟩ := h3
    have he := hsmall hb2
    interval_cases b <;> norm_num at * <;> nlinarith
  by_cases h4 : t=4 ∧ b=1
  · obtain ⟨rfl,rfl⟩ := h4
    have he := hsmall (by decide)
    norm_num at *
    nlinarith
  apply progression_comparison_main (b:ℝ) (t:ℝ) e f g (by exact_mod_cast ht) hf hg hbound
  apply progression_gap
  by_cases ht2 : t=2
  · exact Or.inl (by exact_mod_cast ht2)
  by_cases ht3 : t=3
  · right; left
    exact ⟨by exact_mod_cast ht3,by exact_mod_cast (show 3≤b by omega)⟩
  by_cases ht4 : t=4
  · right; right; left
    exact ⟨by exact_mod_cast ht4,by exact_mod_cast (show 2≤b by omega)⟩
  · right; right; right
    exact ⟨by exact_mod_cast (show 5≤t by omega),by exact_mod_cast hb⟩

def TwoGolombPartition (A : Finset ℤ) : Prop :=
  ∃B C : Finset ℤ,Disjoint B C ∧ Golomb (·∈B) ∧ Golomb (·∈C) ∧ A=B∪C

theorem energy_bound_of_twoGolomb (A : Finset ℤ) (hA:TwoGolombPartition A) :
    (E A:ℝ)≤6*(A.card:ℝ)^2-5*(A.card:ℝ) := by
  obtain ⟨B,C,hBC,hB,hC,rfl⟩ := hA
  have ht : (T (B∪C):ℝ)≤2*(M (B∪C):ℝ) := by exact_mod_cast two_golomb_T_le_twice_M B C hBC hB hC
  have he := real_E (B∪C)
  have hm := real_M (B∪C)
  nlinarith

theorem fiber_twoGolomb (A : Finset ℤ) (z : Point→Bool)
    (hz:properOn (strictSource (·∈A)) z) (d : ℤ) (hd:0<d) :
    TwoGolombPartition (positiveFiber A d) := by
  exact ⟨momentClass A z d false,momentClass A z d true,moment_classes_disjoint A z d,
    moment_class_golomb A z hz d hd false,moment_class_golomb A z hz d hd true,
    (moment_classes_union A z d).symm⟩

theorem progression_energy_of_partition (B : Finset ℤ) (hB:B.Nonempty)
    (Q : ℤ) (hQ:2*(span B:ℤ)<Q) (t : ℕ) (ht:2≤t)
    (hp:TwoGolombPartition (scaledSum B (intervalMarks (t-1)) Q)) :
    (E (scaledSum B (intervalMarks t) Q):ℝ)≤
      9*((t:ℝ)*(B.card:ℝ))^2-15*((t:ℝ)*(B.card:ℝ)) := by
  have hfactor (s : ℕ) : (E (scaledSum B (intervalMarks s) Q):ℝ)=
      (E B:ℝ)*(E (intervalMarks s):ℝ) := by exact_mod_cast separated_energy_product B (intervalMarks s) Q hQ
  have hpoly (s : ℕ) : 3*(E (intervalMarks s):ℝ)=(s:ℝ)*(2*(s:ℝ)^2+1) := by exact_mod_cast interval_energy s
  have hA : 3*(E (scaledSum B (intervalMarks t) Q):ℝ)=(E B:ℝ)*(t:ℝ)*(2*(t:ℝ)^2+1) := by
    rw [hfactor]
    have hh := congrArg (fun x:ℝ=>(E B:ℝ)*x) (hpoly t)
    dsimp only at hh
    nlinarith
  have hF : 3*(E (scaledSum B (intervalMarks (t-1)) Q):ℝ)=
      (E B:ℝ)*((t:ℝ)-1)*(2*((t:ℝ)-1)^2+1) := by
    rw [hfactor]
    have hh := congrArg (fun x:ℝ=>(E B:ℝ)*x) (hpoly (t-1))
    dsimp only at hh
    rw [Nat.cast_sub (by omega : 1≤t),Nat.cast_one] at hh
    nlinarith
  have hbound := energy_bound_of_twoGolomb _ hp
  rw [scaledSum_card B (intervalMarks (t-1)) Q hQ,intervalMarks_card,Nat.cast_mul,
    Nat.cast_sub (by omega : 1≤t),Nat.cast_one] at hbound
  apply progression_comparison B.card t (E B:ℝ)
    (E (scaledSum B (intervalMarks (t-1)) Q):ℝ)
    (E (scaledSum B (intervalMarks t) Q):ℝ) (Finset.card_pos.mpr hB) ht hF hA
  · nlinarith [hbound]
  · exact energy_small_card B

theorem progression_bounds_of_partition (B : Finset ℤ) (hB:B.Nonempty)
    (Q : ℤ) (hQ:2*(span B:ℤ)<Q) (t : ℕ) (ht:2≤t)
    (hp:TwoGolombPartition (scaledSum B (intervalMarks (t-1)) Q)) :
    let A:=scaledSum B (intervalMarks t) Q
    (E A:ℝ)≤9*(A.card:ℝ)^2-15*(A.card:ℝ) ∧
    (T A:ℝ)≤(7/2:ℝ)*(M A:ℝ)-(7/4:ℝ)*(A.card:ℝ) ∧
    M A≤8*span A := by
  dsimp
  let A:=scaledSum B (intervalMarks t) Q
  have hcard : (A.card:ℝ)=(t:ℝ)*(B.card:ℝ) := by
    simp only [A,scaledSum_card B (intervalMarks t) Q hQ,intervalMarks_card,Nat.cast_mul]
    ring
  have he := progression_energy_of_partition B hB Q hQ t ht hp
  rw [← hcard] at he
  have hE := real_E A
  have hM := real_M A
  have hT : (T A:ℝ)≤(7/2:ℝ)*(M A:ℝ)-(7/4:ℝ)*(A.card:ℝ) := by nlinarith
  refine ⟨he,hT,?_⟩
  have hweak : (T A:ℝ)≤(7/2:ℝ)*(M A:ℝ) := by
    have hn : (0:ℝ)≤A.card := by positivity
    linarith
  have hs := span_pair_bound A (7/2:ℝ) (by norm_num) hweak
  norm_num at hs
  exact_mod_cast hs

theorem progression_bounds (B : Finset ℤ) (hB:B.Nonempty)
    (Q : ℤ) (hQ:2*(span B:ℤ)<Q) (t : ℕ) (ht:2≤t)
    (z : Point→Bool) (hz:properOn (strictSource (·∈scaledSum B (intervalMarks t) Q)) z) :
    let A:=scaledSum B (intervalMarks t) Q
    (E A:ℝ)≤9*(A.card:ℝ)^2-15*(A.card:ℝ) ∧
    (T A:ℝ)≤(7/2:ℝ)*(M A:ℝ)-(7/4:ℝ)*(A.card:ℝ) ∧
    M A≤8*span A := by
  apply progression_bounds_of_partition B hB Q hQ t ht
  have hQpos : 0<Q := by omega
  have hp := fiber_twoGolomb (scaledSum B (intervalMarks t) Q) z hz Q hQpos
  rw [progression_fiber B Q hQ] at hp
  exact hp

end EnergyForcing.Counting
