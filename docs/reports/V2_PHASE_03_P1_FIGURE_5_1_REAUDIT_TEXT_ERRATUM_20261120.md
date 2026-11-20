# SYMMETRIA — Paper One Figure 5.1: Specific Erratum to Independent Re-Audit Description

**Date:** 20 November 2026 (Europe/London).  
**Purpose:** Correct a *factually inaccurate description of pixels in an existing independent QA report*, without amending the independent report after the fact or changing any artwork or website text.

## Exact source, independent identity check

- Canonical owner-visually-approved image: `docs/artwork/owner-approved/paper-one/P1_Figure_5_1_OWNER_VISUALLY_APPROVED_1920x1080.png`.
- First GitHub import commit: `c6f60ee180c2f5d401b0f597f512898c010981a9`.
- Source/GitHub readback SHA-256 verified in independent manifest: `945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c`.
- This exact same 1920×1080 RGB PNG was locally reopened and its full-file SHA-256 recalculated to match the GitHub manifest during post-audit review.
- Related independent re-audit report: [P1 Figure 2.1/3.1 science re-audit and 1.1 decision](V2_PHASE_03_P1_FIGURES_2_1_3_1_INDEPENDENT_SCIENCE_REAUDIT_AND_1_1_CAPTION_DECISION_20261120.md), Git blob `5c42722a10dd7c0471df9f5e22e7fd536ec77265`, committed at `48e071e80d7842518c8ee8847fa5d187b61c262b`.

## Inaccurate re-audit statement

The re-audit's `Website source, captions and source-hash discrepancy` section states:

> The Figure 5.1 artwork itself contains declarative in-image statements (for example, “Symmetry is fundamental” and “Nilpotent balance underlies nature”).

**This attribution is contradicted by the exact source PNG.** Neither quoted statement appears in the approved Paper One Figure 5.1 image. No substantive `nilpotent` phrase appears in the image's four main concept panels.

### Actual readable image content (verified visually)

**Title:** `Could Deeper Organisation Underlie Physics?`  
**Subtitle:** `An exploratory perspective on what might connect the fundamental laws`

**Main concept panels:**

1. `SYMMETRY` — “Could deeper symmetries be the key to unifying the fundamental forces of nature?”
2. `INFORMATION` — “Might information be a fundamental physical ingredient of reality, as basic as matter and energy?”
3. `CONSTRAINT` — “Could simple, universal constraints guide which physical laws and structures can exist?”
4. `ORGANISATION` — “Might the universe emerge from a deeper, self-consistent organisation that gives rise to space, time, matter and the laws of physics?”

**Bottom epistemic caution:** `Exploratory hypothesis — not established physics.`

All four scientific propositions in the concept panels are phrased as **questions**, not factual statements. The scientific caution remains necessary because they are exploratory proposals, but the inaccurate sentence above should **not** be cited as a finding that this specific approved image makes the two quoted unconditional assertions.

## Correct interpretation and remaining task

- **Preserve Figure 5.1 original PNG unchanged.** Its four-question formulation and footer satisfy the locked exploratory visual requirement at the review level; there is no verified basis from this discrepancy alone for another image edit.
- **Still amend its external HTML caption** in a future separately authorised website integration to identify the proposal explicitly as **untested**, as the prior science QA already recommended. A suitable independent-caption opening is: `SYMMETRIA presents the following as an untested hypothesis: reality may emerge ...`
- Keep the caption and detailed accessible HTML description independently meaningful for readers who cannot inspect embedded PNG text. The description should explain the four panels as proposed questions, not as proven emergence laws.
- This erratum **does not** change the original independent report, change its other verified 1.1/2.1/3.1 scientific decisions, waive the future website/source-to-caption matching requirement, or authorise HTML/asset modifications.

**File scope:** Documentation-only on the correction branch; no image binaries, original hashes, current website or PR #5 modified; PR #9 and #10 remain draft and unmerged.
