# SYMMETRIA — Reference-Free Discussion Paper Editorial Plan

**Date:** 17 November 2026 · **Status:** Proposed adjustments only; owner approval outstanding  
**Implementation:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Context:** Owner clarification of 17 November: **“these are just discussion papers and don't have any references. They're based on Dr Peter Rowlands Nilpotent Field Theory.”**

## 1. Editorial policy approved for planning, not yet for execution

Treat the original four SYMMETRIA documents as **exploratory discussion papers inspired by Dr Peter Rowlands' nilpotent approach to physical theory**, not peer-reviewed scientific publications or textbooks. **Do not add numbered citations, academic reference lists, footnotes, or a journal-paper apparatus to the public papers.** This direction supersedes the overly formal tone of parts of the 28-figure review.

The site may truthfully distinguish three kinds of content in ordinary prose: **established physics**, **Rowlands' proposed mathematical reformulations and wider interpretation**, and **SYMMETRIA's own exploratory possibilities**. This distinction requires no formal bibliography. The private/internal editorial evidence file may retain links to Rowlands' published work and to standard physics because that supports responsible accuracy checking, **not because the user must cite it inside the discussion papers**.

**A reference-free discussion is compatible with scientific care.** The absence of a reference list is not itself a release blocker. The remaining issues are demonstrably misleading formulas/claims, diagram-label confusion and mismatched image/caption pairings.

The current Paper 3 text **already** introduces Rowlands, describes zero-totality as an interpretation, and distinguishes nilpotence as mathematics from unvalidated unifying physical claims. Preserve this measured tone rather than imposing a research-paper rewrite.

## 2. Three small science corrections — wording for approval, not edits

| Priority | Current generated graphic | Minimal correction to the **graphic itself** (or equally conspicuous adjacent caveat, if the owner opts not to regenerate) | Why |
| --- | --- | --- | --- |
| **Essential accuracy** | Paper 2 `02_noether_symmetry_conservation.webp`: mirror/reflection and time-reversal panels say all physical laws are invariant | **Reflection (parity):** “Some interactions violate mirror symmetry.” **Time reversal:** “Time-reversal symmetry holds in some contexts, but is violated in certain particle processes.” Change heading to **“Examples of transformations and physical symmetries”**; keep Noether's theorem specifically for *continuous symmetries of the action*. If charge row is retained, phrase as **“Global phase symmetry → conserved charge (under the relevant assumptions)”**, rather than implying every arbitrary local gauge change creates a separate charge. | Parity- and T-violating processes exist. Discrete P/T should not be presented as generating the usual Noether currents. |
| **Essential algebra** | Paper 1 `01_symmetria_perspective.webp` shows `N²=0` beside `NA+AN=0` with no additional condition | Keep `N²=0`. **Remove `NA+AN=0` as a general consequence**; if retained, qualify clearly **“For specifically chosen anticommuting operators A and N: AN + NA = 0.”** No claim that self-cancellation alone yields physical emergence. | For nonzero nilpotent N, A=I gives NI+IN=2N, not zero. The extra anticommutation relation must be assumed or derived for the particular operators. |
| **Clarity, not rejection of Rowlands** | Paper 3 `03_dirac_nilpotent_structure.webp` labels a generic `N²=0` construction “mathematically equivalent” to standard Dirac theory | Prefer **“Rowlands' nilpotent formulation: a reformulation of Dirac algebra under a specified construction”**, and **“Proposed wider physical interpretation”** for claims of deeper unity. Existing conventional Dirac equation and `N²=0` can remain as schematic motifs, clearly not a proof by themselves. | Rowlands' nilpotent Dirac framework and a corresponding algebra are real published work; *generic* nilpotence is not enough to establish equivalence. This is a scope clarification, not a dismissal. |

**Do not turn these three graphics into reference-heavy expositions.** The objective is to eliminate specific mistakes/overstatements, not to demand proofs within every image. Keep the owner's dark aesthetic and conceptual visual style.

## 3. Practical image/caption reconciliation

These are **candidate revisions**, not automatic authorisation to modify protected original paper main content. All original illustrations, article words, figure numbering and seven-figure count per paper remain untouched until the owner explicitly accepts a specific swap/caption correction.

### Paper 3 — four image placements are strongly suggestive of a simple swap

| Current section / caption theme | Image currently displayed | Candidate corrected image |
| --- | --- | --- |
| Fig 1.1: symmetry and conservation leading towards nilpotence | `03_symmetry_to_nilpotence.webp` (actually shows Rowlands' three themes) | **`03_rowlands_conceptual_route.webp`** (actually shows rotation, Noether and conservation) |
| Fig 3.1: Rowlands' duality, anticommutativity, nilpotence | `03_rowlands_conceptual_route.webp` (actually shows Noether) | **`03_symmetry_to_nilpotence.webp`** |
| Fig 5.1: algebraic zero versus zero-totality versus quantum vacuum | `03_zero_totality_vacuum.webp` (actually shows future questions) | **`03_nilpotence_to_mathematics_and_reality.webp`** (actually compares these three meanings) |
| Fig 6.1: development, predictions, future questions | `03_nilpotence_to_mathematics_and_reality.webp` (actually compares three meanings of zero) | **`03_zero_totality_vacuum.webp`** |

**Preferred method if approved:** swap the four relevant HTML `img src` references and update their alt text appropriately; keep existing file names, captions and image binaries unchanged. Before doing so, **confirm the immediately adjacent paragraph** still matches. Since these swaps modify protected paper main blocks, establish a new owner-approved integrity baseline and rerun the exact-site regression. No changes to research theories.

### Paper 2 — short descriptive captions may suffice

| Figure | Actual image topic | Suggested caption direction (not final wording) |
| --- | --- | --- |
| 1.1 | “The Problem: Fragmented Theories, Unanswered Questions” | The unresolved relationship between quantum particle physics and gravitation motivates a search for deeper symmetry principles. |
| 2.1 | “The Vision of Unification” | A speculative visual of a common mathematical description across quantum and cosmic scales. |
| 3.1 | “Symmetry in Nature” (snowflakes, crystals, biology and spiral galaxies) | Visual patterns illustrate approximate symmetry in nature; mathematical invariance of physical laws is a more precise concept. |
| 5.1 | “Symmetry in Action” (various patterns and laws, **not** an actual symmetry-breaking demonstration) | Present as examples of symmetry; **prefer a new broken-symmetry graphic** if this figure needs to explain phase transitions specifically. |
| 6.1 | “Why a New Unified Framework?” | The unification problem and the **hypothetical**, symmetry-first research direction of SYMMETRIA. |

The caption can be accurate while the image remains unchanged, provided its place in the surrounding section stays coherent. Avoid attempting a blind renaming/swap in Paper 2 without reading each section.

### Paper 4 — image/caption scope adjustments

- **Figure 3.1:** image is “Symmetry, conservation and deeper structure”, a concrete example of the *symmetry aspect* of elegance — its current caption lists broader features (economy/coherence/explanatory reach). Reword the caption to frame it as one example rather than a comprehensive summary.
- **Figure 4.1:** image titled “The bigger picture” illustrates speculative nilpotence applications to quantum theory, spacetime and cosmology; caption should say these are **possible applications needing evidence**, not imply the graphic already explains the general logic of theoretical elegance.
- **Cover:** visually decorative integral symbol beside Euler's identity looks like malformed mathematics. **Optional correction** if retained as educational notation; this is a secondary refinement, not a reason to demand citations.

### Paper 1 and remaining figures

The earlier 28-image report lists additional wording and scientific-status cautions. They are **not each a release-blocking defect** merely because they are conceptual or lack references. Prioritise objectively misleading universal statements, unjustified mathematical implications and text/image alignment.

## 4. No references in the discussion papers — internal background only

The project team may consult background material for accuracy without citing it publicly. Rowlands' nilpotent Dirac work, including the 2014 review and the 2017 Marcer/Rowlands paper, describes a specific algebraic reformulation and proposed interpretation; it does not establish that an arbitrary nilpotent expression unifies fundamental interactions. The team's internal review also uses established discrete-symmetry experimental results. **These sources are editorial checking aids only, not a required bibliography.**

- Rowlands, “Nilpotent quantum theory: a review” (2014): https://webbut.unitbv.ro/index.php/Series_III/article/view/1967
- Marcer and Rowlands, “Nilpotent Quantum Mechanics: Analogs and Applications” (2017): https://livrepository.liverpool.ac.uk/3033274/
- Rowlands/Cullerne, “The Dirac algebra and its physical interpretation” (2000): https://arxiv.org/abs/quant-ph/0010094

## 5. Guardrails and next decision

**Now:** planning documents only. No changes to the 28 image files, website HTML, original paper main bodies, citations, footer, or captions. PR #5 remains draft; no merge/deployment.

**Upon explicit owner approval of the correction plan:** create the smallest editorial change-set on the existing feature branch, keep an archive/trace of original images, rebaseline the exact protected paper sections under owner approval and run full browser/regression and relevant accessibility checks. Preserve “discussion papers” rather than relabelling as peer-reviewed publications.

**Scientific outcome:** This reframes the internal findings as **proportionate accuracy edits for Rowlands-inspired discussion papers**, not a demand to add academic references or substantiate an entirely new theory before they can be discussed.
