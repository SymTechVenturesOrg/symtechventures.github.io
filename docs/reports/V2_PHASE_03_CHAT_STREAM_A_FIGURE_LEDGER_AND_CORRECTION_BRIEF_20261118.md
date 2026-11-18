# Phase 3 — Stream A source ledger and scientific correction briefs (Chat)

**Prepared:** 18 November 2026 GMT  
**State:** **READ-ONLY PLANNING; Work independent review pending; no figure edits approved**  
**Exact inspected implementation source commit:** `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` on `feature/v2-space-research-website`  
**Implementation PR:** [#5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5) (unmerged/draft)  
**Planning PR:** [#2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)  
**Parent workplan:** [Chat + Work parallel Phase 3](../V2_PHASE_03_CHAT_WORK_PARALLEL_WORKPLAN_20261118.md)

## 1. Provenance and status of this inventory

This ledger is **extracted from the actual four source HTML papers and Git tree** at the exact SHA above, rather than inferred from filenames alone. Each row below captures the placed image file, sequential figure number, a **shortened excerpt of the actual immediately following HTML caption**, and its first 12 Git-blob SHA characters for preservation checks. The full captions, original alt text and complete Git blob SHA identifiers remain authoritative in the inspected original HTML and Git tree; this ledger intentionally abridges the caption text and SHA prefix for review. All **28/28 image links resolve to tracked WebP assets**, all **28/28 have non-empty adjacent figure captions and alt text**, and exactly seven figures occur per existing paper.

**Important limitation:** The triage suggestions below derive from the **17 November full visual review** and the source text, rather than a new pixel-by-pixel image audit performed in this specific pass. Work's independent visual inspection is deliberately still pending. The label **REDRAW** is a **provisional proposed disposition**, **not approval** to generate or substitute graphics. No fact reported as visual should be inferred from an image filename alone.

## 2. Complete 28-figure placement, caption and rollback ledger

| Paper | Figure | Exact placed image filename | Current adjacent caption (abridged) | Provisional editorial handling | Git blob ID prefix |
|---:|---|---|---|---|---|
| 1 | Cover | `01_unified_framework_cover.webp` | Cover Illustration: Modern physics has achieved extraordinary success, yet several fundamental questions re... | KEEP | `6a8aaa0edb49` |
| 1 | 1.1 | `01_historical_progression_physics.webp` | Figure 1.1: Throughout history, physics has repeatedly advanced through the discovery of deeper unifying pr... | KEEP+QUALIFY | `b1534d926dc3` |
| 1 | 2.1 | `01_modern_physics_challenges.webp` | Figure 2.1: Modern physics is built upon two highly successful but fundamentally incompatible frameworks: q... | KEEP+QUALIFY | `cb8a575c186a` |
| 1 | 3.1 | `01_search_for_unification.webp` | Figure 3.1: Modern physics seeks to explain nature through a combination of quantum field theories, particl... | KEEP+QUALIFY | `c6ca2f610595` |
| 1 | 4.1 | `01_current_physics_limitations.webp` | Figure 4.1: Modern physics has achieved extraordinary success, yet unresolved questions concerning unificat... | KEEP+QUALIFY | `ea947f864462` |
| 1 | 5.1 | `01_symmetria_perspective.webp` | Figure 5.1: SYMMETRIA proposes that reality may emerge from deeper layers of symmetry, information, constra... | REDRAW (priority) | `b0334e5aa0c4` |
| 1 | 6.1 | `01_future_research_roadmap.webp` | Figure 6.1: The future development of SYMMETRIA is expected to proceed through a series of increasingly rig... | KEEP+QUALIFY | `5acb11e9579b` |
| 2 | Cover | `02_symmetry_cover.webp` | Cover Illustration: Symmetry appears throughout nature, mathematics and physics. From snowflakes and crysta... | KEEP | `376eb4bcd148` |
| 2 | 1.1 | `02_symmetry_nature_physics.webp` | Figure 1.1: Symmetry appears across many levels of reality, from biological forms and crystalline structure... | RECAPTION | `927a73426881` |
| 2 | 2.1 | `02_natural_symmetry_patterns.webp` | Figure 2.1: Natural symmetry appears in snowflakes, crystals, biological forms, shells, bubbles and galaxie... | RECAPTION | `4abb539e9763` |
| 2 | 3.1 | `02_mathematical_symmetry_invariance.webp` | Figure 3.1: In mathematics and physics, symmetry means invariance under transformation. A law or structure ... | RECAPTION | `7cbc8f64a80f` |
| 2 | 4.1 | `02_noether_symmetry_conservation.webp` | Figure 4.1: Noether's theorem links continuous symmetries to conservation laws. Time symmetry corresponds t... | REDRAW (priority) | `66d7ba1ca508` |
| 2 | 5.1 | `02_broken_symmetry_emergence.webp` | Figure 5.1: Broken symmetry allows structure to emerge from initially balanced conditions. In physics, phas... | RECAPTION or REDRAW | `bd9fc5255a88` |
| 2 | 6.1 | `02_symmetria_symmetry_perspective.webp` | Figure 6.1: The SYMMETRIA perspective explores whether particles, forces, spacetime and physical laws may e... | RECAPTION+QUALIFY | `6cece5b6bd50` |
| 3 | Cover | `03_nilpotent_foundation_cover.webp` | Cover Illustration: Nilpotence asks whether structured physical relationships can be organised by algebraic... | KEEP | `e7a798306602` |
| 3 | 1.1 | `03_symmetry_to_nilpotence.webp` | Figure 1.1: Symmetry and conservation suggest that apparently separate physical quantities can be linked by... | SWAP CANDIDATE →3.1 | `65f0e06443dc` |
| 3 | 2.1 | `03_nilpotence_intuition.webp` | Figure 2.1: A nilpotent object is not simply nothing. It can contain structure, relationships and informati... | KEEP+QUALIFY | `c4be1898adac` |
| 3 | 3.1 | `03_rowlands_conceptual_route.webp` | Figure 3.1: Peter Rowlands' programme explores whether duality, anticommutativity and nilpotent structure c... | SWAP CANDIDATE →1.1 | `d42ebe55559e` |
| 3 | 4.1 | `03_dirac_nilpotent_structure.webp` | Figure 4.1: The nilpotent approach reorganises aspects of relativistic Dirac structure into an algebraic fo... | REDRAW (priority) | `e2ef7767f8f7` |
| 3 | 5.1 | `03_zero_totality_vacuum.webp` | Figure 5.1: Algebraic zero, Rowlands' idea of zero-totality and the quantum-field vacuum occupy related con... | SWAP CANDIDATE →6.1 | `65211b292dc4` |
| 3 | 6.1 | `03_nilpotence_to_mathematics_and_reality.webp` | Figure 6.1: Nilpotence offers a structured set of questions about balance, complementarity and physical org... | SWAP CANDIDATE →5.1 | `6068f0c6f7e4` |
| 4 | Cover | `04_mathematics_elegance_reality_cover.webp` | Cover Illustration: Mathematical structure can illuminate the physical world with remarkable power, but ele... | KEEP+QUALIFY | `84a1465c632d` |
| 4 | 1.1 | `04_mathematics_and_evidence_pathways.webp` | Figure 1.1: Mathematics can describe an enormous landscape of possible structures, relationships and symmet... | KEEP | `2da6a33e0bbe` |
| 4 | 2.1 | `04_mathematics_to_physical_consequences.webp` | Figure 2.1: Mathematical frameworks become physically powerful when their internal relationships generate c... | KEEP | `9de868bd39d0` |
| 4 | 3.1 | `04_components_of_theoretical_elegance.webp` | Figure 3.1: In physics, elegance usually reflects several connected qualities, including economy, symmetry,... | RECAPTION | `b6c0e79acb40` |
| 4 | 4.1 | `04_elegance_requires_empirical_test.webp` | Figure 4.1: Many mathematically coherent possibilities can exist simultaneously, including structures that ... | RECAPTION | `54d86da3e687` |
| 4 | 5.1 | `04_symmetria_research_obligations.webp` | Figure 5.1: An exploratory framework becomes scientifically stronger by progressing from clear mathematics ... | KEEP | `2232092aca8e` |
| 4 | 6.1 | `04_mathematical_structure_to_emergence.webp` | Figure 6.1: The deeper question is not only whether mathematics captures fundamental physical structure, bu... | KEEP+QUALIFY | `8caf3072eeed` |

**Figure-number convention:** one cover plus Figures 1.1–6.1 for each paper. All SHA prefixes refer to **the existing original image bytes**, not revised versions. The precise full paths are `images/symmetria/paper-0X/<filename>`, where X matches the paper number. The exact original alt text and complete captions must be retained in the implementation snapshot and checked against any approved changes; do **not** replace them with the shortened descriptions in this ledger.

## 3. Three scientifically necessary correction specifications

### A1 — Paper 1, Figure 5.1: nilpotence versus anticommutation

**Original WebP:** `images/symmetria/paper-01/01_symmetria_perspective.webp`; original full blob SHA `b0334e5aa0c42dd0463b3810689502f43fae680b`.

The existing 17 November visual review reports that the figure juxtaposes `N² = 0` and `NA + AN = 0` as though the latter follows universally. **It does not.** Counterexample over ordinary matrices: `N = [[0,1],[0,0]]`, `A = I`; `N² = 0` but `AN+NA = 2N ≠ 0`.

**Preferred minimal correction in the graphic:** preserve the nilpotence definition `N² = 0`; **remove any unqualified `AN+NA=0` derived-from-nilpotence arrow**. If an anticommutator is needed, state explicitly, *“For separately specified anticommuting operators A and N, AN + NA = 0.”* Do not imply algebraic cancellation alone establishes emergence, information dynamics or cosmology.

**Acceptance:** verified mathematical notation rendered from controlled text/vector, unchanged surrounding exploratory caption unless a specific mismatch remains; full original WebP preserved with a source hash. A new asset requires owner approval.

### A2 — Paper 2, Figure 4.1: Noether and violated discrete symmetries

**Original:** `images/symmetria/paper-02/02_noether_symmetry_conservation.webp`; full SHA `66d7ba1ca508f4f54457e922a5b5fdc1085ca9f4`.

The earlier visual review reports **incorrectly universal** mirror/parity and time-reversal panels; the actual adjacent HTML caption already correctly says Noether's theorem concerns **continuous symmetries**. Correct the graphic **itself** because its new-tab full-resolution viewer can display it without the caption.

**Proposed controlled-label wording:**
- *Continuous time-translation symmetry → energy conservation* (subject to the usual conditions).
- *Continuous spatial translations → momentum conservation*.
- *Continuous rotations → angular momentum conservation*.
- *Some weak processes violate parity (mirror symmetry).*
- *Time-reversal symmetry is violated in certain particle processes.*
- If included: *Global phase symmetry → conserved charge (under relevant assumptions)*; do not mistake arbitrary local gauge redundancy for a separate independent conservation law per transformation.

Distinguish **discrete examples** from the continuous transformations used in Noether's first theorem. Avoid claiming every process is invariant under reflection or time reversal. References for **internal verification only**, not for insertion into public reference-free discussions: [D. Tong, QFT Noether notes](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S1.html), [CERN parity tests](https://cern-courier.web.cern.ch/a/recent-isolde-results-revisit-parity-violation/), [CERN time-reversal asymmetry](https://home.cern/times-arrow-particles-cannot-go-back-to-the-future/).

### A3 — Paper 3, Figure 4.1: Rowlands' specified algebra versus generic nilpotence

**Original:** `images/symmetria/paper-03/03_dirac_nilpotent_structure.webp`; SHA `e2ef7767f8f77127d67f6732ce7b58656996c0c6`.

The existing review reports a `N²=0` panel claiming mathematical equivalence with the conventional Dirac formulation without showing the **specific algebraic assumptions**. The current paper text and caption **already** distinguish a meaningful Rowlands–Dirac algebraic connection from unverified interpretation; preserve that caution.

**Minimal graphic text:** *“Within Rowlands' specified nilpotent Dirac construction, an algebraic reformulation/correspondence with the standard Dirac algebra is described.”* Label displayed `N²=0` as a **schematic nilpotency condition**, not a proof of generic equivalence. Set any stronger unifying or ontological claims apart as **proposed interpretation**, not an experimentally established result.

**Internal evidence only:** [Marcer & Rowlands 2017](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2017.00028/full) discusses an explicitly structured algebra isomorphic to the gamma matrix algebra. The historical literature supports studying a specific construction; it does **not** validate the entire SYMMETRIA hypothesis.

### Quality bar for all three

Prepare **editable, controlled mathematical text/geometry first**, then generate or render the chosen scientific infographic only after owner approval. A text prompt to image generation alone is unreliable for exact formulae. Prefer verified maths layers, labelled figure panels, consistent dark palette and evidence-qualified conceptual language. Preserve original WebPs as immutable versioned assets for rollback.

## 4. Candidate image/caption alignment actions — NOT YET APPROVED

**Paper 3 (high-confidence candidates from earlier visual review, check adjacent actual paragraph before swapping):**

| Existing figure | Current placed asset | Candidate corrected asset |
| --- | --- | --- |
| 1.1 (symmetry and conservation toward nilpotence) | `03_symmetry_to_nilpotence.webp` | `03_rowlands_conceptual_route.webp` |
| 3.1 (Rowlands duality/anticommutativity/nilpotence) | `03_rowlands_conceptual_route.webp` | `03_symmetry_to_nilpotence.webp` |
| 5.1 (three distinct senses of zero) | `03_zero_totality_vacuum.webp` | `03_nilpotence_to_mathematics_and_reality.webp` |
| 6.1 (future research and testable predictions) | `03_nilpotence_to_mathematics_and_reality.webp` | `03_zero_totality_vacuum.webp` |

These are potential **two pairs of source swaps**, not asset modifications. Correct source paths and image alt text together if approved; do not blindly change the original captions, which are currently focused on their respective sections. After any swap, inspect the exact paragraph immediately before and after each figure.

**Paper 2:** Figures **1.1, 2.1, 3.1, 5.1, 6.1** have earlier-reported content-versus-caption mismatches. Minimal precise recaptioning may suffice for most; **Figure 5.1** could warrant a new graphic only if the teaching purpose truly requires illustrating broken symmetry.

**Paper 4:** Figures **3.1, 4.1** have earlier-reported content/caption topic gaps; precise caption revisions are preferred over broad redraws. The cover's decorative standalone integral glyph is a **secondary** optional typography issue.

## 5. GitHub implementation safety plan for the post-Work, post-owner gate

1. Freeze original paper HTML blob SHAs and every image's full Git SHA/bytes from the pinned source; rerun the complete ledger extraction at the current source HEAD before making changes.
2. Merge independent **Work evidence** into a 28-row decision matrix; mark AGREED, DISPUTED or UNVERIFIED, then obtain owner's **explicit approval for each correction category or exact file change-set**.
3. Commit **new versioned replacement assets** under clear figure names; never overwrite all 28 originals. Save exact text/equations, generation provenance, licence status, output pixel sizes, WebP encoder quality setting (nominal 80 if suitable), and source/file SHA.
4. Only then modify the approved `<img src>`, `alt` and corresponding `figure-caption` portions in the **four protected paper main blocks**. Keep all paper URLs, seven images per paper and publication classifications unchanged. Update the regression's protected original-body baseline **only for those approved precise edits**, not by removing its integrity checks.
5. On the **exact final implementation commit**, run `python3 -u docs/reports/scripts/v2_stage8_qa.py` and relevant browser/accessibility suite. Test 320, 390, 768, 1440 and 1920px, sticky header, no overflow, keyboard access, `pages/figure-viewer.html` with new image sources, wheel/pan/pinch and controlled equation readability when enlarged.
6. Provide before/after screenshots and an explicit per-figure rollback map. **Do not merge PR #5 or publish**, and do not create new formal publications or bibliographies.

## 6. Next gate

**Stream A status:** initial source ledger + three draft science briefs complete; no files changed on implementation branch. **Stream B:** Work independently reviews the same pinned files and returns its own read-only 28-row report. Reconciliation and owner approval are still pending; the provisional triage table does **not** constitute authorisation to correct or regenerate images.
