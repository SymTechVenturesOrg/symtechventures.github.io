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
