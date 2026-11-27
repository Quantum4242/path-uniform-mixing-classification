#!/usr/bin/env python3
"""Cross-check the radical/p>20 localization by independent polynomial remainders.
These finite checks are illustrations of the general algebraic proof, not its basis.
"""
from sympy import Symbol, Poly, cyclotomic_poly, factorint
from itertools import combinations
from math import prod
from random import Random
from collections import defaultdict
x=Symbol('x');rng=Random(20261127)

def cyclo(n):return Poly(cyclotomic_poly(n,x),x)
def poly(A):return Poly.from_dict({(e,):c for e,c in A.items() if c},x,domain='ZZ')
def clean(A):return {e:c for e,c in A.items() if c}
def divisible(A,P):
    # Integer monic long division, independent of SymPy's rational Poly.rem.
    degree,tail=P
    work=dict(A)
    for e in range(max(work,default=-1),degree-1,-1):
        c=work.pop(e,0)
        if c:
            for j,u in tail:
                k=e-degree+j;work[k]=work.get(k,0)-c*u
    return not any(work.values())
def divisor(P):
    return P.degree(),[(e,int(c)) for (e,),c in P.terms() if e<P.degree()]

def check(q):
    even=q%2==0;order=2*q if even else q
    d=prod(p for p in factorint(q) if p!=2);a=q//d
    D=prod(p for p in factorint(d) if p<=20);k=q//D
    full=cyclo(order);small=cyclo(2*d if even else d);local=cyclo(2*D if even else D)
    assert full==poly({i*a:int(c) for (i,),c in small.terms()})
    F,S,L=map(divisor,(full,small,local))
    def vanishes(A):return divisible(A,F)
    def by_cosets(A,step,p):
        groups=defaultdict(dict)
        for e,c in A.items():
            r,j=e%step,e//step;groups[r][j]=c
        return all(divisible(g,p) for g in groups.values())
    # Generate full prime cycles, folded modulo q in the even case.
    def cycle(p,base,coef):
        out=defaultdict(int)
        for j in range(p):
            e=(base+j*(order//p))%order
            if even and e>=q: e-=q;sg=-1
            else:sg=1
            out[e]+=sg*coef
        return clean(out)
    low=[p for p in factorint(d) if p<=20]
    yes=no=0
    for trial in range(36):
        A=defaultdict(int)
        # Half the tests start with exactly vanishing sums, the others with arbitrary sparse sums.
        if trial%2==0 and low:
            for _ in range(rng.randint(1,3)):
                p=rng.choice(low)
                C=cycle(p,rng.randrange(order),rng.choice([-2,-1,1,2]))
                if len(A)+len(C)>20:continue
                for e,c in C.items():A[e]+=c
            if trial%4==2:A[rng.randrange(q)]+=1
        else:
            for e in rng.sample(range(q),min(q,rng.randint(1,20))):A[e]=rng.choice([-2,-1,1,2])
        A=clean(A);assert len(A)<=20
        ans=vanishes(A)
        assert ans==by_cosets(A,a,S),(q,A,'radical')
        assert ans==by_cosets(A,k,L),(q,A,'small-prime localization')
        yes+=ans;no+=not ans
    print('q=',q,'radical=',d,'small-prime conductor=',D,'zero/nonzero=',yes,no,'PASS',flush=True)
    return yes,no

if __name__=='__main__':
    qs=[9,25,27,33,35,49,55,77,99,105,175,225,245,275,385,429,539,595,665,805,1155,20,28,40,70,98,100,140,350,700,320,1610,3036,4232]
    results=[check(q) for q in qs]
    # Enumerate all possible mixed conductors directly from the support inequality.
    for primes,expected in [([5,7,11,13,17,19],[35,55,65,77,85,91,385]),([3,11,13,17,19],[33,39,51,57])]:
        got=sorted(prod(c) for l in range(2,len(primes)+1) for c in combinations(primes,l) if 2+sum(p-2 for p in c)<=20)
        assert got==expected,(got,expected)
        print('mixed conductors',got,'PASS')
    print('All',len(qs),'polynomial identities and',sum(sum(a) for a in results),'exact sparse comparisons PASS; zero/nonzero',sum(a[0] for a in results),sum(a[1] for a in results))
