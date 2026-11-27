#!/usr/bin/env python3
"""Exact parameters for the finite-grid theorem in research-note.md.
No floating point needed to establish the bounds. Decimal digit counts are
computed from exact integers. This does not simulate the astronomical grid.
"""
from fractions import Fraction
from math import comb, gcd
import sys

def phi(n):
    ans=n; d=2
    while d*d<=n:
        if n%d==0:
            ans-=ans//d
            while n%d==0: n//=d
        d+=1
    return ans-ans//n if n>1 else ans

def bounds(q,d=None):
    N=q-1; m=N//2
    # m representatives of the +/- energy pairs; zero, if present, is fixed.
    D=phi(2*q)//2
    if d is None: d=m*m if q%2 else m*(m+1)
    assert 1<=d<=N*(N-1)//2 and m>=1
    # For y=(N-1)/N*v, an l1 margin of r=1/(2N) is available.
    r=Fraction(1,2*N); eta=r/(4*d)
    k=1
    # k eta^2/4 > m log(2k+1)+log(4), proved by a rational test.
    while k*eta**2/4 <= m*(2*k+1).bit_length()+2: k*=2
    W=2*m*k; L=16*W**D*(2*k+1)**m
    delta=Fraction(1,W)
    T=(L-1)*delta
    assert k*eta**2/4 > m*(2*k+1).bit_length()+2
    assert Fraction(4*W**D,L)==Fraction(1,4*(2*k+1)**m)
    assert 2*eta*d==r/2
    print(f'q={q}, N={N}, m={m}, D={D}, gap count bound={d}, eta={eta}, k={k}, delta={delta}')
    print(f'  sample count has {len(str(L))} decimal digits; duration upper bound < 10^{len(str(T.numerator//T.denominator))+0}')
    print(f'  support size <= {d+1}; all parameter inequalities PASS')
    return k,L,delta

def kernel_checks():
    # ((1+cos x)/2)^k = sum_{j=-k}^k binom(2k,k+j)/4^k e^(ijx).
    # Check the identity via exact Laurent-polynomial recurrence.
    p={0:Fraction(1)}
    for k in range(1,33):
        new={}
        for j,a in p.items():
            for h,b in [(-1,Fraction(1,4)),(0,Fraction(1,2)),(1,Fraction(1,4))]:
                new[j+h]=new.get(j+h,0)+a*b
        p=new
        assert all(p[j]==Fraction(comb(2*k,k+j),4**k) for j in range(-k,k+1))
        assert sum(p.values())==1 and p[0]>=Fraction(1,2*k+1)
    print('PASS: 32 exact Laurent-polynomial kernel checks')

if __name__=='__main__':
    if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
    kernel_checks()
    for q,d in [(3,None),(9,None),(20,90),(35,None),(385,None),(429,None),(595,None)]: bounds(q,d)
