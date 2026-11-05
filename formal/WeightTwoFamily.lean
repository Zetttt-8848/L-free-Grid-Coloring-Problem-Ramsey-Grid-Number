import CompleteGraphCounts
import GraphSourceEuclidean

set_option autoImplicit false

namespace EnergyForcing.GraphSources
open Finset
open scoped BigOperators Topology
open EnergyForcing.Counting
open Filter

theorem cast_choose_four (r : ℕ) : (r.choose 4:ℝ)=
    (r:ℝ)*(r-1)*(r-2)*(r-3)/24 := by
  rw [Nat.cast_choose_eq_descPochhammer_div]
  norm_num [descPochhammer_eval_eq_prod_range,Finset.prod_range_succ]

 theorem complete_source_pairs (r : ℕ) : (M (graphSource (completeEdges r)):ℝ)=
    (r:ℝ)*(r-1)*(r-2)*(r+1)/8 := by
  unfold M
  rw [Nat.cast_choose_two,complete_source_card,Nat.cast_choose_two]
  ring

 theorem complete_source_ratio (r : ℕ) (hr : 3 ≤ r) :
    (T (graphSource (completeEdges r)):ℝ)/M (graphSource (completeEdges r))=
      2*((r:ℝ)-3)/(r+1) := by
  have hrR : (3:ℝ) ≤ r := by exact_mod_cast hr
  rw [complete_source_corners,Nat.cast_mul,complete_source_pairs,cast_choose_four]
  push_cast
  have h0 : (r:ℝ)≠0 := by linarith
  have h1 : (r:ℝ)-1≠0 := by linarith
  have h2 : (r:ℝ)-2≠0 := by linarith
  have hp : (r:ℝ)+1≠0 := by linarith
  field_simp
  <;> ring

 theorem complete_source_ratio_limit : Tendsto (fun r : ℕ =>
    (T (graphSource (completeEdges r)):ℝ)/M (graphSource (completeEdges r))) atTop (𝓝 2) := by
  have hlim : Tendsto (fun r : ℕ => (2:ℝ)-8/((r:ℝ)+1)) atTop (𝓝 2) := by
    have hh := (tendsto_const_nhds (x:=(2:ℝ)) (f:=atTop)).sub (tendsto_one_div_add_atTop_nhds_zero_nat.const_mul 8)
    simpa only [mul_one_div,mul_zero,sub_zero] using hh
  apply hlim.congr'
  filter_upwards [eventually_ge_atTop 3] with r hr
  rw [complete_source_ratio r hr]
  have hp : (r:ℝ)+1≠0 := by positivity
  field_simp
  <;> ring

 theorem complete_source_pairs_pos (r : ℕ) (hr : 3 ≤ r) :
    0<(M (graphSource (completeEdges r)):ℝ) := by
  rw [complete_source_pairs]
  have hh : (3:ℝ) ≤ r := by exact_mod_cast hr
  have h0 : (0:ℝ)<r := by linarith
  have h1 : (0:ℝ)<r-1 := by linarith
  have h2 : (0:ℝ)<r-2 := by linarith
  positivity

/-- Any coefficient valid for this family is at least two. -/
theorem graph_coefficient_sharp (κ : ℝ)
    (hκ : ∀r : ℕ, 3 ≤ r → (T (graphSource (completeEdges r)):ℝ) ≤
      κ*M (graphSource (completeEdges r))) : 2 ≤ κ := by
  apply le_of_tendsto complete_source_ratio_limit
  filter_upwards [eventually_ge_atTop 3] with r hr
  exact (div_le_iff₀ (complete_source_pairs_pos r hr)).mpr (hκ r hr)

 theorem complete_source_proper (r : ℕ) :
    properOn (strictSource (fun x => x∈graphSource (completeEdges r))) (graphColor r) :=
  graphSource_proper (completeEdges r) (fun e he => completeEdges_edge_card e he)

end EnergyForcing.GraphSources

