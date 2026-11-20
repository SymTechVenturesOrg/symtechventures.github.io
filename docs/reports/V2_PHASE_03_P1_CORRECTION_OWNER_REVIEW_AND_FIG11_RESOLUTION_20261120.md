# SYMMETRIA — Paper One: Owner Visual Review and Figure 1.1 Scientific Qualification Decision

**Date:** 20 November 2026 (Europe/London)  
**Status:** Two corrected candidates await owner visual approval; Figure 1.1 scientific qualifier remains **BLOCKED** pending an explicit acceptable resolution and independent re-audit.  
**Branch:** `docs/symmetria-paper-one-science-corrections-20261120`, [draft PR #10](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/10), stacked on [draft PR #9](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/9).  
**Grounding:** [Full GitHub-native correction QA](V2_PHASE_03_P1_SCIENCE_TEXT_CORRECTION_WORK_RESULTS_20261120.md), [candidate manifest](../artwork/candidates/paper-one/science-corrections-20261120/candidate_manifest.json), and original seven-figure manifest in `docs/artwork/owner-approved/paper-one/`.

## A. Two precise owner review decisions — visuals only

| Slot | GitHub image candidate | SHA-256 from independent GitHub checkout | Changed only in these original-art image regions | Next decision |
|---|---|---|---|---|
| 2.1 | [Open Figure 2.1 image](../artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png) | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | Standard Model subtitle → **`Quantum theory of three non-gravitational interactions`**; Einstein's equation annotated **`Λ = 0 special case`** | **OWNER VISUAL APPROVAL PENDING** |
| 3.1 | [Open Figure 3.1 image](../artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png) | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | Standard Model explicitly identified as a QFT; open-frontiers strapline says quantum gravity remains unresolved and dark-sector nature unknown | **OWNER VISUAL APPROVAL PENDING** |

**Verified attributes:** Each candidate is 1920×1080 RGB PNG. Fresh GitHub checkout matched source/target SHA and Git blob IDs. Pixel changes occurred only within authorised replacement-text rectangles; no cinematic geometry was changed. The owner previously approved the **originals**, not these corrected files. Independent science re-audit remains necessary even if both visuals are approved.

## B. Figure 1.1 — alternative resolution, no forced image redesign

**Source:** `docs/artwork/owner-approved/paper-one/P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png`, SHA-256 `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675`.

**Scientific finding:** The existing Einstein field equation `G_{μν} = (8πG/c⁴)T_{μν}` is correct as a **Λ = 0 special case** but does not state the cosmological term of the general equation. The image's original cinematic equation capsule has insufficient space to add a legible note without overpainting or redesigning it.

**Proposed low-impact alternative for independent reviewer decision (NOT YET APPROVED):**

- **Keep the owner's approved Figure 1.1 PNG unchanged**, and retain its original SHA-256.
- Amend the *adjacent visible, selectable HTML caption* to carry the explicit qualification, immediately after the historical sentence, such as:

> The Einstein field equation shown is the special case with cosmological constant **Λ = 0**; the general form also contains a cosmological term.

- Add that same qualification to the longer accessible HTML image description. Provide a full-resolution zoom/open link so readers can inspect the original formula.
- Request **independent scientific/editorial re-audit** specifically answering whether a clearly adjacent visible HTML qualification is sufficient for Figure 1.1's narrative and accessibility (versus a requirement for the qualification inside the artwork). **Until independently accepted, Figure 1.1 stays `BLOCKED_NEEDS_NATIVE_IMAGE_EDIT`; this proposal does not override the original audit.**
- If re-audit rejects adjacent text as inadequate, undertake **an isolated native image edit** expanding only the Einstein equation capsule, preserving all Newton/Maxwell/other physical geometry, outputting a new 1920×1080 candidate with its own SHA-256 and owner style re-approval. Do not force a tiny overlaid note.

## C. Other pending captions and site integration

- **Figure 2.1:** revise external caption `fundamentally incompatible` to a nuanced statement that complete experimentally established quantum-gravity reconciliation remains unresolved, despite the success of quantum theory and GR in their respective domains.
- **Figure 5.1:** introduce an explicit `untested hypothesis` caveat in the external HTML caption; the image already carries the disclaimer.
- **Accessibility:** all seven need concise useful `alt`, detailed optional accessible HTML explanation, and keyboard/touch access to full-resolution PNG; the ~390px and 320px mobile readability limitations came from simulated scaling, **not a browser/device test**.
- **Source drift note for the independent reviewer:** latest correction Work report recorded the website Paper One HTML blob as `390a8676189542fc9044c1dabbbf344ad10e69f6` on `feature/v2-space-research-website`, whereas the connected GitHub `fetch_file` read on 20 November 2026 returned `c235e33bbe3a291343125c94af73fe54a23491fa`. Both reads quoted the same 2.1 and 5.1 captions. **Do not silently reconcile this metadata conflict**: re-pin HEAD and compute/compare exact Git blob from a fresh checkout before any future website-specific correction. No change to article has been made here.

## D. Explicit approval and preservation boundaries

Owner's visual decision is now sought for **exactly Figures 2.1 and 3.1 candidate PNGs** linked above. Figure 1.1's caption-only alternative also requires **separate scientific reviewer acceptance and later owner authorisation before a website edit**. No original image may be overwritten or silently relabelled approved, no change to site HTML/assets/PR #5, and no merges or deployment. Draft PRs #9 and #10 remain unmerged.


## Owner visual approval received — 20 November 2026 (supersedes earlier pending flags for these two images ONLY)

After being shown the specific GitHub image links to the corrected Figure 2.1 and 3.1 candidate PNGs, the owner responded **“Approved, continue.”** This is explicit **visual approval of the exact two corrected candidates**:

- Figure 2.1: `P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png`, SHA-256 `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` — **OWNER VISUALLY APPROVED**.
- Figure 3.1: `P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png`, SHA-256 `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` — **OWNER VISUALLY APPROVED**.

The earlier `OWNER VISUAL APPROVAL PENDING` entries in the original inspection table and correction-work report are historical. **They are superseded for visual approval only.** No independent science re-audit, Figure 1.1 caption solution, external website caption update, real-browser mobile test or deployment is approved by this reply. Original seven-image GitHub binaries remain immutable.

Next authorised step: independent GitHub-native **read-only scientific re-audit** of these two corrected image binaries, the proposed Figure 1.1 visible caption qualification, and the Figure 2.1/5.1 proposed web-caption and accessibility texts. A separate scientific reviewer must decide whether the Figure 1.1 caption-only remedy resolves the equation issue or whether a new native-image edit is required. Never silently mark Figure 1.1 ready.
