"""Find a simpler positive density at q=33, independently of the LP certificate.
All moment data and the final positivity inequality are exact fractions.
Floating point optimization is exploratory only.
"""
from verify_lattice import enumerate_lattice
from fractions import Fraction as Q
from itertools import combinations,combinations_with_replacement
from math import factorial
from functools import lru_cache
import numpy as np
from scipy.optimize import differential_evolution
q=33;m=16;N=32
idx,rel=enumerate_lattice(q);rel.add((0,)*m)
# F_k = X^k Fourier coefficients from multinomial expansion.
@lru_cache(None)
def cp(k,pattern):
    if sum(pattern)!=0:return Q(0)
    h=sum(map(abs,pattern))//2
    if h>k:return Q(0)
    # coefficient [t^(k-h)] product_i sum_j t^j/((abs(u_i)+j)! j!).
    poly=[Q(1)]+[Q(0)]*(k-h)
    for a in list(map(abs,pattern))+[0]*(m-len(pattern)):
        p=[Q(1,factorial(a+j)*factorial(j)) for j in range(k-h+1)]
        poly=[sum(poly[j]*p[i-j] for j in range(i+1)) for i in range(k-h+1)]
    return poly[-1]*Q(factorial(k)**2,m**k)

def moments(v):
    patterns={}
    for c in rel:
        u=list(c)
        for i,a in v:u[i]-=a
        if sum(u)!=0 or sum(map(abs,u))>8:continue
        p=tuple(sorted(x for x in u if x));patterns[p]=patterns.get(p,0)+1
    return [sum(n*cp(k,p) for p,n in patterns.items()) for k in range(5)]
vs=[()] + [((i,1),(j,-1)) for i,j in combinations(range(m),2)] + [((i,1),(j,1)) for i,j in combinations_with_replacement(range(m),2)]
M=[moments(v) for v in vs]
# The optimal scale T=-N*V may choose any quantile of conjugate moments.
mat=np.array(M,dtype=float)
kcon=m*(m-1)//2

def conv(a,b,c):return [a*a,2*a*b,b*b+2*a*c,2*b*c,c*c]
def bestscale(vals):
    # concave, piecewise-linear T-Z-2 sum |T/N+conj| - 2 sum |ordinary|.
    # derivative increases by 1 - 2/N per signed crossing; choose breakpoint.
    return -N*np.sort(vals[1:1+kcon])[(kcon-N//2)//2]
def margin_float(x):
    b,c=x;vals=mat@np.array(conv(100,b,c));t=bestscale(vals)
    return t-vals[0]-2*np.sum(np.abs(t/N+vals[1:1+kcon]))-2*np.sum(np.abs(vals[1+kcon:]))
r=differential_evolution(lambda x:-margin_float(x),[(-100,-10),(0,30)],seed=33,tol=1e-9)
print('exploration',r.x,'margin',-r.fun)
# integer coefficient scan near optimum; exact verification below
b0,c0=map(round,r.x);_,b,c=max((margin_float((b,c)),b,c) for b in range(b0-8,b0+9) for c in range(c0-8,c0+9))
print('chosen polynomial',100,b,c)
v=[sum(x*y for x,y in zip(row,conv(100,b,c))) for row in M];Z=v[0]
con=v[1:1+kcon];ordinary=v[1+kcon:]
T=max((-N*x for x in con),key=lambda t:t-Z-2*sum(abs(t/N+y) for y in con)-2*sum(map(abs,ordinary)))
margin=T-Z-2*sum(abs(T/N+y) for y in con)-2*sum(map(abs,ordinary))
print('Z',Z,'T',T,'exact correction margin',margin,'approx',float(margin))
print("PASS" if T>0 and margin>0 else "L1 sufficient test failed; this is not a nonexistence certificate")
