# SymTech Ventures v2.0 — Stage 6 Website Implementation

**Task:** Build the v2.0 website on a separate GitHub branch and return a verified draft pull request.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Tracker:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)  
**Status:** Handover prepared; implementation not yet started.

## 1. Read the approved sources

Use these exact GitHub sources before changing files:

1. [Approved website architecture and visual requirements](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md) — page hierarchy, routes, navigation and starfield.
2. [Stage 5 website copy](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/editorial/V2_STAGE_05_WEBSITE_COPY_DRAFT.md) — page introductions, copy and evidence-status wording.
3. [Programme structures and phase titles](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/PROGRAMME_SERIES_STRUCTURE.md) — authoritative website catalogue for 16 BridgePoint lesson titles and 20 phases each for NSRP and SEIP.
4. [Scientific/editorial review and cautions](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_05_EDITORIAL_REVIEW_20261116.md) — wording boundaries and open issues.
5. [Image reuse and legacy content audit](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/reports/V2_STAGE_02_ASSET_AUDIT_20261116.md).
6. [Approved homepage prototype](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/prototype/space-first-homepage-20261116/prototypes/v2-homepage/index.html) and [its verification notes](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/prototype/space-first-homepage-20261116/prototypes/v2-homepage/README.md).
7. [DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md) — read and follow during execution.

The design and content sources are on the **planning** and **prototype** branches, not on production `main`. Read them directly from their links. The Stage 5 text is an editorial draft: implement it as specified without inventing scientific findings, and flag material ambiguities.

## 2. Branch and pull request

- Fetch the latest `main` and record its starting commit SHA.
- Create `feature/v2-space-research-website` from `main` (use a unique suffix if already present).
- Recreate/adapt the approved prototype in the actual production page structure; do **not** merge the prototype or planning pull requests as a shortcut.
- Make focused commits and open **one draft pull request against `main`**.
- Do **not** push directly to `main`, merge any PR, deploy the website or contact external parties.
- Avoid unrelated refactors, generated placeholder articles and bulk migration of Google Drive materials.

## 3. Implement the website

SymTech Ventures is now an **independent research project focused primarily on space exploration**, not a Silicon Valley start-up. Use the approved dark, elegant research-library design, UK English and accessible layouts.

| Route | Required result |
| --- | --- |
| `/index.html` | New homepage, six main navigation links, four programme cards, links to four original papers and honest project description |
| `/pages/research.html` | Research overview explaining SYMMETRIA, NSRP, SEIP and their relationship to space exploration |
| `/pages/symmetria.html` | Clearly exploratory theoretical framework, linked to discussion papers |
| `/pages/nsrp.html` | **5 named research projects × 4 phases = 20**, with unverified work labelled planned |
| `/pages/seip.html` | **5 engineering companion projects × 4 phases = 20**, with no completed technical results invented |
| `/pages/bridgepoint.html` | **4 lesson categories × 4 lessons = 16**; all unwritten lessons marked planned |
| `/pages/discussion-series.html` | Four existing online discussion papers plus twelve planned entries |
| `/pages/publications.html` | **Zero formal publication entries** and a short empty-state explanation |
| `/pages/about.html` | Independent-project purpose, research limitations and LinkedIn link |
| `/pages/contact.html` | Existing contact route remains reachable; do not silently change the enquiry service |

**Primary navigation:** Home · Research · BridgePoint · Discussion Papers · Publications · About. Contact should be reachable from About and the footer. Use the supplied LinkedIn URL: `https://www.linkedin.com/in/drgeoffthomas`.

Build reusable site CSS, navigation, page layouts and footer. The homepage prototype establishes the approved appearance; replace its prototype-only anchor destinations with actual page routes.

**Do not write or link to a fictitious completed BridgePoint lesson.** A full pilot lesson is a subsequent task. Build a reusable lesson layout only if it is useful without adding false content.

## 4. Preserve existing research material and URLs

These original URLs must remain valid and their substantive article content and paper illustrations must be preserved:

- `/articles/symmetria/symmetria-paper-01.html`
- `/articles/symmetria/symmetria-paper-02.html`
- `/articles/symmetria/symmetria-paper-03.html`
- `/articles/symmetria/symmetria-paper-04.html`

Record the existing Git blob SHA of each before work begins. **Prefer leaving the article HTML files unchanged** during this stage. If changes are essential for compatibility, document exact before/after differences and preserve article text, images, URLs and navigation between papers.

The four accessible papers are **discussion essays**, not automatically peer-reviewed research publications. Papers 5–16 remain planned.

Preserve functioning legacy URLs, including divisions, founding fellows, enquiry and thank-you pages, unless an explicit redirect/historical route is implemented and tested. Keep `CNAME` intact. Update `sitemap.xml` and page metadata only for real implemented pages; keep original paper canonical destinations.

## 5. Retain the starfield

The existing website's recognisable starfield is an **approved design requirement**. Reimplement the effect in a small, appropriately named shared v2 component; do not copy old AetherOS code or branding indiscriminately.

- Keep the effect subtle and visually present on principal pages, without obscuring reading.
- Treat visual canvases as decoration (not focusable or announced by screen readers).
- Honour `prefers-reduced-motion: reduce` with static stars or disabled animation.
- Reduce particle density and rendering cost on mobile.
- Pause or throttle animation when the page is hidden.
- Ensure adequate contrast and readable long-form article surfaces.

Do not claim full accessibility or mobile performance verification until actual tests have been run.

## 6. Scientific, asset and privacy safeguards

- Distinguish **established physics**, **exploratory hypotheses**, **planned research**, **simulations** and **empirical findings**.
- Do not imply verified unified-field physics, new space propulsion, operational laboratories or funded divisions.
- The existing logo, abstract hero and paper artwork may be reused only within their documented existing context or after appropriate rights review. Do not introduce unclear new image rights or use fictitious wormhole/laboratory pictures as evidence of real facilities.
- Do not rewrite the four original scientific papers as part of website styling.
- Keep planned NSRP/SEIP phases marked as plans; the NCP phase wording is provisional in the source catalogue.
- Retain the original Contact/enquiry behaviour unless reviewed. Avoid exposing additional private email addresses or external form details.

## 7. Implementation checkpoints

1. **Shared design:** site shell, responsive navigation, footer, approved homepage styling and starfield.
2. **Research pages:** Research, SYMMETRIA, NSRP, SEIP, BridgePoint; verify exact **16 / 20 / 20** catalogue counts.
3. **Reading and support pages:** Discussion Papers, empty Publications, About and preserved Contact/legacy paths.
4. **Initial technical verification:** desktop/mobile renders, keyboard access, link and resource checks, reduced-motion behaviour, sitemap and article preservation.

Use one branch and one draft PR. Keep changes bounded to the requirements above and stop after reporting verified implementation results; do not begin subsequent editorial or release stages.

## 8. Verification evidence required

Record actual commands and outcomes (passed, failed, skipped or blocked) in a versioned `docs/reports/` report in the draft PR.

- All required routes exist and the six main nav links resolve.
- **BridgePoint:** 4 groups/16 lesson titles; **NSRP:** 5 projects/20 phases; **SEIP:** 5 projects/20 phases.
- **Discussion Papers:** exactly four available online and twelve planned. **Publications:** zero formal entries.
- Existing four article URLs, bodies, key image references and pagination preserved.
- Keyboard navigation, focus visibility, headings, image descriptions and functional mobile menu checked.
- Real desktop and smartphone browser screenshots; test horizontal overflow at **320px and 390px**.
- Basic starfield reduced-motion and hidden-tab behaviour checked and reported.
- Broken links, console errors, missing resources and unresolved privacy/image-rights concerns listed.
- Confirm the implementation branch is isolated and `main` has not changed.

This is the initial implementation check; a separate later stage conducts comprehensive regression and accessibility verification.

## 9. Required progress updates — DTSU v1.1

Read the linked DTSU standard before starting. Send **visible user-facing** updates in this form, at real Europe/London time:

```text
[HH:MM:SS] NN% — Concrete whole-task progress and evidence; ETA ~remaining duration.
```

- Give a **0%** update before making changes.
- Update at genuine 10% milestones, or every 10–20% if steps finish quickly, and every 3–5 minutes on longer intervals.
- Include an **ETA in every update**; use `ETA unknown` if genuinely impossible to estimate.
- Report failures and blockers without inflating progress.
- Give **100% / ETA 0 minutes** only after validating deliverables and handing back the draft PR.
- Do not substitute private logs for visible updates or fabricate timestamps and test results.

## 10. Final COPY TO CHAT handback

Finish with a short, paste-ready **COPY TO CHAT** report giving:

- Draft PR URL, feature branch, exact final commit SHA and list of changed areas.
- Tests actually performed, outcomes, and screenshot/report paths.
- Four article integrity findings, programme counts, empty Publications confirmation and starfield checks.
- Remaining blockers, risks and specific questions for the next content-review stage.
- Confirmation that **nothing was merged or deployed**.

**Stop after the handback. No publication or merge is authorised by this task.**
