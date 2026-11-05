import ArithmeticProgressions

set_option autoImplicit false
set_option maxHeartbeats 2000000
namespace EnergyForcing.Counting

theorem no_two_color_progression_six (z : Point→Bool)
    (hz:properOn (strictSource (·∈progressionSet 0 1 6)) z) : False := by
  have h102:=hz 1 0 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h103:=hz 1 0 2 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h203:=hz 2 0 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h213:=hz 2 1 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h104:=hz 1 0 3 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h204:=hz 2 0 2 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h214:=hz 2 1 2 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h304:=hz 3 0 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h314:=hz 3 1 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h324:=hz 3 2 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h105:=hz 1 0 4 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h205:=hz 2 0 3 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h215:=hz 2 1 3 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h305:=hz 3 0 2 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h315:=hz 3 1 2 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h325:=hz 3 2 2 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h405:=hz 4 0 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h415:=hz 4 1 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h425:=hz 4 2 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  have h435:=hz 4 3 1 (by norm_num) (by unfold strictSource; decide) (by unfold strictSource; decide) (by unfold strictSource; decide)
  norm_num at h102 h103 h203 h213 h104 h204 h214 h304 h314 h324 h105 h205 h215 h305 h315 h325 h405 h415 h425 h435
  clear hz
  all_goals cases hc10 : z (1,0) <;> simp_all
  all_goals cases hc20 : z (2,0) <;> simp_all
  all_goals cases hc21 : z (2,1) <;> simp_all
  all_goals cases hc30 : z (3,0) <;> simp_all
  all_goals cases hc31 : z (3,1) <;> simp_all
  all_goals cases hc32 : z (3,2) <;> simp_all
  all_goals cases hc40 : z (4,0) <;> simp_all
  all_goals cases hc41 : z (4,1) <;> simp_all
  all_goals cases hc42 : z (4,2) <;> simp_all
  all_goals cases hc43 : z (4,3) <;> simp_all
  all_goals cases hc50 : z (5,0) <;> simp_all
  all_goals cases hc51 : z (5,1) <;> simp_all
  all_goals cases hc52 : z (5,2) <;> simp_all
  all_goals cases hc53 : z (5,3) <;> simp_all
  all_goals cases hc54 : z (5,4) <;> simp_all

end EnergyForcing.Counting
