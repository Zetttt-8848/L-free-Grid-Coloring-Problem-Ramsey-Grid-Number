import GraphMidpointBridge
import WeightTwoFamily

set_option autoImplicit false

namespace EnergyForcing.TwoDistance

open EnergyForcing.GraphSources EnergyForcing.Counting

theorem complete_midpoint_family (r : ℕ) :
    Hypotheses (graphSource (completeEdges r)) (graphEmbedding r) 2 ∧
    (∀c, (midpointPairs (points (graphSource (completeEdges r)) (graphEmbedding r)) 2 c).card≤3) ∧
    properOn (strictSource (fun x => x∈graphSource (completeEdges r))) (graphColor r) := by
  exact ⟨graph_embedding_hypotheses _ (fun e he => completeEdges_edge_card e he),
    fun c => graph_midpoint_cap _ (fun e he => completeEdges_edge_card e he) c,
    complete_source_proper r⟩

/-- A uniform coefficient for the midpoint-three subclass must be at least two. -/
theorem midpoint_three_coefficient_sharp (κ : ℝ)
    (hκ : ∀r : ℕ, 3≤r →
      Hypotheses (graphSource (completeEdges r)) (graphEmbedding r) 2 →
      (∀c, (midpointPairs (points (graphSource (completeEdges r)) (graphEmbedding r)) 2 c).card≤3) →
      (T (graphSource (completeEdges r)):ℝ)≤κ*M (graphSource (completeEdges r))) :
    2≤κ := by
  apply graph_coefficient_sharp
  intro r hr
  exact hκ r hr (complete_midpoint_family r).1 (complete_midpoint_family r).2.1

end EnergyForcing.TwoDistance
