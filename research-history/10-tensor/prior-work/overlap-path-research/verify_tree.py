#!/usr/bin/env python3
"""Exact checks of the three-tree construction: small combinatorial audit and
polynomial positivity for all parameters in two infinite ranges."""
from fractions import Fraction as F
from itertools import permutations, product
import sympy as s

P,R,x,y=s.symbols('P R x y')
m=2*P*R+P+R; M=m-3*(P+R)
E=3/P+3/R-3/(P*R)
Jsr=3/P+18/(P*R)+6/(R*(R-1))-6/(P*R)*(1+2/(R-1))
Jsc=Jsr.xreplace({P:R,R:P})
Jdd=6/(P*(P-1))+6/(R*(R-1))+18/(P*R)-6/(P*R)*(2/(P-1)+2/(R-1))+6/(P*(P-1)*R*(R-1))
beta={'parallel':(1-3/P)*(1-3/R), 'same_row':1-E+Jsr/4,
      'same_col':1-E+Jsc/4,'different_cells':1-E+Jdd/4,
      'axis_interior_lower':1-3/(2*P)-E/2,'axes_lower':1-3/P}

def connected(edges,n):
    adj=[[] for _ in range(n)]
    for a,b,_ in edges: adj[a].append(b);adj[b].append(a)
    seen={0};stack=[0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:seen.add(j);stack.append(j)
    return len(seen)==n

def audit(a,b):
    # Enumerate center triples, not flips; conditional probabilities of reserve
    # events from independent fair flips are exact and derived from edge counts.
    n=0; Ecount=0; counts=[F(0)]*4
    pairs=[((0,0),(0,0)),((0,0),(0,1)),((0,0),(1,0)),((0,0),(1,1))]
    for aa,bb in product(permutations(range(a),3),permutations(range(b),3)):
        n+=1
        trees=[]
        for i,j in zip(aa,bb):
            tree={(i,a+k,0) for k in range(b)}|{(k,a+j,1) for k in range(a) if k!=i}|{(i,a+b,0)}
            assert len(tree)==a+b and connected(tree,a+b+1)
            trees.append(tree)
        reserve=set.union(*trees); assert len(reserve)==3*(a+b)
        # Ground attachment could be switched to each corresponding col;
        # all such alternatives are distinct and preserve the tree property.
        for i,j,t in zip(aa,bb,trees):
            alt=(t-{(i,a+b,0)})|{(a+j,a+b,0)}
            assert len(alt)==a+b and connected(alt,a+b+1)
        def k(ij):
            i,j=ij;return sum((i,a+j,e) in reserve for e in [0,1])
        Ecount+=k((0,0))
        for idx,(u,v) in enumerate(pairs):
            counts[idx]+=int(k(u)==0) if u==v else F(2-k(u),2)*F(2-k(v),2)
    assert F(Ecount,n)==F(E.subs({P:a,R:b}))
    for idx,label in enumerate(list(beta)[:4]):
        assert counts[idx]/n==F(beta[label].subs({P:a,R:b})),label
    print(f'PASS P={a} R={b}: {n} ordered triple pairs, disjoint spanning trees and 4 exact pair rates')

def symbolic():
    for name,expr in beta.items():
        num,den=s.fraction(s.factor(s.together((2*m-1)*expr-M)))
        for label,sub in [('P>=6,R>=8',{P:x+6,R:y+8}),('P=5,R>=18',{P:5,R:y+18})]:
            np=s.Poly(num.subs(sub).expand(),x,y);dp=s.Poly(den.subs(sub).expand(),x,y)
            assert all(c>=0 for c in np.coeffs()) and np.eval({x:0,y:0})>0,(name,label,np)
            assert all(c>=0 for c in dp.coeffs()) and dp.eval({x:0,y:0})>0,(name,label,dp)
            print(f'PASS {name:20s} {label:12s}: numerator={np.as_expr()}; denominator={dp.as_expr()}')

if __name__=='__main__':
    for a,b in [(3,4),(4,5),(5,6)]:audit(a,b)
    symbolic()
