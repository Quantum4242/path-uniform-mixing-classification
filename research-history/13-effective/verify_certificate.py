#!/usr/bin/env python3
"""Independent exact verifier. No optimizer, floating-point arithmetic or saved LP matrix.
Uses NumPy only for bounded integer matrix products, SymPy only for Phi_q.
The proof in research-note.md explains why the checked inequalities suffice.
"""
from pathlib import Path
from math import gcd
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
import json, sys
import numpy as np
import sympy as sp

LIM=2**62

def matmul(A,B):
    assert A.ndim==B.ndim==2 and A.shape[1]==B.shape[0]
    assert int(np.max(np.abs(A)))*int(np.max(np.abs(B)))*A.shape[1]<LIM
    return A@B

def check(path):
    c=json.loads(path.read_text()); q=c['q']; Q=c['Q']; N=q-1; m=N//2
    assert q%2==1 and Q>0
    # Independent polynomial reduction by backward monic long division.
    x=sp.Symbol('x'); poly=sp.Poly(sp.cyclotomic_poly(q,x),x); d=poly.degree()
    coeff=[int(poly.nth(i)) for i in range(d+1)]; assert coeff[-1]==1
    V=[]
    for j in range(1,m+1):
        a=[0]*q; a[j]+=1; a[q-j]+=1
        for k in range(q-1,d-1,-1):
            t=a[k]
            if t:
                for i in range(d+1): a[k-d+i]-=t*coeff[i]
        assert not any(a[d:]); V.append(a[:d])
    seeds=np.array(c['seeds'],dtype=np.int64); n=len(seeds)
    assert seeds.shape==(n,d) and ((seeds>=0)&(seeds<4)).all()
    phases=matmul(seeds,np.array(V,dtype=np.int64).T)%4
    # Direct physical-mode phase values: theta_(2j)=alpha_j, theta_(q-2j)=-alpha_j.
    full=np.zeros((n,N),dtype=np.int64)
    for j in range(1,m+1): full[:,2*j-1]=phases[:,j-1]; full[:,q-2*j-1]=-phases[:,j-1]%4
    us=[u for u in range(1,2*q) if gcd(u,2*q)==1]; G=len(us)
    perms=np.array([[min((u*j)%(2*q),(-u*j)%(2*q))-1 for j in range(1,q)] for u in us])
    assert all(sorted(row.tolist())==list(range(N)) for row in perms)
    assert all((int(perms[k,j])-j)%2==0 for k in range(G) for j in range(N))
    # Generate rows from full spectral pairs, not from optimizer's row data.
    # Canonical order is (negative/same parity first, positive/opposite parity second),
    # then lexicographically least pair of alpha-indices.
    rows=[np.ones(n,dtype=np.int64)]; b=[q-2]; checked=set(); cos=np.array([1,0,-1,0],dtype=np.int64)
    for s in [-1,1]:
        pending=set(combinations(range(1,m+1),2) if s==-1 else combinations_with_replacement(range(1,m+1),2))
        while pending:
            i,j=min(pending)
            i0=2*i-1; j0=(2*j-1 if s==-1 else q-2*j-1)
            # Convert each full-mode orbit back to alpha-indices for canonical ordering.
            u0=perms[:,i0]; v0=perms[:,j0]
            def alpha(k):
                r=k+1
                return r//2 if r%2==0 else (q-r)//2
            orb={tuple(sorted((alpha(int(a)),alpha(int(b_))))) for a,b_ in zip(u0,v0)}
            pending.difference_update(orb)
            # All full pairs from the alpha orbit, including both mirrored parities / orientations.
            for a,b_ in orb:
                pairs=([(2*a,2*b_),(q-2*a,q-2*b_)] if s==-1 else [(2*a,q-2*b_),(2*b_,q-2*a)])
                for v,w in pairs:
                    assert v!=w and (v-w)%2==(0 if s==-1 else 1)
                    checked.add(tuple(sorted((v,w))))
            # Evaluate the original full-mode moment over ALL Galois automorphisms.
            sums=cos[(full[:,u0]-full[:,v0])%4].sum(axis=1)
            # In the mixed-parity case, exchanging the two alpha indices has the same cos sum.
            # The quotient orbit is uniform, hence normalized sum equals sum over its distinct pairs.
            assert np.all((sums*len(orb))%G==0)
            rows.append(sums*len(orb)//G); b.append(-len(orb) if s==-1 else 0)
    assert len(checked)==N*(N-1)//2
    A=np.array(rows,dtype=np.int64); b=np.array(b,dtype=np.int64)
    assert A.shape==(n,n), (A.shape,n)
    R=np.array(c['R'],dtype=np.int64); u=np.array(c['u'],dtype=np.int64)
    assert R.shape==(n,n) and u.shape==(n,)
    D=Q*np.eye(n,dtype=np.int64)-matmul(R,A)
    assert int(np.max(np.abs(D)))*n<LIM and int(np.max(np.abs(R)))*n<LIM
    eps=Fraction(int(np.abs(D).sum(axis=1).max()),Q)
    rn=Fraction(int(np.abs(R).sum(axis=1).max()),Q)
    Au=matmul(A,u[:,None])[:,0]
    assert int(np.max(np.abs(Au)))*(q-2)+int(np.max(np.abs(b)))*Q<LIM
    res=Fraction(int(np.abs(Q*b-(q-2)*Au).max()),Q*(q-2))
    assert eps<1
    err=rn*res/(1-eps); wmin=Fraction(int(u.min()),Q)
    assert wmin>err
    print(f'PASS q={q}, N={N}, rows={n}, full pairs={len(checked)}, G={G}',flush=True)
    print(f'  inverse defect <= {eps}; inverse norm <= {rn}; residual <= {res}',flush=True)
    print(f'  min approximate weight = {wmin}; rigorous error <= {err}; strictly positive lower bound = {wmin-err}',flush=True)
    return eps,rn,res,err,wmin

if __name__=='__main__':
    for q in map(int,sys.argv[1:]): check(Path(__file__).with_name(f'q{q}.json'))
