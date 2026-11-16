# SymTech Ventures v2.0 — Stage 6C: Complete Website Pages and Navigation

**Task:** Finish the remaining v2.0 static-site pages and navigation on **the existing Stage 6 development branch and draft PR**. This is the final implementation checkpoint of Stage 6, **not** the final quality/release review.

**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Branch:** `feature/v2-space-research-website`  
**Existing PR:** [#5 — v2 space research website](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5) (**open, draft and unmerged**)  
**Last confirmed head:** `25d1de72b958c7bcaf4d33fa45e2727f4ba73dec` — inspect current branch head before committing.  
**Tracker:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)

## Read these exact sources

1. [Stage 5 website copy](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/editorial/V2_STAGE_05_WEBSITE_COPY_DRAFT.md) — specifically sections **D01 Discussion Papers, P01 Publications and A01 About**, plus footer/status conventions.
2. [Approved information architecture](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/V2_STAGE_03_INFORMATION_ARCHITECTURE.md) — six top-level destinations, stable legacy paths, privacy and accessibility constraints.
3. [Stage 6B verification report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_06B_PROGRAMME_VERIFICATION.md) and [Stage 6A report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_06A_HOMEPAGE_VERIFICATION.md).
4. [Original discussion-series manifest](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/main/articles/symmetria/SYMMETRIA_Paper_Series_Manifest.json) — authoritative existing **four online + twelve planned** titles and statuses.
5. [DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md) — mandatory user-visible updates.

The editorial documents are on an **unmerged planning branch**. Use their exact links; do not assume they are present on the implementation branch.

## Implement only this remaining scope

### A. Create the two outstanding pages

- **`pages/publications.html`**: full shared v2 shell; heading **Publications**; **zero formal publication records** and the exact approved empty-state wording. A clearly labelled link may point to the distinct Discussion Papers index. Do not mislabel the four public essays as peer-reviewed publications, generate fake citations, or show unissued papers as completed.
- **`pages/about.html`**: independent space-exploration research description, scientific/evidence caveat, programme links, **Dr Geoffrey Thomas on LinkedIn** linking to `https://www.linkedin.com/in/drgeoffthomas`, and reachable `pages/contact.html`. Do not invent institutions, qualifications beyond approved source text, laboratory capacity, sponsorship or personal contact details.

### B. Integrate the Discussion Papers index

- Update **the existing** `pages/discussion-series.html` to the v2 dark layout, permanent starfield, responsive shared navigation and accessible reading experience.
- Keep the established **four categories × four entries**, with the first four linked at their **exact existing article URLs**, and **twelve entries labelled Planned** with **no dead article links**.
- Use title spelling from the source manifest. The old manifest calls the four online essays `Published`, but the **public page must say `Available online — discussion paper`**. Do not change the historical manifest merely to change front-end wording.
- Keep original article HTML pages, substantive bodies, illustrations, current URLs and pagination untouched. Do not silently rewrite Paper 15's provisional historical title.

### C. Complete shared navigation and link destinations

- Remove obsolete `Stage 6B` / `Stage 6C` pending markers **only where destination pages really exist**.
- On the homepage and all v2 pages, make the six nav links resolve to actual pages: **Home, Research, BridgePoint, Discussion Papers, Publications, About**.
- Keep the SYMMETRIA, NSRP and SEIP cards linked to their implemented pages and the existing four paper links unchanged.
- Retain the agreed **site-wide subtle starfield**; respect `prefers-reduced-motion`, readable contrast and keyboard navigation. Reuse existing `css/v2-site.css` and `css/v2-programmes.css` rather than redesigning.
- Ensure About and footer link to the existing Contact page. **Do not replace or alter the existing third-party enquiry form handler** in this checkpoint.

### D. Sitemap, metadata and legacy compatibility

- Update **`sitemap.xml`** to include **only real implemented pages**, including newly completed `research.html`, `bridgepoint.html`, `seip.html`, `publications.html` and `about.html`, while preserving all four existing paper URLs and current domain.
- Keep `CNAME` intact. Use accurate canonical URLs and page titles/descriptions. **Do not fabricate historical `lastmod` dates**; omit new lastmod fields if a genuine source date is unavailable.
- Legacy routes **`pages/divisions.html`**, `pages/founding-fellows.html`, division pages, `pages/contact.html`, `pages/enquiry.html` and `pages/enquiry-thanks.html` must remain accessible. Do **not** delete them, create unapproved redirects or silently change form services.
- Record any outdated old-site navigation/recruitment language still present on legacy pages and original article shells as a **Stage 8 editorial/legacy-regression issue**; do not spend this bounded implementation pass rewriting every historical file.
- Preserve existing links to `/pages/discussion-series.html` and all original article paths.

## Not part of Stage 6C

Do **not** create any completed BridgePoint lesson (pilot is Stage 7), add research results, write more SYMMETRIA papers, redesign five programme pages, alter the scope of NSRP/SEIP, conduct a full accessibility/SEO audit, or publish the website. Do not bring in new images or copy private documents into the public repo.

## Required verification

Run actual local website/browser checks and save **`docs/reports/V2_STAGE_06C_SITE_COMPLETION_VERIFICATION.md`** on the feature branch:

1. All six primary nav destinations return **HTTP 200** and appear with the correct titles; no remaining `Stage 6B` / `Stage 6C` placeholders on completed v2 pages.
2. Publications shows **zero** formal research entries. Discussion Papers shows **four live + twelve planned** entries with links only for the live four.
3. BridgePoint **4 categories/16 lessons**, NSRP **5 projects/20 phases**, SEIP **5 projects/20 phases** remain unchanged.
4. All four original paper **Git blob hashes match** the original `main` baseline. Confirm their figures/assets and URLs remain present.
5. Desktop ~1440px and smartphone 390px/320px: at least one actual screenshot each for **About, Publications and Discussion Papers**, plus navigation/overflow/console checks.
6. Keyboard skip links, focus visibility, mobile menu, reduced-motion starfield and link integrity smoke-tested. Be explicit about untested accessibility aspects.
7. Parse `sitemap.xml` as XML, verify it lists the new genuine pages and all four articles and that `CNAME` remains unchanged.
8. Legacy Contact/enquiry and other old URLs remain available; **record privacy/form-handler review as pending** if it cannot be safely verified without submitting personal data.
9. Commit and push changes to **the same branch and draft PR #5**; give actual commit SHA, changed paths and reproducible tests. List anything failed, blocked or deferred rather than claiming it passed.

**Never merge, deploy, move the PR out of draft or touch `main`.** Stage 7 editorial content acceptance and Stage 8 full quality review still follow.

## DTSU v1.1

Read the linked DTSU standard first. Send visible updates using the **actual current UK-local clock**:

`[HH:MM:SS] NN% — Concrete whole-task progress; ETA ~remaining time.`

Start with **0% before work**, give truthful 10% milestone updates (at minimum every 10–20% when steps finish quickly), and update every 3–5 minutes during long intervals. Every update needs an ETA; use `ETA unknown` if genuinely incalculable. Report **100% / ETA 0 minutes** only after the code, checks, report and handback are genuinely complete.

## COPY TO CHAT handback

Finish with a concise, paste-ready report stating: **draft PR #5**, branch, final commit SHA, completed pages, four-plus-twelve and 16/20/20 counts, original article hash integrity, sitemap and navigation checks, screenshot/report links, open risks and next Stage 7 needs. **Stop after Stage 6C.**
