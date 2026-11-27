#!/usr/bin/env python3
"""Independent central two-prime array audit. Enumerate integer rows and use
remaining-weight recursion over columns. No original checker imports.
For A_ij=a_i+b_j with a0=b0=0, inversion symmetry reduces half of each axis.
Each half-array axis value contributes to l1 weight, so every |axis|<=10.
Prune only by the exact contribution to l1 weight, never by predicted types.
"""
from collections import Counter
from itertools import product

def rows(k,limit):
    if not k:
        yield ();return
    for a in range(-limit,limit+1):
        for tail in rows(k-1,limit-abs(a)):yield (a,)+tail

def audit(p,r,anti):
    P,R=(p-1)//2,(r-1)//2; out=Counter(); charge=Counter()
    for a in rows(P,10):
        if not any(a):continue
        rem=10-sum(map(abs,a))
        opts=[]
        for b in range(-rem,rem+1):
            v=(b,)+tuple(t for ai in a for t in ((ai+b,ai-b) if anti else (ai+b,ai+b)))
            cost=sum(map(abs,v))
            if cost<=rem:opts.append((b,cost,v))
        if not opts:continue
        mincost=min(t[1] for t in opts)
        def visit(j,left,vals,nonzero):
            if j==R:
                if not nonzero:return
                pat=tuple(sorted(abs(x) for x in vals if x))
                out[pat]+=1
                if not anti:charge[(sum(pat),sum(vals))]+=1
                return
            for b,c,v in opts:
                if c+(R-j-1)*mincost<=left:visit(j+1,left-c,vals+v,nonzero or b!=0)
        visit(0,rem,a,False)
    return out,charge
for p,r in [(5,7),(5,11),(5,13),(5,17),(7,11),(7,13)]:
    for anti in (False,True):
        out,c=audit(p,r,anti)
        fmt={str(k):v for k,v in sorted(out.items())}
        print(f'{p}x{r}, anti={anti}: {sum(out.values())} arrays; {fmt}',flush=True)
        if not anti: print(' length, charge counts:',dict(sorted(c.items())),flush=True)
        if (p,r)==(5,7):
            expected=Counter({(2,)*5:2,(1,)*8:18,(1,)*5:2,(1,)*8+(2,):6,(1,)*9:12,(1,)*10:4}) if not anti else Counter({(1,)*8+(2,):24})
        else:
            expected=Counter() if anti else {(5,11):Counter({(1,)*7:2,(1,)*10:10}),(5,13):Counter({(1,)*8:2}),(5,17):Counter({(1,)*10:2}),(7,11):Counter({(1,)*8:2}),(7,13):Counter({(1,)*9:2})}[(p,r)]
        assert out==expected,(p,r,anti,out,expected)
print('ALL 12 central two-prime array inventories independently matched')
