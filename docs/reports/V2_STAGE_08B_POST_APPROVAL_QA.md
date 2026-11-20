# SymTech Ventures v2.0 — Stage 8B Post-Approval Regression

**Date:** 16 November 2026 (UTC)
**Branch:** `feature/v2-space-research-website`
**Draft PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)
**Regression base:** `a533470a3af496ad25411335b498acda5ea0cd96`
**Result:** PASS after one narrow, screenshot-confirmed homepage fix.

## Run and evidence

Ran from the feature branch checkout with system Chromium and Playwright:

```sh
python3 docs/reports/scripts/v2_stage8_qa.py
```

Exit status **0**. The script tested the homepage, all eight other v2 pages, one original SYMMETRIA paper, all seven historic pages, Contact, Enquiry, the old confirmation URL and all four original papers. Responsive widths were **320, 390, 768 and 1440 px**. There were **no browser console/page errors, failed local HTTP responses, broken local links/fragments, missing image alt attributes, missing CSS resources or horizontal overflow failures**.

The Enquiry route was navigated read-only. It contains no form, input, textarea, submit button or POST handler, says submissions are paused, and links back to Contact. No data was submitted. The old confirmation route says opening it does not mean a message was sent.

The seven historical pages returned HTTP 200, each retained its historical-context notice and exactly one `noindex,follow`; none appears in the **16-location** sitemap. `robots.txt` remains crawlable. The sitemap retains all four original paper URLs. The site has no canvas/starfield on tested routes; the v2 hero has no pseudo-element background. Homepage prose remains justified, with heading/navigation/control alignment retained. Keyboard checks confirmed the visible skip link, menu tab order, Escape close and focus restoration.

Catalogue checks passed: Discussion Series 4 categories / 4 linked papers / 12 planned titles; BridgePoint 4 categories / 16 lessons planned / no lesson links; NSRP 5 projects / 20 phases / provisional status; SEIP 5 projects / 20 phases; Publications zero records. All four paper body/figure hashes matched the recorded `main` baseline after normalization for the previously approved skip-link and `main` wrapper only. `CNAME` remained intact.

## Narrow adjustment

Visual inspection of the first fresh homepage capture showed unsupported arrow characters rendered as empty boxes in Chromium. Replaced only the homepage's decorative arrows with ASCII `>` marks. Added a direct Enquiry screenshot and an assertion for its Back to Contact link to the regression script. The full script passed again and the refreshed captures show the corrected homepage and status page. No lesson or research content was developed.

## Fresh Chromium screenshots

- Homepage: [desktop, 1440 px](screenshots/postapproval-home-1440.png), [mobile, 390 px](screenshots/postapproval-home-390.png)
- Original Paper 1: [desktop, 1440 px](screenshots/postapproval-articles-symmetria-symmetria-paper-01-1440.png), [mobile, 390 px](screenshots/postapproval-articles-symmetria-symmetria-paper-01-390.png)
- Enquiry status: [desktop, 1440 px](screenshots/postapproval-enquiry-1440.png)
- Historic notice: [Founding Fellows, desktop](screenshots/postapproval-legacy-fellows-1440.png), [mobile](screenshots/postapproval-legacy-fellows-390.png)
- Other v2 captures: [About 1440](screenshots/postapproval-pages-about-1440.png), [About 390](screenshots/postapproval-pages-about-390.png), [Discussion Series 1440](screenshots/postapproval-pages-discussion-series-1440.png), [Discussion Series 390](screenshots/postapproval-pages-discussion-series-390.png), [Publications 1440](screenshots/postapproval-pages-publications-1440.png), [Publications 390](screenshots/postapproval-pages-publications-390.png)

The browser run also covered Research, SYMMETRIA, NSRP, SEIP and BridgePoint at all four widths; screenshots were limited to the requested representative routes.

## Release boundary

The website remains **not release-ready** pending owner clearance of original image and figure provenance. This QA does not certify image rights or research mathematics. Third-party form-provider direct traffic is outside the website change. PR #5 remains a draft; no merge, deployment or external enquiry submission was performed.
