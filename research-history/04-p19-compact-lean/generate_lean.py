"""Export the fixed compact certificate as Lean source (no floating point)."""
import json
from pathlib import Path
root=Path(__file__).parent
c=json.loads((root/'compact.json').read_text()); n=91
out=root/'P19'; out.mkdir(exist_ok=True)
def lst(xs): return '['+', '.join(str(x) if x>=0 else f'({x})' for x in xs)+']'
def mat(xs): return '[\n'+',\n'.join('  '+lst(row) for row in xs)+'\n]'
lines=['import Lean','set_option maxRecDepth 100000','set_option maxHeartbeats 0','namespace P19','def Q : Int := 100000000','def n : Nat := 91', 'def times : List Nat := '+lst(c['times']), 'def A : List (List Int) := '+mat(c['A']), 'def R : List (List Int) := '+mat(c['R']), 'def w : List Int := '+lst(c['w']), 'def b : List Int := '+lst(c['b']), 'end P19']
(out/'Data.lean').write_text('\n\n'.join(lines)+'\n')
s='''import P19.Data

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

'''
# individually proven closed terms; conjunction is not a second expensive computation
for i in range(n): s+=f'theorem row{i:02d} : rowCheck {i} = true := by decide\n'
s+='\n/-- Conjunction of every row check, with the global shape check. -/\ndef AllChecks : Prop :=\n  globalCheck = true ∧\n  '+' ∧\n  '.join(f'rowCheck {i} = true' for i in range(n))+'\n\ntheorem allChecks : AllChecks :=\n  ⟨globalOK, '+', '.join(f'row{i:02d}' for i in range(n))+'⟩\n\n#print axioms allChecks\nend P19\n'
(out/'Certificate.lean').write_text(s)
