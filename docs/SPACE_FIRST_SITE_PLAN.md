# SymTech Ventures — Space-first research website plan

**Version:** 1.0 proposal  
**Date:** 16 November 2026  
**Status:** Content and information-architecture design; not implemented on the live site

## Positioning

**Site identity:** SymTech Ventures — An Independent Research Project  
**Primary focus:** foundations, research questions and computational investigation relevant to **space exploration**.  
**Suggested tagline:** *Exploring the mathematics and physics behind the future of space exploration.*

### Suggested introductory description

> SymTech Ventures is an independent research project examining questions in mathematical and theoretical physics, particularly where they may inform our understanding of space exploration. The website shares accessible lessons, exploratory discussion papers, proposed research targets and computational study plans. The work is at an early stage and does not claim experimental breakthroughs, working propulsion technologies or peer-reviewed findings.

The word "Ventures" is retained as the existing project name and domain, **not** as evidence of a start-up, funded laboratory or product company.

## Public navigation

| Top-level item | Purpose | Recommended destination |
| --- | --- | --- |
| **Home** | Clear independent-research identity, space focus, four programme paths and recent site updates | `/` |
| **Research** | Space exploration research overview; links to SYMMETRIA, NSRP and SEIP | `/pages/research.html` (new) |
| **BridgePoint** | Friendly learning path, sixteen lessons in four groups, gradual mathematics | `/pages/bridgepoint.html` (new) |
| **Discussion Papers** | SYMMETRIA discussion-series pages, clearly labelled as exploratory public writing | Existing `/pages/discussion-series.html` |
| **Publications** | Formal publications catalogue; **no publication entries yet** | `/pages/publications.html` (new, empty state) |
| **About** | Independent-project status, methodology, contact and owner's LinkedIn page | `/pages/about.html` (new); preserve existing contact URLs |

On the Research landing page link to:
- `/pages/symmetria.html` — formulation, hypotheses and discussion
- `/pages/nsrp.html` — **five existing stage projects, each with four proposed research phases** (20 phases total)
- `/pages/seip.html` — **five existing stage projects, each with four proposed engineering/computation phases** (20 phases total)

The homepage should feature four equally presented **programme overview cards**: SYMMETRIA, BridgePoint, NSRP, SEIP. Their sequence should make the audience path comprehensible, while the site headline remains **space exploration**.

## Space focus across the website

- Put space exploration, physical constraints, orbital/mission questions and reliable mathematical models at the centre of the homepage and Research overview.
- Explain that **BridgePoint is an enabling learning route**, not a competing research theory.
- Keep **NSRP** as validation-first theoretical work and **SEIP** as reproducible computational/engineering exploration, with two-way correction between them.
- Frame **SYMMETRIA** as a speculative/exploratory source of research questions, not a validated alternative to physics.
- Reframe the five historical "divisions" as *possible application areas* (with space exploration foregrounded); do not present them as operating departments. Preserve legacy `pages/divisions.html` and child URLs until a deliberate navigation and redirect decision.
- Remove visible references to a "proposed Silicon Valley start-up", venture fundraising, recruitment of founding leads and unearned technology capability. Preserve existing legacy URLs and archive/historical context where appropriate.

## Programme structures — retain their distinct models

See [`PROGRAMME_SERIES_STRUCTURE.md`](PROGRAMME_SERIES_STRUCTURE.md) for the adapted structures:

- **SYMMETRIA:** 4 categories × 4 existing discussion papers (16 total).
- **BridgePoint:** 4 categories × 4 planned lessons (16 total).
- **NSRP:** 5 historical research projects × 4 phases (20 phases total).
- **SEIP:** 5 historical engineering projects × 4 phases (20 phases total), paired with NSRP.

NSRP and SEIP **must not be converted to 4×4**. Show five project sections with four phase entries each. Space exploration is the primary site context, but does not justify replacing the underlying programme structure.

**Status:** The BridgePoint lessons and NSRP/SEIP phase catalogue are descriptions and intentions, not claims that new lessons, results or technologies have been delivered, completed, verified or published.

The SYMMETRIA Discussion Series already has a separate 16-item/4-category manifest. **Retain the existing series**, but review legacy page-level wording for consistency with a space-first, independent-research identity.

## Publications: intentionally empty

The Publications page should show a brief neutral empty state:

> **No formal research publications listed yet.** This section will be updated when work is ready for public release.

**Do not populate** its publication catalogue with planned manuscripts, speculative projects, prior PDF drafts or the SYMMETRIA discussion series without a new explicit decision.

The existing SYMMETRIA manifest currently marks the first four *discussion papers* as `Published` (meaning accessible on the website), with the rest planned. Avoid erasing their URLs or claiming peer review. During later implementation, use wording such as **"Available online — discussion paper"** to distinguish open website discussion from formal academic publication.

## LinkedIn and contact

Use the explicitly supplied profile:
- [Dr Geoffrey Thomas — LinkedIn](https://www.linkedin.com/in/drgeoffthomas)

Place a clearly labelled external LinkedIn link on the **About** page and in the footer, preserving the existing `pages/contact.html` and enquiry flow unless separately revised. Use `rel="noopener noreferrer"` for links opening a new tab. Do not invent affiliations, professional positions or contact details from an unverified external profile.

## Editorial/content rules

- UK English, plain speech first, mathematics explained progressively.
- BridgePoint lessons should show prerequisites, objectives, a short worked example, symbol-by-symbol explanations, a recap and *Going Deeper* optional content.
- NSRP's **five projects and four phases per project** describe research targets/questions with acceptance/failure criteria, not scientific conclusions.
- SEIP's **five companion projects and four phases per project** describe proposed engineering work with runnable baselines or reproducibility criteria, not verified spacecraft engineering.
- Include status metadata: `proposed`, `in progress`, `available online — discussion`, `tested`, `independently verified` only with evidence.
- Avoid implying university/institutional affiliation or funding.

## Website migration requirements

1. Scope and approve wireframes and actual page copy in private/editorial work.
2. Codex implements navigation and page templates on a **new branch**.
3. Work reviews real desktop and mobile HTML renders and scientific language.
4. Check existing paper paths and `sitemap.xml`; do not break the four already accessible SYMMETRIA discussion papers.
5. Do not merge or deploy until the project owner explicitly approves the reviewed implementation.

**This document does not update published website HTML.**
