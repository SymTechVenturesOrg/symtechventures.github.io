# SymTech Ventures v2.0 — Stage 8F-C: Actual axe Accessibility Scan

**Prepared:** 16 November 2026 (GMT)  
**Assignment:** ONE bounded, verifiable accessibility testing pass.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Working branch and PR:** `feature/v2-space-research-website` · [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Pre-handover observed PR head:** `336b14b9442010d546e6f032185987de83e5376d`; fetch latest head at execution start, **do not assume this SHA is unchanged**.  
**Purpose:** Close the genuine automated-accessibility-evidence gap identified in [Stage 8F-B](../reports/V2_STAGE_08FB_ACCESSIBILITY_ASSURANCE_20261116.md).

## 1. One priority: run a real accessibility auditor

Stage 8F-B **did not run axe**: no `axe-core`, `@axe-core/playwright` or `pa11y` was installed. It visited six routes at 390 px and observed Research mobile-menu Escape/focus restoration, but **did not verify** the dynamic accessible label, outside-click closing, contrast, desktop accessibility, skip-link activation or screen-reader behaviour. A previous [Stage 8F-A full regression](../reports/V2_STAGE_08FA_INTEGRATED_REGRESSION_20261116.md) **passed**, so do not repeat that long run until/unless website code changes.

**This task explicitly permits one temporary, development/test-only installation of `axe-core` or an equivalent local automated accessibility checker**, subject to normal execution-environment permissions. **Do not alter production dependencies or introduce a dependency lockfile in the repository.** No purchase, secrets, user account or remote audit service is authorised.

The user alone sets Codex model/thinking effort/speed in the UI. Do not choose or change these settings inside Codex.

## 2. Suggested practical execution, with bounded fallback

1. Fetch current feature-branch head and work against its **real checked-out HTML/CSS/JS**, served locally. Preserve paper bodies, figures and all previous release constraints.
2. Check locally available tools first. If `axe-core` is already installed, use it. Otherwise, if permitted, install **only into an ephemeral directory outside the repository** (e.g. `mktemp -d`, then `npm install --prefix "$TEMP_DIR" --no-save --no-package-lock --ignore-scripts axe-core`). Record exact command, package version and whether the install succeeded. Remove the temporary directory after evidence is collected. **Do not commit `node_modules`, package manifests or caches.**
3. The existing suite uses **Python Playwright and system Chromium**. One way to audit the actual local pages is to launch Chromium through that existing Python environment, add the installed `axe.min.js` file to each visited page via `page.add_script_tag(path=...)`, then execute `axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa']}})` and record the resulting violations with id/impact/affected element/description. Check that `window.axe` genuinely loaded. You may use an equivalent established implementation; **do not fake or substitute DOM assertions for axe output**.
4. If download/package access fails, make **one bounded attempt**, capture the actual command/error, then mark automated scan **BLOCKED** and perform focused manual checks. Avoid endless retries/restarts.
5. Run scans on these **six routes at 390 and 1440 px** (12 audits), unless a documented environment blocker prevents this: `/`, `/pages/research.html`, `/pages/bridgepoint.html`, `/pages/discussion-series.html`, `/pages/contact.html` and `/articles/symmetria/symmetria-paper-01.html`. Confirm site assets load; no external production requests or forms.
6. To isolate mobile controls, evaluate the mobile disclosure both **closed and open** on Research at 390 px, scanning the open state as well where practical. Record contrast/landmark/name/aria findings by real route and width. Be cautious: automated scans have incomplete coverage; success is **not WCAG certification**.

## 3. Focused actual-browser interaction checks

On the real Research page at 390 px, check **each** of:
- Summary's **computed accessible name / `aria-label`**, not its visible `inner_text`: before opening it should be `Open navigation menu`; after opening `Close navigation menu`; after closing it returns to `Open navigation menu`.
- Keyboard open with Enter/Space; Escape dismissal and restoration of focus to the summary; ability to activate menu links; outside pointer click dismissal; no trapping or unintentional focus loss.
- Skip-to-main activation, visible keyboard focus, proper `aria-current="page"` and no horizontal scrolling/obscured links.

At 1440 px check desktop navigation/current-page highlighting, focus indicator and sensible heading/landmark structure. Record actual observed checks, not an inferred pass from source code.

Where possible, inspect body and key navigation text contrast and keyboard focus; treat automated colour contrast as evidence for eligible nodes, not a complete substitute for manual judgement. **Real screen-reader testing remains unverified unless actually conducted.**

## 4. Scope of fixes

- If genuine **small, clearly reproducible** accessibility defects are found, commit minimal safe corrections on existing feature branch **without changing the owner's dark research identity, paragraph justification or no-starfield design**. Test the corrected state with the actual auditor.
- If any website HTML/CSS/JS changes, **rerun** `python3 -u docs/reports/scripts/v2_stage8_qa.py` against the updated branch and record actual exit code. Earlier Stage 8F-A success does not validate newly altered code.
- Complex design trade-offs, research-body/figure edits, attribution/legal concerns, software features and paper mathematics are **not authorised for automatic change**. Report them for Chat and owner.
- Do **not** rewrite original paper text, delete/move its seven figures, reactivate enquiries, publish lessons, replace the missing Earthrise image, change historical `noindex,follow` pages, or claim the work is peer-reviewed.

## 5. Required GitHub deliverable — mandatory

Commit a concise, evidence-backed report to:

`docs/reports/V2_STAGE_08FC_AXE_ACCESSIBILITY_SCAN_20261116.md`

The report must include:
1. Exact starting/final Git SHAs, PR link, local test environment, package version, commands and real exit statuses; whether test-only installation was successful, failed or skipped.
2. A six-route × two-width scan matrix, and separate 390px **Research open-menu** state, with **PASS / ISSUES FOUND / BLOCKED / NOT RUN** distinguished honestly. Summarise each violation by impact, rule ID, selector, affected pages, count and specific proposed or completed fix. If zero issues for a scan, record the actual passing tool output, not an unsupported global claim.
3. Real-browser mobile disclosure accessible-name transition, Escape/focus, outside-click, skip-link and desktop current-page/focus observations.
4. Exact changed files and corrective retest outcomes; whole-site regression exit code **if website code changed**. Otherwise explicitly state full regression was not repeated and why.
5. Screenshots or output snippets only when they genuinely demonstrate an issue or pass; avoid fabricated screenshots/console logs or large raw scan dumps.
6. Remaining limitations: non-automated WCAG criteria, screen readers, owner approval; the approved Earthrise file remains missing, rights/provenance of additional historical assets and scientific claims inside SYMMETRIA figures are separate gates.
7. Final truthful outcome: **scan completed / scan completed with defects / automated scan blocked**; distinguish any true release-blocking accessibility defect and whether corrected.

**Before stopping**, fetch/read back the committed report and confirm PR #5 remains **open, draft, unmerged**, recording final SHA. If the test environment dies or time is exhausted, avoid saying “complete”: commit a candid partial/blocker report if possible and state what was and was not done.

## 6. Mandatory DTSU + COPY TO CHAT

Read the [DTSU v1.1 standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md) completely. Issue **visible user-facing** DTSUs at actual `Europe/London` time, starting at **0% before tools/work** and at truthful 10–20% whole-task milestones; include a factual ~10–20 word status and ETA every time. For long intervals, update at least every 3–5 minutes. Use `ETA unknown` if unsure. **100%** only once evidence, report and PR verification are complete.

Finish with a concise **COPY TO CHAT** containing: PR #5 URL, branch, final SHA, scanner availability and actual audited routes/widths, key findings, any site changes and full-regression outcome if rerun, report link, outstanding blockers, and confirmation that **nothing was merged or deployed**.

**Do not stop after reading the handover.** The objective is genuine audit evidence with a verified committed report or an evidenced technical blocker, not another preparation-only status.

## 7. Release protection

PR #5 **must remain draft and unmerged**. **No deployment, publication, DNS changes, live user-data submission, changes to `main`, or new PR**. Owner's permission to run a temporary dev-only scanner is **not** permission to merge or release.
