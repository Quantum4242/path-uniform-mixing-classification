# B. Spanning-tree completion of overlapping constraints

For q=pr with distinct odd primes p<r, the historical theorem gives sufficient conditions p≥13, or p=11 and r≥37. The construction represents the signed cyclotomic constraints as a bipartite multigraph with an auxiliary root. Three edge-disjoint reserve spanning trees leave a surjective completion after fixing any two reserve coordinates; random matching on active coordinates then supplies the prescribed negative correlations. With P=(p−1)/2, R=(r−1)/2, m=(pr−1)/2 and M=m−3(P+R), the sufficient inequality in the original note is β_ij > M/(2m−1) for every distinct pair, where β_ij is its joint activation probability. The exact probability formulas and all-range polynomial certificates are in the source.

The note also reports 14 finite exact phase certificates for q=33,35,39,55,65,70,77,85,91,95,110,130,140,154. The independent pair verifier uses exact cyclotomic arithmetic and rational weights. These are phase-space certificates, not actual time schedules. Negative controls 12,15,21,30 reproduce prior obstructions; not new negative results.

- [Original proof](../research-history/09-overlap-trees/research-note.md)
- [Tree verification](../research-history/09-overlap-trees/verify_tree.py), [log](../research-history/09-overlap-trees/tree-verification.log)
- [Full pair verifier](../research-history/09-overlap-trees/verify_full.py), [log](../research-history/09-overlap-trees/verification.log)

The proof remains a candidate alternative to the Fourier construction. Its graph-theoretic ingredients are standard; the application and combined construction are the potential contribution.
