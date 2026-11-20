# SymTech Ventures v2.0 — Phase 1B-3: Final Jump Navigation Keyboard + Settled Scroll Verification

**Prepared:** 17 November 2026 (GMT)  
**Repo:** `SymTechVenturesOrg/symtechventures.github.io`  
**PR:** [#5 — existing draft](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Feature branch:** `feature/v2-space-research-website`  
**Verified starting head:** `4e236619408d2be9af6d06df19469412da7d5db9`; re-fetch actual PR head before work.  
**Task type:** ONE finite, **QA-only first** follow-up to [Phase 1B-2](../reports/V2_PHASE_01B2_ANCHOR_ACTIVATION_VERIFICATION_20261117.md). The owner-approved three-phase plan remains layout → website art → selective paper-image corrections; Phase 2 is **NOT authorised** by this task.

## What is already proven

- [Phase 1B full regression](../reports/V2_PHASE_01B_LAYOUT_BROWSER_QA_20261117.md) **exit 0** for 36 HTML files and 27 route visits at 320/390/768/1440 px.
- Four long pages now contain **18 native fragment anchors with unique matching IDs**; Phase 1B-2 independently ran all **18 real pointer clicks** in Chromium at 390×844, confirmed the correct fragment and that target elements became visible, with no document horizontal overflow. **No website code changes** were required.
- **Keyboard activation**, **1440px representative pointer/keyboard activation**, **reduced-motion mode** and the precise **final smooth-scroll resting position** are still unverified.

**Important nuance from the 1B-2 report:** the test waited for a target to **enter the viewport**, not necessarily for smooth scrolling to **finish**. Reported target top coordinates **554–838 px in an 844px viewport** often put the heading near the bottom edge. These support target visibility, **not assured final alignment near the top**. Do not mark resting position PASS based solely on hash or `is_visible()`.

## Finite deterministic browser test — no repeated unproductive Tab loop

Using the actual checked-out feature head, local Python HTTP, Playwright/system Chromium:

1. Capture browser/version, current SHA, CSS `scroll-behavior`, viewport and a script with explicit assertions and bounded timeouts. For each case start at the top by reloading the page.
2. **Four deep links at 390×844 with keyboard Enter**, at least:
   - `/pages/bridgepoint.html` link `a[href="#space-research"]`
   - `/pages/discussion-series.html` link `a[href="#discussion-testing"]`
   - `/pages/nsrp.html` link `a[href="#proj-5"]`
   - `/pages/seip.html` link `a[href="#proj-5"]`

   **First establish focus predictably**, without assuming a fixed number of Tab presses. Try real Tab traversal with an explicit bounded 60-step focus search and log actual active element after each relevant step. If that loop fails to reach the expected link, stop and report that specific issue; **do not just allow a timeout on a fragment assertion**. Separately use `locator.focus()` then assert `document.activeElement === link`, and `locator.press("Enter")`; classify this as **focused-keyboard activation**, not proof of full Tab traversal. Use distinct results for Tab reachability and Enter activation. `expect(page).to_have_url(re.compile(r'#...$'))` or an exact `location.hash` wait shows navigation; it is **not** enough for scrolled positioning.
3. For these deep links and two representative pointer cases, record **before, intermediate, and settled** snapshots of `window.scrollY`, `document.scrollingElement.scrollTop`, target `getBoundingClientRect().top`, target height and `document.scrollingElement.scrollHeight`. Poll every ~100 ms for up to **2.5 seconds**, and classify scroll settled only after e.g. **three consecutive measurements with changes <2 px**. State if timeout, animation or bottom-of-page constraint precludes an exact top alignment. A visible target wholly at the bottom while scroll is still moving is **not** a settled result.
4. Compare **`reduced_motion="reduce"`** (CSS should use instant scrolling) for at least BridgePoint final category and NSRP final project. Check resulting target is visible, not under sticky header, and meaningful keyboard outline is present on focused anchor.
5. At **1440×900** exercise the four deep links above by pointer, with settled scroll/target geometry and no horizontal overflow. Optionally test keyboard on one representative desktop index.
6. Verify no source code change unless **a genuine browser-level defect is proven**. In that case make the smallest semantic CSS/HTML correction; rerun failed cases plus **full `python3 -u docs/reports/scripts/v2_stage8_qa.py`** if website code changes, and focused axe if landmark/focus semantics change. If only test approach is corrected, **DO NOT** repeat the heavy full regression; cite Stage 1B's real exit 0.
7. Avoid infinite retries or another ambiguous `scrollY=0` result. If the browser automation environment cannot focus the link, record the exact active element and failure after a bounded attempt; do not mislabel a testing limitation as a website defect.

## Report and stop

Commit exactly one new evidence report in the **same branch**:

`docs/reports/V2_PHASE_01B3_FINAL_JUMP_KEYBOARD_AND_SCROLL_QA_20261117.md`.

It must include a small **4× keyboard / 4× desktop / reduced-motion** outcome matrix, whether Tab reachability and Enter activation were separately shown, key scroll snapshots and settled-status determinations, the prior 18/18 pointer check explicitly identified as **Phase 1B-2** evidence, any source edits and precise rerun results. **Do not claim full WCAG conformance or Phase 1C owner visual sign-off.**

Read back committed report, verify PR #5 **open/draft/unmerged** and provide COPY TO CHAT with final SHA. No merge, deployment, new images, article changes, DNS, reactivation of enquiry or new PR.

## DTSU / model setting

Follow [DTSU v1.1](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md). Every visible update should include genuine GMT `HH:MM:SS`, completion %, and a **reasonably estimated ETA** (range if needed); start at 0%, report factual stages and only claim 100% after the GitHub report and PR verification.

**Recommended:** Luna / Medium thinking / Standard speed. Luna High only for a reproduced difficult debugger issue; Terra requires owner-authorised escalation. **This is the last stand-alone jump-nav verification pass; if it remains blocked, document the blocker for Phase 1C decision rather than automatically inventing another retry pass.**
