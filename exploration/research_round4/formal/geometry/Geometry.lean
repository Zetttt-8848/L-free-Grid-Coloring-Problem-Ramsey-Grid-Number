import Std

namespace Round4.Geometry

abbrev Point := Int × Int
abbrev Region := Point → Prop

/-- The manuscript's oriented corner predicate. -/
def IsCorner (p₀ p₁ p₂ : Point) : Prop :=
  ∃ x y h : Int, 0 < h ∧
    p₀ = (x, y) ∧ p₁ = (x + h, y) ∧ p₂ = (x + h, y + h)

/-- No three points forming an oriented positive-step corner have one color. -/
def CornerFree {α : Type} (color : Point → α) : Prop :=
  ∀ x y h : Int, 0 < h →
    ¬(color (x, y) = color (x + h, y) ∧
      color (x + h, y) = color (x + h, y + h))

/-- Completion closure on every integer diagonal offset. -/
def CompletionClosed (R : Region) : Prop :=
  ∀ u v τ : Int, u < v → R (u + τ, u) → R (v + τ, v) → R (v + τ, u)

/-- No oriented positive-step corner contained in `R` has one color. -/
def CornerFreeOn {α : Type} (R : Region) (color : Point → α) : Prop :=
  ∀ x y h : Int, 0 < h →
    R (x, y) → R (x + h, y) → R (x + h, y + h) →
    ¬(color (x, y) = color (x + h, y) ∧
      color (x + h, y) = color (x + h, y + h))

/-- Region-scoped color exclusion.  Membership of the completion is derived
from completion closure rather than assumed globally. -/
theorem completion_avoids_source_color_on {α : Type} (R : Region)
    (color : Point → α) (hclosed : CompletionClosed R)
    (hfree : CornerFreeOn R color) (u v σ : Int) (huv : u < v)
    (hu : R (u + σ, u)) (hv : R (v + σ, v))
    (hsame : color (u + σ, u) = color (v + σ, v)) :
    color (v + σ, u) ≠ color (u + σ, u) := by
  have hcompletion_mem : R (v + σ, u) := hclosed u v σ huv hu hv
  intro hcompletion
  have hstep : 0 < v - u := by omega
  have hrow : u + σ + (v - u) = v + σ := by omega
  have hcol : u + (v - u) = v := by omega
  have hmiddle : R (u + σ + (v - u), u) := by
    simpa [hrow] using hcompletion_mem
  have hlast : R (u + σ + (v - u), u + (v - u)) := by
    simpa [hrow, hcol] using hv
  have hforbidden :=
    hfree (u + σ) u (v - u) hstep hu hmiddle hlast
  apply hforbidden
  constructor
  · simpa [hrow] using hcompletion.symm
  · simpa [hrow, hcol] using hcompletion.trans hsame

/-- Global corollary retained for the full integer plane. -/
theorem completion_avoids_source_color {α : Type} (color : Point → α)
    (hfree : CornerFree color) (u v σ : Int) (huv : u < v)
    (hsame : color (u + σ, u) = color (v + σ, v)) :
    color (v + σ, u) ≠ color (u + σ, u) := by
  let plane : Region := fun _ => True
  have hclosed : CompletionClosed plane := by
    intro _ _ _ _ _ _
    trivial
  have hfreeOn : CornerFreeOn plane color := by
    intro x y h hh _ _ _
    exact hfree x y h hh
  exact completion_avoids_source_color_on plane color hclosed hfreeOn
    u v σ huv trivial trivial hsame

/-- Strict completion triangle of a set of diagonal coordinates. -/
def StrictTriangle (S : Int → Prop) (σ : Int) : Region :=
  fun p => ∃ u v : Int, S u ∧ S v ∧ u < v ∧ p = (v + σ, u)

/-- The strict completion triangle is completion closed.  This proof permits
the two endpoint blocks to overlap and assumes no uniqueness of differences. -/
theorem strictTriangle_completionClosed (S : Int → Prop) (σ : Int) :
    CompletionClosed (StrictTriangle S σ) := by
  intro u v τ huv hu hv
  rcases hu with ⟨a, b, hSa, hSb, hab, hp⟩
  rcases hv with ⟨c, d, hSc, hSd, hcd, hq⟩
  have hua : u = a := congrArg Prod.snd hp
  have hvc : v = c := congrArg Prod.snd hq
  have hrow : v + τ = d + σ := congrArg Prod.fst hq
  refine ⟨a, d, hSa, hSd, ?_, ?_⟩
  · omega
  · apply Prod.ext
    · exact hrow
    · exact hua

/-- Starts of the two completion maps agree at both distances. -/
def CommonStarts (B_d B_e : Int → Prop) (u : Int) : Prop :=
  B_d u ∧ B_e u

/-- The second start `q` is in `B_e`, while `q + (e-d)` is in `B_d`. -/
def ShiftedStarts (B_d B_e : Int → Prop) (d e q : Int) : Prop :=
  B_e q ∧ B_d (q + (e - d))

/-- Image of ordered pairs from one completion-color fiber. -/
def PairImage (d : Int) (B : Int → Prop) (z : Point) : Prop :=
  ∃ u v : Int, B u ∧ B v ∧ u < v ∧ z = (v + d, u)

/-- Coordinate equality gives the exact ordered-overlap bijection. -/
theorem ordered_overlap_bijection (B_d B_e : Int → Prop) (d e : Int)
    (hde : d < e) (z : Point) :
    (PairImage d B_d z ∧ PairImage e B_e z) ↔
      ∃ u q : Int,
        CommonStarts B_d B_e u ∧ ShiftedStarts B_d B_e d e q ∧
        u < q ∧ z = (q + e, u) := by
  constructor
  · rintro ⟨⟨u, v, hdu, hdv, huv, hz1⟩,
      ⟨p, q, hep, heq, hpq, hz2⟩⟩
    have hpoints : (v + d, u) = (q + e, p) := hz1.symm.trans hz2
    have hrow : v + d = q + e := congrArg Prod.fst hpoints
    have hcol : u = p := congrArg Prod.snd hpoints
    refine ⟨u, q, ⟨hdu, ?_⟩, ⟨heq, ?_⟩, ?_, ?_⟩
    · simpa [hcol] using hep
    · have hvq : v = q + (e - d) := by omega
      simpa [hvq] using hdv
    · omega
    · simpa [← hcol] using hz2
  · rintro ⟨u, q, ⟨hdu, heu⟩, ⟨heq, hdq⟩, huq, hz⟩
    have hpositive : 0 < e - d := by omega
    constructor
    · refine ⟨u, q + (e - d), hdu, hdq, ?_, ?_⟩
      · omega
      · have hsum : q + (e - d) + d = q + e := by omega
        simpa [hsum] using hz
    · exact ⟨u, q, heu, heq, huq, hz⟩

abbrev W5Triple := Nat × Nat × Nat

/-- Row-major enumeration of `(row,col)` with `0 ≤ col ≤ row ≤ 4`. -/
def w5Coord (i : Nat) : Nat × Nat :=
  match i with
  | 0 => (0, 0)
  | 1 => (1, 0)
  | 2 => (1, 1)
  | 3 => (2, 0)
  | 4 => (2, 1)
  | 5 => (2, 2)
  | 6 => (3, 0)
  | 7 => (3, 1)
  | 8 => (3, 2)
  | 9 => (3, 3)
  | 10 => (4, 0)
  | 11 => (4, 1)
  | 12 => (4, 2)
  | 13 => (4, 3)
  | _ => (4, 4)

/-- The 20 positive-step corners of the weak triangular board. -/
def w5CornerIndices : List W5Triple := [
  (0, 1, 2), (0, 3, 5), (0, 6, 9), (0, 10, 14),
  (1, 3, 4), (1, 6, 8), (1, 10, 13),
  (2, 4, 5), (2, 7, 9), (2, 11, 14),
  (3, 6, 7), (3, 10, 12),
  (4, 7, 8), (4, 11, 13),
  (5, 8, 9), (5, 12, 14),
  (6, 10, 11), (7, 11, 12), (8, 12, 13), (9, 13, 14)
]

def isGeometricW5Corner (t : W5Triple) : Bool :=
  let a := w5Coord t.1
  let b := w5Coord t.2.1
  let c := w5Coord t.2.2
  a.2 == b.2 && a.1 < b.1 && b.1 == c.1 &&
    c.2 == a.2 + (b.1 - a.1)

def derivedW5Corners : List W5Triple :=
  (List.range 15).flatMap fun i =>
    (List.range 15).flatMap fun j =>
      (List.range 15).filterMap fun k =>
        if isGeometricW5Corner (i, j, k) then some (i, j, k) else none

/-- The geometric definition derives exactly the displayed 20 corners. -/
theorem w5_corner_list_exact :
    derivedW5Corners = w5CornerIndices := by
  native_decide

def maskColor (mask index : Nat) : Bool := Nat.testBit mask index

def monochromaticUnderMask (mask : Nat) (t : W5Triple) : Bool :=
  maskColor mask t.1 == maskColor mask t.2.1 &&
  maskColor mask t.2.1 == maskColor mask t.2.2

def w5MaskHasCorner (mask : Nat) : Bool :=
  w5CornerIndices.any (monochromaticUnderMask mask)

/-- Exact finite obstruction: all `2^15` Boolean masks have a listed corner. -/
theorem w5_two_color_obstruction :
    (List.range 32768).all w5MaskHasCorner = true := by
  native_decide

#print axioms completion_avoids_source_color_on
#print axioms completion_avoids_source_color
#print axioms strictTriangle_completionClosed
#print axioms ordered_overlap_bijection
#print axioms w5_corner_list_exact
#print axioms w5_two_color_obstruction

end Round4.Geometry
