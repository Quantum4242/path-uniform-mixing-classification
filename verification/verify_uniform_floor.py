#!/usr/bin/env python3
"""Exact rational/symbolic checks for the uniform Haar floor.
Input formulas from the revised unified manuscript, not numerical fits.
No floating point operations in any assertion.
"""
import sympy as s
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
n,b,x=s.symbols('n b x', real=True)

def positive(f,var,start,label):
    num,den=s.fraction(s.cancel(f))
    pn=s.Poly(num.subs(var,x+start),x); pd=s.Poly(den.subs(var,x+start),x)
    if pd.LC()<0: pn=-pn;pd=-pd
    assert pn.eval(0)>0 and all(a>=0 for a in pn.all_coeffs()),(label,pn)
    assert pd.eval(0)>0 and all(a>=0 for a in pd.all_coeffs()),(label,pd)
    print(label, 'PASS',flush=True)

c=s.Rational(1,100)
# Part I uses the earlier uniform 1/50 floor.
# Part II: verify the floor in the two all-parameter branches.
m=3*b+1
Z=(335016*b**4+414504*b**3+122490*b**2+126705*b+2209)/m**4
U=-8*(8154*b**3+9171*b**2+21603*b-14243)/m**4
V=-24*(2718*b**3+1857*b**2+11035*b-21989)/m**4
W=-8*(8154*b**3+9171*b**2+21015*b-13655)/m**4
T=-2*m*V; G=T-Z; E=6*b*(2*V-U-W)
extra=24917760/m**3+2257920/m**4
positive(T,b,4,'odd three-block normalization')
positive(G-E-c*T,b,4,'odd three-block with no extra relations, floor 1/100')
positive(G-E-extra-c*T,b,16,'odd three-block with extra relations, floor 1/100')
for q,margin in [(33,s.Rational(42831862673,172470272)),(39,s.Rational(9760481,130321))]:
    val=margin/T.subs(b,(q//3-1)//2);assert val>c
    print('odd exception q=',q,'floor ratio=',val,'PASS')
# q=9: Haar weight 1/8. q=3 is pure Haar.
assert s.Rational(1,8)>c

def even_moments(bias):
    if bias==0:
        Z=(121704774*n**3-4750735*n**2+11341862*n-18628995)/(2*n**3)
        U=-2*(9427103*n**3+9607186*n**2-29923359*n+64354710)/n**4
        D=-(37705166*n**3+15783578*n**2-43863387*n+51483768)/(2*n**4);W=s.S(0)
        B=12*(4583117*n**3+117542015*n**2+6833118795*n+18802301105)/n**4
    else:
        Z=(243409548*n**4-47209882*n**3+26186325*n**2-7941564*n+16129)/(4*n**4)
        U=-(18854206*n**3+6845765*n**2-40652319*n+60741814)/n**4
        D=-(37705166*n**3+498483*n**2-25384760*n+18516092)/(2*n**4)
        W=-(18854206*n**3+5639384*n**2-32204787*n+28870910)/n**4
        B=12*(25968783*n**3+323062731*n**2+7159146083*n+22249229695)/n**4
    return Z,U,D,W,B
for bias in [0,1]:
    Z,U,D,W,B=even_moments(bias)
    N=4*n+1 if bias else 4*n-1
    positive(-U,n,2,f'even b={bias} negative U')
    # At fixed n, increasing N increases (1-c)(-NU)-Z-corrections.
    for sg,sh in product([-1,1],repeat=2):
        f=(1-c)*(-N*U)-Z-2*n*(sg*(U-D)+sh*(bias*U-W))
        positive(f,n,2,f'even b={bias} signs={sg,sh}, no relations floor 1/100')
        positive(f-B,n,35,f'even b={bias} signs={sg,sh}, general floor 1/100')
# Each exact finite-case lower bound is read from the previously verified table.
path=Path(__file__).parent/'exact-density-margins.txt'
for line in path.read_text().splitlines():
    q,*margins=line.split();q=int(q)
    for bias,margin in enumerate(margins):
        size=sum((r%2==(q//2)%2)==bool(bias) for r in range(1,q//2))
        U=even_moments(bias)[1].subs(n,size)
        val=s.Rational(margin)/(-(q-1)*U)
        assert val>c,(q,bias,val)
        print('even exception',q,bias,'floor ratio=',val,'PASS')
# q=4,5,6,8 use known ramp; choose lambda=1+1/(2N), valid since 2g<=N-1.
for q in [4,5,6,8]:
    N=q-1;g=(N-1)//2;lam=1+s.Rational(1,2*N)
    assert lam<s.Rational(N,2*g) and 1-1/lam>c
print('ALL PER-GROUP FLOOR ASSERTIONS PASS (1/100); direct product gives 1/10000')
# The stronger joint floor is obtained analytically by removing c from each
# factor, scaling each same-parity moment, then restoring c times global Haar.
# This is not the product of the original two densities.
assert (1-c)*s.Rational(100,99)==1
assert s.Rational(2,621)<c/2
print('rescaled joint floor 1/100 and timing-noise bound: exact constants PASS')
