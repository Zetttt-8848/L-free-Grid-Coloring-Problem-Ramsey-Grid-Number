import FiberDominance
import Geometry
import UniversalCounting

namespace EnergyForcing.Forcing

open EnergyForcing.Counting
open EnergyForcing.FiberDominance
open scoped BigOperators

def forcedCorners (A : Finset ℤ) (z : Point → Bool) : Finset (ℤ × ℤ × ℤ) :=
  (sourceCorners A).filter fun p => z (p.1,p.2.1)=z (p.2.2,p.2.1+p.2.2-p.1)

def F (A : Finset ℤ) (z : Point → Bool) : ℕ := (forcedCorners A z).card

def inputCell (p : ℤ × ℤ × ℤ) (b : Bool) : Point :=
  if b then (p.2.2,p.2.1+p.2.2-p.1) else (p.1,p.2.1)

def outputCell (p : ℤ × ℤ × ℤ) : Point := (p.2.2,p.2.1)

def edgeOf (pb : (ℤ × ℤ × ℤ) × Bool) : Sym2 Point :=
  s(inputCell pb.1 pb.2, outputCell pb.1)

/-- Actual physical edges, identifying reversed endpoint pairs. -/
def edges (A : Finset ℤ) (z : Point → Bool) : Finset (Sym2 Point) :=
  ((forcedCorners A z).product Finset.univ).image edgeOf

def imbalanceSq (A : Finset ℤ) (z : Point → Bool) : ℤ :=
  ∑ d∈posDiffs A,
    ((fiberClass A z d true).card-(fiberClass A z d false).card : ℤ)^2

theorem corner_edge_injective (A : Finset ℤ) :
    Set.InjOn edgeOf ((sourceCorners A).product (Finset.univ : Finset Bool)) := by
  rintro ⟨⟨x,y,w⟩,b⟩ hp ⟨⟨x',y',w'⟩,b'⟩ hp' he
  have h := (mem_sourceCorners A x y w).mp (Finset.mem_product.mp hp).1
  have h' := (mem_sourceCorners A x' y' w').mp (Finset.mem_product.mp hp').1
  cases b <;> cases b' <;>
    simp only [edgeOf,inputCell,outputCell,Bool.false_eq_true,if_false,if_true,Sym2.eq_iff,Prod.mk.injEq] at he <;>
    rcases he with he | he <;> simp_all only [Prod.mk.injEq, and_true] <;> omega

theorem edge_count (A : Finset ℤ) (z : Point → Bool) : (edges A z).card=2*F A z := by
  have hi : Set.InjOn edgeOf ((forcedCorners A z).product (Finset.univ : Finset Bool)) :=
    (corner_edge_injective A).mono (by
      intro p hp
      exact Finset.mem_product.mpr ⟨(Finset.mem_filter.mp (Finset.mem_product.mp hp).1).1,(Finset.mem_product.mp hp).2⟩)
  rw [edges,Finset.card_image_of_injOn hi]
  simp [F,Nat.mul_comm,Finset.card_product]

theorem edge_vertices (A : Finset ℤ) (z : Point → Bool) (p q : Point)
    (he : s(p,q)∈edges A z) : p∈sourceCells A ∧ q∈sourceCells A := by
  obtain ⟨⟨⟨x,y,w⟩,b⟩,hp,heq⟩ := Finset.mem_image.mp he
  have hc := Finset.mem_filter.mp (Finset.mem_product.mp hp).1
  rcases (mem_sourceCorners A x y w).mp hc.1 with ⟨hx,hy,hw,hyx,hxw,ht⟩
  cases b <;>
    simp only [edgeOf,inputCell,outputCell,Bool.false_eq_true,if_false,if_true,Sym2.eq_iff] at heq <;>
    rcases heq with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ <;> simp only [mem_sourceCells] <;>
    constructor <;> constructor <;> first | assumption | (constructor <;> first | assumption | omega)

theorem edges_bipartite (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource fun x => x∈A) z)
    (p q : Point) (he : s(p,q)∈edges A z) : z p≠z q := by
  obtain ⟨⟨⟨x,y,w⟩,b⟩,hp,heq⟩ := Finset.mem_image.mp he
  have hc := Finset.mem_filter.mp (Finset.mem_product.mp hp).1
  rcases (mem_sourceCorners A x y w).mp hc.1 with ⟨hx,hy,hw,hyx,hxw,ht⟩
  have ht' : y+(w-x)=y+w-x := by ring
  have hw' : x+(w-x)=w := by ring
  have hproper := hz x y (w-x) (by omega) ⟨hx,hy,hyx⟩
    (by rw [hw']; exact ⟨hw,hy,by omega⟩)
    (by rw [hw',ht']; exact ⟨hw,ht,by omega⟩)
  rw [hw',ht'] at hproper
  have hforce : z (x,y)=z (w,y+w-x) := hc.2
  cases b <;>
    simp only [edgeOf,inputCell,outputCell,Bool.false_eq_true,if_false,if_true,Sym2.eq_iff] at heq <;>
    rcases heq with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩ <;> intro he <;> apply hproper <;> simp_all

theorem forced_fiber_card (A : Finset ℤ) (z : Point → Bool) (d : ℤ) (hd : 0<d) :
    ((forcedCorners A z).filter fun p => p.1-p.2.1=d).card =
      M (fiberClass A z d false)+M (fiberClass A z d true) := by
  let samePairs := (sourceCells (positiveFiber A d)).filter
    fun p => z (p.1+d,p.1)=z (p.2+d,p.2)
  have hb : ((forcedCorners A z).filter fun p => p.1-p.2.1=d).card = samePairs.card := by
    symm
    refine Finset.card_nbij' (fun p : ℤ×ℤ => (p.2+d,p.2,p.1+d))
      (fun p : ℤ×ℤ×ℤ => (p.2.1+p.2.2-p.1,p.2.1)) ?_ ?_ ?_ ?_
    · rintro ⟨v,u⟩ hp
      rcases Finset.mem_filter.mp hp with ⟨hp,hz⟩
      rcases (mem_sourceCells (positiveFiber A d) v u).mp hp with ⟨hv,hu,huv⟩
      rcases (mem_positiveFiber A d v).mp hv with ⟨hv,hvd⟩
      rcases (mem_positiveFiber A d u).mp hu with ⟨hu,hud⟩
      have he : u+(v+d)-(u+d)=v := by ring
      simp only [Finset.mem_filter,forcedCorners,mem_sourceCorners,he]
      exact ⟨⟨⟨hud,hu,hvd,by omega,by omega,hv⟩,hz.symm⟩,by omega⟩
    · rintro ⟨x,y,w⟩ hp
      simp only [Finset.mem_filter,forcedCorners,mem_sourceCorners] at hp
      rcases hp with ⟨⟨⟨hx,hy,hw,hyx,hxw,ht⟩,hz⟩,he⟩
      have he₁ : y+d=x := by omega
      have he₂ : y+w-x+d=w := by omega
      simp only [samePairs,Finset.mem_filter,mem_sourceCells,mem_positiveFiber,he₁,he₂]
      exact ⟨⟨⟨ht,hw⟩,⟨hy,hx⟩,by omega⟩,hz.symm⟩
    · rintro ⟨v,u⟩ _; apply Prod.ext <;> dsimp <;> omega
    · rintro ⟨x,y,w⟩ hp
      have he := (Finset.mem_filter.mp hp).2
      apply Prod.ext
      · dsimp at *; omega
      · apply Prod.ext <;> dsimp at * <;> omega
  have he : samePairs = sourceCells (fiberClass A z d false) ∪ sourceCells (fiberClass A z d true) := by
    ext ⟨v,u⟩
    simp only [samePairs,Finset.mem_filter,mem_sourceCells,Finset.mem_union,fiberClass]
    cases h₁ : z (v+d,v) <;> cases h₂ : z (u+d,u) <;> simp [h₁,h₂,and_assoc]
  have hdis : Disjoint (sourceCells (fiberClass A z d false)) (sourceCells (fiberClass A z d true)) := by
    apply Finset.disjoint_left.mpr
    rintro ⟨v,u⟩ hv hu
    have hfalse := (Finset.mem_filter.mp ((mem_sourceCells _ v u).mp hv).1).2
    have htrue := (Finset.mem_filter.mp ((mem_sourceCells _ v u).mp hu).1).2
    rw [hfalse] at htrue
    contradiction
  rw [hb,he,Finset.card_union_of_disjoint hdis,sourceCells_card,sourceCells_card]

theorem forcing_count (A : Finset ℤ) (z : Point → Bool) :
    F A z = ∑ d∈posDiffs A, (M (fiberClass A z d false)+M (fiberClass A z d true)) := by
  have hc := Finset.card_eq_sum_card_fiberwise (s:=forcedCorners A z) (t:=posDiffs A)
    (f:=fun p => p.1-p.2.1) (by
      rintro ⟨x,y,w⟩ hp
      rcases (mem_sourceCorners A x y w).mp (Finset.mem_filter.mp hp).1 with ⟨hx,hy,_,hyx,_⟩
      exact (mem_posDiffs A (x-y)).mpr ⟨by omega,y,hy,by simpa using hx⟩)
  change (forcedCorners A z).card=_
  rw [hc]
  exact Finset.sum_congr rfl fun d hd => forced_fiber_card A z d ((mem_posDiffs A d).mp hd).1

theorem fiber_forcing_algebra (b c : ℕ) :
    4*((b.choose 2:ℤ)+(c.choose 2:ℤ)) = (b+c:ℤ)^2+(c-b:ℤ)^2-2*(b+c:ℤ) := by
  have hb : (b:ℤ)^2=b+2*(b.choose 2:ℤ) := by exact_mod_cast square_eq_self_add_twice_choose b
  have hc : (c:ℤ)^2=c+2*(c.choose 2:ℤ) := by exact_mod_cast square_eq_self_add_twice_choose c
  nlinarith

theorem forcing_identity (A : Finset ℤ) (z : Point → Bool) :
    2*(T A:ℤ) = (M A:ℤ)+2*(edges A z).card-imbalanceSq A z := by
  have hf : 4*(F A z:ℤ) =
      ∑ d∈posDiffs A, ((r A d:ℤ)^2+
        ((fiberClass A z d true).card-(fiberClass A z d false).card:ℤ)^2-2*(r A d:ℤ)) := by
    rw [forcing_count]
    push_cast
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro d hd
    have he := fiber_forcing_algebra (fiberClass A z d false).card (fiberClass A z d true).card
    have hp : ((fiberClass A z d false).card:ℤ)+(fiberClass A z d true).card=r A d := by
      exact_mod_cast class_partition A z d
    simpa only [M,hp] using he
  have hs : (∑ d∈posDiffs A, (r A d:ℤ)^2)=(M A:ℤ)+2*(T A:ℤ) := by
    exact_mod_cast sum_r_sq A
  have hm : (∑ d∈posDiffs A, (r A d:ℤ))=(M A:ℤ) := by exact_mod_cast sum_r A
  simp only [Finset.sum_sub_distrib,Finset.sum_add_distrib,← Finset.mul_sum,hs,hm] at hf
  change 4*(F A z:ℤ) = (M A:ℤ)+2*(T A:ℤ)+imbalanceSq A z-2*(M A:ℤ) at hf
  have he : ((edges A z).card:ℤ)=2*(F A z:ℤ) := by exact_mod_cast edge_count A z
  omega

theorem imbalanceSq_nonneg (A : Finset ℤ) (z : Point → Bool) : 0 ≤ imbalanceSq A z := by
  exact Finset.sum_nonneg fun _ _ => sq_nonneg _

def completionOffsets (A : Finset ℤ) (q : Point) : Finset ℤ :=
  (Finset.Ioo 0 (q.1-q.2)).filter fun d => q.2+d∈A ∧ q.1-d∈A

def forcingOffsets (A : Finset ℤ) (z : Point → Bool) (q : Point) : Finset ℤ :=
  (completionOffsets A q).filter fun d => z (q.2+d,q.2)=z (q.1,q.1-d)

def H (A : Finset ℤ) (z : Point → Bool) (q : Point) : ℕ := (forcingOffsets A z q).card

def sign (z : Point → Bool) (p : Point) : ℤ := if z p then 1 else -1

def Ksum (A : Finset ℤ) (z : Point → Bool) (q : Point) : ℤ :=
  ∑ d∈completionOffsets A q, (sign z (q.2+d,q.2)+sign z (q.1,q.1-d))

noncomputable def K (A : Finset ℤ) (z : Point → Bool) (q : Point) : ℝ := Ksum A z q/2

noncomputable def completionOperator (A : Finset ℤ) (f : Point → ℝ) (q : Point) : ℝ :=
  (∑ d∈completionOffsets A q,(f (q.2+d,q.2)+f (q.1,q.1-d)))/2

theorem completionOperator_add (A : Finset ℤ) (f g : Point → ℝ) (q : Point) :
    completionOperator A (fun p => f p+g p) q =
      completionOperator A f q+completionOperator A g q := by
  unfold completionOperator
  simp only [Finset.sum_add_distrib]
  ring

theorem completionOperator_smul (A : Finset ℤ) (f : Point → ℝ) (c : ℝ) (q : Point) :
    completionOperator A (fun p => c*f p) q=c*completionOperator A f q := by
  unfold completionOperator
  simp only [← mul_add,← Finset.mul_sum]
  ring

theorem K_eq_completionOperator (A : Finset ℤ) (z : Point → Bool) (q : Point) :
    K A z q=completionOperator A (fun p => (sign z p:ℝ)) q := by
  unfold K Ksum completionOperator
  push_cast
  rfl

theorem fiber_signed_sum (A : Finset ℤ) (z : Point → Bool) (d : ℤ) :
    (∑ u∈positiveFiber A d, sign z (u+d,u)) =
      ((fiberClass A z d true).card:ℤ)-(fiberClass A z d false).card := by
  simp only [sign,Finset.sum_ite]
  simp [fiberClass,Bool.not_eq_true,sub_eq_add_neg]

theorem imbalanceSq_signed (A : Finset ℤ) (z : Point → Bool) :
    imbalanceSq A z=∑ d∈posDiffs A, (∑ u∈positiveFiber A d,sign z (u+d,u))^2 := by
  simp only [fiber_signed_sum,imbalanceSq]

theorem completion_fiber_count (A : Finset ℤ) (z : Point → Bool) (q : Point)
    (hq : q∈sourceCells A) :
    ((forcedCorners A z).filter fun p => outputCell p=q).card=H A z q := by
  rcases q with ⟨v,u⟩
  rcases (mem_sourceCells A v u).mp hq with ⟨hv,hu,huv⟩
  symm
  change (forcingOffsets A z (v,u)).card=_
  refine Finset.card_nbij' (fun d : ℤ => (u+d,u,v))
    (fun p : ℤ×ℤ×ℤ => p.1-u) ?_ ?_ ?_ ?_
  · intro d hd
    simp only [forcingOffsets,completionOffsets,Finset.mem_filter,Finset.mem_Ioo] at hd
    have he : u+v-(u+d)=v-d := by ring
    simp only [Finset.mem_filter,forcedCorners,mem_sourceCorners,outputCell,he]
    exact ⟨⟨⟨hd.1.2.1,hu,hv,by omega,by omega,hd.1.2.2⟩,hd.2⟩,True.intro⟩
  · rintro ⟨x,y,w⟩ hp
    simp only [Finset.mem_filter,forcedCorners,mem_sourceCorners,outputCell,Prod.mk.injEq] at hp
    have hy : y=u := hp.2.2
    have hw : w=v := hp.2.1
    subst y; subst w
    have he : v-(x-u)=u+v-x := by ring
    have hx : u+(x-u)=x := by ring
    simp only [forcingOffsets,completionOffsets,Finset.mem_filter,Finset.mem_Ioo,he,hx]
    exact ⟨⟨⟨by omega,by omega⟩,hp.1.1.1,hp.1.1.2.2.2.2.2⟩,hp.1.2⟩
  · intros; simp
  · rintro ⟨x,y,w⟩ hp
    have he := (Finset.mem_filter.mp hp).2
    simp only [outputCell,Prod.mk.injEq] at he
    apply Prod.ext
    · dsimp; ring
    · exact Prod.ext he.2.symm he.1.symm

theorem H_sum (A : Finset ℤ) (z : Point → Bool) :
    ∑ q∈sourceCells A, H A z q=F A z := by
  have hc := Finset.card_eq_sum_card_fiberwise (s:=forcedCorners A z) (t:=sourceCells A)
    (f:=outputCell) (by
      rintro ⟨x,y,w⟩ hp
      rcases (mem_sourceCorners A x y w).mp (Finset.mem_filter.mp hp).1 with ⟨hx,hy,hw,hyx,hxw,_⟩
      exact (mem_sourceCells A w y).mpr ⟨hw,hy,by omega⟩)
  change _=(forcedCorners A z).card
  rw [hc]
  exact Finset.sum_congr rfl fun q hq => (completion_fiber_count A z q hq).symm

theorem pointwise_term (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource fun a => a∈A) z) (q : Point) (hq : q∈sourceCells A)
    (d : ℤ) (hd : d∈completionOffsets A q) :
    sign z (q.2+d,q.2)+sign z (q.1,q.1-d) =
      -2*sign z q * (if z (q.2+d,q.2)=z (q.1,q.1-d) then 1 else 0) := by
  rcases q with ⟨v,u⟩
  rcases (mem_sourceCells A v u).mp hq with ⟨hv,hu,huv⟩
  simp only [completionOffsets,Finset.mem_filter,Finset.mem_Ioo] at hd
  have ev : u+d+(v-u-d)=v := by ring
  have eu : u+(v-u-d)=v-d := by ring
  have hp := hz (u+d) u (v-u-d) (by omega) ⟨hd.2.1,hu,by omega⟩
    (by rw [ev]; exact ⟨hv,hu,huv⟩)
    (by rw [ev,eu]; exact ⟨hv,hd.2.2,by omega⟩)
  rw [ev,eu] at hp
  dsimp
  cases h₁ : z (u+d,u) <;> cases h₂ : z (v,v-d) <;> cases h₃ : z (v,u) <;>
    simp_all [sign]

theorem pointwise_Ksum (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource fun a => a∈A) z) (q : Point) (hq : q∈sourceCells A) :
    Ksum A z q = -2*sign z q*(H A z q:ℤ) := by
  unfold Ksum
  rw [Finset.sum_congr rfl (fun d hd => pointwise_term A z hz q hq d hd)]
  rw [← Finset.mul_sum]
  congr 1
  simp only [H,forcingOffsets,Finset.card_filter]
  push_cast
  rfl

/-- Exact real-valued signed completion formula, including its absolute value. -/
theorem pointwise_forcing (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource fun a => a∈A) z) (q : Point) (hq : q∈sourceCells A) :
    (H A z q:ℝ) = -(sign z q:ℝ)*K A z q ∧ (H A z q:ℝ)=|K A z q| := by
  have hk := pointwise_Ksum A z hz q hq
  have hkr : (Ksum A z q:ℝ)= -2*(sign z q:ℝ)*(H A z q:ℝ) := by exact_mod_cast hk
  have hh : 0≤(H A z q:ℝ) := by positivity
  have he : K A z q = -(sign z q:ℝ)*(H A z q:ℝ) := by
    unfold K
    rw [hkr]
    ring
  rw [he]
  constructor
  · cases hqz : z q <;> norm_num [sign,hqz]
  · have hab : |(sign z q:ℝ)|=1 := by cases hqz : z q <;> norm_num [sign,hqz]
    rw [abs_mul,abs_neg,hab,one_mul,abs_of_nonneg hh]

theorem forcing_count_fraction (A : Finset ℤ) (z : Point → Bool) :
    (F A z:ℝ)=(2*(T A:ℝ)-(M A:ℝ)+(imbalanceSq A z:ℝ))/4 := by
  have hi : 2*(T A:ℝ)=(M A:ℝ)+2*(edges A z).card-(imbalanceSq A z:ℝ) := by
    exact_mod_cast forcing_identity A z
  have he : ((edges A z).card:ℝ)=2*(F A z:ℝ) := by exact_mod_cast edge_count A z
  linarith

theorem edges_no_loops (A : Finset ℤ) (z : Point → Bool)
    (hz : properOn (strictSource fun a => a∈A) z) (p : Point) : s(p,p)∉edges A z := by
  intro he
  exact edges_bipartite A z hz p p he rfl

end EnergyForcing.Forcing
