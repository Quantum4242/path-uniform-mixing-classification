#!/usr/bin/env python3
"""Exact formal-polynomial and finite-array checks for the three-block proof.
Requires SymPy. No floating-point arithmetic, optimizer, or numerical eigensolver.
"""
import sympy as s
from math import factorial as fac, prod
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations_with_replacement
from collections import defaultdict, Counter
K=4
@lru_cache(None)
def comps(a,n):
    if n==1:return [(a,)]
    return [(i,)+j for i in range(a+1) for j in comps(a-i,n-1)]
def poly(n,test):
    d={}
    for a,b in product(range(K+1),repeat=2):
        v=F(0)
        for x in comps(a,n):
            for y in comps(b,n):
                u=[x[i]-y[i]+test[i] for i in range(n)]
                if (len(set(u))==1 if n==3 else u[0]==0):
                    v+=F(1,prod(fac(j) for j in x+y))
        if v:d[a,b]=s.Rational(v.numerator,v.denominator)
    return d
def mul(a,b):
    c=defaultdict(lambda:0)
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            if i+k<=K and j+l<=K:c[i+k,j+l]+=u*v
    return {k:s.expand(v) for k,v in c.items() if v!=0}
B=s.symbols('b',integer=True,nonnegative=True); m=3*B+1
P=poly(3,(0,0,0)); Q=poly(1,(0,)); T={ij:u for ij,u in P.items() if ij!=(0,0)}
def powP(b):
    out=defaultdict(lambda:0); pp={(0,0):1}
    for k in range(2*K+1):
        for ij,v in pp.items():out[ij]+=v*s.sympify(s.prod(b-i for i in range(k)))/fac(k)
        pp=mul(pp,T)
    return {k:s.expand(v) for k,v in out.items()}
co=[10000,-12000,5000,-840,49]
def moment(b, factors):
    p=powP(b)
    for f in factors:p=mul(p,f)
    return s.factor(sum(s.Integer(co[k])*fac(k)**2*p.get((k,k),0)/m**k for k in range(K+1)))
Z=moment(B,[Q]); U=moment(B-1,[Q,poly(3,(1,-1,0))]); V=moment(B-2,[Q,poly(3,(1,0,0)),poly(3,(-1,0,0))]); W=moment(B-1,[poly(1,(-1,)),poly(3,(1,0,0))])
expected=[335016*B**4+414504*B**3+122490*B**2+126705*B+2209,-8*(8154*B**3+9171*B**2+21603*B-14243),-24*(2718*B**3+1857*B**2+11035*B-21989),-8*(8154*B**3+9171*B**2+21015*B-13655)]
for name,val,exp in zip(['Z','U','V','W'],[Z,U,V,W],expected):
    assert s.cancel(val*m**4-exp)==0
    print(name,'=',val,'PASS')
G=s.factor(-2*m*V-Z); E=s.factor(6*B*(2*V-U-W)); x=s.symbols('x')
def positive_shift(f,shift):
    num,den=s.fraction(s.factor(f)); pn=s.Poly(s.expand(num.subs(B,x+shift)),x); pd=s.Poly(s.expand(den.subs(B,x+shift)),x)
    assert all(c>=0 for c in pn.all_coeffs()) and pn.eval(0)>0
    assert all(c>=0 for c in pd.all_coeffs()) and pd.eval(0)>0
    return pn.as_expr()
for name,val in [('V-U',V-U),('V-W',V-W),('G-E',G-E)]:
    print(name,'shift b=4+x positive numerator:',positive_shift(val,4))
# Upper bound on ordinary-product corrections. Counts include both 11 and 13 if present.
extra=s.Integer(24917760)/m**3+s.Integer(2257920)/m**4
print('G-E-extra shift b=16+x positive numerator:',positive_shift(G-E-extra,16))
assert s.cancel((G-E-extra).subs(B,16)-s.Rational(4521017,16807))==0
print('margin at b=16:',(G-E-extra).subs(B,16))
# Exhaustive central 3*r array enumeration for t=+1; global sign accounts for t=-1.
# Other entries cannot fit the length bound, as shown in the note.
expected_counts={11:{(8,2,0,'simple'):10,(10,2,0,'double'):5,(10,2,1,'simple'):5},13:{(8,-2,0,'simple'):6,(10,-2,1,'simple'):1},17:{},19:{}}
small={}
for r in (11,13,17,19):
    R=(r-1)//2; counts=Counter(); vectors=[]
    for bs in product(range(-2,2),repeat=R):
        c=(1,)+tuple(v for j in bs for v in (j,1+j,1+j)); l=sum(map(abs,c)); ch=sum(c)
        if l>10:continue
        if l%2==0 and abs(ch) in (0,2):
            kind='double' if max(map(abs,c))>1 else 'simple'
            counts[l,ch,0,kind]+=1
            assert abs(ch)==2
            vectors.append(tuple(v*(ch//2) for v in c))
        for sign in (-1,1):
            ch2=ch+3*sign
            if l+3<=10 and (l+3)%2==0 and abs(ch2) in (0,2):
                counts[l+3,ch2,1,'simple']+=1
                assert max(map(abs,c))==1 and abs(ch2)==2
    assert dict(counts)==expected_counts[r],(r,counts)
    for (l,ch,ext,kind),n in counts.items():
        assert kind in ('simple','double') and ch in (-2,2)
    print('central conductor',3*r,'parameter vectors',4**R,'counts',dict(counts),'PASS')
    small[r]=vectors
@lru_cache(None)
def coeff(n,pattern):
    h=sum(map(abs,pattern))//2
    if h>4:return F(0)
    assert h in (3,4) and sum(pattern)==0
    base=F(1,prod(fac(abs(v)) for v in pattern))
    if h==4:return F(28224,n**4)*base
    return base*(-F(30240,n**3)+F(28224,n**4)*(n-len(pattern)+sum(F(1,abs(v)+1) for v in pattern)))
for r in (11,13):
    b=(r-1)//2; n=3*b+1; err=F(0)
    for i,j in combinations_with_replacement(range(n),2):
        val=F(0)
        for c in small[r]:
            u=list(c);u[i]-=1;u[j]-=1
            val+=coeff(n,tuple(sorted(v for v in u if v)))
        err+=2*abs(val)
    margin=F(G.subs(B,b))-F(E.subs(B,b))-err
    if r==11:assert margin==F(-643381,4096) # this simple density does not prove q=33
    if r==13:assert err==F(34231680,130321) and margin>0
    print('q=',3*r,'exact ordinary correction',err,'positivity margin',margin)
# Small q=9: align the triple with rho=(1-2a)/3; when aligned use
# an opposite singleton with probability a/rho, otherwise independent.
a=F(1,7); rho=(1-2*a)/3; lam=a/rho
assert 0<lam<1 and rho-(1-rho)/2==-a and -rho*lam==-a and a>F(1,8)
print('q=9 explicit law: rho=',rho,'lambda=',lam,'PASS')
print('ALL EXACT ASSERTIONS PASSED')
