# SymTech Ventures v2.0 — Phase 1A Layout Audit and Provisional Image Slots

**Prepared:** 17 November 2026 (GMT)  
**Status:** **FIRST PASS COMPLETE — Phase 1 layout NOT yet frozen or visually approved**  
**Workplan:** [Three-phase layout-first workplan](../V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md)  
**Feature source inspected:** `feature/v2-space-research-website`, PR [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), head at audit start `77f82a0f9169978db6d6996ce5b0160c34da2e01`  
**Planning branch:** `planning/space-first-research-website-20261116`, PR #2  
**Status of original research:** no figure/article/source changes from this audit.

## Audit method and actual evidence

Read the **current GitHub HTML/CSS source** for `index.html`, `css/v2-site.css`, `css/v2-programmes.css` and the landing pages `research`, `bridgepoint`, `discussion-series`, `publications`, `about`, `contact`. Reviewed archived browser screenshot files including:
- [Postapproval Home at 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/postapproval-home-390.png)
- [Postapproval About at 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/postapproval-pages-about-390.png) and [1440px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/postapproval-pages-about-1440.png)
- [Postapproval Contact at 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/postapproval-pages-contact-390.png)
- [Postapproval Discussion Series at 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/postapproval-pages-discussion-series-390.png)
- Earlier [NSRP mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/v2-nsrp-mobile.png), [BridgePoint mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/v2-bridgepoint-mobile.png) and [Research desktop/mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/v2-research-mobile.png).

**Evidence warning:** Archived `v2-*` and `postapproval-*` captures **precede some later navigation/accessibility code changes**, and older `v2-research` screenshots show decorative stars/preview markers that **are not present in the current source after the owner-approved cleanup**. They describe visible historical layouts, **not** independent current-head browser verification. The full Stage 8F-D integration regression passed after later changes; that was functional QA, **not fresh owner visual sign-off**. Phase 1B must produce fresh exact-branch render evidence at **320, 390, 768, 1440 px**.

## What already works — preserve

- A clear **space-first** independent-research proposition and a restrained near-black/midnight palette, subtle blue/gold accents, no starfield in `css/v2-site.css` or active animation script, large serif headings and natural links.
- One consistent header with six primary links and mobile disclosure on the redesigned landing pages, plus readable current-page styling after Stage 8E.
- Homepage order is sensible: **hero → four programme cards → four accessible discussion papers → BridgePoint pathway → evidence caution → footer**. Main pages themselves have **zero embedded `<img>` elements**, so Phase 2 can be deliberately sparse rather than reverse-engineering existing artwork.
- Correct claims and programme counts: four available and twelve planned discussion essays; 16 BridgePoint titles still Planned; NSRP 5×4 and SEIP 5×4; Publications empty; paused Contact/Enquiry.
- Article shells retain four full original papers, seven unique paper illustrations each, accessible keyboard focus and table scrolling from Stage 8F-E. Do not change paper main content until Phase 3.
- Previous technical assurance: Stage 8F-D axe 4.14.1 returned **0 violations across 12 sampled scans**, full regression exited **0**; Stage 8F-E verified Paper 1 table's actual keyboard scrolling. These do **not** substitute for owner layout approval or full WCAG conformance testing.

## Page-specific first-pass findings

| Page/area | Source/screenshot observations | Phase 1 action |
| --- | --- | --- |
| **Home** | Clear two-column desktop hero in CSS; mobile 390 screenshot shows headline, stacked two CTAs, orbit SVG, four single-column programme cards, paper list and learning footer. No overflow evident in inspected 390 capture. Current hero media container is `.orbit-wrap`, SVG with a near-square `viewBox=520×510`; the previously proposed Earthrise WebP binary is not verified in GitHub. | **Keep the good layout**. Define hero image crop/layout and mobile alternative, but **do not replace SVG or point to a missing raster** until Phase 2. Recheck 320px h1 wrapping and below-fold scroll length. |
| **Research** | Text-led, four connected-programme cards, evidence note, space rationale; older mobile/desktop captures show sensible hierarchy but **pre-date final starfield and preview cleanup**. | Preserve card order and claims; get fresh exact-branch 390/1440 screenshots; consider modest sectional visual support only after layout slot approved. |
| **SYMMETRIA landing** | Shared programme page shell; exploratory theory and links to original papers, no required hero raster. | Verify page header/reading route at 390/1440; avoid standalone image that implies validated science. |
| **NSRP / SEIP** | Five project cards with four nested phase cards each. NSRP archived mobile shows very long single-column scrolling but readable cards and clear Planned status. | Consider an optional **static in-page jump list** to the five projects at top for quick mobile navigation; ensure semantic anchors, headings and no JS dependency. Do not collapse/rewrite 20 research or engineering phases. |
| **BridgePoint** | Mobile capture shows four category headings and 16 long sequential lesson cards, all marked Planned. | Consider a concise four-item category jump navigation (not new lesson pages); visually maintain status hierarchy and readability. |
| **Discussion Papers** | Recent 390 capture shows four distinct categories and 16 sequential cards, with four genuine reading links and 12 planned items. Mobile length is substantial. | Consider four-category jump navigation to reduce scrolling; preserve labels and original paper URLs. Investigate card status labels wrapping on 320px. |
| **Publications** | Deliberate empty state in shared shell and link to discussion essays. | Preserve absence of publications; no decorative placeholder intended to suggest actual research output. |
| **About** | Postapproval 390/1440 captures show excellent hierarchy; actual visible issue at 390 is **noticeable uneven/stretched inter-word spaces** in multiple fully justified prose lines. Desktop appears comfortably legible. | **Readability review**, not automatic repeal of owner's full-justification rule. Test responsive hyphenation/line balancing and natural short-label alignment in the real browser; propose any mobile typography compromise **for owner approval**. |
| **Contact** | Postapproval 390 capture shows coherent status note/cards, readable subdued content and a clear paused-enquiry policy; no live form. Some justified-card lines also have wide spacing at 390px. | Preserve privacy boundary and card layout; include focused 320/390 readability and footer checks. |
| **Paper reading shell** | v2 articles CSS, preserved 28 paper illustrations, keyboard-focusable overflowing tables; one page has 7 large images and is necessarily long. | Inspect typography and responsive spacing **without touching original article content/images** during Phase 1. Phase 3 handles figure repairs/captions. |
| **Global header/footer** | Six primary nav links; smaller-screen menu changes after Stage 8E. Footer link sets vary somewhat by page; older pictures show coherent visual identity. | Compare actual current footer consistency and keyboard menu at 320/390/768; change only if a specific navigational/readability problem is demonstrated. |

## Phase 1 corrections — prioritised, not yet implemented

| Priority | Task | Acceptance evidence / boundary |
| --- | --- | --- |
| **P1** | Generate **fresh exact-branch whole-page screenshots** at 390 and 1440 for Home, Research, SYMMETRIA, NSRP, SEIP, BridgePoint, Discussion Papers, Publications, About and Contact; also 320/768 navigation/hero samples. | Current checkout browser; page-by-page visual issues logged; no old stars or temporary preview markers. This is a **visual baseline**, not a new deployment. |
| **P1** | Verify homepage **320px** hero text wrapping, CTA widths, orbital visual, cards and document horizontal overflow; verify 768px navbar breakpoint. | Actual measured scrollWidth/clientWidth, screenshot evidence, keyboard focus where relevant. |
| **P1** | Audit fully justified prose at **320/390** on About, Contact, the Discussion index and programme cards. | Identify specific stretched lines; test *options* that maintain owner's justification where feasible, but **do not silently switch all mobile prose to left alignment**. |
| **P2** | Improve navigability of long **NSRP, SEIP, BridgePoint and Discussion Series** pages if fresh baseline confirms benefit. | Consider **simple in-page anchor index** with visible focus, no JS and preserved phase/lesson/paper counts. Avoid large restructuring. |
| **P2** | Standardise margins/card spacing, section transitions and footer where a visible inconsistency is actually observed. | Narrow CSS/HTML diffs, no redesign or unrelated copy rewrite. |
| **P2** | Freeze **image slots and their responsive crops** before Phase 2. | Owner visual acceptance of the final layout and exact set of image positions, not merely an image-generation wishlist. |

**No confirmed critical structural regression** was identified from the inspected screenshots/source; these are improvements and evidence gaps, not a claim that the current website is broken.

## Provisional Phase 2 image-slot register (NOT final counts)

| Priority | Candidate page/slot | Purpose and visual concept | Candidate desktop ratio | Mobile behaviour | Gate |
| --- | --- | --- | --- | --- | --- |
| **S1 — recommended** | **Home hero**, current `.orbit-wrap` region | One grounded conceptual **Earthrise/planet-and-space visual** signalling space exploration, not an actual NASA photograph. | Approximately **3:2 to 716:494 (~1.45)**, matching the previously proposed 716×494 asset where suitable; evaluate actual two-column crop. | Preserve subject/planet/horizon with mobile `object-position` or less aggressive contain rather than blindly crop. | Owner decides whether to use newly generated art, the previously proposed Earthrise **if the actual binary becomes available**, or retain orbital SVG. |
| **S2 — optional** | Research landing intro / programme pathway | One restrained geometric thematic illustration showing theory → validation → computation, **without labels baked into AI imagery**. | ~**16:9** wide section band, only if it clarifies hierarchy. | Same art cropped/contained, semantic adjacent text conveys meaning. | Owner specifically accepts location and purpose after seeing layout. |
| **S3 — optional** | BridgePoint intro | Calm educational mathematical visual with no fabricated equations; reinforces learning, not completed lessons. | ~**3:2** inset hero or wide feature. | Crop retaining core visual, no textual content required to understand. | Only if image adds value rather than unnecessary page height. |
| **S4 — optional** | One compact shared research-programme visual motif or selected cards | Cohesion across SYMMETRIA/NSRP/SEIP; avoid three speculative spacecraft/experimental photos. | ~**1:1** icons or **4:3** card illustrations, if approved. | Keep cards readable; do not replace accurate status copy with image-only information. | Prefer existing CSS/SVG if sufficient. |
| **No new raster required** | Publications/About/Contact, legacy archive, all original paper figures | These sections already communicate with prose, status notes and retained original content. | — | — | Do not add decorative imagery just to increase count. |

**Image requirements not yet fixed:** actual generation count, byte budget per slot, responsive derivatives, alt text, visual crop and whether S2–S4 are necessary. The user explicitly placed imagery in **Phase 2**, so this is a **slot specification only**, not authorisation to generate images now.

## Next bounded Phase 1B task

Use a **Luna Medium, Standard speed** Codex pass for fresh visual audit and only reproducible, owner-compatible layout fixes, documented in a new finite handover. Codex should not build new imagery or modify SYMMETRIA research bodies. If it changes CSS/HTML, it must rerun the full integrated script and targeted axe checks as necessary; no test result may be invented.

**Phase 1A outcome:** audit/source review and candidate slot register prepared for the owner's layout review. **Phase 1C layout acceptance remains open.** Nothing merged/deployed, no new raster or article figure work started.
