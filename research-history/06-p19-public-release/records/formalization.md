# Lean verification boundary

User-provided screenshot of the official Lean web editor showed the following audit for the finite gap-grouping certificate (Lean v4.37.0-rc1):

```
'P19.allGapChecks' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The screenshot is cropped to show the relevant output only. This is evidence of the reported finite check, not an independent rerun in the manuscript preparation environment. The theorem concerns finite polynomial coefficient comparisons and gap coverage. It does not prove their analytic interpretation or the mixing theorem.

- `P19-online-gap.lean`: reported success above.
- `P19-online-matrix-fast.lean`: optimized finite integer matrix check. Local Lean 4.36.0 was installed and execution observed, but no successful completion or final axiom audit was supplied. The source is retained for reproducibility and further debugging, not marked verified.
- `RadicalBridge.lean`, `WeightBridge.lean`: Mathlib-dependent uncompiled drafts. Some statements are conditional on real inequalities and therefore need further linking with the fixed certificate.

Remaining work: actual completion of the matrix checks, real interval soundness including Taylor bounds, casts from the concrete integer arrays, polynomial evaluation, spectral projectors and matrix exponential, and an unconditional main theorem with a full axiom audit. The current manuscript instead uses conventional mathematical arguments plus exact Python checks. Do not label it a fully machine-formalized proof.
