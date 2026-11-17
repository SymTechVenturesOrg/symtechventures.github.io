# SymTech Ventures v2.0 — Phase 1 Layout Freeze

**Date:** 17 November 2026 (GMT)  
**Status:** **OWNER-APPROVED LAYOUT**; not site publication or image approval  
**Design acceptance:** After the [Phase 1C screenshot review](reports/V2_PHASE_01C_OWNER_LAYOUT_REVIEW_PACK_20261117.md) the owner replied **“Approved. Continue. 😄”**. The site layout is accepted as the starting point for Phase 2 website-level imagery.  
**Implementation baseline:** `feature/v2-space-research-website`, [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5); last independently verified full regression [Stage 1C exit 0](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_PHASE_01C_INTRO_TYPOGRAPHY_QA_20261117.md), final evidence commit `b3084c9efbe413644833e2a084fb8ecaea54d599`.

## Approved layout elements
- Dark navy / cyan / restrained gold, no starfield; independent space-first research identity.
- Responsive two-column desktop Home hero and stacked 390px mobile hero; existing inline orbital SVG stays **until an alternative image is individually accepted**.
- Six-link desktop navigation and accessible mobile disclosure; four long pages have Jump to anchor indexes.
- Fully justified paragraphs; standard main intro width aligned to the full 980px-max content column. Mobile `.page-lead` set to 1rem (~16px) at <=740px, other text unchanged. Some uneven inter-word spacing is an accepted known trade-off at this freeze; no blanket left-align conversion.
- Research programme counts and honest Proposed/Planned statuses; no false publications, live submissions or demonstrated spacecraft technology.
- Four original SYMMETRIA discussion-paper bodies and 28 existing figures remain **protected**, not part of Phase 2.

## Scope of Phase 2 approval
Phase 1C's acceptance **authorises progressing to image concept preparation**, not applying an unreviewed image to the site. The first design slot is the **existing Home `.orbit-wrap` region**. Research and BridgePoint artwork remain **optional**, subject to a later owner decision. No requirement to replace six existing logos, twelve historical images or 28 discussion-paper images in Phase 2.

[Phase 2 single-pilot brief](reports/V2_PHASE_02_SITE_ARTWORK_BRIEF_20261117.md) sets original conceptual Earthrise / planet horizon art, no stars, text or equations, approximately 716×494 WebP 80 after review. Final crop and suitability must be judged alongside actual 390/1440 renders.

## Technical release boundaries
An image added after this freeze is a **new website change** and must be separately tested by real Chromium/Playwright and full `python3 -u docs/reports/scripts/v2_stage8_qa.py` on the precise post-change commit. Existing screen-reader/WCAG limits and Stage 9 release requirements remain independent. **No PR merge, deployment, publication or DNS change authorised.**

**Status:** Phase 1 **complete/approved**. Phase 2 **active at visual pilot stage**; Phase 3 **not started**.

## Post-freeze visual clarification — 17 November 2026

After the Phase 2 Earthrise concept review, the owner clarified that the **starfield animation**, not stars inside individual **static space illustrations**, was the feature removed from the website design. The phrase “no starfield” above therefore means **no animated, page-wide or site-wide starfield background**. Static stars and Milky Way texture in a standalone conceptual image are permitted. This clarification does **not** reopen the accepted Phase 1 layout or approve any particular raster asset or site implementation. See the updated [Phase 2 pilot brief](reports/V2_PHASE_02_SITE_ARTWORK_BRIEF_20261117.md).
