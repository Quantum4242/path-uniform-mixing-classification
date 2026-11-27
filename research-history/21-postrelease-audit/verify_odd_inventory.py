"""Post-release independent odd-modulus lattice inventory audit.
Uses exact cyclotomic RREF and exhaustive free-coordinate enumeration, not
short-relation templates to generate the lattice. Tests only finite moduli.
"""
from verify_lattice import enumerate_lattice
from collections import Counter

def relevant(c):
    return sum(map(abs,c))%2==0 and sum(c) in (-2,0,2)

def triple_cycles(q):
    m=(q-1)//2; h=q//3
    result=[]
    for a in range(1,(h+1)//2):
        pos={min((a+k*h)%q,(-a-k*h)%q) for k in range(3)}
        assert len(pos)==3 and all(1<=j<=m for j in pos)
        result.append(tuple(j-1 for j in sorted(pos)))
    return result

def in_three(c, triples):
    used={i for t in triples for i in t}
    return all(c[i]==c[t[0]] for t in triples for i in t) and all(x==0 for i,x in enumerate(c) if i not in used)

def typ(c): return (sum(map(abs,c)),abs(sum(c)),tuple(sorted(abs(x) for x in c if x)))

for q in [25,35,55,65,77,85,91,39,51,57]:
    idx,allrels=enumerate_lattice(q)
    assert all(sum(map(abs,c))>4 for c in allrels if sum(map(abs,c))%2==0)
    rel={c for c in allrels if relevant(c)}
    if q%3:
        expected=Counter()
        if q%5==0:
            P=(q//5-1)//2
            if P*(P-1):expected[(10,0,(1,)*10)]=P*(P-1)
        if q==35:
            expected[(8,2,(1,)*8)]=12
            expected[(10,2,(2,)*5)]=2
        if q==55:expected[(10,2,(1,)*10)]=10
        if q==77:expected[(8,2,(1,)*8)]=2
        actual=Counter(map(typ,rel))
        assert actual==expected,(q,actual,expected)
        print('  relevant inventory matches:',dict(actual),flush=True)
    else:
        triples=triple_cycles(q)
        extras={c for c in rel if not in_three(c,triples)}
        expected=Counter()
        if q==39:expected[(8,2,(1,)*8)]=12
        actual=Counter(map(typ,extras))
        assert actual==expected,(q,actual,expected)
        print('  extra inventory matches:',dict(actual), 'three-block model relations:',len(rel)-len(extras),flush=True)
print('ALL TEN ODD MODULI: exact inventory counts PASS',flush=True)
