# SYMMETRIA Paper Two — Work Handover: Native Cinematic Cover Style Checkpoint

**Date:** 21 November 2026 (Europe/London).
**Model (choose before Work):** GPT-6 Luna.
**Thinking effort (choose before Work):** High.
**Execution speed (choose before Work):** Standard.
**DTSU v1.1:** Ground updates in actual Europe/London date/time; state 0% at start, actual numeric percentage and realistic **numeric remaining ETA** at each milestone; do not mark 100% until GitHub binary readback, science/style check and COPY TO CHAT are complete. Work must not claim to choose model/effort/speed settings itself.

**Repository:** `SymTechVenturesOrg/symtechventures.github.io`.
**Working branch:** `docs/symmetria-paper-two-cinematic-artwork-20261121`. It is an **isolated documentation/artwork branch**, NOT website PR #5 or Paper One PR #11.
**Authorisation:** Owner approves the **Paper One images** (visual signoff only, no release authority) and the **creative direction** for Paper Two. **No Paper Two image has received owner approval yet.**
**Expected output:** **ONE** new full-canvas Paper Two COVER PNG as the style checkpoint, plus image-science/typographic QA, hash manifest, GitHub binary readback and owner-facing review. **STOP for owner review before generating 1.1–6.1.** The other six section briefs are prepared but not automatically approved.

## Source authority

Read first, and pin exact current source commits:
- [Paper Two seven-image commissioning/science gates](../artwork/paper-two/P2_CINEMATIC_IMAGE_COMMISSIONING_AND_SCIENCE_GATES_20261121.md).
- [Seven-slot production manifest](../artwork/paper-two/production_manifest.json).
- [Three rejected cover attempt QA and historical draft science-risk report](../reports/V2_PHASE_03_P2_INITIAL_COVER_GENERATION_AND_HISTORICAL_DRAFT_QA_20261121.md) — **read this before any new attempt**, do not mistake rejected generated files for assets ready for integration.
- [Locked owner style gate on main](https://github.com/SymTechVenturesOrg/symtechventures.github.io/blob/main/docs/reports/V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md).
- Paper Two article: `articles/symmetria/symmetria-paper-02.html` at `feature/v2-space-research-website`, earlier examined blob `060700e8cdac337583c820f044efe80154d59b6c`.
- Original reference A: `docs/artwork/owner-approved/paper-one/P1_Cover_OWNER_VISUALLY_APPROVED_1920x1080.png` at immutable binary import commit `c6f60ee180c2f5d401b0f597f512898c010981a9`, exact SHA-256 `3eeba0f6bfcefd2a63b5867cad0442ac9a6d356526cc1fed31e057d3de9e95a8`.
- Original reference B: `docs/artwork/owner-approved/paper-one/P1_Figure_5_1_OWNER_VISUALLY_APPROVED_1920x1080.png` same import commit, SHA-256 `945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c`.

Fetch **exact original full-resolution** reference bytes via binary-capable authenticated Git checkout; compare and view the actual images at full size before generating. **Do not use the previous Paper Two geometry-only ZIP or any rejected flat constructed poster** as a style master. The historical seven-image Paper Two draft manifest says scientific and owner signoff pending.

## COVER — creative and science brief

**Only authorised main heading within artwork:**
`Symmetry — Nature's Hidden Language`

**Optional explanatory subtitle:**
`Patterns in nature, transformations in mathematics, invariance in physical law`

**Any other text must be a short, scientifically exact subject explanation**, e.g. `Symmetry: a transformation that preserves a defined feature`. Avoid lengthy explanatory panels, a table of contents, fake formalism and fake conservation equations.

**CRITICAL TEXT BAN (automatic FAIL if broken):**
NEVER print `SYMMETRIA`, `PAPER TWO`, `Paper 2`, `Discussion Series`, `A NEW FRAMEWORK FOR FUNDAMENTAL PHYSICS`, `Figure 0` or other project/paper masthead inside the cover art. These words belong to the website/article context. Rejected native cover attempts in the chat included these mastheads **three times**, so this is a known generator failure mode. Do not call a pretty but non-compliant masthead cover successful.

**Visual narrative:** An exquisite central **sixfold ice-crystal / lattice rotational symmetry** in three-dimensional luminous cyan/gold geometry, with restrained gold arcs indicating rotations and/reflection where physically valid, and subtle surrounding crystal/biological motifs illustrating observed **approximate** natural symmetry. Layer through to a convincing abstract mathematical invariant/physical-field visualization, **without claiming natural shell/galaxy spirals possess exact rotational invariance or that a unification theory is proven**. The aesthetic must match the two owner-approved P1 artworks: midnight navy/black, glowing cyan and warm gold, dramatic volumetric 3D, elegant gold serif subject title, strong light geometry and legible hierarchy. An illustrated physical process, not a decorative gallery of unrelated objects.

The cover is an accessible, scientifically cautious introduction, **not a research result**. Do not include a "conservation laws → unification" arrow implying evidence that all forces are unified; Noether's theorem belongs specifically in Figure 4.1.

## Generation and acceptance

1. Create using a **native AI image-generation capability**, passing the two actual GitHub reference images where supported. Every output must be one standalone frame. If the generator repeatedly insists on masthead text, stop and report `STYLE_TEXT_BLOCKED`, not a fake pass. **Never substitute a full Pillow/Canvas/SVG-built scientific poster**.
2. Output **1920×1080**, 16:9, RGB/RGBA PNG, no crop or geometry distortion. If generated natively at ~1672×941, document that genuine dimension and permitted high-quality export/upscale; check that small type remains legible and new pixels do not invent scientifically misleading markings.
3. Inspect every string and scientific visual relationship. Exact subject title only; all banned words absent; correct crystal sixfold relation; distinguish idealised mathematical symmetry from imperfect natural patterns. If broken, regenerate or mark non-compliant.
4. Side-by-side compare with both original P1 anchors: volumetric quality, palette, typography, border/detail richness, credible science narrative. **Cannot self-certify owner style approval.**
5. Commit only a successful *review candidate* in new path `docs/artwork/paper-two/candidates/P2_Cover_Cinematic_1920x1080_Candidate.png` on the dedicated branch. Record source generator, native and final dimensions, full SHA-256 and byte count, source anchors and QA results in `docs/artwork/paper-two/production_manifest.json`.
6. Independently **fresh binary Git checkout** after candidate commit; verify exact SHA-256/PNG signature/dimensions/decode, and retain the candidate Git blob. Do not claim GitHub binary completion if file bytes could not be committed/read back.
7. Create a `docs/reports/V2_PHASE_03_P2_COVER_STYLE_CHECKPOINT_QA_20261121.md` with science-text review, side-by-side style reasoning, any blocker, hash/geometry results, owner-approval-pending state. Include one `COPY TO CHAT` handback with direct GitHub candidate image link (if it exists), scope, blockers and the next owner decision.

**No Paper Two website asset replacement, no WebP compression yet, no Paper One PR #11 source changes or release, no merge or deployment.** Only after owner approves the cover checkpoint should six independent individual section images be commissioned from the exact source text. These subsequent figures require their own specific scientific/content checks, independent re-audit and per-image owner approvals.
