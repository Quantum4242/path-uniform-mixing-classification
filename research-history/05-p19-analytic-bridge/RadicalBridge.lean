import Mathlib

/-! Draft analytic identities for the alternative interval algorithm.
The interval arithmetic and Taylor remainder still require formalization.
This file has not been compiled. -/

namespace P19Radical

/-- Positive half-angle identity, derived without any numerical approximation to pi. -/
theorem half_angle (x : ℝ) (h : 0 ≤ Real.cos x) :
    2 * Real.cos x = Real.sqrt (2 + 2 * Real.cos (2*x)) := by
  have hsq : (2 * Real.cos x)^2 = 2 + 2 * Real.cos (2*x) := by
    rw [Real.cos_two_mul]
    ring
  rw [← hsq, Real.sqrt_sq_eq_abs, abs_of_nonneg (by positivity : 0 ≤ 2 * Real.cos x)]

/-- Exact first energy of the path P19. -/
theorem theta_one : 2 * Real.cos (Real.pi / 20) =
    Real.sqrt (2 + Real.sqrt ((5 + Real.sqrt 5) / 2)) := by
  have hp := Real.pi_pos
  have h20 : 0 ≤ Real.cos (Real.pi / 20) :=
    Real.cos_nonneg_of_neg_pi_div_two_le_of_le (by linarith) (by linarith)
  have h10 : 0 ≤ Real.cos (Real.pi / 10) :=
    Real.cos_nonneg_of_neg_pi_div_two_le_of_le (by linarith) (by linarith)
  have e20 := half_angle (Real.pi / 20) h20
  have e10 := half_angle (Real.pi / 10) h10
  rw [show 2 * (Real.pi / 20) = Real.pi / 10 by ring] at e20
  rw [show 2 * (Real.pi / 10) = Real.pi / 5 by ring, Real.cos_pi_div_five] at e10
  have e : (2 : ℝ) + 2 * ((1 + Real.sqrt 5) / 4) =
      (5 + Real.sqrt 5) / 2 := by ring
  rw [e20, e10, e]

/-- Chebyshev recurrence for twice the cosine, for every real base angle. -/
theorem theta_recurrence (a x : ℝ) :
    2 * Real.cos (x+a) =
      (2 * Real.cos a) * (2 * Real.cos x) - 2 * Real.cos (x-a) := by
  rw [Real.cos_add, Real.cos_sub]
  ring

/-- Repeated doubling eliminates large arguments in the cosine enclosure. -/
def doubleCos : ℕ → ℝ → ℝ
  | 0, x => x
  | n+1, x => 2 * (doubleCos n x)^2 - 1

theorem doubleCos_correct (n : ℕ) (x : ℝ) :
    doubleCos n (Real.cos x) = Real.cos ((2 : ℝ)^n * x) := by
  induction n with
  | zero => simp [doubleCos]
  | succ n ih =>
    rw [doubleCos, ih, pow_succ (2 : ℝ) n]
    rw [show (2 : ℝ)^n * 2 * x = 2 * ((2 : ℝ)^n * x) by ring,
      Real.cos_two_mul]

end P19Radical

#print axioms P19Radical.theta_one
#print axioms P19Radical.theta_recurrence
#print axioms P19Radical.doubleCos_correct
