# Phase 1C Introductory Typography QA

**Branch:** `feature/v2-space-research-website`
**Starting SHA:** `48baa540ffdefd000a8927ee16f1f4b127dac1a0`
**Outcome:** PASS for specified CSS behavior and full regression; Phase 1C visual acceptance remains with owner.

## Full regression

Ran at the actual feature head after the approved CSS edit:

```sh
python3 -u docs/reports/scripts/v2_stage8_qa.py
```

Exit **0**. Reported 36 HTML files, 27 route visits, 320/390/768/1440 viewports, 16 sitemap entries, expected catalogue counts, preserved paper bodies/figures and no local-reference, alt-text, CSS-resource, browser-console or failed-local-response errors.

## Browser typography measurements

Python Playwright with system Chromium and local HTTP. For Discussion Series, About, Contact, BridgePoint, Research and NSRP, `.page-lead` returned the same values at each width below. Widths are lead and parent content-box widths; document overflow was zero in every sample.

| Viewport | Computed font / line height | max-width | Lead = parent width | Alignment | Overflow |
|---:|---|---|---:|---|---:|
| 320 | 16 px / 27.2 px | 100% | 286 px | justify | 0 |
| 390 | 16 px / 27.2 px | 100% | 356 px | justify | 0 |
| 740 | 16 px / 27.2 px | 100% | 706 px | justify | 0 |
| 768 | 18.08 px / 31.64 px | 100% | 720 px | justify | 0 |
| 1440 | 18.08 px / 31.64 px | 100% | 980 px | justify | 0 |

At 1440, Discussion intro spans the full available `.page-content` width (980 px), rather than the former 820 px cap. Mobile uses the intended 16 px size; tablet at 768 retains desktop sizing. At 740 the mobile rule still applies. Justification remains active; smaller mobile type reduces, but cannot guarantee elimination of, inter-word gaps.

## Captures and anchor caveat

Fresh viewport screenshots: `docs/reports/screenshots/phase1c-discussion-series-390.png`, `phase1c-discussion-series-1440.png`, `phase1c-about-390.png`, `phase1c-about-1440.png`, and `phase1c-bridgepoint-390.png`.

Rechecked NSRP `#proj-5` at 390×844 after smooth scrolling: `scrollY=4067`, target top `100.36`, bottom `169.45`, viewport height 844, document scroll height 5289. The target is in view; this resolves the prior Phase 1B-3 report's inconsistent 3808 px/top-position note for the current head.

No code change was needed. Phase 1C validates the approved typography adjustment, not blanket aesthetic acceptance. Mobile spacing and home hero-art selection remain owner visual decisions; Phase 2 has not started. No research/article content was changed.
