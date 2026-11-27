# Lean 4 formalization plan (not yet verified)

The direct integer-time argument replaces the previous analytic density argument. No Lean toolchain is available in the current execution environment; no `.olean` file or successful `lake build` is claimed. The previous finite phase certificate is a different proof and is not a substitute for this theorem.

Target: define the adjacency matrix of P19 on Fin 19; show existence of a vector of 91 natural-number times bounded by 1999 and 91 positive real weights summing to one, with the entrywise norm-square of the complex matrix exponential averaging to the constant 1/19. Alternatively, first formalize the spectral expression and then prove its equality to that matrix exponential.

Required formal lemmas:
1. Fixed-point interval inclusion: integer endpoints interpreted as real rationals, addition/subtraction/multiplication/division preserve containment.
2. Pi bounds: Machin formula, alternating arctangent remainder. Cosine bounds: periodicity and Taylor remainder. The interval checker must be linked to these lemmas, not just executed.
3. Polynomial reduction soundness and the finite spectral identities; prove the root identity directly, avoiding cyclotomic irreducibility.
4. Row-sum bound and finite-dimensional injective-square-matrix implies invertible. The residual bound yields positivity. A finite norm argument suffices; no Neumann-series convergence proof required.
5. Path sine eigenbasis, spectral exponential, and the final 19x19 equality.
6. Check all arithmetic subcertificates in the kernel, preferably in chunks with `decide` or proof-producing tactics. Avoid unproved axioms, `sorry`, or merely `#eval` results. Inspect `#print axioms` for the final theorem, including dependencies. Pin toolchain and mathlib commit. Only label the theorem Lean-verified once a clean build and axiom audit actually pass.

Open issue: full proof may require additional mathlib lemmas for the Taylor and spectral exponential steps. This is a plan, not Lean source or a compiled proof.
