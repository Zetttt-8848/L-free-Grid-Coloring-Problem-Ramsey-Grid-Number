import MidpointThree

set_option autoImplicit false

namespace EnergyForcing.TwoDistance

open Finset
open scoped BigOperators

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable local instance : DecidableEq E := Classical.decEq E

def TwoDistances (X : Finset E) (tau : ℝ) : Prop :=
  ∀x∈X, ∀y∈X, x≠y → ‖x-y‖^2=tau ∨ ‖x-y‖^2=2*tau

theorem pair_from_sum_and_member (P : Finset E) (hP : P.card=2) (x : E) (hx : x∈P) :
    P={x,(∑a∈P,a)-x} := by
  classical
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hP
  simp only [Finset.mem_insert,Finset.mem_singleton] at hx
  rcases hx with hx|hx
  · subst x
    rw [Finset.sum_pair hab]
    have he : a+b-a=b := by abel
    rw [he]
  · subst x
    rw [Finset.sum_pair hab]
    simp [add_sub_cancel_right,Finset.pair_comm]

theorem pairs_equal_of_shared (P Q : Finset E) (hP : P.card=2) (hQ : Q.card=2)
    (he : (∑a∈P,a)=∑a∈Q,a) (x : E) (hxP : x∈P) (hxQ : x∈Q) : P=Q := by
  rw [pair_from_sum_and_member P hP x hxP,pair_from_sum_and_member Q hQ x hxQ]
  rw [he]

theorem midpoint_pair_radius (X : Finset E) (tau : ℝ) (c : E)
    (P : Finset E) (hP : P∈midpointPairs X tau c) :
    ∃p : E, P={c+p,c-p} ∧ ‖p‖^2=tau/2 := by
  classical
  rcases Finset.mem_filter.mp hP with ⟨hP,hs,hL⟩
  rcases Finset.mem_powersetCard.mp hP with ⟨hPX,hcard⟩
  obtain ⟨a,b,hab,rfl⟩ := Finset.card_eq_two.mp hcard
  rw [Finset.sum_pair hab,two_smul] at hs
  let p := a-c
  have hp : c+p=a := by dsimp [p]; abel
  have hm : c-p=b := by
    dsimp [p]
    calc
      _ = (c+c)-a := by abel
      _ = (a+b)-a := by rw [hs]
      _ = b := by abel
  have hd := hL a (by simp) b (by simp) hab
  have hv : a-b=(2 : ℝ) • p := by
    rw [← hp,← hm,two_smul]
    abel
  rw [hv,norm_smul] at hd
  norm_num at hd
  refine ⟨p,by rw [hp,hm],?_⟩
  nlinarith

def endpoint {k : ℕ} (c : E) (p : Fin k → E) (q : Fin k × Bool) : E :=
  c + if q.2 then p q.1 else -p q.1

/-- A complete actual midpoint block, with indexed orthogonal radii. -/
structure RadiusBlock (X : Finset E) (tau : ℝ) (c : E) (k : ℕ) where
  radii : Fin k → E
  radius_sq : ∀i, ‖radii i‖^2=tau/2
  orthogonal : ∀i j, i≠j → inner (𝕜 := ℝ) (radii i) (radii j)=0
  endpoints_mem : ∀q, endpoint c radii q∈X
  endpoints_injective : Function.Injective (endpoint c radii)
  endpoint_image : (Finset.univ.image (endpoint c radii))=(midpointPairs X tau c).biUnion id
  pairs_image : (Finset.univ.image (fun i => ({c+radii i,c-radii i} : Finset E)))=midpointPairs X tau c

theorem midpoint_block (X : Finset E) (tau : ℝ) (htau : 0<tau)
    (hX : TwoDistances X tau) (c : E) :
    Nonempty (RadiusBlock X tau c (midpointPairs X tau c).card) := by
  classical
  let pairs := midpointPairs X tau c
  let idx : Fin pairs.card ≃ pairs := pairs.equivFin.symm
  have hs (i : Fin pairs.card) : ∃p : E, (idx i).val={c+p,c-p} ∧ ‖p‖^2=tau/2 :=
    midpoint_pair_radius X tau c (idx i).val (idx i).property
  choose p hp hn using hs
  have hpi (i : Fin pairs.card) : ({c+p i,c-p i} : Finset E)∈pairs := by
    rw [← hp i]
    exact (idx i).property
  have hcard (i : Fin pairs.card) : ({c+p i,c-p i} : Finset E).card=2 :=
    (Finset.mem_powersetCard.mp (Finset.mem_filter.mp (hpi i)).1).2
  have hne (i : Fin pairs.card) : c+p i≠c-p i := by
    intro he
    have hh := hcard i
    simp [he] at hh
  have hend (q : Fin pairs.card × Bool) : endpoint c p q∈(idx q.1).val := by
    rw [hp q.1]
    rcases q with ⟨i,b⟩
    cases b <;> simp [endpoint,sub_eq_add_neg]
  have hmem (q : Fin pairs.card × Bool) : endpoint c p q∈X :=
    (Finset.mem_powersetCard.mp (Finset.mem_filter.mp (idx q.1).property).1).1 (hend q)
  have hinj : Function.Injective (endpoint c p) := by
    rintro ⟨i,b⟩ ⟨j,d⟩ he
    have hepair : (idx i).val=(idx j).val := by
      apply pairs_equal_of_shared _ _
        (Finset.mem_powersetCard.mp (Finset.mem_filter.mp (idx i).property).1).2
        (Finset.mem_powersetCard.mp (Finset.mem_filter.mp (idx j).property).1).2
        ((Finset.mem_filter.mp (idx i).property).2.1.trans
          (Finset.mem_filter.mp (idx j).property).2.1.symm) (endpoint c p (i,b)) (hend (i,b))
      rw [he]
      exact hend (j,d)
    have hij : i=j := idx.injective (Subtype.ext hepair)
    subst j
    have hni := hne i
    cases b <;> cases d <;> simp only [endpoint,Bool.false_eq_true,if_false,if_true] at he ⊢
    · exact False.elim (hni (by simpa [sub_eq_add_neg] using he.symm))
    · exact False.elim (hni (by simpa [sub_eq_add_neg] using he))
  have horth (i j : Fin pairs.card) (hij : i≠j) : inner (𝕜 := ℝ) (p i) (p j)=0 := by
    have ha := hX (endpoint c p (i,true)) (hmem (i,true))
      (endpoint c p (j,true)) (hmem (j,true)) (by intro he; exact hij (congrArg Prod.fst (hinj he)))
    have hb := hX (endpoint c p (i,true)) (hmem (i,true))
      (endpoint c p (j,false)) (hmem (j,false)) (by intro he; exact hij (congrArg Prod.fst (hinj he)))
    have hminus : endpoint c p (i,true)-endpoint c p (j,true)=p i-p j := by dsimp [endpoint]; abel
    have hplus : endpoint c p (i,true)-endpoint c p (j,false)=p i+p j := by dsimp [endpoint]; abel
    rw [hminus] at ha
    rw [hplus] at hb
    have hla : tau ≤ ‖p i-p j‖^2 := by rcases ha with ha|ha <;> rw [ha] <;> linarith
    have hlb : tau ≤ ‖p i+p j‖^2 := by rcases hb with hb|hb <;> rw [hb] <;> linarith
    rw [norm_sub_sq_real,hn i,hn j] at hla
    rw [norm_add_sq_real,hn i,hn j] at hlb
    linarith
  have himage : Finset.univ.image (endpoint c p)=pairs.biUnion id := by
    ext x
    constructor
    · intro hx
      obtain ⟨q,_,rfl⟩ := Finset.mem_image.mp hx
      exact Finset.mem_biUnion.mpr ⟨(idx q.1).val,(idx q.1).property,hend q⟩
    · intro hx
      obtain ⟨P,hP,hxP⟩ := Finset.mem_biUnion.mp hx
      let i := idx.symm ⟨P,hP⟩
      have hi : (idx i).val=P := congrArg Subtype.val (idx.apply_symm_apply ⟨P,hP⟩)
      change x∈P at hxP
      rw [← hi,hp i] at hxP
      simp only [Finset.mem_insert,Finset.mem_singleton] at hxP
      rcases hxP with hx|hx
      · exact Finset.mem_image.mpr ⟨(i,true),Finset.mem_univ _,by simpa [endpoint] using hx.symm⟩
      · exact Finset.mem_image.mpr ⟨(i,false),Finset.mem_univ _,by simpa [endpoint,sub_eq_add_neg] using hx.symm⟩
  have hpimage : Finset.univ.image (fun i => ({c+p i,c-p i} : Finset E))=pairs := by
    ext P
    constructor
    · intro h
      obtain ⟨i,_,rfl⟩ := Finset.mem_image.mp h
      exact hpi i
    · intro hP
      let i := idx.symm ⟨P,hP⟩
      refine Finset.mem_image.mpr ⟨i,Finset.mem_univ _,?_⟩
      rw [← hp i]
      exact congrArg Subtype.val (idx.apply_symm_apply ⟨P,hP⟩)
  exact ⟨⟨p,hn,horth,hmem,hinj,himage,hpimage⟩⟩

end EnergyForcing.TwoDistance
