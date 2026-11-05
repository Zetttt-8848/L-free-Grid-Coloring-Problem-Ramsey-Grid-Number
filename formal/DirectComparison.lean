import SmallFactorBounds

set_option autoImplicit false
namespace EnergyForcing.Counting

noncomputable def smallEnergyProfile (n : ℕ) : ℝ := if n=6 then 130 else (n:ℝ)*(2*(n:ℝ)^2+1)/3

theorem smallEnergyProfile_nonneg (n : ℕ) : 0≤ smallEnergyProfile n := by
  unfold smallEnergyProfile
  split_ifs <;> positivity

theorem smallEnergyProfile_comparison (b c : ℕ) (hb:2≤ b) (hc:b≤ c) (hc6:c≤6) :
    2*smallEnergyProfile b*smallEnergyProfile c≤27*((b:ℝ)*c)^2-25*((b:ℝ)*c) := by
  have hb6:b≤6:=by omega
  interval_cases b <;> interval_cases c <;> norm_num [smallEnergyProfile] at *

theorem direct_energy_comparison (b c : ℕ) (hb:2≤ b) (hbc:b≤ c)
    (e f : ℝ) (he:0≤ e) (hf:0≤ f)
    (heSmall:b≤6 → e≤ smallEnergyProfile b)
    (hfSmall:c≤6 → f≤ smallEnergyProfile c)
    (hfGolomb:f≤6*(c:ℝ)^2-5*c)
    (heCap:7≤ c → e≤3*(b:ℝ)^2-2*b)
    (hfCap4:5≤ b → f≤5*(c:ℝ)^2-4*c)
    (hfCap2:7≤ b → f≤3*(c:ℝ)^2-2*c)
    (heFour:b=4 → 7≤ c → e≤36) :
    2*e*f≤27*((b:ℝ)*c)^2-25*((b:ℝ)*c) := by
  by_cases hc6:c≤6
  · have hh:=mul_le_mul (heSmall (by omega)) (hfSmall hc6) hf (smallEnergyProfile_nonneg b)
    have hp:=smallEnergyProfile_comparison b c hb hbc hc6
    nlinarith
  · have hc7:7≤ c:=by omega
    have hcr:(7:ℝ)≤ c:=by exact_mod_cast hc7
    have hecap:=heCap hc7
    by_cases hb6:b≤6
    · interval_cases b
      · have heb:=heSmall (by omega)
        norm_num [smallEnergyProfile] at heb
        have hp:=mul_le_mul heb hfGolomb hf (by norm_num: (0:ℝ)≤6)
        norm_num
        nlinarith
      · have heb:=heSmall (by omega)
        norm_num [smallEnergyProfile] at heb
        have hp:=mul_le_mul heb hfGolomb hf (by norm_num: (0:ℝ)≤19)
        norm_num
        nlinarith
      · have heb:=heFour rfl hc7
        have hp:=mul_le_mul heb hfGolomb hf (by norm_num: (0:ℝ)≤36)
        norm_num
        nlinarith
      · have hfcap:=hfCap4 (by omega)
        norm_num at hecap
        have hp:=mul_le_mul hecap hfcap hf (by norm_num: (0:ℝ)≤65)
        norm_num
        nlinarith
      · have hfcap:=hfCap4 (by omega)
        norm_num at hecap
        have hp:=mul_le_mul hecap hfcap hf (by norm_num: (0:ℝ)≤96)
        norm_num
        nlinarith
    · have hb7:7≤ b:=by omega
      have hbr:(7:ℝ)≤ b:=by exact_mod_cast hb7
      have hfcap:=hfCap2 hb7
      have heb:e≤3*(b:ℝ)^2:=by nlinarith
      have hfb:f≤3*(c:ℝ)^2:=by nlinarith
      have hp:=mul_le_mul heb hfb hf (by positivity:0≤3*(b:ℝ)^2)
      have hprod:(49:ℝ)≤(b:ℝ)*c:=by nlinarith [mul_nonneg (sub_nonneg.mpr hbr) (sub_nonneg.mpr hcr)]
      nlinarith [sq_nonneg ((b:ℝ)*c-49)]

end EnergyForcing.Counting
