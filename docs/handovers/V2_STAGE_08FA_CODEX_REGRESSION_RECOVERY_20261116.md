# SymTech Ventures v2.0 — Stage 8F-A: Codex Regression Recovery

**Prepared:** 16 November 2026 (GMT)  
**Status:** Ready for a short, finite Codex execution. Stage 8F was **not** completed by the previous attempt: fetching the branch and reading its handover did not produce tests or a report.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Feature branch:** `feature/v2-space-research-website`  
**Existing draft PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Last independently checked head (before this handover commit):** `3727476535bb8191f4ed5e41654b3beebc7315a7`  
**Parent task:** [Stage 8F](V2_STAGE_08F_CODEX_FULL_REGRESSION_ACCESSIBILITY_20261116.md)

## Single objective

**Run the current integrated regression against the actual checked-out PR #5 branch and commit one concise, evidence-backed result.** This is Stage 8F-A **only**. Do **not** attempt the separate Stage 8F-B automated accessibility audit, Earthrise artwork work, scientific figure review, broad optimisation or any release action in this assignment.

The project owner selects Codex model, thinking effort and execution speed in the interface. Codex cannot change these settings, and this brief does not ask it to.

## Read these sources

1. [Existing exact-branch regression script](../reports/scripts/v2_stage8_qa.py)
2. [Stage 8C last successful full regression](../reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md)
3. [Stage 8D social metadata changes](../reports/V2_STAGE_08D_SOCIAL_METADATA_SOURCE_QA_20261116.md)
4. [Stage 8E current-page/mobile-menu changes](../reports/V2_STAGE_08E_MOBILE_NAVIGATION_ACCESSIBILITY_20261116.md)
5. [DTSU standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md)

## Work and exact completion criteria

1. Check out `feature/v2-space-research-website` from the existing repository, fetch the current remote head and record the **actual starting Git SHA**. Do not use `main` as the working branch. Do not discard concurrent edits. No separate PR.
2. Run `python3 docs/reports/scripts/v2_stage8_qa.py` at the repository root. Capture the exact command, exit code and output summary. If Python or Playwright fails, report the concrete error and attempt only a bounded environment repair (such as using already available Chromium/packages); do not invent a successful run.
3. If the script passes, spot-check **on the real site** the changes made since Stage 8C: ten main-page Open Graph/title/description/canonical tags; correct desktop and mobile `aria-current` highlighting; mobile menu's Open/Close accessible summary label, Escape/focus restoration and outside-tap dismissal. Test navigation on **320 and 390 px mobile**, and desktop visibility at **768 and 1440 px**. Document true observed outcomes and any test limitations.
4. Preserve baseline gate behaviour checked by the script: 36 HTML files, all four original full SYMMETRIA paper bodies/seven figures each, 16-entry sitemap with all four paper URLs, seven historical `noindex,follow` routes, paused Enquiry form, Contact page, programme counts (BridgePoint 16 planned; NSRP/SEIP 20 phases each; 4 online/12 planned papers; zero formal publications), no starfield, no console failures/overflow.
5. If a test fails, identify precisely why. Make only a narrow and reproducible **test-expectation** or accessibility/navigation fix where appropriate, preserving protections. **Never weaken an assertion just to force a green result.** Rerun the full command after any correction. If a genuine blocker needs owner/design/research decisions, record it and stop rather than expanding scope.
6. Commit **one short QA report** to `docs/reports/V2_STAGE_08FA_INTEGRATED_REGRESSION_20261116.md` on the existing feature branch, including actual SHA(s), command/exit status, visited routes/viewports, minimal screenshots if freshly captured, precise test findings, and a **PASS / FAIL / BLOCKED** conclusion. This is the sole mandatory deliverable (plus only genuinely required small fixes). Do not commit redundant screenshots or environment caches.
7. Fetch/read back the committed report and verify PR #5 is **still open, draft and unmerged**. State the final commit SHA. **Stop** and return a COPY TO CHAT handback. If a checkout or push is blocked, report the exact error and the truthful state; a local-only result is not a completed handback.

## Boundaries and release policy

- **No merge, deployment, DNS changes, publishing, modifications to `main`, or closing PR #5**.
- No edits to article scientific prose, original figure assets, formal Publications catalogue, or BridgePoint lesson contents.
- **No form submissions or personal information sent**, and do not reinstate the old enquiry provider.
- The approved Earthrise WebP is still missing from the branch; **do not invent or replace** it. Leave existing homepage inline orbit art untouched.
- The owner has attested the original figures and logos were generated with ChatGPT, but scientific accuracy in illustrations and other historical imagery remain separate owner review questions.
- **Automated axe/equivalent auditing belongs to Stage 8F-B**, to be handed over separately **after** this regression report is verified. Do not use its absence to fail an otherwise passing 8F-A regression, but do not claim accessibility compliance.

## Mandatory DTSU and COPY TO CHAT

Read the linked DTSU source. Issue a **visible 0% update before any tools/coding**, then brief factual progress at real 10% milestones (or every 3–5 minutes), each with true **Europe/London `HH:MM:SS` time, whole-task percentage and ETA**. Use `ETA unknown` when necessary; do not fabricate time or pretend to have posted updates. Reach 100% only after the report is committed and verified.

Your final **COPY TO CHAT** should include: PR #5 URL, feature branch, exact final SHA; command and actual exit code; main findings including Stage 8D/8E validation; report link; any blockers or tests not run; and confirmation **PR stays draft, with no merge or deployment**.

**Do not stop after merely fetching or reading the handover. The task is complete only with executed regression and committed verified report, or a precise technical blocker with evidence.**
