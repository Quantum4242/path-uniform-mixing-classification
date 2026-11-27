import numpy as np
import sympy as sp
from scipy.optimize import linprog
from math import gcd
from itertools import combinations
from pathlib import Path
import json,sys

def data(q):
    x=sp.Symbol('x'); poly=sp.Poly(sp.cyclotomic_poly(2*q,x),x); d=poly.degree()
    powers=np.zeros((2*q,d),dtype=np.int64); powers[0,0]=1
    coeff=np.array(list(reversed([int(c) for c in poly.all_coeffs()[1:]])),dtype=np.int64)
    for j in range(1,2*q):
        powers[j,1:]=powers[j-1,:-1]; powers[j]-=powers[j-1,-1]*coeff
    V=powers[1:q]+powers[2*q-1:q:-1]
    perms=np.array([[min((u*j)%(2*q),(-u*j)%(2*q))-1 for j in range(1,q)] for u in range(1,q) if gcd(u,2*q)==1])
    unseen=set(combinations(range(q-1),2)); orbits=[]
    while unseen:
        i,j=min(unseen); orb=sorted({tuple(sorted((int(p[i]),int(p[j])))) for p in perms}); unseen.difference_update(orb); orbits.append(orb)
    return V,orbits

def run(q,ns=5000):
    V,orbits=data(q); d=V.shape[1]; rng=np.random.default_rng(q)
    seeds=rng.integers(0,4,(ns,d),dtype=np.int64); phase=(seeds@V.T)%4
    cos=np.array([1,0,-1,0]); rows=[np.ones(ns,dtype=np.int64)]; rhs=[q-2]
    for orb in orbits:
        i,j=np.array(orb).T; rows.append(cos[(phase[:,i]-phase[:,j])%4].sum(axis=1)); rhs.append(-len(orb) if (orb[0][0]-orb[0][1])%2==0 else 0)
    A=np.array(rows); den=q-2; b=np.array(rhs)
    print('q',q,'orbits',len(orbits),'samples',ns,flush=True)
    # remove duplicated rows, detect direct contradictions
    D={}
    for row,val in zip(A,b):
        key=row.tobytes()
        if key in D and D[key]!=val:
            print('Contradiction in sampled rows (not general proof)',q,flush=True); return
        D[key]=val
    ids=np.unique(A,axis=0,return_index=True)[1]; A=A[ids]; b=b[ids]
    print('distinct rows',len(ids),flush=True)
    res=linprog(np.zeros(ns),A_eq=A,b_eq=b/den,bounds=(0,None),method='highs')
    if not res.success: print(res.message,flush=True); return
    idx=np.where(res.x>1e-9)[0]; B=sp.Matrix(A[:,idx]); z=sp.Matrix(b); sol,par=B.gauss_jordan_solve(z); assert not par.rows; assert all(v>0 for v in sol); assert B*sol==z
    out={'q':q,'den':den,'seeds':seeds[idx].tolist(),'weights':[str(v/den) for v in sol],'full_modes':True}
    Path(__file__).with_name(f'q{q}.json').write_text(json.dumps(out,indent=2)+'\n'); print('PASS',q,'support',len(idx),'max denominator digits',max(len(str(sp.denom(v/den))) for v in sol),flush=True)
if __name__=='__main__':
    for q in map(int,sys.argv[1:]): run(q)
