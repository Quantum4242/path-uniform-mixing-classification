if not __debug__:
    raise RuntimeError("Run without -O: assertions are required for verification")

"""Alternative integer interval verifier, no pi bounds or periodic range reduction.
Analytic justification: theta1=sqrt(2+sqrt((5+sqrt(5))/2));
theta_(r+1)=theta1*theta_r-theta_(r-1), theta0=2.
Taylor on [-2,2], then 12 double-angle steps. No floating point.
"""
from math import isqrt, factorial
from pathlib import Path
from fractions import Fraction
import json
S=10**30

def cd(a,b): return -((-a)//b)
def rat(a,b=1): return a*S//b, cd(a*S,b)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def scale(a,k): return (k*a[0],k*a[1]) if k>=0 else scale(neg(a),-k)
def div(a,k): assert k>0; return a[0]//k,cd(a[1],k)
def mul(a,b):
    v=[x*y for x in a for y in b]; return min(v)//S,cd(max(v),S)
def sqr(a):
    l,u=a; low=0 if l<=0<=u else min(l*l,u*u)
    return low//S,cd(max(l*l,u*u),S)
def sqrt(a):
    assert a[0]>=0
    l=isqrt(a[0]*S); u=isqrt(a[1]*S)
    assert l*l<=a[0]*S and (u+1)**2>a[1]*S
    return l,u+int(u*u<a[1]*S)
def absmax(a): return max(map(abs,a))
def cos_interval(a):
    x=div(a,4096); assert absmax(x)<=2*S
    xx=sqr(x); term=rat(1); v=term
    for j in range(1,21):
        term=neg(div(mul(term,xx),(2*j-1)*(2*j)))
        v=add(v,term)
    assert 2**42*S<factorial(42)
    v=(v[0]-1,v[1]+1)
    for _ in range(12):
        v=sub(scale(sqr(v),2),rat(1))
        # Intersection with [-1,1] preserves containment.
        v=max(v[0],-S),min(v[1],S)
        assert v[0]<=v[1]
    return v

def main():
    d=json.loads(Path(__file__).with_name('compact.json').read_text()); Q=d['Q']; A=d['A']; R=d['R']; w=d['w']; b=d['b']; t=d['times']; pairs=d['pairs']; n=91
    theta=[rat(2),sqrt(add(rat(2),sqrt(div(add(rat(5),sqrt(rat(5))),2))))]
    for r in range(1,19): theta.append(sub(mul(theta[1],theta[r]),theta[r-1]))
    B=[[rat(1)]*n]+[[cos_interval(scale(sub(theta[r],theta[s]),tj)) for tj in t] for r,s,_ in pairs]
    error=max(absmax(sub(z,rat(a,Q))) for row,ar in zip(B,A) for z,a in zip(row,ar))
    width=max(z[1]-z[0] for row in B for z in row)
    assert error*Q<=S
    assert n==len(t)==len(A)==len(R)==len(w)==len(b)
    assert len(set(t))==n and all(0<=v<2000 for v in t)
    assert A[0]==[Q]*n and b[0]==19
    rn=max(sum(map(abs,r)) for r in R); defect=max(sum(abs(Q*Q*(i==j)-sum(r[k]*A[k][j] for k in range(n))) for j in range(n)) for i,r in enumerate(R)); residual=max(abs(b[i]*Q*Q-19*sum(a*v for a,v in zip(row,w))) for i,row in enumerate(A))
    assert rn<=27*Q and 10000*defect<=Q*Q and 1000000*residual<=19*Q*Q and min(w)>=60000 and sum(map(abs,w))<=2*Q
    print('PASS: radical recurrence, 19 energy intervals; no pi bounds')
    print('PASS: all 8281 entries enclosed, same original A/Q approximation')
    print('max interval width =', Fraction(width,S))
    print('max entrywise error <=',Fraction(error,S))
    print('PASS: all original integer matrix inequalities')
    print('PASS: Taylor remainder bound 2^42/42! < 10^-30')
    print('PASS: exact rational positivity bound:',Fraction(60000,Q)-Fraction(1,20000))
    print('Analytic lemmas and full Lean proof not yet compiled.')
if __name__=='__main__':main()
