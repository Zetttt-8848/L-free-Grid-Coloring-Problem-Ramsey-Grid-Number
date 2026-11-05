import SourceCounting
import Geometry
import Mathlib

set_option autoImplicit false

namespace EnergyForcing.TwoDistance

open EnergyForcing.Counting
open scoped RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- All hypotheses are restricted to A. Values of phi outside A are irrelevant. -/
structure Hypotheses (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ) : Prop where
  positive : 0 < tau
  injective : Set.InjOn phi (A : Set ℤ)
  freiman : ∀a∈A, ∀b∈A, ∀c∈A, ∀e∈A, a+b=c+e → phi a+phi b=phi c+phi e
  distances : ∀a∈A, ∀b∈A, a≠b → ‖phi a-phi b‖^2=tau ∨ ‖phi a-phi b‖^2=2*tau

theorem distance_bounds (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (a b : ℤ) (ha : a∈A) (hb : b∈A) (hne : a≠b) :
    tau ≤ ‖phi a-phi b‖^2 ∧ ‖phi a-phi b‖^2 ≤ 2*tau := by
  rcases h.distances a ha b hb hne with he|he <;> rw [he] <;> constructor <;> linarith [h.positive]

theorem no_progression (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) :
    ∀a∈A, ∀b∈A, ∀c∈A, a+c=b+b → a=b := by
  intro a ha b hb c hc he
  by_contra hab
  have hac : a≠c := by omega
  have hv := h.freiman a ha c hc b hb b hb he
  have hscale : phi c-phi a=(2 : ℝ) • (phi b-phi a) := by
    calc
      _ = (phi a+phi c)-phi a-phi a := by abel
      _ = (phi b+phi b)-phi a-phi a := by rw [hv]
      _ = _ := by rw [two_smul]; abel
  have hsquare : ‖phi c-phi a‖^2=4*‖phi b-phi a‖^2 := by
    rw [hscale,norm_smul]
    norm_num
    ring
  have h₁ := distance_bounds A phi tau h b a hb ha (Ne.symm hab)
  have h₂ := distance_bounds A phi tau h c a hc ha hac.symm
  nlinarith [h.positive]

/-- The parallelogram law forces every nontrivial equal-sum configuration
to have short sides, long diagonals and orthogonal adjacent sides. -/
theorem parallelogram_square (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (a b c e : ℤ)
    (ha : a∈A) (hb : b∈A) (hc : c∈A) (he : e∈A)
    (hab : a≠b) (hac : a≠c) (hae : a≠e) (hbc : b≠c)
    (hsum : a+e=b+c) :
    ‖phi b-phi a‖^2=tau ∧ ‖phi c-phi a‖^2=tau ∧
      ‖phi e-phi a‖^2=2*tau ∧ ‖phi b-phi c‖^2=2*tau ∧
      inner (𝕜 := ℝ) (phi b-phi a) (phi c-phi a) = 0 := by
  let u := phi b-phi a
  let v := phi c-phi a
  have hv := h.freiman a ha e he b hb c hc hsum
  have hplus : u+v=phi e-phi a := by
    dsimp [u,v]
    calc
      _ = (phi b+phi c)-phi a-phi a := by abel
      _ = (phi a+phi e)-phi a-phi a := by rw [hv]
      _ = _ := by abel
  have hminus : u-v=phi b-phi c := by dsimp [u,v]; abel
  have hu := distance_bounds A phi tau h b a hb ha hab.symm
  have hw := distance_bounds A phi tau h c a hc ha hac.symm
  have hd₁ := distance_bounds A phi tau h e a he ha hae.symm
  have hd₂ := distance_bounds A phi tau h b c hb hc hbc
  have hp := norm_add_sq_real u v
  have hm := norm_sub_sq_real u v
  rw [hplus] at hp
  rw [hminus] at hm
  dsimp [u,v] at hp hm
  constructor
  · nlinarith
  constructor
  · nlinarith
  constructor
  · nlinarith
  constructor <;> nlinarith

theorem corner_distances (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) (x y w : ℤ) (hq : (x,y,w)∈sourceCorners A) :
    ‖phi x-phi y‖^2=tau ∧ ‖phi w-phi (y+w-x)‖^2=tau ∧
      ‖phi w-phi y‖^2=2*tau := by
  rcases (mem_sourceCorners A x y w).mp hq with ⟨hx,hy,hw,hyx,hxw,ht⟩
  have hxt : x≠y+w-x := by
    intro he
    have hh := no_progression A phi tau h y hy x hx w hw (by omega)
    omega
  have hh := parallelogram_square A phi tau h y x (y+w-x) w hy hx ht hw
    (by omega) (by omega) (by omega) hxt (by omega)
  have hv := h.freiman y hy w hw x hx (y+w-x) ht (by omega)
  have hpar : phi w-phi (y+w-x)=phi x-phi y := by
    apply sub_eq_sub_iff_add_eq_add.mpr
    simpa [add_comm] using hv
  exact ⟨hh.1,by rw [hpar]; exact hh.1,hh.2.2.1⟩

noncomputable def distanceColor (phi : ℤ → E) (tau : ℝ) (p : Point) : Bool :=
  by classical exact decide (‖phi p.1-phi p.2‖^2=tau)

/-- Properness follows directly from the three actual squared cell distances. -/
theorem squared_distance_coloring_proper (A : Finset ℤ) (phi : ℤ → E) (tau : ℝ)
    (h : Hypotheses A phi tau) : properOn (strictSource (fun a => a∈A)) (distanceColor phi tau) := by
  intro x y d hd h₁ h₂ h₃ hmono
  have hq : (x,y,x+d)∈sourceCorners A := by
    apply (mem_sourceCorners A x y (x+d)).mpr
    refine ⟨h₁.1,h₁.2.1,h₂.1,h₁.2.2,by omega,?_⟩
    convert h₃.2.1 using 1 <;> omega
  have hc := corner_distances A phi tau h x y (x+d) hq
  have he := hmono.1
  simp only [distanceColor,hc.1,hc.2.2,decide_true] at he
  have hbad : 2*tau=tau := of_decide_eq_true he.symm
  linarith [h.positive]

end EnergyForcing.TwoDistance
