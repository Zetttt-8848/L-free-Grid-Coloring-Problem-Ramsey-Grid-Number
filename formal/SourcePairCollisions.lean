import SourceCounting

set_option autoImplicit false

namespace EnergyForcing.PairCollisions

open Finset
open scoped BigOperators
open EnergyForcing.Counting

def NoProgression (A : Finset ℤ) : Prop :=
  ∀a∈A, ∀b∈A, ∀c∈A, a+c=b+b → a=b

/-- Two disjoint unordered pairs of marks with the same sum. -/
def collisions (A : Finset ℤ) : Finset (Finset (Finset ℤ)) :=
  ((A.powersetCard 2).powersetCard 2).filter fun C =>
    (C.biUnion id).card=4 ∧ ∀P∈C, ∀Q∈C, (∑x∈P, x)=∑x∈Q, x

def flipCorner (q : ℤ×ℤ×ℤ) : ℤ×ℤ×ℤ := (q.2.1+q.2.2-q.1,q.2.1,q.2.2)

def cornerCollision (q : ℤ×ℤ×ℤ) : Finset (Finset ℤ) :=
  {{q.1,q.2.1+q.2.2-q.1},{q.2.1,q.2.2}}

theorem collision_of_four (A : Finset ℤ) (x y z w : ℤ)
    (hx : x∈A) (hy : y∈A) (hz : z∈A) (hw : w∈A)
    (hyx : y<x) (hxz : x<z) (hyw : y<w) (hwz : w<z) (hxw : x≠w)
    (he : x+w=y+z) : {{x,w},{y,z}}∈collisions A := by
  have hyz : y≠z := by omega
  have hp : ({x,w}:Finset ℤ)≠{y,z} := by
    intro hh
    have hh' : y∈({x,w}:Finset ℤ) := by rw [hh]; simp
    simp only [Finset.mem_insert,Finset.mem_singleton] at hh'
    omega
  have hdis : Disjoint ({x,w}:Finset ℤ) {y,z} := by
    apply Finset.disjoint_left.mpr
    intro a ha hb
    simp only [Finset.mem_insert,Finset.mem_singleton] at ha hb
    omega
  have hP : ({x,w}:Finset ℤ)∈A.powersetCard 2 := by
    simp [Finset.mem_powersetCard,Finset.subset_iff,hx,hw,hxw]
  have hQ : ({y,z}:Finset ℤ)∈A.powersetCard 2 := by
    simp [Finset.mem_powersetCard,Finset.subset_iff,hy,hz,hyz]
  unfold collisions
  apply Finset.mem_filter.mpr
  refine ⟨?_,?_,?_⟩
  · apply Finset.mem_powersetCard.mpr
    refine ⟨?_,by simp [hp]⟩
    intro P hmem
    simp only [Finset.mem_insert,Finset.mem_singleton] at hmem
    rcases hmem with rfl | rfl
    · exact hP
    · exact hQ
  · simp only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq]
    rw [Finset.card_union_of_disjoint hdis]
    simp [hxw,hyz]
  · intro P hP Q hQ
    simp only [Finset.mem_insert,Finset.mem_singleton] at hP hQ
    rcases hP with rfl | rfl <;> rcases hQ with rfl | rfl <;>
      simp only [Finset.sum_pair hxw,Finset.sum_pair hyz] <;> omega

theorem corner_four_distinct (A : Finset ℤ) (hA : NoProgression A)
    (q : ℤ×ℤ×ℤ) (hq : q∈sourceCorners A) : q.1≠q.2.1+q.2.2-q.1 := by
  rcases q with ⟨x,y,z⟩
  rcases (mem_sourceCorners A x y z).mp hq with ⟨hx,hy,hz,hyx,hxz,hw⟩
  intro he
  have hh := hA y hy x hx z hz (by dsimp at he; omega)
  omega

theorem cornerCollision_mem (A : Finset ℤ) (hA : NoProgression A)
    (q : ℤ×ℤ×ℤ) (hq : q∈sourceCorners A) : cornerCollision q∈collisions A := by
  rcases q with ⟨x,y,z⟩
  have hn := corner_four_distinct A hA (x,y,z) hq
  rcases (mem_sourceCorners A x y z).mp hq with ⟨hx,hy,hz,hyx,hxz,hw⟩
  exact collision_of_four A x y z (y+z-x) hx hy hz hw hyx hxz (by omega) (by omega) hn (by ring)

theorem flipCorner_mem (A : Finset ℤ) (q : ℤ×ℤ×ℤ) (hq : q∈sourceCorners A) :
    flipCorner q∈sourceCorners A := by
  rcases q with ⟨x,y,z⟩
  rcases (mem_sourceCorners A x y z).mp hq with ⟨hx,hy,hz,hyx,hxz,hw⟩
  simp only [flipCorner,mem_sourceCorners]
  refine ⟨hw,hy,hz,by omega,by omega,?_⟩
  convert hx using 1 <;> ring

theorem flipCorner_collision (q : ℤ×ℤ×ℤ) :
    cornerCollision (flipCorner q)=cornerCollision q := by
  rcases q with ⟨x,y,z⟩
  simp only [cornerCollision,flipCorner]
  rw [show y+z-(y+z-x)=x by ring,Finset.pair_comm (y+z-x) x]

theorem mem_cornerCollision_union (q : ℤ×ℤ×ℤ) (a : ℤ) :
    a∈(cornerCollision q).biUnion id ↔
      a=q.1 ∨ a=q.2.1+q.2.2-q.1 ∨ a=q.2.1 ∨ a=q.2.2 := by
  simp [cornerCollision,or_assoc,or_comm,or_left_comm]

/-- A collision fixes its outer endpoints and allows exactly the two middle marks. -/
theorem cornerCollision_eq_iff (A : Finset ℤ) (q p : ℤ×ℤ×ℤ)
    (hq : q∈sourceCorners A) (hp : p∈sourceCorners A) :
    cornerCollision p=cornerCollision q ↔ p=q ∨ p=flipCorner q := by
  rcases q with ⟨x,y,z⟩
  rcases p with ⟨u,v,w⟩
  have hq' := (mem_sourceCorners A x y z).mp hq
  have hp' := (mem_sourceCorners A u v w).mp hp
  constructor
  · intro he
    have hset := congrArg (fun C : Finset (Finset ℤ) => C.biUnion id) he
    dsimp at hset
    have hv : v∈(cornerCollision (x,y,z)).biUnion id := by
      rw [← hset,mem_cornerCollision_union]
      exact Or.inr (Or.inr (Or.inl rfl))
    have hy : y∈(cornerCollision (u,v,w)).biUnion id := by
      rw [hset,mem_cornerCollision_union]
      exact Or.inr (Or.inr (Or.inl rfl))
    have hw : w∈(cornerCollision (x,y,z)).biUnion id := by
      rw [← hset,mem_cornerCollision_union]
      exact Or.inr (Or.inr (Or.inr rfl))
    have hz : z∈(cornerCollision (u,v,w)).biUnion id := by
      rw [hset,mem_cornerCollision_union]
      exact Or.inr (Or.inr (Or.inr rfl))
    have hu : u∈(cornerCollision (x,y,z)).biUnion id := by
      rw [← hset,mem_cornerCollision_union]
      exact Or.inl rfl
    simp only [mem_cornerCollision_union] at hv hy hw hz hu
    have hvy : v=y := by dsimp at *; omega
    have hwz : w=z := by dsimp at *; omega
    subst v
    subst w
    have hu' : u=x ∨ u=y+z-x := by dsimp at *; omega
    rcases hu' with rfl | rfl
    · exact Or.inl rfl
    · exact Or.inr rfl
  · rintro (he | he)
    · exact congrArg cornerCollision he
    · rw [he]
      exact flipCorner_collision _

theorem cornerCollision_fiber_card (A : Finset ℤ) (hA : NoProgression A)
    (q : ℤ×ℤ×ℤ) (hq : q∈sourceCorners A) :
    ((sourceCorners A).filter fun p => cornerCollision p=cornerCollision q).card=2 := by
  have he : ((sourceCorners A).filter fun p => cornerCollision p=cornerCollision q)=
      {q,flipCorner q} := by
    ext p
    simp only [Finset.mem_filter,Finset.mem_insert,Finset.mem_singleton]
    constructor
    · rintro ⟨hp,he⟩
      exact (cornerCollision_eq_iff A q p hq hp).mp he
    · rintro (rfl | rfl)
      · exact ⟨hq,rfl⟩
      · exact ⟨flipCorner_mem A q hq,flipCorner_collision q⟩
  rw [he]
  have hne : q≠flipCorner q := by
    intro h
    have hh := congrArg Prod.fst h
    exact corner_four_distinct A hA q hq hh
  simp [hne]

theorem ordered_pair_of_card_two (P : Finset ℤ) (hP : P.card=2) :
    ∃a b : ℤ, a<b ∧ P={a,b} := by
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hP
  by_cases h : a<b
  · exact ⟨a,b,h,rfl⟩
  · exact ⟨b,a,by omega,Finset.pair_comm _ _⟩

theorem collision_has_corner (A : Finset ℤ) (C : Finset (Finset ℤ))
    (hC : C∈collisions A) : ∃q∈sourceCorners A, cornerCollision q=C := by
  rcases Finset.mem_filter.mp hC with ⟨hC,hunion,hsum⟩
  rcases Finset.mem_powersetCard.mp hC with ⟨hsub,hcard⟩
  obtain ⟨P,Q,hPQ,rfl⟩ := Finset.card_eq_two.mp hcard
  have hP : P∈A.powersetCard 2 := hsub (by simp)
  have hQ : Q∈A.powersetCard 2 := hsub (by simp)
  rcases Finset.mem_powersetCard.mp hP with ⟨hPA,hPc⟩
  rcases Finset.mem_powersetCard.mp hQ with ⟨hQA,hQc⟩
  obtain ⟨a,b,hab,rfl⟩ := ordered_pair_of_card_two P hPc
  obtain ⟨c,d,hcd,rfl⟩ := ordered_pair_of_card_two Q hQc
  have ha : a∈A := hPA (by simp)
  have hb : b∈A := hPA (by simp)
  have hc : c∈A := hQA (by simp)
  have hd : d∈A := hQA (by simp)
  have he : a+b=c+d := by
    have hh := hsum {a,b} (by simp) {c,d} (by simp)
    simpa [ne_of_lt hab,ne_of_lt hcd] using hh
  have huni : (({a,b}:Finset ℤ)∪{c,d}).card=4 := by
    simpa only [Finset.biUnion_insert,Finset.singleton_biUnion,id_eq] using hunion
  have hcardinter := Finset.card_union_add_card_inter ({a,b}:Finset ℤ) {c,d}
  rw [huni,hPc,hQc] at hcardinter
  have hdis : Disjoint ({a,b}:Finset ℤ) {c,d} :=
    Finset.disjoint_iff_inter_eq_empty.mpr (Finset.card_eq_zero.mp (by omega))
  have hac : a≠c := by
    intro hh
    subst c
    exact (Finset.disjoint_left.mp hdis) (show a∈({a,b}:Finset ℤ) by simp) (by simp)
  by_cases hac' : a<c
  · refine ⟨(c,a,b),?_,?_⟩
    · apply (mem_sourceCorners A c a b).mpr
      refine ⟨hc,ha,hb,hac',by omega,?_⟩
      convert hd using 1 <;> omega
    · simp only [cornerCollision]
      rw [show a+b-c=d by omega,Finset.pair_comm ({c,d}:Finset ℤ) {a,b}]
  · refine ⟨(a,c,d),?_,?_⟩
    · apply (mem_sourceCorners A a c d).mpr
      refine ⟨ha,hc,hd,by omega,by omega,?_⟩
      convert hb using 1 <;> omega
    · simp only [cornerCollision]
      rw [show c+d-a=b by omega]

/-- The actual corner cardinality equals twice the unordered four-mark collision count. -/
theorem corner_count_no_progression (A : Finset ℤ) (hA : NoProgression A) :
    T A=2*(collisions A).card := by
  have hh := Finset.card_eq_sum_card_fiberwise (s:=sourceCorners A) (t:=collisions A)
    (f:=cornerCollision) (fun q hq => cornerCollision_mem A hA q hq)
  change T A=_ at hh
  rw [hh]
  calc
    _ = ∑C∈collisions A, 2 := by
      apply Finset.sum_congr rfl
      intro C hC
      obtain ⟨q,hq,hqc⟩ := collision_has_corner A C hC
      rw [← hqc]
      exact cornerCollision_fiber_card A hA q hq
    _ = _ := by simp [Nat.mul_comm]

end EnergyForcing.PairCollisions



namespace EnergyForcing.PairCollisions

open Finset
open scoped BigOperators
open EnergyForcing.Counting

def sumPairs (A : Finset ℤ) (s : ℤ) : Finset (Finset ℤ) :=
  (A.powersetCard 2).filter fun P => (∑x∈P, x)=s

theorem collision_card_le_pairs (A : Finset ℤ)
    (hcap : ∀s, (sumPairs A s).card ≤ 3) : (collisions A).card ≤ M A := by
  let keys := (A.powersetCard 2).image fun P => ∑x∈P, x
  have hsub : collisions A ⊆ keys.biUnion (fun s => (sumPairs A s).powersetCard 2) := by
    intro C hC
    rcases Finset.mem_filter.mp hC with ⟨hC,h4,hsum⟩
    rcases Finset.mem_powersetCard.mp hC with ⟨hsub,hcard⟩
    obtain ⟨P,Q,hPQ,hCeq⟩ := Finset.card_eq_two.mp hcard
    have hPC : P∈C := by rw [hCeq]; simp
    apply Finset.mem_biUnion.mpr
    refine ⟨∑x∈P, x,Finset.mem_image.mpr ⟨P,hsub hPC,rfl⟩,?_⟩
    apply Finset.mem_powersetCard.mpr
    refine ⟨?_,hcard⟩
    intro R hR
    exact Finset.mem_filter.mpr ⟨hsub hR,hsum R hR P hPC⟩
  calc
    (collisions A).card ≤ (keys.biUnion (fun s => (sumPairs A s).powersetCard 2)).card :=
      Finset.card_le_card hsub
    _ ≤ ∑s∈keys, ((sumPairs A s).powersetCard 2).card := Finset.card_biUnion_le
    _ ≤ ∑s∈keys, (sumPairs A s).card := by
      apply Finset.sum_le_sum
      intro s hs
      rw [Finset.card_powersetCard]
      have h := hcap s
      interval_cases hh : (sumPairs A s).card <;> norm_num
    _ = M A := by
      have he := Finset.card_eq_sum_card_image (fun P : Finset ℤ => ∑x∈P, x) (A.powersetCard 2)
      simpa only [sumPairs,Finset.card_powersetCard,M,keys] using he.symm

theorem pair_sum_cap_bound (A : Finset ℤ) (hA : NoProgression A)
    (hcap : ∀s, (sumPairs A s).card ≤ 3) : T A ≤ 2*M A := by
  rw [corner_count_no_progression A hA]
  exact Nat.mul_le_mul_left 2 (collision_card_le_pairs A hcap)

end EnergyForcing.PairCollisions

namespace EnergyForcing.PairCollisions
open Finset
open scoped BigOperators

theorem equal_sum_pairs_disjoint (P Q : Finset ℤ) (hP : P.card=2) (hQ : Q.card=2)
    (hne : P≠Q) (he : (∑x∈P,x)=∑x∈Q,x) : Disjoint P Q := by
  apply Finset.disjoint_left.mpr
  intro a ha hb
  obtain ⟨u,v,huv,hPe⟩ := Finset.card_eq_two.mp hP
  obtain ⟨w,z,hwz,hQe⟩ := Finset.card_eq_two.mp hQ
  subst P; subst Q
  simp only [Finset.mem_insert,Finset.mem_singleton] at ha hb
  simp only [Finset.sum_pair huv,Finset.sum_pair hwz] at he
  rcases ha with rfl | rfl
  · rcases hb with hh | hh
    · subst w
      have hv : v=z := by omega
      exact hne (by simp [hv])
    · subst z
      have hv : v=w := by omega
      exact hne (by simp [hv,Finset.pair_comm])
  · rcases hb with hh | hh
    · subst w
      have hu : u=z := by omega
      exact hne (by simp [hu,Finset.pair_comm])
    · subst z
      have hu : u=w := by omega
      exact hne (by simp [hu])
end EnergyForcing.PairCollisions

