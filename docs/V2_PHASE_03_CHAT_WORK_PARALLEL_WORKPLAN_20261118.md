# SymTech Ventures v2.0 — Phase 3 Two-Stream Workplan: Chat + Work

**Version:** 1.0 · **Date:** 18 November 2026 (GMT)
**Status:** **PLAN PREPARED — NO PHASE 3 FIGURE/ARTICLE EDITS AUTHORISED; OWNER CORRECTION GATE PENDING**
**Website implementation:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5), `feature/v2-space-research-website`, baseline at planning time `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` (Phase 2 completed and regression-verified; recheck the live head SHA before using).
**Planning:** [draft PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2), `planning/space-first-research-website-20261116`.
**Work briefing:** [Phase 3 bounded independent audit](handovers/V2_PHASE_03_WORK_INDEPENDENT_FIGURE_AUDIT_20261118.md).
**Existing evidence:** [28-figure source-grounded audit](reports/V2_STAGE_09_SYMMETRIA_28_FIGURE_SCIENTIFIC_EDITORIAL_REVIEW_20261117.md) and [minimal reference-free editorial plan](reports/V2_STAGE_09_ROWLANDS_DISCUSSION_PAPER_MINIMAL_EDITORIAL_PLAN_20261117.md).
**Preceding plan:** [phase-gated site and imagery plan](V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md).

## 1. Purpose and boundary

Phase 3 is **selective, scientifically careful correction of existing SYMMETRIA discussion-paper figures and figure/caption placement**. Its scope is four accessible, reference-free, Rowlands-inspired discussion papers and **28 original WebP figures** (seven in each paper). It is **not** a review validating SYMMETRIA as a physical theory, nor permission to redraw all 28, add a bibliography, publish formal research or start Phase 3 production work immediately.

The owner has completed the Phase 2 *design/development* pass, including the full-width space website, sticky header, at-100%-zoom desktop layouts and independent interactive paper-figure zoom. Phase 2 remains **unmerged/unpublished** pending separate release authorisation. Phase 3 planning and read-only work may proceed without changing that boundary.

Two work streams may run **concurrently on distinct read-only/planning outputs**. They converge at a single evidence reconciliation and **explicit owner acceptance gate**. Only *after* that gate does Chat make approved implementation edits. Work must not edit implementation files, and Chat must not accept Work conclusions uncritically.

## 2. Responsibility and file ownership

| Workstream | Lead | Permitted work while streams are parallel | Output / ownership | Forbidden without owner approval |
| --- | --- | --- | --- | --- |
| **A — Chat: science specifications, controlled image design, GitHub integration plan** | Chat (continuous owner-facing project lead) | Freeze a figure-to-caption map; inspect the three known high-risk issues against exact figure/image sources; prepare source-safe replacements and qualification options, caption/alt candidates, file plan, rigorous change/rollback/QA specification; keep editorial records in planning docs | Chat's independent Phase 3 correction specification, figure ledger, proposed reversible implementation changes | Alter the original 28 image binaries, protected paper HTML main blocks, captions, URLs or integrity baseline before the correction set is individually approved |
| **B — Work: independent 28-figure scientific/visual audit** | ChatGPT Work (one bounded specialist run, read-only) | Visually inspect all 28 actual WebPs and adjacent original captions/sections at a pinned source SHA, check labels/formulae and whether full-size independent viewing exaggerates misleading statements, classify dispositions, report concrete evidence and uncertainty; then compare with existing editorial review only *after* first-pass findings | One standalone markdown audit, concise discrepancy matrix and **COPY TO CHAT** handback; Work owns only its audit report or a separate review-only documentation branch if expressly permitted | Modify feature PR #5, create new graphics, replace images, rewrite papers, edit main, merge, deploy, publish or turn discussion papers into peer-reviewed publications |
| **Owner** | Project owner | Decide what is corrected, retained, swapped or deferred | Explicit per-figure/change-set authorisation and release decision | None: approval of this workplan alone is not approval of actual figure changes |

**Concurrency rule:** Start Stream A's source inventory and science wording while Stream B independently assesses the existing files. Both can read the same immutable SHA, but must **not edit the same GitHub paths**. Work's audit must clearly distinguish its own observations from the earlier Chat review. If a contradiction survives reconciliation, label it as unresolved and seek an owner decision rather than silently choosing a version.

**Tooling:** Chat uses connected GitHub for project management, small docs and later bounded implementation. Work uses Work mode's browser/files if available; it must state what was actually opened and any access limitations. Where Codex is beneficial for deterministic image/page integration or exact browser QA, Chat may commission **one narrowly scoped engineering handover**, without creating a third autonomous planning stream. Prefer owner-selected Luna Medium / Standard speed in Work or Codex where selectable, and no Terra escalation without explicit owner consent.

## 3. Shared immutable inspection baseline (gate P3-0)

- Record the exact implementation SHA at the start of the Work run; do not assume the planning-time SHA will stay current.
- Papers: `articles/symmetria/symmetria-paper-01.html` through `-04.html`.
- Figures: `images/symmetria/paper-01/*.webp`, `paper-02/*.webp`, `paper-03/*.webp` and `paper-04/*.webp`; exactly seven actual images per paper.
- Keep each image mapped to *the section, displayed figure number, nearby caption, alt text, actual graphic subject, and what the image itself asserts*. A file's filename must not be mistaken for its true illustrated content.
- Original discussion-paper HTML is protected by `docs/reports/scripts/v2_stage8_qa.py`'s strong main-block baseline check, with only the already approved removal of redundant return buttons permitted. **Do not simply disable or weaken this baseline.**
- The new separate-tab full-resolution viewer is a presentation change: **caption-only qualifications may not accompany a shared image**. Prefer correcting false assertions *inside* a priority graphic.

## 4. Parallel execution schedule

| Milestone | Stream A — Chat | Stream B — Work | Gate / acceptance |
| --- | --- | --- | --- |
| **P3-0 · Snapshot** | Record current SHA, exact 28 asset paths, fig-number/caption ledger, preservation hashes and known regression command | Read the independent audit handover; confirm source access and the same pinned commit | Complete shared inventory; no implementation edits |
| **P3-1 · Independent parallel review** | Draft science-safe correction specifications for the **three priority graphics**; prepare candidate layout/figure-number adjustments and notes on direct image zoom/legibility | **Independently inspect all 28** images plus nearby paper passages/captions; rank inaccuracies, misleading graphical claims and placement errors; report observed evidence and confidence | Two separate review outputs, neither treated as scientific validation |
| **P3-2 · Reconciliation (Chat-led)** | Compare Work findings with current primary reviews; produce one 28-row decision ledger and precise proposed change-set, with controversies/unknowns highlighted | Work stops after its single report and **COPY TO CHAT**; optional single clarification only if a major claim cannot be resolved | **Owner reviews and explicitly selects** replacements, swaps and caption changes, including any deferrals |
| **P3-3 · Controlled correction production (post-approval only)** | Produce or compose *only approved* replacement figures; verified equation/label typesetting, preserve provenance and originals; propose corrected captions/alts; no blanket 28-image regeneration | No simultaneous implementation work; optionally review a finished approved replacement proof as a separately requested small task | Owner accepts each corrected graphic **and its paired caption/placement**, before GitHub source substitution |
| **P3-4 · Implementation and regression** | Implement smallest approved figure paths/alt/caption changes on feature PR #5, or hand narrow deterministic integration to Codex; update explicit integrity baseline for **only authorised differences**; exact-commit browser and visual QA | No editing feature branch; independent review only if requested | Same 4 URLs, 7 figures per paper, accurate page captions, native/interactive zoom still working, no broken refs; exact-branch regression PASS |
| **P3-5 · Close and owner sign-off** | Present before/after screenshots and image comparisons, 28-row disposition, deviations, rollback file map, PASS logs and remaining uncertainty | Findings archived, not portrayed as endorsements | Owner accepts scientific/visual *editorial changes*; PR #5 remains draft until a separate release instruction |

The *streams are parallel only during P3-0/P3-1*. P3-2 is a synchronisation/approval gate, after which Chat alone controls the implementation branch. Work cannot independently approve or merge anything.

## 5. Three priority scientific graphics — exact known issues

1. **Paper 1 — `paper-01/01_symmetria_perspective.webp` (Fig 5.1):** displayed `N²=0` does **not** imply `AN+NA=0` for arbitrary A. Candidate: remove the unconditional anticommutator or explicitly restrict to separately specified anticommuting operators. Do not present self-cancellation as physically established emergence.
2. **Paper 2 — `paper-02/02_noether_symmetry_conservation.webp` (Fig 4.1):** blanket mirror/parity and time-reversal invariance are false for some interactions; discrete P/T are distinct from Noether's continuous-action symmetries. Qualify weak-interaction parity violation, known time-reversal violations and global-vs-local phase/gauge wording. Correct the **image's own** misleading content.
3. **Paper 3 — `paper-03/03_dirac_nilpotent_structure.webp` (Fig 4.1):** distinguish Rowlands' **specific proposed nilpotent Dirac-algebra formulation** from the unsupported suggestion that an arbitrary `N²=0` establishes equivalence or a new experimentally verified unified theory.

**Prominent second-order reconciliations:** Paper 3 candidate **Fig 1.1 ↔ 3.1** source swaps and **Fig 5.1 ↔ 6.1** source swaps; check the adjacent text first. Paper 2 figs **1.1, 2.1, 3.1, 5.1, 6.1** and Paper 4 figs **3.1, 4.1** may need precise caption/subject reconciliation. Paper 4 cover's decorative, unattached integral glyph is optional secondary mathematical typography work. Work may uncover additional issues; no conclusion is automatic.

## 6. Figure disposition scheme and decision register

The reconciliation report must record **every one of the 28** original figures with:
`paper | figure number | original file | actual illustrated topic | nearby caption/topic | scientific classification | flaw/evidence | Work recommendation | Chat recommendation | reconciled disposition | owner approval | proposed file/caption/alt delta | source hash | QA status`.

Allowed dispositions: **KEEP**, **KEEP + QUALIFY**, **RECAPTION**, **REPOSITION/SWAP**, **REDRAW/RECOMPOSE**, **DEFER**. Separate an outright false formula from a theoretical simplification, visual metaphor, caption mismatch and purely cosmetic suggestion. Express uncertainty rather than forcing consensus.

**Production rules:** the source remains seven figures per existing paper and all original URLs; original WebPs remain versioned for provenance/rollback. Use WebP encoder quality **80** for approved new raster assets where appropriate; verify visually, rather than assuming 80 means percentage reduction. For equations, meaningful labels and captions, prefer controlled source-rendered/vector/HTML composition to generative text. Ensure mobile/desktop figure readability, accessible alt text and the existing click-to-view/zoom viewer.

## 7. Evidence and editorial integrity

- The papers are **accessible exploratory discussions**, inspired by Dr Peter Rowlands' nilpotent theoretical approach; they are **not formal peer-reviewed publications**. Do **not** add formal bibliographies, numbered citations, journal presentation or claim independent experimental proof.
- Internal reviewers may use credible external physics/Rowlands publications to check scientific statements. Put evidence links in **internal audit documentation only**, not the public paper body unless the owner requests otherwise.
- Review visual graphics as independent shareable artefacts: captions may not travel with them into the new full-resolution interactive viewer.
- Scientific sign-off means **editorial accuracy within agreed scope** only, never empirical validation of SYMMETRIA.
- Never silently change paper narratives, historical URLs, programme counts, the empty formal Publications index, BridgePoint Planned statuses or any private scientific drafts.
- Publish nothing, and do not merge PR #2 or PR #5 as part of this plan.

## 8. Verification and DTSU v1.1

After **every authorised** implementation change, preserve and check:
- `python3 -u docs/reports/scripts/v2_stage8_qa.py` on the exact checked-out commit; align owner-approved exceptions without weakening unrelated main-body integrity.
- Figure count **7 × 4 = 28**, all figure files/alt/caption pairings and unchanged source images where retained.
- Browser screenshot comparison on **320, 390, 768, 1440 and 1920 px** where relevant; inspect figure typography at full size. Verify keyboard focus, colour contrast, responsive/mobile horizontal overflow, the new-tab viewer, zoom/pan/pinch controls and no false image claims.
- File-specific before/after hashes, replacement provenance, static-link tests, accessibility failures and rollback instructions.
- Use concise **DTSU v1.1** with genuine Europe/London timestamps, factual percentage **of the finite task being performed**, and defensible estimated time remaining; no fabricated time or promised background activity. Work gives its own finite milestone DTSUs and ends with **COPY TO CHAT**.

## 9. Estimated active effort (planning allowances, not delivery promises)

| Work component | Approximate active effort | Overlap |
| --- | ---: | --- |
| Stream A read-only inventory, math/figure design briefs and rollback plan | **3–5 hours** | Overlaps Work audit |
| Stream B one independent 28-figure Work review/report | **2–4 hours** | Overlaps Chat's P3-1 |
| Chat reconciliation, owner decision matrix and selected image proofs | **2–5 hours** | Starts after Work handback |
| Approved figure production, small HTML/caption changes and full QA | **4–9 hours** | Starts after owner authorisation; may expand with re-render cycles |

**Total active effort:** roughly **11–23 hours** across the finite passes if the owner selects the three priority corrections plus limited caption/swaps. Because A/B overlap, this is **not a simple calendar ETA**. A greater number of redrawn figures, unresolved science or repeated image regeneration increases scope. No task is initiated asynchronously merely by this plan.

## 10. Definition of done and next steps

**Plan done:** both workplan and Work audit handover exist on the planning branch, with no paper changes.

**Phase 3 done only when:** independent audit completed; Chat reconciled every figure; owner explicitly approved actual modifications; approved graphics and captions checked; original URLs/seven-per-paper and rollback retained; exact-commit regression and visual/zoom QA passed; owner accepts the resulting editorial presentation.

**To start Work:** open **ChatGPT Work mode**, send the short Work launch request linking [its bounded handover](handovers/V2_PHASE_03_WORK_INDEPENDENT_FIGURE_AUDIT_20261118.md). Work does not start automatically when this workplan is committed. Chat can proceed separately on its *read-only* inventory and figure specifications.
