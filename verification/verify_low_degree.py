import sympy as s
from math import factorial, comb
from itertools import product
n,x=s.symbols('n x', integer=True, positive=True)
K,L=8,2
mom=lambda k: s.Rational(comb(k,k//2),2**k) if k%2==0 else s.S(0)
# E[C^k (2C^2-1)^l]. All coefficients exact rational.
def ct(k,l):return sum(comb(l,j)*2**j*(-1)**(l-j)*mom(k+2*j) for j in range(l+1))
def block(a,b):return {(k,l):ct(k+a,l+b)/(factorial(k)*factorial(l)) for k,l in product(range(K+1),range(L+1)) if ct(k+a,l+b)}
base=block(0,0);mark1=block(1,0);mark2=block(0,1)
def mul(a,b):
 c={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():
   if i+k<=K and j+l<=L:c[i+k,j+l]=c.get((i+k,j+l),s.S(0))+u*v
 return {ij:s.expand(v) for ij,v in c.items() if v!=0}
def power(b):
 res={};t={(0,0):s.S(1)};u={ij:v for ij,v in base.items() if ij!=(0,0)}
 for j in range((K+2*L)//2+1):
  pol=s.sympify(s.prod(b-i for i in range(j)))/factorial(j)
  for ij,v in t.items():res[ij]=res.get(ij,s.S(0))+pol*v
  t=mul(t,u)
 return {ij:s.expand(v) for ij,v in res.items()}
p=[10000,-3707,254]; B=-1336
f=[sum(p[i]*p[j-i] for i in range(max(0,j-2),min(2,j)+1)) for j in range(5)]
print('P coefficients',p,'T coefficient',B,flush=True)
P=[power(n-j) for j in range(3)]
for bias in (0,1):
 c=s.Rational(bias,2);shift={(j,0):c**j/factorial(j) for j in range(K+1) if j==0 or c}
 def integral(poly):
  coeff=mul(poly,shift)
  return s.factor(sum(f[j]*2**j*factorial(2*j)*coeff.get((2*j,0),0)/n**j for j in range(5))+2*B/n*sum(p[j]*2**j*factorial(2*j)*coeff.get((2*j,1),0)/n**j for j in range(3))+s.Integer(B**2)*2*coeff.get((0,2),0)/n**2)
 Z=integral(P[0]); U=integral(mul(mul(P[2],mark1),mark1)); D=integral(mul(P[1],mark2)); W=integral(mul(P[1],mark1))
 N=4*n+1 if bias else 4*n-1
 G=-N*U-Z
 polys=[s.factor(G-2*n*(sg*(U-D)+sh*(bias*U-W))) for sg in (-1,1) for sh in (-1,1)]
 for threshold in (2,3,4,5,6,7,8,9,10,12,15,20,25,50,100):
  ok=True
  for a in [Z,-U]+polys:
   num,den=s.fraction(a)
   pn=s.Poly(num.subs(n,x+threshold),x);pd=s.Poly(den.subs(n,x+threshold),x)
   if not (all(v>=0 for v in pn.all_coeffs()) and pn.eval(0)>0 and all(v>=0 for v in pd.all_coeffs()) and pd.eval(0)>0):ok=False;break
  if ok:break
 print('bias',bias,'threshold',threshold,'success',ok,flush=True)
 assert ok
 print('Z',Z,'U',U,'D',D,'W',W,sep='\n',flush=True)
 for a in polys:
  num,den=s.fraction(s.factor(a-14500000));pn=s.Poly(num.subs(n,x+2),x);pd=s.Poly(den.subs(n,x+2),x)
  assert all(v>=0 for v in pn.all_coeffs()) and pn.eval(0)>0 and all(v>=0 for v in pd.all_coeffs()) and pd.eval(0)>0
 assert not any(a.atoms(s.Float) for a in [Z,U,D,W]+polys)
 print('all margins > 14500000 for n>=2: PASS')
 print('asymptotic margins', [s.limit(a,n,s.oo) for a in polys],flush=True)
 for a in [Z,-U]+polys:
   num,den=s.fraction(a);print('shifted numerator',s.Poly(num.subs(n,x+threshold),x).as_expr(), 'denominator',den)
