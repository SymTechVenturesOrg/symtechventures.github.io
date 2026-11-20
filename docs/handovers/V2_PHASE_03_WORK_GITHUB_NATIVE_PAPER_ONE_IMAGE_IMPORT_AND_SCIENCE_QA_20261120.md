# Work Handover — GitHub-Native Seven-Image Source Import and Paper One Read-Only Science QA

**Date:** 20 November 2026 (Europe/London)
**User-selected Work configuration (not alterable by Work):** **Model GPT-6 Luna (Work)** · **Thinking effort High** · **Execution speed Standard**.
**DTSU v1.1:** genuine Europe/London timestamps; start at 0%; each concise progress report includes percentage, action and a reasoned **numeric remaining ETA**; update ETA honestly; claim 100% only after validation/handback.

## Goal

Remove the brittle manual ZIP hand-off. In ONE bounded pass, **import seven original user-approved image binaries through the authorised cloud computer into a dedicated GitHub documentation branch**, independently verify 7/7 raw GitHub readback hashes, then conduct the already-specified **read-only scientific/editorial audit from the GitHub-pinned files**, committing the audit report as Markdown to the same branch.

**Repo:** `SymTechVenturesOrg/symtechventures.github.io`
**Existing isolated source-import branch:** `docs/symmetria-paper-one-seven-approved-binaries-20261120`
**Target folder:** `docs/artwork/owner-approved/paper-one/`
**Current source manifest:** [manifest.json](../artwork/owner-approved/paper-one/manifest.json)
**Visual standards:** [Locked cinematic artwork standard](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/main/docs/reports/V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md)
**Existing audit requirements:** [Read-only seven-image scientific QA handover](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/docs/symmetria-paper-one-cover-style-gate-20261120/docs/handovers/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_APPROVED_CINEMATIC_FIGURES_INDEPENDENT_QA_20261120.md). Follow its 7-row physics/science/accessibility rubric but **replace its ZIP attachment step with the pinned GitHub PNG files once uploaded**.

## Stage A — Transfer original files to GitHub exactly once, without user manually handling ZIPs

The seven unmodified original PNGs are accessible from this **temporary user-authorised ChatGPT staging page**:

[SYMMETRIA Paper One — Seven Original Approved PNGs](https://chatgpt.com/space/page_7df6e2e9901081918b1f2a29309dd7d4).

It contains **seven separate original image file references** (Cover and Figures 1.1 through 6.1), each with exact source SHA-256 metadata. This Page is used **only as a bootstrap bridge**, not as the permanent archive or final audit source. Use the authorised Work cloud browser/connected file access to retrieve **original binary bytes** via the linked image attachments (not screen captures or low-resolution previews). **Do not instruct the owner to download a ZIP or reattach it.**

1. Inspect `docs/artwork/owner-approved/paper-one/manifest.json` on the above branch and the staging Page's seven original references. Record the currently pinned GitHub branch HEAD and exact source hashes.
2. Via Work cloud computer and the permitted authenticated GitHub checkout, fetch/checkout that isolated branch. Obtain all seven original source binary PNGs. For each, verify exact filename mapping, file size, PNG signature, 1920×1080 actual dimensions, and **SHA-256 of the original retrieved bytes** matching the manifest. Never use screenshots/HTML image previews.
3. Commit **exactly seven unchanged PNG binaries** to the seven manifest target paths on that branch. Avoid LFS unless explicitly required; files are approximately 3 MB each. No HTML/images in deployed website folders.
4. **Independent GitHub readback:** fetch or clone the resultant GitHub commit separately and recompute all seven SHA-256 hashes from bytes **retrieved from GitHub**, not local source copies; confirm 7/7, Git object IDs and exact pixel dimensions. Record commit SHA and commands.
5. **Only on all 7/7 PASS:** update `manifest.json` to `DIRECT_GITHUB_SHA256_VERIFIED`, set each `github_binary_present` and `github_readback_verified` true, and add an accurate `github_verified_commit` property. Update README status accordingly. Document binary verification evidence in `docs/reports/` and commit on same branch. Re-read files from GitHub to confirm status metadata is truthful.
6. **If Work cannot access original bytes in the staging Page, or cannot upload binary PNGs to GitHub, STOP this stage** with explicit `BLOCKED_SOURCE_TRANSPORT`; retain the manifest's PENDING state and report precisely what provider/tool failed. **Do not ask the owner to shuttle the ZIP or claim GitHub upload.** If a connected app can provide an authorised original binary route without owner action, propose it; do not use a different file/generator.

## Stage B — Independent scientific/editorial audit, GitHub-only

Run **only after Stage A verified**. Work must re-check the source code rather than inherit earlier judgments:

- Pin latest repository HEAD/HTML blob on website implementation `feature/v2-space-research-website` and load `articles/symmetria/symmetria-paper-01.html`.
- Use the seven original 1920×1080 PNGs from **the GitHub verified commit**; compare to seven exact paper captions and scientific requirements in the prior seven-image audit handover.
- Every image: inspect word-by-word texts, mathematical symbols, causal arrows, established-vs-hypothetical science, imagery-to-section accuracy, cinematic consistency, and desktop/390px/320px readability. Clarify that browser/mobile testing was not done if only resized previews are used.
- Especially check Newtonian-vs-Einsteinian gravity in 1.1, Standard Model includes only three non-gravitational interactions, Einstein field equations' missing cosmological constant, conjectural SYMMETRIA labels 5.1 and **unvalidated research roadmap** 6.1. Distinguish **visual owner approvals (7/7)** from **pending independent science**.
- Classify each slot: `READY FOR NEXT GATE` / `SCIENCE FIX` / `CAPTION FIX` / `VISUAL FIX` / `BLOCKED`; severity and narrow actionable corrections.
- Commit `docs/reports/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md` on the same isolated docs branch. Include exact first verified image commit, current HTML SHA, per-file hashes, 7-row content decision table, technical/browser limitations, and concise `COPY TO CHAT` handback.

## Scope and authority

Image assets are to remain **unmodified original bytes**, used for review and archival until scientific clearance and a fresh explicit website implementation authorisation. No current site modifications, no PR #5, no production asset changes, no merge, no deployment; do not broaden into other papers. The earlier ZIP-dependent Work handover is **superseded for transport**.

## Closing COPY TO CHAT

Report precise transfer status (7/7 hash evidence or BLOCKED), source and GitHub commit SHAs, whether `manifest.json` was updated, audit result counts and link to GitHub report, exact remaining decisions and a recommended next pass. **No 100% claim unless both verification and the independent audit have been completed.**
