# SymTech Ventures v2.0 — Phase 2 Full-Bleed Earthrise Exact-Branch QA Handover

**Date:** 17 November 2026 GMT  
**Status:** Ready for a bounded engineering QA pass. **NOT TESTED OR RELEASE-APPROVED.**  
**Implementation:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), branch `feature/v2-space-research-website`, visual implementation SHA `94717f44cb65691c39d4054547eb0543ed40eaed`, header-continuity refinement SHA `cb210cab8431596b1f9ec4ed2907fd4509be655e`.  
**Mode:** Codex, Luna Medium, Standard speed as owner-selected. Preserve all current owner-controlled settings.  
**Release:** **Do not merge or deploy.** Do not mark the PR ready for review automatically.

## Owner-approved visual direction

Owner prefers the **first cinematic Earthrise** composition spanning the entire homepage hero and navigation background, with a static starfield, no animated stars. Real accessible text and CTAs should overlay a dark left-safe area. The six nav link labels are enlarged to **16px desktop and ~14.4px intermediate width**, with mobile disclosure for <=919px. The previous two-column lunar art crop is rejected as the main presentation; the original inline orbital SVG remains in source as a rollback alternative.

## Actual code state

- `index.html`: only a homepage-scoped class `v2-earthrise` added; hero copy, nav links, academic status and existing SVG markup retained word-for-word.
- `css/v2-site.css`: appended scoped full-width backdrop, continuous header imagery, enlarged nav typography, mobile hero positioning, text contrast and breakpoints.
- `images/heroes/v2_earthrise_fullbleed.webp`: **257,542-byte**, 1672 × 941 WebP quality 80. AI-generated conceptual art; **source mock-up has baked typography on its left side**; current dark overlays must mask it completely without sacrificing real text contrast.
- `docs/reports/V2_PHASE_02_FULLBLEED_IMPLEMENTATION_20261117.md`: implementation provenance and QA pending.

**Already checked via GitHub source/tree (not full browser testing):** 6 desktop links, 6 mobile links, homepage content identical aside from class; 28 original paper figures present and unchanged; all source files retained; CSS brace count 207 opening/207 closing; new WebP exists and matches expected size; draft PR unmerged. A previous stand-alone HTML preview (not repository checkout) was rendered at 320/390/768/960/1440px without horizontal overflow. No Actions commit statuses were reported.

## Required real engineering verification

1. **Pin exact source HEAD** and check out the feature branch, recording SHA before/after. Verify WebP decodes and displays with no 404, and full-bleed image matches owner-approved first Earthrise visual; no duplicate embedded AI text is visible.
2. Run `python3 -u docs/reports/scripts/v2_stage8_qa.py` on the actual checkout, record command, exit code, total files/routes/papers and any failures. Do not reuse pre-Phase-2 exit-0 report as evidence for this commit.
3. In real Chromium/Playwright, screenshot homepage **320, 390, 768, 919, 920, 960, 1080, 1280, 1440px**, desktop and mobile, with at least one reduced-height mobile viewport; verify no overflow or clipped nav/buttons, background positioning, readable hero lead and caption, image not overlapping content below, navigation visible at all breakpoints.
4. Inspect **every primary desktop link** and all six mobile dropdown links with keyboard, pointer and focus-visible. On mobile, open/close disclosure using keyboard. Verify skip link, six-link counts, accessible semantics and links' actual destinations.
5. Check colour contrast and text over Earth/stars at 200% zoom, reduced-motion CSS, slow-image/failure fallback, performance/LCP/asset bytes, no site-wide animated starfield and no new horizontal scrolling.
6. Smoke-check Research, BridgePoint, Discussion Papers, Publications, About, Contact, NSRP and SEIP shells for header/nav fit after shared CSS change. Preserve 4 online original SYMMETRIA discussion paper bodies, seven figures each and all article URLs; no formal publications claimed.
7. If any actual layout or accessibility defect is found, make **minimal corrections only** to `index.html` and `css/v2-site.css` on the same feature branch, while keeping the approved visual direction and original SVG source. If the baked source-image lettering becomes visible, **do not declare acceptance**; correct the mask or request a clean image-only asset. Do not rewrite programme counts, publish lessons, modify paper figures or introduce unapproved menus.
8. Publish a factual `docs/reports/V2_PHASE_02_FULLBLEED_QA_20261117.md` with exact SHA, test commands/exits, viewport screenshot paths, objective issues/fixes, image provenance/byte budget and remaining release blockers.

## DTSU and handback

Use **DTSU v1.1**: genuine Europe/London clock, `[HH:MM:SS] NN% — factual progress; ETA ~N minutes` at 0%, 10–20% milestones and closure. Estimate ETA; adjust as new evidence appears. Finish with **COPY TO CHAT** containing branch, PR link, commit, verified QA, screenshot links, all known caveats, and the statement **“PR #5 is still draft, unmerged and undeployed.”**

**Do not merge, mark ready, deploy, change DNS or silently count preliminary previews as final QA.**
