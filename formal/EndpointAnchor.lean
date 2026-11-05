import EndpointCounting

namespace EnergyForcing.Counting

/-- The parallel endpoints of every source corner have the same color. -/
def AllForcing (A : Finset ℤ) (z : Point → Bool) : Prop :=
  ∀ x y d : ℤ, 0 < d →
    strictSource (fun a => a ∈ A) (x,y) →
    strictSource (fun a => a ∈ A) (x+d,y) →
    strictSource (fun a => a ∈ A) (x+d,y+d) →
    z (x,y) = z (x+d,y+d)

theorem forcing_addition_colors (A : Finset ℤ) (hzero : 0 ∈ A)
    (z : Point → Bool)
    (hp : properOn (strictSource (fun a => a ∈ A)) z)
    (hf : AllForcing A z) (x y : ℤ)
    (hx : x ∈ A) (hy : y ∈ A) (hxp : 0 < x) (hyp : 0 < y)
    (hs : x+y ∈ A) :
    z (x,0) = z (y,0) ∧ z (x,0) ≠ z (x+y,0) := by
  have h₁ : strictSource (fun a => a ∈ A) (x,0) := ⟨hx,hzero,hxp⟩
  have h₂ : strictSource (fun a => a ∈ A) (x+y,0) := ⟨hs,hzero,by omega⟩
  have h₃ : strictSource (fun a => a ∈ A) (x+y,y) := ⟨hs,hy,by omega⟩
  have he := hf x 0 y hyp h₁ h₂ (by simpa using h₃)
  have hn : z (x,0) ≠ z (x+y,0) := by
    intro h
    apply hp x 0 y hyp h₁ h₂ (by simpa using h₃)
    exact ⟨h,by simpa using h.symm.trans he⟩
  have g₁ : strictSource (fun a => a ∈ A) (y,0) := ⟨hy,hzero,hyp⟩
  have g₂ : strictSource (fun a => a ∈ A) (y+x,0) := by simpa [add_comm] using h₂
  have g₃ : strictSource (fun a => a ∈ A) (y+x,x) :=
    ⟨by simpa [add_comm] using hs,hx,by omega⟩
  have ge := hf y 0 x hxp g₁ g₂ (by simpa using g₃)
  have gn : z (y,0) ≠ z (x+y,0) := by
    intro h
    apply hp y 0 x hxp g₁ g₂ (by simpa using g₃)
    have h' : z (y,0) = z (y+x,0) := by simpa [add_comm] using h
    exact ⟨h',by simpa using h'.symm.trans ge⟩
  constructor
  · cases hxv : z (x,0) <;> cases hyv : z (y,0) <;>
      cases hsv : z (x+y,0) <;> simp_all
  · exact hn

theorem uniform_anchor_zero (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a)
    (hzero : 0 ∈ A) (z : Point → Bool)
    (hp : properOn (strictSource (fun a => a ∈ A)) z)
    (hf : AllForcing A z) (s : Bool)
    (huniform : ∀ a ∈ A.erase 0, z (a,0) = s) : e0 A = 0 := by
  unfold e0
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_not_mem.mpr
  rintro ⟨x,w⟩ hw
  rcases (mem_endpointArcs A hA x w).mp hw with ⟨hx,hw,hxp,hxw,hd⟩
  have hc := forcing_addition_colors A hzero z hp hf x (w-x)
    hx hd hxp (by omega) (by simpa using hw)
  have hxs := huniform x (Finset.mem_erase.mpr ⟨by omega,hx⟩)
  have hws := huniform w (Finset.mem_erase.mpr ⟨by omega,hw⟩)
  apply hc.2
  simpa using hxs.trans hws.symm

theorem exceptional_anchor_arc (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a)
    (hzero : 0 ∈ A) (z : Point → Bool)
    (hp : properOn (strictSource (fun a => a ∈ A)) z)
    (hf : AllForcing A z) (s : Bool) (r : ℤ)
    (hexception : ∀ a ∈ A.erase 0, z (a,0) = s ↔ a ≠ r)
    (x w : ℤ) (harc : (x,w) ∈ endpointArcs A) :
    w = r ∨ (x = r ∧ w = 2*r) := by
  rcases (mem_endpointArcs A hA x w).mp harc with ⟨hx,hw,hxp,hxw,hd⟩
  by_cases hwr : w = r
  · exact Or.inl hwr
  · right
    have hc := forcing_addition_colors A hzero z hp hf x (w-x)
      hx hd hxp (by omega) (by simpa using hw)
    have hws : z (w,0) = s :=
      (hexception w (Finset.mem_erase.mpr ⟨by omega,hw⟩)).mpr hwr
    have hxr : x = r := by
      by_contra hne
      have hxs := (hexception x (Finset.mem_erase.mpr ⟨by omega,hx⟩)).mpr hne
      apply hc.2
      simpa using hxs.trans hws.symm
    have hyr : w-x = r := by
      by_contra hne
      have hys := (hexception (w-x) (Finset.mem_erase.mpr ⟨by omega,hd⟩)).mpr hne
      apply hc.2
      simpa using hc.1.trans (hys.trans hws.symm)
    exact ⟨hxr,by omega⟩

/-- Charge each arc to a distinct regular anchor: x for x→r, and 2r for r→2r. -/
theorem exceptional_anchor_bound (A : Finset ℤ) (hA : ∀ a ∈ A, 0 ≤ a)
    (hzero : 0 ∈ A) (z : Point → Bool)
    (hp : properOn (strictSource (fun a => a ∈ A)) z)
    (hf : AllForcing A z) (s : Bool) (r : ℤ) (hr : r ∈ A.erase 0)
    (hexception : ∀ a ∈ A.erase 0, z (a,0) = s ↔ a ≠ r) :
    e0 A ≤ A.card - 2 := by
  have hrp : 0 < r := by
    have hrA := (Finset.mem_erase.mp hr).2
    have hr0 := (Finset.mem_erase.mp hr).1
    have := hA r hrA
    omega
  let charge : (ℤ × ℤ) → ℤ := fun p => if p.2 = r then p.1 else p.2
  have hclass := exceptional_anchor_arc A hA hzero z hp hf s r hexception
  have hmem : ∀ p ∈ endpointArcs A, charge p ∈ (A.erase 0).erase r := by
    rintro ⟨x,w⟩ hp
    rcases (mem_endpointArcs A hA x w).mp hp with ⟨hx,hw,hxp,hxw,hd⟩
    rcases hclass x w hp with hwr | ⟨hxr,hwr⟩
    · simp only [charge,hwr,if_pos]
      exact Finset.mem_erase.mpr ⟨by omega,Finset.mem_erase.mpr ⟨by omega,hx⟩⟩
    · have hne : w ≠ r := by omega
      simp only [charge,if_neg hne]
      exact Finset.mem_erase.mpr ⟨hne,Finset.mem_erase.mpr ⟨by omega,hw⟩⟩
  have hinj : Set.InjOn charge (↑(endpointArcs A) : Set (ℤ × ℤ)) := by
    rintro ⟨x,w⟩ hp ⟨x',w'⟩ hq he
    have hc := hclass x w hp
    have hd := hclass x' w' hq
    have hxw := ((mem_endpointArcs A hA x w).mp hp).2.2.2.1
    have hxw' := ((mem_endpointArcs A hA x' w').mp hq).2.2.2.1
    dsimp [charge] at he
    by_cases hwr : w = r <;> by_cases hwr' : w' = r
    · simp only [hwr,hwr',if_pos] at he
      exact Prod.ext he (by omega)
    · simp only [hwr,if_pos,if_neg hwr'] at he
      rcases hd with h | ⟨h₁,h₂⟩ <;> omega
    · simp only [hwr',if_pos,if_neg hwr] at he
      rcases hc with h | ⟨h₁,h₂⟩ <;> omega
    · simp only [if_neg hwr,if_neg hwr'] at he
      rcases hc with h | ⟨h₁,h₂⟩
      · exact False.elim (hwr h)
      rcases hd with h | ⟨h₃,h₄⟩
      · exact False.elim (hwr' h)
      exact Prod.ext (by omega) he
  have hcard := Finset.card_le_card_of_injOn charge hmem hinj
  have hsize : ((A.erase 0).erase r).card = A.card - 2 := by
    rw [Finset.card_erase_of_mem hr,Finset.card_erase_of_mem hzero]
    omega
  simpa only [e0,hsize] using hcard

#print axioms uniform_anchor_zero
#print axioms exceptional_anchor_bound

end EnergyForcing.Counting
