# SymTech Ventures v2.0 — Homepage Prototype

**Stage:** 4 — prototype only  
**Status:** Review requested; **not the production homepage**  
**Date:** 16 November 2026 (GMT)  
**Prepared by:** Chat (the Codex tool was not available directly in this conversation; no Codex or Work tokens were consumed)  
**Related:** [Stage 3 design brief](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md) is on the separate planning branch; [planning PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2) and [tracker #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3).

## Prototype file

[`index.html`](index.html) is a **single, self-contained, static HTML/CSS prototype** held at `/prototypes/v2-homepage/index.html`. It does not replace the production root `index.html`, nor alter `CNAME`, the sitemap, enquiry form or articles.

The design implements:

1. Brand and six destinations: Home, Research, BridgePoint, Discussion Papers, Publications, About.
2. Independent, space-focused research hero and two CTAs.
3. Four programme cards, accurately distinguishing SYMMETRIA, BridgePoint, NSRP and SEIP.
4. Four working relative paths to the existing SYMMETRIA discussion-paper HTML files, plus the original Discussion Series index.
5. BridgePoint learning-path preview (4 categories × 4 planned lessons), clear research/evidence disclaimer, empty formal Publications state and the owner's LinkedIn URL.
6. CSS-generated, non-literal abstract orbital decoration. No existing image assets were copied or substituted without a rights decision.

**Important:** The new programme landing pages do **not** exist yet. Until Stage 6, prototype navigation intentionally uses in-page anchors for those headings and known existing relative URLs for preserved content. The complete site-wide navigation is **not yet implemented**. The logo is an intentionally temporary text mark, not a claim to have transferred or replaced the original graphic.

## Real browser verification

Tested by Chat using **Chromium + Playwright** with the exact locally authored HTML. The final committed GitHub blob SHA was checked against the exact local HTML bytes **excluding one trailing local newline**, and matched:

- **Committed HTML blob:** `66542f4ed4fca09b78cbbe55ee77d719ac5ff717`
- Desktop screenshot: 1440 × 900 viewport; full document height 3337px.
- Mobile screenshot: 390 × 844 viewport; full document height 5522px.
- Additional horizontal-overflow checks: **320, 360, 390, 768, 1024, 1440 and 1920px — all pass**.
- Six primary navigation labels present.
- Mobile `<details>` menu opens when activated.
- No missing in-page anchor destinations.
- Four original SYMMETRIA article `href` values present.
- Exactly one `<h1>`; four programme cards.
- No client-side JavaScript used or page errors observed in the browser test.
- Keyboard Tab starts at `Skip to main content`, then the brand link.

**Note on evidence:** Screenshots were produced as files in the conversation's local working environment and linked directly in the Chat handback. They have **not** been deployed as public preview URLs and are not part of this GitHub prototype PR; this repo contains the actual HTML source. The test used local `page.set_content` because `file://` navigation was blocked by the browser policy.

## Remaining before a production release

- Owner approval of visual style and content hierarchy.
- Stage 5 editorial/scientific review and an owner-approved full-page content brief.
- Stage 6 implementation of all actual programme routes and integration with existing site images if provenance permits.
- Stage 7 BridgePoint pilot and content acceptance.
- Stage 8 full end-to-end link, accessibility, device and regression testing, including the legacy forms and four real paper pages.
- A **separate explicit approval** to merge/publish during Stage 9.

## Reproduction

Save `index.html` and open it in a local browser or development server. For automated checks, use a Chromium/Playwright script to load the HTML via `page.set_content` (or a local HTTP server), capture full-page screenshots at 1440px/390px and compare `document.documentElement.scrollWidth` with `clientWidth`.

**No production change has been made.** Do not merge this prototype as the new root website.
