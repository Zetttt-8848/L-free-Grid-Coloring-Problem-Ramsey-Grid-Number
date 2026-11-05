import SourceCounting
import Geometry

set_option autoImplicit false

namespace EnergyForcing.GraphSources

open Finset
open scoped BigOperators

/-- Base-five evaluation of a finite vector of natural digits. -/
def code {r : ℕ} (v : Fin r → ℕ) : ℕ := ∑i, v i*5^i.val

theorem code_succ {r : ℕ} (v : Fin (r+1) → ℕ) :
    code v=v 0+5*code (fun i : Fin r => v i.succ) := by
  simp only [code,Fin.sum_univ_succ,Fin.val_zero,Fin.val_succ,pow_zero,mul_one,pow_succ]
  rw [Finset.mul_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro i hi
  ring

/-- Carry-free digit uniqueness, not an assumed Freiman property. -/
theorem code_injective {r : ℕ} (v w : Fin r → ℕ)
    (hv : ∀i, v i<5) (hw : ∀i, w i<5) (he : code v=code w) : v=w := by
  induction r with
  | zero => funext i; exact Fin.elim0 i
  | succ r ih =>
    rw [code_succ,code_succ] at he
    have he0 : v 0=w 0 := by
      have hm := congrArg (fun n : ℕ => n%5) he
      simpa [Nat.add_mod,Nat.mul_mod,Nat.mod_eq_of_lt (hv 0),Nat.mod_eq_of_lt (hw 0)] using hm
    have het : code (fun i : Fin r => v i.succ)=code (fun i : Fin r => w i.succ) := by omega
    have hs := ih _ _ (fun i => hv i.succ) (fun i => hw i.succ) het
    funext i
    refine Fin.cases he0 ?_ i
    intro j
    exact congrFun hs j

theorem code_add {r : ℕ} (v w : Fin r → ℕ) :
    code (fun i => v i+w i)=code v+code w := by
  simp [code,add_mul,Finset.sum_add_distrib]

def edgeDigits {r : ℕ} (e : Finset (Fin r)) (i : Fin r) : ℕ := if i∈e then 1 else 0

def mark {r : ℕ} (e : Finset (Fin r)) : ℤ := (code (edgeDigits e):ℤ)

theorem edgeDigits_injective {r : ℕ} : Function.Injective (@edgeDigits r) := by
  intro e f he
  ext i
  have hi := congrFun he i
  simp only [edgeDigits] at hi
  split_ifs at hi <;> simp_all

theorem mark_injective {r : ℕ} : Function.Injective (@mark r) := by
  intro e f he
  unfold mark at he
  have hc : code (edgeDigits e)=code (edgeDigits f) := by exact_mod_cast he
  apply edgeDigits_injective
  exact code_injective _ _ (fun i => by unfold edgeDigits; split_ifs <;> norm_num)
    (fun i => by unfold edgeDigits; split_ifs <;> norm_num) hc

/-- Equality of two sums of graph marks is exactly equality of vertex degrees,
including repeated edges on either side. -/
theorem pair_sum_fidelity {r : ℕ} (e f g h : Finset (Fin r)) :
    mark e+mark f=mark g+mark h ↔
      ∀i, edgeDigits e i+edgeDigits f i=edgeDigits g i+edgeDigits h i := by
  constructor
  · intro he
    unfold mark at he
    have hn : code (edgeDigits e)+code (edgeDigits f)=
        code (edgeDigits g)+code (edgeDigits h) := by exact_mod_cast he
    rw [← code_add,← code_add] at hn
    have hh := code_injective _ _
      (fun i => by unfold edgeDigits; split_ifs <;> norm_num)
      (fun i => by unfold edgeDigits; split_ifs <;> norm_num) hn
    exact fun i => congrFun hh i
  · intro he
    have hh : (fun i => edgeDigits e i+edgeDigits f i)=
        (fun i => edgeDigits g i+edgeDigits h i) := funext he
    have hc := congrArg code hh
    rw [code_add,code_add] at hc
    unfold mark
    exact_mod_cast hc

theorem mark_pair {r : ℕ} (i j : Fin r) (hij : i≠j) :
    mark {i,j}=(5:ℤ)^i.val+(5:ℤ)^j.val := by
  have he : code (edgeDigits {i,j})=5^i.val+5^j.val := by
    unfold code edgeDigits
    simp only [ite_mul,one_mul,zero_mul]
    rw [← Finset.sum_filter]
    have hs : (Finset.univ.filter fun k : Fin r => k∈({i,j}:Finset (Fin r)))={i,j} := by
      ext k
      simp
    rw [hs]
    simp [hij]
  unfold mark
  exact_mod_cast he

def graphSource {r : ℕ} (edges : Finset (Finset (Fin r))) : Finset ℤ := edges.image mark

theorem graphSource_card {r : ℕ} (edges : Finset (Finset (Fin r))) :
    (graphSource edges).card=edges.card := by
  exact Finset.card_image_of_injective _ mark_injective

end EnergyForcing.GraphSources
