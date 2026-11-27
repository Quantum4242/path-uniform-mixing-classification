# Third audit supplement

Read `unified-proof.md` (unchanged from the previous version) followed by `audit-addendum.md`. The supplement strengthens the radical/large-prime localization proof and derives a uniform 1/100 Haar component and complex Fourier interior radius 1/200 conditional on the unified classification proof. It also gives a known timing-noise corollary, without assuming symmetric noise. No new claim of formal or external verification.

Reproduce with Python 3 and SymPy:

```
python verify_localization.py
python verify_uniform_floor.py
```

The exact-density-margins table is inherited from the preceding revision; its independent enumeration and density-check scripts are in that revision's separate package, not repeated here. Logs record the completed runs. The initial slow polynomial remainder implementation timed out; the final integer implementation passed. No large LP, no new Lean run, no GitHub modifications.
