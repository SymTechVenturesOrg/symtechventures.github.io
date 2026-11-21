# SYMMETRIA — Paper One: Seven Compressed Cinematic Website Figures — Work Implementation Handover

**Date:** 20 November 2026 (Europe/London).
**Owner decision:** Owner explicitly authorised creating a **separate draft website-integration PR**, and explicitly requested **compression of all seven images**. The authorisation does NOT include merging, deploying, replacing existing approved source masters, or editing the existing PR #5 head.
**Model (select in Work): GPT-6 Luna**.
**Thinking effort (select in Work): High**.
**Speed (select in Work): Standard**.
**DTSU v1.1:** Real Europe/London timestamp; initial 0%; ongoing brief progress percentages and numeric remaining ETA, updated honestly; report 100% only after binary checkout + browser/compression QA, accurate documentation and COPY TO CHAT handback.

## 1. Repository and branch boundaries

**Repo:** `SymTechVenturesOrg/symtechventures.github.io`.
**NEW isolated integration branch already created:** `feature/v2-paper-one-seven-cinematic-optimised-20261120`, originally forked from website implementation PR #5 head `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` (before this handover commit).
**This branch's draft PR:** see its open draft PR against `feature/v2-space-research-website`; **CONTINUE that PR**, do not create a duplicate or push to PR #5's head.
**Original website article:** `articles/symmetria/symmetria-paper-01.html`, pinned previous HTML blob `c235e33bbe3a291343125c94af73fe54a23491fa`.
**CSS:** `css/v2-articles.css`, pinned previous blob `72697a65096fcdbc8c762e86215a8ceb14d1be92`.
**Source original PNG commit:** `c6f60ee180c2f5d401b0f597f512898c010981a9` on docs archival branch.
**Corrected 2.1/3.1 PNG commit:** `ef09d41b6b7fcb85efc75618736c234ccc2fa09c` on `docs/symmetria-paper-one-science-corrections-20261120`.
**Independent science re-audit:** [exact report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/48e071e80d7842518c8ee8847fa5d187b61c262b/docs/reports/V2_PHASE_03_P1_FIGURES_2_1_3_1_INDEPENDENT_SCIENCE_REAUDIT_AND_1_1_CAPTION_DECISION_20261120.md).
**Full mapping/caption/alt-text authority:** [controlled integration plan](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/12c4f37b8f233a8f036db63ad208e1125dbc4212/docs/handovers/V2_PHASE_03_P1_WEBSITE_INTEGRATION_CONTROLLED_OWNER_GATE_20261120.md).

## 2. Seven canonical source-of-truth images — do not use obsolete 3:2 WebP imagery

Obtain image binaries by binary-capable Git checkout of the pinned GitHub source commits. **NO ZIP downloading, user re-uploading or screenshots.** Recompute actual SHA-256 and 1920×1080 RGB/RGBA decoding **before** compression.

| Slot | Immutable GitHub source path (relative to repo, pinned to relevant commit above) | Required source SHA-256 | Old website WebP basename | New asset stem |
|---|---|---|---|---|
| Cover | `docs/artwork/owner-approved/paper-one/P1_Cover_OWNER_VISUALLY_APPROVED_1920x1080.png` | `3eeba0f6bfcefd2a63b5867cad0442ac9a6d356526cc1fed31e057d3de9e95a8` | `01_unified_framework_cover.webp` | `p1_cover` |
| 1.1 | `docs/artwork/owner-approved/paper-one/P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675` | `01_historical_progression_physics.webp` | `p1_figure_1_1` |
| 2.1 | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png` | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | `01_modern_physics_challenges.webp` | `p1_figure_2_1` |
| 3.1 | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png` | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | `01_search_for_unification.webp` | `p1_figure_3_1` |
| 4.1 | `docs/artwork/owner-approved/paper-one/P1_Figure_4_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `788e68dc507c1e408428380b86816e594301384ed29331a3ab9aa9c29cdb9238` | `01_current_physics_limitations.webp` | `p1_figure_4_1` |
| 5.1 | `docs/artwork/owner-approved/paper-one/P1_Figure_5_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c` | `01_symmetria_perspective.webp` | `p1_figure_5_1` |
| 6.1 | `docs/artwork/owner-approved/paper-one/P1_Figure_6_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `a1c9c939c6195a97106a3e4c8a49398a48b27baf108a8ef7b21bdc0ed09e896f` | `01_future_research_roadmap.webp` | `p1_figure_6_1` |

These seven originals amount to **21,896,557 original compressed PNG bytes** (about 21.9 MB). **Never recompress/overwrite the original docs archive**. Install exact byte-for-byte copies of the seven original PNGs to versioned **full-resolution master assets under the new website branch**, to serve as a zoom/open original linked asset; also create separate display-optimised derivatives for all seven. The website's old WebPs stay unmodified (no disruptive replacement).

## 3. MANDATORY compression design, all seven — image quality before arbitrary byte targets

**For each of the seven selected science-reviewed images:**

1. Create a master at `images/symmetria/paper-01/approved-20261120/<stem>_master_1920x1080.png` as an EXACT copy of the selected source image. SHA-256 of website master must exactly equal table SHA-256; this is the zoom target. The docs original also remains unchanged.
2. Generate reproducible **high-quality WebP display derivatives** at widths **768, 1280, 1920** pixels, maintaining original 16:9 proportions (432, 720, 1080 px high). Suggested initial encoding quality **85–92**, calibrated after inspecting actual fine typography, Greek symbols, cyan/gold fine lines, contrast, halos and dark-space gradients. Keep specific encoder, version, settings and output SHA-256 in a report. Lossy quality is not a source identity hash; generate a manifest of derivative hashes/sizes distinct from masters.
3. **Optional** generate matching AVIF derivatives if the Work image encoder/browser can reliably produce and decode them; AVIF is NOT required if visual defects, browser test failure or excessive execution time outweigh gains. Use WebP as the standard interoperable fallback and only adopt AVIF where it genuinely improves quality/size. Do NOT rely on AVIF-only fallback.
4. Use responsive `srcset`/`sizes` or `<picture>` so a mobile viewport does not fetch the 1920px display asset unnecessarily; an HD/retina desktop may select 1920. **Only one display derivative per figure** should be fetched in a typical browser render. The cover is above the fold: avoid deferring its loading; for the six lower figures use `loading="lazy" decoding="async"`. All images need `width` and `height` to minimise layout shift and `height:auto` to preserve the composition. Never `object-fit: cover` crop text.
5. **Compare before/after:** exact RGB shape, image presentation, mathematical notation, symbol/arrow orientation, font strokes, small explanatory labels, and absence of ringing/edge halos/dark-scene colour banding. Inspect 100% pixels and representative crops at 1× and at actual desktop/mobile display scale; use quality measures (e.g. SSIM/PSNR) as *supplements*, not replacements for visible glyph inspection. If Q85 makes text blurry, increase quality or use visually lossless WebP for that image/size; if compression saves little, report it honestly rather than weakening scientific fidelity.
6. Produce **full per-image matrix** with source PNG bytes, each derivative's width, bytes, encoder/quality, SHA-256, compression percentage vs original corresponding PNG and browser transferred bytes for mobile/desktop after `srcset` selection. **Do not invent a fixed 80–90% saving.** Report actual totals for all seven selected derivatives on 320px/390px/desktop test viewports and compare with a baseline of seven original masters.
7. Expose a clear link **"Open full-resolution Figure [n]"** to the exact unchanged master. It must be keyboard/touch accessible, and its destination must show the *same scientific content/equations* as the compressed derivative. Do not point a new figure to any of the seven obsolete existing WebPs or mismatch a caption.

**Accessibility is not optional:** equations can already be illegible at ~286–356 CSS px wide **even with lossless PNG**; compression does not solve that. Keep detailed science claims and uncertainty in accessible, selectable HTML caption/long description alongside zoom. Real 320px/390px browser testing is mandatory; do not call a CSS proportional estimate a tested browser pass.

## 4. Scope of the HTML/CSS changes (seven slots only)

The website currently uses seven standalone `<img>` blocks each followed by `<p class="figure-caption">`; it does not use `.paper-figure-open` despite existing CSS rules. Replace only these seven Figure/Cover image blocks on this isolated integration branch, insert responsive WebP (`picture` AVIF optional), accurate concise alt, visible longer/accessible description and linked exact 1920×1080 master.

**Exactly three caption corrections, and tied to matching images:**

- **Figure 1.1:** KEEP canonical approved `Λ=0` PNG; append to its existing visible historical caption exactly: `The Einstein field equation shown is the special case with cosmological constant Λ = 0; the general form also contains a cosmological term.` Repeat it in the accessible longer description. The currently displayed old 1536×1024 WebP has a **+Λ term**, so this Λ=0 caption **must never be shown alongside that old WebP**. Verify the final mapped asset/equation visibly.
- **Figure 2.1:** `Quantum mechanics and general relativity are each highly successful in their respective domains, but a complete, experimentally established framework reconciling quantum principles with gravity remains an open research challenge.` Do NOT retain the categorical old `fundamentally incompatible` phrasing.
- **Figure 5.1:** `SYMMETRIA presents the following as an untested hypothesis: reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.` Its four source concept panels are **questions**. Do not repeat the incorrect re-audit image quotes `Symmetry is fundamental` or `Nilpotent balance underlies nature` (see [erratum](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/fbfdb67a3ca37e7afd0cd225a6c36c81543171c4/docs/reports/V2_PHASE_03_P1_FIGURE_5_1_REAUDIT_TEXT_ERRATUM_20261120.md)).

All other adjacent figure captions and manuscript body paragraphs remain unchanged. For accurate approved `alt` / long accessible descriptions, follow the detailed [editorial accessibility draft](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/docs/symmetria-paper-one-science-corrections-20261120/docs/artwork/candidates/paper-one/PROPOSED_CAPTIONS_AND_ACCESSIBILITY_COPY_20261120.md) with refinements in the independent re-audit.

## 5. Exact verification and report — no deployment

1. **Fresh Git checkout** on the new integration branch; record current HEAD/HTML/CSS blob and compare against the above source pins, reconciling any drift before making changes.
2. Generate and commit seven website masters (exact original PNG bytes) **plus 21 WebP derivatives** at 768/1280/1920 (and optional AVIF variants), one tightly scoped HTML edit and minimal CSS if needed. Preserve original website WebPs. Use a separate derivative manifest under `docs/reports/` with all source/master/derivative hashes, sizes and expected display-variant mapping.
3. Independently clone the resulting GitHub commit and verify **7/7 master SHA-256 exact matches**, all derivative formats/dimensions/hashes, no source PNG changes, no old WebPs deleted, and exactly seven replaced article image blocks. Check caption/asset mapping automatically and by visible full-resolution inspection.
4. Test the actual draft page using a real cloud browser at **320px, 390px, tablet and desktop** for visual stability, text legibility/zoom, keyboard tab/focus/Enter, touch interaction, accessible labels/long descriptions, broken-image handling, and network transfer bytes. Confirm 16:9 preservation and that `srcset`/`sizes` selects appropriate assets; collect screenshots, performance and requests evidence. If browser is unavailable, mark `BROWSER_QA_BLOCKED` and DO NOT claim completed acceptance.
5. Check the website build, relative URLs and any article content invariants. **No major rewriting of manuscript body**; no non-Paper-One image changes.
6. Commit `docs/reports/V2_PHASE_03_P1_SEVEN_COMPRESSED_CINEMATIC_IMAGES_DRAFT_WEBSITE_QA_20261120.md` with the full image-size matrix, verified commit SHA, caption science, accessibility and browser testing. Final `COPY TO CHAT` must say whether seven compressed display variants passed; source/master identity pass; actual total mobile/desktop bytes and compression rate; browser support; PR link; any unresolved quality/viewport issues and explicit request for owner approval.

**No merge, deploy, direct changes to PR #5 head, source docs PRs #9/#10, protected physics manuscript beyond 7 image/caption blocks, or release.** Keep this website integration as its own DRAFT PR stacked on PR #5's branch. Even a perfect compression result is not permission to publish.

## 6. Stop/partial-completion rules

If source or Work computer cannot fetch binary bytes or use a compatible image codec, stop **that part** and report the actual blocker. Do not claim all 7 compressed if they are not. If a particular figure's compressed text becomes materially unreadable at full 1920px display resolution, retain exact master and flag `IMAGE_COMPRESSION_QUALITY_BLOCKER`; do not silently substitute a corrupted science image. A PNG master is still downloadable, but failed display derivative is not production ready.

## 7. COPY TO WORK launch

Please implement **the seven Paper One cinematic figures** in the **existing new draft website-integration PR**, using this GitHub handover. **Compress ALL SEVEN for website display** as responsive high-quality WebP (AVIF optional), keeping the exact 1920×1080 owner-approved/science-reviewed PNG masters unchanged for full-resolution viewing. Include scientifically matched figure captions, accessible descriptions, real 320px/390px/desktop browser checks and verified GitHub binary size/hash evidence. Use DTSU v1.1; do not touch website PR #5's source branch, merge or deploy. Finish with a complete QA report and COPY TO CHAT.