#!/usr/bin/env python3
"""Independent audit: direct polynomial recurrence mod 4 and bitset counts;
no NumPy, no original verifier imports, no orbit-representative reduction.
SymPy is used only to obtain the cyclotomic polynomial.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm
import json,sys
from sympy import cyclotomic_poly,Poly,Symbol
root=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/even-fourier-path')
x=Symbol('x')

def verify(f):
    data=json.loads(f.read_text()); q=data['q']; N=q-1; full=data.get('full_modes',False)
    assert full or q%2==1
    mod=2*q if full else q
    phi=Poly(cyclotomic_poly(mod,x),x); d=phi.degree()
    coeff=[int(phi.nth(i))%4 for i in range(d)]
    # Recurrence for coefficients of X^k in Z/4Z[X]/Phi. No use of polynomial remainder.
    powers=[[1]+[0]*(d-1)]
    for k in range(1,mod):
        a=powers[-1]; lead=a[-1]; shifted=[0]+a[:-1]
        powers.append([(v-lead*c)%4 for v,c in zip(shifted,coeff)])
    # Explicit action on the exponents, not on a precomputed phase permutation.
    us=[u for u in range(1,2*q) if gcd(u,2*q)==1]
    assert all(len(seed)==d and all(isinstance(v,int) and 0<=v<4 for v in seed) for seed in data['seeds'])
    w=list(map(Fraction,data['weights'])); assert len(w)==len(data['seeds']) and all(v>0 for v in w) and sum(w)==1
    assert data['den']==q-2
    den=lcm(*(v.denominator for v in w)); numer=[int(v*den) for v in w]
    pairs=[(r,s) for r in range(N) for s in range(r+1,N)]
    total=[0]*len(pairs); G=len(us); mask=(1<<G)-1
    for seed,weight in zip(data['seeds'],numer):
        vals=[sum(a*b for a,b in zip(seed,p))%4 for p in powers]
        lo=[0]*N; hi=[0]*N
        for j,u in enumerate(us):
            for i in range(N):
                r=i+1
                if full: a=(u*r)%mod; z=vals[a]+vals[-a%mod]
                elif r%2==0: a=(u*(r//2))%mod; z=vals[a]+vals[-a%mod]
                else: a=(u*((q-r)//2))%mod; z=-vals[a]-vals[-a%mod]
                z%=4
                lo[i]|=(z&1)<<j; hi[i]|=(z>>1)<<j
        for k,(r,s) in enumerate(pairs):
            samepar=mask^(lo[r]^lo[s]); diffhigh=hi[r]^hi[s]
            total[k]+=weight*(samepar.bit_count()-2*(samepar&diffhigh).bit_count())
    for (r,s),v in zip(pairs,total):
        assert (q-2)*v==(-den*G if (r-s)%2==0 else 0),(q,r,s)
    print(f'PASS q={q}: {len(pairs)} mode pairs, {len(w)} seed weights, {G} automorphisms',flush=True)
    return len(pairs)

if __name__=='__main__':
    fs=sorted(root.glob('q*.json'),key=lambda p:int(p.stem[1:]))+sorted((root/'prior-odd').glob('q*.json'))
    print('TOTAL:',len(fs),'certificates,',sum(verify(f) for f in fs),'exact pairs',flush=True)
