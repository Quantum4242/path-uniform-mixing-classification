# Effective finite readout windows and a further three-prime path certificate

Research note, 27 November 2026. No author assigned. AI-assisted, not independently peer reviewed, not fully Lean-formalized. Working supplement, not a public release.

## 1. Scope

For q=N+1>=3 let A be the adjacency matrix of P_N and M(t)=|exp(itA)|^{circ 2}. Uniform average mixing means that some probability law of t has mean M(t)=J_N/N. The full classification conjecture is unchanged: existence iff q is not divisible by 15 or 21, and not divisible by 6 with q>=12. The necessity and the classification of parity collisions are prior work (Kang, arXiv:2609.14463v1); sufficiency remains open in this project outside the families already constructed. This note adds a positive certificate for q=595 and an effective conditional readout-window theorem, not the general classification.

## 2. Exact certificate for P_594

For odd q=595=5*7*17, let m=(q-1)/2=297, zeta=exp(2 pi i/q), and alpha_j=zeta^j+zeta^(-j), j=1,...,m. Physical energies theta_(2j)=alpha_j, theta_(q-2j)=-alpha_j. A seed s in {0,1,2,3}^phi(q) gives a Q-linear functional on Q(zeta) by assigning (pi/2)s_k to zeta^k in the standard power basis. Its phase exponents are s dot V_j mod 4, where V_j are integer coefficients of X^j+X^(q-j) mod Phi_q. Every exact integer relation among physical energies is therefore satisfied by the assigned real angles. Kronecker's character theorem puts each seed phase in the time-orbit closure. Average each seed over the cyclotomic automorphisms given by units modulo 2q. They permute physical modes and preserve parity. The independent verifier reconstructs the full spectral pair orbits, not the floating optimization matrix.

With rows the orbit sums of cosines (integer values 0,+1,-1) and first row ones, B is a 608 by 608 integer matrix. The target y has first entry 1, same-parity orbit rows -|orbit|/(q-2), and opposite-parity orbit rows 0. The supplied integer certificate has scale Q=10^12, approximate inverse R=R0/Q and approximate weights u=u0/Q. Exact integer products and rational inequalities certify ||I-RB||_infty=e<1 and min(u)>||R||_infty ||y-Bu||_infty/(1-e). Therefore B is invertible, w=B^-1 y is strictly positive, and sum w=1. The resulting phase law has cosine moments -1/(N-1) on distinct same-parity modes, 0 on opposite parity modes. Verification covers 176121 unordered physical pairs. See verification595.log for exact fractions. The floating LP is discovery only. q=665 was attempted but no certificate obtained within the execution limit; no inference of nonexistence is made.

## 3. Effective readout-window theorem

Let lambda_1,...,lambda_m be one representative of each nonzero +/- pair of the path energies theta_r=2cos(r pi/q). Zero, if present, is fixed. Here m=floor(N/2). Let H be the closure of t lambda modulo 2 pi in T^m, and let F:H -> R^d be the vector of cosine moments indexed by distinct positive energy gaps. Each gap is represented by a character involving at most two of these coordinates, counting multiplicity. Let C=conv F(H). Suppose the desired vector y satisfies B_1(y,r) subset C for some explicit r>0, where B_1 is the open l1 ball. Let D=phi(2q)/2, an upper bound (indeed the degree of the real cyclotomic field) for the field containing every energy. All energies are algebraic integers and every conjugate has magnitude <=2.

**Theorem.** Choose 0<eta<=1 with 2d eta<=r/2 and an integer K>=1 such that

    K eta^2/4 > m log(2K+1)+log 4.

Set W=2mK, delta=1/W, and L=16 W^D (2K+1)^m. For every t0>=0, the finite convex hull of F((t0+n delta)lambda), n=0,...,L-1, contains the open l1 ball B_1(y,r/2). In particular y has a convex representation by at most d+1 of these samples, with strictly positive weights after zero weights are removed. The latest sample is bounded by t0+(L-1)/W. This result is conditional on the interior-margin hypothesis; it does not prove that all collision-free moduli have such a margin.

### Proof

Fix h in H. Define the nonnegative trigonometric polynomial

    K_h(x)=product_{j=1}^m ((1+cos(x_j-h_j))/2)^K.

In one variable the Fourier coefficients of ((1+cos x)/2)^K are binom(2K,K+a)/4^K for -K<=a<=K, all nonnegative, with sum 1. The central coefficient is the largest, hence >=1/(2K+1). The product has unshifted nonnegative Fourier coefficients c_a of sum 1 and support |a_j|<=K. Translation contributes e^(-i a dot h). The Haar integral on H kills all characters with a dot lambda !=0. For any zero-frequency character a dot lambda=0, its phase at h is 1 by continuity from the time orbit. Thus the Haar integral is at least c_0 >= (2K+1)^(-m)=c.

For any nonzero omega=a dot lambda in this support, |omega^sigma|<=2mK=W for every embedding of the real cyclotomic field. Its field norm is a nonzero integer, so |omega|>=W^(-(D-1)). At step delta, 0<|delta omega|<=1. The elementary inequality |1-exp(iu)|>=|u|/2 for |u|<=1 follows from sin(v)>=v/2 on [0,1/2]. The finite geometric series hence gives

    |(1/L) sum_{n=0}^{L-1} exp(i(t0+n delta)omega)|
       <= 4/(L delta |omega|) <= 4 W^D/L = c/4.

Zero frequencies have average 1, exactly their Haar value. Since the sum of absolute Fourier coefficients is 1, the sample average of K_h differs from its Haar average by at most c/4, and is >=3c/4.

If every sample has max_j |exp(i x_j)-exp(i h_j)|>=eta, at each sample some factor of the product is <=(1-eta^2/4)^K. All other factors are <=1. The choice of K implies the product is <c/4, a contradiction. Thus for each h there exists a grid point with every coordinate chord distance <eta. For each gap character, telescoping products of unit complex numbers bounds its cosine discrepancy by 2eta (also for doubled frequencies and for the fixed zero). The samples consequently form a 2eta-net in l-infinity norm for F(H).

Let C_grid be the finite sample hull. For each linear functional a in R^d, max_{C_grid} a dot x >= max_C a dot x -2eta||a||_1. The interior-margin hypothesis implies max_C a dot x >= a dot y + r||a||_infty, by taking the supremum over the open l1 ball. Since ||a||_1<=d||a||_infty, we obtain max_{C_grid} a dot x >= a dot y+(r/2)||a||_infty. The separating-hyperplane theorem gives B_1(y,r/2) subset C_grid. Caratheodory's theorem gives the support bound. This proves the theorem.

## 4. Applying the theorem to the stronger phase laws

For any phase law v with same-parity moments -a and opposite-parity moments zero, a>1/N, the desired vector is y=v/(Na). Distinct positive-gap cosines on H are orthogonal, have Haar mean zero and squared norm 1/2. The density 1+2 sum x_omega F_omega is nonnegative for ||x||_1<=1/2, so the zero-centered l1 ball of radius 1/2 is contained in C. Convexity then yields r=(1-1/(Na))/2. In particular if a=1/(N-1), r=1/(2N). This applies to the q=595 certificate and to earlier certificates with that stronger target. The path spectral projector identity D0=sum E_r^{circ2}=(2J+I+S)/(2q) and squared parity-projector sums=(I+S)/2 imply exactly M averaged=J/N at the target y. These identities use the standard sine eigenvectors and reversal S; also see Kang's forced-coherence lemma.

For an exact rational choice of K one can take successive powers of 2 until K eta^2/4 > m bit_length(2K+1)+2. This suffices because log(2K+1)<bit_length(2K+1) and log 4<2; the search terminates by exponential growth. effective_bounds.py computes these parameters using exact rational and integer arithmetic, and independently checks small Laurent polynomial cases. It does NOT simulate the astronomical grid. The bound is a mathematically explicit but extremely conservative worst-case guarantee, not an experimentally realistic mixing time. It depends on the chosen small rational sampling step and gives no comparable bound for a preassigned step delta=1. The qualitative existence on every positive algebraic step follows separately from Kronecker and transcendence of pi.

## 5. Lean verification update for the earlier P19 project

User-provided VS Code screenshots on 27 November 2026 display `Rows checked: 91/91`, `[3/3] All finite certificate theorems elaborated. Axiom audit:` and `'P19.allChecks' depends on axioms: [propext]`, with zero errors and zero warnings. In P19-online-matrix-fast.lean, allChecks combines globalOK, transposeOK and row00 through row90. This provides evidence of successful kernel checking of the finite integer certificate. propext is a standard Lean axiom. It does not verify the real trigonometric interval enclosure, the real linear algebra bridge, the spectral interpretation, the P19 main theorem, or the new results in this note. Screenshot-based audit; no independent local recompilation or checksum of the user's working copy was performed.

## 6. References and novelty limitations

Musung Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, arXiv:2609.14463v1 (2026), https://arxiv.org/abs/2609.14463. The positive construction there proves existence without specifying readout times (see main text and Theorem S24). Effective Kronecker approximation, Fourier kernels and algebraic norm estimates are standard tools; see also arXiv:1801.10179, On an effective variation of Kronecker's approximation theorem avoiding algebraic sets. The finite-window bound here is an application of these tools in the presence of an explicit moment-convexity margin. No exhaustive novelty claim is made. Targeted searches did not identify an identical application or a resolution of q=595, but this is not a proof of priority.
