# Uniform average mixing on P19 at integer readout times

## Status
Candidate new theorem with two independently motivated proofs (the previous phase-law argument and the direct certificate below). The direct certificate has been executed using exact integer/rational arithmetic. No Lean compilation or independent human review is claimed. Priority is not established. All times refer to the adjacency-matrix Hamiltonian A (unit coupling and ħ=1).

## Theorem
Let A be the adjacency matrix of the 19-vertex path and J the 19×19 all-ones matrix. There are 91 distinct integers t_j in [0,1999] and positive real weights w_j summing to 1 such that

    Σ_j w_j |exp(i t_j A)|^{∘2} = J/19.

The explicit times are in certificate.json and protocol.csv. Exact weights are defined by the linear system below, not by the rounded CSV weights. They are all greater than 0.0006.

## 1. Spectral reduction
For r=1,...,19, θ_r=2 cos(rπ/20) and u_r(k)=sin(krπ/20)/sqrt(10) for k=1,...,19. The sine recurrence and boundary conditions at k=0,20 give A u_r=θ_r u_r. The eigenvalues are distinct by strict monotonicity of cosine on (0,π). Symmetry of A gives orthogonality; the finite geometric sum Σ_{k=1}^{19} cos(2krπ/20)=-1 gives Σ sin²(krπ/20)=10. Thus E_r=u_r u_r^T are the orthogonal spectral projectors, and

    |exp(itA)_{kl}|² = Σ_r E_r(k,l)² + 2Σ_{r<s} E_r(k,l) E_s(k,l) cos((θ_r-θ_s)t).

It suffices to attain y_rs=-1/19 for same-parity r≠s and y_rs=0 otherwise. To verify this directly (without assuming the sufficiency identity from the literature), put ζ=exp(iπ/20), T_m=ζ^m+ζ^{-m}, F_r=40 E_r(k,l)=T_{r(k-l)}-T_{r(k+l)}. Since ζ^20=-1 and ζ^4≠-1, ζ is a root of P(X)=X^16-X^12+X^8-X^4+1 by (X^4+1)P(X)=X^20+1. The verifier reduces integer polynomials modulo P, using exponents mod 40. For each of the 361 pairs k,l it checks

    20Σ_r F_r² - (Σ_{r odd} F_r)² - (Σ_{r even} F_r)² = 1600

in Z[X]/(P). Evaluating at ζ proves the target mixing formula (divide by 19·1600). No irreducibility theorem is required for this implication.

## 2. Explicit real-time certificate
The same polynomial reduction groups the 171 ordered-index gaps r<s into 90 classes. Equality of residue vectors implies equality of actual gaps, and every class has a consistent target. Choose representatives in the order of first occurrence when enumerating (r,s) lexicographically. No assumption that different residue vectors give different real numbers is needed for the certificate: invertibility verified below also rules out coincident representative rows.

Let B be the real 91×91 matrix with first row all ones and each subsequent row cos((θ_r-θ_s)t_j) for the corresponding representative. Let b=(1,y_1,...,y_90)^T. The goal is Bw=b and w>0. The data file supplies 91 distinct times, a rational approximate inverse R, and a rational approximate weight vector w0. Both rational arrays have denominator 10^12. The generator is exploratory; its floating point results are not trusted by the proof.

## 3. Exact enclosure of B
The verifier uses closed intervals [a/S,b/S], S=10^30, represented by integer endpoints. Addition, negation, multiplication, and positive integer division round outward by floor/ceiling. This preserves containment by the elementary monotonicity and extremal-product rules.

Machin's formula π=16 arctan(1/5)-4 arctan(1/239) and the alternating arctangent series give rational upper and lower bounds using 40 terms and the first omitted term. Machin's formula follows from the tangent addition formula with the angles in their correct principal ranges. To enclose a cosine, subtract an arbitrary integer multiple of 2π using interval arithmetic, verifying that the resulting interval lies in [-4,4]. Sum the degree-60 Taylor polynomial using interval recurrence. The Taylor theorem at degree 61 (the coefficient of x^61 is zero) bounds the remainder by 4^62/62!, strictly less than 1/S (checked by integer arithmetic). Thus the returned interval encloses the true cosine. This constructs certified enclosures of θ_r and every entry of B, with no floating point operations.

## 4. Invertibility and positivity
The verifier checks via outward-rounded arithmetic

    ||I - RB||∞ ≤ 87689342669405671129/500000000000000000000000000000 < 2·10^-10,
    ||R(b-Bw0)||∞ ≤ 49781163298208067/100000000000000000000000000000,
    min_j(w0_j) = 60053007/100000000000.

Here the matrix infinity norm is the maximum absolute row sum. Let δ denote the first rational bound and c the second. If Bv=0, then v=(I-RB)v and ||v||∞≤δ||v||∞, whence v=0. Since B is square it is invertible. Set w=B^-1 b. Then w-w0=(I-RB)(w-w0)+R(b-Bw0), so

    ||w-w0||∞ ≤ c/(1-δ) < 5·10^-13.

In particular w_j>0.0006 for every j. The first row of Bw=b gives Σ w_j=1 exactly. All 171 target cosines follow by gap grouping. Section 1 proves the mixing equation. This direct proof does not require a torus density theorem, probability measure integration, or a convex hull interior theorem.

## 5. Reproduction and limitations
Run `python3 verify_certificate.py` (Python 3 standard library only; do not use `-O`, which disables assertions). The generator is optional and needs numpy/scipy. The fixed certificate is authoritative; regenerating may select different times on different solver versions. verification.txt is an actual log of the checker. The proof relies on the analytic arguments stated above, which have not yet been machine formalized. The rounded weights in protocol.csv need not satisfy the exact equations. No claim is made about minimal support or shortest maximum time. For novelty context see Musung Kang, arXiv:2609.14463 (2026); a targeted search on 2026-11-27 did not find a P19 solution, but the public search was not exhaustive.
