# SymTech Ventures v2.0 — Codex Stage 6 Implementation Handover

**Handover revision:** 1.1 — Chat-led, Luna-first, token-conscious  
**Prepared:** 16 November 2026 (UK)  
**Execution:** **Not started**. This document instructs a future, bounded Codex implementation task.  
**Owner and project lead:** Chat, with the project owner approving release  
**Specialist:** Codex — implementation and implementation-stage checks only  
**Issue:** [SymTech v2 development tracker #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## Codex run configuration — explicit settings

| Setting | Selection |
| --- | --- |
| Model | **GPT-6 Luna** (\`gpt-6-luna\` in Codex CLI, if available) |
| Reasoning effort | **Medium** |
| Execution speed / power | **Standard/default**, not an accelerated or Ultra multi-agent run |
| Advanced/Max/Ultra | **Off** / not requested |
| Terra | **Not authorised**; do not switch models without asking the owner |
| Working mode | Single focused Codex implementation run, one feature branch and one draft PR |
| DTSU | **Required** before and throughout execution, using actual Europe/London clock time |
| Working language | UK English for user-visible pages, documentation and handback |

Select model/effort using the Codex interface where available; these settings are **requirements for the handover**, not a claim that Chat has changed your account's Codex settings. If Luna is unavailable, **stop and report the model constraint**, rather than silently using Terra.

**Why Medium:** this is multi-page static-site coding with specified page copy, responsive layouts and integrity tests, but not an open-ended research task. Reuse the approved visual design; don't spend tokens redesigning, brainstorming alternatives or importing unrelated assets. If stuck, reduce the problem to a small reproducible test and report it. No automatic reasoning-effort escalation.

## Reference versions and GitHub boundaries

**Website repository:** \`SymTechVenturesOrg/symtechventures.github.io\` (public GitHub Pages source).

**Baseline:** create a new branch \`feature/v2-space-research-website\` from the current \`main\` commit. At handover preparation, \`main\` was **\`248feb5084745ebcffca5957ca5c517baa8ba7e0\`**; check for changes before starting. If the branch name already exists, use a distinct suffix instead of overwriting.

**Planning PR #2:** [Chat-led roadmap and source content](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2), **draft / unmerged** as of preparation. Fetch documents at \`planning/space-first-research-website-20261116\`.

**Prototype PR #4:** [approved Stage 4 homepage design](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/4), **draft / unmerged** as of preparation. Fetch \`prototypes/v2-homepage/index.html\` and \`README.md\` from \`prototype/space-first-homepage-20261116\`. **Do not merge this PR** to obtain the template.

**Source priority (highest first):**
1. [Owner-approved site map and layout specification](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md) — six navigation items, space-first identity, approved permanent starfield.
2. [Stage 5 page-copy candidate](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/editorial/V2_STAGE_05_WEBSITE_COPY_DRAFT.md) — nine page-slot drafts; **editorial draft, not owner-authorised published findings**.
3. [Canonical website programme series plan](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/PROGRAMME_SERIES_STRUCTURE.md) — source of titles and **4×4 / 5×4** structure. Do not invent alternative phase titles.
4. [Stage 5 review and open questions](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_05_EDITORIAL_REVIEW_20261116.md) — caveats, provisional NCP phase headings, image/mathematical risks.
5. [Stage 2 source and image audit](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_02_ASSET_AUDIT_20261116.md) — selected image candidates and rights uncertainty.
6. [Site governance and DTSU instructions](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/WEBSITE_DEVELOPMENT_WORKFLOW.md).
7. [Source DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md) — reread before executing.

**Only this implementation PR may change production-bound HTML/CSS/JS** on its own branch. Do not alter either source-planning branch or the site's live \`main\` branch. **Do not merge, publish, deploy, contact users or create external accounts.** Stage 9 requires a separate, explicit owner decision.

## Objective and scope

Create the full **v2.0 replacement website in an unmerged draft PR**, preserving the existing domain and GitHub Pages implementation model. Replace the Silicon Valley/start-up pitch with an **independent research project focused primarily on space exploration**, carefully distinguishing scientific questions from supported results.

Use the Stage 4 prototype as the **approved visual direction**, not as a mandate to copy its prototype-only anchor links or placeholder text uncritically. Preserve the requested elegant dark styling, spacious typography and **recognisable site-wide starfield**.

### Required pages and content

| Route | Acceptance target |
| --- | --- |
| \`/index.html\` | Approved space-first homepage, six working top-level links, four programme cards, four genuine discussion-paper links, status note and footer |
| \`/pages/research.html\` | Plain-language programme relationships, space focus, honest evidence ladder |
| \`/pages/symmetria.html\` | Exploratory theory description, not validated unification; link to Discussion Papers |
| \`/pages/nsrp.html\` | **Five projects × four phases = 20**; NCP, SEP, SDEP, SVP, SMP; phases labelled planned/provisional unless evidenced |
| \`/pages/seip.html\` | **Five engineering projects × four phases = 20**; EFP, SEP, SDP, SVP, SMP; not presented as completed experiments or devices |
| \`/pages/bridgepoint.html\` | **Four learning categories × four lesson titles = 16**; only genuinely complete lessons can have active lesson links |
| \`/pages/discussion-series.html\` | **Four available online essays**, **12 planned**; distinguish from formal publications |
| \`/pages/publications.html\` | **Zero formal publication entries**, with an explicit empty state |
| \`/pages/about.html\` | Independent-project mission, evidence ethos, LinkedIn link |
| \`/pages/contact.html\` | Keep reachable; do not silently alter the existing third-party enquiry service or expose new personal contact information |

**BridgePoint lesson 1 is not a completed deliverable for Stage 6.** Build an accessible lesson-page pattern or template if useful, but only Stage 7 will write, review and approve one genuine pilot lesson. All remaining lessons stay **Planned** without dead links.

**Expected permanent navigation:** Home · Research · BridgePoint · Discussion Papers · Publications · About. Contact is accessible via About and footer.

## Preservation register — non-negotiable

The following four **existing, complete** SYMMETRIA article URLs must continue to resolve, with their substantive bodies, figures and discussion status preserved:

- \`/articles/symmetria/symmetria-paper-01.html\`
- \`/articles/symmetria/symmetria-paper-02.html\`
- \`/articles/symmetria/symmetria-paper-03.html\`
- \`/articles/symmetria/symmetria-paper-04.html\`

Before editing any of these files, record their **Git blob SHAs** and content/image-path inventories from \`main\`. **Preferred:** leave all four article files untouched during Stage 6, then update their surrounding shared site navigation only by a separately reviewable, evidence-backed change if required. If changed, give the exact file/section and original-versus-replacement diff; never silently rewrite the science.

Protect the original SYMMETRIA manifest's meaning: the first four papers are **available on the website as discussion papers**, not certified peer-reviewed formal publications. Planned papers 5–16 must not acquire broken destination URLs or false published status.

Do not delete the old \`pages/divisions.html\`, \`pages/founding-fellows.html\`, related division pages, \`pages/contact.html\`, \`pages/enquiry.html\` or \`pages/enquiry-thanks.html\` without a specific compatibility/redirect decision and tests. Identify existing inbound links and sitemap entries first. Retire their primary navigation prominence and obsolete start-up copy on new pages, but preserve functioning paths.

Keep \`CNAME\` and the site's domain configuration intact. If modifying \`sitemap.xml\` or metadata, add only implemented URLs and preserve existing article canonical destinations; no fake last-modified dates.

## Retained starfield — owner-approved

The original \`main:js/main.js\` creates \`aetheros-starfield\` and \`aetheros-shimmer-layer\` canvases. Stage 5 found its own diagnostic note **"No reduced-motion bypass"**. Do **not** copy the entire legacy JavaScript or AetherOS naming into the new site.

Build a minimal, shared v2 starfield module (CSS or small JavaScript) with these checks:

- Recognisably **spacey but restrained** on all principal v2 pages, not only the homepage.
- Decorative only: \`aria-hidden\` or equivalent, no focus, never covers text/click controls.
- **Reduced motion:** if \`prefers-reduced-motion: reduce\`, render a static starfield or disable movement; adapt if the preference changes.
- **Mobile performance:** reduce star density and animation frequency; cap device pixel ratio and limit repaints.
- **Tab visibility:** stop unnecessary animation when the page is hidden; resume safely.
- **Readability:** solid/opaque article and text surfaces as needed; no bright moving particles through long-form paragraphs.
- No claim that an untested starfield passes accessibility/performance review. Stage 8 performs full verification.

## Asset and scientific integrity rules

- Do not reuse the Golden Gate startup hero, fictional staffed-laboratory hero or wormhole/spacecraft promotional imagery as apparent evidence of facilities or research accomplishments.
- The original project logo, abstract SYMMETRIA hero and existing paper images are **candidates**, but their attribution/rights and the formulae embedded in art were **not independently verified**. Prefer a self-contained CSS starfield at first; use existing paper illustrations only in their already existing article context unless cleared.
- No claim of working propulsion technology, new gravitational effect, unified physics validation, funded laboratory, registered startup or operational five-division team.
- Public research status labels should be \`Planned\`, \`Exploratory\`, \`Available online — discussion paper\`, etc., matched to actual source evidence.
- Preserve UK English and mathematical terminology; do not independently edit theoretical arguments.
- The external third-party contact-form handler in the old site requires a privacy and operational check. **Do not copy recipient email addresses or service configuration into new pages** unnecessarily.
- LinkedIn: \`https://www.linkedin.com/in/drgeoffthomas\`; use a clear accessible label, optional new-tab \`rel="noopener noreferrer"\`.

## Token-efficient delivery — four bounded internal checkpoints

**Chat remains project lead; Codex is an implementation specialist.** Do not perform an open-ended visual redesign, long external literature searches or unrelated refactoring.

1. **Shell and navigation:** establish shared CSS, starfield, header/footer and homepage. Provide one desktop and mobile screenshot and a narrow smoke test. Reuse approved prototype design.
2. **Programme pages:** implement Research, SYMMETRIA, NSRP, SEIP and BridgePoint from source copy; verify **16 / 20 / 20** counts. No full lesson writing.
3. **Reading and supporting pages:** Discussion Papers, deliberately empty Publications and About/Contact; keep original four articles and legacy paths working. Update only necessary sitemap/metadata.
4. **Initial build verification and draft PR:** keyboard/menu functionality, real browser pages, 320/390px no-horizontal-overflow check, link integrity and at least basic reduced-motion starfield check. Stop and hand back for Chat and Stage 7 review.

Prefer **one cohesive draft PR** with checkpoints or small commits, not several simultaneous branches or duplicate Work/Codex edits. Report the checkpoints with factual DTSUs; do not expend tokens on unscheduled marketing, design variants or additional pages.

### Acceptance checks (actual test evidence required)

| Check | Expected result |
| --- | --- |
| Page existence | Ten route groups listed above available on the implementation branch |
| Navigation | Six top-level destinations resolve to implemented pages; mobile navigation opens by keyboard |
| SYMMETRIA articles | Four original paths resolve; bodies and image paths intact |
| SYMMETRIA series | Four readable + twelve planned, with honest labels |
| BridgePoint | Exactly sixteen **planned** lesson slots in four groups, no dead lesson links |
| NSRP | Exactly five projects and twenty phase entries |
| SEIP | Exactly five projects and twenty phase entries |
| Publications | Exactly **zero** research publication entries |
| Visual/UX | Actual browser-generated desktop and smartphone screenshots, legible starfield, no horizontal overflow at 320/390px |
| Accessibility | Semantic headings, descriptive links and image alt, visible keyboard focus, reduced-motion fallback |
| Technical | Actual local HTML/link checks, report JS console errors and missing resources |
| GitHub safety | Changes confined to one feature branch / draft PR; no changes to \`main\` |

Record pass, fail, skipped and blockers separately; do not turn an untested item into a claimed pass. **Stage 6 checks are smoke tests only**; formal end-to-end accessibility and regression review occurs in Stage 8.

## Required v1.1 DTSUs — visible, clock-verified

Read the linked **DTSU — Dr T Style Updates** standard before coding. Issue updates in visible Codex/Chat messages, using actual Europe/London local time:

\`\`\`text
[HH:MM:SS] NN% — Factual, 10–20-word whole-task status; ETA ~remaining duration.
\`\`\`

- **0% before any coding/actions**, using a real clock read, not prefilled time.
- Update at genuine **10% milestones** where possible (at minimum each 10–20% when work moves quickly), and every **3–5 minutes** if longer work continues.
- Every message includes **ETA**; if remaining time is genuinely incalculable, write \`ETA unknown\`.
- **100%, ETA 0 minutes** only after actual files, tests, report and PR handback are verified.
- On blocking failures, report **blocked** with the true percentage and \`ETA unknown\`.
- DTSUs are **user-visible messages**, not just background logs or a Markdown report.
- Never fabricate timestamps, test outcomes or a promise to send future updates from an unattended session.

Do not assume model/effort selection is enforceable through a Markdown file. If the selected configuration differs, disclose it in the first DTSU.

## Stop, report and COPY TO CHAT

Deliver **one concise handback** after Stage 6 (not Stage 7/8/9):

- Exact branch and **draft PR URL**; final commit SHA.
- Files changed and explicit confirmation that \`main\` remains untouched.
- Milestone results with actual commands/browser dimensions; link to a versioned \`docs/reports/\` verification report in the PR.
- Actual desktop/mobile screenshot references or a truthful reason they could not be captured.
- Four article integrity results; 16/20/20 programme counts; zero formal publications; starfield reduced-motion observation.
- Failure list, security/privacy and asset-rights blockers, and concrete Stage 7 review requests.
- Concise **COPY TO CHAT** plain-text summary, not a second long set of instructions.
- Stop. **Do not merge PRs, deploy GitHub Pages, publish scientific work or start Stage 7 autonomously.**

**This handover is ready for an explicit Codex run, but preparation of the handover is not execution of the website build.**
