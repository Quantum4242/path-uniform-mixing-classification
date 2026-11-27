#!/usr/bin/env python3
"""Check every original spectral pair. No optimizer, floats, or orbit partition.
Requires SymPy for exact cyclotomic polynomial remainder and NumPy for small
integer products only. All probability weights and final sums use Python ints.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm
import json
import numpy as np
import sympy as sp

x=sp.Symbol('x')

def full_coeff(q,full):
    mod=2*q if full else q
    f=sp.Poly(sp.cyclotomic_poly(mod,x),x,domain=sp.ZZ)
    d=f.degree()
    def rem(r):
        p=sp.Poly(x**r+x**((mod-r)%mod),x,domain=sp.ZZ).rem(f)
        return [int(p.nth(k)) for k in range(d)]
    if full: return [rem(r) for r in range(1,q)]
    return [rem(r//2) if r%2==0 else [-v for v in rem((q-r)//2)] for r in range(1,q)]

def verify(path):
    c=json.loads(path.read_text()); q=c['q']; N=q-1
    assert c['den']==q-2
    V=full_coeff(q,c.get('full_modes',False))
    d=len(V[0]); seeds=c['seeds']; weights=list(map(Fraction,c['weights']))
    assert len(weights)==len(seeds) and all(w>0 for w in weights) and sum(weights)==1
    assert all(len(seed)==d and all(isinstance(s,int) and 0<=s<4 for s in seed) for seed in seeds)
    # Full cyclotomic Galois action; conjugation acts trivially, so include all units
    us=[u for u in range(1,2*q) if gcd(u,2*q)==1]
    G=len(us)
    # Bound int64 operations: every multiplication below uses a number in {-1,0,1};
    # dot product length G. phase inputs use Python arbitrary precision first.
    assert G<2**62
    perms=np.array([[min((u*r)%(2*q),(-u*r)%(2*q))-1 for r in range(1,q)] for u in us])
    assert all(sorted(p.tolist())==list(range(N)) for p in perms)
    den=lcm(*(w.denominator for w in weights)); nums=[int(w*den) for w in weights]
    tot=np.zeros((N,N),dtype=object); cos=np.array([1,0,-1,0],dtype=np.int64); sin=np.array([0,1,0,-1],dtype=np.int64)
    for seed,num in zip(seeds,nums):
        phases=np.array([sum(a*b for a,b in zip(seed,row))%4 for row in V],dtype=np.int64)[perms]
        C=cos[phases]; S=sin[phases]
        counts=C.T@C+S.T@S
        tot+=counts.astype(object)*num
    for r in range(N):
        assert tot[r,r]==den*G
        for s in range(r+1,N):
            assert (q-2)*tot[r,s]==(-den*G if (r-s)%2==0 else 0),(q,r,s)
    print(f'PASS q={q}, P_{N}: {N*(N-1)//2} full pairs; {len(seeds)} seed orbits; G={G}; exact',flush=True)

def collision(q):
    V=full_coeff(q,True); seen={}
    for i in range(q-1):
        for j in range(i+1,q-1):
            key=tuple(a-b for a,b in zip(V[i],V[j])); parity=(i-j)%2
            if key in seen and seen[key][0]!=parity:
                _,a,b=seen[key]
                print(f'NEGATIVE CONTROL q={q}: exact equal gaps ({a+1},{b+1}) and ({i+1},{j+1}), opposite parity',flush=True);return
            seen[key]=(parity,i,j)
    raise AssertionError('expected collision')

if __name__=='__main__':
    for q in [12,15,21,30]: collision(q)
    for p in sorted(Path(__file__).parent.glob('q*.json'),key=lambda p:int(p.stem[1:])): verify(p)
