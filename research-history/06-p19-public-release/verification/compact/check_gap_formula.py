if not __debug__:
    raise RuntimeError("Run without -O: assertions are required for verification")

"""Check the Lean gap algorithm separately from the original polynomial division."""
from pathlib import Path
import json,sys,itertools
root=Path(__file__).parent
sys.path.insert(0,str(root.parent/'integer'))
import verify_certificate as v
c=json.loads((root/'compact.json').read_text())
def pow_coeff(e,j):
 u=e%40; k=u%20; sg=1 if u<20 else -1
 if k<16:return sg*int(j==k)
 return sg*(int(j==k-4)-int(j==k-8)+int(j==k-12)-int(j==k-16))
def theta(r):return tuple(pow_coeff(r,j)+pow_coeff(40-r%40,j) for j in range(16))
def gap(r,s):return tuple(a-b for a,b in zip(theta(r),theta(s)))
for r in range(40):assert theta(r)==v.theta_vectors()[r]
reps={(gap(r,s),t) for r,s,t in c['pairs']}
assert len(reps)==90
for r,s in itertools.combinations(range(1,20),2):assert (gap(r,s),-1 if (r+s)%2==0 else 0) in reps
print('PASS: simplified power coefficients match all 40 original residue vectors; all 171 gaps covered.')
