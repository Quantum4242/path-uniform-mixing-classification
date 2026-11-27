# D. Column-block completion and odd semiprimes

The original note proposes that q=pr (distinct odd primes p<r) admits UAM iff q is neither 15 nor 21. It combines the spanning-tree family, new whole-column phase completion and 18 exact finite phase certificates. The negative direction is prior work. It further proposes that q=p^e r^f with e,f≥1 and r≥23 is sufficient for UAM, without a restriction on the smaller prime p.

The construction treats a whole p-coordinate column as a unit; aligned and balanced p-th roots control within-column moments, and a uniformly permuted balanced allocation controls cross-column moments. For M=kp+h, 0≤h<p, the magnitude of mean pair anticorrelation in the balanced allocation is

    [M − h(p−h)/(p−1)]/[M(M−1)],  M≥2.

The range r≥23 follows in the original note from an explicit positive-coefficient quartic after shifting r by 23. The finite certificates cover the remaining small semiprime moduli, with 236,591 full unordered eigenmode pairs checked in the original log. The two proof routes and finite certificates are complementary, not a single analytic proof of all semiprimes without data.

- [Original proof](../research-history/11-semiprime/research-note.md), [README](../research-history/11-semiprime/README.md)
- [Column inequalities and exact moments](../research-history/11-semiprime/verify_columns.py), [log](../research-history/11-semiprime/columns-verification.log)
- [Finite certificate verifier](../research-history/11-semiprime/verify_full.py), [log](../research-history/11-semiprime/verification.log)

These are historical candidate results. No claim that the later complete classification has independently validated this earlier method is made.
