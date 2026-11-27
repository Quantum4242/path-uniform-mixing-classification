# Effective path mixing research supplement

Working record, no author assigned. Not a public release or complete Lean formalization.

- research-note.md: exact q=595 certificate, conditional finite readout-window theorem and proof, Lean status update.
- q595.json: integer certificate; verify with `python verify_certificate.py 595` (NumPy and SymPy required).
- verification595.log: successful exact check of 176121 pairs.
- effective_bounds.py: exact parameter generation and small polynomial cross-checks; run with `python effective_bounds.py`.
- effective-bounds.log: output; no huge grid simulated.
- explore.py, fast_search.py, build_certificate.py: floating discovery tools (SciPy required), not trusted for the final proof.
- search595.log: floating search discovery; search665.log: attempt interrupted by execution time limit, not evidence of infeasibility.
