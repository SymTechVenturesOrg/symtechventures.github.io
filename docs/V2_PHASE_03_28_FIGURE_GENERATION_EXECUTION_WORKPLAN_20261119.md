# SymTech Ventures v2.0 — Phase 3: Complete 28-Illustration Production and QA Workplan

**Version:** 1.0 · **Issued:** 19 November 2026 (GMT)  
**Status:** **EXECUTION WORKPLAN COMMITTED — NO MASTER APPROVED; NO FINAL v3 FIGURES GENERATED; NO WEBSITE INTEGRATION STARTED.**  
**Owner direction:** All **28** figures (the cover plus six figures in each of **four** reference-free SYMMETRIA discussion papers) must be regenerated in **one coherent ChatGPT image-generation style** and exported at **1920 × 1080 px (16:9)**, with enough provenance to reuse the same workflow on future papers. Earlier five Python/SVG-only drafts and ad-hoc AI generations **do not constitute an approved common visual master**.  
**Project lead and image producer:** Chat. **Optional independent end-stage reviewer:** Work (read-only and separately scoped). **Approval and release authority:** owner.

## 0. GitHub source of truth and immutable boundaries

- **Planning branch:** `planning/space-first-research-website-20261116`, [draft PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2). All *planning and QA specifications* live here until production is approved.
- **Website implementation branch:** `feature/v2-space-research-website`, [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5). Baseline before this plan: `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`. Re-fetch and record the exact HEAD before *every* production integration batch. **Never edit the live/default branch directly.**
- **Authoritative image-generation standard:** [v1.1 Full HD standard](standards/SYMMETRIA_ILLUSTRATION_GENERATION_STANDARD_v1_1_20261119.md); [per-image provenance JSON](standards/SYMMETRIA_IMAGE_PROVENANCE_TEMPLATE.json).
- **Authoritative slot-to-original mapping:** [28-row source/register and proposed v3 filenames](reports/V2_PHASE_03_ALL_28_ILLUSTRATIONS_REGENERATION_REGISTER_20261119.md).
- **Scientific review evidence:** [Chat/Work 28-figure reconciliation](reports/V2_PHASE_03_CHAT_WORK_RECONCILIATION_AND_OWNER_GATE_20261118.md); [controlled correction blueprints](reports/V2_PHASE_03_CHAT_STREAM_A_CONTROLLED_FIGURE_BLUEPRINTS_20261118.md); [approved A/B/C/D proposal](handovers/V2_PHASE_03_OWNER_APPROVAL_BATCH_A_AND_P3_SWAPS_20261119.md). The independent Work audit exists in the owner's private Library/Work conversation, **not committed publicly**.
- **Reference HTML:** `articles/symmetria/symmetria-paper-01.html` through `-04.html`. Source images are the **28 unchanged original WebPs** at `images/symmetria/paper-01` through `paper-04`. Original Git blob hashes live in the register; maintain all originals for provenance/rollback.
- **User decisions already made:** remake **all 28** in the original rich, sophisticated style rather than flat vector illustrations; **16:9 1920×1080** output; Paper 3 conceptual subject swaps **1.1↔3.1** and **5.1↔6.1** are approved; four source-embedded science corrections, Paper 4 evidence-focused Fig 4.1, and now Paper 2 broken-symmetry Fig 5.1 are in full regeneration scope.
- **Unchanged until separate authorisation:** four paper bodies/URLs, existing image references and image binaries, current responsive layout, image viewer and sticky navigation, website PR draft status, any public publishing. **Approval of this workplan is not approval of a generated master or final images.**

This document **supersedes the limited-figure implementation scope** in the earlier Phase 3 two-stream plan *only for image regeneration*. The already completed Work independent scientific audit stays valid, and the owner-selected Paper 3 subject alignment stays in force. The later 28-image owner instruction supersedes the earlier **defer** recommendation for Paper 2 Fig 5.1.

## 1. Operating model, ownership and stages

| Role | Responsibilities | Explicit limits |
| --- | --- | --- |
| **Chat — production lead** | Build baseline briefs; generate 1 master then each of 28 images through the same ChatGPT image-generation interface; perform controlled math/text repairs; log real parameters and artifacts; maintain provenance; prepare proofs/contact sheets; handle approved GitHub integration and regression | Do not silently change scientific claims or paper narrative; no merge or deployment without permission |
| **Work — independent end-stage verifier** | If commissioned after all owner-accepted proofs, examine all 28 final images against HTML captions and exact generated text; report critical/major/minor defects, consistency, provenance gaps and any accessibility/rights issues | Read-only, no edits to image files or PR #5, no automatic acceptance/merges; **not required to start production** |
| **Owner — scientific/editorial director** | Accept or reject master style; review each seven-figure paper batch; explicitly authorise insertion of accepted images/caption/alt deltas; approve release separately | No implied authorisation from task status updates |

**Execution is a set of finite, interactive passes**: a single master pilot, then four paper batches, consistency audit, controlled integration and final tests. Do not promise unattended/background production. At each handoff, leave GitHub records and a short `COPY TO CHAT` summary so work can continue in a new thread.

## 2. Standard production method and truthful reproducibility

**Artwork engine:** the **ChatGPT integrated image-generation interface** (`image_gen.text2im`) for **every figure's base visual**, using an **owner-approved master image as common style reference** and each figure's original image/adjacent text as *subject reference*. Do not use Python/SVG panel drawing as a substitute image-generation method. Post-processing is allowed for **exact controlled equation/label repair, colour management, cropping/extension without stretching, and WebP export**; record every such step separately. **Full source-independent exact equations are never entrusted to generative lettering without checking.**

**Fixed design system (subject to owner pilot acceptance):** cinematic scientific illustration; rich midnight-blue/near-black cosmic depth; sophisticated glowing cyan, electric blue, violet and restrained gold; serif editorial display type plus clear smaller captions; precise fine wireframes/field/particle geometry; flexible but coherent information hierarchy. **No repetitive generic backdrop, no flat presentation-card appearance, and no made-up decorative physics formulae.**

**Canonical request/extraction settings:**

| Field | Standard / logging requirement |
| --- | --- |
| Image interface | ChatGPT image generation; identify **tool interface** and any returned generation ID or metadata; model version is **unavailable unless exposed**, never claim a version from text inside an AI image |
| Input | One figure at a time, shared master prompt prefix from standard v1.1, **complete figure-specific human brief**, original subject asset, master visual reference, actual SHA-256 for each referenced file |
| Canvas request | Landscape **16:9**; request 1920×1080 if supported. Record **actual native output dimensions** independently of desired size |
| Background | Opaque; static/non-animated; one intended final proof per generation (retries are individually recorded) |
| Corrective typography | Inspect every textual element, symbol, arrow and equation; overlay correctly typeset symbols/labels only if necessary; record exact replacement source text and script or vector source, plus proof hashes |
| Final master | Reviewable, versioned **1920×1080 PNG**; never stretch an old 3:2 source or generated output to 16:9 |
| Website export | **1920×1080 WebP** in sRGB at **quality 85**; record codec/library/version if available, original/output dimensions, crop/extension method, byte size and SHA-256 |
| Filename | `pNN_cover_illustration_v3.webp` or `pNN_fig_S_1_illustration_v3.webp` within the same paper directory; **old originals are retained**, not overwritten |
| Provenance file | One JSON manifest per generated figure based on `SYMMETRIA_IMAGE_PROVENANCE_TEMPLATE.json`; include model metadata **only if actually exposed**, tool calls, prompts, IDs, original SHA, master SHA, iterations, repairs, assertions and owner acceptance |

**Honesty principle:** the original figure-generation engine is not proven from GitHub; the current tool may not expose a stable build number, hidden parameters or a deterministic seed. Replaying a prompt may yield a *similar* image, not byte-identical pixels. The purpose of the documentation is consistent, auditable production—not a fictitious promise of exact repeatability.

## 3. Phase gates, deliverables and conditions to proceed

| Gate | Task and lead | Required deliverables | Proceed only when |
| --- | --- | --- | --- |
| **G0 — Source freeze** | Chat confirms HEAD, copies source ledger and captions, computes original SHA and 28-asset references | Immutable 28-row index, original SHA checks, scientific risk notes, style-reference hashes | All 28 original files and their HTML slots accounted for |
| **G1 — Master pilot** | Chat generates **P1 Fig 3.1** in 16:9 using the existing original image as subject/style guidance | 1920×1080 candidate PNG + WebP, full human prompt/real tool metadata, old/new compare, corrected Standard Model copy, mobile legibility trial | **Owner explicitly approves a single visual golden master** and exact wording. If rejected, iterate pilot only |
| **G2 — Freeze style** | Chat registers chosen master SHA and standard v1.1 style settings | Named immutable master reference, prompt-prefix version and output/export provenance | Owner accepts aesthetics independently of any unresolved mathematical text |
| **G3 — Paper 1** | Chat produces 7 figures (pilot counts as one), checks P1 3.1 and 5.1 corrections | Seven proofs, per-figure manifests, caption/alt proposals, 7× before-after gallery, status register | Owner accepts all seven or returns rejected IDs for revision |
| **G4 — Paper 2** | Chat produces 7 figures; prioritises Noether P/T and **actual broken symmetry** | Same deliverables; scientific proof for P2 4.1 and Fig 5.1 | Owner accepts seven proof slots; issues addressed in image itself |
| **G5 — Paper 3** | Chat produces 7 figures respecting approved subject swaps (see §5) and Dirac qualifications | Same deliverables, source-to-slot swap map, mathematical glyph review | Correct subject at each section, no false generic-Dirac equivalence |
| **G6 — Paper 4** | Chat produces 7 figures including “elegance is not evidence” | Same deliverables, explicit evidence-status labels | All seven visually/scientifically owner-approved |
| **G7 — Whole-set QC** | Chat builds common 28-up gallery and validates all hashes, exports, captions, alt, rights/provenance gaps | 28-piece style contact sheet, all per-image manifests, difference register, editorial issue list | No blocking scientific, spelling, file-format or coherence failures; owner accepts unified series |
| **G8 — Independent Work pass (optional but recommended)** | Owner commissions one bounded Work review of **final** assets vs pinned paper sections | Read-only findings table and COPY TO CHAT handback | Blocking errors corrected; owner decides whether extra review is necessary |
| **G9 — Controlled website integration** | Chat changes only explicit image refs/alt/captions and approved 28 v3 binaries in **draft PR #5** | Versioned assets, exact before/after mapping, preserved original SHA, protected-body test with **specific expected diffs**, rollback instructions | Owner has authorised *site insertion*, exact-branch regression/visual QA green |
| **G10 — Owner final acceptance** | Owner inspects live-equivalent unpublished preview on desktop and phone | Full handback, CI links, visual proofs, 28-row completion matrix, unresolved limitations | Explicit owner acceptance. **PR #5 stays draft/unmerged until a separate release order** |

**Workflow note:** G1 includes the first of 28 final illustrations. Count figures by **accepted unique slots**, not by number of generation attempts. G3 should deliver seven total for Paper 1, not seven on top of the master.

## 4. All 28 illustration tasks — source-caption-grounded subjects

Source subjects below are taken from the four existing HTML papers at `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`; planned corrections follow the reconciled audit. These are **generation briefs**, not claims that these images already exist. The canonical source path and original SHA for each slot are in [the 28-row register](reports/V2_PHASE_03_ALL_28_ILLUSTRATIONS_REGENERATION_REGISTER_20261119.md).

| Paper | Slot | New subject and figure purpose | Required scientific/editorial check | Risk/priority | Reserved versioned asset |
| --- | --- | --- | --- | --- | --- |
| P01 | Cover | Why physics still needs a unified framework; distinguish powerful existing results from unresolved questions | Keep status of a deeper unification explicitly open | Standard | `p01_cover_illustration_v3.webp` |
| P01 | 1.1 | Historical progression: Newton, Maxwell, Einstein; successful advances and new questions | Historical claims; avoid a purported historical 'consciousness' endpoint | Medium | `p01_fig_1_1_illustration_v3.webp` |
| P01 | 2.1 | Quantum theory and general relativity; domains of success and open unification problems | Avoid universal claim that QM and GR are simply inconsistent in all regimes | Medium | `p01_fig_2_1_illustration_v3.webp` |
| P01 | 3.1 | Present-day particle physics plus gravity; difference between electroweak and speculative grand unification | Correct Standard Model: electromagnetic, weak, strong described; EW unified, strong not unified | HIGH — master pilot | `p01_fig_3_1_illustration_v3.webp` |
| P01 | 4.1 | Open questions and limits of present models; scientific uncertainty | No unsupported solved/unsolved certainty; distinguish observation from inference | Medium | `p01_fig_4_1_illustration_v3.webp` |
| P01 | 5.1 | SYMMETRIA exploratory nilpotence/symmetry/information framing | N²=0 does not imply AN+NA=0 for arbitrary A; mark physical emergence speculative | HIGH | `p01_fig_5_1_illustration_v3.webp` |
| P01 | 6.1 | Proposed research programme: formalise, model, predict, test | Stages are a roadmap, not completed experimental milestones | Medium | `p01_fig_6_1_illustration_v3.webp` |
| P02 | Cover | Symmetry across nature, mathematics, and physical law | Avoid implying all visual symmetries establish dynamical symmetry laws | Standard | `p02_cover_illustration_v3.webp` |
| P02 | 1.1 | Symmetry from natural patterns to theoretical physical symmetries | Prior figure/caption mismatch; follow actual introduction, not source filename alone | Medium | `p02_fig_1_1_illustration_v3.webp` |
| P02 | 2.1 | Natural symmetry in crystals, shells, snowflakes and organisms | Distinguish approximate natural patterns from exact mathematical invariance | Medium | `p02_fig_2_1_illustration_v3.webp` |
| P02 | 3.1 | Examples of invariance under defined transformations | Precisely identify object, transformation, and invariant; avoid equations without definitions | Medium | `p02_fig_3_1_illustration_v3.webp` |
| P02 | 4.1 | Noether continuous symmetries and conserved quantities contrasted with discrete P and T | Correct parity/T counterexamples and global-phase versus gauge redundancy; in-image qualifications | HIGH | `p02_fig_4_1_illustration_v3.webp` |
| P02 | 5.1 | Broken symmetry and emergence; a genuine concrete example such as ferromagnetic ordering | Owner's expanded 28-image scope supersedes earlier 'defer'; don't substitute general symmetry for symmetry breaking | Medium | `p02_fig_5_1_illustration_v3.webp` |
| P02 | 6.1 | SYMMETRIA's proposed symmetry-driven research questions | Explicitly hypothetical; avoid established claims of generated forces/spacetime | Medium | `p02_fig_6_1_illustration_v3.webp` |
| P03 | Cover | Nilpotence as an algebraic notion and open foundational questions | N≠0 and some finite power vanishes; if displaying N²=0, identify square-zero special case | Standard | `p03_cover_illustration_v3.webp` |
| P03 | 1.1 | Continuous symmetry and conserved quantities as introduction to deeper algebra | Approved conceptual swap: subject reference 03_rowlands_conceptual_route.webp, NOT old slot's mismatched graphic | Medium — approved swap | `p03_fig_1_1_illustration_v3.webp` |
| P03 | 2.1 | Nilpotence: nonzero algebraic object with vanishing powers under specified multiplication | Avoid interpreting algebraic zero as vacuum or absolute absence | Standard | `p03_fig_2_1_illustration_v3.webp` |
| P03 | 3.1 | Rowlands: duality, anticommutativity and specified nilpotent structures | Approved swap: subject reference 03_symmetry_to_nilpotence.webp; formulas must be independently verified | Medium — approved swap | `p03_fig_3_1_illustration_v3.webp` |
| P03 | 4.1 | Dirac theory and specified Rowlands nilpotent algebraic correspondence | Generic N²=0 alone does not prove general Dirac equivalence; no empirical validation | HIGH | `p03_fig_4_1_illustration_v3.webp` |
| P03 | 5.1 | Three meanings of zero: algebraic, zero-totality proposal and quantum-field vacuum | Approved swap: subject reference 03_nilpotence_to_mathematics_and_reality.webp; distinguish concepts | Medium — approved swap | `p03_fig_5_1_illustration_v3.webp` |
| P03 | 6.1 | Open derivations, testable predictions and evidence requirements for nilpotent ideas | Approved swap: subject reference 03_zero_totality_vacuum.webp; no completed-test claim | Medium — approved swap | `p03_fig_6_1_illustration_v3.webp` |
| P04 | Cover | Mathematical elegance versus empirical truth | Mathematical beauty isn't evidence by itself | Standard | `p04_cover_illustration_v3.webp` |
| P04 | 1.1 | The pathway from mathematical possibility to physically testable explanations | Keep speculative maths separate from measured physics | Standard | `p04_fig_1_1_illustration_v3.webp` |
| P04 | 2.1 | Mathematical predictions that survive observation | Illustration must not invent data, experiments or exact numerical results | Standard | `p04_fig_2_1_illustration_v3.webp` |
| P04 | 3.1 | Economy, symmetry, coherence and explanatory reach as aesthetic/model-building criteria | Earlier mismatch: illustration subject must match elegance, not just Noether alone | Medium | `p04_fig_3_1_illustration_v3.webp` |
| P04 | 4.1 | ELEGANCE IS NOT EVIDENCE: mathematics → consistency → quantitative consequences → comparison → revise/reject/retain | Owner already selected replacement over recaption; testing is a criterion, not an achieved result | HIGH | `p04_fig_4_1_illustration_v3.webp` |
| P04 | 5.1 | SYMMETRIA: clear algebra, consistency, quantitative recovery, falsifiable predictions | Uncompleted programme milestones cannot appear accomplished | Standard | `p04_fig_5_1_illustration_v3.webp` |
| P04 | 6.1 | Emergence, layered physical description and remaining open questions | Qualify speculative technology/consciousness/cosmology applications; match adjacent section | Medium | `p04_fig_6_1_illustration_v3.webp` |

**Total:** seven per paper, **28** unique slots. Retain exact original article figure order and number. A user's previous approval of P3's **source swap** must be applied to the *meaning of the new figure*, not by regenerating the already mismatched image in the wrong slot. Do not imply that an old image filename is a scientifically authoritative explanation.

### Critical content fixes — independent images must be accurate

- **P1 3.1:** the Standard Model **describes** electromagnetic, weak and strong interactions; electroweak theory unifies electromagnetic and weak, **not** all three. Proposed GUTs remain speculative.
- **P1 5.1:** `N²=0` does **not** entail `AN+NA=0` for an arbitrary operator `A`; the anticommutation relation requires a separately specified algebraic assumption. The idea of physical emergence from nilpotence is an **exploratory hypothesis**, not demonstrated reality.
- **P2 4.1:** Noether's first theorem addresses **continuous symmetries of an action** under relevant conditions. Parity and time reversal are **discrete symmetries** and are violated in certain interactions. Avoid conflating global charge-related symmetry with local gauge redundancy.
- **P2 5.1:** depict **actual broken symmetry**, not a generic array of symmetric shapes; clearly identify a model/example and do not imply all emergence results from the example.
- **P3 4.1:** Rowlands' claim concerns a **specific nilpotent Dirac-algebra construction**, not an arbitrary square-zero element implying general equivalence. In the graphic, distinguish specified mathematics, conjectural interpretation and unverified physical consequences.
- **P4 4.1:** show how an elegant mathematical idea must yield quantitative, discriminating consequences that can face evidence; never represent hypothetical test outcomes as observed facts.

**No public bibliography by default:** these are accessible reference-free exploratory discussion papers, not peer-reviewed submissions. Internal reviewers can cite external scientific sources in private QA notes. If the owner separately requests sources in future public papers, review editorial policy before changes.

## 5. Paper 3 subject-placement rule (previously approved)

A new set of illustrations eliminates the need to physically shuffle old image binaries, but their **subjects must follow the corrected slots**:

| Paper 3 slot | Source artwork used as SUBJECT reference | Intended new infographic topic |
| --- | --- | --- |
| **Fig 1.1** | `03_rowlands_conceptual_route.webp` | Continuous rotation/symmetry/Noether as a motivation for structural inquiry |
| **Fig 3.1** | `03_symmetry_to_nilpotence.webp` | Rowlands' three themes: duality, anticommutativity and specified nilpotent algebra |
| **Fig 5.1** | `03_nilpotence_to_mathematics_and_reality.webp` | Differences between algebraic zero, zero-totality and quantum vacuum |
| **Fig 6.1** | `03_zero_totality_vacuum.webp` | Open conceptual questions, formal derivation, predictions and experimental tests |

When integrating new v3 files, map each **final figure slot** to its new, correct image/alt/caption; **do not also apply the old swap references blindly**, which could reverse the intended result. Keep the original swapped source files only as provenance.

## 6. Detailed figure production procedure (repeat for each slot)

1. **Preflight:** pin current feature commit, owner-approved master hash, source image Git blob SHA, exact paper section, caption and alt; check current slot and conceptual swap mapping; identify scientific classification and uncertain claims.
2. **One-page creative brief:** write true subject, image purpose, 2–5 required visual elements, exact permitted lettering, forbidden claims, equations requiring controlled typesetting, palette/composition, resolution and mobile safe area. Keep the **same** master prompt prefix and record version.
3. **Generate base art:** use ChatGPT image generator with approved master style reference and source-subject context. Log human prompt, tool call date, available generation ID, actual native dimensions and intended generation settings. **Do not claim unknown model/seed** or mistake AI-printed metadata for real settings.
4. **Verify text/science before polishing:** inspect every in-image word and glyph at native scale; check equation operands, arrows, conservation conditions, numbers and purported experimental data. Reject or repair AI hallucinations. Correct with an auditable minimal text/compositing pass if needed; keep it stylistically consistent.
5. **Export:** compose/crop/extend to **16:9 without distortion**; create 1920×1080 master PNG and WebP quality 85 in sRGB; record image processing software/version/actual operations where known, bytes and SHA. Re-verify maths after export.
6. **Compare and caption:** original vs revised in one frame; proposed exact HTML alt/caption; figure-title and technical-meaning checks. Note rights/attribution gaps, if any, rather than assuming ownership from file presence.
7. **Visual/device QA:** inspect at native size, desktop Fit and 100%, landscape viewer, **390px portrait** and **844px landscape**; check key text is discoverable via independent zoom; caption remains intelligible even when the image is displayed small.
8. **Owner gate:** present approved-style comparison, manifest and any residual uncertainty. Status = `APPROVED`, `REVISION REQUESTED` or `REJECTED`; do not call a generated proof final before acceptance.
9. **Checkpoint:** update register/manifests and file hashes in GitHub after acceptance; preserve earlier revisions and package for next batch. Production files **must not be substituted into PR #5 merely because they exist**.

## 7. Verification matrix, failure response and release safety

| Layer | Tests / checks | Blocking failure response |
| --- | --- | --- |
| **Scientific claims** | Source-caption match, all embedded words, math identities and defined assumptions; known 5 high and 14 medium findings resolved or explicitly deferred | Stop particular figure, correct content, resubmit owner proof |
| **Visual unity** | Same master hash/palette/type/glow density, comparable quality in 28-up grid, no unapproved generic space filler | Return offending figure to generation; don't silently weaken style standards |
| **Image files** | PNG and WebP 1920×1080 / aspect 16:9 / sRGB / quality-85 export logged / decodable / SHA and bytes logged; original WebP untouched | Re-export; retain prior version as traceable artefact |
| **Placement** | Four HTML URLs; one cover + 6 figures per paper; proper captions and alt; P3 subject swaps preserved; no missing src; original files remain | Stop integration; correct exact map and re-run ledger |
| **Layout** | Existing sticky header, no overflow, source images displayed proportionally at 320/390/768/1440/1920px; 1920×1080 desktop fit and full-size | Re-check CSS/viewer; don't stretch image or hide text |
| **Viewer** | Open image by click/tap/keyboard in separate tab, original linked source, zoom in/out via mouse wheel, +/−, Fit, 100%, drag pan and simulated pinch; phone landscape | Stop deployment candidate; use exact branch browser QA |
| **Article regression** | `python3 -u docs/reports/scripts/v2_stage8_qa.py` exact-branch protected `<main>` checks + GitHub Actions `.github/workflows/phase2-draft-qa.yml` | Amend immutable expected text **only for owner-authorised changes**, retain strict comparison, rerun all checks |
| **Provenance and rights** | One JSON per source, hash and generation log, original source claims differentiated, rights/open issues recorded | Don't claim provenance or publication rights without evidence |
| **Owner release** | Every slot approved, independent review (if commissioned) reconciled, PR draft checked, final before/after gallery, owner release instruction | Keep PR unmerged and unpublished |

**Known original scientific issues:** some inaccuracies live **inside the image**; simply changing adjacent captions is insufficient because the website has an independent full-resolution image viewer. Readability must be tested in the new tab as well as inline.

**Rollback:** keep original 28 binary assets and original image references in version control; save new assets under v3 names, keep a machine-readable mapping `paper/slot/old path+SHA/new path+SHA/alt/caption delta/source commit`. A future rollback reverts the exact integration commit or restores those paths only, without deleting historic originals. Document the actual commit and verification run IDs; never guess.

## 8. Per-figure tracking, evidence, and DTSU v1.1

Use the following states in the canonical [28-row register](reports/V2_PHASE_03_ALL_28_ILLUSTRATIONS_REGENERATION_REGISTER_20261119.md):

`NOT STARTED → BRIEF READY → PROOF GENERATED → SCIENCE/TEXT QA → OWNER REVIEW → APPROVED → INTEGRATED → REGRESSION PASSED`.

If rejected, record `REVISION REQUESTED` and return to `PROOF GENERATED` with a new iteration. Log actual `date/time`, responsible reviewer, SHA and change reason. One generated retry does not count as a second approved figure.

**DTSU format (mandatory):** `[HH:MM:SS] NN% — <10–20-word factual progress sentence>; ETA <defensible duration or unknown>.` All times Europe/London, including GMT/BST as appropriate. Use distinct progress counters for (a) the **current finite production pass** and (b) **whole-project accepted figures**, avoiding misleading percentages. Send at the start, every meaningful milestone (roughly 10–20%), on blockers/revisions and at completion; **100% only when that finite deliverable passes its checks and is handed back**. If time cannot be estimated, say `ETA unknown`, not an invented promise. Do not suggest work is happening between chat turns unless a scheduled automation actually exists.

**Milestone tracker (illustrative, initial):** master not accepted = **0/28**; after Paper 1 seven owner-approved = 7/28 (25%); Paper 2 = 14/28 (50%); Paper 3 = 21/28 (75%); Paper 4 = 28/28 (100% **of figure proofs**, *not* Phase 3 site completion). Integration/regression/release remain separate gates.

**Evidence package after each paper:** `P0N_review_gallery.html` or equivalent, 7 original/new contact-sheet pairs, 7 final PNG + WebP, per-file JSON provenance, prompts/source briefs, exact captions and alt, scientific warnings, QA result sheet, and `COPY TO CHAT` summary with owner-acceptance needs. Keep working files in Chat/Library or a dedicated artefact area until ready; **do not commit unapproved binaries into the live website branch**.

## 9. Effort allowances and dependencies (not a guaranteed timeline)

| Active work component | Planning allowance | Dependency |
| --- | ---: | --- |
| Reconfirm baseline/creative briefs and produce pilot (including iteration/visual sign-off) | **1.5–4 h** | Owner master acceptance |
| Paper 1: seven-figure proof set, including pilot | **4–8 h** | Pilot approved |
| Paper 2: seven science-aware figures | **4–9 h** | Paper 1 style locked |
| Paper 3: seven figures, precise mathematics and swapped subjects | **5–10 h** | Paper 2 style stable |
| Paper 4: seven figures, empirical-evidence framing | **4–8 h** | Paper 3 accepted |
| Complete series audit, provenance completeness and owner review | **2–5 h** | All four sets produced |
| Optional final independent Work audit | **1–3 h** | Accepted 28 images |
| GitHub integration, protected HTML QA, browser regressions and rollback evidence | **3–6 h** | Owner authorises insertion |

**Interpretation:** these are **planning allowances**, not promises of uninterrupted autonomous activity or a scheduled delivery date. Figure generation varies with tool availability, visual revisions and accuracy issues. The pilot is a subset of Paper 1 work—**do not mechanically add its hours twice**. If repeated art-direction revisions or physics reviews are needed, update the plan and ETA honestly.

## 10. Next executable instruction and definition of done

**Next action:** Produce **one new 16:9 P1 Fig 3.1 master-style proof** using the original source artwork to anchor the established style. Correct the Standard Model statement *inside the figure*. Deliver both the review image and a record of **actual** generation metadata. Ask the owner to accept the **look and science** before proceeding to the remaining 27.

**Do not start G3/G4/G5/G6 finals until G1/G2 are accepted.** The user can request drafting individual figure briefs sooner, but no website integration until explicit visual approval.

**Phase 3 illustration production is complete** only after all **28** unique 1920×1080 proofs and their provenance and scientific/caption checks are owner-approved. **Phase 3 website implementation is complete** only after all approved v3 sources are integrated on PR #5, regression and responsive viewer tests pass on the exact HEAD, rollback evidence exists, and owner accepts. **Publication is a separate decision**; keep PR #2 and PR #5 drafts until explicit instruction.

**Scientific honesty:** the diagrams are conceptual aids for exploratory work, not peer-reviewed evidence or experimental demonstration of SYMMETRIA. Confirm each factual claim independently; disclose unresolved research questions rather than inventing certainty.
