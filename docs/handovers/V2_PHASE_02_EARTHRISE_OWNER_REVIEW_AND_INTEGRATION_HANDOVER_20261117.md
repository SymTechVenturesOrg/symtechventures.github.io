# Phase 2 — Full-Bleed Earthrise Hero: Owner Review and Conditional Integration

**Date:** 17 November 2026 GMT  
**Status:** **Local prototype delivered; owner preference logged; implementation NOT authorised**  
**Planning:** [draft PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)  
**Implementation:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), `feature/v2-space-research-website`

## Owner decisions

1. Phase 1C layout was approved; the right-column `.orbit-wrap` orbital SVG is the unmerged implementation baseline.
2. The owner prefers the **first** generated cinematic Earthrise image: cratered lunar foreground, luminous Earth with cyan atmosphere, amber sunlight and stars. The earlier exclusion concerned **animated starfield backgrounds**, not static stars in artwork.
3. After seeing a crop in the right art column, the owner expressly preferred **“the image you generated earlier where the image took up the entire page.”** The preferred next *visual review* is thus **full-bleed, hero-width Earthrise behind site text**, not a standalone crop in the existing right-hand slot.
4. This design preference **does not yet authorise a source-code replacement, PR merge, deployment, site-wide layout redesign or further imagery**. The hero-specific variant requires acceptance before engineering integration.

## Local visual prototype and provenance

A local stand-alone HTML mock-up uses the **first** OpenAI-generated 1672 × 941 conceptual image as a full-width hero background. Its original screenshot-like copy and buttons remain baked into the source image, so a dark CSS overlay on the *left* prevents duplicated lettering, while retaining right-side Earthrise/stars and foreground. Actual HTML displays the GitHub homepage's honest primary messaging and early-stage disclaimer, plus six navigation links and two real anchors. **This is a layout/art study, not a production-ready image source**. Prefer a future clean, image-only Earthrise of matching composition rather than depending permanently on masking embedded text.

- First AI-rendered PNG `a_cinematic_high_detail_photorealistic_space_the.png`: 1672 × 941 px, **2,812,061 bytes**; SHA-256 `e0e15a081a80e91743dfbf31545bc5a7aea5d2bcabb855e8f8e06dfb9a4a8e12`.
- WebP background `symtech_phase2_fullbleed_earthrise_art_q80.webp`: 1672 × 941 px, quality value 80, **257,542 bytes**; SHA-256 `c883df2e90343b7dcb65628028c035f1aa3bb427b11301bc4b73ba2929efaf6d`.
- Self-contained Chat-local HTML: `symtech_phase2_fullbleed_earthrise_preview.html` (WebP embedded as a data URL).
- Chat-local Chromium screenshots: `symtech_phase2_fullbleed_preview_{320,390,768,1440}px.png`. Not checked into GitHub.

**Local Chromium evidence:** Document client and scroll widths match at 320, 390, 768, 1440 px; no horizontal overflow in this **standalone approximation**. Desktop screenshot shows full-width Earthrise extending behind hero; mobile screenshots place copy first with Earthrise/lunar foreground below and behind. The initial mobile disclaimer contrast problem was addressed **within the local preview** using an opaque navy background and gold left border. The entire GitHub website, production keyboard/accessibility flows, exact-branch Python regression and performance have **not** been retested after any actual integration (there has been none).

**Disclosure:** synthetic conceptual art, not a specific Apollo/NASA image, mission photograph, real dataset, established physical discovery or an actual spacecraft view.

## Conditional integration/QA instructions (do not execute until approval)

- Resolve artwork source as a **clean, no-embedded-text** full-bleed asset, following owner's confirmed visual reference. If using this source as-is, keep its baked labels fully obscured across all target viewports; avoid adding duplicate/contradictory content.
- Preserve `index.html` research programme counts/statuses, six primary links, exact page URLs, visible research caveats, and real semantic links/buttons. No animated starfield, parallax or baked-in UI.
- Full-bleed hero may require scoped `css/v2-site.css` and `index.html` changes, **not** a broad redesign. Keep original orbital SVG recoverable.
- Verify under actual feature branch at 320/390/768/1440 px with real Chromium captures, zoom/focus/keyboard/menu checks, Lighthouse/axe where available, contrasting overlaid text, acceptable LCP/image bytes and reduced-motion behaviour.
- Re-run `python3 -u docs/reports/scripts/v2_stage8_qa.py` on the post-change exact commit; record its real exit status, changed-file digest, before/after screenshots and genuine rollback instructions.
- Leave PR #5 draft, unmerged; no publication, paper-figure replacement, new BridgePoint lessons, DNS, enquiry form or scientific status modifications.

## Next owner decision

Review the **full-width Earthrise visual** and decide **accept, refine or reject**. The Chat preview is evidence of a promising direction, **not the final integration-approved website**.

## Owner-directed navigation typography refinement — 17 November 2026

The owner reviewed a screenshot showing the six primary desktop links (**Home, Research, BridgePoint, Discussion Papers, Publications, About**) and asked for them to be slightly larger. A Chat-local full-width Earthrise HTML preview was updated:

- Primary navigation link size increased from **0.83rem (about 13.3px)** to **1rem (16px)** at widths above 1080px, retaining the same link order, wording and destinations.
- At intermediate widths, the prior **0.72rem (11.5px)** fallback was increased to **0.9rem (14.4px)** up to 1080px.
- Since the wider labels previously wrapped awkwardly near tablet width, the preview now uses the existing **mobile disclosure menu at 919px and below** (the prior design used it only at 750px and below); the actual small-screen 750px menu rules are unchanged.
- Local Chromium checked the adjusted stand-alone preview at **320, 390, 768, 960, 1024, 1080, 1100, 1180, 1280 and 1440px**, and found **no horizontal overflow**. At 960px and above, all six links stay on one row. Screenshots were rendered at 1440px, 960px, 768px and 390px. Browser testing covers the local stand-alone preview only, **not the GitHub implementation branch**.

Review files (Chat-local, not GitHub): `symtech_phase2_fullbleed_larger_navigation_preview.html` and `symtech_phase2_larger_navigation_{1440,960,768,390}px.png`. **This is a minor review variant, not a Phase 1C implementation change or an authorisation to merge/deploy**. Future implementation should use these sizes and recheck all navigation links, keyboard disclosure, focus visibility and full regression on the branch.
