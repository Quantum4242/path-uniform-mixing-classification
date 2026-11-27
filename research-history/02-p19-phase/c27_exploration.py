import numpy as np
from scipy.optimize import least_squares
from sympy import symbols, cyclotomic_poly, rem, Poly, Matrix
x=symbols('x'); n=27;p=cyclotomic_poly(n,x)
R=Matrix([[Poly(rem(x**j+x**((-j)%n),p,x),x).nth(k) for j in range(14)] for k in range(18)])
_, piv=R.rref(); B=R[:,list(piv)].gauss_jordan_solve(R)[0].T
print('piv',piv,'B',B,flush=True)
B=np.array(B,dtype=float); B=B[np.minimum(np.arange(n),(-np.arange(n))%n)]
F=np.exp(2j*np.pi*np.outer(np.arange(14),np.arange(n))/n)/np.sqrt(n)
def fun(t):
 z=np.exp(1j*B@t); a=F@z; return abs(a)**2-1
rng=np.random.default_rng(27);best=100
for i in range(100):
 sol=least_squares(fun,rng.uniform(-np.pi,np.pi,9),max_nfev=400,ftol=1e-12,gtol=1e-12,xtol=1e-12)
 err=np.linalg.norm(sol.fun)
 if err<best:
  best=err;print(i,err, np.round((B@sol.x/(2*np.pi))%1,8),flush=True)
  if err<1e-9:break
