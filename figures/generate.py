from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np
from sympy import isprime
root=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.fonttype':'none','figure.dpi':150})
def save(fig,name):
 for ext in ('pdf','svg','png'):fig.savefig(root/'figures'/f'{name}.{ext}',bbox_inches='tight',dpi=180)
 plt.close(fig)
def category(q):
 if q%15==0 or q%21==0 or (q%6==0 and q>=12): return 0
 if isprime(q) or (q%2==0 and isprime(q//2)) or q&(q-1)==0:return 1
 return 2
fig,ax=plt.subplots(figsize=(9.4,4.3));Q=np.arange(3,213).reshape(14,15)
ax.imshow(np.vectorize(category)(Q),cmap=ListedColormap(['#d9dee4','#7ca0b6','#157f78']),vmin=0,vmax=2,aspect='auto')
for i in range(14):
 for j in range(15):ax.text(j,i,str(Q[i,j]),ha='center',va='center',fontsize=7.8,color='white' if category(Q[i,j])==2 else '#182634')
ax.set_xticks([]);ax.set_yticks([]);ax.set_title('Arithmetic classification for $3\u2264q\u2264212$ (illustration)',loc='left',fontweight='bold',pad=10)
for s in ax.spines.values():s.set_visible(False)
ax.legend(handles=[Patch(facecolor='#d9dee4',label='Known obstruction'),Patch(facecolor='#7ca0b6',label='Known existence'),Patch(facecolor='#157f78',label='Candidate new existence')],ncol=3,loc='upper center',bbox_to_anchor=(.5,-.04),frameon=False,fontsize=9)
save(fig,'classification')
rows=[l.split() for l in (root/'verification'/'exact-density-margins.txt').read_text().splitlines() if l.strip()]
q=[int(r[0]) for r in rows]; y=np.array([[float(Fraction(s))/1e6 for s in r[1:]] for r in rows]); x=np.arange(len(q));fig,ax=plt.subplots(figsize=(8.7,3.7));ax.bar(x-.18,y[:,0],width=.36,color='#487eaa',label='Group $b=0$');ax.bar(x+.18,y[:,1],width=.36,color='#157f78',label='Group $b=1$');ax.set_xticks(x,q);ax.set_xlabel('Modulus $q$');ax.set_ylabel('Certified lower bound ($10^6$)');ax.set_title('Unnormalized density margins: 13 finite even cases',loc='left',fontweight='bold');ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True);ax.legend(frameon=False);save(fig,'finite-margins')

# Chinese companion figures, with identical data and independent captions.
from matplotlib.font_manager import FontProperties, findfont
import os
font_path=os.environ.get('CJK_FONT')
if not font_path:
 for family in ('Noto Sans CJK SC','Noto Sans CJK JP','Microsoft YaHei','SimHei'):
  try:
   font_path=findfont(FontProperties(family=family),fallback_to_default=False); break
  except ValueError:
   pass
if not font_path and Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc').is_file():
 font_path='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
if not font_path:
 print('CJK font unavailable; retaining shipped Chinese plots. Set CJK_FONT to regenerate.')
if font_path:
 fp=FontProperties(fname=font_path)
 fig,ax=plt.subplots(figsize=(9.4,4.3));ax.imshow(np.vectorize(category)(Q),cmap=ListedColormap(['#d9dee4','#7ca0b6','#157f78']),vmin=0,vmax=2,aspect='auto')
 for i in range(14):
  for j in range(15):ax.text(j,i,str(Q[i,j]),ha='center',va='center',fontsize=7.8,color='white' if category(Q[i,j])==2 else '#182634')
 ax.set_xticks([]);ax.set_yticks([]);ax.set_title('算术分类示意：q = 3–212',loc='left',fontproperties=fp,fontweight='bold',pad=10)
 for s in ax.spines.values():s.set_visible(False)
 ax.legend(handles=[Patch(facecolor='#d9dee4',label='已知不存在'),Patch(facecolor='#7ca0b6',label='已知存在'),Patch(facecolor='#157f78',label='候选新增存在')],ncol=3,loc='upper center',bbox_to_anchor=(.5,-.04),frameon=False,prop=fp)
 save(fig,'classification-zh')
 fig,ax=plt.subplots(figsize=(8.7,3.7));ax.bar(x-.18,y[:,0],width=.36,color='#487eaa',label='组 b=0');ax.bar(x+.18,y[:,1],width=.36,color='#157f78',label='组 b=1');ax.set_xticks(x,q);ax.set_xlabel('模数 q',fontproperties=fp);ax.set_ylabel('严格下界（百万）',fontproperties=fp);ax.set_title('13 个偶数特殊模数的非归一化正性裕量',loc='left',fontproperties=fp,fontweight='bold');ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True);ax.legend(frameon=False,prop=fp);save(fig,'finite-margins-zh')
