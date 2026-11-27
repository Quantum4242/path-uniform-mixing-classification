import json
from pathlib import Path
root=Path(__file__).parent
c=json.loads((root/'compact.json').read_text())
s='''import P19.Data

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
'''+',\n'.join(f'  ({r}, {t}, ({b}))' for r,t,b in c['pairs'])+'''
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
'''
for i in range(1,20): s+=f'theorem gapRow{i:02d} : coverRow {i} = true := by decide\n'
s+='\ndef AllGapChecks : Prop :=\n  repCheck = true ∧\n  '+' ∧\n  '.join(f'coverRow {i} = true' for i in range(1,20))+'\n\ntheorem allGapChecks : AllGapChecks :=\n  ⟨representativesOK, '+', '.join(f'gapRow{i:02d}' for i in range(1,20))+'⟩\n\n#print axioms allGapChecks\nend P19\n'
(root/'P19/Gap.lean').write_text(s)
