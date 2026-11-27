"""Independent bookkeeping checks for the final theorem's case coverage.
These checks do not prove the infinite short-relation inventory.
"""
from fractions import Fraction as F
from pathlib import Path
from sympy import isprime, factorint
here=Path(__file__).parent
exceptions=[20,28,40,50,56,70,80,98,100,110,112,130,140]
def forbidden(q):return q%15==0 or q%21==0 or (q%6==0 and q>=12)
def known(q):return bool(isprime(q) or (q%2==0 and isprime(q//2)) or (q&(q-1))==0)
def partition(q):
    if q%2 and q%3:return 'I'
    if q%2 and q%5 and q%7:return 'II'
    if q%2==0 and q%3:return 'III'
    if q==6:return 'known'
    return 'obstruction'
for q in range(3,10001):assert (partition(q)=='obstruction')==forbidden(q)
print('Arithmetic case partition checked for q=3..10000; proof is the congruence split.')
qs=[]
for q in range(4,142,2):
    if q%3==0 or known(q):continue
    if all(p>=11 for p in factorint(q) if p!=2):
        assert (q//2-1)//2>=2
    else:qs.append(q)
assert qs==exceptions
print('All 13 even finite exceptional moduli: PASS')
for q in range(142,10001,2):
    h=q//2
    assert (h-1)//2>=35
print('Group-size bound n>=35 for q>=142 (monotone formula): PASS')
rows=[s.split() for s in (here/'exact-density-margins.txt').read_text().splitlines() if s.strip()]
assert [int(row[0]) for row in rows]==exceptions
assert all(len(row)==3 and all(F(x)>0 for x in row[1:]) for row in rows)
print('All 26 recorded exact margins positive and case labels correct: PASS')
rho=F(5,21);lam=F(3,5)
assert rho-(1-rho)/2==-F(1,7) and -rho*lam==-F(1,7)
assert F(7,8)*(-F(1,7))==-F(1,8)
print('q=9 cube-root construction moments: PASS')
for q in (4,5,6,8):
    N=q-1;g=(N-1)//2;lam=1+F(1,2*N)
    assert lam<F(N,2*g) and 1-1/lam>F(1,100)
print('Known small-case ramp floors: PASS')
assert F(2,621)<F(1,200)
print('Noise bound constant: PASS')
