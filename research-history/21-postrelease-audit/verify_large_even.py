"""Compare independently enumerated lattices against template generator
at moduli outside the finite exceptions of the published theorem."""
from verify_lattice import enumerate_lattice
from verify_small_density import relations
for q in (154,170,182,196,242):
    for b in (0,1):
        idx,actual=enumerate_lattice(q,b)
        expected=relations(q,idx)
        assert actual==expected,(q,b,len(actual-expected),len(expected-actual))
        assert all(sum(map(abs,c))>4 for c in actual)
        print('  independent exhaustive list MATCH',flush=True)
print('ALL TEN LARGE EVEN GROUPS: PASS',flush=True)
