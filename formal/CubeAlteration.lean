import FiniteAlteration
import SourceCounting

set_option autoImplicit false

namespace EnergyForcing.CubeAlteration

open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.Alteration

abbrev Bits := Fin 5 → Bool
abbrev Path := Fin 6 → ℤ

def vertex (x : ℤ) (w : Fin 5 → ℤ) (b : Bits) : ℤ :=
  x + ∑i, if b i then w i else 0

def cube (x : ℤ) (w : Fin 5 → ℤ) : Finset ℤ := Finset.univ.image (vertex x w)

def CubeFree (A : Finset ℤ) : Prop :=
  ∀ (x : ℤ) (w : Fin 5 → ℤ), (∀i, 0 < w i) → Function.Injective (vertex x w) →
    ¬ cube x w ⊆ A

def steps (t : Path) (i : Fin 5) : ℤ := t i.succ - t i.castSucc
def pathCube (t : Path) := cube (t 0) (steps t)

def interval (N : ℕ) : Finset ℤ := Finset.Icc 1 (N : ℤ)

noncomputable def paths (N : ℕ) : Finset Path := by
  classical
  exact (Fintype.piFinset (fun _ : Fin 6 => interval N)).filter
    (fun t => StrictMono t ∧ Function.Injective (vertex (t 0) (steps t)))

theorem mem_paths (N : ℕ) (t : Path) :
    t∈paths N ↔ (∀i, t i∈interval N) ∧ StrictMono t ∧
      Function.Injective (vertex (t 0) (steps t)) := by
  classical
  simp [paths]

theorem interval_card (N : ℕ) : (interval N).card=N := by
  simp [interval, Int.card_Icc]

theorem steps_pos (t : Path) (ht : StrictMono t) (i : Fin 5) : 0 < steps t i := by
  exact sub_pos.mpr (ht (by exact i.castSucc_lt_succ))

theorem steps_sum (t : Path) : (∑i, steps t i)=t 5-t 0 := by
  simp only [Fin.sum_univ_succ, steps]
  change (t 1-t 0)+((t 2-t 1)+((t 3-t 2)+((t 4-t 3)+((t 5-t 4)+0))))=t 5-t 0
  ring

theorem vertex_bounds (x : ℤ) (w : Fin 5 → ℤ) (hw : ∀i,0 ≤ w i) (b : Bits) :
    x ≤ vertex x w b ∧ vertex x w b ≤ x+∑i,w i := by
  constructor
  · apply le_add_of_nonneg_right
    exact Finset.sum_nonneg (fun i _ => by split_ifs <;> first | exact hw i | rfl)
  · apply add_le_add_left
    exact Finset.sum_le_sum (fun i _ => by split_ifs <;> first | exact le_rfl | exact hw i)

theorem pathCube_subset (N : ℕ) (t : Path) (ht : t∈paths N) : pathCube t ⊆ interval N := by
  intro a ha
  obtain ⟨b,_,rfl⟩ := Finset.mem_image.mp ha
  have hh := (mem_paths N t).mp ht
  have hb := vertex_bounds (t 0) (steps t) (fun i => (steps_pos t hh.2.1 i).le) b
  have h0 := Finset.mem_Icc.mp (hh.1 0)
  have h5 := Finset.mem_Icc.mp (hh.1 5)
  rw [steps_sum] at hb
  exact Finset.mem_Icc.mpr ⟨by omega,by omega⟩

theorem pathCube_card (N : ℕ) (t : Path) (ht : t∈paths N) : (pathCube t).card=32 := by
  have hi := ((mem_paths N t).mp ht).2.2
  rw [pathCube, cube, Finset.card_image_of_injective _ hi, Finset.card_univ]
  decide

theorem pathCube_root (t : Path) : t 0∈pathCube t := by
  refine Finset.mem_image.mpr ⟨fun _ => false, Finset.mem_univ _, ?_⟩
  simp [vertex]

theorem paths_card_le (N : ℕ) : (paths N).card ≤ N.choose 6 := by
  classical
  have hcard : ((interval N).powersetCard 6).card=N.choose 6 := by
    rw [Finset.card_powersetCard,interval_card]
  rw [← hcard]
  refine Finset.card_le_card_of_injOn (fun t : Path => Finset.univ.image t) ?_ ?_
  · intro t ht
    have hh := (mem_paths N t).mp ht
    apply Finset.mem_powersetCard.mpr
    constructor
    · intro a ha
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp ha
      exact hh.1 i
    · rw [Finset.card_image_of_injective _ hh.2.1.injective]
      rfl
  · intro t ht u hu he
    have ht' := ((mem_paths N t).mp ht).2.1
    have hu' := ((mem_paths N u).mp hu).2.1
    apply (ht'.range_inj hu').mp
    simpa only [Finset.coe_image, Finset.coe_univ, Set.image_univ] using congrArg
      (fun X : Finset ℤ => (X : Set ℤ)) he

def cumulative (x : ℤ) (w : Fin 5 → ℤ) : Path :=
  ![x,x+w 0,x+w 0+w 1,x+w 0+w 1+w 2,x+w 0+w 1+w 2+w 3,
    x+w 0+w 1+w 2+w 3+w 4]

theorem cumulative_steps (x : ℤ) (w : Fin 5 → ℤ) : steps (cumulative x w)=w := by
  funext i
  fin_cases i <;> simp [steps,cumulative] <;> ring

theorem cumulative_zero (x : ℤ) (w : Fin 5 → ℤ) : cumulative x w 0=x := rfl

theorem cumulative_mono (x : ℤ) (w : Fin 5 → ℤ) (hw : ∀i,0 < w i) :
    StrictMono (cumulative x w) := by
  apply Fin.strictMono_iff_lt_succ.mpr
  intro i
  have hh := hw i
  have hs := congrFun (cumulative_steps x w) i
  dsimp [steps] at hs
  omega

theorem cumulative_mem (N : ℕ) (x : ℤ) (w : Fin 5 → ℤ) (hw : ∀i,0 < w i)
    (hi : Function.Injective (vertex x w)) (hA : cube x w ⊆ interval N) :
    cumulative x w∈paths N := by
  apply (mem_paths N _).mpr
  have hx : x∈cube x w := by
    refine Finset.mem_image.mpr ⟨fun _ => false, Finset.mem_univ _, ?_⟩
    simp [vertex]
  have ht : x+∑i,w i∈cube x w := by
    refine Finset.mem_image.mpr ⟨fun _ => true, Finset.mem_univ _, ?_⟩
    simp [vertex]
  have hb := Finset.mem_Icc.mp (hA hx)
  have he := Finset.mem_Icc.mp (hA ht)
  have hm := cumulative_mono x w hw
  refine ⟨?_,hm,?_⟩
  · intro i
    have h0 : cumulative x w 0 ≤ cumulative x w i := hm.monotone (Fin.zero_le i)
    have h5 : cumulative x w i ≤ cumulative x w 5 := hm.monotone (by omega)
    have hsum : cumulative x w 5 = x+∑i,w i := by simp [cumulative,Fin.sum_univ_succ]; ring
    rw [cumulative_zero] at h0
    rw [hsum] at h5
    exact Finset.mem_Icc.mpr ⟨by omega,by omega⟩
  · simpa only [cumulative_zero,cumulative_steps] using hi

theorem path_exclusion_cube_free (N : ℕ) (A : Finset ℤ) (hA : A ⊆ interval N)
    (h : ∀t∈paths N, ¬ pathCube t ⊆ A) : CubeFree A := by
  intro x w hw hi hcube
  apply h (cumulative x w) (cumulative_mem N x w hw hi (hcube.trans hA))
  simpa only [pathCube,cumulative_zero,cumulative_steps] using hcube

theorem choose_six_bound (N : ℕ) : (N.choose 6 : ℝ) ≤ (N : ℝ)^6/720 := by
  have hh := Nat.descFactorial_le_pow N 6
  rw [Nat.descFactorial_eq_factorial_mul_choose] at hh
  norm_num at hh
  have hr : (720 : ℝ)*(N.choose 6 : ℝ) ≤ (N : ℝ)^6 := by exact_mod_cast hh
  linarith

/-- Bernoulli selection and deletion of one actual cube vertex. -/
theorem cube_free_alteration (N : ℕ) (p : ℝ) (hp : 0 ≤ p) (hp1 : p ≤ 1) :
    ∃A⊆interval N, CubeFree A ∧
      (N : ℝ)*p - (N : ℝ)^6*p^32/720 ≤ (A.card : ℝ) := by
  obtain ⟨A,hA,hfree,hcard⟩ := finite_alteration (interval N) (paths N) pathCube
    (fun t => t 0) (pathCube_subset N) (fun t _ => pathCube_root t) p hp hp1
  refine ⟨A,hA,path_exclusion_cube_free N A hA hfree,?_⟩
  have he : (∑t∈paths N,p^(pathCube t).card)=(paths N).card*p^32 := by
    calc
      _ = ∑t∈paths N,p^32 := Finset.sum_congr rfl (fun t ht => by rw [pathCube_card N t ht])
      _ = _ := by simp
  rw [he,interval_card] at hcard
  have hc' : ((paths N).card : ℝ) ≤ (N.choose 6 : ℝ) := by exact_mod_cast paths_card_le N
  have hc : ((paths N).card : ℝ) ≤ (N : ℝ)^6/720 := hc'.trans (choose_six_bound N)
  have hm := mul_le_mul_of_nonneg_right hc (pow_nonneg hp 32)
  nlinarith

end EnergyForcing.CubeAlteration
