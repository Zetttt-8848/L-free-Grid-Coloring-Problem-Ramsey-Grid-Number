import TranslationCorrelations
import EndpointPeeling

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace EnergyForcing.Translation
open Finset
open EnergyForcing.Counting EnergyForcing.EnergyUnion

theorem fourth_sum_bound (b c : ℝ) (hb : 1 ≤ b) (hc : 1 ≤ c) :
    (Real.sqrt (Real.sqrt (22*b^2-12*b))+
      Real.sqrt (Real.sqrt (22*c^2-12*c)))^4 ≤ 88*(b+c)^2-96*(b+c) := by
  let G := 22*b^2-12*b
  let H := 22*c^2-12*c
  let C := 22*b*c-6*(b+c)
  have hG : 0 ≤ G := by dsimp [G]; nlinarith
  have hH : 0 ≤ H := by dsimp [H]; nlinarith
  have hC : 0 ≤ C := by
    have hm := mul_nonneg (sub_nonneg.mpr hb) (sub_nonneg.mpr hc)
    dsimp [C]; nlinarith
  have hCH : G*H ≤ C^2 := by
    dsimp [G,H,C]
    nlinarith [sq_nonneg (b-c)]
  have hprod : (Real.sqrt G*Real.sqrt H)^2=G*H := by
    rw [mul_pow,Real.sq_sqrt hG,Real.sq_sqrt hH]
  have hp : Real.sqrt G*Real.sqrt H ≤ C := by
    nlinarith [Real.sqrt_nonneg G,Real.sqrt_nonneg H]
  have hx := Real.sq_sqrt (Real.sqrt_nonneg G)
  have hy := Real.sq_sqrt (Real.sqrt_nonneg H)
  have hx' := Real.sq_sqrt hG
  have hy' := Real.sq_sqrt hH
  have hfirst : (Real.sqrt (Real.sqrt G)+Real.sqrt (Real.sqrt H))^2 ≤
      2*(Real.sqrt G+Real.sqrt H) := by
    nlinarith [sq_nonneg (Real.sqrt (Real.sqrt G)-Real.sqrt (Real.sqrt H))]
  have hsq := mul_self_le_mul_self (by positivity : 0 ≤
    (Real.sqrt (Real.sqrt G)+Real.sqrt (Real.sqrt H))^2) hfirst
  change (Real.sqrt (Real.sqrt G)+Real.sqrt (Real.sqrt H))^4 ≤ _
  dsimp [G,H,C] at hp hx' hy'
  nlinarith

theorem union_doubled_golomb_energy (B C : Finset ℤ) (d : ℤ)
    (hB : Golomb (·∈B)) (hC : Golomb (·∈C)) (hd : 0 < d)
    (hb : B.Nonempty) (hc : C.Nonempty)
    (hbd : Disjoint B (translate B d)) (hcd : Disjoint C (translate C d))
    (hdis : Disjoint (B∪translate B d) (C∪translate C d)) :
    (E ((B∪translate B d)∪(C∪translate C d)) : ℝ) ≤
      88*((B.card : ℝ)+C.card)^2-96*((B.card : ℝ)+C.card) := by
  have h₁ := doubled_golomb_energy B hB d hd hbd
  have h₂ := doubled_golomb_energy C hC d hd hcd
  have htri := energy_fourth_root_triangle (B∪translate B d) (C∪translate C d) hdis
  have hm₁ := Real.sqrt_le_sqrt (Real.sqrt_le_sqrt h₁)
  have hm₂ := Real.sqrt_le_sqrt (Real.sqrt_le_sqrt h₂)
  have hle : Real.sqrt (Real.sqrt (E ((B∪translate B d)∪(C∪translate C d)) : ℝ)) ≤
    Real.sqrt (Real.sqrt (22*(B.card : ℝ)^2-12*B.card))+
    Real.sqrt (Real.sqrt (22*(C.card : ℝ)^2-12*C.card)) := by linarith
  have hp := pow_le_pow_left₀ (Real.sqrt_nonneg _) hle 4
  have he : (Real.sqrt (Real.sqrt (E ((B∪translate B d)∪(C∪translate C d)) : ℝ)))^4 =
      (E ((B∪translate B d)∪(C∪translate C d)) : ℝ) := by
    rw [show (4:ℕ)=2*2 by decide,pow_mul,Real.sq_sqrt (Real.sqrt_nonneg _),Real.sq_sqrt (by positivity)]
  rw [he] at hp
  exact hp.trans (fourth_sum_bound _ _ (by exact_mod_cast hb.card_pos) (by exact_mod_cast hc.card_pos))

theorem pair_golomb (a b : ℤ) : Golomb (·∈({a,b} : Finset ℤ)) := by
  intro x y u v hx hy hu hv hxy huv he
  simp only [Finset.mem_insert,Finset.mem_singleton] at hx hy hu hv
  rcases hx with rfl|rfl <;> rcases hy with rfl|rfl <;>
    rcases hu with rfl|rfl <;> rcases hv with rfl|rfl <;> omega

theorem one_doubled_golomb_bound (B : Finset ℤ) (d : ℤ)
    (hB : Golomb (·∈B)) (hd : 0 < d) (hdis : Disjoint B (translate B d)) :
    (E (B∪translate B d) : ℝ) ≤ 88*(B.card : ℝ)^2-82*B.card := by
  by_cases hz : B.card=0
  · have he := Finset.card_eq_zero.mp hz
    simp [he,translate,E,energySet]
  by_cases ho : B.card=1
  · obtain ⟨a,rfl⟩ := Finset.card_eq_one.mp ho
    have hs : ({a} : Finset ℤ)∪translate {a} d={a,a+d} := by ext x; simp [translate]
    rw [hs,golomb_energy _ (pair_golomb a (a+d))]
    have hn : a≠a+d := by omega
    norm_num [hn]
  have he := doubled_golomb_energy B hB d hd hdis
  have hb : (2:ℝ) ≤ B.card := by exact_mod_cast (show 2 ≤ B.card by omega)
  nlinarith

def matchingClass (S : Finset ℤ) (d : ℤ) (z : Point→Bool) (b : Bool) :=
  S.filter (fun x => z (x+d,x)=b)

theorem matching_classes (S : Finset ℤ) (d : ℤ) (z : Point→Bool) :
    Disjoint (matchingClass S d z false) (matchingClass S d z true) ∧
    matchingClass S d z false∪matchingClass S d z true=S := by
  constructor
  · apply Finset.disjoint_left.mpr
    intro x hx hy
    simp only [matchingClass,Finset.mem_filter] at hx hy
    exact Bool.false_ne_true (hx.2.symm.trans hy.2)
  · ext x
    simp only [matchingClass,Finset.mem_union,Finset.mem_filter]
    cases z (x+d,x) <;> simp

theorem matching_class_golomb (S : Finset ℤ) (d : ℤ) (z : Point→Bool)
    (hd : 0 < d) (hz : properOn (strictSource (·∈S∪translate S d)) z) (b : Bool) :
    Golomb (·∈matchingClass S d z b) := by
  have hG := fiber_class_golomb (·∈S∪translate S d) z hz d hd b
  have hsub : ∀x∈matchingClass S d z b,
      (x∈S∪translate S d ∧ x+d∈S∪translate S d) ∧ z (x+d,x)=b := by
    intro x hx
    have hh := Finset.mem_filter.mp hx
    exact ⟨⟨Finset.mem_union_left _ hh.1,
      Finset.mem_union_right _ ((mem_translate S d (x+d)).mpr (by simpa using hh.1))⟩,hh.2⟩
  intro x y u v hx hy hu hv hxy huv he
  exact hG x y u v (hsub x hx) (hsub y hy) (hsub u hu) (hsub v hv) hxy huv he

theorem translate_union (B C : Finset ℤ) (d : ℤ) :
    translate (B∪C) d=translate B d∪translate C d := by simp [translate]

theorem matching_doubled_disjoint (B C : Finset ℤ) (d : ℤ)
    (hBC : Disjoint B C) (hdis : Disjoint (B∪C) (translate (B∪C) d)) :
    Disjoint (B∪translate B d) (C∪translate C d) := by
  apply Finset.disjoint_left.mpr
  intro x hx hy
  simp only [Finset.mem_union,mem_translate] at hx hy
  have h₁ := Finset.disjoint_left.mp hBC
  have h₂ := Finset.disjoint_left.mp hdis
  rcases hx with hx|hx <;> rcases hy with hy|hy
  · exact h₁ hx hy
  · exact h₂ (Finset.mem_union_left _ hx) ((mem_translate _ _ _).mpr (Finset.mem_union_right _ hy))
  · exact h₂ (Finset.mem_union_right _ hy) ((mem_translate _ _ _).mpr (Finset.mem_union_left _ hx))
  · exact h₁ hx hy

theorem translation_matching_energy (S : Finset ℤ) (d : ℤ) (z : Point→Bool)
    (hd : 0 < d) (hdis : Disjoint S (translate S d))
    (hz : properOn (strictSource (·∈S∪translate S d)) z) :
    (E (S∪translate S d) : ℝ) ≤ 22*(2*(S.card : ℝ))^2-41*(2*(S.card : ℝ)) := by
  let B := matchingClass S d z false
  let C := matchingClass S d z true
  have hBC : Disjoint B C := (matching_classes S d z).1
  have hU : B∪C=S := (matching_classes S d z).2
  have hcard : (B.card : ℝ)+C.card=(S.card : ℝ) := by exact_mod_cast (hU ▸ Finset.card_union_of_disjoint hBC).symm
  have hB := matching_class_golomb S d z hd hz false
  have hC := matching_class_golomb S d z hd hz true
  have hbd : Disjoint B (translate B d) := hdis.mono (Finset.filter_subset _ _) (by
    intro x hx; rw [mem_translate] at hx ⊢; exact Finset.filter_subset _ _ hx)
  have hcd : Disjoint C (translate C d) := hdis.mono (Finset.filter_subset _ _) (by
    intro x hx; rw [mem_translate] at hx ⊢; exact Finset.filter_subset _ _ hx)
  have hrepr : (B∪translate B d)∪(C∪translate C d)=S∪translate S d := by
    rw [← hU,translate_union]
    ext x; simp only [Finset.mem_union]; tauto
  by_cases hb : B.Nonempty
  · by_cases hc : C.Nonempty
    · have he := union_doubled_golomb_energy B C d hB hC hd hb hc hbd hcd
        (matching_doubled_disjoint B C d hBC (hU.symm ▸ hdis))
      rw [hrepr,hcard] at he
      have hs0 : (0:ℝ) ≤ S.card := by positivity
      nlinarith
    · have heC : C=∅ := Finset.not_nonempty_iff_eq_empty.mp hc
      have he := one_doubled_golomb_bound B d hB hd hbd
      have hBS : B=S := by simpa [heC] using hU
      rw [hBS] at he
      nlinarith
  · have heB : B=∅ := Finset.not_nonempty_iff_eq_empty.mp hb
    have he := one_doubled_golomb_bound C d hC hd hcd
    have hCS : C=S := by simpa [heB] using hU
    rw [hCS] at he
    nlinarith

theorem translation_matching_corners (S : Finset ℤ) (d : ℤ) (z : Point→Bool)
    (hd : 0 < d) (hdis : Disjoint S (translate S d))
    (hz : properOn (strictSource (·∈S∪translate S d)) z) :
    (T (S∪translate S d) : ℝ) ≤ 10*(M (S∪translate S d) : ℝ)-5*(2*(S.card : ℝ)) := by
  have he := translation_matching_energy S d z hd hdis hz
  have hn : ((S∪translate S d).card : ℝ)=2*(S.card : ℝ) := by
    rw [Finset.card_union_of_disjoint hdis,translate_card]; push_cast; ring
  have hid := real_E (S∪translate S d)
  have hm := real_M (S∪translate S d)
  rw [hn] at hid hm
  nlinarith

theorem matching_span_start (S : Finset ℤ) (d : ℤ) (hd : 0 < d) (hS : S.Nonempty) :
    1 ≤ span (S∪translate S d) ∧ span S ≤ span (S∪translate S d)-1 := by
  let A := S∪translate S d
  have hsub : S ⊆ positiveFiber A d := by
    intro x hx
    apply (mem_positiveFiber A d x).mpr
    exact ⟨Finset.mem_union_left _ hx,Finset.mem_union_right _
      ((mem_translate S d (x+d)).mpr (by simpa using hx))⟩
  obtain ⟨x,hx⟩ := hS
  have hdx : d∈posDiffs A := (mem_posDiffs A d).mpr
    ⟨hd,x,(mem_positiveFiber A d x).mp (hsub hx)⟩
  have hL := (Finset.mem_Icc.mp (posDiffs_subset_interval A hdx)).2
  have hspan := (endpoint_span_mono hsub).trans (positiveFiber_span_le A d hd)
  dsimp [A] at hspan hL
  constructor <;> omega

theorem golomb_pair_span (B : Finset ℤ) (hB : Golomb (·∈B)) : (M B : ℝ) ≤ span B := by
  have ht : (T B : ℝ) ≤ 0*(M B : ℝ) := by
    have he := golomb_energy B hB
    have hid := real_E B
    nlinarith
  simpa using span_pair_bound B 0 (by norm_num) ht

theorem matching_span_algebra (b c L : ℝ) (hb : 0 ≤ b) (hc : 0 ≤ c)
    (hL : 1 ≤ L) (hbL : b*(b-1)/2 ≤ L-1) (hcL : c*(c-1)/2 ≤ L-1) :
    (b+c)*(2*(b+c)-1) ≤ 16*L-13+3*Real.sqrt (8*L-7) ∧
      16*L-13+3*Real.sqrt (8*L-7) < 18*L := by
  have hr0 : 0 ≤ 8*L-7 := by linarith
  have hrsq := Real.sq_sqrt hr0
  have hr := Real.sqrt_nonneg (8*L-7)
  have hs : (b+c-1)^2 ≤ 8*L-7 := by nlinarith [sq_nonneg (b-c)]
  have hsr := Real.le_sqrt_of_sq_le hs
  have hh := mul_nonneg (show 0 ≤ 1+Real.sqrt (8*L-7)-(b+c) by linarith)
    (show 0 ≤ 2*(b+c)+2*(1+Real.sqrt (8*L-7))-1 by linarith)
  constructor
  · nlinarith
  · nlinarith [sq_nonneg (L-5/2)]

theorem translation_matching_span (S : Finset ℤ) (d : ℤ) (z : Point→Bool)
    (hd : 0 < d) (hdis : Disjoint S (translate S d))
    (hz : properOn (strictSource (·∈S∪translate S d)) z) (hS : S.Nonempty) :
    1 ≤ span (S∪translate S d) ∧
    (M (S∪translate S d) : ℝ) ≤ 16*(span (S∪translate S d) : ℝ)-13+
      3*Real.sqrt (8*(span (S∪translate S d) : ℝ)-7) ∧
    16*(span (S∪translate S d) : ℝ)-13+
      3*Real.sqrt (8*(span (S∪translate S d) : ℝ)-7) < 18*(span (S∪translate S d) : ℝ) := by
  let B := matchingClass S d z false
  let C := matchingClass S d z true
  have hBC : Disjoint B C := (matching_classes S d z).1
  have hU : B∪C=S := (matching_classes S d z).2
  have hcard : (B.card : ℝ)+C.card=(S.card : ℝ) := by exact_mod_cast (hU ▸ Finset.card_union_of_disjoint hBC).symm
  have hL := matching_span_start S d hd hS
  have hspan : (span S : ℝ) ≤ (span (S∪translate S d) : ℝ)-1 := by
    have hh : span S+1 ≤ span (S∪translate S d) := by omega
    exact_mod_cast (show (span S : ℤ) ≤ (span (S∪translate S d) : ℤ)-1 by omega)
  have hclass (b : Bool) : ((matchingClass S d z b).card : ℝ)*
      ((matchingClass S d z b).card-1)/2 ≤ (span (S∪translate S d) : ℝ)-1 := by
    have hp := golomb_pair_span (matchingClass S d z b) (matching_class_golomb S d z hd hz b)
    have hm : (span (matchingClass S d z b) : ℝ) ≤ span S := by
      exact_mod_cast endpoint_span_mono (Finset.filter_subset (fun x => z (x+d,x)=b) S)
    rw [real_M] at hp
    exact hp.trans (hm.trans hspan)
  have ha := matching_span_algebra (B.card : ℝ) C.card (span (S∪translate S d))
    (by positivity) (by positivity) (by exact_mod_cast hL.1) (hclass false) (hclass true)
  have hn : ((S∪translate S d).card : ℝ)=2*(S.card : ℝ) := by
    rw [Finset.card_union_of_disjoint hdis,translate_card]; push_cast; ring
  refine ⟨hL.1,?_,ha.2⟩
  rw [hcard] at ha
  rw [real_M,hn]
  nlinarith [ha.1]

#print axioms translation_matching_energy
#print axioms translation_matching_corners
#print axioms translation_matching_span
end EnergyForcing.Translation
