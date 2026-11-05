import Std.Tactic.BVDecide

namespace Round4.SmallCases

/-- All positive-step directed corners on a finite square. -/
def HasCorner (n : Nat) (color : Nat → Nat → Bool) : Prop :=
  ∃ x y d : Fin n, 0 < d.val ∧ x.val + d.val < n ∧ y.val + d.val < n ∧
    color x.val y.val = color (x.val + d.val) y.val ∧
    color (x.val + d.val) y.val = color (x.val + d.val) (y.val + d.val)

/-- Universal Boolean tautology, proved with a checked LRAT certificate. -/
theorem boolean5 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 : Bool) :
    (b0 = b5 ∧ b5 = b6) ∨
    (b1 = b6 ∧ b6 = b7) ∨
    (b2 = b7 ∧ b7 = b8) ∨
    (b3 = b8 ∧ b8 = b9) ∨
    (b5 = b10 ∧ b10 = b11) ∨
    (b6 = b11 ∧ b11 = b12) ∨
    (b7 = b12 ∧ b12 = b13) ∨
    (b8 = b13 ∧ b13 = b14) ∨
    (b10 = b15 ∧ b15 = b16) ∨
    (b11 = b16 ∧ b16 = b17) ∨
    (b12 = b17 ∧ b17 = b18) ∨
    (b13 = b18 ∧ b18 = b19) ∨
    (b15 = b20 ∧ b20 = b21) ∨
    (b16 = b21 ∧ b21 = b22) ∨
    (b17 = b22 ∧ b22 = b23) ∨
    (b18 = b23 ∧ b23 = b24) ∨
    (b0 = b10 ∧ b10 = b12) ∨
    (b1 = b11 ∧ b11 = b13) ∨
    (b2 = b12 ∧ b12 = b14) ∨
    (b5 = b15 ∧ b15 = b17) ∨
    (b6 = b16 ∧ b16 = b18) ∨
    (b7 = b17 ∧ b17 = b19) ∨
    (b10 = b20 ∧ b20 = b22) ∨
    (b11 = b21 ∧ b21 = b23) ∨
    (b12 = b22 ∧ b22 = b24) ∨
    (b0 = b15 ∧ b15 = b18) ∨
    (b1 = b16 ∧ b16 = b19) ∨
    (b5 = b20 ∧ b20 = b23) ∨
    (b6 = b21 ∧ b21 = b24) ∨
    (b0 = b20 ∧ b20 = b24) := by
  bv_decide

/-- Every two-coloring of the full side-5 square has a directed corner. -/
theorem every5 (color : Nat → Nat → Bool) : HasCorner 5 color := by
  have hall := boolean5 (color 0 0) (color 0 1) (color 0 2) (color 0 3) (color 0 4) (color 1 0) (color 1 1) (color 1 2) (color 1 3) (color 1 4) (color 2 0) (color 2 1) (color 2 2) (color 2 3) (color 2 4) (color 3 0) (color 3 1) (color 3 2) (color 3 3) (color 3 4) (color 4 0) (color 4 1) (color 4 2) (color 4 3) (color 4 4)
  rcases hall with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · exact ⟨⟨0, by decide⟩, ⟨0, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨1, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨2, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨3, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨0, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨1, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨2, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨3, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨0, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨1, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨2, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨3, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨3, by decide⟩, ⟨0, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨3, by decide⟩, ⟨1, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨3, by decide⟩, ⟨2, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨3, by decide⟩, ⟨3, by decide⟩, ⟨1, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨0, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨1, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨2, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨0, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨1, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨2, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨0, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨1, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨2, by decide⟩, ⟨2, by decide⟩, ⟨2, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨0, by decide⟩, ⟨3, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨1, by decide⟩, ⟨3, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨0, by decide⟩, ⟨3, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨1, by decide⟩, ⟨1, by decide⟩, ⟨3, by decide⟩, by decide, by decide, by decide, h⟩
  · exact ⟨⟨0, by decide⟩, ⟨0, by decide⟩, ⟨4, by decide⟩, by decide, by decide, by decide, h⟩

/-- Literal two-coloring on a square of side 4. -/
def witness4 (x y : Nat) : Bool :=
  match x, y with
  | 0, _ => false
  | 1, 1 => true
  | 1, 3 => true
  | 2, 0 => true
  | 2, 3 => true
  | 3, 2 => true
  | 3, 3 => true
  | _, _ => false

theorem witness4_corner_free : ¬ HasCorner 4 witness4 := by
  rintro ⟨⟨x, hx⟩, ⟨y, hy⟩, ⟨d, hdBound⟩, hd, hxBound, hyBound, hfirst, hsecond⟩
  dsimp at *
  have dx : x = 0 ∨ x = 1 ∨ x = 2 ∨ x = 3 := by omega
  have dy : y = 0 ∨ y = 1 ∨ y = 2 ∨ y = 3 := by omega
  have dd : d = 1 ∨ d = 2 ∨ d = 3 := by omega
  rcases dx with rfl | rfl | rfl | rfl <;>
    rcases dy with rfl | rfl | rfl | rfl <;>
    rcases dd with rfl | rfl | rfl <;>
    simp_all [witness4]

#print axioms boolean5
#print axioms every5
#print axioms witness4_corner_free

end Round4.SmallCases
