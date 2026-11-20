# SymTech Ventures v2.0 — Post-Stage 8 Owner Design Adjustment

**Date:** 16 November 2026 (GMT)  
**Status:** CSS and legacy JavaScript edits made **on the unmerged feature branch** following owner visual feedback. **Browser rerun pending.**  
**Draft PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)

## Current owner decision (supersedes previous starfield approval)

The owner prefers the clean new dark layout **without a starfield**, and requested **text justified to both left and right edges**. The original animated starfield was not to be retained. Keep the approved dark palette, gradient hero, orbital SVG illustration and usual left/natural alignment for headings/navigation/buttons.

All BridgePoint lessons remain deferred: **16 Planned titles, no individual lesson content or links**.

## Implemented on the feature branch

| File | Narrow change | Why |
| --- | --- | --- |
| `css/v2-site.css` | Removed `body::before` global CSS starfield and `.hero:before` dotted star pattern; removed associated pseudo-element stacking rules; added `main p,.site-footer p` full justification, automatic hyphenation and safe word wrapping | Remove stars in the new site while aligning longer prose to both margins |
| `js/main.js` | Removed obsolete two-canvas animated AetherOS starfield code and its invocation. Retained `smoothAnchorScroll` and `revealOnScroll`; kept original file encoding/BOM | Prevent old article and legacy shells from recreating starfield canvases or running a rendering loop |
| `css/styles.css` | Added prose justification for preserved articles/legacy pages; excluded article header author/date/series metadata | Apply requested alignment without touching original paper bodies or visual titles |

**No HTML page, paper body, figure, paper URL, contact-form handler or CNAME was changed by this design adjustment.**

## Verified source-level checks after edits

- Fetched and compared the revised `css/v2-site.css`, `js/main.js` and `css/styles.css` from GitHub against the exact committed content.
- `css/v2-site.css`: removed global and hero star patterns; balanced opening/closing CSS braces; includes `text-align:justify`, `text-justify:inter-word`, `hyphens:auto` and `overflow-wrap:break-word` for running prose.
- `js/main.js`: parsed successfully using JavaScript's `Function` parser in the verification environment; contains no canvas creation, animation loop or starfield invocation; smooth anchor scrolling and scroll reveal functions remain.
- `css/styles.css`: contains the new scope-limited legacy/article prose rule.
- Independently compared each of the four article Git blobs with the **Stage 8 QA head's recorded post-skip-link hashes**; all four are exactly unchanged from Stage 8:
  - Paper 1 `a9d89172a6549b5a26451f2745f1d032659dd32e`
  - Paper 2 `5c94104eef059a18f202768df99591e3050ba50d`
  - Paper 3 `07395d1d309dbe113ca2ed43ebf4bb633af2162f`
  - Paper 4 `0d259414c78c9e1bc8ddaf60f8832a81607b2141`

## Outstanding test and release boundary

**No new browser screenshots or complete Chromium/Playwright regression were generated for the post-QA CSS/JS changes.** The original [Stage 8 QA report](V2_STAGE_08_WEBSITE_QA.md) covers the earlier code, not this modified version. Re-run its [reproducible QA script](scripts/v2_stage8_qa.py) on the latest branch, inspect 320px/390px justified text for excessive spacing or overflow, confirm no canvas stars on a preserved article/legacy page, and capture fresh desktop/mobile screenshots before relying on visual acceptance.

Stage 8 ended **Not ready for owner release review** owing to independent unresolved concerns:
1. Legacy third-party contact/enquiry privacy disclosure and anti-spam handling (form not submitted).
2. Policy for search indexing of preserved historical divisions/founding-fellows pages.
3. Rights/provenance for existing logo and scientific illustrations, including embedded formula checks.
4. The LinkedIn link returned HTTP 999 from the test environment; that does not prove the destination is invalid.

**These issues are not solved by typography/starfield changes.** PR #5 must remain open, draft, unmerged and undeployed pending a new verified QA pass and separate owner decisions.
