# Stage 8C Pre-Release Assurance

**Date:** 16 November 2026 (Europe/London)
**PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)
**Branch:** `feature/v2-space-research-website`
**Code baseline reviewed:** `811405e6e5a36e1501bd046b2e3c0735bd3d2ce7`
**Assessment:** **Pass with owner blockers; not release-ready.**

## Findings and work completed

- **High — owner asset decisions outstanding.** The companion [asset provenance register](V2_STAGE_08C_ASSET_PROVENANCE_REGISTER.md) inventories 52 locally referenced raster files. No creator, source, licence or attribution record substantiating public redistribution was found in the inspected repository material. All rights remain owner-confirmation-required. Original paper images also contain embedded mathematical notation and factual assertions requiring review. No scientific accuracy or copyright clearance is claimed.
- **High — approved homepage image missing.** The handover's approved 716×494 Earthrise PNG/WebP is absent. The homepage therefore retains its existing inline orbit art; no replacement was invented. The approved image must be supplied before the raster-hero change can be completed.
- **Moderate — automated accessibility audit not run.** No axe-core or equivalent audit package is installed in the available environment; no claim of automated WCAG conformance is made. This is a verification limitation, not a pass. Manual/scripted keyboard and structural checks below did run. Full screen-reader review and WCAG certification remain outstanding.
- **Low — regression script stale checks fixed.** At baseline the QA script expected old Contact copy (“View Enquiry Status”) and a legacy-only skip-link class. Updated those assertions to the current Contact link and either of the two existing skip-link shell classes, retaining focus visibility requirements. These were test expectation mismatches; no website markup was changed for them.

## Verification

Command: `python3 docs/reports/scripts/v2_stage8_qa.py` from the actual feature checkout at baseline `811405e`. Exit code **0** after the two narrow test updates. It checked 36 HTML files, local references and fragments, image alt presence, CSS resources, sitemap (16 locations), robots response, historic noindex policy, suspended enquiry and legacy confirmation, six-link v2 navigation, all four paper main blocks and seven figure references per paper, catalogue counts, reduced motion, keyboard skip/menu flow, responsive overflow, console errors and failed local responses. Result: no broken local references, missing alt attributes, CSS reference failures, browser errors or failed local HTTP responses. Screenshots were captured at 390/1440 for Contact and Papers 1–4; the script also spot-checked 320/768 layouts. CNAME hash assertion passed.

Paper bodies and figures matched the script's documented `origin/main` normalization check. Contact and Enquiry were navigated read-only; no form submission or external communication occurred. Four paper routes and all seven historical noindex URLs remained intact. Discussion Series: four available and twelve planned; BridgePoint: sixteen planned; NSRP and SEIP: five projects / twenty phases each; Publications: zero records.

### Fresh screenshots

- Contact: `docs/reports/screenshots/postapproval-pages-contact-{390,1440}.png`
- Papers 1–4: `docs/reports/screenshots/postapproval-articles-symmetria-symmetria-paper-0[1-4]-{390,1440}.png`
- Existing home evidence from Stage 8B remains `postapproval-home-{390,1440}.png`; it does not demonstrate the missing raster hero.
- Historic/context, Enquiry, About, Discussion Series and Publications captures are also in `docs/reports/screenshots/postapproval-*.png`.

## SEO/share and performance review

The regression confirms a 16-entry sitemap, four retained paper URLs, seven historical pages excluded with `noindex,follow`, and crawlable `robots.txt`. Existing v2 canonical/title/description checks passed. Share-media rights could not be substantiated, so no `og:image` was introduced. A full card-by-card metadata/social preview audit was not independently run. Performance review was limited to resource requests observed during browser runs; no Lighthouse, Web Vitals, bandwidth or load-time measurement was performed.

## Release decision

Before Stage 9, the owner must provide the approved Earthrise binary and resolve image provenance/redistribution/attribution; review scientific statements and mathematics embedded in the paper figures; and decide whether to require an automated accessibility scan and screen-reader review. Enquiry submissions remain paused. This report does not authorize release. PR #5 remains draft; no merge, deployment, DNS change, external enquiry or lesson writing occurred.
