#!/usr/bin/env python3
"""Exact marginal and moment audit for selected new tensor-criterion cases.
No time-sampling or numerical LP is involved. All probabilities are Fraction.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod
from functools import lru_cache
from verify_tensor import setup,bounds

@lru_cache(None)
def single(p,d,x):
    if x==0:return F(1)
    return F(p-7,p-1) if x%(d//p)==0 else F(p-6,p)

@lru_cache(None)
def both(p,d,x,y):
    h=d//p; bx,by=x%h,y%h
    if bx!=by and bx!=(-by)%h:
        return single(p,d,x)*single(p,d,y)
    if bx==0:
        if x==0:return single(p,d,y)
        if y==0:return single(p,d,x)
        if x==y or x==(-y)%d:return single(p,d,x)
        return F((p-7)*(p-9),(p-1)*(p-3))
    if bx!=by:y=(-y)%d
    return single(p,d,x) if x==y else F((p-6)*(p-7),p*(p-1))

def audit(q):
    k,odd,_=setup(q); B=prod(d//p*(p-6) for p,d in odd)
    alpha=prod(F(p-7,p-1) for p,d in odd)
    beta=prod(F((p-7)*(p-9),(p-1)*(p-3)) for p,d in odd)
    assert bounds(q)[0]
    a0=F(1,q-1)
    if k:
        groups=[list(range(1,q//2,2)),list(range(2,q//2,2))]
        sizes=[2**k*B//4,2**k*B//4-1] if k>=2 else [(B-1)//2]*2
        Ks=[M-(M%2==0) for M in sizes]
        K=max(Ks)
        for j in range(1,100):
            a=a0*(1+F(1,2**j))
            if K*a/beta+K*a*a/alpha**2 < F(1,2)-3*a/(2*alpha): break
        else:raise AssertionError('no margin')
    else:
        groups=[list(range(1,(q+1)//2))]
        M=(B-1)//2; Ks=[M-(M%2==0)]; K=Ks[0]
        a=(a0+beta/K)/2
    assert a>a0
    def ap(i): return prod(single(p,d,i%d) for p,d in odd)
    def bp(i,j): return prod(both(p,d,i%d,j%d) for p,d in odd)
    n_pairs=0; minmass=F(1)
    for g,kk in zip(groups,Ks):
        ai={i:ap(i) for i in g}
        assert all(v>=alpha for v in ai.values())
        if k:
            mu0=-a if g[0]%2==(q//2)%2 else F(0)
            mus={i:mu0/ai[i] for i in g}; rs={i:F(1,2)-a/(2*ai[i]) for i in g}
            for i in g:
                assert ai[i]*mus[i]==mu0
                assert ai[i]*rs[i]+(1-ai[i])/2==(1-a)/2
                assert rs[i]>=abs(mus[i])
        for i,j in combinations(g,2):
            bb=bp(i,j); assert bb>=beta and bb<=min(ai[i],ai[j])
            c=F(1,kk)
            if k:
                mi,mj,ri,rj=mus[i],mus[j],rs[i],rs[j]
                D=(a/bb+(1-c)*mi*mj)/c
                masses=[D/2,D/2,(ri+mi-D)/2,(ri-mi-D)/2,(rj+mj-D)/2,(rj-mj-D)/2,1-ri-rj+D]
                assert min(masses)>=0 and sum(masses)==1
                vals=[(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1),(0,0)]
                assert sum(w*x for w,(x,y) in zip(masses,vals))==mi
                assert sum(w*y for w,(x,y) in zip(masses,vals))==mj
                assert sum(w*x*x for w,(x,y) in zip(masses,vals))==ri
                assert sum(w*y*y for w,(x,y) in zip(masses,vals))==rj
                cov=sum(w*x*y for w,(x,y) in zip(masses,vals))
                assert bb*(c*cov+(1-c)*mi*mj)==-a
                minmass=min(minmass,*masses)
            else:
                D=a/(bb*c); assert 0<D<1
                # Uniform root and its negative, or independent uniform roots.
                assert -bb*c*D==-a
                minmass=min(minmass,1-D,D)
            n_pairs+=1
    print(f'PASS q={q}: {n_pairs} same-group pairs, auxiliary a={a}, min pair-law mass/mixture bound={minmass}',flush=True)

if __name__=='__main__':
    # Test exact inequalities used in the simple prime-size corollaries.
    import sympy as s
    x=s.symbols('x'); p=x+11
    D=(p-1)*(p-3)*(p-6)
    n=s.Poly((p*(p-7)*(p-9)*(p-5)-(p-11)*D).expand(),x)
    assert all(c>=0 for c in n.all_coeffs()) and n.eval(0)>0
    assert F(46,180)*(F(3,2)+F(9,4*45)) < F(1,2)-F(9,4*45)
    print('PASS symbolic ratio bound and universal even-q margin (q>=46, alpha>=2/3, beta/(B/n)>=2/3)',flush=True)
    for q in [23,46,92,667,1334,1058]:audit(q)
