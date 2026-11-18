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
