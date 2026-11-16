# SymTech Ventures v2.0 — Post-change checks and release options

**Date:** 16 November 2026 (GMT)  
**Website:** [Draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), branch `feature/v2-space-research-website`  
**Review state:** **Still not release-ready**. Source-level changes verified; real-browser checks on exact PR head **not yet repeated**. No merge or deployment.

## 1. Owner-approved styling changes

The owner specifically requested a **clean dark website without the starfield** and **fully justified text**.

**GitHub source checked directly on feature branch:**

| File | Verified state |
| --- | --- |
| `css/v2-site.css` | Removed the global `body::before` starfield pattern and the dotted `.hero:before` overlay. Contains `main p,.site-footer p{text-align:justify;text-justify:inter-word;hyphens:auto;overflow-wrap:break-word}`. |
| `js/main.js` | Legacy AETHEROS animated canvas/starfield creation and animation loop removed; smooth anchor scrolling and scroll-reveal functions retained. |
| `css/styles.css` | Added justified running text to original article and legacy pages without editing their HTML. |
| Four `articles/symmetria/symmetria-paper-0[1-4].html` files | All four blob hashes still match their post-Stage 8 QA baseline. No scientific article body, figure or URL was edited by these design changes. |

All changes were committed to the draft feature branch. The orbital **SVG** illustration remains; it is not an animated starfield.

## 2. Real Chromium preview — scope and limits

**Actual Chromium/Playwright test performed locally** on a copy of the **earlier self-contained homepage prototype** with the same two CSS changes (remove dotted hero star overlay; justify `main p` and `.site-footer p`). The test used `page.set_content` because network and localhost navigation were blocked in this execution environment.

| Viewport width | Horizontal overflow | Computed body paragraph alignment | Hero star pseudo-element | Canvas elements | Page errors |
| ---: | --- | --- | --- | ---: | --- |
| 320px | None | `justify` | `none` | 0 | 0 |
| 390px | None | `justify` | `none` | 0 | 0 |
| 768px | None | `justify` | `none` | 0 | 0 |
| 1440px | None | `justify` | `none` | 0 | 0 |

**Important limitation:** This is a **representative design spot-check**, not an exact-commit Playwright regression of PR #5. The preview does not reproduce all current GitHub pages or their external assets. Locally generated screenshots are held in this conversation's `/mnt/data/symtech_v2_typography_preview/` and are not committed to GitHub. The earlier [Stage 8 QA report](V2_STAGE_08_WEBSITE_QA.md) predates the design adjustment.

**Before any release**, run `python3 docs/reports/scripts/v2_stage8_qa.py` against the **latest** PR #5 checkout and capture fresh homepage, secondary page and original Paper 1 desktop/390px screenshots; test mobile 320px paragraph spacing and verify the old canvas script does not run.

## 3. Three outstanding owner decisions — conservative options

These are **release-policy decisions**, not failures the visual preview can resolve. None were implemented silently.

| Decision | Existing evidence | Conservative recommended option | Owner input needed |
| --- | --- | --- | --- |
| **Contact and enquiry processing** | `pages/enquiry.html` contains an external third-party `POST` form; Stage 8 report documents no verified privacy notice, recipient/processing arrangements and anti-spam protection disabled. The form was **not submitted**. | **Temporarily suspend third-party submission** and display a simple contact explanation/approved alternative, preserving the original URLs, until privacy notice and anti-spam settings have been reviewed. Do not collect new data during review. | Whether to temporarily suspend the form or approve a specific compliant form workflow |
| **Historic division / Founding Fellows search indexing** | Historical notices are in place, but seven old division/fellows URLs remain in `sitemap.xml`; `robots.txt` broadly allows crawling. | Preserve all existing URLs but remove these seven historic pages from the active sitemap and apply targeted `noindex` after owner approval. Keep the historical-context notices to avoid misleading existing visitors. | Whether to index an archive or mark old organisational pages noindex |
| **Original artwork and mathematical figures** | The four paper illustrations and original logo remain in preserved papers. There is no verified source/rights register or independent formula review; v2 programme UI uses CSS/SVG artwork rather than new third-party images. | Avoid new reuse or marketing claims; retain original articles without edits pending owner confirmation of provenance and figure content. If rights are unknown, resolve them before treating release as cleared. | Confirm authorship/source/permission and whether mathematical cover elements are accurate |

**External LinkedIn note:** HTTP 999 from automated read-only checking is compatible with access blocking; it is not evidence the owner's link is invalid. The supplied URL remains unchanged.

## 4. Ready-state assessment

- **Styling/source checks:** PASS on GitHub source for starfield removal and justified running text.
- **Representative browser spot-check:** PASS at 320 / 390 / 768 / 1440px, with the explicit limitation above.
- **Exact-branch post-change browser regression:** **NOT RUN / REQUIRED**.
- **Form privacy and anti-spam:** **BLOCKED ON OWNER DECISION**.
- **Historical indexing:** **BLOCKED ON OWNER DECISION**.
- **Artwork rights and figure accuracy:** **UNVERIFIED / OWNER INPUT REQUIRED**.
- **Merge/deploy:** **NOT AUTHORISED**; PR #5 must remain open and draft until a separate Stage 9 decision.

**Recommended sequence:** confirm the privacy/indexing and image-rights approach; apply approved reversible changes in the existing feature branch; execute the full exact-branch QA script and new screenshots; only then request final owner approval.
