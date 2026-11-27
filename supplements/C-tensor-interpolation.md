# C. Cyclotomic tensor interpolation and phase matching

Write q=2^k ∏ p_j^e_j, with s distinct odd primes and p_* their minimum. The historical note proposes sufficient conditions p_*>12s+5 for odd q and p_*≥18s+5 for even q. It also supplies sharper rational tests, using

    B = ∏ p_j^(e_j−1)(p_j−6),
    α = ∏ (p_j−7)/(p_j−1),
    β = ∏ (p_j−7)(p_j−9)/((p_j−1)(p_j−3)).

For the factorization-dependent test the primes are ≥11. The odd case sets M=(B−1)/2, K=M−1 for even M and M for odd M, and requires β>K/(q−1). The even test is recorded in Theorem 1 of the original note. The important structural claim is the tensor interpolation lemma (Lemma 3): all active phases and two additional reserved phases can be assigned and then extended to the full fiber-sum and symmetry constraints. This is combined with conditional uniformity and random matching.

- [Full original theorem, lemma and proof](../research-history/10-tensor/research-note.md)
- [Interpolation verifier](../research-history/10-tensor/verify_tensor.py), [log](../research-history/10-tensor/verification.log)
- [Moment verifier](../research-history/10-tensor/verify_moments.py), [log](../research-history/10-tensor/moments.log)

The later Fourier proof claims a stronger coverage range, but the tensor interpolation framework remains a separate candidate technique. Do not state that all product-code interpolation theorems are original, or that the sufficient inequalities are necessary.
