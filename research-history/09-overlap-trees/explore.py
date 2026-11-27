import numpy as np
import sympy as sp
from scipy.optimize import linprog
from math import gcd
from itertools import combinations, combinations_with_replacement
import sys

def data(q):
    m=(q-1)//2; x=sp.Symbol('x'); poly=sp.Poly(sp.cyclotomic_poly(q,x),x); d=poly.degree()
    powers=np.zeros((q,d),dtype=np.int64); powers[0,0]=1
    coeff=np.array(list(reversed([int(c) for c in poly.all_coeffs()[1:]])),dtype=np.int64)
    for j in range(1,q):
        powers[j,1:]=powers[j-1,:-1]; powers[j]-=powers[j-1,-1]*coeff
    V=powers[1:m+1]+powers[q-1:q-m-1:-1]
    perms=np.array([[min((u*j)%q,(-u*j)%q)-1 for j in range(1,m+1)] for u in range(1,m+1) if gcd(u,q)==1])
    orbits=[]
    for sign in [-1,1]:
        unseen=set(combinations_with_replacement(range(m),2) if sign==1 else combinations(range(m),2))
        while unseen:
            i,j=min(unseen); orb=sorted({tuple(sorted((int(p[i]),int(p[j])))) for p in perms}); unseen.difference_update(orb); orbits.append((sign,orb))
    return V,orbits

def run(q,ns=5000):
    V,orbits=data(q); m=len(V); d=V.shape[1]; rng=np.random.default_rng(q)
    seeds=rng.integers(0,4,(ns,d),dtype=np.int64); phase=(seeds@V.T)%4
    cos=np.array([1,0,-1,0]); rows=[np.ones(ns,dtype=np.int64)]; rhs=[q-2]
    for s,orb in orbits:
        i,j=np.array(orb).T; rows.append(cos[(phase[:,i]+s*phase[:,j])%4].sum(axis=1)); rhs.append(-len(orb) if s==-1 else 0)
    A=np.array(rows); den=q-2; b=np.array(rhs)
    print('q',q,'m',m,'orbits',len(orbits),'samples',ns,flush=True)
    res=linprog(np.zeros(ns),A_eq=A,b_eq=b/den,bounds=(0,None),method='highs')
    if not res.success: print(res.message,flush=True); return
    idx=np.where(res.x>1e-9)[0]; B=sp.Matrix(A[:,idx]); z=sp.Matrix(b); sol,par=B.gauss_jordan_solve(z); assert not par.rows; assert all(v>0 for v in sol); assert B*sol==z
    from pathlib import Path
    import json
    out={'q':q,'den':den,'seeds':seeds[idx].tolist(),'weights':[str(v/den) for v in sol]}
    Path(__file__).with_name(f'q{q}.json').write_text(json.dumps(out,indent=2)+'\n'); print('PASS',q,'support',len(idx),'max denominator digits',max(len(str(sp.denom(v/den))) for v in sol),flush=True)
if __name__=='__main__':
    for q in map(int,sys.argv[1:]): run(q)
