# SYMMETRIA Paper One — Seven Cinematic WebP Integration QA

**Date:** 20 November 2026 (Europe/London)  
**Status:** IMPLEMENTATION AND BINARY QA COMPLETE; **BROWSER_QA_BLOCKED**. The requested real viewport, keyboard, touch and network-transfer tests could not run in the available browser environment. Therefore, responsive website acceptance is **not claimed** and owner approval should wait for browser QA.  
**Repository:** `SymTechVenturesOrg/symtechventures.github.io`  
**Draft PR:** #11 — https://github.com/SymTechVenturesOrg/symtechventures.github.io/pull/11  
**Dedicated branch:** `feature/v2-paper-one-seven-cinematic-optimised-20261120`  
**Scope:** Seven Paper One image slots and the focused article CSS addition; no PR #5 branch changes, merge or deployment.

## Binary verification and outputs

The seven source PNGs were read from binary Git objects at the pinned original image commit `c6f60ee180c2f5d401b0f597f512898c010981a9`, except corrected Figures 2.1 and 3.1, read from the science-correction commit `ef09d41b6b7fcb85efc75618736c234ccc2fa09c`. Each source decoded as **1920 × 1080 RGB**, passed PNG verification, and matched the independently recomputed SHA-256 in the table. A copy at the website’s versioned `approved-20261120/` master path has the same byte length and SHA-256 as its source.

WebP derivatives are generated with Pillow 13.0.0 / libwebp 1.6.0, quality 93, method 6, Lanczos resize. All 21 files decode at their expected 16:9 dimensions. Full individual paths, all 28 source/master/derivative SHA-256 values, sizes and encoder metadata are in [`V2_PHASE_03_P1_SEVEN_IMAGE_WEBP_DERIVATIVE_MANIFEST_20261120.json`](V2_PHASE_03_P1_SEVEN_IMAGE_WEBP_DERIVATIVE_MANIFEST_20261120.json).

| Slot | Source PNG bytes | Source = master SHA-256 | 768 × 432 WebP bytes (saving) | 1280 × 720 WebP bytes (saving) | 1920 × 1080 WebP bytes (saving) |
|---|---:|---|---:|---:|---:|
| Cover | 3,089,586 | `3eeba0f6bfcefd2a63b5867cad0442ac9a6d356526cc1fed31e057d3de9e95a8` | 141,312 (95.43%) | 320,998 (89.61%) | 551,280 (82.16%) |
| Figure 1.1 | 2,972,672 | `4a16ac9219d3fd46be7291b35d033c19508d8be85f4417510e63bc4373718675` | 132,088 (95.56%) | 297,588 (89.99%) | 520,560 (82.49%) |
| Figure 2.1 | 3,088,099 | `a024ee52cccde7b8acc59dce1d816cfce5c894017808d6ede4337f072037cd3b` | 142,166 (95.40%) | 320,660 (89.62%) | 550,274 (82.18%) |
| Figure 3.1 | 3,348,284 | `72bc6b2f086d06678f7a34e3ec980c86016e40ab99724bb4258bd6c0bda72a92` | 155,260 (95.36%) | 359,318 (89.27%) | 632,554 (81.11%) |
| Figure 4.1 | 3,244,273 | `788e68dc507c1e408428380b86816e594301384ed29331a3ab9aa9c29cdb9238` | 144,782 (95.54%) | 330,788 (89.80%) | 578,152 (82.18%) |
| Figure 5.1 | 3,079,962 | `945a5061c67bd52300cc4823f9664579380c85b36363daadcc7ef88496687b1c` | 137,028 (95.55%) | 310,782 (89.91%) | 547,654 (82.22%) |
| Figure 6.1 | 3,073,681 | `a1c9c939c6195a97106a3e4c8a49398a48b27baf108a8ef7b21bdc0ed09e896f` | 132,952 (95.67%) | 306,764 (90.02%) | 543,580 (82.32%) |

Seven PNG masters total **21,896,557 bytes** and remain unchanged. The 21 derivatives total **7,156,540 bytes**. The measured derivative sums are **985,588 bytes at 768w**, **2,246,898 bytes at 1280w**, and **3,924,054 bytes at 1920w**. Relative to all seven source PNGs, those seven-file sets are 95.50%, 89.74% and 82.08% smaller respectively. The 768w and 1920w values are image-file totals; they are **not actual browser transfer measurements**.

The quality metric in the manifest is PSNR for each decoded derivative against the same Lanczos-resized original PNG. At 768w it ranges from 28.33 to 31.83 dB; this is a supplemental comparison and does not establish glyph readability. I visually inspected the seven 768w compositions and 100% source/WebP crops of the Figure 1.1 equations and Figure 2.1 `Λ = 0 special case` label. At Q93, composition, equation layout and that label remain visually intact in those inspections. Fine embedded copy is still too small to promise reliable reading at narrow inline widths; the corresponding selectable HTML explanations and full-resolution PNG links are supplied. A real browser legibility check remains outstanding.

## Mapping, scientific text and accessibility review

The article contains exactly seven semantic `<figure>` slots, each mapped to its intended source/master, three WebP widths, concise descriptive `alt`, visible selectable detailed description, and a labelled link to that exact 1920 × 1080 PNG master. Intrinsic dimensions are 1920 × 1080; `height:auto` is retained, with no crop or `object-fit`. The cover is eager/high priority; the remaining six use lazy loading and asynchronous decoding. Responsive `srcset`/`sizes` paths resolve to the new versioned image directory. The existing seven legacy website WebPs are preserved. The cover Open Graph and Twitter image references now use the matching new 1920w derivative.

Only the three handover-authorised caption changes were applied:

- Figure 1.1 retains its existing caption with the required visible qualification that the equation is the `Λ = 0` special case and that the general form also has a cosmological term. Its accessible description repeats that qualification.
- Figure 2.1 uses the handover’s exact replacement caption describing the unresolved, experimentally unestablished reconciliation challenge. It maps to the corrected Standard Model / `Λ = 0` candidate.
- Figure 5.1 uses the handover’s exact untested-hypothesis wording. Its accessible description states that the four panels are questions and that no emergence law, unified-field derivation or experimental evidence is asserted.

The remaining captions are unchanged. The 3.1 description distinguishes QFT as the framework underlying the Standard Model and identifies dark matter/dark energy as phenomena whose underlying physical nature remains unknown. Figure 4.1 distinguishes dimensional constants from dimensionless α. Figure 6.1 frames the roadmap as planned research and includes revision or rejection for contrary results. Full accessible copy is selectable HTML and does not rely on text embedded in images.

## Browser QA status

**BROWSER_QA_BLOCKED — no responsive browser pass is claimed.** I attempted to test the local article checkout in Chromium at 320px, 390px, tablet and desktop widths. The available CUA browser cannot reach the execution environment’s loopback server (`http://127.0.0.1:8765` returned `net::ERR_CONNECTION_REFUSED`); the native browser’s direct `file://` access is explicitly restricted (“This page is blocked. Your organization doesn’t allow you to view this site”); headless Chromium also exits with `socket() failed: Operation not permitted (1)`. The accessible GitHub raw-file page presents the HTML source as text rather than rendering it. I did not route around those browser restrictions or deploy a preview.

Consequently, none of the following is certified: actual layout at 320px/390px/tablet/desktop; browser-selected `currentSrc`; layout shift; real loaded bytes; keyboard activation; touch activation; broken-image fallback; or zoom/full-resolution interaction. From the implemented sizes and source-set candidates, expected DPR-1 mobile selection is 768w and 1440px/DPR-2 desktop selection is 1920w, but that selection remains an untested expectation. No browser screenshots or screenshot-based legibility results were produced. The owner should keep this draft unapproved until those checks can run in a browser that can serve the PR checkout.

## Change boundary and verification record

- Seven PNG masters: exact copies, 7/7 SHA-256 matches.
- WebP derivatives: 21/21 decode/dimension checks pass; hashes and sizes recorded in the manifest.
- HTML: exactly seven figure/image blocks mapped; only requested image/caption/accessibility integration and cover social-image metadata updated.
- CSS: one targeted figure-description/layout rule block added.
- Legacy WebPs and original source-art paths: unchanged.
- PR #5 branch: not modified. PRs: no merge. Deployment: none.
- Implementation and binary-verification commit on PR #11: `cc2b9e06f34967847b05c0f7024d6128f165bac0`. A separate fresh Git checkout of that exact GitHub branch head passed all 7 master and 21 derivative hash/decode/dimension checks and the 7-slot HTML mapping checks. This QA report is committed in the subsequent documentation commit on the same draft branch.

## Owner handback

The compression implementation and source/master identity checks are ready for review, but the responsive website acceptance gate is blocked pending browser access. Please do not treat the seven-image integration as fully QA-accepted until real 320px, 390px, tablet and desktop browser tests confirm the actual selected assets, rendered text/readability, keyboard/touch access, failures and transferred bytes.
