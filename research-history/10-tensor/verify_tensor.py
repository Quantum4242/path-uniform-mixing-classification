#!/usr/bin/env python3
"""Independent exact tests of CRT tensor completion and sufficient bounds.
Uses Fraction and SymPy only for independent cyclotomic recurrence check.
The tests are not a proof of the general theorem; see research-note.md.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod
import random
import sympy as sp

rng=random.Random(51739)

def factors(q):
    return dict(sp.factorint(q))

def setup(q):
    fac=factors(q); k=fac.pop(2,0)
    odd=[(int(p),int(p**a)) for p,a in fac.items()]
    mods=([2**(k+1)] if k else [])+[d for p,d in odd]
    return k,odd,mods

def neg(x,mods): return tuple((-a)%d for a,d in zip(x,mods))

def reserve(p,d):
    h=d//p; O=set()
    for b in range(h):
        if b>(-b)%h: continue
        fiber=[b+h*j for j in range(p)]
        if b==0:
            for j in rng.sample(range(1,(p+1)//2),3): O.update((h*j,(-h*j)%d))
        else:
            chosen=rng.sample(fiber,6); O.update(chosen); O.update((-x)%d for x in chosen)
    assert 0 not in O and O=={(-x)%d for x in O}
    assert all(sum(x%h==b for x in O)==6 for b in range(h))
    return O

def spare(p,d,O,protected):
    h=d//p; S=set()
    for b in range(h):
        if b>(-b)%h: continue
        choices=sorted(x for x in O if x%h==b and x not in protected and (-x)%d not in protected)
        assert choices
        x=choices[0]; S.update((x,(-x)%d))
    assert not S&protected
    return S

def orbit(x,k,mods):
    out={x:1,neg(x,mods):1}
    if k:
        for y in list(out):
            z=((y[0]+2**k)%mods[0],)+y[1:]
            if z in out and out[z]!=-1: return {w:0 for w in out}
            out[z]=-1
    return out

def rep(r,mods): return tuple(r%d for d in mods)

def run_trial(q):
    k,odd,mods=setup(q); off=int(bool(k)); n=prod(mods)
    Os=[reserve(p,d) for p,d in odd]
    modes=range(1,q//2) if k else range(1,(q+1)//2)
    coords=[rep(r,mods) for r in modes]
    isactive=lambda x: all(x[i+off] not in O for i,O in enumerate(Os))
    active=[x for x in coords if isactive(x)]; remaining=[x for x in coords if not isactive(x)]
    B=prod(d//p*(p-6) for p,d in odd)
    assert len(active)==((2**k*B)//2-1 if k else (B-1)//2)
    if k:
        for parity in (0,1):
            ct=sum(x[0]%2==parity for x in active)
            assert ct==(2**k*B//4 - (parity==0) if k>=2 else (B-1)//2)
    # Prescribe independent angles for all active modes and two reserved modes.
    extra=rng.sample(remaining,min(2,len(remaining)))
    targets={x:F(rng.randrange(-11,12),rng.randrange(1,6)) for x in active+extra}
    S=[spare(p,d,O,{x[i+off] for x in extra}) for i,((p,d),O) in enumerate(zip(odd,Os))]
    allowed=[list(range(d)) for d in mods]
    for i,s in enumerate(S): allowed[i+off]=[x for x in allowed[i+off] if x not in s]
    vals={x:F(0) for x in product(*allowed)}
    for x,v in targets.items():
        orb=orbit(x,k,mods); assert all(s!=0 for s in orb.values())
        for y,s in orb.items():
            assert y in vals
            vals[y]=s*v
    # Tensor extension: for each fiber fill missing residues with equal share.
    for i,(p,d) in enumerate(odd):
        j=i+off; h=d//p
        other=[allowed[t] for t in range(len(mods)) if t!=j]
        for u in product(*other):
            def key(x): return u[:j]+(x,)+u[j:]
            for b in range(h):
                fiber=list(range(b,d,h)); missing=[x for x in fiber if x in S[i]]
                v=-sum((vals[key(x)] for x in fiber if x not in S[i]), F(0))/len(missing)
                for x in missing: vals[key(x)]=v
        allowed[j]=list(range(d))
    assert len(vals)==n
    for x,v in targets.items(): assert vals[x]==v
    for x,v in vals.items():
        assert vals[neg(x,mods)]==v
        if k: assert vals[((x[0]+2**k)%mods[0],)+x[1:]]==-v
        for i,(p,d) in enumerate(odd):
            j=i+off; h=d//p
            assert sum((vals[x[:j]+((x[j]+h*t)%d,)+x[j+1:]] for t in range(p)),F(0))==0
    # Independent direct check: a functional on powers of zeta must obey the
    # full irreducible cyclotomic polynomial recurrence, not merely line sums.
    X=sp.Symbol('X'); coeff=list(reversed(sp.Poly(sp.cyclotomic_poly(n,X),X).all_coeffs())); D=len(coeff)-1
    v=[vals[rep(r,mods)] for r in range(n)]
    for r in range(n-D):
        assert sum((int(c)*v[r+j] for j,c in enumerate(coeff) if c), F(0))==0
    return len(active),len(extra),n

def bounds(q):
    k,odd,_=setup(q)
    ps=[p for p,d in odd]
    assert ps and min(ps)>=11
    B=prod(d//p*(p-6) for p,d in odd)
    alpha=prod(F(p-7,p-1) for p in ps)
    beta=prod(F((p-7)*(p-9),(p-1)*(p-3)) for p in ps)
    a=F(1,q-1)
    if not k:
        M=(B-1)//2; K=M-(M%2==0)
        ok=beta>K*a
        return ok, beta-K*a
    M=2**k*B//4 if k>=2 else (B-1)//2
    K=M # common upper bound
    margin=F(1,2)-3*a/(2*alpha)-K*a/beta-K*a*a/(alpha*alpha)
    return margin>0,margin

def small_pair_audit():
    for p in (11,13,17):
        # central fibre: exhaustive reserve masks (three pairs)
        masks=[set(xs)|{(-x)%p for x in xs} for xs in combinations(range(1,(p+1)//2),3)]
        single=min(F(sum(x not in O for O in masks),len(masks)) for x in range(p))
        pair=min(F(sum(x not in O and y not in O for O in masks),len(masks)) for x,y in combinations(range(p),2))
        assert single==F(p-7,p-1)
        assert pair==F((p-7)*(p-9),(p-1)*(p-3))
        # noncentral fibre: exhaustive six-subsets
        masks=list(map(set,combinations(range(p),6)))
        assert F(sum(0 not in O and 1 not in O for O in masks),len(masks))==F((p-6)*(p-7),p*(p-1))
        print(f'PASS exact mask probabilities p={p}')

def main():
    small_pair_audit()
    for q in [7,49,77,539,7*11*13,14,28,98,154,308,2*7*11*13]:
        results=[run_trial(q) for _ in range(4)]
        print(f'PASS q={q}: 4 exact tensor completions, active/reserve prescriptions and cyclotomic recurrence; last={results[-1]}')
    # Entire parameter ranges follow from these rational inequalities and
    # monotonicity of q/(q-2), 1/(q-2); not just tests of sampled q.
    assert F(37,140)*(F(3,2)+F(36,25*35)) < F(1,2)-F(9,5*35)
    print('PASS universal even-q conservative bound at q=37, alpha>=5/6, beta>=2/3')
    for q in [13*17,17*19,19*23,23*29,29*31,31*37, 31*37*41, 43*47*53, 53*59*61*67, 2*31*37, 4*31*37, 2*43*47*53, 2*109*113*127, 37**2*41, 4*37**2*41]:
        ok,margin=bounds(q)
        print(f'{"PASS" if ok else "NOT COVERED"} sufficient criterion q={q}, exact margin={margin}')
if __name__=='__main__': main()
