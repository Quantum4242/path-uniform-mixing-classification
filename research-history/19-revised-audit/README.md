# Revised complete path classification: second audit

27 November 2026. AI-assisted working proof. No personal author assigned. No GitHub change. Not peer-reviewed or Lean-formalized.

Read `unified-proof.md` for the combined proof. It replaces fourteen old LP probability certificates with positive Fourier densities, and states the global signed-root localization explicitly. The central order-35 inventory and order-385 exclusion have analytic proofs. The new `audit-addendum.md` explains the changes and remaining proof obligations.

Reproduce the new checks (Python 3, SymPy, and a C++17 compiler):

```
g++ -O3 -std=c++17 enumerate_lattice.cpp -o enumerate_lattice
python verify_lattice.py
python verify_small_density.py
python verify_q33_density.py
```

`verify_lattice.py` independently enumerates all short relations in 26 even parity groups, then compares with the coset generator. `verify_small_density.py` computes exact Fourier correction margins (the printed decimals are just display). `verify_q33_density.py` checks the original three-block density with the new completion-of-square bound. No SciPy or floating LP solver is required for the revised proof. The optional failed `explore_q33_polynomial.py` and its log are retained only as research provenance; they are not part of the proof.

The general-checks directory contains the earlier exact moment, classification, and global positivity scripts. The old certificate-file presence check was removed from `verify_classification.py`; no mathematical checks were removed. Run each script there with Python. General-checks logs, if present, are from their actual executions. No claim of full Lean certification.
