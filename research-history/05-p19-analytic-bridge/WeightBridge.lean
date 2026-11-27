import Mathlib

/-!
Draft: finite-dimensional real linear algebra bridge for the P19 certificate.
No computation on the large integer matrices is done here.
All enclosure and row inequalities are explicit hypotheses, not axioms.
This source has not yet been compiled.
-/

open scoped BigOperators
namespace P19Bridge

variable {ι : Type*} [Fintype ι] [DecidableEq ι] [Nonempty ι]

/-- Absolute row sum controls the action on a vector. -/
theorem row_bound (M : Matrix ι ι ℝ) (x : ι → ℝ) (c m : ℝ)
    (hm : 0 ≤ m) (hc : ∀ i, (∑ j, |M i j|) ≤ c)
    (hx : ∀ j, |x j| ≤ m) (i : ι) : |M.mulVec x i| ≤ c * m := by
  change |∑ j, M i j * x j| ≤ c * m
  calc
    |∑ j, M i j * x j| ≤ ∑ j, |M i j * x j| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ j, |M i j| * m := by
      apply Finset.sum_le_sum
      intro j hj
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_left (hx j) (abs_nonneg _)
    _ = (∑ j, |M i j|) * m := by rw [Finset.sum_mul]
    _ ≤ c * m := mul_le_mul_of_nonneg_right (hc i) hm

/-- A maximum absolute component exists. -/
theorem max_component (x : ι → ℝ) : ∃ k : ι, ∀ j, |x j| ≤ |x k| := by
  obtain ⟨k, _, hk⟩ := Finset.exists_max_image (Finset.univ : Finset ι)
    (fun j => |x j|) Finset.univ_nonempty
  exact ⟨k, fun j => hk j (Finset.mem_univ j)⟩

/-- A small left-inverse defect ensures injectivity, hence surjectivity. -/
theorem surjective_of_defect (B R : Matrix ι ι ℝ)
    (hD : ∀ i, (∑ j, |((1 : Matrix ι ι ℝ) - R * B) i j|) ≤ 1/1000) :
    Function.Surjective B.mulVec := by
  have hinj : Function.Injective B.mulVecLin := by
    intro x y hxy
    change B.mulVec x = B.mulVec y at hxy
    let d := x - y
    have hd : B.mulVec d = 0 := by
      change B.mulVec (x - y) = 0
      rw [Matrix.mulVec_sub, hxy, sub_self]
    have he : ((1 : Matrix ι ι ℝ) - R * B).mulVec d = d := by
      rw [Matrix.sub_mulVec, Matrix.one_mulVec, ← Matrix.mulVec_mulVec,
        hd, Matrix.mulVec_zero, sub_zero]
    obtain ⟨k, hk⟩ := max_component d
    have h := row_bound ((1 : Matrix ι ι ℝ) - R * B) d (1/1000) |d k|
      (abs_nonneg _) hD hk k
    rw [he] at h
    have hz : |d k| = 0 := by
      have hn := abs_nonneg (d k)
      linarith
    funext j
    have hj := hk j
    rw [hz] at hj
    have habs : |d j| = 0 := le_antisymm hj (abs_nonneg _)
    have hzero : d j = 0 := abs_eq_zero.mp habs
    change x j - y j = 0 at hzero
    exact sub_eq_zero.mp hzero
  have hs : Function.Surjective B.mulVecLin :=
    LinearMap.injective_iff_surjective.mp hinj
  exact hs

/-- Existence of strictly positive exact weights from real defect/residual bounds. -/
theorem positive_exact_weights (B R : Matrix ι ι ℝ) (b u : ι → ℝ)
    (hD : ∀ i, (∑ j, |((1 : Matrix ι ι ℝ) - R * B) i j|) ≤ 1/1000)
    (hE : ∀ i, |R.mulVec (b - B.mulVec u) i| ≤ 1/30000)
    (hu : ∀ i, (60000 : ℝ)/100000000 ≤ u i) :
    ∃ w : ι → ℝ, B.mulVec w = b ∧
      (∀ i, |w i - u i| < 1/20000) ∧
      (∀ i, (11 : ℝ)/20000 < w i) := by
  obtain ⟨w, hw⟩ := surjective_of_defect B R hD b
  let d := w - u
  have hd : B.mulVec d = b - B.mulVec u := by
    change B.mulVec (w - u) = b - B.mulVec u
    rw [Matrix.mulVec_sub, hw]
  have he : ((1 : Matrix ι ι ℝ) - R * B).mulVec d =
      d - R.mulVec (b - B.mulVec u) := by
    rw [Matrix.sub_mulVec, Matrix.one_mulVec, ← Matrix.mulVec_mulVec, hd]
  obtain ⟨k, hk⟩ := max_component d
  have h1 := row_bound ((1 : Matrix ι ι ℝ) - R * B) d (1/1000) |d k|
    (abs_nonneg _) hD hk k
  rw [he] at h1
  change |d k - R.mulVec (b - B.mulVec u) k| ≤ (1/1000) * |d k| at h1
  have h2 : |d k| ≤ |d k - R.mulVec (b - B.mulVec u) k| +
      |R.mulVec (b - B.mulVec u) k| := by
    have h := abs_add_le (d k - R.mulVec (b - B.mulVec u) k)
      (R.mulVec (b - B.mulVec u) k)
    rw [sub_add_cancel] at h
    exact h
  have hklt : |d k| < (1 : ℝ)/20000 := by
    have h3 := hE k
    linarith
  have herr : ∀ i, |w i - u i| < (1 : ℝ)/20000 := by
    intro i
    change |d i| < (1 : ℝ)/20000
    exact lt_of_le_of_lt (hk i) hklt
  refine ⟨w, hw, herr, ?_⟩
  intro i
  have hi := (abs_lt.mp (herr i)).1
  have hui := hu i
  linarith

/-- Row zero enforces normalization, independently of the approximate weights. -/
theorem normalized_weights (B R : Matrix ι ι ℝ) (b u : ι → ℝ) (i0 : ι)
    (hD : ∀ i, (∑ j, |((1 : Matrix ι ι ℝ) - R * B) i j|) ≤ 1/1000)
    (hE : ∀ i, |R.mulVec (b - B.mulVec u) i| ≤ 1/30000)
    (hu : ∀ i, (60000 : ℝ)/100000000 ≤ u i)
    (hrow : ∀ j, B i0 j = 1) (hb : b i0 = 1) :
    ∃ w : ι → ℝ, B.mulVec w = b ∧ (∑ i, w i) = 1 ∧
      (∀ i, (11 : ℝ)/20000 < w i) := by
  obtain ⟨w, hw, _, hp⟩ := positive_exact_weights B R b u hD hE hu
  refine ⟨w, hw, ?_, hp⟩
  have hi := congrFun hw i0
  change (∑ j, B i0 j * w j) = b i0 at hi
  simpa only [hrow, one_mul, hb] using hi

/-- Real interpretation of the compact certificate.  The hypotheses are exactly
    the scaled finite arithmetic bounds and the entrywise cosine enclosure.
    This theorem does not assume the final defect or residual estimate. -/
theorem from_compact_bounds (A B R : Matrix (Fin 91) (Fin 91) ℝ)
    (b u : Fin 91 → ℝ)
    (hBA : ∀ i j, |B i j - A i j| ≤ 1/100000000)
    (hR : ∀ i, (∑ j, |R i j|) ≤ 27)
    (hA : ∀ i, (∑ j, |((1 : Matrix (Fin 91) (Fin 91) ℝ) - R * A) i j|) ≤ 1/10000)
    (hres : ∀ i, |b i - A.mulVec u i| ≤ 1/1000000)
    (hu1 : (∑ j, |u j|) ≤ 2)
    (hu : ∀ i, (60000 : ℝ)/100000000 ≤ u i)
    (hrow : ∀ j, B 0 j = 1) (hb : b 0 = 1) :
    ∃ w : Fin 91 → ℝ, B.mulVec w = b ∧ (∑ i, w i) = 1 ∧
      (∀ i, (11 : ℝ)/20000 < w i) := by
  let D := B - A
  have hRD : ∀ i j, |(R * D) i j| ≤ 27 * (1/100000000 : ℝ) := by
    intro i j
    have h := row_bound R (fun k => D k j) 27 (1/100000000)
      (by norm_num) hR (fun k => hBA k j) i
    exact h
  have hidentity : (1 : Matrix (Fin 91) (Fin 91) ℝ) - R * B =
      (1 - R * A) - R * D := by
    dsimp [D]
    rw [Matrix.mul_sub]
    abel
  have hdef : ∀ i, (∑ j, |((1 : Matrix (Fin 91) (Fin 91) ℝ) - R * B) i j|) ≤ 1/1000 := by
    intro i
    rw [hidentity]
    calc
      (∑ j, |((1 - R * A) - R * D) i j|) ≤
          ∑ j, (|(1 - R * A) i j| + 27 * (1/100000000 : ℝ)) := by
        apply Finset.sum_le_sum
        intro j hj
        change |(1 - R * A) i j - (R * D) i j| ≤ _
        calc
          |(1 - R * A) i j - (R * D) i j| ≤
              |(1 - R * A) i j| + |(R * D) i j| := by
            simpa only [← sub_eq_add_neg, abs_neg] using
              (abs_add_le ((1 - R * A) i j) (-(R * D) i j))
          _ ≤ _ := add_le_add_left (hRD i j) _
      _ = (∑ j, |(1 - R * A) i j|) + 91 * (27 * (1/100000000 : ℝ)) := by
        rw [Finset.sum_add_distrib]
        simp [nsmul_eq_mul]
      _ ≤ 1/1000 := by linarith [hA i]
  have hDu : ∀ i, |D.mulVec u i| ≤ 2 * (1/100000000 : ℝ) := by
    intro i
    change |∑ j, D i j * u j| ≤ _
    calc
      |∑ j, D i j * u j| ≤ ∑ j, |D i j * u j| :=
        Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ j, (1/100000000 : ℝ) * |u j| := by
        apply Finset.sum_le_sum
        intro j hj
        rw [abs_mul]
        exact mul_le_mul_of_nonneg_right (hBA i j) (abs_nonneg _)
      _ = (1/100000000 : ℝ) * (∑ j, |u j|) := by rw [Finset.mul_sum]
      _ ≤ _ := by nlinarith [hu1]
  have hvec : b - B.mulVec u = (b - A.mulVec u) - D.mulVec u := by
    dsimp [D]
    rw [Matrix.sub_mulVec]
    abel
  have hresB : ∀ i, |(b - B.mulVec u) i| ≤ (1/1000000 + 2/100000000 : ℝ) := by
    intro i
    rw [hvec]
    change |(b i - A.mulVec u i) - D.mulVec u i| ≤ _
    calc
      |(b i - A.mulVec u i) - D.mulVec u i| ≤
          |b i - A.mulVec u i| + |D.mulVec u i| := by
        simpa only [← sub_eq_add_neg, abs_neg] using
          (abs_add_le (b i - A.mulVec u i) (-D.mulVec u i))
      _ ≤ _ := by linarith [hres i, hDu i]
  have hE : ∀ i, |R.mulVec (b - B.mulVec u) i| ≤ 1/30000 := by
    intro i
    have h := row_bound R (b - B.mulVec u) 27
      (1/1000000 + 2/100000000) (by norm_num) hR hresB i
    linarith
  exact normalized_weights B R b u 0 hdef hE hu hrow hb

end P19Bridge

#print axioms P19Bridge.row_bound
#print axioms P19Bridge.surjective_of_defect
#print axioms P19Bridge.positive_exact_weights
#print axioms P19Bridge.normalized_weights

#print axioms P19Bridge.from_compact_bounds
