# SymTech Ventures v2.0 — Phase 1C: Approved Introductory Typography Adjustment + Real-Browser QA

**Prepared:** 17 November 2026 (GMT)  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Feature branch:** `feature/v2-space-research-website`  
**PR:** [#5 — existing draft](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Owner decision:** On 17 November, the owner approved **full-width introductory paragraphs** and **smaller introductory text on mobile**, while retaining **fully justified paragraphs**. The immediate source was a Discussion Series 1440px screenshot showing the lead text stopped short of the full content panel; the 390px screenshots showed excessive gaps between justified words.

## Implemented source changes (by Chat; do not duplicate)

At commit `3d55faacd09508c3c0f0fa51826391113c4877c1`, the common stylesheet `css/v2-programmes.css` was edited:
- `.page-lead`: replace `max-width:820px` with `max-width:100%`, so introductory text can use the same content width as surrounding sections.
- Add `@media(max-width:740px){.page-lead{font-size:1rem;line-height:1.7}}`. Desktop/tablet default remains `1.13rem` with `line-height:1.75`; at typical 16px root text size, mobile reduces the lead from about **18px to 16px**.
- The existing global `main p,.site-footer p{text-align:justify;text-justify:inter-word;hyphens:auto;overflow-wrap:break-word}` was **left unchanged**. No page content, article main bodies, images or nav changed in this edit.

**Important:** Fetch the actual latest PR #5 SHA before running. The preceding [Phase 1B-3 navigation report](../reports/V2_PHASE_01B3_FINAL_JUMP_KEYBOARD_AND_SCROLL_QA_20261117.md) was committed before the typography change and found no site code changes. Its results are a separate checkpoint, not post-typography evidence.

## Finite verification assignment

1. Check out/fetch the actual latest feature branch, record starting SHA. Run the **full exact-branch regression** `python3 -u docs/reports/scripts/v2_stage8_qa.py` after this CSS change; record real exit code/HTML and browser counts. Do not pretend the earlier Phase 1B regression covers this new head.
2. With real local HTTP + Chromium/Playwright, inspect at **320, 390, 740, 768, 1440 px** the computed CSS of actual `.page-lead` elements on **Discussion Series, About, Contact, BridgePoint, Research and NSRP** (and other v2 pages using `.page-lead`, where relevant). Record `font-size`, `line-height`, computed `max-width`, actual bounding rect/parent content width, `text-align` and `document.documentElement.scrollWidth - clientWidth`.
3. At 1440px, confirm Discussion lead now spans the `.page-content` available width, instead of being capped at 820px; at 390 and 320px confirm the smaller **16px** lead remains readable, justified and does not overflow. At 768px confirm desktop font style is not accidentally overridden. At 740px confirm intended breakpoint.
4. Capture updated screenshots (recommend viewport, not giant full-page images) for **Discussion Series and About at 390/1440**, plus **BridgePoint at 390**, with the intro visible. Compare qualitatively to Phase 1B captures; state whether the reduction alleviates wide inter-word gaps **without claiming they are entirely eliminated**. Avoid switching body prose to left alignment: that was not authorised.
5. Sanity-check keyboard navigation remains available on the four long pages. A previous Phase 1B-3 report claims a keyboard PASS, but one NSRP mobile entry lists the final target top **3808px in an 844px viewport** while also calling it a successful settled scroll. **Treat that entry as not conclusive of target visibility**; verify the actual target is inside viewport or explain geometry/error. Do not rewrite reports retrospectively or silently dismiss conflicting evidence. No broad extra navigation redesign required.
6. **Only if real technical defects arise from this CSS change** make a minimal correction, followed by a second exact-branch full regression. If all checks pass, make **no further site edits** and record tests honestly.
7. Keep six-link nav, 16 BridgePoint Planned entries, four available/12 planned paper entries, NSRP/SEIP 5×4, zero formal Publications, paused enquiry, no starfield, protected four paper bodies/seven figures each; the scientific/graphics changes belong in later Phase 3.

## Deliverable and status

Commit one evidence report at:

`docs/reports/V2_PHASE_01C_INTRO_TYPOGRAPHY_QA_20261117.md`

Include actual branch SHAs, full regression exit code, computed CSS per width (including width alignment), screenshot paths, before/after visual notes, the specific NSRP anchor caveat, and any remaining owner **Phase 1C design acceptance** questions. This pass validates a **specific approved typography change**, not blanket aesthetic approval or Phase 2 launch.

Read back committed report and verify PR #5 **open/draft/unmerged**, with no merge/deployment. Finish with a compact **COPY TO CHAT** with exact results.

## Operating rules

Use [DTSU v1.1](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md), real Europe/London time, truthful percentage milestones and an **estimated ETA on every update**. Suggested owner-selected model: **Luna, Medium effort, Standard speed**. Terra escalation only with explicit owner authorisation after documented hard failure. No image generation, scientific paper edits, publication, PR merge, deployment or DNS change.
