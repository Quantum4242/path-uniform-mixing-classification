# Uniform average mixing on the nineteen-vertex path

**AI-assisted research manuscript · 27 November 2026 · not peer reviewed · not fully Lean-formalized.**

We give a computer-assisted proof that the continuous-time adjacency quantum walk on the path P19 admits exact uniform average mixing using 91 distinct nonnegative integer readout times below 2000. Every exact weight is greater than 0.0006. The weights are defined as the unique solution of the real cosine linear system in the manuscript; rounded CSV weights are not exact solutions. The same distribution works for every initial vertex. A separate phase-torus construction establishes existence with at most 91 actual readout times, without the explicit integer-time restriction.

## Manuscripts

- [English PDF](paper/paper-en.pdf) ([LaTeX source](paper/paper-en.tex))
- [中文论文 PDF](paper/paper-zh.pdf) ([LaTeX 源文件](paper/paper-zh.tex))

Theorem 1 gives the explicit integer-time result. Sections 2–4 supply its spectral and exact interval-arithmetic proof; Section 5 gives the second existence proof. The case q = N + 1 = 20 is not covered by Kang's [arXiv:2609.14463v1](https://arxiv.org/abs/2609.14463v1) existence or nonexistence families. See [novelty record](records/novelty.md) for the limits of the priority check.

## Reproduce the proof certificates

Use Python 3.10+ (arbitrary-precision integers are built in). From the repository root:

```sh
python verification/integer/verify_certificate.py
python verification/compact/check_compact.py
python verification/compact/check_gap_formula.py
python verification/compact/verify_radical.py
```

These four checkers use the Python standard library only. **Do not use `python -O`**, as the checks rely on assertions (an explicit guard prevents this). The finite phase-law enumeration additionally uses SymPy:

```sh
python -m pip install -r verification/requirements.txt
python verification/phase/verify_p19.py
```

Or execute `python verification/run_all.py` after installing SymPy. The [actual reproduction log](verification/reproduction.log) records five successful runs during preparation of the manuscript. The optional exploratory generator is not part of the proof and requires NumPy and SciPy. It writes a separate candidate file, never replacing the fixed published certificate.

| File | Purpose |
| --- | --- |
| `verification/integer/certificate.json` | Fixed 91 times, integer numerators of approximate inverse and weight vector |
| `verification/integer/protocol.csv` | Times and rounded probability weights (not the exact solution) |
| `verification/integer/verify_certificate.py` | Rigorous Machin/Taylor interval check, inverse-defect and positivity bounds, 361 polynomial identities |
| `verification/compact/compact.json` | Fixed-point integer certificate at scale 10^8 |
| `verification/compact/check_compact.py` | Compact certificate and first interval method |
| `verification/compact/verify_radical.py` | Independent radical/double-angle interval method |
| `verification/phase/verify_p19.py` | Cyclotomic rank, phase-law moment checks, polynomial mixing identities |
| `lean/` | Partial formalization and explicitly uncompiled or unconfirmed drafts |

The certificates use exact integer and rational arithmetic. The numerical discovery step is not a proof premise. Analytic correctness still depends on the interval-containment, spectral, and convexity arguments in the manuscript.

## Formalization status

The finite gap-grouping theorem `P19.allGapChecks` produced an axiom-audit result in the Lean web editor (v4.37.0-rc1); see the [verification status](records/formalization.md). The matrix certificate has **no confirmed successful Lean build**. The Mathlib-dependent bridge modules remain uncompiled drafts. A successful check of these individual modules would not itself prove the original theorem; the links to the actual spectral and interval statements still need formalization. Python certificate checks are not Lean kernel proofs.

## Publication status and AI disclosure

This is a research manuscript supported by exact-arithmetic checks, not a peer-reviewed publication or a certified priority claim. ChatGPT assisted literature search, derivations, exploration, code, certificates and writing. The release author should independently review the mathematics and approve authorship and publication. No institutional endorsement is implied. No claim of minimal support, optimal readout horizon, or a general classification of path graphs is made.
