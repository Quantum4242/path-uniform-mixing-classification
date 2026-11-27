# Short-relation Fourier path research

Candidate theorem: every path P_(q-1) for q>=3 coprime to six admits strict uniform average mixing. The proof gives a finite actual-time law and a conservative finite-grid bound, not simply a feasible limit. It expands the preceding coprime-to-thirty theorem without a size threshold.

- `research-note.md`: complete mathematical argument, assumptions, scope, references and novelty caveats.
- `verify_short_relations.py`: supplementary exact arithmetic checker (Python 3 + SymPy).
- `verification.log`: actual checker output.

Run `python verify_short_relations.py`. No large matrix calculation or numerical optimization is required. The general number-theory proof is in the note; finite checks alone do not prove it. Not fully Lean-formalized or independently peer-reviewed. No personal author assigned, no public repository modified.
