# SymTech Ventures v2.0 — Stage 8C Codex/Luna Pre-Release Assurance

**Date:** 16 November 2026 (GMT)  
**Owner instruction:** Final, bounded pre-release technical assignment. **The project owner independently sets Codex model, effort and speed in the interface before starting. Codex cannot select, change or escalate those settings.** This handover does not instruct Codex to select Luna or any other configuration.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Existing implementation branch:** `feature/v2-space-research-website`  
**Existing draft implementation PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Tracking:** [Website issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)  
**Stage:** 8C, narrowly extending Stage 8; Stage 9 owner review remains separate.

## Objective and boundary

Perform a final technical assurance pass on the **existing** v2.0 independent-research website. The design and baseline work are already complete. Do not rebuild the website, change its approved research identity, launch new research projects, author new BridgePoint lessons, or rewrite scientific papers. This is a bounded review-and-low-risk-fix assignment, not permission to release.

Read these before making changes:

1. [Stage 8B post-approval regression report](../reports/V2_STAGE_08B_POST_APPROVAL_QA.md) — current verified technical baseline and sole known remaining release gate.
2. [Stage 8 initial QA report](../reports/V2_STAGE_08_WEBSITE_QA.md) — historical limitations, prior test methods and documented exceptions.
3. [Stage 2 original asset audit](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_02_ASSET_AUDIT_20261116.md) — ten visually reviewed candidates and unverified provenance.
4. [Website editorial/contributor rules](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/AGENTS.md) and [workflow](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/WEBSITE_DEVELOPMENT_WORKFLOW.md).
5. [DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md).

Use the **current actual head** of PR #5, not an old or assumed checkout. Record baseline and final commit SHAs. If another writer has advanced the branch, refresh before editing; never overwrite concurrent changes. Keep all work in the PR #5 branch and leave it a draft.

## Work package A — Image and scientific-figure provenance register (highest priority)

- Enumerate all image files in the implementation branch that are referenced by the new v2 pages, preserved articles, Contact/legacy pages and shared CSS; record paths, usage routes and whether assets are displayed or only retained.
- Start from the Stage 2 ten-image review but do not assume that the ten candidates comprise the complete reference set. Differentiate linked image files, inline SVG/data assets and CSS-generated decoration.
- Look only at **evidence actually present** in the repository or otherwise supplied: original metadata, licences, attribution notes, manifests, project documentation and Git history. Record source/creator, licence, attribution and reuse scope if substantiated; otherwise label **Owner confirmation required / Unverified**. Repository presence alone never establishes redistribution rights.
- Distinguish the project logo, decorative art and original SYMMETRIA paper covers/figures from scientific evidence. Catalogue **embedded equations, symbols and factual assertions** in illustrations as **mathematical review required** where applicable; do not certify them as scientifically correct based on visual plausibility.
- Provide an owner-actionable, per-asset table in `docs/reports/V2_STAGE_08C_ASSET_PROVENANCE_REGISTER.md` with columns: file/path; actual website uses; observed content/role; provenance evidence; licence/attribution; maths/claims concern; recommendation; outstanding owner question.
- **Do not delete, replace, regenerate, purchase, import or publicly relicense images.** Any third-party investigation must be source-grounded. Do not declare the rights gate cleared on the owner's behalf.

## Work package B — Accessibility and responsive assurance

- Run an automated accessibility audit using a suitable available tool (e.g. axe-core or equivalent) on representative v2 and original paper pages at desktop and mobile viewports. Clearly distinguish tooling actually run from manual observations; if packages/network/browser are unavailable, record a blocked/not-run result rather than claiming compliance.
- Review keyboard operation and skip links; mobile navigation open, Escape close and focus restoration; meaningful alt text; accessible landmark and heading structure; focus indication; contrast and target sizes; decorative imagery exposure to assistive technology.
- Preserve existing functional outcomes at 320, 390, 768 and 1440 px and `prefers-reduced-motion`. Conduct manual spot checks for findings that automation does not cover. Fix only low-risk, directly reproducible markup/CSS/JS defects, with before/after evidence.
- Explicitly state that automated tests do not constitute WCAG certification or a complete screen-reader audit.

## Work package C — Share previews and search metadata

- Audit titles, description, canonical URLs, sitemap exclusions, `robots.txt`, four original paper URLs, and existing `noindex,follow` historic-page behaviour.
- Add consistent **Open Graph** and, when justified, Twitter/X card metadata to the public v2 landing pages only, using accurate page titles/descriptions, the real production canonical domain and **only verified, eligible media assets**. If share-image rights or suitability cannot be demonstrated, omit `og:image` and leave a clearly identified owner decision rather than inventing an asset. No false formal-publication, laboratory or scientific claims.
- Keep historic URLs crawlable per existing policy but excluded from the 16-location sitemap; do not undo the contact/enquiry privacy fix or re-enable the old form.
- Do not invent or infer dates of publication, research results, affiliations or third-party approval.

## Work package D — Final regression and release-readiness assessment

- Re-run `python3 docs/reports/scripts/v2_stage8_qa.py` from the actual updated branch; capture exact command, exit code and environment. Keep pre-existing and new checks distinguishable.
- Confirm: all 36 HTML files pass local reference checks; six-link v2 navigation; all four original paper routes, body/figure integrity and preserved URLs; BridgePoint 4×4/16 Planned; NSRP 5×4/20 phases; SEIP 5×4/20 phases; Discussion Series 4 online/12 planned; Publications **zero**; legacy historical notices/indexing; Contact and Enquiry do not transmit data; `CNAME` intact.
- Capture genuine browser screenshots for home and a representative paper at 390 and 1440 px if tooling permits, plus any affected accessibility/metadata pages; do not use simulated visuals. Spot-check 320 and 768 px and recheck browser console/errors.
- Review simple performance signals (image weight/loaded resources, unnecessary scripts or motion) without pursuing speculative optimisations; note if any true performance measurements were not run.
- Deliver `docs/reports/V2_STAGE_08C_PRE_RELEASE_ASSURANCE.md` with findings by severity, changes, exact test commands/results, evidence screenshots, final SHA and a clear **Pass / Pass with owner blockers / Fail** assessment. Include specific unresolved copyright/figure decisions.
- If a defect needs a substantive design, editorial, privacy or content decision, **stop at a documented recommendation** and request Chat/owner review instead of silently changing policy.

## Exclusions and permissions

- **Never merge PR #5, merge planning PR #2, commit to `main`, trigger deployment, publish a website, or update the DNS/domain.**
- **Do not send test enquiries, personal data, emails, or third-party messages**, and do not reactivate the suspended enquiry processor.
- No copyright/permission assumptions, no mathematics validation claims without rigorous source review, no claims that SYMMETRIA is experimentally established.
- No new external images, stock photos, generated replacements or unapproved packages committed to production.
- No Work engagement and no broader site redesign. Model, effort and speed are controlled solely by the project owner, outside Codex's control. Treat the website as an independent exploratory research project primarily interested in space exploration.
- Preserve UK English, static current styling, existing links, article content and all original public paper routes.

## Reporting and acceptance

The project owner selects model, effort and speed before initiating Codex; Codex must not be instructed to select or change these settings. Send visible genuine-time DTSUs in Europe/London, beginning 0% and including percentage, evidence and ETA in the format: `[HH:MM:SS] NN% — factual work update; ETA ~remaining time`. If ETA is impossible, use `ETA unknown`. Do not fabricate intermediate timestamps or percentages.

At completion, provide one short **COPY TO CHAT** summary with:
- PR #5 URL, branch and exact final commit SHA;
- files changed and the two assurance reports;
- actual accessibility/SEO/regression results and screenshot paths;
- per-asset provenance clearance status and outstanding owner decisions;
- remaining blockers for Stage 9;
- explicit confirmation **PR remains draft; no merge or deployment**.

**Definition of done:** Both versioned reports exist and have been read back; low-risk authorised fixes are independently verified; remaining release issues are recorded without pretending they have been resolved. Return control to Chat and the owner for Stage 9. This task alone cannot grant release approval.
