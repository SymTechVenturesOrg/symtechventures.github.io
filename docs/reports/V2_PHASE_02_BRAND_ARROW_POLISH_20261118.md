# Phase 2 — Brand emblem and programme-card arrow polish

**Date:** 18 November 2026 (GMT)  
**Branch:** `feature/v2-space-research-website` / [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Status:** Owner-selected artwork and arrow treatment implemented; exact-branch CI result must be checked before claiming QA completion.

## Owner decision and scope

The owner chose the **third original brand concept**, combining an **S monogram, Earthrise horizon and circular cyan edge**, and requested uniform navigational arrows in the four homepage programme cards. The previously approved full-width Earthrise design and the restrained image count are preserved. No further programme illustrations were commissioned.

## Specific changes

- Added `images/logos/symtech_earthrise_emblem.webp`: 512×512 transparent WebP (29,154 bytes), derived by cropping the owner's selected OpenAI-generated concept illustration `symtech_ventures_space_tech_banner.png` (2172×724) to the Earthrise-S circle. This is **conceptual synthetic brand art**, not evidence of a space mission. Source crop: (121,139)–(531,549), resized to 512×512 and given a soft circular alpha mask; WebP encoder quality 88.
- In `css/v2-site.css`, the existing `.brand-emblem` shows this badge across shared page headers, without removing the accessible linked brand name. Existing desktop and mobile badge dimensions remain.
- The four homepage programme links now all use the single navigational **right arrow (→)**. The BridgePoint **See pathway** link opens another page, so a down arrow had been misleading. CTA link and arrow remain together using `white-space:nowrap`, and the footer grid allows metadata to wrap independently.
- Added an explicit five-breakpoint, four-route badge/link test to the draft-only GitHub QA workflow. The existing full site regression is retained.

## Safeguards / acceptance

No research paper body, published claim, Phase 3 figure, homepage Earthrise background, navigation destination, release route or production site has been changed. The full existing `v2_stage8_qa.py` must pass against the new commit, together with the new dedicated emblem-and-arrow browser check. Draft PR #5 stays unmerged and no deployment is authorised.

## Final QA and legacy-style correction — 18 November 2026 GMT

**Exact tested source commit:** `4399072d6bd82b981d5f948f482207cc196c123c`. **GitHub Actions run:** [#44316872279](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44316872279), **conclusion: success** (all steps). The following was observed rather than assumed:

- Original combined `v2_stage8_qa.py` exact-branch regression: **success**, 36 HTML files; no local-link, CSS-reference or alt-text failures; modern paper text/figure integrity gate retained.
- Nine-width Earthrise/navigation check at 320, 390, 768, 919, 920, 960, 1080, 1280 and 1440px: **success**.
- New dedicated badge/card browser check: **20 passes** (4 routes × 5 widths: 320, 390, 768, 920, 1440); logo CSS visible and loaded at >=30px, fallback letter has computed 0px font size, all four homepage cards use `→` without overflow.
- GitHub Actions generated `symtech-phase2-review-4399072d6bd82b981d5f948f482207cc196c123c`: screenshots, raw full regression logs, breakpoint results and a **complete-site ZIP**. Archive was downloaded and verified without ZIP errors. Desktop 1440px and mobile 390px screenshots visually show the chosen Earthrise emblem and intended full-bleed art.

**Important QA corrections discovered and resolved:**

1. Earlier run [#44313643892](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44313643892) was green **incorrectly**: a pipeline using `python ... | tee` hid a case-sensitive text assertion error. All three piped browser-test commands now use `set -euo pipefail`, and the arrow check compares underlying text rather than the uppercased `innerText`. The newer workflow correctly detects failures.
2. Corrected workflow [#44315532168](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44315532168) then exposed an **actual legacy stylesheet collision**: `css/styles.css` used `display:none!important` on the modern SYMMETRIA article `header.site-header`, making the new badge 0×0 on paper pages. `css/v2-articles.css` now restores the modern header and clears the old small-screen body top-padding. A follow-up run [#44316431301](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44316431301) succeeded.
3. Hardened `css/v2-site.css` badge selector to `.site-header .brand .brand-emblem`, preventing the old `.brand span` font styling from making a fallback “S” visible over the selected image; extended CI to assert computed font-size is 0px. Final run #44316872279 succeeded.

**Design scope:** the chosen third Earthrise-S badge, four uniform programme-card right arrows, original full-width hero and restrained image count. No Phase 3 figure edits. The actual website is still not released, no PR merge, no DNS changes. Draft PR #5 remains unmerged; the user has not yet expressly authorised publication.
