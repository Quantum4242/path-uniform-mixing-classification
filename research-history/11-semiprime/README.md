# Semiprime completion research record

Working draft; no author assigned; AI-assisted; not peer-reviewed and not Lean-formalized. Not a final publication package.

- `research-note.md`: full new candidate classification for odd semiprimes and sufficient condition for two-prime-power moduli, with proofs.
- `prior-tree-proof.md`: earlier tree construction used for the p>=13 part of the classification.
- `q*.json`: 18 exact finite phase certificates (nine new, nine reused).
- `verify_full.py`: independent full-pair verification of each finite certificate, including four known negative controls.
- `verify_columns.py`: symbolic threshold checks and exact modular completion/moment tests.
- `verify_tree.py`: earlier tree-probability checks.
- `explore.py`: floating-point LP discovery followed by exact rational certification; not required for verifying the stored data.

Run in this directory using Python with NumPy, SymPy and SciPy (SciPy is needed only for discovery):

```
python verify_columns.py
python verify_tree.py
python verify_full.py
```

Full-pair verification may take longer than a minute. Actual logs are included. The full theorem on arbitrary path lengths remains unresolved; no new negative case is claimed. No concrete integer readout times are supplied for the general families.
