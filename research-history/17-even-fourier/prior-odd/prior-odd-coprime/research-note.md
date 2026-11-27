# Uniform average mixing for every odd modulus coprime to three

## A low-degree Fourier construction and a classification of short spectral relations

Working mathematical research note, 27 November 2026. AI-assisted; no personal author assigned. Not independently peer-reviewed or fully Lean-formalized. This note supersedes the odd coprime-to-three asymptotic result in the previous Fourier research note; it does not rely on earlier candidate graph-family proofs or on numerical optimization.

### Abstract

We prove a candidate general existence theorem for uniformly coupled paths with q−1 vertices, where q is coprime to six. A fixed nonnegative polynomial in the collective phase amplitude realizes the required moment vector on an independent torus. We classify the only short, low-charge spectral relations that alter this polynomial's relevant Fourier moments on the actual cyclotomic phase torus. The proof uses the Conway–Jones support bound, additive two-prime arrays, and a short-slice argument excluding the exceptional triple conductor 385. All deviations can be removed while preserving strict positivity. This eliminates the astronomical size threshold in our previous asymptotic theorem for odd moduli not divisible by three. Exact integer enumeration and rational checks are supplied as supplementary cross-checks of the mathematical argument. We also obtain finite readout protocols on arbitrary positive algebraic time lattices and a conservative effective bound for a particular lattice.

## 1. Statement and relation to prior work

Let N=q−1, let A be the adjacency matrix of P_N, and set M(t)=|exp(itA)| entrywise squared. Uniform average mixing means a freely chosen probability law mu with E_mu M(t)=J_N/N. It is neither the fixed Cesaro average nor instantaneous uniform mixing.

**Theorem.** For every integer q>=3 with gcd(q,6)=1, P_(q−1) admits uniform average mixing. There is a finite law supported on any prescribed time lattice t0+delta n, n in the nonnegative integers, for t0>=0 and positive algebraic delta. At most m²+1 readout times suffice, where m=(q−1)/2.

Moreover, for q>=7 in this class, put D=phi(q)/2 and L=20000(m²+1)m^4 20^D. One can choose all readout times from {t0+j/20:0<=j<L}. This bound is not intended as a practical time window.

Kang (arXiv:2609.14463v1) proved existence for q a prime, twice a prime, or a power of two, and nonexistence when 15|q, 21|q, or 6|q with q>=12; the latter are exactly the parity collision cases. We use the forced-coherence characterization from that work; we do not claim it or the parity collision classification as new. The positive theorem here extends its scope and also improves our prior internal Fourier note, which treated gcd(q,30)=1 and a very large asymptotic threshold for odd q coprime to 3. This theorem includes arbitrary prime powers and arbitrary products of primes >=5. It does not establish the whole conjecture, in particular odd q divisible by 3 or general even q.

## 2. Spectral moments and polynomial density

For odd q put alpha_j=2cos(2 pi j/q), 1<=j<=m, the energy at mode 2j; the energy at mode q−2j is −alpha_j. These alpha_j need not be positive. Let H be the closure of t alpha modulo 2 pi and h its normalized Haar measure. Put z_j=exp(i phi_j). The integral relation lattice is Lambda={c in Z^m: c dot alpha=0}. The character chi_c=z^c has Haar integral 1 if c in Lambda and 0 otherwise, by translation invariance and density. Write |c|=sum |c_j| and Q(c)=sum c_j (length and charge).

It suffices to realize the moments

    E Re(z_i conjugate(z_j))=−1/(2m), i<j;
    E Re(z_i z_j)=0, i<=j.

By the path sine eigenvectors the Cesaro mean is D0=(2J+I+S)/(2q), where S is reflection. The two parity projector sums are (I+S)/2 and (I−S)/2. The sum of their entrywise squares is (I+S)/2. Substitution of these moments into the spectral expansion of M yields D0−((I+S)/2−D0)/N=J/N. This is the established spectral identity in Kang. The complete target index set is V={e_i−e_j:i<j} union {e_i+e_j:i<=j}, of size m².

Use the nonnegative polynomial F=(100−60X+7X²)² with X=|sum z_j|²/m. Denote independent-circle Haar integration by E_*, and set Z=E_* F, Y=E_* XF. The exact moments E_* X^k=(k!)²/m^k [t^k](sum_{j=0}^k t^j/(j!)²)^m follow by equating occupancies in the two multinomial expansions. For k=0,...,5 they are respectively

    1, 1, 2−1/m, 6−9/m+4/m²,
    24−72/m+82/m²−33/m³,
    120−600/m+1250/m²−1225/m³+456/m^4.

Thus

    Z=(4136m³−968m²+658m−1617)/m³,
    Y=(1720m^4−1920m³+12370m²−32305m+22344)/m^4,
    (m+1)Z−2mY=3(m−1)T(m)/m³,
    T(m)=232m³+2568m²−5782m+15435.

For m>=3, T>=232m³ (substitute m=3+x and expand T−232m³), 3000<Z<4210. By permutation symmetry and global rotation invariance of the independent density F/Z, its distinct conjugate moments are (Y/Z−1)/(m−1), and all ordinary products vanish. Put tau=(m−1)Z/[2m(Z−Y)], so 0<tau<1. Then tau F/Z+(1−tau) realizes exactly the target under E_*. The available unnormalized slack is G=Z(1−tau)/tau=3T(m)/m³>=696. The small prime case q=5 follows from Kang; the rest of this proof assumes m>=3.

## 3. Classification of the short relations that matter

We give the details because a bound on only the number of prime factors would not suffice. A relation c yields a symmetric integer array on Z/qZ, with coefficients c_j at j and −j (the same coefficient at both positions) and zero at 0, vanishing when evaluated at the primitive q-th root zeta. Its total absolute weight is 2|c| and its support size is at most 2|c|. We only require relations of even length <=10 and charge 0 or ±2.

### 3.1. Minimal support decomposition

Use the signed rational version of the Conway–Jones bound: a minimal vanishing relation on distinct roots with reduced exponent d has d squarefree and support length at least 2+sum_{p|d}(p−2). Here minimal means that no proper nonempty subset, with its original coefficients, vanishes. Repeatedly remove minimal vanishing subsets; the resulting supports are disjoint. Each block is contained in a coset of the subgroup of order d. A block with prime reduced exponent is a full prime cycle with constant nonzero coefficient, by irreducibility of Phi_p. The prime factors of d divide q and hence are >=5.

In particular, no nonzero relation of even length <=4 exists: its root support would be at most 8, allowing at most one block; a mixed block needs >=10 roots and a single prime cycle has odd support, impossible by inversion symmetry with zero origin. Thus V consists of nontrivial characters distinct up to inversion modulo Lambda; the Haar cosines are orthogonal, with squared norm 1/2.

In the range of support <=20, the only possible composite reduced exponents are

    35, 55, 65, 85, 77, 91, 385.

This follows directly from the support bound: the two-prime lower bound is p+r−2 and the three-prime bound is p+r+s−4. The latter permits only 5,7,11. Four primes cannot occur.

### 3.2. Pure prime-cycle relations

If all minimal blocks are prime cycles, there are at most four of them. Inversion sends each prime coset to a disjoint coset of the same subgroup, because an inversion-invariant coset in an odd cyclic group would contain 0, which is forbidden. The inverted cycle must coincide with another cycle of the same prime: otherwise it meets every other block of a different prime in at most one root and every block of the same prime in zero roots, and at most three intersections cannot cover >=5 roots. Symmetry then forces the equal coefficients on the paired cycles.

An inverse pair of p-cycles of coefficient A contributes p|A| to spectral length and pA to charge. Even length <=10 and charge 0 or ±2 therefore require exactly two inverse pairs of 5-cycles with coefficients +1 and −1. This is Type I. There are P=(q/5−1)/2=(m−2)/5 noncentral pairs of 5-cosets when 5|q, and at most P(P−1)<=m²/25 ordered choices. Each relation has five +1 and five −1 entries. If 5 does not divide q, there are no such relations.

### 3.3. Mixed reduced exponents other than 35 and 385

For d in {55,65,85,77,91} a mixed block has at least 14 roots. There can be only one. Its support lies in a central coset: if not, inversion would require >=14 more roots in its disjoint inverse coset. The only possible remaining block is one 5-cycle (when d=55), necessarily inside the central subgroup; outside it inversion could not be supplied. Thus the whole array is supported on the subgroup of order d.

For d=pr, CRT coordinates identify the kernel of rational root evaluation with the additive arrays A_ij=a_i+b_j. Indeed row-constant and column-constant arrays vanish by prime cycles, and their combined dimension p+r−1 equals pr−phi(pr). With zero origin choose a0=b0=0. Inversion gives a_i=a_−i and b_j=b_−j. If one axis is identically zero the array is pure cycles, already counted. Otherwise let u,v be the even counts of nonzero a_i,b_j. The support size is at least u(r−v)+(p−u)v. The only even choices with this bound <=20 are:

| p,r | (u,v,baseline) |
|---|---|
| 5,11 | (4,8,20), (4,10,14) |
| 5,13 | (4,12,16) |
| 5,17 | (4,16,20) |
| 7,11 | (6,10,16) |
| 7,13 | (6,12,18) |

In all cases at most one cell of the matrix of paired nonzero row and column indices could have a nonzero sum: such a cell costs four support entries. But a matrix of additive sums on at least 2x2 indices cannot have exactly one nonzero cell, by the rectangle identity. Therefore all intersections vanish. The nonzero a_i are a common A and the nonzero b_j are −A. The length is baseline*|A|/2, so |A|=1. In the full-axis cases the length is (p+r−2)/2 and charge ±(r−p)/2. Only d=77 gives even length and allowed charge: length 8, charge ±2, five positive and three negative entries (choose orientation for charge +2). Call this Type II. For d=55 the partial-axis case u=4,v=8 gives length 10, charge ±2, six positive and four negative entries for charge +2, with five possibilities for the omitted nonzero column pair. Call this Type III. There are no other relevant relations in this case.

### 3.4. The conductor 35

If some mixed block has d=35, no block of any other mixed conductor or prime >=11 can coexist (minimum total support would exceed 20). All blocks lie in cosets of the subgroup of order 35. Group them by coset. The restriction to each coset vanishes, and inversion exchanges noncentral cosets. Each occupied noncentral inverse pair has spectral length at least 5; its length and charge are the absolute weight and signed sum of the 5x7 additive array in one coset. The central array also has length at least 5 by the short-support argument of Section 3.1. Hence at most two components (one central or one inverse coset pair counts as a component) occur.

If two components occur, both have length 5. A noncentral length-5 array is a pure 5-cycle. A central length-5 array has charge ±5 (pure 5-cycle pair) or ±1 (axis difference), as verified below. The only allowed combined charge is zero, from opposite 5-cycle pairs, which is Type I. If a single noncentral component occurs, an additive array with one axis constant consists of pure cycles, giving only Type I. For both axes nonconstant, choose the most frequent row value as zero. If its multiplicity were <=3, each column would have >=2 nonzero entries and total support >=14. Hence four rows are zero and one row is A!=0. Each of the seven columns has at least one nonzero; a column value −A costs four nonzero entries, while a value other than 0 or −A costs five. The support limit 10 forces exactly one column with value −A, all others zero. The ten nonzero entries must be ±1, as the length is <=10. This gives length 10, charge ±2, and six positives and four negatives for charge +2. There are 5*7=35 choices per noncentral inverse pair, with (q/35−1)/2 such pairs, at most m in total. Call this Type IV.

It remains to classify the central symmetric 5x7 array. Its independent coordinate values are

    a1,a2,b1,b2,b3, and two copies of each a_i+b_j (i=1,2; j=1,2,3).

Here a0=b0=0; a1,a2,b1,b2,b3 are integer axis values; the other axis values follow by inversion. The length is

    L=|a1|+|a2|+sum_j (|b_j|+2|a1+b_j|+2|a2+b_j|),

and charge Q=7(a1+a2)+5 sum b_j. We need L<=10. If a1!=a2, their difference is <=1 in absolute value by L>=6|a1−a2|. Up to permutation and global sign the only possible unequal pair is (0,1): if consecutive entries are u,u+1 with both of the same nonzero sign, each column costs at least 2+min(|u|,|u+1|), so L>=12. This column bound follows from |u+b|+|u+1+b|=1+2 dist(b,[−u−1,−u]) and the triangle inequality for |b|. For a=(0,1) each column b is 0 (cost 2) or −1 (cost 3); any other value costs >=7, incompatible with L<=10. With k entries −1 the length is 7+k and charge 7−5k. Even length and allowed charge require k=1, giving six possibilities (two row choices and three column choices) of length 8, charge +2, five +1 and three −1. Include the negatives for charge −2. Call this Type V.

If a1=a2=A then L>=5|A| so |A|<=2. For A=0, L=5 sum|b|, giving the pure cycles of Type I and the length-5 charge ±5. For A=1 up to global sign, each column costs |b|+4|1+b|; the baseline is 1 at b=−1. The only options within the total budget are all b=−1 (length 5, charge −1), one b=0 (length 8, charge 4), or one b=−2 (length 10, charge −6). None of these has even length and allowed charge. For A=2 all b=−2, with length 10 and charge −2; its negative has three +2 entries and two −2 entries. This is Type VI, one for each charge sign. These arguments also establish the length-5 classification used for two components. The companion checker exhaustively enumerates the five integer axes with l1 norm <=10, which is a necessary bound as the axis values are themselves among the coordinates; it independently confirms all 20 relevant central arrays and the length-5 cases.

### 3.5. Excluding the three-prime reduced exponent 385

The Conway–Jones bound for 5*7*11 is 19; inversion forces even support, and weight <=20 forces exactly 20 entries, each +1 or −1. This is a single minimal block in the central subgroup. Write its CRT array as eleven 5x7 slices indexed by the 11-coordinate. Evaluating each slice at the primitive 35-root gives eleven elements of Q(zeta_35) that must all be equal, since Phi_11 is irreducible over Q(zeta_35) (the field degree ratio is 10). The common value is nonzero: otherwise every nonempty slice vanishes and minimality forces at most one nonempty slice, contradicting reduced exponent 385. Each slice is nonempty; since total support is 20, at least two are singletons. The common value is therefore ± a 35th root of unity. Inversion pairs the slice evaluations by conjugation, so the common value is real, necessarily ±1. Multiply all signs to make it +1. Every singleton is then +1 at the origin of its 35-slice.

A nonsingleton slice representing 1 must have at least four entries: subtracting the origin produces a nonzero vanishing relation on at most one additional root, and the minimum support is five. The central slice has zero origin and even support by inversion. Counting the nine support entries in excess of eleven singletons leaves only two configurations: (a) central slice with four entries, plus one inverse pair of slices of four entries; (b) central slice with ten entries and all other slices singleton. In case (a) each exceptional slice minus the origin is a five-term relation, so it is a 5-cycle through the origin and all its coordinates are in the subgroup of order 5. This would restrict the whole conductor to 55, a contradiction.

In case (b), subtract the origin in the central 35-slice. The result is an additive array A_ij=a_i+b_j with a0=0,b0=−1. Inversion pairs the axes. Since every entry is 0 or ±1, the two other independent a values belong to {0,1,2} and the three other independent b values to {−1,0,1}. The nonorigin half-weight would have to be 5, namely

    |a1−1|+|a2−1|+sum_j (|b_j|+2|a1+b_j|+2|a2+b_j|)=5.

This is impossible. If an a is 2, all b must be −1 and the left side is >=10. Otherwise a1,a2 in {0,1}. If both are zero the weight is 2+5k; if one is one and one zero it is >=7; if both are one it is 3+3k (k is a nonnegative integer). None is 5. The checker independently tests all 243 parameter tuples. This excludes reduced exponent 385 entirely in the relevant even-length range.

The six types above exhaust all relevant relations. Note that the classification is for length <=10 and charge 0 or ±2, not for all cyclotomic relations, and uses signed coefficients.

## 4. Positivity after Fourier correction

Write Fhat(u) for the real Fourier coefficient of F on the independent torus. It is zero unless Q(u)=0 and |u|<=8. Let

    E0=E_h F−Z,
    E_v=E_h(F Re chi_v)−E_*(F Re chi_v).

By Fourier expansion and Haar orthogonality these are the sums of Fhat(c) and Fhat(c−v), respectively, over nonzero c in Lambda. Inversion symmetry ensures the expectation of the cosine equals the real character expectation. Only the just-classified lengths and charges can contribute. All charge-zero nonzero relations listed have length 10, so E0=0. On H define

    f=tau F/Z+(1−tau)−(tau/Z) E0−(2tau/Z) sum_{v in V} E_v Re chi_v.

This has mass one and the exact target moments by cosine orthogonality. It suffices to prove E=|E0|+2 sum |E_v| < G. All estimates below count absolute contributions before summing, hence remain valid even if cancellations occur or some types are overcounted.

For balanced u of length 2h, the coefficient of X^j is

    (j!)²/m^j sum_{l_i>=0,sum l_i=j−h} prod_i 1/[(u_i^++l_i)!(u_i^−+l_i)!].

Consequently, using F=10000−12000X+5000X²−840X³+49X^4, the coefficient satisfies |Fhat(u)|<=58464/m³ for h=3, and <=28224/m^4 for h=4. For h>4 it is zero. These follow by bounding the number of summands by m^(j−h) and the individual terms by one.

For a length-10 relation, cancellation of both units of v is required. Type I has at most 25 oriented difference choices per relation, <=m²/25 relations counting both signs. Its contribution to E is <=56448/m². For Type II, a charge +2 length-8 relation with five positives and three negatives can cancel both units at ten distinct positive pairs, or one unit at at most 5m other pairs; the negative charge cannot contribute to our positive-sum orientation. Its E contribution is <=2(10*58464/m³+5m*28224/m^4)=1451520/m³. Type V has six such relations, so <=8709120/m³. Type III has five charge +2 relations of length 10 with six positive entries, each allowing at most 15 pairs, contributing <=4233600/m^4. Type IV has <=m charge +2 relations of the same pattern, contributing <=846720/m³. Type VI permits at most six positive pairs including repeats (three +2 coordinates), contributing <=338688/m^4. Thus, uniformly,

    E <= 56448/m² + 11007360/m³ + 4572288/m^4.

When 35 does not divide q, only Types I, II, III remain, giving

    E <= 56448/m² + 1451520/m³ + 4233600/m^4.

For q>=55 with 35 not dividing q, m>=27, and the last bound is at most 3132416/19683<160. For 35|q with q!=35, coprimality to six implies q>=175 and m>=87; the full bound is at most 17153920/707281<25. For q<55 other than 35 no mixed conductor is possible, and the only pure contribution can occur at q=25 (m=12); it is <=392. For q=35 there is only the central array; the exact finite coefficient sum is

    E = 31239432/83521 < 375,
    G = 5397327/4913 > 1098.

This is computed by summing the 20 central vectors over all 289 characters in V using the factorial coefficient formula above; the checker also checks the simplified coefficient formula for h=3,4. These are exact fractions, not numerical tolerances. Consequently E<=849/2<696<=G in all cases q>=7. The density f is strictly positive on H and realizes the desired moments. In fact f>= (1−tau)(1−E/G)>1/50: use Y>=0, Z<4210 and G>=696 to obtain 1−tau>=696(m−1)/(8420m). This completes the phase-group proof.

## 5. Real readout laws and finite effective window

The construction is on the phase group, not an assertion that the chosen phase vector occurs at a real time. Since f>0, the target lies in the relative interior of the convex hull of the cosine vectors on H: a supporting linear functional extremized at its f-weighted integral would be constant by full support. Algebraicity of alpha and of positive delta, and transcendence of pi, imply that delta c dot alpha in 2 pi Z holds exactly when c dot alpha=0. The integer-time orbit has the same compact group closure H by the character form of Kronecker's theorem; nonnegative iterates have the same closure by compact recurrence. Translation by t0 alpha does not change the closure. The relative interior of a convex set equals that of its closure, so the target belongs to the actual convex hull of the time-grid vectors, not just its closure. Caratheodory's theorem reduces the support to m²+1 points; discard zero weights. For q=5 the known positive case can use the strictly feasible ramp in Kang and the same time-lattice argument.

For q>=7, an explicit finite window follows directly without quantitative Kronecker. The l1 norm S_f of the full torus Fourier coefficients of f is <=12m^4: the l1 norm of X is m; sum of absolute polynomial coefficients is 27889, Z>3000, and the correction has l1 norm <=tau E/Z<1−tau. Any nonzero frequency beta=u dot alpha for |u|<=10 is a nonzero algebraic integer in the real cyclotomic field of degree D=phi(q)/2, and all its conjugates have modulus <=20. Taking its field norm gives |beta|>=20^(−(D−1)). The geometric sum on t_j=t0+j/20 differs from the Haar mean by <=eps=4*20^D/L for each such character, using |1−exp(ix)|>=|x|/2 for |x|<=1. Zero frequencies agree exactly. With h_0=1, h_v=Re chi_v, the empirical Gram matrix G_L differs entrywise by <=eps from diag(1,1/2,...,1/2). Put n=m²+1. If n eps<=1/4, then G_L is invertible with inverse row-sum norm <=4 (factor out the Haar diagonal and use the Neumann estimate). If b is the target including normalization, let e=b−L^(−1)sum_j f(t_j alpha) h(t_j alpha), so ||e||_infty<=S_f eps, and c=G_L^(−1)e. The exact weights w_j=(f(t_j alpha)+c dot h(t_j alpha))/L realize b. Each correction is bounded by 4n S_f eps; choosing L=20000 n m^4 20^D makes this <=192/20000<1/100, below the uniform density floor. Hence all weights are strictly positive, and support reduction to n points applies. This finite bound is an analytic guarantee, not a claim of having enumerated the grid.

## 6. Verification, novelty and limitations

The companion script checks exact symbolic moment identities, the central 35 enumeration (36,365 parameter vectors, 72 nonzero arrays with length <=10, 20 relevant), the five mixed support tables, the 243 triple-slice cases, 31 representative root relations by cyclotomic polynomial reduction, the 289 q=35 target-moment deviations with two coefficient formulas, and all global rational error bounds. Its actual output is in verification.log. The finite arithmetic checks are not a replacement for the general classification proof. In particular no full Lean validation of this theorem has been performed. The separate P19 finite matrix certificate previously passed the user's Lean kernel audit; that does not certify this new theorem.

Targeted web searches on 27 November 2026 included uniform average mixing of paths, cyclotomic phase constraints, Fourier densities, coprime moduli, Kang, and indexed GitHub research results. We reopened arXiv:2609.14463 and its v1 HTML; the abstract and theorem give only the positive prime/twice-prime/power-of-two families. Kang's newer strongly regular graph work (arXiv:2610.10017) treats a different graph class. We located the Conway–Jones 1976 theorem and Lenstra's survey confirming the signed rational support bound. We did not find a prior theorem covering the exact full gcd(q,6)=1 positive family with this construction. These are bounded searches, not an exhaustive priority guarantee or independent peer review. The public GitHub repositories were not modified. The paper is a working note without personal attribution.

The remaining essential arithmetic cases for the full classification are even q with 3 not dividing q, and odd q divisible by 3 but not by 5 or 7 (apart from already known or separately proved families). The present proof does not address them: prime-3 cycles introduce many additional low-order relations, and even q has a different parity moment system. No new nonexistence result is claimed.

## References

1. M. Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, arXiv:2609.14463v1, 13 September 2026, https://arxiv.org/html/2609.14463v1.
2. P. Baptista, G. Coutinho, V. Marques, Unexpected Averages of Mixing Matrices, arXiv:2308.16378, https://arxiv.org/abs/2308.16378.
3. J. H. Conway, A. J. Jones, Trigonometric diophantine equations (On vanishing sums of roots of unity), Acta Arithmetica 30 (1976), 229–240, Theorem 5, https://doi.org/10.4064/aa-30-3-229-240.
4. H. W. Lenstra Jr., Vanishing sums of roots of unity, survey, Theorem 2.6, https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1979d/art.pdf.
5. M. Kang, Moment Methods for Uniform Average Mixing on Strongly Regular Graphs, arXiv:2610.10017, https://arxiv.org/abs/2610.10017.
