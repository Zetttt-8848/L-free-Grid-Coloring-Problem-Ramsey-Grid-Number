import EndpointAnchor

namespace EnergyForcing.Counting

/-- Pair-sum uniqueness includes repeated summands. -/
def EndpointSidon (S : Finset ℤ) : Prop :=
  ∀ a ∈ S, ∀ b ∈ S, ∀ c ∈ S, ∀ d ∈ S, a+b=c+d →
    (a=c ∧ b=d) ∨ (a=d ∧ b=c)

theorem endpoint_sidon_insert (S : Finset ℤ) (m : ℤ) (hm : 0 ≤ m)
    (hbound : ∀ x ∈ S, 0 ≤ x ∧ x ≤ m) (hs : EndpointSidon S) :
    EndpointSidon (insert (2*m+1) S) := by
  intro a ha b hb c hc d hd he
  simp only [Finset.mem_insert] at ha hb hc hd
  rcases ha with rfl | ha <;> rcases hb with rfl | hb <;>
    rcases hc with rfl | hc <;> rcases hd with rfl | hd
  all_goals try exact hs _ ha _ hb _ hc _ hd he
  all_goals try have ba := hbound _ ha
  all_goals try have bb := hbound _ hb
  all_goals try have bc := hbound _ hc
  all_goals try have bd := hbound _ hd
  all_goals omega

theorem endpoint_sidon_exists (k : ℕ) :
    ∃ S : Finset ℤ, ∃ m : ℤ, S.card = k+1 ∧ 0 ∈ S ∧ 0 ≤ m ∧
      (∀ x ∈ S, 0 ≤ x ∧ x ≤ m) ∧ EndpointSidon S := by
  induction k with
  | zero =>
    refine ⟨{0},0,by simp,by simp,by omega,?_,?_⟩
    · simp
    · intro a ha b hb c hc d hd _
      simp only [Finset.mem_singleton] at ha hb hc hd
      exact Or.inl ⟨by omega,by omega⟩
  | succ k ih =>
    obtain ⟨S,m,hcard,hzero,hm,hbound,hs⟩ := ih
    have hx : 2*m+1 ∉ S := by
      intro h
      have := hbound _ h
      omega
    refine ⟨insert (2*m+1) S,2*m+1,?_,?_,by omega,?_,
      endpoint_sidon_insert S m hm hbound hs⟩
    · rw [Finset.card_insert_of_not_mem hx,hcard]
    · exact Finset.mem_insert_of_mem hzero
    · intro x hx
      rcases Finset.mem_insert.mp hx with rfl | hx
      · omega
      · have := hbound x hx; omega

/-- The only permitted nontrivial sum collision has the prescribed center sum r. -/
def EndpointCenteredSidon (A : Finset ℤ) (r : ℤ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A, ∀ d ∈ A, a+b=c+d →
    (a=c ∧ b=d) ∨ (a=d ∧ b=c) ∨ a+b=r

def endpointSymmetricFamily (S : Finset ℤ) (m : ℤ) : Finset ℤ :=
  S ∪ reflectedSource S (4*m+1)

@[simp] theorem mem_endpointSymmetricFamily (S : Finset ℤ) (m x : ℤ) :
    x ∈ endpointSymmetricFamily S m ↔ x∈S ∨ 4*m+1-x∈S := by
  simp [endpointSymmetricFamily]

theorem endpoint_symmetric_centered (S : Finset ℤ) (m : ℤ) (hm : 0 ≤ m)
    (hbound : ∀ x ∈ S, 0 ≤ x ∧ x ≤ m) (hs : EndpointSidon S) :
    EndpointCenteredSidon (endpointSymmetricFamily S m) (4*m+1) := by
  intro a ha b hb c hc d hd he
  simp only [mem_endpointSymmetricFamily] at ha hb hc hd
  rcases ha with ha | ha <;> rcases hb with hb | hb <;>
    rcases hc with hc | hc <;> rcases hd with hd | hd
  all_goals
    have ba := hbound _ ha
    have bb := hbound _ hb
    have bc := hbound _ hc
    have bd := hbound _ hd
  all_goals first
    | omega
    | (have h := hs _ ha _ hb _ hc _ hd (by omega)
       rcases h with ⟨h₁,h₂⟩ | ⟨h₁,h₂⟩ <;> omega)
    | (have h := hs _ ha _ hd _ hc _ hb (by omega)
       rcases h with ⟨h₁,h₂⟩ | ⟨h₁,h₂⟩ <;> omega)
    | (have h := hs _ ha _ hc _ hb _ hd (by omega)
       rcases h with ⟨h₁,h₂⟩ | ⟨h₁,h₂⟩ <;> omega)

theorem endpoint_symmetric_card (S : Finset ℤ) (m : ℤ) (hm : 0 ≤ m)
    (hbound : ∀ x ∈ S, 0 ≤ x ∧ x ≤ m) :
    (endpointSymmetricFamily S m).card = 2*S.card := by
  have hdis : Disjoint S (reflectedSource S (4*m+1)) := by
    apply Finset.disjoint_left.mpr
    intro x hx hy
    have h₁ := hbound x hx
    have h₂ := hbound _ ((mem_reflectedSource S (4*m+1) x).mp hy)
    omega
  have hc : (reflectedSource S (4*m+1)).card = S.card := by
    unfold reflectedSource
    apply Finset.card_image_of_injective
    intro x y he
    dsimp at he
    omega
  rw [endpointSymmetricFamily,Finset.card_union_of_disjoint hdis,hc]
  omega

theorem endpoint_center_corner_sum (A : Finset ℤ) (r : ℤ)
    (hs : EndpointCenteredSidon A r) (x y d : ℤ) (hd : 0<d)
    (h₁ : strictSource (fun a => a∈A) (x,y))
    (h₂ : strictSource (fun a => a∈A) (x+d,y))
    (h₃ : strictSource (fun a => a∈A) (x+d,y+d)) :
    x+d+y=r := by
  have h := hs x h₁.1 (y+d) h₃.2.1 (x+d) h₂.1 y h₁.2.1 (by omega)
  have hyx := h₁.2.2
  rcases h with ⟨h,_⟩ | ⟨h,_⟩ | h <;> omega

def endpointCenterColor (r : ℤ) (p : Point) : Bool := decide (p.1+p.2≠r)

theorem endpoint_center_proper (A : Finset ℤ) (r : ℤ)
    (hs : EndpointCenteredSidon A r) :
    properOn (strictSource (fun a => a∈A)) (endpointCenterColor r) := by
  intro x y d hd h₁ h₂ h₃
  have hc := endpoint_center_corner_sum A r hs x y d hd h₁ h₂ h₃
  have hfirst : x+y≠r := by omega
  simp [endpointCenterColor,hfirst,hc]

theorem endpoint_center_forcing (A : Finset ℤ) (r : ℤ)
    (hs : EndpointCenteredSidon A r) : AllForcing A (endpointCenterColor r) := by
  intro x y d hd h₁ h₂ h₃
  have hc := endpoint_center_corner_sum A r hs x y d hd h₁ h₂ h₃
  have hfirst : x+y≠r := by omega
  have hlast : x+d+(y+d)≠r := by omega
  simp [endpointCenterColor,hfirst,hlast]

theorem endpoint_symmetric_sharp (A : Finset ℤ) (r : ℤ)
    (hrp : 0<r) (hzero : 0∈A) (hr : r∈A)
    (hbound : ∀ x∈A, 0≤x ∧ x≤r)
    (hsymm : ∀ x∈A, r-x∈A) (hs : EndpointCenteredSidon A r) :
    e0 A = A.card-2 := by
  have hA : ∀ x∈A, 0≤x := fun x hx => (hbound x hx).1
  have hrB : r∈A.erase 0 := Finset.mem_erase.mpr ⟨by omega,hr⟩
  have hupper := exceptional_anchor_bound A hA hzero (endpointCenterColor r)
    (endpoint_center_proper A r hs) (endpoint_center_forcing A r hs)
    true r hrB (by simp [endpointCenterColor])
  have hmem : ∀ x∈(A.erase 0).erase r, (x,r)∈endpointArcs A := by
    intro x hx
    rcases Finset.mem_erase.mp hx with ⟨hxr,hx⟩
    rcases Finset.mem_erase.mp hx with ⟨hx0,hx⟩
    have hb := hbound x hx
    exact (mem_endpointArcs A hA x r).mpr
      ⟨hx,hr,by omega,by omega,hsymm x hx⟩
  have hlower := Finset.card_le_card_of_injOn (fun x : ℤ => (x,r)) hmem
    (by intro x hx y hy he; exact congrArg Prod.fst he)
  have hsize : ((A.erase 0).erase r).card = A.card-2 := by
    rw [Finset.card_erase_of_mem hrB,Finset.card_erase_of_mem hzero]
    omega
  change ((A.erase 0).erase r).card ≤ e0 A at hlower
  omega

/-- Unbounded sharpness: a different explicit greedy Sidon construction proves the
    same existence assertion as the base-R family in the manuscript. -/
theorem endpoint_anchor_sharp (k : ℕ) :
    ∃ A : Finset ℤ, ∃ r : ℤ, ∃ z : Point → Bool,
      A.card=2*k+2 ∧ 0∈A ∧ (∀ x∈A, 0≤x) ∧ r∈A.erase 0 ∧
      properOn (strictSource (fun a => a∈A)) z ∧ AllForcing A z ∧
      (∀ a∈A.erase 0, z (a,0)=true ↔ a≠r) ∧ e0 A=A.card-2 := by
  obtain ⟨S,m,hcard,hzero,hm,hbound,hs⟩ := endpoint_sidon_exists k
  let A := endpointSymmetricFamily S m
  let r : ℤ := 4*m+1
  have hrp : 0<r := by dsimp [r]; omega
  have hzA : 0∈A := (mem_endpointSymmetricFamily S m 0).mpr (Or.inl hzero)
  have hrA : r∈A := by
    apply (mem_endpointSymmetricFamily S m r).mpr
    right
    simpa [r] using hzero
  have hbounds : ∀ x∈A, 0≤x ∧ x≤r := by
    intro x hx
    rcases (mem_endpointSymmetricFamily S m x).mp hx with hx | hx
    · have := hbound x hx; dsimp [r]; omega
    · have := hbound _ hx; dsimp [r]; omega
  have hsymm : ∀ x∈A, r-x∈A := by
    intro x hx
    rcases (mem_endpointSymmetricFamily S m x).mp hx with hx | hx
    · apply (mem_endpointSymmetricFamily S m (r-x)).mpr
      right
      simpa [r] using hx
    · exact (mem_endpointSymmetricFamily S m (r-x)).mpr (Or.inl hx)
  have hcenter : EndpointCenteredSidon A r := endpoint_symmetric_centered S m hm hbound hs
  refine ⟨A,r,endpointCenterColor r,?_,hzA,?_,?_,
    endpoint_center_proper A r hcenter,endpoint_center_forcing A r hcenter,?_,
    endpoint_symmetric_sharp A r hrp hzA hrA hbounds hsymm hcenter⟩
  · have h := endpoint_symmetric_card S m hm hbound
    dsimp [A]
    omega
  · exact fun x hx => (hbounds x hx).1
  · exact Finset.mem_erase.mpr ⟨by omega,hrA⟩
  · simp [endpointCenterColor]

#print axioms endpoint_anchor_sharp

end EnergyForcing.Counting
