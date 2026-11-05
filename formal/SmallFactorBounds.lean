import OverlapRestrictions

set_option autoImplicit false

namespace EnergyForcing.Counting
open scoped BigOperators

def cornerTriple (p : ℤ×ℤ×ℤ) : Finset ℤ := {p.1,p.2.1,p.2.2}

theorem cornerTriple_injective (A : Finset ℤ) :
    Set.InjOn cornerTriple (sourceCorners A) := by
  rintro ⟨x,y,z⟩ hp ⟨x',y',z'⟩ hq he
  have hp' := (mem_sourceCorners A x y z).mp hp
  have hq' := (mem_sourceCorners A x' y' z').mp hq
  dsimp [cornerTriple] at he
  have hx : x∈({x',y',z'}:Finset ℤ) := by rw [← he]; simp [cornerTriple]
  have hy : y∈({x',y',z'}:Finset ℤ) := by rw [← he]; simp [cornerTriple]
  have hz : z∈({x',y',z'}:Finset ℤ) := by rw [← he]; simp [cornerTriple]
  have hx' : x'∈({x,y,z}:Finset ℤ) := by rw [he]; simp [cornerTriple]
  have hy' : y'∈({x,y,z}:Finset ℤ) := by rw [he]; simp [cornerTriple]
  have hz' : z'∈({x,y,z}:Finset ℤ) := by rw [he]; simp [cornerTriple]
  simp only [Finset.mem_insert,Finset.mem_singleton] at hx hy hz hx' hy' hz'
  apply Prod.ext
  · omega
  · apply Prod.ext <;> dsimp <;> omega

theorem corner_le_choose_three (A : Finset ℤ) : T A≤A.card.choose 3 := by
  rw [← Finset.card_powersetCard]
  apply Finset.card_le_card_of_injOn cornerTriple ?_ (cornerTriple_injective A)
  rintro ⟨x,y,z⟩ hp
  rcases (mem_sourceCorners A x y z).mp hp with ⟨hx,hy,hz,hyx,hxz,_⟩
  apply Finset.mem_powersetCard.mpr
  constructor
  · intro u hu
    simp only [cornerTriple,Finset.mem_insert,Finset.mem_singleton] at hu
    rcases hu with rfl|rfl|rfl <;> assumption
  · simp [cornerTriple,ne_of_lt hyx,ne_of_gt hyx,ne_of_lt hxz,ne_of_gt hxz,
      ne_of_lt (lt_trans hyx hxz)]

theorem real_choose_three (n : ℕ) :
    6*(n.choose 3:ℝ)=(n:ℝ)*((n:ℝ)-1)*((n:ℝ)-2) := by
  induction n with
  | zero => norm_num
  | succ n ih =>
    rw [Nat.choose_succ_succ,Nat.cast_add]
    push_cast
    have h2 := Nat.cast_choose_two ℝ n
    nlinarith

theorem energy_le_interval_energy (A : Finset ℤ) :
    3*(E A:ℝ)≤(A.card:ℝ)*(2*(A.card:ℝ)^2+1) := by
  have ht : (T A:ℝ)≤(A.card.choose 3:ℝ) := by exact_mod_cast corner_le_choose_three A
  have hc := real_choose_three A.card
  have he := real_E A
  nlinarith

theorem span_fiber_singleton (A : Finset ℤ) (hA:A.Nonempty) :
    positiveFiber A (span A:ℤ)={A.min' hA} := by
  ext u
  simp only [mem_positiveFiber,Finset.mem_singleton]
  have hs := span_cast A hA
  constructor
  · rintro ⟨hu,hu'⟩
    have hlo := Finset.min'_le A u hu
    have hhi := Finset.le_max' A (u+(span A:ℤ)) hu'
    omega
  · intro hu
    subst u
    exact ⟨Finset.min'_mem A hA,by convert Finset.max'_mem A hA using 1 <;> omega⟩

theorem r_span_one (A : Finset ℤ) (hA:A.Nonempty) : r A (span A:ℤ)=1 := by
  simp [r,span_fiber_singleton A hA]

theorem span_mem_posDiffs (A : Finset ℤ) (hA:2≤A.card) : (span A:ℤ)∈posDiffs A := by
  obtain ⟨d,u,hd,hu⟩ := exists_positive_pair A hA
  have hu' := (mem_positiveFiber A d u).mp hu
  have hn : A.Nonempty := ⟨u,hu'.1⟩
  have hb := mark_difference_bounds A (u+d) u hu'.2 hu'.1
  have hs := span_cast A hn
  exact (mem_posDiffs A _).mpr ⟨by omega,A.min' hn,Finset.min'_mem A hn,
    by convert Finset.max'_mem A hn using 1 <;> omega⟩

theorem cap_two_corner_bound (A : Finset ℤ) (hA:2≤A.card)
    (hcap:∀d:ℤ,0<d → r A d≤2) : 2*T A+1≤M A := by
  have hm := span_mem_posDiffs A hA
  have hn : A.Nonempty := Finset.card_pos.mp (by omega)
  have hpoint (d : ℤ) (hd:d∈posDiffs A) :
      2*(r A d).choose 2+(if d=(span A:ℤ) then 1 else 0)≤r A d := by
    by_cases he:d=(span A:ℤ)
    · subst d; rw [r_span_one A hn]; norm_num
    · rw [if_neg he]
      have hc := hcap d ((mem_posDiffs A d).mp hd).1
      interval_cases hr:r A d <;> norm_num
  have hs := Finset.sum_le_sum hpoint
  rw [Finset.sum_add_distrib,← Finset.mul_sum,← corner_count,sum_r] at hs
  have hind : (∑d∈posDiffs A,if d=(span A:ℤ) then (1:ℕ) else 0)=1 := by simp [hm]
  rw [hind] at hs
  exact hs

theorem four_mark_cap_two (A : Finset ℤ) (hA:A.card=4)
    (hcap:∀d:ℤ,0<d → r A d≤2) : T A≤2 ∧ E A≤36 := by
  have ht := cap_two_corner_bound A (by omega) hcap
  have hm : M A=6 := by unfold M; rw [hA]; decide
  have he := energy_corner_identity A
  rw [hA] at he
  norm_num at he
  omega

end EnergyForcing.Counting
