# A. Random matching and prime-power odd part

## Archived results

For an odd prime p, the earlier note proposes the classification for q=4p: UAM on P_(4p−1) iff p≥5, with at most 4p²−2p+1 integer readout times. The negative case p=3 follows from Kang. A single signed relation among the p odd positive-energy coordinates is the key arithmetic input. Random pairs of fourth roots create negative correlation; three reserve variables enforce the product constraint without changing conditional pairwise moments. The p=5 case uses a separate finite pattern law.

The next note treats q=2^k p^ell (k≥0, ell≥1, p odd) and powers of two. Its candidate classification excludes exactly 6|q with q≥12 within this class. The arithmetic decomposes into disjoint signed parity-check blocks; odd moduli use root-of-unity clusters and even moduli use random matching and reserve coordinates. Support bounds in the notes are upper bounds, not minima. The q=9 existence result is prior work.

## Primary records and verification

- [4p original proof](../research-history/07-4p/research-note.md), [exact moment script](../research-history/07-4p/verify_moments.py), [historical log](../research-history/07-4p/verification.txt).
- [Prime-power original proof](../research-history/08-prime-power/research-note.md), [README and reproduction instructions](../research-history/08-prime-power/README.md), [finite test log](../research-history/08-prime-power/finite.log), [matching enumeration](../research-history/08-prime-power/matching-enumeration.log), [p=5 polynomial checks](../research-history/08-prime-power/p5-polynomials.log).

## Assessment

Both are earlier candidate proofs with exact arithmetic support, not formalized or independently reviewed. Their existence ranges are subsumed by the main candidate classification, but the block-wise matching construction is an alternative approach to constrained phase laws and should be retained separately. A failed sufficient bound is not an obstruction.
