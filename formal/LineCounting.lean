import Mathlib
import SourceCounting
import ShiftCounting
import Geometry
set_option autoImplicit false

namespace EnergyForcing.LineCounting

open Finset
open scoped BigOperators

/-- A coloring of integer-coordinate cells, restricted below to the strict triangle. -/
abbrev Coloring := ℕ → ℕ → Fin 3

def colorCount (c : ℕ → Fin 3) (n : ℕ) (i : Fin 3) : ℕ :=
  ∑ j ∈ range n, if c j=i then 1 else 0

def linePairs (c : ℕ → Fin 3) (n : ℕ) : ℕ :=
  ∑ b ∈ range n, ∑ a ∈ range b, if c a=c b then 1 else 0

def lineVariance (c : ℕ → Fin 3) (n : ℕ) : ℚ :=
  ∑ i : Fin 3, ((colorCount c n i : ℚ)-(n:ℚ)/3)^2

theorem colorCount_card (c : ℕ → Fin 3) (n : ℕ) (i : Fin 3) :
    colorCount c n i = ((range n).filter fun j => c j=i).card := by
  simp only [colorCount, card_eq_sum_ones, sum_filter]

theorem colorCount_succ (c : ℕ → Fin 3) (n : ℕ) (i : Fin 3) :
    colorCount c (n+1) i = colorCount c n i + if c n=i then 1 else 0 := by
  simp only [colorCount, sum_range_succ]

theorem colorCount_total (c : ℕ → Fin 3) (n : ℕ) :
    ∑ i : Fin 3, colorCount c n i = n := by
  simp only [colorCount]
  rw [Finset.sum_comm]
  simp

theorem linePairs_succ (c : ℕ → Fin 3) (n : ℕ) :
    linePairs c (n+1) = linePairs c n + colorCount c n (c n) := by
  simp only [linePairs, colorCount, sum_range_succ]

theorem colorSquares_succ (c : ℕ → Fin 3) (n : ℕ) :
    (∑ i : Fin 3, (colorCount c (n+1) i)^2) =
      (∑ i : Fin 3, (colorCount c n i)^2)+2*colorCount c n (c n)+1 := by
  simp only [colorCount_succ, Fin.sum_univ_three]
  have hc : c n=0 ∨ c n=1 ∨ c n=2 := by omega
  rcases hc with hc | hc | hc <;> simp [hc, Fin.ext_iff] <;> ring

theorem linePairs_square_count (c : ℕ → Fin 3) (n : ℕ) :
    2*linePairs c n+n = ∑ i : Fin 3, (colorCount c n i)^2 := by
  induction n with
  | zero => simp [linePairs, colorCount]
  | succ n ih =>
    rw [linePairs_succ, colorSquares_succ, ← ih]
    ring

/-- The variance identity for every three-colored finite line. -/
theorem lineVariance_pairs (c : ℕ → Fin 3) (n : ℕ) :
    6*(linePairs c n:ℚ) = 3*lineVariance c n+(n:ℚ)^2-3*n := by
  have ht : (colorCount c n 0:ℚ)+colorCount c n 1+colorCount c n 2=n := by
    exact_mod_cast (by simpa [Fin.sum_univ_three] using colorCount_total c n)
  have hp : 2*(linePairs c n:ℚ)+n =
      (colorCount c n 0:ℚ)^2+(colorCount c n 1:ℚ)^2+(colorCount c n 2:ℚ)^2 := by
    exact_mod_cast (by simpa [Fin.sum_univ_three] using linePairs_square_count c n)
  simp only [lineVariance, Fin.sum_univ_three]
  nlinarith [sq_nonneg ((colorCount c n 0:ℚ)+colorCount c n 1+colorCount c n 2-n)]

def eqPair (a b : Fin 3) : ℕ := if a=b then 1 else 0
def isRainbow (a b c : Fin 3) : ℕ := if a≠b ∧ a≠c ∧ b≠c then 1 else 0
def isMono (a b c : Fin 3) : ℕ := if a=b ∧ b=c then 1 else 0

/-- Each individual corner contributes three, one, or zero equal-color pairs. -/
theorem corner_color_identity (a b c : Fin 3) :
    eqPair a b + eqPair a c + eqPair b c + isRainbow a b c =
      1+2*isMono a b c := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> decide

/-- The tuple (x,y,z) denotes cells (x,y),(z,y),(z,y+z-x), with y<x<z<N. -/
def cornerSum (N : ℕ) (f : ℕ → ℕ → ℕ → ℕ) : ℕ :=
  ∑ z ∈ range N, ∑ x ∈ range z, ∑ y ∈ range x, f x y z

def rainbowCount (c : Coloring) (N : ℕ) : ℕ :=
  cornerSum N fun x y z => isRainbow (c x y) (c z y) (c z (y+z-x))

def monoCount (c : Coloring) (N : ℕ) : ℕ :=
  cornerSum N fun x y z => isMono (c x y) (c z y) (c z (y+z-x))

def cornerEqualPairs (c : Coloring) (N : ℕ) : ℕ :=
  cornerSum N fun x y z =>
    eqPair (c x y) (c z y)+eqPair (c x y) (c z (y+z-x))+
      eqPair (c z y) (c z (y+z-x))

theorem corner_pair_identity (c : Coloring) (N : ℕ) :
    cornerEqualPairs c N + rainbowCount c N =
      cornerSum N (fun _ _ _ => 1)+2*monoCount c N := by
  simp only [cornerEqualPairs, rainbowCount, monoCount, cornerSum,
    Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro z hz
  apply Finset.sum_congr rfl
  intro x hx
  apply Finset.sum_congr rfl
  intro y hy
  exact corner_color_identity _ _ _

def rowColor (c : Coloring) (l : ℕ) : ℕ → Fin 3 := c l
def colColor (c : Coloring) (N l : ℕ) : ℕ → Fin 3 := fun j => c (N-l+j) (N-l-1)
def diagColor (c : Coloring) (N l : ℕ) : ℕ → Fin 3 := fun j => c (N-l+j) j

/-- These are the three nonempty line families, with an additional empty length-zero line. -/
def totalLinePairs (c : Coloring) (N : ℕ) : ℕ :=
  (∑ l ∈ range N, linePairs (rowColor c l) l)+
  (∑ l ∈ range N, linePairs (colColor c N l) l)+
  (∑ l ∈ range N, linePairs (diagColor c N l) l)

def totalVariance (c : Coloring) (N : ℕ) : ℚ :=
  (∑ l ∈ range N, lineVariance (rowColor c l) l)+
  (∑ l ∈ range N, lineVariance (colColor c N l) l)+
  (∑ l ∈ range N, lineVariance (diagColor c N l) l)

/-- Completion of a pair in a row; the middle index is reflected in the row. -/
theorem rowPairs_bridge (c : Coloring) (N : ℕ) :
    (∑ l ∈ range N, linePairs (rowColor c l) l) =
      cornerSum N (fun x y z => eqPair (c z y) (c z (y+z-x))) := by
  simp only [linePairs, rowColor, cornerSum, eqPair]
  simp_rw [Finset.sum_sigma']
  let reflect : (Σ z : ℕ, Σ x : ℕ, ℕ) → (Σ z : ℕ, Σ x : ℕ, ℕ) :=
    fun p => ⟨p.1,⟨p.2.2+p.1-p.2.1,p.2.2⟩⟩
  refine Finset.sum_nbij' reflect reflect ?_ ?_ ?_ ?_ ?_
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp ⊢
    dsimp [reflect]
    omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp ⊢
    dsimp [reflect]
    omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [reflect]
    congr 2
    omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [reflect]
    congr 2
    omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [reflect]
    rw [show y+z-(y+z-x)=x by omega]

/-- Column pairs and corners correspond by translating the two positions on the column. -/
theorem colPairs_bridge (c : Coloring) (N : ℕ) :
    (∑ l ∈ range N, linePairs (colColor c N l) l) =
      cornerSum N (fun x y z => eqPair (c x y) (c z y)) := by
  simp only [linePairs, colColor, cornerSum, eqPair]
  simp_rw [Finset.sum_sigma']
  let f : (Σ l : ℕ, Σ b : ℕ, ℕ) → (Σ z : ℕ, Σ x : ℕ, ℕ) :=
    fun p => ⟨N-p.1+p.2.1,⟨N-p.1+p.2.2,N-p.1-1⟩⟩
  let g : (Σ z : ℕ, Σ x : ℕ, ℕ) → (Σ l : ℕ, Σ b : ℕ, ℕ) :=
    fun p => ⟨N-1-p.2.2,⟨p.1-p.2.2-1,p.2.1-p.2.2-1⟩⟩
  refine Finset.sum_nbij' f g ?_ ?_ ?_ ?_ ?_
  · rintro ⟨l,b,a⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp ⊢
    dsimp [f]
    omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp ⊢
    dsimp [g]
    omega
  · rintro ⟨l,b,a⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [f,g]
    congr 2 <;> omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [f,g]
    congr 2 <;> omega
  · rintro ⟨l,b,a⟩ hp
    rfl

/-- Offset-line pairs give the first and third cells of a unique corner. -/
theorem diagPairs_bridge (c : Coloring) (N : ℕ) :
    (∑ l ∈ range N, linePairs (diagColor c N l) l) =
      cornerSum N (fun x y z => eqPair (c x y) (c z (y+z-x))) := by
  simp only [linePairs, diagColor, cornerSum, eqPair]
  simp_rw [Finset.sum_sigma']
  let f : (Σ l : ℕ, Σ b : ℕ, ℕ) → (Σ z : ℕ, Σ x : ℕ, ℕ) :=
    fun p => ⟨N-p.1+p.2.1,⟨N-p.1+p.2.2,p.2.2⟩⟩
  let g : (Σ z : ℕ, Σ x : ℕ, ℕ) → (Σ l : ℕ, Σ b : ℕ, ℕ) :=
    fun p => ⟨N-(p.2.1-p.2.2),⟨p.2.2+p.1-p.2.1,p.2.2⟩⟩
  refine Finset.sum_nbij' f g ?_ ?_ ?_ ?_ ?_
  · rintro ⟨l,b,a⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp ⊢
    dsimp [f]
    omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp ⊢
    dsimp [g]
    omega
  · rintro ⟨l,b,a⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [f,g]
    congr 2 <;> omega
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [f,g]
    congr 2 <;> omega
  · rintro ⟨l,b,a⟩ hp
    simp only [Finset.mem_sigma, Finset.mem_range] at hp
    dsimp [f]
    rw [show a+(N-l+b)-(N-l+a)=b by omega]

theorem totalLinePairs_eq (c : Coloring) (N : ℕ) :
    totalLinePairs c N = cornerEqualPairs c N := by
  rw [totalLinePairs, rowPairs_bridge, colPairs_bridge, diagPairs_bridge]
  simp only [cornerSum, cornerEqualPairs, Finset.sum_add_distrib]
  omega

theorem rational_range_sum (n : ℕ) :
    2*(∑ j ∈ range n, (j:ℚ))=(n:ℚ)*(n-1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [sum_range_succ]
    push_cast
    nlinarith

theorem corner_size_relation (N : ℕ) :
    2*(cornerSum N (fun _ _ _ => 1):ℚ)=
      (∑ l ∈ range N, (l:ℚ)^2)-(∑ l ∈ range N, (l:ℚ)) := by
  simp only [cornerSum, Finset.sum_const, Finset.card_range, smul_eq_mul, mul_one]
  push_cast
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro l hl
  nlinarith [rational_range_sum l]

theorem family_variance_pairs (f : ℕ → ℕ → Fin 3) (N : ℕ) :
    6*((∑ l ∈ range N, linePairs (f l) l):ℚ)=
      3*(∑ l ∈ range N, lineVariance (f l) l)+
        (∑ l ∈ range N, (l:ℚ)^2)-3*(∑ l ∈ range N, (l:ℚ)) := by
  simp only [Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl (fun l _ => lineVariance_pairs (f l) l)

/-- The complete geometric line identity of the manuscript, for any three-coloring. -/
theorem variance_identity (c : Coloring) (N : ℕ) :
    totalVariance c N+2*(rainbowCount c N:ℚ)-4*(monoCount c N:ℚ)=
      (N:ℚ)*(N-1) := by
  have hr := family_variance_pairs (rowColor c) N
  have hc := family_variance_pairs (colColor c N) N
  have hd := family_variance_pairs (diagColor c N) N
  have hp : (totalLinePairs c N:ℚ)+(rainbowCount c N:ℚ)=
      (cornerSum N (fun _ _ _ => 1):ℚ)+2*(monoCount c N:ℚ) := by
    rw [totalLinePairs_eq]
    exact_mod_cast corner_pair_identity c N
  have hk := corner_size_relation N
  have hs := rational_range_sum N
  simp only [totalLinePairs, Nat.cast_add, Nat.cast_sum] at hp
  unfold totalVariance
  linarith

theorem three_counts_square_gap (a b c : ℕ) (hm : (a+b+c)%3≠0) :
    (a+b+c)^2+2 ≤ 3*(a^2+b^2+c^2) := by
  have hcsZ : ((a:ℤ)+b+c)^2 ≤ 3*((a:ℤ)^2+(b:ℤ)^2+(c:ℤ)^2) := by
    nlinarith [sq_nonneg ((a:ℤ)-b),sq_nonneg ((a:ℤ)-c),sq_nonneg ((b:ℤ)-c)]
  have hcs : (a+b+c)^2 ≤ 3*(a^2+b^2+c^2) := by exact_mod_cast hcsZ
  have hr : (a+b+c)^2%3=1 := by
    have he : (a+b+c)%3=1 ∨ (a+b+c)%3=2 := by omega
    rcases he with he | he <;> simp [pow_two,Nat.mul_mod,he]
  omega

theorem lineVariance_nonneg (c : ℕ → Fin 3) (n : ℕ) : 0 ≤ lineVariance c n := by
  unfold lineVariance
  exact Finset.sum_nonneg (fun _ _ => sq_nonneg _)

theorem lineVariance_nondivisible (c : ℕ → Fin 3) (n : ℕ) (hn : n%3≠0) :
    (2/3:ℚ) ≤ lineVariance c n := by
  have ht : colorCount c n 0+colorCount c n 1+colorCount c n 2=n := by
    simpa [Fin.sum_univ_three] using colorCount_total c n
  have hq := three_counts_square_gap (colorCount c n 0) (colorCount c n 1)
    (colorCount c n 2) (by simpa [ht] using hn)
  rw [ht] at hq
  have hq' : (n:ℚ)^2+2 ≤ 3*((colorCount c n 0:ℚ)^2+
      (colorCount c n 1:ℚ)^2+(colorCount c n 2:ℚ)^2) := by exact_mod_cast hq
  have ht' : (colorCount c n 0:ℚ)+colorCount c n 1+colorCount c n 2=n := by
    exact_mod_cast ht
  simp only [lineVariance,Fin.sum_univ_three]
  rw [← ht'] at hq' ⊢
  nlinarith

def badLength (n : ℕ) : ℕ := if n%3=0 then 0 else 1

theorem lineVariance_min (c : ℕ → Fin 3) (n : ℕ) :
    (2/3:ℚ)*(badLength n:ℚ) ≤ lineVariance c n := by
  by_cases hn : n%3=0
  · simpa [badLength,hn] using lineVariance_nonneg c n
  · simpa [badLength,hn] using lineVariance_nondivisible c n hn

theorem badLength_sum_succ (n : ℕ) :
    (∑ l ∈ range (n+1), badLength l)=n-n/3 := by
  induction n with
  | zero => simp [badLength]
  | succ n ih =>
    rw [Finset.sum_range_succ,ih]
    unfold badLength
    split_ifs <;> omega

theorem badLength_sum (N : ℕ) (hN : 1≤N) :
    (∑ l ∈ range N, badLength l)=(N-1)-(N-1)/3 := by
  obtain ⟨n,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : N≠0)
  simpa using badLength_sum_succ n

theorem family_variance_lower (f : ℕ → ℕ → Fin 3) (N : ℕ) :
    (2/3:ℚ)*((∑ l ∈ range N, badLength l):ℚ) ≤
      ∑ l ∈ range N, lineVariance (f l) l := by
  rw [Finset.mul_sum]
  exact Finset.sum_le_sum (fun l _ => lineVariance_min (f l) l)

theorem totalVariance_lower (c : Coloring) (N : ℕ) (hN : 1≤N) :
    2*((((N-1)-(N-1)/3):ℕ):ℚ) ≤ totalVariance c N := by
  have hr := family_variance_lower (rowColor c) N
  have hc := family_variance_lower (colColor c N) N
  have hd := family_variance_lower (diagColor c N) N
  have he : (∑ l ∈ range N, (badLength l:ℚ))=
      ((((N-1)-(N-1)/3):ℕ):ℚ) := by exact_mod_cast badLength_sum N hN
  rw [he] at hr hc hd
  unfold totalVariance
  linarith

def ProperTriangle (c : Coloring) (N : ℕ) : Prop :=
  ∀ x y z : ℕ, y<x → x<z → z<N →
    ¬ (c x y=c z y ∧ c z y=c z (y+z-x))

theorem monoCount_zero (c : Coloring) (N : ℕ) (hc : ProperTriangle c N) :
    monoCount c N=0 := by
  unfold monoCount cornerSum
  apply Finset.sum_eq_zero
  intro z hz
  apply Finset.sum_eq_zero
  intro x hx
  apply Finset.sum_eq_zero
  intro y hy
  simp only [isMono, if_neg (hc x y z (mem_range.mp hy) (mem_range.mp hx)
    (mem_range.mp hz))]

theorem proper_variance_identity (c : Coloring) (N : ℕ) (hc : ProperTriangle c N) :
    totalVariance c N+2*(rainbowCount c N:ℚ)=(N:ℚ)*(N-1) := by
  simpa [monoCount_zero c N hc] using variance_identity c N

/-- The sharp separate-line-minimum bound U_N from Lemma lem:variance. -/
theorem rainbowCount_upper (c : Coloring) (N : ℕ) (hN : 1≤N)
    (hc : ProperTriangle c N) :
    rainbowCount c N ≤ N.choose 2-(N-1)+(N-1)/3 := by
  have hm : N.choose 2=∑ l ∈ range N, l := by
    rw [Nat.choose_two_right,Finset.sum_range_id]
  have hm' : 2*(N.choose 2:ℚ)=(N:ℚ)*(N-1) := by
    have he : (N.choose 2:ℚ)=∑ l ∈ range N, (l:ℚ) := by rw [hm]; simp
    rw [he]
    exact rational_range_sum N
  have hbase : N-1≤N.choose 2 := by
    rw [hm]
    obtain ⟨n,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : N≠0)
    rw [Finset.sum_range_succ]
    omega
  have hid := proper_variance_identity c N hc
  have hlo := totalVariance_lower c N hN
  have hdiv : (N-1)/3≤N-1 := Nat.div_le_self _ _
  have hr : (rainbowCount c N:ℚ) ≤
      (N.choose 2:ℚ)-((N-1:ℕ):ℚ)+(((N-1)/3:ℕ):ℚ) := by
    rw [Nat.cast_sub hdiv] at hlo
    linarith
  have he : (((N.choose 2-(N-1)+(N-1)/3):ℕ):ℚ)=
      (N.choose 2:ℚ)-((N-1:ℕ):ℚ)+(((N-1)/3:ℕ):ℚ) := by
    rw [Nat.cast_add,Nat.cast_sub hbase]
  rw [← he] at hr
  exact_mod_cast hr

/-- The nested index sums enumerate precisely the integer source corners of [0,N). -/
theorem cornerSum_source_bridge (N : ℕ) (v : ℕ → ℕ → ℕ → ℕ) :
    cornerSum N v = ∑ p ∈ EnergyForcing.Counting.sourceCorners
      (EnergyForcing.ShiftCounting.shifts N), v p.1.toNat p.2.1.toNat p.2.2.toNat := by
  unfold cornerSum
  simp_rw [Finset.sum_sigma']
  let f : (Σ z : ℕ, Σ x : ℕ, ℕ) → (ℤ×ℤ×ℤ) :=
    fun p => (p.2.1,p.2.2,p.1)
  let g : (ℤ×ℤ×ℤ) → (Σ z : ℕ, Σ x : ℕ, ℕ) :=
    fun p => ⟨p.2.2.toNat,⟨p.1.toNat,p.2.1.toNat⟩⟩
  refine Finset.sum_nbij' f g ?_ ?_ ?_ ?_ ?_
  · rintro ⟨z,x,y⟩ hp
    simp only [Finset.mem_sigma,Finset.mem_range] at hp
    dsimp [f]
    simp only [EnergyForcing.Counting.mem_sourceCorners,
      EnergyForcing.ShiftCounting.mem_shifts]
    omega
  · rintro ⟨x,y,z⟩ hp
    simp only [EnergyForcing.Counting.mem_sourceCorners,
      EnergyForcing.ShiftCounting.mem_shifts] at hp
    dsimp [g]
    simp only [Finset.mem_sigma,Finset.mem_range]
    omega
  · rintro ⟨z,x,y⟩ hp
    simp [f,g]
  · rintro ⟨x,y,z⟩ hp
    simp only [EnergyForcing.Counting.mem_sourceCorners,
      EnergyForcing.ShiftCounting.mem_shifts] at hp
    dsimp [f,g]
    apply Prod.ext
    · omega
    · apply Prod.ext <;> dsimp <;> omega
  · rintro ⟨z,x,y⟩ hp
    simp [f]

theorem properOn_triangle_bridge (c : Point → Fin 3) (N : ℕ)
    (hc : properOn (strictSource (fun x => x∈EnergyForcing.ShiftCounting.shifts N)) c) :
    ProperTriangle (fun x y => c (x,y)) N := by
  intro x y z hyx hxz hz
  have hstep : (0:ℤ)<(z:ℤ)-x := by omega
  have hsrc1 : strictSource (fun x => x∈EnergyForcing.ShiftCounting.shifts N)
      ((x:ℤ),(y:ℤ)) := by
    simp only [strictSource,EnergyForcing.ShiftCounting.mem_shifts]
    omega
  have hsrc2 : strictSource (fun x => x∈EnergyForcing.ShiftCounting.shifts N)
      ((x:ℤ)+((z:ℤ)-x),(y:ℤ)) := by
    simp only [strictSource,EnergyForcing.ShiftCounting.mem_shifts]
    omega
  have hsrc3 : strictSource (fun x => x∈EnergyForcing.ShiftCounting.shifts N)
      ((x:ℤ)+((z:ℤ)-x),(y:ℤ)+((z:ℤ)-x)) := by
    simp only [strictSource,EnergyForcing.ShiftCounting.mem_shifts]
    omega
  have hh := hc x y ((z:ℤ)-x) hstep hsrc1 hsrc2 hsrc3
  have he : ((y+z-x:ℕ):ℤ)=(y:ℤ)+((z:ℤ)-x) := by omega
  simpa only [he,add_sub_cancel] using hh

end EnergyForcing.LineCounting
