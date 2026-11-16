# SymTech Ventures v2.0 — Contact and Discussion Paper Visual Consistency

**16 November 2026 — Source-level handoff (Chat)**

**Status:** Code changes committed to [existing draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5). **NOT browser-tested on the latest branch yet.** Homepage raster upload is still pending. No merge or deployment.

## Owner's visual direction

A clean, grounded, professional **independent space-research** identity rather than v1.0 spectacle. Retain midnight-blue palette, restrained blue/gold accents, clear navigation, and **fully justified running paragraphs**. No decorative starfield. Prefer a few relevant, traceably sourced images to an elaborate collage.

## Completed code changes

### Contact — `pages/contact.html`

- Rebuilt entirely in the shared v2 layout from About's current shell.
- Uses `css/v2-site.css` and `css/v2-programmes.css`, **not** `css/styles.css`; same six-link primary navigation, responsive menu, footer and research-focused content cards.
- Includes a clear paused-enquiry notice and link to the retained Enquiry status page. There is **no `<form>`** and no third-party submission handler.
- Links to research programmes, discussion papers and the owner's existing public LinkedIn profile.
- Current enquiry privacy/anti-spam review remains a prerequisite **before any future reactivation**, not a blocker to shipping the intentionally paused static information page.

### Four SYMMETRIA discussion papers

- `articles/symmetria/symmetria-paper-01.html` to `symmetria-paper-04.html` now contain the **same six primary links** and v2 header/footer as the new pages.
- Dedicated `css/v2-articles.css` overrides the old presentation while retaining legible reading widths, justified body/figure captions, scrollable tables, images and a no-star dark background.
- The original legacy AETHEROS header/icon navigation and associated six decorative navigation images were replaced in the page shell; **the original seven per-paper science illustrations remain**.
- Chat independently compared each **entire `<main id="main-content">...</main>` block** to the immediately preceding tested branch commit `4dc5c4252ae0a3fc59ec9caf3bc64c67ba7e003c`; all four blocks were **byte-for-byte identical**. Every research paragraph, image `src`, caption, heading, page-internal parent link, and paper URL within the content is unchanged.
- **Scientific accuracy and illustration rights are not validated** by cosmetic shell changes. The previously recorded Paper 2/3 figure concerns remain for future content review.

### Regression script

`docs/reports/scripts/v2_stage8_qa.py` now expects Contact in the v2 shell and compares the four article `<main>` blocks/7 image sources with the original `main` branch, rather than requiring a byte-identical whole HTML file. It includes all four articles and Contact in the principal desktop/mobile checks and requests new screenshots at 390/1440px.

**These new checks were authored and read back from GitHub, not yet run through Python/Playwright in Codex's actual checkout.** The prior Stage 8B success was for the earlier design.

## Earth-at-sunrise homepage visual — asset prepared, NOT integrated

The current root `index.html` still embeds an inline SVG orbit graphic. The owner wants a real **raster** image.

- The Chat session prepared a self-contained **716 × 494 PNG** master (510,550 bytes) and a **WebP at quality 80** (48,340 bytes) from the approved Earthrise visual.
- WebP SHA-256: `b80e474a511d927e3ca3bea5f4bd3ab8795c394014353592ae5a15d13f4330f0`.
- It is AI-generated conceptual artwork, **not an authentic NASA mission photograph**. Neither the approved PNG nor WebP is currently committed to GitHub.
- Added `tools/prepare_homepage_webp.py` to reproduce the quality-80 conversion once the PNG is in an implementation checkout.
- **Do not change the homepage to a missing `img` path.** After the approved binary is provided/uploaded, swap the orbit SVG for a responsive `images/heroes/earthrise_hero_q80.webp` and recheck the visual layout. Use accurate alt/credit wording.

## Release gates and next action

The bounded [Stage 8C implementation/visual QA brief](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/handovers/V2_STAGE_08C_CODEX_VISUAL_INTEGRATION.md) requests: approved binary upload, homepage image replacement, Chromium 320/390/768/1440px testing and fresh screenshots of Contact, all four papers and homepage.

Keep PR #5 **open, draft, unmerged, undeployed**. Do not claim full QA PASS or asset-rights/math clearance until independently verified.
