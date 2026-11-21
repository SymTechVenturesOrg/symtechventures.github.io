# SymTech Ventures website — contributor and AI operating instructions

This file governs changes to the public `SymTechVenturesOrg/symtechventures.github.io` site.

## Current editorial identity

- **SymTech Ventures is an independent research project primarily focused on space exploration**, not a Silicon Valley start-up, fundraising campaign or product company.
- Use **UK English**, an accessible tone, semantic markup and an uncluttered, responsive design.
- The four featured programmes are SYMMETRIA, NSRP, SEIP and BridgePoint. They serve different purposes; see [the proposed space-first site plan](docs/SPACE_FIRST_SITE_PLAN.md).
- **Publications must contain zero entries** until the owner explicitly approves a qualifying formal output.
- Preserve existing discussion-paper URLs. Do not conflate "available online discussion paper" with peer-reviewed/formally published research.
- The project owner's public LinkedIn link, when requested on About/footer, is `https://www.linkedin.com/in/drgeoffthomas`. Do not invent affiliations, titles or personal details.

## Work allocation — Chat-led, specialist-token efficient

- **Chat is the continuous lead** and does the primary scoping, source-grounded content drafting, straightforward GitHub/documentation updates, review, status and final owner-approved release coordination.
- **Work supports only stages 2, 5 and 7:** existing content/image assessment, focused scientific/editorial review and the BridgePoint pilot/acceptance. Use **Luna** wherever selectable.
- **Codex supports only stages 4, 6 and 8:** live-renderable prototype, HTML/CSS/JS implementation and technical/browser QA. Use **Luna** wherever selectable.
- **Stages 1, 3 and 9 are Chat-only by default**. The specialist engagement sequence is **Work → Codex → Work → Codex → Work → Codex**.
- **Terra has zero planned use**. Request owner authorisation before any evidence-based escalation.
- Work and Codex must not edit the same HTML/CSS/JS files concurrently. End each specialist stage with verification, a concise COPY TO CHAT and a DTSU including a grounded ETA.
- **The project owner must explicitly approve each production merge or deployment.**

Read the [nine-stage Chat-led workplan](docs/WEBSITE_V2_WORKPLAN.md) and the [development workflow](docs/WEBSITE_DEVELOPMENT_WORKFLOW.md). These documents describe planned roles, not guaranteed tool capabilities or live production changes.

## Coding and content checks

1. Modify only a feature branch; never directly write `main` for substantial changes.
2. Supply real HTML/browser previews and actual test evidence, not generated lookalike screenshots.
3. Check keyboard navigation, mobile portrait layout, semantic headings, screen-reader names, contrast and alt text.
4. Keep `sitemap.xml`, canonical URLs and existing article paths accurate, including on any page restructuring.
5. Label speculative scientific proposals, reproducible simulations and empirical findings distinctly.
6. Do not claim working space-propulsion technologies or confirmed SYMMETRIA predictions.
7. BridgePoint: **4 categories × 4 lessons**; NSRP: **5 research projects × 4 phases**; SEIP: **5 engineering companion projects × 4 phases**. These are different models; do **not** auto-publish drafts.
8. For significant work, report DTSU progress with a defensible percentage, the actual local time, evidence and an estimated ETA.
9. Keep private research files and unfinished manuscripts out of this public repository unless separately reviewed and approved.

## Current planning documents

- [Chat-led v2.0 workplan](docs/WEBSITE_V2_WORKPLAN.md)
- [Space-first information architecture](docs/SPACE_FIRST_SITE_PLAN.md)
- [BridgePoint 4×4 and NSRP/SEIP 5×4 programme structures](docs/PROGRAMME_SERIES_STRUCTURE.md)

These are proposals, **not changes to the current live website**.
