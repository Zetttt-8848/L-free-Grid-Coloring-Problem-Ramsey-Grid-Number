import Std
set_option maxRecDepth 100000
set_option maxHeartbeats 40000000
namespace EnergyForcing.Sources
abbrev Coloring := Nat → Nat → Nat

def checkSource (A : List Nat) (c : Coloring) : Bool :=
  A.all fun v => A.all fun u => A.all fun x =>
    decide (u < v → v < x → u+(x-v) ∈ A →
      ¬ (c v u = c x u ∧ c x u = c x (u+(x-v))))

def properSource (A : List Nat) (c : Coloring) : Prop :=
  ∀ v u d : Nat, 0 < d → v ∈ A → u ∈ A → u < v → v+d ∈ A → u+d ∈ A →
    ¬ (c v u = c (v+d) u ∧ c (v+d) u = c (v+d) (u+d))

/-- Exact transfer from the finite Boolean checker to all source corners. -/
theorem proper_of_check {A : List Nat} {c : Coloring} (h : checkSource A c = true) :
    properSource A c := by
  intro v u d hd hv hu huv hx hy
  have h1 := List.all_eq_true.mp h v hv
  have h2 := List.all_eq_true.mp h1 u hu
  have h3 := List.all_eq_true.mp h2 (v+d) hx
  have h4 := of_decide_eq_true h3
  have hs : v+d-v=d := by omega
  simpa only [hs] using h4 huv (by omega) (by simpa only [hs] using hy)

def sourceCorners (A : List Nat) : List (Nat × Nat × Nat) :=
  A.flatMap fun v => A.flatMap fun u => A.filterMap fun x =>
    if u < v ∧ v < x ∧ u+(x-v) ∈ A then some (v,u,x-v) else none

theorem mem_sourceCorners (A : List Nat) (v u d : Nat) :
    (v,u,d) ∈ sourceCorners A ↔
      v ∈ A ∧ u ∈ A ∧ u < v ∧ 0 < d ∧ v+d ∈ A ∧ u+d ∈ A := by
  simp only [sourceCorners, List.mem_flatMap, List.mem_filterMap]
  constructor
  · rintro ⟨v',hv',u',hu',x,hx,he⟩
    split at he
    · rename_i ht
      have he' := Option.some.inj he
      have ev := congrArg Prod.fst he'
      have eu := congrArg (fun p => p.2.1) he'
      have ed := congrArg (fun p => p.2.2) he'
      dsimp at ev eu ed
      have ex : x=v+d := by omega
      subst v'; subst u'; subst x
      exact ⟨hv',hu',ht.1,by omega,hx,by simpa only [ed] using ht.2.2⟩
    · contradiction
  · rintro ⟨hv,hu,huv,hd,hx,hy⟩
    refine ⟨v,hv,u,hu,v+d,hx,?_⟩
    have hs : v+d-v=d := by omega
    simp only [hs]
    simp [huv, show v<v+d by omega, hy]

def rowColor (A : List Nat) (rows : List (List Nat)) (v u : Nat) : Nat :=
  (rows[A.idxOf v]?.getD [])[A.idxOf u]?.getD 0

def fourMarks : List Nat := [0,1,3,4,9,10,12,13,27,28,30,31,36,37,39,40]
def fourRows : List (List Nat) :=
  [[],[1],[1,0],[1,0,0],[1,0,0,1],[1,0,1,1,0],[1,1,0,1,0,1],[0,0,0,1,1,1,1],
   [1,0,0,1,0,1,1,0],
   [1,0,1,1,1,1,0,0,0],
   [1,1,0,1,1,0,1,0,0,1],
   [0,0,0,1,0,0,0,1,1,1,1],
   [1,1,1,0,0,1,1,0,0,1,1,0],
   [0,0,1,0,0,1,0,0,1,1,0,0,1],
   [0,1,1,0,1,0,0,0,1,0,1,0,1,0],
   [0,1,1,0,1,0,1,0,1,0,0,0,0,0,0]]
def fourColor := rowColor fourMarks fourRows
theorem fourCubeCheck : checkSource fourMarks fourColor = true := by decide
theorem fourCubeProper : properSource fourMarks fourColor := proper_of_check fourCubeCheck
theorem fourCubeCornerCount : (sourceCorners fourMarks).length = 200 := by decide

def threeMarks : List Nat := [0,1,3,4,9,10,12,13]
def threeRows : List (List Nat) :=
  [[],[1],[1,0],[1,0,0],[1,0,0,1],[1,0,1,0,0],[1,1,0,0,0,0],[0,1,1,0,1,0,0]]
def threeColor := rowColor threeMarks threeRows
def mixed (c : Coloring) (p : Nat × Nat × Nat) : Bool :=
  c p.1 p.2.1 != c (p.1+p.2.2) (p.2.1+p.2.2)
theorem threeCubeCheck : checkSource threeMarks threeColor = true := by decide
theorem threeCubeProper : properSource threeMarks threeColor := proper_of_check threeCubeCheck
theorem threeCubeCornerCount : (sourceCorners threeMarks).length = 24 := by decide
theorem threeCubeMixedCount : ((sourceCorners threeMarks).filter (mixed threeColor)).length = 9 := by decide

def checkWeak (A : List Nat) (c : Coloring) : Bool :=
  A.all fun v => A.all fun u => A.all fun x =>
    decide (u ≤ v → v < x → u+(x-v) ∈ A →
      ¬ (c v u = c x u ∧ c x u = c x (u+(x-v))))
def properWeak (A : List Nat) (c : Coloring) : Prop :=
  ∀ v u d : Nat, 0 < d → v ∈ A → u ∈ A → u ≤ v → v+d ∈ A → u+d ∈ A →
    ¬ (c v u = c (v+d) u ∧ c (v+d) u = c (v+d) (u+d))
theorem weak_proper_of_check {A : List Nat} {c : Coloring} (h : checkWeak A c = true) :
    properWeak A c := by
  intro v u d hd hv hu huv hx hy
  have h1 := List.all_eq_true.mp h v hv
  have h2 := List.all_eq_true.mp h1 u hu
  have h3 := List.all_eq_true.mp h2 (v+d) hx
  have h4 := of_decide_eq_true h3
  have hs : v+d-v=d := by omega
  simpa only [hs] using h4 huv (by omega) (by simpa only [hs] using hy)

def weakMarks : List Nat := [0,1,4,5,7,8,12,13,21,22,23,24]
def weakRows : List (List Nat) :=
  [[0],[1,1],[1,1,0],[0,0,1,1],[1,0,1,1,0],[0,0,1,0,0,1],
   [1,1,1,0,1,0,0],[1,0,0,0,1,0,0,1],[1,1,1,1,1,0,1,0,0],
   [1,0,1,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,1,0,0],[0,0,0,0,1,0,1,0,1,0,1,1]]
def weakColor := rowColor weakMarks weakRows
theorem weakCheck : checkWeak weakMarks weakColor = true := by decide
theorem weakProper : properWeak weakMarks weakColor := weak_proper_of_check weakCheck
theorem weakBinary :
    ∀ v u : Fin 25, weakColor v.val u.val < 2 := by decide
theorem weakCornerCount : (sourceCorners weakMarks).length = 74 := by decide
theorem weakDiagonalZero : (weakMarks.filter fun a => weakColor a a == 0).length = 6 := by decide
theorem weakDiagonalOne : (weakMarks.filter fun a => weakColor a a == 1).length = 6 := by decide
theorem weakExceedsProduct : 74 > 2*6*6 := by decide

theorem weakMarksBound (v : Nat) (h : v ∈ weakMarks) : v < 25 := by
  simp only [weakMarks,List.mem_cons,List.not_mem_nil,or_false] at h
  omega
theorem weakSharpness : ∃ A : List Nat, ∃ color : Coloring,
    A.Nodup ∧
    (∀ v u : Nat, v ∈ A → u ∈ A → u ≤ v → color v u < 2) ∧
    properWeak A color ∧
    (A.filter fun a => color a a == 0).length = 6 ∧
    (A.filter fun a => color a a == 1).length = 6 ∧
    (sourceCorners A).Nodup ∧
    (sourceCorners A).length = 74 ∧ 74 > 2*6*6 := by
  refine ⟨weakMarks,weakColor,by decide,?_,weakProper,
    weakDiagonalZero,weakDiagonalOne,by decide,weakCornerCount,weakExceedsProduct⟩
  intro v u hv hu _
  exact weakBinary ⟨v,weakMarksBound v hv⟩ ⟨u,weakMarksBound u hu⟩

def inIntegerMarks (A : List Nat) (z : Int) : Prop := ∃ a : Nat, a ∈ A ∧ z=(a:Int)
def integerColor (color : Coloring) (v u : Int) : Nat := color v.toNat u.toNat
def properWeakInteger (A : List Nat) (color : Coloring) : Prop :=
  ∀ v u d : Int, 0<d → inIntegerMarks A v → inIntegerMarks A u → u≤v →
    inIntegerMarks A (v+d) → inIntegerMarks A (u+d) →
    ¬ (integerColor color v u = integerColor color (v+d) u ∧
       integerColor color (v+d) u = integerColor color (v+d) (u+d))
theorem liftWeakProper {A : List Nat} {color : Coloring} (h : properWeak A color) :
    properWeakInteger A color := by
  intro v u d hd hv hu huv hx hy
  rcases hv with ⟨a,ha,rfl⟩
  rcases hu with ⟨b,hb,rfl⟩
  rcases hx with ⟨x,hx,ex⟩
  rcases hy with ⟨y,hy,ey⟩
  have ex' : x=a+d.toNat := by omega
  have ey' : y=b+d.toNat := by omega
  have hp := h a b d.toNat (by omega) ha hb (by omega)
    (by simpa only [← ex'] using hx) (by simpa only [← ey'] using hy)
  simp only [integerColor,ex,ey,Int.toNat_ofNat]
  simpa only [← ex',← ey'] using hp
theorem weakProperInteger : properWeakInteger weakMarks weakColor := liftWeakProper weakProper

def differences (A : List Nat) : List Nat :=
  A.flatMap fun a => (A.filter fun b => a < b).map fun b => b-a
def deficitB : List Nat := [0,2,5,6]
def deficitC : List Nat := [1,3,4,8]
def positiveMixed (B C : List Nat) (h : Nat) : Nat :=
  (B.flatMap fun b => C.filter fun c => c=b+h).length
def deficitN (B C : List Nat) (bound : Nat) : Nat :=
  ((List.range bound).map fun k =>
    let h := k+1
    ((differences B).count h + (differences C).count h) *
      (positiveMixed B C h + positiveMixed C B h)).sum
theorem deficitBGolomb : (differences deficitB).Nodup := by decide
theorem deficitCGolomb : (differences deficitC).Nodup := by decide
theorem deficitCount : deficitN deficitB deficitC 8 = 29 := by decide
theorem deficitFailsBound : deficitN deficitB deficitC 8 >
    2*deficitB.length*deficitC.length-min deficitB.length deficitC.length := by decide

theorem deficit_tail_zero (h : Nat) (hh : 8<h) :
    ((differences deficitB).count h + (differences deficitC).count h) *
      (positiveMixed deficitB deficitC h + positiveMixed deficitC deficitB h) = 0 := by
  have hb : (differences deficitB).count h = 0 := by
    apply List.count_eq_zero_of_not_mem
    simp [differences,deficitB]
    omega
  have hc : (differences deficitC).count h = 0 := by
    apply List.count_eq_zero_of_not_mem
    simp [differences,deficitC]
    omega
  simp only [hb,hc,Nat.zero_add,Nat.zero_mul]

theorem deficitCertificate :
    (differences deficitB).Nodup ∧ (differences deficitC).Nodup ∧
    deficitN deficitB deficitC 8 = 29 ∧
    (∀ h : Nat, 8<h →
      ((differences deficitB).count h + (differences deficitC).count h) *
        (positiveMixed deficitB deficitC h + positiveMixed deficitC deficitB h) = 0) ∧
    29 > 2*deficitB.length*deficitC.length-min deficitB.length deficitC.length := by
  exact ⟨deficitBGolomb,deficitCGolomb,deficitCount,deficit_tail_zero,by decide⟩

#print axioms proper_of_check
#print axioms mem_sourceCorners
#print axioms fourCubeCheck
#print axioms fourCubeProper
#print axioms fourCubeCornerCount
#print axioms threeCubeProper
#print axioms threeCubeCornerCount
#print axioms threeCubeMixedCount
#print axioms weakProper
#print axioms weakCornerCount
#print axioms weakSharpness
#print axioms weakProperInteger
#print axioms deficitFailsBound
#print axioms deficitCertificate
end EnergyForcing.Sources
