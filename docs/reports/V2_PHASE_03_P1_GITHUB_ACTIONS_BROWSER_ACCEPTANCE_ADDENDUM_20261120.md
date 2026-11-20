# SYMMETRIA Paper One — GitHub Actions Automated Chromium Browser QA Acceptance Addendum

**Date:** 20 November 2026, Europe/London.  
**Final automated browser QA status:** **PASS — 7 test cases; 0 issues.**  
**Website release status:** **DRAFT PR #11 ONLY; OWNER RELEASE ACCEPTANCE PENDING; no merge or deployment.**  
**Scope:** Replaces the **temporary browser-environment blocker** recorded in the earlier [seven-image image integration QA](V2_PHASE_03_P1_SEVEN_COMPRESSED_CINEMATIC_IMAGES_DRAFT_WEBSITE_QA_20261120.md). The earlier report's binary source integrity, compression, captions and file-size evidence remain valid. This addendum documents **subsequent successful tests** rather than rewriting the earlier Work session's actual blocker.

## 1. Exact CI evidence and provenance

- **Draft PR:** [#11 — seven cinematic WebP-responsive Paper One figures](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/11), base `feature/v2-space-research-website`.
- **Verified implementation commit:** `cc2b9e06f34967847b05c0f7024d6128f165bac0`; QA report commit `e17ae25ef356c70a0863d73539ff10a2efc48fbc`.
- **Final browser QA code commit under test:** `498ad9b52d017bb1e8553ecfd435320bc4a906b2`.
- **Final successful GitHub Actions run:** [#44825419792](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44825419792), job [#136596660071](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44825419792/job/136596660071), **completed SUCCESS** (including Chromium install, script compilation, local HTTP browser test and artifact upload).
- **Evidence:** [GitHub Actions artifact `symmetria-p1-pr11-browser-qa`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44825419792/artifacts/14674420623), **14,871,579-byte ZIP**, containing screenshots and `p1-browser-acceptance.json`. The ZIP is stored in GitHub Actions, **not manually transferred by the owner**.
- **Workflow:** [`.github/workflows/p1-seven-cinematic-browser-acceptance.yml`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/498ad9b52d017bb1e8553ecfd435320bc4a906b2/.github/workflows/p1-seven-cinematic-browser-acceptance.yml).
- **Test script:** [`docs/reports/scripts/p1_seven_cinematic_browser_acceptance.py`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/498ad9b52d017bb1e8553ecfd435320bc4a906b2/docs/reports/scripts/p1_seven_cinematic_browser_acceptance.py).
- **Execution mechanism:** Ubuntu 24.04 GitHub-hosted runner, Python Playwright 1.56.0 and Chromium, serving the *exact PR checkout* via an ephemeral `127.0.0.1` HTTP server **inside the same runner**. No public preview, GitHub Pages publish, remote website mutation, hosting change or deployment.

The first run [#44824780432](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44824780432) passed the baseline browser suite. The second run [#44825175998](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44825175998) passed again and printed actual selected WebP variants and network transfer data. **Final** run #44825419792 additionally opened the matching **seven full-resolution PNG links** through browser keyboard-activated navigation on desktop, verifying successful image decoding and 1920×1080 native dimensions for the six non-cover assets; the cover link was also opened and its correct master URL checked. All 7 total cases passed with 0 issues.

## 2. Real Chromium responsive source-selection and transferred bytes

The script loads **all seven** Paper One images into view before reading same-origin PerformanceResourceTiming values. `selected_body_bytes` represents decoded browser-reported *compressed network response bodies*, not raw pixels; `selected_transfer_bytes` also includes browser timing's response transfer overhead. Values below are **actual Chromium local-HTTP resource-timing measurements**, not static manifest estimates. They do **not** estimate mobile cellular throughput or whole-page total bytes (HTML, CSS, scripts and fonts are excluded).

| Chromium configuration | Chosen WebP across all 7 figures | Browser body bytes | Browser transferred bytes | Transferred saving vs 21,896,557 original PNG bytes |
|---|---|---:|---:|---:|
| 320×740 mobile, DPR 1 | 768w × 7 | 985,588 | **987,688** | 95.49% |
| 390×844 mobile, DPR 1 | 768w × 7 | 985,588 | **987,688** | 95.49% |
| 390×844 mobile, DPR 2 | 768w × 7 | 985,588 | **987,688** | 95.49% |
| 768×1024 tablet, DPR 1 | 768w × 7 | 985,588 | **987,688** | 95.49% |
| 1440×900 desktop, DPR 1 | 1280w × 7 | 2,246,898 | **2,248,998** | 89.73% |
| 1440×900 desktop, DPR 2 | 1920w × 7 | 3,924,054 | **3,926,154** | 82.07% |

These are **all-figures-loaded** figures in a local browser, rather than an initial-above-the-fold load. The cover is `loading=eager` and the other six remain `loading=lazy`. The PR's original 21 optimised WebP binaries and seven exact source/master PNG hashes remain unmodified by this QA pass.

## 3. Verified browser behaviours

| Gate | Result |
|---|---|
| HTTP serving local checkout within GitHub runner | PASS |
| Six viewport/DPR cases incl. 320px and 390px | PASS |
| Exactly seven semantic Paper One figure slots | PASS |
| All seven WebPs loaded and selected `currentSrc` matches their slot | PASS |
| Actual 768w / 1280w / 1920w `srcset` selections | PASS |
| Browser-measured selected image resource transfer bytes | PASS |
| No document horizontal overflow in tested viewports | PASS |
| Preserved approximate 16:9 display frame with no detected ratio distortion | PASS |
| Every figure has meaningful alt and associated selectable long description/caption | PASS |
| Visible Figure 1.1 `Λ = 0` caveat in caption and description | PASS |
| Figure 2.1 caption avoids `fundamentally incompatible` | PASS |
| Figure 5.1 caption states `untested hypothesis` | PASS |
| Cover new-tab full-resolution opening by keyboard or Chromium-emulated touch | PASS |
| Remaining six full-resolution links opened via desktop keyboard and correctly decoded 1920×1080 PNGs | PASS |
| Deliberate failed Figure 2.1 display derivative leaves alt/caption/description present and visible | PASS |
| Browser page JavaScript errors | None reported in six viewport cases |
| Screenshots and JSON evidence attached to GitHub Actions run | PASS |
| **Independent human inspection of all collected responsive screenshots** | **NOT CERTIFIED by automation** |
| **Physical device and screen-reader assistive-technology tests** | **NOT PERFORMED** |
| **Public deployment / site publication** | **NOT PERFORMED** |

## 4. Acceptance limitations and required next gate

The previously reported `ERR_CONNECTION_REFUSED`, restricted `file://` and Chromium socket issues occurred in **Work's cloud browser execution environment**. They are no longer a blocker to **automated GitHub-hosted Chromium** checks, because HTTP server and browser shared the GitHub runner network namespace.

This test verifies page structure, responsive layout, asset selection, actual resource timing, link activation, and fallback behaviour. It does **not** make the embedded equation glyphs fully readable at 320–390px inline width. That limitation is addressed by **selectable scientific captions/long descriptions and same-image full-resolution links**; human screenshot review, real phone browsing, screen-reader checks and optional further visual polish are owner/release review activities. The quality-93 encodings and compression fidelity were separately checked against source PNG crops in the earlier integration QA report.

**Recommended current PR #11 status:** `AUTOMATED_BROWSER_QA_PASS; OWNER_VISUAL/RELEASE_REVIEW_PENDING`. Keep the PR **open and DRAFT**. The seven image binaries and original WebPs must remain intact, no PR #5 head changes, no merge and no deployment.

## 5. COPY TO CHAT

**SYMMETRIA Paper One PR #11:** GitHub Actions Chromium browser QA **PASSED** from the isolated, unmerged PR checkout: six responsive viewport/DPR cases, one intentional broken-image fallback (7 cases, 0 issues). All seven selected WebPs loaded correctly with verified `srcset` selection, true measured network image transfers were 987,688 bytes at 320/390px and 2,248,998 / 3,926,154 bytes on 1440px desktop DPR 1/2. All seven full-resolution PNG links were opened or checked, with all six non-cover PNGs independently decoded at 1920×1080. Scientific caption caveats and accessible descriptions are present. The GitHub Actions [run #44825419792](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44825419792) and [screenshot/JSON artifact](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44825419792/artifacts/14674420623) retain browser evidence. Automated browser acceptance is no longer blocked; owner/human responsive visual review and release authorisation remain pending. No merge, website production deployment, PR #5 modification or source PNG alteration.
