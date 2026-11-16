# SymTech Ventures v2.0 — Stage 6 Codex Implementation Handover

**Status:** Prepared by Chat; **not yet executed**  
**Project lead:** Chat  
**Specialist:** Codex, prefer **Luna** wherever selectable; **Terra is not authorised** without owner approval.  
**Scope:** Build the complete **review-only** replacement website on a GitHub feature branch, keeping the live site untouched.  
**Tracker:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## Source documents — read these before coding

1. [Stage 5 page-by-page draft copy](../editorial/V2_STAGE_05_WEBSITE_COPY_DRAFT.md): exact page introductions, evidence/status terminology, title/meta guidance and CTA text.
2. [Stage 5 source/accuracy review](../reports/V2_STAGE_05_EDITORIAL_REVIEW_20261116.md): material scientific limits, copyright/figure risk and source references.
3. [Approved Stage 3 information architecture](../V2_STAGE_03_INFORMATION_ARCHITECTURE.md): page routes, six navigation destinations, mobile design and **retained starfield**.
4. [Corrected programme structure](../PROGRAMME_SERIES_STRUCTURE.md): **SYMMETRIA 4×4**, **BridgePoint 4×4**, **NSRP 5×4**, **SEIP 5×4**. Exact phase names come from this file.
5. [Approved Stage 4 homepage prototype and readme](https://github.com/SymTechVenturesOrg/symtechventures.github.io/tree/prototype/space-first-homepage-20261116/prototypes/v2-homepage), also [prototype PR #4](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/4).
6. [Website development workflow](../WEBSITE_DEVELOPMENT_WORKFLOW.md) and [project charter](../V2_PROJECT_CHARTER.md).

These planning files are on **`planning/space-first-research-website-20261116`**. They are not yet in production `main`. Fetch from this exact branch and don't assume they're accessible at a local relative path in the implementation branch.

## Goal and branch boundary

Implement a visually cohesive, desktop/mobile accessible, **space-exploration-focused independent research website**. The old start-up marketing language and page shell are replaced, **but the live site is not changed** until the owner explicitly approves the final release at Stage 9.

- Branch the implementation work from the **approved Stage 4 prototype branch** or its exact reviewed commit, then compare against production `main`. Do **not** merge PR #4 or PR #2 automatically.
- Open a **draft implementation PR** against `main`. Do not push direct changes to `main`, merge or deploy.
- Keep changes focused: new shared v2 styling, navigation, a restrained starfield, actual page implementations, metadata/sitemap updates where needed, and preservation of original article content/paths.
- Do not copy private theory manuscripts, historic Google Drive folder trees, experimental AetherOS components, old investor content or invented scientific results.
- A standalone/prototype directory may remain; root `index.html` is to be replaced **only on this unmerged implementation branch**, never production before Stage 9.

## Required pages / routes

| Route | Required content |
| --- | --- |
| `/` | Approved homepage style and starfield, four programmes, four existing discussion-paper links, evidence note |
| `/pages/research.html` | Research relationship and space-first interests |
| `/pages/symmetria.html` | Exploratory SYMMETRIA questions; preserve discussion access |
| `/pages/nsrp.html` | **5 named research projects × 4 phases = 20**; all unverified phases explicitly planned |
| `/pages/seip.html` | **5 engineering companion projects × 4 phases = 20**; no simulated result claimed |
| `/pages/bridgepoint.html` | **4 categories × 4 lesson titles = 16**; all marked planned until verified |
| `/pages/discussion-series.html` | Four available essays at original links, twelve future entries clearly planned |
| `/pages/publications.html` | **Zero** formal publication records; plain empty state |
| `/pages/about.html` | Independent research identity, source/assumption transparency, LinkedIn |
| `/pages/contact.html` | Existing URL remains reachable; inspect privacy before reusing form services |

**BridgePoint pilot:** Stage 7 will write/review the first genuinely complete lesson. During Stage 6 provide a reusable lesson layout but **do not publish a fake full lesson or active links to nonexistent lessons**.

## Existing content that must not break

1. `/articles/symmetria/symmetria-paper-01.html`
2. `/articles/symmetria/symmetria-paper-02.html`
3. `/articles/symmetria/symmetria-paper-03.html`
4. `/articles/symmetria/symmetria-paper-04.html`

Preserve the **article's substantive body, existing paper-specific images and URL** exactly unless a separately reviewed editorial change is approved. If changing common nav/shell, compare saved before-and-after article content and all image paths. Keep article pagination intact. The manifest currently has four `Published` and twelve `Planned` entries; show website-facing labels as **`Available online — discussion paper`**, without pretending formal peer-reviewed publication.

Other legacy URLs, including divisions, founding-fellows, enquiry and thank-you pages, must not simply become 404s; preserve/redirect through an intentional documented approach.

## Starfield — **explicit owner approval**

**Keep the recognisable dark starfield across v2.0**, with restrained twinkling and unobtrusive motion. Existing `main:js/main.js` has canvases called `aetheros-starfield` and `aetheros-shimmer-layer` and **explicitly lacks a reduced-motion bypass**.

- Reimplement or extract only the necessary visual behaviour in a **new, appropriately named v2 module**; do not blindly transplant the legacy `main.js` or restore old AetherOS branding.
- Respect `prefers-reduced-motion: reduce`: use a static field or disable animation.
- Throttle/suspend when the tab is hidden; limit device pixel ratio/particle density on mobile; ensure canvas is purely decorative and hidden from screen readers.
- Preserve body text contrast, particularly on lesson/article pages; starfield effects must not create motion sickness or hinder reading.
- Verify low-end smartphone performance during Stage 8; do not claim compliance without tests.

## Accessibility and scientific wording

- Mobile-first, semantic HTML, correct heading order, visible keyboard focus, descriptive alternative text and working navigation without relying solely on JS.
- Six top-level links: Home, Research, BridgePoint, Discussion Papers, Publications, About. Footer includes LinkedIn `https://www.linkedin.com/in/drgeoffthomas` and reachable Contact.
- UK English, clearly differentiating **established physics**, *research questions*, *mathematical consistency*, *planned simulation* and *actual measured evidence*.
- No unverified propulsion, faster-than-light travel, space laboratory, investor funding, registered institution or completed programme claims.
- All 40 NSRP/SEIP phases are **programme plans**, not accomplishments; four Paper 1–4 pages remain discussion essays; formal Publications count is zero.
- Image rights and equation annotations were not independently cleared by Stage 5; avoid unapproved new reuse of visual assets.
- The existing contact-form source contains a recipient email and external submission handler. Avoid spreading those details to new pages without privacy review.

## Bounded milestones within this one Codex engagement

1. Build common site shell, CSS, starfield and homepage from approved prototype.
2. Implement Research, SYMMETRIA, NSRP, SEIP and BridgePoint pages from the **Stage 5 draft** and exact programme structure.
3. Implement Discussion Papers, empty Publications and About; preserve four original articles, legacy URL compatibility and Contact.
4. Perform initial semantic, local link and browser checks; collect real desktop/mobile screenshots and document defects in PR.

Do not proceed to Stage 7 or Stage 8 independently. Chat reviews milestone/PR evidence and will authorise subsequent tasks.

## Minimum handback evidence

- Draft PR URL and exact branch/commit(s).
- New/changed file list and original four article path/content/image preservation evidence.
- Page count and **BridgePoint 16 / NSRP 20 / SEIP 20** count checks.
- At least one real desktop and one real mobile browser screenshot, with honest source paths; check overflow at 390px and 320px.
- Internal link and sitemap checks, heading semantics, tab-focus and starfield reduced-motion fallback results.
- A concise **COPY TO CHAT** message: completed scope, tests passed/failed, issues and next review action.
- Follow the project's DTSU v1.1 format with actual UK clock time, true whole-stage percentage, regular visible updates and ETA. Report tool limitations, don't fabricate tests.

**Stop condition:** Finish after a reviewable **unmerged PR and verification report**. No autonomous production merge, website deployment, contacting people or publication of new science.
