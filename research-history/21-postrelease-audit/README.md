# Post-release audit of path uniform mixing classification v0.1.0

27 November 2026. Internal AI-assisted audit, not independent peer review.

Base release: https://github.com/wangjiashu1/path-uniform-mixing-classification/releases/tag/v0.1.0 (commit 709df4e).

## Scope and results

This supplement does not change the mathematical statement or the tagged release. It extends the exact cyclotomic lattice checks to 10 odd moduli and to both parity groups of 5 even moduli outside the finite-exception threshold q=142. The enumeration engine and cyclotomic RREF setup are copied from v0.1.0; these are new input tests, not a third independently implemented solver. The enumeration itself does not use the predicted relation templates. The odd audit compares counts by length, absolute charge and coefficient pattern, and checks the three-block sublattice; it does not compare vector identities with a second odd template generator. The even audit compares the entire enumerated vector sets to the published template generator.

| Test | Free integer vectors (including zero) | Nonzero relations of l1 length <=10 |
|---|---:|---:|
| Odd: q=25,35,55,65,77,85,91,39,51,57 | 26,247,122 | 2,896 |
| Even: q=154,170,182,196,242, both groups | 25,983,606 | 364 |
| Total | 52,230,728 | 3,260 |

All assertions passed. The odd audit only compares the even-length, charge 0 or ±2 subinventory to the proof; the raw counts above also include irrelevant relations. For the even audit all short relations are compared. The short relations of length <=4 that would invalidate target cosine orthogonality are absent in all of the tested groups (for odd q, this refers to even-length relations).

The exhaustive free-coordinate search is valid because a kernel vector of l1 length <=10 has free coordinates of l1 length <=10. Pivot coordinates are determined by RREF; denominators and l1 length are checked, and all resulting vectors are checked against the exact cyclotomic coefficient matrix. The enumeration counts are independently checked using sum_k 2^k C(d,k) C(10,k). The scope is finite, not a proof of the global short-relation completeness lemma. In particular the general conductor-385 argument is not independently certified by this test. No new contradiction was found; no independent mathematical peer review or Lean compilation was performed.

## Reproduce

Requires Python, SymPy and a C++17 compiler. From this directory:

```sh
python -m pip install sympy==1.14.0
g++ -std=c++17 -O3 enumerate_lattice.cpp -o enumerate_lattice
python verify_odd_inventory.py
python verify_large_even.py
```

On Windows use `-o enumerate_lattice.exe`. Do not use Python -O. `odd-inventory.log` and `large-even.log` contain the actual completed runs. The copied files retain their original purposes; the scripts import only the indicated helper functions.

## Public reproducibility

The public release was accessible and labelled Pre-release. The public main directory listing did not show `.github` or `.gitignore`, and Actions displayed the initial setup page; no remote run was verified. The local original archive passed 78/78 SHA-256 checks. The included `verify-workflow.yml` and `gitignore.txt` are unchanged copies of the original hidden files; upload to `.github/workflows/verify.yml` (use the original filename from the release archive to preserve checksums) and `.gitignore`, respectively. The workflow runs the existing 11-check suite, not this new supplement. Do not add a CI-passing badge until a run actually succeeds. Check hashes against the original archive after restoring the exact original paths. No public repository was changed. No license was assigned.

## Priority

Kang's arXiv:2609.14463 abstract and submission history were rechecked; only v1 (13 September 2026) was shown, with the earlier positive families and negative classes. A targeted search did not identify a newer identical complete positive classification. This is not a priority certificate.
