import sympy as S
from fractions import Fraction as Q
g=S.symbols('g', real=True)

def setup(case):
 if case=='even_even': return 1/(20*g-2),3*g-1, g-1, S.Rational(3,4),S.Rational(1,2),S.Rational(1,1)/3
 if case=='even_odd': return 1/(20*g-2),3*g, g, S.Rational(3,4),S.Rational(1,2),S.Rational(1,1)/3
 if case=='odd': return 1/(20*g+8),3*g+1,g-1,S.Integer(1),S.Integer(1),S.Integer(1)

def calc(case,biased):
 a,K,L,alphaF,betaF,freeIn=setup(case); alpha=S.Rational(3,5); beta=S.Rational(3,10); gamma=S.Rational(1,10)
 mu=-a/alpha if biased else 0; mf=-a/alphaF if biased else 0
 r=S.Rational(1,2)-a/(2*alpha); rf=S.Rational(1,2)-a/(2*alphaF)
 base=(K-1)/K**2; s=base+1/(3*K); cross=base+1/(9*K*L); crossF=cross if case.startswith('even') else base; sf=base+freeIn/K
 T=-a/(beta*s)-(1-s)*mu**2/s
 Y=(mu*T/2+(1-3*s)*mu**3/(6*s))/(1+mu); D=-T+Y
 Dcc=(a/alpha**2+(1-cross)*mu**2)/cross
 Dcf=(a/(alpha*alphaF)+(1-crossF)*mu*mf)/crossF
 Dff=(a/betaF+(1-sf)*mf**2)/sf
 # all denominators need positive, true for valid g and mu.
 return { 'D_same_nonneg':D, 'D_same_margin':r+mu-D, 'Y_nonneg':Y, 'Y_mass':1-2*r+D-Y,
 'cross_cc_margin':r+mu-Dcc,'cross_cf_margin':r+mu-Dcf,'free_same_margin':rf+mf-Dff }

for case,minG in [('even_even',2),('even_odd',5),('odd',2)]:
 for biased in [False,True]:
  print(case,biased)
  for name,x in calc(case,biased).items():
   if case=='even_even' and minG==2 and biased and name=='cross_cc_margin':
    # with g=2 even parity only 1 constrained block. g>=4 for two or more in biased group
    start=4
   else:start=minG
   num,den=S.fraction(S.factor(S.cancel(x)))
   np=S.Poly(num.subs(g,g+start),g);dp=S.Poly(den.subs(g,g+start),g)
   if dp.LC()<0: np=-np;dp=-dp
   ok=all(v>=0 for v in np.all_coeffs()+dp.all_coeffs()) and dp.TC()>0
   print(name, 'g>=',start,ok,'deg',np.degree(),dp.degree(),'min',min(np.all_coeffs()),min(dp.all_coeffs()), 'val',float(x.subs(g,start)))
   if not ok: print('NUM',np.as_expr(),'DEN',dp.as_expr())
   assert ok, (case,biased,name)

print("PASS: all 42 shifted numerator/denominator coefficient checks.")
