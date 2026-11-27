import Mathlib

/-!
Stage 1: universal positivity inequalities in the published detailed proof.
The explicit moment numerators are definitions; this file does not derive
those formulas from Haar integration or prove the Fourier error estimates.
The all-real-parameter bounds below are stronger than integer samples.
-/
namespace PathUAM.Positivity

def oddSlack (n : ℝ) : ℝ :=
  56376 * n^4 - 362232 * n^3 + 2688102 * n^2 - 7757169 * n - 1057681

def oddSlackExtra (n : ℝ) : ℝ :=
  56376 * n^4 - 362232 * n^3 + 2688102 * n^2 - 82510449 * n - 28233361

def errNum0 (n : ℝ) : ℝ :=
  54997404 * n^3 + 1410504180 * n^2 + 81997425540 * n + 225627613260

def errNum1 (n : ℝ) : ℝ :=
  311625396 * n^3 + 3876752772 * n^2 + 85909752996 * n + 266990756340

def Z0 (n : ℝ) : ℝ :=
  243409548 * n^4 - 9501470 * n^3 + 22683724 * n^2 - 37257990 * n

def U0 (n : ℝ) : ℝ :=
  -75416824 * n^3 - 76857488 * n^2 + 239386872 * n - 514837680

def D0 (n : ℝ) : ℝ :=
  -75410332 * n^3 - 31567156 * n^2 + 87726774 * n - 102967536

def Z1 (n : ℝ) : ℝ :=
  243409548 * n^4 - 47209882 * n^3 + 26186325 * n^2 - 7941564 * n + 16129

def U1 (n : ℝ) : ℝ :=
  -75416824 * n^3 - 27383060 * n^2 + 162609276 * n - 242967256

def D1 (n : ℝ) : ℝ :=
  -75410332 * n^3 - 996966 * n^2 + 50769520 * n - 37032184

def W1 (n : ℝ) : ℝ :=
  -75416824 * n^3 - 22557536 * n^2 + 128819148 * n - 115483640

theorem odd_three_base (n : ℝ) (hn : 4 ≤ n) :
    0 < oddSlack n := by
  let x : ℝ := n - 4
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 56376 * x^4 + 539784 * x^3 + 3753414 * x^2 + 10792767 * x + 2172683 := by positivity
    _ = oddSlack n := by
      unfold oddSlack
      dsimp [x]
      ring

theorem odd_three_extra (n : ℝ) (hn : 16 ≤ n) :
    0 < oddSlackExtra n := by
  let x : ℝ := n - 16
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 56376 * x^4 + 3245832 * x^3 + 71894502 * x^2 + 648979023 * x + 1550708831 := by positivity
    _ = oddSlackExtra n := by
      unfold oddSlackExtra
      dsimp [x]
      ring

def errSlack0 (n : ℝ) : ℝ := 14500000*n^4 - errNum0 n
def errSlack1 (n : ℝ) : ℝ := 14500000*n^4 - errNum1 n

theorem even_err0_num (n : ℝ) (hn : 35 ≤ n) :
    0 < errSlack0 n := by
  let x : ℝ := n - 35
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 14500000 * x^4 + 1975002596 * x^3 + 99389768400 * x^2 + 2103901822160 * x + 14577643675840 := by positivity
    _ = errSlack0 n := by
      unfold errSlack0 errNum0
      dsimp [x]
      ring

theorem even_err1_num (n : ℝ) (hn : 35 ≤ n) :
    0 < errSlack1 n := by
  let x : ℝ := n - 35
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 14500000 * x^4 + 1718374604 * x^3 + 69977580648 * x^2 + 984244222664 * x + 375269389600 := by positivity
    _ = errSlack1 n := by
      unfold errSlack1 errNum1
      dsimp [x]
      ring

/-- The error estimates in DP III §5, for every real n ≥ 35. -/
theorem even_err0 (n : ℝ) (hn : 35 ≤ n) : errNum0 n / n^4 < 14500000 := by
  have hn0 : 0 < n := by linarith
  apply (div_lt_iff₀ (pow_pos hn0 4)).2
  have h := even_err0_num n hn
  unfold errSlack0 at h
  exact sub_pos.mp h

theorem even_err1 (n : ℝ) (hn : 35 ≤ n) : errNum1 n / n^4 < 14500000 := by
  have hn0 : 0 < n := by linarith
  apply (div_lt_iff₀ (pow_pos hn0 4)).2
  have h := even_err1_num n hn
  unfold errSlack1 at h
  exact sub_pos.mp h

-- All of Z0,U0,D0,Z1,U1,D1,W1 are scaled by the same positive
-- denominator 4*n^4.  The sign choices below bound absolute values.
def base0 (n sg : ℝ) : ℝ :=
  -(4*n-1)*U0 n - Z0 n - 2*n*(sg*(U0 n-D0 n)) - 58000000*n^4

def base1 (n sg sh : ℝ) : ℝ :=
  -(4*n+1)*U1 n - Z1 n - 2*n*(sg*(U1 n-D1 n)+sh*(U1 n-W1 n)) - 58000000*n^4

theorem base0_p (n : ℝ) (hn : 2 ≤ n) :
    0 < base0 n (1) := by
  let x : ℝ := n - 2
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 270732 * x^4 + 334261118 * x^3 + 638660244 * x^2 + 1711906854 * x + 3024092284 := by positivity
    _ = base0 n (1) := by
      unfold base0 U0 Z0 D0
      dsimp [x]
      ring

theorem base0_m (n : ℝ) (hn : 2 ≤ n) :
    0 < base0 n (-1) := by
  let x : ℝ := n - 2
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 244764 * x^4 + 152892046 * x^3 + 157709436 * x^2 + 316220934 * x + 705986588 := by positivity
    _ = base0 n (-1) := by
      unfold base0 U0 Z0 D0
      dsimp [x]
      ring

theorem base1_pp (n : ℝ) (hn : 2 ≤ n) :
    0 < base1 n (1) (1) := by
  let x : ℝ := n - 2
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 270732 * x^4 + 296748038 * x^3 + 833490523 * x^2 + 1265687748 * x + 1810017123 := by positivity
    _ = base1 n (1) (1) := by
      unfold base1 U1 Z1 D1 W1
      dsimp [x]
      ring

theorem base1_pm (n : ℝ) (hn : 2 ≤ n) :
    0 < base1 n (1) (-1) := by
  let x : ℝ := n - 2
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 270732 * x^4 + 277445942 * x^3 + 852838459 * x^2 + 1064770180 * x + 1176373475 := by positivity
    _ = base1 n (1) (-1) := by
      unfold base1 U1 Z1 D1 W1
      dsimp [x]
      ring

theorem base1_mp (n : ℝ) (hn : 2 ≤ n) :
    0 < base1 n (-1) (1) := by
  let x : ℝ := n - 2
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 244764 * x^4 + 190995918 * x^3 + 646960059 * x^2 + 964020068 * x + 1107202147 := by positivity
    _ = base1 n (-1) (1) := by
      unfold base1 U1 Z1 D1 W1
      dsimp [x]
      ring

theorem base1_mm (n : ℝ) (hn : 2 ≤ n) :
    0 < base1 n (-1) (-1) := by
  let x : ℝ := n - 2
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 244764 * x^4 + 171693822 * x^3 + 666307995 * x^2 + 763102500 * x + 473558499 := by positivity
    _ = base1 n (-1) (-1) := by
      unfold base1 U1 Z1 D1 W1
      dsimp [x]
      ring

/-- The denominator-cleared version of DP III §3 (1), b=0. -/
theorem even0_base_num (n : ℝ) (hn : 2 ≤ n) :
    0 < -(4*n-1)*U0 n - Z0 n - 2*n*|U0 n-D0 n| - 58000000*n^4 := by
  by_cases h : 0 ≤ U0 n - D0 n
  · rw [abs_of_nonneg h]
    simpa [base0] using base0_p n hn
  · rw [abs_of_neg (lt_of_not_ge h)]
    simpa [base0] using base0_m n hn

/-- The denominator-cleared version of DP III §3 (1), b=1. -/
theorem even1_base_num (n : ℝ) (hn : 2 ≤ n) :
    0 < -(4*n+1)*U1 n - Z1 n - 2*n*(|U1 n-D1 n|+|U1 n-W1 n|) - 58000000*n^4 := by
  by_cases h : 0 ≤ U1 n - D1 n
  · by_cases k : 0 ≤ U1 n - W1 n
    · rw [abs_of_nonneg h, abs_of_nonneg k]
      simpa [base1] using base1_pp n hn
    · rw [abs_of_nonneg h, abs_of_neg (lt_of_not_ge k)]
      simpa [base1] using base1_pm n hn
  · by_cases k : 0 ≤ U1 n - W1 n
    · rw [abs_of_neg (lt_of_not_ge h), abs_of_nonneg k]
      simpa [base1] using base1_mp n hn
    · rw [abs_of_neg (lt_of_not_ge h), abs_of_neg (lt_of_not_ge k)]
      simpa [base1] using base1_mm n hn

-- Generic bridge: exact numerator inequalities imply the corresponding
-- rational moment inequality when the common denominator is positive.
theorem scale_slack (d n N Z U D W b : ℝ) (hd : 0 < d)
    (h : 0 < -N*U-Z-2*n*(|U-D|+|b*U-W|)-14500000*d) :
    14500000 < -N*(U/d)-Z/d-2*n*(|U/d-D/d|+|b*(U/d)-W/d|) := by
  have h1 : U/d-D/d = (U-D)/d := by ring
  have h2 : b*(U/d)-W/d = (b*U-W)/d := by ring
  calc
    14500000 < (-N*U-Z-2*n*(|U-D|+|b*U-W|))/d := by
      apply (lt_div_iff₀ hd).2
      exact sub_pos.mp h
    _ = _ := by
      simp only [h1, h2, abs_div, abs_of_pos hd]
      ring

/-- Direct unscaled inequality for b=0 with the minimal N=4n-1. -/
theorem even0_base (n : ℝ) (hn : 2 ≤ n) :
    14500000 < -(4*n-1)*(U0 n/(4*n^4))-Z0 n/(4*n^4)
       -2*n*|U0 n/(4*n^4)-D0 n/(4*n^4)| := by
  have hn0 : 0 < n := by linarith
  have hd : 0 < 4*n^4 := by positivity
  have h : 0 < -(4*n-1)*U0 n-Z0 n-2*n*(|U0 n-D0 n|+|(0:ℝ)*U0 n-0|)
        -14500000*(4*n^4) := by
    have hp := even0_base_num n hn
    simp only [zero_mul, sub_zero, abs_zero, add_zero]
    rw [show (14500000 : ℝ)*(4*n^4) = 58000000*n^4 by ring]
    exact hp
  simpa using scale_slack (4*n^4) n (4*n-1) (Z0 n) (U0 n) (D0 n) 0 0 hd h

/-- Direct unscaled inequality for b=1 with the minimal N=4n+1. -/
theorem even1_base (n : ℝ) (hn : 2 ≤ n) :
    14500000 < -(4*n+1)*(U1 n/(4*n^4))-Z1 n/(4*n^4)
       -2*n*(|U1 n/(4*n^4)-D1 n/(4*n^4)|+|U1 n/(4*n^4)-W1 n/(4*n^4)|) := by
  have hn0 : 0 < n := by linarith
  have hd : 0 < 4*n^4 := by positivity
  have h : 0 < -(4*n+1)*U1 n-Z1 n-2*n*(|U1 n-D1 n|+|(1:ℝ)*U1 n-W1 n|)
        -14500000*(4*n^4) := by
    have hp := even1_base_num n hn
    simp only [one_mul]
    rw [show (14500000 : ℝ)*(4*n^4) = 58000000*n^4 by ring]
    exact hp
  simpa using scale_slack (4*n^4) n (4*n+1) (Z1 n) (U1 n) (D1 n) (W1 n) 1 hd h

-- Part I §4: denominator-cleared bounds for the odd, 3-coprime case.
theorem odd0_gap_num (n : ℝ) (hn : 3 ≤ n) :
    0 < 7704*n^2 - 17346*n + 46305 := by
  let x : ℝ := n - 3
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 7704*x^2 + 28878*x + 63603 := by positivity
    _ = 7704*n^2 - 17346*n + 46305 := by
      dsimp [x]
      ring

theorem odd0_non35_error_num (n : ℝ) (hn : 27 ≤ n) :
    0 < 160*n^4 - 56448*n^2 - 1451520*n - 4233600 := by
  let x : ℝ := n - 27
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 160*x^4 + 17280*x^3 + 643392*x^2 + 8097408*x + 455328 := by positivity
    _ = 160*n^4 - 56448*n^2 - 1451520*n - 4233600 := by
      dsimp [x]
      ring

theorem odd0_mult35_error_num (n : ℝ) (hn : 87 ≤ n) :
    0 < 25*n^4 - 56448*n^2 - 11007360*n - 4572288 := by
  let x : ℝ := n - 87
  have hx : 0 ≤ x := sub_nonneg.mpr hn
  calc
    0 < 25*x^4 + 8700*x^3 + 1078902*x^2 + 45020988*x + 42776505 := by positivity
    _ = 25*n^4 - 56448*n^2 - 11007360*n - 4572288 := by
      dsimp [x]
      ring

theorem q35_margin : (31239432 : ℚ)/83521 < 5397327/4913 := by norm_num

theorem q33_margin : 0 < (42831862673 : ℚ)/172470272 := by norm_num

theorem q39_margin : 0 < (9760481 : ℚ)/130321 := by norm_num

#print axioms odd0_gap_num
#print axioms odd0_non35_error_num
#print axioms odd0_mult35_error_num
#print axioms q35_margin
#print axioms q33_margin
#print axioms q39_margin

#print axioms odd_three_base
#print axioms odd_three_extra
#print axioms even_err0
#print axioms even_err1
#print axioms even0_base
#print axioms even1_base

end PathUAM.Positivity
