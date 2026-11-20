# SymTech Ventures v2.0 — Stage 8F Codex: Integrated Browser Regression and Accessibility

**Prepared:** 16 November 2026 (Europe/London)  
**Task type:** Finite technical verification and narrowly scoped fixes, **not release or publishing**  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Working branch:** `feature/v2-space-research-website`  
**Existing implementation pull request:** [Draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Pre-handover head checked:** `abf332b46847ba6272bc95e75be44cd2dfa2f919` — fetch the **actual latest** branch/PR head when starting and record it in your report.  
**Tracking:** [Website issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## 1. Mission

Carry out a **full, reproducible browser regression and targeted automated accessibility assessment** on the **current GitHub checkout** after Chat's Stage 8D and 8E edits. Correct only clearly reproducible, low-risk accessibility or regression issues discovered during this assignment. Keep all changes on **the same feature branch and draft PR #5**.

The site is an independent research project primarily interested in space exploration, not a commercial startup or a claim of proven propulsion technology. Preserve the owner's approved restrained dark design, **no starfield**, and **fully justified running prose**. Do not make unrelated changes.

**The project owner alone controls Codex's model, thinking effort and speed.** This handover does **not** instruct Codex to select or change any of those settings.

## 2. Read the latest evidence before making changes

1. [Stage 8C exact-branch pre-release assurance](../reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md) — last reported whole-site Playwright run, test outcomes and limitations.
2. [Stage 8D text-only social/SEO metadata changes](../reports/V2_STAGE_08D_SOCIAL_METADATA_SOURCE_QA_20261116.md) — added Open Graph and Twitter/X summary metadata to ten primary pages; no new `og:image`.
3. [Stage 8E current-page and mobile-menu improvements](../reports/V2_STAGE_08E_MOBILE_NAVIGATION_ACCESSIBILITY_20261116.md) — real but **component-level** Chromium tests only; full integrated rerun is due.
4. [Existing regression script](../reports/scripts/v2_stage8_qa.py) — authoritative starting point, not a substitute for assessing actual observed behavior.
5. [Stage 8B full regression baseline](../reports/V2_STAGE_08B_POST_APPROVAL_QA.md).
6. [Stage 8C original asset register](../reports/V2_STAGE_08C_ASSET_PROVENANCE_REGISTER.md) — origin/figure concerns remain separate editorial/owner gates.
7. [DTSU v1.1-style project standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md) — read the whole file and follow its visible progress-update rules.
8. [Stage 9 owner review checklist](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_09_OWNER_RELEASE_CHECKLIST.md) — approval decisions belong to Chat and the owner, **not** Codex.

If a referenced file is missing, record the precise missing path and blocker. Do not assume a previous Chat-side test is an exact-repository browser run.

## 3. Package A — Integrated regression across the actual checkout

- Start from fresh, checked-out PR #5 feature branch. Record branch, starting commit SHA and comparison baseline. Avoid stale workspace files or overwriting concurrent commits.
- Run the existing project check **exactly**:
  `python3 docs/reports/scripts/v2_stage8_qa.py`
  Record exit code, captured output, environment, any missing dependencies and actual count of files/routes tested. If the script fails, classify whether it caught a genuine website regression, a stale test assumption or an environment limitation; fix only a demonstrated issue, never weaken a check to force a pass.
- Test the **ten** principal pages (Home, Research, SYMMETRIA, NSRP, SEIP, BridgePoint, Discussion Papers, Publications, About and Contact), the **four preserved SYMMETRIA discussion papers** and all **seven historical division/fellows URLs** plus Enquiry and the former confirmation URL.
- Use genuine Chromium/Playwright at **320, 390, 768 and 1440 px**. Check local HTTP responses, broken internal/fragment references, browser console exceptions, failed resources, document overflow, visible text wrapping and layout integrity.
- Confirm **no starfield canvas/animation**, expected reduced-motion behaviour, six main navigation links, footer/Contact routes, and justified running prose with heading/control exceptions.
- Verify four original paper paths and actual **paper main text/figure preservation** against the trusted `origin/main` source, allowing only previously approved article-shell changes. Preserve all seven in-article figures per paper. No edits to scientific article bodies or embedded diagrams.
- Confirm the programme/status counts: Discussion Series **4 available + 12 planned**; BridgePoint **4 groups, 16 lessons all Planned, no lesson links**; NSRP **5 projects × 4 phases = 20**, SEIP **5 projects × 4 phases = 20**; formal Publications **zero**.
- Confirm all seven historical pages remain accessible with exactly one historical context notice, exactly one `noindex,follow` and exclusion from the **16-entry sitemap**; retain four paper URLs in the sitemap and `CNAME`.
- Confirm online enquiry **remains disabled**: no HTML submission form or submission controls on Enquiry, truthful old confirmation message, Contact links to status page, no user data transmitted.

## 4. Package B — Integrated navigation behaviour after Stage 8E

On the **actual site HTML/CSS/JS**, not only a standalone component harness, verify desktop and mobile navigation:

- Current page `aria-current="page"` appears on the proper **Home** entry on the homepage and corresponding primary navigation link on other routes. Desktop styling must highlight the actual active destination, **not always Home**.
- Current-page indication also appears in the mobile navigation where appropriate; focus styling must be distinguishable from current-page styling.
- On mobile at **320 and 390 px**: open the native disclosure, confirm its accessible summary label becomes **Close navigation menu**; Escape closes it and restores focus to the summary; reopening and tapping outside closes it; labels revert to **Open navigation menu**. Check menu links can be activated by keyboard, pointer and touch-like input; ensure no horizontal clipping.
- On 768 and 1440 px, verify desktop navigation visibility and that mobile behavior does not leak into desktop layout.
- Check for interaction defects that occur because of page-specific styles or scripts, not merely the isolated navigation test.

## 5. Package C — Automated accessibility examination

Stage 8C could not run axe-core/equivalent. **Make a bounded, genuine attempt** to run a reputable local browser accessibility checker on the actual checkout, covering at least Home, Research, BridgePoint, Discussion Papers, Contact and a representative full paper at desktop/mobile widths.

- Prefer an **already installed** axe-core, Playwright accessibility tooling or an equivalent available offline tool. If none exists, an ordinary, reversible test-only dependency setup is permitted **only if supported by the environment** and without introducing secrets, unapproved remote services or unnecessary production dependencies. Record the package/version and command.
- If automated tooling is unavailable after a reasonable bounded attempt, mark it **BLOCKED/NOT RUN**, and continue meaningful documented manual/DOM checks. Do **not** state or imply that missing axe tests passed or that WCAG compliance is certified.
- Review and report at minimum: document language, page title, landmarks, heading hierarchy, unique IDs, link/button accessible names, image alt text, text/background contrast, keyboard focus visibility, skip links, menu disclosure state/name, touch target concerns and decorative SVG exposure to assistive technologies.
- Triage actual findings by severity (critical/high/medium/low) and list the affected element/route and reproduction steps. Correct only low-risk, clearly evidenced code issues within the existing site style. If a fix touches copy, research figures, licensing, or an owner's design choice, document the finding for Chat/owner rather than rewriting content.
- **Automated accessibility tests are partial**: no blanket WCAG certification or real screen-reader user testing is claimed.

## 6. Package D — Stage 8D share metadata check

- Validate the ten primary page heads: exactly one appropriate `og:type`, `og:site_name`, `og:locale=en_GB`, `og:title`, `og:description`, `og:url`, and `twitter:card=summary`; title/description/URL must match the existing title/description/canonical metadata on that page.
- Confirm no newly added `og:image` on these pages and that no missing share image is referenced. The original four papers already have article-specific social metadata and their original images; do not erase or overwrite it.
- Record any malformed/missing/duplicate metadata, broken canonical URLs and sitemap/robots inconsistencies. Do not contact external social platforms or claim that their crawlers displayed a card unless actually tested and allowed.

## 7. Evidence and screenshot deliverables

Commit one reproducible, concise report at:

`docs/reports/V2_STAGE_08F_FULL_REGRESSION_ACCESSIBILITY_20261116.md`

Include:
1. Starting and final exact commit SHA; branch and PR link; tools, browser/package versions and execution environment.
2. Commands and exit codes; pass/fail/blocked outcomes separated for **full regression**, **navigation**, **automated accessibility**, **manual accessibility**, **metadata/SEO**, and **preserved content**.
3. Genuine screenshots at **390 and 1440 px** of at least Home, Contact and one representative paper, plus **320 px mobile menu open** if useful; screenshots must be browser captures of the real checked-out site, not simulated visuals. Keep naming and number of screenshots bounded; add only evidence that shows the new test coverage or an actual bug/fix.
4. A short findings table with reproducible issues, severity, fix status and remaining risks; link any code or screenshot evidence.
5. Explicit statement that any remaining Earthrise binary, image licensing/provenance and scientific-figure claims are **separate owner/editorial decisions**. The owner has said the **28 original paper figures and six shared logos were ChatGPT-generated under their direction**; this does not certify all other historical visuals or validate embedded physics assertions.
6. A release-readiness verdict: **Pass / Pass with owner blockers / Fail**, reflecting *actual* evidence; do not equate a green regression script with a release authorisation.

If the regression script must be enhanced to check these additions, edit it minimally, keep its existing coverage and rerun the complete script. Do not commit large dependency trees, temporary HTML harnesses, caches or fabricated screenshots.

## 8. Explicit exclusions and safeguards

- **Do not merge, publish, deploy, change DNS, modify `main`, close PR #5 or mark Stage 9 approved.** Keep PR #5 open and draft.
- **Do not invent, regenerate, locate a substitute for, or silently install** the missing approved Earthrise raster. If its real approved binary is not present, log it as an owner-dependent decision. The current inline orbital SVG may stay unchanged.
- Do not revise the four research papers' scientific content, remove figures, manufacture experimental support for SYMMETRIA, publish BridgePoint lessons or create formal publications.
- Do not reactivate, submit to or test with real personal information through the old third-party enquiry form. Historic routes must retain their notices and indexing policy.
- No broad visual redesign or speculative optimisation. Do not use Work or other development streams to edit the same files concurrently. Do not request or change the owner's Codex model/effort/speed settings.
- Any newly discovered external-source/rights, figure-accuracy or policy issues go into the report for owner review; do not assume copyright clearance from GitHub presence or ChatGPT generation alone.

## 9. DTSU and COPY TO CHAT handback

**Mandatory DTSU:** Follow the linked standard: send visible user-facing messages at **real Europe/London local time**, starting **0% before coding/tools**, then at approximately each 10% whole-task milestone and at least every 3–5 minutes for longer intervals. Format `[HH:MM:SS] NN% — brief factual status; ETA ~remaining duration`; use `ETA unknown` rather than guessing. Do not invent timestamps, completion percentages or tests. **100% / ETA 0 minutes** is only appropriate after reports, checks and GitHub readback are finished.

Finish with a concise, paste-ready **COPY TO CHAT** message showing:
- PR #5 URL, current branch and final SHA;
- which regression and accessibility checks **actually ran**, commands and outcomes;
- report path and best screenshot locations;
- any narrow fixes committed and any blocked/missing tests;
- owner decisions pending before Stage 9;
- explicit confirmation **no merge/deployment occurred and PR remains draft**.

**Stop after the handback.** This is a bounded technical verification pass, not continuing background development or permission to launch.
