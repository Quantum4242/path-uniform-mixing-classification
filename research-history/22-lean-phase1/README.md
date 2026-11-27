# Path UAM — Lean 4 formalization, stage 1

Status: **uncompiled Lean draft, exact source-level arithmetic cross-check passed**.
The release basis is `path-uniform-mixing-classification` v0.1.0, `paper/detailed-proof.md` (DP). These files do not import the historical P19 certificates and do not establish the complete classification. No public repository was changed.

## Files and scope

| File / theorem | DP location | Scope |
|---|---|---|
| `PathShortRelations.lean`: `anti35_unit_axes` | III §4.4 | Every mixed antisymmetric central 5×7 array of weight ≤10 has one signed unit on each axis. |
| `sym35_unequal_axes`, `sym35_equal_axes` | I §3.4, III §4.4 | General necessary axis shapes for symmetric arrays, with the nonzero equal-row branch separated from the pure-cycle branch. |
| `support385`, `central385_no_weight5` | I §3.5, III §4.5 | Two inversion-paired support patterns; impossibility of half-weight five in the final slice. The latter strengthens the original 243-tuple check by dropping the additional entry restriction. |
| `PathPositivity.lean` | I §4, II §5, III §§3,5 | Shifted polynomials and exact inequality bounds valid for every real parameter in the indicated range; rational rescaling of the even-case slack for minimal N. Small-case fraction comparisons are arithmetic only. |
| `verify_phase1.py`, `source-check.log` | — | Exact independent comparison of 11 definitions and 13 shifted identities, integer checks and 3 rational inequalities. Not a Lean proof checker. |

The local integer lemmas use `omega`, sign case splits and 243 small branches for the final slice. The real inequalities use `ring`, `positivity`, `norm_num` and elementary ordered-field lemmas. No `sorry`, `admit`, custom axiom, `native_decide` or large matrix certificate is used in the Lean source. This is a source inspection statement, not a claim about the actual axiom report. Ordinary `#print axioms` commands are included.

## Compile with the existing local mathlib project

Test target: Lean 4.36.0 and its matching mathlib4 checkout/cache, as previously used for P19. This environment has neither `lean` nor `lake` and cannot resolve the GitHub host, so the Lean files have **not** been compiled here. Treat any compiler issue as unresolved; do not replace failed proofs with `sorry`.

Extract this archive to `E:\AI4P\path-lean-phase1`, then in PowerShell:

```powershell
$env:Path = "E:\lean-4.36.0-windows\bin;C:\Program Files\Git\cmd;" + $env:Path
Set-Location E:\mathlib4-4.36.0
lake env lean "E:\AI4P\path-lean-phase1\PathShortRelations.lean"
lake env lean "E:\AI4P\path-lean-phase1\PathPositivity.lean"
```

Run the files separately so errors remain localized. Adjust paths if the archive is extracted elsewhere. Confirm exit code zero for each command, no unresolved errors/warnings, and inspect the actual axiom reports (notably absence of `sorryAx` or native-evaluation trust axioms). Do not interpret a successful compile of these files as a proof of the entire DP. A source-level check may be reproduced with `python -m pip install sympy` followed by `python verify_phase1.py` from this folder.

## Remaining dependencies (not formalized here)

1. Cyclotomic annihilator and global minimal-support decomposition, including the use of the Conway–Jones theorem and the lift to central additive arrays.
2. All other local conductors, the pure-cycle case, full inventory/multiplicity derivations and the connection of the 385 slice hypotheses to an actual root-of-unity relation.
3. Derivation of the Haar/Fourier moment formulas and the uniform error bounds themselves (rather than only the inequalities between their explicit formulas).
4. Haar orthogonality and correction, spectral mixing bridge, and passage to a finite time distribution.

Keep the GitHub v0.1.0 release unchanged until genuine kernel results have been obtained and recorded. No new license or authorship designation is assigned by this draft.
