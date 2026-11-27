import numpy as np
from scipy.optimize import linprog
from scipy.linalg import qr
from explore import data
import time,sys
q=int(sys.argv[1]); ns=int(sys.argv[2]) if len(sys.argv)>2 else 3000
V,orbits=data(q); m=len(V); d=V.shape[1]; rng=np.random.default_rng(q)
seeds=rng.integers(0,4,(ns,d),dtype=np.int64); phase=(seeds@V.T)%4
cos=np.array([1,0,-1,0]); rows=[np.ones(ns,dtype=np.int64)]; rhs=[q-2]; sigs=[None]
seen={}
for s,orb in orbits:
    # normalized character signature (exact integer coefficients mod 4, even under inversion)
    from collections import Counter
    from fractions import Fraction
    C=Counter()
    for i,j in orb:
        v=(V[i]+s*V[j])%4; k=min(v.tobytes(),((-v)%4).tobytes()); C[k]+=1
    sig=tuple(sorted((k,Fraction(v,len(orb))) for k,v in C.items()))
    tar=Fraction(-1 if s==-1 else 0,q-2)
    if sig in seen:
        assert seen[sig]==tar
        continue
    seen[sig]=tar
    i,j=np.array(orb).T; rows.append(cos[(phase[:,i]+s*phase[:,j])%4].sum(axis=1)); rhs.append(-len(orb) if s==-1 else 0); sigs.append((s,orb))
A=np.array(rows); b=np.array(rhs)/(q-2); print(q,'rows',len(rows),'ns',ns,flush=True)
scale=np.maximum(1,np.max(abs(A),axis=1)); F=A/scale[:,None]; g=b/scale
print('start LP',flush=True)
res=linprog(np.zeros(ns),A_eq=F,b_eq=g,bounds=(0,None),method='highs-ipm',options={'time_limit':35})
print(res.message,flush=True)
if res.success:
 idx=np.where(res.x>1e-10)[0]; print('support',len(idx),'min',min(res.x[idx]),'err',max(abs(A@res.x-b)),flush=True); np.savez(f'q{q}-lp.npz',A=A[:,idx],bnum=np.array(rhs),seeds=seeds[idx],weights=res.x[idx]); print('saved',flush=True)
else:
 print('rank',np.linalg.matrix_rank(F),flush=True)
