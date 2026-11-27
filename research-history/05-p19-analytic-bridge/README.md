# P19 v5: analytic bridge work (2026-11-27)

This is an incremental supplement, not a replacement for the v4 matrix file currently being checked in VS Code. **The new Lean files are uncompiled drafts**. No full Lean verification or successful build is claimed. They import Mathlib, unlike v4. Do not open the big v4 file again just to run these files. Install/configure a matching Mathlib project first.

## Actual executed work

`python verify_radical.py` runs an alternative rigorous fixed-point interval computation using only Python's standard library. It reads the unchanged v3 `compact.json` (same A, R, w, b, times and representative pairs). All 8281 coefficient enclosures and the original integer inequalities pass. The log is `verification.txt`. This verifier uses no pi approximation or floating point. It does not verify the gap grouping or the spectral identity; the previous certificate handles those.

## Why the radical and double-angle approach is sound mathematically

Let a = pi/20 and theta_r = 2 cos(r a). The exact value cos(pi/5)=(1+sqrt(5))/4 and twice applying the positive half-angle formula give theta_1 = sqrt(2 + sqrt((5+sqrt(5))/2)). Then theta_0 = 2 and theta_(r+1)=theta_1 theta_r - theta_(r-1). All intervals contain their intended real numbers by elementary monotonicity, outward rounding and the integer square root bounds. For each gap-time argument y, use x=y/4096. The checker establishes |x|<=2. Taylor's theorem through degree 41 (the odd coefficient is zero) gives a remainder at most 2^42/42! < 10^-30 for the degree 40 cosine polynomial. Twelve applications of 2 c^2 - 1 recover cos(y); clipping to [-1,1] preserves containment. No pi bounds, periodic reduction or Machin formula needed. The final enclosure is sufficient for the existing compact matrix proof.

## Lean source drafts

- RadicalBridge.lean: exact nested radical, Chebyshev recurrence and repeated double-angle identity.
- WeightBridge.lean: row sum inequality, small inverse-defect implies surjectivity, error and strict positivity, normalization, and a theorem deriving the defect/residual bounds from the real interpretation of the compact certificate. `P19Bridge.from_compact_bounds` has explicit hypotheses for the scaled integer arithmetic and the cosine enclosure. They are not extra axioms, and are not yet discharged by the concrete data. A passing check of the conditional theorem alone does not establish P19.

Both files end with axiom audits. No sorry/admit/native_decide or new axioms have been inserted. Their Lean syntax and tactic scripts still need actual compilation. Start with RadicalBridge, then WeightBridge. The previous gap and matrix certificates are still needed.

## Remaining formalization

1. Confirm v4 arithmetic file build and axiom audit; do not infer success from CPU activity.
2. Compile these small Mathlib modules; repair any version-dependent tactic errors.
3. Link the concrete integer inequalities with the real hypotheses of from_compact_bounds (lists -> Fin matrices, casts, scaled dot products). Formalize the interval arithmetic with Taylor remainder and replay the 8281 inequalities in Lean. Python results are not Lean theorems.
4. Link polynomial gap coefficients to actual energy gaps, and prove the path sine eigenbasis/projector identities and complex matrix exponential expansion.
5. Assemble the unconditional existence theorem for the adjacency matrix on Fin 19; clean build, audit its axioms and all dependencies. No full result is claimed until this step.
