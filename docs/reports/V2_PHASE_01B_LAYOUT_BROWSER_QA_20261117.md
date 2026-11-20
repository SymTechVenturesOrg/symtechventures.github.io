# Phase 1B Layout Browser QA

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `646939692e3bff37760241f5f0fa91db1a5284a0`
**Outcome:** Full regression passed; visual spot-check evidence captured. Jump target activation is incomplete and requires follow-up before layout acceptance.

## Full regression

Command: `python3 -u docs/reports/scripts/v2_stage8_qa.py` — exit **0**. Python Playwright/system Chromium checked 36 HTML files, 27 browser route visits, responsive widths 320/390/768/1440, 16 sitemap entries, four protected paper bodies/figures, historical noindex, catalogue counts, local refs/assets, keyboard/mobile behavior and errors. Results: no local reference/alt/CSS failures, browser errors or failed local responses. Counts remained Discussion 4 online/12 planned, BridgePoint 16 planned, NSRP and SEIP 20 phases each, zero formal publications.

## Layout and jump index spot checks

Fresh Chromium viewport screenshots (not full-page) were captured at 390 and 1440 for Home, Research, BridgePoint, Discussion Papers, NSRP, SEIP, About and Contact. `docs/reports/screenshots/phase1b-<page>-<width>.png`. Full regression also covered 320 and 768 widths and detected no document overflow.

Tried keyboard focus and Enter on BridgePoint `#space-research`, Discussion `#discussion-reality`, NSRP `#proj-5` and SEIP `#proj-5` at 390. Each target existed, and no horizontal overflow was observed, but `scrollY` remained 0 after Enter in this quick check. Therefore target navigation/scroll-margin behavior is **not verified**; this may be a test activation issue and needs a real link activation observation. A first attempt used an invalid Discussion selector and timed out; corrected selector verified target existence but did not demonstrate activation. No site code was changed.

The 18 source anchor/ID pairs were previously checked in the Phase 1B source QA report, but this browser session does not establish that all 18 are operable. Phase 1 layout owner acceptance remains pending. Phase 2 imagery has not started; the approved Earthrise raster remains absent. No starfield, article/body, research-claim or lesson content changes were made.

PR #5 remains draft and unmerged. No deployment.
