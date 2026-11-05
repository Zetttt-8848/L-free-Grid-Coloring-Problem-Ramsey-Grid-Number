import EnergyMomentLower

set_option autoImplicit false

namespace EnergyForcing.Counting

def scaledSum (B C : Finset ℤ) (Q : ℤ) : Finset ℤ :=
  (B.product C).image fun p => p.1+Q*p.2

@[simp] theorem mem_scaledSum (B C : Finset ℤ) (Q x : ℤ) :
    x∈scaledSum B C Q ↔ ∃b∈B,∃c∈C,b+Q*c=x := by
  simp only [scaledSum,Finset.mem_image,Finset.product_eq_sprod,Finset.mem_product]
  constructor
  · rintro ⟨⟨b,c⟩,⟨hb,hc⟩,he⟩
    exact ⟨b,hb,c,hc,he⟩
  · rintro ⟨b,hb,c,hc,he⟩
    exact ⟨(b,c),⟨hb,hc⟩,he⟩

theorem mark_difference_bounds (B : Finset ℤ) (a b : ℤ) (ha:a∈B) (hb:b∈B) :
    -(span B:ℤ)≤a-b ∧ a-b≤(span B:ℤ) := by
  have hB : B.Nonempty := ⟨a,ha⟩
  have hamin := Finset.min'_le B a ha
  have hamax := Finset.le_max' B a ha
  have hbmin := Finset.min'_le B b hb
  have hbmax := Finset.le_max' B b hb
  have hs := span_cast B hB
  omega

theorem separated_difference_unique (B : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q)
    (a b c d k l : ℤ) (ha:a∈B) (hb:b∈B) (hc:c∈B) (hd:d∈B)
    (he:a-b+Q*k=c-d+Q*l) : a-b=c-d ∧ k=l := by
  have h1 := mark_difference_bounds B a b ha hb
  have h2 := mark_difference_bounds B c d hc hd
  have hQpos : 0<Q := by omega
  have hkl : k=l := by
    by_contra hn
    rcases lt_or_gt_of_ne hn with hk|hl
    · have hm := mul_nonneg (le_of_lt hQpos) (show 0≤l-k-1 by omega)
      nlinarith
    · have hm := mul_nonneg (le_of_lt hQpos) (show 0≤k-l-1 by omega)
      nlinarith
  constructor
  · rw [hkl] at he; omega
  · exact hkl

theorem separated_mark_unique (B : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q)
    (a b k l : ℤ) (ha:a∈B) (hb:b∈B) (he:a+Q*k=b+Q*l) : a=b ∧ k=l := by
  have hh := separated_difference_unique B Q hQ a b a a (k-l) 0 ha hb ha ha (by nlinarith)
  omega

theorem scaledSum_card (B C : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q) :
    (scaledSum B C Q).card=B.card*C.card := by
  unfold scaledSum
  rw [Finset.card_image_iff.mpr,Finset.product_eq_sprod,Finset.card_product]
  rintro ⟨a,k⟩ hp ⟨b,l⟩ hq he
  have ha := Finset.mem_product.mp hp
  have hb := Finset.mem_product.mp hq
  have hh := separated_mark_unique B Q hQ a b k l ha.1 hb.1 he
  exact Prod.ext hh.1 hh.2

def energyProductMap (Q : ℤ)
    (p : (((ℤ×ℤ)×(ℤ×ℤ))×((ℤ×ℤ)×(ℤ×ℤ)))) : (ℤ×ℤ)×(ℤ×ℤ) :=
  ((p.1.1.1+Q*p.2.1.1,p.1.1.2+Q*p.2.1.2),
    (p.1.2.1+Q*p.2.2.1,p.1.2.2+Q*p.2.2.2))

theorem separated_energy_product (B C : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q) :
    E (scaledSum B C Q)=E B*E C := by
  unfold E
  rw [← Finset.card_product]
  symm
  refine Finset.card_bij (fun p _ => energyProductMap Q p) ?_ ?_ ?_
  · rintro ⟨⟨⟨a,b⟩,⟨c,d⟩⟩,⟨⟨i,j⟩,⟨k,l⟩⟩⟩ hp
    obtain ⟨hpB,hpC⟩ := Finset.mem_product.mp hp
    rcases (mem_energySet B a b c d).mp hpB with ⟨ha,hb,hc,hd,heB⟩
    rcases (mem_energySet C i j k l).mp hpC with ⟨hi,hj,hk,hl,heC⟩
    apply (mem_energySet _ _ _ _ _).mpr
    refine ⟨(mem_scaledSum _ _ _ _).mpr ⟨a,ha,i,hi,rfl⟩,
      (mem_scaledSum _ _ _ _).mpr ⟨b,hb,j,hj,rfl⟩,
      (mem_scaledSum _ _ _ _).mpr ⟨c,hc,k,hk,rfl⟩,
      (mem_scaledSum _ _ _ _).mpr ⟨d,hd,l,hl,rfl⟩,?_⟩
    dsimp [energyProductMap]
    nlinarith
  · rintro ⟨⟨⟨a,b⟩,⟨c,d⟩⟩,⟨⟨i,j⟩,⟨k,l⟩⟩⟩ hp
      ⟨⟨⟨a',b'⟩,⟨c',d'⟩⟩,⟨⟨i',j'⟩,⟨k',l'⟩⟩⟩ hq he
    have hpB := (mem_energySet B a b c d).mp (Finset.mem_product.mp hp).1
    have hqB := (mem_energySet B a' b' c' d').mp (Finset.mem_product.mp hq).1
    simp only [energyProductMap,Prod.mk.injEq] at he
    have h1 := separated_mark_unique B Q hQ a a' i i' hpB.1 hqB.1 he.1.1
    have h2 := separated_mark_unique B Q hQ b b' j j' hpB.2.1 hqB.2.1 he.1.2
    have h3 := separated_mark_unique B Q hQ c c' k k' hpB.2.2.1 hqB.2.2.1 he.2.1
    have h4 := separated_mark_unique B Q hQ d d' l l' hpB.2.2.2.1 hqB.2.2.2.1 he.2.2
    rcases h1 with ⟨rfl,rfl⟩
    rcases h2 with ⟨rfl,rfl⟩
    rcases h3 with ⟨rfl,rfl⟩
    rcases h4 with ⟨rfl,rfl⟩
    rfl
  · rintro ⟨⟨x,y⟩,⟨z,w⟩⟩ hp
    rcases (mem_energySet _ x y z w).mp hp with ⟨hx,hy,hz,hw,he⟩
    obtain ⟨a,ha,i,hi,rfl⟩ := (mem_scaledSum B C Q x).mp hx
    obtain ⟨b,hb,j,hj,rfl⟩ := (mem_scaledSum B C Q y).mp hy
    obtain ⟨c,hc,k,hk,rfl⟩ := (mem_scaledSum B C Q z).mp hz
    obtain ⟨d,hd,l,hl,rfl⟩ := (mem_scaledSum B C Q w).mp hw
    have hh := separated_difference_unique B Q hQ a b c d (i-j) (k-l) ha hb hc hd (by nlinarith)
    refine ⟨(((a,b),(c,d)),((i,j),(k,l))),?_,rfl⟩
    exact Finset.mk_mem_product ((mem_energySet B a b c d).mpr ⟨ha,hb,hc,hd,hh.1⟩)
      ((mem_energySet C i j k l).mpr ⟨hi,hj,hk,hl,hh.2⟩)

theorem separated_scaled_fiber (B C : Finset ℤ) (Q d : ℤ) (hQ:2*(span B:ℤ)<Q) :
    positiveFiber (scaledSum B C Q) (Q*d)=scaledSum B (positiveFiber C d) Q := by
  ext u
  constructor
  · intro hu
    obtain ⟨hu,hu'⟩ := (mem_positiveFiber _ _ u).mp hu
    obtain ⟨b,hb,c,hc,he⟩ := (mem_scaledSum B C Q u).mp hu
    obtain ⟨b',hb',c',hc',he'⟩ := (mem_scaledSum B C Q (u+Q*d)).mp hu'
    have hh := separated_mark_unique B Q hQ b b' (c+d) c' hb hb' (by nlinarith)
    exact (mem_scaledSum _ _ _ _).mpr ⟨b,hb,c,(mem_positiveFiber C d c).mpr ⟨hc,hh.2 ▸ hc'⟩,he⟩
  · intro hu
    obtain ⟨b,hb,c,hc,he⟩ := (mem_scaledSum B _ Q u).mp hu
    have hc' := (mem_positiveFiber C d c).mp hc
    apply (mem_positiveFiber _ _ u).mpr
    exact ⟨(mem_scaledSum _ _ _ _).mpr ⟨b,hb,c,hc'.1,he⟩,
      (mem_scaledSum _ _ _ _).mpr ⟨b,hb,c+d,hc'.2,by nlinarith⟩⟩

end EnergyForcing.Counting
