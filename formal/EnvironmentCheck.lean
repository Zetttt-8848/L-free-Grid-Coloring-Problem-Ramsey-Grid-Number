import Mathlib

example (n : ℕ) : n * (n + 1) = n^2 + n := by ring

#check Finset.card_nbij'
#check Finset.sum_mul_sq_le_sq_mul_sq
