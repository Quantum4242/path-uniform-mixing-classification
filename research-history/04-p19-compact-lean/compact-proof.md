# Compact integer certificate and analytic spectral reduction

Status: all integer and interval checks have been run in Python. The Lean source is a draft for finite arithmetic checks; it has not been compiled in the authoring environment. The full physical theorem is not Lean-verified.

## Compact certificate

Let Q=10^8, n=91, A=A0/Q, R=R0/Q, w0=u0/Q, b=b0/19, using the fixed data in compact.json. Let B be the real cosine matrix defined in source/proof.md. The checker establishes entrywise |B-A|≤1/Q. It also verifies the following exact integer inequalities (absolute row sums):

* max_i sum_k |R0[i,k]| ≤ 27 Q.
* max_i sum_j |Q² δij − sum_k R0[i,k] A0[k,j]| ≤ Q²/10000.
* max_i |b0[i] Q² −19 sum_k A0[i,k] u0[k]| ≤ 19 Q²/10^6.
* sum_i |u0[i]| ≤ 2Q; each u0[i]≥60000.

Consequently ||I−RB||∞ ≤ 1/10000 + 27·91/Q < 1/1000 and ||R(b−Bw0)||∞ ≤27(10^−6+2/Q)<1/30000. For any v with Bv=0, v=(I−RB)v, hence ||v||∞≤||v||∞/1000 and v=0. B is square, so w=B^−1b exists. From w−w0=(I−RB)(w−w0)+R(b−Bw0), we obtain ||w−w0||∞<(1/30000)/(1−1/1000)<1/20000. Each exact weight is strictly larger than 60000/Q−1/20000=11/20000. The first row gives sum w=1 exactly. This bound is intentionally weaker than the original v2 bound. No rounded weight vector is claimed to be exact.

## Analytic replacement for the 361 polynomial identities

For any integer q≥3 let k,l=1,...,q−1. Set E_r(k,l)=(2/q)sin(krπ/q)sin(lrπ/q) for r=1,...,q−1. These are orthogonal rank-one spectral projectors for the path P_(q−1) (see the sine recurrence and normalization in source/proof.md). Define D=δ_(k,l), F=δ_(k+l,q).

The geometric-series identity C(m)=sum_(r=1)^(q−1) cos(2πmr/q)=q·1_(q divides m)−1 gives, using the product-to-sum formula,

sum_r sin²(krπ/q)sin²(lrπ/q) = (C(0)−C(k)−C(l)+(C(k−l)+C(k+l))/2)/4 = q/4+q(D+F)/8.

Thus sum_r E_r(k,l)^2=1/q+(D+F)/(2q). Reflection of the path maps sine eigenvector r to (−1)^(r+1) times itself. With H the reflection permutation matrix, odd/even spectral projector sums are (I+H)/2 and (I−H)/2 respectively. Squaring their (k,l) entries and adding gives (D+F)/2, including the central vertex case D=F=1.

Therefore, if real averaged pair cosines equal −1/(q−1) for distinct equal-parity r,s and 0 for different parity, the averaged mixing entry is

[q sum_r E_r(k,l)^2 − (sum_odd E_r(k,l))^2 − (sum_even E_r(k,l))^2]/(q−1) = 1/(q−1).

For q=20 the compact certificate attains precisely these pair cosines, proving the mathematical reduction. The integer gap checks ensure equal polynomial residues give equal actual energy gaps once evaluated at ζ=exp(iπ/20); ζ^20=−1 and ζ^4≠−1 imply ζ^16−ζ^12+ζ^8−ζ^4+1=0. No irreducibility proof or distinctness assumption is necessary for grouping; invertibility itself proves distinctness of the actual representative rows.

## Formalization boundary

P19.allChecks is a closed proposition containing the 91 row Boolean equalities and the global dimensions/weight check. P19.allGapChecks is a closed proposition containing the 90 representative checks and all 171 pair coverage checks using the simplified power coefficient formula. Their proof source uses `decide`, not native execution. The source is not compiled yet. Even after both pass, the following remain: prove that the Boolean checks imply the real matrix inequalities; prove the interval cosine enclosure and polynomial evaluation soundness; prove the finite real matrix argument and the spectral/exponential identity. The original P19 existence theorem is not identical to either finite proposition.
