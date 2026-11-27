# Uniform average mixing on odd-modulus paths by a nonnegative Fourier polynomial

Working research note — 27 November 2026. AI-assisted; no personal author assigned. Not independently peer-reviewed or Lean-formalized. This note gives a new candidate analytic proof, independent of the earlier random matching, reserve-coordinate, and finite LP constructions.

## Abstract

For the path on q−1 vertices, uniform average mixing under a freely chosen readout-time law requires a prescribed pattern of equal-parity and opposite-parity cosine moments. We construct a strictly positive finite Fourier density on the spectral phase group. Using the Conway–Jones bound for short rational relations among roots of unity, we show that for odd q with least prime divisor at least seven, the only short relations of relevant charge are the two signs of one central 7-by-11 axis relation, when 77 divides q. The associated Fourier leakage can be corrected with a positive remaining density. This proves uniform average mixing for every odd q coprime to 30. We also give an effective, very conservative asymptotic sufficient condition for odd q coprime to 3 (including the prime 5), and a finite physical-time grid construction with an explicit upper bound. The proof does not rely on large numerical optimization or any previous candidate existence theorem. The finite arithmetic checks in the companion script support the analytic argument and do not replace it.

## 1. Statements

Write N=q−1, A for the path adjacency matrix, M(t)=|exp(itA)| entrywise squared, and J for the all-ones matrix. A uniformly mixing law is a probability measure mu with E_mu M(t)=J/N. It is not a fixed Cesaro average or instantaneous uniform mixing.

**Theorem A.** For every integer q≥3 with gcd(q,30)=1, there exists a finite readout-time law giving uniform average mixing on P_(q−1). There is no restriction on the number or powers of prime factors.

**Theorem B.** Put B=5·7·11·13·17·19=1616615, C=100464, C0=3(6B)^10, and M0=2CC0. If q is odd, 3 does not divide q, and m=(q−1)/2≥M0, then P_(q−1) admits uniform average mixing. This bound is deliberately crude: M0 is approximately 4.44×10^75. It has asymptotic significance, not a practical size threshold, and it does not resolve the smaller cases involving the prime 5.

**Theorem C.** Under the assumptions of A or B, set m=(q−1)/2 and D=phi(q)/2. For every t0≥0, define L=20000(m²+1)m^4·20^D. There is a uniformly mixing law supported on {t0+j/20: 0≤j<L}; at most m²+1 times suffice. Thus t_max≤t0+(L−1)/20. This upper bound is also very conservative. The theorem is a finite existence and search-window guarantee, not an efficient protocol-generation algorithm.

These statements are positive existence results, not a classification of all q. The known negative conditions in Kang (2026) are not new contributions of this note.

## 2. Spectral target and Fourier notation

For odd q put m=(q−1)/2, alpha_j=2 cos(2 pi j/q) for 1≤j≤m. The physical eigenvalues 2 cos(k pi/q) are alpha_j at even k=2j and −alpha_j at odd k=q−2j. The alpha_j need not be positive. Let H be the closure of t alpha modulo 2 pi, a compact subgroup of the m-dimensional torus, with Haar probability h. Put z_j=exp(i phi_j) and chi_u=z^u for u in Z^m. Define Lambda={u:u·alpha=0}; the Haar integral of chi_u is 1 on Lambda and zero otherwise, by invariance and density of the defining orbit. Define charge Q(u)=sum u_j and length |u|_1=sum |u_j|.

The following moments suffice (and are also necessary by Kang's forced-coherence lemma):

    E Re(z_i conjugate(z_j)) = -1/(2m), i≠j,
    E Re(z_i z_j) = 0, all i,j, including i=j.

They give −1/N for the cosine of the difference of distinct physical phases with the same mirror parity, and zero for opposite parity. For completeness, the path sine eigenvectors yield D0=sum E_k^{circ2}=(2J+I+S)/(2q), where S is reversal. The two parity projector sums are (I±S)/2, and the sum of their entrywise squares is (I+S)/2. Inserting the target moments into the spectral expansion of M gives D0−((I+S)/2−D0)/N=J/N. We use this prior spectral identity, not claim it as new.

Use one representative of each target character up to sign in V={e_i−e_j:i<j} union {e_i+e_j:i≤j}. It has m² elements. Each has length 2. Under the hypotheses below, there is no nonzero relation of even length at most 4. Hence these characters are all nontrivial and distinct modulo Lambda up to sign. The cosines are pairwise orthogonal under h, with squared norms 1/2. We prove the absence of these short relations in Section 4.

## 3. A universal polynomial on the unconstrained torus

Let X=|sum_j z_j|²/m, P(X)=100−60X+7X², and F=P(X)². This is nonnegative on the entire torus. All its Fourier monomials have charge zero and length at most 8. Let E_* denote integration over m independent Haar circles, Z=E_* F, Y=E_* XF. The moment formula

    E_* X^k = (k!)²/m^k [t^k](sum_{j=0}^k t^j/(j!)²)^m

follows from counting equal occupancy numbers in the two multinomial expansions. The first six moments are

    1, 1,
    2−1/m,
    6−9/m+4/m²,
    24−72/m+82/m²−33/m³,
    120−600/m+1250/m²−1225/m³+456/m^4.

The exact normalizing and first tilted moments are

    Z=(4136m³−968m²+658m−1617)/m³,
    Y=(1720m^4−1920m³+12370m²−32305m+22344)/m^4.

By permutation symmetry, and global phase invariance of the unconstrained density F/Z, its distinct conjugate moments all equal (Y/Z−1)/(m−1), and its ordinary products all have expectation zero. Thus it generates a strictly stronger negative moment than the target if (m+1)Z−2mY>0. In fact

    (m+1)Z−2mY = 3(m−1)T(m)/m³,
    T(m)=232m³+2568m²−5782m+15435.

For m≥2, setting x=m−2 gives T=232x³+3960x²+7274x+15999>0. For m≥3, T≥232m³, 3000<Z<4210 and Y≥0. Put tau=(m−1)Z/[2m(Z−Y)], so 0<tau<1. On the unconstrained torus the strictly positive density tau F/Z+(1−tau) gives exactly the target. Its slack in units of the unnormalized polynomial is

    G= Z(1−tau)/tau = 3T(m)/m³ ≥696  (m≥3).

The companion code derives the moments by integer partitions, independently expands Laurent polynomials for four small m, and checks the identity exactly.

## 4. Arithmetic input: short relations

We use Mann's theorem on minimal rational relations among roots of unity (1965) and its strengthening by Conway and Jones (1976, Theorems 1 and 5). If a minimal rational relation on l distinct roots has reduced conductor d (least common order of ratios of its terms), then d is squarefree and l≥2+sum_{p|d}(p−2). In particular each prime dividing d is at most l. The original Conway–Jones theorem has been checked in the scanned paper, Acta Arithmetica 30, pp. 230–237 (Theorem 5 at p. 235). We use the signed rational-coefficient version: coefficients may be negative, and l is support size, not necessarily the sum of absolute coefficients.

Take c in Lambda and write zeta=exp(2 pi i/q). The relation sum c_j (zeta^j+zeta^(−j))=0 is a symmetric rational coefficient array on Z/qZ, with no coefficient at 0, integer coefficients, even support size, and support size at most 2|c|_1. Decompose its support into disjoint minimal vanishing subrelations by repeatedly removing a minimal vanishing subset with its original coefficients. For each block its reduced conductor divides q, so it lies in a coset of the corresponding subgroup of roots. If the reduced conductor is a single prime p, the block is the full p-cycle, with all coefficients equal, by irreducibility of Phi_p. The conductor cannot be 1 for a nonempty relation of distinct roots.

If all prime divisors of q are ≥5, there cannot be a nonzero c of even length ≤4. Its root support would have size at most 8; at most one block is possible, since two would need at least 10 roots. A block with two prime divisors needs at least 5+7−2=10 roots. A single-prime block has odd support size, contrary to inversion symmetry. This proves the character orthogonality asserted in Section 2.

### Short low-charge relations when all primes are ≥7

**Lemma.** If all prime factors of q are ≥7, then every nonzero c in Lambda with even |c|_1≤10 and Q(c) in {0,±2} is one of the two signs of the central axis relation c*, which exists only when 77|q. It has five +1 entries at j=q/11,2q/11,...,5q/11 and three −1 entries at j=q/7,2q/7,3q/7. In particular Q(c*)=2 and |c*|_1=8.

Proof. The root support has size at most 20. By Conway–Jones, every minimal block has either a single-prime conductor, or the conductor 7·11 or 7·13: any other product of two primes ≥7 has bound >20, and a product of three has bound >20. A mixed block needs at least 16 roots and hence must be the sole block (another needs at least 7). If all blocks are prime cycles, there can be at most two; one alone is impossible by even support. Two cycles of unequal primes cannot form an inversion-invariant support. Indeed the inverse of the first cycle is either the same coset of its subgroup or disjoint from it, and in the latter case meets the other prime cycle in at most one point. In the former case, an inversion-invariant coset in this odd cyclic group contains the identity, which is forbidden. Two cycles of equal prime length must both have length seven, must be swapped by inversion, and have equal nonzero integer coefficients. Their charge in c is therefore a nonzero multiple of seven, which is excluded.

Now suppose the single block has conductor 7r, r=11 or 13. Its support lies in a coset of the subgroup of order 7r; by symmetry this coset must be the subgroup itself (in the odd-order quotient, 2x=0 implies x=0). Use CRT coordinates on this subgroup and let A_(i,j) be its coefficient array. The kernel of rational root evaluation on a 7×r array consists precisely of A_(i,j)=a_i+b_j: all such arrays vanish by summing complete prime cycles, and they form a space of dimension 7+r−1, equal to the kernel dimension 7r−phi(7r). Because A_(0,0)=0, choose a_i=A_(i,0), b_j=A_(0,j), with a_0=b_0=0. Inversion gives a_i=a_(-i), b_j=b_(-j); hence the numbers u and v of nonzero a_i and b_j are even. Both must be positive, or the minimal block would have single-prime conductor. The support size is at least u(r−v)+(7−u)v, counting the regions with just one nonzero summand. The only even choices 2≤u≤6, 2≤v≤r−1 with this bound ≤20 are u=6 and v=r−1 (enumerated in the companion checker). Their baseline is r+5, namely 16 or 18.

Any nonzero entry in the intersection of the nonzero row and column groups occurs in a four-entry block, because of separate sign symmetry. For r=13 there is no room for such a block. For r=11 there is room for at most one four-entry block, but an additive matrix cannot have a single nonzero cell on the 3×5 matrix of row-pair/column-pair sums: the vanishing of the other three corners of any rectangle forces that cell to vanish. Thus every intersection entry is zero, so all nonzero a_i equal a common integer A, and all nonzero b_j equal −A. The spectral vector is an axis difference, with norm (r+5)|A|/2. Since this norm is at most 10, |A|=1. When r=13 its norm is nine, which is odd; when r=11 it is eight and its charge is ±2. The relation really holds because each of the two nonzero root axes sums to −1. This proves the lemma. QED.

## 5. Fourier correction and proof of Theorem A

Let Fhat(u) be the real Fourier coefficient of F at u; Fhat(−u)=Fhat(u), and it vanishes outside charge zero and length at most eight. For v∈V define

    E_v = integral_H F Re chi_v dh − integral_* F Re chi_v,
    E_0 = integral_H F dh − Z.

By character orthogonality these are respectively sums of Fhat(c−v) over nonzero c∈Lambda, and of Fhat(c) over nonzero c∈Lambda. (The cosine equals the real part of the character; inversion makes the integrals real.) Only even |c|_1≤10 and charge Q(c)=Q(v) occur, with v=0 for normalization. The lemma shows that E0=0, and that E_v=0 for conjugate-pair characters. If 77 does not divide q all E_v vanish. Otherwise for v=e_i+e_j, E_v=Fhat(c*−v). No other relation contributes.

Define the corrected polynomial density on H by

    f= tau F/Z + (1−tau) − tau E0/Z
       − (2tau/Z) sum_{v∈V} E_v Re chi_v.

Its mean is one, and it has exactly the target moments by the orthogonality established in Section 4. It remains to prove positivity. Suffices that E=|E0|+2 sum |E_v| < G=Z(1−tau)/tau.

For 77|q write m≥38. For balanced u of length 2h, the Fourier coefficient of X^j equals

    (j!)²/m^j · sum_{l_i≥0, sum l_i=j−h}
      prod_i [1/((u_i^++l_i)!(u_i^−+l_i)!)]

when h≤j, and zero otherwise. There are at most m^(j−h) terms in the sum, and each is at most one. F=10000−12000X+5000X²−840X³+49X^4. Thus when h=3, |Fhat(u)|≤58464/m³, and when h=4, |Fhat(u)|≤28224/m^4. For c*−e_i−e_j, h=3 if i,j are distinct among the five positive coordinates (ten possibilities); h=4 if only one unit of the two is cancelled (at most 5m possibilities, including equal indices); otherwise h=5 and the coefficient vanishes. It follows that

    sum_{v∈V}|E_v| ≤ 725760/m³.

Consequently E≤1451520/38³<696≤G. This proves strict positivity, hence exact feasibility of the target on H. The physical readout law follows from Section 7; no identification of auxiliary phase samples with real times is made. This proves Theorem A. The checker evaluates the actual correction coefficients by exact rational factorial series for q=77,539,1001, rather than just checking the displayed upper bound.

## 6. Coarse uniform asymptotic theorem including the prime 5

Assume all prime divisors of the odd q are ≥5. The no-even-relation-through-length-four lemma still applies. Therefore in E0 and E_v only nonzero relations c with |c|_1=2k, k∈{3,4,5} contribute. The short-relation count below is deliberately loose but independent of the factorization and of q.

Put Bq=gcd(q,B). By Mann, every minimal block of a root relation of support size≤20 lies in a coset of the subgroup of order Bq. Grouping blocks by cosets shows that the restriction to each occupied coset is itself a nonzero vanishing relation. Each occupied coset contains at least five distinct roots, again by Mann (a minimal relation on fewer than five roots would have no possible prime in its reduced conductor). Inversion pairs noncentral cosets. A pair of occupied noncentral cosets uses at least five spectral coordinates in c, since each spectral coordinate contributes exactly one root to each of the paired cosets. Hence at most l=floor(2k/5) such pairs can occur. There are at most m choices of a coset pair, and at most (l+1)m^l choices of at most l pairs. After the cosets are chosen, the available spectral indices lie in these pairs and the optional central coset, at most (l+1)B≤3B coordinates. An integer vector of length 2k on such a set can be written as a sum of 2k signed coordinate unit vectors. Therefore the number of possible c of length 2k is bounded by

    C0 m^l,   C0=3(6B)^10.

This is a bound on all relations, without charge restriction, not an exact count. For a balanced u of length 2h, the coefficient formula in Section 5 gives |Fhat(u)|≤C/m^h, C=sum_{j=0}^4 |[X^j]F|(j!)²=100464. The same bound holds if u is unbalanced (the coefficient then vanishes). Coefficients vanish when h>4.

For any c of length 2k, classify v∈V by d=(|c|_1+2−|c−v|_1)/2∈{0,1,2}, the number of units cancelled. There are at most m² v with d=0, at most 40m with d=1 (choose one of two positions, a signed coordinate from c, and the other signed coordinate), and at most 100 with d=2 (both from the at most 10 signed units of c). Since |c−v|_1=2(k+1−d),

    sum_{v∈V} |Fhat(c−v)| ≤ 141 C/m^(k−1).

The possible normalization contribution is at most C/m^k. Summing the bounds gives

    E=|E0|+2 sum |E_v| ≤ 283 C C0 sum_{k=3}^5 m^(floor(2k/5)−k+1)
      ≤ 849 C C0 /m.

If m≥M0=2CC0, then E≤849/2<696≤G. The same corrected density is strictly positive and realizes the target. This proves Theorem B using Section 7. The threshold is so large that this is not a useful test of a given small graph. A sharper count of small signed relations, or adapting F to the prime 5, is a clear opportunity for future work. For the prime 3 the displayed count no longer decays for k=3, so this proof cannot be extended to that case without a new argument.

## 7. Direct finite physical time-grid proof (Theorem C)

This section avoids relying on qualitative or quantitative Kronecker approximation to realize the corrected density as a real readout law. All preceding results give a strictly positive Fourier polynomial f on H of degree (Fourier length) ≤8. We record uniform bounds. For m≥3, Z<4210 and Y≥0 imply 1−tau≥696(m−1)/(8420m)≥1392/25260. In both Theorem A and B, E≤849/2: this is immediate from the bound for B, and for A from the sharper 77 estimate (or E=0). Since G≥696, f≥(1−tau)(1−E/G)>1/50. The l1 norm S_f of its full-torus Fourier coefficients is at most (sum |[X^j]F| m^j)/Z+2, since the l1 size of X is m, the correction has size at most tau E/Z<1−tau, and tau<1. The sum of absolute polynomial coefficients is 27889, Z>3000, hence S_f≤12m^4. These are exact rational inequalities checked in the companion code.

Let D=phi(q)/2. Any nonzero frequency beta=u·alpha with |u|_1≤10 is a nonzero algebraic integer in the real cyclotomic field of degree D. Every conjugate has modulus at most 20. Its field norm is a nonzero rational integer, so |beta|≥20^{−(D−1)}. On a time grid t_j=t0+j/20, the geometric sum estimate and |1−exp(ix)|≥|x|/2 for |x|≤1 give

    |(1/L) sum_j exp(i beta t_j)| ≤ 4·20^D/L = eps_L

for all such nonzero beta. Zero frequencies average to one, exactly as under Haar. The same bound times the Fourier l1 norm controls the error for any polynomial of length at most 10.

Set h_0=1 and h_v=Re chi_v for v∈V, evaluated at t_j alpha. Let b=(1, target moments). Define the empirical Gram matrix G_L=(1/L)sum_j h(t_j)h(t_j)^T. Its Haar counterpart is diag(1,1/2,...,1/2). Each entry differs by at most eps_L. With n=m²+1, if n eps_L≤1/4, a Neumann bound (or elementary maximum-row-sum argument) gives invertibility and ||G_L^(−1)||_infty≤4. The residual e=b−(1/L)sum f(t_j alpha) h(t_j) has ||e||_infty≤S_f eps_L. Put c=G_L^(−1)e. Then the weights

    w_j=(f(t_j alpha)+c·h(t_j))/L

satisfy the required moments and normalization exactly. The correction in each numerator is bounded by 4n S_f eps_L. Choose L=20000 n m^4 20^D, so eps_L=4/(20000 n m^4). Then n eps_L≤1/4 and 4n S_f eps_L≤192/20000<1/100. Since f>1/50, all w_j are positive. This establishes a finite real time law, rather than only a torus law. Caratheodory (or eliminating affine dependencies) reduces the support to at most m²+1 times in the same grid. This proves Theorem C and completes A and B. No full grid of this enormous size was actually enumerated, and the inverse is a mathematical definition of exact real weights, not a reported numerical solution.

## 8. Audit, originality and next directions

This note is independent of earlier candidate general theorems. The main new idea is a fixed degree-eight nonnegative Fourier polynomial coupled with a rigorous correction of resonant low-order moments. Existing results used are the spectral target (Kang), root-of-unity relation theorems (Mann and Conway–Jones), Fourier orthogonality, and standard convex/linear algebra. The positivity polynomial was selected using a small numerical moment-matrix optimization, but its displayed integer coefficients and final proof do not rely on numerical optimization. Exact verification uses SymPy and Python fractions. No complete Lean proof or external review has been performed. The short-relation lemma and the uniform asymptotic counting argument should be checked independently before publication. The full classification remains unresolved; even moduli and odd multiples of 3 are not addressed by this note, and the asymptotic threshold for the prime 5 is intentionally very conservative. No new nonexistence example was found.

Targeted searches on 27 November 2026 combined uniform average mixing, paths, least prime factors, Fourier/Haar moments, short relations, cyclotomic phase and GitHub. Kang arXiv:2609.14463v1 was reopened; its Outlook explicitly leaves moduli outside its two families unresolved. We found a recent related paper (Benoist et al., arXiv:2611.12701v1, Nov. 9) using Mann's theorem for one-particle energy resonance multiplicities and thermalization on periodic free-fermion lattices. It is relevant mathematical precedent but its theorem is a different physical question. The old Conway–Jones theorem was read in the original scan. Search results did not reveal the same density construction or the positive theorem for all odd moduli coprime to 30. Search is not exhaustive and cannot guarantee priority. No public GitHub repository was modified in this turn.

## References

1. M. Kang, *Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains*, arXiv:2609.14463v1 (2026), https://arxiv.org/html/2609.14463v1.
2. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378 (2023), https://arxiv.org/abs/2308.16378.
3. H. B. Mann, *On linear relations between roots of unity*, Mathematika 12 (1965), 107–117, https://doi.org/10.1112/S0025579300005210.
4. J. H. Conway, A. J. Jones, *Trigonometric diophantine equations (On vanishing sums of roots of unity)*, Acta Arithmetica 30 (1976), 229–240, Theorem 5, https://doi.org/10.4064/aa-30-3-229-240, scanned text https://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3033.pdf.
5. T. Benoist, V. Jakšić, C.-A. Pillet, A. Szczepanek, C. Vogel, *One-Particle Resonances and Eigenstate Thermalization in Periodic Free-Fermion Lattices*, arXiv:2611.12701v1 (2026), https://arxiv.org/html/2611.12701v1.
6. C. Godsil, *Average mixing of continuous quantum walks*, J. Combin. Theory Ser. A 120 (2013), 1649–1662, https://arxiv.org/abs/1103.2578.
