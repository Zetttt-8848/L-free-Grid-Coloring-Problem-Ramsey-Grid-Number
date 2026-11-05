import ThreeCubeNine

set_option maxHeartbeats 4000000

namespace EnergyForcing.ThreeCube

open EnergyForcing.Counting

def orderedMixedCollisions (A : Finset ℤ) (z : Point → Bool) :
    Finset ((ℤ×ℤ)×(ℤ×ℤ)) :=
  (energySet A).filter fun p => p.1.1≠p.1.2 ∧ z p.1≠z p.2

@[simp] theorem mem_orderedMixedCollisions (A : Finset ℤ) (z : Point → Bool)
    (a b c d : ℤ) : ((a,b),(c,d))∈orderedMixedCollisions A z ↔
      a∈A ∧ b∈A ∧ c∈A ∧ d∈A ∧ a-b=c-d ∧ a≠b ∧ z (a,b)≠z (c,d) := by
  simp [orderedMixedCollisions,mem_energySet,and_assoc]

@[simp] theorem mem_mixedCorners (A : Finset ℤ) (z : Point → Bool) (x y w : ℤ) :
    (x,y,w)∈mixedCorners A z ↔ x∈A ∧ y∈A ∧ w∈A ∧ y<x ∧ x<w ∧
      y+w-x∈A ∧ z (x,y)≠z (w,y+w-x) := by
  simp [mixedCorners,mem_sourceCorners,and_assoc]

def fourfold (p : (ℤ×ℤ×ℤ)×(Bool×Bool)) : (ℤ×ℤ)×(ℤ×ℤ) :=
  let first : Point := (p.1.1,p.1.2.1)
  let second : Point := (p.1.2.2,p.1.2.1+p.1.2.2-p.1.1)
  let first' := if p.2.2 then first.swap else first
  let second' := if p.2.2 then second.swap else second
  if p.2.1 then (second',first') else (first',second')

theorem fourfold_mem (A : Finset ℤ) (z : Point → Bool)
    (hsym : ∀ x y, z (x,y)=z (y,x))
    (p : (ℤ×ℤ×ℤ)×(Bool×Bool))
    (hp : p∈(mixedCorners A z).product Finset.univ) :
    fourfold p∈orderedMixedCollisions A z := by
  rcases p with ⟨⟨x,y,w⟩,b,c⟩
  rcases (mem_mixedCorners A z x y w).mp (Finset.mem_product.mp hp).1 with
    ⟨hx,hy,hw,hyx,hxw,ht,hne⟩
  have hrev : z (y,x)≠z (y+w-x,w) := by
    rw [hsym y x,hsym (y+w-x) w]
    exact hne
  cases b <;> cases c <;> simp only [fourfold,Bool.false_eq_true,if_false,if_true]
  · exact (mem_orderedMixedCollisions A z x y w (y+w-x)).mpr
      ⟨hx,hy,hw,ht,by omega,by omega,hne⟩
  · exact (mem_orderedMixedCollisions A z y x (y+w-x) w).mpr
      ⟨hy,hx,ht,hw,by omega,by omega,hrev⟩
  · exact (mem_orderedMixedCollisions A z w (y+w-x) x y).mpr
      ⟨hw,ht,hx,hy,by omega,by omega,hne.symm⟩
  · exact (mem_orderedMixedCollisions A z (y+w-x) w y x).mpr
      ⟨ht,hw,hy,hx,by omega,by omega,hrev.symm⟩

theorem fourfold_injective (A : Finset ℤ) (z : Point → Bool) :
    Set.InjOn fourfold (↑((mixedCorners A z).product (Finset.univ : Finset (Bool×Bool))) :
      Set ((ℤ×ℤ×ℤ)×(Bool×Bool))) := by
  rintro ⟨⟨x,y,w⟩,b,c⟩ hp ⟨⟨x',y',w'⟩,b',c'⟩ hq he
  have h := (mem_mixedCorners A z x y w).mp (Finset.mem_product.mp hp).1
  have h' := (mem_mixedCorners A z x' y' w').mp (Finset.mem_product.mp hq).1
  cases b <;> cases c <;> cases b' <;> cases c' <;>
    simp only [fourfold,Bool.false_eq_true,if_false,if_true,Prod.swap,Prod.mk.injEq] at he ⊢ <;>
    simp_all <;> omega

theorem fourfold_surjective (A : Finset ℤ) (z : Point → Bool)
    (hsym : ∀ x y, z (x,y)=z (y,x)) :
    Set.SurjOn fourfold
      (↑((mixedCorners A z).product (Finset.univ : Finset (Bool×Bool))) :
        Set ((ℤ×ℤ×ℤ)×(Bool×Bool)))
      (↑(orderedMixedCollisions A z) : Set ((ℤ×ℤ)×(ℤ×ℤ))) := by
  rintro ⟨⟨a,b⟩,c,d⟩ hq
  rcases (mem_orderedMixedCollisions A z a b c d).mp hq with
    ⟨ha,hb,hc,hd,hdiff,hab,hne⟩
  have hbd : b≠d := by
    intro he
    have he' : a=c := by omega
    apply hne
    simp only [he,he']
  have hac : a≠c := by intro he; exact hbd (by omega)
  by_cases hpos : b<a
  · by_cases horder : b<d
    · have ht : b+c-a=d := by omega
      have hp : (a,b,c)∈mixedCorners A z :=
        (mem_mixedCorners A z a b c).mpr
          ⟨ha,hb,hc,hpos,by omega,by simpa only [ht] using hd,by simpa only [ht] using hne⟩
      refine ⟨((a,b,c),(false,false)),Finset.mem_product.mpr ⟨hp,Finset.mem_univ _⟩,?_⟩
      simp [fourfold,ht]
    · have ht : d+a-c=b := by omega
      have hp : (c,d,a)∈mixedCorners A z :=
        (mem_mixedCorners A z c d a).mpr
          ⟨hc,hd,ha,by omega,by omega,by simpa only [ht] using hb,by simpa only [ht] using hne.symm⟩
      refine ⟨((c,d,a),(true,false)),Finset.mem_product.mpr ⟨hp,Finset.mem_univ _⟩,?_⟩
      simp [fourfold,ht]
  · have hrev : z (b,a)≠z (d,c) := by rw [hsym b a,hsym d c]; exact hne
    by_cases horder : a<c
    · have ht : a+d-b=c := by omega
      have hp : (b,a,d)∈mixedCorners A z :=
        (mem_mixedCorners A z b a d).mpr
          ⟨hb,ha,hd,by omega,by omega,by simpa only [ht] using hc,by simpa only [ht] using hrev⟩
      refine ⟨((b,a,d),(false,true)),Finset.mem_product.mpr ⟨hp,Finset.mem_univ _⟩,?_⟩
      simp [fourfold,ht]
    · have ht : c+b-d=a := by omega
      have hp : (d,c,b)∈mixedCorners A z :=
        (mem_mixedCorners A z d c b).mpr
          ⟨hd,hc,hb,by omega,by omega,by simpa only [ht] using ha,by simpa only [ht] using hrev.symm⟩
      refine ⟨((d,c,b),(true,true)),Finset.mem_product.mpr ⟨hp,Finset.mem_univ _⟩,?_⟩
      simp [fourfold,ht]

/-- Every mixed corner has precisely four ordered signed-difference representations. -/
theorem ordered_mixed_fourfold (A : Finset ℤ) (z : Point → Bool)
    (hsym : ∀ x y, z (x,y)=z (y,x)) :
    (orderedMixedCollisions A z).card=4*mixedCount A z := by
  have h := Finset.card_nbij fourfold (fourfold_mem A z hsym)
    (fourfold_injective A z) (fourfold_surjective A z hsym)
  have hc : ((mixedCorners A z).product (Finset.univ : Finset (Bool×Bool))).card=
      4*mixedCount A z := by simp [mixedCount,Finset.card_product,Nat.mul_comm]
  omega

#print axioms ordered_mixed_fourfold

end EnergyForcing.ThreeCube
