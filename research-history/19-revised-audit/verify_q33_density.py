"""Independent q=33 Fourier moments and improved positivity by completing a square."""
from verify_lattice import enumerate_lattice
from fractions import Fraction as Q
from itertools import combinations,combinations_with_replacement
from math import factorial
from functools import lru_cache
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

coef=[10000,-12000,5000,-840,49]
vals=[sum(a*b for a,b in zip(row,coef)) for row in M]
Z=vals[0];con=dict(zip(vs[1:121],vals[1:121]));ordinary=dict(zip(vs[121:],vals[121:]))
def blockid(j):
    r=idx[j]%(q//3);return min(r,q//3-r)
within=set();cross=set();single=set()
for v,t in con.items():
    i,j=(a[0] for a in v);a,b=blockid(i),blockid(j)
    if a==b:within.add(t)
    elif a==0 or b==0:single.add(t)
    else:cross.add(t)
assert len(within)==len(cross)==len(single)==1
U=within.pop();V=cross.pop();W=single.pop();A=V-U;B=V-W;G=-N*V-Z
Eextra=2*sum(map(abs,ordinary.values()))
assert A>0 and B>0
old=G-30*(A+B)-Eextra
# 5 triples, each pairwise plus singleton correction >= -3A-B^2/A.
new=G-5*(3*A+B*B/A)-Eextra
assert old==Q(-643381,4096)
assert new==Q(42831862673,172470272) and new>0
print('Z,U,V,W',Z,U,V,W)
print('G,A,B,Eextra',G,A,B,Eextra)
print('old separate L1 margin',old)
print('new square-completion margin',new,'approx',float(new))
print('All 256 target moments + normalization computed exactly, positivity PASS.')
