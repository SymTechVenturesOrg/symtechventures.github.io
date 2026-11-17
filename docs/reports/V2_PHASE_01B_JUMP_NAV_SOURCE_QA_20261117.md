# SymTech Ventures v2.0 — Phase 1B First Layout Change: Long-Page Jump Navigation

**Date:** 17 November 2026 (GMT)  
**Implementation:** existing [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), branch `feature/v2-space-research-website`  
**Status:** **SOURCE CHECK PASS; REAL BROWSER AND FULL REGRESSION STILL REQUIRED**  
**Starting source baseline:** `77f82a0f9169978db6d6996ce5b0160c34da2e01` (prior Stage 8F-E report)  
**Implementation CSS commit:** `fba9e9f8452fc11209abe760fb0b9ef1e27b28c4`.

## Purpose

Phase 1 of the [layout-first workplan](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md) begins with a small, reversible improvement identified during source/screenshot audit: reduce long scrolling journeys on the **BridgePoint, Discussion Series, NSRP and SEIP** pages. This is **not** a site redesign or the start of image generation.

## Implemented

| File | Change |
| --- | --- |
| `pages/bridgepoint.html` | Accessible `nav` index with four short category links and matching stable section IDs |
| `pages/discussion-series.html` | Accessible `nav` index for four discussion-paper groups and matching stable section IDs |
| `pages/nsrp.html` | Accessible `nav` index for five existing named `proj-1` … `proj-5` targets |
| `pages/seip.html` | Accessible `nav` index for five existing named `proj-1` … `proj-5` targets |
| `css/v2-programmes.css` | Small responsive dark-panel styling for `.section-jump-nav`, visible link focus from global CSS and sensible scroll targets. The links wrap rather than overflow at narrow widths |

The index has a real `aria-label`, visible `Jump to` text, ordinary anchor semantics and **no JavaScript dependency**. Existing page headings and planned-status wording were not rewritten.

## GitHub source readback: PASS, limited scope

- Fetched/read back all five changed source files from the feature branch after commit.
- Checked **one** `section-jump-nav` per page.
- Checked **18 links** have targets and **each matching ID appears exactly once** in its page.
- Verified the structural catalogue counts remain unchanged by this insertion: **BridgePoint 16 Planned lesson cards; Discussion Series 16 paper cards; NSRP five projects / 20 phases; SEIP five projects / 20 phases**.
- The revised CSS has balanced `{}` delimiters; this is **not** a CSS parser/browser test.
- None of these four pages acquired an `<img>`; **no image generation or integration has started**.
- **No paper HTML**, original SYMMETRIA main content, paper graphics, background starfield, status labels, contact forms or production configuration was edited.

## Mandatory unperformed QA

**A full `python3 -u docs/reports/scripts/v2_stage8_qa.py` run HAS NOT been performed on the modified feature head.** The prior Stage 8F-D regression/axe success applies to the earlier source. These new changes require fresh exact-branch tests before any Phase 1 layout approval.

Next Codex pass must:
1. Run full regression with actual exit code and real browser checks for anchor focus/scroll/navigation at 320/390/768/1440.
2. Take fresh current-feature desktop and mobile screenshots to assess homepage, long pages, Research/About/Contact and overall layout.
3. Check newly added `nav` landmarks, keyboard focus/anchor semantics and axe regressions where appropriate.
4. Produce a concise evidence report. Fix only reproducible minor layout defects; **do not weaken test coverage**.
5. Keep PR #5 open/draft/unmerged and report exact final SHA. No merge or deployment.

**Phase 1 status:** design audit completed; **small first layout change implemented but unverified in browser**; full layout approval and Phase 2 imagery remain on hold.
