# Uniform average mixing on paths: a complete arithmetic classification (revised candidate proof)

Working manuscript, 27 November 2026. AI-assisted, no personal author assigned. This revised proof has undergone internal cross-checks but not independent peer review or full Lean verification. No public repository has been changed.

## Abstract
We present a candidate proof of a classification of uniform average mixing for continuous-time adjacency walks on paths. For a path on N=q−1 vertices, the only forbidden moduli are multiples of 15 or 21, and multiples of 6 at least 12. The negative direction and the forced-coherence reduction are due to Kang (2026). The new positive direction uses strictly positive Fourier densities on cyclotomic phase groups, together with a classification of low-weight signed root-of-unity relations. A square-completion inequality and exact small-dimensional Fourier calculations eliminate the earlier reliance on linear-programming probability certificates in all fourteen exceptional moduli. The remaining finite computations are integer lattice enumeration and rational Fourier coefficients. We also establish exact finite readout laws on arbitrary prescribed nonnegative grids with positive algebraic step.

## Main theorem
For each integer q>=3, with N=q−1, let A denote the adjacency matrix of P_N. There exists a probability measure mu with E_mu |exp(itA)|^{circ 2}=J_N/N if and only if 15 does not divide q, 21 does not divide q, and either 6 does not divide q or q=6. For every admitted q, every algebraic delta>0 and every t0>=0, such a measure can be chosen with finite support in t0+delta Z_{>=0}. The support has at most m²+1 points for odd q, m=(q−1)/2, and m(m+1)+1 for even q, m=q/2−1. These bounds are not asserted minimal. The negative direction follows from Kang, arXiv:2609.14463v1; the positive direction outside his positive classes is the contribution here. The following parts supply the full candidate positive proof, without using any earlier general-family conjectures or numerical LP witnesses.

## Common reduction and short-relation localization
For theta_r=2 cos(r pi/q), the sine spectral projectors give E_mu M=D0+2 sum_{r<s} y_rs E_r∘E_s with D0=(2J+I+S)/(2q), S the reflection. The target y_rs=−1/N for equal mirror parity, and 0 otherwise, gives J/N because the sum of the entrywise squared parity projector sums is (I+S)/2. Kang proves necessity and the parity-collision obstructions. Here only sufficiency needs to be constructed.

The relevant compact phase groups are the closures of the real energy flow; their annihilator lattices are exactly the integer spectral relations. A real character cosine has Haar mean zero and squared norm 1/2 if its frequency is nonzero; distinct frequency classes modulo sign are orthogonal. Thus for a real nonnegative Fourier polynomial F, its actual mean Z_H and actual moments M_v, a scalar T>0, and target y_v, the polynomial

    f=[F+(T−Z_H)+2 sum_v(T y_v−M_v) Re chi_v]/T

has mass one and exactly the target moments if the target cosines are nontrivial and orthogonal. A sufficient positivity condition is T−Z_H>2 sum_v |T y_v−M_v|. Stronger pointwise lower bounds on the correction may be used instead, as in q=33 below. Full support is sufficient for this relative-interior argument; it is not necessary for existence of a time law.

We give an explicit justification of the localization step used in the three proof parts. A finite signed rational root array of zero evaluation is partitioned by successively removing nonempty vanishing subsets minimal under inclusion with the original coefficients. This process preserves the original weights; no coefficient is split and the supports are disjoint. For each minimal subset the Conway–Jones theorem (signed rational version, also Lenstra survey Theorem 2.6) says its reduced order d is squarefree and its support cardinality is >=2+sum_{p|d}(p−2). All exponents are in a single coset of the subgroup of order d. In the odd case use the cyclic group Z/q directly. In the even case put zeta=exp(pi i/q). Exponents ±r, 0<r<q/2, are distinct modulo q. Reducing modulo q identifies antipodal roots, absorbing the sign into the integer coefficient. A squarefree reduced order d' in the order-2q group projects to order d=d'/gcd(2,d'), which is odd and squarefree. The support size of each block is unchanged and the factor 2 contributes zero to the Conway–Jones bound. For a coset of order d, choose a representative a and lift its entries as zeta^a times d-th roots; signs are absorbed exactly. If every block order divides d, every block stays entirely in one d-coset; the restriction of the root array to that coset vanishes after this lift. This applies also if the original choice of minimal partition was not invariant under inversion. Reflection on cosets then follows from inversion symmetry of the *whole* array. A stable odd-order coset in Z/q contains exactly one solution of 2x=0, since multiplication by two is bijective on its odd-order subgroup. The fixed point is 0 in the odd case, and either 0 or q/2 in the even case. Both are absent from the positive-mode spectral array. In an even central lift, the common factors at the two fixed points are respectively 1 and i; the corresponding coefficient arrays obey A(−x)=A(x) and A(−x)=−A(x). Noncentral cosets are paired with their inverse and have equal absolute weight. Complete prime cycles are forced by irreducibility of Phi_p. Pure cycles of distinct prime orders intersect in at most one point, while two cosets of the same order coincide or are disjoint. These facts justify the pure-cycle pairing and central reduction used below. Support cardinality is always bounded above by absolute coefficient weight, and root absolute weight is twice spectral L1 weight. In the mixed case the relevant orders are read off from the Conway–Jones inequality and the total budget 20; the detailed partitions and multiplicities are established in the corresponding parts. This lemma does not assume symmetry of the minimal partition.

## Part I. Odd q coprime to 3
### 2. Spectral moments and polynomial density

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

### 3. Classification of the short relations that matter

We give the details because a bound on only the number of prime factors would not suffice. A relation c yields a symmetric integer array on Z/qZ, with coefficients c_j at j and −j (the same coefficient at both positions) and zero at 0, vanishing when evaluated at the primitive q-th root zeta. Its total absolute weight is 2|c| and its support size is at most 2|c|. We only require relations of even length <=10 and charge 0 or ±2.

#### 3.1. Minimal support decomposition

Use the signed rational version of the Conway–Jones bound: a minimal vanishing relation on distinct roots with reduced exponent d has d squarefree and support length at least 2+sum_{p|d}(p−2). Here minimal means that no proper nonempty subset, with its original coefficients, vanishes. Repeatedly remove minimal vanishing subsets; the resulting supports are disjoint. Each block is contained in a coset of the subgroup of order d. A block with prime reduced exponent is a full prime cycle with constant nonzero coefficient, by irreducibility of Phi_p. The prime factors of d divide q and hence are >=5.

In particular, no nonzero relation of even length <=4 exists: its root support would be at most 8, allowing at most one block; a mixed block needs >=10 roots and a single prime cycle has odd support, impossible by inversion symmetry with zero origin. Thus V consists of nontrivial characters distinct up to inversion modulo Lambda; the Haar cosines are orthogonal, with squared norm 1/2.

In the range of support <=20, the only possible composite reduced exponents are

    35, 55, 65, 85, 77, 91, 385.

This follows directly from the support bound: the two-prime lower bound is p+r−2 and the three-prime bound is p+r+s−4. The latter permits only 5,7,11. Four primes cannot occur.

#### 3.2. Pure prime-cycle relations

If all minimal blocks are prime cycles, there are at most four of them. Inversion sends each prime coset to a disjoint coset of the same subgroup, because an inversion-invariant coset in an odd cyclic group would contain 0, which is forbidden. The inverted cycle must coincide with another cycle of the same prime: otherwise it meets every other block of a different prime in at most one root and every block of the same prime in zero roots, and at most three intersections cannot cover >=5 roots. Symmetry then forces the equal coefficients on the paired cycles.

An inverse pair of p-cycles of coefficient A contributes p|A| to spectral length and pA to charge. Even length <=10 and charge 0 or ±2 therefore require exactly two inverse pairs of 5-cycles with coefficients +1 and −1. This is Type I. There are P=(q/5−1)/2=(m−2)/5 noncentral pairs of 5-cosets when 5|q, and at most P(P−1)<=m²/25 ordered choices. Each relation has five +1 and five −1 entries. If 5 does not divide q, there are no such relations.

#### 3.3. Mixed reduced exponents other than 35 and 385

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

#### 3.4. The conductor 35

If some mixed block has d=35, no block of any other mixed conductor or prime >=11 can coexist (minimum total support would exceed 20). All blocks lie in cosets of the subgroup of order 35. Group them by coset. The restriction to each coset vanishes, and inversion exchanges noncentral cosets. Each occupied noncentral inverse pair has spectral length at least 5; its length and charge are the absolute weight and signed sum of the 5x7 additive array in one coset. The central array also has length at least 5 by the short-support argument of Section 3.1. Hence at most two components (one central or one inverse coset pair counts as a component) occur.

If two components occur, both have length 5. A noncentral length-5 array is a pure 5-cycle. A central length-5 array has charge ±5 (pure 5-cycle pair) or ±1 (axis difference), as verified below. The only allowed combined charge is zero, from opposite 5-cycle pairs, which is Type I. If a single noncentral component occurs, an additive array with one axis constant consists of pure cycles, giving only Type I. For both axes nonconstant, choose the most frequent row value as zero. If its multiplicity were <=3, each column would have >=2 nonzero entries and total support >=14. Hence four rows are zero and one row is A!=0. Each of the seven columns has at least one nonzero; a column value −A costs four nonzero entries, while a value other than 0 or −A costs five. The support limit 10 forces exactly one column with value −A, all others zero. The ten nonzero entries must be ±1, as the length is <=10. This gives length 10, charge ±2, and six positives and four negatives for charge +2. There are 5*7=35 choices per noncentral inverse pair, with (q/35−1)/2 such pairs, at most m in total. Call this Type IV.

It remains to classify the central symmetric 5x7 array. Its independent coordinate values are

    a1,a2,b1,b2,b3, and two copies of each a_i+b_j (i=1,2; j=1,2,3).

Here a0=b0=0; a1,a2,b1,b2,b3 are integer axis values; the other axis values follow by inversion. The length is

    L=|a1|+|a2|+sum_j (|b_j|+2|a1+b_j|+2|a2+b_j|),

and charge Q=7(a1+a2)+5 sum b_j. We need L<=10. If a1!=a2, their difference is <=1 in absolute value by L>=6|a1−a2|. Up to permutation and global sign the only possible unequal pair is (0,1): if consecutive entries are u,u+1 with both of the same nonzero sign, each column costs at least 2+min(|u|,|u+1|), so L>=12. This column bound follows from |u+b|+|u+1+b|=1+2 dist(b,[−u−1,−u]) and the triangle inequality for |b|. For a=(0,1) each column b is 0 (cost 2) or −1 (cost 3); any other value costs >=7, incompatible with L<=10. With k entries −1 the length is 7+k and charge 7−5k. Even length and allowed charge require k=1, giving six possibilities (two row choices and three column choices) of length 8, charge +2, five +1 and three −1. Include the negatives for charge −2. Call this Type V.

If a1=a2=A then L>=5|A| so |A|<=2. For A=0, L=5 sum|b|, giving the pure cycles of Type I and the length-5 charge ±5. For A=1 up to global sign, each column costs |b|+4|1+b|; the baseline is 1 at b=−1. The only options within the total budget are all b=−1 (length 5, charge −1), one b=0 (length 8, charge 4), or one b=−2 (length 10, charge −6). None of these has even length and allowed charge. For A=2 all b=−2, with length 10 and charge −2; its negative has three +2 entries and two −2 entries. This is Type VI, one for each charge sign. These arguments also establish the length-5 classification used for two components. The companion checker exhaustively enumerates the five integer axes with l1 norm <=10, which is a necessary bound as the axis values are themselves among the coordinates; it independently confirms all 20 relevant central arrays and the length-5 cases.

#### 3.5. Excluding the three-prime reduced exponent 385

The Conway–Jones bound for 5*7*11 is 19; inversion forces even support, and weight <=20 forces exactly 20 entries, each +1 or −1. This is a single minimal block in the central subgroup. Write its CRT array as eleven 5x7 slices indexed by the 11-coordinate. Evaluating each slice at the primitive 35-root gives eleven elements of Q(zeta_35) that must all be equal, since Phi_11 is irreducible over Q(zeta_35) (the field degree ratio is 10). The common value is nonzero: otherwise every nonempty slice vanishes and minimality forces at most one nonempty slice, contradicting reduced exponent 385. Each slice is nonempty; since total support is 20, at least two are singletons. The common value is therefore ± a 35th root of unity. Inversion pairs the slice evaluations by conjugation, so the common value is real, necessarily ±1. Multiply all signs to make it +1. Every singleton is then +1 at the origin of its 35-slice.

A nonsingleton slice representing 1 must have at least four entries: subtracting the origin produces a nonzero vanishing relation on at most one additional root, and the minimum support is five. The central slice has zero origin and even support by inversion. Counting the nine support entries in excess of eleven singletons leaves only two configurations: (a) central slice with four entries, plus one inverse pair of slices of four entries; (b) central slice with ten entries and all other slices singleton. In case (a) each exceptional slice minus the origin is a five-term relation, so it is a 5-cycle through the origin and all its coordinates are in the subgroup of order 5. This would restrict the whole conductor to 55, a contradiction.

In case (b), subtract the origin in the central 35-slice. The result is an additive array A_ij=a_i+b_j with a0=0,b0=−1. Inversion pairs the axes. Since every entry is 0 or ±1, the two other independent a values belong to {0,1,2} and the three other independent b values to {−1,0,1}. The nonorigin half-weight would have to be 5, namely

    |a1−1|+|a2−1|+sum_j (|b_j|+2|a1+b_j|+2|a2+b_j|)=5.

This is impossible. If an a is 2, all b must be −1 and the left side is >=10. Otherwise a1,a2 in {0,1}. If both are zero the weight is 2+5k; if one is one and one zero it is >=7; if both are one it is 3+3k (k is a nonnegative integer). None is 5. The checker independently tests all 243 parameter tuples. This excludes reduced exponent 385 entirely in the relevant even-length range.

The six types above exhaust all relevant relations. Note that the classification is for length <=10 and charge 0 or ±2, not for all cyclotomic relations, and uses signed coefficients.

### 4. Positivity after Fourier correction

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


## Part II. Odd q divisible by 3 and coprime to 35
### 2. Phase torus and required moments
For odd q, put m=(q−1)/2 and alpha_j=2 cos(2 pi j/q), j=1,...,m. The physical energies consist of alpha_j at even mode 2j and −alpha_j at odd mode q−2j. Let H be the compact subgroup closure of t alpha modulo 2 pi, h its Haar probability, and z_j=exp(i phi_j). The relation lattice Lambda={c integer: c dot alpha=0} is the annihilator of H. For the character chi_c=z^c, E_h chi_c=1 if c in Lambda and zero otherwise.

The needed moments are E Re(z_i conjugate(z_j))=−1/(2m) for i<j, and E Re(z_i z_j)=0 for i<=j. These yield the target equal-parity coherence −1/N and opposite-parity coherence zero. The known spectral projector identity D0=(2J+I+S)/(2q), where S is reflection, and the squared parity projectors sum (I+S)/2 give D0−[(I+S)/2−D0]/N=J/N. Let V_index consist of the m² characters e_i−e_j (i<j), e_i+e_j (i<=j). Write |c| for its l1 length and Q(c)=sum c_i for its charge.

### 3. A model that retains every relation coming from three
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

### 4. Exact classification of the additional short relations
Only even-length c with |c|<=10 and Q(c) in {0,±2} can contribute to E_h F or E_h(F Re chi_v): F has length<=8 and charge zero in Fourier space, and v has length two. For orthogonality of the target cosines we also use the absence of any nonzero even relation of length<=4, regardless of charge.

Represent c as a symmetric signed integer array on Z/qZ, with coefficients c_j at ±j and zero at 0. Its support and absolute weight are at most 20. Partition its nonzero support into disjoint minimal vanishing subsets with their original coefficients. By the rational signed Conway–Jones theorem (Theorem 5, 1976; see also Lenstra's survey, Theorem 2.6), each subset is contained in a coset of a subgroup of squarefree order d, and the support size is at least 2+sum_(prime p|d)(p−2). A prime-order subset is a full prime cycle with constant coefficient by cyclotomic irreducibility.

Under gcd(q,35)=1 and 3|q, possible prime factors are 3 and primes>=11. Two distinct primes >=11 would have bound >=22, and a mixed triple of primes has bound >=23. Thus the only mixed conductors are 3r for r=11,13,17,19, with support at least r+1. At most one such block can occur. A pure large-prime cycle cannot occur in any symmetric array here: it cannot be in the central coset (contains 0), and its inverse coset is disjoint and requires at least r additional support entries, exceeding 20. In the absence of a mixed block, every component is a pure 3-cycle, and inversion pairs the disjoint cosets. The relation is then in Lambda_3. In particular for length<=4 (root support<=8) all relations are in Lambda_3; a nonzero such vector has length a multiple of 3, so none has even length<=4. This proves the target cosines on H are nontrivial, distinct up to inversion, mutually orthogonal, with squared norms 1/2.

If there is a mixed block, it must lie in the central subgroup of order 3r: otherwise its inverse coset would require another >=r+1 entries. Every remaining block is a 3-cycle. Those outside the central subgroup occur in inverse pairs, and inside are included in the central array. The central array vanishes at the 3r-th primitive root, since each of its constituent blocks vanishes. CRT identifies all such rational arrays on a 3 by r rectangle with additive arrays A_(i,j)=a_i+d_j: row and column constant arrays are in the kernel, and their dimension 3+r−1 equals 3r−phi(3r). Normalizing a_0=d_0=0 is valid because the origin coefficient is zero; the axis values are integers. Inversion gives a_1=a_2=t and d_j=d_(−j). Denote the R=(r−1)/2 independent nonzero d values by d_1,...,d_R. The central independent spectral coordinates are exactly

    t, and (d_j,t+d_j,t+d_j) for each j.

If t=0 the array consists only of 3-cycles and lies in Lambda_3. Otherwise |t|>=1, and central length L=|t|+sum_j (|d_j|+2|t+d_j|)>=(R+1)|t|, forcing |t|=1. By global sign assume t=1. Then each d_j is in {−2,−1,0,1}, because any other value has cost>=7 while each remaining column costs at least one, R>=5 and total length<=10. At most one outside inverse pair of 3-cycles can be present, of length3 and coefficient sign ±1, since L>=6. The column values (−2,−1,0,1) have respective length contributions (4,1,2,5), and charges (−4,−1,2,5); the initial t contributes one to length and charge. Count the number of each column value. Keeping only even total length<=10 and charge 0 or ±2, including a possible outside triple, gives the following exhaustive table. Counts refer to t=1; sign is selected uniquely to give charge +2 for the actual correction.

| r | central d pattern (permutation) | outside triple sign | total length | charge | count |
|---|---|---|---|---|---|
| 11 | two 0, three −1 | none | 8 | +2 | 10 |
| 11 | one 1, four −1 (two coefficients of magnitude 2) | none | 10 | +2 | 5 |
| 11 | one 0, four −1 | +1 | 10 | +2 | 5 per external triple |
| 13 | one 0, five −1 | none | 8 | −2 | 6 |
| 13 | six −1 | +1 | 10 | −2 | 1 per external triple |
| 17,19 | none | — | — | — | 0 |

For an elementary check of exhaustiveness, write n_-2,n_0,n_1 for the exceptional counts relative to all d=-1. Then L=R+1+3n_-2+n_0+4n_1 and Q=1−R−3n_-2+3n_0+6n_1. For outside triple add 3 to L and ±3 to Q. The constraints are n_-2+n_0+n_1<=R and 3n_-2+n_0+4n_1<=9−R (or <=6−R with outside triple). Substitution of R=5,6,8,9 gives exactly the table. The checker independently enumerates all 332800 individual central arrays for these four R values, including both possible outside signs.

All extra relations have charge ±2. In particular Z,U,V,W on H agree with those on H_3, since their Fourier integrands have charge zero. Only ordinary-product target moments need extra corrections. This argument includes arbitrary prime powers and arbitrary combinations of the larger primes; it does not require enumeration for the full q.

### 5. Uniform Fourier error bound and positivity
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

The correction magnitude is at most E_b+E_extra<G. The denominator is positive since F>=0 and G>0. Haar orthogonality shows its mass is exactly one and its distinct conjugate moments all equal V/(Z+G)=−1/(2m); its ordinary-product moments vanish. This gives the exact target, with a strict positive floor (not necessarily uniform in q). For q=39, b=6, there are no external triples and the only extra six vectors are the charge +2 sign reversals in the table. Direct exact coefficient summation gives E_extra=34231680/130321 and G−E_b−E_extra=9760481/130321>0, proving this case as well. For q=33 the separate L1 bound is negative (−643381/4096), but Section 6 supplies a sharper square-completion bound proving the same density strictly positive.

### 6. Small cases
For q=3 the known positive result is in Kang's theorem; Haar on the free phase circle also directly gives the required ordinary moment zero.

For q=9 the real cyclotomic field degree is three, and the four independent cosine indices have the one triple relation. Indeed the real root values span the real field because they contain 1 up to sign (alpha_3=−1), and the real subfield is spanned by the symmetric sums of powers of zeta. Thus H=H_3. For auxiliary a=1/7>1/8, choose the triple aligned at a uniform cube root with probability rho=5/21, or a uniform permutation of all three roots otherwise. In the aligned event choose the singleton opposite the common root with probability lambda=3/5, independently uniform otherwise. In the balanced event make the singleton independently uniform. Triple product is one; both distinct within-triple and singleton-to-triple conjugate moments equal −a, since rho−(1−rho)/2=−a and −rho lambda=−a. All ordinary moments vanish by global cube rotation. Mix with Haar to realize the exact target with full support.

For q=33 no probability certificate is needed. There are five triples, with sums s_j=z_{j,1}+z_{j,2}+z_{j,3}, and a singleton z0. Write A_c=V−U=42107/4096>0 and B_c=V−W=40931/4096. The two conjugate correction sums in the numerator of f, per triple, equal

    A_c(|s_j|²−3)+2 B_c Re(s_j conjugate(z0))
      = A_c |s_j+(B_c/A_c) z0|²−3A_c−B_c²/A_c.

Hence the combined five-triple correction is bounded below by −5(3A_c+B_c²/A_c), rather than the old separate L1 bound −30(A_c+B_c). Exact independent cyclotomic enumeration (134245 free vectors of length at most 10, 352 nonzero short relations) and multinomial coefficient extraction give Z=16555999/4096, U=−1342297/8192, V=−1258083/8192, W=−1339945/8192, G=3573329/4096 and E_extra=862785/2048. Therefore

    G−5(3A_c+B_c²/A_c)−E_extra = 42831862673/172470272 > 0.

All 256 target moments and the normalization were checked exactly. This proves positivity of the original three-block density at q=33, independent of the archived LP certificate. See verify_q33_density.py. The failed earlier separate L1 bound and exploratory polynomial optimization are not counterexamples.


## Part III. Even q coprime to 3
### 2. Spectral reduction and independent parity groups

The eigenvalues of the adjacency matrix A of P_N are theta_r=2 cos(r pi/q), 1<=r<=N, with real projectors E_r from normalized sine eigenvectors. If y_rs=E cos((theta_r−theta_s)T), the mean mixing matrix is D0+2 sum_{r<s} y_rs E_r∘E_s. The standard sine sum gives D0=(2J+I+S)/(2q), where S is the reversal matrix. The sum of the two squared parity-projector sums is (I+S)/2. Thus it suffices to realize y_rs=−1/N for distinct indices of the same parity and zero otherwise. The resulting matrix is D0−[(I+S)/2−D0]/N=J/N. The criterion and its necessity are due to Kang, not new here.

For even q=2h there are h−1 positive modes r=1,...,h−1, their negatives at q−r, and a zero mode at r=h. Let H be the closure of the continuous phase flow of the positive modes. Its integer relation lattice Lambda consists of c with sum c_r theta_r=0. Put z_r=exp(i phi_r). The character form of Kronecker's theorem says H is precisely the common kernel of the characters in Lambda. The automorphism of Q(zeta), zeta=exp(pi i/q), sending zeta to −zeta (valid since gcd(q+1,2q)=1) sends theta_r to (−1)^r theta_r. Every rational relation therefore splits into its even and odd parts; the integer relation lattice likewise splits. H is the direct product of its two parity phase groups. We construct independent phase laws on these two groups.

In a group of n positive coordinates write b=1 if its parity is that of the zero mode, and b=0 otherwise. Set a=1/N. Required moments are

    E cos phi_i=−b a,
    E cos(2 phi_i)=−a,
    E cos(phi_i+phi_j)=E cos(phi_i−phi_j)=−a for i<j.

Conjugation-symmetric laws have zero sine means. Independence between groups, and the zero cosine means in the b=0 group, make all cross-parity moments zero. Negative modes receive the opposite phase and the zero mode phase zero; hence the listed requirements cover all full spectral pairs. Counting parity sizes gives N>=4n−1 for b=0 and N>=4n+1 for b=1. Indeed if h=2l the group sizes are l (unbiased) and l−1 (biased), and N=4l−1; if h=2l+1 both sizes are l and N=4l+1.

### 3. A nonnegative low-degree density and exact independent-circle moments

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

### 4. The phase lattice: all short relations relevant to this density

Only integer relations c of length |c|_1<=10 can affect normalization or a moment of length <=2. In this section assume 3 does not divide the even modulus q, so its odd primes are >=5. Work in one parity group of positive indices. Write a relation as an integer root array on exponents ±r, using coefficient c_r at both r and −r. Its support is inversion-symmetric and has size at most 2|c|_1; its absolute weight is exactly 2|c|_1.

#### 4.1 Projective reduction

Project exponents modulo q, identifying antipodal roots of order 2q (the two roots differ by a sign). No two supported exponents are identified: the chosen range −h<r<h has diameter q−2. The two fixed points of inversion, 0 and h, are absent. Each root coefficient keeps its absolute value, and a sign may be absorbed into the coefficient when changing lifts. Partition the root support into disjoint minimal vanishing subsets, retaining the original coefficients. The Conway–Jones bound (Theorems 1 and 5, 1976, p.235) gives a squarefree reduced exponent and support at least 2+sum(p−2) over its distinct prime divisors. After projective reduction the conductor d is odd and squarefree, and the block lies in a coset of the subgroup of order d of Z/q. Indeed the possible factor 2 becomes a sign, and dropping it leaves the support bound unchanged. For odd d, choose a lift of any such coset as zeta^a times all d-th roots. Ratios and coefficients can be adjusted by signs, without changing the absolute weight or vanishing property. A prime-conductor block consists of a complete prime cycle with a constant signed coefficient in this lift.

An inverse-stable coset of an odd-order subgroup contains exactly one of the two fixed points 0,h. In a central coset containing 0, the lifted coefficient array is symmetric under inversion; in the central coset containing h, use zeta^h=i as a common factor and the lifted array is antisymmetric, because inversion conjugates i to −i. For noncentral inverse coset pairs, the arrays correspond by conjugation up to a common sign and have equal absolute weight. These facts are why the even case needs an additional antisymmetric analysis compared with the odd proofs.

A nonzero relation of length <=4 cannot occur: its support is even and <=8, so there is at most one minimal block; a mixed odd conductor needs >=10 entries, and a pure prime cycle has odd support. This also holds if all odd primes are absent. In particular all characters in V={e_i,2e_i, e_i±e_j (i<j)} are nontrivial and pairwise distinct up to sign modulo Lambda. Their real cosines are orthogonal under Haar measure, with squared norm 1/2.

If every odd prime factor is >=11, the same reasoning rules out all nonzero relations of length <=10: two minimal blocks need at least 22 entries, a mixed conductor needs at least 22, and a sole prime cycle has odd support. In that case all moments in Section 3 are exactly the actual Haar moments and no extra correction is necessary.

#### 4.2 Pure cycles

For general odd primes >=5, the support bound allows at most four minimal blocks. If all are pure prime cycles, inversion pairs cycles with other cycles of the same prime. To see this, the inverse coset cannot equal the original one (it would contain an excluded fixed point). If it did not coincide with another same-prime coset, it could meet each of the at most three other blocks in at most one point, insufficient to cover its >=5 points. Equal absolute coefficients follow by symmetry of the original root array. An inverse pair of p-cycles contributes p|A| to the spectral length, where A is a nonzero integer. Distinct inverse pairs of p-cycles have disjoint spectral supports, at most n/p in a parity group. Therefore the possible patterns of absolute nonzero spectral coefficients, with upper bounds on their multiplicities, are:

    5 ones, 2n/5;
    5 twos, 2n/5;
    10 ones from two distinct 5-cycle pairs, 2(n/5)(n/5−1);
    7 ones, 2n/7.

These are real-valued upper bounds on integer counts for n>=35; they include both signs. No combination of 5 and 7 can fit length ten.

#### 4.3 Other mixed conductors than 35 and 385

By the support bound the only possible mixed odd conductors are 35,55,65,85,77,91,385. For d=55,65,85,77,91 a mixed block needs >=14 entries, so its coset is central (otherwise inversion doubles that count). Only a further pure 5-cycle can fit when d=55. It must be inside the same central coset: if outside it would be the only block there and would have to be inversion-stable, impossible for a complete cycle with excluded fixed points. Thus the entire array is in the central coset.

For d=pr, the kernel of root evaluation on a p by r array consists of additive arrays A_ij=a_i+b_j, because these vanish by the complete prime cycles and their dimension p+r−1 is the kernel dimension pr−phi(pr). With the origin coefficient zero, set a0=b0=0; the axes are integer. In the symmetric case a_−i=a_i, b_−j=b_j. In the antisymmetric case a_−i=−a_i, b_−j=−b_j. If an axis vanishes the relation consists of pure cycles already counted. Otherwise let u,v be the even counts of nonzero entries on the axes. The support is at least u(r−v)+(p−u)v. For the antisymmetric case, the nonzero-axis intersection contains at least uv/2 additional nonzero entries (at most two of the four sign-pair sums can vanish). The resulting lower bound exceeds 20 in all five conductors, as verified by enumerating the indicated even u,v.

In the symmetric case the only options with the baseline <=20 are

    5,11: (u,v,baseline)=(4,8,20),(4,10,14);
    5,13: (4,12,16);
    5,17: (4,16,20);
    7,11: (6,10,16);
    7,13: (6,12,18).

There is room for at most one nonzero cell of the matrix on paired nonzero axes (each cell costs four support entries). The rectangle identity for an additive matrix rules out precisely one nonzero cell on a matrix with at least two rows and columns. Hence all intersections vanish, a_i have the same nonzero value A and b_j have −A on their nonzero axes. Since the length is half the baseline times |A|, |A|=1. Counting choices including sign gives at most 2 length-7, 12 length-10, 4 length-8 and 2 length-9 vectors, all with absolute coefficients one. In detail, 55 has two full-axis length-7 relations and ten partial-axis length-10 relations, 65 has two length-8, 85 two length-10, 77 two length-8, and 91 two length-9. All are in the symmetric central coset; overcounting a parity group is harmless.

#### 4.4 Conductor 35

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

The inventory above also has a short analytic proof. In the symmetric case with unequal a1,a2, the length bound L>=6|a1−a2| implies they differ by one. If both are nonzero with the same sign, each column costs at least 2+min(|a1|,|a2|), and the total is at least 12. Up to row swap and global sign the pair is (0,1); b entries are 0 or −1, since any other costs at least 7 and the other two columns cost at least 2 each. The nonzero-axis condition leaves k=1,2,3 entries of −1, giving 4 binomial(3,k) arrays of respective lengths 8,9,10, all unit coefficients. For equal a1=a2=A!=0, each column costs at least |A|, so |A|<=2. At |A|=2 all b_j=−A. At A=1 up to sign, all b_j=−1, except possibly one 0 or one −2; the cost increments are 3 and 5 respectively from baseline 1. This gives 2 length-five, 2 five-double, 6 length-eight and 6 mixed-double arrays. Thus the symmetric table is exactly 44. In the antisymmetric case each column costs |b|+2 max(|a1|,|b|)+2 max(|a2|,|b|). Therefore L>=7(|a1|+|a2|); with both axes nonzero the row pair has precisely one entry ±1. A nonzero column adds at least 3, so exactly one column is ±1 and others zero. The 2*2*3*2=24 arrays have eight unit coefficients and one double. This proves the full inventory without enumeration.

If a central mixed component is accompanied by another nonzero component, each has spectral length >=5 by Section 4.1, so each has length exactly five. A central mixed component of length five is one of the two symmetric entries in the table; there is no antisymmetric one. An accompanying component must therefore be a pure 5-cycle inverse pair, with at most 2n/5 signed choices; its support is disjoint from the central component. This produces at most 4n/5 additional length-10 all-unit relations. If one axis vanishes or a whole central array is purely a sum of cycles, it is already covered by the pure cases; extra counts only enlarge the bound.

#### 4.5 Exclusion of conductor 385

A 5*7*11 minimal block requires >=19 roots. It is alone, must be central by inversion, and has exactly 20 roots of coefficients ±1. In a central lift, take slices indexed by the 11-coordinate. All 11 slices have the same evaluation in Q(zeta_35), by irreducibility of Phi_11 over that field (degree ratio 10). The common value is nonzero by minimality and all slices nonempty. At least two slices are singletons because there are only 20 terms. In the antisymmetric case the common value is purely imaginary, impossible for ± a root of odd order 35. In the symmetric case it is real, thus ±1; fix sign to make it 1. Every singleton is then at the slice origin with coefficient +1. A nonsingleton representing 1 needs at least four entries, since subtracting the origin produces a vanishing sum of minimum length five. The central slice (index zero) has even support, with origin absent. There are nine excess entries beyond eleven singletons, allowing only (i) a central slice of four entries plus one inverse pair of four-entry slices, or (ii) a central slice of ten entries. In (i) subtracting the origin from each exceptional slice produces a five-cycle through the origin, confining all coordinates to the order-5 subgroup and lowering the conductor to 55. In (ii) subtract the origin from the central slice. The resulting additive 5 by 7 array has a0=0,b0=−1, and by symmetry a1,a2 in {0,1,2}, b1,b2,b3 in {−1,0,1}. Its nonorigin spectral absolute weight must be five, with all entries 0,±1. The half-weight is |a1−1|+|a2−1|+sum_j(|b_j|+2|a1+b_j|+2|a2+b_j|). If either a is 2, all b must be −1 and the weight is at least 10. If both a are zero it is 2+5k; if one is zero and one is one it is at least 7; if both are one it is 3+3k (k>=0 integer). None equals 5. Thus no enumeration is needed, although verify_classification.py independently confirms all 243 tuples. It excludes 385 and completes the short-relation count for all even q not divisible by 3.

### 5. Uniform error bound and positivity

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

### 6. The finite exceptional even moduli: a uniform density proof
For q>=142 both parity groups have n>=35 and the preceding global estimate applies. For q<142, all odd primes >=11 give the relation-free construction when n>=2; Kang's prime, twice-prime and power-of-two cases include the remaining small trivial groups. The only leftover moduli are 20,28,40,50,56,70,80,98,100,110,112,130,140. We now use the same F and f from Sections 3 and 5 at each of these, rather than separate rational phase laws. For each group compute its full short relation set using the classified coset templates. Independently, form the integer matrix whose columns are the coefficient vectors of zeta^r+zeta^(2q−r) reduced modulo Phi_(2q). Its kernel is exactly the relation lattice. In exact rational RREF, pivot coordinates are determined by the free coordinates; every vector of L1 length <=10 has free coordinates of L1 length <=10. Enumerate every such free integer vector and retain those whose reconstructed pivots are integral and full length <=10. The two independently generated lists agree for all 26 groups. The exhaustive free-vector count in dimension d is sum_{k=0}^{min(d,10)} 2^k binomial(d,k) binomial(10,k), including zero; this count is checked for every run. The full enumeration visited 30,094,218 free vectors, finding 1,032 nonzero short relations across these groups.

For each group let E0 and E_v be the signed deviations from independent-circle Fourier moments. Use the exact coefficients derived in Section 3, or equivalently the independent rational convolution in verify_small_density.py. Set G=−NU−Z, and compute the lower bound G−|E0|−2 sum_v |M_v−M_v^*−E_v|. This uses the combined correction rather than the loose universal error bound, and it is strictly positive in every group. The exact fractions are as follows (unnormalized density numerator lower bounds).

| q | b=0 | b=1 |
|---:|---:|---:|
| 20 | 752081112/125 | 30605133975/1024 |
| 28 | 4974457406/343 | 133492232099/5184 |
| 40 | 22777155583/2000 | 39539812072/6561 |
| 50 | 55156219957/3456 | 317250915367/82944 |
| 56 | 89452933839/5488 | 516127998194/28561 |
| 70 | 827409267032/83521 | 592910213054/83521 |
| 80 | 8652465777/640 | 75240923933/6859 |
| 98 | 60257790181/3456 | 6700525612253/442368 |
| 100 | 1080680395096/78125 | 15674992291783/1327104 |
| 110 | 2708915506934/177147 | 5465057910343/531441 |
| 112 | 687151899013/43904 | 8869353993959/531441 |
| 130 | 3980234001653/262144 | 44423332664567/4194304 |
| 140 | 589959734214/42875 | 53601692253139/5345344 |

Thus all thirteen small even moduli use the same positive density as the general construction. This removes the need for any large probability matrix certificate. Verification consists of rational Fourier sums and exhaustive integer lattice checks, not a numerical optimizer. The coset-template generator is the fast route; RREF is an independent check of the enumeration.

## Passage to actual readout times and final conclusion
Every positive construction above gives a full-support phase probability on the energy orbit closure H (including the explicit q=9 law mixed with Haar). For the known positive classes, Kang's ramp with amplitude factor >1 mixed with Haar gives the same full-support property; q=3 has the required target under Haar directly. If C is the convex hull of the finite vector of cosines on H, a full-support mean lies in ri C: a supporting linear functional attaining its extremum at that mean must be constant throughout H by continuity. For delta>0 algebraic and any integer coefficient vector c, delta c·theta is algebraic, so delta c·theta belongs to 2pi Z iff c·theta=0 by transcendence of pi. Kronecker's character criterion implies that the grid orbit has the same closure as the continuous orbit; nonnegative iterates are dense in the same compact group by recurrence. Translation by t0 stays in H. The convex hull of grid cosine vectors has closure C and contains ri C, so the target is realized by a finite convex combination of actual grid vectors. Caratheodory's theorem bounds its support by m²+1 for odd q and m(m+1)+1 for even q from the number of possible positive-mode gap characters, including zero-mode gaps in the latter. Zero weights can be removed. Thus the result is existence of a finite exact time law, not a concrete short waiting-time schedule. All moduli q>=3 are covered by the three positive parts and Kang's negative theorem.

## Verification and limitations
The symbolic moment and global positivity checks from the three original notes remain in the accompanying verification sources. The revised small cases no longer use any LP probability certificates. The C++ enumeration uses bounded integer inputs; verify_lattice.py checks the free-vector count, integrality, and every accepted relation against the exact cyclotomic matrix. q33-density.log records the exact square-completion check. These are computational mathematical checks, not a Lean kernel proof or independent peer review. The analytical short-relation localization is stated explicitly above and deserves external review. The priority search on 27 November 2026 found Kang's v1 still giving only the earlier positive and negative families, and no matching complete positive theorem. Related classical vanishing-sum classifications are prior work; novelty is claimed only provisionally for the specific positive construction and complete classification. No personal author assigned.

## References
1. Musung Kang, Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains, arXiv:2609.14463v1 (2026), https://arxiv.org/html/2609.14463v1.
2. P. Baptista, G. Coutinho, V. Marques, Unexpected Averages of Mixing Matrices, Quantum Information Processing 23, 272 (2024), https://doi.org/10.1007/s11128-024-04480-0; arXiv:2308.16378.
3. J. H. Conway, A. J. Jones, Trigonometric diophantine equations (On vanishing sums of roots of unity), Acta Arith. 30 (1976), 229–240, https://doi.org/10.4064/aa-30-3-229-240.
4. H. W. Lenstra Jr., Vanishing sums of roots of unity, Theorem 2.6, https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1979d/art.pdf.
5. M. Kang, Moment Methods for Uniform Average Mixing on Strongly Regular Graphs, arXiv:2610.10017 (2026), https://arxiv.org/abs/2610.10017.
