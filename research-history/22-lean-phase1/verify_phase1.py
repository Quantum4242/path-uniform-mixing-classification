#!/usr/bin/env python3
"""Exact source-level cross-check. This is NOT a Lean compiler or proof checker.
Requires SymPy. Compare actual Lean polynomial text with the released DP formulas.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as Q
import re
import sympy as s

root = Path(__file__).resolve().parent
source = (root/'PathPositivity.lean').read_text(encoding='utf-8')
n,x = s.symbols('n x')
def parse(expr):
    return s.sympify(expr.replace('^','**'), locals={'n':n,'x':x})
def read_def(name):
    m = re.search(r'^def '+name+r' \(n : ℝ\) : ℝ :=\n  (.+)$', source, re.M)
    assert m, name
    return parse(m[1])

def check_shift(name, formula, start):
    m = re.search(r'^theorem '+name+r'\b[\s\S]*?\n    0 < (.+) := by positivity$',source,re.M)
    assert m, name
    p = s.Poly(parse(m[1]),x)
    assert s.expand(p.as_expr() - formula.subs(n,x+start)) == 0, name
    assert p.eval(0)>0 and all(c>=0 for c in p.all_coeffs()), name
    print(name, 'shifted polynomial identity and positivity: PASS')

# From released detailed-proof.md, Part III §3 (common denominator 4*n^4).
Z0 = 2*n*(121704774*n**3-4750735*n**2+11341862*n-18628995)
U0 = -8*(9427103*n**3+9607186*n**2-29923359*n+64354710)
D0 = -2*(37705166*n**3+15783578*n**2-43863387*n+51483768)
Z1 = 243409548*n**4-47209882*n**3+26186325*n**2-7941564*n+16129
U1 = -4*(18854206*n**3+6845765*n**2-40652319*n+60741814)
D1 = -2*(37705166*n**3+498483*n**2-25384760*n+18516092)
W1 = -4*(18854206*n**3+5639384*n**2-32204787*n+28870910)
e0 = 12*(4583117*n**3+117542015*n**2+6833118795*n+18802301105)
e1 = 12*(25968783*n**3+323062731*n**2+7159146083*n+22249229695)
odd = 56376*n**4-362232*n**3+2688102*n**2-7757169*n-1057681
extra = odd-24917760*(3*n+1)-2257920
for name,p in [('Z0',Z0),('U0',U0),('D0',D0),('Z1',Z1),('U1',U1),('D1',D1),('W1',W1),('errNum0',e0),('errNum1',e1),('oddSlack',odd),('oddSlackExtra',extra)]:
    assert s.expand(read_def(name)-p)==0, name
print('11 Lean definitions match DP formulas exactly: PASS')
check_shift('odd_three_base',odd,4)
check_shift('odd_three_extra',extra,16)
check_shift('even_err0_num',14500000*n**4-e0,35)
check_shift('even_err1_num',14500000*n**4-e1,35)
for sg,tag in [(1,'p'),(-1,'m')]:
    check_shift('base0_'+tag,-(4*n-1)*U0-Z0-2*n*sg*(U0-D0)-58000000*n**4,2)
for (sg,a),(sh,b) in product([(1,'p'),(-1,'m')],repeat=2):
    check_shift('base1_'+a+b,-(4*n+1)*U1-Z1-2*n*(sg*(U1-D1)+sh*(U1-W1))-58000000*n**4,2)
check_shift('odd0_gap_num',3*(2568*n**2-5782*n+15435),3)
check_shift('odd0_non35_error_num',160*n**4-56448*n**2-1451520*n-4233600,27)
check_shift('odd0_mult35_error_num',25*n**4-56448*n**2-11007360*n-4572288,87)
assert Q(31239432,83521)<Q(5397327,4913)
assert Q(42831862673,172470272)>0 and Q(9760481,130321)>0
print('3 exceptional exact fraction inequalities: PASS')

# Exhaustive independent check over the necessary axis L1 bound for central 35.
def axes(k,budget):
    if not k:
        yield ()
    else:
        for a in range(-budget,budget+1):
            for rest in axes(k-1,budget-abs(a)):
                yield (a,)+rest

def sym_col(a,b,c): return abs(c)+2*abs(a+c)+2*abs(b+c)
def anti_col(a,b,c): return abs(c)+abs(a+c)+abs(a-c)+abs(b+c)+abs(b-c)
count=0
sym,anti=Counter(),Counter()
for a,b,c,d,e in axes(5,10):
    count+=1
    cs=(c,d,e)
    sw=abs(a)+abs(b)+sum(sym_col(a,b,j) for j in cs)
    aw=abs(a)+abs(b)+sum(anti_col(a,b,j) for j in cs)
    if sw<=10 and a!=b:
        assert abs(a)+abs(b)==1 and all(j in (0,-a-b) for j in cs)
    if sw<=10 and a==b and a:
        dev=sum(abs(a+j) for j in cs)
        assert (abs(a)==1 and dev<=1) or (abs(a)==2 and dev==0)
    if not ((a or b) and (c or d or e)):continue
    if sw<=10:
        v=[a,b,*cs]+[i+j for i in (a,b) for j in cs for _ in range(2)]
        sym[tuple(sorted(abs(i) for i in v if i))]+=1
    if aw<=10:
        assert abs(a)+abs(b)==1 and sum(map(abs,cs))==1
        v=[a,b,*cs]+[k for i in (a,b) for j in cs for k in (i+j,i-j)]
        anti[tuple(sorted(abs(i) for i in v if i))]+=1
assert count==36365
assert sym==Counter({(2,)*5:2,(1,)*8:18,(1,)*5:2,(1,)*8+(2,):6,(1,)*9:12,(1,)*10:4})
assert anti==Counter({(1,)*8+(2,):24})
print(f'35 central axes: {count} vectors, symmetric 44 / antisymmetric 24; structural conditions PASS')

# Every paired size is at most 8, since z>=4 and sum of the five sizes<=8.
patterns=[]
for sizes in product((1,4,5,6,7,8),repeat=5):
    z=20-2*sum(sizes)
    if z>=4:
        assert (z==10 and sizes==(1,)*5) or (z==4 and sorted(sizes)==[1,1,1,1,4])
        patterns.append((z,sizes))
assert len(patterns)==6
print('385 slice support: six ordered patterns, two up to permutation: PASS')
for a,b,c,d,e in product(range(3),range(3),range(-1,2),range(-1,2),range(-1,2)):
    weight=abs(a-1)+abs(b-1)+sum(sym_col(a,b,j) for j in (c,d,e))
    assert weight!=5
print('385 last slice: 243 tuples, no entry bound needed: PASS')
print('SOURCE-LEVEL CHECKS PASSED. Lean kernel compilation NOT performed.')
