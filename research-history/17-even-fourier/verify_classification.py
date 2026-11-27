"""Finite combinatorial checks supporting the analytic classification.
The enumeration is over a proven necessary axis weight bound, not all paths.
"""
from itertools import product
from collections import Counter
from sympy import isprime
from pathlib import Path

def axes(k,remaining):
    if k==0:
        yield ()
        return
    for a in range(-remaining,remaining+1):
        for b in axes(k-1,remaining-abs(a)):
            yield (a,)+b

expected_sym=Counter({(2,)*5:2,(1,)*8:18,(1,)*5:2,(1,)*8+(2,):6,(1,)*9:12,(1,)*10:4})
expected_anti=Counter({(1,)*8+(2,):24})
for anti,expected in [(False,expected_sym),(True,expected_anti)]:
    got=Counter(); checked=0
    for a,b,c,d,e in axes(5,10):
        checked+=1
        if not ((a or b) and (c or d or e)): continue
        vals=[a,b,c,d,e]+[v for i in (a,b) for j in (c,d,e) for v in ((i+j,i-j) if anti else (i+j,i+j))]
        if 0<sum(map(abs,vals))<=10:
            got[tuple(sorted(abs(v) for v in vals if v))]+=1
    assert got==expected,(anti,got)
    print('central 35','antisymmetric' if anti else 'symmetric',checked,'axis vectors; nonzero-axis arrays',sum(got.values()),dict(got),'PASS')
expected={(5,11):[(4,8,20),(4,10,14)],(5,13):[(4,12,16)],(5,17):[(4,16,20)],(7,11):[(6,10,16)],(7,13):[(6,12,18)]}
for (p,r),v in expected.items():
    got=[]
    for u,w in product(range(2,p,2),range(2,r,2)):
        base=u*(r-w)+(p-u)*w
        if base<=20:got.append((u,w,base))
        assert 2*base+u*w>40
    assert got==v
    print('mixed central',p,r,'symmetric cases',got,'antisymmetric none: PASS')
for a,b in product(range(3),repeat=2):
    for cs in product(range(-1,2),repeat=3):
        arr=[a-1,b-1,*cs]+[v for i in (a,b) for j in cs for v in (i+j,i+j)]
        if max(map(abs,arr))<=1: assert sum(map(abs,arr))!=5
print('central 385 symmetric exceptional slice: all 243 axis tuples PASS')
# q>=142 implies both parity groups have >=35 positive levels. For smaller q,
# min odd prime>=11 gives short-relation-free proof; twice-prime cases are known.
qs=[q for q in range(4,142,2) if q%3 and (q%5==0 or q%7==0) and not isprime(q//2)]
assert qs==[20,28,40,50,56,70,80,98,100,110,112,130,140]
assert all(Path(__file__).with_name(f'q{q}.json').is_file() for q in qs)
print('all exceptional even moduli:',qs,'PASS')
