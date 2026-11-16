# SymTech Ventures v2.0 — Stage 8B: Post-Approval Browser Regression

**Task:** Test and verify the **already committed** privacy/indexing and no-star/justified-text changes on the **actual implementation branch**. Fix only reproducible regressions, document results and stop. **Do not merge or deploy.**

**Repo:** `SymTechVenturesOrg/symtechventures.github.io`  
**Branch:** `feature/v2-space-research-website`  
**Existing draft PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5) — do not open another PR.  
**Latest verified Chat commit at handover preparation:** `a533470a3af496ad25411335b498acda5ea0cd96`; inspect the actual HEAD before work.

## Read these exact files

1. [Approved privacy and historical indexing changes — evidence and remaining risks](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_20261116_PRIVACY_AND_ARCHIVE_CONTROLS.md).
2. [Updated reproducible QA script](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/scripts/v2_stage8_qa.py).
3. [Prior Stage 8 QA baseline](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_STAGE_08_WEBSITE_QA.md).
4. [Post-change typographic/no-star design decision](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_POST_QA_DESIGN_ADJUSTMENT_20261116.md).
5. [DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md).

## Work

1. Use the **existing** feature branch. Run `python3 docs/reports/scripts/v2_stage8_qa.py` from its actual checkout with Chromium/Playwright dependencies available. If missing, report precise setup/blocker; do not invent a pass.
2. Debug the revised regression script if necessary; **do not water down checks** to hide failures. It now expects exactly **16 sitemap locations**, retains four paper URLs, checks seven historical `noindex,follow` directives, and checks Contact/Enquiry/legacy confirmation.
3. Test the Contact and Enquiry pages via **read-only browser navigation only**. Confirm the enquiry page has **no `form`/POST handler/input controls**, clearly says submissions are paused, and has a working link back to Contact. Confirm the old thank-you URL does **not** imply a message was received. **Do not submit personal data or reconnect the third-party provider.**
4. Visit all seven historical URLs; confirm they still return HTTP 200, display their historical-context notes, contain exactly one `noindex,follow` directive, and are **not** in the 16-entry sitemap. Keep `robots.txt` crawlable so search engines can read `noindex`.
5. Check all nine v2 pages and a representative original SYMMETRIA paper at **320, 390, 768 and 1440px**. Confirm full justification on running paragraphs with sensible line spacing; headings/nav/buttons normally aligned; **no CSS dotted starfield or animated canvas** anywhere, including original articles.
6. Capture **fresh, actual Chromium screenshots** under `docs/reports/screenshots/postapproval-*.png`, preserving earlier Stage 8 images. In particular show the homepage and an original article at desktop and 390px, plus the Enquiry status and one historical-page notice.
7. Check broken local links/resources, browser console errors, keyboard skip/menu focus, current programme catalogue counts (**BridgePoint 16 Planned/no links; NSRP 5×4; SEIP 5×4; SYMMETRIA four online/twelve planned; Publications zero**).
8. Compare original four paper bodies/figures against `main`, allowing **only** the prior documented skip-link and main landmark wrapper changes. Do not alter paper mathematical content or figures. Keep `CNAME` intact.
9. Record actual commands/results, screenshots, any failures and modifications in `docs/reports/V2_STAGE_08B_POST_APPROVAL_QA.md`; add/fix only narrow issues supported by tests. Commit/push to **the same branch and draft PR #5**.
10. Stop with a short **COPY TO CHAT** containing PR #5 link, final commit, pass/fail matrix, screenshots/report links, and unresolved release blockers (original image/figure provenance). Never claim image rights or research mathematics were independently certified.

## Stop and release boundary

- **No new BridgePoint lessons, new research claims, redirects, live contact form or external submission.**
- Do not undo the owner's **no starfield, justified text** preference.
- Do not re-index historic pages or restore them to sitemap.
- Do not merge PR #5, deploy the site, change the PR out of draft or trigger Stage 9.
- Any remaining concerns about original asset rights/form-provider backend are **owner decisions**, not Codex-improvised legal conclusions.

## User-visible v1.1 DTSUs

Read the linked DTSU file before actions. Begin with a real UK clock **0%** update, then factual whole-task milestones (ideally each 10%, at least 10–20%), with an ETA in every visible message and updates at least every 3–5 minutes during long operations. Use `ETA unknown` if needed; report **100% / ETA 0 minutes** only after the branch, scripts, screenshots, report and handback are verified.

**This is Stage 8B regression only, not authorisation to release the site.**
