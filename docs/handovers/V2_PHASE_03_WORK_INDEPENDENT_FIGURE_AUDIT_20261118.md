# SymTech Ventures — Phase 3 Work Handover: Independent 28-Figure Scientific/Visual Audit

**Date:** 18 November 2026 GMT · **Assignment:** ONE bounded, read-only independent review
**Specialist:** ChatGPT **Work** · owner-select **Luna Medium, Standard speed** where available.
**Project lead:** Chat · **Project owner:** user
**Source repository:** `SymTechVenturesOrg/symtechventures.github.io`
**Feature baseline for source review:** `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f` on `feature/v2-space-research-website`; **verify actual SHA and pin it** before reading.
**Implementation PR:** [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5) — unmerged, unpublished
**Planning:** [Chat + Work parallel plan](../V2_PHASE_03_CHAT_WORK_PARALLEL_WORKPLAN_20261118.md) and [planning PR #2](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/2)

## Objective and independence

Independently inspect **all 28 original visual figures** in the four online SYMMETRIA discussion papers. For each, assess what it *actually depicts and says*, whether its claim is scientifically or mathematically misleading, whether it belongs beside its present adjacent caption/section, and whether its contents remain accurate when independently enlarged/shared without the caption.

**Conduct your first-pass audit from the actual HTML/images before consulting Chat's older critique.** Then make a second clearly labelled comparison with the existing [28-figure review](../reports/V2_STAGE_09_SYMMETRIA_28_FIGURE_SCIENTIFIC_EDITORIAL_REVIEW_20261117.md) and [minimal reference-free corrections plan](../reports/V2_STAGE_09_ROWLANDS_DISCUSSION_PAPER_MINIMAL_EDITORIAL_PLAN_20261117.md). This preserves the value of an independent view.

## Exact source files

- `articles/symmetria/symmetria-paper-01.html`, `-02.html`, `-03.html`, `-04.html`.
- 7 actual figures per paper in `images/symmetria/paper-01/`, `paper-02/`, `paper-03/`, `paper-04/`, all WebP.
- Read *the exact adjacent figure caption and nearest relevant passage*, not just the image filename or alt text. Do not assume a filename describes the image content.
- The current independent full-resolution image viewer means embedded statements may be seen without their HTML captions; consider this in the risk ratings.
- Existing workplan [Phase 3 scope](../V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md) describes the strictly selective approach.

## Scientific/editorial policy

These are **reference-free exploratory discussion papers inspired by Dr Peter Rowlands' nilpotent formulation**, not peer-reviewed research. **Do not require references or academic bibliographies in the papers.** For your private/internal audit, check assertions using credible physics and Rowlands sources where helpful, recording direct links and confidence. Distinguish established standard results, literature-derived specified algebraic reformulation, proposed SYMMETRIA hypotheses, visual analogy and experimentally demonstrated facts. A true source claim is not a proof of SYMMETRIA's overall framework.

Specific hazards to detect independently include:
- Unqualified parity/time-reversal invariance, inaccurate discrete-vs-continuous Noether language or global-vs-local gauge claims.
- Assuming `N²=0` automatically forces anticommutation with arbitrary operators.
- Claiming generic nilpotence alone proves algebraic equivalence with Dirac theory.
- Figure subjects that do not match their caption (especially Papers 2–4); mathematical glyphs that look like statements but have missing components.
- Overstated claims about speculative unification, empirical consequences, consciousness or technological applications.

## Exactly one requested report

Deliver `PHASE3_WORK_28_FIGURE_INDEPENDENT_AUDIT_20261118.md` as a reviewable Markdown report in the Work conversation. If connected GitHub write access and owner-approved review-only branch are available, it may be committed **only** as a documentation-only report on an isolated review branch; do not modify PR #5 or merge anything. A text report plus **COPY TO CHAT** is sufficient; do not block on GitHub write access.

The report must contain:
1. **Source/provenance:** actual commit SHA, files inspected, count/coverage, what was visually observed vs inferred and any inaccessible figures.
2. A **28-row inventory**: paper / section+figure number / exact image path / observed graphic topic / caption topic / status **KEEP, KEEP+QUALIFY, RECAPTION, SWAP, REDRAW or DEFER** / evidence / severity **high, medium, low** / confidence / recommendation. Preserve seven entries per paper.
3. **Three-to-five critical findings**, with exact offending image text/formula and *minimal* source-grounded correction options; distinguish demonstrable scientific falsehood from conjectural framing.
4. **Image-caption mismatch matrix** for affected Papers 2, 3 and 4, especially Paper 3 candidate Figure 1.1↔3.1 and 5.1↔6.1 swaps; no silent file reassignments.
5. A short **reconciliation section** comparing your original findings to Chat's earlier review, naming agreements, disagreements and further checking needed.
6. **Ranked smallest-first change shortlist**, with reasons to **retain** most original figures if they are adequate.
7. **Risk and limitations** including no claim that this audit is peer review, no empirical validation, and no source image alteration.

## Scope restrictions

**Read-only task.** Do not produce or edit images, website pages, HTML/CSS/JS, old paper main blocks, asset filenames, programme status text, release documents or any publication output. Do not commission a second team/agent, contact third parties, perform external outreach or claim the papers are peer-reviewed.

**Stop condition:** the single 28-row report and handback are complete. No new task without another owner instruction. If actual image source cannot be inspected, say so explicitly rather than silently relying on filenames, alt text, existing Chat reports or model imagination.

## DTSU v1.1 and handback

At start and throughout this *finite audit*, provide honest **Europe/London timestamped** status lines such as `[HH:MM:SS] NN% — <factual finding/step>; ETA ~N minutes`, with a reasoned and revised ETA as needed. Do not claim asynchronous completion or invent progress.

Finish with an obvious **COPY TO CHAT** block summarising exactly: baseline SHA, inspected count, high/medium/low findings, three priority corrections, any caption swaps, report location, what was *not* verified and outstanding owner decisions. Include a direct link if the report was actually committed; otherwise paste its content or attach it for Chat to use. **No PR merges, publishing, Phase 2 changes or Phase 3 figure implementation.**
