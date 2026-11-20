# SymTech Ventures v2.0 — Stage 8F-E: Final Table Keyboard-Scroll Verification

**Prepared:** 17 November 2026 (Europe/London)  
**Objective:** One finite keyboard-usability check and, **only if reproduced**, one narrow repair.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Existing PR:** [#5, draft](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Branch:** `feature/v2-space-research-website`  
**Previous verified feature head:** `accd1d642d8f1a9911f179ea7c8018a2e2c3f70c`; fetch latest head before work.  
**Starting evidence:** [Stage 8F-D report](../reports/V2_STAGE_08FD_ACCESSIBILITY_FIX_RETEST_20261116.md).

## Why this pass is necessary

Stage 8F-D corrected two serious findings and reported **axe-core 4.14.1: zero violations on 12 scans** across six routes at 390/1440px, plus `python3 -u docs/reports/scripts/v2_stage8_qa.py` **exit 0**. Original paper bodies and figures were preserved.

One **actual functional uncertainty** remains: on Paper 1 at 390px the overflowing `table` received `tabindex=0` (scrollWidth 400, clientWidth 358), yet a simulated **ArrowRight** press left `scrollLeft=0`. An axe `scrollable-region-focusable` pass confirms focusability, **not usable horizontal keyboard scrolling**. Do not declare accessibility sign-off while this remains uninvestigated.

The previously reported Research menu accessibility test says the Open label was observed, but its wording does not explicitly establish **Close** immediately after opening in Stage 8F-D; Stage 8F-C separately observed the transition. Confirm it quickly in this pass without creating a new broad audit.

## Finite work plan

1. Read [Stage 8F-D report](../reports/V2_STAGE_08FD_ACCESSIBILITY_FIX_RETEST_20261116.md), [Stage 8F-C scan report](../reports/V2_STAGE_08FC_AXE_ACCESSIBILITY_SCAN_20261116.md) and the shared implementation `js/v2-navigation.js`/`css/v2-articles.css`. Check out actual feature branch; record starting SHA; avoid conflicting concurrent writes.
2. Use the **real checked-out site** via local HTTP and Playwright/Chromium, **not** a synthetic table harness. At 390px (and 320px if materially different), locate Paper 1's genuinely overflowed table. Record scrollWidth, clientWidth, scrollLeft, document.scrollX, activeElement and viewport. Focus it via real keyboard Tab navigation where feasible, then perform **ArrowRight multiple times**, allowing a short observation interval, and **ArrowLeft**. Assert that the **table's own `scrollLeft` increases and can return**, and that focus stays visible and page does not horizontally overflow. Check at 1440px that a non-overflowing table is **not** an extra tab stop.
3. If the first test shows no movement, **diagnose first**: verify actual focus, key event target, overflow dimensions, scroll timing, CSS interference and whether the page/another container scrolled instead. Do not infer a defect solely from one instantaneous `scrollLeft` read.
4. **Only if keyboard scrolling genuinely fails:** implement the smallest safe change in shared v2 JS/CSS so **ArrowLeft/ArrowRight on the focused, overflowing table** moves the scroll container; scope any keyboard handler to the exact overflow table, respect standard focus semantics and reduced-motion settings, and do not hijack normal keyboard navigation elsewhere. Consider conditional scrolling only after observing that the native browser behaviour is insufficient. Re-run the keyboard test after the fix. Preserve all original article main text, table cells, figure references and science content unchanged.
5. Check a representative table (if any) in each of Papers 2–4 to ensure conditional focus treatment works and does not add spurious desktop tab stops. At Research 390px, inspect the **actual computed `aria-label`** Open -> Close -> Open across menu toggle, and confirm Escape returns focus and outside click dismisses.
6. If website code changed, re-run the **exact whole-site regression** `python3 -u docs/reports/scripts/v2_stage8_qa.py` and a **focused real axe-core audit** at least on Paper 1 at 390/1440 and Research mobile menu open (use temporary npm cache and prefix if required). If no website code changed, do not repeat all 12 previous scans or the full regression unnecessarily; cite the existing 8F-D results and state that no new code was introduced.
7. Keep any change narrow and inspect diff. **No** modifications to protected SYMMETRIA paper main content or original seven figures per paper, 16-entry sitemap, historic noindex pages, contact/enquiry suspension, content counts, artwork, release settings or research claims.

## Deliverable and acceptance

Commit a short, precise report on the **same feature branch and PR #5**:

`docs/reports/V2_STAGE_08FE_KEYBOARD_TABLE_SCROLL_VERIFICATION_20261117.md`

Include:
- Starting and final SHAs, commands and actual browser/tool versions.
- At 390px, **before/after focus, table `scrollLeft` and keypress data**, with timing/diagnostic details. Describe actual direction/amount or legitimate blocker; not just `tabindex` present.
- Desktop 1440px non-overflow/tab-order outcome, other-paper spot-check results, Research Open/Close and focus observations.
- Exactly which files changed (or **none**), whether a code fix was needed, and a genuine **PASS / FAIL / BLOCKED** for keyboard scrolling.
- If code changed: actual full regression command/exit code and focused axe result. If not: refer to Stage 8F-D prior passed full regression and 12 zero-violation scans; do **not** imply those were rerun.
- Outstanding screen-reader, full WCAG, original image provenance/Earthrise/physics-figure review constraints; **zero axe violations is not WCAG certification**.

Before finishing, **read back the committed report** and fetch PR #5 again to verify open/draft/unmerged at the final commit. Provide brief **COPY TO CHAT** with report link, exact results and remaining blockers.

## Operating safeguards

No merge, deployment, publication, DNS change, main-branch edit, PR status change or enquiry submission. Do not invent missing Earthrise art or rewrite scientific paper claims. Never silently patch a figure or research body. Only the owner controls Codex's model, effort and speed.

## Mandatory DTSU

Follow [DTSU v1.1](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md): visible **0% update before tools/code**, true Europe/London `HH:MM:SS` timestamp, factual progress and ETA at 10–20% milestones and every 3–5 minutes during a long step; 100% only after committed report and PR verification. Do not invent elapsed times or claim a finished browser test without its output.

This is **not** authorisation for any other stage or release. Stop after final handback.
