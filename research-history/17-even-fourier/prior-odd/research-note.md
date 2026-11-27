# Uniform average mixing on odd paths with a factor of three
## A three-coordinate block Fourier construction and completion of the odd-modulus classification (candidate)

Working research note, 27 November 2026. AI-assisted; no personal author assigned. Not independently peer-reviewed or fully Lean-formalized. The original public repositories have not been modified.

### Abstract
For the path P_(q−1), we ask whether a freely chosen random readout time gives uniform transition probabilities for every initial site. We establish an analytic construction for odd q divisible by 3 but not by 5 or 7, with one previously obtained exact finite certificate for q=33. We model the abundant three-term energy relations by independent product-one triples and a singleton. The first four moments of a fixed nonnegative collective-phase polynomial, with marked characters, are evaluated on this block torus. The Conway–Jones theorem reduces departures from the block model to a finite list of mixed short relations, and an explicit positive density is constructed by correcting the necessary Fourier coefficients. Together with the preceding working note for gcd(q,6)=1 and Kang's nonexistence results, this supplies a candidate complete classification of odd q. The even case is not resolved.

## 1. Statement
Let q>=3 be odd, N=q−1, A the adjacency matrix of P_N, and M(t)=|exp(itA)| entrywise squared. Uniform average mixing (UAM) means E_mu M(t)=J_N/N for some probability law mu. It is different from instantaneous mixing and from the fixed Cesaro mean.

**New theorem (candidate proof below).** If 3 divides q and gcd(q,35)=1, P_(q−1) admits UAM. A finite law exists on every grid t0+delta n with t0>=0, delta>0 algebraic, n a nonnegative integer; at most ((q−1)/2)^2+1 points are needed. This theorem covers arbitrary exponents and arbitrary numbers of other prime factors, including 11 and 13. The case q=33 uses a finite rational certificate rather than the uniform polynomial density. The cases q=3,9,39 have separate small proofs.

**Combined candidate classification for odd q.** For every odd q>=3, UAM exists if and only if neither 15 nor 21 divides q. For the coprime-to-three positive direction, use the preceding independent working proof in prior-odd-coprime/research-note.md, whose exact auxiliary checks were rerun for this release; for the negative direction, use Kang's published preprint. For the positive direction with 3|q use this note. The combined claim inherits the proof obligations of that earlier note, which has not been independently peer-reviewed.

Kang, arXiv:2609.14463v1, explicitly leaves moduli outside the prime, twice-prime, power-of-two positive classes and the three collision classes undecided by the theorem. We use his coherence criterion and negative results; neither is claimed as new. We re-opened the source and searched for later positive classification, cyclotomic Fourier moment, and random-time mixing results on 27 November 2026. No matching theorem was found in the returned public results; this is not an exhaustive priority guarantee.

## 2. Phase torus and required moments
For odd q, put m=(q−1)/2 and alpha_j=2 cos(2 pi j/q), j=1,...,m. The physical energies consist of alpha_j at even mode 2j and −alpha_j at odd mode q−2j. Let H be the compact subgroup closure of t alpha modulo 2 pi, h its Haar probability, and z_j=exp(i phi_j). The relation lattice Lambda={c integer: c dot alpha=0} is the annihilator of H. For the character chi_c=z^c, E_h chi_c=1 if c in Lambda and zero otherwise.

The needed moments are E Re(z_i conjugate(z_j))=−1/(2m) for i<j, and E Re(z_i z_j)=0 for i<=j. These yield the target equal-parity coherence −1/N and opposite-parity coherence zero. The known spectral projector identity D0=(2J+I+S)/(2q), where S is reflection, and the squared parity projectors sum (I+S)/2 give D0−[(I+S)/2−D0]/N=J/N. Let V_index consist of the m² characters e_i−e_j (i<j), e_i+e_j (i<=j). Write |c| for its l1 length and Q(c)=sum c_i for its charge.

## 3. A model that retains every relation coming from three
Put b=(q/3−1)/2, so m=3b+1. In Z/qZ the subgroup {0,q/3,2q/3} has order three. Pair each noncentral coset with its inverse; no noncentral coset is fixed by inversion, since q is odd. Each coset pair gives three distinct coordinates among the alpha_j, after identifying j and −j. Their energy sum is zero by the three-term geometric sum. The central coset has only the free singleton alpha_(q/3)=−1 among the nonzero cosine coordinates. Hence H is a subgroup of H_3, the product of b independent tori z_1 z_2 z_3=1 and one independent circle. H_3 is only a model: the actual H can have further constraints. Its annihilator Lambda_3 consists of integer vectors constant on each triple, with zero singleton. Lambda_3 is contained in Lambda.

Under H_3 Haar probability, let X=|sum z_j|²/m and F=(100−60X+7X²)^2. Define Z=E_3 F, U=E_3 F Re(z_i conjugate(z_j)) for distinct coordinates in one triple, V=the analogous moment across two distinct triples, and W=the triple-to-singleton moment. For b>=2 these are, with common denominator m^4:

    Z m^4 = 335016 b^4 + 414504 b^3 + 122490 b² + 126705 b + 2209;
    U m^4 = −8(8154 b³ + 9171 b² + 21603 b − 14243);
    V m^4 = −24(2718 b³ + 1857 b² + 11035 b − 21989);
    W m^4 = −8(8154 b³ + 9171 b² + 21015 b − 13655).

All ordinary-product moments under F are zero: multiplying all coordinates by the same cube root preserves H_3 and F, but multiplies z_i z_j by its square, which is not identically one.

Derivation of the four rational expressions, which can be reproduced by exact coefficient extraction: for one block of n=3 or n=1 coordinates and a marked exponent vector u, define the bivariate polynomial P_(n,u) with coefficient at x^a y^d, a,d<=4, equal to

    sum_(A,B>=0, sum A=a, sum B=d)  1/(prod_i A_i! B_i!)
       * indicator[A−B+u in Lambda_block].

For n=3 the indicator says all three components equal; for n=1 it says the component is zero. The polynomial for all b triples and the singleton is the product of the respective factors. For Z use no marks; for U mark (1,−1,0) in one triple; for V mark (1,0,0) and (−1,0,0) in distinct triples; for W mark (1,0,0) and singleton (−1). A complex character and its inverse have the same real integral. The expectation of X^k times the marked character is (k!)²/m^k times the coefficient of x^k y^k in that product. Multiply by F's coefficients (10000,−12000,5000,−840,49) and sum k=0,...,4. Expanding P^b as sum_(j=0)^8 binomial(b,j)(P−1)^j after truncation gives the displayed rational expressions symbolically for all b, not by interpolation. The exact checker derives them by this procedure.

Let G=−2m V−Z. The constant term G makes the desired common unnormalized conjugate moment V. The differences V−U and V−W are positive for b>=4, as shown by their shifted numerators:

    (V−U)m^4=16(1800b²−5751b+25862),
    (V−W)m^4=16(1800b²−6045b+26156).

The total absolute correction for within-triple and singleton-triple moments is E_b=6b(2V−U−W), because there are 3b pairs of each type. Direct expansion gives

    G m^4=56376b^4−16632b³+1555686b²−2763441b−1057681,
    E_b m^4=192b(1800b²−5898b+26009).

At b=4+x, the numerator of G−E_b is

    56376x^4+539784x³+3753414x²+10792767x+2172683,

which is strictly positive for every x>=0. It remains to control the extra relations in Lambda.

## 4. Exact classification of the additional short relations
Only even-length c with |c|<=10 and Q(c) in {0,±2} can contribute to E_h F or E_h(F Re chi_v): F has length<=8 and charge zero in Fourier space, and v has length two. For orthogonality of the target cosines we also use the absence of any nonzero even relation of length<=4, regardless of charge.

Represent c as a symmetric signed integer array on Z/qZ, with coefficients c_j at ±j and zero at 0. Its support and absolute weight are at most 20. Partition its nonzero support into disjoint minimal vanishing subsets with their original coefficients. By the rational signed Conway–Jones theorem (Theorem 5, 1976; see also Lenstra's survey, Theorem 2.6), each subset is contained in a coset of a subgroup of squarefree order d, and the support size is at least 2+sum_(prime p|d)(p−2). A prime-order subset is a full prime cycle with constant coefficient by cyclotomic irreducibility.

Under gcd(q,35)=1 and 3|q, possible prime factors are 3 and primes>=11. Two distinct primes >=11 would have bound >=22, and a mixed triple of primes has bound >=23. Thus the only mixed conductors are 3r for r=11,13,17,19, with support at least r+1. At most one such block can occur. A pure large-prime cycle cannot occur in any symmetric array here: it cannot be in the central coset (contains 0), and its inverse coset is disjoint and requires at least r additional support entries, exceeding 20. In the absence of a mixed block, every component is a pure 3-cycle, and inversion pairs the disjoint cosets. The relation is then in Lambda_3. In particular for length<=4 (root support<=8) all relations are in Lambda_3; a nonzero such vector has length a multiple of 3, so none has even length<=4. This proves the target cosines on H are nontrivial, distinct up to inversion, mutually orthogonal, with squared norms 1/2.

If there is a mixed block, it must lie in the central subgroup of order 3r: otherwise its inverse coset would require another >=r+1 entries. Every remaining block is a 3-cycle. Those outside the central subgroup occur in inverse pairs, and inside are included in the central array. The central array vanishes at the 3r-th primitive root, since each of its constituent blocks vanishes. CRT identifies all such rational arrays on a 3 by r rectangle with additive arrays A_(i,j)=a_i+d_j: row and column constant arrays are in the kernel, and their dimension 3+r−1 equals 3r−phi(3r). Normalizing a_0=d_0=0 is valid because the origin coefficient is zero; the axis values are integers. Inversion gives a_1=a_2=t and d_j=d_(−j). Denote the R=(r−1)/2 independent nonzero d values by d_1,...,d_R. The central independent spectral coordinates are exactly

    t, and (d_j,t+d_j,t+d_j) for each j.

If t=0 the array consists only of 3-cycles and lies in Lambda_3. Otherwise |t|>=1, and central length L=|t|+sum_j (|d_j|+2|t+d_j|)>=(R+1)|t|, forcing |t|=1. By global sign assume t=1. Then each d_j is in {−2,−1,0,1}, because any other value has cost>=7 while each remaining column costs at least one, R>=5 and total length<=10. At most one outside inverse pair of 3-cycles can be present, of length3 and coefficient sign ±1, since L>=6. The column values (−2,−1,0,1) have respective length contributions (4,1,2,5), and charges (−4,−1,2,5); the initial t contributes one to length and charge. Count the number of each column value. Keeping only even total length<=10 and charge 0 or ±2, including a possible outside triple, gives the following exhaustive table. Counts refer to t=1; sign is selected uniquely to give charge +2 for the actual correction.

| r | central d pattern (permutation) | outside triple sign | total length | charge | count |
|---|---|---|---|---|---|
| 11 | two 0, three −1 | none | 8 | +2 | 10 |
| 11 | one 1, four −1 | none | 10 | +2 | 5 |
| 11 | one 0, four −1 | +1 | 10 | +2 | 5 per external triple |
| 13 | one 0, five −1 | none | 8 | −2 | 6 |
| 13 | six −1 | +1 | 10 | −2 | 1 per external triple |
| 17,19 | none | — | — | — | 0 |

For an elementary check of exhaustiveness, write n_-2,n_0,n_1 for the exceptional counts relative to all d=-1. Then L=R+1+3n_-2+n_0+4n_1 and Q=1−R−3n_-2+3n_0+6n_1. For outside triple add 3 to L and ±3 to Q. The constraints are n_-2+n_0+n_1<=R and 3n_-2+n_0+4n_1<=9−R (or <=6−R with outside triple). Substitution of R=5,6,8,9 gives exactly the table. The checker independently enumerates all 332800 individual central arrays for these four R values, including both possible outside signs.

All extra relations have charge ±2. In particular Z,U,V,W on H agree with those on H_3, since their Fourier integrands have charge zero. Only ordinary-product target moments need extra corrections. This argument includes arbitrary prime powers and arbitrary combinations of the larger primes; it does not require enumeration for the full q.

## 5. Uniform Fourier error bound and positivity
Let E_v=E_h(F Re chi_v) for ordinary-product characters v=e_i+e_j. Under H_3 these are zero. By Fourier expansion, E_v is the sum of Fhat(c−v) for c in Lambda\Lambda_3 with charge +2. For balanced u of length 2h, the Fourier coefficient of X^k is

    (k!)²/m^k sum_(ell>=0,sum ell=k−h) prod_i 1/[(u_i^++ell_i)!(u_i^−+ell_i)!].

Thus |Fhat(u)|<=58464/m³ at h=3, <=28224/m^4 at h=4, and zero at h>4. The first bound follows by the triangle inequality using −840X³ and 49X^4, bounding the number of additional single occupancies by m. The second uses only 49X^4. The table's length-8 relations have five positive unit coefficients, allowing at most ten two-unit cancellation choices of v and at most 5m one-unit choices. There are at most 16 such relations. The length-10 simple relations have six positive unit coefficients, allowing at most fifteen v choices with two-unit cancellation; there are at most 6b of them counting external triples. The five length-10 double relations have two +1 and two +2 entries, allowing at most eight such choices including repeats. It follows that

    E_extra := 2 sum_v |E_v|
       <= 16*2*(10*58464/m³+5m*28224/m^4)
          + 2*6b*15*28224/m^4 + 2*5*8*28224/m^4
       <= 24917760/m³ + 2257920/m^4.

When neither 11 nor 13 divides q, E_extra=0. When either divides q and q>39, q>=99, so b>=16. For b=16+x the numerator of G−E_b minus the last upper bound is

    56376x^4+3245832x³+71894502x²+648979023x+1550708831 >0.

Thus for all these q the following is a strictly positive density on H (the sums are over the indicated cosines):

    f = [F+G+2(V−U) sum_within cos+2(V−W) sum_singleton cos
                   −2 sum_ordinary E_v Re chi_v] / (Z+G).

The correction magnitude is at most E_b+E_extra<G. The denominator is positive since F>=0 and G>0. Haar orthogonality shows its mass is exactly one and its distinct conjugate moments all equal V/(Z+G)=−1/(2m); its ordinary-product moments vanish. This gives the exact target, with a strict positive floor (not necessarily uniform in q). For q=39, b=6, there are no external triples and the only extra six vectors are the charge +2 sign reversals in the table. Direct exact coefficient summation gives E_extra=34231680/130321 and G−E_b−E_extra=9760481/130321>0, proving this case as well. For q=33 the same density's sufficient L1 margin is negative (−643381/4096); this is NOT a nonexistence result. We use the separate certificate in Section 6 instead.

## 6. Small cases
For q=3 the known positive result is in Kang's theorem; Haar on the free phase circle also directly gives the required ordinary moment zero.

For q=9 the real cyclotomic field degree is three, and the four independent cosine indices have the one triple relation. Indeed the real root values span the real field because they contain 1 up to sign (alpha_3=−1), and the real subfield is spanned by the symmetric sums of powers of zeta. Thus H=H_3. For auxiliary a=1/7>1/8, choose the triple aligned at a uniform cube root with probability rho=5/21, or a uniform permutation of all three roots otherwise. In the aligned event choose the singleton opposite the common root with probability lambda=3/5, independently uniform otherwise. In the balanced event make the singleton independently uniform. Triple product is one; both distinct within-triple and singleton-to-triple conjugate moments equal −a, since rho−(1−rho)/2=−a and −rho lambda=−a. All ordinary moments vanish by global cube rotation. Mix with Haar to realize the exact target with full support.

For q=33 the archived exact rational certificate q33.json from the earlier semiprime research is reused, not claimed as a new instance. It lists 32 positive rational weights and fourth-root phase seeds on a power basis of Q(zeta_33), averaged over the 20 units modulo 66. Each seed is the reduction modulo 4 of an integer linear functional on cyclotomic power-basis coefficients; hence all integer energy relations hold modulo 2 pi, and the phase vector lies in H. The Galois permutations preserve parity. The included exact verifier checks every one of the 496 original physical mode pairs, obtaining equal-parity coherence −1/(q−2) and opposite-parity zero; positive weights sum exactly to one. Mix with Haar as above. It was actually rerun for this note, along with the redundant q39.json prior certificate (703 physical pairs). It uses NumPy only for bounded integer counts, and arbitrary-precision rational/integer arithmetic for the result. This does not rely on numerical optimization or a claimed Lean check.

## 7. Passage to real time and combined theorem
The positive density construction yields a target in the relative interior of the convex hull C of cosine vectors on H: any supporting functional extremized at a full-support mean is constant by continuity. In the auxiliary cases q=9,33 mixing with Haar gives the same full-support property. For any positive algebraic delta, algebraicity of alpha and transcendence of pi imply delta c dot alpha in 2 pi Z if and only if c dot alpha=0. Kronecker's character theorem gives density of delta n alpha, n a nonnegative integer, in H (the nonnegative orbit has the same closure by compact recurrence). Translation by t0 alpha preserves H. The convex hull of actual grid cosine vectors has closure C and contains ri C by the standard relative-interior theorem. Hence the target is in the actual convex hull. By Caratheodory it uses at most m²+1 sample times; discard zero weights. This proves an existence result, not an explicit time schedule or a new quantitative maximum-time bound.

Combined with the prior proof for odd q coprime to three, this covers every odd q not divisible by 15 or 21. The remaining odd q are known collision cases, so the combined statement is a full candidate odd classification. For the entire original problem, even q not divisible by three still need general treatment. The present block construction is explicitly for odd q; in even q the positive-energy/zero-mode coherence requirements differ. We have not established the complete classification for all paths, and we found no new nonexistence counterexample.

## 8. Verification, limitations, and references
Run `python verify_three_blocks.py` (SymPy), `python verify_small.py` (SymPy, NumPy), and `cd prior-odd-coprime; python verify_short_relations.py`. Actual logs are included. The new checker derives the symbolic marked moments exactly, checks positive polynomial coefficients, the central enumeration, q=39 and q=33 density margins, and the small q=9 law. The prior exact checks were rerun, not independently Lean formalized. The general short-relation reasoning and the older coprime-to-three proof still need external review. No new Lean certificate has been produced. The previous P19 arithmetic certificate's successful Lean audit does not certify these general theorems. No personal author assigned; no GitHub changes made.

References:
1. M. Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, arXiv:2609.14463v1 (2026), https://arxiv.org/html/2609.14463v1.
2. P. Baptista, G. Coutinho, V. Marques, Unexpected Averages of Mixing Matrices, arXiv:2308.16378 (2023), https://arxiv.org/abs/2308.16378.
3. J. H. Conway and A. J. Jones, Trigonometric diophantine equations (On vanishing sums of roots of unity), Acta Arithmetica 30 (1976), 229–240, Theorem 5, https://doi.org/10.4064/aa-30-3-229-240.
4. H. W. Lenstra Jr., Vanishing sums of roots of unity, Theorem 2.6, https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1979d/art.pdf.
5. Previous working note, Uniform average mixing for every odd modulus coprime to three, included in prior-odd-coprime/; previous finite certificate for q=33 included here.
