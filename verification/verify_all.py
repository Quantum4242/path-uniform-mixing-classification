# Exact Fourier coefficient bounds for the possible short relations when odd primes are >=5.
import sympy as s
from math import factorial,comb
from itertools import product
from collections import Counter
from functools import lru_cache
n,x=s.symbols('n x', integer=True, positive=True); K,L=8,2
@lru_cache(None)
def mk(k,a):
 return s.Rational(comb(k,(k-a)//2),2**k) if k>=a and (k-a)%2==0 else s.S(0)
def ct(k,l,a):return sum(comb(l,j)*2**j*(-1)**(l-j)*mk(k+2*j,a) for j in range(l+1))
@lru_cache(None)
def block(a):return {(k,l):ct(k,l,a)/(factorial(k)*factorial(l)) for k,l in product(range(K+1),range(L+1)) if ct(k,l,a)}
base=block(0)
def mul(a,b):
 c={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():
   if i+k<=K and j+l<=L:c[i+k,j+l]=c.get((i+k,j+l),s.S(0))+u*v
 return {ij:s.expand(v) for ij,v in c.items() if v!=0}
@lru_cache(None)
def power(m):
 res={};t={(0,0):s.S(1)};u={ij:v for ij,v in base.items() if ij!=(0,0)}; b=n-m
 for j in range((K+2*L)//2+1):
  pol=s.sympify(s.prod(b-i for i in range(j)))/factorial(j)
  for ij,v in t.items():res[ij]=res.get(ij,s.S(0))+pol*v
  t=mul(t,u)
 return {ij:s.expand(v) for ij,v in res.items()}
p=[10000,-3707,254]; B=-1336
f=[sum(p[i]*p[j-i] for i in range(max(0,j-2),min(2,j)+1)) for j in range(5)]
@lru_cache(None)
def coeff(pattern,bias):
 if sum(pattern)>8:return s.S(0)
 poly=power(len(pattern))
 for a in pattern:poly=mul(poly,block(a))
 c=s.Rational(bias,2);shift={(j,0):c**j/factorial(j) for j in range(K+1) if j==0 or c};P=mul(poly,shift)
 return s.factor(sum(f[j]*2**j*factorial(2*j)*P.get((2*j,0),0)/n**j for j in range(5))+2*B/n*sum(p[j]*2**j*factorial(2*j)*P.get((2*j,1),0)/n**j for j in range(3))+s.Integer(B**2)*2*P.get((0,2),0)/n**2)
def counts(pat):
 l=len(pat); c=list(pat)+[0]*2
 out=Counter({tuple(sorted(pat)):1})
 def insert(v,mult):
  u=c.copy()
  for i,k in v:u[i]-=k
  pat=tuple(sorted(abs(k) for k in u if k));out[pat]+=mult
 for i in range(l+1):
  for k in (-2,-1,1,2):insert([(i,k)],1 if i<l else n-l)
 for i in range(l+1):
  for j in range(i+1,l+2):
   if j==l+1 and i!=l:continue
   mult=1 if j<l else (n-l if i<l else (n-l)*(n-l-1)/2)
   for a,b in product((-1,1),repeat=2):insert([(i,a),(j,b)],mult)
 return out
# All short relation upper bounds; the arithmetic classification is in the note.
def nonnegative(expr,threshold):
 num,den=s.fraction(s.factor(expr));pn=s.Poly(num.subs(n,x+threshold),x);pd=s.Poly(den.subs(n,x+threshold),x)
 return all(v>=0 for v in pn.all_coeffs()) and all(v>=0 for v in pd.all_coeffs()) and pd.eval(0)>0 and pn.eval(0)>0
for bias in (0,1):
 errors={}
 for pat in [(1,)*i for i in (5,7,8,9,10)]+[(2,)*5,(1,)*8+(2,)]:
  total=0
  for u,mult in counts(pat).items():
   a=coeff(u,bias)
   if not a:continue
   num,den=s.fraction(a); assert len(s.Poly(den,n).terms())==1
   upper=sum(abs(v)*n**k[0] for k,v in s.Poly(num,n).terms())/den
   total+=mult*upper
  errors[pat]=s.factor(total)
  print('bias',bias,'pattern',pat,'one relation error bound',errors[pat],flush=True)
 E=lambda j:errors[(1,)*j]
 pure5=s.factor(2*n/5*(E(5)+errors[(2,)*5])+2*(n/5)*(n/5-1)*E(10))
 pure7=2*n/7*E(7)
 mixed35=2*errors[(2,)*5]+18*E(8)+2*E(5)+30*errors[(1,)*8+(2,)]+12*E(9)+4*E(10)+(2*n+4*n/5)*E(10)
 mixedother=2*E(7)+12*E(10)+4*E(8)+2*E(9)
 bound=s.factor(pure5+pure7+mixed35+mixedother)
 print('bias',bias,'ALL total bound',bound,flush=True)
 assert nonnegative(s.Integer(14500000)-bound,35)
 assert not bound.atoms(s.Float)
 print('All-n >= 35 positivity: PASS',flush=True)
 for t in (17,20,25,27,30,34,35,40,50,60,69,70,100,200):
  print('n',t,'bound',bound.subs(n,t),'below 14500000?',nonnegative(s.Integer(14500000)-bound,t),flush=True)
 no7=s.factor(pure5+2*E(7)+12*E(10)+2*E(8))
 print('no7 bound',no7,'n>=27',nonnegative(s.Integer(14500000)-no7,27),flush=True)
