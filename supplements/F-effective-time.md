# F. Effective finite readout windows

This supplement recovers the previously omitted quantitative time-window theorems. Unlike qualitative existence on a prescribed algebraic-step grid, these give finite search bounds, under explicit hypotheses. They are not efficient numerical algorithms or experimentally useful time scales.

## F.1 General interior-margin theorem

Let m=floor(N/2) count nonzero energy pairs, d count distinct positive gaps, D=φ(2q)/2, and C be the convex hull of the cosine moment map on the spectral phase orbit closure. Suppose the target y has an explicit interior radius r>0, meaning the open ℓ¹ ball B₁(y,r) lies in C. Choose 0<η≤1 with 2dη≤r/2, and a positive integer K satisfying

    Kη²/4 > m log(2K+1)+log 4.

Put W=2mK, δ=1/W, L=16 W^D (2K+1)^m. Then the historical theorem gives B₁(y,r/2) inside the convex hull of the finite grid {t₀+jδ : 0≤j<L}, for t₀≥0. In particular at most d+1 samples suffice, and the latest sample is at most t₀+(L−1)/W.

The proof uses a localized product Fourier kernel, cyclotomic algebraic-integer norm bounds, finite geometric sums and convex separation. Its conditional nature is essential: it does not prove the required margin for any new q by itself. The bound is for the chosen fine rational step, not an effective bound for an arbitrary prescribed algebraic δ. The grid is not enumerated in the verification program.

[Full theorem and proof, §§3–4](../research-history/13-effective/research-note.md) · [exact parameter calculator](../research-history/13-effective/effective_bounds.py) · [historical log](../research-history/13-effective/effective-bounds.log).

## F.2 Direct Fourier sampling bound for odd q

The subsequent Fourier note states Theorem C under the assumptions of its Theorem A (gcd(q,30)=1) or its coarse Theorem B (odd q, 3∤q, m≥M₀ as defined there). Set m=(q−1)/2 and D=φ(q)/2. Its explicit finite grid has step 1/20 and

    L = 20000(m²+1)m⁴ 20^D.

The stated latest sample bound is t₀+(L−1)/20, with at most m²+1 samples. This uses direct Fourier density sampling and moment correction. Do not silently extend the specific constant to all collision-free q: the stated scope is exactly the original theorem's hypotheses. The later classification supersedes the earlier asymptotic existence threshold but does not automatically extend this effective bound.

[Full original Fourier note, Theorem C and §7](../research-history/14-fourier/research-note.md) · [exact checks](../research-history/14-fourier/verify_fourier.py) · [log](../research-history/14-fourier/verification.log).

## Review status

These bounds were omitted from the v0.1.0 main manuscript and are now explicitly indexed. They are archived conditional candidate theorems with their original mathematical proofs; no new independent proof, formal verification, or fresh priority assertion is made here. Standard effective approximation tools are not claimed as new.
