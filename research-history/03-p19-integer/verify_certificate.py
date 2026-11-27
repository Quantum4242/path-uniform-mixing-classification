"""Pure Python exact integer arithmetic validation of a P19 integer-time certificate.
No floats, numpy, sympy, or interval library used by this verifier.
All intervals (a,b) denote [a/S,b/S].
"""
import json
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
S=10**30

def ceildiv(a,b): return -((-a)//b)
def rat(a,b=1): return (a*S//b,ceildiv(a*S,b))
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[1],-x[0]
def sub(x,y): return add(x,neg(y))
def scale(x,n): return (x[0]*n,x[1]*n) if n>=0 else scale(neg(x),-n)
def div(x,n): return x[0]//n,ceildiv(x[1],n)
def mul(x,y):
    v=[a*b for a in x for b in y]; return min(v)//S,ceildiv(max(v),S)
def absmax(x): return max(abs(x[0]),abs(x[1]))
def arctan_inv(k):
    # Alternating series: 40 terms, even count, lower bound.
    v=sum((F((-1)**j,(2*j+1)*k**(2*j+1)) for j in range(40)),F(0))
    u=v+F(1,81*k**81)
    return v.numerator*S//v.denominator,ceildiv(u.numerator*S,u.denominator)
PI=sub(scale(arctan_inv(5),16),scale(arctan_inv(239),4))
TWO_PI=scale(PI,2)
def cos_interval(x):
    # Integer shift is arbitrary: cos(x)=cos(x-2*k*pi).
    k=(x[0]+x[1]+TWO_PI[0])//(2*TWO_PI[0])
    x=sub(x,scale(TWO_PI,k)); assert absmax(x)<=4*S
    xx=mul(x,x); term=rat(1); total=term
    for j in range(1,31):
        term=neg(div(mul(term,xx),(2*j-1)*(2*j)))
        total=add(total,term)
    # Taylor through degree 60 (also degree 61 as odd coefficients vanish).
    # remainder <=4^62/62! < 1/S, checked exactly.
    import math
    assert 4**62*S < math.factorial(62)
    return total[0]-1,total[1]+1

def reduce_poly(a):
    a=list(a)+[0]*max(0,16-len(a))
    for k in range(len(a)-1,15,-1):
        v=a[k]; a[k]=0
        for off,sign in [(4,1),(8,-1),(12,1),(16,-1)]: a[k-off]+=sign*v
    return tuple(a[:16])

def theta_vectors():
    # Reduce X^r+X^(-r) mod Phi40. The polynomial identity also
    # proves equality of grouped gaps when evaluated at exp(i*pi/20).
    def reduce_power(j):
        a=[0]*40; a[j%40]=1
        for k in range(39,15,-1):
            v=a[k]; a[k]=0
            for off,sign in [(4,1),(8,-1),(12,1),(16,-1)]: a[k-off]+=sign*v
        return a[:16]
    return {r:tuple(a+b for a,b in zip(reduce_power(r),reduce_power(-r))) for r in range(40)}
def gap_pairs():
    th=theta_vectors(); reps={}
    for r,s in combinations(range(1,20),2):
        key=tuple(a-b for a,b in zip(th[r],th[s])); target= -1 if (r-s)%2==0 else 0
        if key in reps: assert reps[key][2]==target
        else: reps[key]=(r,s,target)
    assert len(reps)==90
    return list(reps.values())

def verify_mixing_identity():
    # 40 times the sine spectral projector entry equals this polynomial.
    from functools import lru_cache
    th=theta_vectors()
    @lru_cache(None)
    def square(v):
        a=[0]*31
        for i,vi in enumerate(v):
            for j,vj in enumerate(v): a[i+j]+=vi*vj
        return reduce_poly(a)
    for k in range(1,20):
        for l in range(1,20):
            fs=[tuple(a-b for a,b in zip(th[(r*(k-l))%40],th[(r*(k+l))%40])) for r in range(1,20)]
            groups=[tuple(sum(f[j] for f in fs[i::2]) for j in range(16)) for i in (0,1)]
            squares=[square(f) for f in fs]
            g0,g1=map(square,groups)
            val=tuple(20*sum(f[j] for f in squares)-g0[j]-g1[j] for j in range(16))
            assert val==(1600,)+(0,)*15,(k,l,val)
    print('PASS: 361 exact mixing identities in Z[X]/(Phi40).')

def verify(path):
    data=json.loads(Path(path).read_text()); times=data['times']; D=data['denominator']; R=data['inverse_numerators']; w=data['weight_numerators']; n=91
    assert D==10**12 and len(times)==n and len(set(times))==n and all(type(t)==int and t>=0 for t in times)
    assert len(R)==n and all(len(row)==n and all(type(v)==int for v in row) for row in R)
    assert len(w)==n and all(type(v)==int and v>0 for v in w)
    pairs=gap_pairs(); th={r:scale(cos_interval(div(scale(PI,r),20)),2) for r in range(1,20)}
    B=[[rat(1)]*n]+[[cos_interval(scale(sub(th[r],th[s]),t)) for t in times] for r,s,_ in pairs]
    b=[rat(1)]+[rat(t,19) for _,_,t in pairs]
    # All interval products computed with integer coefficients, then divide by D once.
    def dot_int(a,x):
        lo=hi=0
        for k,v in zip(a,x):
            p,q=scale(v,k); lo+=p; hi+=q
        return div((lo,hi),D)
    cols=list(zip(*B)); defect=0
    for i,row in enumerate(R):
        defect=max(defect,sum(absmax(sub(rat(int(i==j)),dot_int(row,col))) for j,col in enumerate(cols)))
    residual=[sub(bi,dot_int(w,row)) for bi,row in zip(b,B)]
    corr=max(absmax(dot_int(row,residual)) for row in R)
    assert defect<S
    # Exact Neumann-series bound on |w_exact - w_approx|_infty.
    err=F(corr,S-defect)
    assert F(min(w),D)>err
    print('PASS: all 171 pair targets consistent with 90 exact gap groups')
    print('PASS: exact interval enclosure for 91 x 91 matrix')
    print('||I-RB||_inf <=',F(defect,S))
    print('||R(b-Bw0)||_inf <=',F(corr,S))
    print('||w_exact-w0||_inf <=',err)
    print('min(w0) =',F(min(w),D))
    # Readable rational conservative bounds, checked without floats.
    assert defect*10**8<S
    assert err<F(1,10**8)
    assert defect*10**10<2*S
    assert err<F(5,10**13)
    assert F(min(w),D)-err>F(6,10000)
    assert all(t<2000 for t in times)
    verify_mixing_identity()
    print('Certified bounds: defect < 2e-10, weight error < 5e-13, min(w_exact) > 0.0006.')
    print('PASS: B invertible; exact w=B^-1 b has all weights strictly positive and sum 1.')
if __name__=='__main__': verify(Path(__file__).with_name('certificate.json'))
