# Phase 2 — Owner-requested removal of redundant paper return buttons

**Date:** 17 November 2026 (GMT)  
**Scope:** The four **available** SYMMETRIA Discussion Papers (01–04) only  
**Decision:** Owner approved the Phase 2 website design, with one final change: the large “Back to SYMMETRIA Discussion Series” button at the bottom of each paper is redundant.

## Surgical edit

- Removed the complete `<!-- AETHEROS:PARENT_NAV:START -->` to `<!-- AETHEROS:PARENT_NAV:END -->` section from each available paper's main block. **No article prose, figures, captions, paper URL or next-paper teaser was changed.**
- Each of the four available papers already has a normal **Discussion Papers** link in its modern footer and six-link top-level website navigation, so the button duplicated an existing route.
- The 12 **planned** papers (05–16) were deliberately not edited. Their placeholder pages have a distinct legacy footer without a direct Discussion Papers link; their only dedicated “Back” button remains useful. They are not represented as available publications.
- The regression's original-paper integrity gate now removes exactly the same marked section from the immutable `origin/main` expected main before performing the complete body equality check. This is **not a relaxation allowing arbitrary edits**: the new main still must match its original byte-for-byte after the specific owner-requested deletion.
- Draft-only GitHub Action path filters now include `articles/symmetria/**` so this editorial UI cleanup triggers real browser regression and visual screenshots.

## Acceptance

1. Exactly four buttons removed from the available papers; their footer **Discussion Papers** links remain, as do the previous/next teaser and all seven images per paper.
2. Full exact-branch GitHub Actions run exits successfully, including the preserved paper content/caption/figure assertions and responsive page checks.
3. Review the updated article screenshots or independently browse Paper 2. No further Phase 2 visual changes assumed.
4. PR #5 stays draft and unmerged, no deployment, no Phase 3 scientific-figure corrections. A later owner decision governs merge/release.

**Evidence:** Await the GitHub Actions run on the final Phase 2 polish commit; prior Phase 2 QA exits cannot be reused for this changed main block.
