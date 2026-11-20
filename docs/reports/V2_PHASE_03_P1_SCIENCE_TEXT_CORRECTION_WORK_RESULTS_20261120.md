# SYMMETRIA Paper One — Targeted Science-Text Correction Results

**Date:** 20 November 2026 (Europe/London)  
**Branch:** `docs/symmetria-paper-one-science-corrections-20261120`  
**DTSU v1.1:** Updates used genuine Europe/London timestamps, a truthful percentage, current activity and numeric remaining ETA.  
**Scope:** Correct only specified text in Figures 1.1, 2.1 and 3.1; audit draft captions and accessible copy. No website, PR #5, merge or deployment changes.

## Result

Two localised candidates (2.1 and 3.1) are committed as new PNG paths and independently verified from a fresh GitHub checkout. Figure 1.1 is **BLOCKED_NEEDS_NATIVE_IMAGE_EDIT**: its Einstein equation capsule has no safe room for the required note at a readable size within the existing visual hierarchy. No replacement candidate was made. The seven approved source PNGs remain unchanged.

The candidate files are technical/editorial candidates only. **OWNER VISUAL RE-APPROVAL PENDING** for 2.1 and 3.1; a separate reviewer/session must conduct the independent science re-audit before either image can be called science-approved.

## Source and branch provenance

- Immutable original-binary import commit: `c6f60ee180c2f5d401b0f597f512898c010981a9`.
- Correction branch HEAD before this pass: `0f552143c45e2d659be0598ba6031884f6ed0913`.
- Candidate PNG commit: `ef09d41b6b7fcb85efc75618736c234ccc2fa09c`.
- The candidate commit adds exactly two paths under `docs/artwork/candidates/paper-one/science-corrections-20261120/`. It changes no `docs/artwork/owner-approved/paper-one/` path. It does not edit `articles/symmetria/symmetria-paper-01.html`, website assets, PR #5, or any other PR.
- A fresh GitHub checkout confirmed each of the seven original SHA-256 values below matches the immutable manifest. `git diff` for owner-approved source paths from the candidate commit's parent to the candidate commit is empty.

| Original slot | Original path suffix | SHA-256 |
|---|---|---|
| Cover | `P1_Cover_OWNER_VISUALLY_APPROVED_1920x1080.png` | `3eeba0f6bfcefd2a63b5867cad0442ac9a6d356526cc1fed31e057d3de9e95a8` |
| 1.1 | `P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675` |
| 2.1 | `P1_Figure_2_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `446af968d82601de428bf719aef9c6a18c837d6b91626955edc04e14613f58e4` |
| 3.1 | `P1_Figure_3_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `62af2ce4790324056dff019c9d1617bd7c9d734b9a9201e40131a0329d1bc317` |
| 4.1 | `P1_Figure_4_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `788e68dc507c1e408428380b86816e594301384ed29331a3ab9aa9c29cdb9238` |
| 5.1 | `P1_Figure_5_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c` |
| 6.1 | `P1_Figure_6_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `a1c9c939c6195a97106a3e4c8a49398a48b27baf108a8ef7b21bdc0ed09e896f` |

## Candidate binary verification

Both candidate PNGs were fetched by a fresh binary-capable GitHub clone after commit `ef09d41b6b7fcb85efc75618736c234ccc2fa09c`, fully decoded, and hashed from the checkout bytes. Git blob IDs independently match the blob IDs returned for the GitHub binary writes. Both have PNG signatures, 1920×1080 geometry and RGB mode.

| Slot | New candidate path | Bytes | SHA-256 | Git blob |
|---|---|---:|---|---|
| 2.1 | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png` | 3,088,099 | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | `16adf23b9d8f61ec4c47c48ac243cae096b3336a` |
| 3.1 | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png` | 3,348,284 | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | `4bcafdc4bbd3d068b582dad27735c6554f008700` |

## Image-by-image science and visual QA

### Figure 1.1 — blocked

The source correctly shows Newtonian orbital mechanics, Maxwell electromagnetism and Einsteinian curved spacetime as historical advances. The displayed Einstein field equation lacks the cosmological term, so the specified `Λ = 0 special case` caveat is scientifically necessary. The equation capsule is tightly composed: the formula nearly fills its interior, with explanatory text immediately beneath it. A legible note cannot be added beside the equation while retaining safe padding and the current hierarchy; placing it outside would intrude on the spacetime mesh or the neighbouring label. Moving/rebuilding the capsule or shrinking/overlapping existing text would be a redesign. **Status: BLOCKED_NEEDS_NATIVE_IMAGE_EDIT.** Original SHA-256 remains `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675`; no candidate path or bytes exist.

### Figure 2.1 — candidate ready for owner visual review

Edits are limited to two text regions: the Standard Model subtitle now reads `Quantum theory of three non-gravitational interactions`; the displayed Einstein equation remains untouched and the nearby note reads `Λ = 0 special case`. The particle panels, labels, central unification question, equation and curved-spacetime composition remain intact. The new note fits in the narrow existing gap beneath the equation capsule and above the curved-spacetime label; it does not obscure the formula or border. The upper-left subtitle remains within its existing capsule. Visual review at full frame and detailed crops found no duplicated old wording or obvious inpainting seam. The style remains cinematic gold/cream serif italic against the original navy/cyan cosmic scene, although the locally typeset lettering is an approximation of the source lettering rather than a claim of exact font identity.

Pixel comparison against the exact original found 41,603 changed pixels, all inside the two authorised text regions. Region bounds (x1,y1,x2,y2; exclusive end) and changed-pixel counts: subtitle `[243,191,709,281)` / 38,419; Λ note `[1491,719,1664,748)` / 3,184. **Zero** changed pixels occurred outside the authorised regions; no equation glyphs or scientific geometry changed.

### Figure 3.1 — candidate ready for owner visual review

The Standard Model description now reads `A quantum field theory describing electromagnetic, weak and strong interactions`, explicitly relating the Standard Model to QFT while naming the three interactions it describes. The Open Frontiers strapline now reads `Quantum gravity is unresolved; the dark sector's nature remains unknown.` This avoids saying that all dark-sector effects are beyond current theories: gravitational and cosmological effects are modelled, while the underlying nature is unknown. Title, QFT waves, Standard Model particles, general-relativity scene, lower questions and gold/cyan geometry remain intact. Full-frame and crop inspection found the replacement lines fit their existing regions, without duplicate old text or obvious seams; typesetting is a close serif-italic/cream style approximation.

Pixel comparison found 92,997 changed pixels, all inside the two authorised text regions: subtitle `[711,189,1254,285)` / 49,251; frontier strapline `[511,684,1409,737)` / 43,746. **Zero** changed pixels occurred outside the authorised regions; no scientific panel or geometry changed.

## Mobile readability proxy

These are proportional-size calculations on the 1920px-wide PNG, not real browser/device tests. At 390px image width, the corrected type is about 4.47–6.30px high; at 320px, about 3.67–5.17px. The labels are therefore **not comfortably readable at native mobile display width without zoom**. The candidate keeps the wording concise and visible at full resolution. A later website integration should retain an accessible visible caption/description and a keyboard/touch-accessible route to the native 1920px image; actual 390px and 320px browser renders remain untested.

## Caption proposal review (documentation only)

The handover/proposal cites HTML blob `c235e33bbe3a291343125c94af73fe54a23491fa`. A fresh read of the named live branch `feature/v2-space-research-website` found the current article blob is `390a8676189542fc9044c1dabbbf344ad10e69f6` at branch head `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`; the relevant Figure 2.1 and 5.1 captions match the proposal's quoted current text. The source was read only.

- **Figure 2.1:** The current caption calls quantum mechanics and general relativity “fundamentally incompatible”. The proposed replacement accurately states that each is successful in its domain while a complete, experimentally established reconciliation remains open. It removes the categorical claim without suggesting that either theory fails in its validated domain. **Recommend adoption in a separately authorised website review.**
- **Figure 5.1:** The proposed opening `As an untested hypothesis, SYMMETRIA proposes…` makes the epistemic status explicit even when the image's internal caveat is not available to a screen reader, search result or zoomed crop. This is scientifically and editorially useful. It is somewhat repetitive (“hypothesis” and “proposes”), but clear; a smoother alternative is `SYMMETRIA presents the following as an untested hypothesis: reality may emerge…` for editorial consideration.

No captions or HTML were edited in this pass.

## Accessibility copy review (all seven slots; proposals only)

The draft correctly separates concise `alt` text from longer descriptions, keeps speculation explicit for 5.1, distinguishes the Standard Model from gravity, and explains the Λ=0 caveat in descriptions for 1.1 and 2.1. The 4.1 description usefully distinguishes dimensional constants from dimensionless α; the 6.1 description correctly calls its roadmap planned work, including computational/AI analysis and the Nilpotent Symmetry Research Program, rather than completed validation. The cover and 5.1 longer descriptions likewise avoid presenting unification or emergence as established.

Suggested small improvements to the proposed `alt` wording, for owner/editor review:

- **1.1:** Replace the awkward phrase `Einstein curved spacetime` with `Einsteinian curved-spacetime account of gravity`; the image depicts Einstein's theory, not a person or a separate “Einstein curved spacetime”.
- **2.1:** State the relationship and missing link more directly: `The Standard Model's particles and three quantum interactions face general relativity's curved spacetime across an unresolved unification gap.`
- **3.1:** Avoid the vague spatial phrase `sit above`; suggested: `Quantum field theory underpins the Standard Model; general relativity and open questions about quantum gravity and the dark sector complete the scene.`
- **4.1:** The proposed phrase `Four open questions concern ... fundamental constants` grammatically treats constants themselves as an open question. Consider `Four themes: quantum gravity, quantum interpretation, physical constants and experimental tests.`

The existing alt proposals for the cover, 5.1 and 6.1 are concise and suitably cautious. Longer descriptions are scientifically sound as drafts; retain the distinction between inferred dark-sector effects and unknown underlying nature, keep all claims testable/qualified, and avoid placing equation caveats only in embedded image text. These refinements remain documentation/editorial recommendations; no HTML or accessible site copy was changed.

## Remaining gates and COPY TO CHAT

- Owner visual approval of candidate 2.1 and 3.1: **pending**.
- Separate independent science re-audit: **pending**.
- Figure 1.1: blocked; next step would require an owner-reviewed native image edit/layout decision.
- Mobile browser/device tests, accessible links and caption integration: not performed; require separate website authorisation.
- No merge, PR #5 modification or deployment occurred.

### COPY TO CHAT

**SYMMETRIA Paper One targeted science-text pass:** Figures **2.1 and 3.1** are committed as new candidate PNGs on `docs/symmetria-paper-one-science-corrections-20261120` (binary commit `ef09d41b6b7fcb85efc75618736c234ccc2fa09c`). Fresh GitHub checkout independently confirmed both as RGB PNGs at 1920×1080, with SHA-256 `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` and `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92`. All seven original PNG hashes still match the immutable source manifest; the binary commit adds only the two candidate paths. Figure **1.1 is blocked** because its equation panel has no safe room for the Λ=0 note without redesign; its original remains unchanged. Caption and seven-slot accessibility drafts were reviewed; recommended text refinements are documented only. The image text is too small to rely on at 390px/320px native display widths, and no real-device test was performed. **Owner visual re-approval and an independent science re-audit remain pending.** No website file or PR #5 was modified; nothing was merged or deployed.
