# SYMMETRIA — Paper One: Targeted Science, Caption and Accessibility Correction Register

**Date:** 20 November 2026 (Europe/London)  
**Status:** **PROPOSED CORRECTIONS ONLY — no artwork, caption, article or website edits authorised or applied by this document.**  
**Source audit:** [Seven-figure independent science/editorial QA](V2_PHASE_03_WORK_PAPER_ONE_SEVEN_GITHUB_NATIVE_INDEPENDENT_QA_20261120.md), verified report Git blob `aafda331d45c59178170b806f6dea5d217125180`.  
**Original approved binary source:** `docs/artwork/owner-approved/paper-one/` at GitHub import commit `c6f60ee180c2f5d401b0f597f512898c010981a9`; identity list [manifest](../artwork/owner-approved/paper-one/manifest.json), `DIRECT_GITHUB_SHA256_VERIFIED`, 7/7.  
**Proven website:** `articles/symmetria/symmetria-paper-01.html` on `feature/v2-space-research-website` at tested HEAD `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`; HTML blob `c235e33bbe3a291343125c94af73fe54a23491fa`.  
**Visual owner approvals:** 7 of 7. **Scientific next-gate status:** 3 ready, 3 science fixes, 1 caption fix. These classifications describe the independent QA report, not peer-reviewed publication acceptance.

## Principles — preserve the originals

- Never overwrite or regenerate the seven original owner-visually-approved PNGs in `docs/artwork/owner-approved/paper-one/`. They provide an immutable provenance baseline. Any altered image gets a **new candidate path, new SHA-256 and new explicit QA/owner decision**.
- **Prefer localised science-text repair or truthful explanatory annotation** to recreating the 3D scene; keep cinematic composition, typography, dark navy/cyan/gold lighting and title rules. Do not rely on programmatic flat poster reconstruction or screenshot crops as an artwork substitute. If the editing capability cannot make a faithful modification, mark image correction BLOCKED rather than submit a mismatched picture.
- Distinguish **scientific image corrections** from **website HTML caption suggestions**. Editing the website is a **separate owner-authorised implementation stage**. This correction register authorises neither.
- Do not call all seven science-approved, promise all can be published, change PR #5, merge PR #9, or deploy.

## Slot-by-slot narrow correction register

| Slot | QA result | Needed correction / caveat | Where the change belongs | Verification |
|---|---|---|---|---|
| Cover | READY FOR NEXT GATE (Low) | Keep successful descriptions separate and the unification goal explicitly unresolved. | **No image correction.** | Preserve original SHA and editorial check. |
| **Figure 1.1** | **SCIENCE FIX (Moderate)** | Image shows Einstein equation `G_{μν} = (8πG/c⁴)T_{μν}` without cosmological constant. This is a **Λ=0 special case**. | **Inside image:** visible, small `Λ = 0 special case` qualification next to the current equation, **OR** replace with convention-consistent `G_{μν} + Λ g_{μν} = (8πG/c⁴)T_{μν}`. Keep Newton and Maxwell panels unchanged. | Inspect exact rendered glyphs, symbols and sign convention; Newton must show classical orbits, not curved spacetime. |
| **Figure 2.1** | **SCIENCE FIX (Moderate)** | Image wording `A Quantum Theory of the Fundamental Forces` wrongly risks claiming the Standard Model covers gravity; its displayed Einstein equation also assumes Λ=0. Website caption says the frameworks are `fundamentally incompatible`, an excessively absolute simplification. | **Inside image:** label the Standard Model `Quantum theory of three non-gravitational interactions` (or equally accurate, sufficiently legible shorter wording); mark Einstein equation `Λ = 0 special case` or use a correct full equation. **External website caption, proposed only:** `Quantum mechanics and general relativity are each highly successful in their domains, but a complete, experimentally established framework reconciling quantum principles with gravity remains an open challenge.` | Confirm wording does not claim complete four-force unification. Verify actual particle/boson symbols, original composition, the Λ annotation, and caption meaning. |
| **Figure 3.1** | **SCIENCE FIX (Moderate)** | QFT and Standard Model are presented as separate peers although the Standard Model is formulated using QFT; phrase `Beyond the reach of current theories` is too broad for dark matter/dark energy effects that current models describe. | **Inside image:** clarify `Standard Model — a quantum field theory of electromagnetic, weak and strong interactions`; QFT is the framework, not a separate independent force theory. Replace broad dark-sector assertion with a short conditional/accurate line such as `Dark matter and dark energy: observable effects, unknown physical nature`. Keep quantum gravity separately unresolved. | Confirm no misleading independent-pillar implication; verify every particle family/gauge label, and that dark-sector statements distinguish inferred effects from unidentified underlying physics. |
| Figure 4.1 | READY FOR NEXT GATE (Low) | Constants panel mixes dimensional parameters (`c, h, G, mₑ, mₚ`) and dimensionless `α`. | **No required image correction.** In later accessible description, note the distinction without implying all constants are equivalent. | Keep original art and SHA. |
| **Figure 5.1** | **CAPTION FIX (Low)** | Image already says `Exploratory hypothesis — not established physics`; external caption does not explicitly say `untested`. | **Website caption proposal only:** `As an untested hypothesis, SYMMETRIA proposes that reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.` The change adds a caveat without changing the proposal's own wording. | Confirm the caption stands independently as an untested proposal; preserve the correct four-concept image unchanged. |
| Figure 6.1 | READY FOR NEXT GATE (Low) | Research path remains prospective with `Revise or reject if unsupported`; NSRP acronym benefits from an expanded accessible description. | **No image correction.** Explain NSRP as `Nilpotent Symmetry Research Program` in future HTML description. | No claims of completed validation or published predictions. |

**Equation convention note:** the full displayed Einstein equation above assumes the same sign/metric convention used for the image's existing `G_{μν}` and `T_{μν}`. A scientifically qualified reviewer must verify the rendering and convention. The simpler visible `Λ=0` annotation is a lower-risk patch that leaves the original equation intact, but may be less pedagogically complete than showing the full equation.

## Website accessibility and caption requirements — defer to authorised integration

The audit inferred approximately 356px rendered image width at a 390px viewport, and 286px at 320px; small labels are too dense to read unzoomed. **These values are CSS simulations, not device tests.**

When integration is separately approved:
- Supply a **keyboard- and touch-accessible open-full-resolution link or equivalent**, with visible focus state and an understandable accessible name. Test on an actual 390px and 320px viewport.
- Give each figure a concise, informative `alt` that describes its subject, not generic `Modern Physics Challenges` text; provide an adjacent longer HTML description or accessible disclosure for detailed equations/panels. Don't cram whole paragraphs into `alt`.
- Keep all scientific caveats and hypothetical status in **selectable HTML**, not solely inside PNG pixels.
- Check links and zoom controls with keyboard, touch, screen reader and genuine browser rendering; don't infer a browser pass from CSS simulations.

## Proposed staged acceptance flow

1. **Science/editing spec sign-off:** owner accepts the above limited set of changes and the choice between `Λ=0` labels versus full-equation replacement. If there is no preference, default to the lower-risk visible special-case labels pending scientific re-audit.
2. **Targeted image correction of 1.1, 2.1 and 3.1 only**, in an image-edit-capable session. Produce three separate original-format 1920×1080 PNG review candidates (not a collage), each with distinct filename, dimensions, SHA-256 and image-level review. Keep all seven original GitHub blobs intact.
3. **Caption source correction of 2.1 and 5.1**, but **only in a separate authorised website PR**. The proposed copy is recorded here for review; no implementation permission is inferred.
4. **Independent re-audit** of the corrected three images + external caption drafts and readability/accessible-text plan, citing exact original and corrected GitHub binary hashes; classify each as ready/fix/blocked.
5. **Controlled integration planning gate** only after owner and independent science acceptance. A future website PR must be separate and unmerged until explicit approval.

## No-action record

Creation of this document is documentation-only on `docs/symmetria-paper-one-seven-approved-binaries-20261120`. No original PNG bytes, image hashes, article captions, website code, website draft PR #5, `main`, merges or deployment are changed. The seven-image binary verification remains valid and immutable.
