# SYMMETRIA Paper Two — Work Handover: Seven Owner-Approved Cinematic Images into Responsive Website WebP (Separate Draft PR)

**Date:** 21 November 2026 (Europe/London).  
**Owner instruction:** “I approve the corrected Paper Two Figures 2.1, 3.1 and 6.1 as the final artwork. Record my approval in GitHub and prepare the next responsive WebP website-integration stage as a separate draft PR. Do not merge or deploy anything.”
**Current stage:** **PREPARATION COMPLETE; IMPLEMENTATION NOT STARTED.** This handover is for the later Work **execution** of the prepared stage. Do not claim images compressed or website-integrated until actual binaries/HTML/browser tests exist.
**Model settings for Work (user selects in UI):** GPT-6 Luna · High thinking effort · Standard speed.
**DTSU v1.1:** Timestamp every update in real Europe/London time, report an honest percentage, realistic numerical remaining ETA when demanded by DTSU, specific current work and blockers; end with a full GitHub QA report and COPY TO CHAT handback. No fabricated success, hidden merge or background execution.
**Repo:** `SymTechVenturesOrg/symtechventures.github.io`.
**CRITICAL new implementation branch:** `feature/v2-paper-two-seven-cinematic-webp-20261121`.
**Existing new integration draft PR:** **[#13](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/13)**.
**PR #13 base branch:** `feature/v2-space-research-website` — source of draft website PR #5, head pinned when created at `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`. **NEVER change PR #5's branch directly.**
**Art source branch:** `docs/symmetria-paper-two-cinematic-artwork-20261121` — original art PR #12 (base main, separate and still draft). Approved identity record at [seven-figure owner approval](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/docs/symmetria-paper-two-cinematic-artwork-20261121/docs/reports/V2_PHASE_03_P2_ALL_SEVEN_FINAL_OWNER_APPROVAL_AND_RELEASE_GATE_20261121.md).
**Reference integration:** Paper One [draft PR #11](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/11), source branch `feature/v2-paper-one-seven-cinematic-optimised-20261120`, **read-only style/HTML/WebP/browser QA reference**, not parent/base to Paper Two.

## A. Canonical evidence and exact source branches

Read all **live committed** sources before touching Paper Two HTML:

1. [Pre-prepared machine-readable 7-image mapping and accessibility/caption copy](../reports/V2_PHASE_03_P2_SEVEN_RESPONSIVE_IMAGE_INTEGRATION_PREPARATION_MANIFEST_20261121.json), on **this PR #13 branch**. This includes baseline figure-caption excerpts directly extracted from the source article, selected filenames, SHA-256, Git blob, alt, external figcaption and long-description copy, image-width plans and explicit zero-work counters. It is the central execution contract. **Never use a superseded candidate.**
2. Paper Two article `articles/symmetria/symmetria-paper-02.html` on the `feature/v2-space-research-website` base; expected pre-work Git blob `060700e8cdac337583c820f044efe80154d59b6c`. Seven ordinary `<img class="article-image">` immediately followed by `<p class="figure-caption">`, in slots **cover, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1**. Preserve their position and adjacent manuscript content.
3. CSS `css/v2-articles.css` on base branch, pre-work blob `72697a65096fcdbc8c762e86215a8ceb14d1be92`. Base already has `.paper-figure-open` link rules but **does not yet contain Paper One's `.paper-figure--cinematic` figure-description styling**. Read PR #11's CSS `e5541abaed39e7a60706d596d645dd999d372a9c`, and port **only minimal reusable additive styling to THIS PR #13 branch**. Do not edit PR #11 or PR #5 directly. Avoid double margins or broken article widths.
4. Paper One approved responsive HTML `articles/symmetria/symmetria-paper-01.html` at PR #11 head before the most recent docs-only update, Git blob `c28221d44d10d9fcd368f3c1f3b945ecffb02306`. Use its seven semantic linked `<figure data-figure-slot="...">` patterns, `picture/source/srcset/sizes/img`, `figcaption`, `aria-describedby` long description and keyboard-focus/full-image link behaviour.
5. [Paper One derivative manifest](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-paper-one-seven-cinematic-optimised-20261120/docs/reports/V2_PHASE_03_P1_SEVEN_IMAGE_WEBP_DERIVATIVE_MANIFEST_20261120.json) and [successful seven-case GitHub Actions browser acceptance addendum](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-paper-one-seven-cinematic-optimised-20261120/docs/reports/V2_PHASE_03_P1_GITHUB_ACTIONS_BROWSER_ACCEPTANCE_ADDENDUM_20261120.md). Clone the verified methodology, **not** numerical compression conclusions: actual Paper Two savings will differ.
6. [Independent Paper Two corrected science re-audit](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/docs/symmetria-paper-two-cinematic-artwork-20261121/docs/reports/V2_PHASE_03_P2_THREE_SCIENCE_FIXES_INDEPENDENT_GITHUB_QA_20261121.md) and initial six-image audit (same art branch) for the exact scientific constraints.

**Do not change the site's existing article content, title, author metadata, other papers, or navigation for unrelated reasons.**

## B. Exact 7 selected 1920×1080 master binaries — NOTHING ELSE is owner approved

| Slot | Source art PR #12 original/corrected file | Exact SHA-256 | Proposed website 1920×1080 master PNG |
|---|---|---|---|
| Cover | `docs/artwork/paper-two/candidates/P2_Cover_Cinematic_1920x1080_Candidate.png` | `d1c2d02620c7b595c88dcfadf8e91ac4628f48d6b7770a1a55fa19cdc52b8a02` | `images/symmetria/paper-02/approved-20261121/p2_cover_master_1920x1080.png` |
| 1.1 | `docs/artwork/paper-two/candidates/P2_Figure_1_1_ChatCandidate_1920x1080.png` | `a53157058eda3e5d594e53284be40f8bb2c58fdb03c399b7401e7fefc525957c` | `images/symmetria/paper-02/approved-20261121/p2_figure_1_1_master_1920x1080.png` |
| 2.1 | `docs/artwork/paper-two/candidates/science-corrections-20261121/P2_Figure_2_1_ScienceFix_Candidate_1920x1080.png` | `ccea83f05ded4bd9479ff624a65e4bbf8261afd2cbbd5e632ebcf0bcdfc3f421` | `images/symmetria/paper-02/approved-20261121/p2_figure_2_1_master_1920x1080.png` |
| 3.1 | `docs/artwork/paper-two/candidates/science-corrections-20261121/P2_Figure_3_1_ScienceFix_Candidate_1920x1080.png` | `962c5465b7ed8d599e24688a173b4ec59f12bf9f7c3ce3288c8af5ccb224f07d` | `images/symmetria/paper-02/approved-20261121/p2_figure_3_1_master_1920x1080.png` |
| 4.1 | `docs/artwork/paper-two/candidates/P2_Figure_4_1_ChatCandidate_1920x1080.png` | `bce9e58d6a5dbb058774051a88f1d76f44e926420f56ca9939440eef7512365c` | `images/symmetria/paper-02/approved-20261121/p2_figure_4_1_master_1920x1080.png` |
| 5.1 | `docs/artwork/paper-two/candidates/P2_Figure_5_1_ChatCandidate_1920x1080.png` | `201f88207b9bd0122a105c59c94b8a17f6d50740c310594718d5b3ababf685cf` | `images/symmetria/paper-02/approved-20261121/p2_figure_5_1_master_1920x1080.png` |
| 6.1 | `docs/artwork/paper-two/candidates/science-corrections-20261121/P2_Figure_6_1_ScienceFix_Candidate_1920x1080.png` | `e0590636813f7a720ca88b225011a5c2b4122a2ccce79263c9f3563f47c0bcff` | `images/symmetria/paper-02/approved-20261121/p2_figure_6_1_master_1920x1080.png` |

**Total: 7 RGB PNG files, exactly 22,023,720 bytes (22.02 MB decimal)**. All have passed independent GitHub binary decode and checksum verification on the artwork branch. Figures **2.1, 3.1 and 6.1** MUST be the `science-corrections-20261121` versions, **not** the earlier unapproved `P2_Figure_*_ChatCandidate` originals.

**Byte-proof import procedure (Work with native binary Git capability):**

- Fetch this PR #13 branch as a fresh working checkout. Then fetch source art branch into a distinct Git ref: `git fetch origin docs/symmetria-paper-two-cinematic-artwork-20261121`.
- For every exact `source_github_path` in the prep manifest, obtain **the actual Git blob bytes** using a binary-safe checkout or `git show origin/docs/symmetria-paper-two-cinematic-artwork-20261121:<source_github_path> > <site_master_png>`. Avoid a connector's text-only response on binary images, and never transcode or resize a master PNG.
- Recalculate `sha256sum`, byte size, Git blob and decode of all seven master paths; compare source hashes and total. **Fail closed** if any mismatch or absent asset. The art source PR #12 need not be merged to copy its immutable approved content.
- Retain approved masters *unchanged* at planned new paths `images/symmetria/paper-02/approved-20261121/`, not the legacy `images/symmetria/paper-02/02_*.webp` files. Preserve legacy assets as unmodified audit/rollback sources.

## C. High-quality WebP derivative generation — only after master checks pass

- 7 masters × widths **768, 1280, 1920** = **21 new WebP binaries**; output dimensions 768×432, 1280×720, 1920×1080 respectively. RGB, nonanimated, high quality **93**, Pillow WebP **method 6**, Lanczos resampling from 1920 PNG masters. Check actual encoder/library versions and record them in a *new* measured derivative manifest.
- Use exact target `planned_webp_variants[].path` from the prep manifest (e.g. `p2_figure_3_1_768w_q93.webp`). **Do not overwrite old Paper Two WebP images** or change approved PNG source hashes.
- Confirm each variant decodes, width/height 16:9, image legibility/typographic artefacts, SHA-256, original-master SHA-256 and actual bytes. Record per-image and aggregated savings for **mobile, tablet and desktop** using the actual selected variant. No guessed transfer/performance numbers.
- **Target responsive HTML sizes** as used by Paper One: `(max-width: 700px) calc(100vw - 2rem), (max-width: 1100px) calc(100vw - 4rem), 860px`. Offer WebP with `<picture><source type="image/webp" srcset="768w, 1280w, 1920w" sizes="...">` and proper image fallback `src/srcset/sizes`. Allow browser-selected variants based on DPR; do not hard-code DPR1 vs DPR2.
- Cover: `loading="eager"`, `fetchpriority="high"`, `decoding="async"`. All six section figures: `loading="lazy"`, `decoding="async"`. Provide `width="1920" height="1080"` to avoid cumulative layout shift.

## D. HTML mapping/accessibility and scientific text guards

Convert **only the seven original image+caption pairs in Paper Two** to `<figure class="paper-figure paper-figure--cinematic" data-figure-slot="...">` with:
- link `<a href="<approved-master-png>" target="_blank" rel="noopener" aria-label="Open full-resolution Figure X (1920 by 1080 PNG; opens in a new tab)">`, opening a native browser zoomable full-resolution PNG (no script/lightbox dependency);
- `<picture>` with WebP variants; concise descriptive `<img alt>` and `aria-describedby` referencing a visible standalone `<p class="figure-description" id="...">`;
- selectable `<figcaption class="figure-caption">` using the paired *original manuscript caption* as the provenance baseline and updated scientifically qualified caption copy from the exact prep manifest, retaining the topic, figure numbering and surrounding manuscript order;
- accessible full-resolution open text link and keyboard focus styles, using Paper One's CSS additions as read-only guidance;
- no image text alone must carry a scientific caveat; full-resolution link and selectable descriptions critical for **2.1 and 3.1** at 320px/390px, plus correct **6.1** untested-hypothesis disclaimer.
- Preserve the paper's original seven image positions and existing seven slot names; avoid duplicate figure content or any new decorative masthead text in artwork. No changes to original approved PNGs.

**Seven scientific caption checks:** Cover: symmetry as an organising description, not a validated grand unification; 1.1: approximate living forms vs ideal mathematical invariance; 2.1: no exact golden-ratio measurement, diverse natural causes; 3.1: `D₆` sixfold rotation/reflection vs finite object relocation, no false translational invariance; 4.1: continuous symmetry of the relevant action and no external torque assumption for angular momentum; 5.1: `V(φ)` shown as 1-D double-well rather than full Mexican-hat potential/Higgs mass claim; 6.1: explicitly **untested exploratory hypothesis** without claiming achieved physical predictions. **Do not change the manuscript's non-image paragraphs as part of this task.**

## E. Real QA, binary and browser acceptance — absolutely required before claiming implementation PASS

1. **Static source HTML tests:** seven figures exactly once, seven slots in correct order, seven captions, unique `aria-describedby` IDs, no duplicate/empty alt, all href/src/srcset paths exist, unchanged original Paper Two article content outside figure conversions, no legacy figure images incorrectly used, no unexpected scripts/network requests, no broken hyperlinks. Test article at local HTTP origin (not `file://`).
2. **Binary regression:** source vs new website 7 master SHA-256, 21 variant hashes/decode/dimensions/actual compression sizes; preserved 7 prior legacy WebP and source PNG hash identities as relevant; Git readback after push; protected PR #5, #11 and #12 branches/heads stay unchanged.
3. **Browser tests, not screenshots alone:** run actual Chromium/Playwright on **320×740 DPR1, 390×844 DPR1, 390×844 DPR2, 768×1024 DPR1, desktop 1440×900 DPR1, desktop 1440×900 DPR2**. Use local HTTP serving the checked-out PR #13 branch, verify `currentSrc` selection for all seven, native click-to-open of master PNG and decode 1920×1080 in a new tab, no horizontal overflow, image aspect and legibility, keyboard/tab focus, no JS runtime issues, blocked-image accessibility, alt/caption/long description remains readable. Log actual resource transfer bytes and selected WebP variants. Explicitly distinguish automatic browser emulation from **physical handset** and actual screen-reader tests.
4. **If local Work browser is blocked** (`ERR_CONNECTION_REFUSED`, denied sockets or `file://`), implement a **PR #13-only GitHub Actions** safe `push` QA workflow modelled on [Paper One's proven browser script and workflow](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-paper-one-seven-cinematic-optimised-20261120/.github/workflows/p1-seven-cinematic-browser-acceptance.yml), permissions `contents:read`, no deploy, no merge, upload screenshots plus JSON and document exact successful Actions run ID. The original Work browser failure does not count as successful QA.
5. **Science and accessibility acceptance:** visual 1920, 320, 390, and desktop screenshots; carefully examine tiny figure 2.1/3.1 text. Ensure visible HTML long descriptions and keyboard-enabled full-size PNG access; no assumption inline fine print becomes readable at phone width. Evaluate protected scientific qualifiers exactly against paper's source section and Work re-audit.
6. **Measured report:** commit e.g. `docs/reports/V2_PHASE_03_P2_SEVEN_RESPONSIVE_WEBP_DERIVATIVE_MANIFEST_20261121.json` and `docs/reports/V2_PHASE_03_P2_SEVEN_RESPONSIVE_WEBP_INTEGRATION_QA_20261121.md`, with actual 7+21 binary hashes, total bytes, independent browser test matrix, DPR variants, transfer measurements and explicit PASS/FIX/BLOCKED outcome. Keep preparation manifest as frozen preimplementation baseline and put measured results in new docs.
7. **GitHub handback:** verify PR #13 still **DRAFT, OPEN, UNMERGED**, base = PR #5 website branch, no commits to any other branch, no deployment. Publish DTSU v1.1 final with complete `COPY TO CHAT` summary and exact links; request owner review of draft HTML/screenshots separately before any release.

## F. STOP conditions and prohibitions

- If any approved image source cannot be fetched byte-exact, **STOP** and report `GITHUB_SOURCE_BINARY_BLOCKED`. No regeneration or AI rewriting of images.
- If any in-image mathematical/science statement conflicts with external description, **STOP** for factually targeted repair, without silently altering approved master PNG.
- If CSS/figure migration breaks existing article reading, **STOP**, document regression and fix only inside PR #13.
- If browser tests cannot execute, explicitly report **BROWSER_QA_BLOCKED** rather than claim responsive QA passed.
- **No merge, deployment, site release, change to PR #5/#11/#12 branches, or alteration of owner-approved source assets.**
- Work in this **existing PR #13**, do not create another PR for the same implementation.

## COPY TO WORK — concise execution prompt

Please execute the [SYMMETRIA Paper Two seven approved cinematic images responsive WebP integration handover](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-paper-two-seven-cinematic-webp-20261121/docs/handovers/V2_PHASE_03_WORK_P2_SEVEN_RESPONSIVE_WEBP_SEPARATE_DRAFT_PR_EXECUTION_20261121.md) **in EXISTING draft PR #13**, based on unmodified PR #5. Pull the **seven exact approved** 1920×1080 PNGs byte-for-byte from Paper Two artwork PR #12, including corrected 2.1, 3.1 and 6.1; independently verify every original SHA-256 and Git blob; preserve masters; generate 21 quality-93 responsive WebPs; implement exact seven-image HTML/caption mapping, selectable scientific descriptions and full-resolution viewing links; perform real 320px/390px/desktop browser tests including DPR1/2, with GitHub Actions if Work's browser is restricted; record actual size savings and 28 binary hashes, science/accessibility QA and screenshots. Follow DTSU v1.1 and finish with complete GitHub reports and COPY TO CHAT. **Do not change PR #5, #11, #12, merge any PR or deploy anything.**
