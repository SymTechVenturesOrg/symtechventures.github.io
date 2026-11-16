# SymTech Ventures v2.0 — Stage 8E Navigation Usability and Accessibility

**Date:** 16 November 2026 (Europe/London)  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Implementation PR:** [#5 — draft](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Starting feature commit:** `15fb02f53a11a79887c61a2b6174b1b557279ac8` (Stage 8D)  
**Feature commit after code changes:** `d0e36ee52301211f458a00f5acae7628d70e8e12`  
**Scope:** Shared navigation styling, homepage current-page semantics and mobile native disclosure behaviour; **no merge or deployment**.

## Issue discovered

The shared stylesheet selected `.main-nav a:first-child{color:#fff}`, which highlighted **Home** on every site page, regardless of which page was active. Other landing pages already had `aria-current="page"` on the correct primary and mobile navigation entries, but the homepage's own two Home entries were missing it. The mobile `<summary>` also used an unchanging `aria-label="Open navigation menu"` even after opening, and the menu did not close when the user tapped outside.

## Changes committed

| File | Change |
| --- | --- |
| `index.html` | Adds `aria-current="page"` to **Home** in both primary and mobile navigation. All existing page content, research claims, article links and metadata remain unchanged. |
| `css/v2-site.css` | Replaces always-active first-child styling with `.main-nav a[aria-current="page"]`, using a restrained gold underline. Mobile current-page links now have a subtle highlighted background/inset marker. |
| `js/v2-navigation.js` | Synchronises the native `<details>` summary's accessible label with the actual open/closed state; retains Escape dismissal and focus return; closes on a pointer tap outside the mobile menu. |

Other primary routes already had two `aria-current="page"` markers (desktop/mobile) for their appropriate navigation destination, including the Research dropdown pages mapping back to Research. The Contact page is footer-reachable and intentionally not a seventh primary navigation item.

## Verification performed

### GitHub exact-branch scope check — PASS

Used GitHub's compare endpoint for starting commit `15fb02f53a11a79887c61a2b6174b1b557279ac8` and code commit `d0e36ee52301211f458a00f5acae7628d70e8e12`. The comparison shows **exactly three files changed:** `index.html`, `css/v2-site.css`, `js/v2-navigation.js`; no research articles, existing image files, `sitemap.xml`, `CNAME`, Contact/Enquiry pages, or research programme catalogue files were changed by the code pass.

### Chromium behavioural component smoke test — PASS

Ran an actual local Playwright/Chromium browser test using the **new shared JavaScript code** and a **minimal representative HTML/CSS navigation harness** with the same native `<details>`, summary, desktop/mobile nav and active-link selectors at:

- **320 px:** current-page links, initial Open label, click-to-open/Close label, Escape-to-close/focus restoration, outside-click dismissal and browser JS error check passed.
- **390 px:** same checks passed.
- **768 px:** current-page selectors and no browser JS errors passed.
- **1440 px:** current-page selectors and no browser JS errors passed.

Chromium was launched locally via the installed Python Playwright package and system Chromium binary. **This is a component-level interaction test, not a full exact-branch end-to-end rendering of every website route.** Full GitHub repository checkout was not available in the execution container, so no exact-site browser screenshots or integrated QA-run results are claimed from this Chat pass.

## Remaining requirements

- The [Stage 8C regression](V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md) was last run before the Stage 8D/8E changes. Run the **exact-branch full** `python3 docs/reports/scripts/v2_stage8_qa.py` in Codex or a complete checkout before release.
- Automated axe-core/equivalent accessibility testing and screen-reader review remain outstanding. This pass improves nav usability but does not certify WCAG conformance.
- The approved Earthrise raster still needs its **actual file** supplied and integrated if retained in the owner-approved release design. No substitute image was introduced.
- The owner attested ChatGPT generation for the 28 SYMMETRIA figures and six shared logos. Remaining historic-image origins and scientific claims embedded in selected diagrams still require a separate Stage 9 decision.

**Stage 8E: source change and focused component interaction tests PASS; final release remains blocked pending full integration tests and owner approvals.**
