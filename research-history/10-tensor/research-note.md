# Uniform average mixing on paths with many distinct prime factors

## Cyclotomic tensor interpolation and randomized phase matching

Research manuscript draft — 27 November 2026. No author assigned. AI-assisted; not independently peer-reviewed or Lean-formalized. The proofs below are self-contained apart from explicitly stated standard results. This is a working research record, not a final release.

### Abstract

For the path graph $P_{q-1}$, uniform average mixing asks whether a single probability law for the readout time produces a uniform final vertex distribution from every initial vertex. We develop a sufficient condition for moduli $q$ with arbitrarily many distinct odd prime factors and arbitrary prime-power multiplicities. The construction identifies the cyclotomic relation space with a tensor product of zero-sum spaces, uses random coordinate reserves to allow arbitrary prescribed phases and two additional marginals, and applies random matching to impose the desired second moments. For odd $q$ with $s$ distinct odd primes, the condition holds whenever the least prime exceeds $12s+5$. For even $q$ with $s\ge1$ distinct odd primes, it holds whenever the least odd prime is at least $18s+5$. The result also provides sharper rational tests depending on the entire factorization and implies the existence of finite readout protocols on any prescribed positive algebraic time lattice, starting after an arbitrary nonnegative offset. Exact rational computations independently test the tensor interpolation and pair-moment formulae. No full classification is claimed.

## 1. Main result and context

Let $q\ge3$, $N=q-1$, and $A$ be the adjacency matrix of $P_N$. Write

$$M(t)=|\exp(itA)|^{\circ2}.$$

We seek a probability law $\mu$ such that $\int M(t)\,d\mu(t)=J_N/N$. In contrast to a Cesàro time average, the law is freely chosen, and must work for all initial vertices simultaneously. Baptista, Coutinho and Marques introduced the relevant question; Kang (2026), arXiv:2609.14463v1, established positive results for prime moduli, twice a prime and powers of two, and nonexistence for $15\mid q$, $21\mid q$, or $6\mid q$ with $q\ge12$. Kang also classified **all parity collisions**, which is prior work, not a new contribution here. Whether their absence is sufficient in every remaining case is still a conjecture in this research record.

**Theorem 1 (factorization-dependent sufficient condition).** Write

$$q=2^k n,\qquad n=\prod_{j=1}^s p_j^{e_j},\qquad e_j\ge1,\quad p_j\ge11$$

with distinct odd primes and $s\ge1$. Define

$$B=\prod_j p_j^{e_j-1}(p_j-6),\quad
\alpha=\prod_j\frac{p_j-7}{p_j-1},\quad
\beta=\prod_j\frac{(p_j-7)(p_j-9)}{(p_j-1)(p_j-3)},\quad a_0=\frac1{q-1}.$$

For a positive integer $M$, define $K(M)=M-1$ if $M$ is even and $K(M)=M$ otherwise. Then each of the following is sufficient for uniform average mixing:

* **Odd $q$ ($k=0$):** set $M=(B-1)/2$ and $K=K(M)$. Require $\beta>K a_0$.
* **Even $q$ ($k\ge1$):** set $M_*=(B-1)/2$ for $k=1$, and $M_*=2^{k-2}B$ for $k\ge2$. Require

$$\frac{M_*a_0}{\beta}+\frac{M_*a_0^2}{\alpha^2}<\frac12-\frac{3a_0}{2\alpha}.$$

Whenever a condition holds, for every $\delta>0$ algebraic over $\mathbb Q$ and every real $t_0\ge0$, there are distinct nonnegative integers $n_i$ and positive probabilities $w_i$ summing to one such that

$$\sum_i w_i M(t_0+n_i\delta)=J_N/N.$$

At most $m^2+1$ times are required when $q$ is odd, and at most $m(m+1)+1$ when $q$ is even, with $m=\lfloor(q-1)/2\rfloor$. These are upper bounds, not optimality claims. Failure of either sufficient test does not imply nonexistence.

**Corollary 2 (arbitrarily many prime factors).** Write $p_*=\min_j p_j$. It suffices that

$$p_*>12s+5\quad (q\text{ odd}),\qquad
p_*\ge18s+5\quad (q\text{ even}).$$

Thus there is no fixed upper bound on the number of distinct odd prime factors in the family proved here, and the exponents $e_j$ and $k$ are unrestricted by these bounds. Section 6 gives a proof with elementary inequalities.

## 2. Spectral target and the passage from phase laws to actual times

The path eigenvalues are $\theta_r=2\cos(r\pi/q)$ for $1\le r\le N$ and the spectral projectors are $E_r=u_ru_r^\top$, with $u_r(v)=\sqrt{2/q}\sin(rv\pi/q)$. Write $H_0$ for the reversal permutation matrix. The standard finite sine sums (or the formula of Godsil) give

$$D_0:=\sum_r E_r^{\circ2}=\frac{2J+I+H_0}{2q}.$$

The parity projector sums are $(I+H_0)/2$ and $(I-H_0)/2$, and the sum of their entrywise squares is $(I+H_0)/2$. Thus the cosine moment target

$$y_{rs}=\begin{cases}-1/N,&r\ne s,\ r\equiv s\pmod2,\\0,&r\not\equiv s\pmod2\end{cases}$$

suffices, since the averaged spectral expansion gives

$$D_0-\frac1N\big((I+H_0)/2-D_0\big)=J/N.$$

Kang's forced-coherence lemma also proves necessity, but only sufficiency is needed for Theorem 1.

Let $H$ be the closure in the phase torus of the continuous-time vector $t\theta$ modulo $2\pi$, with all $N$ modes included. Kronecker's character theorem identifies it as the common kernel of the characters $c\in\mathbb Z^N$ satisfying $c\cdot\theta=0$. The entries of $\theta$ are algebraic. For nonzero algebraic $\delta$, $\delta c\cdot\theta\in2\pi\mathbb Z$ implies $c\cdot\theta=0$ by transcendence of $\pi$. Therefore the closure of integer multiples of $\delta\theta$ is also $H$; the nonnegative multiples have the same closure by recurrence of rotations on a compact group. One elementary justification of the latter statement is that there are arbitrarily large positive integers $h_j$ with $h_j\delta\theta\to0$ modulo $2\pi$ (compactness, or simultaneous approximation); then $(h_j-r)\delta\theta\to-r\delta\theta$ for any fixed positive integer $r$. Translation by $t_0\theta\in H$ preserves $H$.

Define $F:H\to\mathbb R^{\binom N2}$ by $F_{rs}(\phi)=\cos(\phi_r-\phi_s)$ for $r<s$. Let $C=\operatorname{conv}F(H)$, compact by finite-dimensional Carathéodory. Haar probability on $H$ has $F$-mean zero, because each distinct-mode difference character is nontrivial. The full support of Haar places zero in the relative interior of $C$: any supporting affine functional taking its extremal value at the mean would have to be constant on all of $F(H)$ by continuity.

Suppose there is a phase law supported on $H$ realizing the auxiliary moment vector with equal-parity entries $-a$ and opposite-parity entries zero, where $a>a_0$. Its mixture with Haar in proportions $a_0/a$ and $1-a_0/a$ has the exact target as its mean, in the relative interior of $C$. The actual sampled moment vectors $D=\{F((t_0+h\delta)\theta):h\ge0,\ h\in\mathbb Z\}$ are dense in $F(H)$, hence $\overline{\operatorname{conv}D}=C$. The relative interior of a convex set equals that of its closure, so the target is in $\operatorname{conv}D$ itself. This is the crucial step from a torus law to an actual time law. It is not an assertion that the auxiliary phase samples are exact physical-time samples. The target has a finite convex representation; discard zero weights and merge repeats. There are at most $m^2$ different positive frequencies when there is no zero mode (forms $2\theta_i$, $\theta_i+\theta_j$, $\theta_i-\theta_j$), and at most $m(m+1)$ when there is a zero mode (add $\theta_i$). Equal frequency coordinates of $F$ agree on the dense orbit and on $H$. The support bounds follow.

## 3. The cyclotomic tensor interpolation lemma

### 3.1 The full array of root evaluations

For odd $q$ let $L=q$ and $\zeta=\exp(2\pi i/L)$. For even $q$ let $L=2q$ and use the same definition of $\zeta$. Decompose $\mathbb Z/L\mathbb Z$ by the Chinese remainder theorem into coordinates of moduli $p_j^{e_j}$, together with modulus $2^{k+1}$ if $k\ge1$. Denote an element of this product by $x$. For each odd prime coordinate of modulus $d=p^e$, a fiber is a residue class modulo $h=d/p$ in $\mathbb Z/d\mathbb Z$, containing $p$ residues.

Consider real arrays $f(x)$ satisfying all zero-sum constraints on each such fiber, keeping all other coordinates fixed. In the even case also require

$$f(a+2^k,b)=-f(a,b),$$

where $a$ is the 2-power coordinate and $b$ denotes all odd coordinates. These are exactly the arrays $f(x)=\ell(\zeta^{r(x)})$ as $\ell$ ranges over the $\mathbb Q$-linear maps $\mathbb Q(\zeta)\to\mathbb R$ (with $r(x)$ the CRT representative). To see this, evaluations of any such functional satisfy the stated constraints by geometric series; the evaluation map is injective because the powers of $\zeta$ span the field. The real dimension of its domain is $\varphi(L)$. Conversely the array space has dimension $\varphi(L)$: in each prime-power coordinate the constraints on disjoint fibers leave dimension $d-d/p$, and the even-factor space has dimension $2^k$. Simultaneously imposing the constraints in separate tensor coordinates gives the tensor product of these spaces, as is seen by choosing a basis for the kernel in each factor and extending it to a basis of the full factor space. The product of the dimensions is $\varphi(L)$. Thus the evaluation map is onto.

Impose in addition inversion symmetry $f(-x)=f(x)$. Such arrays, restricted to the appropriate independent spectral coordinates, define phase angles satisfying all rational energy relations. Indeed $2f(r)=\ell(\zeta^r+\zeta^{-r})$ by symmetry, so an exact rational relation among those real energies implies the same relation among the angles. In the even case the angles at indices $q-r$ are negatives of those at $r$, and the angle at $q/2$ is zero by the combination of inversion and antipodal symmetry. In the odd case let $\lambda_j=2\cos(2\pi j/q)$ for $1\le j\le(q-1)/2$. The complete physical spectrum is $+\lambda_j$ at even index $2j$ and $-\lambda_j$ at odd index $q-2j$. We work with the angles for the $\lambda_j$ and insert their negatives for the odd physical modes. These sign adjustments are essential; the $\lambda_j$ need not be positive. By the character description of $H$, every angle vector obtained from a symmetric array as above belongs to $H$ modulo $2\pi$. We do not require a classification of a finite code modulo 4 or an assertion about integral torsion.

### 3.2 Random reserves and the active set

For each odd prime-power coordinate, choose a random inversion-invariant set $O$ of omitted residues by the following independent choices (independence is across prime-power coordinates and across fiber orbits under inversion):

* In the fiber containing zero, choose uniformly three distinct nonzero opposite pairs $\{u,-u\}$. Omit their six residues, never zero.
* For each pair of distinct fibers exchanged by inversion, choose uniformly six residues in the first fiber and omit their six negatives in the second.

These choices are possible for all $p\ge11$. An independent spectral coordinate is active exactly when every odd coordinate avoids its omitted set. The entire 2-power coordinate, when present, is retained in the active box. The active box has $B$ odd-coordinate tuples and contains the all-zero odd tuple. It is inversion-invariant and (in the even case) invariant under the antipodal shift.

For odd $q$, the independent coordinates are nonzero residue classes modulo simultaneous negation. Since $q$ is odd, every nonzero orbit has size two, so the number of active spectral coordinates is $M=(B-1)/2$.

For even $q$, positive mode indices $1\le r<q/2$ represent orbits of inversion and antipodal shift on the full residue array. All such orbits have size four except the two excluded orbits containing $r=0$ and $r=q/2$. The former corresponds to the non-mode energy $2$, the latter to the fixed zero-energy mode. Both excluded orbits lie in the active box because their odd components are zero. Since $q$ is even, each orbit has a fixed parity of $r$. The count of active positive coordinates in each parity group is $(B-1)/2$ for $k=1$. For $k\ge2$, the odd group has $2^{k-2}B$, the even group $2^{k-2}B-1$. This proves the counts used in Theorem 1.

### 3.3 Interpolation, including any two reserved coordinates

**Lemma 3.** Fix all omitted sets. Any assignment of real angles to the active independent spectral coordinates and to any two distinct reserved independent spectral coordinates extends to a real array obeying all fiber-sum, inversion and (where present) antipodal constraints. Consequently the corresponding projection of $H$ onto these specified coordinates is surjective onto their full torus.

**Proof.** Protect the two additional coordinates and their simultaneous inverses (and antipodal copies, when present). In each prime-power coordinate, choose a smaller spare set $S\subseteq O$ as follows. In the zero fiber choose one omitted opposite pair which avoids the protected values. There are three pairs and at most two protected opposite-pair classes, so this is possible. In every other fiber pair choose one omitted residue in the first fiber avoiding all protected values there and the negatives of protected values in the second. At most two values are excluded by this test for the two independent spectral coordinates (even the looser bound four suffices), out of six choices. Include its opposite in the paired fiber. The resulting $S$ is inversion-invariant, contains no active or protected coordinate value, and meets every fiber in either one or two elements.

On the product box avoiding every $S$, prescribe the selected angles on their full symmetry orbits with the required signs, and set all other entries to zero. There is no conflict: independent spectral coordinates represent different orbits, and excluded fixed points are not prescribed. This assignment already satisfies inversion and the antipodal rule. Extend the box one odd prime-power factor at a time. In each fiber and for each choice of the other coordinates in the current box, fill every missing entry with the negative sum of the existing entries divided by the number of missing entries. This enforces the fiber sum in that factor. The extension preserves every previously enforced fiber sum because it is linear and uses the same spare set independently of the other coordinates. It preserves inversion by symmetric choice of spare sets and equal filling of missing entries, and preserves the antipodal rule by linearity. After all factors have been filled, the full array satisfies all the required constraints and preserves all original prescriptions. Section 3.1 places its angles in $H$. Lifting arbitrary torus coordinates to real angles proves the projection statement. QED.

**Conditional completion consequence.** Let $\pi_A$ be the projection of $H$ onto the active coordinates. Given any active assignment on the torus, draw the remaining coordinates using normalized Haar measure on the corresponding coset of $\ker\pi_A$. The active assignment can be arbitrary by Lemma 3. For any one or two reserved coordinates, their projection from $\ker\pi_A$ is surjective by applying the lemma with active angles zero. Haar pushforward is Haar on the full one- or two-dimensional torus. Thus each reserve is conditionally uniform and each distinct reserve pair conditionally independent uniform, given all active values and the masks. In particular their first and second phase moments vanish; moments involving two distinct coordinates vanish whenever at least one is a reserve, except the constant diagonal second real-coordinate moment described below. This method is the continuous-torus version of completing a parity-check code with prescribed low-order marginals. It avoids division by two modulo 4, which would not be valid in $\mathbb Z/4\mathbb Z$.

### 3.4 Uniform lower bounds on activation probabilities

Write $\alpha_i=\Pr(i\text{ active})$ and $\beta_{ij}=\Pr(i,j\text{ active})$ for distinct independent spectral coordinates. In a prime-power factor, every coordinate value survives with probability at least $(p-7)/(p-1)$, attained by a nonzero value in the zero fiber. The exact pair-survival probability is smallest when the two values are in distinct nonzero opposite-pair classes in the zero fiber, namely

$$\frac{(p-7)(p-9)}{(p-1)(p-3)}.$$

For completeness, equal opposite-pair classes have the single survival rate; zero is always retained. In a nonzero fiber or its inverted mate, two distinct relevant residues survive with probability $(p-6)(p-7)/(p(p-1))$, which is no smaller than the displayed bound. For independent fiber orbits the pair rate is the product of the two single rates, also no smaller. To see the comparisons, $(p-6)/p\ge(p-7)/(p-1)\ge(p-9)/(p-3)$ for $p\ge11$. Independence across prime-power factors now gives $\alpha_i\ge\alpha$ and $\beta_{ij}\ge\beta$.

## 4. Phase law for odd moduli

In the sign-adjusted odd-modulus coordinates of Section 3.1, write $z_i=\exp(i\phi_i)$. The desired auxiliary target is equivalent to

$$\mathbb E\operatorname{Re}(z_i\overline z_j)=-a\quad(i\ne j),\qquad
\mathbb E\operatorname{Re}(z_i z_j)=0\quad(\text{all }i,j).$$

Indeed physical modes of one parity use the $z_i$ and modes of the other parity use their conjugates. For every choice of active set, uniformly match its $M$ coordinates, adding a dummy if $M$ is odd. Given both coordinates active, the probability of their being matched is $1/K$, where $K=K(M)$. For each matched pair independently draw a uniform fourth root and its opposite with probability $D_{ij}=aK/\beta_{ij}$, and otherwise two independent uniform fourth roots. A coordinate matched to the dummy can simply be drawn uniformly. Conditional single-coordinate means and second complex moments are zero. The real conjugate product within a real pair has mean $-D_{ij}$ and the ordinary product has mean zero; across different pairs both products have mean zero. Complete the reserve angles using Section 3.3. Reserve pairs and reserve-active pairs have both complex moments zero by conditional uniformity. Thus the unconditional moments are exactly the target. Since $\beta>K a_0$, there exists $a>a_0$ with $aK<\beta$ (e.g. the midpoint of $a_0$ and $\beta/K$). All mixture probabilities are valid. Section 2 proves the claim for odd $q$.

## 5. Phase law for even moduli

For a positive mode let $C_i=\cos\phi_i$, $S_i=\sin\phi_i$. Let $\mu_0=-a$ in the parity group containing the zero mode (parity of $q/2$), and $\mu_0=0$ in the other group. The needed auxiliary moments are

$$\mathbb E C_i=\mu_0,\quad \mathbb E S_i=0,\quad \mathbb E C_i^2=(1-a)/2,$$

$$\mathbb E C_iC_j=-a,\quad \mathbb E S_iS_j=0\quad (i\ne j\text{ in one parity}),$$

with both distinct-coordinate products zero across opposite parities. The formulas for cosine sums and differences handle reflected spectral modes, the self-reflected pair uses $\cos(2\phi_i)=2C_i^2-1$, and the zero-mode pairs use the first moments. This gives precisely the auxiliary coherence target of Section 2.

Conditional on being active, prescribe moments

$$\mu_i=\mu_0/\alpha_i,\qquad r_i=1/2-a/(2\alpha_i),$$

as the mean and real-root probability, respectively. A reserve is uniform on the circle and has real second moment $1/2$. Thus after averaging over masks the desired first and second moments follow from these definitions.

For each fixed mask, match active coordinates uniformly and independently in the two parity groups, adding a dummy in a group of odd size. Let $K_g=K(M_g)$ for that group's active size $M_g$. Its conditional match rate for a pair is $c=1/K_g$. For an active matched pair $i,j$, set

$$D_{ij}=\frac{a/\beta_{ij}+(1-c)\mu_i\mu_j}{c}.$$

Give its two cosine variables values according to the following joint law:

| ordered values | probability |
|---|---:|
| $(1,-1)$, $(-1,1)$ | $D_{ij}/2$ each |
| $(1,0)$ | $(r_i+\mu_i-D_{ij})/2$ |
| $(-1,0)$ | $(r_i-\mu_i-D_{ij})/2$ |
| $(0,1)$ | $(r_j+\mu_j-D_{ij})/2$ |
| $(0,-1)$ | $(r_j-\mu_j-D_{ij})/2$ |
| $(0,0)$ | $1-r_i-r_j+D_{ij}$ |

Replace each zero cosine by an independent fair choice of $+i,-i$, and nonzero cosines by the corresponding real fourth roots. Use independent pair draws; a dummy match is filled using the one-coordinate marginal. The law sums to one and gives means $\mu_i,\mu_j$, second real moments $r_i,r_j$, real product $-D_{ij}$ and zero sine product. It is nonnegative if $0\le D_{ij}\le\min(r_i-|\mu_i|,r_j-|\mu_j|)$ and $r_i,r_j\le1/2$. Since the means have the same sign within a group, $D_{ij}\ge0$ automatically.

For both active but unmatched coordinates, the real product has conditional mean $\mu_i\mu_j$. Conditional reserve uniformity removes every other contribution, so the unconditional real product is

$$\beta_{ij}[-cD_{ij}+(1-c)\mu_i\mu_j]=-a.$$

All distinct sine products vanish. Opposite-parity active groups are sampled independently conditional on the masks and one has zero conditional means; if either coordinate is reserved the same zero cross-moments follow from conditional Haar. Thus the cross-parity requirements hold.

It remains to ensure the matched-pair probabilities are valid. Since $K_g\le M_*$, $\beta_{ij}\ge\beta$, $\alpha_i\ge\alpha$, we have

$$D_{ij}\le\frac{M_*a}{\beta}+\frac{M_*a^2}{\alpha^2},\qquad r_i-|\mu_i|\ge\frac12-\frac{3a}{2\alpha}.$$

The strict inequality in Theorem 1 holds at $a=a_0$, so it persists for some $a>a_0$ by continuity. It also makes $r_i-|\mu_i|$ positive. Thus every probability above is nonnegative, all marginal moments are correct, and the reserve completion puts the law in $H$. Section 2 concludes the proof.

## 6. Elementary prime-size corollary and examples

Let $f=B/n$. For each $p\ge11$,

$$\frac{p(p-7)(p-9)}{(p-1)(p-3)(p-6)}\ge1-\frac6{p-5},$$

because after multiplying by the positive denominators the difference is $6(p^2-33)>0$. Thus, using $\prod(1-u_j)\ge1-\sum u_j$ for $u_j\in[0,1]$,

$$\frac\beta f\ge 1-\frac{6s}{p_*-5},\qquad\alpha\ge 1-\frac{6s}{p_*-1}.$$

For odd $q=n$, $K\le(B-1)/2$, so $K/(q-1)\le B/(2q)=f/2$, since $B\le q$. If $p_*>12s+5$, then $\beta/f>1/2$ and the odd sufficient condition follows.

For even $q$, $M_*\le qf/4$ in both cases of its definition. If $p_*\ge18s+5$, then $\beta/f\ge2/3$, $\alpha\ge2/3$, and $q\ge46$. Therefore at $a_0$,

$$\frac{M_*a_0}{\beta}+\frac{M_*a_0^2}{\alpha^2}\le\frac{q}{4(q-1)}\left(\frac32+\frac{9}{4(q-1)}\right)\le\frac{713}{1800}<\frac9{20}\le\frac12-\frac{3a_0}{2\alpha}.$$

The middle bound is evaluated at $q=46$, using monotonicity of $q/(q-1)$ and $1/(q-1)$. This proves Corollary 2. The factorization-dependent test is sharper than the simple prime-size bounds.

Selected positive cases certified by the rational test (the cases with 3 or more distinct odd primes are outside the earlier semiprime and prime-power notes):

| q | factorization | path | criterion margin |
|---:|---|---|---:|
| 1334 | 2 × 23 × 29 | P1333 | 632951/28430224 |
| 2294 | 2 × 31 × 37 | P2293 | 6223369/57836339 |
| 47027 | 31 × 37 × 41 | P47026 | 273403/13402410 |
| 214226 | 2 × 43 × 47 × 53 | P214225 | 105596191011/966154750000 |
| 56129 | 37² × 41 | P56128 | 427537/3199296 |
| 224516 | 4 × 37² × 41 | P224515 | 316962688637/2330818996804 |
| 12780049 | 53 × 59 × 61 × 67 | P12780048 | 452912017/5188699488 |

Here the margin is $\beta-Ka_0$ for odd $q$ and the right minus left side of the even sufficient inequality. These are exact arithmetic evaluations of a theorem, not numerical diagonalizations of graphs with millions of vertices. The tensor interpolation test does not cover all these sizes directly and is not necessary for the general proof.

## 7. Reproducibility and proof boundaries

The companion `verify_tensor.py` checks 44 independent rational prescriptions on 11 moduli, including odd/even, prime powers and three distinct odd primes. It fills the tensor boxes, checks all fiber sums and symmetries, then independently verifies the full cyclotomic-polynomial recurrence on the resulting arrays. Small mask probabilities are enumerated exactly. `verify_moments.py` checks 235,915 same-group pair equations in six factorization examples using exact fractions; it also checks the entire symbolic ratio inequality and the rational endpoint inequality. These tests do not replace the general proofs of the lemmas. The phase laws are mathematical existence constructions; no actual integer samples are reported for these new families. The code is not a Lean proof.

The earlier research notes on the prime-power odd part and on odd semiprimes with smaller primes are included in the archive as separate supplementary work. Their six existing checker scripts were rerun; the actual output is in `prior-recheck.log`. Their general arguments still require independent expert audit. They do not enter the proof of Theorem 1. The new result therefore remains meaningful even if a prior draft needs correction. The present proof also handles arbitrary powers of the odd primes and any even power-of-two multiplier under its own sufficient conditions.

A targeted search on 27 November 2026 included Kang's original arXiv version and public queries combining uniform average mixing with cyclotomic tensor, prime factors, random matching, and GitHub. No matching tensor interpolation theorem was identified in the returned sources. The standard algebra, probability and convexity tools are not claimed as new; the candidate contribution is their specific construction of feasible phase moments and the resulting sufficient criterion for path graphs. A complete citation-chain and priority search, independent scrutiny of the interpolation and conditional completion, and manuscript-level editing remain necessary before a public supplement. No claim of a full Lean proof, priority guarantee, or complete classification is made. The small-prime cases and moduli with many relatively small distinct primes remain a significant open part of the conjecture; failure of a displayed inequality is not a negative result.

### References

1. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378, https://arxiv.org/abs/2308.16378.
2. M. Kang, *Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains*, arXiv:2609.14463v1, 13 September 2026, https://arxiv.org/html/2609.14463v1.
3. C. Godsil, *Average mixing of continuous quantum walks*, J. Combin. Theory Ser. A 120 (2013), 1649–1662, https://arxiv.org/abs/1103.2578.
4. R. T. Rockafellar, *Convex Analysis*, Princeton University Press (1970), relative interiors and supporting hyperplanes.
5. Standard theorems: irreducibility of cyclotomic polynomials, Chinese remainder theorem, transcendence of pi, Kronecker's character description of torus subgroups, Haar probability and Carathéodory's theorem.
