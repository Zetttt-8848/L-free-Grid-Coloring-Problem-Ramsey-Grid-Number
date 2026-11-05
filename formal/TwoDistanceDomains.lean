import TwoDistanceGeometry

set_option autoImplicit false

namespace EnergyForcing.TwoDistance

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Extend a map defined only on the source; outside values play no role. -/
noncomputable def extendSource (A : Finset ℤ) (f : {a : ℤ // a∈A} → E) (x : ℤ) : E :=
  if h : x∈A then f ⟨x,h⟩ else 0

theorem extendSource_mem (A : Finset ℤ) (f : {a : ℤ // a∈A} → E)
    (x : ℤ) (hx : x∈A) : extendSource A f x=f ⟨x,hx⟩ := by
  simp [extendSource,hx]

theorem subtype_embedding_hypotheses (A : Finset ℤ)
    (f : {a : ℤ // a∈A} → E) (tau : ℝ) (htau : 0<tau)
    (hinj : Function.Injective f)
    (hfreiman : ∀a b c d : {a : ℤ // a∈A},
      a.val+b.val=c.val+d.val → f a+f b=f c+f d)
    (hdist : ∀a b : {a : ℤ // a∈A}, a≠b → ‖f a-f b‖^2=tau ∨ ‖f a-f b‖^2=2*tau) :
    Hypotheses A (extendSource A f) tau := by
  refine ⟨htau,?_,?_,?_⟩
  · intro a ha b hb he
    rw [extendSource_mem A f a ha,extendSource_mem A f b hb] at he
    exact congrArg Subtype.val (hinj he)
  · intro a ha b hb c hc d hd he
    simp only [extendSource_mem A f a ha,extendSource_mem A f b hb,
      extendSource_mem A f c hc,extendSource_mem A f d hd]
    exact hfreiman ⟨a,ha⟩ ⟨b,hb⟩ ⟨c,hc⟩ ⟨d,hd⟩ he
  · intro a ha b hb hne
    rw [extendSource_mem A f a ha,extendSource_mem A f b hb]
    exact hdist ⟨a,ha⟩ ⟨b,hb⟩ (fun h => hne (congrArg Subtype.val h))

end EnergyForcing.TwoDistance
