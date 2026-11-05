import ProgressionProducts

set_option autoImplicit false

namespace EnergyForcing.Counting
open scoped BigOperators

def HasRectangle {m n : ℕ} (a : Fin m→Fin n→Bool) : Prop :=
  ∃i j k l,i≠j ∧ k≠l ∧ a i k=a i l ∧ a i l=a j k ∧ a j k=a j l

def pairChoice (a : Fin 3→Bool) : Fin 3 :=
  if a 0=a 1 then 0 else if a 0=a 2 then 1 else 2

def pairLeft (k : Fin 3) : Fin 3 := if k=2 then 1 else 0
def pairRight (k : Fin 3) : Fin 3 := if k=0 then 1 else 2

theorem pairChoice_valid : ∀a:Fin 3→Bool,
    pairLeft (pairChoice a)≠pairRight (pairChoice a) ∧
    a (pairLeft (pairChoice a))=a (pairRight (pairChoice a)) := by decide

theorem rectangle_seven_three (a : Fin 7→Fin 3→Bool) : HasRectangle a := by
  let f : Fin 7→Fin 3×Bool := fun i=>(pairChoice (a i),a i (pairLeft (pairChoice (a i))))
  by_contra hn
  have hinj : Function.Injective f := by
    intro i j he
    by_contra hij
    have hp := pairChoice_valid (a i)
    have hq := pairChoice_valid (a j)
    have he1 := congrArg Prod.fst he
    have he2 := congrArg Prod.snd he
    dsimp [f] at he1 he2
    rw [← he1] at he2 hq
    exact hn ⟨i,j,pairLeft (pairChoice (a i)),pairRight (pairChoice (a i)),
      hij,hp.1,hp.2,hp.2.symm.trans he2,hq.2⟩
  have hc := Fintype.card_le_of_injective f hinj
  norm_num at hc

def colorPairs {n : ℕ} (a : Fin n→Bool) (b : Bool) : Finset (Fin n×Fin n) :=
  (Finset.univ.product Finset.univ).filter fun p=>p.1<p.2 ∧ a p.1=b ∧ a p.2=b

def rowPairs (n : ℕ) : Finset (Fin n×Fin n) :=
  (Finset.univ.product Finset.univ).filter fun p=>p.1<p.2

@[simp] theorem mem_colorPairs {n : ℕ} (a : Fin n→Bool) (b : Bool) (i j : Fin n) :
    (i,j)∈colorPairs a b ↔ i<j ∧ a i=b ∧ a j=b := by simp [colorPairs]

theorem colorPairs_subset {n : ℕ} (a : Fin n→Bool) (b : Bool) :
    colorPairs a b⊆rowPairs n := by
  rintro ⟨i,j⟩ hp
  have hh := (mem_colorPairs a b i j).mp hp
  simp [rowPairs,hh.1]

theorem five_pair_count_min : ∀a:Fin 5→Bool,
    4≤(colorPairs a false).card+(colorPairs a true).card := by decide

theorem five_pair_count_odd : ∀a:Fin 5→Bool,
    (colorPairs a false).card+(colorPairs a true).card=4 →
    (colorPairs a true).card%2=1 := by decide

theorem colorPairs_columns_disjoint (a : Fin 5→Fin 5→Bool) (hn:¬HasRectangle a)
    (b : Bool) (k l : Fin 5) (hkl:k≠l) :
    Disjoint (colorPairs (fun i=>a i k) b) (colorPairs (fun i=>a i l) b) := by
  apply Finset.disjoint_left.mpr
  rintro ⟨i,j⟩ hp hq
  have hh := (mem_colorPairs _ b i j).mp hp
  have hh' := (mem_colorPairs _ b i j).mp hq
  exact hn ⟨i,j,k,l,ne_of_lt hh.1,hkl,hh.2.1.trans hh'.2.1.symm,
    hh'.2.1.trans hh.2.2.symm,hh.2.2.trans hh'.2.2.symm⟩

theorem colorPairs_columns_sum_le (a : Fin 5→Fin 5→Bool) (hn:¬HasRectangle a)
    (b : Bool) : (∑k:Fin 5,(colorPairs (fun i=>a i k) b).card)≤10 := by
  have hdis : (Finset.univ : Finset (Fin 5)).toSet.PairwiseDisjoint
      (fun k=>colorPairs (fun i=>a i k) b) := by
    intro k _ l _ hkl
    exact colorPairs_columns_disjoint a hn b k l hkl
  have he := Finset.card_biUnion hdis
  have hsub : (Finset.univ.biUnion (fun k=>colorPairs (fun i=>a i k) b))⊆rowPairs 5 := by
    intro p hp
    obtain ⟨k,_,hk⟩ := Finset.mem_biUnion.mp hp
    exact colorPairs_subset _ b hk
  have hc := Finset.card_le_card hsub
  rw [he] at hc
  have hten : (rowPairs 5).card=10 := by decide
  simpa [hten] using hc

theorem rectangle_five_five (a : Fin 5→Fin 5→Bool) : HasRectangle a := by
  by_contra hn
  have hf := colorPairs_columns_sum_le a hn false
  have ht := colorPairs_columns_sum_le a hn true
  have hlow := Finset.sum_le_sum (s:=Finset.univ) (fun k _=>five_pair_count_min (fun i=>a i k))
  have htot : (∑k:Fin 5,((colorPairs (fun i=>a i k) false).card+
      (colorPairs (fun i=>a i k) true).card))=20 := by
    simp only [Finset.sum_add_distrib] at hlow ⊢
    norm_num at hlow
    omega
  have heach : ∀k:Fin 5,(colorPairs (fun i=>a i k) false).card+
      (colorPairs (fun i=>a i k) true).card=4 := by
    have heq : (∑_k:Fin 5,4)=(∑k:Fin 5,((colorPairs (fun i=>a i k) false).card+
      (colorPairs (fun i=>a i k) true).card)) := by simpa using htot.symm
    have hh := (Finset.sum_eq_sum_iff_of_le (fun k _=>five_pair_count_min (fun i=>a i k))).mp heq
    intro k
    exact (hh k (Finset.mem_univ k)).symm
  have hten : (∑k:Fin 5,(colorPairs (fun i=>a i k) true).card)=10 := by
    rw [Finset.sum_add_distrib] at htot
    omega
  have h0 := five_pair_count_odd (fun i=>a i 0) (heach 0)
  have h1 := five_pair_count_odd (fun i=>a i 1) (heach 1)
  have h2 := five_pair_count_odd (fun i=>a i 2) (heach 2)
  have h3 := five_pair_count_odd (fun i=>a i 3) (heach 3)
  have h4 := five_pair_count_odd (fun i=>a i 4) (heach 4)
  norm_num [Fin.sum_univ_succ,Fin.succ] at hten
  change (colorPairs (fun i=>a i 0) true).card+
    ((colorPairs (fun i=>a i 1) true).card+
    ((colorPairs (fun i=>a i 2) true).card+
    ((colorPairs (fun i=>a i 3) true).card+(colorPairs (fun i=>a i 4) true).card)))=10 at hten
  omega

end EnergyForcing.Counting
