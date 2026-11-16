# SymTech Ventures website — contributor and AI operating instructions

This file governs changes to the public `SymTechVenturesOrg/symtechventures.github.io` site.

## Current editorial identity

- **SymTech Ventures is an independent research project primarily focused on space exploration**, not a Silicon Valley start-up, fundraising campaign or product company.
- Use **UK English**, an accessible tone, semantic markup and an uncluttered, responsive design.
- The four featured programmes are SYMMETRIA, NSRP, SEIP and BridgePoint. They serve different purposes; see [the proposed space-first site plan](docs/SPACE_FIRST_SITE_PLAN.md).
- **Publications must contain zero entries** until the owner explicitly approves a qualifying formal output.
- Preserve existing discussion-paper URLs. Do not conflate "available online discussion paper" with peer-reviewed/formally published research.
- The project owner's public LinkedIn link, when requested on About/footer, is `https://www.linkedin.com/in/drgeoffthomas`. Do not invent affiliations, titles or personal details.

## Work allocation

- **Chat:** confirm research/website priorities and secure the project owner's approval.
- **Work:** source review, scientific/editorial content, accessible lesson writing, rendered-page evaluation.
- **Codex:** HTML/CSS/JS implementation, responsive layouts, static-site checks and PR preparation.
- Avoid Work and Codex editing the same HTML/CSS files in parallel; agree hand-off boundaries.
- **The project owner must explicitly approve each production merge or deployment.**

Full process: [WEBSITE_DEVELOPMENT_WORKFLOW.md](docs/WEBSITE_DEVELOPMENT_WORKFLOW.md).

## Coding and content checks

1. Modify only a feature branch; never directly write `main` for substantial changes.
2. Supply real HTML/browser previews and actual test evidence, not generated lookalike screenshots.
3. Check keyboard navigation, mobile portrait layout, semantic headings, screen-reader names, contrast and alt text.
4. Keep `sitemap.xml`, canonical URLs and existing article paths accurate, including on any page restructuring.
5. Label speculative scientific proposals, reproducible simulations and empirical findings distinctly.
6. Do not claim working space-propulsion technologies or confirmed SYMMETRIA predictions.
7. BridgePoint: 4×4 lessons; NSRP: 4×4 proposed research targets; SEIP: 4×4 proposed engineering targets; do **not** auto-publish drafts.
8. For significant work, report DTSU progress with a defensible percentage, the actual local time, evidence and an estimated ETA.
9. Keep private research files and unfinished manuscripts out of this public repository unless separately reviewed and approved.

## Current planning documents

- [Space-first information architecture](docs/SPACE_FIRST_SITE_PLAN.md)
- [4×4 series outlines](docs/CONTENT_SERIES_4X4.md)

These are proposals, **not changes to the current live website**.
