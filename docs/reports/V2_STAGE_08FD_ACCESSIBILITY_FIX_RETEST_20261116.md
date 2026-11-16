# Stage 8F-D Accessibility Fix and Retest

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `29ea75d`
**Verdict:** PASS WITH REMAINING ISSUES; targeted axe rules cleared in sampled scans.

## Fixes

- Removed the overriding `aria-label="SymTech Ventures — home"` from v2 site-brand links in ten landing pages and four article shells. The emblem remains decorative/hidden; accessible name now derives from visible brand text.
- Added a progressive `tabindex=0` only to article tables with actual horizontal overflow, updated on resize, with a visible `:focus-visible` outline. No article main content or figure changed.

## Automated retest

Temporary isolated npm cache/prefix; axe-core **4.14.1**, Python Playwright, system Chromium. `axe.run` with `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` tags ran on Home, Research, BridgePoint, Discussion Papers, Contact and Paper 1 at 390 and 1440 px (12 scans). All 12 returned **zero violations**, including the two previously reported rules. Research was also exercised at 390: Open label was observed after Enter, Escape restored focus to SUMMARY, and outside click closed the menu.

Paper 1 table at 390 received `tabindex=0`; measured scrollWidth 400/clientWidth 358. ArrowRight left scrollLeft at 0 in this check, so keyboard scrolling usability is **not confirmed** despite the axe rule clearing. At 1440 the table does not receive tabindex. Further manual keyboard scrolling review remains advisable.

## Integrated regression

`python3 -u docs/reports/scripts/v2_stage8_qa.py` — exit **0** after the website changes. It covered 36 HTML files, all four preserved papers and seven figures each, seven historic routes, 16-entry sitemap, forms/privacy states, catalogue counts, local resources and 320/390/768/1440 overflow checks. No browser errors or failed local responses; no broken references, missing alt attributes or CSS resource failures.

No screen-reader test or WCAG certification is claimed. Earthrise artwork, asset provenance and scientific accuracy of embedded paper figures remain separate owner gates. No merge or deployment.
