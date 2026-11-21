# SymTech Ventures v2.0 — Stage 6B: Research and Programme Pages

**Task:** Continue Stage 6 using the existing Stage 6A feature branch and draft PR. Build **five research/learning pages only**, verify them, then stop.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Implementation branch:** `feature/v2-space-research-website`  
**Existing draft PR:** [#5 — Stage 6A homepage](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Tracker:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## Begin with existing, verified code

Stage 6A is already committed as `49cb1419492dd378078528bed5f65281d794c44c`. Its source, stylesheet, verification report and browser screenshots are in **PR #5**. It preserves the four original SYMMETRIA articles. **Continue from this branch and update PR #5**; do not recreate the homepage, open a duplicate PR, start from `main`, merge earlier planning/prototype PRs or modify production `main`.

First verify the branch head and working tree. If the branch has advanced beyond that commit, inspect the difference and preserve other legitimate work.

## Source of truth — read before editing

1. [Stage 5 page copy](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/editorial/V2_STAGE_05_WEBSITE_COPY_DRAFT.md): sections **R01–R04** and **L01**.
2. [Corrected programme structure](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/PROGRAMME_SERIES_STRUCTURE.md): all canonical category, project, phase and lesson titles.
3. [Approved information architecture](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md).
4. [Stage 5 editorial cautions](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_05_EDITORIAL_REVIEW_20261116.md).
5. [Stage 6A verification report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_06A_HOMEPAGE_VERIFICATION.md).
6. [DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md).

These editorial planning documents are held on a **different unmerged branch**. Fetch them directly from their links; do not assume they are in your implementation checkout.

## Implement exactly five pages

1. `pages/research.html` — **Research Overview:** independent space-exploration focus; SYMMETRIA → NSRP → SEIP with two-way critical feedback; BridgePoint as the learning route. Explain the difference between a question, mathematical statement, simulation and measured evidence.
2. `pages/symmetria.html` — **SYMMETRIA:** adapt the existing page to the v2 shared site design and approved concise exploratory framing. Keep original discussion-paper access and avoid implying the theory is experimentally validated.
3. `pages/nsrp.html` — **NSRP:** five *named research projects*, each displaying **four phases** (**20 total**) with source-grounded titles, short explanations and **Planned/provisional** status labels unless actual evidence supports another status. Projects: NCP, SEP, SDEP, SVP, SMP. Note that detailed NCP phase descriptions are **provisional** in the planning sources.
4. `pages/seip.html` — **SEIP:** five *companion engineering projects*, each with **four phases** (**20 total**) using source-grounded names and explanations. Projects: EFP, SEP, SDP, SVP, SMP. Explicitly distinguish computational proposals from verified spacecraft technology.
5. `pages/bridgepoint.html` — **BridgePoint:** four lesson categories with exactly **four named lessons each** (**16 total**), using the approved titles and learning outcomes. All lessons are currently **Planned**; do not create links to absent lessons or write a fictitious pilot lesson. The full pilot belongs to Stage 7.

**For all five pages:** use the existing `css/v2-site.css`, shared dark/starfield visual language, semantic headings, accessible keyboard navigation, a functional mobile menu, consistent footer and LinkedIn link. Prefer small reusable elements, straightforward HTML/CSS and minimal JavaScript. Preserve the existing site's recognisable space aesthetic without overloading long-form text.

## Shared navigation and link behaviour

- Link from the homepage to **Research** and **BridgePoint** now that their real pages exist; remove Stage 6B placeholder labels from links whose destinations have actually been implemented.
- Ensure page navigation can reach all five new/adapted pages. The homepage's SYMMETRIA and NSRP cards must lead to the correct updated pages; the SEIP card must now lead to the new page.
- **Publications** and **About** are **Stage 6C** destinations; do not pretend they are complete. Keep their pending labels until actual pages exist.
- The existing **Discussion Papers** page and the original four paper URLs remain unchanged in this checkpoint. Do not break or rewrite them.
- Keep working Contact, legacy divisions/founding-fellows URLs, `CNAME`, the original article files and form handlers intact.
- Do not add nonexistent lesson/article routes to `sitemap.xml`. Sitemap integration and broader legacy navigation clean-up belong to Stage 6C and Stage 8.

## Engineering boundaries and acceptance

- Work in **the same feature branch and draft PR #5**. Do not merge, deploy, change PR state to ready or publish the new site.
- Do not independently change scientific claims, programme project names, phase names, mathematical content or article bodies beyond approved summaries.
- Do not add new third-party imagery, contact recipients or unapproved code dependencies.
- Build five actual pages and ensure their document titles, content descriptions and internal links refer to the correct programme and research focus.
- The homepage has an existing **static CSS starfield**; preserve it. Later visual review may consider carefully restrained animation, but do not undertake an open-ended visual redesign here.
- Verify content counts by inspecting actual rendered DOM/source, not by asserting that the planning document itself has the right counts.

## Required checks and evidence

1. Serve the implementation branch using a local server and test **all five pages** at ~1440px desktop and 390px mobile; check 320px where sensible.
2. Confirm **Research, SYMMETRIA, NSRP, SEIP, BridgePoint routes** return HTTP 200 and navigation links resolve.
3. Verify **BridgePoint 4 categories / 16 lessons, NSRP 5 projects / 20 phases, SEIP 5 projects / 20 phases** from the implemented pages.
4. Check semantic headings, keyboard menu and skip links, visible focus, layout overflow and browser console errors.
5. Confirm original four paper file hashes and article URLs remain unchanged; recheck that there are **zero** formal publication entries (the dedicated Publications page is still pending).
6. Capture at least one actual desktop and mobile screenshot of **a programme page**; keep screenshots distinct from the existing Stage 6A screenshots. Capture the navigation menu **closed by default** for visual review and optionally a separate open-menu state for interaction evidence.
7. Record precise test commands and pass/fail/pending outcomes in `docs/reports/V2_STAGE_06B_PROGRAMME_VERIFICATION.md`. Include unresolved **Stage 6C** routes as pending, not as successful links.
8. Commit and push changes to the existing feature branch and update **draft PR #5**. Report the final commit SHA, changed files and verification evidence.

## v1.1 DTSUs and stop condition

Read the linked DTSU standard. Send visible progress updates with actual UK-local time, beginning **0% before actions**, in the form:

`[HH:MM:SS] NN% — Factual whole-task progress; ETA ~remaining time.`

Update on genuine 10% milestones or every 3–5 minutes during longer intervals. Every DTSU requires an ETA (or `ETA unknown` if genuinely unknowable). Report **100% / ETA 0 minutes** only when the Stage 6B files, tests, report and handback are all verified.

Finish with **one concise COPY TO CHAT handback** listing existing draft PR #5, final commit, five implemented routes, counts, checks, evidence URLs and remaining Stage 6C work. **Stop after Stage 6B: no merge, no deployment and no autonomous Stage 6C.**
