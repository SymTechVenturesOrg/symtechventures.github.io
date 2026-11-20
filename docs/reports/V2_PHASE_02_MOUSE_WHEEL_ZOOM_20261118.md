# Phase 2 — Interactive SYMMETRIA figure zoom (mouse wheel and pinch)

**Date:** 18 November 2026 GMT  
**Owner direction:** The existing opening of images into separate browser tabs is useful, but desktop readers should also zoom with the mouse wheel, in both directions; mobile users should retain landscape and pinch-to-zoom.
**Status:** Feature implemented on draft PR #5. Exact-source GitHub Actions QA awaiting final result; no merge or deployment.

## Design

Each of the four available papers still has seven original figures, with a clearly marked **Open interactive image viewer ↗** link. Opening a figure now launches a dedicated standalone viewer page (`pages/figure-viewer.html`) in a new browser tab, keeping the paper at its current place. The viewer uses the original unmodified WebP image from `images/symmetria/paper-01..04`.

The viewer provides wheel zoom anchored to the cursor, drag-to-pan, a mobile two-pointer pinch gesture, Fit, 100%, Zoom In/Out, keyboard +/-/0 and arrow panning when the stage is focused. The image viewer layout fills the available window in both portrait and landscape. A separate **Original image ↗** link remains available for raw WebP access. The original four HTML paper bodies, all 28 image binaries and figure captions are unmodified.

## Security / accessibility

The viewer allows only local image paths matching `images/symmetria/paper-0[1-4]/[A-Za-z0-9_-]+.webp`, rejecting arbitrary user-supplied URLs, and renders the alt description with `textContent`. All controls have accessible labels, keyboard focus, and mobile tap targets; the figure region is keyboard focusable. Invalid links show an error without making an external request. No third-party scripts or trackers. Source links use `rel=noopener`.

## Required validation

GitHub Actions must pass the full legacy v2 website regression and a dedicated 12-case matrix (4 available papers × desktop, mobile portrait and mobile landscape), confirming all 84 image-link renderings, popups to the new viewer, original file load, zoom buttons, actual wheel zoom in/out, pan, simulated two-pointer pinch and invalid-URL rejection. Real-phone pinch/orientation should also be tested by the owner.


## Verified completion — 18 November 2026

**Tested exact source SHA:** `6153a38cb4aa7967a7f7f9873aac70b412839559`  
**Passing GitHub Actions run:** [#44341795971](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44341795971) — **all steps successful**. The result was obtained from an actual GitHub Actions Chromium/Playwright run of the feature branch, not just from static reasoning or a standalone mock-up.

- `Run full exact-branch website regression`: **PASS**; scientific paper bodies and the 28 original image source files preserved.
- `Run detailed full-bleed and navigation breakpoint QA`: **PASS**.
- Emblem/arrow, sticky header, 100%-zoom full-width desktop and page-width checks: **PASS**.
- `Verify interactive full-resolution zoom and independent image viewing`: **PASS**. The test JSON reports **12** page/viewport modes (Papers 01–04, desktop 1440×900, portrait 390×844, landscape 844×390), **84** link-instance checks, actual new-tab opening, decoded unmodified WebP, keyboard Enter and mobile tap, zoom-in/zoom-out/Fit/100% controls, actual desktop mouse-wheel in/out, drag-to-pan, simulated mobile two-pointer pinch, no overflow, and rejection of external source URLs.

### Interim defects found by the new tests

1. [Run #44338702268](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44338702268) correctly failed a *test assumption* on the Paper 3 cover: its original was **1448px** wide versus a **1440px** viewer stage, allowing only 4px pan on either side. The test required >5px horizontal drag without first sufficiently magnifying the image. The test was corrected to press Zoom In after selecting 100% before asserting meaningful drag travel. **Viewer drag behaviour itself was not changed by this correction.**
2. [Run #44339803070](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44339803070) then passed all four papers' zoom/wheel/drag/pinch interactions but detected a **real visibility bug** for invalid source URLs: author CSS `display:inline-flex` overrode the browser's `hidden` attribute on the original-image link. A scoped `[hidden]{display:none!important}` rule in `css/v2-figure-viewer.css` corrected this. The final run #44341795971 passed the invalid-source security/visibility check as well.

The final runner uploaded artifact `symtech-phase2-review-6153a38cb4aa7967a7f7f9873aac70b412839559` with complete 111-file website ZIP, JSON QA results and screenshots of the dedicated viewer on desktop, portrait and landscape. Both the artifact archive and the inner site ZIP passed ZIP CRC integrity checks. The site ZIP was made available in the owner's Chat.

**Release boundaries:** PR #5 remains draft and unmerged; the live website is unchanged. No Phase 3 figure revisions or new scientific claims. For physical-device acceptance, verify mouse wheel on Edge/Windows and touch pinch/rotation on an actual phone; automated pointer simulations are not a substitute for every browser/OS configuration.
