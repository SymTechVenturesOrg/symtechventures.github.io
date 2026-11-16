# SymTech Ventures v2.0 — Approved Contact and Historical Indexing Controls

**Date:** 16 November 2026 (GMT)  
**Approval:** Owner approved (a) retaining seven historical URLs with `noindex` and removal from the sitemap, and (b) temporarily suspending the third-party enquiry form pending privacy/anti-spam review.  
**Implementation:** [Unmerged draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), branch `feature/v2-space-research-website`. **The public website on `main` is unchanged.**

## Implemented and verified from GitHub source

### Historic project pages — preserve URLs, discourage search indexing

Added exactly one `<meta name="robots" content="noindex,follow">` inside `<head>` of each:

| Historical page | Previous Stage 8 blob | Current blob |
| --- | --- | --- |
| `pages/divisions.html` | `dd38e7458ae0b1ac836a02dccfa20c9f9ba7491d` | `639066c8a0040a413e09c3f31be478aa6f30fdea` |
| `pages/founding-fellows.html` | `9193b811d6502f93a8c39b5d5b06bcf975db9458` | `875828009ba45d03b029a4503864d950ab652362` |
| `pages/symcore.html` | `bbf88dd1001f82adf551b31342d69ab4541c4fed` | `dfb7e4bdc76713002148d8c33944387386138cc9` |
| `pages/symcraft.html` | `a544de8f5f68de6b02245fc14e225afc4956fe4a` | `3a528ae91c394f2aa7a3da90ed8622d03ab7eb96` |
| `pages/symcura.html` | `eaa274e95d41c923c0d07456140399017873c498` | `eb26e2bcbf3c8485b67c09f08bb6dd2ac51a0182` |
| `pages/symlogic.html` | `9fc23ec623e188f75ce84b7164e6e8aedb4e7596` | `f2f720fb56b40d14de2184abb67b7ad581f71bc7` |
| `pages/symspace.html` | `9cef67e2faba0ee94f4a804634a0190f7b1377e8` | `a980c3c5621f63949f1af7f5baac0531c4950f16` |

**Independently verified by reading both revisions:** removing the new `noindex` line from each new HTML file reproduces **exactly** the earlier Stage 8 content. Thus the seven legacy page bodies, historical notices and URLs remain unchanged.

**Sitemap:** removed precisely those seven URLs from `sitemap.xml`: **23 → 16 unique `<loc>` entries**, keeping the homepage, current research/BridgePoint/Discussion Pages, Contact/Enquiry URLs and **all four original paper links**.

**Crawler rule:** `robots.txt` remains `Allow: /` so search engines can crawl and read the `noindex` instruction. `noindex` is an indexing directive, **not** an immediate search-result deletion guarantee. No redirects or deleted pages were introduced.

### Suspend enquiry collection on website

- `pages/enquiry.html`: **removed the entire HTML `<form>`**, its action/third-party recipient, hidden fields, CAPTCHA flag and input controls; replaced with a clear temporary-unavailability notice and a link back to Contact. New blob `4a7d2e5d1c3316976c3e91dcdd5e1a1eed5ed181`.
- `pages/contact.html`: changed copy to reflect independent research rather than the old five commercial divisions and clearly explain that online enquiries are paused; links to the Enquiry status page. New blob `21225873b3c2c3fa148b685c93950f65647e1583`.
- `pages/enquiry-thanks.html`: retained this old URL (already `noindex,follow`), but replaced potentially misleading "message sent" wording with a notice that viewing the page **does not confirm a submission**. New blob `99e6cd998ba11fdbf7b02540367f8778876aa123`.
- No external submission was made, no private data sent and no new contact channel/service was installed.

**Scope qualification:** This removes collection **through the website after deployment**. It does **not** disable the third-party provider's old endpoint, which may still accept direct traffic, nor does it affect the original live website until the owner authorises a merge and deployment. A future compliant form would require its own privacy, retention, spam and endpoint review.

### Paper, domain and design safety

- All four original SYMMETRIA paper **substantive bodies and illustrations remain byte-for-byte identical to `main` once the pre-existing Stage 8 skip-link and `main` landmark wrapper additions are removed**. These files were not edited in this task.
- `CNAME` unchanged; new site's starfield remains removed and prose justification retained.
- The original Rights/figure-review release question is **still open**.

## Regression script updated, but full browser rerun still pending

[Updated Stage 8 QA script](../reports/scripts/v2_stage8_qa.py) now expects 16 sitemap URLs, checks seven historic `noindex` tags and preserved historic notices, verifies removal of the enquiry form/third-party handler, checks the confirmation-page disclaimer, verifies no canvas on pages and checks fully justified text. Its browser screenshot filenames now have a `postapproval-` prefix, preserving the old Stage 8 screenshots.

**Source-level verification executed successfully** using connected GitHub reads:
- Seven `noindex` tags unique and correctly located, original content otherwise unchanged.
- Seven absent from 16-entry sitemap; four paper URLs retained.
- Enquiry form/action entirely absent; Contact points to enquiry status; thanks page no longer asserts a submission.
- All four paper bodies and illustrations normalise exactly to the original `main` versions.
- The feature PR remains open, draft and unmerged.

**Not executed in this Chat session:** the full Python/Playwright script and fresh exact-branch desktop/mobile Chromium screenshots. Although Chromium is available locally, this execution environment cannot resolve GitHub to fetch a complete working checkout, so an isolated browser run would not represent the real PR. Do not treat the previous Stage 8 report or local earlier-prototype screenshots as new PR regression evidence.

## Remaining release gates

1. **Run exact-branch QA** on the current feature checkout: `python3 docs/reports/scripts/v2_stage8_qa.py`. Check 320/390/768/1440px, the Contact/Enquiry status flow, seven historic `noindex` tags, the actual absence of starfield canvases, and the four original article bodies.
2. **Inspect fresh `postapproval-` screenshots** for justified text and readability; confirm no new overflow or console failures.
3. **Owner clearance of original image and mathematics figure rights/accuracy** remains pending. No such clearance is asserted by the HTML changes.
4. **Form service follow-up:** before re-enabling submissions, establish appropriate privacy notice, processing conditions, retention, anti-spam and actual recipient verification.
5. **Stage 9 approval:** only the owner can authorise merging/releasing PR #5. This task did not authorise it.

**Current release verdict:** **Not yet release-ready** until exact-branch regression and image/figure clearance. The approved interim privacy and indexing changes are committed on the development branch.
