# SymTech Ventures v2.0 — Stage 8F-D: Fix Two Axe Findings and Retest

**Prepared:** 16 November 2026 (GMT)  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Feature branch:** `feature/v2-space-research-website`  
**Existing draft PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Verified starting head before this handover:** `e38fa99f18c0a6fb85f1f90501b8779a9487a6ad`; fetch and record the **actual latest PR head** at task start.  
**Task:** Narrow accessibility remediation + genuine axe/Playwright retesting. **Not** release approval.

## 1. Evidence and acceptance goal

Read these before coding:
- [Stage 8F-C automated scan and recovery report](../reports/V2_STAGE_08FC_AXE_ACCESSIBILITY_SCAN_20261116.md): axe-core **4.14.1**, 12 scans at 390/1440 px, **two distinct serious findings**, not yet fixed.
- [Stage 8F-A full regression](../reports/V2_STAGE_08FA_INTEGRATED_REGRESSION_20261116.md): previous exact-branch `python3 -u docs/reports/scripts/v2_stage8_qa.py` returned exit 0 **before** this task.
- [Stage 8E navigation improvement](../reports/V2_STAGE_08E_MOBILE_NAVIGATION_ACCESSIBILITY_20261116.md).
- [DTSU v1.1 standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md).

**Success requires both originally reported axe findings to be absent on the corrected real site, confirmed by repeat browser scans**, with the existing full regression still passing after any source changes. An axe scan alone cannot certify WCAG compliance.

## 2. Defect A: `label-content-name-mismatch` on `.brand`

The exact repository source has a branded header link similar to:

```html
<a href="../index.html" class="brand" aria-label="SymTech Ventures — home">
  <span class="brand-emblem" aria-hidden="true">S</span>
  <span><span class="brand-name">SymTech Ventures</span>
  <span class="brand-description">Independent research project</span></span>
</a>
```

The visibly rendered branding text includes **SymTech Ventures** and **Independent research project**, which is not reflected in the current `aria-label`. axe-core reported a **serious accessible-name/visible-label mismatch on all six audited routes at both widths**.

**Preferred minimal correction:** remove the overriding `aria-label` from the branded link in each appropriate site-shell/header source, allowing its *visible link text* to form the accessible name naturally. Confirm the decorative `S` emblem remains `aria-hidden="true"`. If an explicit accessible name is justified, it **must contain the visible text in order**, without false navigation wording; verify with axe/Playwright, not guesswork. Do **not** rely solely on JavaScript removal of `aria-label` if simple semantic HTML correction is possible.

Audit all current v2 pages and paper shells for the same `.brand` mismatch, not just the six sampled pages. Change only header-shell markup; **no alterations to original scientific paper `<main>` body content or figures**. Preserve other link semantics/URLs and desktop/mobile navigation.

## 3. Defect B: `scrollable-region-focusable` on Paper 1's mobile table

On `/articles/symmetria/symmetria-paper-01.html` at 390 px, axe-core reports a **serious `scrollable-region-focusable`** violation on a `table`: article stylesheet uses `display:block;overflow-x:auto` on paper tables, but the horizontal scrolling element cannot receive keyboard focus.

**Implement a small, accessible solution for affected overflowing tables** that:
- Enables keyboard focus and horizontal keyboard scrolling on the actual scroll region at mobile width, with a **clearly visible focus indicator** (for example targeted `:focus-visible` CSS). Validate that the fix does not introduce unnecessary tab stops on non-overflowing desktop tables or compromise table semantics.
- Protects the full, original **paper HTML main/body and all seven figures per paper**. Do not insert or remove article text, change table cell contents, rewrite prose, remove figures, or alter scientific assertions. A narrowly scoped progressive enhancement in already-shared site JS (e.g. assign `tabIndex=0` only where scrollable tables actually overflow, recalculating on relevant resize) with targeted article styling may be preferable to modifying the protected original table markup. The implementation choice must be tested against the exact real checkout, including 390/1440.
- Consider whether other paper tables are affected; apply only where technically appropriate. Avoid a generic `tabindex` on every table regardless of overflow.

For the table, verify: focused by Tab at 390, visible focus, actual horizontal scroll on arrow keys or equivalent native keyboard interaction, and intact table content/semantics. At 1440, verify no unnecessary focusable region if the table does not overflow.

## 4. Actual test execution (not source-only confirmation)

Use the current checked-out feature branch and local server, existing Playwright/system Chromium. As done in 8F-C, install axe-core into an **ephemeral directory outside the repository** with its own npm cache. A proven pattern was:

```sh
AUDIT_TMP=$(mktemp -d /tmp/axe-stage8fd.XXXXXX)
mkdir -p "$AUDIT_TMP/npm-cache" "$AUDIT_TMP/pkg"
NPM_CONFIG_CACHE="$AUDIT_TMP/npm-cache" npm install --prefix "$AUDIT_TMP/pkg" --no-save --no-package-lock --ignore-scripts axe-core
```

Capture real version and exit codes; reuse a working existing temporary installation if available, but **do not assume it persisted**. Do not commit node packages/caches/lockfiles. Stop and disclose actual blockers if the environment cannot complete scans.

- Re-run **real `axe.run`**, WCAG 2.0 A/AA and 2.1 A/AA tags, at **390 and 1440 px** on Home, Research, BridgePoint, Discussion Papers, Contact and Paper 1 (12 scans), plus **390px Research mobile-menu open state**. Record counts, rule IDs, impacts and selectors for any remaining/new violations. Do not claim zero issues without actual scanner output.
- Real browser verify brand link's computed accessible name contains visible text, no label mismatch, and navigation still points to the homepage.
- Real browser verify research table's keyboard focus, visible outline and scroll interaction at 390, plus width/viewport behaviour at 1440; do not treat `tabindex` presence alone as proof of usable keyboard scrolling.
- Confirm mobile menu Open/Close accessible names, Escape/focus restore, outside click and skip link at 390; active page on desktop at 1440.
- **Because website source changes are required, rerun the full integrated script**: `python3 -u docs/reports/scripts/v2_stage8_qa.py`; capture actual exit code and counts. Preserve all old safeguards: four paper main blocks/seven figures each, zero forms, historic noindex and sitemap, programme counts, navigation, media resources, responsiveness, no starfield and zero formal publications. If any check fails, record and diagnose instead of weakening it.
- Document actual HTML/CSS/JS changes and check the diff is limited to appropriate shared-shell branding and narrow table-focus enhancement. If anything changes inside a protected paper body, stop and raise for owner approval rather than silently commit.

## 5. Deliverables, scope and PR safeguards

Commit one report at:

`docs/reports/V2_STAGE_08FD_ACCESSIBILITY_FIX_RETEST_20261116.md`

Include exact starting/final SHA, changed-file list, concise before/after findings matrix, real scanner version/commands/exit codes, scan route/viewport outcomes and Research open-menu check, keyboard/table evidence, **full regression rerun** command/exit status, screenshot evidence where materially useful, unresolved WCAG/screen-reader scope and other release blockers. Use a true **PASS / PASS WITH REMAINING ISSUES / BLOCKED / FAIL** verdict, with no blanket WCAG certification.

Modify only existing PR #5 feature branch; **no separate PR**, no merge, no deployment, no DNS changes, no writing to `main`, no publishing, no form re-enablement, and no Earthrise asset invention. No changes to original SYMMETRIA research main content/figures or independent research claims; 28 original paper images/six shared logos have owner-attested ChatGPT generation, but other historical asset rights and scientific figure accuracy remain owner review gates.

At the end fetch/read back the committed report and verify PR #5 is **still open, draft, unmerged** with final SHA. If not all checks completed, say exactly what remains rather than falsely report completion.

## 6. DTSU and COPY TO CHAT

Follow the linked **DTSU v1.1** precisely: visible `[HH:MM:SS] NN% — factual brief status; ETA ...` from **real Europe/London local time**, 0% before coding/tools, then truthful 10–20% milestones and at least every 3–5 minutes; never fabricate times or progress; 100% only after GitHub report and verification.

Finish with concise paste-ready **COPY TO CHAT**: PR #5 URL, branch, final SHA; exact two fixes and real before/after axe results; full regression actual exit code; report link; any blocked/unverified accessibility criteria and owner release gates; confirmation of no merge/deployment. **Stop after the handback.**
