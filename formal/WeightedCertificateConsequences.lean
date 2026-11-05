import WeightedEmbedding
import WeightCertificates

set_option autoImplicit false

namespace EnergyForcing.WeightedCertificates

open scoped BigOperators
open EnergyForcing.WeightedEmbedding
open EnergyForcing.WeightedEmbeddingCounts

theorem sumRange_cast (f : ℕ → ℕ) (n : ℕ) :
    (sumRange f n : ℝ)=∑ i∈Finset.range n, (f i:ℝ) := by
  induction n with
  | zero => simp [sumRange]
  | succ n ih => simp [sumRange,Finset.sum_range_succ,ih]

/-- The real geometric load is exactly the cast of the verified integer load. -/
theorem load_cast (m : ℕ) (w : ℕ → ℕ) (h : ℕ) :
    WeightedEmbedding.load m (fun d => (w d:ℝ)) h=(Weights.load m w h:ℝ) := by
  unfold WeightedEmbedding.load Weights.load
  rw [sumRange_cast,Finset.sum_Ico_eq_sum_range]
  have hi : m-1-1=m-2 := by omega
  rw [hi]
  apply Finset.sum_congr rfl
  intro i _
  have hc : Weights.coefficient m (i+1)=(m-(i+1)).choose 2 := by
    simp [Weights.coefficient,Weights.chooseTwo,Nat.choose_two_right]
  simp only [Nat.add_comm 1 i,Nat.dvd_iff_mod_eq_zero,hc]
  split_ifs <;> push_cast <;> rfl

/-- Weights vanish beyond the printed42 entries, so longer legal-scale ranges add zero. -/
theorem copies_cast (table : List ℕ) (N m : ℕ)
    (hrange : 42≤(N-2)/(m-2)) :
    weightedCopies N m (fun d => (Weights.weight table d:ℝ))=
      (Weights.copies m N (Weights.weight table):ℝ) := by
  unfold weightedCopies Weights.copies
  have hsub : Finset.Ico 1 43⊆scales N m := by
    intro d hd
    simp only [Finset.mem_Ico,scales] at *
    omega
  have htail : (∑ d∈scales N m,
      (Weights.weight table d:ℝ)*((N-d*(m-2)).choose 2:ℝ))=
      ∑ d∈Finset.Ico 1 43,
        (Weights.weight table d:ℝ)*((N-d*(m-2)).choose 2:ℝ) := by
    symm
    apply Finset.sum_subset hsub
    intro d hd hnot
    have hdlo : 1≤d := (Finset.mem_Ico.mp hd).1
    have hdt : 42<d := by
      have : ¬(1≤d ∧ d<43) := by simpa only [Finset.mem_Ico] using hnot
      omega
    rw [Weights.weight_tail table d hdt]
    simp
  rw [htail,sumRange_cast,Finset.sum_Ico_eq_sum_range]
  norm_num only [Nat.reduceSub]
  apply Finset.sum_congr rfl
  intro i _
  simp [Weights.chooseTwo,Nat.choose_two_right,Nat.mul_comm,Nat.add_comm,mul_comm]

theorem table11_real_load (h : ℕ) :
    WeightedEmbedding.load 11 (fun d => (Weights.weight Weights.table11 d:ℝ)) h≤45000 := by
  rw [load_cast]
  exact_mod_cast Weights.load11_bound h

theorem table12_real_load (h : ℕ) :
    WeightedEmbedding.load 12 (fun d => (Weights.weight Weights.table12 d:ℝ)) h≤55000 := by
  rw [load_cast]
  exact_mod_cast Weights.load12_bound h

theorem table11_real_copies :
    weightedCopies 459 11 (fun d => (Weights.weight Weights.table11 d:ℝ))=944436978 := by
  rw [copies_cast _ _ _ (by decide),Weights.copies11]
  norm_num

theorem table12_real_copies :
    weightedCopies 455 12 (fun d => (Weights.weight Weights.table12 d:ℝ))=809226900 := by
  rw [copies_cast _ _ _ (by decide),Weights.copies12]
  norm_num

/-- Conditional only: the local eleven-mark rainbow lower bound is a hypothesis. -/
theorem conditional_weighted_459 (hlocal : LocalRainbow 11 5) : ramseyL 3 459 := by
  apply weighted_embedding_ramsey 459 11 5 (by decide) (by decide) hlocal
    (fun d => (Weights.weight Weights.table11 d:ℝ)) (by intro d; positivity) 45000
    (by norm_num) (by intro h _ _; exact table11_real_load h)
  rw [table11_real_copies]
  norm_num [Nat.choose_two_right]

/-- Conditional only: the local twelve-mark rainbow lower bound is a hypothesis. -/
theorem conditional_weighted_455 (hlocal : LocalRainbow 12 7) : ramseyL 3 455 := by
  apply weighted_embedding_ramsey 455 12 7 (by decide) (by decide) hlocal
    (fun d => (Weights.weight Weights.table12 d:ℝ)) (by intro d; positivity) 55000
    (by norm_num) (by intro h _ _; exact table12_real_load h)
  rw [table12_real_copies]
  norm_num [Nat.choose_two_right]

#print axioms conditional_weighted_459
#print axioms conditional_weighted_455

end EnergyForcing.WeightedCertificates
