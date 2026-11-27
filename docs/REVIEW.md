# Final integration review — v0.1.0

Date: 2026-11-27. Internal AI-assisted review, not independent peer review.

## Decision

Release candidate for open review, not final certified theorem. The main result is conditional on the correctness and exhaustiveness of the three short-relation inventories. No new mathematical counterexample was identified during integration. This is not a guarantee that no gap exists.

## Proof audit map

| Item | Where to review | Evidence / remaining risk |
|---|---|---|
| Spectral target and obstruction | Main §2; Kang S2–S3 | Prior results; spectral substitution also displayed directly. |
| Character lattice and Fourier correction | Main Lemma 2 | Analytical Haar orthogonality; requires target chars distinct modulo inversion. |
| Signed relation theorem | Main §3; DP common reduction | Conway–Jones Thm 5 (p.235), Lenstra Thm 2.6 (p.259) permit rational signed coefficients; checked original scans. |
| Projection and support | DP common reduction; third-audit §1 | Distinct supported exponents modulo q; central lift factors 1 and i. Prove the statement for whole arrays, not a symmetric minimal partition. |
| Local inventories and 385 | DP I §3, II §4, III §4 | Analytic reductions, bounded central array checks, and exact counts. **Highest priority for external scrutiny**: disjoint minimal-subset partition, paired cosets, mixed-conductor coexisting components, and the 385 slice argument. Finite tests alone do not prove completeness. |
| Symbolic moments and error constants | DP I §4, II §5, III §3 and §5 | Exact coefficients, shifted polynomial positivity; no float assertions. |
| Small cases | DP II §6, III §6 | q=33 square completion; q=9 explicit law; q=35,39 rational corrections; 13 even cases: 26 lattice lists (30,094,218 free vectors; 1,032 relations) agree. |
| Convex grid bridge | Main §5; DP conclusion | Full support is sufficient, not necessary. Dense nonnegative algebraic-step grid, shared relative interior, support bound by number of real moments. |
| Uniform floor and noise | Main Thm 4 and Cor. 5; third-audit | Conditional on classification; separate group floors are combined by removal/scaling/restoration, not by multiplying without adjustment. Complex support count doubles. |
| Formalization | lean/README.md | Historical P19 only. No independent Lean run in current environment; no general kernel proof. |

## Integration corrections

* Replaced the previous overly strong phrase “full support is essential” with “full support is sufficient for this argument”.
* Distinguished 14 formerly LP-dependent cases from all finite special handling (q=35,39 also have exact Fourier calculations; q=9 has an explicit law).
* Updated Baptista et al. to the 2024 journal reference; added Godsil's Cesàro-average reference. Preserved priority of Kang, Conway–Jones, and Lenstra.
* Clarified that q=33 calculates actual moments and corrects them by exact Haar orthogonality. Added direct corrected-moment assertions, explicit checks of the required short-relation absence in the independent finite lattices, and independent case-coverage assertions. Changed the uniform-floor checker to verify the small-case 1/100 assertion (rather than only its square) and clarified its log.
* Made finite-lattice executable selection and exact margin output paths portable. Actual Linux run: 11/11 scripts returned exit 0. Logs are in `records/release-rerun/`.
* The main paper refers explicitly to DP for detailed local inventories and coefficient computations. The Chinese companion is not a full translation of the English detailed proof. No claim of a completely self-contained short main paper separate from the supplement.

## External review request

Reviewers should try to construct an omitted signed relation satisfying the length and charge filters, not just test more graph sizes. For the conductor-35 cases, challenge the pairing argument and the inventory of coexisting five-length components. For 385, check that the central restriction and common-slice value follow from minimality and the support budget. For the even case, check the sign-folding and independence of parity groups. For the robustness claim, check the joint Haar floor and complex moment interpolation. Report an explicit counterexample or a missing implication if found. A successful finite test does not establish an infinite theorem; failure of a sufficient density bound is not nonexistence.

## Archive candidate addendum (v0.2.0-rc1)

The preceding v0.1.0 review is retained. The archive candidate adds historical methods, quantitative bounds and original certificates, plus post-release finite audits and uncompiled Lean stage-1 source. See [contribution ledger](CONTRIBUTIONS.md) for status and provenance, and [release checklist](RELEASE-v0.2.0-rc1.md) for scope. The maintainer supplied a screenshot of a successful `verify` job (29 s and log artifact) on the public main branch. This is not verification of the new archive nor of the general mathematical proof. No mathematical claims or original proof files were changed. The highest priority remains global relation completeness; historical methods are not newly independently audited.
