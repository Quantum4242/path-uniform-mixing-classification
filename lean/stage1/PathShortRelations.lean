import Mathlib

/-!
Stage 1: local integer lemmas from paper/detailed-proof.md,
Parts I §3.5 and III §§4.4–4.5. This is not a formalization of the
cyclotomic localization theorem. All hypotheses are explicit.
-/

namespace PathUAM.ShortRelations

set_option maxHeartbeats 2000000

-- Use an elementary integer magnitude so that the local inequalities
-- reduce directly to Presburger arithmetic.
def mag (x : ℤ) : ℤ := if x < 0 then -x else x

lemma mag_nonneg (x : ℤ) : 0 ≤ mag x := by
  unfold mag
  split <;> omega

lemma mag_pos (x : ℤ) (hx : x ≠ 0) : 1 ≤ mag x := by
  unfold mag
  split <;> omega

lemma mag_eq_abs (x : ℤ) : mag x = |x| := by
  by_cases h : x < 0
  · simp [mag, h, abs_of_neg h]
  · simp [mag, h, abs_of_nonneg (le_of_not_gt h)]

lemma pair_ge_left (a c : ℤ) :
    2 * mag a ≤ mag (a + c) + mag (a - c) := by
  unfold mag
  split_ifs <;> omega

lemma pair_ge_right (a c : ℤ) :
    2 * mag c ≤ mag (a + c) + mag (a - c) := by
  unfold mag
  split_ifs <;> omega

/-- A column in the antisymmetric central 5×7 array. -/
def antiCol (a b c : ℤ) : ℤ :=
  mag c + mag (a+c) + mag (a-c) + mag (b+c) + mag (b-c)

def antiWeight (a b c d e : ℤ) : ℤ :=
  mag a + mag b + antiCol a b c + antiCol a b d + antiCol a b e

lemma antiCol_lower (a b c : ℤ) :
    2 * (mag a + mag b) + mag c ≤ antiCol a b c := by
  have h1 := pair_ge_left a c
  have h2 := pair_ge_left b c
  unfold antiCol
  omega

lemma antiCol_lower_unit (a b c : ℤ) (h : mag a + mag b = 1) :
    2 + 3 * mag c ≤ antiCol a b c := by
  have ha := mag_nonneg a
  have hb := mag_nonneg b
  have h1 := pair_ge_left a c
  have h2 := pair_ge_left b c
  have h3 := pair_ge_right a c
  have h4 := pair_ge_right b c
  have hz : mag a = 0 ∨ mag b = 0 := by omega
  unfold antiCol
  rcases hz with hz | hz <;> omega

/-- Necessary axis shape of any mixed antisymmetric central 35 relation
    of spectral weight at most ten: one signed unit on each axis. -/
theorem anti35_unit_axes (a b c d e : ℤ)
    (hr : a ≠ 0 ∨ b ≠ 0)
    (hc : c ≠ 0 ∨ d ≠ 0 ∨ e ≠ 0)
    (hw : antiWeight a b c d e ≤ 10) :
    mag a + mag b = 1 ∧ mag c + mag d + mag e = 1 := by
  have ha0 := mag_nonneg a
  have hb0 := mag_nonneg b
  have hc0 := mag_nonneg c
  have hd0 := mag_nonneg d
  have he0 := mag_nonneg e
  have hrpos : 1 ≤ mag a + mag b := by
    rcases hr with h | h
    · have hp := mag_pos a h
      omega
    · have hp := mag_pos b h
      omega
  have hcpos : 1 ≤ mag c + mag d + mag e := by
    rcases hc with h | h | h
    · have hp := mag_pos c h
      omega
    · have hp := mag_pos d h
      omega
    · have hp := mag_pos e h
      omega
  have h1 := antiCol_lower a b c
  have h2 := antiCol_lower a b d
  have h3 := antiCol_lower a b e
  unfold antiWeight at hw
  have hrow : mag a + mag b = 1 := by omega
  have k1 := antiCol_lower_unit a b c hrow
  have k2 := antiCol_lower_unit a b d hrow
  have k3 := antiCol_lower_unit a b e hrow
  exact ⟨hrow, by omega⟩

/-- Magnitude one is equivalent to a signed unit. -/
lemma mag_one (a : ℤ) : mag a = 1 ↔ a = 1 ∨ a = -1 := by
  unfold mag
  split <;> omega

@[simp] lemma mag_zero : mag 0 = 0 := by decide

lemma mag_neg (x : ℤ) : mag (-x) = mag x := by
  unfold mag
  split_ifs <;> omega

lemma mag_diff_le (a b c : ℤ) :
    mag (a-b) ≤ mag (a+c) + mag (b+c) := by
  unfold mag
  split_ifs <;> omega

lemma mag_axis_le (a c : ℤ) : mag a ≤ mag c + mag (a+c) := by
  unfold mag
  split_ifs <;> omega

/-- Symmetric central 5×7 array (origin absent). -/
def symCol (a b c : ℤ) : ℤ :=
  mag c + 2 * mag (a+c) + 2 * mag (b+c)

def symWeight (a b c d e : ℤ) : ℤ :=
  mag a + mag b + symCol a b c + symCol a b d + symCol a b e

lemma symCol_diff (a b c : ℤ) : 2 * mag (a-b) ≤ symCol a b c := by
  have h := mag_diff_le a b c
  have hc := mag_nonneg c
  unfold symCol
  omega

lemma consecutive_nonzero_mass (a b : ℤ) (ha : a ≠ 0) (hb : b ≠ 0)
    (hd : mag (a-b) = 1) : 3 ≤ mag a + mag b := by
  unfold mag at hd ⊢
  split_ifs at * <;> omega

lemma symCol_ge_three (a b c : ℤ) (hd : mag (a-b) = 1)
    (hr : 3 ≤ mag a + mag b) : 3 ≤ symCol a b c := by
  by_cases hc : c = 0
  · subst c
    simp only [symCol, mag_zero, add_zero, zero_add]
    omega
  · have h := mag_diff_le a b c
    have hpos := mag_pos c hc
    unfold symCol
    omega

lemma symCol_bad (a b c : ℤ) (hr : mag a + mag b = 1)
    (hc : c ≠ 0) (hd : c ≠ -(a+b)) : 7 ≤ symCol a b c := by
  unfold symCol
  unfold mag at hr ⊢
  split_ifs at * <;> omega

lemma symCol_choice (a b c : ℤ) (hr : mag a + mag b = 1)
    (hw : symCol a b c ≤ 5) : c = 0 ∨ c = -(a+b) := by
  by_cases hc : c = 0
  · exact Or.inl hc
  · by_cases hd : c = -(a+b)
    · exact Or.inr hd
    · have h := symCol_bad a b c hr hc hd
      omega

/-- The unequal-row branch of the symmetric central conductor-35
    inventory: up to row swap and sign the row pair is (0,1), and
    each column is 0 or the negative of the nonzero row. -/
theorem sym35_unequal_axes (a b c d e : ℤ) (hab : a ≠ b)
    (hw : symWeight a b c d e ≤ 10) :
    mag a + mag b = 1 ∧ (c = 0 ∨ c = -(a+b)) ∧
      (d = 0 ∨ d = -(a+b)) ∧ (e = 0 ∨ e = -(a+b)) := by
  have ha0 := mag_nonneg a
  have hb0 := mag_nonneg b
  have hdiff := mag_pos (a-b) (sub_ne_zero.mpr hab)
  have h1 := symCol_diff a b c
  have h2 := symCol_diff a b d
  have h3 := symCol_diff a b e
  unfold symWeight at hw
  have hd1 : mag (a-b) = 1 := by omega
  have hr : mag a + mag b = 1 := by
    by_cases ha : a = 0
    · subst a
      simpa [mag_neg] using hd1
    · by_cases hb : b = 0
      · subst b
        simpa using hd1
      · have hrow := consecutive_nonzero_mass a b ha hb hd1
        have k1 := symCol_ge_three a b c hd1 hrow
        have k2 := symCol_ge_three a b d hd1 hrow
        have k3 := symCol_ge_three a b e hd1 hrow
        omega
  exact ⟨hr, symCol_choice a b c hr (by omega),
    symCol_choice a b d hr (by omega), symCol_choice a b e hr (by omega)⟩

lemma symCol_equal_lower (a c : ℤ) :
    mag a + 3 * mag (a+c) ≤ symCol a a c := by
  have h := mag_axis_le a c
  unfold symCol
  omega

/-- Equal, nonzero rows: the common row is a signed unit with at most
    one unit of column deviation, or a signed double with no deviation.
    The zero-row (pure-cycle) case is deliberately excluded. -/
theorem sym35_equal_axes (a c d e : ℤ) (ha : a ≠ 0)
    (hw : symWeight a a c d e ≤ 10) :
    (mag a = 1 ∧ mag (a+c) + mag (a+d) + mag (a+e) ≤ 1) ∨
    (mag a = 2 ∧ mag (a+c) + mag (a+d) + mag (a+e) = 0) := by
  have hpos := mag_pos a ha
  have h1 := symCol_equal_lower a c
  have h2 := symCol_equal_lower a d
  have h3 := symCol_equal_lower a e
  have k1 := mag_nonneg (a+c)
  have k2 := mag_nonneg (a+d)
  have k3 := mag_nonneg (a+e)
  unfold symWeight at hw
  omega

/-- Slice sizes for conductor 385. The middle slice has even size;
    the other ten are paired by inversion. Each paired slice has size
    1 or at least 4. With total support 20, the only possibilities are
    the two used in the manuscript. -/
theorem support385 (z u v w x y : ℕ)
    (hz : 4 ≤ z) (hpar : z % 2 = 0)
    (hu : u = 1 ∨ 4 ≤ u) (hv : v = 1 ∨ 4 ≤ v)
    (hw : w = 1 ∨ 4 ≤ w) (hx : x = 1 ∨ 4 ≤ x)
    (hy : y = 1 ∨ 4 ≤ y)
    (ht : z + 2 * (u+v+w+x+y) = 20) :
    (z = 10 ∧ u=1 ∧ v=1 ∧ w=1 ∧ x=1 ∧ y=1) ∨
    (z = 4 ∧
      ((u=4 ∧ v=1 ∧ w=1 ∧ x=1 ∧ y=1) ∨
       (u=1 ∧ v=4 ∧ w=1 ∧ x=1 ∧ y=1) ∨
       (u=1 ∧ v=1 ∧ w=4 ∧ x=1 ∧ y=1) ∨
       (u=1 ∧ v=1 ∧ w=1 ∧ x=4 ∧ y=1) ∨
       (u=1 ∧ v=1 ∧ w=1 ∧ x=1 ∧ y=4))) := by
  rcases hu with hu | hu <;> rcases hv with hv | hv <;>
    rcases hw with hw | hw <;> rcases hx with hx | hx <;>
    rcases hy with hy | hy <;> omega

/-- Half-weight of the exceptional symmetric 5×7 central slice,
    after subtraction of the origin. -/
def sym385Col (a b c : ℤ) : ℤ :=
  mag c + 2 * mag (a+c) + 2 * mag (b+c)

def sym385Weight (a b c d e : ℤ) : ℤ :=
  mag (a-1) + mag (b-1) + sym385Col a b c +
    sym385Col a b d + sym385Col a b e

/-- Stronger than the manuscript's last 385 check: the half-weight is
    not 5 on the entire 3^5 box, even without the extra entry bounds.
    interval_cases produces only 243 small arithmetic branches. -/
theorem central385_no_weight5 (a b c d e : ℤ)
    (ha0 : 0 ≤ a) (ha2 : a ≤ 2)
    (hb0 : 0 ≤ b) (hb2 : b ≤ 2)
    (hc0 : -1 ≤ c) (hc1 : c ≤ 1)
    (hd0 : -1 ≤ d) (hd1 : d ≤ 1)
    (he0 : -1 ≤ e) (he1 : e ≤ 1) :
    sym385Weight a b c d e ≠ 5 := by
  intro h
  interval_cases a <;> interval_cases b <;> interval_cases c <;>
    interval_cases d <;> interval_cases e <;>
    norm_num [sym385Weight, sym385Col, mag] at h

#print axioms mag_eq_abs
#print axioms anti35_unit_axes
#print axioms sym35_unequal_axes
#print axioms sym35_equal_axes
#print axioms support385
#print axioms central385_no_weight5

end PathUAM.ShortRelations
