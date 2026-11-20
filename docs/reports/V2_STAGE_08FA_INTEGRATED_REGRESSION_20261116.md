# Stage 8F-A Integrated Regression

**Branch:** `feature/v2-space-research-website`
**PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)
**Starting SHA:** `b8107c2f8a907b628b18df599db23553fc2c4fa8`
**Result:** PASS

The prior execution session did not survive environment restart: process inspection found no running `v2_stage8_qa.py`, and its session ID returned `Unknown process id 42226`. Its exit status was therefore unavailable. I reran the command rather than infer its result.

```text
python3 -u docs/reports/scripts/v2_stage8_qa.py
Exit code: 0
```

Environment: Python Playwright with system Chromium, headless. The script checked 36 HTML files and visited ten main pages, all four papers, seven historical pages, Enquiry and the former confirmation page, plus sitemap/robots. Viewports: 320, 390, 768 and 1440 px. It reported no broken local references, missing alt attributes, CSS-reference failures, browser errors or failed local responses; sitemap count 16. All four paper main blocks and seven figures each matched the trusted `origin/main` comparison. Programme counts passed (Discussion 4 online / 12 planned; BridgePoint 16 planned; NSRP and SEIP 20 phases each; formal Publications zero).

Stage 8D checks: ten-page metadata source audit remains documented in `V2_STAGE_08D_SOCIAL_METADATA_SOURCE_QA_20261116.md`; regression passed the existing canonical/title/description checks and found no browser failures. Stage 8E checks: source reports desktop current-page navigation, mobile Open/Close label, Escape/focus restoration and outside-tap behavior. This integrated script verified six-link navigation, responsive layouts and menu keyboard behavior. A separate real-browser manual spot check of all four specific Stage 8D/8E interactions was not conducted in this recovery run.

Fresh screenshots are the script-generated `postapproval-home-{390,1440}.png`, `postapproval-pages-contact-{390,1440}.png` and `postapproval-articles-symmetria-symmetria-paper-01-{390,1440}.png` under `docs/reports/screenshots/`. No website defect was found. No source or test assertions were changed. Automated axe accessibility testing belongs to Stage 8F-B and was not run here; no WCAG compliance claim is made. The missing approved Earthrise image and asset/figure owner decisions remain separate release gates.

PR #5 remains draft and unmerged. No deployment, enquiry submission or lesson writing occurred.
