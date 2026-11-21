# SYMMETRIA Paper Two — Targeted Science-and-Art Correction Gate for Figures 2.1, 3.1, 6.1

**Prepared:** 21 November 2026 · **Scope: planning and acceptance specifications only**.
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`.
**Draft PR:** [#12](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/12), isolated branch `docs/symmetria-paper-two-cinematic-artwork-20261121`.
**Source independent audit:** [Six-figure QA report](../reports/V2_PHASE_03_P2_SIX_CHAT_IMAGES_BATCH_INDEPENDENT_QA_20261121.md), blob `9968e44f8943e149ab89b231281cacdac73a6013`; six candidate source import commit `be2985ab59657ac4e631a7b8e0084064167188c4`.
**Production manifest:** [current per-figure decisions](../artwork/paper-two/production_manifest.json).
**Owner status:** User has approved the separately staged *Paper Two cover only*. The independent reviewer marked 1.1, 4.1 and 5.1 PASS and 2.1, 3.1 and 6.1 FIX; **none of these six is yet owner approved**. Do not turn scientific acceptance into owner approval.
**Production authority:** This handover is a *proposed repair specification*, not retroactive authority to replace image files, modify the website or release. When the owner authorises correction, make new candidates with distinct names/hashes while preserving all original six candidate bytes.

## 1. Preserve the three independently QA-passed images unchanged

| Figure | Exact source candidate SHA-256 | Independent QA | What later accessible website caption must clarify |
|---|---|---|---|
| **1.1 — Symmetry in Nature and Physics** | `a53157058eda3e5d594e53284be40f8bb2c58fdb03c399b7401e7fefc525957c` | SCIENCE PASS / STYLE PASS | Biological symmetry is approximate; crystalline and mathematical symmetries may be idealised; resemblance alone is not proof of physical invariance |
| **4.1 — Noether's Theorem** | `bce9e58d6a5dbb058774051a88f1d76f44e926420f56ca9939440eef7512365c` | SCIENCE PASS / STYLE PASS | Rotational symmetry of the relevant action/system yields angular momentum conservation under suitable conditions; a mechanical example needs no external torque |
| **5.1 — Broken Symmetry** | `201f88207b9bd0122a105c59c94b8a17f6d50740c310594718d5b3ababf685cf` | SCIENCE PASS / STYLE PASS | `V(φ)` is a **schematic one-dimensional double-well**, not a full continuous-field Mexican-hat surface or universal explanation of mass |

**No new image generation or retouching for these three recommended PASS files.** Owner visual review remains outstanding for them; they are not included in the 3-image repair batch.

## 2. Three targeted science fixes: original source identities and design guardrails

### Figure 2.1 — Natural Symmetry Patterns — remove an unsupported exact-fit claim

- **Existing candidate SHA-256:** `a44fa0463affeaa486bdb000793c7c3674bae78587e245886e5dd27b7ece97b8`.
- The overlaid golden rectangle/Fibonacci spiral on the sunflower falsely suggests exact mathematical measurement of that specimen; the manuscript only discusses recurring but physically diverse natural patterns.
- **Preferred solution:** remove the rectangle + traced golden spiral overlay entirely, retaining the volumetric sunflower/seed head, tree, sixfold ice crystal and water ripple. A label saying `schematic approximation` is a fallback only if the visual geometry itself no longer appears to assert an exact fitted spiral.
- Show natural forms and physical processes as *examples*, not as identical exact invariance classes. A shell spiral can exhibit approximate growth self-similarity involving scale+rotation, which must not be described as pure rotational invariance.
- Preserve the existing cinematic midnight navy, cyan/gold glow, elegant subject title and realistic 3D detailing; do not replace it with a flat programmatic infographic.

### Figure 3.1 — Mathematical Symmetry and Invariance — resolve the invariance/translation distinction

- **Existing candidate SHA-256:** `715d5b9c70f818381e6fcef3e63149079b6e8f9010308bc386e966e3bb0fa233`.
- Main defect: a **finite isolated snowflake has no nontrivial translational symmetry**. Rigidly moving it yields a congruent object at a new position, not invariance of the original shape as a set at its original position.
- **Preferred solution:** keep **idealised sixfold** snowflake and credible **60° rotation** and **mirror reflection** as actual symmetry operations; **clearly separate** the third panel as `Translation — a transformation, not a symmetry of this finite shape`, with an original/moved silhouette and an explicit changing position. Alternative: show a genuinely periodic infinite/extended lattice if explaining translational symmetry, and label its periodicity.
- `D₆` (regular sixfold rotation/reflection group) must exclude translations; keep `D₆=⟨R₆₀°,M⟩` only with a *defined* mirror operator. If reflecting via `x→−x`, name the **reflection across the y-axis**, not ambiguously `Mₓ` unless the convention is explicitly defined. Remove duplicate `x` and `y` glyphs.
- If retaining a coordinate-field translation formula, choose an explicit convention: `f_new(x,y)=f_old(x−a,y−b)` represents **active** object translation by vector `(a,b)`; or consistently use a passive coordinate shift with clearly stated direction. No unstated sign/active-passive ambiguity.
- If space is limited, eliminate the algebra rather than render inaccurate or illegible formulae. Caption/accessible long description can carry detailed caveats but should not have to contradict a misleading image.

### Figure 6.1 — An Exploratory Symmetry Perspective — focused reconstruction

- **Existing candidate SHA-256:** `34d4f861e699cd1ae2f0fa98a6b157aa513544407d778ae111d1b7128f01f4d3`.
- **Rebuild rather than tiny text retouch.** The broad gallery of sunflower/shell/butterfly, Newton cradle, planetary-atom, potential diagram and central geometry fails the locked single-scientific-story gate.
- Make a **single coherent 3D cinematic conceptual illustration** of *a possible deeper symmetry underpinning observable physical structures*, shown by an elegant luminous nested symmetry/constraint structure emerging into an abstract observable field, **without any claim that such a mechanism has been demonstrated**.
- Subject-only heading suggestion: `Could Deeper Symmetry Shape Physical Law?` (NOT `The SYMMETRIA` as a decorative masthead). A short, legible scientific qualifier inside the image is strongly preferred: `Exploratory hypothesis — not established physics`.
- Remove **planetary-orbit atom** (scientifically misleading classical mini-solar-system presentation) and all unrelated thematic collages. No false simulation of experimental evidence, no implied completed unified field theory, no misuse of nilpotent terminology as an established mechanism.
- The actual manuscript names SYMMETRIA, so prose/accessible caption may identify it as the proposed hypothesis. Do not place it as a decorative series brand headline within the image. Maintain exact Paper Two cover and Paper One cinematic visual family.

## 3. Controlled continuation if owner authorises the 3 fixes

- Generate **only these three** separate AI-native cinematic art candidates (or native image edits where feasible) in Chat, **without interrupting for three successive owner decisions**, and keep the original six unchanged.
- Export each accepted-for-audit candidate to verified 1920×1080 PNG with authentic source-generation dimensions disclosed; avoid digital crop/collage or low-quality programme-drawn reconstruction. Compute each candidate SHA-256 and byte count and stage in the same ChatGPT Space Page or another verified persistent source.
- Separate original input and corrected output filenames; make **new candidate paths** with `_ScienceFix_Candidate_1920x1080.png`, not replacements in the six original GitHub paths.
- Independently import all three new candidates and verify GitHub binary SHA-256, RGB mode and dimensions in **one Work science/style re-audit**, checking each explicit correction and unchanged three PASS candidates.
- **One combined owner review at the end** should cover 1.1, 2.1, 3.1, 4.1, 5.1 and 6.1 plus already-approved cover; explicitly record separate owner image approvals before website-image promotion.
- **No Paper Two website edits, WebP compression, changes to PR #5 / Paper One PR #11, merge or deployment** in this correction/QA gate.

## 4. Required acceptance and reporting

For each corrected image return independent `PASS_SCIENCE / FIX_REQUIRED` and `PASS_STYLE / FIX_REQUIRED` disposition, exact image/text descriptions of what changed, science caveats and literal PNG SHA-256/bytes. Use DTSU v1.1 and end with a consolidated `COPY TO CHAT` handback. No image is called owner-approved by Work or automatically released.
