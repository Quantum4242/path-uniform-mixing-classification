# Candidate complete classification of uniform average mixing on paths

Working record, 27 November 2026. AI-assisted, no personal author, not independently peer reviewed or fully Lean formalized. No change to published GitHub repositories.

New result: an even-modulus proof using a degree-eight nonnegative Fourier polynomial, short cyclotomic relations in a projective root group, and thirteen exact finite certificates. Combined with two prior odd-modulus notes and Kang's existing nonexistence theorem, it covers all q=N+1>=3: UAM is conjecturally proved to exist exactly when 15 and 21 do not divide q and either 6 does not divide q or q=6. See research-note.md for the complete new proof, prior-odd/ for both preceding odd proofs, and review limitations. The combined theorem is a candidate pending independent scrutiny of all analytic steps.

## Reproduce
Python dependencies: sympy, numpy (scipy only for optional search).

```
python verify_low_degree.py
python verify_classification.py
python verify_all.py
python verify_full.py
```

The included *.log files are from actual runs. The finite certificates have exact rational positive weights; no optimizer is required to verify them. For the previous odd proofs, see prior-odd/README.md. Their scripts were also rerun this turn.
