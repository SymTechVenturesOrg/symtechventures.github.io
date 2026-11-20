# SYMMETRIA Paper One — Independent Figure Science Re-Audit and Figure 1.1 Caption Decision

**Date:** 20 November 2026 (Europe/London)  
**Review branch:** `docs/symmetria-paper-one-science-corrections-20261120`  
**Scope:** Independent scientific review of the owner-visually-approved Figure 2.1 and 3.1 PNG candidates; a caption-only decision for the unchanged canonical Figure 1.1 PNG; read-only review of caption, accessibility and full-resolution viewing proposals.  
**Write boundary:** This report is the only file added by this audit. No PNG, manifest, HTML, CSS, website asset or pull-request source was changed. No PR was merged and nothing was deployed.

## Source identity and method

- Fresh binary Git checkout of the correction branch: **`9441ae651a64ac907e2a8548457d2cc592a7325a`** (full SHA, checked against the remote branch head at audit start).
- Immutable owner-approved original-image import commit: **`c6f60ee180c2f5d401b0f597f512898c010981a9`**.
- Corrected-candidate binary commit: **`ef09d41b6b7fcb85efc75618736c234ccc2fa09c`**.
- Latest correction branch contains the owner's visual approval record for the exact 2.1 and 3.1 SHA-256 values below. Visual approval is distinct from the scientific decisions in this report.
- Current Paper One website branch: `feature/v2-space-research-website`, head **`f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`**. Current article blob: **`c235e33bbe3a291343125c94af73fe54a23491fa`**.
- PR #10 was checked read-only: open, **draft**, unmerged. Its changed paths are documentation and two candidate PNGs; no website paths are in its file list.

Binary checks were run from the fresh Git checkout, not the text-file API: `sha256sum` for bytes, Pillow `Image.verify()` and reopen for full PNG decoding/dimensions/mode, `git hash-object` for Git blob identity, and a NumPy pixel comparison against each exact original. I inspected the full-frame candidates and enlarged crops of the changed text and Figure 1.1 equation. The approved-original source manifest was also recomputed against all seven original PNGs; all seven SHA-256 values matched. The candidate commit adds only the two new candidate paths and changes no owner-approved image path.

## Binary identity and pixel comparison

All three inspected files have the PNG signature `89504e470d0a1a0a`, decode completely, and are 1920×1080 RGB.

| Slot | GitHub path | Bytes | SHA-256 | Git blob |
|---|---|---:|---|---|
| 1.1 original | `docs/artwork/owner-approved/paper-one/P1_Figure_1_1_OWNER_VISUALLY_APPROVED_1920x1080.png` | 2,972,672 | `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675` | `6d42d6bce260d1f23f0b55b21df9ad05b3fe7c17` |
| 2.1 corrected candidate | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_2_1_SM_Lambda0_Correction_Candidate_1920x1080.png` | 3,088,099 | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | `16adf23b9d8f61ec4c47c48ac243cae096b3336a` |
| 3.1 corrected candidate | `docs/artwork/candidates/paper-one/science-corrections-20261120/P1_Figure_3_1_QFT_DarkSector_Correction_Candidate_1920x1080.png` | 3,348,284 | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | `4bcafdc4bbd3d068b582dad27735c6554f008700` |

Independent pixel results:

| Candidate | Authorised text region | Exact pixel bound `[x1,y1,x2,y2)` | Changed pixels |
|---|---|---:|---:|
| 2.1 | Standard Model subtitle | `[243,191,709,281)` | 38,419 |
| 2.1 | Λ = 0 note | `[1491,719,1664,748)` | 3,184 |
| 3.1 | Standard Model description | `[711,189,1254,285)` | 49,251 |
| 3.1 | Open Frontiers strapline | `[511,684,1409,737)` | 43,746 |

There were 41,603 changed pixels in 2.1 and 92,997 in 3.1. In both images **zero changed pixels lie outside** the specified text rectangles. Formula glyphs, particle diagrams, surrounding panel geometry and cinematic backgrounds are pixel-identical to their respective originals.

## Independent scientific dispositions

### Figure 2.1 — `PASS_SCIENCE_REAUDIT`

The candidate states **`Quantum theory of three non-gravitational interactions`** under the Standard Model heading. This correctly limits the claim to electromagnetism, the weak interaction and the strong interaction; gravity remains outside the Standard Model and is separately depicted by the general-relativity panel. The particle families are consistent with the three generations: up/charm/top and down/strange/bottom quarks; electron/muon/tau charged leptons; and the three corresponding neutrinos. The gauge labels γ (photon), W±/Z⁰ and g (gluon) are consistent with electromagnetic, weak and strong interactions respectively. The Higgs boson is not individually shown in this candidate; that is an omission, not a false label or claim to be a complete particle inventory.

The Einstein equation is rendered as `Gμν = (8πG/c⁴)Tμν`, with `Λ = 0 special case` directly beneath it. This is a correct zero-cosmological-constant form under the displayed convention; the note clearly limits the equation and is legible in the native 1920×1080 view. Equivalent sign arrangements occur under different curvature/stress-energy conventions, but the candidate does not mix conventions or claim to show the most general equation. The central “A Unified Theory?” remains a question, and the image does not claim that quantum gravity has been solved. The equation note is too small for dependable reading when the image is reduced to a typical mobile column width; accessible text and a full-resolution view remain necessary.

### Figure 3.1 — `PASS_SCIENCE_REAUDIT`

The Standard Model panel now says **`A quantum field theory describing electromagnetic, weak and strong interactions`**. This accurately makes the Standard Model a particular quantum field theory, rather than a peer framework competing with quantum field theory itself. The separate General Relativity panel correctly assigns gravity to spacetime geometry; no text says the Standard Model contains gravity or that the three interactions have been unified with it.

The quark and lepton generations are correctly labelled. Gauge bosons are shown generically rather than individually named in this figure; the separate Higgs panel does not misclassify the Higgs as a gauge boson. The replacement strapline, **`Quantum gravity is unresolved; the dark sector's nature remains unknown.`**, is accurate and appropriately bounded. It does not claim that dark matter or dark energy have no observed effects: the gravitational and cosmological phenomena attributed to them are modelled/inferred, while their underlying physical nature remains unsettled. The QFT, Standard Model, General Relativity and unresolved-question relationships are clear in the composition. No science-text fix is required for this candidate.

## Figure 1.1 — caption-only decision

**Decision for the unchanged canonical GitHub PNG: `CAPTION_ONLY_ACCEPTABLE_PENDING_WEBSITE_IMPLEMENTATION`.** The inspected 1920×1080 approved original shows Newton's inverse-square force law, Maxwell's four SI vacuum equations and the Einstein equation `Gμν = (8πG/c⁴)Tμν` without a cosmological term. The latter is correct as the **Λ = 0 special case**; the general field equation may include a term proportional to `Λgμν`. The absence of that term is not a flaw if the adjacent caption explicitly qualifies the displayed equation. The Newton and Maxwell equations are recognisable and consistent with their labelled concepts; the historical progression is narrative, not evidence that any proposed SYMMETRIA unification is established.

The proposed visible caption append is scientifically suitable for that exact PNG:

> The Einstein field equation shown is the special case with cosmological constant Λ = 0; the general form also contains a cosmological term.

The proposed longer Figure 1.1 description already repeats that qualification. Keeping the approved artwork unchanged is therefore acceptable **provided** a later website implementation places this visible/selectable sentence adjacent to the matching canonical PNG, repeats it in the accessible longer description, and provides a keyboard- and touch-accessible full-resolution view of that same 1920×1080 binary. This is conditional readiness for a future separately authorised integration; Figure 1.1 is not yet science-cleared in the existing website.

**Important source mismatch for implementation:** the current website article does not display that canonical PNG. It uses `images/symmetria/paper-01/01_historical_progression_physics.webp`, a separate 1536×1024 RGB WebP. I inspected the actual GitHub bytes: its Einstein panel shows `Gμν + Λgμν = (8πG/c⁴)Tμν` (a cosmological term is present). Thus adding the proposed **Λ = 0** sentence to that existing WebP would be false. Before integration, the owner/editor must map the displayed asset deliberately: either display the unchanged canonical PNG with the Λ=0 caption/description and same-image full-resolution link, or retain the current WebP and use a caption/description consistent with its equation containing a cosmological term. This report authorises neither choice and makes no website changes.

## Website source, captions and source-hash discrepancy

The handover's prior-source discrepancy was **not reproduced**. In a fresh Git checkout, `feature/v2-space-research-website` resolves to `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`; `git rev-parse FETCH_HEAD:articles/symmetria/symmetria-paper-01.html` returns blob `c235e33bbe3a291343125c94af73fe54a23491fa`. The GitHub `fetch_file` result independently returns that same blob SHA. The prior correction-work report's `390a8676189542fc9044c1dabbbf344ad10e69f6` value is inconsistent with the current Git object graph and was not reproducible; it should be treated as an erroneous prior metadata reading, not as a second current version.

Exact captions from the current article checkout:

- **Figure 1.1:** “Throughout history, physics has repeatedly advanced through the discovery of deeper unifying principles. From Newton's laws of motion to Maxwell's electromagnetic theory and Einstein's relativity, each breakthrough has revealed previously hidden connections within nature.”
- **Figure 2.1:** “Modern physics is built upon two highly successful but fundamentally incompatible frameworks: quantum mechanics and General Relativity.”
- **Figure 5.1:** “SYMMETRIA proposes that reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.”

The existing Figure 1.1 caption is adjacent and visible but lacks the Λ qualification. The proposed Figure 2.1 caption appropriately removes “fundamentally incompatible” without suggesting either theory fails in its validated domain. Semiclassical gravity and effective-field-theory treatments are useful in appropriate regimes; the unresolved issue is a complete, empirically established quantum-gravity framework. The proposed sentence is acceptable as written, though a future editorial revision could say explicitly: “Although effective and semiclassical treatments are useful in certain regimes, a complete, experimentally established framework reconciling quantum physics with gravity remains an open research challenge.”

For Figure 5.1, explicit untested status is necessary and the proposal is directionally correct. The smoother option avoids “hypothesis/proposes” repetition while preserving the same epistemic caution:

> SYMMETRIA presents the following as an untested hypothesis: reality may emerge from deeper layers of symmetry, information, constraint and organisation. Matter, energy, spacetime and physical laws may represent higher-level expressions of underlying organisational principles operating beneath observable reality.

The Figure 5.1 artwork itself contains declarative in-image statements (for example, “Symmetry is fundamental” and “Nilpotent balance underlies nature”). Its existing exploratory footer and the proposed untested caption help, but the accessible long description should explicitly identify those statements as SYMMETRIA's conjectures rather than established physics. No caption or HTML change was made.

## Accessible text and full-resolution viewing review

The seven proposed concise `alt` strings and seven longer descriptions were reviewed. Keep the short alternative text distinct from the fuller accessible explanation; do not put equation caveats or the untested status only in image pixels. Recommended small `alt` edits:

| Slot | Review |
|---|---|
| Cover | Retain; it frames the image as an unresolved question, not a solved theory. |
| 1.1 | Replace “Einstein curved spacetime” with “Einsteinian curved-spacetime account of gravity”; include the Newton/Maxwell/Einstein historical progression. |
| 2.1 | Prefer “Diagram contrasts Standard Model particles and three non-gravitational interactions with general relativity's curved spacetime and their unresolved reconciliation.” This states the relation and gap more plainly than “face curved spacetime”. |
| 3.1 | Replace vague “sit above” with “Quantum field theory underpins the Standard Model; general relativity and open questions about quantum gravity and the dark sector complete the scene.” |
| 4.1 | Replace “Four open questions concern … fundamental constants” with “Four themes: quantum gravity, quantum interpretation, physical constants and experimental tests.” |
| 5.1 | Retain the explicit “hypothetical … not established” framing; ensure the long description also qualifies the artwork's assertive in-image statements. |
| 6.1 | Retain the planned/proposed framing; it correctly says unsupported outcomes should prompt revision and does not present the roadmap as completed research. |

The longer descriptions are substantially sound. In particular, they distinguish the Standard Model from gravity, explain the Λ=0 qualification, distinguish dark-sector effects from unknown underlying nature, clarify dimensional constants versus dimensionless α, and describe the Figure 6.1 programme as planned rather than experimentally completed. For accessible implementation, associate each longer description with its figure/caption (for example using a visible expandable description or a properly programmatically associated description).

Current article images are standalone `<img>` elements with generic `alt` labels; they are not wrapped in links to a full-resolution asset, and no longer accessible descriptions are present in that HTML. The three inspected existing WebP assets (Figures 1.1, 2.1 and 5.1) are each **1536×1024**, not the approved 1920×1080 PNGs. The required later integration should provide a discernibly labelled, keyboard-focusable and touch-usable link or equivalent zoom control to the **same exact image shown** at native resolution; do not link a caption to a different artwork variant.

At 390px and 320px viewport widths, equation labels and dense text within the 1920px illustrations reduce to only a few pixels high. These are proportional-size/CSS estimates, not real browser/device tests. At narrow widths, use the visible HTML caption plus the accessible long description to carry scientific meaning and retain usable image zoom. No mobile browser test was performed in this audit.

## Scientific references consulted

- CERN, [The Standard Model](https://home.cern/science/physics/standard-model/): identifies the electromagnetic, strong and weak interactions described by the Standard Model.
- Einstein, [Cosmological Considerations in the General Theory of Relativity (1917)](https://einstein-virtuell.mpiwg-berlin.mpg.de/VEA/SC79182752_MOD1044538897_SEQ1550488920_en.html), primary-text reproduction: background for the cosmological term in the general field equations.
- NASA, [Dark Matter](https://science.nasa.gov/dark-matter/) and [Universe Glossary](https://science.nasa.gov/universe/glossary/): gravitational evidence/inference for dark matter and the unknown nature of dark energy/matter.

## Final status and COPY TO CHAT

- Figure 2.1: **`PASS_SCIENCE_REAUDIT`**; exact candidate hash verified; owner visual approval retained.
- Figure 3.1: **`PASS_SCIENCE_REAUDIT`**; exact candidate hash verified; owner visual approval retained.
- Canonical GitHub Figure 1.1 PNG: **`CAPTION_ONLY_ACCEPTABLE_PENDING_WEBSITE_IMPLEMENTATION`**. The proposed Λ=0 caption and accessible description are adequate for the unchanged PNG, but the existing website uses a different WebP with a Λ term. The asset/caption mapping must be resolved in a later authorised website PR.
- Original PNG integrity: **7/7 verified** against the source manifest; no original paths or bytes changed.
- Current article branch/blob: `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` / `c235e33bbe3a291343125c94af73fe54a23491fa`; the earlier `390a…` discrepancy was not reproducible.
- Remaining gates: future website authorisation, matching image/caption/long-description implementation, accessible full-resolution control, and actual responsive browser tests. PR #10 remains open/draft/unmerged; no changes to website files or PR #5, no merge, no deployment.

### COPY TO CHAT

**Independent SYMMETRIA Paper One science re-audit:** Figure 2.1 (`a024ee52…`) and Figure 3.1 (`72bc6b2f…`) both **PASS_SCIENCE_REAUDIT** from fresh GitHub PNG bytes; their equation, particle/QFT labels and uncertainty wording are accurate. Figure 1.1's unchanged canonical PNG is **CAPTION_ONLY_ACCEPTABLE_PENDING_WEBSITE_IMPLEMENTATION** if its adjacent visible caption and accessible long description state that the displayed equation is the Λ=0 special case and a same-image full-resolution link is provided. Important: current website Figure 1.1 is a different 1536×1024 WebP that already shows a cosmological Λ term, so the Λ=0 wording must not be attached to that asset. The live article source is independently pinned at branch head `f6d8284…`, blob `c235e33…`; the prior `390a…` reading was not reproduced. All seven approved source hashes match. Report committed to the correction documentation branch; no website files, PR #5, originals, merges or deployment were touched.
