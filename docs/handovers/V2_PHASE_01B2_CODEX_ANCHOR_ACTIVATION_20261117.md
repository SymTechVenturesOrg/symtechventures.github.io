# SymTech Ventures v2.0 — Phase 1B-2: Verify In-page Jump-Link Activation

**Date:** 17 November 2026 (GMT)  
**Task type:** Narrow follow-up to the successful Phase 1B regression; **do not redesign the website**.  
**Repo:** `SymTechVenturesOrg/symtechventures.github.io`  
**Feature:** `feature/v2-space-research-website` · existing [draft PR #5](https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/5)  
**Verified starting head before this handover:** `b560926ce02ace41c88ceb4e2e9a287b403d28b5`; fetch the latest branch and PR head at execution.  
**Evidence:** [Phase 1B browser QA report](../reports/V2_PHASE_01B_LAYOUT_BROWSER_QA_20261117.md); [original Phase 1B source QA](../reports/V2_PHASE_01B_JUMP_NAV_SOURCE_QA_20261117.md).

## Known status

The **full `python3 -u docs/reports/scripts/v2_stage8_qa.py` regression exited 0** at the Phase 1B head, with 36 HTML files, 27 browser route visits and 320/390/768/1440px checks. That is already evidenced. **No website source changes** occurred during Phase 1B browser QA.

In a separate **quick** keyboard/Enter spot-check at 390px, Codex reported `scrollY=0` immediately after activation, despite the exact target IDs existing. That did **not** establish actual anchor scrolling, and the report explicitly called it unverified.

Chat reviewed current source: each of the four indexes uses **native `<a href="#...">`** fragments, with 18 unique in-document targets; `js/v2-navigation.js` contains **no anchor-click interception**; `css/v2-site.css` uses `html{scroll-behavior:smooth}` (with `prefers-reduced-motion:reduce` using `auto`). Therefore one immediate `scrollY` read might run **before** a smooth scroll visibly progresses. **This is a plausible hypothesis, not a confirmed test diagnosis.**

## Finite task

1. Start with a real feature checkout at the verified current head, run local HTTP, Playwright and system Chromium. Record actual browser/tool versions and whether `html` computed `scroll-behavior` is smooth.
2. At **390×844**, exercise **all 18** native links in the four index menus:
   - BridgePoint (4): `#maths-toolkit`, `#symmetry-structure`, `#quantum-nilpotence`, `#space-research`.
   - Discussion Papers (4): `#discussion-foundations`, `#discussion-framework`, `#discussion-reality`, `#discussion-testing`.
   - NSRP (5): `#proj-1` through `#proj-5`.
   - SEIP (5): `#proj-1` through `#proj-5`.
   Reset the page to scroll origin for each test and capture `location.hash`, scrolling element's **scrollTop / window.scrollY** before and after, final `getBoundingClientRect().top` of target, and `document.scrollingElement.scrollHeight` vs viewport. Some first targets are near the index: **do not demand a large positive scrollY** if target is already visible or page geometry limits scrolling. The test's true criterion is that the linked target becomes suitably visible and is reached by the correct URL fragment.
3. For representative **deep links** (BridgePoint `#space-research`, Discussion `#discussion-testing`, NSRP/SEIP `#proj-5`), test **real keyboard Tab focus and Enter**, plus pointer click on the link. Confirm actual focus is on the selected `<a>` before Enter; using `locator.focus()` can diagnose but is **not** itself proof of Tab accessibility. Record the active element, key input and URL hash. **Do not infer link failure solely from an instantaneous measurement after Enter.**
4. With smooth scrolling enabled, use a bounded wait for animation progress / scroll position to settle (such as repeated snapshots over a maximum of ~2 seconds). Also rerun representative cases with `reduced_motion="reduce"` (or `scroll-behavior:auto` only in the **test browser**, not by editing site CSS), to separate animation timing from genuine broken navigation. Track the target viewport position and screen/page overflow; ensure header doesn't obscure headings. Test at **1440px** at least BridgePoint final group, Discussion final group and NSRP/SEIP final project.
5. **If a genuine bug is reproduced after this diagnosis**, apply the **smallest scoped** semantic HTML/CSS change and retest the exact failed link/viewport/mode; don't add unnecessary JS navigation. Then rerun the **full `python3 -u docs/reports/scripts/v2_stage8_qa.py`** after code edits and focused axe checks if semantics/focus change. If no code change is needed, **do not rerun the already-passing heavy regression**; accurately cite Phase 1B's exit-0 result.
6. Preserve the owner's design requirements: no starfield, dark palette, justified running paragraphs, six-link header, keyboard-visible focus, original four paper bodies/28 figures, 16 planned lessons, 4 online/12 planned papers, NSRP and SEIP 20 phases each, zero formal publications and paused enquiries. **Do not change justified text alignment**, introduce imagery, alter research or merge/deploy.

## Evidence deliverable

Commit **one** report to the existing feature branch:

`docs/reports/V2_PHASE_01B2_ANCHOR_ACTIVATION_VERIFICATION_20261117.md`

The report must state precisely:
- starting and final SHAs; browser commands/version; whether website code changed;
- results for **18 unique anchors at 390px** and four representative deep links at 1440px, including navigation mechanism (pointer vs keyboard), fragment, scroll/target geometry **after timed settling**, and any genuine failures;
- whether prior `scrollY=0` was caused by test focus/input/smooth scrolling or remains unresolved — distinguish **inferred** from **verified** cause;
- native link access for keyboard/pointer; visible focused link/target and no horizontal overflow;
- if code changed: **new** full regression actual exit status and focused axe evidence; otherwise the **prior** Phase 1B full regression result only, explicitly not rerun;
- any remaining manual/owner visual questions, particularly the mobile justified-spacing screenshots and exact home hero-art choice; **no full layout approval claimed**;
- final PR #5 fetch/readback confirming **open, draft, unmerged**, no deployment, plus concise paste-ready COPY TO CHAT.

**Never claim all 18 PASS if only representative links were actually tested.** A real failure requires clear evidence, not simply finding the target element.

## DTSU / effort policy

Follow [DTSU v1.1](https://github.com/SymTechVenturesOrg/symtech-ventures/blob/design/clean-slate-foundation-20261115/docs/standards/DTSU_Dr_T_Style_Updates.md). Always use a **real Europe/London clock**, accurate progress percentage, and **estimated ETA at every update** (give a reasonable range when uncertain; do not write ETA unknown). Start at 0% before execution and report real 10–20% milestones. 100% only after committing the evidence and re-verifying PR status.

**Recommended Codex:** Luna / Medium / Standard. Luna High only for reproducible unexpected debugger complexity; Terra escalation requires owner instruction. **This task is intentionally narrow. Stop after the handback.**
