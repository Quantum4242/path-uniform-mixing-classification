#!/usr/bin/env python3
"""Exact tests of the column-block construction. Symbolic inequalities plus
independent CRT / cyclotomic-recurrence checks; no numerical LP in this file."""
from fractions import Fraction as F
from random import Random
from itertools import product
from math import prod
import sympy as s

def params(p,r,H=1):
    R=(r-1)//2; P=(p-1)//2; M=(H*(r-3)+p-5)//2
    a0=F(1,H*p*r-1); alpha=F(R-3,R); beta=F((R-3)*(R-4),R*(R-1))
    h=M%p; d=F((p-1)*M-h*(p-h),(p-1)*M*(M-1))
    return R,P,M,a0,alpha,beta,d

def symbolic():
    x=s.symbols('x')
    for p,R0 in [(3,8),(5,10),(7,12),(11,16)]:
        for z in range(p):
            Rb=R0+(z-R0)%p; R=Rb+p*x; M=R+(p-1)//2-3; h=(Rb+(p-1)//2-3)%p
            num=s.Poly(s.expand((R-4)*(2*p*R*(R-3)-3*(p-1))*((p-1)*M-h*(p-h))-p*R*(R-1)*(p-1)*M*(M-1)),x)
            assert all(c>0 for c in num.all_coeffs())
            print(f'PASS symbolic p={p}, R={Rb}+{p}t: {num.as_expr()}')
    v=F(256,361)*F(39,41)*F(16,9)*F(25,28)
    assert v==F(332800,310821)>1
    print('PASS universal disparate-prime margin lower bound:',v)
    r=x+23
    num=s.Poly(s.expand(2*(r-9)**2*(12*r-53)*(3*r-2)-(r-3)**2*(12*r-44)*3*(r-2)),x)
    assert num.as_expr()==36*x**4+2070*x**3+39386*x**2+248672*x+10472
    assert all(c>0 for c in num.all_coeffs())
    print('PASS all nontrivial two-prime powers r>=23:',num.as_expr())

def pair_thin(f,g):
    assert 0<=f<=1 and f*f<=g<=f
    if f in (0,1): assert g==f;return
    t=(g-f*f)/(f-f*f)
    assert 0<=t<=1 and t*f+(1-t)*f*f==g

def audit_moments(p,r,H,semiprime=False):
    R,P,M,a0,alpha,beta,d=params(p,r,H)
    if semiprime:
        assert H==1
        base=beta
    else:
        eta=F(R-4,R-1);base=eta*eta
    def rho(a,al):return (1-(p-1)*a/al)/p
    assert rho(a0,alpha)*base*d>a0
    for k in range(1,100):
        a=a0*(1+F(1,2**k)); common=rho(a,alpha)
        if common*base*d>a:break
    else:raise AssertionError('no strict margin')
    lam=a/(common*base*d);assert 0<lam<1
    sizes=[R]+([r] if H>1 else [])
    for size in sizes:
        al=F(size-3,size);be=F((size-3)*(size-4),size*(size-1));rr=rho(a,al)
        assert 0<common<=rr<1
        assert al*(rr-(1-rr)/F(p-1))==-a
        assert 0<=(rr-common)/(1-common)<=1
        if not semiprime:
            f=eta/al;g=base/be;pair_thin(f,g)
            assert al*f==eta and be*g==base
    if semiprime:
        f=beta/alpha;g=beta;pair_thin(f,g)
        assert alpha*f==base and g==base
    assert common*base*lam*d==a
    print(f'PASS moments p={p},r={r},H={H},M={M},a={a},lambda={lam}')

def completion(p,r,e,f,seed):
    """Independently construct a modular array with arbitrary active columns,
    then check its actual cyclotomic recurrence in natural exponent order."""
    rng=Random(seed);dp=p**e;dr=r**f;hp=dp//p;hr=dr//r;q=dp*dr
    arr={}
    def put(a,b,v):
        a%=dp;b%=dr;v%=p
        for x,y in [(a,b),((-a)%dp,(-b)%dr)]:
            if (x,y) in arr: assert arr[x,y]==v
            arr[x,y]=v
    # central box, inversion-symmetric. label rows/cols by their fiber positions.
    P=(p-1)//2;R=(r-1)//2
    y=[rng.randrange(p) for _ in range(P)]
    for a,v in enumerate(y,1):put(a*hp,0,v)
    reserves=rng.sample(range(1,R+1),3); last=reserves[-1]; cols={}
    for b in range(1,R+1):
        if b==last:continue
        col=[rng.randrange(p) for _ in range(p-1)];col.append(-sum(col)%p)
        cols[b]=col
    # column indexing: (a,+), (a,-), ... then axis
    col=[]
    for j in range(P):
        t=(-y[j]-sum(v[2*j]+v[2*j+1] for v in cols.values()))%p
        u=rng.randrange(p);col.extend([u,(t-u)%p])
    col.append(-sum(col)%p);cols[last]=col
    for b,col in cols.items():
        for a in range(1,P+1):
            put(a*hp,b*hr,col[2*a-2]);put(-a*hp,b*hr,col[2*a-1])
        put(0,b*hr,col[-1])
    put(0,0,-sum(arr[0,b*hr] for b in range(1,r)))
    # noncentral boxes paired by inversion. Complete one box, then reflect.
    seen={(0,0)}
    for i,j in product(range(hp),range(hr)):
        if (i,j) in seen:continue
        seen.update([(i,j),((-i)%hp,(-j)%hr)])
        last=rng.sample(range(r),3)[-1]; cols={}
        for b in range(r):
            if b==last:continue
            v=[rng.randrange(p) for _ in range(p-1)];v.append(-sum(v)%p);cols[b]=v
        cols[last]=[-sum(v[a] for v in cols.values())%p for a in range(p)]
        for b,v in cols.items():
            for a,w in enumerate(v):put(i+a*hp,j+b*hr,w)
    assert len(arr)==q
    for i,b in product(range(hp),range(dr)):
        assert sum(arr[i+a*hp,b] for a in range(p))%p==0
    for a,j in product(range(dp),range(hr)):
        assert sum(arr[a,j+b*hr] for b in range(r))%p==0
    vals=[arr[j%dp,j%dr] for j in range(q)]
    assert all(vals[j]==vals[-j%q] for j in range(q))
    X=s.symbols('X');poly=s.Poly(s.cyclotomic_poly(q,X),X);deg=poly.degree()
    terms=[(int(k[0]),int(v)) for k,v in poly.terms()]
    assert all(sum(c*vals[(j+k)%q] for k,c in terms)%p==0 for j in range(q))
    print(f'PASS completion q={q}, p={p}, r={r}, e={e}, f={f}, seed={seed}, all {q} cyclic recurrence equations')

if __name__=='__main__':
    symbolic()
    for p,R0 in [(3,8),(5,10),(7,12),(11,16)]:
        for r in list(s.primerange(2*R0+1,180))[:6]: audit_moments(p,int(r),1,True)
    for p,r in [(3,41),(5,41),(7,59),(11,89),(13,107)]:
        for H in [1,p,r,p*r,p*p*r]:audit_moments(p,r,H)
    for r in [23,29,31,37]:
        for p in map(int,s.primerange(3,r)):
            for H in [p,r,p*r,p*p*r]:audit_moments(p,r,H)
    for p,r,e,f in [(3,11,1,1),(5,7,1,1),(3,17,2,1),(3,11,1,2),(5,11,2,1),(3,11,2,2),(7,11,1,2)]:
        for seed in range(3):completion(p,r,e,f,seed)
