# Third audit: algebraic localization and uniform interior margin

27 November 2026. Supplement to `../paper/detailed-proof.md` (the preceding revised proof, copied unchanged into this package). AI-assisted working research, no personal author assigned. No GitHub changes. The classification remains a candidate pending external review. This supplement provides an independent justification of the radical and large-prime reductions and a quantitative strengthening **conditional on the positive constructions and their global short-relation inventory in that manuscript**. The new finite tests do not replace that inventory's proof.

## 1. Independent algebraic localization

Let q>=3. In the odd case, use a primitive q-th root z and a rational coefficient array on Z/q. In the even case, use z primitive of order 2q, and fold antipodal terms into a signed rational array on Z/q by z^(j+q)=-z^j. The supported original exponents +/-r for 0<r<q/2 are distinct modulo q, so the folding preserves absolute weight and support. The original array is symmetric under inversion before folding. Let d be the product of the distinct *odd* primes dividing q (empty product 1), and a=q/d. Let A(x) denote the folded polynomial of degree <q, or the ordinary root array in the odd case. Then

    Phi_q(x) = Phi_d(x^a)                 (q odd),
    Phi_(2q)(x) = Phi_(2d)(x^a)           (q even).

For the first identity, a root whose a-th power has order d must itself have order q, since every prime of q is in d. The second follows by the same argument for 2q, with squarefree radical 2d and quotient a. The degrees agree by the totient formula. This proof covers d=1 in the even case. Write uniquely

    A(x) = sum_(j=0)^(a-1) x^j A_j(x^a).

Divisibility by either displayed cyclotomic polynomial holds iff each A_j is divisible by the corresponding Phi_d or Phi_(2d): group the coefficients of any quotient polynomial by residues mod a, or use uniqueness of the monic remainder. Hence every relation is a disjoint union of separately vanishing restrictions to cosets of the subgroup of order d in Z/q. In an even lift, z^a has order 2d and its negative has order d, so replace z^a by minus an odd-order primitive root, absorbing the sign in the coefficients. No cancellation or change of support is involved.

Now suppose an array has at most K nonzero terms. For a squarefree odd conductor d and a prime p|d, write d=p r. CRT represents the root array as coefficients a_(i,j) on p by r indices. Let B_i denote each row's evaluation at a primitive r-th root. Irreducibility of Phi_p over Q(zeta_r) (degree ratio p-1) gives B_0=...=B_(p-1) whenever the whole array vanishes. If p>K, at least one row is empty, so all rows vanish. Iterate for every prime >K. Thus each restriction to a coset of the subgroup of order

    D_K = product of the odd primes p|q with p<=K

vanishes individually (up to the constant lift and signs). The converse follows from summation of the restrictions. The argument is exact for arbitrary prime powers and arbitrary numbers of large primes. In the case K=20 it makes explicit why larger primes cannot create any additional short-relation templates. The same property follows from the minimal-support approach in the unified proof. These algebraic facts are classical: compare Lenstra, *Vanishing sums of roots of unity* (1979), Theorems 2.2 and 2.3, pp.257–258. We use them as an independent audit, not a new number-theory result.

Inversion sends a coset to its inverse. A stable coset of odd order has one fixed point, 0 for odd q, and 0 or q/2 for even q, since multiplication by two is bijective on the odd-order subgroup. These points are excluded from the original spectral support. In even q the lifts at these centers have common factors 1 and i, giving symmetric and antisymmetric coefficient arrays respectively. For a conductor d supporting a minimal subset, the same central-coset geometry applies when the subset has support greater than K/2, regardless of which other blocks were selected: the opposite coset would require equally many entries in the whole symmetric array. For pure prime cycles a distinct-prime cycle meets an inverse cycle in at most one point; in the p>=5 case at most four minimal components fit the budget. In the p=3 case a pure cycle of prime r>=11 is impossible because its inverse is disjoint and would require at least 2r>20 entries, even if supplied by several blocks. These statements do not require the initial partition to be inversion invariant.

The mixed conductors from the Conway–Jones bound (Lenstra Theorem 2.6) are exactly 35,55,65,77,85,91,385 when the odd primes are >=5, and 33,39,51,57 when the primes are 3 or >=11. The detailed mixed conductor inventories and the order-385 exclusion in the preceding manuscript are still needed; the present argument does not by itself replace them. The code `verify_localization.py` checked 34 exact polynomial identities and 1224 sparse-array equivalences (297 zero arrays, 927 nonzero-evaluation arrays), including prime powers and primes greater than 20. It uses integer monic division. The first implementation using slower SymPy remainder timed out; the final integer implementation completed all tests. The tests are only an audit of the exact algebraic derivation.

## 2. Uniform phase-law margin

Let H be the closure of the path phase flow, h its normalized Haar probability. Let Omega be the set of all distinct positive Bohr frequencies. On H let chi_w be the character corresponding to exp(i w t). Write y_w=-1/N for same-parity spectral pairs and zero for opposite-parity pairs. The classification hypotheses ensure that this assignment is consistent, by Kang's collision theorem (arXiv:2609.14463v1); sufficiency is the candidate proof in the preceding manuscript. Since the frequencies are distinct and positive, their characters and inverse characters are pairwise distinct and nontrivial. Haar integrals of nontrivial characters vanish.

**Strengthening.** The preceding constructions give a conjugation-invariant phase probability nu that realizes E chi_w=y_w and dominates (1/100) h, uniformly in every admitted q. Domination is a measure inequality and does not require absolute continuity of the residual law.

Proof. For odd q coprime to 3 with q>=7, use Part I: Z<4210, G>=696 and E<=849/2 give (G-E)/(Z+G)>1/100 (in fact >1/20). For Part II the density denominator is T=-2mV. The shifted-polynomial test in `verify_uniform_floor.py` proves G-E_b-T/100>0 at all b>=4 when E_extra=0; G-E_b-E_extra-T/100>0 at all b>=16 using the general extra bound. The exceptional q=33,39 exact margins divided by T exceed 1/100; q=9 has Haar mixture weight 1/8; q=3 uses Haar. For even q>=10 not divisible by 3 both phase groups have at least two variables. For each bias b=0,1 and all n>=2 with no short relations, and all n>=35 with short relations, the script verifies

    (99/100)(-NU) - Z - 2n(|U-D|+|bU-W|) - Berr > 0,

where Berr is zero in the no-relation case. All four sign choices are checked as exact shifted polynomials. The minimum permitted N for each n suffices because -U>0. The finite 13 exceptions have their exact margins divided by -NU greater than 1/100 for each group. Thus each original group law nu_b dominates c h_b with c=1/100. To get a **joint** Haar floor c (not merely c^2), set rho_b=(nu_b-c h_b)/(1-c). Its nontrivial moments are scaled by 1/(1-c), and the unbiased group's first moments remain zero. The product rho_0 x rho_1 therefore scales the full target vector by 1/(1-c): same-parity coherences scale in their own group and cross-parity coherences remain zero. The joint law

    nu = c(h_0 x h_1)+(1-c)(rho_0 x rho_1)

has the target moments and dominates c h. This uses the exact parity-group product structure from Part III. For q=4,5,6,8 use Kang's phase ramp with lambda=1+1/(2N), mixed with Haar of weight 1-1/lambda=1/(2N+1)>c; for q=3 Haar suffices. Conjugation symmetry holds for the densities, or can be enforced by averaging a law with its inverse without changing any target cosine or domination. This proves the strengthening for every admitted q, conditional on the unified proof's relation inventory. No Lean proof was performed.

## 3. Complex Fourier interior ball and known timing noise

For any complex vector u indexed by Omega with sum |u_w|<c/2 define a correction to nu by adding the real signed Haar density

    2 Re sum_w u_w conjugate(chi_w).

It integrates to zero, is bounded in magnitude by 2 sum |u_w|<c, and changes each complex character mean by precisely u_w by Haar orthogonality. Thus the corrected probability remains positive and the entire open complex l1 ball of radius 1/200 about y lies in the phase-moment convex set. Treat complex coordinates as two real coordinates. Its center and every point in that open ball are interior points. The character criterion and transcendence of pi give density on every grid t0+delta Z_{>=0} for algebraic delta>0 as in the main manuscript. Since the relative interiors of a convex set and its closure agree, each such perturbed moment vector is realized by a finite actual time law. For complex moment constraints Caratheodory bounds the support by 2|Omega|+1, not the smaller real-moment bound. These are standard Fourier and convex-geometric arguments, now with a uniform constant provided by the candidate classification.

**Timing-noise corollary.** Suppose X is a known, real random readout error independent of the planned time T, with finite mean mu and variance sigma^2. If

    sigma <= 1/(25 sqrt(N)),

then every admitted path has a finite law for T on any prescribed nonnegative algebraic-step grid such that E M(T+X)=J/N. No symmetry assumption is required. For the centered error epsilon=X-mu, the characteristic function k_w=E exp(i w epsilon) obeys

    |k_w-1| <= w^2 sigma^2/2 <= 8 sigma^2,

by |exp(ix)-1-ix|<=x^2/2 and |w|<=4. In particular k_w!=0. First target the complex means y_w/k_w; only nonzero entries are changed. The number of distinct nonzero entries is at most choose(ceil(N/2),2)+choose(floor(N/2),2)<=N^2/4. Therefore

    sum_w |y_w/k_w-y_w| <= 2 N sigma^2/(1-8 sigma^2)
                         <= 2/621 < 1/200.

The strict bound uses N>=2. This lies in the open interior ball. Translation by phase -mu (a group element on H) corrects the deterministic mean and sends an interior point to another interior point, since character multiplication by exp(-i w mu) is an invertible linear isometry. Thus a finite actual grid law achieves means exp(-i w mu)y_w/k_w. By independence, the noisy means are exactly y_w. This proves the corollary. The time is dimensionless for adjacency Hamiltonian A; if the Hamiltonian is J A in units hbar=1, scale the physical time standard deviation by |J|. If physical actual times must be nonnegative, require the noise to be bounded below and choose a sufficiently late grid start; arbitrary unbounded negative noise cannot guarantee this. The law depends on the known distribution of X, not just its variance; this is not a fixed protocol robust to unknown noise. The result is conditional on the classification proof, and does not supply a practical waiting-time bound or a measured experiment. Kang already proves existence of absolutely continuous time laws for his constructive cases; do not claim that fact as new.

## 4. Review status and priority

Reopened the preceding unified proof in full, specifically all three conductor classifications and density/convexity sections. No contradictory short relation was found. The algebraic coset argument above supplies an independent reduction but the local classification, coefficient counts and the 14 finite-density evaluations remain essential. The numerical and symbolic checks in this round establish the stated uniform constants given those formulas, not the truth of every prior lemma. The full theorem has not been Lean-verified or externally reviewed. Existing P19 Lean arithmetic certification is a separate result. The revised manuscript's phrase 'full support is essential' should be changed to 'full support is sufficient for this relative-interior argument'; full support is not logically necessary for existence of a time law.

Priority check: re-opened Kang arXiv:2609.14463v1, 13 September 2026, and searched for random-time uniform mixing on paths and timing-noise robustness. No identical complete classification or quantitative result was located in these searches. This is limited search evidence, not proof of priority. The classical localization lemmas are explicitly credited to Lenstra/Conway–Jones. The proposed novelty is the path-specific construction and uniform margin, not the classical Fourier/convex tools.
