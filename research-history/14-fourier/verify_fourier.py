#!/usr/bin/env python3
"""Exact, finite checks supporting the Fourier-density proof (not a proof of its number-theory lemma)."""
from fractions import Fraction as Q
from math import factorial, comb, prod
from collections import defaultdict
from itertools import product
import sympy as sp

m=sp.symbols('m', integer=True, positive=True)
x=sp.symbols('x')
P=100-60*x+7*x*x
F=sp.Poly(P**2,x)
coeff={k[0]:int(a) for k,a in F.terms()}
# Independent derivation by partitions of the occupancy counts of two ordered words.
# E X^k = k!^2 / m^k * [t^k] (sum t^j/(j!)^2)^m.
def partitions(n, lo=1):
    if n==0:
        yield ()
    else:
        for j in range(lo,n+1):
            for tail in partitions(n-j,j): yield (j,)+tail

def moment(k):
    out=0
    for part in partitions(k):
        count=prod(factorial(part.count(i)) for i in set(part))
        fall=prod(m-j for j in range(len(part)))
        out+=fall*sp.Rational(factorial(k)**2,count*prod(factorial(j)**2 for j in part))
    return sp.factor(out/m**k)
mu=[moment(k) for k in range(6)]
for k,v in enumerate(mu): print('moment',k,'=',v)
Z=sp.factor(sum(a*mu[k] for k,a in coeff.items()))
Y=sp.factor(sum(a*mu[k+1] for k,a in coeff.items()))
T=232*m**3+2568*m**2-5782*m+15435
assert sp.simplify((m+1)*Z-2*m*Y-3*(m-1)*T/m**3)==0
assert all(c>0 for c in sp.Poly(T.subs(m,x+2).expand(),x).all_coeffs())
assert all(c>0 for c in sp.Poly((T-232*m**3).subs(m,x+3).expand(),x).all_coeffs())
print('Z =',Z,'\nY =',Y)
print('gap numerator identity and positivity: PASS')
# An independent Laurent polynomial expansion for m=2,3,4,5.
for n in range(2,6):
    zero=(0,)*n
    X=defaultdict(int)
    for i,j in product(range(n),repeat=2):
        u=[0]*n;u[i]+=1;u[j]-=1;X[tuple(u)]+=1
    power={zero:1}
    for k in range(6):
        assert Q(power.get(zero,0),n**k)==Q(mu[k].subs(m,n))
        nxt=defaultdict(int)
        for a,c in power.items():
            for b,d in X.items(): nxt[tuple(i+j for i,j in zip(a,b))]+=c*d
        power=nxt
    print('independent Laurent multiplication: m =',n,'PASS')
# Finite support bounds in symmetric 7 x r coefficient arrays.
for r in (11,13):
    poss=[(a,b,a*(r-b)+(7-a)*b) for a in range(2,7,2) for b in range(2,r,2) if a*(r-b)+(7-a)*b<=20]
    assert poss==[(6,r-1,r+5)]
    print('symmetric mixed block',7*r, 'nonzero axis counts',poss,'PASS')
# Independent cyclotomic reduction of central-axis relations; no floating point.
for q in (77,91,539,1001):
    r=11 if q%11==0 else 13
    if q%(7*r): continue
    c=[0]*((q-1)//2)
    for j in range(1,(r+1)//2): c[q//r*j-1]+=1
    for j in range(1,4): c[q//7*j-1]-=1
    poly=sum(a*(x**(i+1)+x**(q-i-1)) for i,a in enumerate(c) if a)
    assert sp.rem(poly,sp.cyclotomic_poly(q,x),x)==0
    print('axis relation q =',q,'norm =',sum(map(abs,c)),'charge =',sum(c),'PASS')
# Exact coefficient formula by a truncated product of factorial series.
def Fhat(u):
    n=len(u)
    if sum(u) or sum(map(abs,u))>8: return Q(0)
    h=sum(max(v,0) for v in u)
    dp=[Q(1)]+[Q(0)]*(4-h)
    for v in u:
        a,b=max(v,0),max(-v,0)
        fac=[Q(1,factorial(a+l)*factorial(b+l)) for l in range(5-h)]
        dp=[sum(dp[j]*fac[k-j] for j in range(k+1)) for k in range(5-h)]
    return sum(Q(coeff[j]*factorial(j)**2,n**j)*dp[j-h] for j in range(h,5))
for n in (38,269,500):
    q=2*n+1
    assert q%77==0
    c=[0]*n
    for j in range(1,6): c[q//11*j-1]+=1
    for j in range(1,4): c[q//7*j-1]-=1
    # For any candidate pair only its membership and multiplicity in the axis
    # relation affects the coefficient. Cache by sorted residual exponents.
    cache={}; total=Q(0); nonzero=0
    for i in range(n):
        for j in range(i,n):
            if c[i]!=1 and c[j]!=1: continue
            u=c.copy();u[i]-=1;u[j]-=1
            key=tuple(sorted(u))
            if key not in cache: cache[key]=Fhat(u)
            val=cache[key];total+=abs(val);nonzero+=int(val!=0)
    ZZ=Q(Z.subs(m,n));YY=Q(Y.subs(m,n));gap=Q((n+1)*ZZ-2*n*YY,n-1)
    assert total<=Q(725760,n**3)
    assert 2*total<gap
    # Actual lower bound on the corrected normalized density.
    tau=Q((n-1)*ZZ,2*n*(ZZ-YY))
    density_min=1-tau-2*tau*total/ZZ
    assert density_min>0
    print('77-axis correction q =',q,'affected moments =',nonzero,'sum abs error =',total,'density lower bound =',density_min,'PASS')
# General coarse asymptotic constant.
B=prod((5,7,11,13,17,19));C=sum(abs(a)*factorial(k)**2 for k,a in coeff.items());C0=3*(6*B)**10
M0=2*C*C0
assert B==1616615 and C==100464
assert Q(849*C*C0,M0)<696
print('B =',B,'C =',C,'C0 =',C0)
print('m threshold =',M0)
print('ALL EXACT CHECKS PASSED')
# Uniform strictly positive floor and finite-time grid constants.
assert Q(4136)-Q(968,3)-Q(1617,27)>3000
assert Q(4136)+Q(658,9)<4210
assert Q(1451520,38**3)<Q(849,2)
assert Q(696*2,3*8420)*(1-Q(849,2*696))>Q(1,50)
assert Q(sum(abs(a) for a in coeff.values()),3000)+2<12
assert Q(4*4*12,20000)<Q(1,100)
assert Q(4,20000)<Q(1,4)
print('uniform density floor 1/50 and finite-grid constants: PASS')
