# Phase 1B-2 Jump-Link Activation Verification

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `39f538c`
**Result:** Pointer navigation PASS for all 18 anchors; keyboard deep-link check incomplete.

## Browser setup

Actual local checkout served by Python `http.server`; Python Playwright with system Chromium, 390×844, default smooth scrolling enabled. Each pointer case loaded the page, reset `scrollY` to zero, clicked the native `.section-jump-nav` anchor, waited for the exact URL fragment and for the target heading to enter the viewport (maximum 2.5 s). All 18 targets were reached; all reported document horizontal overflow was 0.

| Page | Anchors | Pointer result at 390 px |
|---|---|---|
| BridgePoint | `maths-toolkit`, `symmetry-structure`, `quantum-nilpotence`, `space-research` | 4/4 pass; target tops after settling 749–838 px |
| Discussion Papers | `discussion-foundations`, `discussion-framework`, `discussion-reality`, `discussion-testing` | 4/4 pass; target tops 688–798 px |
| NSRP | `proj-1`…`proj-5` | 5/5 pass; target tops 554–821 px |
| SEIP | `proj-1`…`proj-5` | 5/5 pass; target tops 788–832 px |

The first Discussion anchor remaining at scrollY 0 was expected geometry: its target was already near the visible index. No defect was observed; no source change was made.

## Keyboard and desktop

The attempted keyboard probe did not establish link activation: it timed out waiting for a URL fragment after the tab loop, before confirming focus on the intended deep-link. This is a test-procedure limitation, not evidence of broken site navigation. The four required 1440 px pointer checks and reduced-motion comparison were consequently not completed. The earlier Phase 1B full regression remains the only full regression evidence: exit 0, 36 HTML files and viewports 320/390/768/1440; it was not repeated here because no source changed.

## Outcome and follow-up

All 18 native in-page links passed real pointer activation at 390 px with settled target visibility and no overflow. Keyboard access and 1440 px deep-link behavior remain unverified in this focused run; no layout-wide owner acceptance is implied. Mobile justified-spacing screenshots and home hero-art selection remain owner visual decisions. Earthrise imagery/Phase 2 was not started. No research content, article body or figures changed.

PR #5 remains draft and unmerged; no deployment.
