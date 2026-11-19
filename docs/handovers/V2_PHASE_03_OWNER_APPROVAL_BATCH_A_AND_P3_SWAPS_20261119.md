# Phase 3 — Owner Approval Package: Scientific Corrections + Paper 3 Figure Alignment

**19 November 2026 · Version 1.0 · Proposed — NOT implementation approval**  
**Exact current implementation source SHA:** `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`  
**Source branch:** `feature/v2-space-research-website` / [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Planning branch:** `planning/space-first-research-website-20261116` / [draft PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)  
**Scientific evidence:** the 28-figure Work report in the owner's personal Library (not copied into this public repo); [Chat Stream A blueprints](../reports/V2_PHASE_03_CHAT_STREAM_A_CONTROLLED_FIGURE_BLUEPRINTS_20261118.md), [28-figure owner decision register](../reports/V2_PHASE_03_CHAT_WORK_RECONCILIATION_AND_OWNER_GATE_20261118.md).  
**Purpose:** present the smallest exact change-set for **explicit owner approval** before changing any paper HTML or scientific figure. Agreement to continue planning alone does not authorise publishing.

## A. Embedded scientific claims — four proposed replacements

All original WebP files remain in Git history and on disk. New approved assets, where needed, will use versioned filenames so direct image URLs can still refer to the originals.

### A1 · Paper 1 Fig 3.1 — Standard Model statement
- Original: `images/symmetria/paper-01/01_search_for_unification.webp`; blob SHA `c6ca2f610595cd6eb2677eeae26885c80577ac0a`.
- Defect inside source image: **“Unifies electromagnetic, weak and strong forces.”**
- Exact proposed replacement text in its *Standard Model* panel: **“Describes electromagnetic, weak and strong interactions. Electroweak theory unifies electromagnetic and weak interactions.”**
- Leave separate grand-unified-theory proposals clearly labelled as **proposals**, not completed Standard Model results. Retain existing art where possible.
- Proposed output: `images/symmetria/paper-01/01_search_for_unification_corrected_v2.webp`.
- Proposed accessible alt: **“Modern physics and the search for unification, distinguishing the Standard Model from proposed grand unified theories”**.
- Existing Figure 3.1 caption is thematically adequate; **no caption change proposed** unless review exposes a direct conflict.
- Internal technical background only: [CERN Standard Model](https://home.cern/science/physics/standard-model/), [CERN unified forces](https://home.cern/science/physics/unified-forces).

### A2 · Paper 1 Fig 5.1 — independent anticommutation condition
- Original: `images/symmetria/paper-01/01_symmetria_perspective.webp`; blob SHA `b0334e5aa0c42dd0463b3810689502f43fae680b`.
- Defect: side-by-side **`N²=0`** and **`NA+AN=0`** presented as if the second automatically follows from the first. An unqualified claim of nilpotent balance as the actual origin of physical reality is also premature.
- **Preferred minimal mathematically safe choice:** keep a clearly defined **`N ≠ 0, N² = 0`** as an algebraic example but **omit `NA+AN=0`** altogether unless a specific second operator and independent anticommutation assumption are explained. Never draw a consequence arrow from `N²=0` to universal physical emergence.
- Proposed heading: **“SYMMETRIA: AN EXPLORATORY PERSPECTIVE”**.
- Proposed in-image note: **“Proposed connections to physical reality require a defined model and testable consequences.”**
- Conditional optional separate fact if owner requests it: **“For specifically defined anticommuting operators A and N, AN + NA = 0; this is an additional relation.”**
- Proposed output: `images/symmetria/paper-01/01_symmetria_perspective_corrected_v2.webp`.
- Proposed alt: **“Exploratory SYMMETRIA perspective illustrating nilpotence as an algebraic condition, with proposed physical interpretations marked as hypotheses”**.
- Current Figure 5.1 caption already uses cautious “proposes/may” language; **retain** unless owner chooses a narrower revision.
- Internal arithmetic check: for nonzero square-zero N over real/complex matrices, choosing A=I gives AN+NA=2N ≠ 0.

### A3 · Paper 2 Fig 4.1 — Noether, parity and T symmetry
- Original: `images/symmetria/paper-02/02_noether_symmetry_conservation.webp`; blob SHA `66d7ba1ca508f4f54457e922a5b5fdc1085ca9f4`.
- Defect: unqualified “laws are the same” under mirror/parity and reversal of time; direct **“Gauge Symmetry → Conservation of Charge”** oversimplifies the role of global phase symmetry vs local gauge redundancy.
- Proposed compact replacement image sections:
  1. **Continuous symmetries of the action (under relevant conditions):** time translation → energy; space translation → momentum; continuous rotation → angular momentum.
  2. **Global phase symmetry:** relates to charge conservation **under the relevant assumptions**. **Local gauge transformations:** redundancy of description; not a separate physical charge conservation law for every arbitrary local choice.
  3. **Discrete symmetry exceptions:** **“Some weak interactions violate parity (P).”** **“Certain particle processes violate time-reversal symmetry (T).”**
  4. **“Physical symmetries help organise and constrain models. Experiments determine their applicability.”**
- Do not conflate discrete P/T with Noether's *continuous* symmetry statement; do not imply symmetry alone establishes a specific particle discovery.
- Proposed output: `images/symmetria/paper-02/02_noether_symmetry_conservation_corrected_v2.webp`.
- Proposed alt: **“Continuous Noether symmetries and conservation, contrasted with measured parity and time-reversal symmetry violations”**.
- Existing Figure 4.1 caption correctly specifies continuous symmetries; **retain**.
- Internal verification only: [APS P/T](https://physics.aps.org/articles/v5/129), [Cambridge Noether notes](https://www.damtp.cam.ac.uk/user/tong/qft/qfthtml/S1.html).

### A4 · Paper 3 Fig 4.1 — Rowlands nilpotent Dirac correspondence
- Original: `images/symmetria/paper-03/03_dirac_nilpotent_structure.webp`; blob SHA `e2ef7767f8f77127d67f6732ce7b58656996c0c6`.
- Defect: generic **`N²=0`** is visually adjacent to an unrestricted claim of mathematical equivalence to the standard Dirac structure, with no stated conditions.
- Minimal revised panel headline: **“A SPECIFIED NILPOTENT DIRAC REFORMULATION”**.
- Exact draft in-image qualification: **“Within Rowlands’ specified algebraic construction, a correspondence with Dirac gamma-matrix algebra has been described. The condition N² = 0 alone does not establish that correspondence.”**
- Relabel wider foundational implications **“Possible interpretation — not an experimentally demonstrated new theory.”**
- If the standard Dirac expression is retained, typeset it **from controlled mathematical text**, not by asking image generation to invent symbols, and check conventions before display.
- Proposed output: `images/symmetria/paper-03/03_dirac_nilpotent_structure_corrected_v2.webp`.
- Proposed alt: **“Schematic of Dirac theory and a specified Rowlands nilpotent algebraic reformulation, with assumptions and untested interpretations distinguished”**.
- Existing Figure 4.1 caption is already suitably cautious; **retain**.
- Internal evidence only: [Marcer and Rowlands 2017](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2017.00028/full).

**These four substitutions correct *image-embedded* statements. An extra HTML caption alone is insufficient because the Phase 2 viewer permits independent sharing and enlargement. No figure has yet been regenerated.**

## B. Paper 3 swaps — exact authorised change proposal (no binaries regenerated)

All four paper images remain physically unchanged; exactly **four** `<img>` references in `articles/symmetria/symmetria-paper-03.html` would be updated, together with all four descriptive alt values.

| Figure position | Current src filename | Proposed src filename | Exact new alt |
| --- | --- | --- | --- |
| **1.1** | `03_symmetry_to_nilpotence.webp` | `03_rowlands_conceptual_route.webp` | `Rotation symmetry and angular momentum conservation illustrating continuous physical symmetry` |
| **3.1** | `03_rowlands_conceptual_route.webp` | `03_symmetry_to_nilpotence.webp` | `Rowlands-inspired themes of duality, anticommutativity and nilpotent structure` |
| **5.1** | `03_zero_totality_vacuum.webp` | `03_nilpotence_to_mathematics_and_reality.webp` | `Comparison of algebraic zero, zero-totality and the quantum-field vacuum` |
| **6.1** | `03_nilpotence_to_mathematics_and_reality.webp` | `03_zero_totality_vacuum.webp` | `Open questions, mathematical development, predictions and experimental tests for nilpotent approaches` |

**Optional but recommended Figure 1.1 caption refinement** to match a rotation/Noether image, pending owner approval:
> **Figure 1.1:** Continuous symmetry can connect a transformation of a physical system with a conserved quantity. Rotation and angular momentum provide an established example, motivating investigation of deeper mathematical relationships. This example alone does not establish nilpotence.

**Figure 3.1 caption:** The existing one names Rowlands' duality/anticommutativity/nilpotence and becomes more fitting after the swap; retain as written.

**Figures 5.1 and 6.1 captions:** Existing wording aligns much better with the proposed exchanged images; retain as written, provided the adjacent section review finds no newly introduced contradiction.

**Check:** after swapping, each figure remains in the same document section, and the 7-per-paper count and corresponding image labels still hold. All four image files remain on the original paths for direct linking. Article integrity fixtures must be adjusted for **these four exact substitutions only**; no broad bypass.

## C. Paper 4 Fig 4.1 — owner preference required

**Original:** `images/symmetria/paper-04/04_elegance_requires_empirical_test.webp` (SHA `54d86da3e6878f5a219dfa7a9eb7ed98399f5871`). The graphic **“The bigger picture”** actually depicts proposed nilpotence applications across mathematical physics and cosmology. The adjacent section, **“When Beautiful Mathematics Is Not Enough”**, stresses comparison with observations.

Choose **one**:
- **C1 · Minimum changes:** keep the old image and re-caption as *proposed, unverified research directions*, acknowledging it illustrates the research landscape rather than the section's main lesson.
- **C2 · Recommended educational change:** replace it with a controlled, explicitly schematic **“ELEGANCE IS NOT EVIDENCE”** diagram: define mathematics → check consistency → derive distinct quantitative consequences → compare with observations → revise/reject/provisionally retain. Proposed output `04_elegance_requires_empirical_test_corrected_v2.webp` and alt `Conceptual pathway distinguishing mathematical elegance from testable physical evidence`. Keep the existing cautious Figure 4.1 HTML caption.

## D. Paper 2 Fig 5.1 — optional separate owner choice

Original `02_broken_symmetry_emergence.webp` illustrates broad examples of symmetry, but its section and caption are explicitly about broken symmetry. **Recommend a new controlled symmetry-breaking example (e.g., a schematic ferromagnet above/below the Curie transition) only if the owner wants that illustrative teaching purpose.** Otherwise a truthful short re-caption and deferral are proportionate. No image production until chosen.

## E. Approval decisions and non-negotiable boundaries

| Approval option | Scope | Recommendation |
| --- | --- | --- |
| **A** | Produce **four** scientifically corrected, versioned original-figure replacements for P1 Figs 3.1/5.1, P2 Fig 4.1, P3 Fig 4.1 | **Approve**, with exact text and image-by-image owner preview |
| **B** | Swap **two pairs** of Paper 3 figure references/alt as above, plus optionally refined P3 Fig 1.1 caption | **Approve** |
| **C** | Paper 4 Fig 4.1: C1 recaption versus C2 purpose-built replacement | **Prefer C2** |
| **D** | Paper 2 Fig 5.1: defer, re-caption, or replace with a true broken-symmetry teaching figure | **Prefer defer until A/B/C proof reviewed** |
| **E** | Other medium/low issue wording, separate batch | **Defer for now** |

**No consent inferred from a general “continue” on previous planning work.** Owner must explicitly confirm the A/B/C/D choices before the corresponding scientific image or protected HTML edits. Approval for producing an image proof is **not** approval to publish or merge.

## F. Implementation and test harness constraints

The verified baseline's `docs/reports/scripts/v2_stage8_qa.py` uses an exact-match integrity baseline: it compares each paper's `<main>` with the immutable `origin/main` body after normalising the approved old return-navigation section, and requires the original seven `src` files in order. **It will correctly fail if Phase 3 edits are made without amending the owner's exact approved delta fixture.** Do not disable it or replace it with a weaker count-only assertion. Instead, take an immutable copy of the expected baseline, apply only the owner-authorised `img src`, `alt` and caption transformations to the expected string, and keep a strict equality check on the entire result, plus seven-figure and approved-asset assertions. Record approved change-set paths, old/new values and source SHA. Verify no changes to other article text.

After owner approval and figure proof review, implement on `feature/v2-space-research-website`, not on `main`. Run **exact-commit** full site regression; check image integrity, source availability, browser tests 320/390/768/1440/1920px+, sticky navigation, and all new independent viewer actions (click/tap/keyboard, wheel zoom, drag-pan, Fit/100%, touch pinch simulation, landscape). Check WebP typography at desktop fit, 100% original and magnified zoom. Preserve original seven figures per paper, four URLs and rollback path. Keep PR #5 draft, unmerged and unpublished.

## G. Next action

Present this finite package to the owner. Upon explicit choice of **A / B / C / D**, prepare selected replacement proofs **without substituting them into the four papers yet**; get visual approval on each proof before a source change. Do not silently expand the scope.
