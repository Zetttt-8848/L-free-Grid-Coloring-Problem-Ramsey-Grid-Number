import Std

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

/- All proofs here use Lean kernel reduction with `decide`. No native_decide,
   compiler axiom, imported certificate verdict or trusted Python result is used.
   Coordinates are the manuscript's zero-based strict triangle T_n. -/
namespace EnergyForcing.Finite

abbrev Coloring := Nat → Nat → Nat
def properTriangle (n : Nat) (c : Coloring) : Prop :=
  ∀ v u d : Nat, u < v → 0 < d → v+d < n →
    ¬ (c v u = c (v+d) u ∧ c (v+d) u = c (v+d) (u+d))
def validThree (n : Nat) (c : Coloring) : Prop :=
  ∀ v u : Nat, u < v → v < n → c v u < 3
def boundedProper (n : Nat) (c : Coloring) : Prop :=
  ∀ v u d : Fin n, u.val < v.val → 0 < d.val → v.val+d.val < n →
    ¬ (c v.val u.val = c (v.val+d.val) u.val ∧
       c (v.val+d.val) u.val = c (v.val+d.val) (u.val+d.val))
def boundedValid (n : Nat) (c : Coloring) : Prop :=
  ∀ v u : Fin n, u.val < v.val → c v.val u.val < 3

theorem proper_of_bounded {n : Nat} {c : Coloring} (h : boundedProper n c) :
    properTriangle n c := by
  intro v u d huv hd htop
  have hv : v < n := by omega
  have hu : u < n := by omega
  have hd' : d < n := by omega
  exact h ⟨v,hv⟩ ⟨u,hu⟩ ⟨d,hd'⟩ huv hd htop

theorem valid_of_bounded {n : Nat} {c : Coloring} (h : boundedValid n c) :
    validThree n c := by
  intro v u huv hv
  exact h ⟨v,hv⟩ ⟨u,by omega⟩ huv

def corners (n : Nat) : List (Nat × Nat × Nat) :=
  (List.range n).flatMap fun v =>
    (List.range v).flatMap fun u =>
      ((List.range (n-v)).filter fun d => 0 < d).map fun d => (v,u,d)

theorem mem_corners (n v u d : Nat) :
    (v,u,d) ∈ corners n ↔ u < v ∧ 0 < d ∧ v+d < n := by
  simp only [corners, List.mem_flatMap, List.mem_range, List.mem_map, List.mem_filter,
    decide_eq_true_eq]
  constructor
  · rintro ⟨v',hv',u',hu',d',⟨hd',hdpos⟩,heq⟩
    have ev : v'=v := congrArg Prod.fst heq
    have eu : u'=u := congrArg (fun x => x.2.1) heq
    have ed : d'=d := congrArg (fun x => x.2.2) heq
    omega
  · rintro ⟨huv,hd,htop⟩
    exact ⟨v,by omega,u,huv,d,⟨by omega,hd⟩,rfl⟩

def rainbow (c : Coloring) (p : Nat × Nat × Nat) : Bool :=
  let v := p.1
  let u := p.2.1
  let d := p.2.2
  c v u != c (v+d) u && c v u != c (v+d) (u+d) &&
    c (v+d) u != c (v+d) (u+d)
def rainbowCount (n : Nat) (c : Coloring) : Nat := ((corners n).filter (rainbow c)).length
def localAssertion (n q : Nat) : Prop :=
  ∀ c : Coloring, validThree n c → properTriangle n c → q ≤ rainbowCount n c
def rowColor (rows : List (List Nat)) (v u : Nat) : Nat := (rows[v]?.getD [])[u]?.getD 0

def rows11 : List (List Nat) :=
  [[],[2],[2,0],[2,0,1],[0,0,2,2],[1,0,2,1,1],[2,2,0,0,0,0],
   [0,2,0,2,0,2,0],[1,1,2,2,0,1,1,1],[2,1,2,1,2,0,0,0,1],[1,1,2,0,1,2,0,1,1,2]]
def rows12 : List (List Nat) :=
  [[],[1],[0,1],[1,0,0],[0,0,1,1],[2,0,1,2,1],[1,1,1,0,0,0],
   [0,1,2,1,1,1,0],[2,2,2,1,2,2,2,2],[1,2,1,2,2,0,2,0,2],
   [2,2,1,0,2,1,0,2,0,1],[1,1,0,1,1,2,2,0,0,1,2]]
def rows13 : List (List Nat) :=
  [[],[1],[0,0],[0,2,0],[2,0,2,2],[2,1,0,2,1],[1,2,1,0,0,0],
   [2,0,0,0,2,0,2],[2,1,1,1,0,0,2,1],[1,2,1,2,1,2,2,1,0],
   [1,0,2,1,2,2,1,1,0,2],[0,1,1,2,2,0,2,2,1,1,1],[0,1,0,1,2,0,1,2,0,1,2,1]]
def c11 := rowColor rows11
def c12 := rowColor rows12
def c13 := rowColor rows13

theorem c11_bounded_proper : boundedProper 11 c11 := by unfold boundedProper; decide
theorem c12_bounded_proper : boundedProper 12 c12 := by unfold boundedProper; decide
theorem c13_bounded_proper : boundedProper 13 c13 := by unfold boundedProper; decide
theorem c11_bounded_valid : boundedValid 11 c11 := by unfold boundedValid; decide
theorem c12_bounded_valid : boundedValid 12 c12 := by unfold boundedValid; decide
theorem c13_bounded_valid : boundedValid 13 c13 := by unfold boundedValid; decide
theorem c11_proper : properTriangle 11 c11 := proper_of_bounded c11_bounded_proper
theorem c12_proper : properTriangle 12 c12 := proper_of_bounded c12_bounded_proper
theorem c13_proper : properTriangle 13 c13 := proper_of_bounded c13_bounded_proper
theorem c11_rainbows : rainbowCount 11 c11 = 3 := by decide
theorem c12_rainbows : rainbowCount 12 c12 = 6 := by decide
theorem c13_rainbows : rainbowCount 13 c13 = 14 := by decide
theorem corner_count11 : (corners 11).length = 165 := by decide
theorem corner_count12 : (corners 12).length = 220 := by decide
theorem corner_count13 : (corners 13).length = 286 := by decide
theorem corners11_nodup : (corners 11).Nodup := by decide
theorem corners12_nodup : (corners 12).Nodup := by decide
theorem corners13_nodup : (corners 13).Nodup := by decide

/-- Proposition prop:local-rainbows, the size-eleven refutation. -/
theorem not_F11_5 : ¬ localAssertion 11 5 := by
  intro h
  have hc := h c11 (valid_of_bounded c11_bounded_valid) c11_proper
  rw [c11_rainbows] at hc
  omega
/-- Proposition prop:local-rainbows, the size-twelve refutation. -/
theorem not_F12_7 : ¬ localAssertion 12 7 := by
  intro h
  have hc := h c12 (valid_of_bounded c12_bounded_valid) c12_proper
  rw [c12_rainbows] at hc
  omega
/-- Proposition prop:t13. -/
theorem not_F13_17 : ¬ localAssertion 13 17 := by
  intro h
  have hc := h c13 (valid_of_bounded c13_bounded_valid) c13_proper
  rw [c13_rainbows] at hc
  omega

#print axioms c11_bounded_proper
#print axioms c12_bounded_proper
#print axioms c13_bounded_proper
#print axioms c11_rainbows
#print axioms c12_rainbows
#print axioms c13_rainbows
#print axioms not_F11_5
#print axioms not_F12_7
#print axioms not_F13_17
end EnergyForcing.Finite

