# Triple-prime path research supplement

Working research record (2026-11-27), no author assigned. Not independently peer-reviewed, not Lean-formalized. Four new candidate existence results with exact, independently reconstructed arithmetic certificates. See research-note.md for the complete argument, full moment margin, and timing-noise correction theorem. Full classification remains open in this project.

Verification:

```
python -m pip install numpy sympy
python verify_certificate.py 385 429 455 561
```

Discovery (optional, also requires scipy): `python fast_search.py 385 3000` then `python build_certificate.py 385` (writes certificate). The supplied JSONs are the checked data. Discovery is floating point; verification uses bounded integer arithmetic and exact fractions only. Do not confuse seed orbits with actual readout times. No public upload has been made.
