# Phase 2 — Homepage and SYMMETRIA papers at 100% desktop browser zoom

**Date:** 18 November 2026 GMT  
**Owner request:** At 100% browser zoom, the homepage required 125% zoom and SYMMETRIA discussion papers 150% zoom to appear to fill the desktop screen. Preserve the sticky header and portrait mobile behaviour.  
**Scope:** CSS presentation only, plus hardening the draft-only GitHub Action; no research text, images or scientific claim modified.  
**Branch:** `feature/v2-space-research-website` / [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Exact tested source SHA:** `f0b80791166ba6fa872903f2da9f6ec4ad3a0393`  
**Final GitHub Actions run:** [#44329472724](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44329472724), **all steps SUCCESS**.

## Root causes

- The global desktop `.container` was constrained by `--max:1480px` for wide screens; at 2560px that left 540px margins on both sides.
- Each original SYMMETRIA article had its own `.article-body>.wrap` limited to **940px**; increased browser zoom made it proportionally larger in the viewport but did not correct the layout.
- Article figures had `max-width:100%` but no explicit `width`; they displayed at their intrinsic 1536px or smaller dimensions rather than filling the new article container.

## Corrective implementation

- At desktop widths **>=1200px**, the shared content container scales to **94vw**, including homepage header, hero and programme cards. The homepage hero-copy maximum width and headings/card copy scale proportionally while retaining the existing full-bleed Earthrise.
- At the same breakpoint, available SYMMETRIA article, next-paper and parent panel wraps use **94vw** with no 940px cap. Prose type scales in a bounded clamp while its text and mathematical images remain unedited.
- All paper illustrations across **Papers 1–4** now use `width:100%;max-width:100%;height:auto`; the rule applies to all paper `img` elements, not only Paper 2's optional `.article-image` class. Original **28 WebP files** are unchanged.
- At 320/390px mobile widths, these new desktop-only rules do not apply. Existing sticky header and responsive menu remain unchanged.

## Measured exact-branch browser evidence

GitHub Action uses Playwright Chromium at **100% zoom** (`device_scale_factor=1`), measuring `getBoundingClientRect()` of live DOM elements and scroll widths. It checked **30 page/viewport cases** (Homepage + four available papers at 1366×768, 1440×900, 1920×1080, 2560×1440, 390×844 and 320×720), with these representative measured widths:

| Viewport | Main container | Paper container | First paper image | Horizontal overflow |
|---|---:|---:|---:|---|
| 1366px | 1284px (94%) | 1284px | 1284px | None |
| 1440px | 1354px (94%) | 1354px | 1354px | None |
| 1920px | 1805px (94%) | 1805px | 1805px | None |
| 2560px | 2406px (94%) | 2406px | 2406px | None |
| 390px mobile | 356px | 358px | 358px | None |

The test explicitly asserts **>=92.5% width** for desktop containers and **>=92% of paper width for each paper's first illustration**, with no overflow. Confirmed `position:sticky` header at the top in each route. The previous Phase 2 whole-site regression, nine-breakpoint navigation test, 20 emblem/arrow cases and 35 sticky-header scenarios all passed in the same run.

### Earlier interim QA attempts

- [Run #44326124477](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44326124477) succeeded for the enlarged containers before artwork itself was scaled; that was **not** sufficient to satisfy the owner's image-specific requirement.
- [Run #44327554083](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44327554083) correctly failed the new illustration-width assertion on Paper 1, revealing that only Paper 2 used the `.article-image` class.
- Final run #44329472724 passes after changing the figure style and test to target all four papers' `.paper-content img`.

## Review deliverables

Final Action artifact `symtech-phase2-review-f0b80791166ba6fa872903f2da9f6ec4ad3a0393` contains: screenshots of homepage and Paper 2 at **1920×1080, 2560×1440 and 390×844**, the 30-case `desktop-width-at-100percent.json` test evidence, logs, and the complete offline website ZIP. The owner's Chat copy of the website ZIP was checked against the **exact final CSS Git blob SHA** and its 108 files passed ZIP CRC validation.

**Limits:** The tests confirm 100%-zoom viewport fill and no scroll overflow on tested devices; they cannot independently verify the owner's particular monitor, Windows scaling, browser chrome, or personal aesthetic preference. No promise that a website can set the physical monitor aspect ratio.

## Safeguards / release boundary

**Phase 2 visual correction completed and tested.** The full-bleed Earthrise, selected brand emblem, six-link navigation, 4 available paper bodies and 28 original paper figures remain intact. No Phase 3 repairs or scientific content changes. **Draft PR #5 is still unmerged and unpublished; do not deploy without separate owner approval.**
