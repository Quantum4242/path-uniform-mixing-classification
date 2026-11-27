import Mathlib

/- Draft: finite arithmetic portion only. It has NOT been compiled in this
   environment and is not a formalization of the full P19 theorem. -/
namespace P19PhaseCertificate

def c (a : ℕ) : ℚ := if a = 0 then 1 else if a = 2 then -1 else 0
def s (a : ℕ) : ℚ := if a = 1 then 1 else if a = 3 then -1 else 0

def patternMoment (p : List ℕ) (k : ℕ) : ℚ :=
  let n : ℚ := p.length
  let C := (p.map c).sum
  let S := (p.map s).sum
  let C2 := (p.map (fun a => (c a)^2)).sum
  let S2 := (p.map (fun a => (s a)^2)).sum
  if k = 0 then C / n
  else if k = 1 then (C2-S2) / n
  else if k = 2 then (C^2-C2) / (n*(n-1))
  else (S^2-S2) / (n*(n-1))

def oddLaw : List (List ℕ × ℚ) :=
  [([0,0,0,0,0], 1/96), ([0,0,0,2,2], 25/96),
   ([0,0,2,3,3], 5/36), ([0,1,1,3,3], 5/72),
   ([1,2,3,3,3], 25/48)]

def evenLaw : List (List ℕ × ℚ) :=
  [([0,0,1,3], 1/6), ([0,2,2,3], 1/2),
   ([2,3,3,3], 1/18), ([1,3,3,3], 5/18)]

def weightedMoment (law : List (List ℕ × ℚ)) (k : ℕ) : ℚ :=
  (law.map (fun x => x.2 * patternMoment x.1 k)).sum

set_option maxRecDepth 10000 in
set_option maxHeartbeats 1000000 in
theorem oddMoments :
    weightedMoment oddLaw 0 = 0 ∧
    weightedMoment oddLaw 1 = -1/18 ∧
    weightedMoment oddLaw 2 = -1/18 ∧
    weightedMoment oddLaw 3 = 0 := by
  decide

set_option maxRecDepth 10000 in
set_option maxHeartbeats 1000000 in
theorem evenMoments :
    weightedMoment evenLaw 0 = -1/18 ∧
    weightedMoment evenLaw 1 = -1/18 ∧
    weightedMoment evenLaw 2 = -1/18 ∧
    weightedMoment evenLaw 3 = 0 := by
  decide

theorem weightSums : (oddLaw.map Prod.snd).sum = 1 ∧
    (evenLaw.map Prod.snd).sum = 1 := by decide

theorem oddConstraint :
    oddLaw.all (fun x => x.1.sum % 4 == 0) = true := by decide

#print axioms oddMoments
#print axioms evenMoments
#print axioms weightSums
#print axioms oddConstraint
end P19PhaseCertificate
