import UniversalCounting

set_option maxRecDepth 100000
set_option maxHeartbeats 80000000
namespace EnergyForcing.Weights
def table11 : List Nat := [1000, 200, 377, 373, 666, 351, 866, 541, 743, 400, 1000, 266, 1000, 280, 459, 379, 1000, 98, 1000, 244, 410, 200, 1000, 178, 778, 200, 529, 322, 1000, 118, 1000, 419, 377, 200, 622, 323, 1000, 200, 377, 393, 1000, 258]
def table12 : List Nat := [1000, 181, 345, 342, 618, 326, 818, 518, 719, 407, 1000, 284, 1000, 297, 463, 382, 1000, 94, 1000, 218, 401, 181, 1000, 131, 764, 181, 510, 278, 1000, 55, 1000, 386, 345, 181, 575, 263, 1000, 181, 345, 343, 1000, 195]

def weight (table : List Nat) (n : Nat) : Nat :=
  if n=0 ∨ 42<n then 0 else table[n-1]?.getD 0
def chooseTwo (n : Nat) := n*(n-1)/2
def coefficient (m j : Nat) := chooseTwo (m-j)
def properLoad (m : Nat) (w : Nat → Nat) (n : Nat) : Nat :=
  sumRange (fun i => let j:=i+2; if n%j=0 then coefficient m j*w (n/j) else 0) (m-3)
def load (m : Nat) (w : Nat → Nat) (h : Nat) : Nat :=
  sumRange (fun i => let j:=i+1; if h%j=0 then coefficient m j*w (h/j) else 0) (m-2)
def copies (m N : Nat) (w : Nat → Nat) :=
  sumRange (fun i => w (i+1)*chooseTwo (N-(m-2)*(i+1))) 42
def recurrence (m K : Nat) (w : Nat → Nat) (n : Nat) : Prop :=
  (w n:Int)=((K:Int)-(properLoad m w n:Int))/(coefficient m 1:Int)

theorem weight_zero (table : List Nat) : weight table 0=0 := by simp [weight]
theorem weight_tail (table : List Nat) (n : Nat) (hn : 42<n) : weight table n=0 := by
  simp [weight,hn]

theorem recurrence11_small : ∀ n : Fin 43, 0<n.val → recurrence 11 45000 (weight table11) n.val := by unfold recurrence; decide
theorem recurrence12_small : ∀ n : Fin 43, 0<n.val → recurrence 12 55000 (weight table12) n.val := by unfold recurrence; decide
theorem weight11_small : ∀ n : Fin 43, weight table11 n.val≤1000 := by decide
theorem weight12_small : ∀ n : Fin 43, weight table12 n.val≤1000 := by decide
theorem load11_small : ∀ h : Fin 421, load 11 (weight table11) h.val≤45000 := by decide
theorem load12_small : ∀ h : Fin 421, load 12 (weight table12) h.val≤55000 := by decide

theorem sumRange_zero (f : Nat → Nat) (k : Nat) (h : ∀ i, i<k → f i=0) :
    sumRange f k=0 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    change sumRange f k+f k=0
    rw [ih (fun i hi => h i (by omega)),h k (by omega)]

/-- Above 420 every term vanishes; this closes the universal positive-step range. -/
theorem load_tail (table : List Nat) (m h : Nat) (hm : m≤12) (hh : 420<h) :
    load m (weight table) h=0 := by
  apply sumRange_zero
  intro i hi
  dsimp
  split
  · rename_i hd
    have hq : 42<h/(i+1) := by
      by_cases hgood : 42<h/(i+1)
      · exact hgood
      · have hquot : h/(i+1)≤42 := by omega
        have hj : i+1≤10 := by omega
        have hmul := Nat.mul_le_mul hj hquot
        have he := Nat.div_add_mod h (i+1)
        rw [hd] at he
        omega
    rw [weight_tail table _ hq,Nat.mul_zero]
  · rfl

theorem weight11_bound (n : Nat) : weight table11 n≤1000 := by
  by_cases hn : n<43
  · exact weight11_small ⟨n,hn⟩
  · rw [weight_tail table11 n (by omega)]; omega
theorem weight12_bound (n : Nat) : weight table12 n≤1000 := by
  by_cases hn : n<43
  · exact weight12_small ⟨n,hn⟩
  · rw [weight_tail table12 n (by omega)]; omega
theorem load11_bound (h : Nat) : load 11 (weight table11) h≤45000 := by
  by_cases hh : h<421
  · exact load11_small ⟨h,hh⟩
  · rw [load_tail table11 11 h (by decide) (by omega)]; omega
theorem load12_bound (h : Nat) : load 12 (weight table12) h≤55000 := by
  by_cases hh : h<421
  · exact load12_small ⟨h,hh⟩
  · rw [load_tail table12 12 h (by decide) (by omega)]; omega

theorem copies11 : copies 11 459 (weight table11)=944436978 := by decide
theorem copies12 : copies 12 455 (weight table12)=809226900 := by decide

theorem sumRange_congr (f g : Nat → Nat) (k : Nat)
    (h : ∀ i, i<k → f i=g i) : sumRange f k=sumRange g k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    change sumRange f k+f k=sumRange g k+g k
    rw [ih (fun i hi => h i (by omega)),h k (by omega)]

theorem properLoad_congr (m n : Nat) (v w : Nat → Nat) (hn : 0<n)
    (h : ∀ i, i<n → v i=w i) : properLoad m v n=properLoad m w n := by
  apply sumRange_congr
  intro i _
  dsimp
  split
  · rw [h (n/(i+2)) (Nat.div_lt_self hn (by omega))]
  · rfl

/-- Recurrence uniqueness identifies the literal table with the successively
    defined weights; no alternative sequence is silently substituted. -/
theorem recurrence_unique (m K : Nat) (v w : Nat → Nat)
    (hv0 : v 0=0) (hw0 : w 0=0)
    (hv : ∀ n, 0<n → n≤42 → recurrence m K v n)
    (hw : ∀ n, 0<n → n≤42 → recurrence m K w n)
    (hvt : ∀ n, 42<n → v n=0) (hwt : ∀ n, 42<n → w n=0) :
    ∀ n, v n=w n := by
  have hprefix : ∀ n, n≤42 → v n=w n := by
    intro n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro hn
      by_cases hz : n=0
      · subst n; rw [hv0,hw0]
      · have hnpos : 0<n := by omega
        have hp := properLoad_congr m n v w hnpos
          (fun i hi => ih i hi (by omega))
        have hev := hv n hnpos hn
        have hew := hw n hnpos hn
        unfold recurrence at hev hew
        rw [hp] at hev
        exact Int.ofNat_inj.mp (hev.trans hew.symm)
  intro n
  by_cases hn : n≤42
  · exact hprefix n hn
  · rw [hvt n (by omega),hwt n (by omega)]

/-- Exact finite recurrence, bounded nonnegative weights, all loads, and copy sum. -/
theorem weight_certificate11 :
    (∀ n, 0<n → n≤42 → recurrence 11 45000 (weight table11) n) ∧
    (∀ n, weight table11 n≤1000) ∧
    (∀ n, 42<n → weight table11 n=0) ∧
    (∀ h, load 11 (weight table11) h≤45000) ∧
    copies 11 459 (weight table11)=944436978 := by
  exact ⟨fun n hn hb => recurrence11_small ⟨n,by omega⟩ hn,
    weight11_bound,weight_tail table11,load11_bound,copies11⟩
theorem weight_certificate12 :
    (∀ n, 0<n → n≤42 → recurrence 12 55000 (weight table12) n) ∧
    (∀ n, weight table12 n≤1000) ∧
    (∀ n, 42<n → weight table12 n=0) ∧
    (∀ h, load 12 (weight table12) h≤55000) ∧
    copies 12 455 (weight table12)=809226900 := by
  exact ⟨fun n hn hb => recurrence12_small ⟨n,by omega⟩ hn,
    weight12_bound,weight_tail table12,load12_bound,copies12⟩

#print axioms weight_certificate11
#print axioms weight_certificate12
#print axioms recurrence_unique
end EnergyForcing.Weights
