# E. Explicit readout schedules and rigorous positive-weight certificates

## E.1 Distinguish physical times from phase seeds

The earlier P8 record gives 17 actual half-integer/integer times (maximum 19.5), strict weight lower bound 0.027 and two verification approaches. Its existence and 17-point upper bound are attributed to prior work. The P19 publication gives 91 actual nonnegative integer times below 2000, all exact weights greater than 0.0006, and a separate phase-torus existence proof. Rounded CSV weights are not exact: the exact weights are defined by the real linear system. The P19 finite Lean arithmetic verification is partial, not the complete real-analytic proof.

- [P8 recovered PDF and public repository](../research-history/01-p8/README.md)
- [P19 public manuscript, protocol, code and logs](../research-history/06-p19-public-release/README.md)
- [P19 early phase law](../research-history/02-p19-phase/proof.md), [integer-time certificate](../research-history/03-p19-integer/proof.md), [compact proof](../research-history/04-p19-compact-lean/compact-proof.md), [analytic bridge](../research-history/05-p19-analytic-bridge/README.md)

## E.2 Auxiliary phase certificates for larger moduli

The historical orbit certificates for q=385,429,455,561,595 store an integer matrix of approximate inverse coefficients and approximate weights, scaled by Q=10^12. A floating LP is used only to discover candidates. Let B be the exact integer matrix of orbit sums, y the rational target, R the scaled approximate inverse and u the scaled approximate weights. If ε=||I−RB||∞<1, B is square and hence invertible. For w=B⁻¹y,

    ||w−u||∞ ≤ ||R||∞ ||y−Bu||∞/(1−ε).

A strict lower bound for min(u) exceeding that error certifies all exact weights are positive. The first row normalizes them. Galois-orbit reconstruction checks all original spectral pairs; integer products and rational residual bounds are used. This is a general verification device, not a claim that inverse-defect analysis itself is new.

| q | B order | Full unordered pairs |
|---:|---:|---:|
| 385 | 416 | 73,536 |
| 429 | 494 | 91,378 |
| 455 | 482 | 102,831 |
| 561 | 624 | 156,520 |
| 595 | 608 | 176,121 |

The certificates produce the stronger auxiliary moments −1/(q−2) on same-parity distinct modes and 0 otherwise. Haar mixing and the interior argument are needed for actual time existence. The phase seeds are NOT physical readout times. The historical q=665 search timed out; it is not evidence of nonexistence. The floating NPZ discovery data are preserved separately from the exact JSON certificates.

- [Original triple-prime proof](../research-history/12-triple/research-note.md), [verifier](../research-history/12-triple/verify_certificate.py), [log](../research-history/12-triple/verification.log)
- [q=595 proof and time-window extension](../research-history/13-effective/research-note.md), [q=595 log](../research-history/13-effective/verification595.log), [failed q=665 search](../research-history/13-effective/search665.log)
- [Additional floating discovery data](../research-history/23-additional-local-records/README.md)

The earlier finite orbit certificates in Supplements B and D are also preserved. All statements here describe the archived constructions and results; they are not new independent peer review of their full proofs.
