# Phase 2 — Full-width Earthrise draft implementation

**Date:** 17 November 2026 (GMT)
**Status:** Implemented on draft feature branch; full exact-branch browser/regression checks **PENDING**. No merge, publication or release authorisation.
**Source:** Owner-selected first cinematic Earthrise, larger six-link typography approved in Chat. See planning [hero handover](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/planning/space-first-research-website-20261116/docs/handovers/V2_PHASE_02_EARTHRISE_OWNER_REVIEW_AND_INTEGRATION_HANDOVER_20261117.md).

## Changed files

- `images/heroes/v2_earthrise_fullbleed.webp`: OpenAI-generated first Earthrise website composition, converted to WebP quality setting 80 (1672 × 941 px; 257,542 bytes). Synthetic/conceptual scene, not a real mission photo. **Contains baked image-origin typography on its left side; the live DOM hero CSS masks that region**, which must be inspected at every viewport and zoom level. A later clean image-only asset would be preferable.
- `css/v2-site.css`: enlarged six-link navigation, mobile-menu threshold for narrower widths, full-width hero background with accessible live HTML copy over a dark text-safe overlay, mobile caption contrast.
- `index.html`: homepage-only `v2-earthrise` class enabling scoped hero treatment. All existing page content, links, approved science caveats, programmes, papers and inline orbital SVG kept for rollback. The SVG is hidden solely in the new visual treatment, not deleted.

## Current evidence and release requirements

Prior **standalone local** proof had no horizontal overflow at 320/390/768/1440px; it was not the real site. Binary asset provenance and byte count were checked before creating a GitHub blob. **Do not claim feature-branch screenshot testing, keyboard/accessibility success, performance acceptance or Python regression exit 0 yet.**

After this GitHub commit: inspect full actual checkout of the exact commit at 320, 390, 768, 920, 960, 1080, 1280, 1440px, including responsive nav, real mobile disclosure, image source request, all six links, skip link, focus order, text contrast, visual clipping, no baked text reveal, zoom and reduced-motion. Run `python3 -u docs/reports/scripts/v2_stage8_qa.py` and focused accessibility tests; include screenshots, test exits and rollback diff in a follow-up report. Retain draft PR #5 until the owner separately authorises merging/deployment. Do not alter paper figures or other programme statuses.
