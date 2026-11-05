import RectangleObstructions
import EndpointPeeling

set_option autoImplicit false

namespace EnergyForcing.Counting

noncomputable def selectedMarks (B : Finset ℤ) (k : ℕ) (hk:k≤B.card) : Fin k↪ℤ :=
  ((Fin.castLEEmb (show k≤Fintype.card B by simpa using hk)).trans
    (Fintype.equivFin B).symm.toEmbedding).trans (Function.Embedding.subtype (·∈B))

theorem selectedMarks_mem (B : Finset ℤ) (k : ℕ) (hk:k≤B.card) (i : Fin k) :
    selectedMarks B k hk i∈B := by
  exact ((Fintype.equivFin B).symm (Fin.castLE (by simpa using hk) i)).property

theorem twoGolomb_product_obstruction (B C : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q)
    (m n : ℕ) (hm:m≤B.card) (hn:n≤C.card)
    (hrect:∀a:Fin m→Fin n→Bool,HasRectangle a) :
    ¬TwoGolombPartition (scaledSum B C Q) := by
  rintro ⟨G,H,hGH,hG,hH,hunion⟩
  let f := selectedMarks B m hm
  let g := selectedMarks C n hn
  let a : Fin m→Fin n→Bool := fun i j=>decide (f i+Q*g j∈G)
  obtain ⟨i,j,k,l,hij,hkl,h1,h2,h3⟩ := hrect a
  have hf (i:Fin m) : f i∈B := selectedMarks_mem B m hm i
  have hg (k:Fin n) : g k∈C := selectedMarks_mem C n hn k
  have hmark (i:Fin m) (k:Fin n) : f i+Q*g k∈G∪H := by
    rw [← hunion]
    exact (mem_scaledSum _ _ _ _).mpr ⟨f i,hf i,g k,hg k,rfl⟩
  have hpair :
      (f i+Q*g k=f i+Q*g l ∧ f j+Q*g l=f j+Q*g k) ∨
      (f i+Q*g k=f j+Q*g k ∧ f j+Q*g l=f i+Q*g l) := by
    by_cases hp : a i k=true
    · have hq : a i l=true := h1 ▸ hp
      have hr : a j k=true := h2 ▸ hq
      have hs : a j l=true := h3 ▸ hr
      simp only [a,decide_eq_true_eq] at hp hq hr hs
      exact golomb_pair_or G hG _ _ _ _ hp hs hq hr (by ring)
    · have hp' : a i k=false := Bool.eq_false_iff.mpr hp
      have hq : a i l=false := h1 ▸ hp'
      have hr : a j k=false := h2 ▸ hq
      have hs : a j l=false := h3 ▸ hr
      have inH (i:Fin m) (k:Fin n) (hc:a i k=false) : f i+Q*g k∈H := by
        have hm' := hmark i k
        simp only [a,decide_eq_false_iff_not] at hc
        exact (Finset.mem_union.mp hm').resolve_left hc
      exact golomb_pair_or H hH _ _ _ _ (inH i k hp') (inH j l hs)
        (inH i l hq) (inH j k hr) (by ring)
  rcases hpair with hp|hp
  · have hsame := separated_mark_unique B Q hQ (f i) (f i) (g k) (g l) (hf i) (hf i) hp.1
    exact hkl (g.injective hsame.2)
  · have hsame := separated_mark_unique B Q hQ (f i) (f j) (g k) (g k) (hf i) (hf j) hp.1
    exact hij (f.injective hsame.1)

theorem twoGolomb_product_seven_three (B C : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q)
    (hB:7≤B.card) (hC:3≤C.card) : ¬TwoGolombPartition (scaledSum B C Q) :=
  twoGolomb_product_obstruction B C Q hQ 7 3 hB hC rectangle_seven_three

theorem twoGolomb_product_three_seven (B C : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q)
    (hB:3≤B.card) (hC:7≤C.card) : ¬TwoGolombPartition (scaledSum B C Q) := by
  apply twoGolomb_product_obstruction B C Q hQ 3 7 hB hC
  intro a
  obtain ⟨i,j,k,l,hij,hkl,h1,h2,h3⟩ := rectangle_seven_three (fun i j=>a j i)
  exact ⟨k,l,i,j,hkl,hij,h1.trans h2,(h1.trans h2).symm.trans h1,h2.trans h3⟩

theorem twoGolomb_product_five_five (B C : Finset ℤ) (Q : ℤ) (hQ:2*(span B:ℤ)<Q)
    (hB:5≤B.card) (hC:5≤C.card) : ¬TwoGolombPartition (scaledSum B C Q) :=
  twoGolomb_product_obstruction B C Q hQ 5 5 hB hC rectangle_five_five

theorem separated_base_fiber (B C : Finset ℤ) (Q d : ℤ) (hQ:2*(span B:ℤ)<Q)
    (hd:d∈posDiffs B) :
    positiveFiber (scaledSum B C Q) d=scaledSum (positiveFiber B d) C Q := by
  obtain ⟨hdpos,v,hv,hvd⟩ := (mem_posDiffs B d).mp hd
  ext u
  constructor
  · intro hu
    obtain ⟨hu,hu'⟩ := (mem_positiveFiber _ _ u).mp hu
    obtain ⟨b,hb,c,hc,he⟩ := (mem_scaledSum B C Q u).mp hu
    obtain ⟨b',hb',c',hc',he'⟩ := (mem_scaledSum B C Q (u+d)).mp hu'
    have hh := separated_difference_unique B Q hQ b' b (v+d) v (c'-c) 0 hb' hb hvd hv (by nlinarith)
    have hbb : b+d=b' := by omega
    exact (mem_scaledSum _ _ _ _).mpr ⟨b,(mem_positiveFiber B d b).mpr
      ⟨hb,by simpa [hbb] using hb'⟩,c,hc,he⟩
  · intro hu
    obtain ⟨b,hb,c,hc,he⟩ := (mem_scaledSum _ C Q u).mp hu
    have hb' := (mem_positiveFiber B d b).mp hb
    apply (mem_positiveFiber _ _ u).mpr
    exact ⟨(mem_scaledSum _ _ _ _).mpr ⟨b,hb'.1,c,hc,he⟩,
      (mem_scaledSum _ _ _ _).mpr ⟨b+d,hb'.2,c,hc,by omega⟩⟩

theorem positiveFiber_subset (A : Finset ℤ) (d : ℤ) : positiveFiber A d⊆A :=
  Finset.filter_subset _ _

theorem separated_fiber_separation (B : Finset ℤ) (Q d : ℤ) (hQ:2*(span B:ℤ)<Q) :
    2*(span (positiveFiber B d):ℤ)<Q := by
  have hs := endpoint_span_mono (positiveFiber_subset B d)
  omega

theorem factor_multiplicity_cap_two_left (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hC:7≤C.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    ∀d:ℤ,0<d → r B d≤2 := by
  intro d hd
  by_cases hm:d∈posDiffs B
  · have hp := fiber_twoGolomb (scaledSum B C Q) z hz d hd
    rw [separated_base_fiber B C Q d hQ hm] at hp
    by_contra hn
    exact twoGolomb_product_three_seven (positiveFiber B d) C Q
      (separated_fiber_separation B Q d hQ) (by change 3≤r B d; omega) hC hp
  · rw [r_eq_zero_of_not_mem_posDiffs B d hd hm]
    omega

theorem factor_multiplicity_cap_two_right (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hB:7≤B.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    ∀d:ℤ,0<d → r C d≤2 := by
  intro d hd
  have hQpos : 0<Q := by omega
  have hp := fiber_twoGolomb (scaledSum B C Q) z hz (Q*d) (mul_pos hQpos hd)
  rw [separated_scaled_fiber B C Q d hQ] at hp
  by_contra hn
  exact twoGolomb_product_seven_three B (positiveFiber C d) Q hQ hB (by change 3≤r C d; omega) hp

theorem factor_multiplicity_cap_four_left (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hC:5≤C.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    ∀d:ℤ,0<d → r B d≤4 := by
  intro d hd
  by_cases hm:d∈posDiffs B
  · have hp := fiber_twoGolomb (scaledSum B C Q) z hz d hd
    rw [separated_base_fiber B C Q d hQ hm] at hp
    by_contra hn
    exact twoGolomb_product_five_five (positiveFiber B d) C Q
      (separated_fiber_separation B Q d hQ) (by change 5≤r B d; omega) hC hp
  · rw [r_eq_zero_of_not_mem_posDiffs B d hd hm]
    omega

theorem factor_multiplicity_cap_four_right (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hB:5≤B.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    ∀d:ℤ,0<d → r C d≤4 := by
  intro d hd
  have hQpos : 0<Q := by omega
  have hp := fiber_twoGolomb (scaledSum B C Q) z hz (Q*d) (mul_pos hQpos hd)
  rw [separated_scaled_fiber B C Q d hQ] at hp
  by_contra hn
  exact twoGolomb_product_five_five B (positiveFiber C d) Q hQ hB (by change 5≤r C d; omega) hp

theorem golomb_affine_preimage (S G : Finset ℤ) (a q : ℤ) (hq:0<q)
    (hG:Golomb (·∈G)) : Golomb (·∈S.filter (fun x=>a+q*x∈G)) := by
  intro x y z w hx hy hz hw hxy hzw he
  have hx' := (Finset.mem_filter.mp hx).2
  have hy' := (Finset.mem_filter.mp hy).2
  have hz' := (Finset.mem_filter.mp hz).2
  have hw' := (Finset.mem_filter.mp hw).2
  have hm := congrArg (fun v:ℤ=>q*v) he
  dsimp only at hm
  have hh := hG (a+q*x) (a+q*y) (a+q*z) (a+q*w) hx' hy' hz' hw'
    (by nlinarith [mul_pos hq (show 0<y-x by omega)])
    (by nlinarith [mul_pos hq (show 0<w-z by omega)]) (by nlinarith)
  constructor
  · exact mul_left_cancel₀ (ne_of_gt hq) (by linarith [hh.1] : q*x=q*z)
  · exact mul_left_cancel₀ (ne_of_gt hq) (by linarith [hh.2] : q*y=q*w)

theorem twoGolomb_affine_preimage (S A : Finset ℤ) (a q : ℤ) (hq:0<q)
    (hsub:∀x∈S,a+q*x∈A) (hp:TwoGolombPartition A) : TwoGolombPartition S := by
  obtain ⟨G,H,hGH,hG,hH,hunion⟩ := hp
  refine ⟨S.filter (fun x=>a+q*x∈G),S.filter (fun x=>a+q*x∈H),?_,
    golomb_affine_preimage S G a q hq hG,golomb_affine_preimage S H a q hq hH,?_⟩
  · apply Finset.disjoint_left.mpr
    intro x hx hy
    exact Finset.disjoint_left.mp hGH (Finset.mem_filter.mp hx).2 (Finset.mem_filter.mp hy).2
  · ext x
    simp only [Finset.mem_union,Finset.mem_filter]
    constructor
    · intro hx
      have hh := hsub x hx
      rw [hunion] at hh
      rcases Finset.mem_union.mp hh with hg|hh
      · exact Or.inl ⟨hx,hg⟩
      · exact Or.inr ⟨hx,hh⟩
    · rintro (hx|hx) <;> exact hx.1

theorem exists_positive_pair (A : Finset ℤ) (hA:2≤A.card) :
    ∃d u,0<d ∧ u∈positiveFiber A d := by
  obtain ⟨a,ha,b,hb,hne⟩ := Finset.one_lt_card.mp (show 1<A.card by omega)
  by_cases hab:a<b
  · exact ⟨b-a,a,by omega,(mem_positiveFiber A _ _).mpr ⟨ha,by simpa using hb⟩⟩
  · exact ⟨a-b,b,by omega,(mem_positiveFiber A _ _).mpr ⟨hb,by simpa using ha⟩⟩

theorem left_factor_twoGolomb (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hC:2≤C.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) : TwoGolombPartition B := by
  obtain ⟨d,v,hd,hv⟩ := exists_positive_pair C hC
  have hQpos : 0<Q := by omega
  have hp := fiber_twoGolomb (scaledSum B C Q) z hz (Q*d) (mul_pos hQpos hd)
  rw [separated_scaled_fiber B C Q d hQ] at hp
  apply twoGolomb_affine_preimage B _ (Q*v) 1 (by norm_num) ?_ hp
  intro b hb
  exact (mem_scaledSum _ _ _ _).mpr ⟨b,hb,v,hv,by ring⟩

theorem right_factor_twoGolomb (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hB:2≤B.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) : TwoGolombPartition C := by
  obtain ⟨d,u,hd,hu⟩ := exists_positive_pair B hB
  have hQpos : 0<Q := by omega
  have hdiff : d∈posDiffs B := by
    exact (mem_posDiffs B d).mpr ⟨hd,u,(mem_positiveFiber B d u).mp hu⟩
  have hp := fiber_twoGolomb (scaledSum B C Q) z hz d hd
  rw [separated_base_fiber B C Q d hQ hdiff] at hp
  apply twoGolomb_affine_preimage C _ u Q hQpos ?_ hp
  intro c hc
  exact (mem_scaledSum _ _ _ _).mpr ⟨u,hu,c,hc,rfl⟩

theorem complete_overlap_restrictions (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)<Q) (hB:2≤B.card) (hC:2≤C.card) (z : Point→Bool)
    (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    E (scaledSum B C Q)=E B*E C ∧ TwoGolombPartition B ∧ TwoGolombPartition C ∧
    (7≤B.card → ∀d:ℤ,0<d → r C d≤2) ∧
    (7≤C.card → ∀d:ℤ,0<d → r B d≤2) ∧
    (5≤B.card → ∀d:ℤ,0<d → r C d≤4) ∧
    (5≤C.card → ∀d:ℤ,0<d → r B d≤4) := by
  exact ⟨separated_energy_product B C Q hQ,left_factor_twoGolomb B C Q hQ hC z hz,
    right_factor_twoGolomb B C Q hQ hB z hz,
    (fun h=>factor_multiplicity_cap_two_right B C Q hQ h z hz),
    (fun h=>factor_multiplicity_cap_two_left B C Q hQ h z hz),
    (fun h=>factor_multiplicity_cap_four_right B C Q hQ h z hz),
    (fun h=>factor_multiplicity_cap_four_left B C Q hQ h z hz)⟩

end EnergyForcing.Counting
