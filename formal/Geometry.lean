import Std

/- Kernel-checked geometric parts of the manuscript. No finite sampling is
   used in this file. Counting and Ramsey minima are tracked separately. -/
namespace EnergyForcing

abbrev Point := Int × Int
def square (N : Int) (p : Point) : Prop :=
  1 ≤ p.1 ∧ p.1 ≤ N ∧ 1 ≤ p.2 ∧ p.2 ≤ N

def properL {α : Type} (N : Int) (c : Point → α) : Prop :=
  ∀ x y d : Int, 0 < d →
    square N (x,y) → square N (x+d,y) → square N (x+d,y+d) →
    ¬ (c (x,y) = c (x+d,y) ∧ c (x+d,y) = c (x+d,y+d))

def properP {α : Type} (N : Int) (c : Point → α) : Prop :=
  ∀ x y d : Int, 0 < d →
    square N (x,y) → square N (x,y+d) → square N (x+d,y+d) →
    ¬ (c (x,y) = c (x,y+d) ∧ c (x,y+d) = c (x+d,y+d))

def transpose (p : Point) : Point := (p.2,p.1)
theorem transpose_involution (p : Point) : transpose (transpose p) = p := rfl
theorem transpose_square (N : Int) (p : Point) :
    square N (transpose p) ↔ square N p := by
  simp only [square, transpose]; omega

/-- Lemma lem:transpose: the exact proper-coloring equivalence. -/
theorem transpose_proper {α : Type} (N : Int) (c : Point → α) :
    properL N c ↔ properP N (fun p => c (transpose p)) := by
  constructor
  · intro h x y d hd hp hq hr
    apply h y x d hd <;> simp_all [square, transpose] <;> omega
  · intro h x y d hd hp hq hr
    apply h y x d hd <;> simp_all [square, transpose] <;> omega

def ramseyL (k n : Nat) : Prop := ∀ c : Point → Fin k, ¬ properL (n:Int) c
def ramseyP (k n : Nat) : Prop := ∀ c : Point → Fin k, ¬ properP (n:Int) c
theorem ramsey_transpose (k n : Nat) : ramseyL k n ↔ ramseyP k n := by
  constructor
  · intro h c hp
    have hbad := h (fun p => c (transpose p))
    apply hbad
    apply (transpose_proper (n:Int) (fun p => c (transpose p))).mpr
    simpa only [transpose_involution] using hp
  · intro h c hl
    exact h (fun p => c (transpose p)) ((transpose_proper (n:Int) c).mp hl)

def leastRamseyL (k n : Nat) : Prop :=
  1 ≤ n ∧ ramseyL k n ∧ ∀ m : Nat, 1 ≤ m → m < n → ¬ ramseyL k m
def leastRamseyP (k n : Nat) : Prop :=
  1 ≤ n ∧ ramseyP k n ∧ ∀ m : Nat, 1 ≤ m → m < n → ¬ ramseyP k m
theorem least_ramsey_transpose (k n : Nat) : leastRamseyL k n ↔ leastRamseyP k n := by
  simp only [leastRamseyL,leastRamseyP,ramsey_transpose]
/-- The least excluded positive side lengths for both orientations coincide. -/
theorem least_threshold_equal (k n m : Nat)
    (hn : leastRamseyL k n) (hm : leastRamseyP k m) : n=m := by
  have hm' := (least_ramsey_transpose k m).mpr hm
  by_cases hnm : n<m
  · exact False.elim (hm'.2.2 n hn.1 hnm hn.2.1)
  · by_cases hmn : m<n
    · exact False.elim (hn.2.2 m hm'.1 hmn hm'.2.1)
    · omega

def H (N : Int) (p : Point) : Point := (N+1-p.1,p.2)
def J (N : Int) (p : Point) : Point := (N+1-p.1,N+1-p.2)
theorem H_involution (N : Int) (p : Point) : H N (H N p) = p := by
  apply Prod.ext <;> simp [H] <;> omega
theorem H_square (N : Int) (p : Point) : square N (H N p) ↔ square N p := by
  simp only [square, H]; omega
theorem J_square (N : Int) (p : Point) : square N (J N p) ↔ square N p := by
  simp only [square, J]; omega

def properCorner {α : Type} (N : Int) (c : Point → α) : Prop :=
  ∀ x y d : Int, 0 < d →
    square N (x,y) → square N (x+d,y) → square N (x,y+d) →
    ¬ (c (x,y) = c (x+d,y) ∧ c (x+d,y) = c (x,y+d))

/-- Lemma lem:H, with its domain and positive orientation explicit. -/
theorem reflection_proper {α : Type} (N : Int) (c : Point → α) :
    properL N c ↔ properCorner N (fun p => c (H N p)) := by
  constructor
  · intro h x y d hd hp hq hr heq
    have hs : N+1-(x+d)+d = N+1-x := by omega
    have hp' : square N (N+1-(x+d),y) := by simp_all [square]; omega
    have hq' : square N (N+1-(x+d)+d,y) := by simp_all [square]; omega
    have hr' : square N (N+1-(x+d)+d,y+d) := by simp_all [square] <;> omega
    apply h (N+1-(x+d)) y d hd hp' hq' hr'
    simp only [H] at heq
    constructor
    · simpa [hs] using heq.1.symm
    · simpa [hs] using heq.1.trans heq.2
  · intro h x y d hd hp hq hr heq
    have hs : N+1-(x+d)+d = N+1-x := by omega
    have h1 : N+1-(N+1-(x+d)) = x+d := by omega
    have h2 : N+1-(N+1-(x+d)+d) = x := by omega
    have hp' : square N (N+1-(x+d),y) := by simp_all [square] <;> omega
    have hq' : square N (N+1-(x+d)+d,y) := by simp_all [square]; omega
    have hr' : square N (N+1-(x+d),y+d) := by simp_all [square] <;> omega
    apply h (N+1-(x+d)) y d hd hp' hq' hr'
    simp only [H,h1,h2]
    exact ⟨heq.1.symm, heq.1.trans heq.2⟩

def paired {α : Type} (N : Int) (c : Point → α) (p : Point) :=
  (c p, c (J N p))

/-- The no-corner part of lem:J. Color-class counting is not claimed here. -/
theorem paired_no_signed_corner {α : Type} (N : Int) (c : Point → α)
    (h : properCorner N c) (x y d : Int) (hd : d ≠ 0)
    (hp : square N (x,y)) (hq : square N (x+d,y))
    (hr : square N (x,y+d)) :
    ¬ (paired N c (x,y) = paired N c (x+d,y) ∧
       paired N c (x+d,y) = paired N c (x,y+d)) := by
  intro heq
  by_cases hdpos : 0 < d
  · apply h x y d hdpos hp hq hr
    exact ⟨congrArg Prod.fst heq.1, congrArg Prod.fst heq.2⟩
  · have hm : 0 < -d := by omega
    have hp' : square N (N+1-x,N+1-y) := by simp_all [square]; omega
    have hq' : square N (N+1-x+ -d,N+1-y) := by simp_all [square]; omega
    have hr' : square N (N+1-x,N+1-y+ -d) := by simp_all [square]; omega
    have e1 := congrArg Prod.snd heq.1
    have e2 := congrArg Prod.snd heq.2
    have hx : N+1-(x+d) = N+1-x+ -d := by omega
    have hy : N+1-(y+d) = N+1-y+ -d := by omega
    apply h (N+1-x) (N+1-y) (-d) hm hp' hq' hr'
    simpa only [paired,J,hx,hy] using And.intro e1 e2

theorem centered_emod (h m : Int) (_hm : 0 < m) (hh : -m < h ∧ h < m) :
    h % m = if 0 ≤ h then h else h+m := by
  split
  · rename_i hp
    exact Int.emod_eq_of_lt hp hh.2
  · rename_i hn
    rw [Int.emod_eq_add_self_emod]
    apply Int.emod_eq_of_lt <;> omega

/-- Arithmetic core of lem:embed: no wrapped unequal increments in [1,N]. -/
theorem equal_mod_increments (N a a' b b' : Int)
    (hN : 1 ≤ N) (ha : 1 ≤ a) (ha' : a ≤ N)
    (hc : 1 ≤ a') (hc' : a' ≤ N) (hb : 1 ≤ b) (hb' : b ≤ N)
    (he : 1 ≤ b') (he' : b' ≤ N)
    (hmod : (a'-a) % (2*N) = (b'-b) % (2*N)) : a'-a = b'-b := by
  have hp : 0 < 2*N := by omega
  rw [centered_emod (a'-a) (2*N) hp (by constructor <;> omega),
      centered_emod (b'-b) (2*N) hp (by constructor <;> omega)] at hmod
  split at hmod <;> split at hmod <;> omega

def strictSource (A : Int → Prop) (p : Point) : Prop := A p.1 ∧ A p.2 ∧ p.2 < p.1
def weakSource (A : Int → Prop) (p : Point) : Prop := A p.1 ∧ A p.2 ∧ p.2 ≤ p.1
def properOn {α : Type} (D : Point → Prop) (c : Point → α) : Prop :=
  ∀ x y h : Int, 0 < h → D (x,y) → D (x+h,y) → D (x+h,y+h) →
    ¬ (c (x,y) = c (x+h,y) ∧ c (x+h,y) = c (x+h,y+h))

/-- Exact diagonal exclusion used by lem:restriction, for arbitrary colors. -/
theorem diagonal_exclusion {α : Type} (A : Int → Prop) (c : Point → α)
    (proper : properOn (weakSource A) c) (u v : Int)
    (hu : A u) (hv : A v) (huv : u < v) (hs : c (u,u) = c (v,v)) :
    c (v,u) ≠ c (u,u) := by
  intro heq
  have hstep : 0 < v-u := by omega
  have hsimp : u+(v-u)=v := by omega
  have hh := proper u u (v-u) hstep
  simp only [hsimp,weakSource] at hh
  apply hh ⟨hu,hu,Int.le_refl u⟩ ⟨hv,hu,by omega⟩ ⟨hv,hv,Int.le_refl v⟩
  exact ⟨heq.symm,heq.trans hs⟩

/-- Every corner of an inherited weak fiber maps to a strict source corner. -/
theorem fiber_restriction {α : Type} (A : Int → Prop) (c : Point → α)
    (proper : properOn (strictSource A) c) (d : Int) (hd : 0 < d) :
    properOn (weakSource (fun u => A u ∧ A (u+d))) (fun p => c (p.1+d,p.2)) := by
  intro x y h hh hp hq hr heq
  have e1 : x+h+d=x+d+h := by omega
  apply proper (x+d) y h hh
  · exact ⟨hp.1.2,hp.2.1.1,by have := hp.2.2; omega⟩
  · simp only [← e1]; exact ⟨hq.1.2,hq.2.1.1,by have := hq.2.2; omega⟩
  · simp only [← e1]; exact ⟨hr.1.2,hr.2.1.1,by have := hr.2.2; omega⟩
  · simpa only [e1] using heq

def Golomb (A : Int → Prop) : Prop :=
  ∀ a b c d : Int, A a → A b → A c → A d → a < b → c < d →
    b-a = d-c → a=c ∧ b=d

theorem bool_eq_not_of_ne (x y : Bool) (h : x ≠ y) : x = !y := by
  cases x <;> cases y <;> simp_all

theorem diagonal_class_no_ordered_repeat (A : Int → Prop) (color : Point → Bool)
    (proper : properOn (weakSource A) color) (i : Bool) (a b c d : Int)
    (ha : A a) (hb : A b) (hc : A c) (hd : A d)
    (ca : color (a,a)=i) (cb : color (b,b)=i)
    (cc : color (c,c)=i) (cd : color (d,d)=i)
    (hab : a<b) (hcd : c<d) (hac : a<c) (he : b-a=d-c) : False := by
  have eba : color (b,a) = !i := by
    apply bool_eq_not_of_ne
    simpa only [ca] using diagonal_exclusion A color proper a b ha hb hab (ca.trans cb.symm)
  have eda : color (d,a) = !i := by
    apply bool_eq_not_of_ne
    simpa only [ca] using diagonal_exclusion A color proper a d ha hd (by omega) (ca.trans cd.symm)
  have edc : color (d,c) = !i := by
    apply bool_eq_not_of_ne
    simpa only [cc] using diagonal_exclusion A color proper c d hc hd hcd (cc.trans cd.symm)
  have ebd : b+(c-a)=d := by omega
  have eac : a+(c-a)=c := by omega
  have h := proper b a (c-a) (by omega)
  simp only [ebd,eac,weakSource] at h
  apply h ⟨hb,ha,by omega⟩ ⟨hd,ha,by omega⟩ ⟨hd,hc,by omega⟩
  exact ⟨eba.trans eda.symm,eda.trans edc.symm⟩

/-- The weak-source diagonal color classes are Golomb, with overlaps allowed. -/
theorem diagonal_class_golomb (A : Int → Prop) (color : Point → Bool)
    (proper : properOn (weakSource A) color) (i : Bool) :
    Golomb (fun a => A a ∧ color (a,a)=i) := by
  intro a b c d ha hb hc hd hab hcd he
  by_cases hac : a<c
  · exact False.elim (diagonal_class_no_ordered_repeat A color proper i a b c d
      ha.1 hb.1 hc.1 hd.1 ha.2 hb.2 hc.2 hd.2 hab hcd hac he)
  · by_cases hca : c<a
    · exact False.elim (diagonal_class_no_ordered_repeat A color proper i c d a b
        hc.1 hd.1 ha.1 hb.1 hc.2 hd.2 ha.2 hb.2 hcd hab hca he.symm)
    · constructor <;> omega

/-- The inherited strict-source fibers have Golomb color classes. -/
theorem fiber_class_golomb (A : Int → Prop) (color : Point → Bool)
    (proper : properOn (strictSource A) color) (d : Int) (hd : 0<d) (i : Bool) :
    Golomb (fun u => (A u ∧ A (u+d)) ∧ color (u+d,u)=i) := by
  exact diagonal_class_golomb (fun u => A u ∧ A (u+d))
    (fun p => color (p.1+d,p.2)) (fiber_restriction A color proper d hd) i

/-- Unordered pair sums, with repeated endpoints permitted. Ordered representatives
    make unordered equality exactly equality of both coordinates. -/
theorem golomb_pair_sum_unique (A : Int → Prop) (h : Golomb A)
    (a b c d : Int) (ha : A a) (hb : A b) (hc : A c) (hd : A d)
    (hab : a≤b) (hcd : c≤d) (he : a+b=c+d) : a=c ∧ b=d := by
  by_cases hac : a<c
  · have hbad := h a c d b ha hc hd hb hac (by omega) (by omega)
    omega
  · by_cases hca : c<a
    · have hbad := h c a b d hc ha hb hd hca (by omega) (by omega)
      omega
    · constructor <;> omega

#print axioms transpose_proper
#print axioms ramsey_transpose
#print axioms least_threshold_equal
#print axioms reflection_proper
#print axioms paired_no_signed_corner
#print axioms equal_mod_increments
#print axioms diagonal_exclusion
#print axioms fiber_restriction
#print axioms diagonal_class_golomb
#print axioms fiber_class_golomb
#print axioms golomb_pair_sum_unique
/- Round 2: complete domains for restriction and cyclic embedding. -/
theorem properOn_mono {α : Type} (D E : Point → Prop) (color : Point → α)
    (hDE : ∀ p, D p → E p) (h : properOn E color) : properOn D color := by
  intro x y d hd hp hq hr
  exact h x y d hd (hDE _ hp) (hDE _ hq) (hDE _ hr)

/-- Full first assertion of lem:restriction, including square-domain restriction. -/
theorem square_diagonal_restriction {α : Type} (N : Int) (A : Int → Prop)
    (color : Point → α) (c₀ : α) (hA : ∀ a, A a → 1 ≤ a ∧ a ≤ N)
    (hproper : properL N color) (hdiag : ∀ a, A a → color (a,a)=c₀) :
    properOn (strictSource A) color ∧
    ∀ p, strictSource A p → color p ≠ c₀ := by
  have hw : properOn (weakSource A) color := by
    apply properOn_mono (weakSource A) (square N) color
    · intro p hp
      exact ⟨(hA p.1 hp.1).1,(hA p.1 hp.1).2,
        (hA p.2 hp.2.1).1,(hA p.2 hp.2.1).2⟩
    · exact hproper
  constructor
  · apply properOn_mono (strictSource A) (weakSource A) color
    · intro p hp
      exact ⟨hp.1,hp.2.1,by have := hp.2.2; omega⟩
    · exact hw
  · intro p hp
    have hc := diagonal_exclusion A color hw p.2 p.1 hp.2.1 hp.1 hp.2.2
      ((hdiag p.2 hp.2.1).trans (hdiag p.1 hp.1).symm)
    simpa only [hdiag p.2 hp.2.1] using hc

theorem fiber_map_defined (A : Int → Prop) (d : Int) (hd : 0<d)
    (p : Point) (hp : weakSource (fun u => A u ∧ A (u+d)) p) :
    strictSource A (p.1+d,p.2) := by
  exact ⟨hp.1.2,hp.2.1.1,by have := hp.2.2; omega⟩

/-- The weak-fiber assertion, together with its domain and diagonal. -/
theorem weak_restriction_complete {α : Type} (A : Int → Prop) (c : Point → α)
    (h : properOn (strictSource A) c) (d : Int) (hd : 0<d) :
    (∀ p, weakSource (fun u => A u ∧ A (u+d)) p →
      strictSource A (p.1+d,p.2)) ∧
    properOn (weakSource (fun u => A u ∧ A (u+d))) (fun p => c (p.1+d,p.2)) ∧
    ∀ u, (fun p : Point => c (p.1+d,p.2)) (u,u)=c (u+d,u) := by
  exact ⟨fiber_map_defined A d hd,fiber_restriction A c h d hd,fun _ => rfl⟩

/-- Canonical integer residues are the concrete model of Z/(m Z). -/
def reducePoint (m : Int) (p : Point) : Point := (p.1%m,p.2%m)
def residueImage (m : Int) (S : Point → Prop) (q : Point) : Prop :=
  ∃ p, S p ∧ reducePoint m p=q

def noSignedCorners (S : Point → Prop) : Prop :=
  ∀ a b d : Int, d≠0 → ¬ (S (a,b) ∧ S (a+d,b) ∧ S (a,b+d))

theorem reduce_square_eq (N : Int) (hN : 1≤N) (p : Point) (hp : square N p) :
    reducePoint (2*N) p=p := by
  apply Prod.ext <;> dsimp [reducePoint]
  · exact Int.emod_eq_of_lt (by have := hp.1; omega) (by have := hp.2.1; omega)
  · exact Int.emod_eq_of_lt (by have := hp.2.2.1; omega) (by have := hp.2.2.2; omega)

theorem cyclic_embedding_injective (N : Int) (hN : 1≤N) (p q : Point)
    (hp : square N p) (hq : square N q)
    (he : reducePoint (2*N) p=reducePoint (2*N) q) : p=q := by
  simpa only [reduce_square_eq N hN p hp,reduce_square_eq N hN q hq] using he

theorem image_eq_source (N : Int) (hN : 1≤N) (S : Point → Prop)
    (hs : ∀ p, S p → square N p) (q : Point) : residueImage (2*N) S q ↔ S q := by
  constructor
  · rintro ⟨p,hp,he⟩
    rw [reduce_square_eq N hN p (hs p hp)] at he
    simpa only [← he] using hp
  · intro hq
    exact ⟨q,hq,reduce_square_eq N hN q (hs q hq)⟩

theorem residue_increment (m a d : Int) : ((a+d)%m-a)%m=d%m := by
  calc
    ((a+d)%m-a)%m = ((a+d)-a)%m := by
      rw [Int.sub_emod ((a+d)%m) a m,Int.emod_emod,← Int.sub_emod]
    _ = d%m := by congr 1; omega

/-- Full no-corner assertion of lem:embed in canonical residues. Group addition
    is modulo 2N and the step must be nonzero modulo 2N. -/
theorem cyclic_embedding_no_corner (N : Int) (hN : 1≤N) (S : Point → Prop)
    (hs : ∀ p, S p → square N p) (hc : noSignedCorners S)
    (a b δ : Int) (hδ : δ%(2*N)≠0) :
    ¬ (residueImage (2*N) S (a,b) ∧
       residueImage (2*N) S ((a+δ)%(2*N),b) ∧
       residueImage (2*N) S (a,(b+δ)%(2*N))) := by
  intro h
  simp only [image_eq_source N hN S hs] at h
  have hp := hs (a,b) h.1
  have hq := hs ((a+δ)%(2*N),b) h.2.1
  have hr := hs (a,(b+δ)%(2*N)) h.2.2
  have hh : ((a+δ)%(2*N)-a)%(2*N)=((b+δ)%(2*N)-b)%(2*N) := by
    rw [residue_increment,residue_increment]
  have he := equal_mod_increments N a ((a+δ)%(2*N)) b ((b+δ)%(2*N))
    hN hp.1 hp.2.1 hq.1 hq.2.1 hp.2.2.1 hp.2.2.2 hr.2.2.1 hr.2.2.2 hh
  have hn : (a+δ)%(2*N)-a≠0 := by
    intro hz
    have hd := residue_increment (2*N) a δ
    rw [hz] at hd
    exact hδ (by simpa using hd.symm)
  apply hc a b ((a+δ)%(2*N)-a) hn
  have ex : a+((a+δ)%(2*N)-a)=(a+δ)%(2*N) := by omega
  have ey : b+((a+δ)%(2*N)-a)=(b+δ)%(2*N) := by omega
  simpa only [ex,ey] using h

/-- A corner is parametrized by its first cell and its positive step. -/
def sourceCorner (A : Int → Prop) (p : Int × Int × Int) : Prop :=
  0<p.2.2 ∧ strictSource A (p.1,p.2.1) ∧
    strictSource A (p.1+p.2.2,p.2.1) ∧
    strictSource A (p.1+p.2.2,p.2.1+p.2.2)

def fiberPair (A : Int → Prop) (p : Int × Int × Int) : Prop :=
  0<p.1 ∧ p.2.1<p.2.2 ∧
    A p.2.1 ∧ A (p.2.1+p.1) ∧ A p.2.2 ∧ A (p.2.2+p.1)

def cornerToFiber (p : Int × Int × Int) : Int × Int × Int :=
  (p.1-p.2.1,p.2.1,p.2.1+p.2.2)
def fiberToCorner (p : Int × Int × Int) : Int × Int × Int :=
  (p.2.1+p.1,p.2.1,p.2.2-p.2.1)

theorem corner_to_fiber (A : Int → Prop) (p : Int × Int × Int)
    (h : sourceCorner A p) : fiberPair A (cornerToFiber p) := by
  rcases p with ⟨x,y,d⟩
  simp only [sourceCorner,strictSource] at h
  dsimp [fiberPair,cornerToFiber]
  have e₁ : y+(x-y)=x := by omega
  have e₂ : y+d+(x-y)=x+d := by omega
  exact ⟨by omega,by omega,h.2.1.2.1,by simpa only [e₁] using h.2.1.1,
    h.2.2.2.2.1,by simpa only [e₂] using h.2.2.1.1⟩

theorem fiber_to_corner (A : Int → Prop) (p : Int × Int × Int)
    (h : fiberPair A p) : sourceCorner A (fiberToCorner p) := by
  rcases p with ⟨d,u,v⟩
  simp only [fiberPair] at h
  dsimp [sourceCorner,strictSource,fiberToCorner]
  have e₁ : u+d+(v-u)=v+d := by omega
  have e₂ : u+(v-u)=v := by omega
  simp only [e₁,e₂]
  exact ⟨by omega,⟨h.2.2.2.1,h.2.2.1,by omega⟩,
    ⟨h.2.2.2.2.2,h.2.2.1,by omega⟩,⟨h.2.2.2.2.2,h.2.2.2.2.1,by omega⟩⟩

theorem corner_fiber_left_inverse (p : Int × Int × Int) :
    fiberToCorner (cornerToFiber p)=p := by
  rcases p with ⟨x,y,d⟩
  apply Prod.ext
  · dsimp [fiberToCorner,cornerToFiber]; omega
  · apply Prod.ext <;> dsimp [fiberToCorner,cornerToFiber] <;> omega

theorem corner_fiber_right_inverse (p : Int × Int × Int) :
    cornerToFiber (fiberToCorner p)=p := by
  rcases p with ⟨d,u,v⟩
  apply Prod.ext
  · dsimp [fiberToCorner,cornerToFiber]; omega
  · apply Prod.ext <;> dsimp [fiberToCorner,cornerToFiber] <;> omega

def deletedSource (A : Int → Prop) : Int → Prop := fun a => A a ∧ a≠0
def endpointArc (A : Int → Prop) (p : Point) : Prop :=
  deletedSource A p.1 ∧ deletedSource A p.2 ∧ p.1<p.2 ∧
    deletedSource A (p.2-p.1)

/-- All lost corners at a minimum zero have lower coordinate zero. -/
theorem corner_survives_delete_zero (A : Int → Prop)
    (hA : ∀ a, A a → 0≤a) (p : Int × Int × Int) (hp : sourceCorner A p) :
    sourceCorner (deletedSource A) p ↔ p.2.1≠0 := by
  rcases p with ⟨x,y,d⟩
  simp only [sourceCorner,strictSource] at hp ⊢
  constructor
  · intro h; exact h.2.1.2.1.2
  · intro hy
    have hx : x≠0 := by have := hA y hp.2.1.2.1; omega
    have hxd : x+d≠0 := by have := hA y hp.2.1.2.1; omega
    have hyd : y+d≠0 := by have := hA y hp.2.1.2.1; omega
    exact ⟨hp.1,⟨⟨hp.2.1.1,hx⟩,⟨hp.2.1.2.1,hy⟩,hp.2.1.2.2⟩,
      ⟨⟨hp.2.2.1.1,hxd⟩,⟨hp.2.2.1.2.1,hy⟩,hp.2.2.1.2.2⟩,
      ⟨⟨hp.2.2.2.1,hxd⟩,⟨hp.2.2.2.2.1,hyd⟩,hp.2.2.2.2.2⟩⟩

/-- Exact parametrization of lost corners by arcs of J₀(A). -/
theorem endpoint_arc_corner (A : Int → Prop) (hA : ∀ a, A a → 0≤a)
    (hzero : A 0) (x w : Int) :
    endpointArc A (x,w) ↔ sourceCorner A (x,0,w-x) := by
  constructor
  · intro h
    have hx := hA x h.1.1
    have e : x+(w-x)=w := by omega
    dsimp [sourceCorner,strictSource]
    simp only [e,Int.zero_add]
    exact ⟨by have := h.2.2.1; omega,
      ⟨h.1.1,hzero,by have := h.1.2; omega⟩,
      ⟨h.2.1.1,hzero,by have := h.2.2.1; omega⟩,
      ⟨h.2.1.1,h.2.2.2.1,by have := h.1.2; omega⟩⟩
  · intro h
    have e : x+(w-x)=w := by omega
    simp only [sourceCorner,strictSource,e,Int.zero_add] at h
    exact ⟨⟨h.2.1.1,by omega⟩,⟨h.2.2.1.1,by omega⟩,
      by omega,⟨h.2.2.2.2.1,by omega⟩⟩

#print axioms corner_to_fiber
#print axioms fiber_to_corner
#print axioms corner_fiber_left_inverse
#print axioms corner_fiber_right_inverse
#print axioms corner_survives_delete_zero
#print axioms endpoint_arc_corner
#print axioms square_diagonal_restriction
#print axioms weak_restriction_complete
#print axioms cyclic_embedding_injective
#print axioms cyclic_embedding_no_corner
end EnergyForcing
