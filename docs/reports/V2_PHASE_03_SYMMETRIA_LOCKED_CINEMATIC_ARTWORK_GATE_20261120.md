# SYMMETRIA — Locked Cinematic AI-Illustration Style and Acceptance Gate

**Owner decision recorded:** 20 November 2026, Europe/London.  
**Status:** **BINDING FOR ALL NEW OR REVISED SYMMETRIA DISCUSSION-PAPER FIGURES**. This document amends and clarifies the [28-figure production standard](V2_PHASE_03_SYMMETRIA_FIGURE_PRODUCTION_STANDARD_20261120.md). No approval to alter existing website assets, merge a PR or deploy.

## Why this exists — failure and replacement rule

The owner rejected repeated batches of figures produced as **programmatically assembled technical diagrams with AI artwork used as a backdrop**, despite some passing mathematical and pixel QA. The owner approved a different visual result: the **rich, fully AI-generated, cinematic physics-infographic appearance originally shown in Papers One and Two**, subsequently carried into the accepted visual direction of Papers Three and Four. These are NOT interchangeable visual styles. A file that is dimensionally compliant, has a beautiful decorative background or is factually corrected **still fails if it looks like a flat slide/constructed chart rather than the approved cinematic science artwork**.

The previous `SYMMETRIA_28_Figure_Complete_Candidate_Reaudit_Package.zip` and its associated 20 November final candidate re-audit handover are **WITHDRAWN / SUPERSEDED FOR VISUAL ACCEPTANCE AND INTEGRATION**. The handover file is not present in this branch snapshot, so no broken relative link is retained. Do not present that package as owner-approved, use it as the master to integrate or send it for the proposed acceptance re-audit. It is retained only as historical QA/correction evidence. Independently re-use individual scientifically valid explanations only after regenerating a genuinely style-matched illustration and checking it again.

## Visual reference — primary authority

The two original *owner-accepted* illustrated sets for SYMMETRIA Papers **One and Two** are the visual style authority. Their defining qualities:

1. **Native AI-generated cinematic artwork dominates the entire composition.** Rich, believable, luminous 3D physical geometry (field meshes, curved surfaces, topological forms, particle/spacetime conceptual diagrams, waves) is tightly integrated with the explanations. No flat stacked rectangles posing as finished illustrations.
2. **Midnight navy to deep-black scientific atmosphere**, restrained cosmic/technical texture, glowing cyan/blue and warm gold/amber, sophisticated volume/light, strong contrast.
3. **Elegant prominent gold serif-style scientific subject title**, meaningful explanatory subtitle, concise legible callouts, precise labels and an optional compact take-away strip. Text is a real explanatory layer, not meaningless filler.
4. **One scientifically specific visual story per section**, not seven-up posters, generic multi-topic montages, dashboard/status layouts, pictorial summaries or reused unrelated physics decoration. The main graphic should materially **explain the scientific idea**, not merely evoke “science”.
5. **No scientist portraits**, and no image-internal “Discussion Paper X”, “Paper Three”, “Figure x.x”, figure number, or website caption. Those identifiers go **in surrounding HTML**.
6. The aesthetic must be recognisably the **same design family** across Papers One–Four. Paper Three/Four controlled-diagram sets are **rejected as style masters**.

### Required canonical reference images

Before any generation, open or provide **at least two original owner-approved Paper One/Two full-resolution illustrations** as visual reference files. Record their filenames, provenance, source hash and the specific qualities to match in the figure manifest. **Do not treat a rejected contact sheet, programming-rendered image or later correction draft as the style reference.**

If the original accepted reference images or the matching AI image-generation capability are unavailable, **mark STYLE ANCHOR BLOCKED and request/source the actual references**; never quietly substitute an unrelated generator or scripted poster creator and describe its results as “same style”. The three original references are now present in [draft PR #7 at immutable commit 01430576f5643442f715e0bdfcd6433ddbcee1f4](https://github.com/SymTechVenturesOrg/symtechventures.github.io/tree/01430576f5643442f715e0bdfcd6433ddbcee1f4/docs/artwork/style-reference/), with direct GitHub-byte SHA-256 verification recorded in its manifest. This staged documentation asset does not imply a merge or any image-generation approval.

## Approved production technique and prohibitions

**Primary method:** Generate each image using the native AI image-generation capability that produces the owner-approved cinematic science illustrations; where supported, supply the actual approved style reference images to the generator as visual references. Produce **one independently usable full-canvas visual per slot**. Do not create a seven-panel grid and crop/upscale its tiny tiles to impersonate separate full-resolution figures.

**Not an acceptable replacement technique:** SVG/HTML/Canvas/Pillow/Matplotlib or other programmatic assembly used to design the full image from flat boxes/arrows/text, regardless of mathematically accurate labels. Do not solve a style-mismatch by layering a scripted infographic over a stock/AI space scene. No silent substitution to a different generator merely because a tool returned an invalid montage.

**Allowed restrained finishing:** lossless conversion, proportion-preserving canvas extension/recomposition, a technically necessary 1920×1080 export, checking dimensions/hashes, and **localised repairs of verified mathematical glyphs and small labels**. These must not replace the original AI composition with a new predominantly programmatic layout. If a major title, diagram, panel arrangement or scientific narrative needs changing, **regenerate the entire figure in the correct native AI style**, then re-check mathematics and visual fidelity.

**Generator failure:** Reject inappropriate composite outputs, collages, wrong paper/topic, status dashboards, illegible fake text and invented formulas immediately; do not include them in approved counts. Report the blocking mismatch; retry the **individual named slot** using locked style anchors. After repeat failures, stop and document the blocker rather than fabricate a pass.

## Pixel and text requirements — still mandatory

- Each output **exactly 1920 × 1080 pixels**, **16:9 landscape**, one full-size PNG master per image (approved WebP derivative may follow). Programmatically inspect pixels **after** export. A generator’s “16:9” claim or 1672×941 file does not pass.
- No stretching, crop of explanatory text, tiny cropped contact-sheet panels or fake extra detail from simple upscaling. If native resolution is smaller, a high-quality faithful finishing process may achieve pixel compliance, but record the **native dimension and enhancement method**; dimensional compliance does NOT imply genuine 1920×1080 detail.
- Short, legible English explanations, a substantive scientific title and accurate notation; no embedded paper/figure identifiers. External captions remain editable/accessibly rendered in the website.
- The actual article HTML section/caption is the source of content truth; the separate Unified Field Framework manuscript is not a substitute for online Paper One.

## Two completely separate acceptance gates

**A. SCIENCE/EDITORIAL (independent):** every scientific claim, equation, arrow, conditional inference, intended analogy, and figure-to-section mapping must be reviewed. Distinguish standard established physics, Rowlands-specific mathematical proposals, and speculative SYMMETRIA interpretation; no fake measured data or unproved consequence.

**B. CINEMATIC STYLE (owner):** compare the proposed individual image side by side with **two original approved Paper One/Two reference images**. The owner must explicitly judge it a genuine match in 3D illustration richness, light/colour, integrated diagrams, typography, hierarchy and readability. A scientifically perfect *but flat/scripted* image is **STYLE FAIL**. No model self-certification or “closest available” substitutions count as owner approval.

A candidate only advances when: (1) actual standalone 1920×1080 geometry passes; (2) factual/math QA passes; (3) **owner visual style approval** is expressly recorded **for that image**. Subsequent independent re-audit and mobile/browser integration QA are distinct later gates. Missing owner sign-off means **AWAITING OWNER**, not “PASS”.

## Required per-image manifest

Maintain: paper / cover-or-figure-slot; exact section and external caption text; native generation mode/tool; original reference image filenames and hashes; generated native dimensions; final dimensions; file SHA-256; scientific QA status; cinematic style QA status; owner verdict/date; remaining issues; postprocessing provenance; website URL/asset path only after integration permission.

### Stop conditions

- **STOP:** no original accepted visual anchors or cannot match style.
- **STOP:** generator produces a collage/status dashboard/another paper/topic.
- **STOP:** wrong dimensions or misleading mathematical/physical claim.
- **STOP:** no explicit owner visual approval. Do not hand off for integration.
- **STOP:** changes attempted to website PR, main, original image assets, or deployment without a fresh authorised implementation handover.

## Application to ongoing work

1. Withdraw the earlier full 28-figure candidate package from any pending “ready to integrate” status.
2. Rebuild the unsatisfactory artwork **from the proper AI-native full-canvas style**, starting with one Paper One cover as a *style checkpoint*, then one figure at a time. No auto-approval of prior controlled-diagram rounds.
3. Keep the scientific correction register as a **content risk checklist**, not an instruction to use its rejected artwork.
4. After owner agrees the style checkpoint, proceed in batches; independent scientific recheck and owner image-by-image acceptance precede a new, separate read-only Work audit and later limited implementation.
5. For **every future Work handover**, separately state **Model**, **Thinking effort**, and **Execution speed**, for the owner to select **before starting Work**. Suggested default for bounded documentation/verification: **Model: GPT-6 Luna (Work); Effort: Medium; Speed: Standard**. For a technically demanding 28-figure scientific audit: **Model: GPT-6 Luna (Work); Effort: High; Speed: Standard**. **Work cannot set or change these controls itself**; never put the configuration responsibility on Work. No merge or deployment without new owner instruction.

**Summary: the visual production method, the target appearance, and owner style approval are hard gates—not optional preferences.**
