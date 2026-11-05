import WeightedEmbeddingCounts
import LineCounting
set_option autoImplicit false

namespace EnergyForcing.WeightedEmbedding

open Finset
open scoped BigOperators
open EnergyForcing.Counting EnergyForcing.ShiftCounting EnergyForcing.WeightedEmbeddingCounts

abbrev EmbeddingIndex := Σ _ : ℕ, ℤ×ℤ

def scales (N m : ℕ) : Finset ℕ := Finset.Ico 1 ((N-2)/(m-2)+1)
def embeddings (N m : ℕ) : Finset EmbeddingIndex :=
  (scales N m).sigma (translationCells N m)

/-- p=(alpha+beta+1,alpha) parametrizes the gap-coordinate translations. -/
def embedPoint (e : EmbeddingIndex) (p : Point) : Point :=
  (e.2.1-(e.1:ℤ)+(e.1:ℤ)*p.1,e.2.2+(e.1:ℤ)*p.2)

def embedCorner (e : EmbeddingIndex) (q : ℤ×ℤ×ℤ) : ℤ×ℤ×ℤ :=
  (e.2.1-(e.1:ℤ)+(e.1:ℤ)*q.1,e.2.2+(e.1:ℤ)*q.2.1,
    e.2.1-(e.1:ℤ)+(e.1:ℤ)*q.2.2)

theorem embedding_scale_pos (N m : ℕ) (e : EmbeddingIndex) (he : e∈embeddings N m) :
    1 ≤ e.1 := by
  exact (Finset.mem_Ico.mp (Finset.mem_sigma.mp he).1).1

theorem embedPoint_mem (N m : ℕ) (hm : 3 ≤ m) (e : EmbeddingIndex)
    (he : e∈embeddings N m) (p : Point)
    (hp : strictSource (fun a => a∈shifts m) p) :
    strictSource (fun a => a∈shifts N) (embedPoint e p) := by
  rcases e with ⟨d,a,b⟩
  rcases p with ⟨x,y⟩
  have hd := embedding_scale_pos N m ⟨d,a,b⟩ he
  dsimp at hd
  have ht := (Finset.mem_sigma.mp he).2
  rcases (mem_sourceCells (shifts (N-d*(m-2))) a b).mp ht with ⟨ha,hb,hba⟩
  have ha' := (mem_shifts _ a).mp ha
  have hb' := (mem_shifts _ b).mp hb
  have hx := (mem_shifts _ x).mp hp.1
  have hy := (mem_shifts _ y).mp hp.2.1
  have hyx := hp.2.2
  have hLZ : (0:ℤ)<((N-d*(m-2):ℕ):ℤ) :=
    lt_of_le_of_lt hb'.1 (lt_trans hba ha'.2)
  have hL : 0<N-d*(m-2) := by exact_mod_cast hLZ
  have hprod : d*(m-2) ≤ N := Nat.le_of_lt (Nat.sub_pos_iff_lt.mp hL)
  have hw : ((N-d*(m-2):ℕ):ℤ)=(N:ℤ)-(d:ℤ)*((m:ℤ)-2) := by
    rw [Nat.cast_sub hprod,Nat.cast_mul,Nat.cast_sub (by omega : 2 ≤ m)]
    norm_num
  rw [hw] at ha' hb'
  have hd' : (0:ℤ)<d := by omega
  simp only [strictSource,embedPoint,mem_shifts]
  refine ⟨⟨?_,?_⟩,⟨?_,?_⟩,?_⟩ <;> nlinarith

theorem embedPoint_injective (e : EmbeddingIndex) (hd : 1 ≤ e.1) :
    Function.Injective (embedPoint e) := by
  rintro ⟨x,y⟩ ⟨v,u⟩ h
  have hx := congrArg Prod.fst h
  have hy := congrArg Prod.snd h
  dsimp [embedPoint] at hx hy
  have hd' : (e.1:ℤ)≠0 := by omega
  apply Prod.ext
  · exact mul_left_cancel₀ hd' (by linarith)
  · exact mul_left_cancel₀ hd' (by linarith)

theorem embedCorner_mem (N m : ℕ) (hm : 3 ≤ m) (e : EmbeddingIndex)
    (he : e∈embeddings N m) (q : ℤ×ℤ×ℤ)
    (hq : q∈sourceCorners (shifts m)) : embedCorner e q∈sourceCorners (shifts N) := by
  rcases q with ⟨x,y,z⟩
  rcases (mem_sourceCorners (shifts m) x y z).mp hq with ⟨hx,hy,hz,hyx,hxz,hw⟩
  have h₁ := embedPoint_mem N m hm e he (x,y) ⟨hx,hy,hyx⟩
  have h₂ := embedPoint_mem N m hm e he (z,y) ⟨hz,hy,by omega⟩
  have h₃ := embedPoint_mem N m hm e he (z,y+z-x) ⟨hz,hw,by omega⟩
  have hd := embedding_scale_pos N m e he
  simp only [embedPoint,strictSource] at h₁ h₂ h₃
  simp only [embedCorner,mem_sourceCorners]
  refine ⟨h₁.1,h₁.2.1,h₂.1,h₁.2.2,?_,?_⟩
  · have hd' : (0:ℤ)<e.1 := by omega
    nlinarith
  · convert h₃.2.1 using 1; ring

theorem embedCorner_step (e : EmbeddingIndex) (_hd : 1 ≤ e.1)
    (q : ℤ×ℤ×ℤ) (hq : q.1<q.2.2) :
    cornerStep (embedCorner e q)=e.1*cornerStep q := by
  have hq' : (cornerStep q:ℤ)=q.2.2-q.1 := by dsimp [cornerStep]; omega
  have he : (embedCorner e q).2.2-(embedCorner e q).1=
      (e.1:ℤ)*(q.2.2-q.1) := by simp [embedCorner]; ring
  have hz : 0 ≤ (e.1:ℤ)*(q.2.2-q.1) := mul_nonneg (Int.natCast_nonneg _) (by omega)
  have hleft : (cornerStep (embedCorner e q):ℤ)=(e.1:ℤ)*(q.2.2-q.1) := by
    unfold cornerStep
    rw [he]
    omega
  have hall : (cornerStep (embedCorner e q):ℤ)=((e.1*cornerStep q:ℕ):ℤ) := by
    rw [Nat.cast_mul,hq',hleft]
  exact_mod_cast hall

/-- A fixed local corner and its image determine both the scale and the translation. -/
theorem embedCorner_parameters_injective (q : ℤ×ℤ×ℤ) (hq : q.1<q.2.2) :
    Function.Injective (fun e : EmbeddingIndex => embedCorner e q) := by
  rintro ⟨d,a,b⟩ ⟨d',a',b'⟩ he
  have hx := congrArg Prod.fst he
  have hy := congrArg (fun p : ℤ×ℤ×ℤ => p.2.1) he
  have hz := congrArg (fun p : ℤ×ℤ×ℤ => p.2.2) he
  dsimp [embedCorner] at hx hy hz
  have hmul : (d:ℤ)*(q.2.2-q.1)=(d':ℤ)*(q.2.2-q.1) := by nlinarith
  have hdZ : (d:ℤ)=(d':ℤ) := mul_right_cancel₀ (by omega) hmul
  have hd : d=d' := by exact_mod_cast hdZ
  subst d'
  have ha : a=a' := by linarith
  have hb : b=b' := by linarith
  simp [ha,hb]

def RainbowPred (c : Point → Fin 3) (q : ℤ×ℤ×ℤ) : Prop :=
  c (q.1,q.2.1)≠c (q.2.2,q.2.1) ∧
    c (q.1,q.2.1)≠c (q.2.2,q.2.1+q.2.2-q.1) ∧
    c (q.2.2,q.2.1)≠c (q.2.2,q.2.1+q.2.2-q.1)

instance (c : Point → Fin 3) (q : ℤ×ℤ×ℤ) : Decidable (RainbowPred c q) :=
  inferInstanceAs (Decidable (_∧_∧_))

def rainbows (c : Point → Fin 3) (m : ℕ) : Finset (ℤ×ℤ×ℤ) :=
  (sourceCorners (shifts m)).filter (RainbowPred c)

theorem rainbow_embedding (c : Point → Fin 3) (e : EmbeddingIndex) (q : ℤ×ℤ×ℤ) :
    RainbowPred (fun p => c (embedPoint e p)) q ↔ RainbowPred c (embedCorner e q) := by
  have he : e.2.2+(e.1:ℤ)*(q.2.1+q.2.2-q.1)=
      e.2.2+(e.1:ℤ)*q.2.1+(e.2.1-(e.1:ℤ)+(e.1:ℤ)*q.2.2)-
        (e.2.1-(e.1:ℤ)+(e.1:ℤ)*q.1) := by ring
  simp only [RainbowPred,embedPoint,embedCorner,he]

theorem proper_embedding (N m : ℕ) (hm : 3 ≤ m) (e : EmbeddingIndex)
    (he : e∈embeddings N m) (c : Point → Fin 3)
    (hc : properOn (strictSource (fun a => a∈shifts N)) c) :
    properOn (strictSource (fun a => a∈shifts m)) (fun p => c (embedPoint e p)) := by
  intro x y h hh h₁ h₂ h₃ hmono
  have hi₁ := embedPoint_mem N m hm e he (x,y) h₁
  have hi₂ := embedPoint_mem N m hm e he (x+h,y) h₂
  have hi₃ := embedPoint_mem N m hm e he (x+h,y+h) h₃
  have hd := embedding_scale_pos N m e he
  have hstep : (0:ℤ)<(e.1:ℤ)*h := mul_pos (by omega) hh
  have hx : e.2.1-(e.1:ℤ)+(e.1:ℤ)*(x+h)=
      e.2.1-(e.1:ℤ)+(e.1:ℤ)*x+(e.1:ℤ)*h := by ring
  have hy : e.2.2+(e.1:ℤ)*(y+h)=e.2.2+(e.1:ℤ)*y+(e.1:ℤ)*h := by ring
  simp only [embedPoint,hx,hy] at hi₁ hi₂ hi₃ hmono
  exact hc _ _ _ hstep hi₁ hi₂ hi₃ hmono

theorem rainbows_card_eq (c : Point → Fin 3) (N : ℕ) :
    (rainbows c N).card=
      EnergyForcing.LineCounting.rainbowCount (fun x y => c ((x:ℤ),(y:ℤ))) N := by
  rw [EnergyForcing.LineCounting.rainbowCount,
    EnergyForcing.LineCounting.cornerSum_source_bridge]
  simp only [rainbows,Finset.card_eq_sum_ones,Finset.sum_filter]
  apply Finset.sum_congr rfl
  rintro ⟨x,y,z⟩ hq
  rcases (mem_sourceCorners (shifts N) x y z).mp hq with ⟨hx,hy,hz,hyx,hxz,_⟩
  have hx' := (mem_shifts N x).mp hx
  have hy' := (mem_shifts N y).mp hy
  have hz' := (mem_shifts N z).mp hz
  have ex : (x.toNat:ℤ)=x := by omega
  have ey : (y.toNat:ℤ)=y := by omega
  have ez : (z.toNat:ℤ)=z := by omega
  have ew : ((y.toNat+z.toNat-x.toNat:ℕ):ℤ)=y+z-x := by omega
  simp only [EnergyForcing.LineCounting.isRainbow,RainbowPred,ex,ey,ez,ew]

theorem rainbows_card_upper (c : Point → Fin 3) (N : ℕ) (hN : 1 ≤ N)
    (hc : properOn (strictSource (fun a => a∈shifts N)) c) :
    (rainbows c N).card ≤ N.choose 2-(N-1)+(N-1)/3 := by
  rw [rainbows_card_eq]
  exact EnergyForcing.LineCounting.rainbowCount_upper _ N hN
    (EnergyForcing.LineCounting.properOn_triangle_bridge c N hc)

theorem square_triangle_proper (N : ℕ) (c : Point → Fin 3) (hc : properL N c) :
    properOn (strictSource (fun a => a∈shifts N)) (fun p => c (p.1+1,p.2+1)) := by
  intro x y h hh h₁ h₂ h₃ heq
  have hb : ∀p : Point, strictSource (fun a => a∈shifts N) p →
      square N (p.1+1,p.2+1) := by
    intro p hp
    have hx := (mem_shifts N p.1).mp hp.1
    have hy := (mem_shifts N p.2).mp hp.2.1
    simp only [square]
    omega
  have hp := hb (x,y) h₁
  have hq := hb (x+h,y) h₂
  have hr := hb (x+h,y+h) h₃
  have hx : x+h+1=x+1+h := by omega
  have hy : y+h+1=y+1+h := by omega
  simp only [hx,hy] at hq hr heq
  exact hc (x+1) (y+1) h hh hp hq hr heq

end EnergyForcing.WeightedEmbedding

