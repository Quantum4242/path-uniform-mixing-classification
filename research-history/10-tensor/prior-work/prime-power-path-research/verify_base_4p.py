"""Exact finite checks of the phase laws for P_(4p-1).
No floating point or external packages. Not a proof of density or primality classification.
The accompanying analytic proof applies to all odd primes p >= 5.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
from math import isqrt
C=(1,0,-1,0); S=(0,1,0,-1)

def add(law,z,w):
    assert w>=0
    law[z]+=w

def check_law(law):
    assert all(w>=0 for w in law.values())
    assert sum(law.values())==1

def expect(law,f):
    return sum((w*f(*z) for z,w in law.items()),Q(0))

def odd5():
    patterns=[((0,0,0,0,0),Q(1,96)),((0,0,0,2,2),Q(25,96)),((0,0,2,3,3),Q(5,36)),((0,1,1,3,3),Q(5,72)),((1,2,3,3,3),Q(25,48))]
    m=5
    assert sum(w for _,w in patterns)==1
    assert all(sum(z)%4==0 for z,w in patterns)
    c=sum(w*Q(sum(C[j] for j in z),m) for z,w in patterns)
    c2=sum(w*Q(sum(C[j]**2 for j in z),m) for z,w in patterns)
    cc=sum(w*Q(sum(C[j] for j in z)**2-sum(C[j]**2 for j in z),m*(m-1)) for z,w in patterns)
    ss=sum(w*Q(sum(S[j] for j in z)**2-sum(S[j]**2 for j in z),m*(m-1)) for z,w in patterns)
    assert (c,2*c2-1,cc,ss)==(0,-Q(1,18),-Q(1,18),0)

def odd(p):
    if p==5: return odd5()
    a=Q(1,4*p-2); r=Q(1,2)-p*a/(2*(p-3)); d=a*p*(p-1)/(p-3)
    law=defaultdict(Q)
    for z in [(0,2),(2,0)]: add(law,z,d/2)
    for z in product((0,2),repeat=2): add(law,z,(r-d)/4)
    for z in product((1,3),repeat=2): add(law,z,(1-r)/4)
    check_law(law)
    for i in (0,1):
        assert sum(w*C[z[i]] for z,w in law.items())==0
        assert sum(w*S[z[i]] for z,w in law.items())==0
        assert sum(w*C[z[i]]**2 for z,w in law.items())==r
    cc=expect(law,lambda x,y:C[x]*C[y]); ss=expect(law,lambda x,y:S[x]*S[y])
    assert cc==-d and ss==0
    # Exhaustively verify each possible required product of the three reserve phases.
    for h in range(4):
        reserve={(x,y,(h-x-y)%4):Q(1,16) for x,y in product(range(4),repeat=2)}
        check_law(reserve)
        for i in range(3):
            for j in range(i+1,3):
                for u,v in product(range(4),repeat=2):
                    assert sum(w for z,w in reserve.items() if z[i]==u and z[j]==v)==Q(1,16)
    # Pair count after random permutation, including reserve coordinates.
    assert 2*((p-3)*r+Q(3,2))/p-1==-a
    assert cc*Q(p-3,p*(p-1))==-a
    assert ss==0

def even(p):
    a=Q(1,4*p-2); m=p-1; r=(1-a)/2; d=(m-1)*a+(m-2)*a*a
    # First assign cosine values, then independent fair signs to all imaginary entries.
    law=defaultdict(Q)
    for z in [(1,-1),(-1,1)]: add(law,z,d/2)
    for z in [(1,0),(0,1)]: add(law,z,(r-a-d)/2)
    for z in [(-1,0),(0,-1)]: add(law,z,(r+a-d)/2)
    add(law,(0,0),1-2*r+d)
    check_law(law)
    for i in (0,1):
        assert sum(w*z[i] for z,w in law.items())==-a
        assert sum(w*z[i]**2 for z,w in law.items())==r
    assert expect(law,lambda x,y:x*y)==-d
    assert 2*r-1==-a
    assert (-d+(m-2)*a*a)/(m-1)==-a

def cyclotomic(p):
    # Phi_(8p)=(X^(4p)+1)/(X^4+1), valid for odd prime p.
    D=4*p-4; m=2*p-1
    phi=[0]*(D+1)
    for k in range(p): phi[4*k]=(-1)**k
    prod=[0]*(D+3)
    for i,c in enumerate(phi): prod[i]+=c; prod[i+2]+=c
    assert prod[m]==0
    assert all(prod[m+j]==prod[m-j] for j in range(1,m+1))
    assert all(abs(prod[m+j])==(j%2) for j in range(1,m+1))
    # Formal frequency vectors and their support-size separation from the relation.
    # 2 theta_i, theta_i, theta_i +/- theta_j are distinct positive gaps
    # for p>=5; a difference of two such forms has support <=4.
    assert 2*m+m*(m-1)==4*p*p-2*p

def main():
    primes=[p for p in range(5,102,2) if all(p%d for d in range(2,isqrt(p)+1))]
    for p in primes:
        odd(p); even(p); cyclotomic(p)
        print(f'p={p:3d} N={4*p-1:3d} bound={4*p*p-2*p+1:5d}: PASS')
    print(f'PASS: all {len(primes)} odd primes from 5 through 101; exact rational moment and coefficient checks.')
    print('Scope: finite checks only, not a Lean proof. General proof in research-note.md.')
if __name__=='__main__': main()
