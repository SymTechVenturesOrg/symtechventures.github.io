# Phase 2 — Full-width Earthrise draft implementation

**Date:** 17 November 2026 (GMT)
**Status:** Implemented on draft feature branch; full exact-branch browser/regression checks **PENDING**. No merge, publication or release authorisation.
**Source:** Owner-selected first cinematic Earthrise, larger six-link typography approved in Chat. See planning [hero handover](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/handovers/V2_PHASE_02_EARTHRISE_OWNER_REVIEW_AND_INTEGRATION_HANDOVER_20261117.md).

## Changed files

- `images/heroes/v2_earthrise_fullbleed.webp`: OpenAI-generated first Earthrise website composition, converted to WebP quality setting 80 (1672 × 941 px; 257,542 bytes). Synthetic/conceptual scene, not a real mission photo. **Contains baked image-origin typography on its left side; the live DOM hero CSS masks that region**, which must be inspected at every viewport and zoom level. A later clean image-only asset would be preferable.
- `css/v2-site.css`: enlarged six-link navigation, mobile-menu threshold for narrower widths, full-width hero background with accessible live HTML copy over a dark text-safe overlay, mobile caption contrast.
- `index.html`: homepage-only `v2-earthrise` class enabling scoped hero treatment. All existing page content, links, approved science caveats, programmes, papers and inline orbital SVG kept for rollback. The SVG is hidden solely in the new visual treatment, not deleted.

## Current evidence and release requirements

Prior **standalone local** proof had no horizontal overflow at 320/390/768/1440px; it was not the real site. Binary asset provenance and byte count were checked before creating a GitHub blob. **Do not claim feature-branch screenshot testing, keyboard/accessibility success, performance acceptance or Python regression exit 0 yet.**

After this GitHub commit: inspect full actual checkout of the exact commit at 320, 390, 768, 920, 960, 1080, 1280, 1440px, including responsive nav, real mobile disclosure, image source request, all six links, skip link, focus order, text contrast, visual clipping, no baked text reveal, zoom and reduced-motion. Run `python3 -u docs/reports/scripts/v2_stage8_qa.py` and focused accessibility tests; include screenshots, test exits and rollback diff in a follow-up report. Retain draft PR #5 until the owner separately authorises merging/deployment. Do not alter paper figures or other programme statuses.

## Final clean-image correction and visual inspection — 17 November 2026

The first exact-branch GitHub Actions run [#44130238440](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44130238440) completed **successfully** at commit `df876e5496dc8ef7959495d0e3c728faa9244fdd`, including the full regression and nine 320–1440px Earthrise/nav breakpoint checks. **Visual inspection of the downloaded 1440px screenshot detected faint background lettering from the original mock-up**, despite passing the automated checks.

To remove that defect, a **new image-only original conceptual Earthrise** was generated in the same approved visual direction: cratered lunar surface, Earth on the right, cyan rim, amber sunrise and static stars with **no embedded branding, interface labels or UI**. The replacement `images/heroes/v2_earthrise_fullbleed.webp` is **1672 × 941 px, 244,768 bytes, WebP encoder quality 80**, SHA-256 `cab7d18ea55e9e2701954bc08e6a9042e8136b505b7f448cdc51c9d2aad08833`. It remains **synthetic conceptual artwork**, not documentary photography or evidence of research results.

The hero CSS has been consolidated and the opaque text-hiding mask replaced with a softer, readable gradient. **Local headless Chromium rendered the actual extracted HTML/CSS with the new asset inlined as data WebP** at **320,390,768,920,1440px**, all with no horizontal overflow. Visual review of desktop and 390px screenshots confirmed no embedded lettering and adequate obvious text readability. This is a *local exact-source presentation proof*, not yet final exact-branch QA for the newly committed image.

**Post-change final gate:** run the exact-branch GitHub Actions workflow again on the **new HEAD**; inspect final desktop/mobile images, save actual report and bundle full offline website only after all checks pass. No Phase 3 changes, no merge, no deployment.
