# SymTech Ventures v2.0 — Stage 8F-B: Focused Accessibility Assurance

**Prepared:** 16 November 2026 (GMT)  
**Status:** Ready for a **short, finite Codex engagement**; not a release approval.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Working branch:** `feature/v2-space-research-website`  
**Existing PR:** [#5 — draft, unmerged](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Verified pre-handover head:** `db3a92d92d327ded3a83e020495ea99261ca8ad4` — fetch and record the *actual latest* head when beginning.  
**Completed precursor:** [Stage 8F-A integrated regression](../reports/V2_STAGE_08FA_INTEGRATED_REGRESSION_20261116.md) — Codex reported `python3 -u docs/reports/scripts/v2_stage8_qa.py` **exit 0**, 36 HTML files, viewports 320/390/768/1440. **Do not needlessly repeat that whole regression unless site code changes.**

## 1. One objective only

Conduct **an automated accessibility scan if reasonably achievable**, plus a documented, targeted manual/keyboard review of key live *local-checkout* website routes. Commit one useful report and stop.

The purpose is to address the **specific verification gap** left by Stage 8C/8F-A: axe-core or an equivalent was not run. Successful HTML regression and missing-alt checks do **not** establish accessibility conformance.

**The project owner selects the Codex model, thinking effort and execution speed before running it.** Codex cannot choose or change those settings. Do not request any model or effort adjustment.

## 2. Read the evidence and preserve design decisions

- [Stage 8F-A result](../reports/V2_STAGE_08FA_INTEGRATED_REGRESSION_20261116.md)
- [Stage 8E native mobile menu and current-page highlighting](../reports/V2_STAGE_08E_MOBILE_NAVIGATION_ACCESSIBILITY_20261116.md)
- [Stage 8C accessibility limitation](../reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md)
- [Existing full regression script](../reports/scripts/v2_stage8_qa.py)
- [DTSU v1.1 project communication standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md)

Visual constraints: restrained professional dark research website; **no starfield**; paragraphs **fully justified**, while headings/navigation remain naturally aligned; preserve reduced-motion behaviour. Original four paper bodies and figures are protected; conceptual theories must not be presented as empirically proven.

## 3. Bounded scan and manual checks

1. Check out/fetch the **current existing feature branch and PR #5**, record starting Git SHA; do not overwrite changes from another contributor.
2. Inspect available **offline/local** accessibility tools first: an already installed `axe-core`, `@axe-core/playwright`, `axe-playwright`, `pa11y`, equivalent browser-check package, or accessible approved runtime tooling. If none exists, make **one bounded ordinary attempt** at reversible, dev/test-only package setup *when environment/policy permits*; no large production dependency changes, secret keys, browser extensions requiring personal accounts or external audit services. Record exact installation outcome. If tooling cannot run, report **automated audit BLOCKED**, then **continue manual checks**; do not invent a pass or repeatedly restart environments.
3. Use an actual Chromium/Playwright browser against the local **checked-out site**, not a self-contained synthetic component. Audit at least these **six routes**: `/`, `/pages/research.html`, `/pages/bridgepoint.html`, `/pages/discussion-series.html`, `/pages/contact.html`, and `/articles/symmetria/symmetria-paper-01.html`. Evaluate **390 and 1440 px** if automated tooling is available; use 320 px as a focused mobile-menu/overflow check if needed.
4. Record **actual tool and version, ruleset/standard, route and width, per-route violations/impact, representative offending selectors and practical fixes**. Pay particular attention to text/background contrast (including muted/status text and links), heading hierarchy, page title and language, landmark structure, link accessible names, skip link, unique IDs, img alt, SVG decoration, input/form safety, mobile menu open/closed label, keyboard focus and target size. Avoid presenting colour-contrast numerical claims unless based on actual measurements.
5. Manually test at least: keyboard Tab from address bar to skip-to-main; visible focus; mobile menu open label and Close label after opening; Escape closes and returns focus to summary; tapping/clicking outside closes; menu links and current-page state; links on paper navigation; no keyboard trap. Document exactly which assertions were observed in a real browser and which were inferred from markup.
6. Fix **only small, reproducible and high-confidence accessibility defects** (e.g., missing accessible name, focus style, obvious contrast deficiency) *within the existing design*. If doing so changes website HTML/CSS/JS, commit narrow changes and **rerun `python3 -u docs/reports/scripts/v2_stage8_qa.py`** to preserve the previously passing integrated baseline, reporting actual exit code. If no site code changes, **do not rerun the entire 8F-A regression just for repetition**.
7. For complex, disputed or science/editorial-sensitive issues (rewriting figures, paper prose, licensing, brand design) **record a proposed fix for Chat/owner instead of editing**. Report both genuine accessibility defects and scanning-tool limitations, with severity and evidence.

## 4. Mandatory deliverable and stopping rule

Create and commit exactly one concise verification report, plus only any necessary minimal fixes:

`docs/reports/V2_STAGE_08FB_ACCESSIBILITY_ASSURANCE_20261116.md`

The report must contain:
- Branch, original and final SHA(s), PR link and operating environment.
- Automated-tool availability/setup outcome; exact commands, results, versions and **PASS / FAIL / BLOCKED** status. Use `BLOCKED` rather than a fabricated success if the scanner was unavailable.
- Six route × two viewport result matrix if automated scanning ran (or candid coverage matrix if incomplete). Distinguish scanner violations, manual findings and incomplete/untested aspects.
- Focused real-browser keyboard/menu check results with actual evidence; screenshots only where they substantiate an observed issue or correction.
- Severity-ranked findings, exact affected routes/selectors, whether fixed, and any outstanding manual screen-reader and accessibility limitations. **Do not claim WCAG certification or actual screen-reader testing unless performed.**
- Exact regression rerun command and exit status **if** website code was changed.
- Explicitly separate **owner-dependent** blockers: missing approved Earthrise image, source/rights exceptions for other historical graphics, and scientific accuracy of illustrations. Original 28 paper figures and six shared logos were attested by the owner as ChatGPT-generated; that is **not** a physics validation or full licence audit.
- An overall verdict: **Accessibility scan PASS / issues found / audit blocked**, and whether any discovered accessibility defect is a release blocker. No claim that a passing audit authorises publication.

**Verify readback of the report and PR #5 still open/draft/unmerged**. Provide final Git commit SHA and **COPY TO CHAT** handback. Stop after this single assignment; do not write a further handover yourself.

## 5. Strict exclusions

- **No PR merge, deployment, DNS changes, main-branch write, publication, moving PR #5 out of draft or enabling enquiry submissions.**
- **No replacement Earthrise image** unless the exact owner-approved file is separately supplied in a later specifically authorised task. Do not invent one.
- Do not modify the four preserved SYMMETRIA articles' scientific main content/figures, publish BridgePoint lessons or formal publications, silently correct research claims, or alter asset rights/licensing.
- No broad SEO work, visual redesign, unrelated refactors, synthetic stand-in screenshots, external contact form testing or user-data submission.

## 6. DTSU and final handback

Read and obey the linked **DTSU v1.1** standard in full. Send visible updates in this format, using **actual Europe/London local time** and whole-task progress:

`[HH:MM:SS] NN% — 10–20 word factual status; ETA ~remaining duration.`

Start at **0% before tools/code**, continue at truthful 10–20% milestones and at least every 3–5 minutes on a long interval. Say `ETA unknown` when the remaining time is genuinely uncertain. Finish 100% only after the report is committed and PR verified; otherwise report blocked with truthful progress, not an invented 100%.

Finish with brief **COPY TO CHAT**:
- PR #5, final branch SHA;
- actual automated scan and manual test results, including blockers and commands;
- report link and narrow fixes;
- rerun status if code changed;
- precise release blockers and confirmation of **no merge/deployment**.

**Completion requires a committed, verifiable report and actual QA evidence, not merely fetching the handover or starting a test process.**
