# SymTech Ventures v2.0 — Phase 1C Owner Layout Review Pack

**Prepared:** 17 November 2026 (GMT)  
**Status:** **DRAFT FOR OWNER VISUAL REVIEW — NOT APPROVED, NO PHASE 2 AUTHORISATION**  
**Parent plan:** [Phased layout and imagery workplan](../V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md)  
**Current feature:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)

## 1. Grounded visual evidence

These are actual **390px and 1440px Chromium viewport screenshots**, not mock-ups and **not complete full-page screenshots**. They were committed in [Phase 1B QA](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_PHASE_01B_LAYOUT_BROWSER_QA_20261117.md). The link collection shows what can actually be reviewed without claiming an entire page has been visually inspected below the viewport.

| Page | Mobile (390px) | Desktop (1440px) | Review question |
| --- | --- | --- | --- |
| Home | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-home-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-home-1440.png) | Approve two-column desktop and stacked mobile hero layout; home image slot currently uses orbit SVG |
| Research | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-research-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-research-1440.png) | Preserve sober text-led research page? |
| BridgePoint | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-bridgepoint-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-bridgepoint-1440.png) | Approve new Jump to navigation after intro/status note? |
| Discussion Papers | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-discussion-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-discussion-1440.png) | Four groups visible; correct Available/Planned semantics |
| NSRP | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-nsrp-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-nsrp-1440.png) | Verify header hierarchy and project index, no change to 5×4 planned structure |
| SEIP | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-seip-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-seip-1440.png) | Same hierarchy and project index |
| About | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-about-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-about-1440.png) | Confirm mobile full-justification spacing is acceptable |
| Contact | [mobile](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-contact-390.png) | [desktop](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1b-contact-1440.png) | Confirm paused enquiries/privacy state remains clear and justified text is legible |

## 2. Initial visual assessment from actual captures

- **Positive:** clear research/space-first positioning, restrained midnight background, readable light foreground, serif/display versus sans-serif/body hierarchy, effective desktop two-column hero and mobile stacking, no starfield in current screenshots.
- **Positive:** visible top-level navigation and mobile disclosure; page navigation/landmarks and four new category/project indexes maintain a coherent, subdued design.
- **Potential weakness (owner style choice):** at 390px, **full justification produces wide spaces between words** in About, Contact, BridgePoint and NSRP introductions. The CSS already specifies `text-align:justify;text-justify:inter-word;hyphens:auto;overflow-wrap:break-word`; the screenshot spacing is therefore not simply a missing hyphenation declaration. There is **no owner authorisation to switch to left-aligned mobile prose**. Options are **A: retain the current fully justified mobile typography** (highest fidelity to current Dr T style) or **B: explicitly approve a narrow mobile readability exception** after comparing a browser rendering. **Neither is assumed selected**.
- **Possible UX improvement already committed:** on long BridgePoint/Discussion/NSRP/SEIP pages the new `Jump to` boxes make major sections easier to find; [18/18 actual mobile pointer links reached the appropriate target](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_PHASE_01B2_ANCHOR_ACTIVATION_VERIFICATION_20261117.md). A final [keyboard, settled-position and desktop check](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/handovers/V2_PHASE_01B3_CODEX_KEYBOARD_AND_SCROLL_SETTLEMENT_20261117.md) remains open.
- **Guardrail:** current images inside four protected SYMMETRIA papers remain unchanged; Phase 3 is deliberately later. The intended but absent Earthrise raster is a **candidate Phase 2 asset, not a completed layout/image change**.
- **No claim of universal visual correctness:** these are viewport captures; Phase 1B full integration regression separately checked structural/layout errors at 320/390/768/1440, but final aesthetics require the owner.

## 3. Suggested minimum layout freeze / Phase 2 slot decisions

These are recommendations for consideration, **not owner-approved selections**.

| Decision | Proposed default | Why it follows from source evidence |
| --- | --- | --- |
| Header/footer/page palette | **Retain** current midnight/gold/cyan visual identity | Cohesive in current viewport screenshots; no validated need for redesign |
| Home hero placement | **Retain current orbit region as the future single Phase 2 hero image slot** | Already responsive two-column desktop, below CTA mobile; avoids rebuilding HTML structure |
| Home hero artwork | **Deferred to Phase 2**: choose an owner-approved ChatGPT-generated Earthrise or keep the existing CSS/SVG orbit | Actual Earthrise file was not found in site checkout; no invented upload |
| Research/BridgePoint illustrations | **Optional** and sparse, only if owner sees a clear explanatory purpose | Current pages communicate through cards/status prose; no need to fill empty space |
| NSRP/SEIP, publications, about, contact | **No additional images required by default** | Maintains early-stage research integrity and restrained identity |
| Mobile justified prose | **Explicit owner decision** before any CSS change | Visible word-spacing trade-off in 390px screenshots |

**Phase 2 output count is intentionally not fixed until the owner accepts image positions and aspect-ratio slots.** WebP quality 80 applies later to actual approved image outputs; it is encoder quality, not a guaranteed file-size reduction.

## 17 November 2026 — Owner-approved introductory typography refinement

After reviewing a 1440px screenshot of Discussion Series, the owner explicitly approved **introductory paragraphs using the entire main content width**, rather than stopping short at `max-width:820px`, and a **smaller mobile intro font** to reduce the unsightly gaps caused by fully justified lines. The owner did **not** retract the global fully-justified prose preference.

Chat implemented both narrow edits in the existing feature branch at [`css/v2-programmes.css`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/css/v2-programmes.css):
- `.page-lead` now has `max-width:100%` within the pre-existing maximum **980px** `.page-content` container. This applies consistently to redesigned programme and introductory pages.
- At **viewport widths of 740px or less**, `.page-lead` uses `font-size:1rem` (typically **16px** rather than 18.08px), `line-height:1.7`; wider viewports retain `1.13rem`, `line-height:1.75`.
- The shared `text-align:justify; hyphens:auto; overflow-wrap:break-word` CSS is **unchanged**. The homepage's distinct `.hero-lead` was **not** altered.

**Status:** source was fetched and checked; CSS braces balanced; no paper HTML or image changed. **The 16 screenshot links earlier in this file pre-date the CSS adjustment.** Do not present them as post-change evidence. The [focused Codex browser/regression handover](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/handovers/V2_PHASE_01C_TYPOGRAPHY_REGRESSION_20261117.md) is prepared, **not yet executed**; fresh before/after screenshots and a new full regression are required before declaring the revised look tested.

This closes **one typography policy question**, not overall owner layout approval, all page-specific design decisions, or Phase 2 image-slot authorisation.

## 4. Phase 1C review/acceptance gate

Phase 1C may be marked **LAYOUT ACCEPTED** only after:
1. The owner reviews the current screenshot evidence and any narrow refinements.
2. The final native-jump-link keyboard/settled scroll/desktop checks are either verified or consciously recorded as a residual acceptance limitation — not silently declared PASS.
3. The owner has **approved retaining justification while reducing mobile introductory `.page-lead` text to 1rem**; inspect the actual post-change screenshots to decide whether the visual result is accepted. Any further changes to other body prose require separate approval.
4. The owner approves the **homepage hero image slot** (placement/aspect/crop) and decides whether the remaining optional slots actually belong in the layout.
5. If any site HTML/CSS changes are made, a **new post-change full regression** is run and recorded; otherwise existing Phase 1B regression exit 0 stands as evidence.

**No Phase 2 generation, paper-figure replacements, merges, deployments or scientific-publication claims have been authorised.** The owner alone decides when to advance.


## 17 November 2026 — actual post-change typography QA and refreshed screenshots

The approved typography adjustment has now been checked in an **actual browser** against the feature checkout. The [Phase 1C verification report](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/V2_PHASE_01C_INTRO_TYPOGRAPHY_QA_20261117.md) records **full regression exit 0** across 36 files and 27 browser visits, with expected research-paper integrity and programme counts.

Computed `.page-lead` readings across six representative pages:
- **320 / 390 / 740px:** **16px** text, **27.2px** line height, fully justified and full parent width (286 / 356 / 706px respectively).
- **768 / 1440px:** **18.08px** text, **31.64px** line height, justified and full parent width (720 / 980px).
- Zero horizontal document overflow in all sampled cases. **The desktop Discussion lead now reaches the 980px page-content column**, rather than being artificially capped at 820px.

**Fresh post-change Chromium viewport captures**, replacing the outdated typography evidence for these specific pages:
- [Discussion Series — 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1c-discussion-series-390.png) · [1440px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1c-discussion-series-1440.png)
- [About — 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1c-about-390.png) · [1440px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1c-about-1440.png)
- [BridgePoint — 390px](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/feature/v2-space-research-website/docs/reports/screenshots/phase1c-bridgepoint-390.png)

**Chat visual inspection:** The new Discussion Series 1440px lead aligns with the width of the index/category content below; at 390px, smaller lead text results in more compact lines. The refreshed About screenshot shows that some word spacing remains visibly uneven because full justification is still active. This is an **aesthetic observation**, not a failed code test or permission to override owner styling.

**Navigation clarification:** Phase 1B-3's keyboard/deep-link/reduced-motion report had one contradictory NSRP entry (target top outside viewport). The Phase 1C regression report independently rechecked **NSRP #proj-5 at 390×844** and measured `scrollY=4067`, target top **100.36px**, bottom **169.45px**: target visibly within viewport. Other earlier keyboard tests remain scoped to the links actually checked.

**Current decision gate:** Phase 1C typography is **implemented and technically verified**. Site-wide final visual acceptance, approval of remaining mobile justified spacing and **exact homepage / optional image slot choices** are still for the owner. **Phase 2 imagery is NOT yet approved.**
