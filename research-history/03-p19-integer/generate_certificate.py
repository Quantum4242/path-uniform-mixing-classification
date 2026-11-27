"""Exploratory numerical search only. The exact verifier does not trust this script."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from verify_certificate import gap_pairs
pairs=gap_pairs(); theta=2*np.cos(np.arange(1,20)*np.pi/20)
f=np.array([theta[r-1]-theta[s-1] for r,s,_ in pairs]); b=np.r_[1.,[v/19 for _,_,v in pairs]]
t=np.arange(2000); A=np.vstack([np.ones(len(t)),np.cos(f[:,None]*t)])
res=linprog(np.zeros(len(t)),A_eq=A,b_eq=b,bounds=(0,None),method='highs'); assert res.success
sel=np.flatnonzero(res.x>1e-10); assert len(sel)==91
B=A[:,sel]; w=np.linalg.solve(B,b); R=np.linalg.inv(B); D=10**12
assert min(w)>0
out={'times':sel.tolist(),'denominator':D,'inverse_numerators':np.rint(R*D).astype('int64').tolist(),'weight_numerators':np.rint(w*D).astype('int64').tolist()}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('91 integer times; min weight',min(w),'condition number',np.linalg.cond(B))
