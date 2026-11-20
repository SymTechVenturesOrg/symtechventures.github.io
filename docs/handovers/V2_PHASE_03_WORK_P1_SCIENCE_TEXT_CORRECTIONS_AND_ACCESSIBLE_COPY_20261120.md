# SYMMETRIA — Work Handover: Paper One Localised Science Text Repairs and Caption Draft QA

**Date:** 20 November 2026, Europe/London.
**Work configuration — OWNER SELECTS BEFORE LAUNCH:** **Model: GPT-6 Luna (Work)**; **Thinking effort: High**; **Execution speed: Standard**. Work cannot select or change these settings.
**DTSU v1.1:** genuine Europe/London time in every update; explicit 0% start; one concise sentence containing progress percentage, present activity and realistic **numeric remaining ETA** (revise when circumstances change); do not claim 100% until validation and full COPY TO CHAT handback.
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`
**Working branch:** `docs/symmetria-paper-one-science-corrections-20261120`, branched from `docs/symmetria-paper-one-seven-approved-binaries-20261120` (draft source PR #9).
**Output:** **Three new science-corrected image candidates** where faithful local edits are possible, one separate candidate manifest, technical QA evidence, and a report; verified GitHub-native process only. No manual ZIP transfer.
**Already prepared on working branch:**
- [Exact per-image correction specification](../artwork/candidates/paper-one/SCIENCE_TEXT_REPAIR_SPEC_20261120.md).
- [Caption 2.1/5.1 proposals and seven accessible descriptions](../artwork/candidates/paper-one/PROPOSED_CAPTIONS_AND_ACCESSIBILITY_COPY_20261120.md).
- [Independent seven-image QA report](../reports/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md).
- [Verified original PNG identity manifest](../artwork/owner-approved/paper-one/manifest.json).

## Why these images require targeted editing

All seven original Paper One images are **visually owner-approved** and preserved **unchanged** on GitHub at immutable import commit `c6f60ee180c2f5d401b0f597f512898c010981a9`. Work independently verified all seven source byte hashes and science-audited them at branch head `574e430ca54bd5dd3dfe762c59b8565279f0f9b1`. QA returned: 3 ready (cover/4.1/6.1), 3 science fixes (1.1/2.1/3.1), 1 external-caption fix (5.1). This pass only corrects the three annotated science images and reviews caption drafts; it does **not** revise the website.

**Binding aesthetic:** The main-branch cinematic AI artwork standard requires the gold-serif/navy/cyan/volumetric scientific look. **Only localised and scientifically verified text/glyph repairs** are permitted without a fresh AI edit; do not programmatically reconstruct a flat infographic, replace full panels or change fundamental geometry.

## Stage 0 — read the exact GitHub originals and revalidate scope

1. Check out `docs/symmetria-paper-one-science-corrections-20261120` via a **binary-capable authenticated Git checkout**. Read exact input PNGs under `docs/artwork/owner-approved/paper-one/`; recompute SHA-256 for 1.1, 2.1, 3.1 against `manifest.json` before editing. Record branch HEAD and check that `articles/symmetria/symmetria-paper-01.html` in website implementation PR #5 has not been altered by this work.
2. Re-open the independent QA report and the two correction-spec documents on the working branch. If any reference/caption has changed, reconcile it explicitly before edits. All approved originals are READ-ONLY.
3. Before modifying anything, take full-resolution working crops of each exact text area and check its actual typography/background so local edits preserve appearance.

## Stage 1 — produce correct science-label candidates

Use the exact [SCIENCE_TEXT_REPAIR_SPEC](../artwork/candidates/paper-one/SCIENCE_TEXT_REPAIR_SPEC_20261120.md) and make **only** these changes:

- **1.1:** next to the original Einstein equation add **`Λ = 0 special case`**, not a new arbitrary equation; **leave Newton/Maxwell intact**.
- **2.1:** replace the overbroad Standard Model subtitle with **`Quantum theory of three non-gravitational interactions`** (equivalent accurate line breaks allowed); add **`Λ = 0 special case`** by the Einstein equation. Preserve the particle panels and open-unification question.
- **3.1:** revise the Standard Model subtitle to clarify **it is formulated within quantum field theory**, and replace the overbroad `Beyond the reach of current theories` strapline with the concise truth that **quantum gravity remains unresolved whereas dark matter/dark energy effects are modelled but underlying physics unknown**. Use the shorter exact in-figure examples in the specification if they are necessary for fit.

Write one NEW standalone 1920×1080 PNG per successful slot under `docs/artwork/candidates/paper-one/science-corrections-20261120/` with these proposed filenames:
- `P1_Figure_1_1_Lambda0_Correction_Candidate_1920x1080.png`
- `P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png`
- `P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png`

Use the capable image editor/computer tool to make **minimal source-faithful label inpainting/typesetting**; *do not* crop a contact sheet, regenerate a different scene, use a flat-slide replacement or delete a scientific caveat. Maintain readability and compositional integrity. **If the needed text-area change is not genuinely localised**, mark that figure `BLOCKED_NEEDS_NATIVE_IMAGE_EDIT`, omit its candidate binary, and preserve the original. Partial results are preferred to unfaithful substitutions.

## Stage 2 — technical QA and independent GitHub binary readback

For each actual new candidate:
1. Verify PNG signature, exact 1920×1080 RGB/RGBA geometry, full decoding, new byte count and SHA-256; do not confuse candidate hashes with owner-approved originals.
2. Inspect original/corrected crops, check every changed glyph and any duplicate/occluded original text. Show full-frame vs crop views in report. Note that a locally changed text region is **not** a new owner visual approval.
3. Audit pixel differences outside permitted text masks, identify bounds and confirm no altered scientific geometry/panel strokes.
4. Compute 390px and 320px readability proxies and honestly note that real-browser or device tests have **not** yet occurred.
5. Commit successful candidates and `candidate_manifest.json` to the correction branch only; independently checkout the candidate commit in a **fresh GitHub checkout**, recompute every candidate's SHA-256 and image geometry from GitHub bytes, and record the Git blob IDs.
6. Recompute original **seven** owner-approved PNG SHA-256 values, or at minimum inspect `git diff` to show NONE of their bytes/paths changed plus the verified manifest. Do not silently modify the original JSON statuses.

## Stage 3 — editorial text proposals (not website changes)

Read [prepared caption/accessibility draft](../artwork/candidates/paper-one/PROPOSED_CAPTIONS_AND_ACCESSIBILITY_COPY_20261120.md) and review for scientific precision, British English, standalone hypothesis labelling and accessibility. Source captions must be compared against **live GitHub website article** `articles/symmetria/symmetria-paper-01.html` on `feature/v2-space-research-website`, pinned HTML blob `c235e33bbe3a291343125c94af73fe54a23491fa` at prior audit. Do NOT apply caption changes to site HTML, do not edit PR #5 or propose an automatic live release.

Required draft captions: replace the categorical `fundamentally incompatible` statement in 2.1 with an open-reconciliation formulation; make 5.1 stand-alone explicit that the SYMMETRIA proposal is **untested**. Review seven concise alt texts and longer HTML-descriptions; the direct 1920px viewing link and real 390px/320px tests are separate integration gates.

## Stage 4 — Work deliverables and completion boundary

Commit a concise `docs/reports/V2_PHASE_03_P1_SCIENCE_TEXT_CORRECTION_WORK_RESULTS_20261120.md` to the correction branch with:
- Original source and correction-branch HEAD SHAs, original hash-to-candidate hash matrix, successes/blockers by slot, exact edited strings, image diff bounds and any scientific uncertainty.
- Evidence for every binary-candidate GitHub readback and unchanged original hashes.
- Review of two caption proposals and the accessible descriptions, with proposed improvements **inside docs only**.
- Explicit **OWNER VISUAL RE-APPROVAL PENDING** for any corrected image; independent science re-audit requires **another reviewer/session**, not self-certification by this edit executor.
- **COPY TO CHAT** (brief, shareable) summarising updated paths, 3/3 or partial result, source SHA, QA, blockers and next owner decisions.

**Never change the website HTML/CSS/assets, scientific manuscript body, website draft PR #5, main branch or existing verified seven originals; never merge PR #9 or any PR and never deploy.** If text repair cannot meet the locked cinematic style, stop that slot rather than overclaiming success. In that case the next pass is an isolated native AI image edit under owner review, not an automatic image replacement.
