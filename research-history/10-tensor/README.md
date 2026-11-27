# Working research record: tensor interpolation on quantum paths

No author assigned. Not a publication release. No full Lean formalization. Read `research-note.md` for the standalone theorem, proof and limitations. The new sufficient criteria do not depend on the earlier research drafts.

## Reproduce

Python 3 and SymPy are required for the new exact tests (the prior supplemental checkers also use NumPy). No LP solver is needed for the new theorem checks.

```
python verify_tensor.py
python verify_moments.py
```

`verification.log` and `moments.log` are actual outputs. `prior-recheck.log` records the six earlier checker reruns. See `prior-work/` for the preceding prime-power and overlapping-constraint research drafts and their code/data. Their proof scope and audit status differ from the new theorem; they are not silently assumed in its proof.

The examples are applications of the general sufficient condition, not computed time protocols. The theorem is a mathematical existence argument, with exact finite supplementary checks. Failure of the sufficient condition is not proof of nonexistence. Priority and independent expert review remain pending.
