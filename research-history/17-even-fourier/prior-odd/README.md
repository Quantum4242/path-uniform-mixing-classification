# Three-block path research

Working note (no personal attribution, AI-assisted, not peer-reviewed). A candidate proof for every odd q divisible by 3 with gcd(q,35)=1. Together with the included earlier note it gives a candidate complete classification for odd q. The even q case remains open in this work.

- `research-note.md`: new mathematical proof, full scope and limitations.
- `verify_three_blocks.py`: exact symbolic calculations and central relation enumeration (SymPy).
- `verify_small.py`, `q33.json`, `q39.json`: previous exact certificates (SymPy and NumPy for bounded integer counts), rerun.
- `verification.log`, `small-verification.log`, `prior-recheck.log`: actual outputs.
- `prior-odd-coprime/`: earlier proof and supporting checker.

Run `python verify_three_blocks.py` and `python verify_small.py`, then `python prior-odd-coprime/verify_short_relations.py` (or from its own directory). No full Lean formalization, priority guarantee or external peer review. This archive is not a formal public release.
