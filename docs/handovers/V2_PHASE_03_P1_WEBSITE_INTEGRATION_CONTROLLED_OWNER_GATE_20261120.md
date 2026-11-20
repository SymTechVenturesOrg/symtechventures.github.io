# SYMMETRIA — Paper One Controlled Website Integration: Owner-Authorisation Gate and Exact Binary/Caption Map

**Prepared:** 20 November 2026 (Europe/London).
**Status:** **PLAN ONLY — NOT AUTHORISED TO MODIFY THE WEBSITE.** This handover may only be executed as a website-changing task after an explicit *new* owner authorisation. Its creation on a docs branch grants no implicit release permission.
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`.
**Verified live source for future integration planning:** `feature/v2-space-research-website`, head `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`, HTML blob `c235e33bbe3a291343125c94af73fe54a23491fa`, `articles/symmetria/symmetria-paper-01.html`; article CSS `css/v2-articles.css` blob `72697a65096fcdbc8c762e86215a8ceb14d1be92`.
**Current website PR:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5) with the site source branch as its head; do not modify that branch or PR without explicit authorisation.
**GitHub original source:** exact seven owner-approved PNG originals committed at `c6f60ee180c2f5d401b0f597f512898c010981a9` on documentation branch `docs/symmetria-paper-one-seven-approved-binaries-20261120` (draft PR #9).
**Science-corrected source:** 2.1 and 3.1 PNGs from commit `ef09d41b6b7fcb85efc75618736c234ccc2fa09c` on branch `docs/symmetria-paper-one-science-corrections-20261120` (draft PR #10). Both exact candidates are **owner visually approved and independently science re-audited**.
**Authoritative independent reviewer:** [re-audit report](../reports/V2_PHASE_03_P1_FIGURES_2_1_3_1_INDEPENDENT_SCIENCE_REAUDIT_AND_1_1_CAPTION_DECISION_20261120.md), commit `48e071e80d7842518c8ee8847fa5d187b61c262b`.
**Figure 5.1 erratum:** [Corrections to misattributed assertions in the re-audit text](../reports/V2_PHASE_03_P1_FIGURE_5_1_REAUDIT_TEXT_ERRATUM_20261120.md). Its approved original contains four **questions**, not the two declarative statements incorrectly attributed to it in the re-audit. The website caption still requires explicit `untested hypothesis` qualification.

## 1. Exact asset mapping — no approximation, no substitution

Currently the website contains **seven standalone `<img>` elements**, one per Paper One slot, each followed by a `<p class="figure-caption">`, rather than semantic `<figure>` elements. The existing seven source paths are **1536×1024-era WebP graphics where individually audited**; their old aspect and text/equations must never be assumed identical to the new owner-approved 1920×1080 cinematic art. The canonical replacement set is exactly:

| Slot | Existing website WebP filename (legacy) | Chosen source image path in GitHub documentation branch | Required SHA-256 of full-resolution PNG bytes | Proposed NEW versioned website PNG filename |
|---|---|---|---|---|
| Cover | `01_unified_framework_cover.webp` | `docs/artwork/owner-approved/paper-one/P1_Cover_OWNER_VISUALLY_APPROVED_1920x1080.png` | `3eeba0f6bfcefd2a63b5867cad0442ac9a6d356526cc1fed31e057d3de9e95a8` | `01_p1_cover_cinematic_1920x1080.png` |
| 1.1 | `01_historical_progression_physics.webp` | `docs/artwork/owner-approved/paper-one/P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675` | `02_p1_fig_1_1_unification_1920x1080.png` |
| 2.1 | `01_modern_physics_challenges.webp` | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png` | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | `03_p1_fig_2_1_quantum_gravity_1920x1080.png` |
| 3.1 | `01_search_for_unification.webp` | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png` | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | `04_p1_fig_3_1_open_frontiers_1920x1080.png` |
| 4.1 | `01_current_physics_limitations.webp` | `docs/artwork/owner-approved/paper-one/P1_Figure_4_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `788e68dc507c1e408428380b86816e594301384ed29331a3ab9aa9c29cdb9238` | `05_p1_fig_4_1_open_questions_1920x1080.png` |
| 5.1 | `01_symmetria_perspective.webp` | `docs/artwork/owner-approved/paper-one/P1_Figure_5_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c` | `06_p1_fig_5_1_deeper_organisation_1920x1080.png` |
| 6.1 | `01_future_research_roadmap.webp` | `docs/artwork/owner-approved/paper-one/P1_Figure_6_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | `a1c9c939c6195a97106a3e4c8a49398a48b27baf108a8ef7b21bdc0ed09e896f` | `07_p1_fig_6_1_research_testing_1920x1080.png` |

**Source route:** For unchanged originals, pull from original import commit; for 2.1/3.1 pull from corrected candidate commit. Both commits are GitHub authoritative and must be verified via a **binary-capable Git checkout**, not inferred from filenames or Markdown. Do **not** promote older uncorrected 2.1/3.1 PNGs by mistake.
**Proposed final asset folder (ONLY once authorised):** `images/symmetria/paper-01/` alongside, not overwriting, current WebP files. Use the proposed versioned filenames above. After copying verify each committed new asset SHA-256 **equals** its table source, not merely that it is visually similar. The exact bytes of the seven science/owner-reviewed PNGs define the canonical full-resolution images.

## 2. Crucial image/caption consistency — Figure 1.1

The *currently displayed* legacy `01_historical_progression_physics.webp` is a **different 1536×1024 WebP** and shows an Einstein field equation **with the `+ Λgμν` term**. The *new canonical* owner-approved `P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png` shows **`Gμν = (8πG/c⁴)Tμν`**, which is a **Λ=0 special case**.

Therefore:
- **NEVER append a `Λ=0` explanation to the current legacy WebP.** It would be scientifically false for the image currently shown.
- The proposed visible/selectable adjacent caption qualification is permitted **ONLY IF** the canonical new 1.1 PNG is simultaneously displayed and its full-resolution link opens that **same exact PNG**.
- For that new PNG, append the independently science-accepted sentence: **`The Einstein field equation shown is the special case with cosmological constant Λ = 0; the general form also contains a cosmological term.`** Add the same caveat to an accessible longer description. Its visible figure-panel symbols must match the actual image.
- If a future implementation retains the old WebP instead, **do not use the Λ=0 caption**; provide an image-specific explanation of the general equation if needed. The intended new artwork route is the canonical PNG, subject to explicit owner integration approval.

## 3. Editorial changes tied to these exact images

**Figures 2.1 and 5.1 require external caption updates**, independent from embedded text:

- **Figure 2.1 recommended complete caption:** `Quantum mechanics and general relativity are each highly successful in their respective domains, but a complete, experimentally established framework reconciling quantum principles with gravity remains an open research challenge.` No categorical `fundamentally incompatible` statement.
- **Figure 5.1 recommended complete caption:** `SYMMETRIA presents the following as an untested hypothesis: reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.` This avoids saying the hypothesis is established and avoids the redundant `hypothesis ... proposes` phrasing.
- **Figure 1.1:** preserve its existing historical text, but append the exact Λ=0 qualification **only with the canonical new PNG** as specified above.
- **Cover/3.1/4.1/6.1:** retain the existing external caption wording unless independent regression QA finds a new specific defect. Any unrelated revision is outside this narrow imaging integration.

Keep original Paper One body prose and headings unchanged. Preserve adjacent `figure-caption` semantics or improve to actual `<figure>/<figcaption>` only if the change is limited to each exact image-caption block and verified not to alter the surrounding research text.

## 4. Alt text, long explanations and accessible full-resolution view

Use the [seven vetted alt-text and longer-description drafts](../artwork/candidates/paper-one/PROPOSED_CAPTIONS_AND_ACCESSIBILITY_COPY_20261120.md) and subsequent [independent refinements](../reports/V2_PHASE_03_P1_FIGURES_2_1_3_1_INDEPENDENT_SCIENCE_REAUDIT_AND_1_1_CAPTION_DECISION_20261120.md). Important detailed coverage:

- **1.1:** Newtonian classical orbits; Maxwell electromagnetic unification; Einstein geometric gravity; clear visible/accessible **Λ=0 qualifier** with exact canonical new PNG.
- **2.1:** Standard Model's **three non-gravitational interactions**, gravity in GR, no proven unified quantum gravity, Λ=0 note.
- **3.1:** Standard Model **is a quantum field theory**; GR and dark-sector questions are distinct; observational/cosmological effects are modelled, underlying dark-sector nature unknown.
- **4.1:** dimensional constants vs dimensionless `α` distinction in longer description.
- **5.1:** four hypothetical **questions**, no fabricated or proved emergence. Do **not** repeat the independent re-audit's factually incorrect attribution of `Symmetry is fundamental`/`Nilpotent balance underlies nature` to this specific image; it has neither. Keep untested conjecture status in selectable HTML.
- **6.1:** expand **Nilpotent Symmetry Research Program (NSRP)** and call every stage **proposed future work**, not validated findings.

**Full-resolution UI:** the current CSS already defines `.paper-figure-open`, `.paper-figure-open-label` styles but the seven actual article `<img>` blocks do not use these links. In a later authorised implementation, add a discernible **keyboard- and touch-accessible same-image 1920×1080 link** for each, with visible focus and proper `target`/`rel` if new-tab semantics are chosen; external full-resolution link must point to the exact displayed source image (or a pixel-identical canonical source when an optimised display derivative has been scientifically/visually compared). Caption and zoom must not show different mathematical formulas.
**Mobile:** prior QA inferred image widths ~356px at 390px viewport and ~286px at 320px, making small inside-figure text/notations illegible unzoomed. This is **simulation only**. In a future authorised Work computer/browser, actually test desktop + responsive viewports 390px/320px, keyboard focus, touch, image linking, accessible descriptions and reduced/broken-image fallback. Never claim mobile/browser PASS from CSS projection alone.

## 5. Performance and 16:9 layout guard

The seven 1920×1080 reviewed PNG binaries total **21,896,557 bytes (about 21.9 MB) of existing compressed PNG transfer data**. Serving all eagerly may hurt mobile page performance. Original WebPs are a different size/aspect (typically 3:2 for those inspected). The future implementation must explicitly test:

- No CSS crops/warps: `width:100%;height:auto` or equivalent preserves the new 16:9 composition. Avoid `object-fit:cover` cropping labels or a fixed-height box that would cut captions.
- `loading=lazy`, `decoding=async` for non-cover figures; preserve a good first-contentful/large-contentful experience for cover without harmful layout shifting (`width=1920 height=1080`).
- If WebP/AVIF responsive display derivatives are introduced for performance, **they are separate unapproved display derivatives** requiring legibility and source-fidelity QA. The owner's canonical **full-resolution originals must remain retrievable unchanged** at a directly linked path with matching SHA. Do not silently replace the certified source bytes with lossy conversions, altered typography or differently composed images.
- Network totals, 320/390 browser rendering, laptop/desktop layout, alt text, caption visibility and open-full-resolution actions must be verified from an actual built webpage, not guessed.

## 6. Safe implementation workflow — DO NOT EXECUTE without owner authorisation

1. First obtain the owner's explicit permission for a **separate, unmerged, non-deployed website-integration PR**. This planning document is NOT that permission.
2. Re-read draft site PR #5 and its **current** head, article HTML blob and CSS. If branch/asset paths have drifted, stop and update the map before making any changes.
3. Create a fresh **website-integration branch from the current website implementation head** (not a commit to existing site PR #5), e.g. `feature/v2-paper-one-seven-approved-cinematic-images-20261120`. Create a distinct **draft stacked PR targeting `feature/v2-space-research-website`**. Never merge automatically; the draft may eventually be reviewed/retargeted with owner approval.
4. Copy the seven exact GitHub source PNGs byte-for-byte into the new website assets folder with versioned filenames above; compute GitHub fresh checkout SHA-256, decode, byte count and 1920×1080 for all seven. Do not modify source docs branches, old WebPs or source manifests.
5. Update exactly the seven article `<img>` src/alt/long-description/zoom blocks and the three explicitly identified captions (1.1 conditional, 2.1 and 5.1), with matching full-resolution links. Do not rewrite paper body prose.
6. Run actual browser tests, image/caption mapping inspection, scientific reviewer check, keyboard/tab navigation, screen-reader/accessible-name checks, mobile 390/320 test and performance analysis. Provide before/after screenshots, source hashes and issue counts.
7. Produce audit report and COPY TO CHAT with source website commit/hash, new draft PR, seven binary mappings, accessibility outcomes, performance, unresolved findings and a **separate owner approval request**. **No merge/deployment automatically.**

**Absolute safety boundary while in this planning stage:** no changes to website branch, PR #5, `main`, old WebP image files, published site, source original PNGs or science-corrected PNGs; no PR merge, no deployment. This file and associated erratum are **documentation only**.

## 7. Integration authorisation wording for a future explicit owner decision

Only if the owner elects to authorise implementation, launch a Work pass whose scope is: `Create a separate draft website-integration PR for the seven exact Paper One GitHub-science-reviewed PNGs and matching accessible captions/zoom. Do not modify website PR #5's branch; do not merge or deploy. Follow this pinned mapping and verify full GitHub binary hashes, exact captions and real responsive browser behaviour.` Work should then operate through GitHub and an authorised browser, with no ZIP hand-off.