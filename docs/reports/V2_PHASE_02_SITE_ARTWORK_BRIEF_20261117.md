# SymTech Ventures v2.0 — Phase 2 Website Image Design Brief

**Date:** 17 November 2026 (GMT)  
**Status:** **Phase 2 open, single homepage pilot authorised by sequence; no asset accepted or integrated yet**  
**Parent:** [Owner-approved phased workplan](../V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md)  
**Implementation:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), `feature/v2-space-research-website`

## 1. Why Phase 2 starts

The owner explicitly said **“Approved. Continue. 😄”** following Phase 1C visual inspection. Therefore the existing responsive layout (not a redesign) is accepted for moving to artwork selection. The [actual Phase 1C browser report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_PHASE_01C_INTRO_TYPOGRAPHY_QA_20261117.md) confirmed full regression exit **0**, including the full-width lead and mobile 16px type. **The owner has not yet approved any specific new artwork**.

## 2. Approved design system and exclusions

- Brand: **SymTech Ventures**, independent exploratory research motivated by space exploration, mathematics and fundamental physics.
- Visuals: restrained midnight navy/near-black background, cool cyan-blue and restrained warm gold accents; scientific elegance, physically plausible cosmic imagery **without suggesting actual spacecraft, experiments or confirmed new theory**.
- **No animated or site-wide starfield background.** Static stars and restrained galactic texture are welcome **inside space illustrations**. Avoid artificial UI dots, excessive glow, sci-fi interface labels, embedded AI-generated equations or text, NASA badges/crests, watermarks, logos of other institutions, and claims that conceptual imagery depicts real photographs or existing missions.
- Preserve all existing technical structure: current Home responsive two-column hero / mobile stack, accessible nav, status notes, and the four Rowlands-inspired reference-free SYMMETRIA discussion papers.
- Use genuine AI-generated conceptual artwork with **owner-confirmed provenance**; the *composition* may evoke an Earthrise from a lunar-orbital perspective, but **do not reproduce a specific historic Apollo/NASA Earthrise photograph or imply documentary authenticity**.

## 3. Home hero — pilot #1

**Location:** `index.html`, the existing right-hand hero art container `.orbit-wrap`, currently housing an approved **inline orbital SVG**. This SVG **must remain in place** until a separately approved image integration pass.

**Concept:** **Earthrise / planetary horizon as a metaphor for scientific exploration**, with a richly shaded curved lunar or cratered rocky foreground, a luminous physically believable Earth rising above its edge, expansive near-black/navy cosmic negative space with **optional static stars or a restrained Milky Way texture**, controlled cyan atmosphere and one subtle amber light on the horizon, depth and editorial calm. Should feel like **original fine-art science illustration**, not stock astrophotography or a movie poster.

**Composition requirements:** main planet/horizon centred toward the right half of frame, subject and interesting luminosity away from all edges for responsive `contain` or modest crop; allow quiet dark negative space around silhouette; no captions/text. Preview at landscape **approximately 1.45–1.50:1**, e.g. a source 1536×1024 leading to a tested **716×494 px** WebP variant if visually appropriate. The existing SVG region is near-square, so **do not assume a 716×494 replacement can be inserted without a small owner-reviewed fit rule**; check real 390 and 1440px placement before integration.

**Deliverables from a Chat-led pilot:**
- One original rendered source image and one review variant of the **same pilot** exported as **WebP quality value 80** (this is *not* a guaranteed 80% reduction in size), with actual dimensions and file size.
- Descriptive provenance record, meaning/visual intent, safe neutral alt-text candidate (“Conceptual illustration of Earth rising above a dark planetary horizon”) and evidence no baked-in scientific claims.
- **Pilot must be visually approved by owner before image binary is committed for live site use or replaces the orbit SVG.** Keep a rollback option.
- Codex **Luna / Medium / Standard** for deterministic image conversion/integration and browser/axe/full regression later, not for deciding physics or aesthetic taste.

## 4. Other possible site-level images — NOT commissioned yet

| Slot | Current position | Candidate art | Status |
| --- | --- | --- | --- |
| **Research introduction** | Current text-led content | One restrained theoretical research geometry visual, no equations or labels | **Optional — owner to decide only after Home pilot** |
| **BridgePoint introduction** | Structured Planned 16-lesson overview | One approachable abstract geometry and light educational motif | **Optional — owner to decide only after Home pilot** |
| **NSRP / SEIP** | Existing 5×4 Planned cards | Retain text/card clarity; avoid imagery implying functioning spacecraft | **No new image assumed** |
| **Publications / About / Contact** | Empty-state/info/status pages | None required by default | **No image planned** |
| **Six shared logos / twelve historical images** | Existing AI art | Keep until a specific improvement is justified | **No blanket replacement** |
| **Four SYMMETRIA discussion papers** | Existing 28 illustrations | Three targeted scientific corrections + placement/caption changes | **Phase 3, not Phase 2** |

## 5. Approval, quality and implementation gates

1. Chat proposes a single home pilot (not a batch of 46). Owner decides accept, refine or reject.
2. If accepted, Codex integrates an **approved** WebP quality-80 asset in the existing layout with an appropriate aspect/crop and unchanged original SVG available for rollback; verify alt text and that image is decorative/non-essential relative to visible copy.
3. Check at 320/390/768/1440px; ensure no horizontal overflow, acceptable load/byte budget, dark border-free integration, no obscured CTA, no new keyboard traps or false content.
4. After any HTML/CSS/asset changes run **full exact-branch regression**, screenshot before/after and focused accessibility checks where necessary. Update provenance/size inventory.
5. The owner separately decides whether Research/BridgePoint slots are worthwhile; completion of one Home asset does **not** automatically authorise all other images.

**PR #5 remains draft and unmerged. No live deployment, release, document citation requirement or scientific-paper modification is authorised by this brief.**

## 6. Owner design clarification and selected visual direction — 17 November 2026

The owner clarified: **“I think the first image was closest to what I wanted. Don't worry about including stars in the images, we're a space focused company after all. The starfield animation was what we decided to ditch.”** The exclusion applies to **animated starfield backgrounds**, **not** stars within static imagery. The first generated full-width Earthrise *website mock-up* is now the **preferred artistic reference**, not an approved final website implementation or source for embedded web copy.

A non-destructive **art-only review crop** of that first AI-generated visual has been produced locally in Chat: source frame 1672 × 941 px, cropped at (810,185)-(1672,767) to a clean text-free **862 × 582 PNG (872,124 bytes)** and resized to a **716 × 484 WebP (65,914 bytes, encoder quality 80, method 6)**. The crop depicts a luminous conceptual Earthrise, cratered rocky lunar foreground, a static starfield, cyan rim and warm amber horizon glow. This is an **AI-generated conceptual illustration**, not documentary astrophotography; rendered surface detail and city lights should not be treated as empirical data. Neutral alt text proposal: **“Conceptual illustration of Earth rising above a cratered lunar landscape under a starry sky.”**

The user has expressed a **visual preference**, not yet an explicit decision to replace the approved `.orbit-wrap` SVG. The image remains a **review candidate**; the Chat-local PNG/WebP files are not stored in GitHub. The website must not link to transient Chat assets. If individually approved, use a separate engineering pass to store the binary via a supported path, integrate it in the approved two-column layout (without baking headers or buttons into the art), and run 320/390/768/1440px QA and the entire exact-branch regression before requesting any merge approval. Static artwork needs no animation or parallax.
