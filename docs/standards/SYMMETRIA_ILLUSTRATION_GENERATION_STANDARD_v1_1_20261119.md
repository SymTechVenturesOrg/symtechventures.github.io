# SYMMETRIA — Illustration generation and provenance standard (v1.1)

**Date:** 19 November 2026 · **Owner style amendment (14:47 GMT):** no paper/figure numbering within artwork; titles are subject-only. **Revision:** v1.1 — approved move from 3:2 (1536×1024) to 16:9 Full HD (1920×1080). Previous v1.0 remains in Git history. · **Scope:** all 28 figures of the first four SYMMETRIA discussion papers and future series illustrations.  
**Status:** **OWNER-APPROVED FULL HD (1920×1080) OUTPUT STANDARD, PENDING MASTER-STYLE PILOT APPROVAL; NOT AN ASSERTION ABOUT HOW THE ORIGINALS WERE CREATED.** The owner requested a single visually consistent image-generation approach and a reusable GitHub record. No production figure has yet been overwritten under this standard.

## 1. The two meanings of consistency

**Visual consistency:** same approved reference image, unified editorial palette/layout/typography, a stable prompt prefix and repeated QC across the series. **Tool consistency:** use ChatGPT's integrated **image-generation tool** (the image_gen interface) for the base artwork of every figure. These are related but **not equivalent**; identical tool calls do not guarantee identical style.

**Critical reproducibility caveat:** the interface may not expose an immutable underlying model build, random seed, sampling parameters or other internal inference settings. **Do not use text generated inside an image as evidence of tool metadata**: AI imagery can invent names such as model/version, seeds, timestamps, completion percentages or ETAs. Only externally verified tool-returned metadata and source file measurements qualify as provenance. Do not guess or falsely claim exact pixel reproducibility or a guaranteed unchanged engine months later. If the service/version evolves, create a new standard revision (v2), compare against the golden master and require owner approval before applying the new version to an entire series.

**Historical originals:** their generating tool, model, prompts, seeds and licence provenance **cannot be conclusively reconstructed** from GitHub. Record `historical_engine=unknown`, retain original bytes and Git blob hashes. Do not imply the proposed standard was retrospectively used for the old images. The five earlier Batch A/C2 flat SVG-only prototypes used a different **Python/SVG/CairoSVG/Pillow workflow**, and are **rejected for stylistic inconsistency**. Recent Chat-generated raster experiments are **draft references**, not a frozen approved style or published images.

## 2. Source-derived visual identity

The owner-approved look to reproduce is the existing original 28-image family, **not the flatter SVG-only prototypes**. Reference priorities:
- `images/symmetria/paper-02/02_noether_symmetry_conservation.webp` — dark, carefully staged scientific panels, gold serif headings, blue cosmic highlights.
- `images/symmetria/paper-03/03_dirac_nilpotent_structure.webp` — vivid abstract algebra/physics geometry, coherent columns, violet/cyan/gold light.
- `images/symmetria/paper-01/01_search_for_unification.webp` — rich subject-matched scientific diagrams and a dense but ordered information hierarchy.
- Other original images may be used as **subject references only**; always correct content problems identified by the scientific audit.

**Aesthetic invariants**: landscape 16:9 composition (final exported 1920×1080); strong dark midnight-blue/near-black base; restrained but rich cyan/blue/violet/gold light; editorial serif headings with legible supporting text; fine outlined boxes only where useful; sophisticated physics-specific visualisations; subtle cosmic/space depth, stars/galaxies where relevant, **not** a generic identical starfield pasted behind every figure. Preserve purpose, not generic decoration. Avoid flat PowerPoint-style panels, noisy neon or excessive long paragraphs inside raster images.

**Mandatory artwork-title rule (owner amendment, 19 November 2026):** **Never place “Figure x.x”, “Fig. x.x”, “Discussion Paper x”, a paper number, a figure number, or equivalent series numbering anywhere inside the image pixels** — not in the masthead, title, subtitle, badge, diagram or footer. The in-artwork heading is **the subject title only** (e.g., “Foundations of Modern Physics”); a plain “SYMMETRIA” wordmark is permitted if aesthetically appropriate, with no paper/figure qualifier. **Only the HTML page and its external caption display “Discussion Paper n” and “Figure n.n”.** Do not inadvertently render numeric figure IDs as decoration. Treat any generated image containing these forbidden in-artwork labels as **REVISION REQUIRED**, even if its scientific content and style are otherwise correct.

## 3. Master style workflow — use for every figure

1. **Freeze one golden-master image after owner visual acceptance.** Record its local filename and SHA-256 and keep it on GitHub with the versioned design specification. Do not start regenerating 28 finals before this sign-off. First pilot: Paper 1 Figure 3.1; it represents a dense scientific composition and already has a known Standard Model wording correction.
2. For each figure, prepare a **source-grounded brief** from the exact current HTML paragraph/caption, the relevant earlier WebP, Work's audit and the Phase 3 approved scientific wording. Paper 3 image-topic source references must reflect the owner-approved **1.1↔3.1 and 5.1↔6.1 swaps**.
3. **Artwork method:** call ChatGPT built-in `image_gen.text2im` to create the **entire visually rich image base** using the master style reference, the same shared style prefix and the figure-specific brief. One intended figure per output. Request a **16:9 canvas** and, where the generator supports it, **1920×1080**. Use a *static, opaque* image; no animation or transparent background. **The generator may return a different pixel count.** Record native dimensions. Export the final master to **1920×1080** at 16:9 without distorting the content; crop with composition review or extend the artwork as necessary. Never stretch a 3:2 image to 16:9 or claim native 1920×1080 when it was resampled.
4. **Maths/text rule:** generative renderings are NOT guaranteed to spell equations or scientific labels correctly. Verify *every* letter/symbol/panel, not just the visual impression. Prefer sparse in-image text plus the exact article caption. Where necessary, use a **small deterministic typography/compositing pass** to replace/correct text over the generated artwork; retain the image-generated aesthetic rather than recreating the entire picture with SVG shapes. Record text/equations and the source of every repaired label. Never treat an AI-drawn physical illustration as experimental evidence.
5. **Output:** freeze an immutable reviewed master PNG at **1920×1080** then export archival WebP at **quality 85** as a proposed common target (lossy encoder setting, not an accuracy or compression percentage); verify **1920×1080**, 16:9 aspect, sRGB, original full-size image readability, file SHA-256, byte size, and versioned naming `pNN_cover_illustration_v3.webp` / `pNN_fig_S_1_illustration_v3.webp`.
6. **Record a manifest for each figure**, using [the per-image template](SYMMETRIA_IMAGE_PROVENANCE_TEMPLATE.json), with original/ref source blob hashes, human prompt, style-master reference/hash, invoked parameters, actual generator ID (if exposed), tool limitations, all correction passes, exact equations, final output hash, scientific/editorial review and owner approval.
7. **Verification before use:** ask owner to accept the master style, then complete each paper sequentially (**7 at a time**) with comparison sheet, cross-paper consistency review, visual source checks and scientific/accessible text QA. Test at full size and website fit/mobile; check the independent viewer's click/tap/keyboard, wheel zoom, pan, pinch, original-image link and landscape display. Update the strict protected-paper regression only with an **explicit owner-accepted exact difference list**; never disable original integrity checks. Four paper URLs and 7 images per paper remain.

## 4. Stable master prompt prefix (copy verbatim into every future figure brief)

> Create one original, premium, editorial scientific illustration for the SYMMETRIA discussion-paper series, in the *specific visual language of the attached approved master reference*. Landscape 16:9, rich midnight navy and near-black cosmic depth, sophisticated glowing cyan/blue/violet/gold physical structures, elegant serif hierarchy, polished legible fine detail, well-ordered subject-specific information panels, subtle observational-science atmosphere. Maintain the same typography treatment, visual density, glow intensity and colour relationships as the approved master. Science-first and aesthetically coherent: depict the specified topic rather than generic space scenery. Do not invent mathematical identities, experimental results, equations, numbers or technical jargon; do not present conjecture as fact. Keep in-image words brief, exact and readable; NEVER print a figure number, 'Figure x.x', 'Fig. x.x', 'Discussion Paper x', or any paper/figure numbering anywhere in the artwork; use a subject-only title, optionally preceded by the plain SYMMETRIA wordmark; reserve space for subsequent controlled typesetting where mathematical detail is required. Do not copy illegible decorative formulae from historical images. No commercial watermarks, third-party logos or misleading laboratory photographs.

Append per-image:
- **Paper and canonical figure slot:** PNN Cover / Fig N.1.
- **Established fact / specified algebra / hypothesis:** distinguish clearly, with exact allowed scientific claims.
- **Subject and composition:** 2–5 visual elements from the real caption and a factual source brief; say what should be eliminated/changed from the old picture.
- **Exact labels/equations to check manually:** itemise; do not infer mathematically invalid arrows. If labels are longer than a few words, prefer later controlled text overlay.
- **Composition constraints:** panel arrangement, illustrative subject, generous legibility, full-width cropping/safe margins, and consistency with master.
- **Failure negatives:** forbidden false statements, ambiguous claims and misleading decorative equations; **any 'Figure x.x' or 'Discussion Paper x' or equivalent numbering printed within the image**. **16:9 composition constraint:** reserve breathing room at the sides, keep all essential lettering inside a central safe area for narrow mobile display, and avoid thin scientific lettering that becomes unreadable on a phone at fit-to-width. Do not stretch old 3:2 source illustrations.
- **Original and approved style reference SHA:** record for provenance and owner comparison.

## 5. Invocation settings and limits

| Field | Standard planned value | Truth/limitation |
| --- | --- | --- |
| Generator | ChatGPT built-in image generator, `image_gen.text2im` | Record generation date and exposed generation ID; underlying stable engine identifier may not be available |
| Number of requested final images | One figure per independent generation/revision | Avoid batch ambiguity, especially when every figure has unique science |
| Requested canvas | Landscape **16:9**, target output **1920×1080** | Record ACTUAL native image-generation output dimensions; 1920×1080 is the accepted final export target, not a guarantee of native model output |
| Transparency | `false` | Dark opaque base |
| Animation | disabled / not requested | Static figure |
| Source image | Original figure as *content* reference + owner-approved master as *style* reference | Do not reproduce known inaccurate embedded equations verbatim |
| `is_style_transfer` | `true` when intentionally transforming an image reference | Depends on the individual request; log the actual call |
| Prompt and engine model version | Full human-authored figure brief stored; underlying tool prompt/model build/seed if not exposed marked **unavailable** | **No guarantee of identical pixels from the same prompt** |
| Final export | WebP, **quality 85**, sRGB, dimensions 1920×1080 | This is a newly proposed setting; old files are not assumed to have used it |
| Names | Versioned `pNN_*_illustration_v3.webp` | Originals never overwritten; suffix increments for a future standard |
| Scientific integrity | Work+Chat 28-figure audit and current owner-approved scope | Each rendered label/math verified explicitly |
| Public paper status | Reference-free exploratory discussion, not peer reviewed | No claim of scientific or experimental validation |
| Release | PR #5 draft, original figures retained, owner accepts every visual batch | Nothing merged or deployed without a separate release instruction |

## 6. Project rollout

**Gate 0: master pilot**: regenerate only P1 Fig 3.1 using the accepted source style; inspect original/new side by side and sign off the *look*, independently of technical text correctness. Rework until the look genuinely matches the original family.

**Gate 1: Paper 1 (seven)**: original content intent maintained; known Fig 3.1 (Standard Model) and Fig 5.1 (nilpotence/anticommutation) issues corrected inside the images.

**Gate 2: Paper 2 (seven)**: Fig 4.1 Noether/P/T corrections, Fig 5.1 originally deferred under the old limited-scope plan must now be **redesigned because the owner explicitly wants all 28 regenerated**; depict real broken symmetry, not generic symmetry. Align Figs 1.1–3.1 with their actual sections, not existing mismatched artworks.

**Gate 3: Paper 3 (seven)**: honor approved subject placements (1.1↔3.1 and 5.1↔6.1), correct Fig 4.1 Dirac correspondence, remove decorative mathematical pseudo-notation.

**Gate 4: Paper 4 (seven)**: design Fig 4.1 around scientific testing rather than a general cosmic research map; other figures reflect their true caption topics, qualifiers and evidence status.

**Gate 5: final site integration** only after proof approvals: versioned files on **draft** PR #5, updated alt/captions where authorised, exact-delta protected baseline, full GitHub browser QA, mobile and full-size viewer QA, 28-asset manifest reconciliation. Keep 7 slots per paper and all four URLs; no merge or deployment.

## 7. Desktop and mobile acceptance for the new 16:9 masters

**Desktop:** validate the exported figure as a 1920×1080 image, without requiring browser zoom beyond 100% to fit the page; check the dedicated image viewer at Fit, 100%, mouse-wheel zoom and pan. The browser viewport may have different proportions from the source image; natural empty bands are fine and must not be replaced by stretched pixels.

**Mobile:** maintain responsive width and the existing separately opened pinch-to-zoom viewer; check 390px portrait and 844px landscape. At portrait fit-to-width, a 16:9 figure may be short and internal text very small. This is a real usability trade-off: verify key concepts are understood from the HTML figure caption, and that full details are readable via the dedicated viewer and phone rotation. Consider additional accessible HTML explanations for important formulae, rather than cramming the image with tiny text.

**Market rationale:** in StatCounter desktop-resolution statistics for October 2026, 1920×1080 was the largest individual desktop category (approximately 36.8% UK, 27.8% worldwide), **not a majority of all devices**. Source: https://gs.statcounter.com/screen-resolution-stats/desktop/united-kingdom and https://gs.statcounter.com/screen-resolution-stats/desktop/worldwide . Image export dimensions are not a claim the site's visitors share that screen resolution.

## 8. Future-paper use

For a fifth or later paper, copy the same master prompt and style hash, figure manifest and scientific QA checklist; use a **new figure-specific brief for each distinct subject**. If the image model or artistic output noticeably changes, create `v2` of this standard, generate a fresh pilot, and require owner sign-off before claiming series consistency.

**Principle:** document what was actually done, separately from what was intended. Repeated generator choice is a useful standard; a master reference, precise science, reliable provenance and independent visual acceptance are what make the final series coherent.
