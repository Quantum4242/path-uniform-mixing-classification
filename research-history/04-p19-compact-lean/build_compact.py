from pathlib import Path
import sys,json, shutil
from fractions import Fraction as F
ROOT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'source'))
import verify_certificate as v
c=json.loads((ROOT/'source/certificate.json').read_text()); n=91; Q=10**8; S=v.S
pairs=v.gap_pairs(); ts=c['times']; th={r:v.scale(v.cos_interval(v.div(v.scale(v.PI,r),20)),2) for r in range(1,20)}
B=[[v.rat(1)]*n]+[[v.cos_interval(v.scale(v.sub(th[r],th[s]),t)) for t in ts] for r,s,_ in pairs]
# choose nearest rational centre, then check enclosure with exact integers.
def nearest(x): return round(x)
A=[[nearest(F((lo+hi)*Q,2*S)) for lo,hi in row] for row in B]
for i,row in enumerate(B):
 for j,(lo,hi) in enumerate(row):
  assert (A[i][j]-1)*S<=lo*Q<=hi*Q<=(A[i][j]+1)*S
R=[[nearest(F(x*Q,c['denominator'])) for x in row] for row in c['inverse_numerators']]
w=[nearest(F(x*Q,c['denominator'])) for x in c['weight_numerators']]
b=[19]+[t for _,_,t in pairs]
C=list(zip(*A)); defect=[sum(abs((Q*Q if i==j else 0)-sum(a*x for a,x in zip(row,col))) for j,col in enumerate(C)) for i,row in enumerate(R)]
# residual with denominator 19*Q^2
res=[bi*Q*Q-19*sum(a*x for a,x in zip(row,w)) for bi,row in zip(b,A)]
rnorm=max(sum(map(abs,row)) for row in R); wnorm=sum(map(abs,w)); d=max(defect); e=max(map(abs,res))
# use loose, simple bounds
assert rnorm<=27*Q and wnorm<=2*Q and min(w)>=60000
assert d*10000<=Q*Q # defect <= 1e-4
assert e*10**6<=19*Q*Q # residual <= 1e-6
# ||I-RB|| <= 1e-4+27*91/Q < 1/1000
# ||R(b-Bw0)|| <= 27*(1e-6+2/Q) < 1/30000
# exact weight error < (1/30000)/(1-1/1000) < 1/20000
assert F(1,10000)+F(27*91,Q)<F(1,1000)
assert 27*(F(1,10**6)+F(2,Q))<F(1,30000)
assert F(1,30000)/(1-F(1,1000))<F(1,20000)
print('All 8281 entry enclosures verified; |B-A/Q| <= 1/Q')
for name,x in [('R norm',F(rnorm,Q)),('w L1',F(wnorm,Q)),('min w0',F(min(w),Q)),('A defect',F(d,Q*Q)),('A residual',F(e,19*Q*Q))]: print(name,x,float(x))
print('Certified true B defect < 1/1000; true weight error < 1/20000; exact weights > 11/20000.')
(ROOT/'compact.json').write_text(json.dumps(dict(Q=Q,times=ts,A=A,R=R,w=w,b=b,pairs=pairs),separators=(',',':'))+'\n')
