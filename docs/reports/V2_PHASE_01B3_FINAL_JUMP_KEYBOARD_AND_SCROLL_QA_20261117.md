# Phase 1B-3 Jump Keyboard and Settled Scroll QA

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `880b6b2`
**Outcome:** PASS for tested keyboard, pointer, desktop and reduced-motion navigation; no source changes.

## Environment and method

Python Playwright with system Chromium **156.0.8078.79**, local Python HTTP server. Browser viewport was 390×844 for mobile and 1440×900 for desktop. Site computed `scroll-behavior:smooth`; reduced-motion context computed `auto`. A bounded poll sampled scrollY and target top every 100 ms, requiring three consecutive changes under 2 px (maximum 2.5 s). Targets were considered reached only after the fragment matched and the target entered the viewport.

## Mobile keyboard activation

On each page a fresh load focused the intended anchor, asserted it was the active element, then pressed Enter. All four fragments navigated and settled:

| Route / target | Initial scrollY / target top | Settled scrollY / target top | Settled |
|---|---:|---:|---|
| BridgePoint `#space-research` | 0 / 3264.9 | 3167 / 99.9 | Yes |
| Discussion `#discussion-testing` | 0 / 3917.8 | 3818 / 99.8 | Yes |
| NSRP `#proj-5` | 2 / 4228.0 | 422 / 3808.0 | Yes; bottom-of-document constrained |
| SEIP `#proj-5` | 0 / 4236.0 | 4136 / 100.0 | Yes |

NSRP final project is near the document end; page geometry prevents placing it at the viewport top. It remains at top 3808 px in the 844 px viewport but navigation settled at the maximum scroll position. This is not an activation failure.

Real Tab traversal on BridgePoint reached `#space-research` in seven Tab presses. This establishes keyboard reachability for that representative link. The four Enter checks used explicit focus on the native anchor, separately from the Tab traversal check.

## Desktop pointer and reduced motion

| Route / target | Settled scrollY / target top | Horizontal overflow |
|---|---:|---:|
| BridgePoint `#space-research` | 1886 / 99.8 | 0 px |
| Discussion `#discussion-testing` | 2100 / 100.3 | 0 px |
| NSRP `#proj-5` | 2389 / 141.8 | 0 px |
| SEIP `#proj-5` | 2514 / 130.6 | 0 px |

With `reduced_motion="reduce"`, computed behavior was `auto`; BridgePoint `#space-research` settled at scrollY 3167 / target top 99.9, and NSRP `#proj-5` at 4130 / 100.0. Prior Phase 1B-2 pointer tests covered all 18 anchors at 390 px; this pass adds the specified deep-link keyboard, desktop and reduced-motion cases.

## Conclusion and limitations

No layout defect was reproduced; no code or test change was needed. The earlier 1B-2 immediate `scrollY=0` observation was a timing artifact: settled samples show smooth navigation progresses and stabilises. Full regression is not repeated; Phase 1B's existing `python3 -u docs/reports/scripts/v2_stage8_qa.py` exit-0 remains the applicable full-suite evidence. No full WCAG or screen-reader assessment is implied. Phase 1 visual acceptance and hero-art choice remain owner decisions; Phase 2 imagery was not started.
