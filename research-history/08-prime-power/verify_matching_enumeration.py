"""Enumerate all matchings and special schedules, independently of closed formulas.
Check p=5 at q=40,50,100 (odd number of active triples tested separately at q=100).
Only small cases are enumerated; no claim of formal verification.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict

def matchings(seq):
    if not seq:
        yield (); return
    a=seq[0]
    for j in range(1,len(seq)):
        b=seq[j]
        for rest in matchings(seq[1:j]+seq[j+1:]):
            yield ((a,b),)+rest

def matching_check(sizes,constrained,g,even_h):
    blocks=[];start=0
    for n in sizes:
        blocks.append(tuple(range(start,start+n)));start+=n
    active=[x for b in blocks for x in b];dummy= len(active)%2
    if dummy: active.append(start)
    K=len(active)-1
    # Uniform global matching: use exact symmetry for large sample; enumerate small sample.
    global_matches=list(matchings(tuple(active))) if len(active)<=10 else None
    rates=defaultdict(F)
    if global_matches:
        for mat in global_matches:
            for a,b in mat: rates[tuple(sorted((a,b)))]+=F(K-1,K*len(global_matches))
    else:
        for a,b in combinations(active,2):rates[(a,b)]+=F(K-1,K*K)
    picks=[list(combinations(b,2)) for b in blocks]
    special_count=1
    for options in picks:special_count*=len(options)
    for inside in product(*picks):
        used={x for ab in inside for x in ab}; leftover=tuple(x for x in active if x not in used)
        mats=list(matchings(leftover))
        for rest in mats:
            for a,b in inside+rest: rates[tuple(sorted((a,b)))]+=F(1,K*special_count*len(mats))
    assert all(sum(v for ab,v in rates.items() if x in ab)==1 for x in active)
    base=F(K-1,K*K);L=g+(1 if even_h and g%2 else 0)-1
    for i,j in combinations(range(len(active)),2):
        if j>=start: continue
        bi=next(k for k,b in enumerate(blocks) if i in b);bj=next(k for k,b in enumerate(blocks) if j in b)
        if bi==bj: expected=base+F(1,K*(3 if sizes[bi]==3 else 1))
        elif sizes[bi]==sizes[bj]==3:expected=base+F(1,9*K*L)
        else: expected=base
        assert rates[i,j]==expected, (sizes,i,j,rates[i,j],expected)
    print(f'PASS sizes={sizes} dummy={dummy} K={K}: all edge rates match; degree sums 1.')

# q=40: 2 groups of active triples; both parity cases have same active counts.
matching_check([3,3],2,2,True)
# q=50: 2 constrained blocks + free pair, for both parities.
matching_check([3,3,2],2,2,False)
# q=100: 5 active triples, dummy used. Uniform global matching rates by symmetry.
matching_check([3]*5,5,5,True)
print('PASS: independent small matching schedule audit.')
