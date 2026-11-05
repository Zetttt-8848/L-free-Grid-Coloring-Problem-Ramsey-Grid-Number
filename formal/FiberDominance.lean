import SourceCounting

namespace EnergyForcing.FiberDominance

open EnergyForcing.Counting
open scoped BigOperators

def fiberClass (A : Finset ℤ) (z : ℤ × ℤ → Bool) (d : ℤ) (b : Bool) : Finset ℤ :=
  (positiveFiber A d).filter fun u => z (u+d,u)=b

def shared (A : Finset ℤ) (z : ℤ × ℤ → Bool) (d : ℤ) : ℕ :=
  (posDiffs (fiberClass A z d false) ∩ posDiffs (fiberClass A z d true)).card

def R (A : Finset ℤ) (z : ℤ × ℤ → Bool) : ℕ :=
  ∑ d∈posDiffs A, shared A z d

def D (A : Finset ℤ) (z : ℤ × ℤ → Bool) : ℕ :=
  ∑ d∈posDiffs A, (r A d-1)*Nat.dist (fiberClass A z d false).card (fiberClass A z d true).card

noncomputable def P (A : Finset ℤ) (z : ℤ × ℤ → Bool) : ℝ :=
  (∑ d∈posDiffs A, (r A d:ℝ)*
    ((Nat.dist (fiberClass A z d false).card (fiberClass A z d true).card-1:ℕ):ℝ))/2

theorem class_partition (A : Finset ℤ) (z : ℤ × ℤ → Bool) (d : ℤ) :
    (fiberClass A z d false).card + (fiberClass A z d true).card = r A d := by
  have hd : Disjoint (fiberClass A z d false) (fiberClass A z d true) := by
    apply Finset.disjoint_left.mpr
    intro x hx hy
    have hf := (Finset.mem_filter.mp hx).2
    have ht := (Finset.mem_filter.mp hy).2
    rw [hf] at ht
    contradiction
  have hu : fiberClass A z d false ∪ fiberClass A z d true = positiveFiber A d := by
    ext u
    simp only [fiberClass,Finset.mem_union,Finset.mem_filter]
    cases h : z (u+d,u) <;> simp [h]
  rw [← Finset.card_union_of_disjoint hd,hu]
  rfl

theorem positiveDiff_card (B : Finset ℤ) : (posDiffs B).card ≤ B.card.choose 2 := by
  have he : posDiffs B = (sourceCells B).image (fun p => p.1-p.2) := by
    ext d
    constructor
    · intro hd
      obtain ⟨hpos,u,hu,hud⟩ := (mem_posDiffs B d).mp hd
      refine Finset.mem_image.mpr ⟨(u+d,u),?_,by simp⟩
      exact (mem_sourceCells B (u+d) u).mpr ⟨hud,hu,by omega⟩
    · intro hd
      obtain ⟨⟨x,y⟩,hp,heq⟩ := Finset.mem_image.mp hd
      rcases (mem_sourceCells B x y).mp hp with ⟨hx,hy,hxy⟩
      dsimp at heq
      apply (mem_posDiffs B d).mpr
      refine ⟨by omega,y,hy,?_⟩
      convert hx using 1 <;> omega
  rw [he]
  exact (Finset.card_image_le).trans (le_of_eq (sourceCells_card B))

theorem shared_bounds (A : Finset ℤ) (z : ℤ × ℤ → Bool) (d : ℤ) :
    shared A z d ≤ (fiberClass A z d false).card.choose 2 ∧
    shared A z d ≤ (fiberClass A z d true).card.choose 2 := by
  constructor
  · exact (Finset.card_le_card Finset.inter_subset_left).trans (positiveDiff_card _)
  · exact (Finset.card_le_card Finset.inter_subset_right).trans (positiveDiff_card _)

theorem scalar_dominance_left (b c q : ℕ) (hbc : b≤c) (hb : b≤3)
    (hq : q≤b.choose 2) :
    10*q+(b+c-1)*Nat.dist b c ≤ 2*(b+c).choose 2 := by
  have hd : Nat.dist b c + 2*b = b+c := by rw [Nat.dist_eq_sub_of_le hbc]; omega
  have hs : 10*q ≤ 2*b*(b+c-1) := by
    interval_cases b <;> norm_num at hq ⊢ <;> nlinarith
  have hc : (b+c)*(b+c-1)=2*(b+c).choose 2 := by
    have hh := square_eq_self_add_twice_choose (b+c)
    rw [pow_two] at hh
    rw [Nat.mul_sub_left_distrib,Nat.mul_one]
    omega
  have he := congrArg (fun x : ℕ => (b+c-1)*x) hd
  nlinarith

theorem scalar_dominance (b c q : ℕ) (hm : min b c≤3)
    (hq : q≤b.choose 2 ∧ q≤c.choose 2) :
    10*q+(b+c-1)*Nat.dist b c ≤ 2*(b+c).choose 2 := by
  rcases le_total b c with hbc | hcb
  · exact scalar_dominance_left b c q hbc (by simpa [min_eq_left hbc] using hm) hq.1
  · have ht := scalar_dominance_left c b q hcb (by simpa [min_eq_right hcb] using hm) hq.2
    simpa [Nat.add_comm,Nat.dist_comm] using ht

theorem small_class_dominance_nat (A : Finset ℤ) (z : ℤ × ℤ → Bool)
    (hsmall : ∀ d∈posDiffs A,
      min (fiberClass A z d false).card (fiberClass A z d true).card ≤ 3) :
    10*R A z+D A z≤2*T A := by
  have hsum := Finset.sum_le_sum (s:=posDiffs A) (fun d hd =>
    scalar_dominance (fiberClass A z d false).card (fiberClass A z d true).card
      (shared A z d) (hsmall d hd) (shared_bounds A z d))
  simp_rw [class_partition] at hsum
  simpa only [Finset.sum_add_distrib,← Finset.mul_sum,← corner_count,R,D] using hsum

theorem P_nonneg (A : Finset ℤ) (z : ℤ × ℤ → Bool) : 0≤P A z := by
  unfold P
  positivity

/-- Full small-class comparison, with R,D,P computed from the actual colored fibers.
    Properness is not needed for this comparison, so it applies to the paper's proper colorings. -/
theorem small_class_dominance (A : Finset ℤ) (z : ℤ × ℤ → Bool)
    (hsmall : ∀ d∈posDiffs A,
      min (fiberClass A z d false).card (fiberClass A z d true).card ≤ 3) :
    (T A:ℝ)+5*R A z-P A z ≤ 2*T A-(D A z:ℝ)/2-P A z ∧
    2*(T A:ℝ)-(D A z:ℝ)/2-P A z ≤ 2*T A := by
  have hnat := small_class_dominance_nat A z hsmall
  have hr : 10*(R A z:ℝ)+(D A z:ℝ)≤2*(T A:ℝ) := by exact_mod_cast hnat
  have hp := P_nonneg A z
  have hd : 0≤(D A z:ℝ) := by positivity
  constructor <;> linarith

theorem small_class_of_fiber_seven (A : Finset ℤ) (z : ℤ × ℤ → Bool)
    (hseven : ∀ d∈posDiffs A, r A d≤7) (d : ℤ) (hd : d∈posDiffs A) :
    min (fiberClass A z d false).card (fiberClass A z d true).card ≤ 3 := by
  have h := class_partition A z d
  have hh := hseven d hd
  omega

end EnergyForcing.FiberDominance
