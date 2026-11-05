import GraphSourceSets

set_option autoImplicit false

namespace EnergyForcing.GraphSources

open Finset
open scoped BigOperators

noncomputable def decode {r : ℕ} (x : ℤ) : Finset (Fin r) := Function.invFun mark x

theorem decode_mark {r : ℕ} (e : Finset (Fin r)) : decode (mark e)=e :=
  Function.leftInverse_invFun mark_injective e

noncomputable def graphColor (r : ℕ) (p : Point) : Bool := by
  classical
  exact decide (Disjoint (@decode r p.1) (@decode r p.2))

/-- The actual integer source attached to every simple edge family has a proper coloring. -/
theorem graphSource_proper {r : ℕ} (edges : Finset (Finset (Fin r)))
    (hedges : ∀e∈edges, e.card=2) :
    properOn (strictSource (fun x => x∈graphSource edges)) (graphColor r) := by
  classical
  intro x y d hd h₁ h₂ h₃ hmono
  obtain ⟨a,ha,hax⟩ := Finset.mem_image.mp h₁.1
  obtain ⟨b,hb,hby⟩ := Finset.mem_image.mp h₁.2.1
  obtain ⟨g,hg,hgz⟩ := Finset.mem_image.mp h₂.1
  obtain ⟨h,hh,hhw⟩ := Finset.mem_image.mp h₃.2.1
  dsimp at hax hby hgz hhw
  have hab : a≠b := by intro he; subst b; have hxy := h₁.2.2; omega
  have hag : a≠g := by intro he; subst g; omega
  have hdeg : ∀i, edgeDigits a i+edgeDigits h i=edgeDigits g i+edgeDigits b i := by
    apply (pair_sum_fidelity a h g b).mp
    omega
  have hdis := (nontrivial_pair_disjoint a h g b (hedges a ha) (hedges h hh)
    (hedges g hg) (hedges b hb) hdeg hag hab).2
  have hcross := cross_pair_not_disjoint a h g b (hedges a ha) (hedges g hg) hdeg hag
  have hx : @decode r x=a := by rw [← hax,decode_mark]
  have hy : @decode r y=b := by rw [← hby,decode_mark]
  have hz : @decode r (x+d)=g := by rw [← hgz,decode_mark]
  have hc := hmono.1
  simp [graphColor,hx,hy,hz,hcross,hdis] at hc

/-- Graph marks have no nonconstant three-term arithmetic progression. -/
theorem graphSource_no_progression {r : ℕ} (edges : Finset (Finset (Fin r)))
    (a b c : ℤ) (ha : a∈graphSource edges) (hb : b∈graphSource edges)
    (hc : c∈graphSource edges) (he : a+c=b+b) : a=b ∧ c=b := by
  obtain ⟨e,he',rfl⟩ := Finset.mem_image.mp ha
  obtain ⟨f,hf',rfl⟩ := Finset.mem_image.mp hb
  obtain ⟨g,hg',rfl⟩ := Finset.mem_image.mp hc
  have hdeg := (pair_sum_fidelity f f e g).mp he.symm
  have hh := repeated_pair_unique f e g hdeg
  simp [← hh.1,← hh.2]

def vertexVector {r : ℕ} (e : Finset (Fin r)) : Fin r → ℝ := fun i => edgeDigits e i

theorem vertexVector_injective {r : ℕ} : Function.Injective (@vertexVector r) := by
  intro e f he
  apply edgeDigits_injective
  funext i
  have hi := congrFun he i
  unfold vertexVector at hi
  exact_mod_cast hi

theorem vector_pair_sum_fidelity {r : ℕ} (e f g h : Finset (Fin r)) :
    mark e+mark f=mark g+mark h ↔ vertexVector e+vertexVector f=vertexVector g+vertexVector h := by
  rw [pair_sum_fidelity]
  constructor
  · intro hh
    funext i
    have hi := hh i
    change (edgeDigits e i:ℝ)+edgeDigits f i=(edgeDigits g i:ℝ)+edgeDigits h i
    exact_mod_cast hi
  · intro hh i
    have hi := congrFun hh i
    change (edgeDigits e i:ℝ)+edgeDigits f i=(edgeDigits g i:ℝ)+edgeDigits h i at hi
    exact_mod_cast hi

end EnergyForcing.GraphSources
