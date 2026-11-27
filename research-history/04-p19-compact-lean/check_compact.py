"""Independent fixed-certificate checker. Does not generate or round any entries."""
import sys,json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).parent
sys.path.insert(0,str(root/'source'))
import verify_certificate as v
c=json.loads((root/'compact.json').read_text()); Q=c['Q']; n=91
A,R,w,b,ts,pairs=[c[k] for k in ('A','R','w','b','times','pairs')]
assert Q==10**8 and len(ts)==len(set(ts))==n and all(type(t)==int and 0<=t<2000 for t in ts)
assert all(len(x)==n for x in (A,R,w,b)) and all(len(row)==n for row in A+R)
assert all(type(x)==int for row in A+R for x in row) and all(type(x)==int for x in w+b)
assert pairs==[list(p) for p in v.gap_pairs()] and b==[19]+[p[2] for p in pairs]
assert A[0]==[Q]*n
th=[v.scale(v.cos_interval(v.div(v.scale(v.PI,r),20)),2) for r in range(1,20)]
for i,(r,s,_) in enumerate(pairs,1):
 for j,t in enumerate(ts):
  lo,hi=v.cos_interval(v.scale(v.sub(th[r-1],th[s-1]),t))
  assert (A[i][j]-1)*v.S<=lo*Q<=hi*Q<=(A[i][j]+1)*v.S
print('PASS: 8281 entry enclosures; 171 gap targets in 90 groups.')
for i in range(n):
 assert sum(abs(x) for x in R[i])<=27*Q
 d=sum(abs((Q*Q if j==i else 0)-sum(R[i][k]*A[k][j] for k in range(n))) for j in range(n))
 assert 10000*d<=Q*Q
 r=abs(b[i]*Q*Q-19*sum(A[i][k]*w[k] for k in range(n)))
 assert 10**6*r<=19*Q*Q and w[i]>=60000
assert sum(map(abs,w))<=2*Q
assert F(1,10000)+F(27*91,Q)<F(1,1000)
assert 27*(F(1,10**6)+F(2,Q))<F(1,30000)
assert F(1,30000)/(1-F(1,1000))<F(1,20000)
print('PASS: 91 integer row certificates; global norm and exact rational bounds.')
v.verify_mixing_identity()
print('PASS: all conditions of the mathematical compact-certificate proof.')
