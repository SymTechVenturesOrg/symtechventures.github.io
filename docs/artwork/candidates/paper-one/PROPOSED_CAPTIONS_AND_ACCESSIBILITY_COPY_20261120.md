# SYMMETRIA — Paper One: Proposed Caption Corrections and Accessible Figure Text

**Date:** 20 November 2026 (Europe/London)  
**Status:** DOCUMENTATION-ONLY EDITORIAL DRAFT; **no change to article HTML, website PR #5, deployment or approved image binaries**.  
**Exact source:** `articles/symmetria/symmetria-paper-01.html` on `feature/v2-space-research-website`, inspected HTML Git blob `c235e33bbe3a291343125c94af73fe54a23491fa`.  
**Independent audit:** [GitHub-native seven-image scientific QA](../../../reports/V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md).  
**Rule:** Visible figure captions, concise image `alt` text, and optional longer descriptions must be editable accessible HTML, not text embedded only in the PNG. Proposals below require owner/editorial review and a future **separately authorised website PR**, not retroactive modifications to the existing site.

## Required caption corrections — exact current source and proposed copy

### Figure 2.1 — quantum theory and gravity

**Current caption, verbatim:**

> Modern physics is built upon two highly successful but fundamentally incompatible frameworks: quantum mechanics and General Relativity.

**Proposed replacement:**

> Quantum mechanics and general relativity are each highly successful in their respective domains, but a complete, experimentally established framework reconciling quantum principles with gravity remains an open research challenge.

**Reason:** `fundamentally incompatible` is too categorical for successful effective and semiclassical applications; the unresolved challenge is the complete quantum description of gravity where quantum and gravitational effects both matter. The in-image Standard Model panel separately needs to avoid claiming four-force coverage, and its Einstein equation needs a clear `Λ = 0 special case` label.

### Figure 5.1 — proposed underlying organisation

**Current caption, verbatim:**

> SYMMETRIA proposes that reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.

**Proposed replacement:**

> As an untested hypothesis, SYMMETRIA proposes that reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.

**Reason:** The image already states `Exploratory hypothesis — not established physics`, but the independent HTML caption must also explicitly say it is untested for screen-reader, search and zoom contexts.

**No other existing caption is proposed for replacement during this narrow pass.**

## Draft accessible alternatives — editorial proposals, not generated HTML changes

The `alt` suggestions are intentionally concise; they should not duplicate the full adjacent figcaption. Detailed physical relationships and equation caveats belong in the visible expandable or otherwise accessible longer descriptions.

| Slot | Suggested concise `alt` text |
|---|---|
| Cover | `Three successful approaches to modern physics frame an unresolved question about a deeper unified framework.` |
| 1.1 | `Newtonian orbits, Maxwell electromagnetic waves and Einstein curved spacetime illustrate three historical breakthroughs.` |
| 2.1 | `Standard Model particles and quantum interactions face curved relativistic spacetime across an unresolved theory gap.` |
| 3.1 | `Quantum field theory, the Standard Model and general relativity sit above open questions of quantum gravity and the dark sector.` |
| 4.1 | `Four open questions concern quantum gravity, quantum interpretation, fundamental constants and experimental tests.` |
| 5.1 | `Symmetry, information, constraint and organisation are pictured as hypothetical deeper concepts, not established mechanisms.` |
| 6.1 | `Eight proposed research steps lead from mathematical formalisation through prediction and tests, with revision if unsupported.` |

### Suggested longer explanatory HTML content by figure

**Cover:** Contemporary quantum theory, the Standard Model and general relativity each account for important phenomena. Their rich but different descriptions leave the challenge of a deeper framework unresolved. The artwork's question mark represents a research question, not a solved synthesis.

**Figure 1.1:** Newton's laws of mechanics and universal gravitation connect terrestrial and celestial motion in the same theoretical description. Maxwell united electricity and magnetism and identified light as electromagnetic. General relativity describes gravity via spacetime geometry. The displayed Einstein equation without a cosmological term is a **Λ = 0 special case**; its original formulation must not be presented as the most general field equation.

**Figure 2.1:** The Standard Model uses quantum field theory to describe electromagnetic, weak and strong interactions; **gravity is not included**. General relativity describes gravity as curved spacetime. Their complete reconciliation, especially a validated quantum treatment of gravity, remains an open scientific challenge. The displayed Einstein equation without a cosmological constant represents the **Λ = 0 special case**.

**Figure 3.1:** Quantum field theory is the mathematical framework underlying the Standard Model; the two images illustrate a general approach and one specific highly tested theory, not mutually independent forces. General relativity describes gravity and spacetime geometry. Quantum gravity remains unresolved, while the gravitational and cosmological phenomena attributed to dark matter and dark energy are modelled even though their underlying physical nature remains unknown.

**Figure 4.1:** The image asks about the quantum treatment of gravity, the measurement and interpretation of quantum theory, parameters used by physical theories, and falsifiable empirical tests. The pictured constants include dimensional quantities such as `c`, `h`, `G` and masses, as well as dimensionless `α`; their numerical values do not all have the same dependence on measurement units.

**Figure 5.1:** SYMMETRIA raises, but does not establish, the possibility that symmetry, information, constraint and organisation underlie familiar physical descriptions. The figure poses four questions and explicitly labels the proposal exploratory. No emergence law, unified-field derivation or experimental evidence is asserted.

**Figure 6.1:** The figure proposes a future research programme: formalise mathematics; check consistency; compare established physics; perform computational modelling and AI-assisted analysis; investigate through the **Nilpotent Symmetry Research Program (NSRP)**; derive distinctive testable predictions; and seek experimental evaluation. Inconclusive or contrary results should prompt revision or rejection. These steps are *planned*, not already experimentally validated.

## Website integration accessibility acceptance (later, separately authorised)

- Provide a real `<a>` or equivalently accessible control to open each original 1920×1080 image at full resolution, with keyboard access, discernible label, focus indication and touch support.
- Keep short `alt` text distinct from a detailed accessible HTML description. Do not put long mathematical explanations solely in the alt field.
- Check a 390px and 320px responsive browser with real browser rendering; the independent audit's ~356px/~286px widths were **CSS estimates**, not verified device renders.
- Keep all speculative qualifiers and `Λ = 0` caveats accessible as ordinary HTML as well as in corrected science labels.
- Do not edit `articles/symmetria/symmetria-paper-01.html` during image correction. A separate website PR and explicit integration authorisation are required.
