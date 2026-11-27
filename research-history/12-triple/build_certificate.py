"""Discovery only. The separate verifier uses no floating point."""
import numpy as np,sys,json
from pathlib import Path
for q in map(int,sys.argv[1:]):
 f=np.load(f'q{q}-lp.npz'); A=f['A']; b=f['bnum']; seeds=f['seeds']; w=f['weights']; n=len(w); assert A.shape==(n,n)
 # Refine the LP approximate weights before constructing rational certificate.
 R=np.linalg.inv(A.astype(float)); w=R@(b/(q-2)); Q=10**12
 Ri=np.rint(Q*R).astype(np.int64); ui=np.rint(Q*w).astype(np.int64)
 print(q, 'min weight',w.min(),'max inverse entry',abs(R).max(),flush=True)
 assert max(abs(A).flat)*int(abs(Ri).max())*n<2**62
 D=Q*np.eye(n,dtype=np.int64)-Ri@A
 print('defect scaled',np.abs(D).sum(axis=1).max(), 'max R row sum',np.abs(Ri).sum(axis=1).max(),flush=True)
 assert w.min()>0
 out={'q':q,'Q':Q,'seeds':seeds.tolist(),'R':Ri.tolist(),'u':ui.tolist()}
 Path(f'q{q}.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
