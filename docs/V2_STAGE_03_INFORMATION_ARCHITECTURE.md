# SymTech Ventures v2.0 — Stage 3 Information Architecture and Page Briefs

**Date:** 16 November 2026  
**Status:** Chat-authored **proposal for owner review** — no website implementation or publication authorised  
**Tracking:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3) · [Planning PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)  
**Inputs:** [Project charter](V2_PROJECT_CHARTER.md), [Stage 2 read-only audit](reports/V2_STAGE_02_ASSET_AUDIT_20261116.md), [programme structures](PROGRAMME_SERIES_STRUCTURE.md), [Chat-led workplan](WEBSITE_V2_WORKPLAN.md).

## Core decision: a simple, space-first public research library

SymTech Ventures is an **independent research project** with a primary interest in **space exploration**, theoretical/mathematical foundations and responsible computational investigation. The site exists so interested people can read, learn and follow actual progress. It is **not** an investor pitch, start-up recruitment platform, working laboratory or evidence of established new propulsion technology.

### Proposed primary navigation (six items)

| Label | Proposed route | Reader's purpose |
| --- | --- | --- |
| **Home** | `/` | Understand the independent project and its space-exploration focus |
| **Research** | `/pages/research.html` | Explore SYMMETRIA, NSRP and SEIP, with clear status and evidence limits |
| **BridgePoint** | `/pages/bridgepoint.html` | Learn the mathematics and physics from beginner-friendly lessons |
| **Discussion Papers** | `/pages/discussion-series.html` | Read the four currently accessible SYMMETRIA essays and view 12 planned titles |
| **Publications** | `/pages/publications.html` | See the **empty formal publications catalogue**, with a clear explanation |
| **About** | `/pages/about.html` | Project description, research approach, attribution and LinkedIn/contact routes |

The primary navigation must remain usable on smartphone portrait. On narrow screens use a semantic accessible mobile menu if necessary; do not rely on pointer hover.

### Secondary and preserved routes

- Research child pages: existing `/pages/symmetria.html`, existing `/pages/nsrp.html`, and new `/pages/seip.html`.
- Existing `/pages/contact.html` remains reachable from About and footer. Its enquiry/form-related routes require a privacy and functional check before changing.
- Preserve old `/pages/divisions.html`, `/pages/founding-fellows.html` and current division-specific pages as working legacy routes at minimum. Later provide approved historical notes or redirects; do **not** silently erase indexed links.
- Preserve `/articles/symmetria/symmetria-paper-01.html` through `symmetria-paper-04.html`, their article bodies, paper-specific images and internal progression links.
- The existing `/pages/discussion-series.html` and planned Papers 5–16 remain distinguishable from formal publications.
- No separate empty "Research Updates" page at initial launch; add only after there are genuine dated updates to post, rather than publish more placeholders.

## Home page — editorial and visual brief

### Content order

1. **Header:** logo + six primary destinations; modest independent-research identity, not start-up slogan.
2. **Hero:** suggested headline **`Exploring the Physics of Space`**; subheading **`An independent research project exploring the mathematics, theoretical questions and computational methods that underpin space exploration.`** Display as *exploratory research*, not a claim of validated discoveries. Proposed CTAs: **Explore the Research** and **Start with BridgePoint**.
3. **Four compact programme cards:** **SYMMETRIA**, **BridgePoint**, **NSRP** and **SEIP**, each a distinct reader journey. Use accurate maturity labels where appropriate.
4. **Reading starting point:** four currently accessible SYMMETRIA discussion essays, with title, status **Available online — discussion paper** and links to the original URLs.
5. **How we work:** established physics vs hypotheses vs mathematics vs simulation vs evidence — concise cautionary explanation with a link to Research.
6. **Footer:** basic project identity, direct LinkedIn link and About/Contact; avoid staffing, investor, facility or business-office claims.

### Visual direction

- Minimal, contemporary research-library presentation: dark midnight blue / near-black, restrained cool blue and subtle gold highlights, generous whitespace, readable off-white body text.
- Retain existing `images/logos/symtech.webp` (source/rights to be confirmed), and use the abstract `images/heroes/symmetria_hero.webp` as optional **secondary research imagery**.
- **Do not** reuse the current Golden Gate / Silicon Valley hero, staged lab photograph-like visuals or fictional wormhole spaceship as the actual homepage's claim of capability.
- **Updated owner preference, 16 November 2026 (supersedes earlier starfield approval):** **Remove the decorative starfield**, including the old animated canvas/shimmer and the v2 CSS dot patterns. Retain the contemporary near-black/midnight-blue background, subtle gradients, the orbital illustration and the existing readable design.
- **Fully justify running prose** (`text-align: justify`) across redesigned and preserved article/legacy pages, with sensible hyphenation and readable line lengths. Keep headings, navigation, short labels, links and buttons naturally aligned.
- Do not add stars/animation back during later QA or deployment. A genuinely licensed astronomical image is optional only following separate source/rights approval; no image is necessary for the present design.
- Responsive from ~360px mobile portrait upward; avoid relying on tiny text baked into large illustrations for essential information.

## Research overview and programme child briefs

### Research landing — `/pages/research.html`

Explain the programme relationship in plain language: **SYMMETRIA** develops exploratory theoretical questions; **NSRP** checks mathematical consistency and possible implications; **SEIP** investigates bounded computational/engineering feasibility, providing corrective feedback. **BridgePoint** supports the learning required to follow those ideas. Space exploration is the principal longer-term research interest, not an assumed immediate practical application.

### SYMMETRIA — existing `/pages/symmetria.html`

Describe SYMMETRIA as an **exploratory conceptual/theoretical framework** with explicit distinction from established physics. Link to the Discussion Papers index, and preserve its existing four accessible articles. Do not claim the entire 16-paper programme is completed.

### NSRP — existing `/pages/nsrp.html`

Show **five named project sections**, each with **four research phases** (20 total): NCP, SEP, SDEP, SVP, SMP. Use semantic headings and accessible `details/summary` only if the resulting content remains navigable without JavaScript. Each phase shows **Proposed** by default (or a source-supported actual status), focus, method/validation question and evidence note. The NCP detailed phase names require final source-of-truth reconciliation before publication; see the [programme structure source note](PROGRAMME_SERIES_STRUCTURE.md).

### SEIP — new `/pages/seip.html`

Show **five companion engineering projects** of four phases each (20 total): EFP, SEP, SDP, SVP, SMP, paired respectively with NSRP's five projects. A phase description is **a target, not a completed experiment**. Mention standard-PC/Python modelling and reproducibility as intended approaches, not results. Space engineering/propulsion questions must stay within accepted conservation and feasibility constraints.

### BridgePoint — new `/pages/bridgepoint.html`

Use the approved **four categories × four lesson titles** (16 total). Each lesson card may have a plain-language objective, prerequisite tag and honest **Planned** status. **For the initial website release, all 16 lessons remain Planned.** Do not create active lesson links, completed lesson content or placeholder lesson pages. Individual lessons will be developed separately after the website upgrade.

## Discussion Papers and Publications: deliberately separate

### Discussion Papers

The existing manifest has 16 items: **four labelled `Published` in the current JSON and twelve `Planned`**. Present the first four as **available online discussion essays** (not formal peer-reviewed publications) while preserving their original URLs and images. Existing planned-paper placeholder routes must not masquerade as completed results.

### Formal Publications

The new `/pages/publications.html` contains **zero publication records** and a neutral empty state:

> No formal research publications listed yet. This section will be updated when work is ready for public release.

Do not auto-populate with SYMMETRIA discussion essays, unfinished preprints or aspirational paper titles.

## About, LinkedIn and contact

- State explicitly that this is an independent research project, not an operational commercial research venture.
- Link to the supplied public profile: https://www.linkedin.com/in/drgeoffthomas. Use a clear label like **Dr Geoffrey Thomas on LinkedIn**, without inventing a current professional role or endorsement.
- Preserve existing Contact/enquiry URLs initially. The existing enquiry form uses an external submission service; assess privacy text, anti-spam handling, destination settings and whether the form should remain before reusing it in v2.0. Do not publish any private contact details just because they exist in source HTML.
- Avoid unverified professional affiliations, laboratory claims or company registration statements.

## Cross-page content standards

- **UK English** and accessible, direct language for interested non-specialists, with optional deeper technical sections.
- Use transparent scientific/evidence labels: `Established science`, `Research hypothesis`, `Planned`, `Mathematical analysis`, `Simulation`, `Independent measurement` — display only the actual evidence category supported.
- Do not infer science completion from naming a programme stage.
- Explain mathematical symbols on BridgePoint pages; keep diagrams and equations readable in smartphone portrait and keyboard accessible.
- Use semantic HTML, descriptive image alt text, clear focus indicators and readable type sizes. No critical content in image text alone.
- Update titles, meta descriptions, canonical links and sitemap; preserve external inbound URL paths and retain a redirect/historical policy for obsolete sections.
- Do not auto-create new article URLs for uncompleted lessons or programme phases.
- No Work or Codex session is needed to approve/edit this information architecture in Chat.

## Proposed Stage 4 prototype acceptance criteria

Codex should create **one actual homepage implementation prototype** on a separate branch/PR, responsive on desktop and smartphone, using approved text and only allowed/cleared assets. It must show:

- Six usable nav links (with placeholders routed only to existing pages or clearly identified unmerged prototypes).
- The new independent space-exploration research hero, tasteful existing branding and four programme cards.
- Discussion-paper starting links to the original existing Paper 1–4 paths.
- A footer with the supplied LinkedIn URL.
- Real browser screenshots for desktop and ~390px smartphone portrait, and a concise evidence/test report.
- No modifications to production `main`; no merger, deployment or synthetic image falsely claimed as a real rendered preview.

**Stage 3 is ready for owner review once this brief is validated.** Stage 4 must not begin until the project owner accepts the structure and visual direction.
