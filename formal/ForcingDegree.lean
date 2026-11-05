import ForcingCounting

namespace EnergyForcing.Forcing

open EnergyForcing.Counting
open EnergyForcing.FiberDominance

def tags (A : Finset ℤ) (z : Point → Bool) : Finset ((ℤ×ℤ×ℤ)×Bool) :=
  (forcedCorners A z).product Finset.univ

def inputTags (A : Finset ℤ) (z : Point → Bool) (q : Point) :=
  (tags A z).filter fun t => inputCell t.1 t.2=q

def outputTags (A : Finset ℤ) (z : Point → Bool) (q : Point) :=
  (tags A z).filter fun t => outputCell t.1=q

def incidentTags (A : Finset ℤ) (z : Point → Bool) (q : Point) :=
  (tags A z).filter fun t => q∈edgeOf t

def degree (A : Finset ℤ) (z : Point → Bool) (q : Point) : ℕ :=
  ((edges A z).filter fun e => q∈e).card

theorem input_ne_output (A : Finset ℤ) (p : ℤ×ℤ×ℤ) (hp : p∈sourceCorners A) (b : Bool) :
    inputCell p b≠outputCell p := by
  rcases p with ⟨x,y,w⟩
  have h := (mem_sourceCorners A x y w).mp hp
  intro he
  cases b <;> simp only [inputCell,outputCell,Bool.false_eq_true,if_false,if_true,Prod.mk.injEq] at he <;> omega

theorem degree_tag_count (A : Finset ℤ) (z : Point → Bool) (q : Point) :
    degree A z q = (incidentTags A z q).card := by
  have hi : Set.InjOn edgeOf (incidentTags A z q) :=
    (corner_edge_injective A).mono (by
      intro p hp
      have hp' := Finset.mem_filter.mp hp
      have ht := Finset.mem_product.mp hp'.1
      exact Finset.mem_product.mpr ⟨(Finset.mem_filter.mp ht.1).1,ht.2⟩)
  unfold degree edges
  rw [Finset.filter_image]
  exact Finset.card_image_of_injOn hi

theorem incident_partition (A : Finset ℤ) (z : Point → Bool) (q : Point) :
    incidentTags A z q=inputTags A z q ∪ outputTags A z q := by
  ext ⟨p,b⟩
  simp [incidentTags,inputTags,outputTags,edgeOf,or_comm,and_or_left,eq_comm]

theorem incident_disjoint (A : Finset ℤ) (z : Point → Bool) (q : Point) :
    Disjoint (inputTags A z q) (outputTags A z q) := by
  apply Finset.disjoint_left.mpr
  rintro ⟨p,b⟩ hi ho
  have hp := (Finset.mem_filter.mp (Finset.mem_product.mp (Finset.mem_filter.mp hi).1).1).1
  exact input_ne_output A p hp b ((Finset.mem_filter.mp hi).2.trans (Finset.mem_filter.mp ho).2.symm)

theorem outputTags_card (A : Finset ℤ) (z : Point → Bool) (q : Point) (hq : q∈sourceCells A) :
    (outputTags A z q).card=2*H A z q := by
  have he : outputTags A z q =
      ((forcedCorners A z).filter fun p => outputCell p=q).product (Finset.univ : Finset Bool) := by
    ext p
    simp [outputTags,tags,and_assoc,and_left_comm,and_comm]
  rw [he]
  simp [Finset.card_product,completion_fiber_count A z q hq,Nat.mul_comm]

def tagFromMate (q : Point) (a : ℤ) : (ℤ×ℤ×ℤ)×Bool :=
  if a<q.2 then ((a+(q.1-q.2),a,q.1),true) else ((q.1,q.2,a+(q.1-q.2)),false)

def mateFromTag (t : (ℤ×ℤ×ℤ)×Bool) : ℤ :=
  if t.2 then t.1.2.1 else t.1.2.1+t.1.2.2-t.1.1

theorem inputTags_card (A : Finset ℤ) (z : Point → Bool) (q : Point) (hq : q∈sourceCells A) :
    (inputTags A z q).card=(fiberClass A z (q.1-q.2) (z q)).card-1 := by
  rcases q with ⟨v,u⟩
  rcases (mem_sourceCells A v u).mp hq with ⟨hv,hu,huv⟩
  have hself : u∈fiberClass A z (v-u) (z (v,u)) := by
    simp [fiberClass,mem_positiveFiber,hu,hv]
  rw [← Finset.card_erase_of_mem hself]
  symm
  refine Finset.card_nbij' (tagFromMate (v,u)) mateFromTag ?_ ?_ ?_ ?_
  · intro a ha
    rcases Finset.mem_erase.mp ha with ⟨hneq,hclass⟩
    rcases Finset.mem_filter.mp hclass with ⟨hf,hcolor⟩
    rcases (mem_positiveFiber A (v-u) a).mp hf with ⟨ha,had⟩
    by_cases hal : a<u
    · have he : a+v-(a+(v-u))=u := by ring
      simp only [tagFromMate,hal,if_pos]
      apply Finset.mem_filter.mpr
      constructor
      · apply Finset.mem_product.mpr
        refine ⟨Finset.mem_filter.mpr ⟨?_,?_⟩,Finset.mem_univ _⟩
        · apply (mem_sourceCorners A (a+(v-u)) a v).mpr
          rw [he]
          exact ⟨had,ha,hv,by omega,by omega,hu⟩
        · simpa only [he] using hcolor
      · simp [inputCell,he]
    · have he : u+(a+(v-u))-v=a := by ring
      simp only [tagFromMate,hal,if_false]
      apply Finset.mem_filter.mpr
      constructor
      · apply Finset.mem_product.mpr
        refine ⟨Finset.mem_filter.mpr ⟨?_,?_⟩,Finset.mem_univ _⟩
        · apply (mem_sourceCorners A v u (a+(v-u))).mpr
          rw [he]
          exact ⟨hv,hu,had,huv,by omega,ha⟩
        · simpa only [he] using hcolor.symm
      · rfl
  · rintro ⟨⟨x,y,w⟩,b⟩ hp
    have ht := Finset.mem_filter.mp hp
    have hf := Finset.mem_filter.mp (Finset.mem_product.mp ht.1).1
    rcases (mem_sourceCorners A x y w).mp hf.1 with ⟨hx,hy,hw,hyx,hxw,ha⟩
    have hcolor := hf.2
    cases b
    · have he := ht.2
      simp only [inputCell,Bool.false_eq_true,if_false,Prod.mk.injEq] at he
      obtain ⟨hex,hey⟩ := he
      subst x; subst y
      simp only [mateFromTag,Bool.false_eq_true,if_false,Finset.mem_erase,fiberClass,Finset.mem_filter,mem_positiveFiber]
      have he : u+w-v+(v-u)=w := by ring
      rw [he]
      exact ⟨by omega,⟨ha,hw⟩,hcolor.symm⟩
    · have he := ht.2
      simp only [inputCell,if_true,Prod.mk.injEq] at he
      have ew := he.1
      have ey := he.2
      simp only [mateFromTag,if_true,Finset.mem_erase,fiberClass,Finset.mem_filter,mem_positiveFiber]
      have ex : y+(v-u)=x := by omega
      rw [ex]
      refine ⟨by omega,⟨hy,hx⟩,?_⟩
      convert hcolor using 1 <;> simp_all
  · intro a ha
    dsimp [tagFromMate]
    split <;> simp only [mateFromTag,Bool.false_eq_true,if_false,if_true] <;> ring
  · rintro ⟨⟨x,y,w⟩,b⟩ hp
    have ht := Finset.mem_filter.mp hp
    have hf := Finset.mem_filter.mp (Finset.mem_product.mp ht.1).1
    have hc := (mem_sourceCorners A x y w).mp hf.1
    have he := ht.2
    cases b
    · simp only [inputCell,Bool.false_eq_true,if_false,Prod.mk.injEq] at he
      obtain ⟨hex,hey⟩ := he
      subst x; subst y
      have hn : ¬u+w-v<u := by omega
      simp only [mateFromTag,Bool.false_eq_true,if_false,tagFromMate,hn,if_false]
      congr 3 <;> omega
    · simp only [inputCell,if_true,Prod.mk.injEq] at he
      have hyu : y<u := by omega
      simp only [mateFromTag,if_true,tagFromMate,hyu,if_true]
      congr 3 <;> omega

/-- The actual undirected graph degree formula, with no duplicated physical edges. -/
theorem forcing_degree (A : Finset ℤ) (z : Point → Bool) (q : Point) (hq : q∈sourceCells A) :
    degree A z q=(fiberClass A z (q.1-q.2) (z q)).card-1+2*H A z q := by
  rw [degree_tag_count,incident_partition,Finset.card_union_of_disjoint (incident_disjoint A z q),
    inputTags_card A z q hq,outputTags_card A z q hq]

end EnergyForcing.Forcing
