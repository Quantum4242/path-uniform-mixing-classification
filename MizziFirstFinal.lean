import MizziFirstTwoPower
import Mathlib.Data.Nat.ModEq

/-! Candidate end-to-end formalization of the first conjecture.
    The preceding five modules were checked by the user in Lean 4.36.0.
    This new module has not yet been compiled. -/

namespace MizziCore

section Arithmetic

private theorem first_pow_dvd (a b : ℕ) (h : a ≤ b) : 2^a ∣ 2^b := by
  refine ⟨2^(b-a), ?_⟩
  rw [← pow_add, show a+(b-a)=b by omega]

private theorem first_two_pow_pos (b : ℕ) : 0 < (2:ℕ)^b := by
  induction b with
  | zero => simp
  | succ b ih => rw [pow_succ]; omega

private theorem first_two_pow_even (b : ℕ) (hb : 0 < b) :
    2 ≤ 2^b ∧ 2^b % 2 = 0 := by
  obtain ⟨d, hd⟩ : ∃ d : ℕ, b = d+1 := ⟨b-1, by omega⟩
  rw [hd, pow_succ]
  have hp : 0 < (2:ℕ)^d := first_two_pow_pos d
  omega

private def firstModFin {P L : ℕ} (hL : 0 < L) (x : Fin P) : Fin L :=
  ⟨x.val % L, Nat.mod_lt _ hL⟩

private theorem first_reflect_sum_mod {P L : ℕ} (hd : L ∣ P) (c x : Fin P) :
    Nat.ModEq L (x.val + (reflection c x).val) c.val := by
  have hc := c.isLt
  have hx := x.isLt
  have hsum : x.val + (reflection c x).val = c.val ∨
      x.val + (reflection c x).val = P + c.val := by
    change x.val + rv P c.val x.val = c.val ∨ x.val + rv P c.val x.val = P+c.val
    unfold rv
    split <;> omega
  rcases hsum with h | h
  · rw [h]
  · rw [h]
    change (P+c.val)%L = c.val%L
    rw [Nat.add_mod, Nat.mod_eq_zero_of_dvd hd, zero_add, Nat.mod_mod]

/-- Reflection commutes with reducing coordinates to a common divisor. -/
theorem first_reflection_mod {P L : ℕ} (hL : 0 < L) (hd : L ∣ P) (c x : Fin P) :
    firstModFin hL (reflection c x) =
      reflection (firstModFin hL c) (firstModFin hL x) := by
  have h1 := first_reflect_sum_mod hd c x
  have h2 := first_reflect_sum_mod (dvd_refl L) (firstModFin hL c) (firstModFin hL x)
  have hc : Nat.ModEq L c.val (firstModFin hL c).val := by
    change c.val%L = (c.val%L)%L
    rw [Nat.mod_mod]
  have hx : Nat.ModEq L x.val (firstModFin hL x).val := by
    change x.val%L = (x.val%L)%L
    rw [Nat.mod_mod]
  have hh := Nat.ModEq.add_left_cancel hx ((h1.trans hc).trans h2.symm)
  change (reflection c x).val % L =
    (reflection (firstModFin hL c) (firstModFin hL x)).val % L at hh
  apply Fin.ext
  change (reflection c x).val % L = (reflection (firstModFin hL c) (firstModFin hL x)).val
  exact hh.trans (Nat.mod_eq_of_lt (reflection (firstModFin hL c) (firstModFin hL x)).isLt)

private theorem first_pow_reduce {V : Type*} {s : Equiv.Perm V} {P : ℕ}
    (hp : s^P = 1) (n : ℕ) : s^(n%P) = s^n := by
  calc
    s^(n%P) = s^(n%P) * s^(P*(n/P)) := by rw [pow_mul, hp, one_pow, mul_one]
    _ = s^(n%P + P*(n/P)) := (pow_add _ _ _).symm
    _ = s^n := congrArg (fun i : ℕ => s^i) (Nat.mod_add_div n P)

end Arithmetic

section Rotation
variable {V : Type*} {A : V → V → Prop} {s : Equiv.Perm V}

/-- Rotate the quotient cycle to start at a shortest nontrivial orbit. -/
theorem first_minimal_representatives [Fintype V] {a k : ℕ} (hp : s^(2^a) = 1)
    (hk : 3 ≤ k) (rep : ℕ → V) (c : ℕ → ℕ)
    (hm : ∀ i, i < k → s (rep i) ≠ rep i)
    (hd : ∀ i j, i < k → j < k → orbitClass s (rep i) = orbitClass s (rep j) → i = j)
    (he : ∀ i, i+1 < k → A (rep i) ((s^c i) (rep (i+1))))
    (hc : A (rep (k-1)) ((s^c (k-1)) (rep 0))) :
    ∃ (L : ℕ) (r : ℕ → V) (d : ℕ → ℕ),
      2 ≤ L ∧ L%2 = 0 ∧ L ∣ 2^a ∧ firstOrbitLength s (r 0) = L ∧
      (∀ i, i < k → L ∣ firstOrbitLength s (r i)) ∧
      (∀ i, i < k → s (r i) ≠ r i) ∧
      (∀ i j, i < k → j < k → orbitClass s (r i) = orbitClass s (r j) → i = j) ∧
      (∀ i, i+1 < k → A (r i) ((s^d i) (r (i+1)))) ∧
      A (r (k-1)) ((s^d (k-1)) (r 0)) := by
  classical
  let Q : ℕ → Prop := fun b => ∃ i, i < k ∧ 0 < b ∧ b ≤ a ∧ firstOrbitLength s (rep i) = 2^b
  have hQ : ∃ b, Q b := by
    obtain ⟨b,hb,hba,hl⟩ := first_orbitLength_two_power s hp (hm 0 (by omega))
    exact ⟨b,0,by omega,hb,hba,hl⟩
  let b := Nat.find hQ
  obtain ⟨m,hmk,hb,hba,hmL⟩ := Nat.find_spec hQ
  let L := 2^b
  have hLev := first_two_pow_even b hb
  let rot : ℕ → ℕ := fun i => if m+i < k then m+i else m+i-k
  have hrot0 : rot 0 = m := by simp [rot, hmk]
  have hrotk : rot k = rot 0 := by
    rw [hrot0]
    dsimp [rot]
    split <;> omega
  have hrlt (i : ℕ) (hi : i < k) : rot i < k := by
    dsimp [rot]
    split <;> omega
  have hrinj (i j : ℕ) (hi : i < k) (hj : j < k) (h : rot i = rot j) : i = j := by
    dsimp [rot] at h
    split_ifs at h <;> omega
  have hrsucc (i : ℕ) (hi : i < k) : rot (i+1) = if rot i + 1 < k then rot i + 1 else 0 := by
    dsimp [rot]
    split_ifs <;> omega
  have hedge (i : ℕ) (hi : i < k) : A (rep (rot i)) ((s^c (rot i)) (rep (rot (i+1)))) := by
    rw [hrsucc i hi]
    by_cases h : rot i+1 < k
    · rw [if_pos h]
      exact he _ h
    · rw [if_neg h]
      have hh : rot i = k-1 := by have := hrlt i hi; omega
      rw [hh]
      exact hc
  refine ⟨L, fun i => rep (rot i), fun i => c (rot i), hLev.1, hLev.2,
    first_pow_dvd b a hba, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [hrot0]
    exact hmL
  · intro i hi
    obtain ⟨j,hj,hja,hjL⟩ := first_orbitLength_two_power s hp (hm (rot i) (hrlt i hi))
    have hbmin : b ≤ j := Nat.find_min' hQ (show Q j from ⟨rot i,hrlt i hi,hj,hja,hjL⟩)
    rw [hjL]
    exact first_pow_dvd b j hbmin
  · intro i hi
    exact hm (rot i) (hrlt i hi)
  · intro i j hi hj h
    exact hrinj i j hi hj (hd (rot i) (rot j) (hrlt i hi) (hrlt j hj) h)
  · intro i hi
    exact hedge i (by omega)
  · have h := hedge (k-1) (by omega)
    rw [show k-1+1=k by omega, hrotk] at h
    exact h

end Rotation

section ActualBlocks
variable {V : Type*} {A B : V → V → Prop} {s : Equiv.Perm V} {P L k : ℕ}

/-- Construct the audited abstract BlockData from genuine permutation orbits.
    P is a global period, and L is the shortest local period on the cycle. -/
noncomputable def first_actual_blocks [Fintype V] (hP : 0 < P) (hL : 0 < L)
    (hLP : L ∣ P) (hk : 3 ≤ k) (hp : s^P = 1) (ht : Twisted A s)
    (rep : ℕ → V) (c : ℕ → Fin P)
    (hperiod : firstOrbitLength s (rep 0) = L)
    (hdiv : ∀ i, i < k → L ∣ firstOrbitLength s (rep i))
    (hm : ∀ i, i < k → s (rep i) ≠ rep i)
    (hd : ∀ i j, i < k → j < k → orbitClass s (rep i) = orbitClass s (rep j) → i = j)
    (he : ∀ i, i+1 < k → A (rep i) ((s^(c i).val) (rep (i+1))))
    (hc : A (rep (k-1)) ((s^(c (k-1)).val) (rep 0))) :
    BlockData A k (fun i => firstModFin hL (c i)) := by
  classical
  let block : ℕ → V → Prop := fun i v => orbitClass s v = orbitClass s (rep i)
  let Q : V → Prop := fun v => ∃ z : Fin P, ∃ i : ℕ, i < k ∧ (s^z.val) (rep i) = v
  let label : V → Fin P := fun v => if h : Q v then Classical.choose h else ⟨0,hP⟩
  have hblockLabel (i : ℕ) (v : V) (hi : i < k) (hv : block i v) : Q v := by
    have hh : orbitClass s (rep i) = orbitClass s v := hv.symm
    obtain ⟨n,hn⟩ := ((orbitClass_eq_iff s _ _).mp hh).exists_nat_pow_eq
    refine ⟨⟨n%P,Nat.mod_lt _ hP⟩,i,hi,?_⟩
    change (s^(n%P)) (rep i) = v
    rw [first_pow_reduce hp]
    exact hn
  have hlabelAt (i : ℕ) (v : V) (hi : i < k) (hv : block i v) :
      (s^(label v).val) (rep i) = v := by
    have hq := hblockLabel i v hi hv
    obtain ⟨j,hj,hz⟩ := Classical.choose_spec hq
    have hlabel : label v = Classical.choose hq := by simp [label,hq]
    rw [← hlabel] at hz
    have hcl : orbitClass s (rep j) = orbitClass s (rep i) := by
      calc
        orbitClass s (rep j) = orbitClass s ((s^(label v).val) (rep j)) := (orbitClass_pow s _ _).symm
        _ = orbitClass s v := congrArg (orbitClass s) hz
        _ = orbitClass s (rep i) := hv
    have hji := hd j i hj hi hcl
    simpa only [hji] using hz
  let residue : V → Fin L := fun v => firstModFin hL (label v)
  have hres (i : ℕ) (hi : i < k) (z : Fin P) (v : V) (hz : (s^z.val) (rep i) = v) :
      residue v = firstModFin hL z := by
    have hv : block i v := by
      change orbitClass s v = orbitClass s (rep i)
      rw [← hz]
      exact orbitClass_pow s _ _
    apply Fin.ext
    change (label v).val % L = z.val % L
    exact first_label_common_mod s (hm i hi) (hdiv i hi) ((hlabelAt i v hi hv).trans hz.symm)
  have hle : L ≤ P := Nat.le_of_dvd hP hLP
  let start : Fin L → V := fun x => (s^x.val) (rep 0)
  let next : ℕ → V → V := fun i v => (s^(reflection (c i) (label v)).val) (rep (i+1))
  refine { block := block, residue := residue, start := start, next := next,
    start_mem := ?_, start_residue := ?_, disjoint := ?_, next_mem := ?_,
    next_edge := ?_, next_residue := ?_, last_edge := ?_ }
  · intro x
    exact orbitClass_pow s _ _
  · intro x
    let z : Fin P := ⟨x.val, lt_of_lt_of_le x.isLt hle⟩
    have hh := hres 0 (by omega) z (start x) rfl
    apply Fin.ext
    exact (congrArg Fin.val hh).trans (Nat.mod_eq_of_lt x.isLt)
  · intro i j v hi hj hv hw
    exact hd i j hi hj (hv.symm.trans hw)
  · intro i v hi hv
    exact orbitClass_pow s _ _
  · intro i v hi hv
    have hh := prime_reflection_edge ht hp (c i) (label v) (he i hi)
    rw [hlabelAt i v (by omega) hv] at hh
    exact hh
  · intro i v hi hv
    change residue (next i v) = reflection (firstModFin hL (c i)) (firstModFin hL (label v))
    rw [hres (i+1) hi (reflection (c i) (label v)) (next i v) rfl]
    exact first_reflection_mod hL hLP _ _
  · intro v hv
    have hh := prime_reflection_edge ht hp (c (k-1)) (label v) hc
    rw [hlabelAt (k-1) v (by omega) hv] at hh
    have hred := first_label_mod_apply s (rep 0) (reflection (c (k-1)) (label v)).val
    rw [hperiod] at hred
    have hr := congrArg Fin.val (first_reflection_mod hL hLP (c (k-1)) (label v))
    change (reflection (c (k-1)) (label v)).val % L =
      (reflection (firstModFin hL (c (k-1))) (firstModFin hL (label v))).val at hr
    rw [hr] at hred
    change A v ((s^(reflection (firstModFin hL (c (k-1))) (firstModFin hL (label v))).val) (rep 0))
    rw [hred]
    exact hh

private theorem first_column_twisted (ht : Twisted A s)
    (hcol : ∀ x y, B x y ↔ A x (s y)) : Twisted B s := by
  intro x y
  calc
    B (s x) (s.symm y) ↔ A (s x) (s (s.symm y)) := hcol _ _
    _ ↔ A (s x) y := by rw [s.apply_symm_apply]
    _ ↔ A x (s y) := twisted_shift ht _ _
    _ ↔ B x y := (hcol _ _).symm

private theorem first_column_edge (hp : s^P = 1) (one : Fin P) (hone : one.val = 1)
    (hcol : ∀ x y, B x y ↔ A x (s y)) (x y : V) (c : Fin P)
    (he : A x ((s^c.val) y)) : B x ((s^(reflection c one).val) y) := by
  apply (hcol _ _).mpr
  have hsum : 1 + (reflection c one).val = c.val ∨
      1 + (reflection c one).val = P+c.val := by
    have h1 := one.isLt
    have h2 := c.isLt
    change 1 + rv P c.val one.val = c.val ∨ 1 + rv P c.val one.val = P+c.val
    rw [hone]
    unfold rv
    split <;> omega
  have hpow : s * s^(reflection c one).val = s^(1+(reflection c one).val) := by rw [pow_add, pow_one]
  rw [← Equiv.Perm.mul_apply, hpow]
  rcases hsum with h | h
  · rw [h]; exact he
  · rw [h,pow_add,hp,one_mul]; exact he

/-- A column shift changes every reduced reflection constant by one modulo L. -/
theorem first_column_parity (hL : 2 ≤ L) (hLe : L%2 = 0) (hLP : L ∣ P)
    (one : Fin P) (hone : one.val = 1) (c : Fin P) :
    ((firstModFin (by omega : 0 < L) c).val +
      (firstModFin (by omega : 0 < L) (reflection c one)).val)%2 = 1 := by
  have hpos : 0 < L := by omega
  rw [first_reflection_mod hpos hLP]
  have h1 : (firstModFin hpos one).val = 1 := by
    change one.val%L = 1
    rw [hone, Nat.mod_eq_of_lt (by omega : 1 < L)]
  have h2 := (firstModFin hpos c).isLt
  change ((firstModFin hpos c).val + rv L (firstModFin hpos c).val (firstModFin hpos one).val)%2 = 1
  rw [h1]
  unfold rv
  split <;> omega

/-- Obtain the two different cycle types in the two column-related graphs. -/
theorem first_even_actual_pair [Fintype V] {a : ℕ} (hp : s^(2^a) = 1)
    (ht : Twisted A s) (hcol : ∀ x y, B x y ↔ A x (s y))
    (hs : ∀ x y, A x y ↔ A y x) (ho : k%2 = 1)
    (C : Cycle (movedOrbitGraph A s).Adj k) :
    (HasTwo A k ∧ Nonempty (Cycle B (2*k))) ∨
    (HasTwo B k ∧ Nonempty (Cycle A (2*k))) := by
  obtain ⟨r,d,hm,hd,he,hc⟩ := first_cycle_representatives hs C
  obtain ⟨L,rep,c,hL,hLe,hLP,hperiod,hdiv,hm',hd',he',hc'⟩ :=
    first_minimal_representatives hp C.length_ge r d hm hd he hc
  let P := 2^a
  have hP : 0 < P := first_two_pow_pos a
  have hL' : 0 < L := by omega
  have hle : L ≤ P := Nat.le_of_dvd hP hLP
  let one : Fin P := ⟨1,by omega⟩
  let ca : ℕ → Fin P := fun i => ⟨c i%P,Nat.mod_lt _ hP⟩
  let cb : ℕ → Fin P := fun i => reflection (ca i) one
  have ha (i : ℕ) (hi : i+1 < k) : A (rep i) ((s^(ca i).val) (rep (i+1))) := by
    change A (rep i) ((s^(c i%P)) (rep (i+1)))
    rw [first_pow_reduce hp]
    exact he' i hi
  have hac : A (rep (k-1)) ((s^(ca (k-1)).val) (rep 0)) := by
    change A (rep (k-1)) ((s^(c (k-1)%P)) (rep 0))
    rw [first_pow_reduce hp]
    exact hc'
  have hb (i : ℕ) (hi : i+1 < k) : B (rep i) ((s^(cb i).val) (rep (i+1))) :=
    first_column_edge hp one rfl hcol _ _ (ca i) (ha i hi)
  have hbc : B (rep (k-1)) ((s^(cb (k-1)).val) (rep 0)) :=
    first_column_edge hp one rfl hcol _ _ (ca (k-1)) hac
  let D := first_actual_blocks hP hL' hLP C.length_ge hp ht rep ca hperiod hdiv hm' hd' ha hac
  let E := first_actual_blocks hP hL' hLP C.length_ge hp (first_column_twisted ht hcol)
    rep cb hperiod hdiv hm' hd' hb hbc
  exact even_pair_from_blocks D E C.length_ge ho hL hLe (fun i => first_column_parity hL hLe hLP one rfl (ca i))

end ActualBlocks

section Finish
variable {V W : Type*} {A : V → V → Prop} {B : W → W → Prop}

private def firstMapCycle (e : V ≃ W) (he : ∀ x y, A x y ↔ B (e x) (e y))
    {k : ℕ} (C : Cycle A k) : Cycle B k where
  vertex i := e (C.vertex i)
  length_ge := C.length_ge
  distinct i j hi hj h := C.distinct i j hi hj (e.injective h)
  step i hi := (he _ _).mp (C.step i hi)
  close := (he _ _).mp C.close

private theorem first_map_nonempty {k : ℕ} (h : Iso A B) (hc : Nonempty (Cycle A k)) :
    Nonempty (Cycle B k) := by
  obtain ⟨e,he⟩ := h
  obtain ⟨C⟩ := hc
  exact ⟨firstMapCycle e he C⟩

private theorem first_map_two {k : ℕ} (h : Iso A B) (hc : HasTwo A k) : HasTwo B k := by
  obtain ⟨e,he⟩ := h
  obtain ⟨C,D,hs⟩ := hc
  refine ⟨firstMapCycle e he C, firstMapCycle e he D, ?_⟩
  intro i j hi hj hh
  exact hs i j hi hj (e.injective hh)

/-- Final statement: no extra layout, orbit or coloring assumptions. -/
theorem original1_final : Original1 := by
  intro n A B hsA hsB hcA hcB hn hi
  obtain ⟨D,s,hsD,hDB,hnD,ht,hcol,_⟩ := first_column_reduction hsA hsB hcA hcB hn hi
  obtain ⟨E,t,a,hsE,hED,_,ht',hp,hcol',hcolor⟩ := first_two_power_reduction hsA hsD ht hcol hnD
  obtain ⟨k,ho,⟨C⟩⟩ := first_actual_odd_cycle hsA hsE ht' hcol' hcolor
  have hEB := first_iso_trans hED hDB
  refine ⟨k,C.length_ge,ho,?_⟩
  rcases first_even_actual_pair hp ht' hcol' hsA.2 ho C with h | h
  · exact Or.inl ⟨h.1,first_map_nonempty hEB h.2⟩
  · exact Or.inr ⟨first_map_two hEB h.1,h.2⟩

end Finish

#print axioms first_reflection_mod
#print axioms first_minimal_representatives
#print axioms first_actual_blocks
#print axioms first_column_parity
#print axioms first_even_actual_pair
#print axioms original1_final

end MizziCore
