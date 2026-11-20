# SymTech Ventures — Work Phase 3: SYMMETRIA 28-Figure Candidate Acceptance Audit

**Handover date:** 20 November 2026, Europe/London  
**Assignment:** one **bounded read-only** independent audit of manuscript/figure concordance and latest Chat-reviewed artwork candidates; prepare a concrete owner decision list.  
**Execution:** ChatGPT **Work**, Standard speed, Medium effort where available; DTSU v1.1 status reporting and COPY TO CHAT on completion.  
**Repository:** \`SymTechVenturesOrg/symtechventures.github.io\`  
**Website source:** \`feature/v2-space-research-website\` (open draft PR #5; **pin actual current HEAD SHA on entry**).  
**Documentation:** \`docs/symmetria-figure-production-standard-20261120\` (documentation-only, not yet merged).  
**No changes to site pages, images, branches, PR state, merges, DNS or deployments.**

## 1. Why this assignment is ready

The owner has reviewed the visual direction of new sets for the four online reference-free SYMMETRIA discussion papers. The approved stylistic target is the cinematic navy / cyan / gold illustrated physics-infographic language in Papers One and Two, with meaningful subject titles, explanatory subtitles and diagrams, and **no portraits or embedded "Discussion Paper X"/"Figure x.x" labels**. Exactly **seven slots per paper: cover plus Figures 1.1–6.1**, total 28.

These are **visual candidates**, NOT scientifically certified, publication-approved assets. The most recent Paper Three and Four native AI generation was 1672 × 941 despite earlier statements implying final resolution; a Chat-created **21-figure attachment package** has now proportionally resized them to exact 1920 × 1080. This geometric repair **does not validate the content or increase the source's intrinsic detail**. For each of Papers 2, 3 and 4 the package includes the seven full-size PNGs and a CSV of source dimensions, transformation and SHA-256.

**Required separate user-supplied attachment to this Work task:** \`SYMMETRIA_Work_21_Candidate_Figures_1920x1080_2026-11-20.zip\`, supplied in the Chat handover. Do not pretend the ZIP is in GitHub. If it is not attached/accessible, explicitly report that limitation; audit the repository's original 28, but do not claim the new candidate set was viewed.

**Paper One caveat:** its visual development in Chat used a separate "Unified Field Framework" document at some stages. The current website's Paper One is **"Why Physics Still Needs a Unified Framework"**. Paper One's seven new final candidates have **not** been incorporated in the 21-image ZIP and are not verified against the website's manuscript. Audit all seven **actual existing website images** for Paper One, and provide a separately marked missing/corrective candidate request before any attempt to replace them. Never silently relabel, reuse, invent, or approve them.

## 2. Binding production standard and source

Read these first:
- [Mandatory 28-figure production standard](../reports/V2_PHASE_03_SYMMETRIA_FIGURE_PRODUCTION_STANDARD_20261120.md) (including image dimensions, image-contained text exclusions and per-slot acceptance criteria).
- [Active phased workplan including 20 November owner override](../V2_PHASED_LAYOUT_AND_IMAGERY_WORKPLAN_20261117.md).
- Previous [read-only original 28-figure independent audit handover](V2_PHASE_03_WORK_INDEPENDENT_FIGURE_AUDIT_20261118.md) as methodological context only; do not reuse its results without checking current files.

The manuscript sources on the **exact pinned feature branch**:
- \`articles/symmetria/symmetria-paper-01.html\`
- \`articles/symmetria/symmetria-paper-02.html\`
- \`articles/symmetria/symmetria-paper-03.html\`
- \`articles/symmetria/symmetria-paper-04.html\`
- their corresponding original assets in \`images/symmetria/paper-01/\` through \`paper-04/\`.

Inspect the actual paragraph around each figure plus the immediately adjacent **external** figure caption. Do not rely only on filenames or older review summaries. If the website HTML has changed, use its actual current section/figure assignment.

## 3. Exact audit steps

**A — Independent first pass:** for each of the 28 website figure slots, read the manuscript/caption and independently inspect its currently referenced original WebP. Identify mismatch, misleading formula, unqualified claim, poor typography or weak image-to-text alignment. Preserve distinctions between (i) established physical law/mathematics, (ii) Rowlands-specific proposed algebra, (iii) SYMMETRIA's unvalidated conjecture, (iv) visual analogy.

**B — Candidate audit:** for the 21 new candidate images supplied in the ZIP (Papers 2–4), inspect them at full resolution; compare each to the exact HTML paragraph/caption and the original. Log **all written text, mathematical statements, visual arrows and inferred causation** that may mislead, even if the surrounding caption corrects them. Check no paper number or figure ID is printed *inside* any artwork. Check one standalone image per figure and actual dimensions of *each file* = 1920 × 1080; log file size and relevant readability concerns for mobile.

**C — Known high-risk test cases (verify, don't assume):**
- Paper 3, Figure 1.1: symmetric opposites/additive cancellation **do not imply** nilpotence N²=0 without a specified algebra.
- Paper 3, Figure 2.1: distinguish a nonzero nilpotent matrix whose square is zero from A+(-A)=0.
- Paper 3, Figure 4.1: generic Dirac operator (gamma.p - m) **is not square-zero in general**; do not imply an unspecified N²=0 proves equivalence.
- Paper 3, Figure 5.1: algebraic zero, zero-totality and quantum vacuum are separate notions.
- Paper 4, Figure 2.1: treat displayed prediction/data and decorative formulas as *illustrative*, with accurate notation, not real SYMMETRIA data.
- Paper 4, Figure 6.1: don't imply emergence from algebraic structure is demonstrated or uniquely predicted.
- Paper 2, Noether: continuous vs discrete transformations, parity and T violation, global/local gauge distinctions.
- Paper 1: verify actual online subject and images; do **not** substitute the separate unified-field document's illustrations automatically.

**D — Reconcile after independent review:** compare to [existing scientific and caption audit](../reports/V2_STAGE_09_SYMMETRIA_28_FIGURE_SCIENTIFIC_EDITORIAL_REVIEW_20261117.md) and [reference-free editorial plan](../reports/V2_STAGE_09_ROWLANDS_DISCUSSION_PAPER_MINIMAL_EDITORIAL_PLAN_20261117.md). Explain substantive agreements/disagreements; do not treat older "three priority images only" as a veto on the later owner's request for consistent new candidate artwork.

**E — Acceptance recommendation and staged integration plan:** give each of 28 slots one status: **READY FOR OWNER APPROVAL**, **REQUIRES SCIENCE CORRECTION**, **REQUIRES VISUAL CORRECTION**, **MISSING NEW CANDIDATE**, or **RETAIN ORIGINAL**, with severity and independent evidence. Work must make explicit that candidate QA is not experimental validation of SYMMETRIA. Provide a *proposed* safe later integration checklist, but do not implement it in this read-only assignment.

## 4. Deliverable

Provide exactly one review report: \`V2_PHASE_03_28_FIGURE_CANDIDATE_ACCEPTANCE_QA_20261120.md\` in the Work conversation. Include:

1. Pinned website HEAD SHA, working sources and independently inspected counts (**28 original + up to 21 new**), what could not be read.
2. A **28-row per-slot matrix** including actual site image, candidate image/availability, subject+caption fit, accurate scientific text/equations, exactly measured dimensions, style/legibility, risk severity, status and narrow fix.
3. A separate list of all **candidate failures** (even when the older image was acceptable), with reproduction/evidence and a precise safe replacement description.
4. One concise **Paper One source and new-artwork gap assessment**, specifically checking subject mismatches with the separate manuscript.
5. A documented set of image corrections and approval gates with **no changes made** to the website or PR.
6. Clear caveats: aesthetic approval != scientific verification; mathematics != experimental support; no peer-review claims; source artifact integrity preserved.

If writing back a report to GitHub is appropriate **and** an isolated review-only branch is explicitly authorised, put the report only there; otherwise deliver in the Work conversation. Do not block the handback on a GitHub commit. The user expects owner review, not deployment.

## 5. DTSU and COPY TO CHAT

Use the owner's **DTSU v1.1** with Europe/London timestamps, genuine completion percentage and evidence-based remaining-work estimate. Conclude with a clearly marked **COPY TO CHAT** message including: pinned SHA, exact original/candidate counts, failures by severity, the Paper One gap, candidate-image decisions, report attachment/link, and the **next precise owner approval** needed.

**Hard stop:** report and COPY TO CHAT delivered. No asset substitution, HTML change, PR merge, website release, DNS change or other modification.
