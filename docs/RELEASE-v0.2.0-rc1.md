# v0.2.0-rc1 — archive release candidate

This is an archival expansion of the public v0.1.0 preprint, not a revised proof of the complete classification. The English/Chinese manuscript PDFs, LaTeX sources, detailed proof and core verification scripts retain their original bytes. Do not re-label those papers v0.2.0 without revising their actual contents and publication metadata. The repository/archive version is v0.2.0-rc1; the manuscript version is v0.1.0.

## Maintainer checklist

1. Extract the full ZIP and run `python verification/check_hashes.py` before editing. Read the contribution ledger and supplements. The original v0.1.0 integrity list is saved as `records/SHA256SUMS-v0.1.0` (for the original tagged snapshot only).
2. Read all historical materials before redistributing; confirm permission and attribution, especially old Lean and P8 material. This candidate does not grant an effective license. The prior MIT/CC BY proposal remains pending. P8 repository archive remains an external link; do not claim it is bundled.
3. Run `python verification/run_checks.py` and optionally `python verification/run_supplement_checks.py`. The latter does not compile Lean. Review logs and resolve any errors rather than relying on a badge.
4. Keep existing v0.1.0 tag and release immutable. For an archival update use `v0.2.0-rc1` pre-release after the checks and license decision. An appropriate title is **Research Archive and Verification Supplements — v0.2.0-rc1**. The full candidate ZIP can be attached as a Release asset.
5. Prefer Git / GitHub Desktop to uploading several hundred individual files through the browser. Copy the unpacked contents into a clean checkout of the existing repository, preserving `.github/` and `.gitignore`; inspect `git status` and the diff before commit. Do not replace newer remote changes blindly. The main CI still runs the same 11 core checks, and the supplementary runner is optional. The original tag is unaffected by commits on main.

Suggested commit: `Archive research methods and verification records`.

Suggested release notes: This release candidate preserves the v0.1.0 classification manuscript and adds historical proofs, finite certificates, effective time bounds, robustness notes, post-release arithmetic checks and uncompiled Lean stage-1 source. Earlier methods remain candidate proofs, not new peer-reviewed results. No new claim of priority or full kernel verification is made. See `docs/CONTRIBUTIONS.md`, `research-history/README.md` and `supplements/README.md`.
