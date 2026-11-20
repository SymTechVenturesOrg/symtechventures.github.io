# SYMMETRIA — Paper One: Independent Science Re-Audit of Corrected Figures 2.1 and 3.1 + Figure 1.1 Caption Decision

**Date:** 20 November 2026 (Europe/London).  
**Handover status:** READY FOR INDEPENDENT WORK REVIEW; NOT SCIENCE-CLEARED OR WEBSITE-INTEGRATION AUTHORISED.
**User-selected Work settings, chosen in the interface before launch:** **Model: GPT-6 Luna (Work)** · **Thinking effort: High** · **Execution speed: Standard**. These are user choices; Work cannot choose them autonomously.
**DTSU v1.1:** start with real Europe/London timestamp and 0%; give concise progress reports containing verified completion percentage, present activity and a reasoned **numerical remaining ETA**; revise estimates as required; do not report 100% until all verification, the report and COPY TO CHAT are done.
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`.
**Work branch:** `docs/symmetria-paper-one-science-corrections-20261120`, stacked draft PR #10 over draft PR #9. Verify current HEAD at execution; the initial owner-approval record was committed as part of preparation, after prior candidate production HEAD `2058f2a72ab8c3e44737b061d323e7022e032299`.
**Output:** one independent, evidence-backed **science/editorial decision report**, committed under `docs/reports/` on the documentation-only correction branch. The audit is **read-only for PNGs, manifests, HTML, CSS and the website**. It may commit the new Markdown audit report only.
**No ZIP handoff:** all originals and corrected candidates are already in GitHub, including binary Git objects.

## 1. User approvals and protected source identities

The owner visually approved **both corrected candidates** after their individual GitHub image links were presented, replying **“Approved, continue.”** This applies solely to the exact SHA-256 identities below and does not certify scientific correctness or website readiness.

| Slot | Candidate PNG (GitHub repo-relative path) | Verified prior SHA-256 | Git blob |
|---|---|---|---|
| 2.1 | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png` | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | `16adf23b9d8f61ec4c47c48ac243cae096b3336a` |
| 3.1 | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png` | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | `4bcafdc4bbd3d068b582dad27735c6554f008700` |
| Original 1.1 | `docs/artwork/owner-approved/paper-one/P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675` | `6d42d6bce260d1f23f0b55b21df9ad05b3fe7c17` |

**Unchanged full original set:** `docs/artwork/owner-approved/paper-one/` contains seven approved 1920×1080 PNGs and [verified source manifest](../artwork/owner-approved/paper-one/manifest.json), first GitHub binary commit `c6f60ee180c2f5d401b0f597f512898c010981a9`. The original assets are not to be overwritten, renamed, recompressed or promoted as replacements. Latest correction [candidate_manifest.json](../artwork/candidates/paper-one/science-corrections-20261120/candidate_manifest.json) records distinct owner visual approvals and pending independent science review.

References to read:
- [Earlier initial seven-figure science audit](../reports/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md).
- [Exact science-editing Work QA report](../reports/V2_PHASE_03_P1_SCIENCE_TEXT_CORRECTION_WORK_RESULTS_20261120.md).
- [Owner approval and Figure 1.1 decision register](../reports/V2_PHASE_03_P1_CORRECTION_OWNER_REVIEW_AND_FIG11_RESOLUTION_20261120.md).
- [Caption 2.1/5.1 and accessible-copy proposals](../artwork/candidates/paper-one/PROPOSED_CAPTIONS_AND_ACCESSIBILITY_COPY_20261120.md).
- [Locked cinematic production standard](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/main/docs/reports/V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md).

## 2. Binary and provenance review — entirely from GitHub

1. Start with a **fresh binary-capable Git checkout** of the work branch, pin its actual full commit SHA; do not rely on only GitHub's text file API for image bytes. Recompute SHA-256, PNG signature, exact 1920×1080 geometry, decodability and Git blob ID of **both corrected PNGs and original Figure 1.1**, comparing the table above. Record bytes and commands.
2. Compare each corrected PNG **pixel for pixel** to its original corresponding PNG. Earlier correction QA reported 0 changed pixels outside permitted text boxes. Independently verify this, using exact masks:
    - 2.1 subtitle `[243,191,709,281)` and Λ note `[1491,719,1664,748)`.
    - 3.1 Standard Model description `[711,189,1254,285)` and Open Frontiers strapline `[511,684,1409,737)`.
   Explicitly flag any changed pixels outside these boxes; verify visually against full-resolution originals and examine zoomed repaired-area crops for seams, old-word remnants, clipping, incorrect physical diagrams, unreadable Greek glyphs or misleading punctuation.
3. Confirm `git diff` shows **no modifications to the seven owner-approved original PNG paths**, website HTML or deployed image assets, and that branch PR #10 remains draft and unmerged.

## 3. Independent figure-specific science and editorial re-audit

### Figure 2.1 — quantum interactions and gravity

Check the *actual revised artwork*, not just the previous textual correction report:

- Standard Model subtitle is accurately and legibly **`Quantum theory of three non-gravitational interactions`**. Confirm that the particle/gauge-interaction labels support this and no visual element claims gravity is part of the Standard Model.
- Existing Einstein equation (G_{μν} = 8πGT_{μν}/c⁴) is labelled unambiguously **`Λ = 0 special case`**; verify visibility and that it is not interpreted as an unqualified general field equation. Check all mathematical symbols at full scale.
- No assertion of completed quantum-gravity unification. Review whether the explanatory text is legible under the locked cinematic design.
- Audit the **proposed website caption**, not website source modifications: `Quantum mechanics and general relativity are each highly successful in their respective domains, but a complete, experimentally established framework reconciling quantum principles with gravity remains an open research challenge.` Confirm nuanced, accurate scientific wording; note effective/semiclassical treatments do exist.

### Figure 3.1 — Quantum Field Theory, Standard Model and dark sector

Inspect all rendered labels, concept relations and geometry:

- The Standard Model is **formulated using quantum field theory**, rather than sitting as a wholly independent competing foundational framework. The candidate label says **`A quantum field theory describing electromagnetic, weak and strong interactions`**; check this is legible, qualified and compatible with adjacent QFT panel.
- Gravity remains under general relativity, and the Standard Model's three forces are not confused with gravity or an asserted complete grand unification.
- The new frontier strapline says **`Quantum gravity is unresolved; the dark sector's nature remains unknown.`** Verify that dark matter/energy gravitational and cosmological effects are **modelled/inferred**; this language must not imply their phenomena are unmodelled or that their particulate/field identity has already been established.
- Check all actual particle-family/gauge boson notation and whether explanatory text fits the original cinematic design.

### Figure 1.1 — independent decision on minimal *caption-only* special-case caveat

**This is an actual decision gate, not a pre-decided pass.** The original, aesthetically approved Figure 1.1 cannot safely accommodate another legible annotation in its Einstein formula capsule; no modified binary was created.

Examine the source image, its original external caption, section context and proposed **adjacent visible HTML caption append**:

> The Einstein field equation shown is the special case with cosmological constant Λ = 0; the general form also contains a cosmological term.

Decide explicitly, providing scientific/editorial reasoning:
- **ACCEPT CAPTION-ONLY RESOLUTION** if the existing on-image equation is correct for `Λ=0`, the adjacent visible/selectable caption clearly qualifies the depicted mathematical expression, the accessible longer description repeats the qualification, and a full-resolution view makes the formula inspectable. If acceptable, mark `CONDITIONALLY READY — CAPTION INTEGRATION REQUIRED`, **not science-passed in the existing website**.
- **REJECT CAPTION-ONLY RESOLUTION** if the image is intrinsically misleading without an in-pixel caveat, in which case retain `BLOCKED_NEEDS_NATIVE_IMAGE_EDIT` and specify the smallest viable native AI/edit change; do not fabricate a new candidate or silently waive the issue.
- Clarify whether the formula uses the expected sign and conventions; audit Newtonian vs curved-spacetime visuals and Maxwell equations if required for this decision.

## 4. Caption and accessibility review (read-only)

Review **both** exact proposed captions for Figure 2.1 and 5.1, plus the Figure 1.1 new append proposal; revise only within the new **documentation audit report**, not the HTML:

- 2.1: replace categorical `fundamentally incompatible` with a carefully qualified quantum-gravity open challenge statement.
- 5.1: mark SYMMETRIA's four proposed concepts explicitly **untested**. Evaluate the smoother `SYMMETRIA presents the following as an untested hypothesis: ...` versus the earlier `As an untested hypothesis, SYMMETRIA proposes ...`. Preserve the exact science/status and British English.
- 1.1: full Einstein `Λ=0` caveat in visible caption and longer explanation if accepted.
- Inspect the seven proposed short `alt` strings and explanatory text. Prefer precise succinct alt labels and a separate detailed accessible HTML description; figure numbers/series mastheads stay **outside** PNG art. Retain the open-full-resolution link and accessible zoom as later website work.
- Re-read the **current** actual website Paper One HTML from `feature/v2-space-research-website` in a binary Git checkout, pin current branch HEAD and **HTML blob SHA**. Earlier Work noted a discrepancy: its `390a8676189542fc9044c1dabbbf344ad10e69f6` vs connected `fetch_file` reading `c235e33bbe3a291343125c94af73fe54a23491fa`. Do not silently treat these as equal; report whether the discrepancy can be independently reproduced, and quote exact Figure 1.1, 2.1, 5.1 current captions from the checkout.
- Clearly distinguish CSS-based **390px/320px projections** from actual browser/device tests (none done in prior passes); recommend keyboard/touch zoom and accessible long descriptions without claiming they were implemented.

## 5. Report and exact completion states

Commit **only one new markdown audit report** to `docs/reports/V2_PHASE_03_P1_FIGURES_2_1_3_1_INDEPENDENT_SCIENCE_REAUDIT_AND_1_1_CAPTION_DECISION_20261120.md` on the corrections documentation branch. Include:

- First line-level **source citations**: verified repo SHA of correction branch, original import commit, image candidate commit `ef09d41b6b7fcb85efc75618736c234ccc2fa09c`, actual website branch HEAD + blob, and the exact two PNG SHA-256 values.
- Fresh checkout SHA-256/bytes/geometry/Git-blob matrix for 2.1, 3.1 and original 1.1; pixel-diff mask outcome; each corrected caption and literal on-image wording checked.
- A clear **independent science disposition** for each of 2.1 and 3.1: `PASS_SCIENCE_REAUDIT`, `SCIENCE_TEXT_FIX_REQUIRED` or `BLOCKED`, with precise reasons. Owner visual approval remains separate and retained.
- A clear **Figure 1.1 conditional disposition**: `CAPTION_ONLY_ACCEPTABLE_PENDING_WEBSITE_IMPLEMENTATION` or `NATIVE_IMAGE_REPAIR_REQUIRED`. No actual website HTML modification is permitted by this pass.
- Decision on exact caption 2.1 and 5.1 wording, 7 alt text suggestions and mobile open-original requirement; separate what is planned from tested.
- **COPY TO CHAT**: time, three image statuses, 7/7 original integrity state, audit report link, website SHA conflict result, remaining owner/implementation gates.
- Claim **100% only for this read-only QA task** once all checks are complete; do **not** say website release/scientific hypothesis is validated.

**Absolute non-authority:** No modified PNGs, no changes to any seven owner-approved originals, no website HTML/CSS, no live article/PR #5, no `main` changes, no review status or PR merges, no deployment. If binary access is missing, report blocked; do not ask the user to download/upload ZIPs.
