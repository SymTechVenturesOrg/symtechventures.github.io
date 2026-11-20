# SymTech Ventures v2.0 — Phase 1B Codex: Layout and In-Page Navigation Browser QA

**Date:** 17 November 2026 (GMT) · **Scope:** ONE bounded browser QA + small reproducible fixes if necessary.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Existing working branch:** `feature/v2-space-research-website`  
**Existing PR:** [#5 — draft, unmerged](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Before starting:** Fetch the latest feature PR head; do not presume the preparatory commit is still HEAD.  
**Planning decisions:** [Three-phase workplan](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md) and [Phase 1A source/screenshot audit](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_PHASE_01A_LAYOUT_AUDIT_AND_IMAGE_SLOTS_20261117.md).  
**Source-only implementation evidence:** [Phase 1B first source QA](../reports/V2_PHASE_01B_JUMP_NAV_SOURCE_QA_20261117.md).

## Exactly what changed, and what remains unverified

Chat implemented a compact, responsive accessible `Jump to` index in four long pages:
- `pages/bridgepoint.html`: four category anchors;
- `pages/discussion-series.html`: four group anchors;
- `pages/nsrp.html`: five project anchors;
- `pages/seip.html`: five project anchors;
- `css/v2-programmes.css`: narrow shared style, mobile wrapping, scroll margins.

Source readback reports **all 18 anchors have unique matching IDs** and pre-existing counts remain 16/16/5×4/5×4. **No current-head real Chromium browser test or full regression has yet been run for these new edits**. Don't report pass based on older Stage 8F-D/E tests.

**No new images in Phase 1**. The proposed Earthrise WebP is not verified in the repository; keep the homepage's current orbit SVG. Don't touch any of the original 28 SYMMETRIA images or four article main-body sections.

## Bounded execution tasks

1. Fetch/checkout latest feature branch and record SHA. Read the two linked phase documents and the changed files only as needed.
2. Run `python3 -u docs/reports/scripts/v2_stage8_qa.py` with the exact real checkout, Chromium/Playwright; **record actual command, exit status, counts and errors**, with no fabricated pass. The run has been slow before because of screenshots/network-idle waits. **Monitor the running process and obtain its exit code before starting a duplicate**; use unbuffered output. If environment restart loses process/session, document that candidly.
3. In actual Chromium, at **320, 390, 768, and 1440px**, exercise at least:
   - BridgePoint category link to final four-lesson group;
   - Discussion Series link to the third or fourth group;
   - NSRP `proj-5`, SEIP `proj-5`;
   - keyboard Tab-to-index and Enter anchor activation, visible focus and absence of overlap/obscured destination;
   - no horizontal overflow or forced truncation; the 16/16/20/20 catalogue counts and Planned status remain intact.
4. Produce a **fresh, current-head visual reference**, reusing screenshot outputs from the full regression where suitable, with representative **Home, Research, BridgePoint, Discussion Series, NSRP, SEIP, About and Contact** at **390 and 1440px**. For very long pages, viewport/section captures are preferable to massive duplicate full-page raster files; specify which captures are complete versus partial. Include **320 hero/header** and **768 header/nav** samples. **Do not use older `v2-*` screenshots as if they represent the current code**.
5. Inspect the **owner-required fully justified running prose** on narrow screens. Record actual examples of unnatural gaps if observed on About/Contact or long catalogue cards, and propose at most **one narrow owner-compatible improvement**; do **not** silently switch all mobile text to left-aligned. Preserve **no starfield**, readable dark palette, natural heading/control alignment, and research/project truthfulness.
6. If simple, reproducible technical defects exist in the new index or layout, fix them narrowly on PR #5, rerun the relevant browser check and **full regression again after source changes**. Consider a focused axe scan if changes affect names, focus order or contrast. If correcting justified typography would conflict with owner's explicit style, **report option, don't implement**.
7. Check that six-link nav, paused Contact/Enquiry, seven historical `noindex` pages, four original paper URLs/body/figures and no formal publication entries remain unchanged. Do not rewrite scientific claims, merge PRs or revive forms.

## Deliverable and acceptance boundary

Commit one focused evidence report in the same branch:

`docs/reports/V2_PHASE_01B_LAYOUT_BROWSER_QA_20261117.md`

Include:
- starting/final feature SHA; full exact-command regression result/exit code;
- real browser/Playwright environment, viewport matrix, sample screenshots with exact paths;
- 18 anchor targets actually navigable (or exact observed scope), focused keyboard/mouse outcomes, scroll/overflow checks and any accessibility findings;
- concise page-by-page **owner visual review notes**, distinguishing defects from optional preferences and any old screenshots;
- any small code changes and their retests, or explicit statement no further changes;
- **Phase 1 layout owner acceptance still pending**, Phase 2 imagery not started; the Earthrise image still absent;
- PR #5 readback showing open/draft/unmerged at final SHA.

**Stop after report and COPY TO CHAT handback**. This assignment does not approve the entire layout or authorise Phase 2 generation; Chat and the owner will decide the final visual acceptance stage separately.

## DTSU and model policy

Read and follow [DTSU v1.1](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md). Report **actual Europe/London time**, starting at **0% before tools/work**, at real milestones in `[HH:MM:SS] NN% — factual task status; ETA ~estimated remaining time` format. **Always estimate an ETA** based on current evidence; if uncertain, give a reasoned range rather than `unknown`. Do not invent process success. Finish 100% only after the report is committed and PR verified.

The **owner controls Codex model, effort and speed** and prefers Luna, Medium effort, Standard speed. If hard debugging arises, record why a harder mode might be needed; **do not independently escalate to Terra**. No merge, deploy, DNS, `main` edits, new PR, image generation or article research revisions.
