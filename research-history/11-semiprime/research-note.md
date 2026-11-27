# Uniform average mixing on paths with odd semiprime moduli

## A complete candidate classification and a prime-power extension by column-block phase completion

Research record — 27 November 2026. No author assigned. AI-assisted. Not independently peer-reviewed or Lean-formalized. This is a working supplement, not a release to the public repository.

### Abstract

We combine a new phase law based on entire cyclotomic constraint columns, the previously developed spanning-tree phase construction, and eighteen exact rational certificates to classify odd semiprime moduli. For distinct odd primes p<r, the path P_(pr-1) admits uniform average mixing under a freely chosen distribution of readout times if and only if pr is neither 15 nor 21. The positive direction includes existence of finite readout laws on every positive algebraic time lattice, with arbitrary nonnegative initial offset. A new analytic construction also treats all odd moduli p^e r^f, e,f>=1, for r>=23. The latter is a sufficient condition, not a complete classification of these powers. All eighteen finite certificates are checked on 236591 original eigenmode pairs by exact arithmetic. The four small-prime threshold ranges are proved by positive-coefficient polynomial certificates. The general conjecture for arbitrary moduli remains unresolved.

## 1. Definitions and principal results

Let q>=3, N=q-1 and let A be the adjacency matrix of the N-vertex path. Write M(t)=|exp(itA)|^{circ 2}. Uniform average mixing means that a probability measure mu on real times satisfies E_mu M(t)=J_N/N. This is neither instantaneous mixing nor the fixed Cesaro mean.

Theorem A (odd semiprimes). For distinct odd primes p<r and q=pr, uniform average mixing exists if and only if q is not 15 or 21.

Theorem B (prime-power extension). If q=p^e r^f with distinct odd primes p<r, positive integers e,f, and r>=23, uniform average mixing exists.

In both positive results, for any real t0>=0 and any positive algebraic delta, there exist finitely many distinct nonnegative integers n_j and strictly positive weights w_j summing to one such that sum_j w_j M(t0+delta n_j)=J_N/N. At most ((q-1)/2)^2+1 readout times suffice. This is an existence result, not an explicit schedule or a bound on the largest time.

The negative direction in Theorem A is exactly a special case of Kang, arXiv:2609.14463v1, Theorem S18. Kang classified the parity-collision moduli (15|q, 21|q, or 6|q and q>=12) and gave positive results for certain other arithmetic classes. We do not claim the collision theorem as novel. Our new objective is the positive direction beyond those cases.

## 2. Spectral target and integer time bridge

For odd q write m=(q-1)/2, and alpha_j=2 cos(2 pi j/q), 1<=j<=m. The path eigenvalues theta_k=2 cos(k pi/q) are alpha_j at even k=2j and -alpha_j at odd k=q-2j. The closure H of t alpha modulo 2 pi is the compact torus subgroup whose integer annihilators are exactly the relations c dot alpha=0. Use z_j=exp(i phi_j) for phases on H.

It suffices to construct a law on H such that for some a>1/N,

    E Re(z_i conjugate(z_j))=-a for i!=j,
    E Re(z_i z_j)=0 for all i,j (including i=j).

After inserting the negative modes, the mean cosines of phase differences are -a for distinct same-parity eigenmode pairs and zero for opposite-parity pairs. At a=1/N this is the uniform mixing coherence target of Kang. To see sufficiency directly, let E_k be the spectral projectors and let S be the path reversal permutation matrix. The standard sine-eigenvector identities yield D=sum E_k^{circ 2}=(2J+I+S)/(2q); the sum of the two squared parity projector sums is (I+S)/2. Thus the target gives D-(1/N)((I+S)/2-D)=J/N.

The uniform Haar measure on H has zero mean for every distinct-mode cosine difference, since its frequency is nonzero. The vector of those means lies in the relative interior of C=conv F(H), where F is the vector of cosine differences. Indeed C is compact by Caratheodory's theorem and a supporting functional extremized at the Haar mean would be constant on F(H) by full support. Mixing the auxiliary law with Haar in proportions 1/(Na) and 1-1/(Na) gives the desired vector in ri C.

By algebraicity of the energies and of delta and transcendence of pi, the integer-character condition delta(c dot alpha) in 2 pi Z is equivalent to c dot alpha=0. Kronecker's character theorem shows that the nonnegative-integer orbit delta n alpha is dense in H (negative iterates are approximated by positive iterates by recurrence on a compact group). Translation by t0 alpha preserves H. The convex hull of the actual sample vectors therefore has closure C and the same relative interior as C, so the target belongs to the actual convex hull. Caratheodory, with at most m^2 distinct positive frequencies of forms 2 alpha_i or |alpha_i +/- alpha_j|, proves the support bound. This argument does not identify torus phase samples with actual readout times.

## 3. Cyclotomic column blocks

Take q=p^e r^f, p,r odd primes. Put h_p=p^(e-1), h_r=r^(f-1), H0=h_p h_r, P=(p-1)/2, R=(r-1)/2. Write CRT coordinates x=(u,v) in Z_(p^e) x Z_(r^f). A fiber box fixes u modulo h_p and v modulo h_r and has p by r entries. The root evaluations f(x)=ell(zeta^x), with zeta=exp(2 pi i/q) and ell a Q-linear functional from Q(zeta) to R, are precisely real arrays whose sum on every p-fiber and every r-fiber is zero. The forward direction is a geometric series; the reverse follows by dimension: each fiber box has (p-1)(r-1) degrees of freedom, hence total phi(q), equal to the dimension of the injective root-evaluation map.

Inversion sends each box to its opposite. Apart from the central box, the boxes form (H0-1)/2 disjoint pairs, and choosing one box in each pair allows arbitrary real zero-row-sum and zero-column-sum arrays in that box, then reflection. In the central box inversion identifies (u,v) with (-u,-v). The independent nonzero spectral coordinates comprise R columns of p coordinates (one coordinate for each row in a nonzero column representative), plus P axis coordinates y_a (row a on the zero column). Each nonzero column has a product-one constraint on its p phases. Each nonzero row imposes a product-one constraint on its axis y_a and the two corresponding entries in each of the R columns. No other constraints on these phases are needed: the remaining central entry (0,0) may be chosen to satisfy both the zero row and zero column, since the nonzero row and column sums vanish.

These statements apply to phase exponents modulo p as well. A modular zero-sum rectangle lifts to a real zero-sum rectangle by prescribing real lifts of its entries away from one row and one column, then solving the remaining row and column sums exactly. In the central box, independently adjust the row and column axis lifts by multiples of 2 pi to enforce each nonzero-row and nonzero-column constraint; then fill the (0,0) entry. Consequently every symmetric modular array constructed below corresponds to a symmetric real root-evaluation array, and any integral relation among alpha_j holds for its phases modulo 2 pi. Indeed 2 f(j)=ell(zeta^j+zeta^-j). Scaling the real functional by one half if necessary gives exactly the assigned angles. By the character description in Section 2 the constructed phase vectors belong to H. No assumption about a nonsaturated relation lattice modulo p is made.

### Reserve-column lemma

Choose three whole columns as reserves in each box (in the central box this refers to three of the R column representatives). All remaining columns are active; the central P axis coordinates are always active singleton nodes. Give every active column any phases that are p-th roots with product one, and give the singleton nodes arbitrary p-th roots. Completion exists. In an ordinary box, each column is a vector in the group V={x in (Z/pZ)^p: sum x=0}; any prescribed active columns can be completed by the reserved columns whose vector sum is the required residual. In the central box the map from V to (Z/pZ)^P sending a column to its P pair sums is surjective: choose the two entries of each row pair with the prescribed sum, and determine the axis entry by the column sum. Thus the reserved columns can complete every row equation. Uniformly sample from the finite affine solution set of reserves (independently for different boxes). Any one or two reserved columns have uniform independent V marginals conditional on all active data, because even after prescribing those columns the third can solve the residual equation. This is an exact counting statement, all fibers of the surjective group homomorphism have equal size. A uniform V column has uniform single entries and pairwise independent entries since p>=3. Consequently the reserve completion contributes zero to all first and second ordinary complex moments and all distinct-coordinate conjugate moments involving reserves. This includes two entries of the same reserve column.

## 4. New analytic law for odd semiprimes with small p

First take e=f=1, so only the central box occurs. Select three of its R columns uniformly as reserves (R>=5). Let alpha=(R-3)/R and beta=(R-3)(R-4)/(R(R-1)). These are the single and pair activation probabilities of columns. There are M=R-3+P active nodes: active columns and singleton axes.

For a prescribed auxiliary coherence magnitude a, let rho=(1-(p-1)a/alpha)/p. An active column is either aligned (its p entries are all the same p-th root) with probability rho, or balanced (uniformly permuted full list of the p roots) otherwise. Both choices have product one since p is odd. The conjugate expectation for distinct entries is 1 or -1/(p-1), respectively. With the reserved columns' zero moments the unconditional within-column moment is alpha*(rho-(1-rho)/(p-1))=-a. Uniform root rotations kill ordinary products and second moments.

Use one common Bernoulli switch with probability rho for all active nodes. If off, draw each column independently balanced and each singleton independently uniform. If on, align every active column; jointly assign their roots and the singleton roots as follows. Write M=kp+h, 0<=h<p. Take k copies of each p-th root, plus a uniformly chosen h-element subset of roots, uniformly permute these M entries, and rotate all by a uniform p-th root. For distinct nodes this gives conjugate moment -d, where

    d=(M-h(p-h)/(p-1))/(M(M-1)).

Proof: E|sum of the M roots|^2 = h(p-h)/(p-1) because the complete root lists sum to zero and each distinct pair among the h residual roots has conjugate mean -1/(p-1). Expand the square and use exchangeability. Global rotation kills all ordinary products, including diagonal ones (p odd). With probability lambda use this balanced assignment, otherwise independent uniform roots; the cross-node moment becomes -lambda d.

Column-column pair activation probability is beta, column-singleton alpha and singleton-singleton one. Equalize these by thinning singleton correlations, keeping each singleton assigned root with probability f=beta/alpha, and each distinct pair with joint keep probability g=beta; replace non-kept roots by independent uniform roots. Such indicators exist: f^2<=g<=f, since beta<=alpha^2 and alpha<=1. Mix independent Bernoulli(f) indicators with perfectly shared Bernoulli(f) indicators in proportion (g-f^2)/(f-f^2) for the shared law. This preserves all first and ordinary moments and gives a common effective factor beta for every cross-node conjugate moment. The thinning does not change column alignment or within-column moments.

Therefore all cross-node moments equal -rho beta lambda d; take lambda=a/(rho beta d). If at a0=1/(pr-1) the strict inequality beta rho(a0) d>a0 holds, then continuity gives a>a0 with valid rho,lambda. The reserve lemma and Section 2 complete the proof.

### All-parameter threshold certificate

At a=a0, beta rho/a0=(R-4)/(R-1)*(2(R-3)-3(p-1)/(pR)). With M=R+P-3 and h=M mod p, the inequality above is equivalent to positivity of

    (R-4)(2pR(R-3)-3(p-1))((p-1)M-h(p-h))
    - pR(R-1)(p-1)M(M-1).

For each p in {3,5,7,11}, split R into its p residue classes, let R=R_b+p t with R_b the smallest integer in that class no smaller than R0 and t>=0. The exact polynomial has all strictly positive coefficients in all 26 cases, checked by verify_columns.py (the actual polynomials are in columns-verification.log). The boundaries are (p,R0)=(3,8),(5,10),(7,12),(11,16). This is a finite symbolic certificate of the whole unbounded parameter range, not a numerical extrapolation. For prime r the bounds mean respectively r>=17,23,29,37.

## 5. Proof of the complete odd-semiprime classification

For p>=13 use the preceding research note, included as prior-tree-proof.md, Sections 4.1--4.3, independently rerun in tree-recheck.log: random three edge-disjoint spanning trees produce pairwise independent reserve completions; exact rational inequalities verified symbolically on P>=6,R>=8 prove the result for every p>=13 and r>p. The tree result also covers p=11,r>=37, though the new column law independently covers that range.

For p=3,5,7,11 the thresholds in Section 4 cover all primes r except the following finite list of positive cases (15 and 21 are excluded by the prior collision theorem):

    p=3:  q=33,39
    p=5:  q=35,55,65,85,95
    p=7:  q=77,91,119,133,161
    p=11: q=143,187,209,253,319,341.

All eighteen JSON certificates establish the strict auxiliary target a=1/(q-2). Nine are prior certificates, nine are newly generated. A seed is an integer linear functional on cyclotomic power-basis coefficients, with its values reduced modulo 4. Thus its fourth-root phase assignment satisfies every energy relation. Average each seed over all units modulo 2q, acting as parity-preserving permutations of the spectral modes, and weight the seeds by the listed positive rationals. The independent verifier uses exact polynomial remainders and checks all original mode pairs directly, without the LP orbit partition; each computed cosine is an integer in {-1,0,1}. Bounded int64 products only count those values; all final weighted sums use arbitrary-precision integers. The 18 checks total 236591 distinct-mode pair equations. Section 2 turns each auxiliary certificate into a genuine finite time law. This covers every remaining pair of distinct odd primes. Theorem A follows, conditional on the correctness of the displayed proofs and exact certificates. No Lean certification is claimed.

## 6. Arbitrary prime powers with sufficiently disparate primes

Now H0=p^(e-1)r^(f-1) and there are (H0-1)/2 additional ordinary boxes. In each reserve three columns independently and uniformly. The active node count is M=(H0(r-3)+p-5)/2. For a column group of size s (s=R centrally, s=r otherwise) set alpha_s=(s-3)/s, beta_s=(s-3)(s-4)/(s(s-1)), rho_s=(1-(p-1)a/alpha_s)/p. Use the common switch with probability rho=rho_R, which is the smallest rho_s. When it is on, align all active columns. Otherwise independently align a column of group s with probability (rho_s-rho)/(1-rho), and use an independent balanced permutation when it is not aligned. Singleton nodes in the off mode are independently uniform. Every column has the required internal moment, as before.

Set eta=(R-4)/(R-1). In the on mode use the joint root assignment of Section 4 on all M active nodes, with mixture parameter lambda. For each column group, conditionally on its active columns, keep their assigned roots with marginal f_s=eta/alpha_s and pair probability g_s=eta^2/beta_s; otherwise replace by independent uniform roots. Such thinning is possible because eta<=beta_s/alpha_s<=alpha_s, and beta_s<=alpha_s^2, giving f_s^2<=g_s<=f_s<=1. Use the independent/shared Bernoulli mixture within a group, independently across groups. Singleton nodes are independently kept with probability eta. For each pair of different nodes, the unconditional probability of both being active and kept is eta^2: within a group it is beta_s g_s, across groups it is the product of the two marginal effective keep probabilities eta. Therefore every cross-node moment is -rho eta^2 lambda d, so the sufficient condition is rho(a0) eta^2 d>a0 with a0=1/(H0 pr-1). Ordinary moments are zero and reserves complete all constraints as in Section 3.

For r>=max(41,8p), R>=20, alpha_R>=17/20, eta>=16/19. We have rho(a0)/a0=(H0 pr-1-(p-1)/alpha_R)/p >= H0 r-2 >= (39/41)H0 r. Also M<=9H0 r/16 and M>= (r+p-8)/2 >= (r-5)/2 >=7r/16. Since h(p-h)/(p-1)<=p^2/(4(p-1))<=3p/8<=3r/64, its ratio to M is at most 3/28. Thus d>=(25/28)/M. Combining all bounds,

    rho(a0) eta^2 d / a0 >= (256/361)(39/41)(16/9)(25/28)
                          = 332800/310821 > 1.

Choose a slightly greater than a0 by continuity and lambda=a/(rho eta^2 d). This proves Theorem B uniformly in both exponents, without numerical optimization.

### Sharpening the bound to r>=23

If e=f=1, Theorem A already covers r>=23. Otherwise H0>=p>=3. For r>=23, alpha_R>=8/11 and eta=(r-9)/(r-3). The previous estimate rho(a0)/a0>=H0 r-2 remains valid because 1/p+(p-1)/(p alpha_R)<=1/alpha_R<2. Moreover M<=(H0(r-3)+p)/2<=H0(r-2)/2, and M>=(H0(r-3)-2)/2. Thus c/M<=9/(12r-44) for c=p^2/(4(p-1))<=3p/8. From d>=(1-c/M)/M we obtain

    rho(a0) eta^2 d/a0 >= ((r-9)/(r-3))^2 (1-9/(12r-44)) 2(r-2/3)/(r-2).

This exceeds one for every r>=23: multiply by the positive denominator and write x=r-23>=0. The resulting numerator is exactly

    36 x^4 + 2070 x^3 + 39386 x^2 + 248672 x + 10472 > 0.

The exact expansion is independently checked in verify_columns.py. This removes any restriction on the relative size of p and r and establishes Theorem B as stated. The earlier disparate-prime bound is retained above as a redundant direct derivation.

## 7. Tests, priority, and unresolved cases

The new code checks all 26 shifted polynomial inequalities, the exact universal rational bound, the marginal and cross-node moment equations for representative parameters, and 21 independently completed modular arrays in seven factorization cases, checking fiber sums, inversion symmetry, and every cyclic cyclotomic recurrence equation. These tests supplement, not replace, the analytic proof. The finite certificates are a separate computer-assisted portion, using exact rational weights; all eighteen have been rerun on full original eigenmode pairs. Known negative cases 12,15,21,30 are used as controls, not new counterexamples. The full conjecture (absence of parity collisions is sufficient) remains open in this work; the new results prove it on odd semiprimes, and a larger class of two-prime powers. No claim that a failed sufficient inequality or finite LP infeasibility rules out mixing. No complete Lean proof or external peer review has been achieved. Targeted literature searches on 27 November 2026 for uniform average mixing with semiprimes, two distinct primes, and prime factors did not identify matching positive classification results; the search is not exhaustive and does not establish priority. For future publication verify again, and commission independent review of both column and tree arguments and the finite certificates.

References: M. Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, arXiv:2609.14463v1, https://arxiv.org/html/2609.14463v1 (in particular Theorem S18 and the coherence criterion). P. Baptista, G. Coutinho, V. Marques, Unexpected Averages of Mixing Matrices, arXiv:2308.16378, https://arxiv.org/abs/2308.16378. Standard results: cyclotomic irreducibility, Chinese remainder theorem, Kronecker character theorem, transcendence of pi, Haar probability, Caratheodory and relative-interior convexity theorems. Prior unpublished research note on overlapping cyclotomic constraints, included in this archive.
