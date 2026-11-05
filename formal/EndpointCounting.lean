import SourceCounting
import Geometry

namespace EnergyForcing.Counting

/-- The finite tuple convention agrees with the geometric three-cell definition. -/
theorem endpoint_corner_fidelity (A : Finset ℤ) (x y w : ℤ) :
    (x,y,w) ∈ sourceCorners A ↔
      sourceCorner (fun a => a ∈ A) (x,y,w-x) := by
  simp only [mem_sourceCorners, sourceCorner, strictSource]
  have ex : x+(w-x) = w := by omega
  have ey : y+(w-x) = y+w-x := by omega
  rw [ex,ey]
  constructor
  · rintro ⟨hx,hy,hw,hyx,hxw,hz⟩
    exact ⟨by omega,⟨hx,hy,hyx⟩,⟨hw,hy,by omega⟩,⟨hw,hz,by omega⟩⟩
  · rintro ⟨hd,⟨hx,hy,hyx⟩,⟨hw,_,_⟩,⟨_,hz,_⟩⟩
    exact ⟨hx,hy,hw,hyx,by omega,hz⟩

/-- Arcs of the directed endpoint graph, on the actual set A without zero. -/
def endpointArcs (A : Finset ℤ) : Finset (ℤ × ℤ) :=
  ((A.erase 0).product (A.erase 0)).filter fun p =>
    p.1 < p.2 ∧ p.2-p.1 ∈ A.erase 0

/-- Ordered positive additions in the nonzero source. -/
def endpointAdditions (A : Finset ℤ) : Finset (ℤ × ℤ) :=
  ((A.erase 0).product (A.erase 0)).filter fun p =>
    0 < p.1 ∧ 0 < p.2 ∧ p.1+p.2 ∈ A.erase 0

def endpointDistinctAdditions (A : Finset ℤ) : Finset (ℤ × ℤ) :=
  (endpointAdditions A).filter fun p => p.1 < p.2

def endpointDoublings (A : Finset ℤ) : Finset ℤ :=
  (A.erase 0).filter fun x => 0 < x ∧ 2*x ∈ A.erase 0

def e0 (A : Finset ℤ) : ℕ := (endpointArcs A).card
def D0 (A : Finset ℤ) : ℕ := (endpointDistinctAdditions A).card
def P0 (A : Finset ℤ) : ℕ := (endpointDoublings A).card

@[simp] theorem mem_endpointAdditions (A : Finset ℤ) (x y : ℤ) :
    (x,y) ∈ endpointAdditions A ↔
      x ∈ A ∧ y ∈ A ∧ 0 < x ∧ 0 < y ∧ x+y ∈ A := by
  unfold endpointAdditions
  rw [Finset.mem_filter, Finset.product_eq_sprod, Finset.mem_product]
  simp only [Finset.mem_erase]
  constructor
  · rintro ⟨⟨⟨_,hx⟩,⟨_,hy⟩⟩,hxp,hyp,_,hs⟩
    exact ⟨hx,hy,hxp,hyp,hs⟩
  · rintro ⟨hx,hy,hxp,hyp,hs⟩
    exact ⟨⟨⟨by omega,hx⟩,⟨by omega,hy⟩⟩,hxp,hyp,by omega,hs⟩

theorem mem_endpointArcs (A : Finset ℤ)
    (hA : ∀ a ∈ A, 0 ≤ a) (x w : ℤ) :
    (x,w) ∈ endpointArcs A ↔
      x ∈ A ∧ w ∈ A ∧ 0 < x ∧ x < w ∧ w-x ∈ A := by
  unfold endpointArcs
  rw [Finset.mem_filter, Finset.product_eq_sprod, Finset.mem_product]
  simp only [Finset.mem_erase]
  constructor
  · rintro ⟨⟨⟨hx0,hx⟩,⟨_,hw⟩⟩,hxw,_,hd⟩
    exact ⟨hx,hw,by have := hA x hx; omega,hxw,hd⟩
  · rintro ⟨hx,hw,hxp,hxw,hd⟩
    exact ⟨⟨⟨by omega,hx⟩,⟨by omega,hw⟩⟩,hxw,by omega,hd⟩

@[simp] theorem mem_endpointDoublings (A : Finset ℤ) (x : ℤ) :
    x ∈ endpointDoublings A ↔ x ∈ A ∧ 0 < x ∧ 2*x ∈ A := by
  simp only [endpointDoublings, Finset.mem_filter, Finset.mem_erase]
  constructor
  · rintro ⟨⟨_,hx⟩,hp,_,h2⟩; exact ⟨hx,hp,h2⟩
  · rintro ⟨hx,hp,h2⟩; exact ⟨⟨by omega,hx⟩,hp,by omega,h2⟩

theorem corners_erase_zero (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a) :
    sourceCorners (A.erase 0) =
      (sourceCorners A).filter (fun p => p.2.1 ≠ 0) := by
  ext ⟨x,y,w⟩
  simp only [mem_sourceCorners, Finset.mem_filter, Finset.mem_erase]
  constructor
  · rintro ⟨⟨_,hx⟩,⟨hy0,hy⟩,⟨_,hw⟩,hyx,hxw,_,hz⟩
    exact ⟨⟨hx,hy,hw,hyx,hxw,hz⟩,hy0⟩
  · rintro ⟨⟨hx,hy,hw,hyx,hxw,hz⟩,hy0⟩
    have hypos := hA y hy
    exact ⟨⟨by omega,hx⟩,⟨hy0,hy⟩,⟨by omega,hw⟩,
      hyx,hxw,by omega,hz⟩

theorem lost_corners_card (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a)
    (hzero : 0 ∈ A) :
    ((sourceCorners A).filter (fun p => p.2.1 = 0)).card = e0 A := by
  unfold e0
  refine Finset.card_bij' (fun p _ => (p.1,p.2.2)) (fun p _ => (p.1,0,p.2)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y,w⟩ hp
    rcases Finset.mem_filter.mp hp with ⟨hp,hy⟩
    dsimp at hy
    subst y
    rcases (mem_sourceCorners A x 0 w).mp hp with ⟨hx,_,hw,hxp,hxw,hd⟩
    exact (mem_endpointArcs A hA x w).mpr ⟨hx,hw,hxp,hxw,by simpa using hd⟩
  · rintro ⟨x,w⟩ hp
    rcases (mem_endpointArcs A hA x w).mp hp with ⟨hx,hw,hxp,hxw,hd⟩
    apply Finset.mem_filter.mpr
    exact ⟨(mem_sourceCorners A x 0 w).mpr
      ⟨hx,hzero,hw,hxp,hxw,by simpa using hd⟩,rfl⟩
  · rintro ⟨x,y,w⟩ hp
    have hy := (Finset.mem_filter.mp hp).2
    dsimp at hy
    simp [hy]
  · rintro ⟨x,w⟩ _; rfl

/-- The deletion partition is an equality before natural-number subtraction. -/
theorem endpoint_deletion_add (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a)
    (hzero : 0 ∈ A) : T A = T (A.erase 0) + e0 A := by
  have h := Finset.filter_card_add_filter_neg_card_eq_card
    (s := sourceCorners A) (fun p => p.2.1 = 0)
  rw [← corners_erase_zero A hA, lost_corners_card A hA hzero] at h
  unfold T
  omega

theorem endpoint_additions_card (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a) :
    (endpointAdditions A).card = e0 A := by
  unfold e0
  refine Finset.card_bij' (fun p _ => (p.1,p.1+p.2))
    (fun p _ => (p.1,p.2-p.1)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y⟩ hp
    rcases (mem_endpointAdditions A x y).mp hp with ⟨hx,hy,hxp,hyp,hs⟩
    exact (mem_endpointArcs A hA x (x+y)).mpr
      ⟨hx,hs,hxp,by omega,by simpa using hy⟩
  · rintro ⟨x,w⟩ hp
    rcases (mem_endpointArcs A hA x w).mp hp with ⟨hx,hw,hxp,hxw,hd⟩
    exact (mem_endpointAdditions A x (w-x)).mpr
      ⟨hx,hd,hxp,by omega,by simpa using hw⟩
  · rintro ⟨x,y⟩ _; simp
  · rintro ⟨x,w⟩ _; simp

theorem endpoint_swapped_additions_card (A : Finset ℤ) :
    ((endpointAdditions A).filter (fun p => p.2 < p.1)).card = D0 A := by
  unfold D0 endpointDistinctAdditions
  refine Finset.card_bij' (fun p _ => (p.2,p.1)) (fun p _ => (p.2,p.1)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y⟩ hp
    simpa only [Finset.mem_filter, mem_endpointAdditions, Prod.fst, Prod.snd,
      add_comm, and_assoc, and_left_comm, and_comm] using hp
  · rintro ⟨x,y⟩ hp
    simpa only [Finset.mem_filter, mem_endpointAdditions, Prod.fst, Prod.snd,
      add_comm, and_assoc, and_left_comm, and_comm] using hp
  · rintro ⟨x,y⟩ _; rfl
  · rintro ⟨x,y⟩ _; rfl

theorem endpoint_diagonal_additions_card (A : Finset ℤ) :
    ((endpointAdditions A).filter (fun p => p.1 = p.2)).card = P0 A := by
  unfold P0
  refine Finset.card_bij' (fun p _ => p.1) (fun x _ => (x,x)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y⟩ hp
    rcases Finset.mem_filter.mp hp with ⟨hp,hxy⟩
    dsimp at hxy
    subst y
    rcases (mem_endpointAdditions A x x).mp hp with ⟨hx,_,hxp,_,hs⟩
    exact (mem_endpointDoublings A x).mpr ⟨hx,hxp,by simpa [two_mul] using hs⟩
  · intro x hx
    rcases (mem_endpointDoublings A x).mp hx with ⟨hx,hxp,hs⟩
    exact Finset.mem_filter.mpr ⟨(mem_endpointAdditions A x x).mpr
      ⟨hx,hx,hxp,hxp,by simpa [two_mul] using hs⟩,rfl⟩
  · rintro ⟨x,y⟩ hp
    have hxy := (Finset.mem_filter.mp hp).2
    dsimp at hxy
    simp [hxy]
  · intro x _; rfl

theorem endpoint_addition_partition (A : Finset ℤ) :
    (endpointAdditions A).card = 2 * D0 A + P0 A := by
  let S := endpointAdditions A
  have h₁ := Finset.filter_card_add_filter_neg_card_eq_card
    (s := S) (fun p => p.1 < p.2)
  have h₂ := Finset.filter_card_add_filter_neg_card_eq_card
    (s := S.filter (fun p => ¬ p.1 < p.2)) (fun p => p.1 = p.2)
  have hd : (S.filter (fun p => ¬ p.1 < p.2)).filter (fun p => p.1 = p.2) =
      S.filter (fun p => p.1 = p.2) := by
    ext p
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨⟨hp,_⟩,he⟩; exact ⟨hp,he⟩
    · rintro ⟨hp,he⟩; exact ⟨⟨hp,by omega⟩,he⟩
  have hh : (S.filter (fun p => ¬ p.1 < p.2)).filter (fun p => ¬ p.1 = p.2) =
      S.filter (fun p => p.2 < p.1) := by
    ext p
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨⟨hp,hle⟩,hne⟩; exact ⟨hp,by omega⟩
    · rintro ⟨hp,hlt⟩; exact ⟨⟨hp,by omega⟩,by omega⟩
  rw [hd,hh] at h₂
  have hl : (S.filter (fun p => p.1 < p.2)).card = D0 A := rfl
  have he := endpoint_diagonal_additions_card A
  have hg := endpoint_swapped_additions_card A
  change (S.filter (fun p => p.1 = p.2)).card = P0 A at he
  change (S.filter (fun p => p.2 < p.1)).card = D0 A at hg
  change S.card = 2 * D0 A + P0 A
  omega

/-- Exact endpoint deletion, including the empty surviving set. No coloring hypothesis. -/
theorem exact_endpoint_deletion (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a)
    (hzero : 0 ∈ A) :
    T A - T (A.erase 0) = e0 A ∧ e0 A = 2 * D0 A + P0 A := by
  have hdel := endpoint_deletion_add A hA hzero
  have hadd := endpoint_additions_card A hA
  have hpart := endpoint_addition_partition A
  omega

def reflectedSource (A : Finset ℤ) (a : ℤ) : Finset ℤ :=
  A.image (fun x => a-x)

@[simp] theorem mem_reflectedSource (A : Finset ℤ) (a x : ℤ) :
    x ∈ reflectedSource A a ↔ a-x ∈ A := by
  simp only [reflectedSource, Finset.mem_image]
  constructor
  · rintro ⟨y,hy,hxy⟩
    have : a-x = y := by omega
    simpa only [this] using hy
  · intro hx
    exact ⟨a-x,hx,by omega⟩

def reflectCorner (a : ℤ) (p : ℤ × ℤ × ℤ) : ℤ × ℤ × ℤ :=
  (a-p.2.1-p.2.2+p.1,a-p.2.2,a-p.2.1)

theorem reflectCorner_involution (a : ℤ) (p : ℤ × ℤ × ℤ) :
    reflectCorner a (reflectCorner a p) = p := by
  rcases p with ⟨x,y,w⟩
  apply Prod.ext
  · dsimp [reflectCorner]; omega
  · apply Prod.ext <;> dsimp [reflectCorner] <;> omega

theorem reflectCorner_mem (A : Finset ℤ) (a : ℤ) (p : ℤ × ℤ × ℤ) :
    reflectCorner a p ∈ sourceCorners (reflectedSource A a) ↔
      p ∈ sourceCorners A := by
  rcases p with ⟨x,y,w⟩
  simp only [reflectCorner, mem_sourceCorners, mem_reflectedSource]
  have e₁ : a-(a-y-w+x) = y+w-x := by omega
  have e₂ : a-(a-w) = w := by omega
  have e₃ : a-(a-y) = y := by omega
  have e₄ : a-(a-w+(a-y)-(a-y-w+x)) = x := by omega
  rw [e₁,e₂,e₃,e₄]
  constructor
  · rintro ⟨hz,hw,hy,h₁,h₂,hx⟩
    exact ⟨hx,hy,hw,by omega,by omega,hz⟩
  · rintro ⟨hx,hy,hw,h₁,h₂,hz⟩
    exact ⟨hz,hw,hy,by omega,by omega,hx⟩

theorem reflected_T (A : Finset ℤ) (a : ℤ) :
    T (reflectedSource A a) = T A := by
  unfold T
  symm
  refine Finset.card_bij' (fun p _ => reflectCorner a p)
    (fun p _ => reflectCorner a p) ?_ ?_ ?_ ?_
  · intro p hp; exact (reflectCorner_mem A a p).mpr hp
  · intro p hp
    apply (reflectCorner_mem A a (reflectCorner a p)).mp
    simpa only [reflectCorner_involution] using hp
  · intro p _; exact reflectCorner_involution a p
  · intro p _; exact reflectCorner_involution a p

theorem reflected_erase (A : Finset ℤ) (a : ℤ) :
    reflectedSource (A.erase a) a = (reflectedSource A a).erase 0 := by
  ext x
  simp only [mem_reflectedSource, Finset.mem_erase]
  constructor
  · rintro ⟨hne,hmem⟩; exact ⟨by omega,hmem⟩
  · rintro ⟨hne,hmem⟩; exact ⟨by omega,hmem⟩

theorem exact_maximum_deletion (A : Finset ℤ) (a : ℤ)
    (ha : a ∈ A) (hmax : ∀ x ∈ A, x ≤ a) :
    T A - T (A.erase a) = e0 (reflectedSource A a) ∧
      e0 (reflectedSource A a) =
        2 * D0 (reflectedSource A a) + P0 (reflectedSource A a) := by
  have hnonneg : ∀ x ∈ reflectedSource A a, 0 ≤ x := by
    intro x hx
    have := hmax (a-x) ((mem_reflectedSource A a x).mp hx)
    omega
  have hz : 0 ∈ reflectedSource A a := by simpa using ha
  have h := exact_endpoint_deletion (reflectedSource A a) hnonneg hz
  rw [reflected_T, ← reflected_erase, reflected_T] at h
  exact h

def reflectCell (a : ℤ) (p : Point) : Point := (a-p.2,a-p.1)

theorem reflectCell_involution (a : ℤ) (p : Point) :
    reflectCell a (reflectCell a p) = p := by
  rcases p with ⟨x,y⟩
  apply Prod.ext <;> dsimp [reflectCell] <;> omega

theorem reflected_strictSource (A : Finset ℤ) (a : ℤ) (p : Point) :
    strictSource (fun x => x ∈ reflectedSource A a) p ↔
      strictSource (fun x => x ∈ A) (reflectCell a p) := by
  rcases p with ⟨x,y⟩
  simp only [strictSource, reflectCell, mem_reflectedSource]
  constructor
  · rintro ⟨hx,hy,hxy⟩; exact ⟨hy,hx,by omega⟩
  · rintro ⟨hy,hx,hxy⟩; exact ⟨hx,hy,by omega⟩

/-- Reflection reverses the parallel endpoints and preserves properness for any color type. -/
theorem reflected_properOn {α : Type} (A : Finset ℤ) (a : ℤ) (z : Point → α)
    (hz : properOn (strictSource (fun x => x ∈ A)) z) :
    properOn (strictSource (fun x => x ∈ reflectedSource A a))
      (fun p => z (reflectCell a p)) := by
  intro x y d hd h₁ h₂ h₃ hm
  have hp₁ := (reflected_strictSource A a (x,y)).mp h₁
  have hp₂ := (reflected_strictSource A a (x+d,y)).mp h₂
  have hp₃ := (reflected_strictSource A a (x+d,y+d)).mp h₃
  have ex : a-y-d+d = a-y := by omega
  have ey : a-x-d+d = a-x := by omega
  have esx : a-(x+d) = a-x-d := by omega
  have esy : a-(y+d) = a-y-d := by omega
  dsimp [reflectCell] at hp₁ hp₂ hp₃ hm
  rw [esx,esy] at hp₃
  rw [esx] at hp₂
  apply hz (a-y-d) (a-x-d) d hd hp₃
  · simpa only [ex] using hp₂
  · simpa only [ex,ey] using hp₁
  · simpa only [ex,ey,esx,esy] using And.intro hm.2.symm hm.1.symm

#print axioms exact_endpoint_deletion
#print axioms exact_maximum_deletion
#print axioms reflected_T
#print axioms reflected_properOn

end EnergyForcing.Counting
