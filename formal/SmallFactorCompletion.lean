import ProgressionSix
import SharpSmallFactors

set_option autoImplicit false
namespace EnergyForcing.Counting

theorem properOn_affine_pullback (S A : Finset ℤ) (a q : ℤ) (hq:0< q)
    (hsub:∀x∈S,a+q*x∈A) (z : Point→Bool)
    (hz:properOn (strictSource (·∈A)) z) :
    properOn (strictSource (·∈S)) (fun p=> z (a+q*p.1,a+q*p.2)) := by
  intro x y h hh h1 h2 h3
  rcases h1 with ⟨hx,hy,hyx⟩
  rcases h2 with ⟨hxh,_,hyxh⟩
  rcases h3 with ⟨_,hyh,hyhxh⟩
  have hp:q*h>0:=mul_pos hq hh
  have haxh:a+q*x+q*h∈A:=by convert hsub (x+h) hxh using 1 <;> ring
  have hayh:a+q*y+q*h∈A:=by convert hsub (y+h) hyh using 1 <;> ring
  have horder:a+q*y< a+q*x:=by nlinarith [mul_pos hq (show 0< x-y by omega)]
  have h:=hz (a+q*x) (a+q*y) (q*h) hp
    ⟨hsub x hx,hsub y hy,horder⟩ ⟨haxh,hsub y hy,by omega⟩ ⟨haxh,hayh,by omega⟩
  convert h using 1 <;> ring_nf

theorem six_AP_not_proper (A : Finset ℤ) (hn:A.card=6)
    (hAP:IsArithmeticProgression A) (z : Point→Bool)
    (hz:properOn (strictSource (·∈A)) z) : False := by
  obtain ⟨a,d,hd,hrepr⟩:=hAP
  rw [hn] at hrepr
  have hsub:∀x∈progressionSet 0 1 6,a+d*x∈A:=by
    intro x hx
    obtain ⟨i,hi,he⟩:=(mem_progressionSet 0 1 x 6).mp hx
    have he':(i:ℤ)=x:=by simpa using he
    rw [hrepr]
    exact (mem_progressionSet a d _ 6).mpr ⟨i,hi,by rw [he']⟩
  exact no_two_color_progression_six _ (properOn_affine_pullback _ A a d hd hsub z hz)

theorem left_factor_proper (B C : Finset ℤ) (Q : ℤ) (hC:C.Nonempty)
    (z : Point→Bool) (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    ∃w:Point→Bool,properOn (strictSource (·∈B)) w := by
  obtain ⟨c,hc⟩:=hC
  exact ⟨_,properOn_affine_pullback B (scaledSum B C Q) (Q*c) 1 (by omega)
    (fun b hb=>(mem_scaledSum B C Q _).mpr ⟨b,hb,c,hc,by ring⟩) z hz⟩

theorem right_factor_proper (B C : Finset ℤ) (Q : ℤ) (hQ:0< Q) (hB:B.Nonempty)
    (z : Point→Bool) (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    ∃w:Point→Bool,properOn (strictSource (·∈C)) w := by
  obtain ⟨b,hb⟩:=hB
  exact ⟨_,properOn_affine_pullback C (scaledSum B C Q) b Q hQ
    (fun c hc=>(mem_scaledSum B C Q _).mpr ⟨b,hb,c,hc,rfl⟩) z hz⟩

theorem six_mark_proper_bounds (A : Finset ℤ) (hn:A.card=6) (z : Point→Bool)
    (hz:properOn (strictSource (·∈A)) z) : T A≤16 ∧ E A≤130 := by
  apply six_mark_nonAP_bounds A hn
  exact fun hAP=> six_AP_not_proper A hn hAP z hz

theorem six_mark_factor_bounds (B C : Finset ℤ) (Q : ℤ)
    (hQ:2*(span B:ℤ)< Q) (hB:2≤ B.card) (hC:2≤ C.card)
    (z : Point→Bool) (hz:properOn (strictSource (·∈scaledSum B C Q)) z) :
    (B.card=6 → T B≤16 ∧ E B≤130) ∧ (C.card=6 → T C≤16 ∧ E C≤130) := by
  obtain ⟨zb,hzb⟩:=left_factor_proper B C Q (Finset.card_pos.mp (by omega)) z hz
  obtain ⟨zc,hzc⟩:=right_factor_proper B C Q (by omega) (Finset.card_pos.mp (by omega)) z hz
  exact ⟨fun hn=> six_mark_proper_bounds B hn zb hzb,fun hn=> six_mark_proper_bounds C hn zc hzc⟩

end EnergyForcing.Counting
