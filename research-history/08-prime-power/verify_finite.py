"""Independent exact finite checks of arithmetic blocks and matching parameters.
General proofs are in research-note.md. Finite checks are not a Lean proof.
"""
from fractions import Fraction as F
from math import isqrt
from itertools import combinations, product

def arithmetic(p,h,even):
    m=h*p-1 if even else (h*p-1)//2
    step=2*h if even else h
    t=step-2 if even else h-1
    supports=[]
    for s in range(t//2):
        coeff={}
        for j in range(p):
            for d in (s,t-s): coeff[step*j+d]=(-1)**j
        assert coeff.get(m,0)==0
        assert all(coeff.get(2*m-i,0)==v for i,v in coeff.items())
        block={i-m:v for i,v in coeff.items() if i>m}
        assert len(block)==p
        if even:
            d=h-1-s
            assert all(r%step in (d,step-d) for r in block)
            assert len({r%2 for r in block})==1
        else:
            d=(h-1)//2-s
            assert all(r%h in (d,h-d) for r in block)
            assert len({v*(-1)**r for r,v in block.items()})==1
        supports.extend(block)
    assert len(supports)==len(set(supports))
    assert set(range(1,m+1))-set(supports)==set(range(h,m+1,h))

def oddlaw(p,h):
    b=F(1,h*p-1); r=(1-(p-1)*b)/p; G=(h+p-2)//2
    assert r>0 and r<1
    if p>=5:
        K=G-1 if G%2==0 else G
        d=b*K/r
        assert 0<d<1-F(5,p*p) # stricter rational lower bound for cos(pi/p)
        assert r*d/K==b
    elif h==3:
        assert b/r<1
    else:
        k,j=divmod(G,3)
        smax=F(k*6+j*(j-1),G*(G-1)); s=2*b/r
        assert 0<s<smax
    assert (p*r-1)/(p-1)==-b

def evenlaw(p,h):
    a=F(1,2*h*p-2)
    for parity in (0,1):
        biased=(h*p)%2==parity
        g=(h//2)-(1 if h%2==0 and parity==0 else 0) if h%2==0 else (h-1)//2
        f=(p-1 if h%2==0 and parity==0 else 0) if h%2==0 else (p-1)//2
        A=p-(2 if p==5 else 3)
        if p>=11: B=f
        elif p==7: B=(4 if h%2==0 else 2) if f else 0
        else: B=(3 if h%2==0 else 2) if f else 0
        M=g*A+B; K=M-1 if M%2==0 else M
        groups=[('c',p,A,g)]+([('f',f,B,1)] if f else [])
        alpha=F(A,p); mu=-a/alpha if biased else F(0); r=F(1,2)-a/(2*alpha)
        base=F(K-1,K*K) if p in (5,7) else F(1,K)
        def edge(i,j,same):
            ti,ni,ai,gi=i; tj,nj,aj,gj=j
            al=F(ai,ni); ar=F(aj,nj)
            m1=-a/al if biased else F(0);m2=-a/ar if biased else F(0)
            r1=F(1,2)-a/(2*al);r2=F(1,2)-a/(2*ar)
            beta=F(ai*(ai-1),ni*(ni-1)) if same else al*ar
            c=base
            if p==7 and same: c+=F(1,K*(ai-1))
            if p==5:
                if same: c+=F(1,3*K) if ai==3 else F(1,K)
                elif ai==aj==3:
                    # special-mode remaining singletons = all triples + possible dummy
                    triples=g+(1 if f and B==3 else 0); L=triples+(M%2)-1
                    c+=F(1,9*K*L)
            if p==5 and same and ti=='c':
                gamma=F(1,10); T=-a/(beta*c)-(1-c)*m1*m2/c
                Y=(m1*T/2+(1-3*c)*m1**3/(6*c))/(1+m1); D=-T+Y
                P=3*c*m1*(-D-Y)+(1-3*c)*m1**3
                assert beta*(-c*D+(1-c)*m1*m2)+gamma*P/2==-a
                assert beta*c*Y-gamma*P/2==0
            else:
                D=(a/beta+(1-c)*m1*m2)/c; Y=F(0)
                assert beta*(-c*D+(1-c)*m1*m2)==-a
            probs=[D/2,D/2,(r1+m1-D)/2,(r1-m1-D)/2,(r2+m2-D)/2,(r2-m2-D)/2,1-r1-r2+D]
            assert min(probs)>=0 and sum(probs)==1
            assert abs(Y)<=probs[-1]
            cs=[(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1),(0,0)]
            for j,mm,rr in [(0,m1,r1),(1,m2,r2)]:
                assert sum(w*z[j] for w,z in zip(probs,cs))==mm
                assert sum(w*z[j]**2 for w,z in zip(probs,cs))==rr
            assert sum(w*z[0]*z[1] for w,z in zip(probs,cs))==-D
            assert al*m1==(-a if biased else 0) and ar*m2==(-a if biased else 0)
            assert 2*(al*r1+(1-al)/2)-1==-a
        for x in groups:
            if x[3]:
                edge(x,x,True)
                if x[3]>1: edge(x,x,False)
        if len(groups)==2 and g: edge(groups[0],groups[1],False)

def main():
    # Conditional three-reserve marginal check for every required fourth-root product.
    for k in range(4):
        z=[(x,y,(k-x-y)%4) for x,y in product(range(4),repeat=2)]
        for i,j in combinations(range(3),2): assert len({(w[i],w[j]) for w in z})==16
    count=0;largest=0; odd_count=even_count=0
    for p in range(3,102,2):
        if any(p%d==0 for d in range(2,isqrt(p)+1)): continue
        for ell in range(1,6):
            h=p**(ell-1)
            if p*h>10000: break
            if ell>=2:
                arithmetic(p,h,False);oddlaw(p,h);count+=1;odd_count+=1;largest=max(largest,p*h-1)
            if p==3: continue
            for k in range(1,10):
                hh=h*2**(k-1);q=2*hh*p
                if q>10000: break
                if hh>=4:
                    arithmetic(p,hh,True);evenlaw(p,hh);count+=1;even_count+=1;largest=max(largest,q-1)
    print(f'PASS: {count} finite instances ({odd_count} odd, {even_count} even); maximum N={largest}.')
    print('All relation block coefficients, pair-probability tables and target moments checked exactly.')
    print('Scope: finite checks; general proof and symbolic inequalities in companion files.')
if __name__=='__main__':main()
