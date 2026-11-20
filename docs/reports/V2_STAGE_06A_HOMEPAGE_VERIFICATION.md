# SymTech Ventures v2.0 — Stage 6A Homepage Verification

**Date:** 16 November 2026 (GMT)
**Branch:** `feature/v2-space-research-website`
**Base:** `main` at `248feb5084745ebcffca5957ca5c517baa8ba7e0`
**Scope:** Homepage shell only. No Stage 6B pages, merge or deployment.

## Implementation

Adapted the approved Stage 4 homepage prototype into the production root page. Added `css/v2-site.css` for the visual shell, responsive layout, focus styling and restrained decorative CSS starfield. The homepage presents the independent space-focused project, four programme cards, four online discussion essays, an empty formal Publications state and the supplied LinkedIn profile. No external or unverified image assets were introduced.

The primary navigation contains all six required labels. Home and Discussion Papers resolve to the homepage and existing discussion-series route. Research, BridgePoint, Publications and About are explicitly labelled as Stage 6B destinations and intentionally remain pending. Contact remains available in the footer. The contact/enquiry pages, deployment configuration, legacy pages, article files and paper images were not changed.

## Verification performed

Command: `python3 /tmp/check_home.py` using Python Playwright with system Chromium against `python3 -m http.server 8765 --bind 127.0.0.1`.

- **PASS:** Homepage renders at 1440px desktop, 390px and 320px mobile.
- **PASS:** No horizontal overflow at 390px or 320px (scroll width equals client width).
- **PASS:** One H1, six primary navigation links, skip link receives first keyboard focus, and the mobile `<details>` menu opens.
- **PASS:** No page errors or console errors after adding a data favicon to avoid a missing-favicon request.
- **PASS:** Four article links point to the existing `/articles/symmetria/symmetria-paper-01.html` through `-04.html` routes.
- **PASS:** Existing article HTML blob hashes match the pre-change baseline:
  - Paper 1 `390a8676189542fc9044c1dabbbf344ad10e69f6`
  - Paper 2 `ec70f57a24f160e5971bad5fa4567529ef54bb79`
  - Paper 3 `90385bd2da97c75d0da3ebe17355753e762599ee`
  - Paper 4 `702e47f1883335c4a4202d71e10ad8da431a9d87`
- **PASS:** `CNAME`, contact/enquiry pages and all four article files have no diff.
- **PASS:** `prefers-reduced-motion` disables scrolling animation and card transitions; starfield is static CSS decoration, pointer-inert and absent from the accessibility tree.
- **PASS:** No formal publication records were added.
- **PENDING / Stage 6B:** Research, BridgePoint, Publications and About destinations. Discussion Papers continues to point to the existing legacy route pending v2 integration.

## Screenshots

- `docs/reports/screenshots/v2-home-desktop.png` — 1440px viewport.
- `docs/reports/screenshots/v2-home-390px.png` — smartphone viewport.
- `docs/reports/screenshots/v2-home-320px.png` — narrow viewport.

These are local Chromium captures from the current implementation, not deployed previews.
