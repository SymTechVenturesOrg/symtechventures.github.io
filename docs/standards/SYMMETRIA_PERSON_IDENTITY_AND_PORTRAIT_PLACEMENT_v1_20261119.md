# SYMMETRIA — Person Likeness and Scientific-Portrait Placement Standard (v1.0)

**19 November 2026 GMT · Owner-directed Phase 3 amendment**  
**Applies to:** all regenerated Figures in Papers 1–4 and future research-paper illustration production.  
**State:** **Style/identity guidance recorded; new Paper 1 cover proof only, six remaining images NOT accepted.** Nothing is published. Preserve the [16:9 generation standard](SYMMETRIA_ILLUSTRATION_GENERATION_STANDARD_v1_1_20261119.md) and [28-image execution plan](../V2_PHASE_03_28_FIGURE_GENERATION_EXECUTION_WORKPLAN_20261119.md).

## 1. Essential rule — subject leads, people support

1. Images depict the **specific scientific subject of their local HTML section**, not a generic gallery of famous physicists. Do not turn every figure into a three-scientist portrait or a staged group meeting.
2. **Portrait continuity** applies whenever a person appears: Einstein, Dirac and Rowlands must retain the *same recognisable face, apparent age, characteristic hair, glasses where appropriate, attire and colour treatment* between Papers 1 and 3. A consistent visual reference helps but generated faces can still vary: inspect each proof.
3. **Dr Peter Rowlands**: user's supplied reference photo `Rowlands.jpeg` (SHA-256 `e0972721c08b4894b1bf7d8b1b284207def9aee87adf98d8e9c78752df7d1a8a`) is authoritative for project visual direction. Older light-blond/grey hair, thin metal-frame aviator-style glasses, dark suit, light-blue shirt, dark tie, composed expression. **Neaten only stray forehead hair**, do not change identity, age or spectacles. The user photograph is not publicly committed without a rights review.
4. **Albert Einstein**: recognisable older man with wild white hair, heavy moustache, thoughtful expression, mid-century tweed/wool scientific-portrait styling. Maintain consistency with the approved Paper 3 imagery, not a new stylisation each time.
5. **Paul Dirac**: recognisable younger/middle-aged slender man with dark swept or curly hair, modest formal suit and restrained scholarly expression. The chosen generated image style shows a slim moustache; verify likeness against dependable historical references and owner preference before public release, rather than assuming AI rendering is a literal archival portrait.
6. **Never depict an invented real meeting or actual joint experiment between Einstein, Dirac and Rowlands.** If all three appear together, use **explicitly conceptual adjacent portraits** or an art-directed comparison, never an implied photographic event.
7. **No invented equations or claims** merely to fill portrait backgrounds. Names and portraits are not evidence of theoretical equivalence. Distinguish established physics, named published reformulations and proposed SYMMETRIA hypotheses.
8. No oversized SYMMETRIA wordmark, no “Discussion Paper n”, no figure number **inside image pixels**, no text-removal inpainting artefacts. **Entire compositions generated fresh** as the user requested; a cropped/inpainted old figure is not an acceptable new v3 figure.

## 2. Stable identity references and copyright/provenance

- **Rowlands user's reference:** `Rowlands.jpeg`, sha256 above; the source remains in the user's conversation workspace rather than the public repository.
- **Generated Paper 3 identity reference:** `the_nilpotent_foundation_cosmic_foundations.png`, SHA-256 `2eff634723d047990ba1be37be8029033dc611a7f18ac8509342cfc097173b7e`. This is an *artistic* reference, not historical photographic proof.
- **Einstein and Dirac reference:** `a_crisp_cinematic_hyper_detailed_digital_illustr.png` created in the owner's 19 November Chat session, SHA-256 `b2137bae051427591447ed0fc96951a1e50479eb7b0d362e8d11dfc804b679d9`. It depicts stylised likenesses; accuracy requires separate checking.
- **Local identity contact sheet:** `Papers1and3_Scientist_Portrait_Continuity_Reference.jpg`, SHA-256 `52bc1fd5009881f3c37e70e20d86742551e89e32863a3d30ff193bc93c79b64d`, owner review artifact. **Reference only**; do not insert sheet into article or assume the reference automatically makes new generations identical.
- Tool interface: ChatGPT integrated image generation; hidden underlying model build/seed are not guaranteed exposed. Use one canonical portrait reference per person and keep actual output generation ID + reference image SHA + accepted final visual hash in the per-image JSON provenance.
- Public-release rights and likeness review remains pending.

## 3. Paper 1 specific subject/portrait allocations (7 exact slots)

| Slot | Scientific purpose | Allowed portraits | Required composition |
| --- | --- | --- | --- |
| Cover | Established theoretical achievements + unanswered unification problem | **None** | Rich science-first 4-domain illustration. No implied completed quantum gravity |
| Figure 1.1 | Historical progression Newton → Maxwell → Einstein → quantum theory | **Einstein and optionally Dirac** | Portraits SMALL, timeline and principles PRIMARY; no Rowlands |
| Figure 2.1 | Quantum theory vs general relativity | **Einstein and Dirac, optional, small** | Two frameworks and open domain-matching problem PRIMARY; no false blanket incompatibility |
| Figure 3.1 | Current QFT/Standard Model and GR; electroweak versus proposed GUT | **None** | Three established-interaction sectors, gravity separately, proposed unification visibly labelled as unverified |
| Figure 4.1 | Limits: fundamental constants, dark components, quantum gravity, interpretation | **None** | Open questions, not people; avoid claiming unanswered issues invalidate successful theories |
| Figure 5.1 | SYMMETRIA exploratory perspective informed by Rowlands | **Rowlands once, optional supporting portrait** | Nilpotence/symmetry/information as labelled questions; do **not** assert `N²=0 ⇒ AN+NA=0` |
| Figure 6.1 | Roadmap formalise → test consistency → model → predict → experiment | **None** | Forward-looking process, with zero invented empirical data/results |

**Maximum portrait-heavy Paper 1 slots: 3** (Figs 1.1, 2.1, 5.1). The other four must be science-led and portrait-free. The owner may request even fewer. A future image with a person outside the above placements must receive an explicit exception and a clear local scientific justification.

## 4. Attempt rejection and corrective direction, 19 November 2026

During the full Paper 1 regeneration request, the image generator produced one **on-topic, portrait-free cover draft**, plus multiple attempted images which instead depicted an invented group discussion or a broad, unrelated collection of Einstein/Dirac/Rowlands portraits with decorative unverified formulae. **All those group images are REJECTED for topic failure**, not accepted as replacements and not uploaded to the website.

**Current cover candidate:** `p01_cover_illustration_v3_portrait_consistency_rebuild.webp`, WebP SHA-256 `5d3e5d63cf29b66e1223e5044735efb2b796a244336cb3a44d45404e150187f7`; source image-generation ID `fe47d0ad-9095-44a0-8dc1-abbd07643655`; source 1672×941; exported 1920×1080 16:9, sRGB, WebP quality 85. **Visual/technical owner sign-off pending; no HTML changes.**

**Why this matters:** this update is a stop-the-line QC action. An artwork that is visually attractive but depicts an invented meeting or fails to explain the correct section subject **cannot** pass scientific or owner acceptance.

## 5. Acceptance checklist for each regeneration

- Right paper and exact section/caption; no generic scientist montage.
- Scientist appearances match reference set and the user's Rowlands photo; naturally tidy Rowlands hair.
- No portrait where not authorised; no staged historical meetings; no fake quotes or decorative formulae.
- Recreated artwork from scratch using the **same image-generation interface and visual styling**; no masked erasures/inpaint blur.
- 16:9 Full HD 1920×1080 *export*, sRGB, WebP quality 85; note native generator dimensions separately.
- Image title is scientific subject only. No in-artwork series, figure, paper numbers or big wordmarks.
- Exact mathematical symbols checked; speculative claims marked prospective. Caption/alt and source figure slot accurate.
- Owner reviews per image or per seven-figure sheet; **no production source replacement before approval**.

**PR state:** planning PR #2 and implementation PR #5 draft/unmerged; the feature's content was not changed by this guide.
