#!/usr/bin/env python3
"""Exact arithmetic audit of the coprime-to-six path theorem.
The general classification uses the mathematical proof in research-note.md.
No floating point, LP, or numerical diagonalization is needed for these checks.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import factorial, prod
import sympy as sp

def ball(dim, radius):
    if dim == 0:
        yield ()
        return
    for a in range(-radius, radius+1):
        for rest in ball(dim-1, radius-abs(a)):
            yield (a,)+rest

def central(a,b):
    return a+b+tuple(i+j for i in a for j in b for _ in range(2))

# A completely exhaustive integer enumeration. The axis coordinates are part
# of the array, so the parameter l1 norm cannot exceed the spectral l1 norm.
relations=[]; counts=Counter(); nparams=0
for p in ball(5,10):
    nparams+=1
    a,b=p[:2],p[2:]; u=central(a,b)
    ell=sum(map(abs,u)); charge=sum(u)
    if 0<ell<=10:
        assert ell>=5
        counts[(ell,charge)]+=1
        if ell%2==0 and charge in (-2,0,2):
            relations.append((a,b,u))
assert {k:v for k,v in counts.items() if k[0]==5}=={(5,-5):3,(5,-1):1,(5,1):1,(5,5):3}
assert Counter((sum(map(abs,u)),sum(u),tuple(sorted(x for x in u if x))) for a,b,u in relations)==Counter({
    (8,2,(-1,)*3+(1,)*5):6,
    (8,-2,(-1,)*5+(1,)*3):6,
    (10,0,(-1,)*5+(1,)*5):6,
    (10,2,(-2,)*2+(2,)*3):1,
    (10,-2,(-2,)*3+(2,)*2):1})
print('central 35 parameter vectors checked:',nparams)
print('central 35 nonzero arrays of length <=10:',sum(counts.values()))
print('central 35 relevant arrays:',len(relations),'PASS')

# Central symmetric array support bound for all other possible mixed pairs.
expected={(5,11):[(4,8,20),(4,10,14)],(5,13):[(4,12,16)],
          (5,17):[(4,16,20)],(7,11):[(6,10,16)],(7,13):[(6,12,18)]}
for (p,r),target in expected.items():
    result=[(u,v,u*(r-v)+(p-u)*v) for u in range(2,p,2)
            for v in range(2,r,2) if u*(r-v)+(p-u)*v<=20]
    assert result==target
    print('mixed central support',p*r,result,'PASS')

# The triple conductor 385 would force a central 35 slice representing 1
# with ten nonzero +/-1 entries and no origin. Subtracting the origin gives
# an additive array whose five axis parameters have only 3 choices each.
ns=0; hist=Counter()
for a in product(range(3),repeat=2):
    for b in product(range(-1,2),repeat=3):
        ns+=1
        u=tuple(x-1 for x in a)+b+tuple(x+y for x in a for y in b for _ in range(2))
        if all(abs(x)<=1 for x in u): hist[sum(map(abs,u))]+=1
assert hist[5]==0
print('385 central slice:',ns,'integer arrays checked; no feasible norm 5: PASS')

# Check actual relation vectors by direct cyclotomic polynomial reduction.
x=sp.Symbol('x')
def check_array(q,p,r,a,b,offset=0):
    m=(q-1)//2; u=[0]*m; seen={}
    for i in range(p):
        for j in range(r):
            e=(offset+i*(q//p)+j*(q//r))%q
            v=a[i]+b[j]
            if e==0:
                assert v==0; continue
            k=min(e,q-e)
            if k in seen: assert seen[k]==v
            seen[k]=v;u[k-1]=v
    poly=sum(v*(x**(i+1)+x**(q-i-1)) for i,v in enumerate(u) if v)
    assert sp.rem(poly,sp.cyclotomic_poly(q,x),x)==0
    return u
for a,b,u in relations:
    aa=(0,)+a+a[::-1];bb=(0,)+b+b[::-1]
    assert sorted(check_array(35,5,7,aa,bb))==sorted(u)
for p,r in [(5,11),(5,13),(5,17),(7,11),(7,13)]:
    check_array(p*r,p,r,(0,)+(-1,)*(p-1),(0,)+(1,)*(r-1))
for j in range(1,6):
    # 55-axis variant with one omitted nonzero column pair.
    b=tuple(0 if k in (0,j,11-j) else -1 for k in range(11))
    u=check_array(55,5,11,(0,)+(1,)*4,b)
    assert (sum(map(abs,u)),sum(u))==(10,2)
u=check_array(175,5,7,(1,0,0,0,0),(-1,0,0,0,0,0,0),offset=1)
assert (sum(map(abs,u)),sum(u))==(10,2)
print('direct cyclotomic checks: 31 relations PASS')

# Independent derivation of F moments from multinomial occupancy partitions.
m=sp.Symbol('m',positive=True,integer=True)
def partitions(n,lo=1):
    if n==0:
        yield ()
    else:
        for k in range(lo,n+1):
            for rest in partitions(n-k,k): yield (k,)+rest
def moment(k):
    return sp.factor(sum(prod(m-j for j in range(len(p)))*sp.Rational(factorial(k)**2,
        prod(factorial(p.count(i)) for i in set(p))*prod(factorial(i)**2 for i in p))
        for p in partitions(k))/m**k)
co=[10000,-12000,5000,-840,49]
mu=[moment(k) for k in range(6)]
Z=sp.factor(sum(c*mu[k] for k,c in enumerate(co)))
Y=sp.factor(sum(c*mu[k+1] for k,c in enumerate(co)))
T=232*m**3+2568*m**2-5782*m+15435
assert sp.simplify((m+1)*Z-2*m*Y-3*(m-1)*T/m**3)==0
assert all(v>0 for v in sp.Poly((T-232*m**3).subs(m,x+3),x).all_coeffs())
print('moment formula, density slack >=696: PASS')

# Compute the exceptional small modulus q=35 exactly. Fhat is symmetric in
# coordinate permutations, so using any fixed order of inversion pairs works.
# Check two formulas for every nonzero coefficient (full factorial series and
# its simplified h=3 or 4 version).
cache={}
def Fhat(u):
    key=tuple(sorted(u))
    if key in cache: return cache[key]
    n=len(u);h=sum(max(v,0) for v in u)
    if sum(u) or h>4: return Q(0)
    dp=[Q(1)]+[Q(0)]*(4-h)
    for v in u:
        a,b=max(v,0),max(-v,0)
        fac=[Q(1,factorial(a+l)*factorial(b+l)) for l in range(5-h)]
        dp=[sum(dp[j]*fac[k-j] for j in range(k+1)) for k in range(5-h)]
    out=sum(Q(co[j]*factorial(j)**2,n**j)*dp[j-h] for j in range(h,5))
    denom=prod(factorial(abs(v)) for v in u)
    if h==4:
        assert out==Q(28224,n**4*denom)
    elif h==3:
        assert out==(Q(-30240,n**3)+Q(28224,n**4)*sum(Q(1,abs(v)+1) for v in u))/denom
    cache[key]=out
    return out
cs=[u for a,b,u in relations];n=17
E0=sum(Fhat(u) for u in cs)
errors=[]
for i in range(n):
    for j in range(i,n):
        for s in (1,-1) if i!=j else (1,):
            v=[]
            for c in cs:
                a=list(c);a[i]-=1;a[j]-=s;v.append(Fhat(a))
            errors.append(sum(v))
assert len(errors)==n*n
E=abs(E0)+2*sum(map(abs,errors));G=Q(3*T.subs(m,n),n**3)
assert E0==0 and E==Q(31239432,83521) and G==Q(5397327,4913)
assert E<G and E<Q(849,2)
print('q=35: all',len(errors),'moments, E=',E,'G=',G,'PASS')

# Uniform estimates, monotone in m; the following are exact rational checks.
def pure(n): return Q(56448,n**2)
def mixed_no35(n): return pure(n)+Q(1451520,n**3)+Q(4233600,n**4)
def mixed_all(n): return pure(n)+Q(11007360,n**3)+Q(4572288,n**4)
for label,val in [('pure q>=25',pure(12)),('q>=55 and 35 not dividing q',mixed_no35(27)),
                  ('35 divides q, q>=175',mixed_all(87)),('q=35 exact',E)]:
    assert val<Q(849,2)<696
    print(label,': E <=',val,'PASS')
# The uniform positive floor and finite-grid bound carry over unchanged.
assert Q(696*2,3*8420)*(1-Q(849,2*696))>Q(1,50)
assert Q(4*4*12,20000)<Q(1,100)
print('strict density floor and grid constants: PASS')
print('ALL EXACT CHECKS PASSED')
