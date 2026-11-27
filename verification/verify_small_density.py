"""Construct all short even-group relations by the proved coset classification,
and compute signed Fourier errors exactly (not the original absolute upper bound).
Every generated relation is independently checked by cyclotomic reduction.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product,combinations
from collections import Counter
from functools import lru_cache
from math import factorial,comb
from sympy import cyclotomic_poly,Poly,Symbol

# A central array with both axes nonzero, q=pr; for symmetric 35 use analytical list.
def central(p,r,anti):
    P,R=(p-1)//2,(r-1)//2
    if (p,r)==(5,7):
        if anti:
            for i,j,s,t in product(range(2),range(3),(-1,1),(-1,1)):
                a=[0]*2;b=[0]*3;a[i]=s;b[j]=t;yield a,b
        else:
            for s in (-1,1):
                for A in (1,2):yield [s*A]*2,[-s*A]*3
                for j in range(3):
                    for t in (0,-2):
                        b=[-s]*3;b[j]=s*t;yield [s]*2,b
                for i in range(2):
                    a=[0]*2;a[i]=s
                    for k in (1,2,3):
                        for js in combinations(range(3),k):
                            b=[-s if j in js else 0 for j in range(3)];yield a,b
    elif not anti:
        for u in range(2,p,2):
            for v in range(2,r,2):
                if u*(r-v)+(p-u)*v>20:continue
                for ii,jj,sg in product(combinations(range(P),u//2),combinations(range(R),v//2),(-1,1)):
                    yield [sg if i in ii else 0 for i in range(P)],[-sg if j in jj else 0 for j in range(R)]

def relations(q,idx):
    h=q//2;n=len(idx); lookup={r:i for i,r in enumerate(idx)}
    def vec(arr):
        # arr is a root exponent -> coefficient map, exponents modulo 2q.
        v=[0]*n; a=Counter()
        for e,c in arr:
            e%=2*q
            if e>=q:e-=q;c=-c
            a[e]+=c
        for e,c in a.items():
            if not c:continue
            if e in (0,h):return None
            r=min(e,q-e)
            if r not in lookup:return None
            cv=c if e<h else -c
            if a[q-e]!=-c:return None
            v[lookup[r]]=cv
        if 0<sum(map(abs,v))<=10:return tuple(v)
    pure5=set();pure7=set();out=set();central5=set()
    for p,store in [(5,pure5),(7,pure7)]:
        if q%p:continue
        for a in range(q//p):
            if a==(-a)%(q//p):continue
            for s in (-1,1):
                v=vec([(e,s) for k in range(p) for e in (a+2*q*k//p,-a-2*q*k//p)])
                if v:store.add(v)
        out|=store
    for v in pure5:
        out.add(tuple(2*x for x in v))
    for v,w in combinations(pure5,2):
        if all(not (x and y) for x,y in zip(v,w)):out.add(tuple(x+y for x,y in zip(v,w)))
    for p,r in [(5,7),(5,11),(5,13),(5,17),(7,11),(7,13)]:
        d=p*r
        if q%d:continue
        for a,anti in [(0,False),(h,True)]:
            for A,B in central(p,r,anti):
                sign=-1 if anti else 1
                aa=[0]+A+[sign*x for x in A[::-1]];bb=[0]+B+[sign*x for x in B[::-1]]
                v=vec([(a+2*q*i//p+2*q*j//r,aa[i]+bb[j]) for i,j in product(range(p),range(r))])
                if v:
                    out.add(v)
                    if d==35 and sum(map(abs,v))==5:central5.add(v)
        if d==35:
            for a in range(q//d):
                if a==(-a)%(q//d):continue
                for i,j,s in product(range(p),range(r),(-1,1)):
                    arr=[]
                    for k,l in product(range(p),range(r)):
                        c=s*((k==i)-(l==j));e=a+2*q*k//p+2*q*l//r
                        if c:arr.extend([(e,c),(-e,c)])
                    v=vec(arr)
                    if v:out.add(v)
    for v,w in product(central5,pure5):
        if all(not(x and y) for x,y in zip(v,w)):out.add(tuple(x+y for x,y in zip(v,w)))
    # Independently verify every relation in integer arithmetic, not floating point.
    z=Symbol('z');poly=Poly(cyclotomic_poly(2*q,z),z);D=poly.degree();p=[int(poly.nth(i)) for i in range(D)]
    powers=[[1]+[0]*(D-1)]
    for _ in range(1,2*q):
        w=powers[-1];powers.append([v-w[-1]*c for v,c in zip([0]+w[:-1],p)])
    energies=[[a+b for a,b in zip(powers[r],powers[2*q-r])] for r in idx]
    for v in out:
        assert sum(map(abs,v))<=10 and any(v)
        assert all(sum(x*a for x,a in zip(v,col))==0 for col in zip(*energies)),(q,idx,v)
    return out

# Independent direct finite Laurent moment coefficient calculation via rational convolution.
@lru_cache(None)
def block(a):
    d={}
    for k,l in product(range(9),range(3)):
        c=Q(0)
        for j in range(l+1):
            h=k+2*j
            if h>=a and (h-a)%2==0:c+=Q(comb(l,j)*2**j*(-1)**(l-j)*comb(h,(h-a)//2),2**h)
        if c:d[k,l]=c/factorial(k)/factorial(l)
    return d

def mul(a,b):
    d={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            if i+k+2*(j+l)<=8 and j+l<=2:
                key=i+k,j+l;d[key]=d.get(key,Q(0))+x*y
    return {k:v for k,v in d.items() if v}
@lru_cache(None)
def basepower(n):
    if n==0:return {(0,0):Q(1)}
    return mul(basepower(n-1),block(0))
@lru_cache(None)
def coeff(n,b,pat):
    if sum(pat)>8 or len(pat)>n:return Q(0)
    poly=basepower(n-len(pat))
    for a in pat:poly=mul(poly,block(a))
    if b:poly=mul(poly,{(i,0):Q(1,2**i*factorial(i)) for i in range(9)})
    p=[10000,-3707,254];f=[sum(p[i]*p[j-i] for i in range(max(0,j-2),min(2,j)+1)) for j in range(5)]
    return sum(f[j]*Q(2,n)**j*factorial(2*j)*poly.get((2*j,0),0) for j in range(5))-Q(2672,n)*sum(p[j]*Q(2,n)**j*factorial(2*j)*poly.get((2*j,1),0) for j in range(3))+Q(1336**2*2,n*n)*poly.get((0,2),0)
def pat(v):return tuple(sorted(abs(x) for x in v if x))
def check(q,b):
    h=q//2;idx=[r for r in range(1,h) if (r%2==h%2)==bool(b)];n=len(idx);N=q-1
    rel=relations(q,idx)
    Z=coeff(n,b,());U=coeff(n,b,(1,1));D=coeff(n,b,(2,));W=coeff(n,b,(1,))
    G=-N*U-Z; margin=G-2*n*(abs(U-D)+abs(b*U-W))
    es=abs(sum(coeff(n,b,pat(c)) for c in rel));E0=es
    vs=[]
    for i in range(n):vs.extend([((i,1),),((i,2),)])
    for i,j in combinations(range(n),2):vs.extend([((i,1),(j,1)),((i,1),(j,-1))])
    exact=0
    for v in vs:
        e=Q(0)
        for c in rel:
            w=list(c)
            for i,k in v:w[i]-=k
            e+=coeff(n,b,pat(w))
        exact+=abs(e)
    es+=2*exact
    # combine baseline and Fourier correction BEFORE absolute value (sharper).
    rem=G-E0;combined=Q(0)
    for v in vs:
        e=Q(0)
        for c in rel:
            w=list(c)
            for i,k in v:w[i]-=k
            e+=coeff(n,b,pat(w))
        target=b*U if len(v)==1 and v[0][1]==1 else U
        base=W if len(v)==1 and v[0][1]==1 else D if len(v)==1 else U
        combined+=abs(target-base-e)
    rem-=2*combined
    print(q,b,n,len(rel),'patterns',dict(Counter(pat(v) for v in rel)),'separate_margin',float(margin-es),'combined_margin',float(rem),'PASS' if rem>0 else 'not proved',flush=True)
    return rem
if __name__=='__main__':
    qs=[20,28,40,50,56,70,80,98,100,110,112,130,140]
    results={q:[check(q,b) for b in (0,1)] for q in qs}
    print('both groups passed:',[q for q,v in results.items() if min(v)>0])
    print('still need certificates:',[q for q,v in results.items() if min(v)<=0])
    assert all(min(v)>0 for v in results.values())
    with (Path(__file__).parent/'exact-density-margins.txt').open('w',encoding='utf-8') as f:
        for q,v in results.items(): print(q,*(str(a) for a in v),file=f)
