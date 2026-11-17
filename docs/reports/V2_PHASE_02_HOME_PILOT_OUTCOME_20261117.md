# Phase 2 — Homepage Hero Artwork Pilot: First Attempt

**Date:** 17 November 2026 (GMT)  
**Project:** SymTech Ventures v2.0  
**Source:** [Approved Phase 1 layout freeze](../V2_PHASE_01_LAYOUT_FREEZE_20261117.md), [Phase 2 design brief](V2_PHASE_02_SITE_ARTWORK_BRIEF_20261117.md)  
**Status:** **NOT APPROVED FOR WEBSITE — PILOT NEEDS VISUAL REFINEMENT**

## What was actually done

Phase 2 begins with the agreed **single homepage hero** slot in the existing `.orbit-wrap` container; no Research/BridgePoint images have been commissioned.

- Two initial AI image-generation attempts produced **off-brief status-dashboard compositions**, containing text and several imagery/quantity claims inconsistent with the artwork brief. They are **rejected** and will not be used or committed as production website assets. Do not treat their embedded checklist texts or image counts as project facts.
- As a fallback **technical/format prototype**, Chat generated an original, procedural Earth-above-lunar-horizon illustration without stars or typography. It was rendered in Python at **1432×988 PNG** and exported at **716×494 WebP** with encoder **quality value 80**, method 6.
- Measured local output sizes: source PNG **546,366 bytes**; WebP quality 80 **10,888 bytes**. The smaller WebP is largely a result of simple smooth shapes and does **not** show that visual image detail is sufficient.
- **Aesthetic evaluation:** this procedural output is **not polished enough to replace the existing orbital SVG**. Its purpose is to verify target size and WebP conversion settings, **not** obtain automatic final art approval.

The technical pilot files are available to the user in the active Chat conversation as generated attachments:
- `symtech_phase2_earthrise_pilot_source.png`
- `symtech_phase2_earthrise_pilot_q80.webp`

These local generated files are **not committed to the implementation GitHub branch** and should not be referenced in website HTML or used as live assets. There is no GitHub binary for them to link to.

## Next controlled art step

Obtain one **high-quality AI-rendered, text-free** Earthrise-style conceptual image that meets the actual restrained navy/cyan/amber design brief, with no starfield. The user must review it before Codex conversion/integration. A technical prototype showing WebP encoding is **not equivalent to approved artwork**.

Once the user chooses a suitable image, use Codex (Luna Medium / Standard) for deterministic WebP quality-80 export and *separate* PR #5 integration with full 320/390/768/1440 browser and regression verification. Current orbit SVG remains until then.

## Current state

**Phase 1 layout: owner-approved. Phase 2: design brief and first technical pilot complete, no approved raster image. Phase 3: not started.** No website source/paper figure changes, no merge and no deployment.

## 17 November 2026 — follow-up artwork generation (Chat continuation)

Following the Phase 1-approved handover, four further image-generation attempts were made to obtain the one standalone homepage Earthrise image. **All four were rejected**: they produced complete marketing/website hero mock-ups with baked-in branding, headings, navigation or CTAs, starfields and/or broad technology claims, despite the explicit Phase 2 exclusion of these elements. They are not suitable for insertion into the existing `.orbit-wrap` art slot, and none is owner-approved.

**Decision:** no image integration, no WebP conversion of a selected asset, no site HTML/CSS/JS updates and no release action. Keep the current orbital SVG on feature PR #5. A future suitable image must be a clean, text-free, star-free **standalone Earthrise illustration**; it should be reviewed as artwork before conversion or integration. The Phase 1 layout approval remains intact and is not reopened.

**Status after this continuation:** Phase 1 frozen/approved; Phase 2 image selection remains open with no approved raster; Phase 3 not started. The generated mock-ups are rejected examples, not production assets and not evidence of website or research capabilities.

## 17 November 2026 — owner preference; static-stars correction; usable review crop

**Owner preference:** the **first** AI-generated Earthrise full-width mock-up is the closest to the desired look. The earlier rejection of starfields **as an inherent property of imagery is superseded**. Static stars, including a photographic-looking galaxy backdrop, are welcome **inside artwork**; the discarded design feature was the **animated website starfield background**. The first image's Earthrise/lunar light treatment is a visual reference, not approval to switch the homepage into the mock-up's copy, links, navigation or division claims.

**New candidate created without re-generating content:** an art-only crop of the **first** original AI-generated mock-up, excluding its baked-in branding, typography, CTAs and navigation. Source original: **1672 × 941 PNG**. Crop coordinates (left,top,right,bottom) **(810,185,1672,767)**; preview PNG **862 × 582**, **872,124 bytes**. Responsive review export **716 × 484 WebP**, quality parameter **80**, method **6**, **65,914 bytes**. Visual inspection in Chat confirmed only a cratered lunar surface, Earthrise, static stars/Milky Way, cool blue atmospheric light and warm amber backlighting; no embedded website text or buttons remain in this crop.

**Provenance:** OpenAI-generated synthetic/conceptual illustration, manually cropped/resized by Chat for owner's visual review on 17 November 2026. The PNG and WebP are available as downloadable attachments in that Chat, **not in the GitHub repository**. Not a NASA image, scientific observation, mission photograph or evidence of technological achievement. Candidate alt text: “Conceptual illustration of Earth rising above a cratered lunar landscape under a starry sky.”

**Decision/gates:** New **pilot candidate available for owner review**, not yet explicitly approved as an actual replacement. The `index.html` inline orbital SVG is unchanged. No raster binary has been committed, no browser regression on a replaced-art site has been run, PR #5 remains draft/unmerged, and no deployment or scientific paper changes are authorised. On approval, integrate and test the image via a discrete feature-branch engineering pass.

## 17 November 2026 — full-bleed visual-direction correction and responsive preview

The owner made a further explicit preference: **“I prefer the image you generated earlier where the image took up the entire page.”** Therefore the previously produced **small right-column crop is *not* the preferred presentation**. The desired treatment is the first dramatic Earthrise/lunar/stars artwork occupying the *entire homepage hero width*, with website header, live text and buttons overlaid. This is not an instruction to copy the AI image's original baked-in claims or to remove the rest of the website.

**Local implementation proof of concept, not committed:** The original first rendered 1672 × 941 conceptual PNG (2,812,061 bytes; SHA-256 `e0e15a081a80e91743dfbf31545bc5a7aea5d2bcabb855e8f8e06dfb9a4a8e12`) was converted to a WebP quality-80 background (257,542 bytes; SHA-256 `c883df2e90343b7dcb65628028c035f1aa3bb427b11301bc4b73ba2929efaf6d`). A self-contained Chat-local HTML variant recreates the approved homepage's main messaging, research caveat, six navigation links and two real HTML buttons, using a left opaque gradient/mask to obscure the source mock-up's embedded text and prevent double text. Source background bytes are embedded for an offline review; there is no animation.

**Actual local Chromium (not full site) checks:** viewport widths **320, 390, 768, 1440** each had `document.documentElement.scrollWidth === clientWidth` (no horizontal overflow); screenshots were generated for each. Desktop at 1440 shows lunar/Earth scene filling the hero right/top-to-bottom behind live left-aligned copy. At 390, design stacks the content while retaining lunar texture below. **Issue to fix:** mobile disclaimer loses contrast where it overlaps lunar rock; adjust gradient or give text an opaque background. Also confirm crop, header contrast, active/focus states, menu keyboard operation and genuine full-branch browser QA in the later implementation pass.

**Review artefacts in the active Chat, not GitHub:** `symtech_phase2_fullbleed_earthrise_preview.html`, `symtech_phase2_fullbleed_preview_1440px.png`, `symtech_phase2_fullbleed_preview_390px.png`, `symtech_phase2_fullbleed_preview_320px.png`, `symtech_phase2_fullbleed_preview_768px.png`. These are design concepts only, not real deployment screenshots. The previously recorded first-art crop remains available as an alternative, but is no longer preferred.

**Status:** owner preference updated; image/background concept prototype complete. Owner approval of the final full-width composition, formal asset transfer, integration into PR #5, full exact-branch regression, owner release and merge all remain pending. The existing orbital SVG and all published pages are unchanged.
