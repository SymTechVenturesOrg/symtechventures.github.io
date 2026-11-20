# SYMMETRIA Discussion Papers — Owner-Approved Figure Production Standard

**Decision date:** 20 November 2026 (Europe/London)  
**Status:** MANDATORY FOR NEW PAPER ARTWORK; NOT PUBLICATION OR SCIENTIFIC APPROVAL  
**Applies to:** four online SYMMETRIA discussion papers; seven image slots per paper (cover plus Figures 1.1–6.1), **28 total**.  
**Authority:** subsequent explicit owner decisions during Chat visual review on 20 November 2026. These supersede earlier dimensions, number/title placement, and selective-only commissioning assumptions *for preparation of new review candidates*. They do **not** authorise website integration, merging, deployment, or the removal of originals.  
**Source of truth for figure subjects and captions:** the live **source HTML on the specific implementation baseline being reviewed**; filenames and drafts are not sufficient.  
**Related:** [Locked Cinematic AI-Illustration Style and Acceptance Gate](V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md); [canonical style-reference registry](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/01430576f5643442f715e0bdfcd6433ddbcee1f4/docs/artwork/style-reference/README.md) at verified draft PR #7. The earlier phased workplan and 28-figure review documents are not present in this branch snapshot, so they are not linked here.

## 1. Non-negotiable output geometry

- Every *final review master* must be **exactly 1920 × 1080 pixels**, **16:9 landscape**. Neither “approximately 16:9” nor 1672 × 941, 1536 × 1024, 1600 × 900, or a contact-sheet tile passes. Final website WebP derivatives must preserve exactly **1920 × 1080** unless the owner explicitly revises this standard in a subsequent recorded decision.
- Keep one **independent, full-canvas image per figure**; no grouped contact sheets as replacements. Contact sheets are optional **review aids only**, not deliverable figure binaries.
- If an image generator produces a different size or aspect ratio, **do not assert that it complies**. Recompose with appropriate crop/extension, preserving all information and geometry, then export at the required size and *measure the resulting pixel dimensions*. Do not stretch a 3:2 composition into 16:9 or crop explanatory text.
- Generate/retain a full-resolution lossless master (PNG suitable) and, after approval, a WebP derivative at encoder quality 80 (or documented higher-quality exception if needed for formulas). Check the derivative again for dimensions and text clarity; encoder quality 80 is not a claim about percentage file-size reduction.
- Any figure failing dimensions, legibility, geometry or scientific checks is **DRAFT / REWORK**, not approved.

## 2A. Mandatory AI-native cinematic illustration method and separate owner style gate (20 November 2026 override)

**New owner decision — takes precedence over generic “diagrams / post-processing” language below:** use the owner-approved **fully AI-generated, rich cinematic scientific infographic style** of the original Papers One and Two. **Do not** substitute programmatically constructed flat diagrams/posters with AI decorations, even when 1920×1080, mathematically corrected, and coloured navy/cyan/gold. Avoid inadvertent generator changes; use the original approved visual references recorded in the [PR #7 registry](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/01430576f5643442f715e0bdfcd6433ddbcee1f4/docs/artwork/style-reference/README.md), or stop if the actual references/generation capability are not available. Generate **one standalone image for each exact figure slot**; reject combined montages, generic science collages, and project-status dashboards. Localised corrections to mathematical glyphs and dimension export are permitted **only if the image remains visually AI-native rather than a scripted reconstruction**. Have the owner explicitly approve **visual/style fidelity separately from scientific accuracy** before release or Work integration; no batch self-certification.

**Authoritative detailed rule, failure history, pass/fail gates, manifest and next steps:** [Locked Cinematic AI-Illustration Style and Acceptance Gate](V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md).

**WITHDRAWN visual candidate package:** `SYMMETRIA_28_Figure_Complete_Candidate_Reaudit_Package.zip`. Its associated 20 November final 28-candidate re-audit handover is **SUPERSEDED**, not a live permission to proceed. The original owner-approved visual anchors and hashes are now recorded and direct-binary-verified in [draft PR #7 at immutable commit 01430576f5643442f715e0bdfcd6433ddbcee1f4](https://github.com/SymTechVenturesOrg/symtechventures.github.io/tree/01430576f5643442f715e0bdfcd6433ddbcee1f4/docs/artwork/style-reference/). This documentation link does not authorise merging PR #7 or starting image generation. The scientific audit findings remain useful as a content QA checklist.

## 2. Locked image style

Use the visual aesthetic approved by the owner for Paper One and subsequently Paper Two:

- Midnight navy / near-black science-space background; fine technical/cosmic textures; controlled electric cyan/blue and warm gold highlights; glowing but readable 3-D scientific geometry and diagrams.
- Prominent **scientific subject title** at top; useful one-line explanatory subtitle; substantive diagram labels, short explanatory annotations/panels, where appropriate an easy-to-follow bottom summary or progression band.
- Strong hierarchy, generous safe margins, consistent panel outlines and gold serif-style major headings; clear, readable body labels (do not rely on tiny generator-written glyphs).
- The physics, mathematical relationships and their explanatory value are the centre of every composition; no scientist portraits, celebrity likenesses or decorative human figures.
- No generic science collage, automatically generated grid of seven figures, unrelated technical applications or arbitrary space-technology imagery. Each illustration must be independently specific to the figure’s *exact* adjacent section and caption.
- The desired aesthetic is not a licence for decorative fake equations, invented quantitative results, unnecessary UI furniture, or misrepresentations of an actual apparatus or experiment.

## 3. Embedded text and figure-identification policy — important

**Inside the artwork, include:**
- A clear, meaningful topic title, e.g. “The Nilpotent Foundation”, “Noether’s Theorem and Conservation Laws”, “The Meaning of Zero”.
- A concise subtitle, explanatory captions *within the diagram*, scientific labels and verified equations where they materially explain the section.
- Where needed, explicit distinctions such as “Established physics”, “Proposed interpretation”, and “Exploratory SYMMETRIA hypothesis”.

**Inside the artwork, NEVER include:**
- **No project or series branding as an image title/masthead:** do not put “SYMMETRIA” above, before or alongside the scientific subject title; no “SYMMETRIA — PAPER ONE”, “Paper One”, “Discussion Paper One/Two/Three/Four”, “Discussion Paper X”, “Paper 3”, “Paper Three”, any other paper sequence number/name, “Figure 4.1”, “Figure x.x”, “Figure Three”, numbered figure badges or other HTML-identification metadata. These belong **only in the website chrome and external caption**. A scientifically necessary mention of the SYMMETRIA *hypothesis* in a diagram label (not masthead) may appear only where required by the actual article text.
- **Paper One cover title must be exactly “Why Physics Still Needs a Unified Framework”.** No additional “SYMMETRIA” nameplate, “PAPER ONE” banner, project logo or series heading anywhere in that cover illustration. Check the top edge and every label at full resolution before presenting a draft.
- The website’s external caption line; a second unrelated title; scientist portraits; fake claims of publication, peer review, results or validation.

**Outside the artwork:** preserve each existing paper/figure identity and its caption in accessible HTML immediately beneath the image. The visible main title **is** allowed in the picture; the paper number and figure number belong only to the document/page chrome and external caption. Alt text should describe what the actual figure explains, not merely repeat a filename.

## 4. Scientific/editorial safeguards (mandatory on each image)

1. Read the exact heading, relevant section prose and adjacent caption in that paper's implementation HTML. Identify what is **established**, a **particular proposed algebraic formulation**, and **SYMMETRIA conjecture**. Frame hypotheses as questions/possibilities, not demonstrated laws.
2. Check every equation, index, matrix entry, sign, unit, arrow, conservation law, operator relation, word and attribution. AI imagery must not be accepted as a source of correct formula typography.
3. **Nilpotence**: N² = 0 is an algebraic property for a specified N; it does not mean N = 0, ordinary additive cancellation, a generic physical vacuum state, or automatic anticommutation with arbitrary operators. A nilpotent matrix example such as [[0,1],[0,0]] is valid. **Do not** label N = γμ pμ − m as square-zero in general; N = γμ pμ satisfies N² = p² I in Clifford conventions, so square-zero requires the particular massless null/on-shell condition. Generic N² = 0 does not prove Dirac equivalence.
4. **Dirac theory**: the free Dirac equation and gamma-matrix anticommutation can be shown as established; a Rowlands-specific nilpotent Dirac correspondence needs its specified construction/assumptions, and its wider interpretation is not an experimentally established new theory.
5. **Zero and vacuum**: an algebraic zero, Rowlands’ proposed zero-totality and the quantum-field vacuum are **not interchangeable**.
6. **Noether / gauge**: Noether’s usual conserved-current mapping concerns continuous action symmetries with appropriate assumptions; do not treat all discrete reflections or time reversals as conservation-law cases. Do not assert universal parity or time-reversal invariance. Distinguish global charge symmetries from local gauge redundancy where relevant.
7. Do not imply that field emergence, particle properties, gravity, technology, or experimental signatures automatically follow from nilpotence. Define a physical model and derive its distinctive testable consequences first. Avoid illustrations that make speculative collider or cosmic predictions look already measured.
8. If accurate complex notation cannot be reliably rendered, simplify to a conceptual diagram and put the exact verified equation/derivation in accessible source-rendered page text after owner approval; never substitute decorative gibberish.

## 5. Figure register — titles and intended paper subjects

The following reflects the inspected source HTML on the feature/v2-space-research-website implementation branch as of 20 November 2026. Before integration, refetch and compare the exact current revision; if it changed, rebaseline.

| Slot | Paper One — Why Physics Still Needs a Unified Framework | Paper Two — Symmetry: Nature's Hidden Language | Paper Three — The Nilpotent Foundation | Paper Four — Mathematics, Elegance and Reality |
| --- | --- | --- | --- | --- |
| Cover | Why a deeper framework is sought | Symmetry across nature, mathematics and physics | Nilpotent structure without trivial emptiness | Mathematical elegance versus physical truth |
| 1.1 | Introductory unification and open questions | Symmetry across biological forms, crystals, mathematics and laws | Symmetry/conservation motivating algebraic balance | Mathematical possibility filtered by observation |
| 2.1 | Problems and unresolved joins in present theories | Snowflakes, shells, crystals, bubbles, galaxies, biological forms | Square-zero non-zero operator; multiplication differs from addition | Model assumptions -> consequences -> comparison with data |
| 3.1 | Current physics strengths and limitations | Transformations: reflection, rotation, translation, invariance | Rowlands: duality, anticommutation, nilpotent algebra | Elegance: economy, symmetry, coherence, explanatory reach |
| 4.1 | Limitations of separate descriptions | Continuous symmetry and conserved quantities (Noether) | Specified correspondence to relativistic Dirac structure | Beautiful mathematics alone cannot decide physical truth |
| 5.1 | SYMMETRIA as exploratory perspective | Symmetry breaking and emergence without overclaim | Algebraic zero versus zero-totality versus quantum vacuum | SYMMETRIA research obligations and falsifiability |
| 6.1 | Methodology and future research questions | Deeper symmetry as a *possible* organising framework | Algebra -> known physics -> quantitative predictions -> evidence | From mathematical structure to emergence and layered reality |

**Crucial cross-check:** The owner’s earlier Paper One AI-generated set also drew on a separate “Unified Field Framework” manuscript, which is **not automatically the same as** the current website Paper One, “Why Physics Still Needs a Unified Framework”. Before any Paper One replacements are accepted, explicitly compare each candidate with the correct online paper. Do not silently treat the documents as identical.

## 6. Production and acceptance workflow

For **every one of 28** slots:
1. Pin the source implementation commit and quote the short relevant internal caption/section in an internal production record (no citations added to the public paper).
2. Compose **one standalone image** in the locked style, with title/subtitle and the correct explanatory content but **no paper or figure identifier inside the artwork**.
3. Inspect at full resolution for legibility and content; independently check formulas, claims, arrows, labels, physical meaning, and correspondence to the real adjacent paper section.
4. Export the approved-looking master at **1920 × 1080**. Programmatically verify actual width = 1920, height = 1080, orientation = landscape, ratio exactly 16:9. Verify the actual image file, not a claimed generation size.
5. Record status per slot: **PASS / FIX REQUIRED / AWAITING OWNER REVIEW**; list open scientific/editorial risks explicitly. No “scientifically approved” claim without appropriate verification.
6. Present individual images and optional contact sheet to the owner; owner approves each final picture before any site integration.
7. Only after approval should Work/Codex replace selected site assets in a scoped non-merged implementation branch; retain original WebPs and rollback map; preserve seven image slots per paper, URLs, appropriate outside-image captions, provenance and responsive display. Test 320/390/768/1440px, check accessibility, build/regression, file paths and WebP quality.
8. Do not merge, deploy, rewrite protected original paper blocks, or announce theoretical validation without separate owner authorisation.

**Pass/fail checklist for a release candidate:** EXACT 1920×1080 ✓; 16:9 ✓; one standalone figure ✓; Paper One visual style ✓; correct paper/section/caption ✓; main subject title ✓; no paper number/figure ID inside image ✓; physics and mathematics reviewed ✓; hypotheses correctly qualified ✓; legible at desktop and mobile ✓; owner approval recorded ✓; original available for rollback ✓.

## 7. Scope and provenance

This document records new owner artwork standards and **does not retroactively certify** prior draft PNGs, earlier contact sheets, any previous “corrected” figure, or the 28 existing site WebPs. It supersedes previous *generation preferences* but does not erase the November 17 scientific findings or authorise a mass replacement before owner approval. The site-level Phase 2 hero has a separate approved composition/aspect rule; this exact 1920×1080 standard concerns **SYMMETRIA paper figure outputs** unless the owner extends it.

**No GitHub website code, original paper, or PR merges are authorised by recording this standard.**
