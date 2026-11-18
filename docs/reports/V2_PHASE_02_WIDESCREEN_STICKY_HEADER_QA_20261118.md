# Phase 2 — 16:9 Desktop Scaling and Persistent Navigation

**Date:** 18 November 2026 (GMT)  
**Feature branch:** `feature/v2-space-research-website`  
**Code commit actually verified:** `a67ac656a5d021e162d59685d56cbfca33746ca8`  
**QA:** [GitHub Actions run #44323010928](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44323010928) — **PASS**  
**Release:** Draft PR #5 stays unmerged and undeployed.

## Owner feedback and changes

The owner reported that the website looked naturally proportioned only at 150% browser zoom, and asked to design for a modern 16:9 desktop presentation at 100% while retaining a portrait-scroll mobile site. They also asked for the primary site header to remain at the top while scrolling.

The application cannot dictate or change the user's monitor/window aspect ratio. The solution is responsive **100% zoom** layout, not CSS/browser zoom overrides and not a fixed 16:9 page height. For viewports from 1600px wide and 800px high the design now uses a wider 1480px content max, a larger brand emblem/wordmark, a readable six-link desktop navigation, scaled hero heading and lead and a full-height Earthrise hero. Mobile and other aspect ratios retain their own responsive rules, real HTML text and normal vertical page scrolling.

The header is now sticky (`position:sticky; top:0`), with sufficient stacking order, semi-opaque navy backdrop and blur. This preserves real keyboard-navigable primary links or the existing mobile `<details>` disclosure during scroll. Anchor scroll offsets were extended to avoid obscured in-page headings.

The four actual SYMMETRIA paper pages required a **separate legacy-style correction**: `css/styles.css` applies `display:none!important` to modern headers, `padding-top:82px!important` to body at desktop and `overflow-x:hidden!important`. The prior Phase 2 header restoration remains and now has all-width body padding reset and **`overflow-x:clip!important; overflow-y:visible!important`** within `body.symmetria-article-page` to prevent an unintended scrolling container from defeating sticky. This is a scoped presentation fix only: no scientific prose or figure modified.

## Test evidence

The first new scroll QA at code `424ac9f268796e37e292627d08dd95afece04158` exposed the **82px old header gap**; following revision `553f68ac5aab3c331a3ac9e54026433679020df5` exposed the legacy body scrolling container moving the header to top `-850px`. These are recorded failures, not release passes. The final code fix `a67ac656a5d021e162d59685d56cbfca33746ca8` ran the entire exact-branch workflow cleanly:

- **Original full regression:** PASS (`python -u docs/reports/scripts/v2_stage8_qa.py`, 36 HTML files, existing research and figure guards).
- **Phase 2 nine-width hero/navigation browser QA:** PASS.
- **Badge/right-arrow test:** PASS (four representative routes × five viewport widths).
- **New widescreen/sticky scroll QA:** PASS; **35 combinations** across seven page types and five window sizes: `1920×1080`, `2560×1440`, `1366×768`, `390×844`, `320×720`.
- For each of the 35 cases: actual header `position:sticky`, start and post-scroll top coordinate **0px**, page scroll `850px`, no horizontal overflow, initial response 200. Mobile disclosure opened on click and closed with Escape; desktop primary nav visible.
- GitHub Actions bundled exact-branch screenshots `home-sticky-1920x1080.png`, `home-sticky-2560x1440.png`, `home-sticky-390x844.png`, `home-sticky-1366x768.png`, regression logs, JSON data and full site ZIP. Workflow artifact: [symtech-phase2-review-a67ac656…](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44323010928/artifacts/14435313968).
- Chat-side artifact extraction and ZIP integrity verification: PASS; full-site ZIP comprises 108 files. Screenshots visually inspected at 1920×1080 and 390×844.

**Limitations:** automated Chromium at specific viewport sizes is not a physical-device or owner-monitor acceptance test, and a sticky header cannot alter physical monitor ratio. Owner should visually inspect at 100% zoom in their normal browser, particularly if OS display scaling differs from test setup.

**No merge, deployment, DNS change, paper figure edits or Phase 3 work.** This is a completed Phase 2 layout/usability polish on an unmerged draft feature branch.
