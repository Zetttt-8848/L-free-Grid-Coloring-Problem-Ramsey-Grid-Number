import WeightedEmbeddingGeometry
set_option autoImplicit false

namespace EnergyForcing.WeightedEmbedding

open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.ShiftCounting EnergyForcing.WeightedEmbeddingCounts

def LocalRainbow (m rho : ℕ) : Prop :=
  ∀ c : Point → Fin 3, properOn (strictSource (fun a => a∈shifts m)) c →
    rho ≤ (rainbows c m).card

def weightedCopies (N m : ℕ) (a : ℕ → ℝ) : ℝ :=
  ∑d ∈ scales N m, a d*((N-d*(m-2)).choose 2:ℝ)

def load (m : ℕ) (a : ℕ → ℝ) (h : ℕ) : ℝ :=
  ∑j ∈ Finset.Ico 1 (m-1), if j∣h then ((m-j).choose 2:ℝ)*a (h/j) else 0

def localCharge (N m : ℕ) (a : ℕ → ℝ) (q r : ℤ×ℤ×ℤ) : ℝ :=
  ∑e ∈ embeddings N m, if embedCorner e q=r then a e.1 else 0

theorem weightedCopies_eq (N m : ℕ) (a : ℕ → ℝ) :
    weightedCopies N m a=∑e ∈ embeddings N m, a e.1 := by
  simp only [weightedCopies,embeddings,Finset.sum_sigma]
  apply Finset.sum_congr rfl
  intro d hd
  simp only [Finset.sum_const, nsmul_eq_mul, translationCells_card]
  ring

/-- Fixed local and host corners determine at most one labeled embedding. -/
theorem localCharge_bound (N m : ℕ) (a : ℕ → ℝ) (ha : ∀d, 0 ≤ a d)
    (q r : ℤ×ℤ×ℤ) (hq : q∈sourceCorners (shifts m)) :
    localCharge N m a q r  ≤ 
      if cornerStep q∣cornerStep r then a (cornerStep r/cornerStep q) else 0 := by
  have hqpos := ((mem_sourceCorners (shifts m) q.1 q.2.1 q.2.2).mp hq).2.2.2.2.1
  have hj := (cornerStep_bounds m q hq).1
  let F := (embeddings N m).filter (fun e => embedCorner e q=r)
  have hcard : F.card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro e he f hf
    exact embedCorner_parameters_injective q hqpos
      ((Finset.mem_filter.mp he).2.trans (Finset.mem_filter.mp hf).2.symm)
  by_cases hF : F.Nonempty
  · obtain ⟨e,he⟩ := hF
    have he' := Finset.mem_filter.mp he
    have hs := embedCorner_step e (embedding_scale_pos N m e he'.1) q hqpos
    rw [he'.2] at hs
    have hdiv : cornerStep q∣cornerStep r := ⟨e.1,by simpa [Nat.mul_comm] using hs⟩
    rw [if_pos hdiv]
    have hscale : ∀f∈F, f.1=cornerStep r/cornerStep q := by
      intro f hf
      have hf' := Finset.mem_filter.mp hf
      have ht := embedCorner_step f (embedding_scale_pos N m f hf'.1) q hqpos
      rw [hf'.2] at ht
      rw [ht,Nat.mul_div_cancel _ (by omega : 0<cornerStep q)]
    have heq : localCharge N m a q r=(F.card:ℝ)*a (cornerStep r/cornerStep q) := by
      unfold localCharge
      rw [← Finset.sum_filter]
      change (∑f∈F, a f.1)=_
      calc
        _ = ∑f∈F, a (cornerStep r/cornerStep q) :=
          Finset.sum_congr rfl (fun f hf => by rw [hscale f hf])
        _ = _ := by simp [nsmul_eq_mul]
    rw [heq]
    have hcard' : (F.card:ℝ) ≤ 1 := by exact_mod_cast hcard
    nlinarith [ha (cornerStep r/cornerStep q)]
  · have he : localCharge N m a q r=0 := by
      unfold localCharge
      apply Finset.sum_eq_zero
      intro e he
      rw [if_neg (by intro hh; exact hF ⟨e,Finset.mem_filter.mpr ⟨he,hh⟩⟩)]
    rw [he]
    split_ifs
    · exact ha _
    · exact le_refl _

theorem totalCharge_bound (N m : ℕ) (a : ℕ → ℝ) (ha : ∀d,0 ≤ a d)
    (r : ℤ×ℤ×ℤ) :
    (∑q ∈ sourceCorners (shifts m), localCharge N m a q r) ≤ load m a (cornerStep r) := by
  calc
    _  ≤  ∑q ∈ sourceCorners (shifts m),
        if cornerStep q∣cornerStep r then a (cornerStep r/cornerStep q) else 0 :=
      Finset.sum_le_sum (fun q hq => localCharge_bound N m a ha q r hq)
    _ = _ := by
      have hmaps : ∀q∈sourceCorners (shifts m), cornerStep q∈Finset.Ico 1 (m-1) := by
        intro q hq
        have hh := cornerStep_bounds m q hq
        have hm : 3 ≤ m := by
          rcases q with ⟨x,y,z⟩
          rcases (mem_sourceCorners (shifts m) x y z).mp hq with ⟨hx,hy,hz,hyx,hxz,_⟩
          have hx' := (mem_shifts m x).mp hx
          have hy' := (mem_shifts m y).mp hy
          have hz' := (mem_shifts m z).mp hz
          omega
        exact Finset.mem_Ico.mpr ⟨hh.1,by omega⟩
      rw [← Finset.sum_fiberwise_of_maps_to' hmaps
        (fun j => if j∣cornerStep r then a (cornerStep r/j) else 0)]
      unfold load
      apply Finset.sum_congr rfl
      intro j hj
      change (∑q∈stepCorners m j, if j∣cornerStep r then a (cornerStep r/j) else 0)=_
      rw [Finset.sum_const, nsmul_eq_mul, stepCorners_card m j (Finset.mem_Ico.mp hj).1]
      split_ifs <;> simp

/-- Weighted double counting over an actual map into the finite host set. -/
theorem weighted_incidence_count {E L H : Type*} [DecidableEq E] [DecidableEq L]
    [DecidableEq H] (es : Finset E) (ls : Finset L) (hs : Finset H)
    (f : E → L → H) (w : E → ℝ) (P : H → Prop) [DecidablePred P]
    (hmap : ∀e∈es, ∀q∈ls, f e q∈hs) :
    (∑e∈es, w e*((ls.filter fun q => P (f e q)).card:ℝ))=
      ∑r∈hs.filter P, ∑q∈ls, ∑e∈es, if f e q=r then w e else 0 := by
  have hleft : (∑e∈es, w e*((ls.filter fun q => P (f e q)).card:ℝ))=
      ∑q∈ls, ∑e∈es, if P (f e q) then w e else 0 := by
    simp only [Finset.card_eq_sum_ones,Finset.sum_filter,Nat.cast_sum,Nat.cast_ite,
      Nat.cast_one,Nat.cast_zero,Finset.mul_sum,mul_ite,mul_one,mul_zero]
    exact Finset.sum_comm
  rw [hleft,Finset.sum_comm (s:=hs.filter P) (t:=ls)]
  apply Finset.sum_congr rfl
  intro q hq
  symm
  calc
    _ = ∑r∈hs, ∑e∈es.filter (fun e => f e q=r), if P (f e q) then w e else 0 := by
      rw [Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro r hr
      by_cases hp : P r
      · rw [if_pos hp,← Finset.sum_filter]
        apply Finset.sum_congr rfl
        intro e he
        rw [(Finset.mem_filter.mp he).2,if_pos hp]
      · rw [if_neg hp]
        symm
        apply Finset.sum_eq_zero
        intro e he
        rw [(Finset.mem_filter.mp he).2,if_neg hp]
    _ = _ := Finset.sum_fiberwise_of_maps_to (fun e he => hmap e he q hq) _

theorem weighted_rainbow_count (N m : ℕ) (hm : 3 ≤ m) (a : ℕ → ℝ)
    (c : Point → Fin 3) :
    (∑e∈embeddings N m, a e.1*(rainbows (fun p => c (embedPoint e p)) m).card)=
      ∑r∈rainbows c N, ∑q∈sourceCorners (shifts m), localCharge N m a q r := by
  have hi := weighted_incidence_count (embeddings N m) (sourceCorners (shifts m))
    (sourceCorners (shifts N)) embedCorner (fun e => a e.1) (RainbowPred c)
    (fun e he q hq => embedCorner_mem N m hm e he q hq)
  have he : ∀e, RainbowPred (fun p => c (embedPoint e p))=
      (fun q => RainbowPred c (embedCorner e q)) := by
    intro e
    funext q
    exact propext (rainbow_embedding c e q)
  simpa only [rainbows,he,localCharge] using hi

/-- The local hypothesis charges at least rho times the total embedding weight. -/
theorem weighted_rainbow_lower (N m rho : ℕ) (hm : 3 ≤ m)
    (hlocal : LocalRainbow m rho) (a : ℕ → ℝ) (ha : ∀d,0 ≤ a d)
    (c : Point → Fin 3) (hc : properOn (strictSource (fun a => a∈shifts N)) c) :
    (rho:ℝ)*weightedCopies N m a  ≤ 
      ∑e∈embeddings N m, a e.1*(rainbows (fun p => c (embedPoint e p)) m).card := by
  rw [weightedCopies_eq,Finset.mul_sum]
  apply Finset.sum_le_sum
  intro e he
  have hb := hlocal (fun p => c (embedPoint e p)) (proper_embedding N m hm e he c hc)
  have hb' : (rho:ℝ) ≤ (rainbows (fun p => c (embedPoint e p)) m).card := by exact_mod_cast hb
  nlinarith [mul_le_mul_of_nonneg_left hb' (ha e.1)]

/-- Every host rainbow receives at most the divisor-sum load in the manuscript. -/
theorem weighted_rainbow_upper (N m : ℕ) (hm : 3 ≤ m) (a : ℕ → ℝ)
    (ha : ∀d,0 ≤ a d) (K : ℝ)
    (hK : ∀h : ℕ, 1 ≤ h → h ≤ N-2 → load m a h ≤ K) (c : Point → Fin 3) :
    (∑e∈embeddings N m, a e.1*(rainbows (fun p => c (embedPoint e p)) m).card) ≤ 
      K*(rainbows c N).card := by
  rw [weighted_rainbow_count N m hm a c]
  calc
    _  ≤  ∑r∈rainbows c N, K := by
      apply Finset.sum_le_sum
      intro r hr
      have hr' := (Finset.mem_filter.mp hr).1
      have hb := cornerStep_bounds N r hr'
      exact (totalCharge_bound N m a ha r).trans (hK (cornerStep r) hb.1 hb.2)
    _ = _ := by simp [nsmul_eq_mul,mul_comm]

/-- The first inequality of Lemma lem:weighted for arbitrary real nonnegative weights. -/
theorem weighted_embedding_charge (N m rho : ℕ) (hm : 3 ≤ m)
    (hlocal : LocalRainbow m rho) (a : ℕ → ℝ) (ha : ∀d,0 ≤ a d) (K : ℝ)
    (hK : ∀h : ℕ, 1 ≤ h → h ≤ N-2 → load m a h ≤ K)
    (c : Point → Fin 3) (hc : properOn (strictSource (fun a => a∈shifts N)) c) :
    (rho:ℝ)*weightedCopies N m a  ≤  K*(rainbows c N).card :=
  (weighted_rainbow_lower N m rho hm hlocal a ha c hc).trans
    (weighted_rainbow_upper N m hm a ha K hK c)

/-- Both inequalities of Lemma lem:weighted, with the exact U_N from the line count. -/
theorem weighted_embedding_implication (N m rho : ℕ) (hm : 3 ≤ m) (hNm : m ≤ N)
    (hlocal : LocalRainbow m rho) (a : ℕ → ℝ) (ha : ∀d,0 ≤ a d) (K : ℝ) (hK0 : 0 ≤ K)
    (hK : ∀h : ℕ, 1 ≤ h → h ≤ N-2 → load m a h ≤ K)
    (c : Point → Fin 3) (hc : properOn (strictSource (fun a => a∈shifts N)) c) :
    (rho:ℝ)*weightedCopies N m a  ≤  K*(rainbows c N).card ∧
      K*(rainbows c N).card  ≤  K*((N.choose 2-(N-1)+(N-1)/3:ℕ):ℝ) := by
  constructor
  · exact weighted_embedding_charge N m rho hm hlocal a ha K hK c hc
  · apply mul_le_mul_of_nonneg_left _ hK0
    exact_mod_cast rainbows_card_upper c N (by omega) hc

theorem weighted_embedding_ramsey (N m rho : ℕ) (hm : 3 ≤ m) (hNm : m ≤ N)
    (hlocal : LocalRainbow m rho) (a : ℕ → ℝ) (ha : ∀d,0 ≤ a d) (K : ℝ) (hK0 : 0 ≤ K)
    (hK : ∀h : ℕ, 1 ≤ h → h ≤ N-2 → load m a h ≤ K)
    (hstrict : K*((N.choose 2-(N-1)+(N-1)/3:ℕ):ℝ)<(rho:ℝ)*weightedCopies N m a) :
    ramseyL 3 N := by
  intro c hc
  have hh := weighted_embedding_implication N m rho hm hNm hlocal a ha K hK0 hK
    (fun p => c (p.1+1,p.2+1)) (square_triangle_proper N c hc)
  linarith [hh.1,hh.2]

end EnergyForcing.WeightedEmbedding

