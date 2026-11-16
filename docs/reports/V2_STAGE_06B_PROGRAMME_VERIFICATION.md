# SymTech Ventures v2.0 — Stage 6B Programme Verification

**Date:** 16 November 2026 (GMT)
**Branch:** `feature/v2-space-research-website`
**Base:** `main` at `248feb5084745ebcffca5957ca5c517baa8ba7e0`
**Scope:** Research, SYMMETRIA, NSRP, SEIP and BridgePoint pages. No merge or deployment.

## Implemented pages

- `/pages/research.html` explains the space-exploration focus, programme relationships, feedback and the difference between research questions, mathematical formulation, simulation and measurement.
- `/pages/symmetria.html` replaces the legacy page with the shared v2 shell, exploratory-status wording and links to the four original discussion essays.
- `/pages/nsrp.html` presents five named projects and 20 planned phases. The NCP phase labels are explicitly provisional.
- `/pages/seip.html` presents five companion projects and 20 planned phases, with explicit limits on what simulations establish.
- `/pages/bridgepoint.html` presents four lesson categories and 16 canonical lesson titles/outcomes, all marked Planned; there are no lesson links.

All pages use the shared styles, semantic headings, skip link, keyboard-operable native mobile menu, consistent footer and LinkedIn link. Homepage navigation now links to the implemented Research and BridgePoint pages; programme cards link to the appropriate pages. Publications and About remain marked Stage 6C. Contact and Discussion Papers legacy routes remain available.

## Commands and outcomes

- `python3 -m http.server 8765 --bind 127.0.0.1` — served local branch for browser checks.
- `python3 /tmp/check_6b.py` — **PASS**; Playwright with system Chromium visited all five pages, checked HTTP 200, one H1, six navigation links, skip-link keyboard focus, mobile menu open/close, 1440px screenshots, 390px layout, zero console/page errors, and rendered catalogue DOM counts.
- Additional Playwright viewport check — **PASS**; all five routes have no horizontal overflow at 320px.
- Rendered catalogue counts — **PASS:** BridgePoint 4 categories / 16 lessons; NSRP 5 projects / 20 phases; SEIP 5 projects / 20 phases.
- Original paper HTML hashes — **PASS, unchanged:**
  - Paper 1 `390a8676189542fc9044c1dabbbf344ad10e69f6`
  - Paper 2 `ec70f57a24f160e5971bad5fa4567529ef54bb79`
  - Paper 3 `90385bd2da97c75d0da3ebe17355753e762599ee`
  - Paper 4 `702e47f1883335c4a4202d71e10ad8da431a9d87`
- No formal Publications page or entries were added; that destination remains pending Stage 6C.
- **Not claimed:** full accessibility audit, comprehensive legacy regression, sitemap integration, scientific validation or publication readiness.

## Screenshots

Captured from actual local Chromium renders with the mobile menu closed by default:

- Research: `docs/reports/screenshots/v2-research-desktop.png`, `v2-research-mobile.png`
- SYMMETRIA: `docs/reports/screenshots/v2-symmetria-desktop.png`
- NSRP: `docs/reports/screenshots/v2-nsrp-desktop.png`, `v2-nsrp-mobile.png`
- SEIP: `docs/reports/screenshots/v2-seip-desktop.png`, `v2-seip-mobile.png`
- BridgePoint: `docs/reports/screenshots/v2-bridgepoint-desktop.png`, `v2-bridgepoint-mobile.png`

Desktop viewports are 1440px and mobile viewports are 390px wide. Additional 320px checks passed on all five pages.

## Pending Stage 6C

Research, SYMMETRIA, NSRP, SEIP and BridgePoint are implemented. About and formal Publications remain pending. Sitemap integration and broader legacy navigation cleanup are also deferred per the Stage 6B handover. The existing Discussion Papers route and four article pages were left unchanged.
