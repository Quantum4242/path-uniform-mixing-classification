if not __debug__:
    raise RuntimeError("Run without -O: assertions are required for verification")

"""Exact arithmetic certificate for the P19 phase distribution.
Requires Python 3 and SymPy. No floating-point calculations.
Verifies the cyclotomic relation and all phase moments, not the analytic
Kronecker/convexity arguments (which are in proof.md).
"""
from collections import defaultdict, Counter
from fractions import Fraction as Q
from itertools import permutations, combinations
from math import lcm
import sympy as sp

ODD = [((0,0,0,0,0), Q(1,96)),
       ((0,0,0,2,2), Q(25,96)),
       ((0,0,2,3,3), Q(5,36)),
       ((0,1,1,3,3), Q(5,72)),
       ((1,2,3,3,3), Q(25,48))]
EVEN = [((0,0,1,3), Q(1,6)),
        ((0,2,2,3), Q(1,2)),
        ((2,3,3,3), Q(1,18)),
        ((1,3,3,3), Q(5,18))]
COS = (1,0,-1,0)

def orbit_law(patterns, constrained=False):
    result = defaultdict(Q)
    for p,w in patterns:
        assert w>0
        if constrained: assert sum(p)%4 == 0
        orbit = sorted(set(permutations(p)))
        for a in orbit:
            result[a] += w/(2*len(orbit))
            result[tuple((-v)%4 for v in a)] += w/(2*len(orbit))
    assert sum(result.values()) == 1
    assert all(w>0 for w in result.values())
    return result

def integer_law(law):
    den=lcm(*(w.denominator for w in law.values()))
    return den, [(a,int(w*den)) for a,w in law.items()]

def main():
    x=sp.symbols('x')
    p=sp.cyclotomic_poly(40,x)
    assert p==x**16-x**12+x**8-x**4+1
    R=sp.Matrix([[sp.Poly(sp.rem(x**j+x**(40-j),p,x),x).nth(k)
                  for j in range(1,10)] for k in range(16)])
    relation=sp.Matrix([1,0,-1,0,-1,0,1,0,1])
    assert R*relation==sp.zeros(16,1)
    minor=R.extract([0,1,2,5,6,7,8,9],list(range(8)))
    assert minor.det()==-2
    assert R.rank()==8
    print('Cyclotomic relation verified; rank = 8; minor determinant = -2.')
    theta = {j: sp.Poly(sp.rem(x**j + x**((-j)%40),p,x),x)
             for j in range(40)}
    gaps={tuple((theta[r]-theta[s]).nth(k) for k in range(16))
          for r,s in combinations(range(1,20),2)}
    assert len(gaps)==90
    print('Distinct positive Bohr frequencies = 90; Carathéodory bound = 91.')
    od=orbit_law(ODD,True); ev=orbit_law(EVEN)
    do,oi=integer_law(od); de,ei=integer_law(ev)
    pairs=list(combinations(range(1,20),2)); totals=Counter()
    for a,wa in oi:
        for b,wb in ei:
            ph=[0]*20
            for j,s,v in zip((1,3,5,7,9),(1,-1,-1,1,1),a):
                ph[j]=(s*v)%4
            for j,v in zip((2,4,6,8),b): ph[j]=v
            for j in range(1,10): ph[20-j]=(-ph[j])%4
            assert (ph[1]-ph[3]-ph[5]+ph[7]+ph[9])%4==0
            for r,s in pairs:
                totals[r,s]+=wa*wb*COS[(ph[r]-ph[s])%4]
    counts=Counter()
    for r,s in pairs:
        actual=Q(totals[r,s],do*de)
        expected=Q(-1,18) if (r-s)%2==0 else Q(0)
        assert actual==expected,(r,s,actual,expected)
        assert Q(18,19)*actual==(Q(-1,19) if (r-s)%2==0 else Q(0))
        counts[str(actual)]+=1
    print(f'Odd support {len(od)}, even support {len(ev)}, joint support {len(od)*len(ev)}.')
    print(f'All {len(pairs)} distinct spectral pairs verified exactly: {dict(counts)}.')
    print('Mixing with 1/19 Haar measure gives the exact target moments.')
    # Independent check of the spectral mixing identity in Q[zeta_40].
    # F_r = 40 E_r = theta_(r(k-l)) - theta_(r(k+l)), where E_r is
    # the sine eigenvector projector. For the target moments,
    # 19*1600*M_kl = 20*sum F_r^2 - (sum F_even)^2 - (sum F_odd)^2.
    from functools import lru_cache
    phi=sp.Poly(p,x)
    vectors={j:tuple(int(theta[j].nth(k)) for k in range(16)) for j in range(40)}
    @lru_cache(None)
    def square(v):
        a=[0]*31
        for i,vi in enumerate(v):
            for j,vj in enumerate(v): a[i+j]+=vi*vj
        for i in range(30,15,-1):
            u=a[i]; a[i]=0
            for offset, sign in [(4,1),(8,-1),(12,1),(16,-1)]: a[i-offset]+=sign*u
        return tuple(a[:16])
    for k in range(1,20):
        for l in range(1,20):
            fs=[tuple(a-b for a,b in zip(vectors[(r*(k-l))%40],vectors[(r*(k+l))%40]))
                for r in range(1,20)]
            oe=[tuple(sum(f[j] for f in fs[i::2]) for j in range(16)) for i in (0,1)]
            tot=tuple(20*sum(z[j] for z in map(square,fs))-square(oe[0])[j]-square(oe[1])[j]
                      for j in range(16))
            assert tot==(1600,)+(0,)*15,(k,l,tot)
    print('Independent exact spectral mixing check: all 361 entries equal 1/19.')
    print('PASS (finite algebra certificate only; not a Lean proof).')

if __name__=='__main__': main()
