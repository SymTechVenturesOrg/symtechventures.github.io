# SYMMETRIA — Paper One: Three-Image Localised Scientific Label Repair Specification

**Date:** 20 November 2026 (Europe/London)  
**Status:** AUTHORISED CORRECTION PREPARATION ONLY; no corrected binary exists at the time this specification is written.  
**Source of truth:** [independent QA report](../../../reports/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md) and [post-audit correction register](../../../reports/V2_PHASE_03_PAPER_ONE_POST_AUDIT_TARGETED_CORRECTION_REGISTER_20261120.md) on the parent source branch `docs/symmetria-paper-one-seven-approved-binaries-20261120`.
**Immutable GitHub source commit:** `c6f60ee180c2f5d401b0f597f512898c010981a9`. The seven originals are at `docs/artwork/owner-approved/paper-one/` with `manifest.json` verifying SHA-256 and original Git blobs. These must remain BYTE-FOR-BYTE unchanged.
**Current correction branch:** `docs/symmetria-paper-one-science-corrections-20261120`, cut from the verified source-review branch.
**Technical output:** three separate **1920×1080 PNGs** in `docs/artwork/candidates/paper-one/science-corrections-20261120/`, with new truthful filenames and hashes, not overwritten originals.

## Editing scope

The three source images were visually inspected at full resolution against the science-audit findings. They are genuine rich AI-native cinematic images, not technical drawings that may be completely redrawn from scratch. The locked production standard permits **restrained localised correction of verified text and mathematical labels**, not a flat programmatically assembled remake.

### Figure 1.1 — 'Unification Through the Ages'

**Source binary:** `P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png`  
**Expected source SHA-256:** `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675`.

- The Einstein panel at the lower right contains `G_{μν} = (8πG/c⁴)T_{μν}` without the cosmological term. **Do not change the equation itself** on this minimal pass. Add a clearly legible **`Λ = 0 special case`** note immediately adjacent to that equation, using a harmonious smaller typeface and ensuring the note is not mistaken for another equation.
- Leave **Newton's classical orbital diagram**, inverse-square law, Maxwell field-wave visual, all four Maxwell equations, title, and three historical labels completely unchanged. Do not add spacetime curvature into the Newton panel or imply historical advances together constitute a new verified unified theory.
- The tag must remain readable at full size, within safe padding and without covering the Einstein formula or its gold border. If the tag cannot fit **within the existing visual hierarchy**, mark `NEEDS_NATIVE_IMAGE_EDIT` rather than redraw the entire panel.

### Figure 2.1 — 'Two Successful Theories, One Missing Link'

**Source binary:** `P1_Figure_2_1_OWNER_VISUALLY_APPROVED_1920x1080.png`  
**Expected source SHA-256:** `446af968d82601de428bf719aef9c6a18c837d6b91626955edc04e14613f58e4`.

- Top-left Standard Model heading currently says **`A Quantum Theory of the Fundamental Forces`**. Replace only those subtitle lines with **`Quantum theory of three non-gravitational interactions`** (or a semantically identical shorter line break that visibly preserves `three non-gravitational`). This must not suggest the Standard Model incorporates gravity.
- Bottom-right displayed Einstein equation again assumes zero cosmological constant. Add the same precise explanatory note **`Λ = 0 special case`** nearby without altering the actual equation or surrounding curved-spacetime illustration.
- Preserve all original quark, lepton, gauge-boson panels, their particle labels and the central question-mark gap. Verify the Standard Model's three gauge interaction categories remain visibly correct.
- The website caption's phrase `fundamentally incompatible` is treated **separately** in the proposed caption patch; do not compensate by editing the PNG's scientific centrepiece.

### Figure 3.1 — 'Modern Physics: Successes and Open Frontiers'

**Source binary:** `P1_Figure_3_1_OWNER_VISUALLY_APPROVED_1920x1080.png`  
**Expected source SHA-256:** `62af2ce4790324056dff019c9d1617bd7c9d734b9a9201e40131a0329d1bc317`.

- Top-centre **Standard Model** description currently lists electromagnetic, weak and strong interactions correctly but omits its relationship to the left-hand **Quantum Field Theory** panel. Revise ONLY the explanatory subtitle to state: **`A quantum field theory describing electromagnetic, weak and strong interactions`**. The word `quantum` must establish that these panels are related, **not independent competing foundations**.
- The **Open Frontiers** strapline currently states `Major questions remain beyond the reach of current theories.` This is too absolute for the inferred/modelled gravitational or cosmological effects of dark matter and dark energy. Replace that strapline with: **`Quantum gravity is unresolved; the dark sector's nature remains unknown.`** A more explicit two-line equivalent may be used only if clearly legible and contained within its existing box.
- Preserve the title, QFT field waves, central Standard Model particle panel, gravitational spacetime scene, the three lower scientific question labels, and all gold/cyan visual geometry. Do not fabricate an experimental graph or imply that dark matter/energy have no inferred observable effects.
- If the wording cannot be repaired without major layout intervention, mark `NEEDS_NATIVE_IMAGE_EDIT` and preserve original pixels; do not turn the illustration into a flat slide or use a rejected montage.

## Allowed implementation techniques and exact acceptance

Localised typesetting/cosmetic inpainting of verified label regions is permitted, with adjacent matching cosmic texture and typography. **Do not repaint entire panels, alter main physical geometry, substitute a new illustration, or flatten the composition**. If the edit cannot meet these quality rules, **STOP that slot**; no 'close enough' image.

For each candidate, the Work executor must produce:
1. New standalone PNG **exactly 1920×1080**, source expected SHA-256 proof, candidate SHA-256 and byte length, PNG signature, image decode check, and Git blob SHA.
2. A side-by-side/original-versus-repaired crop inspection for all changed regions, an unedited-area fidelity check, evidence that text is not cropped/duplicated/illegible and a 390px/320px display proxy (with honest zoom limitations).
3. A per-slot status `CANDIDATE_READY_FOR_OWNER_VISUAL_REVIEW` or `BLOCKED_NEEDS_NATIVE_IMAGE_EDIT`. **Do not promote the candidate to science-approved or owner-approved without a separate decision.**
4. Independent GitHub binary readback from a clean checkout after committing candidate PNGs; never use source bytes as proof that new GitHub candidate bytes were saved.
5. No modification to the original 7 SHA-256 manifest or the existing owner-approved original PNGs. Prepare a **separate** candidate manifest that records `source_sha256`, `candidate_sha256`, target path, status and clear diff/QA notes.

**No website integration/HTML/CSS changes, no PR #5 edits, no merge, no deploy.** Full independent science re-audit must come from a separate verification pass once candidates have passed owner visual review.
