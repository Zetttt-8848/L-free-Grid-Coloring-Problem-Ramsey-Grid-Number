import Mathlib
import Geometry

namespace EnergyForcing.Capacity

open scoped BigOperators

abbrev Label (d : ℕ) := Fin d → Bool

def bitZ (b : Bool) : ℤ := if b then 1 else 0

def BinarySidon {d : ℕ} (B : Finset (Label d)) : Prop :=
  ∀ a ∈ B, ∀ b ∈ B, ∀ c ∈ B, ∀ e ∈ B,
    (∀ i, bitZ (a i)+bitZ (b i)=bitZ (c i)+bitZ (e i)) →
    (a=c ∧ b=e) ∨ (a=e ∧ b=c)

def support {d : ℕ} (p : Label d × Label d) : Finset (Fin d) :=
  Finset.univ.filter fun i => p.1 i ≠ p.2 i

@[simp] theorem mem_support {d : ℕ} (p : Label d × Label d) (i : Fin d) :
    i∈support p ↔ p.1 i≠p.2 i := by simp [support]

theorem support_swap {d : ℕ} (p : Label d × Label d) : support p.swap=support p := by
  ext i
  simp [ne_comm]

/-- An unordered pair with support J has a unique orientation with pivot bit zero. -/
def alignedPairs {d : ℕ} (B : Finset (Label d)) (J : Finset (Fin d)) (j : Fin d) :
    Finset (Label d × Label d) :=
  (B.product B).filter fun p => support p=J ∧ p.1 j=false

@[simp] theorem mem_alignedPairs {d : ℕ} (B : Finset (Label d))
    (J : Finset (Fin d)) (j : Fin d) (p : Label d × Label d) :
    p∈alignedPairs B J j ↔ p.1∈B ∧ p.2∈B ∧ support p=J ∧ p.1 j=false := by
  simp [alignedPairs,and_assoc]

theorem aligned_pivot_right {d : ℕ} (B : Finset (Label d))
    (J : Finset (Fin d)) (j : Fin d) (hj : j∈J)
    (p : Label d × Label d) (hp : p∈alignedPairs B J j) : p.2 j=true := by
  rcases (mem_alignedPairs B J j p).mp hp with ⟨_,_,hs,hj0⟩
  have hn : p.1 j≠p.2 j := (mem_support p j).mp (hs.symm ▸ hj)
  cases h : p.2 j <;> simp_all

theorem aligned_ne {d : ℕ} (B : Finset (Label d)) (J : Finset (Fin d))
    (j : Fin d) (hj : j∈J) (p : Label d × Label d)
    (hp : p∈alignedPairs B J j) : p.1≠p.2 := by
  intro he
  have hl := ((mem_alignedPairs B J j p).mp hp).2.2.2
  have hr := aligned_pivot_right B J j hj p hp
  rw [he] at hl
  simp_all

theorem aligned_internal_injective {d : ℕ} (B : Finset (Label d))
    (hs : BinarySidon B) (J : Finset (Fin d)) (j : Fin d) (hj : j∈J) :
    Set.InjOn (fun p : Label d × Label d => fun i : ↥(J.erase j) => p.1 i)
      (↑(alignedPairs B J j) : Set (Label d × Label d)) := by
  intro p hp q hq he
  rcases (mem_alignedPairs B J j p).mp hp with ⟨hp₁,hp₂,hps,hpj⟩
  rcases (mem_alignedPairs B J j q).mp hq with ⟨hq₁,hq₂,hqs,hqj⟩
  have hadd : ∀ i, bitZ (p.1 i)+bitZ (q.2 i)=bitZ (q.1 i)+bitZ (p.2 i) := by
    intro i
    by_cases hi : i∈J
    · have hl : p.1 i=q.1 i := by
        by_cases hij : i=j
        · simpa [hij,hpj,hqj]
        · exact congrFun he ⟨i,Finset.mem_erase.mpr ⟨hij,hi⟩⟩
      have hn₁ : p.1 i≠p.2 i := (mem_support p i).mp (hps.symm ▸ hi)
      have hn₂ : q.1 i≠q.2 i := (mem_support q i).mp (hqs.symm ▸ hi)
      cases a : p.1 i <;> cases b : p.2 i <;> cases c : q.1 i <;>
        cases e : q.2 i <;> simp_all [bitZ]
    · have he₁ : p.1 i=p.2 i := by
        by_contra hne
        exact hi (hps ▸ (mem_support p i).mpr hne)
      have he₂ : q.1 i=q.2 i := by
        by_contra hne
        exact hi (hqs ▸ (mem_support q i).mpr hne)
      rw [he₁,he₂,add_comm]
  rcases hs p.1 hp₁ q.2 hq₂ q.1 hq₁ p.2 hp₂ hadd with ⟨h₁,h₂⟩ | ⟨h₁,_⟩
  · exact Prod.ext h₁ h₂.symm
  · exact False.elim (aligned_ne B J j hj p hp h₁)

theorem aligned_external_injective {d : ℕ} (B : Finset (Label d))
    (hs : BinarySidon B) (J : Finset (Fin d)) (j : Fin d) (hj : j∈J) :
    Set.InjOn (fun p : Label d × Label d => fun i : ↥(Finset.univ \ J) => p.1 i)
      (↑(alignedPairs B J j) : Set (Label d × Label d)) := by
  intro p hp q hq he
  rcases (mem_alignedPairs B J j p).mp hp with ⟨hp₁,hp₂,hps,hpj⟩
  rcases (mem_alignedPairs B J j q).mp hq with ⟨hq₁,hq₂,hqs,hqj⟩
  have hadd : ∀ i, bitZ (p.1 i)+bitZ (p.2 i)=bitZ (q.1 i)+bitZ (q.2 i) := by
    intro i
    by_cases hi : i∈J
    · have hn₁ : p.1 i≠p.2 i := (mem_support p i).mp (hps.symm ▸ hi)
      have hn₂ : q.1 i≠q.2 i := (mem_support q i).mp (hqs.symm ▸ hi)
      cases a : p.1 i <;> cases b : p.2 i <;> cases c : q.1 i <;>
        cases e : q.2 i <;> simp_all [bitZ]
    · have he₁ : p.1 i=p.2 i := by
        by_contra hne
        exact hi (hps ▸ (mem_support p i).mpr hne)
      have he₂ : q.1 i=q.2 i := by
        by_contra hne
        exact hi (hqs ▸ (mem_support q i).mpr hne)
      have he₃ : p.1 i=q.1 i := congrFun he ⟨i,by simp [hi]⟩
      rw [← he₁,← he₂,he₃]
  rcases hs p.1 hp₁ p.2 hp₂ q.1 hq₁ q.2 hq₂ hadd with ⟨h₁,h₂⟩ | ⟨h₁,_⟩
  · exact Prod.ext h₁ h₂
  · have hqt := aligned_pivot_right B J j hj q hq
    have heq := congrFun h₁ j
    simp_all

theorem aligned_capacity_internal {d : ℕ} (B : Finset (Label d))
    (hs : BinarySidon B) (J : Finset (Fin d)) (j : Fin d) (hj : j∈J) :
    (alignedPairs B J j).card ≤ 2^(J.card-1) := by
  have h := Finset.card_le_card_of_injOn
    (fun p : Label d × Label d => fun i : ↥(J.erase j) => p.1 i)
    (t := Finset.univ) (by simp) (aligned_internal_injective B hs J j hj)
  simpa only [Finset.card_univ, Fintype.card_fun, Fintype.card_bool,
    Fintype.card_coe, Finset.card_erase_of_mem hj] using h

theorem aligned_capacity_external {d : ℕ} (B : Finset (Label d))
    (hs : BinarySidon B) (J : Finset (Fin d)) (j : Fin d) (hj : j∈J) :
    (alignedPairs B J j).card ≤ 2^(d-J.card) := by
  have h := Finset.card_le_card_of_injOn
    (fun p : Label d × Label d => fun i : ↥(Finset.univ \ J) => p.1 i)
    (t := Finset.univ) (by simp) (aligned_external_injective B hs J j hj)
  simpa [Finset.card_sdiff (Finset.subset_univ J)] using h

/-- Support of an actual two-element subset of binary labels. -/
def setSupport {d : ℕ} (C : Finset (Label d)) : Finset (Fin d) :=
  Finset.univ.filter fun i => ∃ a∈C, ∃ b∈C, a i≠b i

@[simp] theorem setSupport_pair {d : ℕ} (a b : Label d) :
    setSupport {a,b}=support (a,b) := by
  ext i
  simp only [setSupport,Finset.mem_filter,Finset.mem_univ,true_and,
    Finset.mem_insert,Finset.mem_singleton,mem_support,Prod.fst,Prod.snd]
  constructor
  · rintro ⟨x,hx,y,hy,hne⟩
    rcases hx with rfl | rfl <;> rcases hy with rfl | rfl <;> simp_all [ne_comm]
  · intro hne; exact ⟨a,Or.inl rfl,b,Or.inr rfl,hne⟩

def pairFiber {d : ℕ} (B : Finset (Label d)) (J : Finset (Fin d)) :
    Finset (Finset (Label d)) := (B.powersetCard 2).filter fun C => setSupport C=J

def e {d : ℕ} (B : Finset (Label d)) (J : Finset (Fin d)) : ℕ := (pairFiber B J).card

theorem aligned_card_eq_e {d : ℕ} (B : Finset (Label d))
    (J : Finset (Fin d)) (j : Fin d) (hj : j∈J) :
    (alignedPairs B J j).card=e B J := by
  unfold e
  refine Finset.card_bij (fun p _ => {p.1,p.2}) ?_ ?_ ?_
  · intro p hp
    rcases (mem_alignedPairs B J j p).mp hp with ⟨hp₁,hp₂,hps,hpj⟩
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_powersetCard.mpr ⟨?_,?_⟩,?_⟩
    · intro a ha
      rcases Finset.mem_insert.mp ha with rfl | ha
      · exact hp₁
      · have he : a=p.2 := Finset.mem_singleton.mp ha
        simpa only [he] using hp₂
    · simp [aligned_ne B J j hj p hp]
    · simpa using hps
  · intro p hp q hq he
    change ({p.1,p.2} : Finset (Label d))={q.1,q.2} at he
    have hpj := ((mem_alignedPairs B J j p).mp hp).2.2.2
    have hqj := ((mem_alignedPairs B J j q).mp hq).2.2.2
    have hpt := aligned_pivot_right B J j hj p hp
    have hqt := aligned_pivot_right B J j hj q hq
    have h₁ : p.1=q.1 := by
      have hm : p.1∈({q.1,q.2} : Finset (Label d)) := by rw [← he]; simp
      rcases Finset.mem_insert.mp hm with h | h
      · exact h
      · have h' : p.1=q.2 := Finset.mem_singleton.mp h
        have := congrFun h' j
        simp_all
    have h₂ : p.2=q.2 := by
      have hm : p.2∈({q.1,q.2} : Finset (Label d)) := by rw [← he]; simp
      rcases Finset.mem_insert.mp hm with h | h
      · have := congrFun h j
        simp_all
      · exact Finset.mem_singleton.mp h
    exact Prod.ext h₁ h₂
  · intro C hC
    rcases Finset.mem_filter.mp hC with ⟨hC,hJ⟩
    rcases Finset.mem_powersetCard.mp hC with ⟨hsub,hcard⟩
    obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hcard
    have ha : a∈B := hsub (by simp)
    have hb : b∈B := hsub (by simp)
    have hs : support (a,b)=J := by simpa using hJ
    have hne : a j≠b j := (mem_support (a,b) j).mp (hs.symm ▸ hj)
    cases haj : a j
    · refine ⟨(a,b),(mem_alignedPairs B J j (a,b)).mpr ⟨ha,hb,hs,haj⟩,rfl⟩
    · have hbj : b j=false := by cases h : b j <;> simp_all
      refine ⟨(b,a),(mem_alignedPairs B J j (b,a)).mpr ⟨hb,ha,?_,hbj⟩,?_⟩
      · change support (a,b).swap=J
        rw [support_swap]
        exact hs
      · exact Finset.pair_comm b a

theorem pair_capacity {d : ℕ} (B : Finset (Label d)) (hs : BinarySidon B)
    (J : Finset (Fin d)) (hJ : J.Nonempty) :
    e B J ≤ min (2^(J.card-1)) (2^(d-J.card)) := by
  obtain ⟨j,hj⟩ := hJ
  rw [← aligned_card_eq_e B J j hj]
  exact le_min (aligned_capacity_internal B hs J j hj)
    (aligned_capacity_external B hs J j hj)

theorem e_empty {d : ℕ} (B : Finset (Label d)) : e B ∅=0 := by
  unfold e
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  intro C hC
  rcases Finset.mem_filter.mp hC with ⟨hC,hJ⟩
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp (Finset.mem_powersetCard.mp hC).2
  apply hab
  funext i
  by_contra hne
  have hm : i∈setSupport ({a,b} : Finset (Label d)) := by
    simpa using (mem_support (a,b) i).mpr hne
  simpa [hJ] using hm

theorem sum_e {d : ℕ} (B : Finset (Label d)) :
    ∑ J∈(Finset.univ : Finset (Fin d)).powerset, e B J = B.card.choose 2 := by
  have h := Finset.card_eq_sum_card_fiberwise (s := B.powersetCard 2)
    (t := (Finset.univ : Finset (Fin d)).powerset) (f := setSupport)
    (by intro C _; simp)
  simpa only [Finset.card_powersetCard,pairFiber,e] using h.symm

def capacityAt (d j : ℕ) : ℕ := if j=0 then 0 else min (2^(j-1)) (2^(d-j))

theorem cube_pair_sum_bound {d : ℕ} (B : Finset (Label d)) (hs : BinarySidon B) :
    B.card.choose 2 ≤ ∑ j∈Finset.Icc 1 d,
      d.choose j * min (2^(j-1)) (2^(d-j)) := by
  have hc : B.card.choose 2 ≤
      ∑ J∈(Finset.univ : Finset (Fin d)).powerset, capacityAt d J.card := by
    rw [← sum_e B]
    apply Finset.sum_le_sum
    intro J hJ
    by_cases hj : J.Nonempty
    · have hn : J.card≠0 := Finset.card_ne_zero.mpr hj
      simpa [capacityAt,hn] using pair_capacity B hs J hj
    · have he : J=∅ := Finset.not_nonempty_iff_eq_empty.mp hj
      subst J
      simp [e_empty,capacityAt]
  have hsum := Finset.sum_powerset_apply_card (capacityAt d)
    (x := (Finset.univ : Finset (Fin d)))
  simp only [Finset.card_univ,Fintype.card_fin,nsmul_eq_mul] at hsum
  rw [hsum] at hc
  have hr : Finset.range (d+1)=insert 0 (Finset.Icc 1 d) := by
    ext j
    simp only [Finset.mem_range,Finset.mem_insert,Finset.mem_Icc]
    omega
  rw [hr,Finset.sum_insert (by simp)] at hc
  simp only [capacityAt,ite_true,Nat.cast_id,mul_zero,zero_add] at hc
  convert hc using 1
  apply Finset.sum_congr rfl
  intro j hj
  have hj0 : j≠0 := by have := (Finset.mem_Icc.mp hj).1; omega
  simp [capacityAt,hj0]

theorem binary_four_bound (B : Finset (Label 4)) (hs : BinarySidon B) : B.card≤7 := by
  have h := cube_pair_sum_bound B hs
  have hsum : (∑ j∈Finset.Icc 1 4,
      Nat.choose 4 j * min (2^(j-1)) (2^(4-j)))=25 := by decide
  rw [hsum] at h
  have h8 : 8≤B.card → (8:ℕ).choose 2≤B.card.choose 2 :=
    fun hh => Nat.choose_le_choose 2 hh
  by_contra hn
  have hh := h8 (by omega)
  have hc : (8:ℕ).choose 2=28 := by decide
  rw [hc] at hh
  omega

def RealGolomb (A : ℝ → Prop) : Prop :=
  ∀ a b c e : ℝ, A a → A b → A c → A e → a<b → c<e →
    b-a=e-c → a=c ∧ b=e

theorem real_golomb_sum_ordered (A : ℝ → Prop) (h : RealGolomb A)
    (a b c e : ℝ) (ha : A a) (hb : A b) (hc : A c) (he : A e)
    (hab : a≤b) (hce : c≤e) (hs : a+b=c+e) : a=c ∧ b=e := by
  by_cases hac : a<c
  · have hh := h a c e b ha hc he hb hac (by linarith) (by linarith)
    rcases hh with ⟨h₁,h₂⟩
    constructor <;> linarith
  · by_cases hca : c<a
    · have hh := h c a b e hc ha hb he hca (by linarith) (by linarith)
      rcases hh with ⟨h₁,h₂⟩
      constructor <;> linarith
    · constructor <;> linarith

theorem real_golomb_sum_unique (A : ℝ → Prop) (h : RealGolomb A)
    (a b c e : ℝ) (ha : A a) (hb : A b) (hc : A c) (he : A e)
    (hs : a+b=c+e) : (a=c ∧ b=e) ∨ (a=e ∧ b=c) := by
  rcases le_total a b with hab | hba <;> rcases le_total c e with hce | hec
  · exact Or.inl (real_golomb_sum_ordered A h a b c e ha hb hc he hab hce hs)
  · exact Or.inr (real_golomb_sum_ordered A h a b e c ha hb he hc hab hec (by linarith))
  · have hh := real_golomb_sum_ordered A h b a c e hb ha hc he hba hce (by linarith)
    exact Or.inr ⟨hh.2,hh.1⟩
  · have hh := real_golomb_sum_ordered A h b a e c hb ha he hc hba hec (by linarith)
    exact Or.inl ⟨hh.2,hh.1⟩

noncomputable def weightedValue {d : ℕ} (a : ℝ) (w : Fin d → ℝ) (v : Label d) : ℝ :=
  a+∑ i, (bitZ (v i) : ℝ)*w i

noncomputable def realCube {d : ℕ} (a : ℝ) (w : Fin d → ℝ) : Finset ℝ := by
  classical
  exact Finset.univ.image (weightedValue a w)

noncomputable def labelsOf {d : ℕ} (a : ℝ) (w : Fin d → ℝ) (B : Finset ℝ) :
    Finset (Label d) := by
  classical
  exact Finset.univ.filter fun v => weightedValue a w v∈B

@[simp] theorem mem_labelsOf {d : ℕ} (a : ℝ) (w : Fin d → ℝ)
    (B : Finset ℝ) (v : Label d) : v∈labelsOf a w B ↔ weightedValue a w v∈B := by
  classical
  simp [labelsOf]

theorem weighted_binary_sidon {d : ℕ} (a : ℝ) (w : Fin d → ℝ)
    (B : Finset (Label d)) (hinj : Function.Injective (weightedValue a w))
    (hg : RealGolomb (fun x => x∈B.image (weightedValue a w))) : BinarySidon B := by
  classical
  intro p hp q hq u hu v hv hcoord
  have he : ∑ i, ((bitZ (p i) : ℝ)+(bitZ (q i) : ℝ))*w i =
      ∑ i, ((bitZ (u i) : ℝ)+(bitZ (v i) : ℝ))*w i := by
    apply Finset.sum_congr rfl
    intro i _
    have h : (bitZ (p i) : ℝ)+(bitZ (q i) : ℝ)=
        (bitZ (u i) : ℝ)+(bitZ (v i) : ℝ) := by exact_mod_cast hcoord i
    rw [h]
  simp_rw [add_mul] at he
  rw [Finset.sum_add_distrib,Finset.sum_add_distrib] at he
  have hs : weightedValue a w p+weightedValue a w q=
      weightedValue a w u+weightedValue a w v := by
    unfold weightedValue
    linarith
  rcases real_golomb_sum_unique _ hg _ _ _ _
    (Finset.mem_image_of_mem _ hp) (Finset.mem_image_of_mem _ hq)
    (Finset.mem_image_of_mem _ hu) (Finset.mem_image_of_mem _ hv) hs with
      ⟨h₁,h₂⟩ | ⟨h₁,h₂⟩
  · exact Or.inl ⟨hinj h₁,hinj h₂⟩
  · exact Or.inr ⟨hinj h₁,hinj h₂⟩

theorem labelsOf_image {d : ℕ} (a : ℝ) (w : Fin d → ℝ)
    (B : Finset ℝ) (hB : B ⊆ realCube a w) :
    (labelsOf a w B).image (weightedValue a w)=B := by
  classical
  ext x
  constructor
  · rintro hx
    obtain ⟨v,hv,rfl⟩ := Finset.mem_image.mp hx
    exact (mem_labelsOf a w B v).mp hv
  · intro hx
    obtain ⟨v,_,hv⟩ := Finset.mem_image.mp (hB hx)
    exact Finset.mem_image.mpr ⟨v,(mem_labelsOf a w B v).mpr (by simpa [hv] using hx),hv⟩

theorem labelsOf_card {d : ℕ} (a : ℝ) (w : Fin d → ℝ)
    (B : Finset ℝ) (hB : B ⊆ realCube a w)
    (hinj : Function.Injective (weightedValue a w)) : (labelsOf a w B).card=B.card := by
  classical
  calc
    (labelsOf a w B).card = ((labelsOf a w B).image (weightedValue a w)).card :=
      (Finset.card_image_of_injective _ hinj).symm
    _ = B.card := congrArg Finset.card (labelsOf_image a w B hB)

/-- Pair capacities for an actual Golomb subset of an injective real weighted cube.
    Positivity of the weights is not needed once injectivity is assumed. -/
theorem real_cube_pair_capacity {d : ℕ} (a : ℝ) (w : Fin d → ℝ)
    (B : Finset ℝ) (hB : B ⊆ realCube a w)
    (hinj : Function.Injective (weightedValue a w))
    (hg : RealGolomb (fun x => x∈B)) (J : Finset (Fin d)) (hJ : J.Nonempty) :
    e (labelsOf a w B) J ≤ min (2^(J.card-1)) (2^(d-J.card)) := by
  apply pair_capacity _ _ J hJ
  apply weighted_binary_sidon a w _ hinj
  simpa only [labelsOf_image a w B hB] using hg

theorem real_cube_pair_sum_bound {d : ℕ} (a : ℝ) (w : Fin d → ℝ)
    (B : Finset ℝ) (hB : B ⊆ realCube a w)
    (hinj : Function.Injective (weightedValue a w))
    (hg : RealGolomb (fun x => x∈B)) :
    B.card.choose 2 ≤ ∑ j∈Finset.Icc 1 d,
      d.choose j * min (2^(j-1)) (2^(d-j)) := by
  have hs : BinarySidon (labelsOf a w B) := by
    apply weighted_binary_sidon a w _ hinj
    simpa only [labelsOf_image a w B hB] using hg
  simpa only [labelsOf_card a w B hB hinj] using cube_pair_sum_bound _ hs

theorem real_four_cube_golomb_bound (a : ℝ) (w : Fin 4 → ℝ)
    (B : Finset ℝ) (hB : B ⊆ realCube a w)
    (hinj : Function.Injective (weightedValue a w))
    (hg : RealGolomb (fun x => x∈B)) : B.card≤7 := by
  have hs : BinarySidon (labelsOf a w B) := by
    apply weighted_binary_sidon a w _ hinj
    simpa only [labelsOf_image a w B hB] using hg
  simpa only [labelsOf_card a w B hB hinj] using binary_four_bound _ hs

#print axioms aligned_capacity_internal
#print axioms aligned_capacity_external
#print axioms pair_capacity
#print axioms cube_pair_sum_bound
#print axioms binary_four_bound
#print axioms real_cube_pair_capacity
#print axioms real_cube_pair_sum_bound
#print axioms real_four_cube_golomb_bound

end EnergyForcing.Capacity
