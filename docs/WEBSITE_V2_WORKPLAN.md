# SymTech Ventures Website v2.0 — Staged Development Workplan

**Status:** Proposed; requires review. No production changes authorised.  
**Date:** 16 November 2026  
**Site:** https://www.symtechventures.com/  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Related planning:** [Website workflow](WEBSITE_DEVELOPMENT_WORKFLOW.md), [space-first site plan](SPACE_FIRST_SITE_PLAN.md) and [programme structures](PROGRAMME_SERIES_STRUCTURE.md).

## Objective and definition of "v2.0"

Create a **new, independent space-exploration research website**, retaining the domain, a selected set of existing scientific images, and the **four currently readable SYMMETRIA discussion papers** under their original URLs. Replace the start-up identity, navigation and general page design, without disrupting GitHub Pages until explicitly approved.

The initial release should include:

- Homepage and space-oriented independent-research identity.
- Research overview, SYMMETRIA, NSRP and SEIP pages.
- BridgePoint: 4 groups × 4 lessons (**16 planned lesson titles**) plus one fully written and reviewed pilot lesson.
- NSRP: **5 projects × 4 phases = 20 planned research phases**.
- SEIP: **5 companion projects × 4 phases = 20 planned engineering phases**.
- Discussion Papers index and the four existing SYMMETRIA articles, with stable URLs.
- **Formal Publications page with zero listed publications.** Existing online discussion papers are not formal academic publications.
- About/Contact and explicit [LinkedIn](https://www.linkedin.com/in/drgeoffthomas) link.
- Accessible, smartphone-friendly responsive pages, verified links and sitemap; no unreviewed scientific breakthrough claims.

**Out of scope for initial release:** writing all 16 complete BridgePoint lessons, producing completed NSRP/SEIP research outputs or simulations, redesigning original scientific manuscripts, building paid services or commercial infrastructure, recreating legacy Aletheia systems, migrating old Google Drive folders wholesale.

## Team assignments and model policy

- **Chat — project director:** decide scope, prioritise, resolve ambiguities, review scientific risk, approve stage gates and merges.
- **Work — editorial researcher / visual acceptance:** reuse and critically review source material, draft educational and research explanations, maintain evidence/status labels, review actual browser renders.
- **Codex — implementation owner:** HTML/CSS/JS, templates, GitHub branches and PRs, migration/preservation of article paths, local/static validation, responsive fixes and launch checks.

**Model default:** Luna for every Work and Codex stage where selectable; start with focused tasks and medium/lower reasoning. **Terra planned use: none.** Only consider Terra if a specific reproducible problem remains unresolved after reasonable scoped Luna attempts, and ask for the owner's approval before switching. The website project is not a model-performance benchmark; correctness, traceable checks and restrained usage are the priorities.

Work should **not** edit the same HTML/CSS/JS paths that Codex owns. Chat may update decisions/briefs, while Codex implements approved copy. Keep internal drafts in the private `symtech-ventures` repo; use the public GitHub Pages repo only for reviewed material and publicly safe planning docs.

## Nine stages and effort estimates

| Stage | Primary owner | Preferred model | Estimated active effort | Deliverable / acceptance gate |
| --- | --- | --- | ---: | --- |
| **1. Project charter and governance** | Chat, supported by Work | Luna for Work | **2–3 h** | Confirm detailed v2.0 scope, page inventory, owner review checkpoints, branch rules and legacy URL freeze |
| **2. Legacy audit and selection** | Work, Codex for code/assets inventory | Luna | **4–6 h** | Preserve four article URLs; select usable image/logo assets; rights/alt-text check; identify stale start-up copy, redirects and sitemap risks |
| **3. Research/editorial architecture** | Work; Chat acceptance | Luna | **6–8 h** | Approved sitemap, page briefs, statuses, BridgePoint 4×4, NSRP/SEIP each 5×4, space focus, Publications zero entries, About/LinkedIn wording |
| **4. Visual design system and prototype** | Codex, Work evaluates actual renders | Luna | **6–9 h** | Reusable type/spacing/colour/navigation components; real desktop and phone homepage prototype; approval checkpoint |
| **5. Core v2.0 site implementation** | Codex | Luna | **10–14 h** | New homepage, shared shell/nav/footer, research/programme pages, publication empty state, About/Contact and space-focused language on a non-production branch |
| **6. Discussion-paper and image integration** | Codex, Work editorial review | Luna | **5–7 h** | Papers 1–4 retained at same URLs, article styles integrated, their original body content/images preserved or changed only via separately approved editorial corrections; planned Papers 5–16 not passed off as completed |
| **7. Educational/programme content pilot** | Work for copy; Codex for layout | Luna | **6–9 h** | One fully checked BridgePoint pilot lesson, other 15 lesson titles marked planned; 5×4 project/phase descriptions for NSRP and SEIP, with no false completion claims |
| **8. Quality, accessibility and scientific review** | Codex technical; Work content/design; Chat final acceptance | Luna; Terra only if justified and approved | **4–6 h** | Actual desktop/mobile browser renders, keyboard checks, link and sitemap audit, metadata, contrast, alt text, content statuses, regression test evidence and correction PRs |
| **9. Publication and post-launch verification** | Chat authorises; Codex deploys/checks | Luna | **2–3 h** | Owner-approved merge only; GitHub Pages status and live URL checks; documented release, rollback path and completion DTSU |

**Total estimated active effort: 45–65 hours.** These figures include normal first-pass corrections and review work, but exclude waiting between user approvals and extensive new content research beyond the initial pilot.

**Indicative elapsed schedule:** **3–5 weeks** if the work receives roughly 12–20 productive hours per week and the project owner can review outputs promptly. A different cadence, unexpected rework or third-party asset issues can extend the calendar duration. This is a planning estimate, **not** a promise that any work will run asynchronously or be delivered on a particular date.

## Review/release gates

1. **After Stage 3:** Owner approves content scope, IA, programme terminology and scientific maturity labels.
2. **After Stage 4:** Owner approves real browser design renders before site-wide coding.
3. **After Stage 7:** Owner reviews site content and one BridgePoint lesson; outstanding planned content is labelled honestly.
4. **After Stage 8:** Owner sees actual smartphone/desktop results, accessibility tests and list of unresolved issues.
5. **Stage 9:** A separate, explicit **merge/deploy approval** is required. No earlier design/content approval is permission to merge.

## GitHub delivery strategy

- Maintain the current public `main` branch and existing site until Stage 9.
- Keep this plan in the documentation-only planning PR.
- Codex opens a **separate implementation PR** on a new feature branch; no direct edits to public `main`.
- Use short, independently reviewable commits/PRs for design shell, sections, legacy articles and QA (avoid merging partially completed replacement pages into production).
- Build and check previews from the implementation branch or a safe staging environment. If a preview route cannot be verified, report the limitation instead of inventing screenshots.
- The current website remains recoverable from Git history; document the specific rollback commit/steps before launch.
- Use the established DTSU convention at milestones, with source links, actual checks, defendable progress percentages and updated ETA ranges.

## Risk/contingency register

| Risk | Control |
| --- | --- |
| Existing discussion papers or SEO URLs break | Freeze four original article paths and run regression/link tests |
| Old start-up claims remain | Explicit content inventory and final editorial sweep |
| Scientific claims overstate evidence | Work review with status labels and relevant source traces |
| Broken mobile or inaccessible mathematical layout | Mobile-first prototypes, semantic math, keyboard and actual browser tests |
| Existing images are unsuitable or unlicensed | Asset shortlist and rights/provenance review; use neutral alternatives where needed |
| Model costs/usage inflate | Luna-first, small task briefs, avoid overlapping Work/Codex writes; Terra only with approval |
| Launch affects live site unexpectedly | Separate branch/PR, owner merge gate, GitHub Pages validation and rollback plan |

## Later development (not part of v2.0 launch estimate)

- Write, fact-check, illustrate and publish the **remaining 15 BridgePoint lessons** through a separate editorial programme; preliminary extra effort **~45–90 hours**, highly dependent on mathematical depth and graphics.
- Add real NSRP/SEIP results **only** after research, calculations and/or simulations are actually completed and reviewed; no finite delivery estimate is justified before those studies are scoped.
- Consider search, interactive mathematics, downloadable notebooks or a dedicated space-science reading library only when the core website is stable.

**No website HTML, CSS, JavaScript or public article content is changed by this planning document.**
