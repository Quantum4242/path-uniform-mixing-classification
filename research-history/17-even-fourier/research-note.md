# Uniform average mixing on every path: an even-modulus Fourier construction and a candidate complete arithmetic classification

Working research record, 27 November 2026. AI-assisted. No personal author assigned. Not independently peer-reviewed or fully Lean-formalized. The public GitHub repositories have not been modified.

## Abstract

Let q=N+1>=3. We study uniform average mixing (UAM) of the continuous-time adjacency walk on P_N with an arbitrary readout-time probability law. This note supplies a candidate proof that every even q not divisible by 3 admits UAM. Its main contribution is a degree-eight nonnegative Fourier polynomial involving both the sum of real phase components and the sum of their double-angle cosines. The positive-energy phase group separates into two mirror-parity groups. An exact symbolic moment calculation gives a strictly positive correction budget on the independent torus. A projective version of the Conway–Jones short-relation analysis bounds the departure from independent moments uniformly when a parity group has at least 35 coordinates. Thirteen small even moduli are covered by exact rational phase certificates. Together with the two preceding odd-modulus proofs (included in prior-odd/), and Kang's known negative cases, this supplies a candidate classification for every path, without any remaining arithmetic case. The combined theorem inherits the earlier odd proofs and their review obligations.

## 1. Statements

**New even-modulus theorem.** For every even q>=4 with 3 not dividing q, P_(q−1) admits UAM. Moreover, for every positive algebraic real sampling step delta and nonnegative starting time t0, a finite probability law supported on t0+j delta, j a nonnegative integer, realizes exact UAM. The support has at most m(m+1)+1 points, where m=q/2−1. These are upper bounds, not minimality claims.

**Combined candidate classification.** For all q>=3, P_(q−1) admits UAM if and only if neither 15 nor 21 divides q and it is not the case that 6 divides q with q>=12. Necessity and the positive prime, twice-prime, and power-of-two families are prior results of Kang, arXiv:2609.14463v1. The odd positive direction is supplied by prior-odd/research-note.md and prior-odd/prior-odd-coprime/research-note.md. The new even direction is proved below; q=6 is twice a prime. The classification is a candidate theorem pending independent review of all three notes, not a claim of a published or fully formalized result.

## 2. Spectral reduction and independent parity groups

The eigenvalues of the adjacency matrix A of P_N are theta_r=2 cos(r pi/q), 1<=r<=N, with real projectors E_r from normalized sine eigenvectors. If y_rs=E cos((theta_r−theta_s)T), the mean mixing matrix is D0+2 sum_{r<s} y_rs E_r∘E_s. The standard sine sum gives D0=(2J+I+S)/(2q), where S is the reversal matrix. The sum of the two squared parity-projector sums is (I+S)/2. Thus it suffices to realize y_rs=−1/N for distinct indices of the same parity and zero otherwise. The resulting matrix is D0−[(I+S)/2−D0]/N=J/N. The criterion and its necessity are due to Kang, not new here.

For even q=2h there are h−1 positive modes r=1,...,h−1, their negatives at q−r, and a zero mode at r=h. Let H be the closure of the continuous phase flow of the positive modes. Its integer relation lattice Lambda consists of c with sum c_r theta_r=0. Put z_r=exp(i phi_r). The character form of Kronecker's theorem says H is precisely the common kernel of the characters in Lambda. The automorphism of Q(zeta), zeta=exp(pi i/q), sending zeta to −zeta (valid since gcd(q+1,2q)=1) sends theta_r to (−1)^r theta_r. Every rational relation therefore splits into its even and odd parts; the integer relation lattice likewise splits. H is the direct product of its two parity phase groups. We construct independent phase laws on these two groups.

In a group of n positive coordinates write b=1 if its parity is that of the zero mode, and b=0 otherwise. Set a=1/N. Required moments are

    E cos phi_i=−b a,
    E cos(2 phi_i)=−a,
    E cos(phi_i+phi_j)=E cos(phi_i−phi_j)=−a for i<j.

Conjugation-symmetric laws have zero sine means. Independence between groups, and the zero cosine means in the b=0 group, make all cross-parity moments zero. Negative modes receive the opposite phase and the zero mode phase zero; hence the listed requirements cover all full spectral pairs. Counting parity sizes gives N>=4n−1 for b=0 and N>=4n+1 for b=1. Indeed if h=2l the group sizes are l (unbiased) and l−1 (biased), and N=4l−1; if h=2l+1 both sizes are l and N=4l+1.

## 3. A nonnegative low-degree density and exact independent-circle moments

In one group define C_i=cos phi_i, S0=sum C_i, T2=sum cos(2 phi_i), X=2(S0+b/2)^2/n, and

    F=[10000−3707 X+254 X^2−1336 T2/n]^2.

It is nonnegative pointwise. On the full independent torus its Fourier monomials have l1 length <=8. It is permutation-symmetric and invariant under individual sign reversals of the phase angles. Let Z=E_*F, U=E_*F C_1 C_2, D=E_*F cos(2 phi_1), W=E_*F C_1, where E_* denotes independent uniform angles. The same U is E_*F cos(phi_1±phi_2), because the sine product integrates to zero. The following exact formulas are derived by coefficient extraction in verify_low_degree.py.

For b=0:

    2 n^3 Z = 121704774 n^3−4750735 n^2+11341862 n−18628995
    n^4 U = −2(9427103 n^3+9607186 n^2−29923359 n+64354710)
    2 n^4 D = −(37705166 n^3+15783578 n^2−43863387 n+51483768)
    W=0.

For b=1:

    4 n^4 Z=243409548 n^4−47209882 n^3+26186325 n^2−7941564 n+16129
    n^4 U=−(18854206 n^3+6845765 n^2−40652319 n+60741814)
    2 n^4 D=−(37705166 n^3+498483 n^2−25384760 n+18516092)
    n^4 W=−(18854206 n^3+5639384 n^2−32204787 n+28870910).

To reproduce these formulas, define a truncated bivariate series B_j(t,u) whose coefficient at t^k u^l is E[C^k (2C^2−1)^l cos(j phi)]/(k!l!), with 0<=k<=8 and 0<=l<=2, C=cos phi and phi uniform. The cosine moments used in it follow from E[C^k exp(i j phi)]=2^(−k) binomial(k,(k−j)/2) when k>=j and k−j is even, zero otherwise. The four marked moment series before multiplying by exp(bt/2) are B_0^n, B_0^(n−2) B_1^2, B_0^(n−1) B_2, B_0^(n−1) B_1. Write P(X)=10000−3707X+254X^2 and B=−1336. Use F=P(X)^2+2B P(X)T2/n+B^2 T2^2/n^2. For a term X^j T2^l extract coefficient t^(2j)u^l, multiply by (2j)!l! (2/n)^j. Symbolic powers of B_0 are evaluated by the finite binomial expansion in B_0−1 (weighted degree at least two, weight of u two). This proves the displayed rational formulas for every integer n>=2 rather than fitting finite samples.

Let G=−NU−Z. Exact polynomial expansion with n=2+x gives Z>0, U<0 and, for b=0,1 and all n>=2,

    G−2n(|U−D|+|bU−W|) > 14500000.                 (1)

For this check use the smallest N for the corresponding parity group, 4n−1 or 4n+1, since U<0. To verify the absolute-value inequality, check all four expressions G−2n[s(U−D)+t(bU−W)]−14500000 for s,t in {−1,1}. Each has a positive constant numerator and nonnegative numerator coefficients after shifting n=2+x, and a strictly positive denominator; all eight checks are asserted in the script. Thus the unnormalized density has an absolute correction budget independent of n. The numerical choice of integer coefficients was informed by a preliminary optimization, but the proof uses only the explicit polynomial and exact algebra.

## 4. The phase lattice: all short relations relevant to this density

Only integer relations c of length |c|_1<=10 can affect normalization or a moment of length <=2. In this section assume 3 does not divide the even modulus q, so its odd primes are >=5. Work in one parity group of positive indices. Write a relation as an integer root array on exponents ±r, using coefficient c_r at both r and −r. Its support is inversion-symmetric and has size at most 2|c|_1; its absolute weight is exactly 2|c|_1.

### 4.1 Projective reduction

Project exponents modulo q, identifying antipodal roots of order 2q (the two roots differ by a sign). No two supported exponents are identified: the chosen range −h<r<h has diameter q−2. The two fixed points of inversion, 0 and h, are absent. Each root coefficient keeps its absolute value, and a sign may be absorbed into the coefficient when changing lifts. Partition the root support into disjoint minimal vanishing subsets, retaining the original coefficients. The Conway–Jones bound (Theorems 1 and 5, 1976, p.235) gives a squarefree reduced exponent and support at least 2+sum(p−2) over its distinct prime divisors. After projective reduction the conductor d is odd and squarefree, and the block lies in a coset of the subgroup of order d of Z/q. Indeed the possible factor 2 becomes a sign, and dropping it leaves the support bound unchanged. For odd d, choose a lift of any such coset as zeta^a times all d-th roots. Ratios and coefficients can be adjusted by signs, without changing the absolute weight or vanishing property. A prime-conductor block consists of a complete prime cycle with a constant signed coefficient in this lift.

An inverse-stable coset of an odd-order subgroup contains exactly one of the two fixed points 0,h. In a central coset containing 0, the lifted coefficient array is symmetric under inversion; in the central coset containing h, use zeta^h=i as a common factor and the lifted array is antisymmetric, because inversion conjugates i to −i. For noncentral inverse coset pairs, the arrays correspond by conjugation up to a common sign and have equal absolute weight. These facts are why the even case needs an additional antisymmetric analysis compared with the odd proofs.

A nonzero relation of length <=4 cannot occur: its support is even and <=8, so there is at most one minimal block; a mixed odd conductor needs >=10 entries, and a pure prime cycle has odd support. This also holds if all odd primes are absent. In particular all characters in V={e_i,2e_i, e_i±e_j (i<j)} are nontrivial and pairwise distinct up to sign modulo Lambda. Their real cosines are orthogonal under Haar measure, with squared norm 1/2.

If every odd prime factor is >=11, the same reasoning rules out all nonzero relations of length <=10: two minimal blocks need at least 22 entries, a mixed conductor needs at least 22, and a sole prime cycle has odd support. In that case all moments in Section 3 are exactly the actual Haar moments and no extra correction is necessary.

### 4.2 Pure cycles

For general odd primes >=5, the support bound allows at most four minimal blocks. If all are pure prime cycles, inversion pairs cycles with other cycles of the same prime. To see this, the inverse coset cannot equal the original one (it would contain an excluded fixed point). If it did not coincide with another same-prime coset, it could meet each of the at most three other blocks in at most one point, insufficient to cover its >=5 points. Equal absolute coefficients follow by symmetry of the original root array. An inverse pair of p-cycles contributes p|A| to the spectral length, where A is a nonzero integer. Distinct inverse pairs of p-cycles have disjoint spectral supports, at most n/p in a parity group. Therefore the possible patterns of absolute nonzero spectral coefficients, with upper bounds on their multiplicities, are:

    5 ones, 2n/5;
    5 twos, 2n/5;
    10 ones from two distinct 5-cycle pairs, 2(n/5)(n/5−1);
    7 ones, 2n/7.

These are real-valued upper bounds on integer counts for n>=35; they include both signs. No combination of 5 and 7 can fit length ten.

### 4.3 Other mixed conductors than 35 and 385

By the support bound the only possible mixed odd conductors are 35,55,65,85,77,91,385. For d=55,65,85,77,91 a mixed block needs >=14 entries, so its coset is central (otherwise inversion doubles that count). Only a further pure 5-cycle can fit when d=55. It must be inside the same central coset: if outside it would be the only block there and would have to be inversion-stable, impossible for a complete cycle with excluded fixed points. Thus the entire array is in the central coset.

For d=pr, the kernel of root evaluation on a p by r array consists of additive arrays A_ij=a_i+b_j, because these vanish by the complete prime cycles and their dimension p+r−1 is the kernel dimension pr−phi(pr). With the origin coefficient zero, set a0=b0=0; the axes are integer. In the symmetric case a_−i=a_i, b_−j=b_j. In the antisymmetric case a_−i=−a_i, b_−j=−b_j. If an axis vanishes the relation consists of pure cycles already counted. Otherwise let u,v be the even counts of nonzero entries on the axes. The support is at least u(r−v)+(p−u)v. For the antisymmetric case, the nonzero-axis intersection contains at least uv/2 additional nonzero entries (at most two of the four sign-pair sums can vanish). The resulting lower bound exceeds 20 in all five conductors, as verified by enumerating the indicated even u,v.

In the symmetric case the only options with the baseline <=20 are

    5,11: (u,v,baseline)=(4,8,20),(4,10,14);
    5,13: (4,12,16);
    5,17: (4,16,20);
    7,11: (6,10,16);
    7,13: (6,12,18).

There is room for at most one nonzero cell of the matrix on paired nonzero axes (each cell costs four support entries). The rectangle identity for an additive matrix rules out precisely one nonzero cell on a matrix with at least two rows and columns. Hence all intersections vanish, a_i have the same nonzero value A and b_j have −A on their nonzero axes. Since the length is half the baseline times |A|, |A|=1. Counting choices including sign gives at most 2 length-7, 12 length-10, 4 length-8 and 2 length-9 vectors, all with absolute coefficients one. In detail, 55 has two full-axis length-7 relations and ten partial-axis length-10 relations, 65 has two length-8, 85 two length-10, 77 two length-8, and 91 two length-9. All are in the symmetric central coset; overcounting a parity group is harmless.

### 4.4 Conductor 35

If a minimal block of conductor 35 occurs, all other blocks (if any) have conductors 5,7,35, since a 35 block needs >=10 support entries and every different mixed conductor or prime >=11 would exceed the remaining budget. Restrict to cosets of the subgroup of order 35; every restriction vanishes. If a mixed block is in a noncentral coset, its inverse coset doubles the support, so each coset has exactly ten nonzero entries, all ±1, and there are no other components. In a 5 by 7 additive array in that coset both axes must vary to require the mixed conductor. Choose the most frequent row value as zero. If at most three rows have the same value, every column has at least two nonzero entries and the support is >=14. Thus four rows have zero and one A!=0. Every column costs at least one entry, and a column with value −A costs four; any other nonzero column value costs five. With ten support entries there is exactly one column of value −A, all others zero. Hence |A|=1 and there are 35 choices of exceptional row and column, two choices of sign. Noncentral inverse coset pairs each occupy 35 spectral coordinates of the same parity, so at most n/35 such pairs exist. The total multiplicity of these length-10 all-unit relations is <=2n.

For central cosets, a symmetric or antisymmetric additive array is determined by five independent integer axes (a1,a2,b1,b2,b3). The spectral absolute coefficient lists are respectively the five axes followed by two copies of each a_i+b_j, or the five axes followed by a_i+b_j and a_i−b_j for each pair. Therefore sum of absolute axis values <=10 is a necessary finite enumeration bound. The exact enumeration in verify_classification.py covers all 36,365 axis tuples for each symmetry and retains arrays with both axes nonzero and 0<total length<=10. Counts (both signs included) are:

| absolute pattern | symmetric | antisymmetric |
|---|---:|---:|
| five ones | 2 | 0 |
| five twos | 2 | 0 |
| eight ones | 18 | 0 |
| nine ones | 12 | 0 |
| ten ones | 4 | 0 |
| eight ones and one two | 6 | 24 |

If a central mixed component is accompanied by another nonzero component, each has spectral length >=5 by Section 4.1, so each has length exactly five. A central mixed component of length five is one of the two symmetric entries in the table; there is no antisymmetric one. An accompanying component must therefore be a pure 5-cycle inverse pair, with at most 2n/5 signed choices; its support is disjoint from the central component. This produces at most 4n/5 additional length-10 all-unit relations. If one axis vanishes or a whole central array is purely a sum of cycles, it is already covered by the pure cases; extra counts only enlarge the bound.

### 4.5 Exclusion of conductor 385

A 5*7*11 minimal block requires >=19 roots. It is alone, must be central by inversion, and has exactly 20 roots of coefficients ±1. In a central lift, take slices indexed by the 11-coordinate. All 11 slices have the same evaluation in Q(zeta_35), by irreducibility of Phi_11 over that field (degree ratio 10). The common value is nonzero by minimality and all slices nonempty. At least two slices are singletons because there are only 20 terms. In the antisymmetric case the common value is purely imaginary, impossible for ± a root of odd order 35. In the symmetric case it is real, thus ±1; fix sign to make it 1. Every singleton is then at the slice origin with coefficient +1. A nonsingleton representing 1 needs at least four entries, since subtracting the origin produces a vanishing sum of minimum length five. The central slice (index zero) has even support, with origin absent. There are nine excess entries beyond eleven singletons, allowing only (i) a central slice of four entries plus one inverse pair of four-entry slices, or (ii) a central slice of ten entries. In (i) subtracting the origin from each exceptional slice produces a five-cycle through the origin, confining all coordinates to the order-5 subgroup and lowering the conductor to 55. In (ii) subtract the origin from the central slice. The resulting additive 5 by 7 array has a0=0,b0=−1, and by symmetry a1,a2 in {0,1,2}, b1,b2,b3 in {−1,0,1}. Its nonorigin spectral absolute weight must be five, with all entries 0,±1. Exhaustion of the 243 tuples proves this impossible (verify_classification.py). This is a finite check with analytically proved parameter bounds. It excludes 385 and completes the short-relation count for all even q not divisible by 3.

## 5. Uniform error bound and positivity

For a group Haar measure h, let E0=E_h F−Z and for v in V let E_v=E_h(F Re z^v)−E_* (F Re z^v). Fourier coefficients Fhat(u) of the independent polynomial are real, invariant under individual sign changes and permutation of the indices, and vanish for |u|_1>8. By Haar character orthogonality the errors are sums of Fhat(c−v) over nonzero c in Lambda (v=0 for E0). For a fixed relation c, define the error cost as the sum of |Fhat(c−v)| over all integer v of length <=2 (including 0). This equals the triangle bound for its contribution to |E0|+2 sum_{v in V}|E_v| after summing both signs of v. Costs only depend on the absolute coefficient pattern of c.

The exact checker verify_all.py computes bounds E_pattern on each cost as follows. Use the marked generating functions of Section 3 for Fhat(u), with B_|u_i| for each nonzero component and B_0 for each zero component. For every pattern of c, enumerate v=0, ±e_i,±2e_i,±e_i±e_j. Indices inside the support are enumerated directly; outside indices are counted with multiplicity n−s for a single outside choice or binomial(n−s,2) for two, where s is support size. Replace each coefficient's polynomial numerator coefficients by their absolute values, retaining the positive monomial denominator. For n>=35 all multiplicities are nonnegative, so this is a rigorous upper bound. The marked series derivation works for all n>=35 and the calculation uses only exact rational polynomials.

Write E_l for l ones, E_D for five twos and E_M for eight ones and one two. From Section 4, a simultaneous (possibly redundant) upper bound on the total error is

    Berr = (2n/5)(E5+E_D) + 2(n/5)(n/5−1)E10 + (2n/7)E7
         +2E_D+18E8+2E5+30E_M+12E9+4E10+(2n+4n/5)E10
         +2E7+12E10+4E8+2E9.

The first line is the pure-cycle bound, second line conductor 35, third line all other mixed conductors. Conductor 385 gives no additional term. The resulting exact expressions are

    b=0: Berr=12(4583117 n^3+117542015 n^2+6833118795 n+18802301105)/n^4;
    b=1: Berr=12(25968783 n^3+323062731 n^2+7159146083 n+22249229695)/n^4.

At n=35 these equal 4187416224/875 and 122193103488/8575, respectively, both less than 14500000. All numerator coefficients are positive, so each term decreases for n>0. Equivalently verify_all.py proves 14500000−Berr>0 by shifted polynomial coefficients for all n>=35. This and (1) give strict positivity after all corrections, regardless of the number and powers of odd prime factors.

Let M_v=U for v=2e_i or e_i±e_j, and M_v=bU for v=e_i. Let M_v^*=E_* F Re z^v, i.e. D,U,W in these cases. The actual phase density is

    f=[F+G−E0+2 sum_{v in V}(M_v−M_v^*−E_v) Re z^v]/(−NU).

By orthogonality of the cosines, its Haar mass is one and its required moments are U/(−NU)=−1/N or bU/(−NU)=−b/N. Pointwise its unnormalized numerator is at least G−2n(|U−D|+|bU−W|)−Berr>0. Thus it is a strictly positive probability density. It also is invariant under simultaneous phase conjugation. When no short relations occur, E0=E_v=0 and the same proof works for every n>=2. This proves the even positive direction for all q>=142 with 3 not dividing q, and for smaller even q with all odd primes >=11 and both group sizes >=2.

## 6. The finite exceptional even moduli

The remaining even q<142, 3 not dividing q, are handled as follows. Powers of two and twice primes are known from Kang. If q has odd prime factors but none smaller than 11, n>=2 and the relation-free proof above applies. The complete list of leftover cases is

    20,28,40,50,56,70,80,98,100,110,112,130,140.

The list is checked independently in verify_classification.py. Nine fresh rational phase certificates were generated for q=20,28,40,50,56,80,98,100,112; the four earlier certificates for q=70,110,130,140 were reused. These are stored as q*.json. Each seed is an integer linear functional modulo 4 on the power-basis coefficients of Q(zeta_(2q)), so the seed assigns fourth-root phases satisfying every actual integer energy relation. Galois conjugation preserves all relations and the parity classes, hence the orbit-averaged seed phases remain in the true phase group. The exact positive rational weights sum to one. The independent verify_full.py checks all original spectral pairs, not just a reduced system: the moments are exactly −1/(q−2) for distinct equal-parity modes and zero for opposite parity. A mixture with Haar, with weights (q−2)/(q−1) and 1/(q−1), respectively, realizes the actual target with full support. The exploratory optimizer is not needed to verify the supplied weights; all certification sums are integer/rational. The current run checked 48,696 full pairs across the thirteen moduli, and four known negative cases as controls. Logs small-search.log and small-search-2.log show the new searches, and small-verification.log gives the actual exact verification.

## 7. From phases to real readout times

The product of the two constructed densities has full support on H. The finite-exception mixtures also have full support. The mean target of a full-support measure is in the relative interior of the compact convex hull C of the phase coherence vectors: a supporting linear functional attaining its extreme at the mean must be constant on the whole support by continuity. For algebraic delta>0, the energies are algebraic and transcendence of pi implies delta c·theta in 2 pi Z if and only if c·theta=0. Thus the integer sampled orbit has the same group closure as continuous time, by Kronecker's character criterion. The nonnegative iterates have the same closure by compact recurrence. Translation by t0 preserves that closure. Since the relative interior of a convex set equals that of its closure, the target lies in the actual convex hull of the sampled vectors, not only its closure. Caratheodory's theorem gives the support bound from the at most m(m+1) positive Bohr frequencies (including the zero-mode gaps). The known positive cases for q>=4 have the strictly stronger ramp law in Kang and likewise a full-support mixture. For q=3 Haar gives the required moment directly. This proves the time-grid assertion. It does not give an efficient maximum waiting time or a concrete protocol for every q.

## 8. Combined result and verification status

The previous two working notes for odd moduli are included, unchanged, under prior-odd. Their exact verification scripts were rerun in this turn (prior-odd-recheck.log). Together with this even-modulus proof and the existing negative theorem, they cover every integer q>=3. No new nonexistence claim is made. The key proof obligations for independent review are the completeness of the short-relation classifications, the arithmetic count multiplicities, and the connection of phase densities to actual time laws. The new even proof does not rely on the truth of the earlier general positive families; the combined classification does rely on the two odd notes. Finite symbolic arithmetic checks support, but do not replace, the stated analytic arguments. Full Lean 4 formalization has not been undertaken. The user's earlier successful Lean check for P19 verified only its finite integer matrix certificate, not these classification theorems.

Reproduction commands (Python with SymPy and NumPy):

    python verify_low_degree.py
    python verify_classification.py
    python verify_all.py
    python verify_full.py

The optional search script explore_even.py needs SciPy and produces new rational certificates using LP followed by exact solving. It is not required for verification. The saved logs are from actual runs. Re-run prior odd checks with the commands in prior-odd/README.md. No personal author assigned; no GitHub changes made.

## 9. Priority search and references

We reopened Kang's September 2026 v1 text and checked the abstract, main theorem, coherence criterion, and positive-case ramp. Its stated positive range is still primes, twice primes and powers of two; its negative result and collision classification are prior work. Targeted current web searches included random-time uniform mixing on paths, cyclotomic phase distributions, positive-definite moments, Fourier polynomial phase density, and related quantum-walk results. We located Kang's October 2026 strongly regular graph work, not the present path classification, and rechecked the original scanned Conway–Jones Theorem 5 on p.235. No matching complete path classification was found in the returned results. The search is not exhaustive and cannot certify priority. In particular the new Fourier density and short-relation bound are potential original contributions; classical Fourier coefficient extraction, the root-of-unity bound, and convex geometry are established tools.

1. M. Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, arXiv:2609.14463v1, https://arxiv.org/html/2609.14463v1.
2. P. Baptista, G. Coutinho, V. Marques, Unexpected Averages of Mixing Matrices, arXiv:2308.16378, https://arxiv.org/abs/2308.16378.
3. J. H. Conway, A. J. Jones, Trigonometric diophantine equations (On vanishing sums of roots of unity), Acta Arithmetica 30 (1976), 229–240, https://doi.org/10.4064/aa-30-3-229-240.
4. M. Kang, Moment Methods for Uniform Average Mixing on Strongly Regular Graphs, arXiv:2610.10017, https://arxiv.org/abs/2610.10017.
5. Previous odd-modulus working notes and exact certificates, included under prior-odd/.
