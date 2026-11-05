import SourceCounting
import Geometry

set_option autoImplicit false

namespace EnergyForcing.Counting
open scoped BigOperators

def crossFiber (B C : Finset ℤ) (h : ℤ) : Finset ℤ :=
  B.filter fun u => u+h∈C

@[simp] theorem mem_crossFiber (B C : Finset ℤ) (h u : ℤ) :
    u∈crossFiber B C h ↔ u∈B ∧ u+h∈C := by simp [crossFiber]

def crossCount (B C : Finset ℤ) (h : ℤ) : ℕ := (crossFiber B C h).card

def Qinc (B C : Finset ℤ) : Finset (Σ _ : ℤ, ℤ×ℤ) :=
  (posDiffs (B∪C)).sigma fun h => (crossFiber B C h).product (crossFiber C B h)

def Q (B C : Finset ℤ) : ℕ :=
  ∑h∈posDiffs (B∪C),crossCount B C h*crossCount C B h

@[simp] theorem mem_Qinc (B C : Finset ℤ) (h u v : ℤ) :
    ⟨h,(u,v)⟩∈Qinc B C ↔ 0<h ∧ u∈B ∧ u+h∈C ∧ v∈C ∧ v+h∈B := by
  simp only [Qinc,Finset.mem_sigma,Finset.product_eq_sprod,Finset.mem_product,mem_crossFiber]
  constructor
  · rintro ⟨hh,⟨hu,hu'⟩,⟨hv,hv'⟩⟩
    exact ⟨((mem_posDiffs _ h).mp hh).1,hu,hu',hv,hv'⟩
  · rintro ⟨hh,hu,hu',hv,hv'⟩
    exact ⟨(mem_posDiffs _ h).mpr ⟨hh,u,Finset.mem_union_left _ hu,
      Finset.mem_union_right _ hu'⟩,⟨hu,hu'⟩,⟨hv,hv'⟩⟩

theorem Q_eq_card (B C : Finset ℤ) : Q B C=(Qinc B C).card := by
  simp [Q,Qinc,Finset.card_sigma,Finset.card_product,crossCount]

theorem golomb_pair_or (A : Finset ℤ) (hA : Golomb (·∈A))
    (a b c d : ℤ) (ha:a∈A) (hb:b∈A) (hc:c∈A) (hd:d∈A)
    (he:a+b=c+d) : (a=c ∧ b=d) ∨ (a=d ∧ b=c) := by
  by_cases hab : a≤b <;> by_cases hcd : c≤d
  · exact Or.inl (golomb_pair_sum_unique (·∈A) hA a b c d ha hb hc hd hab hcd he)
  · have hh := golomb_pair_sum_unique (·∈A) hA a b d c ha hb hd hc hab (by omega) (by omega)
    exact Or.inr hh
  · have hh := golomb_pair_sum_unique (·∈A) hA b a c d hb ha hc hd (by omega) hcd (by omega)
    exact Or.inr ⟨hh.2,hh.1⟩
  · have hh := golomb_pair_sum_unique (·∈A) hA b a d c hb ha hd hc (by omega) (by omega) (by omega)
    exact Or.inl ⟨hh.2,hh.1⟩

def QcodeB (p : Σ _ : ℤ, ℤ×ℤ) : ℤ×ℤ :=
  if p.2.1+p.1≤p.2.2 then (p.2.1,p.2.2+p.1) else (p.2.2+p.1,p.2.1)

theorem Q_le_B_sq (B C : Finset ℤ) (hC : Golomb (·∈C)) : Q B C≤B.card^2 := by
  rw [Q_eq_card,pow_two,← Finset.card_product]
  refine Finset.card_le_card_of_injOn QcodeB ?_ ?_
  · rintro ⟨h,u,v⟩ hp
    rcases (mem_Qinc B C h u v).mp hp with ⟨_,hu,_,_,hv⟩
    simp only [QcodeB]
    split <;> simp [hu,hv]
  · rintro ⟨h,u,v⟩ hp ⟨k,w,z⟩ hq he
    rcases (mem_Qinc B C h u v).mp hp with ⟨hh,hu,huh,hv,hvh⟩
    rcases (mem_Qinc B C k w z).mp hq with ⟨hk,hw,hwk,hz,hzk⟩
    have hes : u+h+v=w+k+z := by
      dsimp only [QcodeB] at he
      split_ifs at he <;> simp only [Prod.mk.injEq] at he <;> omega
    have hc := golomb_pair_or C hC (u+h) v (w+k) z huh hv hwk hz hes
    have hhkw : h=k ∧ u=w ∧ v=z := by
      dsimp only [QcodeB] at he
      split_ifs at he <;> simp only [Prod.mk.injEq] at he <;> rcases hc with hc|hc <;> omega
    rcases hhkw with ⟨rfl,rfl,rfl⟩
    rfl

theorem Q_swap (B C : Finset ℤ) : Q B C=Q C B := by
  simp only [Q,Finset.union_comm B C]
  apply Finset.sum_congr rfl
  intro h _
  exact Nat.mul_comm _ _

theorem Q_le_C_sq (B C : Finset ℤ) (hB : Golomb (·∈B)) : Q B C≤C.card^2 := by
  rw [Q_swap]
  exact Q_le_B_sq C B hB

def Qcharge (p : Σ _ : ℤ, ℤ×ℤ) : (ℤ×ℤ) ⊕ (ℤ×ℤ) :=
  if p.2.1+p.1≤p.2.2 ∨ p.2.2+p.1<p.2.1 then
    Sum.inl (max p.2.1 (p.2.2+p.1),min p.2.1 (p.2.2+p.1))
  else
    Sum.inr (max (p.2.1+p.1) p.2.2,min (p.2.1+p.1) p.2.2)

theorem Q_le_U (B C : Finset ℤ) (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    Q B C≤M B+M C := by
  rw [Q_eq_card,← sourceCells_card,← sourceCells_card,← Finset.card_disjSum]
  refine Finset.card_le_card_of_injOn Qcharge ?_ ?_
  · rintro ⟨h,u,v⟩ hp
    rcases (mem_Qinc B C h u v).mp hp with ⟨hh,hu,huh,hv,hvh⟩
    simp only [Qcharge]
    split_ifs with hc
    · apply Finset.inl_mem_disjSum.mpr
      apply (mem_sourceCells B _ _).mpr
      constructor
      · by_cases h : u≤v+h <;> simp [max_def,h,hu,hvh]
      constructor
      · by_cases h : u≤v+h <;> simp [min_def,h,hu,hvh]
      · rcases hc with hc|hc <;> omega
    · apply Finset.inr_mem_disjSum.mpr
      apply (mem_sourceCells C _ _).mpr
      constructor
      · by_cases h : u+h≤v <;> simp [max_def,h,huh,hv]
      constructor
      · by_cases h : u+h≤v <;> simp [min_def,h,huh,hv]
      · omega
  · rintro ⟨h,u,v⟩ hp ⟨k,w,z⟩ hq he
    rcases (mem_Qinc B C h u v).mp hp with ⟨hh,hu,huh,hv,hvh⟩
    rcases (mem_Qinc B C k w z).mp hq with ⟨hk,hw,hwk,hz,hzk⟩
    have hes : u+(v+h)=w+(z+k) := by
      dsimp only [Qcharge] at he
      split_ifs at he <;> simp only [Sum.inl.injEq,Sum.inr.injEq,Sum.inl_ne_inr,
        Sum.inr_ne_inl,Prod.mk.injEq] at he
      all_goals omega
    have hb := golomb_pair_or B hB u (v+h) w (z+k) hu hvh hw hzk hes
    have hc := golomb_pair_or C hC (u+h) v (w+k) z huh hv hwk hz (by omega)
    have hhkw : h=k ∧ u=w ∧ v=z := by
      dsimp only [Qcharge] at he
      split_ifs at he <;> simp only [Sum.inl.injEq,Sum.inr.injEq,Sum.inl_ne_inr,
        Sum.inr_ne_inl,Prod.mk.injEq] at he
      all_goals rcases hb with hb|hb <;> rcases hc with hc|hc <;> omega
    rcases hhkw with ⟨rfl,rfl,rfl⟩
    rfl

def crossCollisions (B C : Finset ℤ) : Finset (Σ _ : ℤ, ℤ×ℤ) :=
  (posDiffs (B∪C)).sigma fun h => sourceCells (crossFiber B C h)

@[simp] theorem mem_crossCollisions (B C : Finset ℤ) (h v u : ℤ) :
    ⟨h,(v,u)⟩∈crossCollisions B C ↔
    0<h ∧ u<v ∧ u∈B ∧ v∈B ∧ u+h∈C ∧ v+h∈C := by
  simp only [crossCollisions,Finset.mem_sigma,mem_sourceCells,mem_crossFiber]
  constructor
  · rintro ⟨hh,⟨hv,hvh⟩,⟨hu,huh⟩,huv⟩
    exact ⟨((mem_posDiffs _ h).mp hh).1,huv,hu,hv,huh,hvh⟩
  · rintro ⟨hh,huv,hu,hv,huh,hvh⟩
    exact ⟨(mem_posDiffs _ h).mpr ⟨hh,u,Finset.mem_union_left _ hu,
      Finset.mem_union_right _ huh⟩,⟨hv,hvh⟩,⟨hu,huh⟩,huv⟩

theorem crossCollisions_card (B C : Finset ℤ) :
    (crossCollisions B C).card=∑h∈posDiffs (B∪C),(crossCount B C h).choose 2 := by
  simp only [crossCollisions,Finset.card_sigma,sourceCells_card,M,crossCount]

def rho (B C : Finset ℤ) : ℕ := (posDiffs B∩posDiffs C).card

def collisionLength : (Σ _ : ℤ, ℤ×ℤ) ⊕ (Σ _ : ℤ, ℤ×ℤ) → ℤ :=
  Sum.elim (fun p => p.2.1-p.2.2) (fun p => p.2.1-p.2.2)

theorem collision_same_injective (B C : Finset ℤ)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C))
    (p q : Σ _ : ℤ, ℤ×ℤ) (hp:p∈crossCollisions B C) (hq:q∈crossCollisions B C)
    (he:p.2.1-p.2.2=q.2.1-q.2.2) : p=q := by
  rcases p with ⟨h,v,u⟩; rcases q with ⟨k,z,w⟩
  rcases (mem_crossCollisions B C h v u).mp hp with ⟨hh,huv,hu,hv,huh,hvh⟩
  rcases (mem_crossCollisions B C k z w).mp hq with ⟨hk,hwz,hw,hz,hwk,hzk⟩
  have hb := hB u v w z hu hv hw hz huv hwz he
  have hc := hC (u+h) (v+h) (w+k) (z+k) huh hvh hwk hzk (by omega) (by omega) (by dsimp at he; omega)
  have hhkw : h=k ∧ u=w ∧ v=z := by omega
  rcases hhkw with ⟨rfl,rfl,rfl⟩
  rfl

theorem collision_cross_ne (B C : Finset ℤ)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C))
    (p q : Σ _ : ℤ, ℤ×ℤ) (hp:p∈crossCollisions B C) (hq:q∈crossCollisions C B) :
    p.2.1-p.2.2≠q.2.1-q.2.2 := by
  rcases p with ⟨h,v,u⟩; rcases q with ⟨k,z,w⟩
  rcases (mem_crossCollisions B C h v u).mp hp with ⟨hh,huv,hu,hv,huh,hvh⟩
  rcases (mem_crossCollisions C B k z w).mp hq with ⟨hk,hwz,hw,hz,hwk,hzk⟩
  intro he
  have hb := hB u v (w+k) (z+k) hu hv hwk hzk huv (by omega) (by dsimp at he; omega)
  have hc := hC (u+h) (v+h) w z huh hvh hw hz (by omega) hwz (by dsimp at he; omega)
  omega

theorem collision_identity (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (crossCollisions B C).card+(crossCollisions C B).card=rho B C := by
  rw [← Finset.card_disjSum]
  unfold rho
  refine Finset.card_bij (fun p _ => collisionLength p) ?_ ?_ ?_
  · intro p hp
    rcases p with p|p
    · obtain hp := Finset.inl_mem_disjSum.mp hp
      rcases p with ⟨h,v,u⟩
      rcases (mem_crossCollisions B C h v u).mp hp with ⟨hh,huv,hu,hv,huh,hvh⟩
      apply Finset.mem_inter.mpr
      exact ⟨(mem_posDiffs B _).mpr ⟨by dsimp [collisionLength]; omega,u,hu,by simpa [collisionLength] using hv⟩,
        (mem_posDiffs C _).mpr ⟨by dsimp [collisionLength]; omega,u+h,huh,by convert hvh using 1 <;> dsimp [collisionLength] <;> omega⟩⟩
    · obtain hp := Finset.inr_mem_disjSum.mp hp
      rcases p with ⟨h,v,u⟩
      rcases (mem_crossCollisions C B h v u).mp hp with ⟨hh,huv,hu,hv,huh,hvh⟩
      apply Finset.mem_inter.mpr
      exact ⟨(mem_posDiffs B _).mpr ⟨by dsimp [collisionLength]; omega,u+h,huh,by convert hvh using 1 <;> dsimp [collisionLength] <;> omega⟩,
        (mem_posDiffs C _).mpr ⟨by dsimp [collisionLength]; omega,u,hu,by simpa [collisionLength] using hv⟩⟩
  · intro p hp q hq he
    rcases p with p|p <;> rcases q with q|q
    · exact congrArg Sum.inl (collision_same_injective B C hB hC p q
        (Finset.inl_mem_disjSum.mp hp) (Finset.inl_mem_disjSum.mp hq) he)
    · exact False.elim (collision_cross_ne B C hB hC p q
        (Finset.inl_mem_disjSum.mp hp) (Finset.inr_mem_disjSum.mp hq) he)
    · exact False.elim (collision_cross_ne C B hC hB p q
        (Finset.inr_mem_disjSum.mp hp) (Finset.inl_mem_disjSum.mp hq) he)
    · exact congrArg Sum.inr (collision_same_injective C B hC hB p q
        (Finset.inr_mem_disjSum.mp hp) (Finset.inr_mem_disjSum.mp hq) he)
  · intro d hd
    obtain ⟨hdB,hdC⟩ := Finset.mem_inter.mp hd
    obtain ⟨hdpos,u,hu,hud⟩ := (mem_posDiffs B d).mp hdB
    obtain ⟨_,v,hv,hvd⟩ := (mem_posDiffs C d).mp hdC
    have hne : u≠v := by
      intro he
      exact Finset.disjoint_left.mp hBC hu (he ▸ hv)
    by_cases huv : u<v
    · refine ⟨Sum.inl ⟨v-u,(u+d,u)⟩,?_,?_⟩
      · apply Finset.inl_mem_disjSum.mpr
        apply (mem_crossCollisions B C _ _ _).mpr
        refine ⟨by omega,by omega,hu,hud,by simpa using hv,?_⟩
        convert hvd using 1 <;> omega
      · simp [collisionLength]
    · refine ⟨Sum.inr ⟨u-v,(v+d,v)⟩,?_,?_⟩
      · apply Finset.inr_mem_disjSum.mpr
        apply (mem_crossCollisions C B _ _ _).mpr
        refine ⟨by omega,by omega,hv,hvd,by simpa using hu,?_⟩
        convert hud using 1 <;> omega
      · simp [collisionLength]

theorem collision_sum_identity (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (∑h∈posDiffs (B∪C),((crossCount B C h).choose 2+(crossCount C B h).choose 2))=rho B C := by
  rw [Finset.sum_add_distrib,← crossCollisions_card]
  rw [Finset.union_comm B C,← crossCollisions_card]
  exact collision_identity B C hBC hB hC

def crossStarts (B C : Finset ℤ) : Finset (Σ _ : ℤ, ℤ) :=
  (posDiffs (B∪C)).sigma fun h => crossFiber B C h

@[simp] theorem mem_crossStarts (B C : Finset ℤ) (h u : ℤ) :
    ⟨h,u⟩∈crossStarts B C ↔ 0<h ∧ u∈B ∧ u+h∈C := by
  simp only [crossStarts,Finset.mem_sigma,mem_crossFiber]
  constructor
  · rintro ⟨hh,hu,huh⟩
    exact ⟨((mem_posDiffs _ h).mp hh).1,hu,huh⟩
  · rintro ⟨hh,hu,huh⟩
    exact ⟨(mem_posDiffs _ h).mpr ⟨hh,u,Finset.mem_union_left _ hu,
      Finset.mem_union_right _ huh⟩,hu,huh⟩

def crossPair : (Σ _ : ℤ, ℤ) ⊕ (Σ _ : ℤ, ℤ) → ℤ×ℤ :=
  Sum.elim (fun p => (p.2,p.2+p.1)) (fun p => (p.2+p.1,p.2))

theorem crossStarts_card (B C : Finset ℤ) (hBC : Disjoint B C) :
    (crossStarts B C).card+(crossStarts C B).card=B.card*C.card := by
  rw [← Finset.card_disjSum,← Finset.card_product]
  refine Finset.card_bij (fun p _ => crossPair p) ?_ ?_ ?_
  · intro p hp
    rcases p with ⟨h,u⟩|⟨h,u⟩
    · have hh := (mem_crossStarts B C h u).mp (Finset.inl_mem_disjSum.mp hp)
      simpa [crossPair] using Finset.mk_mem_product hh.2.1 hh.2.2
    · have hh := (mem_crossStarts C B h u).mp (Finset.inr_mem_disjSum.mp hp)
      simpa [crossPair] using Finset.mk_mem_product hh.2.2 hh.2.1
  · intro p hp q hq he
    rcases p with ⟨h,u⟩|⟨h,u⟩ <;> rcases q with ⟨k,v⟩|⟨k,v⟩
    · have hh := (mem_crossStarts B C h u).mp (Finset.inl_mem_disjSum.mp hp)
      have hk := (mem_crossStarts B C k v).mp (Finset.inl_mem_disjSum.mp hq)
      have huv : h=k ∧ u=v := by
        dsimp [crossPair] at he
        simp only [Prod.mk.injEq] at he
        omega
      rcases huv with ⟨rfl,rfl⟩; rfl
    · have hh := (mem_crossStarts B C h u).mp (Finset.inl_mem_disjSum.mp hp)
      have hk := (mem_crossStarts C B k v).mp (Finset.inr_mem_disjSum.mp hq)
      dsimp [crossPair] at he
      simp only [Prod.mk.injEq] at he
      omega
    · have hh := (mem_crossStarts C B h u).mp (Finset.inr_mem_disjSum.mp hp)
      have hk := (mem_crossStarts B C k v).mp (Finset.inl_mem_disjSum.mp hq)
      dsimp [crossPair] at he
      simp only [Prod.mk.injEq] at he
      omega
    · have hh := (mem_crossStarts C B h u).mp (Finset.inr_mem_disjSum.mp hp)
      have hk := (mem_crossStarts C B k v).mp (Finset.inr_mem_disjSum.mp hq)
      have huv : h=k ∧ u=v := by
        dsimp [crossPair] at he
        simp only [Prod.mk.injEq] at he
        omega
      rcases huv with ⟨rfl,rfl⟩; rfl
  · rintro ⟨u,v⟩ hp
    have hmem := Finset.mem_product.mp hp
    have huv : u≠v := by
      intro he
      exact Finset.disjoint_left.mp hBC hmem.1 (he ▸ hmem.2)
    by_cases hlt : u<v
    · refine ⟨Sum.inl ⟨v-u,u⟩,?_,?_⟩
      · exact Finset.inl_mem_disjSum.mpr ((mem_crossStarts B C _ _).mpr
          ⟨by omega,hmem.1,by simpa using hmem.2⟩)
      · simp [crossPair]
    · refine ⟨Sum.inr ⟨u-v,v⟩,?_,?_⟩
      · exact Finset.inr_mem_disjSum.mpr ((mem_crossStarts C B _ _).mpr
          ⟨by omega,hmem.2,by simpa using hmem.1⟩)
      · simp [crossPair]

theorem cross_mass (B C : Finset ℤ) (hBC : Disjoint B C) :
    (∑h∈posDiffs (B∪C),(crossCount B C h+crossCount C B h))=B.card*C.card := by
  have hc := crossStarts_card B C hBC
  simp only [crossStarts,Finset.card_sigma] at hc
  rw [Finset.union_comm C B] at hc
  simpa only [Finset.sum_add_distrib,crossCount] using hc

theorem r_union (B C : Finset ℤ) (hBC : Disjoint B C) (h : ℤ) :
    r (B∪C) h=r B h+r C h+crossCount B C h+crossCount C B h := by
  have hd := Finset.disjoint_left.mp hBC
  have hset : positiveFiber (B∪C) h=
      (positiveFiber B h∪crossFiber B C h)∪(positiveFiber C h∪crossFiber C B h) := by
    ext u
    simp only [mem_positiveFiber,Finset.mem_union,mem_crossFiber]
    tauto
  have h1 : Disjoint (positiveFiber B h) (crossFiber B C h) := by
    apply Finset.disjoint_left.mpr
    intro u hu hv
    exact hd ((mem_positiveFiber B h u).mp hu).2 ((mem_crossFiber B C h u).mp hv).2
  have h2 : Disjoint (positiveFiber C h) (crossFiber C B h) := by
    apply Finset.disjoint_left.mpr
    intro u hu hv
    exact hd ((mem_crossFiber C B h u).mp hv).2 ((mem_positiveFiber C h u).mp hu).2
  have h3 : Disjoint (positiveFiber B h∪crossFiber B C h)
      (positiveFiber C h∪crossFiber C B h) := by
    apply Finset.disjoint_left.mpr
    intro u hu hv
    simp only [Finset.mem_union,mem_positiveFiber,mem_crossFiber] at hu hv
    rcases hu with hu|hu <;> rcases hv with hv|hv <;> exact hd hu.1 hv.1
  unfold r crossCount
  rw [hset,Finset.card_union_of_disjoint h3,Finset.card_union_of_disjoint h1,
    Finset.card_union_of_disjoint h2]
  omega

theorem golomb_r_le_one (A : Finset ℤ) (hA : Golomb (·∈A)) (h : ℤ) (hh:0<h) :
    r A h≤1 := by
  apply Finset.card_le_one.mpr
  intro u hu v hv
  have hu' := (mem_positiveFiber A h u).mp hu
  have hv' := (mem_positiveFiber A h v).mp hv
  exact (hA u (u+h) v (v+h) hu'.1 hu'.2 hv'.1 hv'.2 (by omega) (by omega) (by omega)).1

theorem golomb_r_indicator (A : Finset ℤ) (hA : Golomb (·∈A)) (h : ℤ) (hh:0<h) :
    r A h=if h∈posDiffs A then 1 else 0 := by
  split_ifs with hm
  · have hup := golomb_r_le_one A hA h hh
    obtain ⟨_,u,hu,huh⟩ := (mem_posDiffs A h).mp hm
    have hlo : 0<r A h := Finset.card_pos.mpr ⟨u,(mem_positiveFiber A h u).mpr ⟨hu,huh⟩⟩
    omega
  · exact r_eq_zero_of_not_mem_posDiffs A h hh hm

theorem posDiffs_mono {A S : Finset ℤ} (hAS:A⊆S) : posDiffs A⊆posDiffs S := by
  intro h hh
  obtain ⟨hp,u,hu,huh⟩ := (mem_posDiffs A h).mp hh
  exact (mem_posDiffs S h).mpr ⟨hp,u,hAS hu,hAS huh⟩

theorem sum_r_on_superset (A S : Finset ℤ) (hAS:A⊆S) :
    ∑h∈posDiffs S,r A h=M A := by
  rw [← sum_r A]
  symm
  apply Finset.sum_subset (posDiffs_mono hAS)
  intro h hh hn
  exact r_eq_zero_of_not_mem_posDiffs A h ((mem_posDiffs S h).mp hh).1 hn

theorem rho_le_M_left (B C : Finset ℤ) (hB : Golomb (·∈B)) : rho B C≤M B := by
  have hsum : (posDiffs B).card=M B := by
    rw [← sum_r B]
    have hh : (∑h∈posDiffs B,r B h)=∑_h∈posDiffs B,1 := by
      apply Finset.sum_congr rfl
      intro h hh
      rw [golomb_r_indicator B hB h ((mem_posDiffs B h).mp hh).1,if_pos hh]
    simpa using hh.symm
  rw [← hsum]
  exact Finset.card_le_card Finset.inter_subset_left

theorem rho_le_M_right (B C : Finset ℤ) (hC : Golomb (·∈C)) : rho B C≤M C := by
  have h := rho_le_M_left C B hC
  simpa only [rho,Finset.inter_comm] using h

theorem two_rho_le_U (B C : Finset ℤ) (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    2*rho B C≤M B+M C := by
  have h1 := rho_le_M_left B C hB
  have h2 := rho_le_M_right B C hC
  omega

def Ncross (B C : Finset ℤ) : ℕ :=
  ∑h∈posDiffs (B∪C),(r B h+r C h)*(crossCount B C h+crossCount C B h)

theorem shared_internal_count (B C : Finset ℤ)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    (∑h∈posDiffs (B∪C),r B h*r C h)=rho B C := by
  have hh : (∑h∈posDiffs (B∪C),r B h*r C h)=
      ∑h∈posDiffs (B∪C),if h∈posDiffs B∩posDiffs C then 1 else 0 := by
    apply Finset.sum_congr rfl
    intro h hh
    have hp := ((mem_posDiffs (B∪C) h).mp hh).1
    rw [golomb_r_indicator B hB h hp,golomb_r_indicator C hC h hp]
    simp only [Finset.mem_inter]
    split_ifs <;> simp_all
  rw [hh,Finset.sum_boole]
  have hf : (posDiffs (B∪C)).filter (·∈posDiffs B∩posDiffs C)=posDiffs B∩posDiffs C := by
    ext h
    simp only [Finset.mem_filter]
    constructor
    · exact And.right
    · intro hh
      exact ⟨posDiffs_mono Finset.subset_union_left (Finset.mem_inter.mp hh).1,hh⟩
  rw [hf]
  rfl

theorem choose_four_parts (a b x y : ℕ) (ha:a≤1) (hb:b≤1) :
    (a+b+x+y).choose 2=a*b+x.choose 2+y.choose 2+(a+b)*(x+y)+x*y := by
  have hs := square_eq_self_add_twice_choose (a+b+x+y)
  have hx := square_eq_self_add_twice_choose x
  have hy := square_eq_self_add_twice_choose y
  interval_cases a <;> interval_cases b <;> norm_num at * <;> nlinarith

theorem two_golomb_corner_identity (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    T (B∪C)=2*rho B C+Ncross B C+Q B C := by
  rw [corner_count]
  have he : (∑h∈posDiffs (B∪C),(r (B∪C) h).choose 2)=
      ∑h∈posDiffs (B∪C),(r B h*r C h+
        ((crossCount B C h).choose 2+(crossCount C B h).choose 2)+
        (r B h+r C h)*(crossCount B C h+crossCount C B h)+crossCount B C h*crossCount C B h) := by
    apply Finset.sum_congr rfl
    intro h hh
    have hp := ((mem_posDiffs (B∪C) h).mp hh).1
    rw [r_union B C hBC h]
    have hc := choose_four_parts (r B h) (r C h) (crossCount B C h) (crossCount C B h)
      (golomb_r_le_one B hB h hp) (golomb_r_le_one C hC h hp)
    omega
  rw [he]
  simp only [Finset.sum_add_distrib]
  rw [shared_internal_count B C hB hC]
  have hcol := collision_sum_identity B C hBC hB hC
  rw [Finset.sum_add_distrib] at hcol
  unfold Ncross Q
  omega

theorem Ncross_le_twice_cross_mass (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) : Ncross B C≤2*(B.card*C.card) := by
  rw [← cross_mass B C hBC,Finset.mul_sum]
  apply Finset.sum_le_sum
  intro h hh
  have hp := ((mem_posDiffs (B∪C) h).mp hh).1
  exact Nat.mul_le_mul_right _ (by
    have hb := golomb_r_le_one B hB h hp
    have hc := golomb_r_le_one C hC h hp
    omega)

theorem M_union (B C : Finset ℤ) (hBC : Disjoint B C) :
    M (B∪C)=M B+M C+B.card*C.card := by
  have hu := square_eq_self_add_twice_choose (B∪C).card
  have hb := square_eq_self_add_twice_choose B.card
  have hc := square_eq_self_add_twice_choose C.card
  rw [Finset.card_union_of_disjoint hBC] at hu
  unfold M
  rw [Finset.card_union_of_disjoint hBC]
  nlinarith

theorem two_golomb_T_le_twice_M (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) : T (B∪C)≤2*M (B∪C) := by
  have ht := two_golomb_corner_identity B C hBC hB hC
  have hr := two_rho_le_U B C hB hC
  have hn := Ncross_le_twice_cross_mass B C hBC hB hC
  have hq := Q_le_U B C hB hC
  have hm := M_union B C hBC
  omega

theorem count_le_one_add_choose (n : ℕ) : n≤1+n.choose 2 := by
  rcases n with _|_|n
  · simp
  · simp
  · have h := square_eq_self_add_twice_choose (n+2)
    nlinarith

theorem Ncross_pointwise (a b x y : ℕ) (ha:a≤1) (hb:b≤1) :
    (a+b)*(x+y)≤(x+y)+2*(a*b)+(x.choose 2+y.choose 2) := by
  have hx := count_le_one_add_choose x
  have hy := count_le_one_add_choose y
  interval_cases a <;> interval_cases b <;> norm_num at * <;> omega

theorem Ncross_le_cross_mass_add_rho (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    Ncross B C≤B.card*C.card+3*rho B C := by
  have hp : Ncross B C≤∑h∈posDiffs (B∪C),(
      (crossCount B C h+crossCount C B h)+2*(r B h*r C h)+
      ((crossCount B C h).choose 2+(crossCount C B h).choose 2)) := by
    apply Finset.sum_le_sum
    intro h hh
    have hpos := ((mem_posDiffs (B∪C) h).mp hh).1
    exact Ncross_pointwise _ _ _ _ (golomb_r_le_one B hB h hpos) (golomb_r_le_one C hC h hpos)
  rw [Finset.sum_add_distrib,Finset.sum_add_distrib,← Finset.mul_sum,
    cross_mass B C hBC,shared_internal_count B C hB hC,collision_sum_identity B C hBC hB hC] at hp
  omega

theorem two_golomb_T_le_M_add_rho (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    T (B∪C)≤M (B∪C)+5*rho B C := by
  have ht := two_golomb_corner_identity B C hBC hB hC
  have hn := Ncross_le_cross_mass_add_rho B C hBC hB hC
  have hq := Q_le_U B C hB hC
  have hm := M_union B C hBC
  omega

theorem two_golomb_energy_bound (B C : Finset ℤ) (hBC : Disjoint B C)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) :
    E (B∪C)≤6*(B.card+C.card)^2-5*(B.card+C.card) := by
  have ht := two_golomb_T_le_twice_M B C hBC hB hC
  have he := energy_corner_identity (B∪C)
  have hn := square_eq_self_add_twice_choose (B∪C).card
  change (B∪C).card^2=(B∪C).card+2*M (B∪C) at hn
  rw [Finset.card_union_of_disjoint hBC] at he hn
  omega

end EnergyForcing.Counting

