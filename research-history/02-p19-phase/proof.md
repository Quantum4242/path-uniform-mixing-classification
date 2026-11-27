# A candidate proof of uniform average mixing on P19

Status: mathematical proof draft, exact finite-arithmetic checks passed. Not yet peer reviewed or Lean-verified. Novelty search has not established absolute priority.

## Theorem
For the adjacency matrix A of P19, there exists a finitely supported probability measure μ on real times such that the entrywise squared moduli of exp(itA), averaged over μ, equal J/19.

## 1. Coherence target
Let θ_r = 2 cos(rπ/20), 1 ≤ r ≤ 19. Then θ_10 = 0 and θ_(20-r) = -θ_r. Kang, arXiv:2609.14463v1, equation (4) and its proof, shows that the sufficient target for averaged cosines of spectral gaps is y_rs = -1/19 for distinct same-parity indices and 0 for opposite-parity indices. The result below constructs that target. The original theorem of Kang does not cover q=20.

## 2. Phase torus
Let ζ be exp(iπ/20), with minimal polynomial Φ40(X) = X^16 - X^12 + X^8 - X^4 + 1. Reduce X^r + X^(40-r) modulo Φ40 for r=1,...,9. The resulting 16×9 integer coefficient matrix R has kernel generated over Q by (1,0,-1,0,-1,0,1,0,1). The integer relation is primitive; the 8×8 minor with rows 0,1,2,5,6,7,8,9 (zero-based) and columns 0,...,7 has determinant -2. This proves that the integer relations are exactly multiples of that vector. By the continuous form of Kronecker's theorem, the closure of the phase flow is the subtorus H of (R/2πZ)^9 given by φ1-φ3-φ5+φ7+φ9 = 0 mod 2π. Extend each phase vector to 19 entries by φ10=0, φ_(20-r)=-φ_r.

## 3. Exact finite phase law
Represent a fourth-root phase by a residue a mod 4, corresponding to aπ/2. For a pattern a and weight w, select a uniformly random permutation of the pattern and, independently, negate every entry with probability 1/2. Patterns are sampled with the following weights.

Odd transformed phases (φ1,-φ3,-φ5,φ7,φ9):

| pattern | weight |
|---|---:|
| 0,0,0,0,0 | 1/96 |
| 0,0,0,2,2 | 25/96 |
| 0,0,2,3,3 | 5/36 |
| 0,1,1,3,3 | 5/72 |
| 1,2,3,3,3 | 25/48 |

Every pattern sums to zero mod 4. Even phases (φ2,φ4,φ6,φ8), independently:

| pattern | weight |
|---|---:|
| 0,0,1,3 | 1/6 |
| 0,2,2,3 | 1/2 |
| 2,3,3,3 | 1/18 |
| 1,3,3,3 | 5/18 |

Both weight lists are positive and sum to 1. The resulting probability law ν is supported on H.

For a pattern of length m let c_j=cos(a_jπ/2), s_j=sin(a_jπ/2), C=sum c_j, S=sum s_j, C2=sum c_j², S2=sum s_j². Exchangeability gives E cos φ = C/m, E cos 2φ = (C2-S2)/m, E cos φ_i cos φ_j = (C²-C2)/(m(m-1)), E sin φ_i sin φ_j = (S²-S2)/(m(m-1)) for distinct indices. Negation symmetry makes sine means and mixed sine-cosine expectations zero. Taking the listed weighted averages gives, for both groups, E cos 2φ=-1/18, E cos φ_i cos φ_j=-1/18 and E sin φ_i sin φ_j=0. The mean cosine is zero for the odd group, -1/18 for the even group. Sign changes on odd coordinates do not alter these conclusions. Independence between groups gives zero cross-parity cosines. The fixed zero phase pairs with even coordinates at -1/18 and odd coordinates at zero. Reflected pairs use cos 2φ. Thus all 171 distinct spectral pairs have coherence -1/18 for same parity, zero otherwise. verify_p19.py checks this by exact enumeration independently of the moment formulas.

## 4. From torus to actual times
Define F:H→R^171 by F(φ)_(r,s)=cos(φ_r-φ_s), r<s. Let K=conv F(H), compact by finite dimensionality and compactness of H. Let h be Haar probability on H. Each gap θ_r-θ_s is nonzero because the eigenvalues are distinct; consequently the corresponding character on H is nontrivial (otherwise it would be trivial along the actual time flow). Haar orthogonality gives ∫F dh=0. Full support of Haar and continuity imply 0∈ri K: if it were on the relative boundary, a nonconstant supporting affine functional would attain its maximum at the mean and hence be constant on all F(H), a contradiction.

Write w=∫F dν. Section 3 yields the desired coherence vector y=(18/19)w+(1/19)0. Since w∈K and 0∈ri K, y∈ri K. Let D={F(tθ):t∈R}. Kronecker density gives closure(conv D)=K. In finite dimensional real vector spaces ri(conv D)=ri K, hence y∈conv D. By definition of convex hull there are finitely many actual times t_j and nonnegative weights summing to 1 realizing y exactly. The exact cyclotomic computation counts 90 distinct positive Bohr frequencies, so Carathéodory gives at most 91 actual times. Applying Kang's sufficient coherence identity proves the theorem. No assertion is made that the listed discrete phases are attained at actual times individually.

## Verification status
The exact Python certificate checks the cyclotomic matrix rank and relation and all 171 pair moments using rational numbers only. It also independently verifies all 361 entries of the target mixing matrix by reducing integer polynomials modulo Φ40. The analytic steps above are conventional mathematical arguments; they have not been checked in Lean. The current environment lacks Lean/Lake/Elan and cannot download them (DNS failure). A full formal proof must include the original mixing statement, the spectral identities, the phase-flow density and the relative-interior transfer, not merely the finite arithmetic certificate.

Source: Musung Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, https://arxiv.org/abs/2609.14463 (2026), v1.
