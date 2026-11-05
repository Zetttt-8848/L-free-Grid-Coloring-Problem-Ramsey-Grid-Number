import ShiftCounting

namespace EnergyForcing.WeightedEmbeddingCounts

open EnergyForcing.Counting
open EnergyForcing.ShiftCounting

def cornerStep (p : ℤ×ℤ×ℤ) : ℕ := (p.2.2-p.1).toNat

def stepCorners (m j : ℕ) : Finset (ℤ×ℤ×ℤ) :=
  (sourceCorners (shifts m)).filter fun p => cornerStep p=j

theorem cornerStep_bounds (m : ℕ) (p : ℤ×ℤ×ℤ) (hp : p∈sourceCorners (shifts m)) :
    1 ≤ cornerStep p ∧ cornerStep p ≤ m-2 := by
  rcases p with ⟨x,y,w⟩
  rcases (mem_sourceCorners (shifts m) x y w).mp hp with ⟨hx,hy,hw,hyx,hxw,_⟩
  have hx' := (mem_shifts m x).mp hx
  have hy' := (mem_shifts m y).mp hy
  have hw' := (mem_shifts m w).mp hw
  dsimp [cornerStep]
  omega

theorem stepCorners_card (m j : ℕ) (hj : 1≤j) :
    (stepCorners m j).card=(m-j).choose 2 := by
  rw [← card_shifts (m-j)]
  change _=M (shifts (m-j))
  rw [← sourceCells_card]
  symm
  refine Finset.card_nbij' (fun p : ℤ×ℤ => (p.1,p.2,p.1+(j:ℤ)))
    (fun p : ℤ×ℤ×ℤ => (p.1,p.2.1)) ?_ ?_ ?_ ?_
  · rintro ⟨x,y⟩ hp
    rcases (mem_sourceCells (shifts (m-j)) x y).mp hp with ⟨hx,hy,hyx⟩
    have hx' := (mem_shifts (m-j) x).mp hx
    have hy' := (mem_shifts (m-j) y).mp hy
    have hmj : j ≤ m := by omega
    have he : y+(x+(j:ℤ))-x=y+j := by ring
    simp only [stepCorners,Finset.mem_filter,mem_sourceCorners,mem_shifts,he,cornerStep]
    refine ⟨⟨⟨by omega,by omega⟩,⟨by omega,by omega⟩,⟨by omega,by omega⟩,hyx,by omega,by omega,by omega⟩,?_⟩
    omega
  · rintro ⟨x,y,w⟩ hp
    rcases Finset.mem_filter.mp hp with ⟨hc,hs⟩
    rcases (mem_sourceCorners (shifts m) x y w).mp hc with ⟨hx,hy,hw,hyx,hxw,_⟩
    have hx' := (mem_shifts m x).mp hx
    have hy' := (mem_shifts m y).mp hy
    have hw' := (mem_shifts m w).mp hw
    dsimp [cornerStep] at hs
    apply (mem_sourceCells (shifts (m-j)) x y).mpr
    simp only [mem_shifts]
    omega
  · intros; rfl
  · rintro ⟨x,y,w⟩ hp
    rcases Finset.mem_filter.mp hp with ⟨hc,hs⟩
    have ht := (mem_sourceCorners (shifts m) x y w).mp hc
    dsimp [cornerStep] at hs
    apply Prod.ext
    · rfl
    · apply Prod.ext
      · rfl
      · dsimp; omega

def translationCells (N m d : ℕ) : Finset (ℤ×ℤ) :=
  sourceCells (shifts (N-d*(m-2)))

theorem translationCells_card (N m d : ℕ) :
    (translationCells N m d).card=(N-d*(m-2)).choose 2 := by
  rw [translationCells,sourceCells_card]
  simp [M]

end EnergyForcing.WeightedEmbeddingCounts
