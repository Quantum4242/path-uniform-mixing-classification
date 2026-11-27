# Reproducibility and build

## Exact arithmetic

Tested locally with Python 3.13.5, SymPy 1.14.0, GCC 14.2.0, Linux x86_64. Install `requirements.txt` in a virtual environment. Run `python verification/run_checks.py`. Use `--cxx` for a different GCC-compatible C++17 compiler. Logs in `records/latest/` are generated, not used as proof inputs. The runner runs `verify_small_density.py` before the floor checker; the former recomputes the exact rational table. `verify_lattice.py` and `verify_q33_density.py` use the compiled C++ enumeration. No optimizer or external service required. All arithmetic assertions use integer/rational/symbolic data; decimal output and figures are illustrative. The independent finite lattice lists are generated with exact rational RREF and a bounded exhaustive free-coordinate search. The runner checks exit codes and leaves full logs. The release-rerun logs are the actual release test run. Historical reports may describe earlier implementation versions.

The CI workflow is supplied, but no remote CI run has occurred. Do not treat CI success as proof of the unbounded relation classification. Run without `-O` or other assertion-disabling options.

## Figures

Install `requirements-figures.txt` and run `python figures/generate.py`. It reads the verified rational margins and calculates the illustrative classification by congruence. It emits PDF, SVG and PNG. Noto Sans CJK is recommended for Chinese labels; set `CJK_FONT` to an installed font file if automatic detection fails. Font files are not distributed. Plotting itself uses floats only to render exact source data.

## PDF build

Use XeLaTeX with AMS math, graphics, hyperref, microtype, fancyhdr, ctex and Noto Serif/Sans CJK SC fonts. From `paper/` run:

```bash
xelatex -interaction=nonstopmode -halt-on-error paper-en.tex
xelatex -interaction=nonstopmode -halt-on-error paper-en.tex
xelatex -interaction=nonstopmode -halt-on-error paper-zh.tex
xelatex -interaction=nonstopmode -halt-on-error paper-zh.tex
```

PDF timestamps, font subsetting and machine-specific TeX versions may change bytes; mathematical content and test assertions should reproduce. The English detailed Markdown proof and the third audit are normative supplementary arguments. PDF copies of the main manuscripts are included. The Chinese paper is a companion summary of the proof chain, not a verbatim translation of the entire appendix.

## Checksums

`SHA256SUMS` describes the distributed release files (it excludes itself). It verifies integrity of the original release, not reproduction of byte-identical generated PDFs/logs. Linux: `sha256sum -c SHA256SUMS` at the repo root. Windows: use `Get-FileHash` or `python verification/check_hashes.py`. Re-running scripts or rebuilding PDFs may legitimately update files. Do not overwrite the archived release logs when reproducing.
