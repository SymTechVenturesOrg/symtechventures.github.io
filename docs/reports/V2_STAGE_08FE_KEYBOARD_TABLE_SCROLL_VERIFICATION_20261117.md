# Stage 8F-E Table Keyboard-Scroll Verification

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `a124f998bed206232f1db32dbe986dbf5abc163c`
**Outcome:** PASS; no code change required.

## Paper 1 table

Used Python Playwright and system Chromium against the real local checkout over HTTP on 17 November 2026. At 390×844, Paper 1's first table measured `scrollWidth=400`, `clientWidth=358`, `scrollLeft=0`, `tabindex=0`. Focusing the table produced active element `TABLE` and a solid focus outline. ArrowRight moved the table's own `scrollLeft` to 40, then 42 after a second press; ArrowLeft returned it to 2. `document.documentElement.scrollLeft` stayed 0, confirming the table itself moved and the page did not.

At 1440×900, the table measured `scrollWidth=940`, `clientWidth=940` and had no `tabindex`, so it is not an unnecessary desktop stop.

## Navigation spot check

Research at 390×844: summary accessible label was `Open navigation menu`; Space opened it and changed the label to `Close navigation menu`; Escape closed it, restored `Open navigation menu`, and returned focus to `SUMMARY`. Outside pointer click closed the disclosure. The menu behavior is from a separate live browser run; on that check the label after `Enter` was sampled before its asynchronous update, so Space with a short wait was used to verify the transition.

## Scope and limitations

No source files changed. Papers 2–4 were not separately table-keyboard tested in this finite pass. The Stage 8F-D full regression (exit 0) and 12 axe scans (zero findings) remain prior evidence; they were not rerun because no website code changed. Full screen-reader testing, WCAG certification, Earthrise asset provenance and scientific figure review remain outstanding. No merge or deployment.
