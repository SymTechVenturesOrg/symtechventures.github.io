# Phase 3 — Five Scientific Replacement Figure Proofs (owner review pending)

**19 November 2026 · Review-only deliverable · No article or figure substitution performed.**

## Approval and scope

Owner approved **A** (four image-embedded scientific corrections), **B** (Paper 3 Figures 1.1↔3.1 and 5.1↔6.1 swaps), **C2** (new Paper 4 Fig. 4.1 explaining evidence), and **D deferred** (no new Paper 2 Fig. 5.1). The preceding owner-approval package is [here](../handovers/V2_PHASE_03_OWNER_APPROVAL_BATCH_A_AND_P3_SWAPS_20261119.md).

This pass produced **five new 1536×1024 review images**, each in editable SVG plus PNG and high-quality WebP, with the original source image included alongside for comparison. A responsive self-contained `index.html` gallery also includes the four **Paper 3 swap-placement comparisons**. The ZIP and an original-vs-revised contact sheet were delivered to the owner in the **19 November 2026 Chat conversation**; the unpublished proof binaries are **not** committed into the website repository until the owner approves the visuals. The source generator and original-image checksums are contained in the ZIP.

**Implementation baseline:** `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` (draft PR #5). **No change to its original images, four paper HTML bodies, figure counts, refs, CSS or JS.** Planning PR #2 remains draft.

## Original-to-proposed mapping and QA hashes

| Paper figure | Original source asset | Proposed versioned WebP proof | Rendered WebP SHA-256 |
|---|---|---|---|
| P1 Fig 3.1 | `01_search_for_unification.webp` | `01_search_for_unification_corrected_v2.webp` | `1a97dad90e952cee85fbd4ed80f830aa5c133272906e2b465a4aa2c3e5e4de28` |
| P1 Fig 5.1 | `01_symmetria_perspective.webp` | `01_symmetria_perspective_corrected_v2.webp` | `a769c7a36ee9e38ba29f909078bcce2e9e63c384913b4605f197ee605d1c9c3e` |
| P2 Fig 4.1 | `02_noether_symmetry_conservation.webp` | `02_noether_symmetry_conservation_corrected_v2.webp` | `0d5796a83674105fdcb2e4e4a24f3fa7300b1b185476cfec2aa2fc0fbf4e2b6e` |
| P3 Fig 4.1 | `03_dirac_nilpotent_structure.webp` | `03_dirac_nilpotent_structure_corrected_v2.webp` | `9629fd6bf940d738e6cecb1ef3a86b8d27ffdc1333191b8211564e7f9da50b0a` |
| P4 Fig 4.1 | `04_elegance_requires_empirical_test.webp` | `04_elegance_requires_empirical_test_corrected_v2.webp` | `f240dbd583a5c6140904a8e191c1d0c4d11e828ba01ecc78c7bd9d2bfb78600f` |

## Content differences (what the owner will see)

- **P1 3.1:** correctly separates what the Standard Model describes from electroweak unification and proposed grand unification; does not pretend that it includes gravitation.
- **P1 5.1:** keeps `N ≠ 0, N²=0` as a precise algebraic definition; removes unqualified `NA + AN=0` and marks proposed physical emergence as unresolved.
- **P2 4.1:** distinguishes continuous Noether action symmetries from known parity/time-reversal violations and local gauge redundancy.
- **P3 4.1:** distinguishes a specified Rowlands Dirac-algebra reformulation in published literature from arbitrary nilpotence or new experimental validation.
- **P4 4.1:** replaces unrelated speculative nilpotence applications with a staged process from a defined model through quantitative consequences to empirical testing.

The edited vector artwork has a consistent restrained navy-and-cyan/gold aesthetic, fully controlled live SVG text (no image-model-generated equations), accessible caption/alt candidates in the owner approval package, and the same original pixel dimensions.

## Review package / checks

The owner received `SymTech_Phase3_Five_Figure_Proofs_and_Paper3_Swaps.zip` with **33 validated entries**, approximately **5.79MB**, package SHA-256 `5d20ba37e9c9c0544b3c9fb25aed2d73c93cc6b56966966e8638b9eff6517231`, containing:
- `index.html` visual side-by-side gallery;
- five edited `svg/`, `png/`, and `webp/` assets;
- nine unchanged original WebP image sources (five replaced-figure comparisons plus four Paper 3 swap sources);
- `Phase3_Five_Figures_Before_After.jpg` comparison sheet;
- `README.md`, generators, original hash manifest and machine-readable QA report.

**Static QA PASS:** all nine original image SHA sources matched pinned Git blob IDs; the five WebP output dimensions were 1536×1024; SVG text element bounds were within the canvas; selected misleading original text was absent from the new SVG; ZIP CRC integrity was good; versioned filenames match the existing full-resolution viewer's allowed path pattern. **Local interactive Chromium gallery QA was blocked** by `net::ERR_BLOCKED_BY_ADMINISTRATOR` and is **not claimed to have passed** in this run. Physical-owner browser acceptance and final scientific editorial visual proof approval remain required.

## Remaining gates (not yet authorised)

1. Owner visually reviews the five figures, compares their design to original branding, and decides to **accept or request adjustments to each proof**.
2. After visual acceptance, integrate approved *versioned* assets and only the exact authorised `img src`, `alt` and Paper 3 swap/caption changes into feature PR #5, with strict protected-main-block QA expectations updated only by specific deltas. Original figure binaries remain.
3. Run exact-commit GitHub Actions browser regression on desktop/mobile and independent viewer; take before/after screenshots and recheck scientific wording, figure placements and 7×4 count.
4. Keep PRs **draft**, do not merge or publish without separate explicit owner approval.

This report is **editorial/artifact tracking**, not a claim of theoretical proof or empirical validation of SYMMETRIA. The public discussion papers remain reference-free.
