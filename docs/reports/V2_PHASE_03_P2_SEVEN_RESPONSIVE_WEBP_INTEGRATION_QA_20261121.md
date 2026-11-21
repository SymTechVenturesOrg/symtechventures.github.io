# SYMMETRIA Paper Two — seven responsive WebP integration QA

**Status: PASS — integration and independent GitHub browser acceptance complete.**
**Date:** 21 November 2026 (Europe/London).
**Scope:** PR #13 only, on `feature/v2-paper-two-seven-cinematic-webp-20261121`, stacked on the PR #5 website branch at `f6d8284f8399bcc73928d4c2f92ae8bac6c9a92f`. PR #5, #11 and #12 were not modified. PR #13 remains draft, open and unmerged; nothing was deployed.

## Evidence and method

- Integration source commit tested by the successful screenshot-producing GitHub Actions run: [`d039123`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/commit/d0391237ae250d71b61600fd3a5bb895406dfc28).
- Successful non-deploying Chromium browser run and source screenshots: [Actions run 44897246061](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44897246061) (`pull_request` event; conclusion `success`). Subsequent [final-head verification run 44897425199](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44897425199) also passed on PR #13 head `0ff92932a715d5bd8c1e972b4ee34365a408527b`; the intervening commit modified only this QA report and the derivative manifest, not browser code or website assets.
- [QA screenshots and raw browser JSON artifact](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44897246061/artifacts/14704567736) — artifact ZIP SHA-256 `cb087bbfc20d8c2572c604f9781a6e1c477f311954af10f02156a145069c50b8`, browser JSON SHA-256 `5e4909667d07d4939fb1237d7eaef685c3154141aab6ee104b8e3193ca79a152`; retained on GitHub Actions according to its retention policy (originally 30 days).
- The Work runtime blocked Chromium launch with `socket() failed: Operation not permitted`. Following the handover, a read-only PR #13 GitHub Actions workflow ran Playwright 1.56.0 / Chromium on Ubuntu 24.04 with `contents: read`, no deployment credentials, no page publishing and no write token.
- The runner checked out PR #13 as a binary-capable Git checkout and independently recomputed PNG/WebP SHA-256 values, sizes, Git blob IDs, decodes, formats and dimensions. All seven PNG master bytes matched the seven approved PR #12 source SHA-256 values and Git blobs.
- Local WebP generation used Pillow 13.0.0 and libwebp 1.6.0, RGB, quality 93, method 6, Lanczos downsampling. The runner independently decoded all 21 committed WebPs.
- Preparation manifest retained as the frozen input contract; measured results are in the companion derivative manifest. Automated static checks confirmed seven ordered slots, unique `aria-describedby` targets, non-empty alt text, existing image references, and article text outside the seven converted image/caption slots unchanged.

## Approved PNG master identity

| Slot | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| Cover | 3,220,866 | `d1c2d02620c7b595c88dcfadf8e91ac4628f48d6b7770a1a55fa19cdc52b8a02` | `ecc305bb758cabd8d0760fc3faef978cf7b05a82` |
| 1.1 | 3,385,272 | `a53157058eda3e5d594e53284be40f8bb2c58fdb03c399b7401e7fefc525957c` | `60056cbfbaafddf025ab68dc0d5c37745764ebba` |
| 2.1 | 3,561,649 | `ccea83f05ded4bd9479ff624a65e4bbf8261afd2cbbd5e632ebcf0bcdfc3f421` | `65d8c7a21d68a93f0ae495e0f543f4f7779a100c` |
| 3.1 | 3,041,897 | `962c5465b7ed8d599e24688a173b4ec59f12bf9f7c3ce3288c8af5ccb224f07d` | `cb4cd8e072f1fe212d52cf082d782b316ed9ee29` |
| 4.1 | 2,688,456 | `bce9e58d6a5dbb058774051a88f1d76f44e926420f56ca9939440eef7512365c` | `6e887323f3436799708a6ca62105cf33d04c997d` |
| 5.1 | 3,062,628 | `201f88207b9bd0122a105c59c94b8a17f6d50740c310594718d5b3ababf685cf` | `3634d6375f45321e08cf3aa45ee308b9850bd0bd` |
| 6.1 | 3,062,952 | `e0590636813f7a720ca88b225011a5c2b4122a2ccce79263c9f3563f47c0bcff` | `babf8cc33ae4542c018b3a99d8b3817728ecc2e4` |

**PNG total: 22,023,720 bytes** (7 RGB PNGs, each 1920 × 1080). Masters are byte-exact copies; no original was overwritten. The corrected final PR #12 art was selected for Figures 2.1, 3.1 and 6.1.

## 21 WebP derivatives and checksum evidence

| Slot | Width | File | Bytes | Savings vs master | SHA-256 | Git blob |
|---|---:|---|---:|---:|---|---|
| Cover | 768 × 432 | `p2_cover_768w_q93.webp` | 131,354 | 95.92% | `912da17d9825c2fab6c5eec17e36522c2fc670d75dcb78746469f802c4c18701` | `4475ce023df60d208aa83808af45ee0753abc5a7` |
| Cover | 1280 × 720 | `p2_cover_1280w_q93.webp` | 306,530 | 90.48% | `6479049e2686a2359cb0f15916f9e022b44572c649f3a5db7f39ed4695743dba` | `11cad913b7b5c48e7abad448c1f207bb67474041` |
| Cover | 1920 × 1080 | `p2_cover_1920w_q93.webp` | 543,900 | 83.11% | `bdf2805ae2b55a12ef228e74e3adead7542f54667c013c4869df49e7c07e33a9` | `42934bf9a49d2fc8839c6b5303f686ece5d8f613` |
| 1.1 | 768 × 432 | `p2_figure_1_1_768w_q93.webp` | 144,898 | 95.72% | `b8c0ef18d3701391b271650627134b0c430ed59c419f030d5ae92a7ae4550c23` | `1a1747178991ad904fc8c5241c3d5c02ccf9e010` |
| 1.1 | 1280 × 720 | `p2_figure_1_1_1280w_q93.webp` | 339,056 | 89.98% | `077364f8cdf7a61fd5eeee12801dfef93acb8c82b170f2893c25968a543f62f6` | `2d28515a0fcfabc959d99cc261ee4076e0b295e9` |
| 1.1 | 1920 × 1080 | `p2_figure_1_1_1920w_q93.webp` | 599,318 | 82.30% | `2d8f2516356757c4d719c9e6e3981630c4116f4905e1c1524a2b455500b2aaa0` | `aa9c31d6123f8de0da40fd03e949122d970b4c97` |
| 2.1 | 768 × 432 | `p2_figure_2_1_768w_q93.webp` | 166,748 | 95.32% | `b0668937aa6251ef30e9517c0bd38a73cd7b5f1cec099567d5adc6ed09e75809` | `e6c37ce2e141e802b481ee5d4d14101829d9a607` |
| 2.1 | 1280 × 720 | `p2_figure_2_1_1280w_q93.webp` | 383,114 | 89.24% | `19e379d05679c95c400a6daefb3bc2ef466063e15b471ce0d8017948a0268601` | `825e049159eb70581ed03922e292e55e0628b365` |
| 2.1 | 1920 × 1080 | `p2_figure_2_1_1920w_q93.webp` | 693,680 | 80.52% | `449670ad7de3c22e6b00885025f583fe7c055b795814e9466b4a92e964705540` | `995837cd50fe3b79c590b037b5fa576558751c13` |
| 3.1 | 768 × 432 | `p2_figure_3_1_768w_q93.webp` | 133,598 | 95.61% | `0a8f41847f7b7f3895a6caf079800d24f66421da66e78bb9c3e7e854cd2d09b9` | `0b2116db55f0e96eda73116e61a13e8585e7f27d` |
| 3.1 | 1280 × 720 | `p2_figure_3_1_1280w_q93.webp` | 296,030 | 90.27% | `2797b83ff592c5c0c8e0cb843d7d6896fb3dfee6e27178ec9a641a120039bbe9` | `ca4750df1d438e56b3994901c181c26d8f8e6466` |
| 3.1 | 1920 × 1080 | `p2_figure_3_1_1920w_q93.webp` | 522,660 | 82.82% | `ac02732c16121153d047b012e9b891f82e65afa3ddb95c8cc62743effe4bc98d` | `098f681b65d73a5e2039e47224f768f31ae7571c` |
| 4.1 | 768 × 432 | `p2_figure_4_1_768w_q93.webp` | 112,060 | 95.83% | `afa02f2b3c0200e40d752a509fe828ff8b692cc714d7552f3228c57481d43a4a` | `9fd886b892f1188a9c820cd03b0ea5b7524d4463` |
| 4.1 | 1280 × 720 | `p2_figure_4_1_1280w_q93.webp` | 243,948 | 90.93% | `73f3f3d5f8d431dbabe06faa7eac7c6966d1c73a38fb24bda5d0164fb1b97365` | `367a95c032658bc1578823b25a621b0f4595462c` |
| 4.1 | 1920 × 1080 | `p2_figure_4_1_1920w_q93.webp` | 421,744 | 84.31% | `556bb5977b1db9a6358f1aef5e284613e4bbd32a02d1d6ae59a10641bdfae70a` | `09c6624f319992f5d478bc47b00f59dfd36f0bd0` |
| 5.1 | 768 × 432 | `p2_figure_5_1_768w_q93.webp` | 127,386 | 95.84% | `0984eed62a02d0a5c822a123be03f511f32da67a22b8535a1b72c774e5a5f44c` | `6fc8c5322a0dd3f26afcfb63ad0a55db46664a35` |
| 5.1 | 1280 × 720 | `p2_figure_5_1_1280w_q93.webp` | 307,164 | 89.97% | `9b135c7207a69cdda128cfcf22061c0d728583dc9a5cbc6701378ec5adeb2ae2` | `19e515f032caaa8aa5b63696e66ff282871d4b83` |
| 5.1 | 1920 × 1080 | `p2_figure_5_1_1920w_q93.webp` | 556,924 | 81.82% | `afceb53516b906260a08de2274eae7e856742417cb2705cbebcee4c4e1ae85b6` | `28497a6fb3b6b9e29d475732743c86a11b19dd7a` |
| 6.1 | 768 × 432 | `p2_figure_6_1_768w_q93.webp` | 120,592 | 96.06% | `5ea52aefb69912d77356182d26d84ec1a665b2aa35de24d77ee157489de4dcb7` | `f0cb4a504a371ec39834f52059bc6cb9ad5d91be` |
| 6.1 | 1280 × 720 | `p2_figure_6_1_1280w_q93.webp` | 287,414 | 90.62% | `413f75103578cdbfba19d5e24ec842a724cc17487faac735a6b24b57adbf4fd5` | `7de06d0bd0ac3c6335c50d10432e7e77e5a2a2ec` |
| 6.1 | 1920 × 1080 | `p2_figure_6_1_1920w_q93.webp` | 509,284 | 83.37% | `00bef554b6fb6e0f883ad437c1d476f396e4c021ffddcb0b87d45c5c3ad18dd8` | `9943a400b4e1364d95aa0dc441a9da1e2cecd295` |

## Measured seven-image transfer totals

| Responsive width | Seven WebPs | Seven PNG masters | Bytes saved | Reduction | Browser-observed encoded body / transfer |
|---:|---:|---:|---:|---:|---:|
| 768px | 936,636 B | 22,023,720 B | 21,087,084 B | 95.75% | 936,636 / 938,736 B (mobile-320-dpr1) |
| 1280px | 2,163,256 B | 22,023,720 B | 19,860,464 B | 90.18% | 2,163,256 / 2,165,356 B (desktop-1440-dpr1) |
| 1920px | 3,847,510 B | 22,023,720 B | 18,176,210 B | 82.53% | 3,847,510 / 3,849,610 B (desktop-1440-dpr2) |

Browser transfer figures are measured resource-timing bytes from seven actual selected WebPs in the local HTTP test, with transfer size including protocol/header overhead. These are not cellular-network performance promises. All 21 variants together occupy **6,947,402 bytes** in the repository; that is storage for all alternatives, not a single page-view.

## Browser, DPR and responsive selection results

| Test case | Viewport | DPR | Selected widths for all 7 figures | Encoded body | Transfer | Overflow | Result |
|---|---:|---:|---|---:|---:|---|---|
| mobile-320-dpr1 | 320 × 740 | 1 | 768, 768, 768, 768, 768, 768, 768 px | 936,636 B | 938,736 B | 320 / 320 px | PASS |
| mobile-390-dpr1 | 390 × 844 | 1 | 768, 768, 768, 768, 768, 768, 768 px | 936,636 B | 938,736 B | 390 / 390 px | PASS |
| mobile-390-dpr2 | 390 × 844 | 2 | 768, 768, 768, 768, 768, 768, 768 px | 936,636 B | 938,736 B | 390 / 390 px | PASS |
| tablet-768-dpr1 | 768 × 1024 | 1 | 768, 768, 768, 768, 768, 768, 768 px | 936,636 B | 938,736 B | 768 / 768 px | PASS |
| desktop-1440-dpr1 | 1440 × 900 | 1 | 1280, 1280, 1280, 1280, 1280, 1280, 1280 px | 2,163,256 B | 2,165,356 B | 1440 / 1440 px | PASS |
| desktop-1440-dpr2 | 1440 × 900 | 2 | 1920, 1920, 1920, 1920, 1920, 1920, 1920 px | 3,847,510 B | 3,849,610 B | 1440 / 1440 px | PASS |

- Passed: 320×740 DPR1, 390×844 DPR1 and DPR2, tablet 768×1024 DPR1, desktop 1440×900 DPR1 and DPR2. No horizontal overflow, JavaScript/console errors, failed resource requests or unexpected external requests were observed.
- Browser selected 768px WebPs for each mobile/tablet scenario; 1280px at desktop DPR1 and 1920px at desktop DPR2, across all seven figures.
- The browser keyboard-focused and activated all seven full-resolution PNG links; each native PNG tab decoded at 1920×1080. Cover was eager/high-priority; six article figures were lazy; all images kept their 16:9 aspect ratio.
- Deliberately blocking Figure 2.1’s 768px WebP left useful alt text, visible caption, long description and the full-resolution master link available. Keyboard focus is visible.
- The report verifies browser-emulated DPR; no physical handset, pinch-zoom session or real screen-reader run was performed.

## Scientific, editorial and mobile legibility audit

| Slot | QA decision | Qualification retained in article copy |
|---|---|---|
| Cover | PASS | Symmetry is an organising description; deeper symmetry-based explanations remain research, not a validated grand unification. |
| 1.1 | PASS | Living patterns are approximate; mathematical symmetry is precise invariance under specified transformations. |
| 2.1 | PASS | Distinct causes explain the illustrated patterns; no exact golden-ratio measurement or exact-fit spiral is asserted. |
| 3.1 | PASS | D₆ sixfold rotations/reflections are separated from translation of a finite object; moving it is not invariance at its original position. |
| 4.1 | PASS | Noether relates continuous symmetries of the relevant action to conserved quantities; the mechanical angular-momentum example states no net external torque. |
| 5.1 | PASS | V(φ) is identified as a one-dimensional double-well sketch, not the full Mexican-hat field potential or a universal mass-generation model. |
| 6.1 | PASS | The sequence is explicitly an exploratory, untested hypothesis, not established physics or experimental evidence of a unified theory. |

- Caption, descriptive alt and visible long description are selectable HTML text mapped to the approved artwork; every image exposes a unique `aria-describedby` target and a clear, keyboard-usable “Open full-resolution” PNG link.
- The phone screenshots show that embedded figure microcopy (especially the detailed labels in Figures 2.1 and 3.1) is **not legible at 320/390 CSS pixels**. The test does not claim otherwise. The figures’ scientific meaning and caveats remain available in visible caption/description text; opening the 1920×1080 original provides the intended enlargement route. Figure 6.1’s hypothesis disclaimer remains present in both the artwork and its surrounding text.
- Editorial order and article content around the original seven slots were preserved. No masthead, unrelated manuscript rewrite or external network dependency was added.

## Files changed in PR #13

- `articles/symmetria/symmetria-paper-02.html` — seven semantic figures, responsive `<picture>` sources, approved captions/descriptions, full-size links.
- `css/v2-articles.css` — minimal additive figure/image/description styling.
- `images/symmetria/paper-02/approved-20261121/` — seven immutable PNG masters plus 21 WebP derivatives.
- `.github/workflows/p2-seven-cinematic-browser-acceptance.yml` and `docs/reports/scripts/p2_seven_cinematic_browser_acceptance.py` — read-only acceptance workflow and tests.
- `docs/reports/V2_PHASE_03_P2_SEVEN_RESPONSIVE_WEBP_DERIVATIVE_MANIFEST_20261121.json` — complete PNG/WebP hashes, bytes, dimensions, compression and browser evidence.
- This report.

## Handover status

**Implementation QA: PASS. Owner visual/editorial approval of website integration remains pending.** PR #13 is still **DRAFT · OPEN · UNMERGED**, based on the PR #5 website branch at the pinned base SHA. No commits were sent to PR #5, #11 or #12; no merge or deployment occurred. Review the article and screenshots before any release decision.

## Post-review mobile caption readability correction (21 November 2026)

**Result: PASS.** After reviewing the 320px and 390px browser screenshots, overly wide inter-word gaps from justified figure captions were identified and corrected only in PR #13.

- [Presentation fix commit `a536c508`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/commit/a536c5083d4eb50ac69507842db156f4413b2733): the seven cinematic figure captions are explicitly left-aligned, with `0.95rem` font size and `1.65` line height. Their descriptive paragraphs are also left-aligned. The fix changes only `css/v2-articles.css`; no caption wording, article science, HTML, approved artwork or WebP bytes were edited.
- [Regression test commit `d1711366`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/commit/d1711366021d54666143c317f7e8cff42bacb005): the existing Chromium acceptance script now records computed caption `text-align`, font size and line height, and computed description alignment for every figure. In the 320px and both 390px/DPR configurations, it asserts left alignment, caption font size at least 15px and line height at least 24px.
- [Post-fix GitHub Actions run 44899270195](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44899270195): **SUCCESS** on exact tested head `d1711366021d54666143c317f7e8cff42bacb005`. Python compilation, binary preflight and the full six-configuration Playwright/Chromium suite passed. That encompasses all seven figures at 320px DPR1, 390px DPR1/DPR2, 768px DPR1 and 1440px DPR1/DPR2, plus full-resolution links and blocked-image fallback.
- [Post-fix screenshots, browser JSON and network-evidence artifact](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44899270195/artifacts/14705605629), archive SHA-256 `90f3b5c820541a35ee3e3c6b522a15ecd615cb1001c98031f02d630c334b6f66` (reported by GitHub Actions). The browser JSON contains the measured computed alignment and sizing properties for each figure.
- Tests remain browser-emulated and do not represent physical-handset or real screen-reader testing. The previously recorded limitations on legibility of microtext inside the artwork remain unchanged; full-resolution PNG links and explanatory HTML captions/descriptions remain available.

**Release gate unchanged:** PR #13 is draft, open, unmerged and awaiting owner presentation approval. PRs #5, #11 and #12 remain untouched; nothing was deployed.

## Mobile navigation and visible-paint acceptance follow-up

**Status: PASS — 21 November 2026.** During owner-facing screenshots review, the 320px mobile header showed a clipped navigation control. The page-level horizontal-overflow assertion was insufficient because the parent page clips overflow. Figure 2.1 also appeared blank in an intermediate screenshot, despite the browser reporting a decoded WebP; a paint-level regression check was therefore added.

- [Navigation CSS commit `ac2bd43`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/commit/ac2bd43de1e2948b820f270977c26053feaf8417) — **PR #13 CSS only**: compact header spacing and flexible brand text allow the six-link mobile menu button to remain wholly visible without changing the shared site stylesheet.
- [Menu acceptance script commit `0c027aaa`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/commit/0c027aaa2a0dcb0b0cdb59ac80399871946684d7) — 320px/390px computed button and brand coordinates must not overlap or leave the viewport; the six expanded links must be visible and the panel within the viewport.
- [Image-paint acceptance commit `f9afe8de`](https://github.com/SymTechVenturesOrg/symtechventures.github.io/commit/f9afe8debcdeaa3830493ce6adee6708600165b0) — explicitly waits for image decode and two animation frames, then captures actual image pixels for all seven figures at 320px/390px DPR1. A cropped image luminance-spread test must exceed a conservative blank-image threshold, with up to three capture attempts. This is visual-rendering regression evidence, not a semantic image-correctness assertion.
- [GitHub Actions run 44900259725](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44900259725) — **SUCCESS** on exact head `f9afe8debcdeaa3830493ce6adee6708600165b0`. All six existing responsive browser configurations passed, all seven full-resolution PNG links and accessibility assertions passed, all 14 DPR1 phone image-paint checks passed first attempt; `acceptance_status=PASS`, `issues=[]`.
- [Screenshot + browser JSON artifact 14705762478](https://github.com/SymTechVenturesOrg/symtechventures.github.io/actions/runs/44900259725/artifacts/14705762478), GitHub reported ZIP SHA-256 `469b8ebe71ba3b13e09a470107dc0b2487d4c30c6b97e7306addfb40239eb4b7`. Actual screenshots of Figure 2.1 and expanded navigation at 320px/390px were examined; both show the artwork painted and the menu and all six navigation links visible.

**Measured mobile navigation coordinates:** at 320px, menu left=220.390625px and right=304px, with brand ending at 212.390625px. At 390px, menu left=290.390625px and right=374px, with brand ending at 282.390625px. Both leave a right margin and avoid brand overlap. **Figure 2.1 image-paint luminance standard deviation:** 56.29 (320px DPR1), 56.24 (390px DPR1). The overall range across seven figures was 49.34–57.74. Screenshots and computed values are in the JSON artifact. This does not constitute physical handset or screen-reader verification.

**Scope/safety:** No image bytes, scientific manuscript text, captions or original PNG masters were edited. PR #13 is reserved for owner review; PRs #5, #11, #12 remain unmodified, and no merge or deploy was performed.
