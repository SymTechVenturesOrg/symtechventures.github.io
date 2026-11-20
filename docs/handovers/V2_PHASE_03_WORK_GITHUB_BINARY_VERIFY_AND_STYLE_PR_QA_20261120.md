# SymTech Ventures — Work Pass: Verify Canonical Cinematic PNGs and Make Documentation PRs Review-Ready

**Date:** 20 November 2026 (Europe/London)  
**Specialist:** ChatGPT Work — **Luna Medium · Standard Speed** (select Medium effort when available)  
**Reporting:** DTSU v1.1 with genuine Europe/London timestamps, honest percentage, grounded ETA; complete report and **COPY TO CHAT**.  
**Scope:** One finite technical verification and strictly scoped **documentation-only** tidy-up, **no PR merges**.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Style standards:** draft [PR #6](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/6), branch `docs/lock-symmetria-cinematic-artwork-20261120`  
**Original reference PNGs:** draft [PR #7](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/7), branch `docs/symmetria-style-reference-assets-20261120`  
**Website implementation:** existing draft [PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5); **do not touch**.

## Why this pass is needed

Three original, visually approved Paper One/Two PNGs are already committed in PR #7, and independently computed Git blob SHA-1 identities match the source ZIP. GitHub's text-oriented connector **cannot retrieve their binary bytes**, leaving direct *GitHub-readback* SHA-256 unverified. The README and manifest accurately reflect that remaining gap. The next task must use an **actual authenticated binary-capable checkout or raw-file download**, **not** repeat the blocked text fetch route, and then check the document PRs for broken links/stale descriptions.

The new locked style is **fully AI-generated cinematic science art**, *not* a flat programmatically constructed slide/diagram. The reference PNGs are **STYLE ONLY** and have original dimensions 1672 × 941; all subsequent individual figures must be truly standalone, exactly **1920 × 1080**, with genuine scientific explanations, no scientist portraits and no embedded paper/figure identifiers. Work is **not** being asked to generate or approve replacement figures here.

## Sources — read fresh, pin heads and compare PR scope

Before any writing, read and pin the exact HEAD SHA of both PR branches; do not rely on an earlier recorded SHA. Check that both PRs remain **draft/open** and that the changes are limited to documentation/style assets. Read:

- PR #7 `docs/artwork/style-reference/manifest.json`
- PR #7 `docs/artwork/style-reference/README.md`
- PR #7 `docs/reports/V2_PHASE_03_CANONICAL_STYLE_ANCHOR_OBJECT_IDENTITY_20261120.md`
- PR #6 `docs/reports/V2_PHASE_03_SYMMETRIA_FIGURE_PRODUCTION_STANDARD_20261120.md`
- PR #6 `docs/reports/V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md`

For convenience, the three full repository paths and expected hashes are:

| GitHub PNG path (on PR #7 branch) | Expected original bytes | Expected SHA-256 | Git blob SHA-1 already corroborated |
|---|---:|---|---|
| `docs/artwork/style-reference/P1_Nilpotent_Operator_STYLE_ONLY.png` | 2109047 | `1cb364be9159452134594f3f7e86de5424d82c8738b209d7ebb8622b90e7d9f2` | `51831f2a286b7f7dc96524aeb15ca1855c804d52` |
| `docs/artwork/style-reference/P2_Noether_Conservation_STYLE_ONLY.png` | 2276356 | `1f7515074252b54bf4cbb6ef70683610e528c1f322097090751e1304a5f35593` | `19fca380f96c8e9ef4bd4a37d396b22658019631` |
| `docs/artwork/style-reference/P2_Broken_Symmetry_STYLE_ONLY.png` | 2232529 | `484191f41f002cc286938299da77de91b0dac14e8e9ef808ef356cb5b93e5817` | `9064d2a8dcdea6c5256dac690021adcf8e89b0a7` |

## Step A — read bytes **from GitHub**, not just the original attachment

1. In the Work cloud computer or supported terminal, use a binary-capable **authenticated Git clone/fetch** of the PR #7 branch. A verified raw GitHub binary download is also acceptable. If Git is available, pin a commit and use `git show <PINNED_COMMIT>:docs/artwork/style-reference/<filename>.png > <local_output>.png` for each. Do **not** use a text-decoding GitHub connector which returns empty or UTF-8 errors for PNG. If the repository requires authentication, use approved connected GitHub credentials/workflows; do not ask for personal tokens in chat.
2. Verify fetched bytes: actual byte length, PNG signature, 1672 × 941 native dimensions, `sha256sum` (or platform equivalent), and `git hash-object` / `git rev-parse <PIN>:<path>` where available. **The SHA-256 must be computed from bytes independently retrieved from GitHub**, not from the user ZIP.
3. Record exact commands, pinned commit, raw-vs-source provenance and results in a 3-row matrix. Hash/magic/size mismatch is a BLOCKER; do not overwrite original PNGs. Avoid accidental HTML login/error pages masquerading as image downloads.
4. If the current Work environment cannot obtain independent GitHub bytes, report **BLOCKED: DIRECT GITHUB SHA-256 PENDING** and preserve the existing honest registry status. The 3/3 Git-object SHA-1 corroboration is valuable but must not be mislabelled as a completed direct download SHA-256.

## Step B — restricted documentation updates, only if appropriate

**If and only if all three direct-download SHA-256 checks PASS:**

- On PR #7 branch only, update `manifest.json` and `README.md` from "readback pending" to **DIRECT_GITHUB_SHA256_VERIFIED**, recording the exact pinned commit and test evidence. Keep original-byte dimensions, style-only/non-scientific caveat and SHA values.
- Update the existing historical upload handover note or append an erratum if it would otherwise still tell future readers an upload is pending. Do not rewrite historical facts to claim the original Work attempt succeeded when it was blocked.
- Commit a concise binary verification report to PR #7 under `docs/reports/`. Keep those changes strictly textual.

**Regardless of Step A success:** read PR #6's two standards files and perform a **documentation-only readiness check**: both still teach exact 1920×1080, no embedded figure numbers, no portraits, one native AI-generated cinematic full-canvas image per section, science vs owner-style gates, and supersession of the rejected 28-image package. Flag stale text claiming the reference images have never been committed, broken relative references to planning-only reports, escaped Markdown/backticks and any contradictory instructions. Fix obvious documentation defects **on PR #6 branch only**, with a minimal scoped commit and evidence. Do not add new content about scientific validation, and do not change PR's draft state.

Re-fetch all files actually changed and compare **PR #6 and PR #7 against main** to verify neither contains website images, HTML, JS/CSS, production code or deployment changes. **Do not merge either PR**, regardless of verification success.

## Deliverable and stop

Produce `V2_PHASE_03_WORK_CANONICAL_ANCHOR_BINARY_VERIFY_AND_PR_READINESS_20261120.md` in the Work conversation (and a scoped PR #7 documentation report only if Step A passes), including:

1. Both current PR branch heads and PR draft/open states.
2. Three-by-three byte count/SHA-256/Git-object-id verification results, with exact provenance and commands; clear **PASS** or **BLOCKED**.
3. Exact documentation edits and resulting commit SHAs, if any, or reasons not changed.
4. All remaining PR #6/#7 documentation/link concerns and whether they are **ready for owner merge review** (NOT automatic merge approval).
5. Next proposed step: owner reviews PR #6/#7, then we restart with **one** Paper One cinematic cover as a **style checkpoint** using original reference images and independent science/style gates. Do not generate that cover in this Work pass.

Finish with the owner's **COPY TO CHAT** block: pinned branch SHAs, 3-image verification status, any blockers, PR #6/#7 state, report link, and owner decision required. **Absolute stop:** no new figure generation, website PR #5 edits, production image replacements, PR merges, release or deployment.
