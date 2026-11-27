import P19.Data

/- Finite integer certificate ONLY. The link to real cosine values and the
   spectral theorem are separate mathematical obligations. -/
namespace P19
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def dot (xs ys : List Int) : Int :=
  (List.zipWith (fun x y => x*y) xs ys).foldl (· + ·) 0

def l1 (xs : List Int) : Nat :=
  (xs.map Int.natAbs).foldl (· + ·) 0

def cols : List (List Int) :=
  (List.range n).map (fun j => A.map (fun row => row[j]!))

def defect (i : Nat) : Nat :=
  ((List.range n).map (fun j =>
    Int.natAbs ((if i == j then Q*Q else 0) - dot R[i]! cols[j]!))).foldl (· + ·) 0

def residual (i : Nat) : Nat :=
  Int.natAbs (b[i]! * Q * Q - 19 * dot A[i]! w)

def rowCheck (i : Nat) : Bool :=
  decide (l1 R[i]! ≤ 27 * Q.natAbs) &&
  decide (10000 * defect i ≤ (Q*Q).natAbs) &&
  decide (1000000 * residual i ≤ (19*Q*Q).natAbs) &&
  decide (60000 ≤ w[i]!)

def globalCheck : Bool :=
  decide (A.length = n) && decide (R.length = n) &&
  A.all (fun row => decide (row.length = n)) &&
  R.all (fun row => decide (row.length = n)) &&
  decide (w.length = n) && decide (b.length = n) &&
  decide (times.length = n) &&
  (times.all (fun t => decide (t < 2000))) &&
  decide (times.eraseDups.length = n) &&
  decide (A[0]! = List.replicate n Q) &&
  decide (b[0]! = 19) &&
  decide (l1 w ≤ 2 * Q.natAbs)

theorem globalOK : globalCheck = true := by decide

theorem row00 : rowCheck 0 = true := by decide
theorem row01 : rowCheck 1 = true := by decide
theorem row02 : rowCheck 2 = true := by decide
theorem row03 : rowCheck 3 = true := by decide
theorem row04 : rowCheck 4 = true := by decide
theorem row05 : rowCheck 5 = true := by decide
theorem row06 : rowCheck 6 = true := by decide
theorem row07 : rowCheck 7 = true := by decide
theorem row08 : rowCheck 8 = true := by decide
theorem row09 : rowCheck 9 = true := by decide
theorem row10 : rowCheck 10 = true := by decide
theorem row11 : rowCheck 11 = true := by decide
theorem row12 : rowCheck 12 = true := by decide
theorem row13 : rowCheck 13 = true := by decide
theorem row14 : rowCheck 14 = true := by decide
theorem row15 : rowCheck 15 = true := by decide
theorem row16 : rowCheck 16 = true := by decide
theorem row17 : rowCheck 17 = true := by decide
theorem row18 : rowCheck 18 = true := by decide
theorem row19 : rowCheck 19 = true := by decide
theorem row20 : rowCheck 20 = true := by decide
theorem row21 : rowCheck 21 = true := by decide
theorem row22 : rowCheck 22 = true := by decide
theorem row23 : rowCheck 23 = true := by decide
theorem row24 : rowCheck 24 = true := by decide
theorem row25 : rowCheck 25 = true := by decide
theorem row26 : rowCheck 26 = true := by decide
theorem row27 : rowCheck 27 = true := by decide
theorem row28 : rowCheck 28 = true := by decide
theorem row29 : rowCheck 29 = true := by decide
theorem row30 : rowCheck 30 = true := by decide
theorem row31 : rowCheck 31 = true := by decide
theorem row32 : rowCheck 32 = true := by decide
theorem row33 : rowCheck 33 = true := by decide
theorem row34 : rowCheck 34 = true := by decide
theorem row35 : rowCheck 35 = true := by decide
theorem row36 : rowCheck 36 = true := by decide
theorem row37 : rowCheck 37 = true := by decide
theorem row38 : rowCheck 38 = true := by decide
theorem row39 : rowCheck 39 = true := by decide
theorem row40 : rowCheck 40 = true := by decide
theorem row41 : rowCheck 41 = true := by decide
theorem row42 : rowCheck 42 = true := by decide
theorem row43 : rowCheck 43 = true := by decide
theorem row44 : rowCheck 44 = true := by decide
theorem row45 : rowCheck 45 = true := by decide
theorem row46 : rowCheck 46 = true := by decide
theorem row47 : rowCheck 47 = true := by decide
theorem row48 : rowCheck 48 = true := by decide
theorem row49 : rowCheck 49 = true := by decide
theorem row50 : rowCheck 50 = true := by decide
theorem row51 : rowCheck 51 = true := by decide
theorem row52 : rowCheck 52 = true := by decide
theorem row53 : rowCheck 53 = true := by decide
theorem row54 : rowCheck 54 = true := by decide
theorem row55 : rowCheck 55 = true := by decide
theorem row56 : rowCheck 56 = true := by decide
theorem row57 : rowCheck 57 = true := by decide
theorem row58 : rowCheck 58 = true := by decide
theorem row59 : rowCheck 59 = true := by decide
theorem row60 : rowCheck 60 = true := by decide
theorem row61 : rowCheck 61 = true := by decide
theorem row62 : rowCheck 62 = true := by decide
theorem row63 : rowCheck 63 = true := by decide
theorem row64 : rowCheck 64 = true := by decide
theorem row65 : rowCheck 65 = true := by decide
theorem row66 : rowCheck 66 = true := by decide
theorem row67 : rowCheck 67 = true := by decide
theorem row68 : rowCheck 68 = true := by decide
theorem row69 : rowCheck 69 = true := by decide
theorem row70 : rowCheck 70 = true := by decide
theorem row71 : rowCheck 71 = true := by decide
theorem row72 : rowCheck 72 = true := by decide
theorem row73 : rowCheck 73 = true := by decide
theorem row74 : rowCheck 74 = true := by decide
theorem row75 : rowCheck 75 = true := by decide
theorem row76 : rowCheck 76 = true := by decide
theorem row77 : rowCheck 77 = true := by decide
theorem row78 : rowCheck 78 = true := by decide
theorem row79 : rowCheck 79 = true := by decide
theorem row80 : rowCheck 80 = true := by decide
theorem row81 : rowCheck 81 = true := by decide
theorem row82 : rowCheck 82 = true := by decide
theorem row83 : rowCheck 83 = true := by decide
theorem row84 : rowCheck 84 = true := by decide
theorem row85 : rowCheck 85 = true := by decide
theorem row86 : rowCheck 86 = true := by decide
theorem row87 : rowCheck 87 = true := by decide
theorem row88 : rowCheck 88 = true := by decide
theorem row89 : rowCheck 89 = true := by decide
theorem row90 : rowCheck 90 = true := by decide

/-- Conjunction of every row check, with the global shape check. -/
def AllChecks : Prop :=
  globalCheck = true ∧
  rowCheck 0 = true ∧
  rowCheck 1 = true ∧
  rowCheck 2 = true ∧
  rowCheck 3 = true ∧
  rowCheck 4 = true ∧
  rowCheck 5 = true ∧
  rowCheck 6 = true ∧
  rowCheck 7 = true ∧
  rowCheck 8 = true ∧
  rowCheck 9 = true ∧
  rowCheck 10 = true ∧
  rowCheck 11 = true ∧
  rowCheck 12 = true ∧
  rowCheck 13 = true ∧
  rowCheck 14 = true ∧
  rowCheck 15 = true ∧
  rowCheck 16 = true ∧
  rowCheck 17 = true ∧
  rowCheck 18 = true ∧
  rowCheck 19 = true ∧
  rowCheck 20 = true ∧
  rowCheck 21 = true ∧
  rowCheck 22 = true ∧
  rowCheck 23 = true ∧
  rowCheck 24 = true ∧
  rowCheck 25 = true ∧
  rowCheck 26 = true ∧
  rowCheck 27 = true ∧
  rowCheck 28 = true ∧
  rowCheck 29 = true ∧
  rowCheck 30 = true ∧
  rowCheck 31 = true ∧
  rowCheck 32 = true ∧
  rowCheck 33 = true ∧
  rowCheck 34 = true ∧
  rowCheck 35 = true ∧
  rowCheck 36 = true ∧
  rowCheck 37 = true ∧
  rowCheck 38 = true ∧
  rowCheck 39 = true ∧
  rowCheck 40 = true ∧
  rowCheck 41 = true ∧
  rowCheck 42 = true ∧
  rowCheck 43 = true ∧
  rowCheck 44 = true ∧
  rowCheck 45 = true ∧
  rowCheck 46 = true ∧
  rowCheck 47 = true ∧
  rowCheck 48 = true ∧
  rowCheck 49 = true ∧
  rowCheck 50 = true ∧
  rowCheck 51 = true ∧
  rowCheck 52 = true ∧
  rowCheck 53 = true ∧
  rowCheck 54 = true ∧
  rowCheck 55 = true ∧
  rowCheck 56 = true ∧
  rowCheck 57 = true ∧
  rowCheck 58 = true ∧
  rowCheck 59 = true ∧
  rowCheck 60 = true ∧
  rowCheck 61 = true ∧
  rowCheck 62 = true ∧
  rowCheck 63 = true ∧
  rowCheck 64 = true ∧
  rowCheck 65 = true ∧
  rowCheck 66 = true ∧
  rowCheck 67 = true ∧
  rowCheck 68 = true ∧
  rowCheck 69 = true ∧
  rowCheck 70 = true ∧
  rowCheck 71 = true ∧
  rowCheck 72 = true ∧
  rowCheck 73 = true ∧
  rowCheck 74 = true ∧
  rowCheck 75 = true ∧
  rowCheck 76 = true ∧
  rowCheck 77 = true ∧
  rowCheck 78 = true ∧
  rowCheck 79 = true ∧
  rowCheck 80 = true ∧
  rowCheck 81 = true ∧
  rowCheck 82 = true ∧
  rowCheck 83 = true ∧
  rowCheck 84 = true ∧
  rowCheck 85 = true ∧
  rowCheck 86 = true ∧
  rowCheck 87 = true ∧
  rowCheck 88 = true ∧
  rowCheck 89 = true ∧
  rowCheck 90 = true

theorem allChecks : AllChecks :=
  ⟨globalOK, row00, row01, row02, row03, row04, row05, row06, row07, row08, row09, row10, row11, row12, row13, row14, row15, row16, row17, row18, row19, row20, row21, row22, row23, row24, row25, row26, row27, row28, row29, row30, row31, row32, row33, row34, row35, row36, row37, row38, row39, row40, row41, row42, row43, row44, row45, row46, row47, row48, row49, row50, row51, row52, row53, row54, row55, row56, row57, row58, row59, row60, row61, row62, row63, row64, row65, row66, row67, row68, row69, row70, row71, row72, row73, row74, row75, row76, row77, row78, row79, row80, row81, row82, row83, row84, row85, row86, row87, row88, row89, row90⟩

#print axioms allChecks
end P19
