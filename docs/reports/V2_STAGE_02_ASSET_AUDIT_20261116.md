# SymTech Ventures v2.0 — Stage 2 Existing Site Asset and Editorial Audit

**Date:** 16 November 2026 (GMT)  
**Status:** Completed read-only **Chat** source and visual audit; no Work/Codex session consumed  
**Tracking:** [Issue #3](https://github.com/SymTechVenturesOrg/symtechventures.github.io/issues/3) · [Planning PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)  
**Source:** Existing public `main` branch of `SymTechVenturesOrg/symtechventures.github.io`  
**Purpose:** Decide what images, content and URLs to preserve in a fresh independent, space-exploration-focused site.

## Method and scope

- Read the `main` Git tree and examined current primary-page HTML, SYMMETRIA article paths and four-paper series manifest.
- **Visually inspected all ten exact shortlisted WebP files** retrieved from GitHub as binary/base64 via the connected repository tool and displayed for image-based review. This report reflects the actual observed visuals; it does **not** rely on filenames alone.
- Examined HTML `<img>` tags, their `alt` attributes, stale navigation references and start-up language for seven site pages and four articles.
- Initial source tree: **117 tracked files**, of which **57 are under `images/`**. These numbers come from the current `main` tree and are not a claim of an exhaustive visual review of every image.
- No evidence of an asset attribution/licence/credits file was found in the tracked tree by filename (`.gitattributes` exists, but is not a licence). **Ownership, provenance and redistribution rights are unverified.** Before expanding reuse or deriving new media, confirm source/rights with the owner and retain relevant records.
- Neither the live website nor the existing paper files were changed.

## Ten visually inspected candidates

| Asset in existing repository | Observed visual content | Recommendation for v2.0 | Suggested accessible description / caution |
| --- | --- | --- | --- |
| `images/logos/symtech.webp` | Metallic blue/silver stylised **S** within partial circular sweep, transparent background | **Retain** as project logo; ensure a text label alongside it | Alt text `SymTech Ventures` if used as a linked brand logo; `alt=""` if adjacent text duplicates it. Rights provenance remains unverified |
| `images/heroes/symtech_hero.webp` | Golden Gate Bridge at sunset, San Francisco skyline and luminous geometric network against night sky | **Omit from new home hero**; suggests the abandoned Silicon Valley start-up identity | If kept only in an archive, call it conceptual artwork and do not imply a local office, physical presence or real observation |
| `images/heroes/symmetria_hero.webp` | Abstract intersecting gold/blue wave lines, luminous symmetric loops and network patterns | **Strong reuse** as SYMMETRIA research landing hero or restrained supporting background | Describe as `Abstract illustration of intersecting light patterns and symmetric wave structures`; explicitly conceptual, not a measured field |
| `images/heroes/nsrp_hero.webp` | Futuristic dark laboratory with numerous researchers, glowing columns and holographic structures | **Omit from research hero**; portrays operational staff, facilities and apparatus the project has not established | If preserved as archival concept art, label `Fictional depiction of a research laboratory`, not a documentary photograph |
| `images/divisions/symspace_dynamics_banner.webp` | Cinematic futuristic spacecraft, populated orbital platforms, planet/moon and apparent wormhole/tunnel | **Omit from main site**; *optional* for a distinctly labelled speculative-concepts page | Alt text should mention `Illustration of a fictional spacecraft and orbital station with a speculative space tunnel`; no FTL/warp implication as real technology |
| `images/heroes/divisions_hero.webp` | Five illuminated circular subject icons (energy, materials, health, spacecraft and computing) over an Earth/space background | **Retire from primary navigation/homepage**, because it promotes the outdated five-division commercial umbrella | Could remain in a separately described historical-vision archive after approval |
| `images/symmetria/paper-01/01_unified_framework_cover.webp` | Text-rich illustrated title cover; relativity, quantum theory, physics history and unification motifs | **Preserve in Paper 1**, optionally thumbnail on Discussion Papers page | Existing alt text is title-only; embedded equations and small diagram annotations warrant factual/legibility review before featured educational reuse |
| `images/symmetria/paper-02/02_symmetry_cover.webp` | Text-rich symmetry cover with spiral shell, galaxy, snowflake, sunflower, waves and equations | **Preserve in Paper 2**, optionally thumbnail | Existing title-only alt text; embedded maths and illustrative claims should not be treated as verified equations without review |
| `images/symmetria/paper-03/03_nilpotent_foundation_cover.webp` | Text-rich cover with paired blue/gold swirling structures around a dark centre and galaxies | **Preserve in Paper 3**, optionally thumbnail | Label as conceptual illustration of nilpotent ideas; not a literal depiction of physical structures |
| `images/symmetria/paper-04/04_mathematics_elegance_reality_cover.webp` | Text-rich mathematical/physics cover with symmetrical blue/gold forms, formulae and central dark circle | **Preserve in Paper 4**, optionally thumbnail | Inspect embedded formulae carefully for accuracy and typography; alt text need not reproduce every decorative equation |

**Overall aesthetic:** keep midnight blue, restrained silver/white typography, one sparing blue/gold accent and scientifically modest abstract imagery. Avoid simulated research facilities, impossible machines and the old investor-pitch look. For a space-focused homepage, a legitimate astronomy/space image or a modest abstract starfield would convey the theme more responsibly than a fictional wormhole/spacecraft.

## Source image use and rights gate

The asset files currently reside in the site's existing repository, but that fact **does not establish authorship or permission for additional uses**. The owner should confirm whether images were self-produced, AI-generated, licensed or sourced externally, and record any required attribution. No rights conclusion was possible from filename metadata or tracked files alone. The current visual review does not certify embedded mathematical content.

## Existing content and URL audit

### Four live SYMMETRIA discussion papers

| Paper | Original public path | Status and handling |
| ---: | --- | --- |
| 1 | `/articles/symmetria/symmetria-paper-01.html` | Existing complete HTML with seven paper-specific images. Preserve contents, relative asset paths and URL |
| 2 | `/articles/symmetria/symmetria-paper-02.html` | Existing complete HTML with seven paper-specific images. Preserve contents, relative asset paths and URL |
| 3 | `/articles/symmetria/symmetria-paper-03.html` | Existing complete HTML with seven paper-specific images. Preserve contents, relative asset paths and URL |
| 4 | `/articles/symmetria/symmetria-paper-04.html` | Existing complete HTML with seven paper-specific images. Preserve contents, relative asset paths and URL |

These files additionally contain six common navigation/logo images each. **All 52 `<img>` elements across these four source files have `alt` attributes**, though quality and relevance vary. All four pages currently link to the obsolete `founding-fellows.html` navigation item and must receive the new shared navigation without losing their article bodies or imagery.

The existing `SYMMETRIA_Paper_Series_Manifest.json` contains **16 entries**: **4 with `Status: Published` and 12 with `Status: Planned`**. In v2.0, the first four should be described publicly as **`Available online — discussion paper`**, not as peer-reviewed or formal publications. The **formal Publications section must have zero entries** pending a separate approval.

### Old identity and navigation

Sampled: `index.html`, `pages/symmetria.html`, `pages/nsrp.html`, `pages/divisions.html`, `pages/founding-fellows.html`, `pages/contact.html` and `pages/discussion-series.html`.

- `index.html` literally displays **`Proposed Silicon Valley start-up`** and presents a commercial/organisational research ecosystem with recruitment language. Replace completely with independent space-exploration project identity.
- `pages/founding-fellows.html` contains early-recruitment language; remove from primary navigation but consider preserving its legacy URL with a plain historical note or approved redirect.
- `pages/divisions.html` still elevates five research divisions; remove from primary navigation, perhaps describe their historical role in an archive/Future Applications page rather than implying operational departments.
- `pages/nsrp.html` contains existing stage descriptions, but needs the verified **5 projects × 4 phases** reader-friendly format; SEIP and BridgePoint require new landing pages.
- `pages/discussion-series.html` contains the four-category discussion-paper scheme; keep original paper destinations, update status semantics.
- Existing primary page samples have `alt` attributes for all `<img>` elements, but some are just short labels such as `NSRP`, `SYMMETRIA`, `Divisions`. Improve contextual semantics when building a new shared shell.
- Do not delete or break `pages/contact.html`, `pages/enquiry.html` or existing thank-you/legacy URLs before verifying routing and form handling.

## Recommendation / acceptance

**Reuse shortlist:** existing logo + abstract SYMMETRIA hero + the four paper cover images in their article context.  
**Retire from primary visual identity:** Golden Gate/Seattle-like tech-startup skyline, staged futuristic research lab, giant fictional spacecraft/warp tunnel, and five-division infographic hero.  
**New imagery to consider later:** grounded space-science imagery or abstract non-literal starfields, subject to rights and text contrast checks.

**Stage 2 Chat audit conclusion:** The entire intended image/content shortlist is assessed and the read-only audit has a verified versioned report. There is **no immediate need to spend Work tokens** repeating the visual assessment. If the owner later requests independent editorial judgment, the [original Work/Luna handover](../handovers/V2_STAGE_02_WORK_ASSET_AUDIT.md) remains available as an optional second opinion — not an executed Work task.

### Open questions for Stage 3

1. Confirm image creation/licensing provenance before deciding final public reuse.
2. Approve a space-first home image concept that does **not** depict an achieved physical breakthrough.
3. Define exact new navigation, legacy URL handling and the status labels for the 16 BridgePoint lessons / 20 NSRP phases / 20 SEIP phases.
4. Check formulae embedded in cover illustrations before educational promotion.

**No preview, runtime test, merge or deployment is claimed in Stage 2.**
