# Working research record (not a release)

Read `research-note.md` for the mathematical statement, proof and caveats. No author assigned. No claim of independent peer review or complete Lean proof.

Reproduce the exact checks using Python 3, SymPy and NumPy:

```
python verify_full.py
python verify_tree.py
```

`verify_full.py` verifies every original spectral pair from the 14 JSON certificates using exact integer and rational arithmetic. `verify_tree.py` checks the finite symbolic inequalities for the two infinite ranges and small spanning-tree schedules. Logs are included. The exploratory scripts use SciPy and floating-point LP only to find candidate certificates; the exact verifiers do not require SciPy. The certificate weights are auxiliary phase-law weights, not physical readout-time weights. The proof of existence of physical integer times is in Section 2 of the note. No formal publication requested in this round.
