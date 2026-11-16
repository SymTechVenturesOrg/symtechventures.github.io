# SymTech Ventures v2.0 — Chat-led Website Development Workplan

**Version:** 2.0 (replaces the earlier specialist-led workplan)  
**Date:** 16 November 2026  
**Status:** Proposed; planning PR only — no deployment or production HTML/CSS/JS changes authorised.  
**Website:** https://www.symtechventures.com/  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Related documents:** [Work/Chat/Codex workflow](WEBSITE_DEVELOPMENT_WORKFLOW.md), [space-first site plan](SPACE_FIRST_SITE_PLAN.md), [programme structure](PROGRAMME_SERIES_STRUCTURE.md).

## Core operating decision

**Chat is the continuous lead, organiser and primary working environment.** Chat performs as much of the research inventory, source-grounded planning, page copy, small document changes, GitHub organisation, review and status reporting as available tools permit.

**Work and Codex are limited, alternating specialist support roles** invoked only for high-value, bounded tasks:
- **Work:** stages 2, 5 and 7 — source/asset assessment and focused website editorial/visual acceptance. Individual BridgePoint lessons are deferred.
- **Codex:** stages 4, 6 and 8 — real browser-compatible prototype, implementation, and technical/visual regression testing.
- **Chat only:** stages 1, 3 and 9 — charter, information architecture, and owner-approved publication coordination.

Sequence of specialist engagements: **Work → Codex → Work → Codex → Work → Codex**. Do not keep both engaged simultaneously on the same files. No standing Work/Codex background task is assumed.

**Luna-first policy:** request/select Luna wherever available for the six specialist engagements. **Terra has zero planned uses** and is considered only after a specific persistent problem is documented, the scope has been narrowed and the project owner explicitly approves escalation. The user controls model selection where the application offers that choice; Chat cannot guarantee a particular underlying model. Use focused, finite instructions and avoid open-ended "keep working" requests.

## What v2.0 includes

1. New independent, space-exploration-focused identity and site design; preserve the domain and public GitHub Pages hosting.
2. New homepage, research overview, SYMMETRIA, NSRP, SEIP, BridgePoint, Discussion Papers, formal Publications, About/Contact and responsive shared navigation.
3. Preserve the **four existing SYMMETRIA discussion-paper bodies, illustrations and URLs**, reusing only selected other images after suitability and rights review.
4. **SYMMETRIA:** existing four discussion categories × four planned/current discussion-paper entries; preserve currently readable Papers 1–4.
5. **BridgePoint:** four lesson categories × four planned lessons (**16 titles**), **no authored lessons in the initial website release**. All 16 lesson entries remain clearly labelled Planned.
6. **NSRP:** five original stage projects × four phases (**20 phases**) with evidence/status labels; these are research aims, not accomplished findings.
7. **SEIP:** five engineering stage projects × four phases (**20 phases**) with baseline/reproducibility requirements; no invented experiments or working spacecraft technologies.
8. Formal **Publications section with zero entries**; the existing publicly readable discussion papers remain separate.
9. Owner-supplied LinkedIn profile: https://www.linkedin.com/in/drgeoffthomas; UK English; clear evidence boundaries; verified desktop/mobile usability.

Not included: writing any of the 16 BridgePoint lessons, actual NSRP/SEIP scientific output, old folder-tree migration, speculative hardware prototypes, or a commercial start-up infrastructure.

## Staged delivery and effort estimates

**All nine stages are led by Chat.** The listed specialist is a *support role*, not a separate project manager.

| Stage | Chat leads by doing… | Specialist support (alternating) | Estimated active effort | Deliverable / gate |
| --- | --- | --- | ---: | --- |
| **1. Scope and GitHub governance** | Lock scope, constraints, approvals, issue/PR plan and URLs to preserve | **None** | **2–3 h** | Written charter; review-only PR; project owner agrees to proceed |
| **2. Asset/source audit** | Inventory existing pages, articles, images, source links and old start-up copy | **Work · Luna** — short visual/editorial suitability review | **3–5 h** | Reuse/retire shortlist; four article URLs frozen; provenance/rights questions flagged |
| **3. Architecture and page briefs** | Write sitemap, navigation, status rules, page-by-page text plan and content priorities | **None** | **3–5 h** | Approved space-first wireframe brief, BridgePoint 4×4, NSRP/SEIP 5×4, empty Publications |
| **4. Design prototype** | Specify colours, type, reference layouts, content hierarchy and acceptance criteria | **Codex · Luna** — one bounded desktop/mobile homepage prototype with real renders | **4–7 h** | Functional prototype and screenshots; owner approves style before large code build |
| **5. Editorial and scientific copy** | Draft/revise core page text, About/LinkedIn text, phase summaries and all planned lesson descriptions | **Work · Luna** — focused accuracy, readability and claim-status review | **4–6 h** | Approved copy files/briefs; no false publications or scientific breakthrough claims |
| **6. Construct v2.0 on feature branch** | Supply final approved copy, scope changes, GitHub coordination, interim PR review | **Codex · Luna** — implement templates/pages, reuse articles/images, handle navigation and responsive CSS | **9–14 h** | Working replacement site on unmerged implementation PR; existing article paths preserved |
| **7. Website content and visual acceptance** | Review all implemented website pages, programme structures, scientific status labels, layout and design consistency; do not write lessons | **Chat first; Work only if a distinct independent website review adds value** | **2–4 h** | Site wording/status review; all 16 BridgePoint lessons remain Planned, with no completed lesson links |
| **8. Technical QA and corrections** | Prioritise defects, check pages/links and acceptance checklist, decide release readiness | **Codex · Luna** — accessibility, mobile/desktop browser checks, automated/static tests and targeted fixes | **4–7 h** | Test evidence, regression/URL results, resolved critical issues and rollback instructions |
| **9. Owner-approved release** | Present final checklist; obtain explicit merge approval; coordinate GitHub merge and verify live pages | **None** unless a specific technical fault needs a new bounded Codex task | **2–3 h** | Approved production merge, confirmed GitHub Pages deployment, live checks and final DTSU |
| **Total** | | | **35–56 h** | Complete v2.0 first release, subject to review gates |

**Estimated allocation of active effort (not tokens):**
- **Chat:** approximately **17–27 hours**
- **Work:** approximately **5–8 hours** across three bounded engagements
- **Codex:** approximately **13–21 hours** across three bounded engagements
- **Total:** **35–56 hours**

These are planning ranges for active effort including expected ordinary revisions, *not* model token budgets or timed guarantees. Work/Codex token consumption varies by task size, tool usage and retries. An apparent reduction from the earlier 45–65-hour estimate comes from moving preparatory/editorial work into Chat, eliminating duplicate reviews and bundling specialist tasks; the actual saving must be measured, not presumed.

**Estimated calendar duration:** **2–4 weeks** at roughly 12–20 productive hours per week and prompt owner feedback. If either Work or Codex quotas are exhausted, pause that specialist stage; continue useful Chat-only work without bypassing its quality gate. Calendar length may extend with content corrections or access issues.

## Token-efficient hand-off standard

For each specialist engagement, Chat prepares exactly one bounded GitHub-linked task brief:

1. **Why:** objective and acceptance criteria (specific files/pages).
2. **Inputs:** approved source links, current branch/PR, asset selections and exclusions.
3. **Work limit:** fixed deliverables, small named file scope, no unrequested improvements.
4. **Checks:** exact evidence needed and what must *not* be claimed.
5. **Handback:** concise **COPY TO CHAT**, test result/PR link, DTSU with estimated ETA and unresolved issues.

A specialist performs **only its assigned stage**, produces a reviewable artefact and stops. Chat then examines the output, resolves small decisions/edits and decides if a follow-up engagement is justified. Avoid repetitive overlapping Work and Codex passes and do not reopen completed work for cosmetic changes without clear benefit.

### Responsibilities to protect token budgets

- Chat handles GitHub Issues, branch/PR briefs, markdown schedules, status tracking, source-grounded drafting, straightforward metadata checks and final approval coordination when tools permit.
- Work does **not** recreate a site from scratch or modify Codex-owned HTML/CSS/JS. Use it for genuinely useful scientific/editorial judgment and real-render evaluation when available.
- Codex does **not** research and rewrite whole physics narratives; it implements approved material and performs technical checks.
- Owner approvals should be batched into the gates below to avoid unnecessary cycles.

## Four pre-release owner review gates

1. **After Stage 3:** approve sitemap, research positioning, programme layout and page briefs.
2. **After Stage 4:** approve real desktop/mobile homepage prototype and visual system.
3. **After Stage 7:** approve website content, visual consistency, research statuses and the 16-entry BridgePoint planned catalogue; no lessons required.
4. **After Stage 8:** approve tested site and release checklist; **Stage 9 requires a separate explicit merge/deploy instruction**.

Never treat assent to a workplan as authorisation to publish.

## Technical and editorial safeguards

- Keep production `main` unchanged until Stage 9. The website implementation is a **separate feature branch/PR** from the planning PR.
- Preserve SYMMETRIA Paper 1–4 URLs, the original article content and required illustrations; ensure internal links, sitemap and SEO metadata work after redesign.
- Keep formal Publications empty; label the discussion series **online discussion papers**, not formal peer-reviewed publications.
- Distinguish an established equation, exploratory hypothesis, Python model result and empirical evidence.
- Any reused image requires suitability/rights review, descriptive alt text and reasonable load performance.
- Check phone-portrait layouts, keyboard use, headings, meaningful link labels, visual contrast, mathematical readability and browser-generated previews.
- Document the pre-launch main commit and practical rollback route before a merge.
- Report milestone DTSUs with actual local time, **estimated ETA** and concrete evidence; avoid claiming ongoing work after the response ends.

## Later work excluded from launch estimate

Writing all 16 BridgePoint lessons is deferred to a later, separately agreed educational project. No lesson-writing time is included in the website launch estimate. Actual NSRP/SEIP work requires independent scoping; do not estimate experimental or scientific breakthroughs.

**This file is a plan. No website implementation files or public articles have been changed.**
