# Phase 2 — Original SYMMETRIA figures open independently

**Date:** 18 November 2026 GMT  
**Status:** Implementation staged; exact-branch browser verification pending  
**Owner requirement:** Open each original discussion-paper illustration independently of the website, so desktop readers can zoom and mobile readers can rotate to landscape and zoom/pan.

## Technical approach

- The four available discussion papers already load `js/v2-navigation.js`. The shared script progressively wraps only their seven original paper images each, giving **28** same-origin links to the unchanged WebP source file. Every link uses `target="_blank"` and `rel="noopener"`, so the article remains open in the original tab.
- An explicit **Open full-size image ↗** line appears beneath every figure; the picture itself is also clickable/tappable. Links receive descriptive accessible names derived from each image's existing alt text, and visible focus/hover treatments.
- The new tab opens the actual **image file**, not a shrunk screenshot or an overlay tied to article scroll. Browsers handle direct image viewing, pan and zoom; mobile users may rotate their device to landscape. Browser-specific native pinch/click-to-zoom implementation is outside our code's control.
- Strict regular expression limits the enhanced images to `../../images/symmetria/paper-01..04/*.webp`. Images outside this exact set are left alone, including logo and unrelated pages.
- **All four original paper HTML bodies, 28 image binaries and figure captions remain completely unchanged.** Links are added on load without rewriting the authoritative paper files. With JavaScript disabled, readers still see the original static figures.

## Validation gate

A new exact-commit GitHub Actions Playwright step must verify four papers at desktop (1440×900), mobile portrait (390×844) and landscape (844×390), **84 enhanced image links**, real new-tab creation by keyboard Enter/touch tap, original page remaining open, full-resolution decoded WebP, and no horizontal overflow. The existing 36-page regression, sticky nav, 100%-zoom responsive width checks, scientific content integrity and all previous Phase 2 tests must remain successful.

**Release:** Only draft PR #5; no merge or publication. Phase 3 figure accuracy changes remain unstarted. Browser-specific image zoom may require device acceptance testing by the owner.


## Verified final QA — 18 November 2026

**Exact verified source commit:** `1e19539791b089eec3f20d6267d0b0da3dd81ce7`  
**GitHub Actions run:** [#44335322026](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44335322026), **all steps succeeded**. No deployment or merge.

The complete existing regression (36 HTML files), nine-breakpoint Earthrise responsive tests, enlarged brand/arrow checks, sticky-header scroll tests and 100%-zoom desktop width checks all passed unchanged. The dedicated `Verify paper image opening in separate tabs on desktop and mobile` step returned `result: PASS` with **12 route/viewport combinations** (Papers 1–4 × desktop 1440×900, portrait 390×844 and landscape 844×390), **84 link-instance assertions** (7 per paper in every mode), all with no horizontal overflow. For the first image of each paper, the browser actually opened a popup/new tab by Enter on desktop or tap on mobile, verified its URL matched the original source WebP, verified its native decoded dimensions were non-zero, then checked that the original paper tab remained on its URL.

**Review evidence:** GitHub Action artifact `symtech-phase2-review-1e19539791b089eec3f20d6267d0b0da3dd81ce7` includes the standalone report `paper-image-new-tab-check.json`, screenshots of Paper 2 in both mobile orientations, the original full site ZIP and overall QA logs. The 28-file artifact ZIP passed its CRC integrity check; the embedded 108-file complete website ZIP also passed. The corresponding screenshot shows the clearly labelled **Open full-size image ↗** action below the figure, preserving the adjacent original caption.

**Browser-device caveat:** the site reliably opens the original image as its own tab, but zoom/pan gestures and landscape rotation are provided by browser/OS and should be personally checked in Chrome/Edge/Safari on physical hardware; we did not automate pinch gestures, forced rotation or iOS/Safari. The image data are unchanged and no new lightbox/gesture code is required.

**Current Phase 2 status:** owner-requested image-opening feature implementation and automated browser checks complete. Draft PR #5 remains unmerged and unpublished, and no Phase 3 content has been edited.
