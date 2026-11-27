# P19 integer-time certificate (research draft)

A reproducible direct certificate for uniform average mixing on P19 using 91 integer times. **Exact Python check passed; full Lean 4 proof not yet completed or compiled.**

- proof.md: mathematical argument and certificate interpretation
- certificate.json: times and rational approximate inverse/weights
- protocol.csv: readable time list and rounded weights, not exact weights
- verify_certificate.py: independent integer/rational checker (standard library only)
- verification.txt: recorded output of actual checker run
- generate_certificate.py: optional numerical discovery procedure
- lean-plan.md: remaining formalization obligations

Run `python3 verify_certificate.py` without `-O`. No dependency installation is required for verification.
