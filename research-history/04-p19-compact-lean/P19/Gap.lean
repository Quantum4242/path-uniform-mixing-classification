import P19.Data

namespace P19
set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-- Coefficients of X^e using X^20=-1 and
    X^16=X^12-X^8+X^4-1.  Interpretation at the actual complex root
    is a separate analytic/algebraic lemma, not claimed here. -/
def powCoeff (e j : Nat) : Int :=
  let u := e % 40
  let k := u % 20
  let sg : Int := if u < 20 then 1 else -1
  if k < 16 then (if j == k then sg else 0)
  else sg * ((if j == k-4 then 1 else 0) - (if j == k-8 then 1 else 0) +
             (if j == k-12 then 1 else 0) - (if j == k-16 then 1 else 0))

def theta (r : Nat) : List Int :=
  (List.range 16).map (fun j => powCoeff r j + powCoeff (40-r%40) j)

def gap (r s : Nat) : List Int := List.zipWith (· - ·) (theta r) (theta s)

def target (r s : Nat) : Int := if (r+s)%2 == 0 then -1 else 0

def reps : List (Nat × Nat × Int) := [
  (1, 2, (0)),
  (1, 3, (-1)),
  (1, 4, (0)),
  (1, 5, (-1)),
  (1, 6, (0)),
  (1, 7, (-1)),
  (1, 8, (0)),
  (1, 9, (-1)),
  (1, 10, (0)),
  (1, 11, (-1)),
  (1, 12, (0)),
  (1, 13, (-1)),
  (1, 14, (0)),
  (1, 15, (-1)),
  (1, 16, (0)),
  (1, 17, (-1)),
  (1, 18, (0)),
  (1, 19, (-1)),
  (2, 3, (0)),
  (2, 4, (-1)),
  (2, 5, (0)),
  (2, 6, (-1)),
  (2, 7, (0)),
  (2, 8, (-1)),
  (2, 9, (0)),
  (2, 10, (-1)),
  (2, 11, (0)),
  (2, 12, (-1)),
  (2, 13, (0)),
  (2, 14, (-1)),
  (2, 15, (0)),
  (2, 16, (-1)),
  (2, 17, (0)),
  (2, 18, (-1)),
  (3, 4, (0)),
  (3, 5, (-1)),
  (3, 6, (0)),
  (3, 7, (-1)),
  (3, 8, (0)),
  (3, 9, (-1)),
  (3, 10, (0)),
  (3, 11, (-1)),
  (3, 12, (0)),
  (3, 13, (-1)),
  (3, 14, (0)),
  (3, 15, (-1)),
  (3, 16, (0)),
  (3, 17, (-1)),
  (4, 5, (0)),
  (4, 6, (-1)),
  (4, 7, (0)),
  (4, 8, (-1)),
  (4, 9, (0)),
  (4, 10, (-1)),
  (4, 11, (0)),
  (4, 12, (-1)),
  (4, 13, (0)),
  (4, 14, (-1)),
  (4, 15, (0)),
  (4, 16, (-1)),
  (5, 6, (0)),
  (5, 7, (-1)),
  (5, 8, (0)),
  (5, 9, (-1)),
  (5, 10, (0)),
  (5, 11, (-1)),
  (5, 12, (0)),
  (5, 13, (-1)),
  (5, 14, (0)),
  (5, 15, (-1)),
  (6, 7, (0)),
  (6, 8, (-1)),
  (6, 9, (0)),
  (6, 10, (-1)),
  (6, 11, (0)),
  (6, 12, (-1)),
  (6, 13, (0)),
  (6, 14, (-1)),
  (7, 8, (0)),
  (7, 9, (-1)),
  (7, 10, (0)),
  (7, 11, (-1)),
  (7, 12, (0)),
  (7, 13, (-1)),
  (8, 9, (0)),
  (8, 10, (-1)),
  (8, 11, (0)),
  (8, 12, (-1)),
  (9, 10, (0)),
  (9, 11, (-1))
]

def repGaps : List (List Int × Int) := reps.map (fun (r,s,t) => (gap r s,t))

def repCheck : Bool :=
  decide (reps.length = 90) &&
  reps.all (fun (r,s,t) => decide (1 ≤ r ∧ r < s ∧ s ≤ 19 ∧ t = target r s)) &&
  decide (b = 19 :: reps.map (fun x => x.2.2)) &&
  decide ((repGaps.map Prod.fst).eraseDups.length = 90)

def covers (r s : Nat) : Bool :=
  repGaps.any (fun x => x == (gap r s, target r s))

def coverRow (r : Nat) : Bool :=
  (List.range 19).all (fun j => if r < j+1 then covers r (j+1) else true)

theorem representativesOK : repCheck = true := by decide
theorem gapRow01 : coverRow 1 = true := by decide
theorem gapRow02 : coverRow 2 = true := by decide
theorem gapRow03 : coverRow 3 = true := by decide
theorem gapRow04 : coverRow 4 = true := by decide
theorem gapRow05 : coverRow 5 = true := by decide
theorem gapRow06 : coverRow 6 = true := by decide
theorem gapRow07 : coverRow 7 = true := by decide
theorem gapRow08 : coverRow 8 = true := by decide
theorem gapRow09 : coverRow 9 = true := by decide
theorem gapRow10 : coverRow 10 = true := by decide
theorem gapRow11 : coverRow 11 = true := by decide
theorem gapRow12 : coverRow 12 = true := by decide
theorem gapRow13 : coverRow 13 = true := by decide
theorem gapRow14 : coverRow 14 = true := by decide
theorem gapRow15 : coverRow 15 = true := by decide
theorem gapRow16 : coverRow 16 = true := by decide
theorem gapRow17 : coverRow 17 = true := by decide
theorem gapRow18 : coverRow 18 = true := by decide
theorem gapRow19 : coverRow 19 = true := by decide

def AllGapChecks : Prop :=
  repCheck = true ∧
  coverRow 1 = true ∧
  coverRow 2 = true ∧
  coverRow 3 = true ∧
  coverRow 4 = true ∧
  coverRow 5 = true ∧
  coverRow 6 = true ∧
  coverRow 7 = true ∧
  coverRow 8 = true ∧
  coverRow 9 = true ∧
  coverRow 10 = true ∧
  coverRow 11 = true ∧
  coverRow 12 = true ∧
  coverRow 13 = true ∧
  coverRow 14 = true ∧
  coverRow 15 = true ∧
  coverRow 16 = true ∧
  coverRow 17 = true ∧
  coverRow 18 = true ∧
  coverRow 19 = true

theorem allGapChecks : AllGapChecks :=
  ⟨representativesOK, gapRow01, gapRow02, gapRow03, gapRow04, gapRow05, gapRow06, gapRow07, gapRow08, gapRow09, gapRow10, gapRow11, gapRow12, gapRow13, gapRow14, gapRow15, gapRow16, gapRow17, gapRow18, gapRow19⟩

#print axioms allGapChecks
end P19
