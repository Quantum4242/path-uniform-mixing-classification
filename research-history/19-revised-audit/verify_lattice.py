"""Independent exhaustive lattice check: free coordinate L1 <=10 follows directly
from RREF. C++ enumerates all free integer vectors; denominators checked exactly.
No short-relation classifications used in generating this enumeration.
"""
from pathlib import Path
from sympy import Symbol,Poly,cyclotomic_poly,Matrix,ilcm
from math import comb
import subprocess
from verify_small_density import relations
HERE=Path(__file__).parent

def enumerate_lattice(q,b=None):
    h=q//2;idx=[r for r in range(1,h) if (r%2==h%2)==bool(b)] if b is not None else list(range(1,h+1));order=2*q if b is not None else q
    z=Symbol('z'); p=Poly(cyclotomic_poly(order,z),z);D=p.degree();cs=[int(p.nth(i)) for i in range(D)]
    powers=[[1]+[0]*(D-1)]
    for _ in range(1,order):
        w=powers[-1];powers.append([v-w[-1]*c for v,c in zip([0]+w[:-1],cs)])
    A=Matrix([[powers[r][i]+powers[order-r][i] for r in idx] for i in range(D)])
    R,piv=A.rref();free=[i for i in range(len(idx)) if i not in piv];d=len(free)
    lines=[f'{len(idx)} {d} {len(piv)}',' '.join(map(str,free))]
    for i,j in enumerate(piv):
        den=1
        for k in free:den=ilcm(den,R[i,k].q)
        coeffs=[-R[i,k]*den for k in free]
        assert den>0 and den<2**30 and all(c.q==1 and 10*abs(c)<2**30 for c in coeffs)
        lines.append(' '.join(map(str,[j,den]+coeffs)))
    result=subprocess.run([str(HERE/'enumerate_lattice')],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True)
    rel={tuple(map(int,l.split())) for l in result.stdout.splitlines()}
    expected=sum(comb(d,k)*comb(10,k)*2**k for k in range(min(d,10)+1))
    assert int(result.stderr.split()[0])==expected
    assert all(0<sum(map(abs,c))<=10 and A*Matrix(c)==Matrix.zeros(D,1) for c in rel)
    print(q,b,'dimension',d,result.stderr.strip(),flush=True)
    return idx,rel
if __name__=='__main__':
    for q in (20,28,40,50,56,70,80,98,100,110,112,130,140):
        for b in (0,1):
            idx,rel=enumerate_lattice(q,b);old=relations(q,idx)
            assert rel==old,(q,b,len(rel-old),len(old-rel))
            print('  independent exhaustive list MATCH',flush=True)
    print('All 26 groups: PASS',flush=True)
