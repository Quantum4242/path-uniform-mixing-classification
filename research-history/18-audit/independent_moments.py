#!/usr/bin/env python3
"""Independent moment audit via raw binomial convolution and polynomial identity testing.
No imports from original programs. All calculations are Fraction/integer.
For each marked moment, after multiplying by n^4 (even) or m^4 (odd),
its degree in n or b is <=8: each term has at most 2j+l marked/unmarked
summation factors (even), or 2j (odd), and denominator n^(j+l) or m^j.
Grouping index choices by equalities yields falling factorial polynomials.
Nine distinct parameter values therefore suffice to establish the identities.
"""
from fractions import Fraction as Q
from math import comb
from functools import lru_cache
from itertools import product
from collections import defaultdict

# even: direct recurrence for raw moments of (sum cos, sum cos 2phi)
@lru_cache(None)
def cm(k): return Q(comb(k,k//2),2**k) if k%2==0 else Q(0)
def single(k,l,mark):
    out=0
    for j in range(l+1):
        a=comb(l,j)*2**j*(-1)**(l-j)
        t=k+2*j
        out+=a*(cm(t) if mark==0 else cm(t+1) if mark==1 else 2*cm(t+2)-cm(t))
    return out

def join(A,B,K,L):
    return {(k,l):sum(comb(k,i)*comb(l,j)*A[i,j]*B[k-i,l-j] for i in range(k+1) for j in range(l+1)) for k in range(K+1) for l in range(L+1)}

def identity(K,L): return {(k,l):int(k==l==0) for k in range(K+1) for l in range(L+1)}
def even(n,b,marks):
    K,L=8,2; A=identity(K,L)
    for mark in list(marks)+[0]*(n-len(marks)):
        B={(k,l):single(k,l,mark) for k in range(K+1) for l in range(L+1)}
        A=join(A,B,K,L)
    def mixed(j,l):
        return Q(2,n)**j*sum(comb(2*j,k)*Q(b,2)**(2*j-k)*A[k,l] for k in range(2*j+1))
    p=[10000,-3707,254]; t=-1336
    return sum(p[i]*p[j]*mixed(i+j,0) for i in range(3) for j in range(3))+Q(2*t,n)*sum(p[j]*mixed(j,1) for j in range(3))+Q(t*t,n*n)*mixed(0,2)

def expected_even(n,b):
    if not b:
        return [Q(121704774*n**3-4750735*n**2+11341862*n-18628995,2*n**3),Q(-2*(9427103*n**3+9607186*n**2-29923359*n+64354710),n**4),Q(-(37705166*n**3+15783578*n**2-43863387*n+51483768),2*n**4),Q(0)]
    return [Q(243409548*n**4-47209882*n**3+26186325*n**2-7941564*n+16129,4*n**4),Q(-(18854206*n**3+6845765*n**2-40652319*n+60741814),n**4),Q(-(37705166*n**3+498483*n**2-25384760*n+18516092),2*n**4),Q(-(18854206*n**3+5639384*n**2-32204787*n+28870910),n**4)]
for b in (0,1):
    for n in range(2,11):
        got=[even(n,b,mark) for mark in ((),(1,1),(2,),(1,))]
        assert got==expected_even(n,b),(b,n,got,expected_even(n,b))
    print('even bias',b,': 36 exact evaluations; degree <=8 => 4 polynomial identities PASS')

# odd: raw joint moments of complex sums via Laurent polynomial expansion
@lru_cache(None)
def laurent_power(base,k):
    d=len(base[0]); A={(0,)*d:1}
    for _ in range(k):
        B=defaultdict(int)
        for u,v in A.items():
            for t in base: B[tuple(a+b for a,b in zip(u,t))]+=v
        A=B
    return A

def block_mom(base,mark,K=4):
    neg=tuple(tuple(-v for v in u) for u in base)
    out={}
    for k,l in product(range(K+1),repeat=2):
        a=laurent_power(base,k); b=laurent_power(neg,l)
        out[k,l]=sum(v*b.get(tuple(-x-y for x,y in zip(u,mark)),0) for u,v in a.items())
    return out
triple=((1,0),(0,1),(-1,-1)); singleton=((1,),)
F=[10000,-12000,5000,-840,49]
def odd(b,marks,sm):
    A=identity(4,4)
    for mark in list(marks)+[(0,0)]*(b-len(marks)):
        A=join(A,block_mom(triple,mark),4,4)
    A=join(A,block_mom(singleton,(sm,)),4,4)
    m=3*b+1
    return sum(Q(F[j]*A[j,j],m**j) for j in range(5))
for b in range(2,11):
    m=3*b+1
    got=[odd(b,(),0),odd(b,((1,-1),),0),odd(b,((1,0),(-1,0)),0),odd(b,((1,0),),-1)]
    exp=[Q(335016*b**4+414504*b**3+122490*b*b+126705*b+2209,m**4),Q(-8*(8154*b**3+9171*b*b+21603*b-14243),m**4),Q(-24*(2718*b**3+1857*b*b+11035*b-21989),m**4),Q(-8*(8154*b**3+9171*b*b+21015*b-13655),m**4)]
    assert got==exp,(b,got,exp)
print('odd three-block: 36 exact evaluations; degree <=8 => 4 polynomial identities PASS')
print('TOTAL: 108 exact evaluations, 12 general polynomial identities PASS')
