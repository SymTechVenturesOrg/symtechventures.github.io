# SymTech Ventures v2.0 — Stage 4 Codex/Luna Prototype Handover

**Status:** Prepared by Chat, **not authorised to execute until Stage 3 owner approval**  
**Owner/lead:** Chat; Codex is a bounded implementation specialist, not the programme manager  
**Model:** **Luna preferred wherever selectable**. Terra is **not authorised**; report need and obtain owner approval before escalation.  
**GitHub issue:** [#3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3)  
**Planning PR:** [#2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)  
**Inputs:** [Stage 3 sitemap and page briefs](../V2_STAGE_03_INFORMATION_ARCHITECTURE.md), [Stage 2 visual audit](../reports/V2_STAGE_02_ASSET_AUDIT_20261116.md), [project charter](../V2_PROJECT_CHARTER.md), [development workflow](../WEBSITE_DEVELOPMENT_WORKFLOW.md).

## Precise task

Create **one working, responsive homepage prototype** for the new independent research website focused primarily on space exploration.

**Do not** build the full site or all programme pages. Stage 6 handles broad implementation after the owner approves this design. **Do not merge, deploy or alter the live GitHub Pages website.**

The prototype should display, in this order:
1. Simple brand/logo and accessible six-item navigation: Home, Research, BridgePoint, Discussion Papers, Publications, About.
2. New independent research hero: **Exploring the Physics of Space**, supporting text and two sensible links: Research and BridgePoint. State exploratory status plainly.
3. Four programme overview cards: SYMMETRIA, BridgePoint, NSRP, SEIP, with accurate distinctions.
4. Readable cards for the **four existing SYMMETRIA discussion papers**, linking to their **unchanged original article URLs**.
5. Short approach/evidence disclosure distinguishing accepted science, speculative questions, modelling and tested findings.
6. Footer with About, Contact and the explicit LinkedIn link https://www.linkedin.com/in/drgeoffthomas.

### Design and image rules

- Midnight blue and near-black background, subtle blue/gold accent, readable typographic hierarchy, clear focus indicators, accessible colour contrast, generous whitespace.
- Existing `images/logos/symtech.webp` may be used as a **provisional existing-site asset**, pending documented rights/source confirmation.
- `images/heroes/symmetria_hero.webp` is eligible for a **secondary** abstract research-themed image if visually useful.
- Do **not** use `images/heroes/symtech_hero.webp` (Golden Gate startup), `images/heroes/nsrp_hero.webp` (fictional staffed lab), `images/divisions/symspace_dynamics_banner.webp` (fictional FTL/wormhole craft) or `images/heroes/divisions_hero.webp` as evidence of operational capability.
- Use restrained CSS stars/gradients if a safe space-themed image is needed; do not fabricate real observatory photographs or actual technology diagrams.
- Preserve article paths; do not change the original four paper files, their copy or imagery in Stage 4.

### Engineering and GitHub boundaries

- Create a **new, purpose-named GitHub feature branch** off current `main`; **open a draft PR** for the prototype. Do not commit to `main` and do not merge.
- Limit changes to a standalone prototype page (or a carefully isolated prototype folder) plus only essential prototype CSS/JS and verification notes. Avoid replacing live `index.html` until the owner approves the design and begins Stage 6.
- Do not reformat unrelated existing files or revise scientific claims without a Chat-approved editorial brief.
- Existing `CNAME`, `sitemap.xml`, inquiry form and online articles must remain unchanged at this stage.
- Ensure prototype links are meaningful: use known existing routes where possible; do not present a dead placeholder as a live page.
- Prefer static HTML/CSS with minimal JS. Keep navigation keyboard accessible; core information must remain available without JS.

## Verification requested

- Actual browser-generated **desktop and smartphone portrait** renders (target desktop ~1440px, phone ~390px); do not substitute AI-created lookalikes and call them screenshots.
- A working demo URL where available; otherwise precise local preview/run steps and screenshots. **Never claim an unverified live preview.**
- Check heading order, visible keyboard focus, navigation, contrast, image alt descriptions, layout overflow and existing four article links.
- Record actual commands, tools, test outcomes and known limitations in the draft PR.
- Give Chat a short **COPY TO CHAT** handback: PR link, summary, screenshot/demo paths, checks, defects and recommended adjustments. Stop; do not proceed to Stage 5/6 autonomously.

## DTSU — read before execution

Read [DTSU — Dr T Style Updates](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md). At genuine Europe/London current time send:

`[HH:MM:SS] NN% — factual 10–20-word status; ETA ~remaining duration.`

Send 0% **before actions**, every honest 10% whole-task milestone and every 3–5 minutes during long intervals. Report ETA in each visible update, 100% only on verified completion. Never prefill timestamps or claim continued background work without a running system.

## Acceptance boundary

The prototype is **for owner review**. No production merge/deploy is authorised by either this document or the Stage 3 design approval. If tool capability, preview access or asset rights are uncertain, disclose rather than assume.
