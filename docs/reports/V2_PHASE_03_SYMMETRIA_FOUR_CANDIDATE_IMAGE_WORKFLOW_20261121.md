# SYMMETRIA — Four-Candidate Cinematic Physics Image Production Method

**Owner instruction:** 21 November 2026. **Status:** owner-agreed production-method addendum, preserved in an isolated documentation branch; **not** an approval of any new individual image or authorisation to merge/deploy.  
**Applies to:** all future new/replacement figures in the SYMMETRIA Discussion Series, starting with Paper Three Figure 4.1 and continuing through Paper Four and subsequent papers.  
**Supersession:** supplements, does **not** weaken, [the mandatory figure production standard](V2_PHASE_03_SYMMETRIA_FIGURE_PRODUCTION_STANDARD_20261120.md) or [the locked cinematic style/scientific acceptance gate](V2_PHASE_03_SYMMETRIA_LOCKED_CINEMATIC_ARTWORK_GATE_20261120.md).

## 1. The decision and why it is needed

For a single figure slot, request **four alternative, independently generated, standalone full-canvas cinematic illustrations** rather than one image that is repeatedly regenerated and repaired. The variants should explore four **different scientific visual emphases**, while all obeying one identical, verified subject/caption brief, approved Paper One/Two style anchors, and the same science and labelling rules. Present all four together **only for selection**, with a review contact sheet clearly marked as a contact sheet—not as deliverable artwork. Individual source images remain separate and unchanged.

This method emerged from the owner-reviewed four-alternative exercise for **Paper Three Figure 4.1 — Dirac Structure and Nilpotent Reorganisation**, where Candidate D was judged the **preferred** image after comparing A–D. **Preferred is not the same as an exact-byte final/master approval**: record owner sign-off and verified publication geometry separately.

Do not request a single four-panel collage and crop its small tiles. Do not use AI to invent equations or claim a speculative theory is proven. Do not repeat a failed prompt indefinitely; keep the usable candidates and change the brief or stop.

## 2. Preflight: two source locks

1. **Manuscript lock** — Read the exact article HTML heading, figure slot, adjacent caption and section prose at a pinned GitHub commit. Record SHA/path and separate: (a) established mathematics/physics; (b) Rowlands-specific proposed algebraic reformulation; (c) speculative SYMMETRIA interpretation. Review all equations, signs, physical conditions and diagram causality **before** image generation. If ambiguous, omit complex notation from the artwork and give a correct accessible explanation in HTML.
2. **Cinematic style lock** — Use **at least two original owner-approved full-resolution Paper One or Paper Two source images** as genuine visual references; record exact path, provenance and SHA-256. The reference set is documented at `docs/artwork/style-reference/manifest.json` and `README.md` on the canonical style-reference branch. It includes: `P1_Nilpotent_Operator_STYLE_ONLY.png` (SHA-256 `1cb364be9159452134594f3f7e86de5424d82c8738b209d7ebb8622b90e7d9f2`), `P2_Noether_Conservation_STYLE_ONLY.png` (`1f7515074252b54bf4cbb6ef70683610e528c1f322097090751e1304a5f35593`) and `P2_Broken_Symmetry_STYLE_ONLY.png` (`484191f41f002cc286938299da77de91b0dac14e8e9ef808ef356cb5b93e5817`). These are **style only**, not evidence for scientific claims. Original owner-approved final cover/figures may also serve as reference anchors.

## 3. Request four independent alternatives

Generate A, B, C and D for **one named figure**. Each generated image must be its own large, complete landscape scene, never a montage or seven-up contact sheet. Choose distinct visual story variants while preserving the section's precise meaning. The four standard emphases are:

- **A — Physical geometry first:** established physical structures, verified dispersion/conservation/transformations, with the new interpretation separated.
- **B — Mathematical structure first:** rigorously checked operator/spinor/anticommutation relationships, with visually expressive 3-D algebraic geometry.
- **C — Contrast/comparison:** established framework and proposal shown distinctly, with clear epistemic status and a careful bridge.
- **D — Integrated explanatory composition:** one visually coherent scientific narrative with a prominent hero subject and minimal verified text.

All four must match the approved AI-native cinematic style: deep navy/near-black scientific atmosphere, volumetric 3-D geometry, cyan/blue and warm gold lighting, elegant gold/cream serif scientific subject title, restrained subtitle and concise labels. The scientific visual **must explain the specific section**. Generic cosmic backgrounds, ornamental lobes, empty physics-looking diagrams, flat code-built posters and unrelated object collages fail.

**Never embed:** project masthead, `SYMMETRIA` series branding, paper or figure number, figure caption metadata, scientist portrait or generic instrument. Figure identification remains outside artwork in website HTML.

## 4. Non-negotiable scientific gates

For *each* candidate, inspect every equation, operator, sign, matrix, axis, graph and implied relationship. Reject rather than cosmetically fix major scientific mistakes.

For Paper Three Figure 4.1 specifically:

- **Established:** conventional Dirac equation/operator, spinors, and massive relativistic dispersion `E² = p²c² + m²c⁴` (or `E² = p² + m²` with stated natural units); positive/negative energy branches for nonzero mass must not meet at a massless cone apex.
- **Proposed:** Rowlands' particular nilpotent algebraic reorganisation, **under a specified algebra and appropriate on-shell conditions**. `N² = 0` may be shown only with such a qualification and not attributed to an arbitrary Dirac operator.
- **Unproven:** complete field-theoretic equivalence, novel ontology, automatically recovered interactions, or new physical laws must **not** be presented as established.
- Clear distinctions between descriptions, status and conditionality matter more than decorative detail.

A beautiful but incorrect candidate is **SCIENCE FAIL**, not “almost approved”.

## 5. Review and selection

Evaluate each independent A–D source against five recorded gates:

| Gate | Required outcome |
|---|---|
| Section/caption mapping | Exact manuscript figure slot and one scientific story |
| Scientific/editorial accuracy | No incorrect equations, false inferences or unqualified speculative claims |
| Owner-approved cinematic style | Rich native AI cinematic visual matching at least two approved originals; not flat diagram/boxed slide |
| Legibility/accessibility | Scientific subject title and key visual concepts readable; detailed explanation can live in accessible HTML |
| File/provenance/geometry | Original bytes, generator native dimensions and SHA-256 recorded; final exported master **exact 1920×1080** |

Make an owner-facing **labelled contact sheet only for comparing variants**, with A/B/C/D and brief scientific review of each. Keep each actual candidate as a separate original. Recommend one preferred candidate but never infer owner approval from the assistant's recommendation. Record explicit owner decision for the exact image identity; do not infer approval from approving the *method*.

If one candidate needs a **minor localised** glyph or label repair, a targeted edit is allowed only if the underlying AI-generated full-canvas artwork stays unchanged. Major semantic errors, wrong topics and montage outputs require **rejection/regeneration**, not programmatically rebuilding the picture.

## 6. Native 1672×941 vs mandatory 1920×1080

The current image-generation service has returned `1672×941` pixels for requested 16:9 landscape illustrations. This is an approximately 16:9 generation size, **not** a 1920×1080 deliverable. A request for a particular aspect ratio does not guarantee those exact pixel dimensions. The generation service determines its supported pixel grid.

Measured original Candidate D for Paper Three Figure 4.1 (local conversation source `imagegen.png`, **not yet in GitHub**): **1672×941 RGB PNG**, **2,295,582 bytes**, SHA-256 `5378c4216db1e5fcccc7e60bfc23a9f87a91e6eb70078a3e11548fd1719f4102`.

- Pixel compliance can be achieved by a carefully measured, **proportion-preserving** high-quality Lanczos enlargement to approximately `1919×1080`, followed by a **one-pixel edge extension** to reach **1920×1080**. Avoid stretching, cropped labels or significant alteration of explanatory content. Record the exact original and finished geometries and SHA-256 values.
- The upscale adds pixels, **not native optical detail**. It cannot recover mathematical strokes or resolution the generator never produced. Verify all source equations and labels **after** enlargement; no declaration of “native 1920×1080”.
- Keep the original generator PNG unchanged; store the finished PNG separately and link it via manifest. Use lossless PNG as the review/master; only after owner approval, make and independently verify responsive WebP derivatives at a suitable quality, typically ≥80 when text legibility requires.
- Perform binary PNG decode, RGB/mode and exact dimension checks; check full-resolution typography and 320px/390px browser projections; offer original-image enlargement and selectable descriptions.

## 7. Provenance, gates, and GitHub workflow

Maintain **one manifest row per candidate**, with paper, slot, exact source caption and commit, A–D emphasis, reference names/hashes, generator mode, native file size and dimensions, source SHA-256, finishing operations, final 1920×1080 SHA-256, science/editorial pass/fail, cinematic-style pass/fail, and explicit owner verdict/date.

Preserve candidate, rejected and preferred histories without overwriting original files. Store artwork only on a **new isolated draft PR/branch** after the owner authorises that upload; keep existing site image files, original masters and rollback mapping unchanged. Content changes to production paper HTML require a separately scoped authorisation and responsive/browser/accessibility QA.

The four-candidate workflow is a **production-selection technique**, not an exemption from the locked standards and not permission to merge, deploy or change `main`. Do not touch protected PRs #5, #11, #12 or #13 as part of committing this methodology.

## 8. Handover requirements

For each completed candidate round, report: exact figures attempted; A–D individual image identities; science/style verdict per candidate; recommended candidate; owner approval status; native/export dimensions; postprocessing method; SHA-256; GitHub branch/PR if archived; limitations; next gate. Follow existing DTSU v1.1 during multi-step work, including **estimated** ETA updates when reasonably possible. End with **COPY TO CHAT** status.