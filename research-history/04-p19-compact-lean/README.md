# P19 — Lean 4 finite certificate draft (v3)

**Status:** exact Python checks passed, Lean build NOT run (Lean/Lake/Elan absent and network DNS unavailable in the authoring environment). This is not a claim of full formal verification. Originality still requires review. This package has not been uploaded to GitHub.

## Reproduce exact checks

```
python3 check_compact.py
python3 check_gap_formula.py
```

Both use only the Python standard library; do not disable assertions. `compact-verification.txt` records actual output. `compact.json` is the fixed data. `source/` holds the v2 high-precision source certificate and exact interval checker; `build_compact.py` is the optional generator for the new rational approximation. `generate_lean.py` and `generate_gaps.py` export the fixed data/checks into Lean source. `compact-proof.md` explains the proof and formalization boundary.

## Lean build (not tested here)

Install Elan from https://lean-lang.org/install/ or use the supplied GitHub Actions workflow in a private repository. This finite stage needs Lean 4 v4.19.0 only, no mathlib downloads. At the repository root:

```
lake build
lake env lean Audit.lean
```

The two finite theorem declarations are `P19.allChecks` and `P19.allGapChecks`. Neither theorem is the original P19 theorem. The workflow runs both Python checkers, builds the Lean project, prints the axioms of both finite theorems, flags known disallowed proof dependencies, and uploads logs. It is a proposed workflow and may need adjustments for resource limits or Lean API compatibility; no CI run has occurred. Inspect the actual axiom output, not just the build status. No `sorry`, `admit`, or `native_decide` is used in the Lean source.

Next formalization stage: checked fixed-point interval soundness, cosine error bound, root evaluation, finite-matrix invertibility/positivity, spectral exponential and final equality. Use mathlib when needed. See compact-proof.md for the precise obligations.
