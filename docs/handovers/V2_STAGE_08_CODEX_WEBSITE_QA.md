# SymTech Ventures v2.0 — Stage 8 Website Quality, Accessibility and Legacy Review

**Task:** Perform the final **website-only** technical, accessibility, compatibility and visual QA on the completed v2.0 implementation; apply narrow evidence-backed fixes on its existing branch and return a reviewable, unmerged PR.

**Website repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Existing feature branch:** `feature/v2-space-research-website`  
**Existing draft PR:** [#5 — v2.0 implementation](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Verified Stage 6 head:** `13f668358d3946efad13a47b338955b9443813fc`; recheck current HEAD before editing.  
**Project tracking:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

**Owner's scope change:** **Do not write, review, integrate, link or publish any individual BridgePoint lessons.** The site must show **four categories / 16 Planned lesson entries** only. A former introductory pilot has been shelved as too basic. This task is exclusively a **website upgrade and release-quality pass**.

## Read exact sources before work

1. [Stage 7 website-only editorial review](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_07_WEBSITE_EDITORIAL_REVIEW_20261116.md) — prioritised fixes and release concerns.
2. [Approved website architecture](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md) — space-first design, retained starfield, routes and status language.
3. [Canonical programme counts and titles](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/PROGRAMME_SERIES_STRUCTURE.md).
4. [Stage 6C browser and sitemap verification](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_06C_SITE_COMPLETION_VERIFICATION.md) plus the [existing reproducible smoke script](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/scripts/v2_stage6c_smoke.py).
5. [User-visible DTSU v1.1 standard](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md).

All planning/editorial references are on a separate **unmerged branch**. Do not assume they exist in the implementation checkout.

## Goal and scope boundaries

Keep v2.0 a calm, dark, space-themed **independent research website** with the recognisable starfield. Protect the original scientific articles; maintain all original URLs. No unverified research or functioning spacecraft/propulsion claims. No investor, startup recruitment or operational five-division portrayal on the new pages.

**Continue on the exact existing feature branch and draft PR #5**. Do not merge, deploy, mark ready, modify production `main`, create duplicate PRs or autonomously start Stage 9.

## Priority 1 — Website regressions and accuracy

**A. Full navigation/link coverage:** test every new top-level page, sub-programme page, four online papers, external LinkedIn, Contact/enquiry/thank-you, legacy division/founding-fellows pages and known relative image/CSS/JS references. Parse sitemap XML. Report HTTP codes, broken links, console errors and missing assets. External-service functionality must not be presumed from HTTP 200.

**B. Preserve content integrity:** record/compare blob hashes and image src inventories for the four original article files. Do not modify their main text, equations, figures or URLs without explicit owner approval. Preserve `CNAME` and domain configuration.

**C. Status integrity:** BridgePoint 16 **Planned** entries and **zero** lesson links. NSRP 5 projects/20 phases, SEIP 5 projects/20 phases, SYMMETRIA 4 readable/12 planned, formal Publications **zero**. NCP phase names still marked provisional. Compare actual DOM counts and accessible labels.

**D. Legacy identity:** inspect Founding Fellows, old five-division pages, Contact and article-shell navigation, which still contain former organisational messaging. Because these URLs are publicly reachable, **document an explicit approach**: preserve URL and add a clearly labelled historical/legacy context where appropriate; or propose a reviewed redirect/noindex strategy. A narrow, reversible archival notice on the implementation branch is allowed where clearly justified, with before/after evidence. Do not silently erase pages, remove incoming URLs or rewrite original research papers. Flag any policy choice requiring owner approval.

**E. Contact-form privacy:** inspect existing third-party form behaviour and visible privacy wording. Do **not** submit personal information, alter recipients, make real contact, introduce a new form service or publicly disclose embedded recipient addresses without owner permission. State what was actually tested, what requires owner decision and what should block deployment.

## Priority 2 — Visual system, accessibility and performance

**F. Starfield:** the owner wants the original space-like starfield retained. The current v2 shell has faint static CSS stars. Compare with the existing visual intent and verify stars are apparent on Home and secondary pages. If improving the effect is safe and small, propose or implement a **restrained, accessible** enhancement on the feature branch; keep the `prefers-reduced-motion` static fallback, reasonable mobile rendering cost and readable text. Do not copy legacy AetherOS animation wholesale. Mark any visual change for owner screenshot approval.

**G. Accessibility:** use actual Chromium keyboard-only navigation across site, check skip links, logical heading structure, menu open/close and focus management, contrast of text/links/focus, labelled controls and img alt, reduced motion, reading order and touch targets. Use available automated a11y tools where possible, but distinguish checks performed from WCAG certification. Manually inspect high-risk items; report skipped assistive-technology tests.

**H. Device and performance:** at minimum use 320px, 390px, 768px and 1440px viewports for principal pages, plus a representative long article; check overflow, nav, images, typography and CPU/memory burden of any starfield animation. Capture actual desktop/mobile screenshots (closed mobile menu by default; separate open-menu evidence optional). Be explicit whether a screenshot is from this run.

**I. SEO and metadata:** verify page titles, meta descriptions, canonical URLs, robots directives, Open Graph consistency as used, `sitemap.xml` validity, all 23 current entries' local destinations and whether outdated public legacy pages are prominently indexed. Do not fabricate last-modified dates or change historical article URLs.

**J. Asset permissions and mathematical figures:** avoid adding any new unverified image. Log source/rights uncertainties for original logos/figures and review whether formulae embedded in images were checked. If copyright provenance or exact maths correctness is unknown, mark it **unverified**, not passed. Owner decides final rights clearance.

## Deliverables and verification

- Record actual local test commands and browser environments, plus a concise pass/fail/skipped/blocker matrix, in `docs/reports/V2_STAGE_08_WEBSITE_QA.md`.
- Reuse and extend the committed Stage 6C smoke script where appropriate; add targeted checks rather than rewriting the entire test setup.
- Include links/paths to actual screenshots and a short ordered list of **P1 release blockers**, **P2 owner visual decisions** and **P3 optional improvements**.
- Include specific old/new file hashes or diffs for any modified legacy page, and a statement that the four paper URLs/content/images remain intact.
- Fix narrow safe issues directly in the existing draft PR #5; for unapproved redirects, form changes, asset rights or research-text revisions, leave a precise proposal rather than changing them.
- Conclude with a clear **Ready for owner release review** / **Not ready** decision backed by evidence. It is okay for QA to end as Not ready if issues remain.
- Keep PR #5 **open and draft**. Give final branch/commit, changed files, report and screenshot links, tests, unresolved risks, and a concise **COPY TO CHAT** handback. Stop; no merge/deployment.

## DTSU v1.1

Read the linked standard before work. Start with a **genuine UK-local current-time** 0% DTSU. Send factual progress updates at genuine ~10% whole-task milestones and at least every 3–5 minutes during long intervals. Use exactly this format:

`[HH:MM:SS] NN% — Factual status; ETA ~remaining duration.`

Every update includes ETA (or `ETA unknown` when not reliably estimable). Report 100%/ETA 0 minutes only after the actual tests, report, push and handback are verified. Do not invent time, results, work done or future deliveries.

**Stop after Stage 8 technical QA and verified draft PR evidence. Stage 9 production release requires separate explicit owner authorisation.**
